# AI News Daily Summary — 2026-07-22

> 本サマリーは 01_ai-news-Master・02_ai-news-Copilot・03_ai-news-industry の3ソース（7/22分）を統合して作成。

静かな水曜。大型ローンチや国内発表はなく、Microsoft 一次情報源は全て据え置き（CS 版ページの 2026.7.x は依然未反映、次の監視日は 7/28）。動きの中心は開発ツールの版更新と、既報の catch-up 収録。**OpenAI Codex CLI 0.145.0 が GA**（ページネーション付きスレッド履歴・memories・サブエージェント対応）、**GitHub Copilot CLI v1.0.73 安定版＋v1.0.74-0 pre-release**、**Claude Code v2.1.216** が出揃った。エンプラ運用では **Amazon CloudWatch「Coding Agent Insights」が提供開始**し、コーディングエージェントの利用可視化が製品化。資本・規制面では **Meta × Anthropic の最大$10B コンピュートリース協議**（NYT）と、**ホワイトハウスのフロンティアモデル公開前レビュー枠組みが8月初旬合意観測**という制度化の動きが並ぶ。

## 今日のハイライト

### 1. Meta × Anthropic、最大$10B のコンピュートリース協議 — 「計算資源確保が最重要」路線を裏づけ

**事実** Meta が Anthropic に対し、2年間で最大$100億（$10B）規模の計算資源をリースする方向で協議中（NYT が先行報道、Bloomberg 等が追随）。Anthropic は Meta の余剰インフラを借りて自前データセンター建設を回避し、月次分割払い＋双方に早期解約条項を織り込む。6月に Anthropic 側から提案していた枠組み。

**根拠** Zuckerberg は5月株主総会で「クラウド事業参入も選択肢」と言及済み。数週前の SpaceX Colossus 1 データセンター利用契約、Tom Blomfield の Anthropic compute チーム合流（既報）と同じ路線に連なる。協議は初期段階で流動的。

**影響** Meta には新規事業ライン、Anthropic には逼迫する compute 確保という双方メリット。10月観測の Anthropic IPO を控え、コスト構造・供給余力が投資家評価の焦点になる。フロンティアラボの compute 調達が「自前建設」から「他社インフラのリース」へ多様化する兆し。

**行動指針** Anthropic 依存のプロダクトは、compute 供給の安定性が中期的に改善する材料として捉えつつ、契約が初期段階・流動的である点を割り引く。IPO 関連報道での供給余力・粗利の言及を継続監視。

- https://www.bloomberg.com/news/articles/2026-07-17/meta-in-talks-to-sell-computing-power-to-anthropic-nyt-reports
- https://money.usnews.com/investing/news/articles/2026-07-17/meta-in-talks-for-10-billion-anthropic-compute-deal-nyt-reports

### 2. ホワイトハウス、フロンティアモデル自主フレームワーク合意間近 — 公開前レビューが制度化へ

**事実** White House と主要AIラボ（OpenAI / Anthropic / Google DeepMind）が、フロンティアモデルの公開前レビューを含む自主フレームワークで合意間近。発表は8月1日より前〜8月第1週の観測。評価は商務省 CAISI の TRAINS（サイバー/生物/化学兵器の国家安全保障リスク）経由で、最大30日の事前審査を想定。

**根拠** 6/2 大統領令（EO・AIとサイバーセキュリティ）が Treasury/Defense/DHS に課した60日期限の満了（8/1）に合わせる。既報「フロンティア3社CEO 規制収斂」（7/16 Axios）が具体的な政府フレームワークとして着地しつつある段階。Meta は現時点で不参加。

**影響** 「主要モデルは公開前に政府審査を通る」前提が制度化に向かう。最大30日の事前審査はモデルの GA タイミングに影響し得るため、リリース計画の読みに直結する。正式合意・条文は未確定で、参加ラボの範囲（Meta 不参加）も流動的。

**行動指針** 米国発フロンティアモデルの新規 GA を前提にした導入計画は、審査リードタイム（最大30日）を見込んだバッファを想定。8月第1週の正式発表・条文で参加範囲と審査対象の閾値を確認する。

- https://aiweekly.co/alerts/white-house-nears-voluntary-frontier-model-deal-with-top-ai-labs
- https://www.pymnts.com/news/artificial-intelligence/2026/white-house-wants-to-review-ai-models-before-roll-out/

### 3. OpenAI Codex CLI 0.145.0 安定版リリース — スレッド履歴・memories・サブエージェント対応

**事実** OpenAI Codex CLI が 0.144.6（7/18）から alpha を経て 0.145.0 GA（7/21）。目玉は「実験的なページネーション付きスレッド履歴」で、効率的な resume・検索・名前の永続化・サブエージェント対応・memories（メモリ）を搭載。あわせて他社ツールからの設定インポート拡充、Amazon Bedrock ログイン対応、音声入力を追加。長い会話でのターミナル応答性も改善。

**根拠** OpenAI 公式 GitHub releases での GA 表記。サブエージェント・memories は Claude Code / Copilot CLI が先行していた領域で、Codex CLI が機能面で追随・拡充する形。

**影響** 主要コーディングエージェント CLI 3種（Codex / Copilot / Claude Code）がスレッド履歴・サブエージェント・メモリで機能収斂しつつあり、選定基準がバックエンド（Bedrock 対応等）・運用可視化・価格に移りつつある。Bedrock ログイン対応は AWS 環境での採用障壁を下げる。

**行動指針** Codex CLI を評価対象に含めるチームは、resume・検索の実運用体感とサブエージェント構成を試す好機。AWS ベースの組織は Bedrock ログイン対応で認証フローが簡素化される点を検証。

- https://github.com/openai/codex/releases

## カテゴリ別まとめ

### コーディングエージェント / 開発ツール
- **GitHub Copilot CLI v1.0.73 安定版（7/20）＋ v1.0.74-0 pre-release（7/21）**：v1.0.73 は Anthropic サブエージェントが追加ディレクトリ（`--add-dir`）でも動作するよう修正、カスタムエージェント指示内の相対リンク解決を改善。pre-release は `/model plan`（plan モード用モデル選択）追加、セッション resume のタイトル空白揺れ吸収。 https://github.com/github/copilot-cli/releases
- **Claude Code v2.1.216（7/20）**：`sandbox.filesystem.disabled` 設定を追加（ネットワーク egress 制御は維持しつつファイルシステム分離のみスキップ可能）。長時間セッションでのメッセージ正規化コストの二次増大・ストールを修正、OAuth トークン失効後に auto モードが「HTTP 401」で誤拒否する不具合、worktree 分離サブエージェントの共有チェックアウト書き込み、クラウドセッション再起動でのメッセージ喪失を是正。dataviz スキルのチャートパレット更新も同梱。 https://code.claude.com/docs/en/changelog
- **OpenAI Codex CLI 0.145.0 GA（7/21）**：（ハイライト参照）

### 企業導入 / 運用
- **Amazon CloudWatch「Coding Agent Insights」提供開始（7/20）**：AI コーディングエージェントの利用状況を監視する専用ダッシュボード。各エージェントが emit する OpenTelemetry メトリクスをベースに、Claude apps gateway 経由で Claude Code のテレメトリを追加計装なしで収集（Codex・GitHub Copilot も対応）。個人・小規模はベアラートークンで CloudWatch ネイティブ OTLP エンドポイントへ直接送信、企業規模は Claude apps gateway で集中管理（Bedrock / Claude Platform on AWS / Google Cloud / Microsoft Foundry 対応）。中東（UAE / Bahrain）・イスラエル（Tel Aviv）を除く全 AWS 商用リージョンで利用可能。 https://aws.amazon.com/about-aws/whats-new/2026/07/cloudwatch-coding-agent-insights/

### 資本・インフラ
- **Meta × Anthropic、最大$10B コンピュートリース協議（NYT・7/17）**：（ハイライト参照）

### 規制・政策
- **ホワイトハウス、フロンティアモデル公開前レビュー枠組み合意間近（8月初旬観測）**：（ハイライト参照）

### ディール（エンプラ自前構築）
- **Prime Intellect、$130M Series A・評価額$1B（7/8）**：Radical Ventures 主導（Nvidia Ventures / Intel Capital / Dell Technologies Capital / Iconiq 等）。フロンティアラボに依存せず組織が自前でエージェントを訓練できる「フルスタック」（compute アクセス＋強化学習フレームワーク＋評価ツール）をマーケットプレイス型で提供。顧客に Ramp / Zapier 等、6,000社超・ARR 約$100M。「クローズド汎用フロンティアからの脱却＝自前・特化・低コスト」路線の資本集中の一例（state 未収録のため catch-up 収録）。 https://techcrunch.com/2026/07/08/prime-intellect-raises-130m-series-a-to-help-enterprises-build-their-own-ai-agents/

### Microsoft / Copilot Studio（一次・全据え置き）
- **Copilot Studio What's New** は June 2026 セクションのまま（7月未公開）。**M365 Copilot Release Notes** は「July 15, 2026」バッチが最新（次バッチは 7/29 前後見込み）。**Released Versions** は Build 2026.6.3（6/30初出）据え置きで、予告の 2026.7.x は依然未反映（次の要監視は 7/28 火）。Roadmap / Message Center / Power Platform 系ブログも新規なし。 https://learn.microsoft.com/en-us/power-platform/released-versions/copilotstudio

### その他（据え置き確認）
- **Cursor** は公式 changelog 上 3.11（7/10）のまま。**Devin** は SWE-1.7（7/8）・Security Swarm（7/1）が直近で 7/22 新規なし。**Anthropic** は 7/22 の新規製品発表なし（Reflect ダッシュボード 7/19・ヘルスケア提携＋HIPAA 構成 7/17 が継続）。

## 直近の注目予定

- **7/23**: OpenAI computer-use-preview シャットダウン / GPT-5.4 退役予定
- **7/28（火）**: Copilot Studio 版ページ 2026.7.x 反映見込み（要監視）
- **7/29 前後**: M365 Copilot Release Notes 次バッチ見込み
- **7/30**: M365 Copilot メモリ活用のエージェント提案 GA
- **7/31**: Devin classic 環境設定 read-only 参照終了
- **8/1**: covered frontier model 60 日 EO 期限 / フロンティアモデル自主フレームワーク発表観測（〜8月第1週）
- **8/3**: 旧「Claude in Slack」退役
- **8/5**: Opus 4.1 Claude API 退役 / Cowork 倍増利用枠終了
- **8/9**: ChatGPT Atlas シャットダウン
- **8/26**: OpenAI Assistants API 廃止 / o3 退役 / GPT-4.5 完全廃止
- **8/31**: Sonnet 5 促進価格終了（→ $3/$15）
- **9 月**: iOS 27 / macOS 27 GA（AFM 3 本番）

## 改善メモ

- 3ソースとも新規提案・障害の変化なし（継続分は各リポの IMPROVEMENT-BACKLOG.md 参照）。01_Master は水曜のため週次復旧チェック非対象（次回 07-27 月曜）。
- 03_industry: 継続提案 1件（B-004 取得方法欄を WebSearch 優先へ、23回目）。
- Copilot Studio 版ページの 2026.7.x 反映は 7/21 火に未着で 7/28 へスライド。cursor.com/changelog は 403 継続で WebSearch 照合中。ソース間の重複・矛盾は検出せず。
