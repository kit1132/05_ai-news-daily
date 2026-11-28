"""更新タグ検査の回帰。

2026-10-19 の修正は本番スクリプトだけだった。規約どおりの
「（ハイライトN参照）」を、番号の無い「ハイライト参照」だけに戻すと、
番号付きの参照行が不合格になる。料金+破壊的変更の例外、
2026-09-24 より前を見ないこと、commit フックの終了コード 2 もここで固定する。

合格表示が標準出力か標準エラーかは見ない。01 とこのリポジトリの検査は
まだ標準出力で、02 と 03 は標準エラーへ移している。
"""

from __future__ import annotations

import importlib.util
import io
import json
import tempfile
import unittest
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "check_update_tags",
    ROOT / "scripts" / "check-update-tags.py",
)
mod = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(mod)

SHIPPED = ROOT / "daily/2026/ai-news-daily-2026-11-28.md"
BEFORE_ROLLOUT = ROOT / "daily/2026/ai-news-daily-2026-09-23.md"


def digest(*sections: str) -> str:
    return "\n".join(sections) + "\n"


class TagErrorTest(unittest.TestCase):
    def test_single_and_ordered_compound_tags(self):
        self.assertIsNone(mod.tag_error("新機能"))
        self.assertIsNone(mod.tag_error("破壊的変更+新機能"))
        self.assertIsNone(mod.tag_error("据え置き"))

    def test_price_may_lead_breaking_change(self):
        self.assertIsNone(mod.tag_error("料金+破壊的変更"))

    def test_secondary_must_rank_below_primary(self):
        self.assertEqual(mod.tag_error("新機能+料金"), "副は主より優先順が下")
        self.assertEqual(mod.tag_error("新機能+新機能"), "副は主より優先順が下")
        self.assertEqual(mod.tag_error("予定+破壊的変更"), "副は主より優先順が下")

    def test_shape_and_vocabulary(self):
        self.assertEqual(mod.tag_error("料金+新機能+仕様"), "主は1語、副は1語まで")
        self.assertEqual(mod.tag_error("速報"), "11語以外")
        self.assertEqual(mod.tag_error("料金+"), "11語以外")


class CheckTextTest(unittest.TestCase):
    def test_numbered_highlight_references_are_not_items(self):
        text = "\n".join(
            [
                "## 開発ツール",
                "- [不明] （ハイライト1参照）",
                "- [不明] （ハイライト１参照）",
                "- [不明] ハイライト参照",
                "- [不明] （ハイライト 12 参照）",
                "- [不明] ハイライトの話",
            ]
        )
        self.assertEqual(mod.check_text(text, "digest"), ["6: [不明] 11語以外"])

    def test_daily_shape_used_by_shipped_summaries(self):
        text = digest(
            "## 今日のハイライト",
            "",
            "### 1. [破壊的変更+新機能] 既定の経路が変わる — 設定を直すまで起動できない",
            "### 2. [新機能] 新しい操作が増えた — 既存の手順はそのまま使える",
            "",
            "## カテゴリ別まとめ",
            "",
            "### 開発ツール",
            "- [据え置き] **一次情報** — 新しい記事は無い",
            "- （ハイライト1参照）",
            "- https://example.com/only",
            "",
            "## 直近の注目予定",
            "- タグの無い期限",
            "",
            "## 改善メモ",
            "- タグの無いメモ",
        )
        self.assertEqual(mod.check_text(text, "daily"), [])

    def test_daily_category_requires_bold_heading(self):
        text = digest(
            "## 今日のハイライト",
            "### 1. [新機能] 題 — 含意",
            "",
            "## カテゴリ別まとめ",
            "- [新機能] 太字が無い — 本文",
        )
        self.assertEqual(
            mod.check_text(text, "daily"),
            ["5: カテゴリ行は「- [タグ] **見出し** — 本文」"],
        )

    def test_digest_accepts_the_line_daily_rejects(self):
        text = digest("## 開発ツール", "- [新機能] 太字が無い — 本文")
        self.assertEqual(mod.check_text(text, "digest"), [])

    def test_daily_ignores_sections_outside_highlight_and_category(self):
        text = digest("## 開発ツール", "- タグが無い")
        self.assertEqual(mod.check_text(text, "daily"), [])
        self.assertNotEqual(mod.check_text(text, "digest"), [])

    def test_highlight_shape_and_reversed_compound(self):
        text = digest(
            "## 今日のハイライト",
            "### 1. タグが無い題 — 含意",
            "### 2. [新機能+料金] 順序が逆 — 副が主より上",
        )
        self.assertEqual(
            mod.check_text(text, "daily"),
            [
                "2: ハイライトは「### N. [タグ] タイトル — 含意」",
                "3: [新機能+料金] 副は主より優先順が下",
            ],
        )

    def test_excluded_heading_prefixes_and_non_items(self):
        text = digest(
            "## 今後の期限（記録済み・日付順）",
            "- タグが無い期限",
            "## 採録を見送った案件",
            "- タグが無い見送り",
            "## 開発ツール",
            "- https://example.com/a",
            "- 直近の期限: 11月16日",
            "- [観測] 見出し — 本文",
        )
        self.assertEqual(mod.check_text(text, "digest"), [])


class CheckFileTest(unittest.TestCase):
    def test_shipped_summary_still_passes(self):
        self.assertTrue(SHIPPED.is_file())
        self.assertEqual(mod.check_file(SHIPPED), [])

    def test_history_before_rollout_is_skipped_even_when_the_text_fails(self):
        self.assertTrue(BEFORE_ROLLOUT.is_file())
        self.assertGreater(
            len(mod.check_text(BEFORE_ROLLOUT.read_text(encoding="utf-8"), "daily")),
            0,
        )
        self.assertEqual(mod.check_file(BEFORE_ROLLOUT), [])

    def test_rollout_boundary_is_the_filename_date(self):
        body = "## カテゴリ別まとめ\n- タグが無い\n"
        with tempfile.TemporaryDirectory() as tmp:
            before = Path(tmp) / "ai-news-daily-2026-09-23.md"
            first = Path(tmp) / "ai-news-daily-2026-09-24.md"
            before.write_text(body, encoding="utf-8")
            first.write_text(body, encoding="utf-8")
            self.assertEqual(mod.check_file(before), [])
            errors = mod.check_file(first)
        self.assertEqual(
            errors,
            ["2: カテゴリ行は「- [タグ] **見出し** — 本文」"],
        )

    def test_missing_file_follows_the_rollout_date(self):
        covered = Path("daily/ai-news-daily-2026-11-28.md")
        early = Path("daily/ai-news-daily-2026-09-23.md")
        self.assertEqual(mod.check_file(covered), [f"ファイルが無い: {covered}"])
        self.assertEqual(mod.check_file(early), [])


class HookTargetTest(unittest.TestCase):
    def test_commit_uses_the_index_and_drops_non_news(self):
        with mock.patch.object(
            mod,
            "git_lines",
            return_value=[
                "daily/2026/ai-news-daily-2026-11-28.md",
                "README.md",
            ],
        ) as git:
            got = mod.hook_targets("git commit -m 'daily'")
        git.assert_called_once_with(["diff", "--cached", "--name-only"])
        self.assertEqual(got, [Path("daily/2026/ai-news-daily-2026-11-28.md")])

    def test_commit_all_uses_worktree_status_and_rename_destination(self):
        porcelain = [
            " M daily/2026/ai-news-daily-2026-11-28.md",
            "R  old.md -> daily/2026/ai-news-daily-2026-11-27.md",
            "?? notes.txt",
        ]
        with mock.patch.object(mod, "git_lines", return_value=porcelain) as git:
            got = mod.hook_targets("git commit -a -m 'daily'")
        git.assert_called_once_with(["status", "--porcelain"])
        self.assertEqual(
            got,
            [
                Path("daily/2026/ai-news-daily-2026-11-28.md"),
                Path("daily/2026/ai-news-daily-2026-11-27.md"),
            ],
        )

    def test_push_falls_back_when_the_main_diff_is_empty(self):
        def fake(args):
            if "origin/main...HEAD" in args:
                return []
            return ["daily/2026/ai-news-daily-2026-11-28.md", "CLAUDE.md"]

        with mock.patch.object(mod, "git_lines", side_effect=fake) as git:
            got = mod.hook_targets("git push origin HEAD")
        self.assertEqual(
            git.call_args_list[0].args[0],
            ["diff", "--name-only", "origin/main...HEAD"],
        )
        self.assertEqual(
            git.call_args_list[1].args[0],
            ["diff", "--name-only", "HEAD~1", "HEAD"],
        )
        self.assertEqual(got, [Path("daily/2026/ai-news-daily-2026-11-28.md")])

    def test_zero_since_falls_back_to_the_last_commit(self):
        with mock.patch.object(
            mod,
            "git_lines",
            return_value=["daily/2026/ai-news-daily-2026-11-28.md", "README.md"],
        ) as git:
            got = mod.ci_targets("0" * 40)
        git.assert_called_once_with(["diff", "--name-only", "HEAD~1", "HEAD"])
        self.assertEqual(got, [Path("daily/2026/ai-news-daily-2026-11-28.md")])


class RunHookTest(unittest.TestCase):
    def invoke(self, payload, targets):
        stdout, stderr = io.StringIO(), io.StringIO()
        raw = payload if isinstance(payload, str) else json.dumps(payload)
        with (
            mock.patch.object(mod, "hook_targets", return_value=targets),
            mock.patch("sys.stdin", io.StringIO(raw)),
            mock.patch("sys.stdout", stdout),
            mock.patch("sys.stderr", stderr),
        ):
            code = mod.run_hook()
        return code, stdout.getvalue(), stderr.getvalue()

    def test_ignores_empty_invalid_and_non_git_input(self):
        self.assertEqual(self.invoke("", [])[0], 0)
        self.assertEqual(self.invoke("{", [])[0], 0)
        code, _, _ = self.invoke(
            {"tool_input": {"command": "python3 scripts/check-update-tags.py"}},
            [],
        )
        self.assertEqual(code, 0)
        code, _, _ = self.invoke({"tool_input": {"command": 1}}, [])
        self.assertEqual(code, 0)

    def test_passing_news_file_does_not_block_the_commit(self):
        code, _, stderr = self.invoke(
            {"tool_input": {"command": "git commit -m 'daily'"}},
            [SHIPPED],
        )
        self.assertEqual(code, 0)
        self.assertNotIn("不一致のまま", stderr)

    def test_failing_news_file_blocks_the_commit(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "ai-news-daily-2026-11-28.md"
            path.write_text(
                "## カテゴリ別まとめ\n- タグが無い\n",
                encoding="utf-8",
            )
            code, _, stderr = self.invoke(
                {"tool_input": {"command": "git commit -m 'daily'"}},
                [path],
            )
        self.assertEqual(code, 2)
        self.assertIn("更新タグの検査が不合格", stderr)
        self.assertIn("カテゴリ行は「- [タグ] **見出し** — 本文」", stderr)
        self.assertIn("不一致のままコミット・push しない", stderr)

    def test_main_return_codes(self):
        with (
            mock.patch("sys.stdout", io.StringIO()),
            mock.patch("sys.stderr", io.StringIO()),
        ):
            self.assertEqual(mod.main([]), 1)
            self.assertEqual(mod.main([str(SHIPPED)]), 0)


if __name__ == "__main__":
    unittest.main()
