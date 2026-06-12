# AI News Daily Summary — 2026-06-12

> 本サマリーは 01_ai-news-Master・03_ai-news-industry の2ソース（6/12分）を統合して作成。

## 今日のハイライト

### 1. Microsoft が社内従業員の Fable 5 利用を禁止 — 自社製品で売りながら自社で使えない構造的矛盾

**事実**: Anthropic の Fable 5 は安全分類器運用のためプロンプト/出力を default 30 日間保持する（policy 違反 flag 時は最大 2 年）。Microsoft 法務がこの retention 条件を承認できず、社内版 GitHub Copilot の model picker から Fable 5 を除外した。一方、GitHub Copilot / Microsoft Foundry の外部顧客向けには 6/9 同日 GA で提供継続中。Opus 4.x / Sonnet 4.x は Zero Data Retention（ZDR）規約下にあり、社内利用は継続許可。

**根拠**: 「自社製品で即日 GA 提供、自社従業員には禁止」という二重基準が成立した事実そのものが、Fable 5 の 30 日 retention が enterprise セキュリティ審査において構造的障壁であることを証明している。Microsoft 法務すら通過できない条件を、他社の CISO が通す理由はない。

**影響**: Fable 5 導入を検討中の企業は「性能が上がっても retention policy が通らなければ使えない」という制約に直面する。GitHub Copilot で Fable 5 を有効化するには管理者が明示的に enable する必要があり、その判断は今回の Microsoft 法務の判断と同じ論点を通過しなければならない。結果として、多くの企業で Fable 5 は「API 経由の ZDR 契約が成立するまで Opus 4.8 で代替」という選択になる可能性が高い。

**行動指針**: Fable 5 を enterprise 環境で使いたい場合は、まず自社の情報セキュリティ部門に 30 日 retention の可否を確認する。ZDR が必須なら Opus 4.8 / Sonnet 4.6 で運用を継続し、Anthropic が Fable 5 向け ZDR オプションを提供するかを追跡する。6/22 までの試食期間は個人検証に限定し、enterprise 本番投入は retention 問題の決着を待つ。

- https://cryptobriefing.com/microsoft-restricts-claude-fable-5-data-retention/
- https://analyticsindiamag.com/ai-news/microsoft-restricts-internal-use-of-anthropics-claude-fable-5-over-data-retention-concerns
- https://www.technobezz.com/news/microsoft-blocks-employees-from-using-anthropics-claude-fable-5-over-data-retention-risks

### 2. 本日 6/12 が OpenAI macOS アプリ旧証明書失効期限 — ChatGPT Desktop / Codex App / Codex CLI / Atlas が動作停止

**事実**: 5/11 の TanStack supply chain attack（Mini Shai-Hulud キャンペーン）で OpenAI 社員 2 端末が侵害され、Windows / macOS / iOS / Android 用署名鍵すべてが影響を受けた。全アプリは新証明書で再署名・再リリース済みだが、旧証明書での起動は本日 6/12 以降 macOS 標準保護機能によりブロックされる。

**根拠**: AI 開発ツールの署名鍵が supply chain attack で無効化され、OS レベルでの強制更新が発生するのは初の大規模事例。同期間に Snowflake・GitHub・Microsoft も独自の再署名キャンペーンを実施しており、AI ツールチェーン全体が OS 級メンテナンスサイクルに組み込まれ始めている。

**影響**: 旧バージョンのまま放置した macOS ユーザーは本日以降、ChatGPT Desktop・Codex App・Codex CLI・Atlas が起動しなくなる。顧客データや本番システムへの侵害は確認されていないが、限定的な credential material の流出は確認済み。

**行動指針**: macOS で OpenAI 製アプリを使っている場合、本日中に最新版へアップデートする。すでに更新済みなら対応不要。

- https://openai.com/index/our-response-to-the-tanstack-npm-supply-chain-attack/
- https://thehackernews.com/2026/04/openai-revokes-macos-app-certificate.html

### 3. Apple Foundation Models の全容判明 — AFM 3 は 5 モデル構成、Cloud Pro は Nvidia GPU on Google Cloud で稼働

**事実**: Apple ML Research ブログ（6/10-11）で AFM 3 ファミリーの詳細が公開された。on-device 2 種（AFM 3 Core / AFM 3 Core Advanced）+ Private Cloud Compute 3 種の計 5 モデル。AFM 3 Core Advanced は 20B パラメータの sparse architecture で、リクエストごとに 1-4B のみ activate する設計。AFM 3 Cloud Pro は Nvidia GPU に最適化され、Google Cloud 上の Nvidia インフラで動作する（Apple × Google × Nvidia 3 社共同）。訓練には Google 貸与の Gemini からの distillation を使用するが、推論時には Gemini モデルも Google コードも使用しない。

**根拠**: WWDC keynote 時点では「Siri = Gemini 1.2T カスタム」と単純化されていたが、実態は「Gemini は distillation の教師」「Google Cloud は Nvidia GPU の場所貸し」「推論は完全に Apple 独自」という 3 層構造。Apple が単一顧客として Google Cloud 上に Nvidia 専用クラスタを長期借り上げる構図は、Google Cloud の AI infrastructure ビジネスにとって数億ドル級の契約。

**影響**: Apple エコシステムの AI バックエンドが「Apple 自前モデル + Google インフラ + Nvidia GPU」という三位一体構造であることが確定した。Gemini への推論依存がないため、Apple は Google との関係が変化しても推論パイプラインを維持できる。iOS/macOS 開発者にとっては、9 月の iOS 27 GA で AFM 3 ファミリーが本番投入される際の性能特性（on-device は sparse で低レイテンシ、Cloud Pro はフロンティア級品質）の見通しが立った。

**行動指針**: iOS/macOS 開発者は WWDC セッション動画（本日 Day 5 最終日）で Foundation Models Framework の詳細を確認する。サーバーサイドでの Apple AI 活用を検討している場合は、Private Cloud Compute の利用条件（Small Business Program 参加要件など）を整理しておく。経過観察。

- https://machinelearning.apple.com/research/introducing-third-generation-of-apple-foundation-models
- https://appleinsider.com/articles/26/06/08/apples-new-foundation-models-dont-contain-a-drop-of-gemini-as-we-said-they-wouldnt

---

## カテゴリ別まとめ

### Claude / Anthropic

- **Claude Code v2.1.172（6/10）**: sub-agents の 5 段ネスト spawn 解禁。各 sub-agent が独立 window で実行され summary のみ返却する設計。Amazon Bedrock が `~/.aws` config から region 自動読込、バグ修正 20 件以上。v2.1.173（6/11）で Fable 5 model 名の `[1m]` suffix 自動正規化を追加。Fable 5 GA から 3 日連続 stable release。
  - https://code.claude.com/docs/en/changelog
- **Claude Managed Agents が cron + vault を public beta 化**: 自前 scheduler なしで cron スケジュール実行が可能に。vault 環境変数で secret の安全注入を標準化。同時に 20+ legal MCP connectors と 12 practice-area plugins を公開。
  - https://claude.com/blog/whats-new-in-claude-managed-agents
  - https://platform.claude.com/docs/en/managed-agents/overview
- **Fable 5 安全策の議論継続**: Fortune「secret sabotage」、The Register「hello で refuse」等の報道。安全分類器の Opus 4.8 フォールバック動作（<5% session）が批判の対象。
- **Code with Claude Tokyo Extended（6/11）終了**: 録画は 6/12 以降に claude.com/blog で公開予定。
- **6/15 に Sonnet 4 / Opus 4 API 退役まで 3 日**。Opus 4.6/4.7/4.8 + Fable 5 への migration ピーク。

### OpenAI

- **macOS cert revoke 期限が本日**（ハイライト参照）
- **OpenAI S-1 非公開提出（6/8）**: 評価額 $852B、Goldman Sachs・Morgan Stanley が主幹事、秋上場が有力。Anthropic（6/1、$965B）に続く申請。
  - https://openai.com/index/openai-submits-confidential-s-1/
  - https://fortune.com/2026/06/09/openai-files-confidential-s-1-sec-ipo/
- **Oracle Cloud 経由でのモデル提供を発表（6/11）**: Oracle Universal Credits で OpenAI モデルと Codex を利用可能に。$300B 超の Stargate パートナーシップの延長線。数週間以内に提供開始。
  - https://openai.com/index/openai-on-oracle-cloud/
- **ChatGPT Lockdown Mode が全 personal account + self-serve Business に拡大**: live web browsing / Deep Research / Agent Mode 等の外部接続機能を制限し、prompt injection 起点のデータ流出経路を遮断。
- **Active sessions セキュリティ機能 GA**: 全 ChatGPT account でサインインデバイス・位置情報表示・遠隔サインアウトが可能に。

### Google / DeepMind

- **Gemini 障害は復旧**: 6/10 10:30 PDT に大半のユーザーで解消確認。6/11 は新規 incident なし。
- **Gemini 3.5 Pro GA は依然未発表**: 6 月内目標（Pichai I/O 公約）。Vertex limited preview 継続、価格推定 $15/$60 per 1M tokens。
- **AFM 3 Cloud Pro の Google Cloud 上稼働**（ハイライト参照）が Google Cloud の AI infrastructure ビジネスにとって大きな勝利。
- WWDC 2026 最終日（本日 6/12）。Foundation Models Framework の Claude / Gemini 統合詳細の追加情報待ち。

### Microsoft / GitHub

- **Fable 5 社内利用 block**（ハイライト参照）
- **GitHub Copilot 内部ベンチ**: Fable 5 は autonomous coding work で旧 Opus tier 比ツール呼出 fewer + token 消費 lower。
- **6/16 Microsoft Work IQ API GA** まで 4 日。

### Cursor / 開発ツール

- **Cursor Bugbot アップデート**: review 時間 ~5 分→ ~90 秒（3x 高速化）、コスト 22% 低下、bug 検出率 10% 向上。内部エンジンを Composer 2.5（Moonshot Kimi K2.5 ベース）に置換。`/review` コマンドで push 前に Bugbot + Security Review を同時起動可能に。
  - https://cursor.com/blog/bugbot-updates-june-2026
- **Grok V9-Medium（1.5T params）**: 6 月中旬公開予定。Cursor data で post-training。

### その他

- **SpaceX 本日 Nasdaq 上場**: ティッカー SPCX、$75B 調達、評価額 $1.77T で史上最大 IPO。AI 企業ではないが Anthropic・OpenAI IPO と並ぶテック上場ラッシュの文脈。
  - https://www.cnbc.com/2026/05/20/spacex-ipo-live-updates.html
- **Cohere North Mini Code オープンソース公開（6/9）**: 30B パラメータ（MoE、アクティブ 3B）のコーディング特化モデル。H100 1 基で動作。Apache 2.0。Fable 5 等マネージドモデルのオンプレ代替候補。
  - https://cohere.com/blog/north-mini-code
- **Docker Gordon 正式 GA**: Docker Desktop 4.74+ 統合の AI エージェント。無料アカウントで利用可能。
  - https://www.docker.com/blog/meet-gordon-dockers-ai-agent-for-your-entire-container-workflow/

---

## 直近の注目予定

- **本日 6/12**: Apple WWDC 2026 最終日 / OpenAI macOS app cert revoke 期限
- **6/15**: Anthropic Programmatic Credit Pool 施行 / Claude API で Sonnet 4 / Opus 4 退役
- **6/16**: Microsoft Work IQ API GA
- **6/18**: Gemini CLI / Gemini Code Assist IDE 拡張サービス終了（Antigravity CLI 移行）
- **6/22**: Fable 5 の Pro/Max/Team/Enterprise 追加料金なし期間終了
- **6/23**: Fable 5 利用に usage credits 必要化
- **6/25**: gemini-3.1-flash-image-preview / gemini-3-pro-image-preview 廃止
- **6/27**: GPT-4.5 が ChatGPT から退役
- **6/30**: Devin クラシック環境廃止 / GPT-5.2・5.3-Codex 新規 API 不可化
- **6 月中旬**: Grok V9-Medium 公開予定
- **6 月後半**: Gemini 3.5 Pro GA / Mistral Vibe Slack 連携 Code Mode
- **7/1**: Anthropic Claude Partner Network 初回レビュー / Devin Cascade 完全廃止

---

## 改善メモ

- OpenAI Codex CLI changelog（developers.openai.com/codex/changelog）が再び 403。`daily-sources.md` で 3rd party 集約を fallback として明記を推奨
- Apple Machine Learning Research blog（machinelearning.apple.com/research）が AFM 3 詳細の一次情報源として高価値。`daily-sources.md` の Apple セクションに正式追加候補
- Snowflake 公式ブログを `daily-sources.md` に追加候補（2 回目の提案）
- Microsoft 社内 Fable 5 ban の報道は 3rd party 中心。Anthropic / Microsoft 公式の retention policy 比較表ページの URL を `daily-sources.md` に追加候補
- 各主要ソース WebFetch 403 継続中（2 ヶ月超）。Claude Code Changelog のみ WebFetch 安定取得可能、その他は WebSearch primary 運用継続
- 03_ai-news-industry で Fable 5（6/9）・OpenAI S-1（6/8）・Cohere North Mini Code（6/9）・Docker Gordon GA（5/27）が過去ダイジェストで未掲載だったとの補足あり。本サマリーでは統合済み
