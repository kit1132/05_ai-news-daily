# AI News Daily Summary — 2026-07-25

> 本サマリーは 01_ai-news-Master・02_ai-news-Copilot・03_ai-news-industry の3ソース（7/25分）を統合して作成。

本日の主役は **Anthropic「Claude Opus 5」の GA（米 7/23 夜〜7/24）**。1M コンテキスト・思考デフォルト ON を **Opus 4.8 据え置きの $5/$25** で提供し、Fable 5 に迫る知能を「約半額」で出す位置づけ。注目は波及速度で、**Claude Code v2.1.219 が既定 Opus を Opus 5 に切替**、**GitHub Copilot CLI v1.0.75 も即日 Opus 5 対応**と、開発ツール側へ同日反映された。市場面では **Google が大規模実データ「AI & Economy ATLAS v1.0」**を公開し「AI＝人員代替」ではなく「タスク単位の協働」を裏づけ。セキュリティ面では **エージェント運用のインシデント多発（54%が経験）・Kimi K3 の攻撃サイバー低評価・Five Eyes の警告**が同時に並び、権限統制の緊急度が上がった。Microsoft 一次は全据え置き（土曜）。

## 今日のハイライト

### 1. Anthropic「Claude Opus 5」GA — 思考 ON・1M 文脈を Opus 4.8 と同価格で、開発ツールへ即日波及

**事実**: Anthropic が **Claude Opus 5（`claude-opus-5`）を GA 公開**（米 7/23 夜〜7/24）。Mythos 5・Fable 5・Sonnet 5 に続き **2ヶ月弱で4本目**という異例のペース。多くのユーザー向け標準モデルに昇格し、Opus 4.8 も併存する。

**根拠**: **1M トークンコンテキストがデフォルト兼最大**（小容量版なし）、**最大出力 128k**、**思考（thinking）がデフォルト ON**。料金は **$5/$25 per Mtok と Opus 4.8 据え置き**、Fast モードは **$10/$50**（Claude API のみ。Bedrock/Vertex/Foundry では未提供）。推論はタスクごとに **effort を low/medium/high でトグル**でき、コストと能力を調整可能。ベンチはターミナル型エージェント coding の **Frontier-Bench v0.1 で 43.3%**（Opus 4.8 18.7%・Fable 5 33.7% を上回る）、GDPval-AA でも新 SOTA を主張する一方、**サイバーセキュリティ課題では Mythos 5 に及ばず**。提供面は **Claude API・Amazon Bedrock・Google Cloud（Vertex）・Microsoft Foundry**。

**影響**: **Claude Code v2.1.219 が既定 Opus を Opus 5 に切替**、**GitHub Copilot CLI v1.0.75 が即日 Opus 5 対応**と、旗艦モデルの更新が同日で開発ツールに波及。Microsoft Foundry でも提供済みで、**Copilot Studio の外部モデル選択（現在 Sonnet 5 / GPT-5.5 Chat が GA 最新）への Opus 5 追加が次の監視点**。

**行動指針**: **破壊的変更に注意** — 思考の無効化（`thinking:{"type":"disabled"}`）は **effort が `high` 以下でのみ許可**、`xhigh`/`max` で無効化指定すると 400 エラー（Opus 4.8 では独立だった）。思考 ON がデフォルトのため **既存の `max_tokens` 見直しが必要**。挙動面では応答が長め・進捗ナレーション増・サブエージェント委譲を積極化し、**自己検証を明示指示なしで実施**するため、旧モデル向けの「検証ステップを追加」指示は過剰検証を招くので削除推奨。prompt cache 最小長は 1,024→**512 トークン**に低下。

- https://www.anthropic.com/news/claude-opus-5
- https://platform.claude.com/docs/en/about-claude/models/whats-new-opus-5

### 2. Google「AI & Economy ATLAS v1.0」— 1,500万件の実データで「タスク単位の協働」を実証

**事実**: 7/23、Google が **Gemini アプリ／AI Mode／API の1,500万件の匿名化インタラクション**を **150カ国超・140言語・800職種・約4,000タスク**で分析した経済レポートを公開（月間10億人超が利用）。

**根拠**: 採用は職種の **68%（米国雇用の90%相当）**に到達する一方、典型的な職務で AI が使われるのは **タスクの約21%のみ**。**完全自動化は全インタラクションの1割未満**で、大半は調査・草稿・反復・troubleshooting・学習の「協働」用途。Anthropic Cowork 実態調査（9割超が非コーディング）に続く一次データ。

**影響**: 「AI＝人員代替」ではなく「**タスク単位の協働**」を大規模実データで裏づけ。導入提案のターゲット粒度を職種でなくタスクに置く根拠として引用可。

**行動指針**: エージェント/Copilot 導入の ROI 提案は、職務全体の置換ではなく **高頻度タスク（調査・草稿・反復作業）への割当**で設計する。実データを提案の裏付けに使う場合の一次ソースとして本レポートを参照。

- https://blog.google/innovation-and-ai/technology/research/understanding-the-ai-economy/
- https://www.axios.com/2026/07/23/google-ai-adoption-work-atlas

### 3. エージェント・セキュリティが一斉に前景化 — インシデント54%・認証情報共有69%、Kimi K3 低評価、Five Eyes 警告

**事実**: VentureBeat 調査（6月・従業員100名超・n=107）で **54%が AI エージェントのセキュリティインシデント（確認済18%＋ニアミス36%）を経験**、**69%がエージェント間で認証情報を共有**。同時期に **Moonshot「Kimi K3」の攻撃サイバー評価が低位**、機密同盟 **Five Eyes がフロンティア AI のサイバー変革を「月単位」で警告**。

**根拠**: 各エージェントに固有スコープ ID を付与しているのは約1/3、最高リスクのエージェントを隔離しているのは 30% のみ。Kimi K3（7/27 オープンウェイト公開予定・Modified MIT）は英 AISI・米 CAISI 評価で **ExploitBench 32%**（米主要モデル76%に対し低位）、セーフガードがエクスプロイト開発・模擬攻撃を阻止できず。加えて公表ベンチから欠落との指摘がある **51% のハルシネーション率**。

**影響**: 認証情報共有は単一侵害の横展開を招く。中国製オープンウェイト（Kimi/DeepSeek/GLM）採用時の **モデル出自・セキュリティ・法域リスク**が調達要件に格上げ。「モデル→実装体制」競争の裏で、本番運用の権限統制が導入可否を左右する段階に入った。

**行動指針**: エージェント本番運用の提案要件に **①スコープ化した固有 ID、②高リスクエージェントの隔離、③認証情報の非共有（MCP/EMA 等）、④デプロイ前評価**を標準化。中国製オープンモデル採用検討時は出自・輸出規制・制裁エクスポージャを調達チェックリストに追加し、Kimi K3 は **7/27 公開後の技術検証を待って再評価**するのが妥当。

- https://venturebeat.com/ai/the-agent-security-gap-54-of-enterprises-have-already-had-an-ai-agent-incident-and-most-still-let-agents-share-credentials
- https://www.techtimes.com/articles/321499/20260724/kimi-k3-open-weights-drop-july-27-near-frontier-coding-undisclosed-hallucination-risk.htm

## カテゴリ別まとめ

### Anthropic / Claude
- **Claude Opus 5 GA**（ハイライト参照）
- **Claude 音声モードを Opus/Sonnet に拡張**（7/24 報道）— 従来 Haiku 中心だった音声モードを上位モデルでも稼働可能に。音声 UI での高度な推論利用が広がる。あわせて OpenAI もデスクトップアプリで ChatGPT Voice を Work/Codex に展開。 https://the-decoder.com/

### OpenAI
- **「Health in ChatGPT」を全米ユーザーに GA**（7/23）— 健康記録と ChatGPT を統合。**Apple Health（運動・睡眠・アクティビティ）＋米病院システム・One Medical・Function Health の医療記録**を会話に引き込める。18歳以上の Free/Go/Plus/Pro（EEA・スイス・英国を除く）が対象、Web・iOS で提供。2026年1月の不発パイロットを作り直しての再ローンチ。 https://openai.com/index/health-in-chatgpt/
- **Codex CLI 0.146.0-alpha.7 進行中**（7/24）— 安定版は 0.145.0（7/21）据え置き。alpha ビルドが日次で刻まれるが公開リリースノートに具体的変更記載なし。 https://github.com/openai/codex/releases

### 開発ツール（Claude Code / Copilot / Cursor）
- **Claude Code v2.1.219**（7/24）— ① **既定 Opus モデルを Claude Opus 5 に切替**（1M 文脈・Fast $10/$50、`/fast` は Opus 5/4.8 に適用、Fast から Opus 4.7 除外）、② 許可リスト外ホストをプロンプトなしで拒否する `sandbox.network.strictAllowlist` 追加、③ `/add-dir`・SDK での作業ディレクトリ追加後に発火する `DirectoryAdded` フック、④ Dynamic workflow サイズ推奨を制御する `workflowSizeGuideline`、⑤ サブエージェントのネスト生成を既定深さ3まで許可（`CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH` で変更）。修正: `claude -p` がストリーム中の API エラーで回答を落とす問題、self-hosted runner 再起動で承認済み権限が失われる問題ほか。 https://code.claude.com/docs/en/changelog
- **GitHub Copilot CLI v1.0.75（7/24）／v1.0.74（7/23）**— **1.0.75 = Claude Opus 5 対応を追加**。1.0.74 = 安定版昇格、Open Plugin Spec v1 マニフェスト対応、Gemini 3.6 Flash サポート、MCP 再接続を含む IDE 連携安定化、サブエージェント由来（メイン/サブ）識別、`/model plan`。従来安定版 v1.0.73（7/20）から更新。 https://github.com/github/copilot-cli/releases
- **Cursor「Cursor Router」導入**（7/22）— Auto モードをリクエスト内容解析で最適モデルへ振り分けるルーターで駆動。チームは **Intelligence / Balance / Cost** の3モードを選択でき、管理者が既定モデルとアクセスを制御。なお 7/9 の「Claude Honeycomb EAP」は Opus 5 の early-access だったと判明。 https://cursor.com/changelog

### Google / DeepMind
- **AI & Economy ATLAS v1.0**（ハイライト参照）
- **Alphabet Q2 2026・通年 capex を $195–205B へ上方修正**（7/22 決算）— 売上約$1,198億（+24% YoY）、Google Cloud 大幅増（前年比+82%集計）。四半期 capex $44.9B（前年比倍増）、通年ガイダンスを $180–190B→**$195–205B** へ引き上げ（約6割サーバー・4割 DC/ネットワーク）。株価は capex 拡大を嫌気し時間外で下落。 https://www.cnbc.com/2026/07/22/google-earnings-q2-goog-live-updates.html

### 開発者ツール / ディール
- **デザインツール「Paper」$34M Series A**（7/23）— Accel・ICONIQ 主導、Anthropic/OpenAI のエンジニア/デザイナーがエンジェル参加。「エージェント・ネイティブなデザイン基盤」を標榜し、Paper Desktop 投入以降 ARR 25倍。設計↔コード↔データを人間とエージェントが共有する協働ワークフローで Figma に対抗。 https://www.businesswire.com/news/home/20260723608438/en/Paper-Raises-%2434-Million-Series-A-with-Accel-and-ICONIQ-to-Build-the-Design-Platform-for-the-Agentic-Era

### 規制・政策・セキュリティ
- **VentureBeat「エージェント・セキュリティギャップ」調査**（ハイライト参照）
- **Moonshot「Kimi K3」オープンウェイト 7/27 公開・攻撃サイバー低評価**（ハイライト参照）— なお MXFP4 4bit でも約1.4TB の高速メモリを要し自己ホストの敷居は高い。
- **Five Eyes、フロンティア AI のサイバー変革を警告**（7月）— 「フロンティアモデルは攻防双方のサイバー能力を根本的に変え、その時間軸は年単位でなく月単位」。Kimi K3 の攻撃サイバー評価公表と同時期で、導入時セキュリティ要件の緊急度を裏づけ。 https://www.artificialintelligence-news.com/

### Microsoft / Copilot Studio（一次据え置き・新規なし）
- **Copilot Studio What's New**: June 2026 節のまま（7月節未公開）。外部モデル選択は **Sonnet 5 / GPT-5.5 Chat が GA 最新で Opus 5 は未追加**（Foundry では提供済みのため波及が次の監視点）。
- **M365 Copilot Release Notes**: 「July 15, 2026」バッチが最新のまま。次バッチは 7/29 前後見込み。
- **Released Versions（Copilot Studio）**: Build **2026.6.3（6/30初出）が最新のまま**。予告の 2026.7.x は未反映（次の要監視は 7/28 火）。
- **Message Center / Power Platform**: 本日の新規 MC 検知なし（MC1422074 は 7/24 発効済み）。Power Platform 月次「July 2026」は未公開（最新は 6/11 June）。

## 直近の注目予定

- **7/27**: Kimi K3 オープンウェイト公開予定（HuggingFace・Modified MIT）
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
- **要監視**: Copilot Studio 外部モデル選択への Claude Opus 5 追加（Foundry で提供済み）

## 改善メモ

- **Opus 5 GA 日付の表記差**: Master/Copilot は「7/24」、industry は「7/23（米）」。米国時間 7/23 夜＝日本時間 7/24 として統合（ベンチ数値・仕様・価格は3ソースで整合）。
- 3ソースとも新規提案・障害の変化なし（継続分は各リポの IMPROVEMENT-BACKLOG.md 参照）。
- **Gemini 3.5 Pro GA は依然「未ローンチ」**（Master で言及、8月ずれ込み観測継続）。新規進展なしのため本文非掲載、GA・価格判明後に更新。
- Master: 土曜のため週次復旧チェックは非対象（次回 07-27 月曜）。
- industry: 継続提案 1件（B-004 取得方法欄の WebSearch 優先化、26回目）。
</content>
</invoke>
