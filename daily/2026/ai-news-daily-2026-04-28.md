# AI News Daily - 2026-04-28

## 今日のハイライト

### 1. 中国、MetaによるManus（$2B）買収を阻止 — AI地政学がM&Aを直接支配する時代に

- **事実**: 中国商務部がMetaによるシンガポール拠点AIエージェント企業Manusの$2B買収を正式にブロックした。Manusは中国にルーツを持ち、輸出管理・技術輸出入に関する法規制への適合性を理由に不許可と判断された。
- **根拠**: 米中間のAI規制がチップ輸出規制から一段階進み、M&A自体を阻止する初の大型事例となった。AI企業の「国籍」がバリュエーションや買収可能性を左右する構造が現実になっている。
- **影響**: AIスタートアップの買収・出資において、技術の出自（どの国で開発されたか）がデューデリジェンスの必須項目になる。中国ルーツの技術を持つ企業への投資・買収は、米中双方の規制リスクを織り込む必要がある。
- **行動指針**: 直接的な行動は不要。ただし、AIツール選定時に「開発元の国籍・データ所在地」を評価軸に入れておくと、将来の規制変更による利用停止リスクを事前に回避できる。経過観察。
- https://www.cnbc.com/2026/04/27/meta-manus-china-blocks-acquisition-ai-startup.html

### 2. Microsoft-OpenAI提携を再構築 — Azure独占が終了し、マルチクラウド時代へ

- **事実**: MicrosoftとOpenAIが提携条件を改定。OpenAIは全プロダクトを任意のクラウドプロバイダーで提供可能になり、MicrosoftはOpenAIへのレベニューシェア支払いを終了した。
- **根拠**: これまでOpenAIのAPIはAzure経由が原則だったが、AWS・GCPでもChatGPT Enterprise / Workspace Agentsが展開可能になる。Microsoftにとってはレベニューシェア負担の解消、OpenAIにとっては顧客基盤拡大のメリットがある。
- **影響**: エンタープライズAI導入時の「クラウドロックイン」という障壁が下がる。既にAWSやGCPを主力にしている企業がOpenAIモデルを採用しやすくなり、Anthropic（AWS Bedrock）やGoogle（Vertex AI）との直接競合が激化する。
- **行動指針**: マルチクラウド環境でOpenAIモデルを検討中の企業は、AWS/GCPでの提供開始時期と価格体系を注視する。現時点ではAzure経由の既存契約を変更する必要はないが、次回の契約更新時にマルチクラウド選択肢を比較材料に加える。
- https://www.aiandnews.com/blog/april-2026-ai-news/

### 3. Agent 365 / M365 E7 GA まで3日（5/1） — Microsoft Copilotのエージェント基盤が本格稼働

- **事実**: Agent 365（$15/user/月）とM365 E7 Frontier Suite（$99/user/月）のGAが5/1に迫る。GA時点ではライセンスユーザー代理のエージェントのみ対象。E7はE5 + Copilot + Entra Suite + Agent 365のバンドルで単品合計$117に対し約15%割引。
- **根拠**: 同時にCopilot Studioに実験モデル（Grok 4.1 Fast / GPT-5.3 Thinking / GPT-5.4 Instant）が追加され、マルチエージェントオーケストレーション（Fabric / M365 Agents SDK / A2A）もGA。Word/Excel/PowerPointのアジェンティック機能GA後、Wordエンゲージメント52%増・Excel 67%増という初期指標が出ている。
- **影響**: M365を導入済みの企業は、追加$15/userでエージェント機能を利用可能になる。既存のCopilotライセンスとの棲み分け・追加コストの正当化が導入判断のポイントになる。
- **行動指針**: 5/1のGA後すぐに全社展開する必要はない。まずパイロットチーム（5-10名）でAgent 365の実効性を検証し、ROIが見合うユースケースを特定してから拡大する。E7バンドルはE5+各単品を既に持つ企業には割高になるケースもあるため、既存ライセンス構成との比較が必要。
- https://licensing.guide/may-1-ga-is-not-yet-the-final-frontier-for-agent-365/
- https://samexpert.com/agent-365/

---

## カテゴリ別まとめ

### Anthropic / Claude

- **Claude Opus 4.7 リリース（4/16）**: SWE-bench Verified 87.6%（+7pt）、SWE-bench Pro 64.3%でGPT-5.4・Gemini超え。ビジョン解像度3.3倍向上、自己検証機能搭載。新`xhigh`エフォートレベル追加。価格はOpus 4.6と同じ$5/$25 per MTok
  - https://www.cnbc.com/2026/04/16/anthropic-claude-opus-4-7-model-mythos.html
- **Claude Code v2.1.111〜v2.1.120（9+リリース）**: Opus 4.7+xhighエフォート、Auto mode GA、ネイティブバイナリ化、Vim visual mode、カスタムテーマ、MCP tool hooks、`/ultrareview`、設定永続化。ただしv2.1.119/120で自動更新破損・サイレントモデルスワップ等8件のリグレッション発生。安定版はv2.1.117
  - https://code.claude.com/docs/en/changelog
  - https://github.com/anthropics/claude-code/releases
- **Google、Anthropicに最大$40B投資（4/24）**: $10B確定＋$30B追加オプション。計算基盤の大幅拡張を支援
  - https://www.cnbc.com/2026/04/24/google-to-invest-up-to-40-billion-in-anthropic-as-search-giant-spreads-its-ai-bets.html

### OpenAI

- **GPT-5.5 リリース（4/23-24）**: エージェンティックコーディング・Computer Use・Deep Research強化。1Mコンテキスト対応。API価格$5/$30 per MTok。ChatGPT Plus/Pro/Business/Enterpriseで利用可能
  - https://openai.com/index/introducing-gpt-5-5/
- **GPT-5.4 mini / nano リリース**: GPT-5.4クラスの能力を高速・低コストで提供。miniは高ボリュームワークロード向け、nanoは速度・コスト重視
  - https://releasebot.io/updates/openai
- **ChatGPT for Clinicians（4/23）**: 米国の医療従事者向け無料臨床AI。7,000会話テストで99.6%が正確・安全と評価
  - https://openai.com/index/making-chatgpt-better-for-clinicians/
- **Microsoft-OpenAI提携再構築**: Azure独占終了、マルチクラウド展開可能に（ハイライト参照）
- **ChatGPT広告開始**: 無料/Goプラン対象（豪・NZ・加）。Plus以上は広告なし
- **Sora アプリ版停止（4/26）**: API版は9/24まで

### Google

- **Google Cloud Next '26（4/22-24）— 260件発表**: Gemini Enterprise Agent Platform、TPU 8t（第8世代）、Virgoネットワーク、Agentic Data Cloud、Workspace Intelligence、$750Mパートナー投資
  - https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/next-2026/
- **Deep Research / Deep Research Max（4/21）**: Gemini 3.1 Pro搭載の自律リサーチエージェント。MCP対応、FactSet/S&P/PitchBookとMCPサーバー連携
  - https://blog.google/innovation-and-ai/models-and-research/gemini-models/next-generation-gemini-deep-research/
- **EU、GoogleにAIサービスへのアクセス開放を指導**: DMAに基づく規制がAIプラットフォーム層に拡大
  - https://www.usnews.com/news/top-news/articles/2026-04-27/google-gets-pointers-from-eu-regulators-on-helping-ai-rivals-access-services
- **Gemini 3 Pro 一般提供 / Gemini for Mac / AI Overviews in Drive GA / Docs AIライティング**

### Microsoft 365 / Copilot

- **Agent 365 / M365 E7 GA（5/1）**: ハイライト参照
- **Copilot アジェンティック機能 GA エンゲージメント指標**: Word 52%増、Excel 67%増、PowerPoint新規ユーザーリテンション36%改善
  - https://www.microsoft.com/en-us/microsoft-365/blog/2026/04/22/copilots-agentic-capabilities-in-word-excel-and-powerpoint-are-generally-available/
- **Copilot Studio 実験モデル追加**: Grok 4.1 Fast / GPT-5.3 Thinking / GPT-5.4 Instant。マルチエージェントオーケストレーションGA
  - https://www.microsoft.com/en-us/microsoft-copilot/blog/copilot-studio/new-and-improved-multi-agent-orchestration-connected-experiences-and-faster-prompt-iteration/
- **Power BI April 2026**: モバイル In-report Copilot（オープンエンド質問・音声入力対応）、Direct Lake計算列Preview
  - https://powerbi.microsoft.com/en-us/blog/power-bi-april-2026-feature-summary/

### 開発ツール

- **Cursor 3.2（4/24）**: `/multitask`で非同期サブエージェント並列化、Self-Hosted Cloud Agents（プライベートネットワーク内実行）、Canvases、大規模編集フレーム落ち約87%削減
  - https://cursor.com/changelog
- **Cognition（Devin）$25B評価額での資金調達協議継続**: PWA対応、新料金体系運用中
  - https://siliconangle.com/2026/04/23/cognition-creator-ai-software-engineer-devin-talks-raise-hundreds-millions-25b-valuation/
- **Devin アップデート（4/15-22）**: SSO Connection Picker、MCP OAuthトークン管理、Repository Permissions分離、v3 API正式版
  - https://docs.devin.ai/release-notes/2026
- **Microsoft Agent Framework 1.0**: 安定API、長期サポート、フルMCP対応、ブラウザベースDevUI

### 市場・研究

- **AIソフトウェアプラットフォーム市場: 2026年$1,069億（前年比+34.7%）**: 2030年には$2,965.7B（CAGR 29.1%）見通し
  - https://www.globenewswire.com/news-release/2026/04/27/3281500/28124/en/artificial-intelligence-software-platforms-global-market-report-2026-google-microsoft-aws-tencent-and-ibm-led-the-79-38-billion-market-in-2025.html
- **MIT EnergAIzer**: AIワークロードの消費電力を高速推定する新手法。データセンターが2028年までに米国総電力12%消費の見通しに対応
  - https://news.mit.edu/2026/faster-way-to-estimate-ai-power-consumption-0427
- **ICLR 2026閉幕（4/24-28、リオデジャネイロ）**: エージェンティックAI・長文脈推論・安全性評価が主要テーマ。企業研究者の発表比率が過去最高

---

## 直近の注目予定

- **5/1**: Agent 365 GA（$15/user/月）、M365 E7 Frontier Suite GA（$99/user/月）
- **5/1**: Power Apps MCP Server 移行期限
- **5/4**: Power Apps Agent Feed GA
- **5/16**: Copilot ライセンス変更延期後の新期限（Word/Excel/PPTでのCopilot Chat制限）
- **9/24**: Sora API版終了

---

## 改善メモ

- [Master] 前回チェックから13日空き差分が大量。スケジュールタスクの正常動作を要確認
- [Master/Copilot/Industry共通] WebFetch 403が常態化。WebSearchをプライマリ取得方法に恒久変更することを強く推奨（複数ソースから同一提案が継続中）
- [Industry] Microsoft-OpenAI提携再構築の公式プレスリリースURLが未確認。複数メディアの報道ベース
- [Industry] China blocks Meta-Manus — AI地政学関連ニュースのキャッチ率を上げるため、WebSearchクエリに「AI acquisition blocked regulation」等を追加検討
- [Master] Sora終了（アプリ版4/26停止）を確認。daily-sources.mdからSora関連の監視は不要
- [Master] Google Cloud Next '26関連の情報が多量。次回から独立セクションにする検討
