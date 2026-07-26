# AI News Daily Summary — 2026-07-27

> 本サマリーは 01_ai-news-Master・02_ai-news-Copilot・03_ai-news-industry の3ソース（7/27分）を統合して作成。

月曜の主戦場はオープンウェイト。Moonshot AI が **Kimi K3** の 2.8兆パラメータ重みを本日 9:00 JST に公開予定（各ソースの執筆時点では未公開）。同じ論点で米国側は割れており、規制反対書簡の署名が1日で25社→50社に倍増する一方、Anthropic と Amazon は不参加、トランプ政権は中国製モデルの調達締め出しを検討中。プロダクト面は Microsoft 一次がすべて据え置きで、実務に効くのは Claude API 7/24 分の破壊的変更2件、および取りこぼし回収の Claude Security プラグイン・Cursor Router・Devin マルチリポスキャン。

## 今日のハイライト

### 1. Kimi K3 の重み、本日 9:00 JST 公開予定 — 公開ウェイト史上最大

**要点**: Moonshot AI が **Kimi K3** の重みを本日 9:00 JST に公開予定。公開ウェイトとして史上最大で、自前ホストなら中国側APIへのデータ送信を避けられる。

**詳細**: **2.8兆パラメータ**の MoE（896エキスパート中16のみ発火）・1M トークン文脈・ネイティブ画像入力。7/16 に API 提供を開始してから11日での重み公開で、ライセンスは Modified MIT（商用利用可）。容量は BF16 で約594GB、MXFP4（4bit 浮動小数点＋ブロック単位スケール）量子化でも **約1.4TB** が高速メモリに必要で、実験用途でも H100 80GB が4〜8基必須。KV キャッシュと実行時オーバーヘッドは別枠。コンシューマ機は量子化しても load 不可。各ソースの執筆時点（4:00／5:06 JST）では未公開。

**意味**: API を中国側に通さずに frontier 級コーディングモデルを動かせる選択肢が初めて出る。ただし 7/22-23 の蒸留疑惑・制裁リスク（モデル出自の問題）は重みを落としても消えず、1.4TB の要件で自前運用は実質大企業限定。中堅以下は結局ホスト型 API 経由になり、同じデータ論点に戻る。

- https://huggingface.co/blog/ResterChed/kimi-k3-model-overview-mxfp4-quantization-open-wei
- https://venturebeat.com/technology/chinas-moonshot-ai-releases-kimi-k3-the-largest-open-source-model-ever-rivaling-top-u-s-systems
- https://www.techtimes.com/articles/321551/20260725/kimi-k3-open-weights-arrive-sunday-self-hosting-cuts-china-data-risk-api-never-can.htm

### 2. オープンウェイト書簡が50社に倍増、Anthropic は不参加 — 政策リスクが調達要件の話に

**要点**: ダウンロード可能なモデルの規制反対書簡が1日で **50社** に倍増。Anthropic と Amazon は不参加で、クローズド専業ほど規制強化で利する構図が可視化された。

**詳細**: 7/24、NVIDIA CEO Jensen Huang が人生初のX投稿で書簡「Open Weights and American AI Leadership」を公開。「時期尚早な規制」に反対する内容で、当初 **25社**（Nvidia／Microsoft／Meta／IBM／Dell／Palantir／Hugging Face／Mozilla／Linux Foundation 等）が署名し1日で倍増した。OpenAI は不参加を広く指摘された後に署名。背景は Axios 7/20 報道で、トランプ政権が中国製AIモデルの事実上の締め出しを検討中。手段は直接禁止でなく、制裁リスト・サイバー警告・企業責任ルール・連邦調達規則（契約企業に中国製モデル利用を禁止）の組み合わせで、大統領令・正式規則は未署名の「検討中」段階。契機は Kimi K3 と、OpenRouter 上の中国製モデルのトークン比率 **46.4%**。

**意味**: 中国製オープンモデル採用の政策リスクが、将来の懸念から具体的な調達要件の話に移りつつある。官公需・防衛関連の取引がある顧客では、モデル出自が調達条件として問われうる段階に入った。ハイライト1のセルフホスト論と正面から衝突する。

- https://www.cnbc.com/2026/07/24/nvidia-microsoft-meta-open-weight-ai-models.html
- https://www.tomshardware.com/tech-industry/artificial-intelligence/nvidia-and-24-other-companies-sign-open-weights-letter-as-washington-weighs-chinese-ai-model-ban
- https://fortune.com/2026/07/24/jensen-huang-open-source-letter-nvidia-kimi/
- https://cryptobriefing.com/trump-white-house-ban-chinese-ai-models/

### 3. Claude API 7/24 分に破壊的変更2件 — Opus 5 発表の陰で未報告

**要点**: Opus 5 では thinking 無効化と effort `xhigh`／`max` の併用が **400 エラー**になる。Opus 4.7 の fast mode も廃止された。

**詳細**: Opus 5 リリースと同日の Platform release notes に、モデル本体以外の実務直結項目が入っていた。破壊的変更は ① Opus 5 で `thinking: {"type":"disabled"}` を effort `xhigh`／`max` と併用すると 400（Opus 4.8 からの挙動変更。無効化できるのは effort `high` 以下）、② **Opus 4.7 の fast mode** を廃止し、`claude-opus-4-7` に `speed:"fast"` を投げるとエラー。Opus 4.6 と違って標準速度へのフォールバックもしない。beta 追加は ③ 会話途中のツール差し替えが Fable 5／Mythos 5／Opus 4.8／Opus 5 で提供（`mid-conversation-tool-changes-2026-07-01` ヘッダ）、④ `fallbacks` パラメータに `"default"` モード追加で、拒否カテゴリ別に推奨フォールバックモデルを自動適用（`server-side-fallback-2026-07-01` ヘッダ）。

**意味**: Opus 4.7 の fast mode や thinking 無効化に依存した既存実装は、Opus 5 への移行時にそのまま落ちる。③は**プロンプトキャッシュを保持**したままターン間でツールを追加・削除できるため、長いエージェントループでツール構成を切り替えるとキャッシュが飛ぶ問題への直接の回答になる。

- https://platform.claude.com/docs/en/release-notes/api

## カテゴリ別まとめ

### Anthropic / Claude

- Opus 5 が第三者ベンチでも首位（続報）— Artificial Analysis の Intelligence Index で **61** を記録し1位（Fable 5 が60、GPT-5.6 Sol が59）、Agentic Index もローンチ当日に首位。ARC-AGI-3 は **30.2%** で次点の約3倍。価格 $5／$25（100万トークン）は Opus 4.8 と同額据え置きで、Fable 5（$10／$50）の半額。値上げなしの世代交代が確認できたため、Opus 4.8 前提の既存見積りは価格そのままで性能を上げられ、Fable 5 用途のうち半額で足りるものの棚卸しが直近のコスト削減余地。 https://www.developersdigest.tech/blog/claude-opus-5-hn-analysis / https://kingy.ai/blog/claude-opus-5-specs-benchmarks-pricing/
- Claude Security プラグインが **public beta**（7/22・catch-up）— Claude Code のターミナルから `/claude-security` で Scan codebase／Scan changes／Suggest patches の3モードを実行。複数エージェントがコードベースのマッピング→脅威の洗い出し→ファイル横断・業務ロジック横断の関連付け→findings の独立再検証→修正パッチ付きレポートと分業するため、パターンマッチ型が取りこぼす injection・認証バイパス・メモリ破壊・ロジック欠陥を狙う。要件は有料プラン＋Claude Code v2.1.154 以降、`/config` で dynamic workflows 有効化、PATH 上に `python3`（3.9.6+）と Git。組織単位の有効化は `claude.ai/admin-settings/claude-code`。 https://claude.com/product/claude-security
- Claude API の破壊的変更2件＋beta 2件（ハイライト参照）
- run-rate は $47B（5月中旬）— 推移は2025年末 $9B → 2月 $14B → 3月 $19B → 4月 $30B → 5月 $47B。5/28 の Series H は $65B 調達・$965B post-money、6/1 に極秘S-1提出済みで 7/18 時点でも EDGAR に公開S-1・S-1/A は未掲載、ティッカー・価格レンジ・取引所も未発表。10月上場目標に対しセカンダリ実勢は約 $1.2T 相当、社内目標は2028年に売上$70B・キャッシュフロー$17B。industry 台帳は 07-04 時点の「$30B超」から訂正。 https://sacra.com/c/anthropic/
- Opus 5（7/24）以降の新規発表なし。

### 開発ツール（Cursor / Devin / Claude Code / Copilot CLI / Codex）

- **Cursor Router**（7/22・catch-up）— Auto モードが Cursor Router に置き換わり、リクエストごとに内容を解析してフロンティアモデルが必要な処理だけ高価なモデルへ振り分ける。最適化モードは Intelligence／Balance／Cost の3段階。組織導入に効くのは管理面で、チーム／グループ単位の有効化、メンバーが選べる最適化モードの制限、既定モードの設定、個別モデルの許可・ブロックを管理者側で制御できる。提供は Teams / Enterprise から。 https://cursor.com/changelog/router （403 のため二次照合: https://cursor.com/blog/router ）
- **Devin** のマルチリポジトリコードスキャン（7/17・catch-up）— 1回のスキャンで複数リポジトリを横断でき、リポジトリ別の詳細表示と検出結果のリポジトリフィルターが付いた。Security Swarm（7/1）の単体リポジトリ前提という制約の解消にあたる。同日のエンタープライズ管理強化では、全組織へ自動共有されるシークレット管理、ACU 使用量表示の可否制御、組織横断の MCP サーバー許可リスト強制、特定 Devin ビルドのピン留めと旧版へのロールバックが入った。テナント統制では MCP 許可リストとビルド固定が実務的に効く。 https://docs.devin.ai/release-notes/2026 （403 のため二次照合）
- **据え置き**: Claude Code v2.1.220（7/25）、GitHub Copilot CLI v1.0.75（7/24）はいずれも新版なし。Codex CLI も安定版 0.145.0（7/21）のままで、`0.146.0-alpha.10.1`（7/25 20:29 UTC）以降の新規ビルドはなく、公開リリースノートにも具体的な変更記載なし。 https://github.com/openai/codex/releases

### エージェント運用・市場データ

- 統制レイヤーのベンダー再編（続報）— VentureBeat Research の6月調査（5並行サーベイ・計573名。Agentic Orchestration 101／Agent Reliability & Evals 157／Agentic Security & Identity 107／AI Infrastructure & Compute 107／Context Layers・RAG 101）。測定した5レイヤーすべてで **57〜68%** の企業が12カ月以内にベンダーの変更または追加を計画し、約1/3は四半期内に動く。結論は「プラットフォームの問題ではなく展開の問題」で、多くの企業が実態はチャットボットのものをエージェントと呼んでいる。1年以内に総入れ替えされる前提なら、提案は特定製品固定より差し替え可能な構成のほうが顧客の乗り換えコストを抑えられる。 https://venturebeat.com/technology/venturebeat-research-where-enterprise-ai-agent-governance-hasnt-caught-up
- ChatGPT と Claude が同日に音声操作を強化（7/23）— OpenAI は ChatGPT Voice のデスクトップ版（macOS / Windows）を投入し、ChatGPT Work と Codex を音声のみで操作、AIの発話に割り込んで指示を差し込める（基盤は 7/8 の全二重音声モデル GPT-Live）。Anthropic も同日に Claude 音声モードを刷新し、会話中に外部ツール連携を呼び出せるようにした。エージェントの操作UIがチャット欄から音声へ広がり、長時間タスクの進捗確認と軌道修正のコストが下がる方向。 https://www.itmedia.co.jp/aiplus/article/2607/24/2000000218/

### Microsoft / Copilot Studio（一次すべて据え置き）

- Copilot Studio What's New: June 2026 節のままで7月節は未公開。外部モデルは Claude Sonnet 5 / GPT-5.5 Chat が GA 最新で、**Opus 5 は未追加**（Foundry では提供済み）。 https://learn.microsoft.com/en-us/microsoft-copilot-studio/whats-new
- M365 Copilot Release Notes: `July 15, 2026` バッチが最新のまま。2026年の 7/22・7/29 バッチが未公開であることを一次確認。次バッチは隔週傾向で 7/29 前後見込み。 https://learn.microsoft.com/en-us/copilot/microsoft-365/release-notes
- Released Versions（Copilot Studio）: Build `2026.6.3`（6/30初出）が最新のまま、予告の 2026.7.x は未反映。リージョン分布も無変化（2026.6.3 = 11リージョン／UK・Asia・UAE・Japan・Europe = 2026.6.2／Australia・US 本体・GCC = 2026.6.1）。版ページは火曜更新のため次の要監視は 7/28。
- **ソース構造の変化（要確認）**: Copilot Studio の Release Wave 計画ページ（`release-plan/2026wave1/microsoft-copilot-studio/planned-features`）を Learn MCP で取得すると、計画機能テーブルではなく M365 Roadmap ページの内容が返る。Power Platform 全体版（`release-plan/2026wave1/`）は従来どおりのため当該パス固有。7/2 告知の「Copilot Studio / Sales・Finance・Service Agent のロードマップを M365 Roadmap へ移行」がドキュメント側のリダイレクトとして反映された可能性が高いが、WebFetch 403・旧 URL が検索インデックス上は生存のため断定は避ける。
- その他: Power Platform の新規非推奨項目なし（直近は Visio → Power Automate エクスポート廃止・7/14 発効）。Message Center の新規検知なし。Power Platform Blog 月次「July 2026」は未公開（最新は 6/11 の June）。M365 Roadmap の最新 Announcement は 7/9 の GPT-5.6 提供開始のまま。

### Google

- Workspace の AI ブランドを Gemini 側へ再統合（catch-up）— NotebookLM を「**Gemini Notebook**」に改称（7/16 ロールアウト開始）、「Gemini Alpha」プログラムを「Gemini Beta」に改称（7/22 開始・最大15日で段階展開）。Gemini CLI → Antigravity CLI 統合（6/18 停止）と同じ方向で、開発者向け・ナレッジ向けツールがブランド単位で畳まれ続けている。 https://workspaceupdates.googleblog.com/2026/07/notebooklm-now-gemini-notebook.html
- **Gemini 3.5 Pro は未発表** が継続 — 7/21 に Gemini 3.6 Flash / 3.5 Flash-Lite / Flash Cyber の3モデルが公開されたが 3.5 Pro は含まれず。7/16 Bloomberg の「数カ月遅れ」報道から状況変化なし。公開APIは gemini-3.5-flash / gemini-3.1-pro-preview のまま。 https://techcrunch.com/2026/07/21/google-releases-three-new-gemini-models-but-no-3-5-pro/

## 直近の注目予定

- **7/27（月）**: Kimi K3 オープンウェイト公開（00:00 UTC / 9:00 JST）
- **7/28（火）**: Copilot Studio 版ページ 2026.7.x 反映見込み・Released Versions / Release Wave / Power Platform 非推奨の定例更新
- **7/29 前後**: M365 Copilot Release Notes 次バッチ見込み
- **7/30**: M365 Copilot メモリ活用のエージェント提案 GA・拡張機能 What's New 次月次見込み
- **7/31**: Devin classic 環境設定 read-only 参照終了
- **8/1**: covered frontier model 60日 EO 期限
- **8/3**: 旧「Claude in Slack」退役
- **8/5**: Claude Opus 4.1 の Claude API 退役 / Cowork 倍増利用枠終了
- **8/9**: ChatGPT Atlas シャットダウン
- **8/17**: Claude Console 旧 Workbench 退役 ＋ 実験的プロンプトツール API（`/v1/experimental/generate_prompt`・`improve_prompt`・`templatize_prompt`）廃止
- **8/26**: OpenAI Assistants API 廃止 / o3 退役 / GPT-4.5 完全廃止
- **8/31**: Sonnet 5 促進価格終了（→ $3/$15）
- **9月**: iOS 27 / macOS 27 GA（AFM 3 本番）
- **10月**: Anthropic 上場目標
- **要監視**: Copilot Studio 外部モデル選択への Claude Opus 5 追加（Foundry では提供済み）

## 改善メモ

- **不一致: Kimi K3 の起点日**: Master は「7/16 に API 提供を開始」、industry は政策節で「契機は Kimi K3（7/17）」と記載。API 提供開始日と報道・政策上の契機日のどちらを指すかが曖昧なため両論併記とした。
- **不一致: Claude 音声モード**の対応範囲: industry は「Fable 5 を除く全モデルで音声対話が可能」、07-26 の当サマリー（Master 系）は「Haiku 固定から Opus / Sonnet へ拡張」。対応モデル集合の記述が一致しないため、本文は共通部分（会話中の外部ツール連携）に絞った。
- **台帳番号の衝突**: Master の B-012（07-26 追加の Cursor 等ソース）と Copilot の B-012（Release Wave のソース定義見直し）は別台帳の同番号。横断参照時に混同しないこと。
- Master: 新規提案 B-013（403 を「ゲートウェイ拒否」と「オリジン 403」に分類して記録）、B-014（Claude Code Changelog のフォールバック URL を `raw.githubusercontent.com` へ変更）。
- **障害の変化: Master**: `cursor.com` / `forum.cursor.com` / `www.testingcatalog.com` / `simonwillison.net` / `community.openai.com` の5ホストがゲートウェイ拒否（CONNECT 403）と判明。前4者は 07-26 に B-012 でローカル curl 200 を根拠に追加したソースだが、クラウド定期実行からは到達不可のため WebSearch のみで代替。サイト側の復旧待ちでは解消せず実行環境の許可リスト対応が必要（B-013）。`code.claude.com/docs/en/changelog` は一時 503（同一セッション内で raw フォールバックにより取得完了・継続障害ではない）。
- **障害の変化: industry**: 主要ニュースドメインの記事本文 WebFetch が広範に 403（Forbes / ITmedia / Publickey 記事ページ / MLQ / buildfastwithai）。本日は WebSearch のスニペットで代替。
- **週次復旧チェック**（月曜）実施: `developers.openai.com/changelog`・`codex/changelog`・`www.anthropic.com/news` はいずれも 403 継続・未復旧。
- 継続提案: industry B-004（取得方法の WebSearch 優先化、28回目）、Copilot 5件（最多は B-011 Power Platform Blog のトピック記事照合、8回目）。
- 前日（07-26）分の欠損リカバリは対象なし（3ソース統合で生成済み）。
