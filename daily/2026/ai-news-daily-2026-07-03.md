# AI News Daily Summary — 2026-07-03

> 本サマリーは 01_ai-news-Master・02_ai-news-Copilot・03_ai-news-industry の3ソース（7/3分）を統合して作成。速報系（Claude Code / Copilot / Cursor）は 7/1 更新以降の新リリースが乏しく、7/1 発表分の GA・新プロダクトが実務に効いてくる「静かな追認の日」。

## 今日のハイライト

### 1. ブラウザ操作エージェントが一斉GA — Claude in Chrome と Copilot Browser tools が同日（7/1）に正式版

**事実** Anthropic の **Claude in Chrome 拡張が一般提供（GA）** に到達（Claude Code v2.1.198、7/1）。同日、**GitHub Copilot の Browser tools for VS Code も GA**（7/1）となり、エージェントが実ブラウザを起動してライブ Web アプリを操作・巡回し、結果をチャットに反映できるようになった。主要コーディングエージェント2社がブラウザ操作対応を同じ日に本格解禁した。

**根拠** 従来ブラウザ操作は各社ともプレビュー/ベータ扱いで、E2E テストや Web アプリ検証は人手のスクリーンショット添付に依存していた。GA 化で、エージェントが自らページを開き DOM 操作・遷移・確認まで完結できる。Copilot 側はライブアプリの巡回結果をチャットへ、Claude 側は拡張として常設のブラウザ制御を提供する。

**影響** 「コードを書く」から「動くアプリを触って直す」までがエージェント内で閉じる。フロントエンド/E2E 検証、リグレッション確認、UI バグ再現といった従来ボトルネックだった工程がエージェント委譲の対象になり、2社同日 GA は業界の既定路線化を示す。

**行動指針** フロント/E2E を持つチームは、ブラウザ操作を前提にレビュー・検証フローを再設計する好機。まずリグレッション確認や UI 再現など「観測して直す」系タスクをエージェントに委譲し、権限・スコープ（操作可能なドメイン・認証情報の扱い）を先に定めてから常設運用へ移す。

- https://code.claude.com/docs/en/changelog
- https://github.blog/changelog/label/copilot/

### 2. バックグラウンドエージェントの自律運用が既定挙動へ — 自動 commit・push・draft PR 化

**事実** Claude Code v2.1.198（7/1）で、**バックグラウンドエージェントがコード作業完了時に自動で commit・push・draft PR を作成**する挙動が既定になった（従来は都度確認）。併せて `Notification` hook に `agent_needs_input` / `agent_completed` イベントが追加され、完了・入力待ちを通知で拾える。`claude --bg` と `--print`/`-p` の競合フラグは今後拒否される。

**根拠** 承認待ちが非同期エージェント運用の最大のボトルネックだった。完了時の成果物を自動で PR（draft）まで持っていき、必要時のみ通知で人を呼ぶことで、常駐エージェントが「投げて放置、通知で回収」の運用に耐える。Explore サブエージェントが親セッションのモデルを継承（haiku 固定 → opus 上限で継承）、サブエージェントのコンパクションが extended thinking 設定を継承するなど、常駐運用の品質担保も同時に前進した。

**影響** エージェント運用の既定が「同期・逐次承認」から「非同期・通知ドリブン」へ移る。1人が複数エージェントを並走させ、draft PR とレビューで束ねる働き方が現実的になる。一方で自動 push が既定になるぶん、ブランチ保護・PR ゲート・CI の整備が前提条件として重みを増す。

**行動指針** バックグラウンド運用を始める前に、保護ブランチ・必須レビュー・CI ゲートを先に固める（自動 push の受け皿）。`Notification` hook を Slack/メール等に接続して `agent_completed` / `agent_needs_input` を拾えるようにし、draft PR を既定の合流点に据える。

- https://code.claude.com/docs/en/changelog

### 3. 競争軸が「モデル性能」から「実装インフラ」へ — Sonnet 5 と各社の実装部門投資

**事実** Anthropic は **Claude Sonnet 5**（6/30 提供開始、エージェント志向の中位モデル）を「Opus 4.8 級の性能を大幅な低コストで」と位置づけ、8/31 まで導入価格 **$2/$10 per Mtok**（入力/出力）で提供。並行して **Microsoft が $2.5B の「Frontier Company」部門**を新設し、顧客サイトに 6,000 名規模の専門家を常駐させ導入・最適化を担う（顧客データを学習に使わない明示コミット付き）。

**根拠** AWS・OpenAI・Anthropic・Google が揃って専用の実装/導入部門へ数十億ドル規模を投じており、03（industry）は「成否はモデル性能そのものより実装能力で決まる」段階への移行と整理する。Sonnet 5 の低価格・エージェント志向も、フラッグシップ競争ではなく「実装インフラ」への布石として読める。

**影響** フロンティア各社の差別化がベンチマークからデリバリ（現場導入・運用・データ保護）へ移る。ユーザー企業にとっては、モデル選定より「どの実装体制・ガバナンスに乗るか」が意思決定の中心に近づく。中位モデルの低価格化はエージェント量産のコスト前提を押し下げる。

**行動指針** 高頻度・大量のエージェントワークロードは、Opus 級フラッグシップと Sonnet 5（$2/$10、8/31 まで）でコスト/品質の切り分けを再評価する。8/31 の促進価格終了（$3/$15 へ）を織り込んだ試算を今のうちに。ベンダー選定は実装体制・データ保護条項まで含めて比較する。

- https://openai.com/index/previewing-gpt-5-6-sol/

## カテゴリ別まとめ

### Anthropic / Claude
- Claude Code v2.1.198（7/1）: Claude in Chrome GA・バックグラウンドエージェント自律化（ハイライト参照）。`/dataviz` skill（配色バリデータ付き）追加、Gateway に Claude Platform on AWS を upstream 追加（model-not-found でフェイルオーバー前進） https://code.claude.com/docs/en/changelog
- Sonnet 5（6/30 提供、$2/$10・8/31 まで、ハイライト参照）。Fable 5 は 7/1 グローバル復旧後の追加展開なし。**7/7 まで週次利用上限の最大50%込み、以降 usage credits 経由** https://www.anthropic.com/news/redeploying-fable-5

### GitHub Copilot
- **Browser tools for VS Code が GA（7/1、ハイライト参照）**。Copilot CLI に**自動モデル選択（7/1）** — 稼働率・モデル健全性・タスク特性（推論/コード生成/バグ診断/ツールオーケストレーション需要）から最適モデルへルーティング
- **CLI 安定版 v1.0.68（7/1）: kimi-k2.7-code モデル対応**、slash エイリアス表示改善、切断中の IDE ツール可用性、サブディレクトリからの git 操作改善。pre-release v1.0.69-0（7/2）で `/sandbox` パス補完・大規模モノレポの tgrep メモリ改善 https://github.com/github/copilot-cli/releases

### Devin / Cognition
- **Devin Security Swarm 提供開始（7/1）** — 脆弱性の発見・実行時実証（validate at runtime）・低コスト修正を担う新プロダクト。実世界 50 件ベンチで **36 件検出（テスト対象 AI スキャナ中最多）**、検出あたりコストは次点比 30% 低いと主張。併せてエンタープライズ機能（ACU 可視性制御、MCP レジストリ allowlist 強制、ビルドのピン留め・ロールバック、企業レベル secret 共有）追加。classic 環境設定は 6/30 廃止、read-only 参照は 7/31 まで https://www.prnewswire.com/news-releases/cognition-launches-devin-security-swarm-to-tackle-the-vulnerability-backlog-302814800.html

### xAI / Grok
- **Grok Voice Agent Builder がベータ→GA（7/1、no-code、$0.05/分）** — API 統合経験なしで音声エージェントを構築でき、開発者向けだった Voice Agent を非技術者に開放。旗艦 Grok 5（噂 6T MoE）は依然未出荷 https://x.ai/news

### Cursor
- **Team Marketplaces が Team MCP・組織グループに対応（6/30）** — 管理者が Team MCP を一度設定すればクラウドエージェント / agents ウィンドウ / IDE / CLI へ配布、組織グループ単位のアクセス制限も可能
- **Teams 料金改定 7/1 開始**（新規は即時、更新顧客は 7/1 以降の請求サイクルから）。各シートに Composer/Auto と Third-Party API の2利用プールを分離、標準 $40/月 シートは追加費用なしで利用枠を大幅増。**Composer 2.5 実行 75% オフは 7/5 まで** https://cursor.com/changelog

### OpenAI / Codex
- Codex CLI 0.143.0-alpha.33（7/2）は pre-release でリリースノート未掲載。安定版は 0.142.5（7/1）のまま、実質最新機能は 0.142.2（6/25）
- GPT-5.6 Sol / Terra / Luna は約 20 組織（政府承認）への限定プレビュー継続、一般提供「数週間内」・ChatGPT 未提供。価格 Sol $5/$30・Terra $2.5/$15・Luna $1/$6 per Mtok。新規なし https://openai.com/index/previewing-gpt-5-6-sol/

### Google / DeepMind
- Gemini 3.5 Pro は 7 月延期継続。Vertex AI 限定 Enterprise preview のみで GA 日未定（トークン効率・推論品質の refinement が理由）。2M context / Deep Think（Ultra $250/月）

### Microsoft / Copilot Studio・Power Platform
- **EPPC 2026 基調講演（コペンハーゲン、6/29 開幕）** — 新 Copilot Studio は Power Platform の「置き換え」ではなく「統合・拡張」と整理。Power Apps Studio 内で自然言語からコパイロット構築、Power Automate に AI ワークフロー埋め込み。Power Platform 管理センターに**専用 Copilot 管理ブレード**を追加予定（利用モニタリング・ポリシー適用・分析）。**Work IQ**（M365 横断でコパイロットを接続する work management レイヤー、Teams/Outlook/サードパーティ横断で自動化提案）。GA は 2026 下半期に段階展開見込み https://msdynamicsworld.com/story/eppc-2026-microsoft-aims-balance-new-copilot-studio-vision-power-platform-strengths
- **Microsoft $2.5B「Frontier Company」新設**（6,000 名を顧客サイト常駐、データ非学習コミット、ハイライト参照）

## 直近の注目予定

- **7/5**: Cursor Composer 2.5 割引（75% オフ）終了
- **7/7**: Fable 5 の週次利用上限 50% 制限が解除見込み（以降 usage credits 経由）
- **7/8**: Anthropic 政府発行 ID・生体情報検証ポリシー施行
- **7/14**: 破壊的変更 — Visio → Power Automate エクスポート廃止発効（Current Channel は 6/30 適用済み）
- **7/15**: Claude Science（AI for Science）応募締切
- **7/17**: Claude Corps 第1期応募締切
- **7月中旬〜下旬**: 2026 Release Wave 2 計画ページ公開見込み（要監視）
- **7月**: GPT-5.6 Sol 一般提供 / Gemini 3.5 Pro GA
- **7/31**: Devin classic 環境設定の read-only 参照終了
- **8/1**: covered frontier model フレームワーク 60 日 EO 期限
- **8/3**: 旧「Claude in Slack」アプリ退役
- **8/5**: Opus 4.1 Claude API 退役
- **8/26**: OpenAI Assistants API 廃止 / o3 退役 / GPT-4.5 完全廃止
- **8/31**: Sonnet 5 促進価格終了（$2/$10 → $3/$15）
- **9月**: iOS 27 / macOS 27 GA（AFM 3 本番）

## 改善メモ

- 3ソースとも「新規提案・障害の変化なし」で一致（継続分は各リポの IMPROVEMENT-BACKLOG.md 参照）。02 は 7/2 の全ソースフル巡回で 6/12 以降の取りこぼしを回収済みのため本日は静かな1日と明記
- ブラウザ操作 GA（Claude in Chrome / Copilot Browser tools）は 01 が両社を横断で拾い、02 は「7/1 各更新以降 検証可能な新規なし」と補完。同日 GA という業界横断の含意はハイライトで統合した
- Microsoft $2.5B Frontier Company は 03（industry）が「実装インフラ」トレンドの一例として提示、01/02 は未収録。ソース間の粒度差（01/02＝ツール速報、03＝業界マクロ）を統合してハイライト3に反映
