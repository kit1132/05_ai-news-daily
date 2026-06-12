# AI News Daily Summary

## 基本方針

- 出力は日本語
- 簡潔で実用的な情報を好む。冗長な説明は不要。定量的な根拠を重視
- kit1132/01_ai-news-Master, 02_ai-news-Copilot, 03_ai-news-industry の**当日分**ダイジェストを統合した日次サマリー（週次集約は kit1132/04_ai-news-weekly が担当）

## プロジェクト構成

- `daily/YYYY/ai-news-daily-YYYY-MM-DD.md` — 日次サマリー本体
- `.claude/commands/daily-summary.md` — **生成手順の正本**（ルーチンはこのファイルに従う）
- `index.html` — ダイジェストの HTML ビューア（marked.js 使用、GitHub Pages で公開）
- `files.json` — ビューアが参照するファイル一覧（新しい順、パスはルートからの相対）
- `.nojekyll` — GitHub Pages の Jekyll 処理を無効化

## 実行環境

- claude.ai リモートルーチン（Routines）で毎朝 07:00 JST（cron `0 22 * * *` UTC）に自動実行
- **ブランチ運用**: `main` へ直接 commit & push する。feature ブランチ・PR は作らない
- **日付**: JST（Asia/Tokyo, UTC+9）で判定する。`TZ=Asia/Tokyo date +%Y-%m-%d` で当日日付を取得

## 不変条件

- 入力3リポ（01_ai-news-Master / 02_ai-news-Copilot / 03_ai-news-industry）へは一切書き込まない
- main 以外のブランチへ push しない
- 既存の当日ファイルがあれば上書きせずスキップ通知のみ
