# AI News Daily Summary — 2026-11-11

Microsoft は EU / EFTA のテナントで 12/9 に Claude モデルを既定で有効にすると告知し、GitHub は 12/8 から1年動きのないリポジトリの Dependabot アラートを止める。Copilot には Claude Fable 5.2 と Gemini 4 Carbon が載り、Anthropic は Claude Code 2.1.321 で Fable 5.2 を既定にした。Anthropic は IPO の仮条件を $70〜78 としてロードショーを始めた。

## 今日のハイライト

### 1. [廃止+破壊的変更] EU / EFTA のテナントで 12/9 に Claude モデルが既定で有効になる — EU の Claude は「既定オフで必要なら有効化」から「既定オンで不要なら 12/9 までに無効化」に変わった

**要点**: 12月上旬に Claude モデルの処理が EU Data Boundary の内側へ移り、12/9 には Anthropic を選んでいない EU / EFTA のテナントで全ユーザーに有効になる。「M365 アプリの Copilot だけで許可」の選択肢も退役し、All users に移る。使わせない組織は 12/9 までに設定を変える必要がある。

**詳細**: MC1546438（11/10 公開・Major change・Act by 12/9）。
- 対象: EU Data Boundary の対象になる EU / EFTA のテナント。Copilot の各体験と Copilot Studio で Claude モデルが使えるようになる
- 設定の場所: M365 管理センター > Copilot > Settings > View all > AI providers operating as Microsoft subprocessors > Anthropic。AI 管理者かグローバル管理者のロールが要る
- 既存の選択: All users / No users / Specific users and groups は尊重される。既に有効にしているテナントは処理が自動で EU Data Boundary 内に移る
- 範囲外: Anthropic models with Data Retention（11/9 掲載）は別の設定で、今回の変更に含まれない。12月上旬までは Claude モデルは EU Data Boundary の処理の約束の対象外である

出典:
- https://mc.merill.net/message/MC1546438

### 2. [破壊的変更+予定] GitHub が 12/8 から1年間 push のないリポジトリの Dependabot アラートを止める — 保守だけ続けているリポジトリでも、何もしないと脆弱性の通知が来なくなる

**要点**: GitHub が 12/8 から、過去1年に活動のないリポジトリの Dependabot アラートを停止する。既存のアラートは削除ではなくアーカイブになる。push の少ない社内リポジトリも対象になりうるため、通知を前提にした脆弱性管理は 12/8 で前提が崩れる。

**詳細**: GitHub changelog（11/10）。
- 活動の定義: いずれかのブランチ・タグへの push、リポジトリの作成、Dependabot アラートの有効化
- 対象外: Dependabot アラートを有効にするセキュリティ設定を強制しているリポジトリ、アラートの切り替えを Enterprise のポリシーで禁じているリポジトリ、GitHub Enterprise Server
- 再開: push すれば自動で戻り、設定画面からも戻せる。どちらでも1年の計測はやり直しになる。Dependabot のセキュリティアップデートへの影響は書かれていない

出典:
- https://github.blog/changelog/2026-11-10-dependabot-alerts-will-pause-on-inactive-repositories

### 3. [新機能+予定] GitHub が Copilot で Claude Fable 5.2 を GA にした — Business / Enterprise ではポリシーを入れると Anthropic のデータ保持に同意したことになり、ZDR の例外は 12/31 で終わる

**要点**: GitHub が 11/9、Copilot Pro+ / Max / Business / Enterprise で Fable 5.2 を使えるようにした。Business / Enterprise は既定オフで、管理者がポリシーを入れると Anthropic がプロンプトと出力を保持することに同意したことになる。審査を通った企業の ZDR 例外は 2026 年末までで、2027 年以降は EFS が要る。

**詳細**:
- 使える場所: VS Code・Visual Studio・Copilot CLI・coding agent・Copilot app・github.com・GitHub Mobile・JetBrains・Xcode・Eclipse の model picker。順次展開
- 課金: 従量課金で、提供元の表示単価で請求する
- データ保持: Fable 5 / 5.1 / 5.2 だけは安全分類器のために Anthropic がデータを保持する（学習には使わない）。他の Claude モデルは ZDR のまま
- ZDR の例外: 審査を通った企業は Fable 系を暦年末まで ZDR で使える。資格は GitHub の担当チームに問い合わせる。承認後も管理者がポリシーを入れる必要がある
- 2027 年以降: Enterprise Frontier Safeguards（EFS）が必要になる。自動の安全監視を行い、顧客が管理する保存先と暗号鍵も選べる
- Copilot CLI でも 11/10 の安定版 `v1.0.109` で model picker に Fable 5.2 が入った

出典:
- https://github.blog/changelog/2026-11-09-claude-fable-5-2-in-github-copilot/

## カテゴリ別まとめ

### Anthropic / Claude

- [破壊的変更+セキュリティ] **Claude Code 2.1.321 / 2.1.322** — Anthropic が Claude Code `2.1.321`（11/9）で Fable 5.2 を既定の Fable にし、MCP OAuth のリダイレクト先へリフレッシュトークンを送っていた不具合と、読み取り専用の Bash が確認なしでサンドボックス外で動く不具合を直した。Pro / Max では保存済みの Fable 5.1 の選択がすぐ 5.2 に移る（Team / Enterprise は組織の許可後）。戻すときは `/model claude-fable-5-1`（Master・industry）
  - 管理設定: Claude が書く mods は auto / bypass モードで確認なしにオンになり、managed の `allowUnsandboxedCommands: false` でも変わらない。managed `extraKnownMarketplaces` は宣言した名前を別ソースから足せなくなった
  - Claude apps gateway: `policy_mode: layered` で条件に合う全ポリシーの managed MCP サーバーを足し合わせるため、配られるサーバーが増えうる。Bedrock / Vertex / Foundry の上流は `ANTHROPIC_*_BASE_URL` を無視する
  - 権限: `cp` / `mv` でディレクトリへ書くファイルにも deny ルールと保護ファイルの確認が効くようになった
  - `2.1.322`（11/10）: Vertex の global / us / eu リージョンで fast mode を使えるようにした。npm は stable 2.1.311 / latest 2.1.322
  - 11/10 に既報の `settings.local.json` 経由の秘密情報の保存を防ぐ変更は、まだ入っていない
  - https://code.claude.com/docs/en/changelog
- [新機能] **Claude の Whiteboards・Sheets・Data とアプリの埋め込み** — Anthropic が 11/10、有料プランの Claude に共有ボードの Whiteboards（beta）、表計算の Sheets（beta）、旧 Dashboards の Claude Data（GA）を加え、Notion や Confluence などのアプリを会話の横で開いて Claude が中を編集できるようにした。Enterprise では Claude Data が 11/19 に既定でオンになり、Whiteboards と Sheets は既定オフ（Team は3機能とも既定オン）（Master・industry）
  - アプリの埋め込み: 対象例は Asana・Canva・Dropbox・monday.com・Adobe・Atlassian・Box・HubSpot・Notion など。基盤は MCP の拡張 MCP Apps（開発者向けパブリックプレビュー）で、実行前に承認する
  - 料金・利用上限は記事に書かれていない。会議に参加してメモを取る Claude Meetings は近日提供（industry）
  - https://claude.com/resources/articles/sheets-whiteboards-data
  - https://claude.com/resources/articles/interactive-connectors-full-tool
- [観測] **Opus 5.5 の推論低下の指摘と反証** — GIGAZINE（11/10）によると、開発者の Shane Melaugh 氏が Claude Code の約1,400セッションで最初の操作までの thinking トークンの中央値が84から54に減ったとした一方、Theo 氏は約45.8万件の応答で平均が369から413に増えたとした。表示される thinking は別モデルの要約なので、要約側の変更でも見え方は変わる。Anthropic の説明はない（industry）
  - https://gigazine.net/news/20261110-claude-opus-nerf/
- [動向] **JPMorganChase の Claude Code 拡大** — Anthropic が 11/9、JPMorganChase が Claude Code を社内のより多くの従業員へ広げたと公表した。同じ日に Curative が提供者ネットワークの契約交渉（週 2,000 件超）に Claude Platform のエージェントを使う事例も出た（Master）
  - https://claude.com/resources/articles/jpmorganchase-expands-claude-code
- [据え置き] **Anthropic の一次** — Claude Platform の release notes は 11/9（Fable 5.2 / Mythos 5.2）が最上位のままで、モデル退役一覧も Active 17件で変わらず、Opus 4.5（下限 11/24）の告知もない。`/research` と support の release notes、Privacy Center も動いていない（Master・industry）
  - https://platform.claude.com/docs/en/release-notes/overview

### GitHub Copilot / Microsoft 開発ツール

- **Claude Fable 5.2 の Copilot 提供**（ハイライト3参照）
- **Dependabot アラートの停止**（ハイライト2参照）
- [料金+新機能] **Gemini 4 Carbon の正式提供と Copilot 対応** — Google が 11/10 に Gemini 4 Carbon を正式提供し、開発者は導入価格の入力 $2・出力 $10（通常 $4/$20）で使えるようになった。GitHub は 11/9 に Copilot Pro+ / Max / Business / Enterprise で提供を始め、モデルが既定で有効になる設定の組織では管理者が切らない限り自動で有効になる（industry）
  - 性能: CursorBench 4.0 で1位（60%弱）、Artificial Analysis Intelligence Index は60（Fable 5.2 High は62）。解決1タスクあたり $7.76 で、Fable 5.2 Max の $26.50 より安い
  - 導入価格の終了日は未確認（Google の一次 `aistudio.google.com` はゲートウェイ拒否）
  - https://github.blog/changelog/2026-11-09-gemini-4-carbon-in-github-copilot
  - https://the-decoder.com/gemini-4-carbon-arrives-just-in-time-to-feel-like-yesterdays-news-in-the-fastest-model-cycle-yet/
- [破壊的変更+新機能] **Copilot CLI v1.0.109** — GitHub が 11/10 に Copilot CLI の安定版 `v1.0.109` を出し、使えないモデルを指定すると黙って別のモデルへ切り替えずエラーにするようにした（Master）
  - JSON 出力: `copilot -p --output-format json` は早い段階で失敗しても終了状態つきの最終結果レコードを出す
  - ACP モード: preToolUse フックが `ask` を返すと、呼び出しを断らず ACP クライアントに確認を求める
  - サンドボックス: 許可・拒否ルールに IPv4 / IPv6 の CIDR を書ける。Linux では開発ツールの設定ファイルも拒否パスの対象になった
  - https://github.com/github/copilot-cli/releases
- [新機能] **C++ Language Server の MSBuild 自動設定** — GitHub が 11/10、Copilot CLI 用の Microsoft C++ Language Server に MSBuild の compile commands 抽出を同梱した。MSBuild のプロジェクトを開くと compilation database が自動で作られ、エージェントが設定用スキルを探す手間とトークンが要らなくなる（Master）
  - https://github.blog/changelog/2026-11-10-c-language-server-now-auto-configures-msbuild-builds/

### Microsoft 365 Copilot

- **EU / EFTA の Claude 既定有効化**（ハイライト1参照）
- [廃止+破壊的変更] **Power BI の単体 Copilot の退役** — Microsoft が、Power BI のホーム・モバイル・Teams・ワークスペースアプリにある単体の Copilot（preview）を2027年1月中旬に退役させ、12/8 から M365 Copilot in Power BI and Microsoft Fabric（preview）を全世界で既定オンにすると告知した（MC1546429・11/10）。テナント設定「Show Copilot in app navigation」なども消える（Copilot）
  - https://mc.merill.net/message/MC1546429
- [破壊的変更] **UBB の Cowork / Code / Autopilot の入口の既定表示** — Microsoft が、2027年1月末から M365 Copilot ライセンス保有者全員に従量課金（UBB）体験の入口を表示し、支出ポリシーで許可されていない利用者には「Request access」か「Learn more」を出すと告知した（MC1546354・11/9）。実際の利用と課金は従来どおり支出ポリシーで決まる（Copilot）
  - 11月中旬: 新しい管理設定「Access requests to usage-based billing experiences」が入り、要求を出せる利用者を選べる
  - 12月中旬: 「Learn more」に組織のガイダンスの URL を設定できる
  - 2027年1月末: 新しい表示が強制され、旧設定「Allow users to discover and use AI experiences enabled by usage-based billing」が退役する（Deferred release は2月末）
  - https://mc.merill.net/message/MC1546354
- [新機能] **App Blocks と PowerPoint の解説動画** — M365 Copilot の利用者は Copilot Chat の会話の中で電卓やダッシュボードのような対話型アプリ（App Blocks、MC1545695）を使えるようになった。Frontier の利用者は PowerPoint の Copilot で静的なスライドをアニメーションの解説動画に変えられるようになる（MC1546430、11月上旬〜中旬に展開）（Copilot）
  - https://mc.merill.net/message/MC1545695
  - https://mc.merill.net/message/MC1546430
- [予定] **Edge for Business の Copilot Chat による書き直し** — 利用者は Edge for Business で編集できるテキストを右クリックして Copilot Chat の書き直しを使えるようになる。2027年1月下旬までに既定オンで展開され、管理者は `InlineComposeEnabled` ポリシーで止められる（MC1146821・11/9 更新）（Copilot）
  - https://mc.merill.net/message/MC1146821
- [予定] **Agent 365 の Ignite ガイド** — 製品チームが 11/10、Agent 365 を「エージェントの制御プレーンから AI の可観測性基盤へ」進めると予告し、11/17 の基調講演と BRK214・BRK345 などを案内した。同日の Copilot Blog には Moody's・LSEG・FactSet のコネクタを Chat・Excel・Cowork で使う例も出た（Copilot）
  - https://techcommunity.microsoft.com/t5/agent-365-blog/microsoft-ignite-2026-your-guide-to-agent-365/ba-p/4571750
- [観測] **Roadmap の総項目数** — Microsoft の Roadmap の総項目数が 2,296 から 2,288 に減った。新しいバッチはなく、API の最終 `modified` も 11/6 23:04Z のままで、消えた項目は特定できない（Copilot）
  - https://www.microsoft.com/releasecommunications/api/v1/m365

### ライセンス・ガバナンス

- [廃止] **Purview Data Governance の退役** — Microsoft が Partner Center 11月ページ（11/10 追記）で、Purview Data Governance（Unified Catalog・Data Map・Workflows・Azure Purview）が 11/12 に退役に入り、サポートは2027年11月12日に終わると告知した。パートナーにはデータガバナンスの提案を Fabric の OneLake カタログへ移すよう求めている。Message Center と Purview の Learn での告知は見つかっていない（Copilot）
  - https://learn.microsoft.com/en-us/partner-center/announcements/2026-november
- [廃止] **Purview DSPM のパートナー連携** — Microsoft が、Microsoft 以外のデータソース向けの Varonis・BigID・Cyera・OneTrust と DSPM の連携を 12/7 に退役させると告知した（MC1545691・11/9）。DSPM のほかの機能は影響を受けない（Copilot）
  - https://mc.merill.net/message/MC1545691

### Copilot Studio / Power Platform

- [新機能] **Power Platform の10〜11月の月次まとめ** — 製品チームが 11/10 に PPCC の発表を含む月次の機能更新をまとめた。未掲載だった主な項目は次のとおり（Copilot）
  - 監視アラートのトリガー: Power Platform for Admins V2 コネクタに「when an alert fires」が加わり、管理者は監視のアラートを Teams などへ送れる（preview）
  - 監視メトリクスのエクスポート: OpenTelemetry 形式で書き出し、30日の保持期間を超えて自分のストレージに残せる（preview）
  - `Dataverse.Unmask`: キャンバスアプリから、マスクされた Dataverse 列の値を明示的な操作で表示できる
  - モダンコントロール: 添付ファイル（preview）・アバターグループ・ペルソナ・メトリクスカード・カードギャラリーが加わった
  - https://www.microsoft.com/en-us/power-platform/blog/power-apps/whats-new-in-power-platform-october-2026-feature-update/
- [新機能] **PPAC のコネクタのインベントリ** — 管理者は PPAC の在庫に出る Connectors 列で、どのリソースがどのコネクタを使っているかを確かめられるようになった（MC1546312・11/10 までに GA）。同じデータは inventory API・PAC CLI・Azure Resource Graph からも取れる（Copilot）
  - https://mc.merill.net/message/MC1546312
- [予定] **フィードバックフォームの既定ポリシー** — 管理者が、Dynamics 365・Power Platform・Copilot Studio で利用者が Microsoft にフィードバックを送るときの共有チェックボックスの既定値を決められるようになる（MC1545686・11/16 GA）（Copilot）
  - https://mc.merill.net/message/MC1545686
- [仕様] **多言語の IT セルフサービスエージェントの参照アーキテクチャ** — Microsoft が Architecture Center に、Teams 上の Copilot Studio エージェントが言語を判定して答え、ITSM のチケットを作成・更新して担当者へ引き継ぐ構成を載せた（11/9）。ガイダンスハブの What's New にもこの記事が加わった（Copilot）
  - https://learn.microsoft.com/en-us/power-platform/architecture/reference-architectures/multilingual-it-self-service-agent
- [据え置き] **Copilot Studio の Learn** — What's New・課金レート表・課金3本・モデル表3本・非推奨一覧・Purview は改訂されていない。Released Versions は 2026.6.3 のまま133日たつ（Copilot）
  - https://learn.microsoft.com/en-us/power-platform/released-versions/copilotstudio

### OpenAI / Codex / ChatGPT

- [廃止] **`gpt-image-2` の API 停止** — OpenAI が 11/10、API の `gpt-image-2` と `gpt-image-2-2026-04-21` を非推奨にし、2027-02-10 に停止すると告知した。移行先は 11/4 に出た `gpt-image-2.6-sunburst` か `gpt-image-2.6-flare`（Master・industry）
  - https://developers.openai.com/api/docs/deprecations
- [版更新] **Codex CLI の pre-release** — Codex CLI は安定版 `0.167.0`（11/6）のままで、pre-release が `0.169.0-alpha.7` と `0.167.0-alpha.4.1`（11/9）まで進んだ。本文は版番号だけである（Master）
  - https://github.com/openai/codex/releases
- [据え置き] **OpenAI の他の一次** — API changelog（11/5 `gpt-6-cyber`）、Deployment Safety Hub、misalignment reports、ChatGPT & Codex changelog（11/6）は動いていない。11/10 の OpenAI の発表は検索で見つからない（Master・industry）
  - https://community.openai.com/c/announcements/6

### Google

- [新機能] **Google Chat の Gemini による会議設定** — Google が 11/10、Google Chat の会話から Gemini で会議を1クリックで設定できるようにした（Business Standard / Plus・Enterprise Standard / Plus ほか、展開に15日超かかることがある）。Workspace Studio には自動化の途中で待つ「Wait until」ステップが入った（11/9）（Master）
  - https://workspaceupdates.googleblog.com/
- [動向] **The Keyword の発表** — Google が 11/10、Google Cloud の Gemini for healthcare と、Adobe のツールを Google のアプリに近づける提携を出した（Master）
  - https://blog.google/technology/ai/
- [観測] **Gemini API の一次に届かない** — `ai.google.dev/gemini-api/docs/changelog` の転送先 `aistudio.google.com` に本日も届かず、検索で見える最新は 10/27 の `gemini-api` CLI beta だった。11/17 の Live / TTS preview 停止は9日続けて一次で確認できていない（Master・industry）
  - https://ai.google.dev/gemini-api/docs/changelog

### Cursor / 開発ツール / エージェント

- [据え置き] **Cursor・xAI・Devin・Orca・MCP・Hugging Face** — Cursor の changelog（11/6）とフォーラム（10/12）に Fable 5.2 の提供告知はない。xAI、Devin（11/6）、Orca（`v1.4.255`）、TypeSafe AI（`jev-1.14.0`）、MCP blog（10/30）も動かず、Hugging Face の8 org に新しいリポジトリはない（Meta の Muse Ember も `meta-models` に出ていない）（Master）
  - https://forum.cursor.com/c/announcements/11

### 業界・市場

- [セキュリティ] **Fireworks AI の2回目の侵害と Notion AI の流出** — 推論基盤の Fireworks AI が 11/9、2回目の侵害で顧客のデータセット・学習途中の重み・秘密情報に届いたと公表した。Notion は自社 AI のチャット記録の流出（ワークスペースの1%未満）を認め、Insights と Fireworks 経由のオープンウェイトモデルの提供を止めた。一次はゲートウェイ拒否で読めず、報道の突き合わせによる（industry）
  - 経路: 侵害された外部クラウド事業者を経由して開発用マシンに入られた。1回目（10/9 公表）では評価ジョブの環境変数（API キー・トークン）が読まれていた
  - 範囲: 影響したアカウント数・重みの量は非公表。顧客は1万社超で、Notion・Cursor・Harvey を含む
  - https://thehackernews.com/2026/11/fireworks-ai-breach-widens-to-expose.html
  - https://news.ycombinator.com/item?id=50437106
- [動向] **Anthropic の IPO 仮条件とロードショー** — Anthropic が 11/10 の修正届出で、Class A 普通株 8.25億株を1株 $70〜78 で Nasdaq に「ANT」として上場し、最大 $64.4B を調達するとした。評価額は TechCrunch が完全希薄化で最大 $1.404兆、The Decoder が最大 $1.02兆と報道で幅がある。CNBC によると 11/18 に価格を決め、11/19 に取引を始める見込み。Q3 の売上は $16.96B（前四半期比+47%）（industry）
  - https://the-decoder.com/anthropic-kicks-off-ipo-roadshow-offering-shares-at-70-to-78-and-targeting-a-trillion-dollar-valuation/
  - https://techcrunch.com/2026/11/10/anthropic-sets-ipo-price-range-of-70-to-78-per-share-to-reach-an-implied-valuation-of-1-404-trillion/
- [据え置き] **未決の買収協議と国内調査** — Amazon × Decart、Nvidia × Reflection AI の協議に続報はなく、IDC Japan・MM総研・NRC の新しい公表もない（industry）

### 日本語コミュニティ

- [動向] **Qiita の Copilot Studio / Copilot 記事** — Qiita に、Copilot Studio で社内エージェントを作ったときの権限まわりのハマりどころと、Microsoft Copilot の Code タブで何が作れるかを Learn の記載と実機で突き合わせた記事が 11/10 に出た（Copilot）
  - https://qiita.com/tags/copilotstudio/feed

## 直近の注目予定

- **11/12**: Anthropic の改定 Usage Policy が発効 ／ Copilot Studio の GPT-4.1 / GPT-5 系と、Microsoft Copilot ハーネスの GPT-5 Chat・GPT 5.6 Sol / Luna が退役（MC1506318） ／ Purview Data Governance が退役に入る ／ OpenAI → Cursor のモデル供給停止予定（一次未読）
- **11/13**: Excel と Cowork の会計機能が GA（MC1536053）
- **11/15**: Dataverse for Teams 環境とアンマネージド開発者環境の新規作成が停止 ／ Copilot Studio のカスタム採点器ライブラリが GA
- **11/16**: Copilot から Claude Opus 4.8 / Opus 5 / GPT-5.6 Terra を廃止 ／ Teams の旧 GitHub アプリが退役 ／ `pull_request_target` の2回目の試験ブロック ／ Fable 5.2 ローンチ特典の Pro・Team 標準席の枠が 23:59 PT に終了 ／ Cowork / Autopilot の Engage プラグインが GA ／ PPAC のフィードバックフォームの既定ポリシーが GA
- **11月中旬**: UBB の入口のアクセス要求の新しい管理設定が入る（MC1546354）
- **11/17**: Gemini API の Live / TTS preview モデルが停止（4〜5種。一次未確認） ／ Gems が Gemini アプリの設定パネルへ移動 ／ Intelligent call delegation が従量課金のパブリックプレビューに移行
- **11/17〜20**: Microsoft Ignite（11/17 基調講演）
- **11/18**: Anthropic の IPO 価格決定（11/19 取引開始の見込み・報道） ／ MODS の Workforce Insights エンドポイントが退役（MC1542066）
- **11/19**: Claude Enterprise で Claude Data が既定でオンになる
- **11/20**: Copilot Studio のコスト管理を M365 管理センターへ移す機能が GA（MC1530368） ／ Conductor のクラウド版が終了（二次）
- **11/24 以降**: `claude-opus-4-5-20251101` の暫定退役日（確定日ではない）
- **11/29**: OpenAI が Daybreak Blue のセッションデータの学習利用を開始（二次）
- **11/30**: `claude-sonnet-4-5-20250929` が退役 ／ Opus 4.8 の fast mode を削除 ／ OpenAI の Evals・`v1/prompts`・Agent Builder が停止 ／ App Builder のアプリが開けなくなる ／ vibe.powerapps.com と Power Automate のデザイナーの Copilot が退役 ／ Gemini 4 Argon の導入価格が終了
- **12/1**: Gemini 4 Argon の単価が $4/$20 に倍増 ／ Copilot の前提サブスク不要オファーが開始
- **12/2**: GitHub が公開リポジトリの `pull_request_target` を既定でブロック ／ Power Platform のプロンプトから Anthropic・Grok・旧 GPT 系モデルが退役（MC1536101）
- **12/4**: Copilot Studio エージェントの指標とアラートが GA（MC1538998）
- **12/7**: Purview DSPM のパートナー連携の一部が退役（MC1545691）
- **12/8**: GitHub が1年活動のないリポジトリの Dependabot アラートを停止 ／ M365 Copilot in Power BI が既定でオン（MC1546429）
- **12/9**: EU / EFTA で Claude モデルが既定で有効になり、「M365 アプリの Copilot だけで許可」が退役（MC1546438）
- **12/11**: Power Apps の式の生成・Power Apps Ideas などが退役（MC1532421・MC1532426）
- **12/14**: claude.ai/design の単体サイトが閉鎖
- **12/31**: Claude Security の無償クレジットの対象期間が終了 ／ Copilot の Fable 系の ZDR 例外が終了（以後は EFS） ／ Partner Center の Copilot in 30 プロモーションが終了
- **2027-01-06**: OpenAI `tts-1` / `tts-1-hd` / `gpt-4o-mini-tts` 2版が停止
- **2027-01-14**: OpenAI `gpt-4o` 2版 / `gpt-4o-mini` / `gpt-4.1` / `gpt-4.1-mini` が停止
- **2027-01-15**: Claude Code Review の Enterprise 向けクレジット請求期限
- **2027年1月中旬**: Power BI の単体の Copilot が退役（MC1546429）
- **2027年1月末**: UBB の入口が既定で表示され、旧設定が退役（MC1546354） ／ ChatGPT Classic（旧デスクトップアプリ）が終了（1/30・二次）
- **2027-02-01**: OpenAI `gpt-5.5-cyber-preview` が停止
- **2027-02-10**: OpenAI `gpt-image-2` / `gpt-image-2-2026-04-21` が停止
- **2027-03-08**: Fable 5.2 ローンチ特典のリセット（Max / Ultra / premium 席）が失効
- **2027-04-01**: OpenAI `gpt-5.1` / `gpt-5.3-codex` / `gpt-5.4-nano` が停止
- **2027-11-12**: Purview Data Governance のサポートが終了

## 改善メモ

- 障害の変化（industry）: `www.notion.com`・`thehackernews.com`・`www.theregister.com` がゲートウェイ拒否（新規。Fireworks AI 侵害の一次・詳報に届かず）
- Master・Copilot は新規提案・障害の変化なし。継続提案は Master 7件（最多 B-036、12回目）、Copilot 5件（最多 B-080、16回目）、industry 7件（最多 B-040、17回）
- ソース間の差異: Copilot の ZDR 例外の対象を Master は「Fable 5.2 / 5.1 / 5」、industry は「Fable 5.1・Fable 5」と書いている。本サマリーは「Fable 系」とし、5.2 が含まれるかは一次で再確認が要る
- ソース間の差異: Claude Data の接続先を Master は Amplitude・Mixpanel など、industry は Snowflake・Salesforce と書き、出典の記事 URL も異なる。Claude Meetings（近日）は industry のみが記載している
- 前日（11/10）分に欠損ソースはなく、欠損リカバリは不要
