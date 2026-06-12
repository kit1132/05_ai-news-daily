# AI News Daily Summary — 2026-06-10

> 本サマリーは 01_ai-news-Master・02_ai-news-Copilot・03_ai-news-industry の3ソース（6/10分）を統合して作成。

## 今日のハイライト

### 1. Claude Fable 5 / Mythos 5 公開 — SWE-Bench Pro 80.3%、初の公開 Mythos クラスモデル

**事実**: Anthropic が 6/9 に Claude Fable 5（一般公開）と Mythos 5（認定パートナー限定・セーフガード一部解除版）を同時リリースした。SWE-Bench Pro 80.3%（Opus 4.8 比 +11pt、GPT-5.5 比 +21.7pt）、Hex 分析ベンチ初の 90% 超達成。価格は入力 $10 / 出力 $50 per 1M tokens（Opus 4.8 の 2 倍、caching 90% 割引は継続）。コンテキスト 1M 入力 / 128k 出力。Claude API / AWS Bedrock / Vertex AI / Microsoft Foundry / GitHub Copilot / Harvey に同日 GA。6/22 まで Pro/Max/Team/Enterprise に追加料金なし。

**根拠**: +21.7pt という GPT-5.5 との SWE-Bench Pro 差は、現行フロンティアモデル間で過去最大級のギャップ。Opus 4.8（5/28 GA からわずか 12 日）が「安全フォールバック先」に格下げされ、ブロックされた応答（全セッションの <5%）のみ Opus 4.8 が処理する設計。6/4-5 の「pause button」提案から 4-5 日で史上最強モデルを公開する「安全議論と商用 GA の同時実行」戦略が鮮明になった。

**影響**: 開発者にとっての実質的な変化は「Opus 4.8 の 2 倍のコストで、SWE-Bench Pro +11pt の性能向上が得られるか」の判断。6/22 までの試食期間中に自分のユースケースで Fable 5 vs Opus 4.8 のコスパを検証できる時限的な機会がある。GitHub Copilot でも即日利用可能になったことで、OpenAI 製モデルだけで Copilot を提供する時代が完全に終わった。

**行動指針**: 6/22 までに Fable 5 を自分の主要タスクで検証し、Opus 4.8 比でどの程度の品質差があるか定量化する。品質差が実作業で体感できないなら、6/23 以降は Opus 4.8 据え置きでコスト最適化する。Claude Code ユーザーは v2.1.170 へのアップデートが必須（旧バージョンでは Fable 5 が picker に表示されない）。

- https://www.anthropic.com/news/claude-fable-5-mythos-5
- https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5
- https://techcrunch.com/2026/06/09/anthropic-released-claude-fable-5-its-most-powerful-model-publicly-days-after-warning-ai-is-getting-too-dangerous/
- https://github.blog/changelog/2026-06-09-claude-fable-5-is-generally-available-for-github-copilot/

### 2. Apple WWDC Day 2 — Xcode 27 にデュアルエンジン AI コーディング搭載、Foundation Models オープンソース化へ

**事実**: 6/9 の Platforms State of the Union で発表。Xcode 27 はローカル Neural Engine で動作する Swift 特化モデル（リアルタイム補完）と、Claude・Gemini・ChatGPT へのクラウドルーティング（大規模リファクタリング・テスト生成・自律デバッグ）のデュアルエンジン構成を採用。MCP および Agent Client Protocol に対応し、エージェントがシミュレータ操作・テスト実行を自律的に行える。Foundation Models フレームワークは同一 Swift API で Claude/Gemini を呼び出せるサーバーサイドモデル統合を追加し、今夏オープンソース化予定。Small Business Program 参加（累計 DL 200 万未満）のアプリは Private Cloud Compute 上の Apple Foundation Models を無料利用可能。

**根拠**: Apple が IDE レベルで Claude・Gemini・ChatGPT を「交換可能なバックエンド」として扱う設計は、特定 AI プロバイダへのロックインを回避する業界初のメジャー実装。MCP/ACP 対応は Anthropic 発のプロトコルが Apple エコシステムに正式採用されたことを意味し、MCP のデファクト標準化が一段進んだ。

**影響**: iOS/macOS 開発者は Xcode 27 移行で AI コーディング支援が IDE ネイティブになる。ローカルモデルによるリアルタイム補完はオフライン・低レイテンシで動作するため、Cursor や GitHub Copilot とは異なる体験になる。一方、EU 圏では DMA 問題により Siri AI が iOS 27/iPadOS 27 で提供されず、Apple Intelligence Extensions マーケットプレイスの欧州展開にも影響が出る。

**行動指針**: Swift/iOS 開発者は Xcode 27 ベータでデュアルエンジンを早期検証する。Foundation Models フレームワークのオープンソース化時期を追跡し、サーバーサイド Swift で Claude/Gemini を統合する選択肢を評価する。EU 向けアプリを提供している場合は、Siri AI 非対応の影響範囲を確認する。

- https://www.apple.com/newsroom/2026/06/apple-aids-app-development-with-new-intelligence-frameworks-and-advanced-tools/
- https://www.macrumors.com/2026/06/09/apple-outlines-major-ai-and-developer-tool-updates/
- https://www.apple.com/newsroom/2026/06/due-to-dma-siri-ai-delayed-in-eu-for-ios-27-and-ipados-27/

### 3. Code with Claude Tokyo 本日開催 — Anthropic 初の APAC 開発者カンファレンス

**事実**: Anthropic 初の APAC 開発者カンファレンスが本日 6/10 に東京で開催。Boris Cherny（Claude Code lead）、Ami Vora（CPO）、Angela Jiang（Claude API & SDK product lead）が登壇。Research / Claude Platform / Claude Code の 3 トラック構成で、「Beyond the Basics with Claude Code」では long-horizon タスク・multi-repo agent・並列実行が取り上げられる。ライブストリームは無料・グローバル公開、日英バイリンガル同時通訳。6/11 の Extended Tokyo は独立開発者向け。

**根拠**: 日本は Anthropic の APAC 最大ユーザーベースであり、NEC 30,000 人展開（4 月）+ Hitachi physical AI 提携（5 月）に続く APAC 戦略の集大成。SF（5/6）・London（5/19）に続く 3 都市目で、Fable 5 GA 翌日の開催により demo モデルとして Fable 5 が中心になる見通し。

**行動指針**: ライブストリームで「Beyond the Basics with Claude Code」セッションを優先視聴し、multi-repo agent・並列実行の実装パターンを確認する。録画は後日公開されるため、リアルタイム参加が難しければ Extended Tokyo（6/11）の録画を待つ。

- https://claude.com/code-with-claude/tokyo
- https://claude.com/code-with-claude/tokyo-extended

---

## カテゴリ別まとめ

### Anthropic / Claude

- **Claude Code v2.1.170（6/9 stable）** — Fable 5 を model picker に追加。VS Code 統合端末からの transcript 保存不具合を修正。旧バージョンでは Fable 5 選択不可のため実質強制アップデート（[changelog](https://code.claude.com/docs/en/changelog)）
- **Claude Code v2.1.169（6/8）** — `--safe-mode`フラグ、`/cd`コマンド（プロンプトキャッシュ維持でディレクトリ移動）、`disableBundledSkills`設定追加。エンタープライズ MCP ポリシー強制修正（[changelog](https://code.claude.com/docs/en/changelog)）
- **Claude Code v2.1.166（6/6）** — `fallbackModel`設定（最大 3 モデル）、deny ルールに glob パターン対応、`MAX_THINKING_TOKENS=0`で思考無効化（[changelog](https://code.claude.com/docs/en/changelog)）
- **Claude Cowork 利用時間倍増プロモーション（6/5–7/5）** — Pro/Max/Team の 5 時間制限を期間限定で倍増（[The New Stack](https://thenewstack.io/anthropic-claude-cowork-promotion/)）
- **Claude の自己コード生成率が 80% 超** — 昨年 2 月の 10% 未満から急増。自律的に後継システムを設計・開発できる AI への道筋を示唆（[Yahoo Finance](https://uk.finance.yahoo.com/news/anthropic-says-something-unsettling-happening-103500529.html)）
- **Anthropic、Google・Broadcom とのコンピュートパートナーシップ拡大** — IPO S-1 提出直後に発表。カスタム AI チップ共同開発を検討、NVIDIA 依存分散と推論コスト削減が狙い（[TechCrunch](https://techcrunch.com/2026/06/05/anthropic-google-broadcom-compute-partnership/)）
- **6/15: Sonnet 4 / Opus 4 API 退役まで 5 日** — Opus 4.6/4.7/4.8 + Fable 5 への migration ピーク

### OpenAI

- 6/9-6/10 に公式 changelog / release notes の新規エントリなし
- Codex CLI は v0.137.0 stable / v0.138.0-alpha.2 のまま据え置き（6/4 以降進展なし）
- GPT-5.2 / GPT-5.3-Codex は **6/30 で新規 API リクエスト不可化**（GPT-5.5 系への一本化加速）
- Fable 5 vs GPT-5.5 = 21.7pt 差（SWE-Bench Pro）が出回り、対抗モデル発表観測が再燃

### Google / DeepMind

- 6/9-6/10 に公式 release notes の新規エントリなし
- Gemini 3.5 Pro GA は 6 月内目標のまま未発表（Vertex limited preview 継続）
- WWDC 2026 で Gemini 1.2T params カスタムモデルが Apple Siri 中核プロバイダとして年 $1B ライセンス採用が確定

### Microsoft / GitHub

- **GitHub Copilot で Fable 5 GA 開始（6/9）** — VS Code / cloud agent / Copilot CLI / Copilot SDK の model picker に追加（[GitHub Blog](https://github.blog/changelog/2026-06-09-claude-fable-5-is-generally-available-for-github-copilot/)）
- **Microsoft Foundry にも Fable 5 同日 GA** — 3,000+ モデルカタログで Anthropic が「同日 frontier 解禁」を継続
- **GitHub Copilot 従量課金「請求ショック」継続** — 6/1 開始後、10x–50x コスト増報告が続出。8/31 まで一時的クレジット増量の救済措置中（[Visual Studio Magazine](https://visualstudiomagazine.com/articles/2026/06/04/copilot-billing-shock-hits-developers.aspx)）
- **MXC（Execution Containers）** — Build 2026 発表の AI エージェント向け OS レベルサンドボックス。ハイパーバイザーベース分離で起動 1 桁 ms。OpenAI・NVIDIA・Manus が採用パートナー（[VentureBeat](https://venturebeat.com/security/microsoft-launches-mxc-an-os-level-sandbox-for-ai-agents-with-openai-and-nvidia-already-on-board)）
- **Microsoft AI Models 7 モデル正式発表** — MAI-Thinking-1（推論）、MAI-Code-1-Flash（コーディング）等。学習データに非ライセンス Web データ使用が判明（[Publickey](https://www.publickey1.jp/blog/26/7aimicrosoft_ai_models.html)）

### Copilot Studio / Power Platform

- **Platform Build 2026.5.4** — 多言語音声エージェント、マルチエージェント分析、カスタムメトリクス分析追加。**破壊的変更**: GPT-5 Auto が enhanced task completion エージェントで利用不可に（[Microsoft Learn](https://learn.microsoft.com/en-us/power-platform/released-versions/copilotstudio/2026.5.4)）
- **Release Wave 2026w1** — マルチターン会話評価（6 月 GA）、MCP 準拠ツール（7 月 GA）、SharePoint リスト知識ソース（7 月 Preview）

### Apple

- **Siri AI、DMA 問題で EU 圏内 iOS 27/iPadOS 27 展開を延期** — Mac・Apple Watch・Vision Pro では提供。欧州委員会は反論（[Apple Newsroom](https://www.apple.com/newsroom/2026/06/due-to-dma-siri-ai-delayed-in-eu-for-ios-27-and-ipados-27/)）

### Cursor / Devin

- Cursor 3.7（6/4-5）以降新規 changelog なし。Design Mode（ブラウザ内 UI 直接編集）が直近の主要機能
- Devin: v3 API GA（6/5）以降新規エントリなし。6/30 Classic 環境廃止、7/1 Cascade EOL が直近の期限

### 規制・政策

- **EU AI Act、8/2 に高リスク AI システム規制が本格適用** — 生体認証・重要インフラ・採用/人事・信用スコアリング等が対象。違反時は最大 €35M or 売上 7% の罰金。日本企業の EU 向け AI サービスにも影響（[Legal Nodes](https://www.legalnodes.com/article/eu-ai-act-2026-updates-compliance-requirements-and-business-risks)）

### 業界動向

- **Strava、AI スクレイピング対策で API 有料化（6/30）** — 開発者登録が年初来 448% 増加への対策。IPO 準備中（[TechCrunch](https://techcrunch.com/2026/06/01/strava-declares-war-on-scrapers-ahead-of-ipo/)）

---

## 直近の注目予定

- **6/11**: Code with Claude Tokyo Extended（独立開発者向け、録画後日公開）
- **6/15**: Sonnet 4 / Opus 4 API 退役 / Anthropic Programmatic Credit Pool 施行 / Conditional Access ポリシー変更
- **6/16**: Microsoft Work IQ API GA
- **6/18**: Gemini CLI / Gemini Code Assist IDE 拡張サービス終了（Antigravity CLI 移行）
- **6/22**: Fable 5 の Pro/Max/Team/Enterprise 追加料金なし期間終了
- **6/25**: gemini-3.1-flash-image-preview / gemini-3-pro-image-preview 廃止
- **6/27**: GPT-4.5 が ChatGPT から退役
- **6/30**: Devin Classic 環境廃止 / GPT-5.2・GPT-5.3-Codex 新規 API 不可化 / Copilot Studio Teams クラシック作成終了 / Strava API 有料化
- **7/1**: M365 価格改定発効 / Cursor 新価格体系 / Cascade EOL
- **8/2**: EU AI Act 高リスク AI システム規制の本格適用
- **8/31**: GitHub Copilot クレジット救済措置終了

---

## 改善メモ

- **Fable 5 / Mythos 5 system card** の公式 URL を `daily-sources.md` 最優先に追加候補。`anthropic.com/news/claude-fable-5-mythos-5` が WebFetch 403 継続
- **`platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5`** が Fable 5 公式仕様の決定版 URL。WebFetch 疎通成功時は `daily-sources.md` 最優先層に追加
- **GitHub Copilot 公式 changelog**（github.blog/changelog）は Fable 5 GA を 6/9 同日公開、WebSearch で安定取得可能。`daily-sources.md` 追加候補
- 各主要ソース WebFetch 403 継続中（anthropic.com/news、mc.merill.net、GIGAZINE、Hacker News 等）。WebSearch 経由で代替取得を継続
- WWDC 2026 Day 2 以降（〜6/12）の Platform セッションは Apple Intelligence Extensions API 仕様の情報源として臨時追跡継続
