# AI News Daily Summary — 2026-07-13

> 本サマリーは 01_ai-news-Master・02_ai-news-Copilot・03_ai-news-industry の3ソース（7/13分）を統合して作成。

月曜・週末明けで**本日発の大型モデルローンチはなし**。開発ツールも Claude Code v2.1.207 / Cursor 3.11 / Codex CLI alpha いずれも据え置きで、唯一 **GitHub Copilot CLI が v1.0.70 で GPT-5.6 対応・シェルサンドボックス制御を追加**。動きの中心はエンプラ導入の実態データで、最重要は **VentureBeat Research の企業リーダー573名調査**——「社内評価をパスしたエージェントが顧客対応で失敗」「本番投入が統制を追い越す」実態を定量化した提案根拠向けの一次データ。あわせて **Bun の Zig→Rust 全面移植を Claude Fable 5 が11日・約$165kで完遂**（AI支援大規模移行のROIの実像）、**Fable 5 の有料プラン無償提供が 7/12 で終了**し週次利用上限の対象外へ移行した点を捕捉。Apple の OpenAI 提訴（7/10）は Master が本日補足したが日次サマリーでは前日 7/12 に詳報済み。Microsoft 一次情報は静穏継続。

## 今日のハイライト

### 1. エンタープライズAIエージェントの「評価ギャップ」— 統制が本番投入に追いつかない（VentureBeat Research）

**事実**: VB Transform 2026（7/14-15・Menlo Park）に先立ち、VentureBeat Research が **従業員100名以上の企業リーダー573名**（オーケストレーション/信頼性・評価/セキュリティ・ID/インフラ・計算/コンテキスト・RAG の5調査、いずれも2026年6月実施）を対象にした一連の調査を公開。**半数の企業が「社内評価をパスしたエージェント/LLM機能が顧客対応で失敗」を経験**（うち4社に1社は複数回）、にもかかわらず **66%が人間レビューなしの本番投入を一部許可済み、または今後12カ月で構築予定**。自社GPUを運用する企業の **86%が稼働率50%以下**、27%が「請求書が来て初めてエージェントのコストを知る」リアクティブ統制のみ。

**根拠**: 直近6月実施の573名規模という定量ベース。自律度の上昇（本番投入）が保証（評価・ガードレール・人間レビュー・コスト上限）の整備を追い越しているという構造を、単発の逸話ではなく分布として示した。

**影響**: (1) エージェント導入の論点は「モデル選定」より「評価・ガードレール・人間レビュー境界・エージェント単位のコスト上限」の設計に移る。(2) GPU 稼働率50%以下は「AIバブル論」に対し現場の過剰投資を実データで裏づけ、内製インフラの TCO 精査（クラウド従量 vs 自社GPU）の切り口になる。(3) API 鍵の共有によるエージェント群の露出（別調査で69%）はセキュリティ設計の宿題。

**行動指針**: エージェント案件の提案では PoC 設計に「本番投入前の評価ゲート・人間レビュー境界・エージェント単位の予算/上限・API鍵の分離」を必須要件として組み込む。数値は「直近の企業リーダー573名調査」として提案書に引用可能。GPU 稼働率データは内製インフラの投資妥当性レビューの起点に使う。

- https://venturebeat.com/orchestration/enterprise-ai-is-entering-an-evaluation-gap-agents-are-gaining-autonomy-faster-than-companies-can-verify-them
- https://venturebeat.com/orchestration/wall-street-is-debating-the-ai-buildout-enterprises-just-answered-86-say-their-gpus-run-at-half-capacity-or-less

### 2. Bun の Zig→Rust 全面移植を Claude Fable 5 が11日で完遂 — AI支援大規模リファクタリングのROIの実像

**事実**: JavaScript ランタイム Bun が、**約53.5万行の Zig コードを Claude Fable 5 で11日間（作業5/3〜5/14、純コーディング約6日）で Rust へ全面移植**（7/10 Publickey・7/12 GIGAZINE 等が報道、Zig 作者も反応）。「implementer/reviewer」を分けた並列ワークフローで **Claude を最大64インスタンス並走**、Claude Code 内で約50の動的ワークフローを実行し、100万行超の生成を検証しながら進めた。定量成果は 2,000ビルドのストレステストで**メモリ 6.7GB→609MB・性能+2〜5%・バイナリ約20%縮小**、API 換算コスト **約$165,000**（非キャッシュ入力59億トークン、出力6.9億トークン、キャッシュ入力読み72億トークン）。作者は AI なしなら「エンジニア3名×約1年」と試算。

**根拠**: 人月換算3人年 → 11日・$165k という具体数字と、実装役／検証役を分離した並列エージェント運用という設計知見。レガシー言語移行の「AI支援ROI」を語れる数少ない一次事例。

**影響**: モダナイゼーション／言語移行案件の投資対効果の当たりを付ける参照値になる。同時に「最大64インスタンス並走・約50の動的ワークフロー・生成物の検証工程」がコストと品質担保の両面で不可欠だった点は、AI 支援移行を安易な工数削減として売らないための注意材料。

**行動指針**: レガシー移行・大規模リファクタリング提案では、本件を「AI支援で人月×桁の圧縮が起きうる」参照事例として提示しつつ、実装役と検証役の分離・生成物の検証工程・並列エージェント運用コストを見積り前提に含める。$165k・11日は上振れケースとして扱い、対象コード規模・テスト資産の有無で補正する。

- https://www.publickey1.jp/blog/26/javascriptbunclaude_fable_511zigrustclaude.html
- https://gigazine.net/news/20260712-bun-zig-rust/

### 3. Fable 5 の有料プラン無償提供が 7/12 で終了 — 週次利用上限の対象外・クレジット経由へ移行

**事実**: Anthropic「Redeploying Claude Fable 5」に基づく **Pro / Max / Team / premium seat 型 Enterprise 向けの追加課金なし提供が 7/12 23:59 PT で予定通り終了**。**7/12 以降、Fable 5 は各プランの週次利用上限（included weekly usage）にカウントされず、利用クレジット経由での提供に移行**した。公式ドキュメント上も「Fable 5 / Mythos 5 へのアクセスは復旧済み」（6/12 の輸出規制 → 6/30 解除 → 7/1 再展開の一連）と明記され、現行仕様は 1M context / 128k output / $10・$50 で据え置き（Fable 5 は refusal 分類器あり・違反技術を99%+ブロックし Opus 4.8 へリルート、Mythos 5 は分類器なし・Project Glasswing 限定）。

**根拠**: 無償枠の扱いが「週次上限に含む」から「上限対象外・クレジット消費」へ変わる転換点。当初の早期打ち切りへの反発を受けた延長分がここで終わった。

**影響**: Fable 5 を常用ワークフロー（上のような大規模移行含む）に組み込んでいる利用者は、7/12 以降クレジット消費ベースでのコスト計上に切り替わる。無償枠前提で回していた PoC・検証の実コストが顕在化する。

**行動指針**: Fable 5 を使う社内・顧客ワークフローのコスト前提を「週次上限内の無償」から「クレジット消費」に更新する。大規模ジョブ（移行・一括リファクタリング）では上記 Bun 事例のトークン規模を参考に、事前にクレジット消費の見積りを取る。

- https://www.anthropic.com/news/redeploying-fable-5
- https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5

## カテゴリ別まとめ

### Anthropic / Claude
- **Fable 5 無償提供の終了・週次上限対象外へ**（ハイライト参照）。
- **Claude Code v2.1.207（7/11）** が最新のまま、7/12 から新版なし。**本日 7/13 は週次上限+50%プロモ（5月開始）の期限**で、延長発表は未確認。
- **Bun の Zig→Rust 移植を Fable 5 が完遂**（ハイライト参照）。Anthropic Reflect（7/9）以降の公式 news 新規なし、UST 提携（7/8 発表・7/10 続報）以降の続報なし。

### 開発ツール（Copilot CLI / Claude Code / Cursor / Codex CLI）
- **GitHub Copilot CLI v1.0.70（7/9・回収）** — 本日唯一の版更新。**GPT-5.6 モデル対応**を追加、**`--sandbox` / `--no-sandbox` フラグ**でセッション単位のシェルサンドボックス挙動を制御、プロンプト書き換え用 **`/refine`** を新設、ページング対応の MCP リソース管理を追加。**信頼済みリポジトリ設定（`.github/copilot/settings.json`）** でモデルと reasoning effort をリポジトリ単位でピン留め可能に。 https://github.com/github/copilot-cli/blob/main/changelog.md
- **Claude Code / Cursor / Codex CLI**: いずれも据え置き。Claude Code v2.1.207（7/11）、Cursor 3.11（7/10・Side Chats）、Codex CLI alpha 0.145.0-alpha.4（7/11）／安定版 0.144.1。週末を挟み新バージョン・新 pre-release なし。

### OpenAI / ChatGPT
- **Apple による提訴**（7/10・前日 7/12 サマリーで詳報済み）。Master が本日 ※新規 として補足掲載したが、日次では既報。消費者ハードウェア戦略・IPO バリュエーションへの影響が焦点。
- GPT-5.6 GA（7/9）以降の新機能なし。**ChatGPT Team への全面提供は 7/14 予定**（本日時点で追加報なし）。Enterprise の文脈長は 1.5M トークン（GPT-5.5 の 400K の約3.75倍）。

### Google / DeepMind
- **Gemini 3.5 Pro** は限定 preview 継続。第三者報道は **7/17 GA 目標**で一致するが、Google 公式のモデルカード・API ドキュメント・確定価格は未発表。2M トークン文脈・Deep Think 層を予告、Vertex AI 限定プレビュー継続。

### Microsoft / Copilot / Power Platform（一次情報の動きなし）
- **一次情報は静穏継続（Learn MCP で一次確認）**: Copilot Studio Released Versions は Build 2026.6.3（6/30）のまま、次ビルド 2026.7.x は未反映（版ページは火曜更新、**次回 7/14 が要監視**）。What's New は June 2026 セクションのまま7月項目なし。M365 Copilot Release Notes は July 01 バッチが最新で off-cycle なし（次バッチは 7/14〜7/15 前後見込み）。
- 月次「What's New in Power Platform: July 2026」は未公開（最新は 6/11 の June Feature Update）。2026 Release Wave 2 計画ページも未公開（7月中旬〜下旬公開見込み）。**破壊的変更**: Visio → Power Automate エクスポート廃止が 7/14 発効。

### OSS・ローカルLLM
- **推論エンジン「Colibrì」（Pure C・依存ゼロ）が 744B の GLM-5.2 を約25GB RAM のコンシューマ機で実行**（7/10・HN 453ポイント）。密部（int4で約9.9GB）のみ常駐、21,504のルーテッド・エキスパート（計約370GB）をディスクから LRU キャッシュでストリーミング、MLA 注意（KVキャッシュ57倍圧縮）・投機的デコード等で省メモリ化。速度は 0.05〜1 tok/s（常用不可・動作実証レベル）だが、**API 契約前に大型OSSモデルを数千プロンプトで検証する「フィージビリティ用ローカル実行」**やオンプレ・機密データ環境での評価手段として意味を持つ。 https://github.com/JustVugg/colibri

### SpaceXAI / Grok
- Grok 4.5 一般公開（7/8〜7/9）以降の新規進展なし。EU 提供は 7 月中旬めど（EU AI Act の systemic risk 分類による遅延、確定日なし）。

## 直近の注目予定

- **7/13（本日）**: Claude Code 週次上限+50%プロモの期限（延長発表は未確認）
- **7/14**: ChatGPT GPT-5.6 の Team 全面提供予定 / iOS 27 Public Beta 公開予定（〜7/14 頃）/ Copilot Studio 版ページ次更新（2026.7.x 反映見込み）/ M365 Copilot Release Notes 次バッチ見込み / VB Transform 2026 開幕（〜7/15）/ 破壊的変更: Visio → Power Automate エクスポート廃止発効
- **7/15**: Claude Science（AI for Science）応募締切 / 新 M365 Copilot アプリ UI（MC1325422）の opt-out トグル終了・以降デフォルト化
- **7/17**: Claude Corps 第 1 期応募締切 / Gemini 3.5 Pro GA 候補日（未確定）
- **7/21**: Copilot Cowork GA 告知イベント
- **7/23**: OpenAI computer-use-preview シャットダウン
- **7/31**: Devin classic 環境設定の read-only 参照終了
- **8/1**: covered frontier model 大統領令 60 日期限
- **8/3**: 旧「Claude in Slack」退役
- **8/5**: Opus 4.1 Claude API 退役 / Cowork 倍増利用枠の終了
- **8/26**: OpenAI Assistants API 廃止 / o3 退役 / GPT-4.5 完全廃止
- **8/31**: Sonnet 5 促進価格終了（$2/$10 → $3/$15）
- **9 月**: iOS 27 / macOS 27 GA（AFM 3 本番）

## 改善メモ

- **既報の版番号確定**: GitHub Copilot CLI は 02 が本日 v1.0.70（7/9・回収）を一次確認。前日 7/12 サマリーで指摘した 01（v1.0.71-0 pre-release / v1.0.70 安定版）との版番号差異は、安定版 v1.0.70 で整合。02 側の版番号取得ロジックは追跡継続。
- **既報の重複整理**: Apple の OpenAI 提訴（7/10）を Master が本日 ※新規 として掲載したが、日次サマリーでは前日 7/12 にハイライトとして詳報済み。二重掲載を避け本日は既報として扱った。
- **障害の変化なし**: RSS/WebFetch は x.ai/*・cursor.com/changelog・anthropic.com/news・wave2 planned-features 等で 403 継続（各ソースとも WebSearch・二次ソースで補完）。取得方法の WebSearch 優先化提案（03 の B-004、14 回目）が継続中。
- **ソース間整合**: Fable 5 無償提供終了・Bun 移植・Copilot CLI v1.0.70・VentureBeat 調査の各件で 3 ソース間の内容矛盾は検出されず。
