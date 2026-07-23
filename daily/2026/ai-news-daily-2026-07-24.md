# AI News Daily Summary — 2026-07-24

> 本サマリーは 01_ai-news-Master・02_ai-news-Copilot・03_ai-news-industry の3ソース（7/24分）を統合して作成。

本日の中心は**ガバナンスと地政学**。昨日予告した **OpenAI GPT-5.6 のサブプロセッサー既定有効化（MC1422074）が本日 7/24 発効**し、M365 Copilot 系3レイヤーで opt-out 判断が現実の期限を迎えた。地政学面では **ホワイトハウスが Moonshot AI による Anthropic「Fable」蒸留（Kimi K3）を名指しし財務省が制裁を示唆**。戦略面では **OpenAI が本番運用エージェント基盤「Presence」を限定 GA** で投入し「モデル→実装体制」競争が本格化。開発ツールでは **Anthropic が Claude Code 向け「Claude Security」プラグインを beta 提供**、一方 **Claude Opus 4.7 Fast モードは本日提供終了**。

## 今日のハイライト

### 1. OpenAI サブプロセッサー（GPT-5.6）既定有効化が本日発効 — テナント管理者は opt-out 判断の期限

**事実**: MC1422074 の予告どおり、OpenAI 運用モデル（GPT-5.6 含む）を Microsoft サブプロセッサーとして扱う既定有効化が **2026-07-24 に発効**した（opt-out 制）。公式 Learn ページで一次確認済み。

**根拠**: 適用範囲は **M365 Copilot・M365 アプリ内 Copilot・Copilot Studio の3レイヤー**。GPT-5.6 は Word/Excel/PowerPoint/Copilot Chat/Cowork の優先エンジンとして展開され、Copilot Studio ではエージェント作成時にモデル選択が可能。**Azure OpenAI（Microsoft 運用の OpenAI モデル）には非該当**。政府/ソブリンクラウド（GCC/GCC High/DoD）は対象外、EU Data Boundary には含まれる。

**影響**: 除外事項が重い — **FedRAMP High 未認証・PCI DSS AOC 未提供・HITRUST CSF 未提供・SOC 1 Type 2 未提供**。規制業種（金融・医療・公共）は自動有効化のまま放置するとコンプライアンス前提を崩す恐れ。

**行動指針**: opt-out は M365 admin center →「AI providers operating as Microsoft subprocessors」→ OpenAI →「No users」（AI 管理者/グローバル管理者ロール必要）。**Copilot Studio/Power Platform 利用組織は Power Platform admin center 側の外部 LLM 許可設定も併せて制御**。ガバナンス方針がある組織は本日中に有効/無効の意思決定を確定させる。

- https://learn.microsoft.com/en-us/microsoft-365/copilot/openai-subprocessor
- https://mc.merill.net/message/MC1422074

### 2. ホワイトハウス、Moonshot AI が Anthropic「Fable」蒸留で Kimi K3 を開発と名指し — 財務省が制裁示唆

**事実**: 7/22-23、OSTP 局長 Michael Kratsios が中国 Moonshot AI を公に名指しし、米国モデルへの大規模「産業的蒸留」を行う内部プラットフォームを構築し **Anthropic の Fable を蒸留して Kimi K3 を開発**、あわせて禁輸対象の NVIDIA GB300 サーバーをタイ経由で取得したと主張。財務省が制裁の可能性に言及。

**根拠**: 背景に Anthropic の 2/23 開示（DeepSeek/Moonshot/MiniMax が約24,000の不正アカウントで Claude と計1,600万回超やり取り、うち Moonshot 340万回超）。ただし **Fable の一般公開は 7/1** で、2.8兆パラメータの K3 を蒸留のみで構築できたか疑問視する専門家もいる。

**影響**: 中国製オープンモデル（Kimi/DeepSeek/GLM）採用時の**モデル出自・サプライチェーン・制裁リスク**が提案の前提条件に格上げされる。「米エンタープライズ・トークン最大46%が中国製」（7/7 CNBC）と表裏の論点。

**行動指針**: 中国製オープンウェイト採用を検討する組織は、出自・輸出規制・制裁エクスポージャを調達チェックリストに追加。**Kimi K3 オープンウェイトは 7/27 公開予定**で、公開後に技術的検証が進むため判断は同日以降に再評価するのが妥当。

- https://cyberscoop.com/white-house-accuses-moonshot-ai-anthropic-model-distillation/
- https://www.cnbc.com/2026/07/23/moonshot-kimi-nvidia-ai-chips-export-ban.html

### 3. OpenAI「Presence」限定 GA — 本番運用エージェントの構築・統制・改善を一括する企業向け基盤

**事実**: 7/22、OpenAI が音声・チャット両対応のエンタープライズ向けエージェント運用プラットフォーム **「Presence」を限定 GA** で投入。ポリシー/SOP、ガードレール、承認済みアクション、デプロイ前シミュレーション、評価、Codex による継続改善ループを単一枠組みに統合。

**根拠**: 対象業務はカスタマーサポート・アウトバウンド営業・調達・IT・HR。**OpenAI 自社の受信サポート約75%を処理**、稼働数週でヘルプデスク担当者の応答品質に到達と主張。BBVA México、SoftBank（日本語エージェント）、IAG 傘下 Retail Insurance Australia が先行利用。Forward Deployed Engineers 帯同の「コンサル型」課金。

**影響**: Anthropic「Ode」（7/15・$1.5B規模の実装 JV）/ ChatGPT Work（7/9）に続く **「モデル→実装体制」競争の OpenAI 版**。生モデル提供から本番グレードのマネージド基盤への戦略転換が鮮明。

**行動指針**: エージェント導入提案は、**権限制御・エスカレーション規則・デプロイ前評価を要件化する標準テンプレート**として Presence の構成を参照可。価格・広範提供は limited GA 拡大に合わせ開示予定のため、正式価格の追跡を継続。

- https://openai.com/index/introducing-presence/
- https://venturebeat.com/orchestration/openai-unveils-presence-a-new-platform-that-lets-enterprises-launch-and-manage-realtime-voice-agents-and-chatbots

## カテゴリ別まとめ

### Anthropic / Claude
- **Claude Security プラグインを Claude Code に beta 提供**（7/22、7/23 アクセス拡大）— ターミナルからコミット前差分スキャンやリポジトリ全体の深掘りセキュリティレビューを実行するマルチエージェント型脆弱性スキャナ。インジェクション・認証バイパス・メモリ破損・ロジック欠陥などを検出し、各指摘は敵対的検証パスを通してから提示。有料プラン＋Claude Code v2.1.154 以降・`/config` で dynamic workflows 有効化が必要。 https://claude.com/product/claude-security
- **「Teach Claude a Skill」**（7/22）— 作業を画面録画・ナレーションで実演すると Claude が再利用可能な Skill に変換。デスクトップアプリの Cowork インターフェースで Pro/Max/Team に順次提供。 https://www.anthropic.com/news
- **Claude Opus 4.7 Fast モードを本日 7/24 提供終了** — 終了後は `claude-opus-4-7` へ `speed: "fast"` 指定でエラー。**Claude Opus 4.8 の Fast モードへ移行が必要**。 https://platform.claude.com/docs/en/release-notes/overview
- **Claude Opus 5 ローンチ間近観測（新規ウォッチ）** — 複数トラッカーが準備を報告、Polymarket で「7/23 launch」確率が一時88%。噂では 1M トークン文脈・"xhigh" 推論。7/24 時点で公式発表（モデルカード/API/`claude-opus-5` ID/価格）は未確認、現行旗艦は Opus 4.8（5/28）のまま。 https://www.testingcatalog.com/anthropic-preparing-for-potential-claude-opus-5-rollout/

### OpenAI
- **Presence 限定 GA**（ハイライト参照）
- **Project Camellia — ジョージア州に初の自社建設データセンター**（7/22）: $20B コミット、フルスケール総額$30B超、Georgia Power と 3.2GW 契約（2028〜2032段階供給）で単一サイト電力コミットとして世界最大級。25年契約で最大1,000MW の需要応答、既存顧客の電気料金は非転嫁・インフラ費用は OpenAI 全額負担、閉ループ冷却で水使用抑制。 https://www.datacenterdynamics.com/en/news/openai-reveals-32gw-data-center-project-in-effingham-county-georgia/
- **Codex CLI 0.146.0-alpha.4 進行中**（7/23）— 安定版は 0.145.0（7/21）据え置き。alpha ビルドが日次で刻まれるが公開リリースノートに具体的変更記載なし。 https://github.com/openai/codex/releases

### 開発ツール（Claude Code / Copilot）
- **Claude Code v2.1.218**（7/22）— ① `/code-review` をバックグラウンドのサブエージェントとして実行（レビュー出力で会話が埋まるのを防止）、② スクリーンリーダー向けの削除操作読み上げ、③ **Windows で `\u` プレフィックス区間を含むパスがアクセス不能になる不具合を修正**、④ MCP 接続診断に HTTP ステータス/エラー詳細を表示、⑤ 複数行ペースト対応、⑥ compaction 後のトークン表示不具合修正、⑦ Bedrock スペンド計測改善。既報 v2.1.217（7/21・サブエージェント同時実行上限 既定20）。 https://code.claude.com/docs/en/changelog
- **GitHub Copilot CLI v1.0.74-4 pre-release**（7/23）— Open Plugin Spec v1 マニフェストと `mcp.json` 設定サポート、サブエージェント由来のプロンプト識別表示、IDE 連携の再接続安定化。安定版は v1.0.73（7/20）据え置き。 https://github.com/github/copilot-cli/releases

### Microsoft / Copilot Studio（一次据え置き・新規なし）
- **Copilot Studio What's New**: June 2026 節のまま（7月節未公開）。
- **M365 Copilot Release Notes**: 「July 15, 2026」バッチが最新のまま。次バッチは 7/29 前後見込み。
- **Released Versions（Copilot Studio）**: Build **2026.6.3（6/30初出）が最新のまま**。予告の 2026.7.x は未反映（次の要監視は 7/28 火）。
- Message Center 本日の新規 MC は MC1422074 発効のみ（ハイライト参照）。Power Platform 月次「July 2026」フィーチャー更新は未公開（最新は 6/11 June）。

### 市場データ
- **Okta Enterprise AI Index**（7/23）— 2026年6月までの4年間の純エンタープライズ・アカウント成長で **Anthropic を100とすると OpenAI 66.9・Google Workspace 59.8・GitHub 56.6・Cursor 42.4**。Anthropic は 3月に企業顧客数、4月に MAU で OpenAI を逆転済み。ただし総リーチは **Microsoft 365 が首位**（Anthropic のアカウント規模は M365 の5割未満）、組織の57%が2つ以上の AI プラットフォームを併用。 https://www.okta.com/newsroom/articles/the-okta-enterprise-ai-index/

### 規制・地政学
- ホワイトハウス／Moonshot「Fable」蒸留・制裁示唆（ハイライト参照）

## 直近の注目予定

- **7/27**: Kimi K3 オープンウェイト公開予定
- **7/28（火）**: Copilot Studio 版ページ 2026.7.x 反映見込み・Power Platform 非推奨/Released Versions/Release Wave 定例更新
- **7/29 前後**: M365 Copilot Release Notes 次バッチ見込み
- **7/30**: M365 Copilot メモリ活用のエージェント提案 GA・拡張機能 What's New 次月次見込み
- **7/31**: Devin classic 環境設定 read-only 参照終了
- **8/1**: covered frontier model 60日 EO 期限
- **8/3**: 旧「Claude in Slack」退役
- **8/5**: Claude Opus 4.1 の Claude API 退役 / Cowork 倍増利用枠終了
- **8/9**: ChatGPT Atlas シャットダウン
- **8/26**: OpenAI Assistants API 廃止 / o3 退役 / GPT-4.5 完全廃止
- **8/31**: Sonnet 5 促進価格終了（→ $3/$15）
- **9月**: iOS 27 / macOS 27 GA（AFM 3 本番）

## 改善メモ

- 3ソースとも新規提案・障害の変化なし（継続分は各リポの IMPROVEMENT-BACKLOG.md 参照）。
- **Gemini 3.5 Pro GA は複数ソースで依然「未ローンチ」**（Master・industry で言及一致）。公開 API は gemini-3.5-flash / gemini-3.1-pro-preview のまま、7/16 Bloomberg の「月単位遅延」から状況変化なし。GA・価格判明後に更新。
- Master: 金曜のため週次復旧チェックは非対象（次回 07-27 月曜）。
- industry: 継続提案 1件（B-004 取得方法欄の WebSearch 優先化、25回目）。
