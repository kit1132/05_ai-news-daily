# AI News Daily Summary — 2026-06-30

> 本サマリーは 01_ai-news-Master・02_ai-news-Copilot・03_ai-news-industry の3ソース（6/30分）を統合して作成。

## 今日のハイライト

### 1. Fable 5 世界停止 19 日目 — 復旧は Pentagon / NSA 署名待ちで足踏み

**事実** — 米輸出規制指令（6/12 BIS 指令）による Anthropic モデルの世界停止は本日で 19 日目。Mythos 5 は Annex A（重要インフラを運用・防衛する約 100 の米組織・政府機関）に限定再提供されたが、一般向けの Fable 5 は依然として制限下にある。

**根拠** — Axios（6/27）の「今週中」復旧観測を複数メディアが追随する一方、Pentagon・NSA の最終署名が未了で復旧の正式日付・条件は未確定。Anthropic 公式 X（6/29）も Mythos 5 の一部 US 組織への再展開を再確認したのみで、Fable 5 解禁の新規進展はなし。返金・解約申請の締切（6/20）は終了済み。

**影響** — 復旧条件が不透明（無制限提供に戻るのか、追加料金・本人確認付きになるか未公表）。7/8 に政府発行 ID・生体情報検証ポリシー施行が控えており、復旧後の利用形態が変わる可能性。顧客提訴も継続中。

**行動指針** — 本日 6/30 の Anthropic「The Briefing: AI for Science」ライブ配信（10:00 PDT＝7/1 未明 JST）を公式発信としてクロスチェック。Fable 5 を本番依存している場合は復旧条件（ID 検証）を見込んだ代替プランを継続維持。

- https://x.com/AnthropicAI/status/2070665903440871779
- https://www.axios.com/2026/06/27/anthropic-fable-5-return-soon
- https://www.anthropic.com/news/fable-mythos-access

### 2. Google Gemini 3.5 Pro が「6 月内公開」期限を逸し 7 月へスリップ

**事実** — Pichai が 5 月 I/O で約束した「6 月公開」が本日 6/30 の期限を迎えたが、Gemini 3.5 Pro は依然として Vertex AI のエンタープライズ preview 限定（2M context / Deep Think）にとどまり、一般 Gemini アプリ・AI Studio・標準 API へは未提供。

**根拠** — CryptoBriefing・TechTimes など複数メディアが 7 月 GA への延期を報道。品質の追い込みとトークン消費・agentic タスク最適化の課題が理由として挙げられている。予測市場でも「6/30 までに公開」は拮抗〜低位。

**影響** — GPT-5.6・Fable 5 と並んで主要フロンティアモデルのローンチが 7 月に集中。7 月中旬に各社のローンチ報道が重なる見込みで、モデル選定・移行計画の前提が動く。

**行動指針** — Gemini 3.5 Pro を見込んだ検証は Vertex AI preview で先行可能。一般提供前提の本番計画は 7 月以降にスライドして再見積もり。

- https://cryptobriefing.com/google-delays-gemini-35-pro-launch-to-july-2026/
- https://www.techtimes.com/articles/317919/20260606/google-gemini-35-pro-nears-june-launch-2-million-token-context-deep-think-reasoning.htm

### 3. Qualcomm が Modular を約 $3.9B で買収 — Nvidia 依存低減の布石

**事実** — Qualcomm が AI ソフトウェア企業 Modular（Mojo 言語・MAX 推論エンジン）を約 39 億ドルで買収。開発者の Nvidia ハードウェア依存を低減する戦略的取得と位置づけられる。

**根拠** — Tenstorrent との協議も含め、Qualcomm は Nvidia 中心の AI 開発に対する $140B+ 規模の代替戦略を進めているとされる。Modular の MAX エンジンと Mojo はハード非依存の推論スタックを標榜。

**影響** — 推論レイヤの「脱 Nvidia」選択肢が大手主導で具体化。中長期的にはハードウェア多様化とコスト構造の変化につながりうるが、当面は開発者の実利用エコシステムが鍵。

**行動指針** — 推論コストの最適化を検討中なら Mojo / MAX の動向をウォッチリストに追加。短期の本番採用判断はエコシステム成熟を見極めてから。

- （出典 URL は 03_ai-news-industry 当日ダイジェスト参照）

## カテゴリ別まとめ

### Anthropic / Claude
- **Fable 5 / Mythos 5 輸出規制**（ハイライト参照）。Mythos 5 は約 100 の米重要インフラ・政府機関に限定復旧
- **収益が加速** — Anthropic の年間ラン・レートが約 $30B に到達（2025 年末の約 $9B から約 3.3 倍）。年間 $1M 以上を支出するエンタープライズ顧客は 1,000 社超
- **Claude Code は v2.1.195（6/26）から更新なし**。既報の修正（ハイフン入り識別子の hook matcher 完全一致化、`CLAUDE_CODE_DISABLE_MOUSE_CLICKS`、日本語・中国語・タイ語の音声 auto-submit 修正、Remote セッション起動の provisioning チェックリスト）が最新 / https://code.claude.com/docs/en/changelog
- 本日 6/30 に Anthropic「The Briefing: AI for Science」ライブ配信（10:00 PDT）

### OpenAI / Codex
- **GPT-5.6（Sol/Terra/Luna）は限定プレビュー継続** — 一般提供は「数週間内」。審査済みパートナーに API/Codex で先行。料金 Sol $5/$30、Terra $2.50/$15、Luna $1/$6（per 1M）。明示的キャッシュ breakpoint・30 分最小キャッシュ寿命を導入 / https://openai.com/index/previewing-gpt-5-6-sol/
- **Codex CLI 0.142.4（6/29）/ 0.142.3（6/26）は保守リリース**（ユーザー向け変更なし）。実質最新機能は 0.142.2（MCP ツール検索の既定化・PowerShell AST 承認強化）。次期 0.143 系は alpha 開発中 / https://github.com/openai/codex/releases

### Google / DeepMind
- **Gemini 3.5 Pro が 6 月期限を逸し 7 月へ**（ハイライト参照）

### Microsoft / GitHub
- **M365 Copilot 6 月アップデート** — Word/Excel/PowerPoint のエージェントがマルチステップ・ワークフロー向けに GA。Microsoft Scout（Autopilot エージェント）・Copilot Cowork が GA。宣言型エージェントが GPT-5.1 へ更新（自動モデル選択）。**Copilot Chat に Claude がモデル選択肢として追加**
- **GitHub Copilot CLI pre-release v1.0.66-2（6/29）** — 異なるプラグイン由来の同名 skill が共存可能に、Integrations が CLI ユーザー設定を読み書き可能、`/lsp logs` で LSP サーバーログ閲覧。安定版は v1.0.65（6/24）のまま / https://github.com/github/copilot-cli/releases
- **ガバナンス**: 機密度ラベルが「すべてのコンテンツ分析エクスペリエンス」（Copilot のファイル要約含む）をブロックするよう変更

### Copilot Studio / Power Platform（本日 6/30 が期限の変更）
- **Copilot Studio クラシック作成終了** — Teams 内のクラシックエージェント作成が本日終了、Web アプリへリダイレクト（MC1315217）。既存エージェントは継続動作
- **Copilot Cowork 従量課金設定の期限** — 未設定テナントは 7/1 にアクセス喪失（早期採用者は移行猶予あり、課金は 7/1 開始）。Copilot Credit は「$0.01/credit」
- **M365 価格ロック失効** — 7/1 から E3 $36→$39、E5 $57→$61、Copilot Business $18→$21
- **認定の廃止** — APL-4002（Copilot セキュリティ/コンプライアンス）と APL-7008（Studio カスタムエージェント）が今月廃止

### Cursor / 開発ツール
- **Cursor for iOS 公開ベータ開始**（6/29） — 全有料プランで提供。モバイルアプリからリポジトリを選んで always-on エージェントを起動・管理でき、デスクトップ同等の操作感。Codex Remote（ChatGPT）に続くモバイル発エージェント操作の流れ / https://cursor.com/changelog

### 市場・業界
- **AI チャット市場シェア（2026 年 4 月）** — ChatGPT 54.7% / Gemini 27.4% / Claude 8.2% / DeepSeek 4.1% / Grok 2.8%
- **Qualcomm が Modular を約 $3.9B で買収**（ハイライト参照）

## 直近の注目予定

- **6/30（本日）**: Anthropic「AI for Science」ライブ配信（10:00 PDT）/ Copilot Studio クラシック作成終了 / Copilot Cowork 課金設定期限 / M365 価格ロック失効 / Devin classic 環境設定廃止 → declarative blueprints 移行 / GPT-5.2・5.3-Codex 新規 API 利用不可化 / Gemini 3.5 Pro「6 月内公開」予測の期限
- **〜7 月上旬**: Fable 5 US 復旧（Pentagon/NSA 署名待ち）/ GPT-5.6 一般提供（数週間内）/ Claude Partner Network 初回昇格レビュー
- **7/8**: Anthropic 政府発行 ID・生体情報検証ポリシー施行
- **7 月中旬**: GPT-5.6・Gemini 3.5 Pro・Claude Opus 4.7 のローンチ集中報道
- **7/17**: Claude Corps 第 1 期応募締切
- **8/1**: covered frontier model フレームワーク 60 日 EO 期限
- **8/3**: 旧「Claude in Slack」アプリ退役
- **8/5**: Opus 4.1 Claude API 退役
- **8/26**: OpenAI Assistants API 廃止 / o3 退役 / GPT-4.5 完全廃止
- **9 月**: iOS 27 / macOS 27 GA（AFM 3 本番）

## 改善メモ

- 3ソースとも当日分を取得・統合済み（欠損なし）。ただし 02・03 の原文 URL は WebFetch が要約整形したため一部未取得。次回は raw 取得時に URL 抜けがないか確認したい
- Qualcomm × Modular 買収の一次出典 URL（03_ai-news-industry）を次回ダイジェストで補完したい
- releasebot の Claude 更新スニペットが Managed Agents の self-hosted sandboxes / MCP tunnels（5/26 発表）を「公開ベータ」と新規表示しやすい点に注意。一次の発表日を確認し既報扱いとする（01 側の指摘を継続）
