# AI News Daily Summary — 2026-11-27

OpenAI はセルフサーブのファインチューニングの新規ジョブ作成の締切を 2027-01-06 から 2026-12-15 に早め、年明けの再学習は間に合わなくなった。GitHub は Copilot code review の課金先の既定を 12/30 から組織に変え、何も保存しない組織は AI Credits の従量課金で払うことになる。Microsoft は Copilot in 30 の試用 SKU を 12/1 から新しい ID に切り替え、CSP パートナーは登録を直さないと取引できない。

## 今日のハイライト

### 1. [廃止+予定] OpenAI がファインチューニングの新規ジョブ作成の締切を 2026-12-15 に前倒しした — 2027-01-06 を前提にした再学習の計画は3週間早く止まる

**要点**: OpenAI の廃止ページで、セルフサーブのファインチューニングの新規ジョブを作れなくなる日が、告知済みの 2027-01-06 から 2026-12-15 に早まった。既存顧客もこの日以降は再学習できない。年明けに再学習を予定していた組織は、残り18日で済ませる必要がある。

**詳細**: OpenAI の廃止ページ「Update to OpenAI's self-serve fine-tuning」節による（industry）。前倒しを告知した日付は書かれていない。WebSearch の結果はまだ 1/6 のままで、二次報道は見つかっていない。
- 2026-05-07: ファインチューニングを一度も実行していない組織は作成できなくなった（実施済み）
- 2026-07-02: 過去60日にファインチューン済みモデルで推論していない組織は学習ジョブを作れなくなった（実施済み）
- 2026-12-15: すべての組織が新規ジョブを作れなくなる
- 作成済みのファインチューン済みモデルは、元のベースモデルが退役するまで推論で使える

出典:
- https://developers.openai.com/api/docs/deprecations

### 2. [料金+破壊的変更] GitHub が Copilot code review の課金先の既定を 12/30 から組織に変える — 何も選ばないと、メンバーの Copilot 枠で賄っていたレビューが組織の AI Credits 従量課金に乗る

**要点**: GitHub が 11/25、Copilot Business / Enterprise で課金先が未設定のとき、ライセンスを持つメンバーの code review を 12/30 から「メンバーの Copilot 枠」ではなく「リポジトリを所有する組織」へ請求すると告知した。従来どおりにするには、期限までに管理者が Member を保存する必要がある。

**詳細**: GitHub changelog（11/25）による（Master・industry）。単価はページに書かれていない。
- 今の既定: 選択を保存していなければ、メンバー自身の Copilot の利用枠を使う。設定画面には期限まで `Default (Member)` と変更の告知が出る
- 12/30 以降の既定: リポジトリを所有する組織に請求する。組織側は AI Credits の従量課金が前提で、支出が増えうる
- 例外: AI Credits の従量課金が無効・請求ロック中・請求先が無いアカウントは Member に設定される。すでに Member / Organization を保存した組織はその選択が残る
- ライセンスの無いメンバー向けの別設定は変わらない。Enterprise が管理している場合は Enterprise オーナーが選ぶ

出典:
- https://github.blog/changelog/2026-11-25-copilot-code-review-billing-will-default-to-the-organization

### 3. [破壊的変更+料金] Microsoft が Copilot in 30 の試用 SKU を 12/1 から新しい ID に切り替える — CSP パートナーは登録を直さないと取引できず、オファーは 2027-03-31 まで延びた

**要点**: Partner Center 11月ページの Ignite のまとめ（11/25 付）によると、CSP パートナーが 12/1 以降も Copilot in 30 の試用を取引するには、システムに `CFQ7TTBZWGG1:0008` を登録しておく必要がある。12/31 で終わるとしていた試用オファーは、2027-03-31 まで延びた。

**詳細**: 11/25 23:04Z の改訂（`4407678d`・`ms.date` 11/25）で、11/25 付の3項目が加わった（Copilot）。
- Microsoft 365 E7 AI Activation Offer: 新しい CSP サブスクリプションで E7 を300ライセンス以上買った顧客に、6か月分 $7,500 の Copilot クレジットを追加料金なしで付ける。2027-03-31 まで
- パートナー特典: Partner Launch Benefits と Partner Success Core Benefits に M365 Copilot Business が追加料金なしで入った。新しい Partner Success Advanced Benefits には Copilot Studio の容量が入る
- Business Central + Copilot のバンドル: 2027-01-01 から提供される（既報の日程のまま）

出典:
- https://learn.microsoft.com/en-us/partner-center/announcements/2026-november

## カテゴリ別まとめ

### OpenAI / Codex / ChatGPT

- **ファインチューニングの新規作成の前倒し**（ハイライト1参照）
- [料金] **GPT-6.2 Astra の利用上限** — OpenAI の Codex 担当の Thibault Sottiaux 氏が、GPT-6.2 の展開時に課金の不具合で大半の利用者に誤った割引が掛かっていたと認めて修正した。修正後は Astra で40%、Sol で25%早く上限に達し、導入初週の消費ペースは見積もりの基準にならない（industry）
  - それでも上限までの量は GPT-6 Astra・GPT-6.1 Sol のときより多い。他のモデルは影響を受けず、差額のさかのぼり請求もしない
  - 補償: Go・Plus・Pro・Business の全員に保存できるリセットを1回追加し、Business には年末まで Fast Mode を無料で開放する
  - 対象が ChatGPT・Codex・API のどれかを記事は明記していない（日本語の二次報道は ChatGPT と Codex の有料プランとしている）
  - https://the-decoder.com/gpt-6-2-astra-users-now-hit-limits-40-faster-after-openai-patched-a-pricing-error/
- [版更新] **Codex の pre-release `0.174.0-alpha.7`** — OpenAI の Codex は安定版 `0.172.0`（11/24）のまま、pre-release が `0.174.0-alpha.7`（11/26）に進んだ。alpha のリリース本文は版番号だけである（Master）
  - https://github.com/openai/codex/releases
- [据え置き] **OpenAI のその他の一次** — API changelog（11/24）、community Announcements（11/20）、`openai.com/news`（11/24）、ChatGPT release notes（11/23）、ChatGPT & Codex changelog（11/24）、Deployment Safety Hub（11/23）、misalignment reports（First posted 最新 11/18・29件）は動いていない（Master・industry）

### Anthropic / Claude

- [新機能] **Skills over MCP（beta）** — Publickey（11/26）によると、エージェントは MCP サーバーに接続したときにスキルを受け取り、必要な場面でだけ読み込めるようになった。これまでは `SKILL.md` などを実行環境に置く必要があった。Anthropic は対応を始め、Claude と Claude Code の Pro・Max・Ultra で既定で有効にした（Claude Code 側は `2.1.332` の MCP スキル対応として 11/26 に収録済み。仕様の版は記事に無い）（industry）
  - https://www.publickey1.jp/blog/26/mcpskills_over_mcpmcp.html
- [動向] **Messages API の Rust 移行の検証手順** — GIGAZINE（11/26）が、11/26 に収録した Anthropic の移行記事の検証手順を紹介した。稼働中の Python 版を正解として同じリクエストの結果を突き合わせ、差異をグループ化して Claude のエージェントに直させ、人が承認した。2026年4月時点では Rust 版がテストの約98%に合格しても実トラフィックとの一致は約4分の1で、移植したテストの100カ所以上で合格条件が緩められていたという（industry）
  - https://www.anthropic.com/research/migrating-api-to-rust
- [観測] **Claude の Google Drive ファイルブラウザー** — TestingCatalog が、Anthropic が Claude に Google Drive のファイルブラウザーを用意しているとの観測を報じた（二次・公式未確認・リリース日なし）（Master）
  - https://www.testingcatalog.com/anthropic-prepares-google-drive-file-browser-for-claude/
- [据え置き] **Anthropic のその他の一次** — Claude Code（`2.1.332`・npm `stable` は `2.1.326`）、Platform release notes（11/23 付6項目）、モデル退役一覧（Active 16件・最新告知 11/23 Opus 4.5）、`/news`（11/20）、`/research`（11/25）、`claude.com/resources/articles`（11/24）、`support.claude.com`（11/24）は動いていない（Master・industry）

### GitHub Copilot / GitHub

- **Copilot code review の課金先の既定変更**（ハイライト2参照）
- [版更新] **Copilot CLI の pre-release `v1.0.117-2`** — GitHub の Copilot CLI は安定版 `v1.0.116`（11/25）のまま、pre-release が `v1.0.117-2`（11/26）まで進んだ（Master）
  - https://github.com/github/copilot-cli/releases

### Microsoft 365 Copilot / Cowork

- **Copilot in 30 の試用 SKU の切り替え**（ハイライト3参照）
- [廃止+新機能] **Cowork のモデルピッカーの入れ替え** — Microsoft が `cowork-models`（11/26 01:03Z `80197bc3`）を改訂し、利用者は GPT 6.2 Sol と GPT 6.2 Astra を選べるようになった。GPT 6.1 Sol、GPT 6 Astra、GPT 5.6 Terra は選べなくなり、ピッカーは Auto と6モデルになった（前回は7モデル）。旧モデルを名指しした手順や試算は引き直しになる（Copilot）
  - GPT 6.2 Sol: Microsoft がホストし、OpenAI をサブプロセッサーとして無効にしたテナントでも使える。Fast オプションがある。GPT 6.2 Astra は OpenAI がサブプロセッサーとして提供する
  - 残ったモデル: Claude Opus 5.5、Claude Sonnet 5.5、Claude Fable 5.2、Grok 4.7。EU Data Boundary 内では GPT 系しか使えない注記も残る
  - Auto: 既定の選択肢で、Fast オプションが付いた。管理者が無効にしたモデルは Auto の候補からも外れる。同じ節で Customize ページが Plugins に改名された
  - What's New は「GPT 6.1 Sol が GPT 5.5 を置き換える」と書いたままで、GPT 6.1 Sol を外したモデル表と合わない
  - https://learn.microsoft.com/en-us/copilot/cowork/cowork-models
  - https://learn.microsoft.com/en-us/copilot/cowork/whats-new
- [新機能] **Copilot デスクトップアプリのアプリ内ブラウザーの管理ポリシー** — Microsoft が MC1568702（11/25・GA）で、管理者が Windows と Mac の Copilot デスクトップアプリの内蔵ブラウザーにエンタープライズポリシーを掛けられるようにした。対象はセキュリティ、プライバシー、コンテンツへのアクセス、認証とネットワーク、ダウンロードと権限の各領域で、2027年1月の既定オン（MC1560922）にオフ以外の選択肢ができた（Copilot）
  - 追加のポリシーが効くのは `BrowsingEnabled` で内蔵ブラウザーを有効にしたときだけ。1/3 までの判断が要ることは変わらない
  - https://mc.merill.net/message/MC1568702
- [廃止] **Researcher の Copilot メモリの取り消し** — Microsoft が Roadmap 562996 を 11/26 のバッチで `Cancelled` にした。過去のやり取りを Researcher に引き継ぐ予定だった機能で、Roadmap はこの項目はもう正確ではなく削除すると書いている（Copilot）
  - https://www.microsoft.com/releasecommunications/api/v1/m365
- [新機能] **Outlook の共有・代理メールボックスで Copilot Chat** — 共有メールボックスの利用者と代理人は、クラシック Outlook で共有メールボックスをリソースとして追加すれば、そこから Copilot Chat を使えるようになった。Roadmap 573698 の状態が 11/26 に `Rolling out` へ進んだ（Copilot）
  - https://www.microsoft.com/releasecommunications/api/v1/m365
- [予定] **Copilot の回答を出典付きでコピーする設定** — Microsoft が MC1568700（11/25）で、利用者が Copilot の回答をコピーするときに出典を含めるかを選べるようになると告知した。「Copy with sources」は既定でオンになり、展開は12月中旬に始まり12月下旬に終わる。管理者の作業は要らない（Copilot）
  - https://mc.merill.net/message/MC1568700
- [予定] **Copilot Analytics のアクセス管理** — Microsoft が Roadmap 578862（11/26 起票・January CY2027）で、グローバル管理者・AI 管理者・Viva Insights 管理者が Copilot Analytics の閲覧範囲と権限を製品内で割り当てられるようになると告知した。M365 管理センターの VFAM と製品内の Manager Settings に分かれていた設定がまとまり、既存の割り当てはシステム定義のポリシーに自動で移る（Copilot）
  - https://www.microsoft.com/releasecommunications/api/v1/m365
- [予定] **旧来の Teams 保持ポリシーの再告知** — Microsoft が MC1481313 を 11/25 に再告知した。旧来の Teams 保持ポリシーが Copilot の対話を対象から外す日程は、2027年1月中旬開始・1月末完了のままである。Copilot の対話を保持・削除したい組織は、Copilot ワークロード用の保持ポリシーを別に作る必要がある（Copilot）
  - https://mc.merill.net/message/MC1481313
- [観測] **Roadmap の新規バッチ** — Release Communications の API と RSS は 2,420 項目を返し、前日の 2,411 から9件増えた。11/26 00:16Z のバッチは Dynamics 365 Finance が中心で、Copilot 関連は上の3件のほかに Excel の iPhone 版の Edit with Copilot（577177・`Launched`）がある（Copilot）
  - https://www.microsoft.com/releasecommunications/api/v2/m365/rss
- [据え置き] **Release Notes・Purview・Cowork の管理者統制・ブログ** — M365 Copilot Release Notes（先頭 November 17）、Purview と拡張機能の What's New、`cowork-admin-governance` などの Cowork 前提ページは前日から変わっていない。TC の各 board と M365 Developer Blog にも新しい記事は無い（Copilot）
  - https://learn.microsoft.com/en-us/microsoft-365/copilot/release-notes

### Copilot Studio / Power Platform

- [予定] **Dataverse の Filter-based Security** — Microsoft が Roadmap 581895（11/26 起票・March CY2027）で、管理者とメーカーが Dataverse のレコードへのアクセスを条件付きフィルターのポリシーで一元管理できるようになると告知した。レコードを個別に共有しなくてよくなる（Copilot）
  - https://www.microsoft.com/releasecommunications/api/v1/m365
- [据え置き] **Copilot Studio と Power Platform の一次** — Copilot Studio What's New（`1e58d09d`）、課金レート表（`ed8d14af`）、PPAC の容量管理、ガイダンスハブ、モデル表3本、非推奨一覧、Released Versions（2026.6.3）は前日から変わっていない。Copilot ブログと Power Platform ブログにも新しい記事は無い（Copilot）
  - https://learn.microsoft.com/en-us/microsoft-copilot-studio/whats-new

### 開発ツール・エージェント

- [破壊的変更+新機能] **Orca `v1.4.278`** — Stably AI が 11/26 に Orca `v1.4.277` と `v1.4.278` を続けて出し、`v1.4.278` で Gemini CLI の対応を削除した。Google 系のエージェントは Orca 内でサインインできる Antigravity の `agy` に一本化され、Gemini CLI を Orca から使っていた環境は移行が要る（Master）
  - `v1.4.278`: 新しい bot は Claude 固定ではなく既定のエージェントで始まる。Claude と Codex の長い返答を滑らかにストリーミングする。ClickUp / Airtable / Todoist / Zapier / Granola / Intercom をワンクリックで接続できる
  - `v1.4.277`: インストール済みプラグインのスキルが最初のメッセージ前から `/` メニューに出る。Windows の Codex で Stop が正しく効き、偽の利用上限が出なくなった。Google アカウントをエージェントごとに選べる
  - https://github.com/stablyai/orca/releases
- [新機能] **Devin の管理と MCP の更新** — Cognition が Devin に 11/24・11/25 付の更新を入れ、管理者は Bot が automation を保存する前に人の承認を必須にできるようになった。MCP の OAuth クライアント資格情報の取得失敗が成功と表示されなくなった（Master。11/26 は最上位を 11/23 と記録して取りこぼし、本日はじめて載った）
  - 11/24: Bot に Auto-approve automations の切り替えが付き、メッセージ欄が書式と Markdown 入力に対応した
  - 11/25: 「Creator only」共有のセッションに Enterprise 管理者が自分を足して読み取り専用で開ける。Blueprint に `clone.filter`（blobless / treeless）が加わった。Jira Rovo から起動したセッションに Jira playbook と添付が渡る
  - https://docs.devin.ai/release-notes/overview
- [据え置き] **Cursor・xAI・TypeSafe AI・MCP・Hugging Face・Obsidian・Apple** — Cursor の changelog（11/6）とフォーラム（10/12）、xAI（11/19）、TypeSafe AI（9件）、MCP blog（11/24）、Obsidian（1.15.1）、Apple Developer News（11/18）は動いていない。Hugging Face の8 org にも新しいリポジトリは無い（Master）

### Google

- [据え置き] **Gemini アプリと The Keyword** — Gemini アプリ（11/19）と The Keyword の AI カテゴリ（11/24）は動いていない。Workspace Updates の 11/25 付は Meet ハードウェアの操作パネルの並び替えで、AI とは関係が無い（Master）
- [観測] **Gemini API changelog に届かない** — Gemini API changelog は転送先 `aistudio.google.com` に届かないままである（Master の B-088、industry の B-048）

### 市場・企業

- [予定] **さくらインターネットの「シンプルAI」** — Publickey（11/26）によると、さくらインターネットはシステムへの AI 組み込み向けに、月額固定料金の「シンプルAI」を 12/10 に出す。従量課金の「さくらのAI Engine」とは別のサービスで、国産 LLM を含むモデルを長期に提供し、ISMAP への登録を申請中とした。月額・モデル名・利用上限は記事に無い（industry）
  - https://www.publickey1.jp/blog/26/aiai_1.html
- [動向] **Nvidia の東南アジア4カ国への出荷停止** — The Decoder（11/26）は Financial Times の報道として、Nvidia が Dell・Supermicro などにマレーシア・シンガポール・タイ・インドネシア向けのサーバー出荷停止を指示したと報じた。米商務省の新しい輸出規制は、東南アジアのクラウド事業者に90日以内のライセンス申請と、制限対象の企業が利用者にいないことの証明を求める。停止が一時的かは不明（industry）
  - https://the-decoder.com/nvidia-halts-server-shipments-to-malaysia-singapore-thailand-and-indonesia-after-tighter-us-export-controls/
- [据え置き] **Nvidia × Inception、Nvidia × Reflection AI** — 2件の買収協議に続報はない。Anthropic の終値の一次、MM総研と IDC Japan の新しい公表も見つからなかった（industry）

## 直近の注目予定

- **11月下旬**: Copilot ライセンスの無い利用者の検索画面が新しくなる（MC1562275）。Copilot Code のローカル Sandbox が既定でオンになる（MC1519871）。Copilot のタスクバー固定の通知の展開が始まる（MC1567263）
- **11月中**: GitHub の cloud sandbox の課金が始まる（日付は明記なし）
- **11/29**: OpenAI が Daybreak Blue のセッションデータの学習利用を始める（二次）
- **11/30**: `claude-sonnet-4-5-20250929` が退役し、Opus 4.8 の fast mode が削除される。OpenAI の `/v1/prompts`・Evals・Agent Builder が停止する。Power Automate デザイナーの Copilot と Copilot Studio の Mistral Medium 3.5 が退役する。GPT-5.6 Sol の期間限定価格と Gemini 4 Argon・Carbon の導入価格が終わる。この日以降の Claude Code で managed マーケットプレイスの自動更新が既定でオンになる
- **12/1**: Copilot in 30 の試用は新しい SKU ID（`CFQ7TTBZWGG1:0008`）でしか取引できなくなる。GitHub の使用量レポートに `user_id` 列が加わる。PPAC のデータエクスポートがインベントリを出力しなくなる（MC1567221）。OpenAI `gpt-image-1-mini` / `gpt-image-1.5` / `chatgpt-image-latest` が停止する。Gemini 4 Argon・Carbon の単価が $4/$20 に倍増する。Copilot Studio のワークフローの Code ノードが GA になる
- **12/2**: GitHub が公開リポジトリの `pull_request_target` を既定でブロックする。Power Platform のプロンプトから Anthropic・Grok・旧 GPT 系が退役する（MC1536101）
- **12/3**: Agent ノードからのファイル生成が GA になる（MC1561859）
- **12月上旬**: Teams のチャネル単位の Copilot がパブリックプレビューに入る（MC1562277）。Mac の PowerPoint の Copilot のプラグインの展開が終わる（MC1556095）
- **12/8**: GitHub が活動の無いリポジトリの Dependabot アラートを停止し、ARM32 ジョブのサポートを終える。Dataverse のエージェントユーザーが GA、M365 Copilot in Power BI が既定でオンになる
- **12/9**: EU / EFTA / UK で Claude モデルが既定で有効になる（MC1546438）
- **12/10**: さくらインターネットの「シンプルAI」の提供が始まる
- **12/11**: OpenAI `gpt-5` 系 / `o3` / `o3-pro` が停止する。ChatGPT の Advanced / Standard 音声モードが退役する（二次）
- **12/14**: Copilot から Claude Fable 5 / Haiku 4.5 / Gemini 3.8 Flash / Gemini 4 Argon / Grok 4.6 / Kimi K3 が廃止される。claude.ai/design の単体サイトが閉鎖する
- **12/15**: OpenAI のセルフサーブ・ファインチューニングで新規ジョブを作れなくなる（2027-01-06 から前倒し）。アンマネージドの開発者環境の削除が始まる（MC1515303）
- **12月中旬**: Copilot デスクトップアプリと Edge の同期が展開される（MC1562269）。Chat と Office のモデルの従量課金が GA になる（MC1557754）。Viva Insights の GitHub Copilot 指標の既定オンが始まる（MC1523085）。Copilot の回答の出典付きコピーの展開が始まる（MC1568700）
- **12月中**: ChatGPT と Codex の利用枠が Plus・Pro・Business で1つの予算に統合される（二次）
- **12/17**: Copilot Studio のワークフローのサービスプリンシパル認証が GA になる（MC1557509）
- **12/18**: Copilot から MAI-Code-1.1-Flash が廃止される
- **12月下旬**: Copilot のタスクバー固定の通知と、回答の出典付きコピーの展開が終わる（MC1567263・MC1568700）
- **12/30**: Copilot code review の課金先の既定が組織に変わる（Business / Enterprise。維持するには Member を保存）
- **12/31**: Copilot の Fable 5 系の ZDR 例外が終わる（以後は EFS が必要）。Claude Security の無償クレジットの対象期間が終わる。OpenAI の医療向けモデル構成の期間限定価格が最短でこの日に終わる。MCP の File Uploads 拡張を安定版にする目標
- **2027-01-01**: Anthropic の新しい開示期限（高・重大度30日）が、この日以降の報告に適用される。ChatGPT Sites の利用量がアプリに表示される。Business Central + Copilot のバンドルが提供される
- **2027-01-03**: Copilot デスクトップアプリのアプリ内ブラウズの既定オンに備える期限（MC1560922）
- **2027-01-06**: OpenAI `tts-1` / `tts-1-hd` / `gpt-4o-mini-tts` が停止する
- **2027-01-11**: OpenAI の EU データレジデンシーで GPT-5.2 / 5.4 / 5.4 mini の `fast` / `priority` 処理が停止する
- **2027-01-14**: OpenAI `gpt-4o` / `gpt-4o-mini` / `gpt-4.1` / `gpt-4.1-mini` が停止する
- **2027-01-15**: アンマネージドの開発者環境が完全に削除される。Claude Code Review / Claude Ship の Enterprise 向けクレジットの請求期限
- **2027年1月中旬**: 旧来の Teams 保持ポリシーが Copilot の対話に効かなくなる（MC1481313）
- **2027年1月**: Copilot Analytics の製品内アクセス管理（Roadmap 578862）
- **2027-01-20**: OpenAI `gpt-realtime` / `gpt-audio` 系が停止する
- **2027-01-22**: `claude-opus-4-5-20251101` / `claude-opus-4-5` が Claude API から退役する
- **2027-01-30**: ChatGPT Classic（旧デスクトップアプリ）が終了する（二次）
- **2027-01-31**: テナント App Catalog への app-only 書き込みに `SharePointTenantSettings.ReadWrite.All` が必須になる。ChatGPT Sites のホスティングの無料期間が終わる
- **2027-02-01**: Google Workspace で外部 AI エージェントの MCP 利用の強制が始まる（REST の直接呼び出し不可）。ChatGPT Sites で月間枠を超えた分の課金が始まる。OpenAI `gpt-5.5-cyber-preview` が停止する
- **2027年2月**: VS Code の Copilot から Local harness が削除される
- **2027-02-10**: OpenAI `gpt-image-2` が停止する。Claude Meetings の成果物の無料期間が終わる
- **2027-02-15**: Copilot Studio の Claude Opus 4.8・Opus 5・Sonnet 4.6・Sonnet 5 が退役する
- **2027-02-26**: OpenAI `/v1/audio/translations` が停止する
- **2027年2月末**: Clipchamp のプロンプトからの動画作成が新しい体験に置き換わる（MC1566260）
- **2027-03-01**: GPT-6.2 Astra・Sol の Ultrafast が Standard の3倍から6倍になる
- **2027-03-08**: Fable 5.2 ローンチ特典のリセット（Max / Ultra / premium 席）が失効する
- **2027-03-30**: MCP 仕様 `2027-03-30` 版のリリース予定
- **2027年3月**: Dataverse の Filter-based Security（Roadmap 581895）
- **2027-03-31**: Copilot in 30 の試用オファーと M365 E7 AI Activation Offer が終わる
- **2027-04-01**: Google Workspace API の Scaled 枠の課金が始まる（標準枠超過のプロジェクトは指定しないと上限が戻る）。OpenAI `gpt-5.1` / `gpt-5.3-codex` / `gpt-5.4-nano` が停止する
- **2027-05-17**: GitHub Copilot の MAI Code 2・MAI Code 2 Flash の導入価格が終わり、単価が倍になる
- **2027-09-15**: Dataverse for Teams 環境の削除が始まる（MC1515294）

## 改善メモ

- Master: 新規提案・障害の変化なし。継続提案の最多は B-088（Gemini API changelog の URL 差し替え、24回目）。11-26 に Devin の 11/24・11/25 付を取りこぼしたため、本サマリーでも本日はじめて載った
- Copilot: 新規提案・障害の変化なし。継続提案 5件（最多: B-080 Cowork の Learn URL の移設、29回目）
- industry: 継続提案 7件（最多: B-048 Gemini 一次 URL、25回目）。見送り候補 B-036
- ソース間の差: OpenAI のファインチューニングの新規作成の制限を、Master の注目スケジュールは 2027-01-06 のまま載せ、industry は廃止ページで 2026-12-15 への前倒しを確認した。本サマリーは一次を読んだ industry の 12/15 を採った
- ソース間の差: Copilot code review の課金先の既定変更は Master と industry がともにハイライトにし、タグ（`[料金+破壊的変更]`）も一致した。本サマリーは1件に寄せた
- ソース間の差: Cowork の What's New は「GPT 6.1 Sol が GPT 5.5 を置き換える」と書いたまま、モデル表は GPT 6.1 Sol を外しており、一次どうしが合わない（Copilot の指摘）
- ソース間の差: Messages API の Rust 移行は 11/26 に収録済みのため、本日は industry が加えた検証手順の詳細だけを `[動向]` で載せた
