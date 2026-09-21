# AI News Daily Summary

## 基本方針

- 出力は日本語
- 簡潔で実用的な情報を好む。冗長な説明は不要。定量的な根拠を重視
- kit1132/01_ai-news-Master, 02_ai-news-Copilot, 03_ai-news-industry の**当日分**ダイジェストを統合した日次サマリー（週次集約は kit1132/04_ai-news-weekly が担当）

## プロジェクト構成

- `daily/YYYY/ai-news-daily-YYYY-MM-DD.md` — 日次サマリー本体
- `.claude/commands/daily-summary.md` — **生成手順の正本**（ルーチンはこのファイルに従う）
- `index.html` — 統合ビューア（https://kit1132.github.io/01_ai-news-Master/ ）へのリダイレクト。実体は 01_ai-news-Master/index.html にある。**このファイルは編集不要**
- `files.json` — ビューアが参照するファイル一覧（新しい順、パスはルートからの相対）
- `.nojekyll` — GitHub Pages の Jekyll 処理を無効化

## 実行環境

- claude.ai リモートルーチン（Routines）で毎朝 07:00 JST（cron `0 22 * * *` UTC）に自動実行
- **ブランチ運用**: `main` へ直接 commit & push する。feature ブランチ・PR は作らない
- **日付**: JST（Asia/Tokyo, UTC+9）で判定する。`TZ=Asia/Tokyo date +%Y-%m-%d` で当日日付を取得
- **入力取得**: 3ソースは必ず `raw.githubusercontent.com` から読む（GitHub MCP 禁止）。手順の正本は `daily-summary.md`「入力の取得経路」
- **セーフティネット**: ローカル `ai-news-digest-safety-net`（毎朝 ~8:30 JST）が当日分未生成なら raw 経由でバックフィルする

## 不変条件

- 入力3リポ（01_ai-news-Master / 02_ai-news-Copilot / 03_ai-news-industry）へは一切書き込まない
- 入力3リポを GitHub MCP 経由で読まない（スコープ欠落で空振りする）
- main 以外のブランチへ push しない
- 既存の当日ファイルがあれば上書きせずスキップ通知のみ（daily-summary.md 手順3の欠損リカバリによる前日分再生成のみ例外）
