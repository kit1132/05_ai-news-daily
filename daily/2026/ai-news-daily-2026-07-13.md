# AI News Daily Summary — 2026-07-13

> 本サマリーは 01_ai-news-Master・02_ai-news-Copilot・03_ai-news-industry の3ソース（7/13分）を統合して作成。

月曜。大型モデルローンチはなし。新規で最も重要なのは **VentureBeat Research のエンタープライズAIエージェント調査**——「評価をパスしたエージェントが本番で失敗」「GPU稼働率50%以下が86%」という定量データが、エージェント導入のリスク議論の土台を変える。技術事例では **Bun の Zig→Rust 全面移植を Claude Fable 5 が11日・$165Kで完遂**し、AI支援リファクタリングのROIに具体的な参照値が生まれた。

## 今日のハイライト

### 1. エンタープライズAIエージェントの「評価ギャップ」— 自律度が統制を追い越している（VentureBeat Research）

**事実** VB Transform 2026（7/14-15）に先立ち、VentureBeat Research が従業員100名以上の企業リーダー573名を対象にした5本の調査を公開した。半数の企業が「社内評価をパスしたエージェントが顧客対応で失敗」を経験し、うち4社に1社は複数回。それでも66%が人間レビューなしの本番投入を許可済みまたは今後12カ月で予定している。

**根拠** 3つの数字が構造問題を裏づける。(1) GPU稼働率50%以下が自社GPU運用企業の86%——過剰投資の兆候。(2) 27%がエージェントのコストを「請求書が来て初めて知る」リアクティブ統制のみ。(3) API鍵の共有でエージェント群が露出している企業が69%。いずれも2026年6月実施の自社調査で、引用可能な一次データ。

**影響** エージェント導入の議論が「モデル選定」から「評価・ガードレール・コスト上限の設計」に重心移動する根拠が揃った。提案書やリスク評価で「直近573名調査」として数字を使える。GPU稼働率のデータはクラウド従量 vs 自社GPUのTCO比較の切り口にもなる。

**行動指針** エージェント導入を検討中なら、モデル選定より先に「評価基準・人間レビュー境界・エージェント単位のコスト上限」の3点を設計する。既に本番投入済みなら、API鍵の共有状況と稼働率を棚卸しする。

- https://venturebeat.com/orchestration/enterprise-ai-is-entering-an-evaluation-gap-agents-are-gaining-autonomy-faster-than-companies-can-verify-them
- https://venturebeat.com/orchestration/wall-street-is-debating-the-ai-buildout-enterprises-just-answered-86-say-their-gpus-run-at-half-capacity-or-less

### 2. Bun の Zig→Rust 全面移植を Claude Fable 5 が11日・$165Kで完遂 — AI支援リファクタリングのROI参照値

**事実** JavaScriptランタイム Bun が約53.5万行のZigコードを Claude Fable 5 で11日間（純コーディング約6日）でRustに全面移植した。Claudeを最大64インスタンス並走させ、「実装役と検証役の分離」で品質を担保。作者はAIなしなら「エンジニア3名×約1年」と試算。

**根拠** API換算コスト約$165,000（非キャッシュ入力59億トークン、出力6.9億トークン、キャッシュ読み72億トークン）。移植後の成果はメモリ 6.7GB→609MB（91%削減）、性能+2〜5%、バイナリ約20%縮小。Publickey（7/10）・GIGAZINE（7/12）が報道、Zig作者も反応。

**影響** 「人月換算3人年→11日・$165K」という数字は、レガシー言語移行やモダナイゼーション案件の投資対効果の当たりをつける参照値になる。並列エージェント運用（実装役と検証役の分離）という設計パターンは他の大規模リファクタリングにも再利用可能。

**行動指針** 大規模な言語移行・リファクタリングを検討中なら、まず対象コードベースの行数と構造的複雑さを洗い出し、Bunのケース（53.5万行・型付き言語間移行）との比較で見積もりの妥当性を検証する。ただしBunのケースは言語仕様の近さ（Zig→Rust）と作者自身の深いドメイン知識が前提であり、動的言語からの移行やドメイン知識が薄い場合は割り引いて考える必要がある。

- https://www.publickey1.jp/blog/26/javascriptbunclaude_fable_511zigrustclaude.html
- https://gigazine.net/news/20260712-bun-zig-rust/

### 3. Claude Code 週次上限+50%プロモが本日期限 — 利用パターンの見直しタイミング

**事実** 5月から継続していた Claude Code の週次利用上限+50%プロモーションが本日 7/13 で期限を迎える。延長発表は未確認。昨日終了した Fable 5 無償提供と合わせ、Anthropic の利用条件が2日連続で引き締め方向に動いている。

**根拠** 02_ai-news-Copilot が一次確認。Anthropic 公式の延長アナウンスは本日時点で未検出。

**影響** Claude Code を業務の中心に据えているユーザーにとって、利用量が実質33%減となる可能性がある（+50%の解除）。Fable 5 の課金体系変更と重なるため、今週のコスト変動に注意が必要。

**行動指針** 今日以降の利用量推移を数日モニタリングし、上限に当たるようなら Opus 4.8 / Sonnet 5 の使い分け比率を調整する。延長発表が出る可能性もあるため、Anthropic の公式チャネルを1週間ウォッチする。

## カテゴリ別まとめ

### 開発ツール

- **Claude Code v2.1.207（7/11）**: 据え置き。週次上限+50%プロモが本日期限 — [CHANGELOG](https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md)
- **GitHub Copilot CLI v1.0.70（7/9・回収）**: GPT-5.6モデル対応、`--sandbox` / `--no-sandbox` フラグ、`/refine` 新設、信頼済みリポジトリ設定を追加。pre-release v1.0.71-0（7/10）は据え置き — [copilot-cli changelog](https://github.com/github/copilot-cli/blob/main/changelog.md)
- **Cursor 3.11（7/10）/ Codex CLI alpha 0.145.0-alpha.4（7/11）**: いずれも据え置き

### Anthropic

- Fable 5 有料プラン無償提供は昨日 7/12 で終了済み。週次利用上限にカウントされず、利用クレジット経由での提供に移行 — [Redeploying Fable 5](https://www.anthropic.com/news/redeploying-fable-5)
- Claude Code 週次上限+50%プロモが本日期限（ハイライト3参照）

### OpenAI / ChatGPT

- GPT-5.6 GA（7/9）後の新規なし。Team 全面展開は 7/14 予定

### SpaceXAI / Grok

- Grok 4.5 一般公開（7/8〜7/9）以降の新規なし。EU 提供は7月中旬めど

### Google / DeepMind

- Gemini 3.5 Pro は限定 preview 継続。GA は 7/17 目標（未確定）。公式モデルカード・料金は未公表

### Apple

- OpenAI を営業秘密窃取で提訴（7/10提訴、続報なし）。iOS 27 Public Beta は 7/14 頃の予定で変更なし — [CNBC](https://www.cnbc.com/2026/07/10/apple-openai-lawsuit-trade-secrets.html) / [TechCrunch](https://techcrunch.com/2026/07/10/apple-sues-openai-over-alleged-trade-secret-theft/)

### Microsoft Copilot / Power Platform

- 一次情報の動きなし。Released Versions は Build 2026.6.3（6/30）のまま。M365 Copilot Release Notes は July 01 バッチが最新。**次回火曜 7/14 が要監視**（版ページ更新・2026.7.x 反映見込み）
- 新 M365 Copilot アプリ UI（MC1325422）の opt-out トグルが 7/15 で終了、以降デフォルト化

### OSS・ローカルLLM

- **Colibrì（Pure C・依存ゼロ）**: 744BパラメータのMoEモデル GLM-5.2 を約25GBのコンシューマ機で実行。速度は0.05〜1 tok/sで常用不可だが、API契約前の大型OSSモデル検証手段として意味がある — [GitHub](https://github.com/JustVugg/colibri) / [GIGAZINE](https://gigazine.net/gsc_news/en/20260710-colibri-glm)

### エンタープライズ・調査

- VentureBeat Research エンタープライズAIエージェント調査シリーズ（ハイライト1参照）

## 直近の注目予定

- **7/14** GPT-5.6 Team 全面展開 / 破壊的変更: Visio → Power Automate エクスポート廃止発効 / Copilot Studio 版ページ次更新見込み / iOS 27 Public Beta 公開予定 / VB Transform 2026 開幕（〜7/15）
- **7/15** Claude Science（AI for Science）応募締切 / 新 M365 Copilot アプリ UI opt-out トグル終了
- **7月中旬** Grok 4.5 EU 提供予定 / ChatGPT Work が Plus・Business へ拡大予定
- **7/17** Claude Corps 第1期応募締切 / Gemini 3.5 Pro GA 候補日（未確定）
- **7/21** Copilot Cowork GA 告知イベント
- **7/23** OpenAI computer-use-preview シャットダウン
- **7/31** Devin classic 環境設定の read-only 参照終了
- **8/1** covered frontier model 60日 EO 期限
- **8/3** 旧「Claude in Slack」退役
- **8/5** Opus 4.1 Claude API 退役 / Cowork 倍増利用枠の終了
- **8/26** OpenAI Assistants API 廃止 / o3 退役 / GPT-4.5 完全廃止
- **8/31** Sonnet 5 促進価格終了（$2/$10 → $3/$15）
- **9月** iOS 27 / macOS 27 GA（AFM 3 本番）

## 改善メモ

- 新規提案・障害の変化なし（継続分は IMPROVEMENT-BACKLOG.md 参照）
- 02_ai-news-Copilot: RSS/WebFetch 全ソース 403 継続、取得方法の WebSearch 優先化提案（B-004）が継続
