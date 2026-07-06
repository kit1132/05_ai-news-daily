# daily-summary — AIニュース日次サマリー生成

## 目的

kit1132 の3つのソースリポジトリの当日ダイジェストを統合し、日次サマリー Markdown を生成して main に直接 push する。

## 前提

- タイムゾーンは JST（Asia/Tokyo）。当日日付 `<DATE>` は `TZ=Asia/Tokyo date +%Y-%m-%d` で取得する（`<YYYY>` = 年4桁、`<MM>` = 月2桁）
- 作業ブランチは必ず `main`。feature ブランチ・PR は作らない
- 入力リポジトリへは一切書き込まない（読み取り専用）

## 入力（読み取り専用・3リポ）

| リポ | パス | 更新時刻（JST目安） |
|---|---|---|
| `kit1132/01_ai-news-Master` | `digests/<YYYY>/<MM>/ai-news-<DATE>.md` | 前日 19:10 頃 |
| `kit1132/03_ai-news-industry` | `digests/<YYYY>/<MM>/ai-news-<DATE>.md` | 前日 20:05 頃 |
| `kit1132/02_ai-news-Copilot` | `digests/<YYYY>/<MM>/ai-news-<DATE>.md` | 前日 21:05 頃 |

※ `<DATE>` 付きダイジェストは前日の夜にコミットされる（例: 7/6 分は 7/5 19〜21時台）。当日 07:00 の実行時点で当日分が無い場合、そのソースの前夜の実行が失敗している。

## 手順

1. ブランチを main に揃える:
   ```
   git fetch origin main
   git checkout main
   git pull origin main
   ```
2. 出力先 `daily/<YYYY>/ai-news-daily-<DATE>.md` が既に存在する場合は、何も変更せず「本日分は生成済み」と通知して終了する（後述の欠損リカバリは実施してよい）
3. **欠損リカバリ**: 前日のサマリー `daily/<YYYY>/ai-news-daily-<前日DATE>.md` の冒頭注記に欠損ソースが記録されている場合、そのソースの前日分ダイジェストが現在は取得できるか確認する
   - 取得できる場合: 前日のサマリーを全ソースで再生成して**上書きする**（欠損リカバリに限り上書きを許可）。冒頭注記を「Nソース統合」に更新し、`Regenerate AI news daily summary for <前日DATE> (missing source recovered)` として当日分とは別にコミットする
   - 取得できない場合: 当日サマリーの改善メモに「<リポ名> の <前日DATE> 分は依然欠損（ソース側ルーチンの実行失敗の可能性、要確認）」と記録する
4. 3ソースの当日ダイジェストを読み取る。取得できないソースは「欠損」として記録する
   - **3ソース全欠損**: 生成を中止し、その旨を通知して終了
   - **一部欠損**: 取得できたソースのみで生成し、冒頭の注記に欠損ソースを明記
5. 下記フォーマットに従い日次サマリーを生成し、`daily/<YYYY>/ai-news-daily-<DATE>.md` に保存する
6. `files.json` の配列先頭に新ファイルのパス（例: `daily/2026/ai-news-daily-2026-06-13.md`）を追加する
7. コミット & プッシュ:
   ```
   git add daily/ files.json
   git commit -m "Add AI news daily summary for <DATE>"
   git push origin main
   ```
8. push 後、`git log origin/main -1` で main に反映されたことを確認する

## 出力フォーマット（日本語）

```
# AI News Daily Summary — <DATE>

> 本サマリーは 01_ai-news-Master・02_ai-news-Copilot・03_ai-news-industry の3ソース（M/D分）を統合して作成。
（欠損があれば「※ <リポ名> は当日分が未取得のため N ソースで作成」と追記）

## 今日のハイライト

最重要ニュース3件。各件は `### N. タイトル — 一言の含意` の見出しに続けて
**事実** / **根拠** / **影響** / **行動指針** の4段落で構成し、末尾に出典URLを箇条書きで付ける。

## カテゴリ別まとめ

ハイライト以外のニュースをカテゴリごとに箇条書きでまとめる。
カテゴリは当日のニュース内容に応じて柔軟に設定する
（例: Anthropic / Claude、OpenAI、Google / DeepMind、Microsoft / GitHub、
Copilot Studio / Power Platform、Cursor / 開発ツール、規制・政策、その他）。
重要項目には出典URLを付け、ハイライトで詳述済みの項目は「（ハイライト参照）」と書く。

## 直近の注目予定

今後の確定日付イベント（GA日、モデル退役日、カンファレンス等）を日付順の箇条書きで。

## 改善メモ

3ソースのダイジェストに含まれる改善メモ（取得失敗したソース、追加候補ソース等）を
引き継いでまとめる。ソース間の重複・矛盾に気づいた場合もここに記録する。
```

### 統合の方針

- 複数ソースで重複するニュースは1つに統合し、情報量の多い方をベースにする
- 矛盾する記述があれば両論併記し、改善メモに記録する
- URL は原文のまま記載する

## 不変条件

- 入力3リポの `digests/` 配下を一切変更しない
- main 以外のブランチへ push しない
- 既存の当日ファイルを上書きしない（手順3の欠損リカバリによる前日分の再生成のみ例外）
