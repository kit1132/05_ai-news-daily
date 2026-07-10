# AI News Daily Summary — 2026-07-11

> 本サマリーは 01_ai-news-Master・02_ai-news-Copilot・03_ai-news-industry の3ソース（7/11分）を統合して作成。

土曜。**今週前半の大型ローンチ（GPT-5.6 GA / ChatGPT Work / Grok 4.5 / Claude Cowork の Web・モバイル化）が一巡した静かな一日**。新規は「業種特化アプリ」と「エコシステム基盤」に集約された。最重要は **M-Files が提案〜デリバリを一気通貫でガバナンスするコンサル特化アプリ「M-Files for Consulting」を投入** — 汎用常駐エージェント（ChatGPT Work / Claude Cowork）に対する専門特化の対抗軸。あわせて **UST が Anthropic と提携し全世界2万人を Claude 認定**（SI 大手による業種横断展開）、**Microsoft の Dataverse プラグインが Claude / Cursor / GitHub Copilot のコーディングエージェントへ提供開始**（MCP 認定プログラムも新設）。開発ツールは Claude Code v2.1.206・Copilot CLI 安定版 v1.0.70・Codex CLI 0.144.1 と定常アップデート。Microsoft の一次情報は静穏継続。

## 今日のハイライト

### 1. M-Files が「M-Files for Consulting」を投入 — 提案〜デリバリを一気通貫、ガバナンス組込み型で汎用エージェントに対抗

**事実**: M-Files が、コンサル業務のライフサイクル（proposal → engagement → delivery）をクライアント・提案・案件文脈で構造化する AI ネイティブ・アプリを 7/9 に発表。過去の承認済み提案・事例・テンプレートを AI が参照する「AI-accelerated proposals」、役割別ビュー（パートナー＝デリバリ状況/全社ナレッジ、マネージャ＝レビュー・承認、コンサル＝ドラフト・再利用、IT＝ガバナンス）、成果物・プレイブックを再利用資産化する「governed knowledge reuse」を提供。

**根拠**: ChatGPT Work / Claude Cowork が「汎用の常駐エージェント」で業務成果物を生成する流れに対し、M-Files は「機密クライアント情報のガバナンスと承認フローを前提にした専門特化型」で差別化する設計。

**影響**: 専門サービス業の AI 導入は、①汎用エージェント＋横断ガバナンス（MCP の EMA 等）か、②業種特化アプリ（承認・権限が組込み済）か、の二択が実質的な設計判断になる。

**行動指針**: コンサル向け AI 提案では「承認フロー・権限モデルが最初から組み込まれているか」を選定軸に据える。汎用エージェント案を出す場合は、ガバナンス層（監査・事前レビュー・アクセス制御）をどう補うかをセットで提示する。

- https://www.accessnewswire.com/newsroom/en/computers-technology-and-internet/m-files-launches-m-files-for-consulting-transforming-a-firms-know-1188403

### 2. UST が Anthropic と戦略提携 — 全世界2万人を Claude 認定、frontier モデルの業種横断 SI 展開が本格化

**事実**: SI 大手 UST が Anthropic と戦略提携（7/8 発表・7/10 続報）。自社が設計・構築・運用するエンジニアリング環境と業務ワークフローに Claude を組込み、Global 1000 企業の「AI ネイティブ化」を支援。アーキテクト/エンジニアからコンサル・業界専門家・forward-deployed engineer まで、全世界 20,000 名の従業員を Claude で認定する。UST は Claude Partner Network の Services Tier で Global Premier Partner に位置づけ。

**根拠**: 孤立した AI パイロットから、業務基盤に埋め込まれたエンタープライズ規模の AI への移行を狙う体制。法務 SaaS Harvey に続く、frontier モデルの業種横断 SI 展開事例。

**影響**: モデル提供元が SI パートナーの人材認定・デリバリ体制ごと囲い込む段階に入った。Claude の導入は「モデル選定」から「認定済みデリバリ体制の有無」へと評価軸が広がる。

**行動指針**: エンタープライズ AI 提案では、モデル性能だけでなく「認定済みインテグレーターの層の厚さ・デリバリ実績」を比較材料に加える。競合提案が SI 認定規模を訴求してくる前提で自社の実装体制を可視化しておく。

- https://www.prnewswire.com/news-releases/ust-partners-with-anthropic-to-bring-claude-into-usts-platforms-engineering-and-operations-and-train-20-000-ust-employees-globally-302820669.html
- https://www.hpcwire.com/aiwire/2026/07/10/ust-partners-with-anthropic-to-bring-claude-to-engineering-and-enterprise-operations/

### 3. Dataverse プラグインが Claude / Cursor / GitHub Copilot に提供開始 — MCP 認定プログラム新設でエコシステムが横断化

**事実**: Power Platform Blog の Dataverse 7 月更新（7/6・5 日遅れで回収）で、**Dataverse プラグインが Claude / Cursor / GitHub Copilot のマーケットプレイスで利用可能**に。自然言語指示でプラグインがツールルーティングを処理（エンタープライズのセキュリティ標準を維持）。MCP カタログは 60+ の即利用可能サーバーに拡大し、ISV が Partner Center 経由で MCP をパッケージ化・申請できる **MCP 認定プログラム**を新設（認定後は Copilot Studio と Azure AI Foundry の両方で発見可能）。「Bring Your Own MCP」で社内向けカスタム MCP も登録可能。

**根拠**: Microsoft の業務データ基盤（Dataverse）が、自社の Copilot 系だけでなく Claude / Cursor など第三者コーディングエージェントへ横断的に開かれた。単一の標準接続モデル（MCP）でツール接続を統一する方向。

**影響**: 「どのエージェントを使うか」と「どのデータ基盤に繋ぐか」が分離し、コーディングエージェントの選定がベンダーロックから解放されつつある。MCP 認定は ISV 側の配布チャネルとしても機能する。

**行動指針**: Dataverse を業務データ基盤に持つ顧客には、エージェント選定を Microsoft 純正に限定せず「Claude/Cursor 含む横断案」を提示できる。MCP 認定の取得可否を、社内ツールをエージェントに接続する際のロードマップに織り込む。

- https://www.microsoft.com/en-us/power-platform/blog/2026/07/06/dataverse-july2026/

## カテゴリ別まとめ

### Anthropic / Claude
- **UST × Anthropic 提携・2万人認定**（ハイライト参照）。
- Anthropic 公式 news は 7/9 の Claude Reflect（利用分析ダッシュボード beta）以降、新規発表なし。

### OpenAI / ChatGPT
- **GPT-5.6 の ChatGPT Plus 展開が 7/10 完了** — 7/9 GA から 24 時間で段階展開が進行。Team 全面は 7/14 予定。ChatGPT Work は Pro/Enterprise/Edu 先行から Plus/Business へ拡大中（接続先に Slack/Gmail/Google Drive/CRM 等を明示）。 https://www.technology.org/2026/07/10/openai-chatgpt-work-gpt-5-6-agent-launch/
- ChatGPT Work・Codex 統合デスクトップアプリ・GPT-5.6 GA 本体は 7/9 掲載済み。本日は展開完了の続報のみ。

### Microsoft / Copilot / Power Platform
- **Dataverse プラグイン → Claude/Cursor/Copilot 提供・MCP 認定プログラム新設**（ハイライト参照）。
- **一次情報は静穏継続**（Learn MCP で一次確認）: Copilot Studio Released Versions は Build 2026.6.3（6/30 初出）のまま、次ビルド 2026.7.x は未反映（次回火曜 **7/14** が要監視）。What's New は June セクションのまま 7 月項目なし。M365 Copilot Release Notes は July 01 バッチが最新・off-cycle なし（次バッチは 7/14〜7/15 前後見込み）。
- 月次「What's New in Power Platform: July 2026」フィーチャー更新は未公開（最新は 6/11 の June）。

### 開発ツール（Claude Code / Copilot CLI / Codex CLI / Cursor / Devin）
- **Claude Code v2.1.206（7/9）** — `/cd` にディレクトリパス補完追加（`/add-dir` 同等）、`/doctor` がチェックイン済み `CLAUDE.md` の肥大化検知・整理提案、`/commit-push-pr` が `remote.pushDefault`（設定済み push リモート）への `git push` も自動許可、gateway `/login` が公開ゲートウェイ対応、`.claude/worktrees/` 外の worktree 進入時に確認、更新後は背景エージェント即時アップグレード、**opus-4-8 での `/code-review` 品質を全 effort で改善**。 https://code.claude.com/docs/en/changelog
- **GitHub Copilot CLI 安定版 v1.0.70（7/10）** — pre-release を安定版に昇格。**GPT-5.6 対応**、`/refine`（プロンプト精緻化）、プラグインの commit SHA ピン留め、`--sandbox`/`--no-sandbox`、リポジトリ単位設定 `.github/copilot/settings.json`（model/effort/context tier ピン留め）。 https://github.com/github/copilot-cli/releases
- **OpenAI Codex CLI 安定版 0.144.1（7/9）** — スタンドアロンインストールの GitHub リリースメタデータ圧縮/並べ替え時の不具合修正、macOS で code-mode ホストを主実行体と併設・フォールバック対応。alpha は 0.145.0-alpha.2（7/10）。 https://github.com/openai/codex/releases
- **Cursor / Devin**: 日付確定の新規リリースなし。Cursor 3.9・iOS 公開ベータ（7/9）、Devin SWE-1.7（7/8）が確認済みの最新。

### SpaceXAI / Grok
- Grok 4.5 一般公開（7/9）以降の新規進展なし。EU 提供は 7 月中旬めどのまま。

### Google / DeepMind
- **Gemini 3.5 Pro** GA は 7/17 目標のまま進展なし。Google 公式のモデルカード・API ドキュメント・確定価格は未発表で、7 月中の提供を再表明する状況が継続。

## 直近の注目予定

- **7/13**: Claude Code 週次上限+50%プロモ（5 月開始）の期限（延長なき場合）
- **7/14**: Copilot Studio 版ページ次更新（2026.7.x 反映見込み）/ M365 Copilot Release Notes 次バッチ見込み / ChatGPT GPT-5.6 の Team 全面展開予定 / iOS 27 Public Beta 公開予定（〜7/14 頃）/ 破壊的変更: Visio → Power Automate エクスポート廃止発効
- **7/15**: Claude Science（AI for Science）応募締切
- **7/17**: Claude Corps 第 1 期応募締切 / Gemini 3.5 Pro GA 候補日（未確定）
- **7/21**: Copilot Cowork GA 告知イベント
- **7/23**: OpenAI computer-use-preview シャットダウン
- **7/31**: Devin classic 環境設定の read-only 参照終了
- **8/1**: covered frontier model 大統領令 60 日期限
- **8/3**: 旧「Claude in Slack」退役
- **8/5**: Opus 4.1 Claude API 退役
- **8/26**: OpenAI Assistants API 廃止 / o3 退役 / GPT-4.5 完全廃止
- **8/31**: Sonnet 5 促進価格終了（$2/$10 → $3/$15）
- **9 月**: iOS 27 / macOS 27 GA（AFM 3 本番）

## 改善メモ

- **障害の変化なし**: xAI/SpaceXAI `x.ai/*`・Anthropic news・github.blog・cursor.com/changelog・9to5Mac の WebFetch/RSS 403 継続（3 ソースとも WebSearch・二次ソースで補完）。取得方法の WebSearch 優先化提案（03 の B-004、12 回目）が継続中。
- **回収遅延の指摘**: 02 が Power Platform Blog の Dataverse 記事（7/6）を 5 日間未回収だった点を報告し、月次フィーチャー更新以外のトピック記事（Dataverse/Power Apps/Power Automate 個別記事）も拾うクエリ拡張（B-011）を提案。
- **ソース間整合**: Claude Code v2.1.206・GPT-5.6 展開・Grok 4.5・M-Files/UST/Dataverse の各件で 3 ソース間の矛盾は検出されず。開発ツールの版番号（Claude Code v2.1.206、Copilot CLI v1.0.70、Codex CLI 0.144.1）は 01・02 で整合。
