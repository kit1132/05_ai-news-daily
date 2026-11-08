# AI News Daily Summary — 2026-11-09

週末明けで各社の発表は少ない。Gemini API の Live / TTS preview 4モデルの 11/17 停止は、公式 deprecations ページの検索インデックスで裏づけられた。Microsoft は App Builder のアプリを Cowork へ移すワンクリック移行を 11/4 から順次展開し、Copilot の Claude モデルの一部（Anthropic models with Data Retention）では Microsoft の DPA が適用されないと Learn に明記した。

## 今日のハイライト

### 1. [予定] Gemini API の Live / TTS preview 4モデルの 11/17 停止が公式ページの記載で裏づけられた — 二次ブログだけが報じていた期限が、残り8日の確定した期限になった

**要点**: 11/7 には二次ブログでしか確かめられなかった Gemini Live / TTS の preview モデル停止について、Google の Gemini API deprecations ページの検索インデックスに 11/17 停止の4モデルと移行先が載っていた。期限の根拠が二次から公式の記載に変わった。ページ本体は 301 の転送先に本日も届いていない。

**詳細**（Master）:
- 11/17 に停止する4モデルと移行先:
  - `gemini-2.5-flash-preview-tts` / `gemini-2.5-pro-preview-tts` → `gemini-3.8-flash-tts` か `gemini-3.8-flash-lite-tts`
  - `gemini-3.1-flash-live-preview` / `gemini-2.5-flash-native-audio-preview-12-2025` → `gemini-3.8-live`
- ⚠️ 5本目の `gemini-3.1-flash-tts-preview` は、二次ブログが同日停止に含める一方、公式ページの古い版は「No shutdown date announced」で、一次では確定しない
- Vertex AI は別の日付になる（例: `gemini-live-2.5-flash-native-audio` は 12/13）。11/17 は Gemini API 側の期限
- 取得経路: `ai.google.dev/gemini-api/docs/deprecations` は 301 で `aistudio.google.com` へ移り、そのホストはゲートウェイ拒否。本文は WebSearch の結果からしか読めていない

- https://ai.google.dev/gemini-api/docs/deprecations
- https://www.developersdigest.tech/blog/gemini-live-tts-retirement-november-2026

### 2. [新機能] App Builder のアプリをワンクリックで Cowork へ移せるようになった — 11/30 の退役までに移す手段ができたが、移行先は Frontier と Copilot Credits が前提になる

**要点**: App Builder でアプリを作った利用者は、「Migrate app」で Cowork の Copilot Managed Runtime アプリへ移せるようになった（11/4 から全世界で順次展開）。App Builder のアプリを開けるのは 11/30 まで。移行先は Frontier 参加・Copilot Credits の消費・個人開発者環境が前提で、共有とリンクは引き継がれない。

**詳細**（Copilot）: `copilot/manage/app-builder-migration`（`ms.date` 11/3・11/4 18:33Z）。App Builder の退役そのものは既報。
- ワンクリック移行: アプリを編集できる人（通常は作成者）だけが使える。画面・ナビゲーション・ロジックはソースコードから移り、SharePoint リストのデータはそのままで接続は自動でつなぎ直される
- 手動移行: ソースの .zip をダウンロードし、移行用プロンプトに添付して Cowork か Copilot Studio の Apps で作り直す。こちらは今すぐ使える
- 移行後の作業: 新しいアプリを公開し、元の利用者にあらためて共有する。元のアプリは 11/30 まで残る
- 課金: Cowork の App スキルは Frontier 参加テナントだけで使え、作成と実行は Copilot Credits を消費する（Power Apps Premium の要求上限内の実行を除く）

- https://learn.microsoft.com/en-us/copilot/manage/app-builder-migration
- https://learn.microsoft.com/en-us/copilot/cowork/cowork-build-apps

### 3. [仕様] Copilot の Claude モデルの一部は Anthropic がデータを保持し、Microsoft の DPA が適用されない — 「Copilot の Claude はすべて Microsoft の DPA の内側」という前提は成り立たない

**要点**: Claude Fable 5・Claude Mythos 5 などの「Anthropic models with Data Retention」は、管理者が M365 管理センターで明示的に opt-in しない限り使えない。opt-in すると Anthropic は独立した処理者になり、入出力の大半を最長30日保持する。ここには Microsoft の Product Terms と DPA が適用されない。

**詳細**（Copilot）: `copilot/implement/connect-to-ai-subprocessor`（`ms.date` 11/4・11/4 21:31Z。改訂の差分は特定できていない）。
- Fable 5.1: 対象組織では Anthropic をサブプロセッサーとして提供し、Microsoft の DPA が適用される。Anthropic は顧客コンテンツを保持せず、追加の opt-in は要らない
- データ保持つきのモデル: Claude が既定オンの地域でも全シナリオで既定オフ。使うには Anthropic の Commercial Terms of Service と DPA への同意が要り、管理者は全員か特定のユーザー・グループを選ぶ
- 保持期間: 入出力の大半は最長30日。利用ポリシー違反の疑いがあるとコンテンツは最長2年、分類スコアは最長7年。明示の許可なく学習には使わない
- 利用者の見え方: そのモデルが Anthropic のデータ保持を要すると分かる表示が製品内に出る

- https://learn.microsoft.com/en-us/copilot/implement/connect-to-ai-subprocessor

## カテゴリ別まとめ

### Copilot Studio / Power Platform

- [新機能] **埋め込み資格情報エージェントの共有統制** — 管理者は PPAC の環境設定「Sharing agents with embedded maker credentials」で、メーカーへの警告だけにするか（All sharing allowed）、安全でないエージェントの新規共有と公開を止めるか（Safe sharing enforced）を選べるようになった。Roadmap 566873（In development のまま）が告げていた統制が Learn に載った（Copilot）
  - 判定条件: 資格情報の共有を許さない接続を使い、その接続がデザイン時の資格情報で動くこと。呼び出すフローやエージェントの依存関係も含む
  - 止まるもの / 止まらないもの: 新規の共有と、共有操作のないチャネルでの公開が止まり、再公開で止まることもある。実行中のエージェントと既存の共有はさかのぼって止めない
  - 回避策: 利用者ごとの認証か、サービスプリンシパル・API キー・マネージド ID に置き換える。設定は Manage > Environments > Settings > Features
  - https://learn.microsoft.com/en-us/microsoft-copilot-studio/configure-sharing-agents-embedded-maker-credentials
- [新機能] **Microsoft MCP management MCP サーバー** — Microsoft が preview で、標準ハーネスのエージェントから環境の MCP サーバーを一覧・作成・更新・削除し、テナント全体へ公開できるようにした。サーバー ID は `MCPManagement`、スコープは `McpServers.Management.All`。preview の間はツール名とパラメーターが変わりうると明記している（Copilot）
  - https://learn.microsoft.com/en-us/microsoft-copilot-studio/mcp-management
- [仕様] **Microsoft Copilot ハーネスの FAQ** — Microsoft が FAQ で、管理者は Microsoft Copilot ハーネスをオフにする設定を持たず、統制は「誰が作れるか・いくら使えるか・どのデータとコネクタに届くか・誰に共有できるか」で行うと明記した。標準ハーネスは引き続きサポートされ強制移行はないが、2つのハーネスのエージェントは互いを直接呼べない。移行するとプロンプトと子エージェントはスキルか接続エージェントに置き換わる（Copilot）
  - https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-experience/faqs-copilot-harness
- [据え置き] **Learn・ブログ** — Copilot Studio What's New・課金レート表・課金3本・モデル表3本・ガイダンスハブ・非推奨一覧・Purview は改訂されていない。Released Versions は 2026.6.3 のまま131日たち、Power Platform 系ブログと TC の Copilot Studio Blog にも新しい記事はない（Copilot）
  - https://learn.microsoft.com/en-us/microsoft-copilot-studio/whats-new

### Microsoft 365 Copilot

- **App Builder から Cowork へのワンクリック移行**（ハイライト2参照）
- **Anthropic models with Data Retention**（ハイライト3参照）
- [観測] **Roadmap API の総項目数** — Microsoft の Roadmap API の総項目数が 2,302 から 2,297 に減った。11/6 23:04Z 以降に新しいバッチはなく、2回取得しても 2,297 だった。前回の一覧を残していないため、消えた項目は特定できない（Copilot）
  - https://www.microsoft.com/releasecommunications/api/v1/m365
- [据え置き] **Roadmap・Message Center・M365 Copilot の Learn** — Roadmap の RSS は 11/6 23:04Z、Message Center のアーカイブは 11/7 00:00Z から動いていない。Release Notes（先頭 November 4）・拡張機能 What's New・Cowork What's New・`cowork-models`・Partner Center 11月ページも改訂されていない（Copilot）
  - https://www.microsoft.com/releasecommunications/api/v2/m365/rss

### GitHub Copilot / Microsoft 開発ツール

- [新機能] **Intelligent Terminal 0.3** — Microsoft が 11/4、Windows 向け Intelligent Terminal 0.3 を出し、利用者はタブ・エージェントセッション・端末を縦のサイドバーで管理できるようになった。各タブにエージェントの状態と入力待ちの印が出る（Master）
  - headless mode: 有効にしたエージェントのタブは、端末を閉じてもマシンが止まるまで動き続け、サイドバーとシステムトレイに出る
  - 検索と再開: 開いているタブと最近のエージェントセッションを横断して探せ、「Agents only」で CLI タブだけを出せる。Recent agent sessions から過去のセッションを開き直す
  - エージェント検出: インストール済みの GitHub Copilot CLI・Claude などを検出し、新しいタブのメニューにプロファイルを自動で作る
  - サイドバーは既定でオン（Settings > Appearance > Tab Layout で横に戻せる）。製品は experimental のまま
  - https://devblogs.microsoft.com/commandline/intelligent-terminal-v0-3-a-new-way-to-see-and-manage-your-tabs-and-agents/
- [据え置き] **Copilot CLI・github.blog** — Copilot CLI の安定版は `v1.0.107`（11/6）、pre-release は `v1.0.108-1`（11/7）のまま。`github.blog/changelog/label/copilot/` の最上位も 11/6 の code review API 管理のままである（Master・industry）
  - https://github.com/github/copilot-cli/releases

### Anthropic / Claude

- [据え置き] **Claude Code・Platform・Anthropic の一次** — Claude Code の最上位は `2.1.319`（11/6）、npm は `{stable: 2.1.311, latest: 2.1.319, next: 2.1.319}` のまま。Platform の release notes は 11/5、退役ページは Active 15件・Deprecation history 最新 9/30 で、Opus 4.5（下限 11/24）の告知はまだない。`/news`・`/research`・`claude.com/resources/articles`・support の release notes・Privacy Center も動いていない（Master・industry）
  - https://platform.claude.com/docs/en/about-claude/model-deprecations

### OpenAI / Codex / ChatGPT

- [仕様] **ChatGPT Pro 3プランの利用枠の倍率** — OpenAI の Codex 責任者 Thibault Sottiaux 氏が 11/8 の投稿で、Pro 100・Pro 200・Pro 500 の利用枠を Plus 比10倍・20倍・50倍と示したと伊メディアが報じた。DevDay（9/29）時点の5倍・10倍・25倍から、10/29 の倍増と Pro 200 の削減撤回を経てすべて2倍になった。月額 $100 / $200 / $500 は変わらない（industry）
  - ⚠️ 一次未確認: 報道は WebSearch のスニペットのみ。OpenAI ヘルプ「About ChatGPT Pro tiers」は Work・Codex 枠の倍増までで、「50倍」の数字とチャット上限の倍率は書いていない
  - https://pasqualepillitteri.it/en/news/31080/openai-confirms-chatgpt-pro-500-50x
  - https://help.openai.com/en/articles/9793128-about-chatgpt-pro-tiers
- [版更新] **Codex CLI 0.169.0-alpha.3** — OpenAI が pre-release `0.169.0-alpha.3`（11/7）を出した。安定版は `0.167.0`（11/6）のまま（Master）
  - https://github.com/openai/codex/releases
- [据え置き] **OpenAI の一次** — API changelog・deprecations（いずれも最上位 11/5）、Deployment Safety Hub、community Announcements（11/4）、misalignment reports、ChatGPT & Codex changelog（11/6）は前回のまま。ChatGPT Release Notes も 11/4 の Images 2.6 より新しい項目はない（Master・industry）
  - https://developers.openai.com/api/docs/deprecations

### Google

- **Gemini Live / TTS preview モデルの 11/17 停止**（ハイライト1参照）
- [据え置き] **Google の一次** — Workspace Updates の最上位は 11/6 の週次まとめ、The Keyword の AI RSS は 11/5 の Gemini Omni 1.2 Flash、Gemini アプリの release notes は 2026.10.13 のまま。Gemini API changelog は検索でも 10/27 の `gemini-api` CLI beta より新しい項目が見つからない（Master）

### Cursor / 開発ツール / エージェント

- [破壊的変更+新機能] **Devin の PagerDuty 連携変更** — Cognition が 11/6 のリリースノートで、PagerDuty のインシデントを PagerDuty が作る Slack チャンネルから始めるように変え、インシデントソースに Slack チャンネル名の接頭辞の設定を必須にした（Master）
  - ⚠️ 既存の連携: 接頭辞を PagerDuty 側のチャンネル名と合わせないと動かない。新しい responder トリガーは空のフィルターで始まる
  - 管理機能: 管理者がセッション共有の既定を決め、共有を organization 内に限れる。Settings → Connections から全デバイスをログアウトできる。Enterprise Settings に Oncall タブが加わった
  - API: V3 のセッション作成が `memory_enabled: false` を受け付ける。grants API では secret の所有者自身のアクセスを変更・削除できなくなった
  - 連携: Gerrit 3.13 以降のアクセス権同期、GitLab の fine-grained PAT での MR 閲覧と Devin Review、プラグインの MCP 宣言の `oauthResource`
  - https://docs.devin.ai/release-notes/overview
- [仕様] **MCP Ruby SDK が Tier 1** — Publickey（11/9）によると、MCP の仕様を管理する Linux Foundation 傘下の Agentic AI Foundation（AAIF）が、Ruby SDK を仕様の全実装を満たす「Tier 1」に認定した。Tier 1 はこれまで TypeScript・Python・C#・Go・Rust の5つで、Ruby SDK は 7月の 1.0 時点では Tier 2 だった。MCP blog の最上位も 10/30 のこの件のまま（industry・Master）
  - https://www.publickey1.jp/blog/26/mcpmcpruby_sdkmcp_sdk_tier_1.html
- [動向] **Co-Design Bench** — The Decoder（11/8）によると、Alibaba とアジアの複数大学の研究者が実際のコーディングセッションの言い直し・差し戻しから課題を作ったベンチマークで、首位の GPT-6 Astra でも完全正解は26.4%（要件達成は平均約70%）だった。従来の WebCompass-edit では同じモデルが99%を超えており、差は35ポイント以上ある。GLM-5.2 は小さな変更で GPT-6 Astra の約6倍のトークンを使った（industry）
  - https://the-decoder.com/ai-coding-agents-still-need-human-cleanup-on-nearly-three-out-of-four-tasks-in-a-real-world-test/
- [動向] **AI によるエージェントログ監査** — The Decoder（11/7）によると、Anthropic の Andy Hall 氏の研究で、GPT-5 はエージェントのログから報酬ハッキングの約98%を見つけたが、探索を徹底させるほど誤警報が増え、安全確認にそのまま使える精度には届かないとした（industry）
  - https://the-decoder.com/ai-auditors-catch-most-agent-misbehavior-but-flood-reviewers-with-false-alarms-new-study-finds/
- [据え置き] **Cursor・xAI・Orca ほか** — Cursor の changelog（11/6 Voice Chat）とフォーラム（10/12）、xAI、Orca（`v1.4.253`・11/7）は動いていない。TypeSafe AI の sitemap は9件、Hugging Face の8 org に新規はなく、Obsidian・Apple Developer News も前回のまま（Master）

### 業界・市場

- [動向] **Anthropic の発電設備確保** — Reuters・Bloomberg（11/8）が FT をもとに、Anthropic がデータセンター用のガス発電機 1.7GW 分を約 $3.4B で確保したと伝えた。AI 企業による発電設備の単独購入としては知られている中で最大とされる。9月下旬に OnePWR Solutions から Caterpillar 向け発注を含む調達枠を引き取ったもので、会社の買収ではない。設置場所は報じられておらず、両社とも公式に認めていない（industry）
  - https://www.bloomberg.com/news/articles/2026-11-08/anthropic-buys-power-for-ai-data-centres-in-3-4b-deal-ft-says
- [据え置き] **買収協議・上場・国内調査** — Amazon × Decart、Nvidia × Reflection AI の買収協議に続報はなく、Anthropic の上場日・ロードショー開始の確定報道もない。S-1/A の本文は未確認のまま。IDC Japan・MM総研・NRC の新しい公表もない（industry）

### 日本語コミュニティ

- [据え置き] **Qiita / Zenn / Power Platform Weekly** — Qiita・Zenn とも 11/8 以降の新しい記事はなく、Power Platform Weekly も #282（11/2）が最新のまま（Copilot）
  - https://qiita.com/tags/copilotstudio/feed

## 直近の注目予定

- **11/9**: Opal（Frontier）で UBB と支出ポリシーが前提になる（MC1540330） ／ GitHub が公開リポジトリの `pull_request_target` を試験ブロック（16:00〜18:00 UTC） ／ 2,001席以上の組織で、ライセンスのない Copilot Chat 利用者の上限拡大が開始 ／ Dataverse のみのテナントでストレージ検証が開始（MC1483529）
- **11月中**: GitHub の cloud sandbox の課金が開始（日付は明記なし） ／ Work IQ Execute（Recipes）と Work IQ Federated connectors が GA（Roadmap 570866・570670）
- **11/10**: Amazon Bedrock の Mythos 5 / Opus 4.7 / Sonnet 4.6 へのテキスト透かし展開が完了予定 ／ Claude Desktop の管理ポリシーに関わる変更（中身は一次未確認）
- **11/12**: Copilot Studio の GPT-4.1 / GPT-5 系と、Copilot ハーネスの GPT-5 Chat・GPT-5.6 Sol / Luna が退役（MC1506318） ／ Anthropic Usage Policy 改定版が発効 ／ OpenAI → Cursor のモデル供給停止予定（一次未読）
- **11/13**: Excel と Cowork の会計機能が GA（MC1536053）
- **11/15**: Dataverse for Teams 環境とアンマネージド開発者環境の新規作成が停止 ／ Copilot Studio のカスタム採点器ライブラリが GA（MC1531932）
- **11/16**: GitHub Copilot が Claude Opus 4.8・Opus 5・GPT-5.6 Terra を廃止 ／ Teams の旧 GitHub アプリが退役 ／ `pull_request_target` の2回目の試験ブロック ／ Cowork / Autopilot の Engage プラグインが GA（MC1530609） ／ Claude Opus 4.6・Opus 4.5・Sonnet 4.5・Haiku 4.5 に透かしが入る
- **11/17**: Gemini API の Live / TTS preview 4モデルが停止（5本目は未確定） ／ Gems が Gemini アプリの設定パネルへ移動 ／ Intelligent call delegation が従量課金のパブリックプレビューへ移行（MC1537490） ／ Sales Agent のセマンティックモデルが GA（MC1540293）
- **11月中旬**: 単体の Word / Excel / PowerPoint エージェントの撤去が開始（MC1536062） ／ Office in Copilot の展開が完了（MC1530611） ／ Learning Agent のプレイリスト（MC1537495） ／ Cowork の Power Platform コネクタの展開が完了（MC1542062）
- **11/17〜20**: Microsoft Ignite
- **11/18**: MODS の Workforce Insights エンドポイントが退役（MC1542066）
- **11/20**: Conductor のクラウド版が終了（二次） ／ Copilot Studio のコスト管理を M365 管理センターへ移す機能が GA（MC1530368）
- **11/24 以降**: `claude-opus-4-5-20251101` の暫定退役日（確定日ではない）
- **11月下旬**: Work IQ API で Copilot コネクタのデータが使えるようになる（MC1538999） ／ Cowork の Planner Plugin の GA 展開が完了（MC1540339） ／ 管理者主導の Copilot オンボーディングの展開が完了（MC1486291）
- **11/29**: OpenAI が Daybreak Blue のセッションデータの学習利用を開始（二次）
- **11月末**: Word の Top of Doc 要約の廃止が完了（MC1454113） ／ Notebooks の Power BI 参照の GA が開始（MC1474458） ／ Windows の Copilot Notebooks のマルチモーダルキャプチャ（MC1405506）
- **11/30**: App Builder のアプリを開けなくなる ／ EU / EFTA でデータ移動オフの環境の GPT-5 Chat（Copilot ハーネス）が終了 ／ `claude-sonnet-4-5-20250929` が Claude API から退役し、Opus 4.8 の fast mode を削除 ／ OpenAI の Evals・`v1/prompts`・Agent Builder が停止 ／ Gemini 4 Argon の導入価格が終了 ／ Power Automate のデザイナーの Copilot がサポート終了（MC1540258） ／ Describe it to design it が退役（MC1537406） ／ モデル駆動アプリの説明文の AI 生成が退役（MC1540110） ／ vibe.powerapps.com が退役
- **12/1**: M365 Copilot の前提サブスク不要オファー開始 ／ Business Central + Copilot Business のバンドルが CSP の価格表プレビューに載る ／ Gemini 4 Argon の単価が $4/$20 に倍増 ／ Google スライドの複数スライド作成の上限引き上げ優待が終了しうる
- **12/2**: Power Platform のプロンプトから Anthropic・Grok・旧 GPT 系のモデルが退役し自動移行（MC1536101） ／ GitHub が公開リポジトリの `pull_request_target` を既定でブロック
- **12/4**: Copilot Studio エージェントの指標とアラートが GA（MC1538998）
- **12月上旬**: UBB モデル（GPT-6 Astra / Claude Fable 5.1）の Chat と Word / Excel / PowerPoint での GA が開始（MC1519122） ／ Teams 会議の MeetingAI ポリシーの Targeted Release が開始（MC1532253） ／ Work IQ MCP のメモリーの読み取り（MC1539004）と Planner Agent の拡張（MC1539002）が開始
- **12月**: Teams Facilitator follow-up mode が GA（Roadmap 566523） ／ ChatGPT と Codex の利用枠が Plus・Pro・Business で1つの予算に統合（日付未公表・二次）
- **12/11**: Power Apps の式の生成・Power Apps Ideas・Copilot によるコントロール名の変更が退役（MC1532421・MC1532426）
- **12/14**: claude.ai/design の単体サイトが閉鎖
- **12/31**: Power Platform の環境間のコメントのインポート・エクスポートが終了 ／ Claude Security の無償クレジットの対象期間が終了 ／ Partner Center の Copilot in 30 プロモーションが終了
- **2026年末まで**: Copilot の Claude モデルの処理が EU Data Boundary の内側に移る
- **2027-01-06**: OpenAI `tts-1` / `tts-1-hd` / `gpt-4o-mini-tts` 2版が停止
- **2027年1月**: Targeted release が退役 ／ Business Central + Copilot Business のバンドルの販売が開始（1/1） ／ SharePoint / OneDrive の Copilot Search の GA 展開が開始（1月中旬・MC1540513）
- **2027-01-14**: OpenAI の GPT-4o・GPT-4o mini・GPT-4.1・GPT-4.1 mini が API から削除（→ `gpt-6-luna`）
- **2027-01-15**: Claude Code Review の Enterprise 向けクレジット請求期限
- **2027-01-30**: ChatGPT Classic（旧デスクトップアプリ）が終了（二次）
- **2027年1〜3月**: CSP の Copilot Business 新規購入で従量課金が既定オン
- **2027-02-01**: OpenAI の `gpt-5.5-cyber-preview` が API から削除
- **2027-03-01 以降**: Gems 廃止（Business / Enterprise）
- **2027年春**: Siri AI 対応アプリの App Store 提出受付が開始
- **2027-04-01**: OpenAI `gpt-5.1` / `gpt-5.3-codex` / `gpt-5.4-nano` が停止
- **2027年6月**: 外部メールを Copilot の処理から外す Purview DLP が GA（MC1301714）

## 改善メモ

- 新規提案: 3ソースとも新規起票なし
- 継続提案: Master は継続7件（最多 B-036 DeepSeek 登録、12回目。B-088 Gemini API Changelog の URL 差し替えは6回目） ／ Copilot は継続5件（最多 B-080 Cowork の Learn URL 差し替え、14回目。B-084 は週次突合の目次 `microsoft-365/copilot/toc.json` が 404 で `copilot/toc.json` に移っていたことを追記） ／ industry は継続7件（最多 B-040 セキュリティ開示の定点、15回）
- 障害の変化: industry で `pasqualepillitteri.it`・`www.investing.com` がゲートウェイ拒否（新規。WebSearch のスニペットで代替）。Master は月曜の週次復旧チェックで復旧0件・分類の変化0件
- ソース間の食い違い: Gemini API の 11/17 停止について、Master は公式 deprecations ページの検索インデックスで4モデルを確認したが、industry は「7日連続で一次に届かず未確認・5種」と書いている。本サマリーは Master の記載（4モデル確定・5本目は未確定）を採った
- 欠損リカバリ: 前日（11/8）分は3ソース揃っており、対象なし
