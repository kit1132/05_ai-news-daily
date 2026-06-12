# AI News Daily Summary — 2026-05-28（水）

> 対象ダイジェスト: 3ソース（Master / Copilot / Industry）の `ai-news-2026-05-27.md`

---

## 今日のハイライト

### 1. DeepSeek V4-Pro、75%永久値下げ — API価格戦争の構造的転換点

**事実**: DeepSeek が 5/23 に V4-Pro の API 価格を恒久的に 75% 引き下げた。入力 $0.003625〜/M tokens、出力 $0.87〜/M tokens。長コンテキスト推論で前世代比 1/4 の計算コスト・1/10 のメモリ使用量を実現したことによる構造的値下げであり、一時的なプロモーションではない。100 万トークンのコンテキストウィンドウでエンタープライズ用途にも対応。$45B 評価額での資金調達交渉中。

**根拠**: 比較対象として、Claude Sonnet 4.6 は入力 $3/M・出力 $15/M、GPT-4.1 は入力 $2/M・出力 $8/M。V4-Pro の新価格は入力で約 800 倍、出力で約 9〜17 倍安い。コスト構造の改善に裏付けされた値下げのため、他社が同水準まで追随する可能性は低いが、中〜低価格帯モデルの値下げ圧力は確実に強まる。

**影響**: API を直接利用するユーザーにとって、品質要件を満たすタスク（要約、分類、大量バッチ処理など）で V4-Pro が費用対効果の最適解になるケースが増える。一方、推論品質・安全性・エコシステム（MCP、Agent SDK 等）は依然として Anthropic / OpenAI が先行しており、単純な価格比較では判断できない。

**行動指針**: コスト感度の高いバッチ処理タスクがあるなら V4-Pro の品質を実タスクで検証する価値がある。ただし、エージェント用途やツール連携が必要なワークフローでは Claude / GPT のエコシステム優位が大きいため、用途別に使い分ける判断が合理的。

ソース: [US News](https://money.usnews.com/investing/news/articles/2026-05-23/chinas-deepseek-to-make-permanent-75-price-cut-on-flagship-v4-pro-ai-model), [InfoWorld](https://www.infoworld.com/article/4176709/deepseeks-steep-v4-pro-price-cut-escalates-ai-pricing-war.html)

---

### 2. Andrej Karpathy、Anthropic 事前学習チームに入社

**事実**: 5/19 発表。OpenAI 共同創業者・元 Tesla AI 責任者の Karpathy が Anthropic に移籍し、Nick Joseph 率いる事前学習チームに配属。Claude 自身を使って事前学習研究を加速する新チームを立ち上げる。教育スタートアップ Eureka Labs は継続。

**根拠**: Karpathy は GPT-2/3 時代の OpenAI 事前学習を主導し、Tesla FSD の NN アーキテクチャを設計した実績を持つ。Anthropic は直近で $30B 調達（$900B 評価額）、xAI Colossus の大規模コンピュート契約、Stainless 買収と、資金・インフラ・人材のすべてを同時に積み上げている。

**影響**: 事前学習の改善は次世代モデル（Sonnet 4.8 以降や Opus 5 世代）の基礎能力に直結する。ただし成果が API ユーザーに届くのは数四半期先であり、短期的な変化は生じない。

**行動指針**: 経過観察。Anthropic のモデルロードマップに関する公式発表を注視する。

ソース: [TechCrunch](https://techcrunch.com/2026/05/19/openai-co-founder-andrej-karpathy-joins-anthropics-pre-training-team/), [VentureBeat](https://venturebeat.com/technology/andrej-karpathy-announces-hes-joining-anthropic)

---

### 3. Microsoft Copilot Studio May 2026 アップデート — ワークフロー体験刷新とオーケストレーション効率化

**事実**: 5/26 に月次「What's New」ブログが公開。主要な新機能として、統合ビジュアルキャンバスでのワークフロー設計（Preview）、ワークフロー内 Computer Use 埋め込み（Preview）、Work IQ REST API & CLI（リモート MCP サーバー接続対応）が追加。オーケストレーション性能は評価精度 20%向上・トークン消費 50%削減。

**根拠**: Computer Use をワークフロー内に埋め込めるようになったことで、API 操作→承認→UI 操作を単一フローで完結させるエンタープライズ自動化が実用段階に入る。トークン消費 50%削減はコスト面でも大きい。Copilot Studio CLI の GA は 5/31 予定。

**影響**: Microsoft エコシステムでエージェント自動化を構築している組織にとって、ワークフロー設計の自由度が大幅に向上する。特に「API がないレガシーシステム」を Computer Use で橋渡しする用途が現実的になる。

**行動指針**: Copilot Studio を利用中なら、ワークフロー内 Computer Use の Preview を試す価値がある。5/31 の CLI GA と合わせて、CI/CD パイプラインへのエージェント組み込みを検討するタイミング。

ソース: [Microsoft Copilot Blog](https://www.microsoft.com/en-us/microsoft-copilot/blog/copilot-studio/new-and-improved-computer-using-agents-a-new-workflows-experience-and-real-time-voice-experiences/)

---

## カテゴリ別まとめ

### Anthropic / Claude

- **Karpathy 入社**（5/19）: 事前学習チームに配属、Claude を使った研究加速チーム立ち上げ — [TechCrunch](https://techcrunch.com/2026/05/19/openai-co-founder-andrej-karpathy-joins-anthropics-pre-training-team/)
- **MCP Tunnels + Self-Hosted Sandboxes**（5/19, Code with Claude London）: エージェントのツール実行を顧客インフラで実行（Cloudflare, Daytona, Modal, Vercel 等）。MCP Tunnels でプライベート DB/API を安全公開 — [The New Stack](https://thenewstack.io/anthropic-mcp-tunnels-sandboxes/)
- **Claude Code v2.1.150**（5/23）: `/diff` キーボードスクロール、GFM タスクリスト対応。v2.1.149（5/22）で `/usage` コマンド追加 — [GitHub Releases](https://github.com/anthropics/claude-code/releases)
- **Sonnet 4.8 / Mythos**: 公式発表なし継続。Sonnet 4.6 が最新、Mythos は Project Glasswing 限定アクセスのみ — [Anthropic News](https://www.anthropic.com/news)

### GitHub Copilot

- **Desktop App テクニカルプレビュー**（5/14）: macOS/Windows/Linux ネイティブクライアント。Agent Merge（レビュー→修正→マージ自動化）、並列セッション（独立 worktree）対応。Pro/Pro+/Business/Enterprise 向け — [GitHub Blog](https://github.blog/changelog/2026-05-14-github-copilot-app-is-now-available-in-technical-preview/)
- **Individual プラン変更**（4月下旬〜）: Pro/Pro+/Student 新規登録一時停止、Pro から Opus モデル削除（Opus 4.7 は Pro+ のみ）、VS Code/CLI に使用量リアルタイム表示 — [GitHub Blog](https://github.blog/news-insights/company-news/changes-to-github-copilot-individual-plans/)
- **Copilot CLI v1.0.54〜v1.0.55-1**（5/24-26）: `--continue` のブランチコンテキスト再取得、SEA 動作時の Extensions 修正、CJK クリップボード修正等 — [GitHub Releases](https://github.com/github/copilot-cli/releases)

### Microsoft / Copilot

- **Copilot Studio May 2026**: ワークフロー体験刷新（Preview）、Computer Use ワークフロー埋め込み、Work IQ REST API & CLI、オーケストレーション 20%精度向上/50%トークン削減 — [Microsoft Blog](https://www.microsoft.com/en-us/microsoft-copilot/blog/copilot-studio/new-and-improved-computer-using-agents-a-new-workflows-experience-and-real-time-voice-experiences/)
- **社内 Claude Code → Copilot CLI 移行**（5/15 報道）: 6/30 が移行期限。Claude モデル自体は Copilot CLI 経由で継続利用可 — [Developer Tech](https://www.developer-tech.com/news/microsoft-claude-code-github-copilot-cli/)
- **Copilot Notebooks Infographics**（MC1317195）: ノートブックからインフォグラフィックス生成。5-7月展開中 — [mc.merill.net](https://mc.merill.net/message/MC1317195)
- **MDASH**: 100+ AI エージェントで Windows 脆弱性 16 件を自動発見（Critical RCE 4件）。5月 Patch Tuesday で修正済 — [Microsoft Security Blog](https://www.microsoft.com/en-us/security/blog/2026/05/12/defense-at-ai-speed-microsofts-new-multi-model-agentic-security-system-tops-leading-industry-benchmark/)

### OpenAI

- **Codex モバイル対応**（5/14）: ChatGPT アプリから Codex セッションにリモートアクセス。コードレビュー・承認・モデル切替をスマホで操作。全プラン利用可 — [OpenAI](https://openai.com/index/work-with-codex-from-anywhere/)
- 公式 News / Codex Changelog: 5/22 以降の新規発表なし

### Google / Gemini

- Workspace Updates / Gemini App: I/O 2026 発表の段階展開が継続中（Gemini 3.5 Flash GA、Spark ベータ等）
- **AI 料金体系 3 ティア刷新**: AI Plus $7.99/月、AI Pro $19.99/月、AI Ultra $99.99/月。日次プロンプト上限→従量課金に移行 — [The Decoder](https://the-decoder.com/google-overhauls-its-ai-subscriptions-at-i-o-2026-with-three-tiers-starting-at-10-a-month/)
- Gemini 3.5 Pro は 6 月提供予定のまま

### xAI

- **Grok Build ベータ**（5/17）: ターミナルベースのコーディングエージェント。最大 8 並列エージェント、MCP サーバー対応。SWE-Bench Verified 70.8%。SuperGrok Heavy $300/月（導入価格 $99/月） — [xAI](https://x.ai/news/grok-build-cli)

### 市場・業界動向

- **DeepSeek V4-Pro 75%永久値下げ**（5/23）: 入力 $0.003625〜/M tokens。構造的コスト改善による恒久値下げ — [US News](https://money.usnews.com/investing/news/articles/2026-05-23/chinas-deepseek-to-make-permanent-75-price-cut-on-flagship-v4-pro-ai-model)
- **Meta AI 設備投資 $125-145B に上方修正**（Q1 2026 決算）: 前年比ほぼ 2 倍 — [Fortune](https://fortune.com/2026/04/29/meta-zuckerberg-145-billion-ai-spending-roi/)
- **Cloudflare AI リストラ 1,100 人削減**（5/8）: Q1 売上過去最高でも全従業員 20%削減。社内 AI 利用 3 カ月で 600%増 — [TechCrunch](https://techcrunch.com/2026/05/08/cloudflare-says-ai-made-1100-jobs-obsolete-even-as-revenue-hit-a-record-high/)
- **Thinking Machines Lab「Interaction Model」**（5/11）: 200ms フルデュプレックス音声対話。元 OpenAI CTO Mira Murati 創業 — [VentureBeat](https://venturebeat.com/technology/thinking-machines-shows-off-preview-of-near-realtime-ai-voice-and-video-conversation-with-new-interaction-models)
- **Notion External Agents API** で Claude Code / Cursor / Codex がワークスペースに参加する追随報道が拡散（5/13 発表の既報の深掘り）
- **AI コーディングエージェント「スタック化」論**: Cursor / Claude Code / Codex は単一勝者ではなく層構造で併用される見方が定着

### Cursor / Devin

- **Cursor 3.5 Shared Canvases**（5/20）: Canvas 共有リンク、ダッシュボードでの一覧表示。Pro/Teams/Enterprise — [Cursor Changelog](https://cursor.com/changelog/shared-canvases)
- Devin: 5/17 以降の明確な更新なし

---

## 直近の注目予定

- **2026-05-31**: Copilot Studio CLI GA
- **2026-06-01**: GitHub Copilot 従量課金開始・GPT-4.1 廃止・Code Review Actions minutes 消費開始
- **2026-06-08 頃**: Anthropic 6/15 課金変更のクレジット申請メール
- **2026-06-10**: Code with Claude Tokyo
- **2026-06-15**: Anthropic Agent SDK / claude -p 別枠クレジット移行
- **2026-06 中**: Gemini 3.5 Pro 提供開始予定
- **2026-06-30**: Microsoft 社内 Claude Code 利用終了期限

---

## 改善メモ

- 当日（5/28）の digest が未生成のため、5/27 分の 3 ソースを使用してサマリーを作成。Industry ソースは 5 月中旬のニュース（Karpathy 5/19、Codex モバイル 5/14、MDASH 5/12、Grok Build 5/17 等）を補完カバーしている
- GitHub Copilot CLI の pre-release（`-0`/`-1` サフィックス）は安定版とまとめて 1 項目に集約する運用が機能している
- 検索インデックスが過去リリース（Codex-Spark 等）を繰り返し返す問題は、公式ページ日付での裏取りで誤計上を回避できている
- WebFetch 403 継続中ソース多数。全ソース WebSearch プライマリ運用を継続
