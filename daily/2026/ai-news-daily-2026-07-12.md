# AI News Daily Summary — 2026-07-12

> 本サマリーは 01_ai-news-Master・02_ai-news-Copilot・03_ai-news-industry の3ソース（7/12分）を統合して作成。

日曜。**本日発の大型ローンチはなし**だが、業界地図を揺らす一件が浮上。最重要は **Apple が OpenAI を営業秘密窃取で提訴し、刷新版 Siri を OpenAI ではなく Google Gemini ベースに切替**——プラットフォーマー×AIラボの提携が固定的でないことを示す再編。あわせて **エージェントが自社の $100M 調達を主導した Lyzr**（エージェント自律の実証）、**総額1兆円規模の国産フィジカルAI連合「Noetra」始動**（主権AI）を捕捉。開発ツールは Claude Code v2.1.207（Auto mode デフォルト化）・Cursor 3.11（Side Chats）と定常更新、**Anthropic は Fable 5 の有料プラン無償提供を本日 7/12 で終了**。Microsoft 一次情報は静穏継続。

## 今日のハイライト

### 1. Apple が OpenAI を提訴、刷新版 Siri は Gemini ベースへ — 主要プレイヤーの提携が再編局面に

**事実**: Apple が OpenAI・そのハードウェア子会社 io Products・元Apple社員2名（最高ハードウェア責任者 Tang Tan、元シニア電気系エンジニア Chang Liu）を営業秘密窃取で北カリフォルニア連邦地裁に提訴（7/10）。「技術スタッフから最高ハードウェア責任者に至るあらゆる階層で Apple の営業秘密・機密情報を盗用」と主張し、採用面接を通じたハードウェア機密の抽出も指摘。同時に、今秋の刷新版 Siri は OpenAI ではなく **Google Gemini ベース**に切り替わると報道され、2024年の「ChatGPT を iOS に統合」提携からの明確な反転となる。

**根拠**: ハードウェア（OpenAI/io の消費者デバイス戦略）とアシスタント（Siri のモデル基盤）の両面で、Apple と OpenAI の関係が協調から対立へ転じた。CNBC・CNN・Benzinga 等が一斉報道。

**影響**: (1) プラットフォーマー×AIラボの提携は固定的でなく、ハードウェア・アシスタント領域で再編が起きうる。(2) 訴訟は OpenAI の消費者ハードウェア戦略と IPO バリュエーションに下押し圧力。(3) 「Siri＝Gemini」採用は Google のコンシューマ／エンタープライズ両面での巻き返しを裏づける。

**行動指針**: 顧客のベンダーロックイン評価では「AIラボとの提携は数年で反転しうる」前提で、モデル基盤の差し替え可能性（抽象化レイヤー・マルチモデル対応）を設計要件に加える。Apple エコシステム前提の提案では Siri のモデル基盤が Gemini に移る可能性を織り込む。

- https://www.cnbc.com/2026/07/10/apple-openai-lawsuit-trade-secrets.html
- https://www.cnn.com/2026/07/10/tech/apple-openai-devices-lawsuit

### 2. Lyzr が自社エージェントに $100M 調達を主導させる — エージェント自律の到達点を実証

**事実**: エンタープライズ向け AI エージェント構築の Lyzr（ニュージャージー）が $100M Series B・評価額約$500M を調達（7/9、Bloomberg/TechCrunch）。自社エージェント「SivaClaw」が130社超の投資家からの質問対応・投資メモ作成・スライド閲覧の食いつき追跡までを担当し、創業者が Sand Hill Road に足を運ぶことなく $400M の関心を集め、実質4倍のオーバーサブスクライブとなった。

**根拠**: 資金調達という高ステークスかつ非定型の業務プロセスをエージェントが主導し、成果（オーバーサブスクライブ）を出した実例。プロダクトのデモを兼ねた調達。

**影響**: 「エージェントは補助ツール」から「エージェントが業務プロセスを代行して成果を出す」への具体的な証拠。エージェント導入提案における「業務代行の到達点」の説得材料になる。

**行動指針**: エージェント案件では、単純作業の自動化にとどめず「非定型・対人・高ステークスの業務プロセス（調達・与信・顧客折衝）をどこまで委任できるか」を PoC の設計軸に据える。委任範囲の拡張に伴うガバナンス（人間の承認ポイント）とセットで提示する。

- https://techcrunch.com/2026/07/09/an-ai-agent-startup-just-let-its-agent-run-its-100-million-fundraise/

### 3. 国産フィジカルAI連合「Noetra」始動 — 総額1兆円規模の国家プロジェクトで主権AIが加速

**事実**: 国産マルチモーダル基盤モデル開発の「Noetra」が 7/1 始動（経産省採択）。産総研とともに産業現場データを安全活用する物理空間認識型の「ワールド基盤モデル」を志向。ソフトバンク・NEC・ソニーグループ・ホンダが中核出資、3メガバンクを含む40社超が出資見込み。経産省が初年度約3,873億円を拠出し、**2030年度まで総額約1兆円規模**。学習済み重みを国内向けに順次公開予定。

**根拠**: 汎用LLM（OpenAI/Anthropic/Google）とは別軸の、フィジカルAI（ロボティクス・製造現場）向け国産基盤モデルへの大型国費投下。

**影響**: 国内エンプラの AI 調達に「主権AI／国産オプション」という新たな選択軸が加わる。特に製造・産業現場データの安全活用が要件の案件で、汎用海外LLMとの棲み分け設計が論点化する。

**行動指針**: 国内製造・産業系の顧客提案では、汎用LLM一択ではなく「国産フィジカル基盤モデル（Noetra 系）との併用・棲み分け」を選択肢として提示できるよう、公開予定の重み・API 提供条件を継続ウォッチする。

- https://www.itmedia.co.jp/aiplus/article/2606/30/2000000138/
- https://www.meti.go.jp/press/2026/06/20260630005/20260630005.html

## カテゴリ別まとめ

### Anthropic / Claude
- **Fable 5 の有料プラン無償提供が本日 7/12 で終了** — Anthropic「Redeploying Claude Fable 5」により、Pro/Max/Team/premium seat 型 Enterprise の対象有料プランで **7/12 23:59:59 PT まで追加課金なしで提供**（当初の早期打ち切りへの反発を受けた延長）。**7/12 以降は Fable 5 が各プランの週次利用上限（included weekly usage）にカウントされなくなる**。無償枠の扱いが変わる転換点。 https://www.anthropic.com/news/redeploying-fable-5
- Anthropic 公式 news は上記のほか新規発表なし。UST 提携（7/8 発表・7/10 続報）以降の続報なし。

### OpenAI / ChatGPT
- **Apple による提訴**（ハイライト参照）。消費者ハードウェア戦略・IPO バリュエーションへの影響が焦点。
- GPT-5.6 GA（7/9）・ChatGPT Work・Codex 統合デスクトップアプリ以降の新規なし。Team 全面展開は 7/14 予定（本日時点で追加報なし）。

### Google / DeepMind
- **刷新版 Siri の基盤に Gemini 採用**（ハイライト参照）。コンシューマ領域での巻き返しの裏づけ。
- **Gemini 3.5 Pro** は限定 preview 継続。AI Studio whitelist preview（7/8〜12）、Vertex 企業向け（7/15 頃）、GA（7/22〜28）との段階展開報道はあるが未確定で、公式モデルカード・API ドキュメント・確定価格は未公表。7/17 GA 目安は据え置き。

### Microsoft / Copilot / Power Platform
- **一次情報は静穏継続**: Copilot Studio Released Versions は Build 2026.6.3（6/30）のまま、次ビルド 2026.7.x は未反映（次回火曜 **7/14** が要監視）。M365 Copilot Release Notes は July 01 バッチが最新で off-cycle なし（次バッチは 7/14〜7/15 前後見込み）。月次「What's New in Power Platform」の July 更新も未公開。
- **破壊的変更**: Visio → Power Automate エクスポート廃止が 7/14 発効。

### 開発ツール（Claude Code / Cursor / Copilot CLI / Codex CLI）
- **Claude Code v2.1.207（7/11）** — **Bedrock / Vertex AI / Foundry で Auto mode が opt-in（`CLAUDE_CODE_ENABLE_AUTO_MODE`）なしでデフォルト有効化**（無効化は settings の `disableAutoMode`）、**Bedrock / Vertex / Claude Platform on AWS の既定モデルを Opus 4.8 に変更**。セキュリティ修正: プラグイン hooks/monitors/MCP の shell-form コマンドで `${user_config.*}` を拒否（shell-injection 対策）、非対話実行（`claude -p`/SDK）でリモート管理設定が同意ダイアログ非表示のまま consent 記録される不具合を修正。ほか長文ストリーミング時の端末フリーズ、agent teams の mailbox 不正メッセージによるクラッシュループ、auto-updater のカスタムランチャー上書き等を修正。 https://code.claude.com/docs/en/changelog
- **Cursor 3.11（7/10）** — **Side Chats**（メインの agent 会話を止めずに脱線調査できる並走チャット。`/side`・`/btw`・チャットパネルの + から作成、メインの文脈を引き継ぎ後から本流へ at-mention で戻せる）、agent transcript の検索強化（名前/PR 番号を超えた検索、会話内 Cmd+F ジャンプ）、project/repo ピッカーの簡素化。Cloud Agents に team hooks、Cursor Teams が MCP 統合対応。 https://cursor.com/changelog
- **GitHub Copilot CLI**（7/10）— pre-release **v1.0.71-0** で `/settings` に pinned prompts 設定・リポジトリスコープタブ追加、セッション終了/サイドバー非表示のキー変更、interactive shell 再設定エラーのリトライ扱い化。安定版は **v1.0.70**（7/10）据え置き。 https://github.com/github/copilot-cli/releases
- **OpenAI Codex CLI** — alpha が 7/9〜7/11 で 0.145.0-alpha.1→alpha.4 まで急速反復（installer 信頼性・code-mode）。安定版は 0.144.1（7/9）据え置き。 https://github.com/openai/codex/releases

### SpaceXAI / Grok
- Grok 4.5 一般公開（7/8〜7/9）以降の新規進展なし。EU 提供は 7 月中旬めどのまま。

### 資金調達・業界動向
- **Lyzr $100M Series B**（ハイライト参照）。
- **Noetra 始動・総額1兆円規模の国家プロジェクト**（ハイライト参照）。

## 直近の注目予定

- **7/12（本日）**: Fable 5 の有料プラン無償提供終了（23:59 PT）→ 以降は週次利用上限の対象外に
- **7/13**: Claude Code 週次上限+50%プロモの期限（延長なき場合）
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

- **前日の取りこぼし補足**: 前日 7/11 のダイジェストが Apple の OpenAI 提訴・Siri→Gemini 切替（7/10）を取りこぼしていたため、03 が本日補足掲載。日次サマリー側でも本日のハイライトとして反映済み。
- **障害の変化なし**: RSS/WebFetch は x.ai/*・Anthropic news・github.blog・cursor.com/changelog 等で 403 継続（各ソースとも WebSearch・二次ソースで補完）。取得方法の WebSearch 優先化提案（03 の B-004、13 回目）が継続中。
- **ソース間の版番号差異**: GitHub Copilot CLI の版番号で 01（pre-release v1.0.71-0 / 安定版 v1.0.70、7/10）と 02（v1.0.69・7/7 として言及）に食い違い。より新しく詳細な 01 を採用し v1.0.70/71-0 で記載。次回、02 側の版番号取得ロジックの確認が必要。
- **ソース間整合**: Claude Code v2.1.207・Cursor 3.11・Fable 5 延長・Apple/OpenAI・Lyzr・Noetra の各件で 3 ソース間の内容矛盾は検出されず（版番号差異のみ上記）。
