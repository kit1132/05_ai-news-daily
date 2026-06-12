# AI News Daily Summary - 2026-04-07

## 今日のハイライト

### 1. OpenAI $1,220億調達の裏で Sora 終了・GPT-4o 引退 — 「選択と集中」の加速が示す、特定プロダクト依存のリスク

**事実**: OpenAIが$1,220億（評価額$8,520億）の資金調達を完了。月間売上$20億、週間アクティブユーザー9億人超、エンタープライズ収益が全体の40%超に成長し年内IPOを準備中。一方、GPT-4oは4/3に全プランから完全引退。Soraも4/26にアプリ終了、9/24にAPI終了の2段階シャットダウンを発表。

**根拠**: Soraはピーク時ユーザー約100万→50万未満に減少し、運用コストは推定1日$100万に対し累計収益はわずか$210万。計算資源はコーディング・エンタープライズ製品（コードネーム"Spud"）に再配分される。SoftBank・a16z・Amazon・Nvidiaが参加した資金調達と同時に不採算プロダクトを切る判断は、IPO前の収益構造最適化として整合する。

**影響**: Sora APIを組み込んでいるプロダクトは9月までに代替が必要。GPT-4oベースのプロンプト・ファインチューニング資産も移行対象。OpenAIの製品ライフサイクルが「公開→急速な世代交代→終了」のパターンを繰り返しており、特定モデル・機能への依存リスクが顕在化した。

**行動指針**: Sora APIを使っている場合は即座に移行計画を立てる。GPT-4oのプロンプト資産がある場合はGPT-5系への互換性テストを実施。OpenAI製品への依存度が高い組織は、モデル抽象化レイヤー（LiteLLM等）の導入を検討し、単一ベンダーロックインを回避する設計に移行すべき。

- https://openai.com/index/accelerating-the-next-phase-ai/
- https://the-decoder.com/openai-sets-two-stage-sora-shutdown-with-app-closing-april-2026-and-api-following-in-september/
- https://help.openai.com/en/articles/20001152-what-to-know-about-the-sora-discontinuation

### 2. Copilot Chat 4/15 仕様変更まであと8日 — 2,000人以上の組織は Word/Excel/PowerPoint で完全削除、対応猶予ゼロ

**事実**: 4/15よりWord/Excel/PowerPoint/OneNoteでのCopilot Chat（無料版）アクセスが制限。2,000人以上の組織ではボタン・サイドパネルが完全削除されアプリ内アクセス不可に。2,000人未満の組織は「標準アクセス」に格下げでピーク時に品質・パフォーマンスが制限。Outlookでのアクセスは全組織で維持。

**根拠**: 無料ユーザーは「Copilot Chat (Basic)」、有料ライセンスは「M365 Copilot (Premium)」に明確に二層化。Microsoftが無料利用を段階的に絞り、有料ライセンスへの誘導を強化する価格戦略の一環。組織規模で影響度が異なる点が今回新たに判明した。

**影響**: 大規模組織で無料Copilot Chatを日常的に使っているユーザーは、4/15以降にWord/Excel/PowerPoint内でCopilotを利用できなくなる。ユーザーからの問い合わせ急増が予想され、IT部門への事前告知が間に合わない組織も出てくる。

**行動指針**: 2,000人以上の組織のIT管理者は、今週中に影響範囲の社内周知を完了させる。有料ライセンスの追加購入判断が必要な場合は予算確保を急ぐ。2,000人未満の組織はピーク時制限の影響度を見極めてから判断でよい。

- https://office-watch.com/2026/microsoft-removes-copilot-chat-word-excel-powerpoint-april-2026/
- https://samexpert.com/copilot-chat-enterprise-restriction-april-2026/

### 3. DeepSeek V4 発表 — 1Tパラメータ・Huaweiチップ・$0.30/MTok、コスト構造を根本から変える選択肢

**事実**: DeepSeek V4が4月後半リリース予定。1T MoEパラメータ（アクティブ37B）、1Mコンテキスト、SWE-bench 81%。Huawei Ascend 950PRチップで動作する初のフロンティアモデル。Apache 2.0でオープンソース。料金$0.30/MTok。

**根拠**: SWE-bench 81%はコーディングタスクでトップクラス。$0.30/MTokはClaude Opus 4.6やGPT-5と比較して桁違いに安い。Huaweiチップでの動作は、米国輸出規制下でもNvidia非依存のAI開発が可能であることを実証した。

**影響**: コスト感度の高いユースケース（大量バッチ処理、社内ツール等）で有力な選択肢になる。同時にHuaweiチップ上でフロンティアモデルが動く事実は、半導体規制の実効性に疑問を投げかける。

**行動指針**: 4月後半のリリース後、自社ユースケースでの性能評価を計画しておく。ただし地政学リスク（データ主権・取引規制の将来変更）を考慮し、本番環境での採用は慎重に判断。コスト比較のベンチマーク用途として先行テストするのが妥当。

- https://www.nxcode.io/resources/news/deepseek-v4-release-specs-benchmarks-2026
- https://findskill.ai/blog/deepseek-v4-release-date-specs/

---

## カテゴリ別まとめ

### Microsoft 365 Copilot / Copilot Studio

- **Copilot Chat 4/15仕様変更の詳細判明**: 2,000人以上の組織はWord/Excel/PowerPoint/OneNoteで完全削除、2,000人未満は標準アクセスに格下げ。Outlookは全組織で維持
  - https://office-watch.com/2026/microsoft-removes-copilot-chat-word-excel-powerpoint-april-2026/
  - https://samexpert.com/copilot-chat-enterprise-restriction-april-2026/

- **Word for iPhone で Copilot 共同作成機能追加**: 文書内でCopilotを共同作成者として直接利用可能に
  - https://techcommunity.microsoft.com/blog/microsoft365insiderblog/work-with-copilot-as-a-co%E2%80%91creator-directly-in-word-for-iphone/4507902

- **Project Manager Agent がワールドワイド展開中（4月〜）**: AIプロジェクト計画・進行管理エージェント。3月パブリックプレビュー開始
  - https://techcommunity.microsoft.com/blog/microsoft365copilotblog/what%E2%80%99s-new-in-microsoft-365-copilot--march-2026/4506322

- **2026 Release Wave 1 新機能**: OpenAPI v3コネクタ構築、エージェントワークフローへの人間入力（Outlook経由）、M365 Copilot→Copilot Studioコピー機能、GCCH環境対応
  - https://learn.microsoft.com/en-us/power-platform/release-plan/2026wave1/microsoft-copilot-studio/planned-features

- **M365 Message Center注目**: Outlook iOS/Androidの秘密度ラベル推奨・自動適用（4月中旬〜）、Viva Engageダイジェスト改善、プロフィールカードにAwards/Certifications追加
  - https://mc.merill.net/

- **MAI自社モデル3種リリース（4/2）**: MAI-Transcribe-1（音声認識、25言語、2.5倍速）、MAI-Voice-1（音声生成）、MAI-Image-2（画像生成）をFoundryで提供。OpenAI依存からの脱却
  - https://microsoft.ai/news/today-were-announcing-3-new-world-class-mai-models-available-in-foundry/
  - https://venturebeat.com/technology/microsoft-launches-3-new-ai-models-in-direct-shot-at-openai-and-google

### OpenAI

- **$1,220億調達完了（評価額$8,520億）**: SoftBank・a16z・Amazon・Nvidia参加。月間売上$20億、週間アクティブ9億人超。年内IPO準備中
  - https://openai.com/index/accelerating-the-next-phase-ai/

- **Sora終了の詳細**: ピーク時100万→50万未満ユーザーに減少、運用コスト推定1日$100万、累計収益$210万。計算資源はコーディング・エンタープライズ製品に再配分。アプリ4/26終了、API 9/24終了
  - https://help.openai.com/en/articles/20001152-what-to-know-about-the-sora-discontinuation
  - https://the-decoder.com/openai-sets-two-stage-sora-shutdown-with-app-closing-april-2026-and-api-following-in-september/

- **GPT-4o全プランから完全引退（4/3）**

### Anthropic / Claude

- **サードパーティエージェント課金ポリシー変更（4/4〜）**: Claude Pro/MaxでOpenClaw等のサードパーティAIエージェント利用をブロック。最大50倍のコスト増
  - https://techcrunch.com/2026/04/04/anthropic-says-claude-code-subscribers-will-need-to-pay-extra-for-openclaw-support/

- **Claude Codeソースコード流出（約51.2万行）**: リリースパッケージングのミス。顧客データ・認証情報の漏洩はなし
  - https://www.spokesman.com/stories/2026/apr/01/anthropic-accidentally-exposes-system-behind-claud/

- **Claude.ai 大規模障害（4/6）**: 約2時間のダウン。ログイン・チャット・音声モード・Claude Codeに影響。Downdetectorで2,500人以上が報告
  - https://www.techradar.com/news/live/claude-anthropic-down-outage-april-6-2026

- **英国政府がAnthropic事業拡大を誘致**: Pentagon対立（軍事利用拒否によるブラックリスト指定）を受け、英国政府がロンドンオフィス拡張・二重株式上場を提案。5月下旬のDario Amodei訪英時に正式提示予定
  - https://www.business-standard.com/technology/tech-news/britain-woos-anthropic-to-expand-after-clash-with-pentagon-report-126040500137_1.html

- **Claude API max_tokens 300Kに引き上げ**: Message Batches APIでOpus 4.6/Sonnet 4.6対応。1Mコンテキストβ（Sonnet 4.5/4）は4/30終了
  - https://releasebot.io/updates/anthropic

- **Claude Code: /powerupレッスン・パフォーマンス改善**: セッション再開の高速化、各種バグ修正
  - https://releasebot.io/updates/anthropic/claude-code

### Google

- **Gemma 4公開**: Gemini 3ベースのオープンウェイトモデル。E2B/E4B/26B MoE/31B Denseの4サイズ、Apache 2.0
  - https://blog.google/innovation-and-ai/technology/developers-tools/gemma-4/

- **Gemini 3.1 Flash Live + AI Studio「Antigravity」コーディングエージェント追加**
  - https://android-developers.googleblog.com/2026/04/AI-Core-Developer-Preview.html

- **DeepMind + Agile Robots 産業用AIロボティクス提携**: Gemini Roboticsファウンデーションモデルを産業用ロボットに統合。電子機器製造・自動車・データセンター・物流分野で展開予定
  - https://techcrunch.com/2026/03/24/agile-robots-becomes-the-latest-robotics-company-to-partner-with-google-deepmind/

### モデル・技術

- **DeepSeek V4**: 1T MoEパラメータ、1Mコンテキスト、SWE-bench 81%、$0.30/MTok。Huawei Ascend 950PRチップ対応。4月後半リリース予定
  - https://www.nxcode.io/resources/news/deepseek-v4-release-specs-benchmarks-2026

- **Arcee AI Trinity-Large-Thinking**: 398B MoE（アクティブ13B）の米国製オープンソース推論モデル。Apache 2.0。PinchBenchでClaude Opus 4.6に肉薄（91.9 vs 93.3）。訓練コスト$2,000万
  - https://venturebeat.com/technology/arcees-new-open-source-trinity-large-thinking-is-the-rare-powerful-u-s-made
  - https://huggingface.co/arcee-ai/Trinity-Large-Thinking

- **PrismML 1-bit Bonsai**: 8Bパラメータでメモリ1.15GB。メモリ14倍のモデルと同等以上の性能
  - https://gigazine.net/news/20260406-prismml-1-bit-bonsai/

- **Google TurboQuant**: KVキャッシュ圧縮でメモリ100倍削減。ICLR 2026発表
  - https://www.sciencedaily.com/releases/2026/04/260405003952.htm

### エンタープライズ・ツール

- **Stripe Minions**: AIコーディングエージェントが週1,300+ PR生成。Slack/バグレポート/機能リクエストから自動PR→人間レビュー→本番投入
  - https://news.ycombinator.com/

- **Nvidia エンタープライズAIエージェントプラットフォーム**: Adobe・Salesforce・SAP・ServiceNow等17社が採用するオープンソースAgent Toolkit
  - https://venturebeat.com/technology/nvidia-launches-enterprise-ai-agent-platform-with-adobe-salesforce-sap-among

- **GitHub Copilot: ユーザーデータでAIモデル訓練開始（4/24〜）**: Free/Pro/Pro+が対象。オプトアウトしない限り自動適用
  - https://the-decoder.com/github-will-use-copilot-interaction-data-to-train-ai-models-starting-april-2026/

- **OpenClaw: GitHub 21万スター到達**: ローカルAIアシスタント。50以上のサービス統合。Anthropic課金ポリシー変更の直接原因
  - https://github.com/trending

### 市場データ

- **Similarweb AIトラッカー**: ChatGPTのトラフィックシェアが65%未満に低下（1年前86.7%）。Geminiが20%超に成長。Grokが3.4%でDeepSeek（3.7%）に接近
  - https://x.com/Similarweb/status/2008805674893939041

- **IDC: 欧州AI支出2029年に$2,900億予測**: CAGR 33.7%。グローバルでは2030年にAI累積経済効果$22.3兆（GDP比3.7%）
  - https://cyprus-mail.com/2026/04/06/european-ai-spending-set-to-reach-290bn-by-2029

- **MCP（Model Context Protocol）: 9,700万インストール突破**: 全主要AIプロバイダーがMCP対応ツールを出荷中
  - https://news.ycombinator.com/

- **AIデータセンター建設の半数が延期・中止見込み**: $6,500億投資計画のうち約半数がトランスフォーマー・バッテリー不足で遅延
  - https://gigazine.net/gsc_news/en/20260404-ai-data-center-delayed-canceled/

### 新興ツール

- **Baton**: AIコーディングエージェントのオーケストレーションツール（Product Hunt 4/1）
- **Claudoscope**: Claude Codeセッションのコスト追跡・検索
- **Cursor 3**: 並列エージェント・マルチリポワークフロー対応
  - https://www.producthunt.com/leaderboard/monthly/2026/4

---

## 直近の注目予定

- **4/15**: Copilot Chat 仕様変更（Basic/Premium 二層化）
- **4/15**: Power Platform & Copilot Studio アップデートイベント（9:00 AM PDT）
- **4/17**: Anthropic OpenClaw 移行クレジット期限
- **4/20**: Teams Pre-Day（Orlando）
- **4/20〜**: Security Copilot M365 E5 自動有効化開始
- **4/21-23**: Microsoft 365 Community Conference（Orlando）
- **4/24**: GitHub Copilot Free/Pro データ学習利用開始
- **4/26**: Sora アプリ終了
- **4/30**: Claude 1M コンテキストベータ終了（Sonnet 4.5/4）
- **5/1**: M365 E7 Frontier Suite GA / Agent 365 GA

---

## 改善メモ

### 01_ai-news-Master
- 全12ソース中11ソースでWebFetch 403（3日連続）。WebSearchフォールバックで取得成功
- daily-sources.md の取得方法をWebSearch優先に変更することを強く推奨

### 02_ai-news-Copilot
- learn.microsoft.com 配下でWebFetch 403継続（5日連続）。daily-sources.md の取得方法をWebSearchプライマリに更新することを強く推奨（2回目の提案）
- mc.merill.net / supersimple365.com / releasebot.io / techcommunity.microsoft.com: WebFetch 403 → WebSearch経由で取得成功

### 03_ai-news-industry
- 全RSSフィード（Google News RSS・GIGAZINE・The Decoder・VentureBeat・Publickey・Hacker News・Product Hunt・GitHub Trending）がWebFetch 403。全ソースWebSearchフォールバックで取得
- WebSearch主体の取得フローへの変更を推奨（2回目の提案）

### 共通
- 3ソースすべてでWebFetch 403率が極めて高い状態が数日間継続。全ソースのdaily-sources.mdでWebSearchをプライマリに一括変更すべき段階
