# AI News Daily Summary - 2026-04-13

## 今日のハイライト

### 1. GitHub Copilot、4/24からFree/Pro/Pro+ユーザーのインタラクションデータをAI訓練に使用開始

**事実**: GitHubが3/25に発表したプライバシーポリシー変更が4/24に発効する。Free・Pro・Pro+プランのCopilotユーザーのインタラクションデータ（受け入れた提案、コードスニペット、カーソル周辺コンテキスト、ファイル名、リポジトリ構造、フィードバック等）がデフォルトでAIモデル訓練に使用される。オプトアウトは手動設定が必要。Business/Enterpriseプランは対象外。

**根拠**: デフォルトオプトイン＋手動オプトアウトという設計は、過去のLinkedIn・Facebook等のデータ利用拡大と同じパターン。GitHubのMAU 1.5億人超のうちFree/Proが大多数を占めるため、影響範囲はCopilot利用者の80%超と推定される。GDPR準拠性（正当な利益の根拠が曖昧）・OSS貢献者のIP懸念から、EUのDPA調査や訴訟リスクが今後浮上する可能性がある。

**影響**: Copilotを業務で使っているFree/Proユーザーは、自分のコード・操作パターンがモデル訓練データに含まれる。企業の非公開コードが含まれるリポジトリでの利用は特にリスクが高い。一方、Business/Enterpriseプランは除外されているため、組織利用の場合はプランの確認が最優先。

**行動指針**: **4/24までに `/settings/copilot/features` でオプトアウト設定を確認・変更する**。業務利用なら即対応。個人プロジェクトでも非公開コードがある場合は同様。Business/Enterpriseユーザーは対象外のため対応不要だが、チーム内にFree/Proアカウントで併用している人がいないか確認する。

- https://github.blog/news-insights/company-news/updates-to-github-copilot-interaction-data-usage-policy/
- https://www.infoq.com/news/2026/04/github-copilot-training-data/
- https://smartscope.blog/en/generative-ai/github-copilot/github-copilot-data-training-policy-2026/

### 2. Copilot Chat 4/15仕様変更まであと2日 — Office内アクセス制限の発効

**事実**: 4月15日から、2,000席以上の組織ではCopilot Chat（Basic）がWord/Excel/PowerPoint/OneNoteから削除される。有料M365 Copilotライセンスなしではこれらアプリ内のCopilotボタン・サイドパネルが非表示に。ラベルも「Copilot Chat (Basic)」「M365 Copilot (Premium)」に分離。Outlookのメール・カレンダー推論は引き続き利用可能。2,000席未満の組織は混雑時の品質低下（「標準アクセス」制限）のみ。

**根拠**: Microsoftは2026年初頭から「無料Copilot Chatの利用範囲を段階的に縮小し有料M365 Copilotへの移行を促進する」方針を明確にしており、今回はその最大のマイルストーン。2,000席以上の大企業がまず対象になるのは、エンタープライズ契約でのM365 Copilotアップセルが主目的であることを示す。

**影響**: 2,000席以上の組織で有料Copilotライセンスなしの場合、4/15以降にWord/Excel/PowerPointでAIアシスタントが突然消える。現在これらを業務に組み込んでいる場合、代替手段（ブラウザ版Copilot Chat、またはライセンス購入）を事前に確保しないと業務フローが中断する。

**行動指針**: **自組織の席数と現在のライセンス状況を4/14までに確認する**。2,000席以上でM365 Copilotライセンス未購入の場合、ブラウザ版Copilot Chatへの一時的な切り替え手順をチームに周知する。ライセンス購入判断は仕様変更後の実影響を見てからでも遅くない。

- https://kurtsh.com/2026/04/05/info-copilot-chat-behavior-changes-for-microsoft-365-users-coming-april-15-2026/
- https://office-watch.com/2026/microsoft-removes-copilot-chat-word-excel-powerpoint-april-2026/

### 3. Copilot StudioでChatGPT-5・Claude全モデルがグローバルGA — マルチモデル選択が標準化

**事実**: Copilot StudioでChatGPT-5が全リージョン（GCC除く）でGA。Claude Sonnet 4.5、Claude Sonnet 4.6、Claude Opusも同様にグローバルGA。従来は米国限定の有料実験プレビューだったが、全パブリックリージョンに拡大。同時にマルチエージェントオーケストレーション関連（Microsoft Fabric統合、M365 Agents SDKオーケストレーション、A2Aプロトコル）もGA。

**根拠**: Copilot Studioは従来OpenAIモデル一択だったが、Claude全モデル＋GPT-5のグローバルGAにより「モデル選択」がCopilot Studioの標準ワークフローになった。4/11のM365 Copilot Researcher Critique Mode（GPT生成→Claude検証）と合わせ、Microsoft自身がマルチモデル前提のアーキテクチャに完全移行したことを示す。

**影響**: Copilot Studioでエージェントを構築している組織は、タスクに応じてモデルを使い分けられるようになった。コーディングタスクにはClaude、推論にはGPT-5、といった最適化が可能。Fabric統合によりエンタープライズデータへのエージェント直接アクセスも実現し、データパイプラインの簡素化が見込める。

**行動指針**: Copilot Studioでエージェントを運用中なら、既存エージェントのモデルをClaude Sonnet 4.6に切り替えてA/Bテストを実施するのが最もROIが高い。マルチエージェントオーケストレーションは既存エージェントの拡張フェーズで検討すればよく、今すぐの着手は不要。

- https://learn.microsoft.com/en-us/microsoft-copilot-studio/whats-new
- https://learn.microsoft.com/en-us/power-platform/release-plan/2026wave1/microsoft-copilot-studio/
- https://www.microsoft.com/en-us/microsoft-copilot/blog/copilot-studio/new-and-improved-multi-agent-orchestration-connected-experiences-and-faster-prompt-iteration/

---

## カテゴリ別まとめ

### Anthropic / Claude

- **HumanX「Claude Mania」続報 — TechCrunch・CNBC報道**: HumanX（4/6-9, SF）事後報道が相次ぐ。6,500人超の参加者の間でClaude CodeがOpenAIを上回る話題の中心。Glean CEOは「Claude Maniaは宗教レベル」と表現。Claude Code ARRは$2.5B超（2026年2月時点）
  - https://techcrunch.com/2026/04/12/at-the-humanx-conference-everyone-was-talking-about-claude/
  - https://www.cnbc.com/2026/04/11/vibe-check-from-ai-industry-humanx-anthropic-is-talk-of-the-town.html

- **Mythos / Project Glasswing 国際報道拡大**: RTE.ie（アイルランド公共放送）が「Fail Safe: Why Anthropic won't release its new AI model」と題し、Mythosのゼロデイ脆弱性自律発見能力と一般公開しない判断を詳報。FreeBSD 17年来のRCE（CVE-2026-4747）自律発見事例が注目を集める
  - https://www.rte.ie/news/business/2026/0412/1567631-anthropic-claude-ai/
  - https://red.anthropic.com/2026/mythos-preview/

- **MCP 97Mインストール突破**: 2025年11月ローンチ時の約200万から16ヶ月で4,750%成長。5,800以上のコミュニティ・エンタープライズサーバーに拡大。Linux Foundation傘下のAgentic AI Foundationに寄贈済み
  - https://www.affiliatebooster.com/anthropic-mcp-protocol-97-million-installs/

- **CoreWeave × Anthropic 複数年契約**: Claudeモデルの本番稼働をCoreWeaveのGPUインフラで支える。前日のMeta $21B契約と合わせ48時間で2件のランドマーク契約。CoreWeave株1日で11%上昇
  - https://www.cnbc.com/2026/04/10/coreweave-anthropic-claude-ai-deal.html
  - https://investors.coreweave.com/news/news-details/2026/CoreWeave-Announces-Multi-Year-Agreement-With-Anthropic/default.aspx

### OpenAI

- **ARR $25B突破、$122B調達完了、IPO準備**: 2026年2月末時点でARR $25B（前年末$21.4Bから17%増）。3/31に史上最大の民間資金調達$122B（評価額$852B）をクローズ。Amazon $50B、NVIDIA $30B、SoftBank $30B。Sam AltmanはQ4 2026 IPOを志向
  - https://finance.yahoo.com/news/openai-tops-25-billion-annualized-033836274.html
  - https://nerdleveltech.com/openai-122-billion-funding-round-ipo-superapp

### Microsoft / Copilot

- **Copilot Tuning / Authoritative Sources 4月展開**: Copilot Tuningが5,000席以上のFrontierライセンス向けに展開開始。組織固有データでCopilot応答をチューニング可能に。Authoritative SourcesでSharePoint Onlineサイトを権威的コンテンツとして指定可能
  - https://techcommunity.microsoft.com/blog/microsoft365copilotblog/what%E2%80%99s-new-in-microsoft-365-copilot--march-2026/4506322

- **Power Platform April 2026 Feature Update**: Generative Pages GA（GitHub Copilot CLI等でカスタムページ構築）、カスタムテーマGA（Fluent 2デザイン）、Power Apps→M365 Copilot MCP統合、Power Platform Monitor アラートGA
  - https://www.microsoft.com/en-us/power-platform/blog/2026/04/09/whats-new-in-power-platform-april-2026-feature-update/

- **スケジュールプロンプト編集・Scatter画像エフェクト**: スケジュールプロンプトの直接編集機能追加。Scatter画像エフェクトがCopilot Chatと作成モジュールに追加
  - https://learn.microsoft.com/en-us/copilot/microsoft-365/release-notes

### Google

- **NotebookLMをGeminiアプリに完全統合**: PDF・ドキュメント・URL・YouTube動画をアップロードし検索可能なナレッジベースを構築。GeminiアプリとNotebookLM間でノートブックが自動同期。AI Ultra/Pro/Plusから順次提供、無料ユーザーにも拡大予定
  - https://blog.google/innovation-and-ai/products/gemini-app/notebooks-gemini-notebooklm/
  - https://9to5google.com/2026/04/08/gemini-app-notebooks/

### AIインフラ / エコシステム

- **ThinkLabs AI: Nvidia出資で$28M調達**: 物理法則をAIに組み込んだ電力グリッドモデリングで、従来数週間〜数ヶ月のスタディを数分に圧縮
  - https://venturebeat.com/technology/nvidia-backed-thinklabs-ai-raises-28m/

### 市場データ

- **Stanford HAI AI Index 2026 詳細解説イベント**: 本日12:00-13:00（米国時間）開催。47カ国のAI規制を体系分析（施行メカニズム確立は12カ国のみ）。イベント後に主要データポイント反映予定
  - https://hai.stanford.edu/events/inside-the-2026-ai-index-report

---

## 直近の注目予定

| 日付 | イベント |
|------|---------|
| 4/15 | Copilot Chat仕様変更発効 / Power Platform & Copilot Studio アップデートイベント（9AM PDT） |
| 4/17 | Anthropic OpenClaw 移行クレジット期限 |
| 4/19 | Claude Haiku 3 非推奨（リタイア） |
| 4/20 | Security Copilot for M365 E5 段階展開開始（〜6/30） |
| 4/21 | Power Automate Process License共有 GA |
| 4/21-23 | M365 Community Conference（Orlando） |
| 4/23 | Google Drive限定アクセス自動移行開始 |
| 4/24 | GitHub Copilot データ訓練ポリシー変更発効 |
| 4/30 | Alibaba HappyHorse-1.0 API提供開始予定 / 1Mコンテキストベータ終了 |
| 5/1 | M365 E7 Frontier Suite GA / Agent 365 GA |

---

## 改善メモ

- 01_ai-news-Master の4/13ダイジェストが未生成。Copilot（02）+ Industry（03）の2ソースのみで本サマリーを作成
- Copilotソース: WebFetch 403継続（Copilot Studio What's New / M365 Release Notes / Microsoft Copilot Blog / mc.merill.net / Power Platform Released Versions / Tech Community Blog）。全てWebSearch経由で取得
- Industryソース: 全RSSフィード403が7日以上連続。`daily-sources.md` の取得方法欄を `WebSearch` に変更することを強く推奨（7回目の提案）
- GitHub Copilot データ訓練ポリシー変更発効日（4/24）を注目予定に追加
- Stanford HAI AI Index 2026イベントが本日開催。明日以降のダイジェストでレポートの主要定量データを詳細反映予定
