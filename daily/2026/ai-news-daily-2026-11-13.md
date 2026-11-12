# AI News Daily Summary — 2026-11-13

M365 Copilot の予約実行は Copilot 自身の仕組みに移り、Power Platform 版のスケジュール済みプロンプトは 12/31 に退役する。前日に消えた Purview Data Governance の退役の節は、Partner Center に日付を改めて戻った。Google は Gemini 4 Hydrogen を $1.50 / $7.50 で出し、12/1 に倍額になる Argon を性能でも上回ったと報じられている。Anthropic は Managed Agents のサービス本体を自社環境で動かせる版を private beta で出した。

## 今日のハイライト

### 1. [廃止+破壊的変更] Power Platform 上の M365 Copilot のスケジュール済みプロンプトが 12/31 に退役し、Copilot のネイティブな予約実行に移る — 自動で移らない予約は、利用者が年内に作り直さないと止まる

**要点**: 予約実行の基盤が Power Platform から M365 Copilot 自身に移る。Power Automate を無効にしているテナントでも予約が動くようになる一方、移行の対象外の予約は 12/31 で止まる。管理は Copilot アプリの Tasks > Scheduled に移る。

**詳細**: MC1550533（11/12 公開・Major change・Retirement・Act by 12/31）。
- 展開: Frontier / TAP は 11/11、全世界は 11/30〜12/31。退役は 12/31
- 上限: 1ユーザーあたり有効な予約10件・合計50件。承認が要るタスクは、利用者が会話で応答するまで止まる
- 移行期間: Scheduled タブが出てから30日間は、従来の「…」メニューからも開ける。過去の実行結果は残る
- 管理者の作業: 利用者への周知と、自動で移らない予約の再作成の案内。対象は M365 Copilot のプレミアムライセンスの利用者

出典:
- https://mc.merill.net/message/MC1550533

### 2. [廃止] Partner Center に Purview Data Governance の退役の節が戻った — 前日の本サマリーの「一次の根拠がなくなった」は覆り、11/12 退役開始・2027-11-12 サポート終了を移行計画の期日として扱える

**要点**: 11/11 に消えた節「Update on the Microsoft Data Governance strategy」が、11/12 17:03Z の改訂で日付を November 12, 2026 に改めて戻った。対象は Unified Catalog・Data Map・Workflows・Azure Purview で、Purview のデータセキュリティとコンプライアンスは変わらない。

**詳細**: `2026-november` は `a54215d5` → `25fd8573`（`ms.date` 11/12）。
- 本文: 11/12 から退役が始まり、サポートは 2027-11-12 に終わる。新しいデータガバナンスの提案は Microsoft Fabric と OneLake カタログを軸にするよう求めている
- 対象読者: GSI 向けの告知。Purview What's New（`4a204948`・10/20 から改訂なし）と Message Center には本日も退役の記載がない
- 本サマリーの「直近の注目予定」に 2027-11-12 のサポート終了を戻した

出典:
- https://learn.microsoft.com/en-us/partner-center/announcements/2026-november

### 3. [料金+新機能] Google の Gemini 4 Hydrogen が $1.50 / $7.50 で出て、上位の Argon を性能でも上回ったと報じられた — 12/1 に $4 / $20 へ倍額になる Argon を前提にした費用の試算は、Hydrogen で引き直す対象になる

**要点**: Google が 11/12、Gemini 3.8 Flash の後継として Gemini 4 Hydrogen を Google 検索に全世界で入れた。The Decoder によると単価は入力 $1.50・出力 $7.50 で、AA Index でも Argon を上回る。単価と API での提供は Google の一次で未確認。

**詳細**: 検索への投入は Google のブログ（一次）、単価と性能は The Decoder（11/12）による。
- 単価: 入力 $1.50・出力 $7.50・キャッシュヒット $0.075（100万トークンあたり）。コンテキストは入力・出力とも最大 1M
- 性能（Hydrogen 対 Argon）: AA Intelligence Index 51 対 50（xhigh は 54）、SWE-sweep 13.5% 対 4.3%、OSWorld-2.1 77.6% 対 74.7%。Chartography だけは Argon が上（71.6% 対 66.6%）
- 提供先（The Decoder）: Gemini API（AI Studio）、Gemini アプリ、Google 検索、Antigravity（Pro・Ultra）、Gemini for Business。Google の検索ブログは API とアプリでの提供に触れていない
- Gemini API changelog は転送先の `aistudio.google.com` に届かず、Hydrogen の項目は確認できない

出典:
- https://blog.google/products-and-platforms/products/search/gemini-4-hydrogen-search-upgrade/
- https://the-decoder.com/googles-gemini-4-hydrogen-outscores-the-bigger-argon-just-four-weeks-after-its-launch/

## カテゴリ別まとめ

### Anthropic / Claude

- [新機能] **self-hosted の Claude Managed Agents** — Anthropic が 11/12、Managed Agents のサーバー・データベース・ワーカーを自社クラウドやオンプレミスで動かせる版を private beta で出した。これまで自社に置けたのはサンドボックスだけで、セッション履歴は Anthropic 側にあった。申し込みはアカウントチーム経由で、料金は書かれていない（Master・industry）
  - 構成: `cma-server`（API・エージェントループ・保存）と PostgreSQL 16 以降、ツールを実行するワーカー。DB を置かないとデータは再起動で消える
  - 推論先: Anthropic 直・Bedrock・Google の Agent Platform・Microsoft Foundry・自社ゲートウェイ。会話内容はモデル呼び出しごとに推論先へ出る。ZDR 契約があれば Messages API と同じく適用される
  - 自社の責任: サーバーの保護、更新、隔離。`bash` ツールはワーカーの権限で動く本物のシェルで、隔離は実行するコンテナや VM で確保する。一部の機能はホスト版にしか無い
  - https://platform.claude.com/docs/en/release-notes/overview
  - https://platform.claude.com/docs/en/managed-agents/self-hosted
- [新機能] **Claude for Manufacturing** — Anthropic が 11/12、Team / Enterprise プラン向けに製造業向けプラグインを出した。見積もり・品質報告・サプライヤー依頼を既存システムのデータで下書きし、送る前に担当者が確認する。スキルは17種類、コネクタは Autodesk Fusion・Infor・Microsoft 365・Oracle NetSuite の4種類で、機器の操作はしない（Master）
  - https://claude.com/resources/articles/claude-for-manufacturing
- [据え置き] **Claude Code と Anthropic の他の一次** — Claude Code の changelog は `2.1.322` が最上位のままで、npm も stable 2.1.311 / latest 2.1.322 で動いていない。モデル退役一覧、廃止履歴（9/30 が最新）、`/news`（11/10 IPO ロードショー）、`/research`、support の release notes、Privacy Center も変わらず、Opus 4.5（下限 11/24）の告知もない（Master・industry）

### GitHub Copilot / Microsoft 開発ツール

- [予定] **Copilot CLI の pre-release で旧リモート操作を削除** — GitHub が Copilot CLI の pre-release `v1.0.110-0`（11/10）で、旧来のリモート操作（steering）を削除した。クラウドセッションとリモート接続には AHP 環境が要る。安定版は `v1.0.109` のままで、pre-release は `v1.0.110-3`（11/12）まで進んだ。`-p` の JSON モードは認証失敗時も最後の result レコードを出すようになった（Master）
  - https://github.com/github/copilot-cli/releases
- [観測] **Copilot Studio の「GitHub Copilot harness」が新名に揃った** — Copilot Studio の Learn は 11/12 19:07Z の一括改訂（`1e58d09d`）で、追跡中の11ページから「GitHub Copilot harness」の表記が消えた。PPAC の費用管理のページは `manage-usage-github-copilot-harness` から `manage-usage-microsoft-copilot-harness` へ 301 で転送される（Copilot）
  - https://learn.microsoft.com/en-us/power-platform/admin/manage-usage-microsoft-copilot-harness
- [据え置き] **github.blog の Copilot changelog** — Copilot ラベルの最上位は 11/10 の Enterprise シート管理のまま動いていない（Master）

### Microsoft 365 Copilot

- [新機能] **Claude Fable 5.2 が Cowork と Copilot Studio に** — Microsoft が 11/11、Anthropic の Claude Fable 5.2 を Copilot Cowork と Copilot Studio の対象ユーザーへ展開し始めた。管理者は M365 管理センターで利用の可否を決められる。`cowork-models` と Copilot Studio のモデル表3本は本日も Fable 5.1 までで、5.2 は告知済み・表未掲載（Copilot）
  - https://techcommunity.microsoft.com/t5/microsoft-copilot-blog/available-today-anthropic-claude-fable-5-2-in-microsoft-copilot/ba-p/4571829
- [破壊的変更] **Copilot Workspaces でエージェントの個別選択が消える** — Copilot Workspaces の利用者は、Researcher・Analyst・Designer を選ぶ代わりにやりたいことを書けば、Copilot がスキルを自動で当てるようになる（MC1550540・Roadmap 516041）。Frontier で12月から始まり、GA は未定。3つのエージェントは Copilot アプリでは引き続き個別に使え、管理者は社内の研修資料を直すことになる（Copilot）
  - https://mc.merill.net/message/MC1550540
- [新機能] **Copilot コネクタの10月アップデート** — 利用者は、Copilot Chat・Word・Excel・PowerPoint・Researcher のどこでも同じコネクタのカタログを使えるようになった（TC・11/11）（Copilot）
  - 新しいコネクタ: Trello Enterprise、Galileo（HR）、PubMed・ClinicalTrials.gov など医療・ライフサイエンスの25件超
  - コネクタのスキル: HubSpot と Notion から始まり、Tasks で LexisNexis・Bloomberg などの数分かかるツールを進捗つきで実行できる
  - 既存コネクタ: ServiceNow はナレッジの添付を 64 MB まで扱い、Salesforce はカスタム項目、Confluence はページのコメントと添付に対応した
  - https://techcommunity.microsoft.com/t5/microsoft-copilot-blog/microsoft-copilot-connectors-update-october-2026/ba-p/4572240
- [新機能] **Copilot Chat のスキルが GA** — 利用者と開発者は、宣言型エージェントを作らずに、手順・リソース・スクリプトをまとめたスキルを Copilot Chat で使えるようになった（拡張機能 What's New・11/11）。利用者が選ぶか Copilot に自動で選ばせ、開発者はプラグインパッケージで配布できる（Copilot）
  - https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/whats-new
- [予定] **Teams の Facilitator が2027年2月へ延期** — Microsoft が、会議の疑問を Web 検索で答える Facilitator の Targeted Release を12月上旬から2027年2月上旬へ、GA を12月中旬から2027年2月中旬〜3月上旬へずらした（MC1409304・11/12 更新）（Copilot）
  - https://mc.merill.net/message/MC1409304
- [予定] **Copilot Workspaces の一般展開の時期** — Notebooks から Workspaces への切り替えは、Frontier の次に Standard release へ2027年1月まで、Deferred release へ2027年2月までに届く（MC1535647・11/11 更新）（Copilot）
  - https://mc.merill.net/message/MC1535647
- [据え置き] **その他の M365 Copilot** — Release Notes（先頭 November 4）、Cowork What's New、`cowork-admin-governance`、前提条件3本は改訂されていない。M365 ブログ（先頭 11/5）、SharePoint Blog（11/4）、Agent 365 Blog（11/10）に新しい記事はない（Copilot）

### Copilot Studio / Power Platform

- [新機能] **Copilot Studio What's New に October 2026 節** — Copilot Studio の What's New に、9月節以降はじめて10月の節が加わった（11/12 19:07Z）。11/4 のブログで既報の項目のほかに、本サマリー未掲載の4項目がある（Copilot）
  - ナレッジソースの制限: 管理者は PPAC の Security > Data and privacy で、ローカルファイル・SharePoint と OneDrive・公開 Web サイトを環境ごとに個別に禁止できる（設定ページは preview 表記）
  - モデルの据え置き: 既定のモデルが新しくなったあとも、最長30日はエージェントを今のモデルのまま使える
  - プライバシーの案内（preview）: 会話の冒頭に組織のプライバシーポリシーへのリンクを出せる
  - WhatsApp: 10/23 から、Azure Communication Services 経由のチャネルに新しいエージェントを接続できなくなった。接続済みのエージェントは動き続ける
  - https://learn.microsoft.com/en-us/microsoft-copilot-studio/whats-new
- [予定] **デスクトップフローの直接トリガー** — Power Automate のデスクトップフローは、クラウドフローを挟まずにイベントで起動できるようになる（Roadmap 579975・プレビュー2027年1月・GA 2027年3月）。同じバッチの 579974 では、Delinea Secret Server を外部の資格情報プロバイダーとして使えるようになる（Copilot）
  - https://www.microsoft.com/microsoft-365/roadmap?id=579975
- [動向] **Copilot Studio エージェントの統制の分担** — Microsoft が Copilot Studio Blog（11/12）で、エージェントの統制を PPAC・Entra・Purview・Agent 365・脅威対応の5つの役割に分け、どの管理者がどの製品で何を持つかを整理した。新機能の告知はない（Copilot）
  - https://techcommunity.microsoft.com/t5/copilot-studio-blog/where-do-i-govern-my-copilot-studio-agents/ba-p/4572592
- [据え置き] **Copilot Studio の他の Learn** — 課金レート表・課金3本・モデル表・ガイダンスハブは一括改訂で再ビルドされただけで、`ms.date` は動いていない。非推奨一覧も新しい節はなく、Released Versions は 2026.6.3 のまま135日たつ（Copilot）

### ライセンス・ガバナンス

- [動向] **Frontier Accelerate for Security に Agent 365 のモジュール** — Microsoft が、セキュリティ系パートナーの構想策定と POC の支援に、Agent 365 の試用を使うモジュールと提供ガイドを加えた（Partner Center 11月ページ・11/12 付）。対象の条件と顧客の要件は変わらない（Copilot）
  - https://learn.microsoft.com/en-us/partner-center/announcements/2026-november

### OpenAI / Codex / ChatGPT

- [破壊的変更] **Codex CLI 0.167.2 の Vertex AI の既定** — OpenAI が Codex CLI の安定版 `0.167.2`（11/11）で、Google Cloud Vertex AI 上ではツールの更新を逐次送るのを既定にした。止めるときは `config.toml` の `[features]` に `incremental_tools_legacy_gcp = false` を書く。pre-release は `0.170.0-alpha.2`（11/12）まで進んだ（Master）
  - https://github.com/openai/codex/releases
- [版更新] **ChatGPT for iOS の Codex 機能** — OpenAI が 11/10、iOS の Codex で全画面の入力欄に画像やファイルを貼れるようにし、Windows ホストのフォルダ選択でドライブを切り替えられるようにした（Master）
  - https://learn.chatgpt.com/docs/changelog
- [据え置き] **OpenAI の他の一次** — API changelog（11/5 `gpt-6-cyber`）、deprecations（11/10 GPT Image 2）、Deployment Safety Hub（11/5）、misalignment reports（11/10）、community Announcements（11/10）は動いておらず、11/12 の OpenAI の発表は検索で見つからない。Businesses in ChatGPT（beta）は前日の本サマリーに収録済み（Master・industry）

### Google

- [新機能] **Antigravity のリモートエージェント** — Publickey（11/13）によると、Google AI Pro・Ultra の個人加入者は、Google が管理する隔離されたクラウド VM で Antigravity のエージェントを動かし続けられるようになった。PC の電源を切っても作業が続き、スマートフォンから確認や指示ができる。11/6 の週から順次展開している（industry）
  - https://www.publickey1.jp/blog/26/google_antigravityaiai.html
- [新機能] **Sheets canvas の単独リンク公開** — Google が 11/11、Gemini で表計算のデータから作る Sheets canvas を単独のリンクとして公開できるようにした（Master）
  - https://workspaceupdates.googleblog.com/
- [観測] **Gemini API の一次に届かない** — `ai.google.dev/gemini-api/docs/changelog` の転送先 `aistudio.google.com` に本日も届かず、検索で見える最新は 10/27 で、Hydrogen・Decisions API・Carbon の項目は確認できない。11/17 の Live / TTS preview 停止は11日続けて一次で確認できておらず、Gemini アプリの release notes は 2026.10.13 のまま（Master・industry）

### AWS / クラウド

- [新機能] **公式の AWS エミュレータ** — Publickey（11/13）によると、AWS が SDK や CLI の呼び出しにローカルで AWS と同じ結果・エラーを返すエミュレータを正式にリリースした。無料で AWS アカウントも不要。コードは Bedrock AgentCore 上の自律エージェント数百体が書いたという。対応サービスの一覧は記事に無い（industry）
  - https://www.publickey1.jp/blog/26/awsawsaws_1.html

### Cursor / 開発ツール / エージェント

- [予定] **MCP 仕様のリリースを年2回に** — MCP の Core Maintainers が 11/11、仕様のリリースを原則3月と9月の最終火曜の年2回にすると決めた。次は `2027-03-30` 版で、既存のクライアントとサーバーに変更は要らない。リリースの2.5か月前に soft freeze、1か月前に hard freeze を置き、SDK が遅れても仕様の日付は動かさない（Master）
  - https://blog.modelcontextprotocol.io/posts/mcp-release-cycle/
- [版更新] **Orca v1.4.257 と Devin の 11/11 版** — Stably AI が 11/12 に Orca `v1.4.257` を出し、長いチャットの同時ストリーミング時のフリーズを減らした。Cognition は Devin の 11/11 版で、Devin が自分でリマインダーを設定して後から再開できるようにした（Master）
  - https://github.com/stablyai/orca/releases
  - https://docs.devin.ai/release-notes/overview
- [動向] **SlopCodeBench で Strict 合格率が1割台** — GIGAZINE（11/12）が紹介した SprocketLab の SlopCodeBench（36課題・196チェックポイント）で、コーディングエージェントは各段階の新機能だけを見る Core では65.82〜73.98%合格したが、過去の機能も壊さないことを求める Strict では12.24〜16.33%に下がった。最高は GPT-6 Astra XHigh の16.33%（industry）
  - https://gigazine.net/news/20261112-slopcodebench/
- [据え置き] **Cursor・xAI・TypeSafe AI・Hugging Face** — Cursor の changelog（11/6）とフォーラム（10/12）、xAI（grok-4.7 が最新）、TypeSafe AI（`jev-1.14.0`）は動いておらず、Hugging Face の8 org に新しいリポジトリもない。Obsidian 1.15.1 に AI 関連の変更はない（Master・industry）

### 業界・市場

- [動向] **Nvidia の Jensen Huang 氏が CEO を辞任** — The Decoder（11/12）によると、Huang 氏が CEO・社長・取締役を即日退き、CFO の Colette Kress 氏が暫定 CEO に就いた。WSJ は取締役会が解任を準備していたと報じ、10/29 の NYT 報道以降に時価総額は約 $1.4兆減った（industry）
  - https://the-decoder.com/jensen-huang-resigns-as-nvidia-ceo-after-espionage-scandal-wipes-out-1-4-trillion-in-market-valu
- [据え置き] **未決の買収協議と国内調査** — Amazon × Decart、Nvidia × Reflection AI の協議に続報はなく、Anthropic の IPO も 11/18 の価格決定待ちで仮条件（$70〜78）は変わっていない。IDC Japan・MM総研・NRC の新しい公表もない（industry）

### 日本語コミュニティ

- [据え置き] **Qiita / Zenn** — Copilot Studio の新しい記事は出ていない。Zenn の powerautomate の「HTTP 要求の受信時」トリガーの解説（11/12）は Copilot と関係がなく掲載を見送った（Copilot）

## 直近の注目予定

- **11/13（本日）**: Excel と Cowork の会計機能が GA（MC1536053）
- **11月中**: GitHub の cloud sandbox の課金が開始（日付は明記なし）
- **11/15**: Dataverse for Teams 環境とアンマネージド開発者環境の新規作成が停止 ／ Copilot Studio のカスタム採点器ライブラリが GA
- **11/16**: Copilot から Claude Opus 4.8 / Opus 5 / GPT-5.6 Terra を廃止 ／ Teams の旧 GitHub アプリが退役 ／ `pull_request_target` の2回目の試験ブロック ／ Claude Opus 4.6・Opus 4.5・Sonnet 4.5・Haiku 4.5 に透かしが入る ／ Fable 5.2 ローンチ特典の Pro・Team 標準席の枠が 23:59 PT に終了 ／ Cowork / Autopilot の Engage プラグインが GA ／ PPAC のフィードバックフォームの既定ポリシーが GA
- **11月中旬**: UBB の入口のアクセス要求の新しい管理設定が入る（MC1546354） ／ 単体の Word / Excel / PowerPoint エージェントの撤去が開始（MC1536062） ／ Copilot Chat のコンテンツソース絞り込みが展開（MC1548004） ／ Study and Learn 専用モードが開始（MC1548047）
- **11/17**: Gemini API の Live / TTS preview モデルが停止（4〜5種。一次未確認） ／ Gems が Gemini アプリの設定パネルへ移動 ／ Intelligent call delegation が従量課金のパブリックプレビューに移行 ／ Sales Agent のセマンティックモデルが GA（MC1540293）
- **11/17〜20**: Microsoft Ignite（11/17 基調講演）
- **11/18**: Anthropic の IPO 価格決定（11/19 取引開始の見込み・報道） ／ MODS の Workforce Insights エンドポイントが退役（MC1542066）
- **11/19**: Claude Enterprise で Claude Data が既定でオンになる
- **11/20**: Copilot Studio のコスト管理を M365 管理センターへ移す機能が GA（MC1530368） ／ Power Platform Monitor の毎時アラートがパブリックプレビュー ／ Conductor のクラウド版が終了（二次）
- **11/24 以降**: `claude-opus-4-5-20251101` の暫定退役日（確定日ではない）
- **11/29**: OpenAI が Daybreak Blue のセッションデータの学習利用を開始（二次）
- **11/30**: `claude-sonnet-4-5-20250929` が退役 ／ Opus 4.8 の fast mode を削除 ／ OpenAI の Evals・`v1/prompts`・Agent Builder が停止 ／ App Builder のアプリが開けなくなる ／ vibe.powerapps.com・Power Automate のデザイナーの Copilot・Describe it to design it が退役 ／ EU / EFTA のデータ移動オフ環境の GPT-5 Chat が終了 ／ Gemini 4 Argon の導入価格が終了 ／ M365 Copilot の新しい予約実行が全世界で展開開始（MC1550533）
- **12/1**: Gemini 4 Argon の単価が $4/$20 に倍増 ／ Copilot の前提サブスク不要オファーが開始
- **12/2**: GitHub が公開リポジトリの `pull_request_target` を既定でブロック ／ Power Platform のプロンプトから Anthropic・Grok・旧 GPT 系モデルが退役（MC1536101）
- **12/4**: Copilot Studio エージェントの指標とアラートが GA（MC1538998）
- **12/7**: Purview DSPM のパートナー連携の一部が退役（MC1545691）
- **12/8**: GitHub が1年活動のないリポジトリの Dependabot アラートを停止 ／ M365 Copilot in Power BI が既定でオン（MC1546429）
- **12/9**: EU / EFTA で Claude モデルが既定で有効になり、「M365 アプリの Copilot だけで許可」が退役（MC1546438）
- **12/11**: Power Apps の式の生成・Power Apps Ideas などが退役（MC1532421・MC1532426）
- **12月中**: ChatGPT と Codex の利用枠が Plus・Pro・Business で1つの予算に統合（二次） ／ Copilot Workspaces のエージェント個別選択が Frontier で消え始める（MC1550540）
- **12/14**: claude.ai/design の単体サイトが閉鎖
- **12月中旬**: UBB の「Learn more」に組織の URL を設定できるようになる（MC1546354）
- **12/31**: Power Platform 版のスケジュール済みプロンプトが退役（MC1550533） ／ Copilot Studio の会話内での接続設定が GA（MC1548034） ／ 環境間のコメントのインポート・エクスポートが終了 ／ Claude Security の無償クレジットの対象期間が終了 ／ Copilot の Fable 系の ZDR 例外が終了（以後は EFS） ／ Partner Center の Copilot in 30 プロモーションが終了 ／ MCP の File Uploads 拡張を安定版にする目標
- **2027-01-01**: Microsoft Commercial Cloud の現地通貨価格が5通貨で改定（日本円は対象外）
- **2027-01-06**: OpenAI `tts-1` / `tts-1-hd` / `gpt-4o-mini-tts` 2版が停止
- **2027-01-14**: OpenAI `gpt-4o` 2版 / `gpt-4o-mini` / `gpt-4.1` / `gpt-4.1-mini` が停止
- **2027-01-15**: Claude Code Review の Enterprise 向けクレジット請求期限
- **2027年1月**: Dataverse の列ベースのレコードセキュリティが GA（Roadmap 577860） ／ Copilot Workspaces が Standard release に届く（MC1535647）
- **2027年1月中旬**: Power BI の単体の Copilot が退役（MC1546429）
- **2027年1月末**: UBB の入口が既定で表示され、旧設定が退役（MC1546354） ／ Edge for Business の Copilot Chat による書き直しの展開が終了（MC1146821） ／ ChatGPT Classic（旧デスクトップアプリ）が終了（1/30・二次）
- **2027-02-01**: OpenAI `gpt-5.5-cyber-preview` が停止
- **2027年2月**: 日本円の2027年4月の価格改定の詳細が出る ／ Teams の Facilitator が Targeted Release に入る（MC1409304）
- **2027-02-10**: OpenAI `gpt-image-2` / `gpt-image-2-2026-04-21` が停止
- **2027-03-01 以降**: Gems が廃止（Business / Enterprise）
- **2027-03-08**: Fable 5.2 ローンチ特典のリセット（Max / Ultra / premium 席）が失効
- **2027年3月**: Power Automate のデスクトップフローの直接トリガーが GA（Roadmap 579975）
- **2027-03-30**: MCP 仕様 `2027-03-30` 版のリリース予定
- **2027 春**: Siri AI 対応アプリの App Store 提出受付が開始
- **2027-04-01**: OpenAI `gpt-5.1` / `gpt-5.3-codex` / `gpt-5.4-nano` が停止
- **2027-11-12**: Purview Data Governance（Unified Catalog・Data Map・Workflows・Azure Purview）のサポート終了

## 改善メモ

- 3ソースとも新規提案・障害の変化なし。継続提案は Master 7件（最多 B-036、12回目。B-088 は10回目）、Copilot 5件（最多 B-080、18回目。B-081 に `manage-usage-github-copilot-harness` の 301、B-083 に Purview の節の再掲を実例として追記）、industry 7件（最多 B-040、17回）
- 本サマリーの訂正: 11/12 分で「一次の根拠がなくなった」として外した Purview Data Governance の退役は、一次の節が戻ったため本日の注目予定に 2027-11-12 を戻した（ハイライト2）。11/12 分のファイルは書き換えていない
- ソース間の差異: Gemini 4 Hydrogen について、Master は Google の検索ブログを根拠に「API や Gemini アプリでの提供は記事に書かれていない」とし、industry は The Decoder を根拠に Gemini API・アプリ・Antigravity・Gemini for Business での提供と単価を書いている。Google の一次（`aistudio.google.com`）には両ソースとも届いていない
- ソース間の差異: Gemini Decisions API を、11/12 分の本サマリー（Master 由来）は入力 $0.10 と書いたが、industry は本日「単価未確認」として採録を見送っている
- ソース間の差異: Copilot の ZDR 例外の対象を Master は「Fable 5 系」、industry は「Fable 5.1・Fable 5」と書いている（継続）。本サマリーは「Fable 系」とする
- 前日（11/12）分に欠損ソースはなく、欠損リカバリは不要
