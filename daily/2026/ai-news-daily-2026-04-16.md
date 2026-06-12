# AI News Daily - 2026-04-16

## 今日のハイライト

### 1. GitHub Copilot データ学習ポリシー変更 — 4/24オプトアウト期限（残り8日）

- **事実**: 4/24以降、GitHub Copilot Free / Pro / Pro+ ユーザーのインタラクションデータ（プロンプト・出力・コードスニペット・ファイル名等）がAIモデル学習に使用される。Business / Enterpriseは対象外。
- **根拠**: 以前オプトアウト済みの設定は引き継がれるが、未設定ユーザーは自動的に学習対象。Settings > Copilot > Features から設定変更可能。4/10には無料トライアルの不正利用急増で既に新規Pro トライアルが停止されている状況。
- **影響**: 個人開発のPro/Pro+ ユーザーが業務コードや機密ロジックをCopilotで扱っている場合、そのまま放置すると学習素材に流れる。一方Business / Enterpriseライセンスなら作業は不要。
- **行動指針**: Pro / Pro+ユーザーは今週中に Settings > Copilot > Features でオプトアウトを確認する。Business / Enterprise ユーザーは作業不要（経過観察）。
- https://github.blog/news-insights/company-news/updates-to-github-copilot-interaction-data-usage-policy/

### 2. Anthropic $800B評価額報道＋取締役体制強化 — IPO準備の本格化

- **事実**: Bloombergが4/14、投資家から最大$800B評価でのラウンド提案があったと報道。同日、Novartis CEOのVas Narasimhan氏が取締役就任、Long-Term Benefit Trust指名取締役が過半数に。
- **根拠**: 2月の$350B（プレマネー）から倍増以上で、OpenAI級の評価帯に到達。Trustによるガバナンス強化はIPO前の典型的な体制整備。同時期にMythos Preview（セキュリティ用途）がAISI評価で専門サイバータスク73%成功と技術的優位も示す。
- **影響**: Claude/Claude Code前提の業務設計は当面継続可能性が高い一方、IPO後はポリシー変更速度が上がる可能性（公開企業の四半期プレッシャー）。代替としてのGPT-5.5 / Gemini / オープンソース（MiniMax M2.7、Gemma 4）の比較軸を持っておくと判断スピードが落ちない。
- **行動指針**: Claudeへの依存度が高い業務フローを棚卸しし、代替モデルへの切り替え手順（最低でもGPT-5.4と1つのOSSモデル）をドライランしておく。急ぐ必要はないが、半期に一度は実施する。
- https://www.bloomberg.com/news/articles/2026-04-14/anthropic-attracts-investor-offers-at-a-800-billion-valuation
- https://www.anthropic.com/news/narasimhan-board

### 3. Power Apps × M365 Copilot 統合新段階 — App Skills GA・MCP Server Public Preview

- **事実**: 4/15、Power Apps ブログで M365 Copilot in model-driven apps のGA、App Skills のGA、Power Apps MCP Server の Public Preview を発表。Agent Feed は5/4 GA、5/1以降 MCP Server 経由タスクのみサポート。
- **根拠**: これで業務アプリの機能が外部エージェント（Copilot Studio / M365 Copilot / サードパーティ）から MCP 経由で呼び出し可能になる。Agent Feed はリスクレベル別の承認閾値設定に対応。M365 Agent Store も同週Adobe Express / Figma / Miro / monday.com等と拡充。
- **影響**: 社内Power Appsを「人間が開く画面」から「エージェントが呼ぶAPI」に格上げできる。ただし5/1の Agent Feed 移行期限を過ぎるとMCP Server経由以外のタスクがAgent Feedで監視できなくなる—既存のエージェント運用を持つ組織は対応が必要。
- **行動指針**: 現状Power Appsを業務導入済みの組織は、（a）既存エージェントのAgent Feed対応状況を4月内に棚卸し、（b）MCP Server経由の移行計画を5/1までに策定。未導入組織はまだ触る必要はない（経過観察）。
- https://www.microsoft.com/en-us/power-platform/blog/power-apps/public-preview-power-apps-mcp-and-enhanced-agent-feed-for-your-business-applications/

---

## カテゴリ別まとめ

### Anthropic / Claude

- **Claude Code v2.1.110（4/15）**: `/tui`コマンド（フリッカーフリー描画）、`autoScrollEnabled`、`--resume`/`--continue`でスケジュールタスク復活、Bash toolタイムアウト強制、SDK/headless向け分散トレースリンク
  - https://code.claude.com/docs/en/changelog
- **Claude Code v2.1.108〜v2.1.109（4/14-15）**: `ENABLE_PROMPT_CACHING_1H`（1時間キャッシュ、Bedrock/Vertex/Foundry対応）、`/recap`コマンド、Skill toolからビルトインスラッシュコマンド起動可能に
  - https://code.claude.com/docs/en/changelog
- **Claude.ai 大規模障害（4/15）**: 約3時間ダウン（10:53 AM ET確認→1:42 PM ET復旧）、15,000人以上に影響
  - https://status.claude.com/history
- **Anthropic 評価額 $800B 報道（4/14）** / **Vas Narasimhan取締役就任**（Novartis CEO、Trust指名過半数化）
  - https://www.bloomberg.com/news/articles/2026-04-14/anthropic-attracts-investor-offers-at-a-800-billion-valuation
  - https://www.anthropic.com/news/narasimhan-board
- **Claude Mythos Preview続報**: 英国AISI評価で専門サイバータスク73%成功。OpenBSD 27年/FFmpeg 16年の脆弱性を自律発見。一般公開見送り（約7年ぶりの安全上非公開事例）
  - https://www.aisi.gov.uk/blog/our-evaluation-of-claude-mythos-previews-cyber-capabilities
- **廃止予告**: Claude Haiku 3（4/19）、Claude Sonnet 4 / Opus 4（6/15 API）

### OpenAI

- **GPT-5.5 "Spud" リリース近づく**: Polymarket 4月中確率78%、4/23に63%コンビクション。Sam Altman「経済を加速させうる」
  - https://polymarket.com/event/gpt-5pt5-released-on/will-gpt-5pt5-be-released-on-april-30-2026
- **GPT-5.4-Cyber（4/14）**: サイバーセキュリティ特化ファインチューン。Trusted Access for Cyber（TAC）で数千人規模に展開
  - https://thehackernews.com/2026/04/openai-launches-gpt-54-cyber-with.html
- **ChatGPT 新統合アプリ**: Box、Notion、Linear、Dropbox（書き込み機能含む）
- **Codex Realtime V2**: バックグラウンドエージェント進捗ストリーミング、TUI hookステータス更新
- **ChatGPT広告事業予測**: 2026年$2.5B → 2030年$100B（Axios 4/9）。無料ティア広告テスト開始6週で年換算$100M突破、600社以上出稿
  - https://www.axios.com/2026/04/09/openai-100-billion-in-ad-revenue

### Google

- **Personal Intelligence グローバル展開（4/14〜）**: Gemini のGmail/Calendar/Drive/Photos/YouTube/Maps横断パーソナライズ。AI Plus/Pro/Ultra→無料ユーザー順次。EEA・スイス・英国除外、オプトイン方式
  - https://9to5google.com/2026/04/14/gemini-personal-intelligence-global/
- **Gemini in Chrome「Skills」機能**: プロンプトテンプレート化、50+プリセットSkills
  - https://siliconangle.com/2026/04/14/google-adds-reusable-prompts-gemini-chrome/
- **Gemma 4 → AICore Developer Preview**: Android オンデバイス実行、次世代Gemini Nano 4のベース
  - https://android-developers.googleblog.com/2026/04/AI-Core-Developer-Preview.html
- **Gemma 4本体**: 4バリアント（E2B / E4B / 26B MoE / 31B Dense）、Apache 2.0、256K、140言語、Raspberry Pi/Jetson Orin Nanoで動作
  - https://blog.google/innovation-and-ai/technology/developers-tools/gemma-4/

### Microsoft 365 Copilot / Copilot Studio

- **M365 Copilot Agent Store 大幅拡充（4/13）**: Adobe Express、Figma、Miro、monday.com、Optimizely、Box、Coursera、Wix/Base44
  - https://www.microsoft.com/en-us/microsoft-365/blog/2026/04/13/bring-your-everyday-business-apps-into-the-flow-of-work-with-agents-in-microsoft-365-copilot/
- **Copilot in Word — 変更履歴記録対応**: 法務/財務/コンプライアンス向け。Frontier（Office Insiders Beta Channel）で先行
  - https://techcommunity.microsoft.com/blog/microsoft365copilotblog/copilot-in-word-new-capabilities-for-document-workflows/4508974
- **M365 Roadmap更新**: エージェントのTeams共有、Agent Builder→Agent Store投稿、PowerPoint Copilot強化、SharePoint Knowledge Agent、Teams話者言語自動検出
  - https://sharepointstuff.com/2026/04/14/microsoft-roadmap-roundup-13-april-2026/
- **M365 Community Conference（4/21-23）キーノート発表**: Jeff Teper、Ryan Cunningham
  - https://techcommunity.microsoft.com/blog/microsoft_365blog/announcing-the-2026-microsoft-365-community-conference-keynotes/4494714

### Power Platform

- **Power Apps × M365 Copilot統合**: App Skills GA、Power Apps MCP Server Public Preview、Agent Feed 5/4 GA（ハイライト #3 参照）
  - https://www.microsoft.com/en-us/power-platform/blog/power-apps/public-preview-power-apps-mcp-and-enhanced-agent-feed-for-your-business-applications/

### Cursor / Devin

- **Cursor 3.1（4/13）**: Agents Window バグ修正（Network Access Controls、マルチルートhooks、thinkingブロック、キュー再開）、セルフホストCloud Agents対応
  - https://cursor.com/changelog
- **Devin 知識管理・プレイブック**: ナレッジノート CRUD、プレイブック統計表示、スケジュールセッション（定期・ワンタイム）

### GitHub Copilot

- **データ学習ポリシー4/24変更**（ハイライト #1 参照）
  - https://github.blog/news-insights/company-news/updates-to-github-copilot-interaction-data-usage-policy/
- **Pro トライアル一時停止（4/10〜）**: 不正利用急増対応、Free / 有料Pro/Pro+は継続
  - https://github.blog/changelog/2026-04-10-pausing-new-github-copilot-pro-trials/
- **リモートCLIセッション / データレジデンシー**: Web/Mobileから監視・操作、US/EU リージョン対応
  - https://github.com/features/copilot/whats-new

### モデル・技術

- **MiniMax M2.7（4/12 OSS公開）**: 229B MoE、自己進化能力（100ラウンド自律実行で30%性能改善）、SWE-Pro 56.22%（GPT-5.3-Codex同等）。ライセンス事後変更に注意
  - https://www.marktechpost.com/2026/04/12/minimax-just-open-sourced-minimax-m2-7-a-self-evolving-agent-model-that-scores-56-22-on-swe-pro-and-57-0-on-terminal-bench-2/
  - https://decrypt.co/364225/minimax-m27-agent-model-license-change
- **Microsoft MAI 3モデル（4月初旬）**: MAI-Transcribe-1（FLEURS 25言語平均WER 3.8%、Whisper-large-v3超）、MAI-Voice-1、MAI-Image-2
  - https://microsoft.ai/news/today-were-announcing-3-new-world-class-mai-models-available-in-foundry/

### 開発者ツール・プラットフォーム

- **Microsoft Foundry Local GA（4/9）**: ローカルAIランタイム、アプリ同梱可能、OpenAI互換API
  - https://devblogs.microsoft.com/foundry/foundry-local-ga/
- **Cloudflare AIエージェント最適化CLI表明（4/15）**: CDN/Workers/R2/D1をエージェント操作対象に
  - https://www.publickey1.jp/
- **AWS DevOps Agent Azure/オンプレ対応（4/9）**
- **Microsoft Agent Governance Toolkit**: AIエージェント向けOSSセキュリティシールド、10種攻撃ブロック、<0.1msレイテンシ
- **Box Agent**: 自然言語で組織コンテンツ横断操作
- **Visa Intelligent Commerce Connect（4/8）**: AIエージェント決済基盤、4プロトコル対応（Trusted Agent / MPP / ACP / UCP）
  - https://investor.visa.com/news/news-details/2026/Visa-Opens-the-Door-to-AI-Driven-Shopping-for-Businesses-Worldwide/default.aspx

### 調査・レポート

- **Stanford HAI AI Index 2026（4/13）**: 生成AI普及率53%（PC/インターネットより速い）、SWE-bench Verified 60%→ほぼ100%、米中モデル性能差2.7%、米国AI民間投資$285.9B（中国23倍）、組織導入率88%、Transparency Index 58→40低下
  - https://hai.stanford.edu/ai-index/2026-ai-index-report
- **PwC 2026 AI Performance Study（4/13）**: 上位20%企業がAI経済価値の74%を独占、競合比7.2倍の成果。差別化要因は「効率化」ではなく「成長・事業再構築」
  - https://www.pwc.com/gx/en/news-room/press-releases/2026/pwc-2026-ai-performance-study.html
- **IDC Directions 2026（4/9）**: AI累積経済効果2031年$22.5T、転換点は2029年（推論大規模化・エージェント数十億規模）
  - https://www.financialcontent.com/article/accwirecq-2026-4-9-idc-highlights-new-ai-research-at-directions-2026-on-economic-impact-agentic-buyers-and-the-rise-of-ai-agents

### GitHub Trending

- **google/adk-python**（8,200+★）、**meta-llama/llama-stack**（6,400+★）、**openai/codex-cli**（5,800+★）、**block/goose**（4,900+★）、**huggingface/smolagents**（4,100+★）
  - https://github.com/trending

---

## 直近の注目予定

| 日付 | イベント |
|------|---------|
| 4/19 | Claude Haiku 3 API リタイア |
| 4/20 | Security Copilot M365 E5同梱ロールアウト開始 |
| 4/21-23 | Microsoft 365 Community Conference（Orlando） |
| 4/23頃 | GPT-5.5 "Spud" リリース予測（Polymarket） |
| 4/24 | GitHub Copilot データ学習ポリシー変更発効 |
| 4/26 | Sora アプリ版停止 |
| 4/30 | Claude Sonnet 4.5/4 1Mコンテキストbeta終了 |
| 4/30 | Gemini Robotics-ER 1.5 廃止 |
| 4/30 | Google Whisk → Flow 統合 |
| 5/1 | Power Apps Agent Feed — MCP Server移行期限 |
| 5/4 | Power Apps Agent Feed GA |
| 6/15 | Claude Sonnet 4 / Opus 4 API リタイア |

---

## 改善メモ

- 本ダイジェスト（Master）は欠損日（4/13, 4/14）のブランチマージ作業と同時に生成。`.last-check-state.md` の差分検出状態は4/15時点のままのため、一部既報情報との重複あり
- 全ソースWebSearch取得方式で安定動作確認。403復旧時にWebFetchプライマリへ戻すこと
- [Copilot Studio What's New / M365 Copilot Release Notes / mc.merill.net / Power Platform Released Versions / SharePoint Stuff Roadmap Roundup / Tech Community M365 Copilot Blog] 取得失敗（403、WebSearchで成功）— 継続
- 全RSSフィード（Google News RSS / GIGAZINE / The Decoder / VentureBeat / Publickey / hnrss.org / Product Hunt / GitHub Trending RSS）が引き続き403。WebSearchフォールバックで取得
- daily-sources.mdの取得方法をWebSearch優先に変更することを推奨（5回目の提案。rulesファイルへの反映を強く推奨）
