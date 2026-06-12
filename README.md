# 05_ai-news-daily — AIニュース日次サマリー

3つのソースリポジトリ（[01_ai-news-Master](https://github.com/kit1132/01_ai-news-Master) / [02_ai-news-Copilot](https://github.com/kit1132/02_ai-news-Copilot) / [03_ai-news-industry](https://github.com/kit1132/03_ai-news-industry)）の当日ダイジェストを統合し、毎朝 07:00 JST に claude.ai リモートルーチンが日次サマリーを生成して main に push するリポジトリ。

- 出力: `daily/YYYY/ai-news-daily-YYYY-MM-DD.md`
- 生成手順の正本: `.claude/commands/daily-summary.md`
- ビューア: GitHub Pages（`index.html` + `files.json`）
- 週次集約は [04_ai-news-weekly](https://github.com/kit1132/04_ai-news-weekly) が担当

`daily/2026/` の 2026-04-05〜2026-06-12 分は、ローカル（Cowork / ルーチン）時代に生成した2ソース版アーカイブ。3ソース統合版は 2026-06-13 以降。
