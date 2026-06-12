# AI News Daily Summary - 2026-04-08

## 今日のハイライト

### 1. Anthropic「Claude Mythos Preview」発表 — Project Glasswing でサイバーセキュリティ防御の枠組みが変わる

**事実**: Anthropicが次世代フロンティアモデル「Claude Mythos Preview」を限定公開した（4/7）。サイバーセキュリティ防御イニシアティブ「Project Glasswing」として、AWS・Apple・Google・Microsoft・Nvidia・CrowdStrike・Palo Alto Networks・Linux Foundation等12社を含む40組織に限定提供。過去数週間で「数千のゼロデイ脆弱性（多くがクリティカル、1〜2十年前のものを含む）」を発見済み。エクスプロイトの自動生成も可能なため、安全策が整うまで一般公開は見送り。

**根拠**: セキュリティ研究者レベルの脆弱性発見能力を持つAIが、数週間で数千件のゼロデイを発見したという規模は前例がない。従来のバグバウンティプログラムやペネトレーションテストでは年間数十件の発見が相場であり、桁が2つ以上異なる。Vertex AIでも利用可能な点から、エンタープライズ展開を前提とした設計であることがわかる。

**影響**: セキュリティベンダーのサービス価値が根本的に問い直される。AIが自動で脆弱性を発見・報告する体制が普及すれば、脆弱性の「発見」から「修正」にボトルネックが移行する。同時に、攻撃者側が同等能力のモデルを入手した場合のリスクも桁違いに上がる。

**行動指針**: 一般公開時期は未定のため、現時点で直接使えるアクションはない。ただし自社のパッチ適用体制が「月次」の場合、AIによる脆弱性発見の高速化に対応できない。パッチ適用サイクルの短縮（最低週次）を検討すべき段階に入った。経過観察。

- https://techcrunch.com/2026/04/07/anthropic-mythos-ai-model-preview-security/
- https://www.anthropic.com/glasswing

### 2. Anthropic 売上ランレート $30B 突破・Google/Broadcom と 3.5GW TPU 契約 — AI基盤の「持てる者」と「持たざる者」の差が決定的に

**事実**: Anthropicが Google・Broadcom と新たな計算資源契約を締結。2027年から約3.5GWの Google TPU 容量を確保（現在の1GWに追加）。年間売上ランレートは$30B（2025年末の$9Bから3倍超）。年間$1M以上を支出する法人顧客は1,000社超（2月から倍増）。Mizuhoアナリストは、BroadcomのAnthropic向けAI売上を2026年$210億、2027年$420億と推計。

**根拠**: $30Bの売上ランレートは、OpenAIの月間売上$2B（年換算$24B）を上回る水準。3.5GWの追加計算資源は原発2〜3基分に相当し、Anthropic単体で確保する量としては異例。法人顧客1,000社超の倍増ペースは、エンタープライズ市場でのClaude採用が加速していることを示す。

**影響**: AI基盤企業の計算資源確保競争が「兆円単位」のインフラ投資戦に移行した。この規模の投資を回収するには法人顧客からの継続課金が前提であり、API料金の値下げ余地は限定的。中小のAIスタートアップが同等のインフラを確保することは事実上不可能になりつつある。

**行動指針**: Claude APIを業務利用している場合、サービス継続性のリスクは低い（財務基盤は盤石）。一方で、この規模のインフラ投資は最終的にAPI料金に反映される可能性がある。コスト管理の観点から、利用量モニタリングとバジェットアラートの設定を確認しておく。

- https://techcrunch.com/2026/04/07/anthropic-compute-deal-google-broadcom-tpus/
- https://www.bloomberg.com/news/articles/2026-04-06/broadcom-confirms-deal-to-ship-google-tpu-chips-to-anthropic
- https://qz.com/anthropic-google-broadcom-tpu-compute-deal-revenue-040726

### 3. OpenAI・Anthropic・Google が中国によるモデル蒸留対策で異例の連携 — 競合3社が「防衛」で手を組んだ意味

**事実**: OpenAI・Anthropic・Google の3社がFrontier Model Forum経由で、中国企業による不正な「蒸留」（大規模モデルの出力で小型モデルを訓練する手法）の検知・対策で情報共有を開始。米政府は不正コピーによる損害を年間数十億ドルと推計。利用規約違反の検知体制を強化。

**根拠**: 通常は激しく競合する3社が共同で対策に動いたこと自体が、蒸留による損失の深刻さを示している。DeepSeek V4がHuawei Ascend 950PRチップで動作し$0.30/MTokの価格を実現している背景にも、蒸留を含む効率的な訓練手法がある可能性が指摘されている。

**影響**: API利用規約の厳格化（出力の二次利用制限、異常な利用パターンの検知強化）が進む可能性がある。合法的な用途（評価用のモデル間比較、RAG用のエンベディング生成等）にも影響が及ぶ可能性は低いが、大量出力の自動取得には注意が必要。

**行動指針**: 自社のAPI利用が利用規約に準拠していることを確認する。特に、モデル出力をデータセットとして蓄積・再利用している場合は規約を再読する。直接的な行動変更は不要だが、今後の規約改定には注意を払う。経過観察。

- https://www.japantimes.co.jp/business/2026/04/07/tech/openai-anthropic-google-china-copy/
- https://www.businesstoday.in/technology/story/openai-anthropic-google-team-up-to-stop-chinese-ai-distillation-threat-524367-2026-04-07

---

## カテゴリ別まとめ

### Anthropic / Claude

- **Claude Code v2.1.94**: Amazon Bedrock Mantle対応、デフォルトeffortレベルをmedium→highに変更、Slack MCP改善、429レートリミット時のスタック問題修正、CJKテキスト描画修正等
  - https://code.claude.com/docs/en/changelog

- **Claude API 1Mコンテキストベータ 4/30終了**: Sonnet 4.5/4の`context-1m-2025-08-07`ヘッダーは4/30で終了。継続にはSonnet 4.6またはOpus 4.6への移行が必要
  - https://platform.claude.com/docs/en/release-notes/overview

### Microsoft 365 Copilot / Power Platform

- **Copilot Chat 4/15仕様変更まで残り1週間**: 2,000人以上の組織はWord/Excel/PowerPoint/OneNoteからCopilot Chat完全削除。2,000人未満は「標準アクセス」に格下げ。Outlookは影響なし
  - https://kurtsh.com/2026/04/05/info-copilot-chat-behavior-changes-for-microsoft-365-users-coming-april-15-2026/

- **M365 Copilot 4月新機能ロールアウト中**: Copilot Search（SharePointソース指定）、Researcherエージェント新出力形式（PPT/PDF/インフォグラフィック/Audio）、PowerPoint Agent Mode、Designer画像生成強化
  - https://learn.microsoft.com/en-us/copilot/microsoft-365/release-notes

- **M365 Copilot Developer Portal強化**: エージェントマニフェスト管理、Gong/GitHub/Mondayコネクタ簡易OAuth、Agent Blueprint対応
  - https://releasebot.io/updates/microsoft

- **Power Apps Generative Pages GA**: GitHub CopilotやClaude Codeから直接Dataverse接続でGenerative Pages作成・編集可能に
  - https://mwpro.co.uk/blog/2026/04/02/power-apps-build-generative-pages-using-external-code-generations-tools-mc1268500/

- **M365 E7 Frontier Suite 5/1 CSP販売開始**: E5+Entra Suite+Copilot+Agent 365統合。$99/user/月
  - https://learn.microsoft.com/en-us/partner-center/announcements/2026-april

- **Purview Data Security Investigations**: AI個人データ自動特定機能を4月下旬追加
  - https://mc.merill.net/message/MC1266016

### OpenAI

- **「Intelligence Age」産業政策提言**: 週32時間・給与維持の週4日勤務パイロット、AI企業への公共資産ファンド、ロボット税・キャピタルゲイン増税、介護・教育・医療分野への就労支援を提案
  - https://techcrunch.com/2026/04/06/openais-vision-for-the-ai-economy-public-wealth-funds-robot-taxes-and-a-four-day-work-week/

- **OpenAI Safety Fellowship新設**: 2026年9月〜2027年2月の6ヶ月間、外部研究者向けAI安全性・アラインメント研究プログラム
  - https://openai.com/news/

- **New Yorker: Sam Altman氏の調査記事公開**: $1,220億調達完了・IPO準備中のタイミングで「操作と透明性の欠如のパターン」を指摘
  - https://www.cnn.com/2026/04/07/business/video/the-new-yorker-investigates-sam-altmans-alleged-deceptions-at-openai-vrtc

### Google

- **Gemma 4 AI Edge Gallery がApp Store Top 10入り**: iOS版配信後、生産性カテゴリ#8に急浮上。Thinking Mode・Agent Skills対応のオンデバイスAI
  - https://officechai.com/ai/google-ai-edge-gallery-breaks-into-top-10-on-app-store-as-users-try-out-on-device-gemma-4-model/

### エンタープライズ・ツール

- **Cathay Financial（台湾最大級金融持株）がOpenAIと大規模提携**: ChatGPT Enterprise導入、コーポレートバンキング・保険向けエージェンティックAI開発
  - https://www.prnewswire.com/apac/news-releases/cathay-fhc-advances-ai-adoption-across-the-group-with-openai-302735655.html

- **Voice AIの技術課題が一挙解決**: Nvidia・Inworld・FlashLabs・Alibaba Qwen・Google DeepMindが相次いでVoice AIモデル公開。レイテンシ・流暢性・効率・感情表現の4大課題を実質解決
  - https://venturebeat.com/orchestration/everything-in-voice-ai-just-changed-how-enterprise-ai-builders-can-benefit

- **Devin PWA対応**: Chrome/Edge/iOS Safariからインストール可能に。ブラウザタブにステータスドット表示
  - https://docs.devin.ai/release-notes/overview

### ハードウェア・インフラ

- **Tiny Corp exabox**: 20ftコンテナ型AIスパコン、720基RDNA5 GPUs、約1 EXAFLOP、$10Mで予約開始。2027年出荷予定
  - https://www.phoronix.com/news/Tiny-Corp-Exabox-Pre-Order

---

## 直近の注目予定

- **4/15**: Copilot Chat 仕様変更適用（Basic/Premium 二層化）
- **4/15**: Power Platform & Copilot Studio アップデートイベント（9:00 AM PDT）
- **4/20**: Teams Pre-Day（Orlando）
- **4/21-23**: M365 Community Conference（Orlando）
- **4/24**: GitHub Copilot Free/Pro データ学習利用開始
- **4/26**: Sora アプリ終了
- **4/30**: Claude 1M コンテキストベータ終了（Sonnet 4.5/4）
- **5/1**: M365 E7 Frontier Suite GA / Agent 365 GA

---

## 改善メモ

### 01_ai-news-Master
- 全12ソース中11ソースでWebFetch 403（4日連続）。WebSearchフォールバックで取得成功
- daily-sources.md の取得方法をWebSearch優先に変更することを強く推奨

### 02_ai-news-Copilot
- learn.microsoft.com 配下でWebFetch 403継続（6日連続）。daily-sources.md の取得方法をWebSearchプライマリに更新することを強く推奨
- mc.merill.net / supersimple365.com: WebFetch 403 → WebSearch経由で取得成功

### 03_ai-news-industry
- 全RSSフィードがWebFetch 403。全ソースWebSearchフォールバックで取得
- WebSearch主体の取得フローへの変更を推奨

### 共通
- 3ソースすべてでWebFetch 403率が極めて高い状態が数日間継続。全ソースのdaily-sources.mdでWebSearchをプライマリに一括変更すべき段階
