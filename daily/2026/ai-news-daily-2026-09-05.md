# AI News Daily Summary — 2026-09-05

9月3日〜4日は、期日の短い作業が2件降ってきた一方で、前日までの整理が1件覆った日である。GitHub は `gh` の Linux 署名鍵の失効を告知2日前に出し、期日は本日9月5日にあたる。Microsoft は Power Automate メーカーポータルの PVA ヘルプチャットボットを 9/9 に削除すると非推奨一覧へ追加した。OpenAI は GPT-6 Astra の単価と仕様を一次で公開し、短文脈 $10/$50・長文脈 $20/$75 が確定したことで、「最上位のサイバー能力は API 調達の対象から外れた」という 09-03・09-04 の読みはモデル本体には当たらないことが判明した。Claude Code 2.1.260 は Bash 権限チェックの脆弱性を複数修正したが、前版 2.1.259 で入った `Read()` 拒否ルールの拡張が同時に差し戻されており、2版で前提が反転している。Anthropic 側では Cowork にデスクトップ専用ブラウザが載っていたことが9日遅れで判明し、クラウド調達では Lambda との約 $350億契約とリボルビング枠 $150億への拡大観測が加わった。

## 今日のハイライト

### 1. gh の Linux 署名鍵が本日失効する — 4月8日より前に APT / RPM で入れた環境は今日中に鍵を入れ替える

**要点**: GitHub が `gh` の Linux パッケージ署名鍵を本日 **9/5** に失効させる。告知は 9/3 で猶予は2日しかなかった。2026年4月8日より前に APT / RPM で導入した環境は、鍵を更新しない限り以後の取得が検証エラーで止まる。

**詳細**: 失効するのは GitHub CLI の Linux パッケージリポジトリ用 PGP 鍵で、以後 APT / RPM のリポジトリメタデータと新規公開の RPM パッケージは差し替え鍵のみで署名される。対象は APT リポジトリ（Debian / Ubuntu 系）と RPM リポジトリ（Red Hat / Fedora 系）の2経路である。

- 影響を受けない導入方法を一次告知が明示している
  - Windows / macOS を使っている場合
  - ソースからビルドしている場合
  - Homebrew・Conda・コミュニティ製パッケージマネージャー経由
  - GitHub Releases の `.deb` 直取得または単体バイナリ
- 差し替え鍵を含むキーリングは **2026年4月8日**に公開済みで、それ以降に導入・更新した環境は対応済みである。手当てが要るのは、それより前に入れて以来キーリング設定を触っていない環境に限られる。手順は一次告知および GitHub CLI issue #13118 に記載がある

⚠️ 本件は GitHub Changelog で **Retired** 区分の告知として出ており、通常のリリース告知の並びからは目に入りにくい。CI ランナーやコンテナイメージで `gh` を APT 経由で入れている場合、失効後の初回 `apt update` で初めて表面化する。

- https://github.blog/changelog/2026-09-03-github-cli-linux-package-signing-key-expires-september-5

### 2. Power Automate のヘルプチャットボットが 9/9 に消える — ポータル内のヘルプ導線が Help (?) メニュー1本になる

**要点**: メーカーポータル左下の PVA ヘルプチャットボットが **9/9** に全ページから削除される。ポータル内でヘルプを引く導線は右上の Help (?) メニュー一本になり、チャットボットを前提に書いた社内手順書と研修資料は差し替え対象になる。

**詳細**: 一次は `power-platform/important-changes-coming` で、`updated_at` が **2026-09-04T19:03Z** へ動き、`## ` 見出しが 90本 → 91本に増えた。追加された節「Deprecation of help chatbot in Power Automate maker portal」は「Effective September 9, 2026, Microsoft is removing the Power Virtual Agents (PVA) help chatbot in the Power Automate maker portal from all pages」と発効日を明記する。Microsoft は削除理由を「PVA ヘルプチャットボットは旧来のサポート体験で、古く保守もほとんど行われていない」とし、右上の Help (?) メニューへヘルプとサポートの導線を集約すると説明する。

- 9/9 以降に起きるのは4点で、左下にチャットボットが表示されなくなり、チャットボットへの質問ができなくなる。一方で Help (?) メニューは引き続き利用でき、そこからのヘルプ記事閲覧とサポート要求の作成も続けられる
- クラウドフロー・デスクトップフロー・コネクタなど Power Automate の他の機能には影響しない。管理作業は不要で、Microsoft が求めているのは利用者への周知と社内文書の更新だけである

⚠️ **本ページは週次確認ソースで、直前の定例確認は 9/3 だった。**次回の定例は 9/10 で、発効日 9/9 の翌日にあたる。02 はこれを根拠に、非推奨一覧の確認頻度を週次から毎日へ引き上げる提案（B-058）を起票している。

- https://learn.microsoft.com/en-us/power-platform/important-changes-coming

### 3. GPT-6 Astra の単価と仕様が一次で確定した — Critical 級のモデルが通常の API 調達に載り、Sol 比2.5倍で試算が引き直しになる

**要点**: OpenAI の公開料金ページに `gpt-6-astra` が載り、短文脈 入力 $10・出力 $50、長文脈 $20・$75 と明記された。「最上位のサイバー能力は API 調達の対象から外れた」とした 09-03・09-04 の整理は、**モデル本体には当たらない**。

**詳細**: 一次料金ページの Flagship Models 節に全ティアが掲載された（100万トークンあたり）。

- 短文脈: 入力 **$10.00** ／ キャッシュ入力 $1.00 ／ キャッシュ書込 $12.50 ／ 出力 **$50.00**
- 長文脈: 入力 $20.00 ／ キャッシュ入力 $2.00 ／ キャッシュ書込 $25.00 ／ 出力 $75.00
- Batch と Flex: いずれも短文脈で入力 $5.00 ／ 出力 $25.00（Standard の50%引き）
- Fast mode: 短文脈で入力 $20.00 ／ 出力 $100.00（Standard の2倍）

一次モデルページの仕様も確定した。コンテキスト 1,050,000トークン（最大入力 922,000）、最大出力 128,000、知識カットオフは 2026年4月30日。入力は text / image、出力は text で、computer use・MCP・hosted shell・apply patch・skills に対応する。提供経路は ChatGPT Plus / Pro / Business / Enterprise と OpenAI API に加え、Microsoft Azure と AWS Bedrock が並び、Enterprise はワークスペース単位の有効化かつ既定オフとされる。

⚠️ **既存コードがそのまま通らない制約が4点ある**。

- reasoning effort は `low` / `medium` / `high` / `xhigh` / `max` の5段階で、`none` は非対応
- `temperature` / `top_p` / log probabilities の指定を受け付けない
- tool calling は Responses API 必須で、Chat Completions では使えない
- エージェント動作中は misalignment monitoring が非同期で走る

⚠️ 単価は Sol 比で入力2.5倍・出力2.5倍にあたる（Sol は $4／$20 で据え置き）。既存の Sol ベースの試算をそのまま置き換えると費用が2.5倍で効き、長文脈側を使う設計では差がさらに開く。⚠️ Astra は realtime エンドポイント・Assistants API・ファインチューニング・embeddings・画像生成・音声処理・legacy completions に非対応で、既存パイプラインの一括置換はできない。

system card（`deploymentsafety.openai.com`・一次200）によれば、Preparedness Framework の Critical はサイバーのみで生物・化学は High。間接プロンプトインジェクションの堅牢性は 99.79%（従来 96.23%）、deployment simulation の severity-3+ フラグは GPT-5.6 Sol 比で 53% 減とされる。⚠️ 一方で chain-of-thought の監視可能性は従来モデル比で大幅に低下したと明記されており、敵対的条件下では意図的な性能低下（sandbagging）で監視を回避しうるとしている。⚠️ ベンチマーク値（FrontierMath Tier 4 98% / ARC-AGI-3 99.9% / ExploitBench 100% / 未知の 0-day 2件発見）と Microsoft Foundry の Limited Access Program 提供は二次情報である。

- https://developers.openai.com/api/docs/pricing
- https://developers.openai.com/api/docs/models/gpt-6-astra
- https://deploymentsafety.openai.com/gpt-6-astra
- https://developers.openai.com/api/docs/changelog

## カテゴリ別まとめ

### Anthropic / Claude

- Anthropic が Claude Code **2.1.260** をリリースした（9/3 22:32 UTC publish）。権限まわりの修正が中心で、会話の横に未コミット差分を出す Diff パネルが加わっている
  - 修正: Bash 権限チェックの複数の脆弱性 ／ 括弧を含むパスの `Edit` / `Write` / `Read` 権限ルールが無効扱いで捨てられ Bash サンドボックスからも無視される不具合 ／ コンパイルできないパターンのファイル権限ルールが1件あると全ファイル編集が `Invalid regular expression` で失敗する不具合
  - `REPORTTIME`・`REPORTMEMORY`・`DIRSTACKSIZE` への代入にコマンド置換を隠した zsh コマンドを自動承認していた不具合も塞がれた。`permissions.blockReadsOutsideWorkingDirectories` が macOS でサンドボックス下の git からユーザーの git 設定を隠す不具合も対象である
  - ⚠️ **差し戻しが1件ある。** 2.1.259 で入った「Bash の `Read()` 拒否ルールをオプション値のファイルにも適用する」変更が 2.1.260 で撤回された。09-04 の本サマリーはこれを統制の強化として記録しており、**2版で前提が反転している**
  - 統制面では、`!` の bash モードで打ったコマンドがサンドボックス外で実行されるようになり、閉じ括弧の後ろに文字が続く権限ルールは無効な設定として報告されるようになった。管理下 CLAUDE.md がセキュリティ承認ダイアログを出さなくなる変更も入っている
  - 機能面は `/diff`（フルスクリーン時に会話の横へ表示）、`/cost` とステータスラインへのキャッシュミス原因表示、ヘッドレスセッション向けの `/reload-plugins` と文字列版 `/advisor` である
  - ⚠️ **スケジュール実行環境の不具合修正が3版連続で続いている**（2.1.258・2.1.259・2.1.260）
- ⚠️ npm の `dist-tags` が `{stable: 2.1.236, latest: 2.1.260, next: 2.1.261}` になり、8/31 以降続いていた `next` == `latest` の合流が解けた。`2.1.261` は 9/4 17:49 UTC に publish されているが changelog に記載がなく内容は未確定である
  - `stable` は 2.1.236 のままで `latest` と **24版差**（前日23版差から拡大）。8/28 の 2.1.251 に入った symlink 経由の権限境界修正群は stable 固定組織へ8日経っても未到達で、本日の Bash 権限チェック修正も同じ経路で止まる
  - 欠番は `2.1.244` / `2.1.249` / `2.1.253`〜`2.1.256` の計6件で据え置きである
- Anthropic が Cowork のデスクトップアプリに専用ブラウザを内蔵した（**8/26** 公開・01 は9日遅れで初検出）。拡張機能なしでサイドパネルにブラウザが開き、Claude がページを読み・クリックし・入力する
  - 自分のタブ・ブックマーク・パスワードは見えない別プロファイルで、明示的に選ばない限り自分のブラウザからは何も共有されない。Claude in Chrome で必要だった「自分のセッションを貸す」判断が不要になる
  - ログインはサイト単位でインポートでき、macOS では Chrome / Edge / Firefox から、Windows / Linux では Firefox から取り込める（銀行・メール・シングルサインオンのサイトは除外）
  - 対象は Pro / Max / Team で macOS / Windows / Linux に順次展開し、Enterprise は管理者が Organization settings → Cowork → Built-in browser で有効化する。既に Claude in Chrome を使っている場合はそちらが既定のままで、設定 → Cowork → 優先ブラウザで切り替えられる
- Anthropic が `ant` CLI **v1.30.0** に `ant apply` を追加した（9/3）。リポジトリ内のファイル定義からエージェント・環境・スキル・メモリストア・デプロイメントを作成／更新できる
  - 実行計画を出して承認してから適用し、`claude-lock.json` をコミットして管理対象を追跡するため、以後の実行は新規作成ではなく同一リソースの更新になる。⚠️ エージェント構成の Infrastructure as Code 化にあたり、CI からの再実行が前提に置かれている
  - Claude Platform API release notes の日付列は 9/3 → 9/1 → 8/27 → 8/26 → 8/20 → 8/19 と連続しており、隣接日付ブロックの欠落は起きていない
- モデル退役ページに新規の退役告知はない。直近告知は 2026-06-05 の Opus 4.1（8/5 退役済み）のままで、Active は11件で据え置きである。表の外の Note にある `claude-mythos-preview` の deprecated 扱い（移行先 `claude-mythos-5`）も変わらない
- `claude.com/blog` は 9/2 の commerce agents 2本が最新のままで、`support.claude.com` の Release Notes も 9/1 の Fable 5.1 / Mythos 5.1 が最上位のままである
- ⚠️ Anthropic の8月 Risk Report は **20日連続で一次未読**である（初出 08-17）
- 既報: 週次上限50%増の 9/13 終了と 9/14 からの恒久 +25%（現行比17%減）、Enterprise Frontier Safeguards（9/1〜9/2・今秋から段階提供）、Fable 5.1 / Mythos 5.1 の GA（9/1）、Claudeforce（オープンベータは9月中）、Claude for Teachers（登録期限 2027-06-30）、ウェルビーイング研究助成 $5M（締切 9/21・full proposal 10/5）

### GitHub Copilot / 開発ツール

- GitHub が `gh` の Linux パッケージ署名鍵を本日失効させる（9/3 告知・ハイライト1参照）
- GitHub が Copilot CLI の安定版 **v1.0.83** を公開した（9/4 15:38 UTC）。8/29 の `v1.0.82` 以来6日ぶりで、`1.0.83-0`〜`-5` の pre-release 6版を束ねた内容になっている
  - 新機能: Windows 11 タスクバーにセッションを表示しホバーでステータスカードを出す ／ MCP の OAuth サインインで CIMD（Client ID Metadata Document）に対応 ／ `claude-fable-5.1` 対応 ／ セッションサイドバーの並べ替え（Recent / Created / Name / None）／ enterprise 管理者による GitHub 組織サインインのピン留め ／ HTTPS プロキシの mTLS クライアント証明書の自動処理 ／ Linux サンドボックスの egress 制限
  - 変更: カスタムエージェントが優先順位つきで複数モデルを列挙できるようになり、**廃止モデル（Claude・Gemini）がモデルピッカーから削除**された。10/2 の廃止に向けたクライアント側の反映は既に始まっている
  - 修正: セッションロック再入時のフリーズ、Kerberos プロキシ認証の再接続、タイムアウトしたシェルコマンド停止時のメッセージ処理、オートパイロット実行中のプロンプト消失、Anthropic セッション継続時の署名検証エラー
- GitHub が Actions の月初更新で権限とコンテキストを3件追加した（9/3）。ランナーの廃止時期を照会する REST API `GET /actions/runners/deprecations/{version}` が新設され、`runner_version`・`runtime_deprecates_at`・`registration_deprecates_at` をリポジトリ／組織／エンタープライズの各スコープで返す
  - `GITHUB_TOKEN` に Dependabot アラートを読み取り専用で扱う `vulnerability-alerts` 権限（`read` / `none`）が加わった
  - 再利用可能ワークフロー側に `job.workflow_ref`・`job.workflow_sha`・`job.workflow_repository`・`job.workflow_file_path` の4プロパティが追加された
- GitHub が CodeQL **2.26.4** を公開し、GitHub Actions 向けのセキュリティ検知を改善したとしている（9/3）
- GitHub が star 履歴を返す API エンドポイントを新設した（9/4）。プライバシーに配慮したデータを返す。⚠️ AI 関連の統制・料金には直接関わらないが、GitHub Trending 非公式RSS がゲートウェイ拒否で使えない現状に対し、リポジトリの伸びを別経路で測る材料になりうる
- `github.blog/changelog` の Copilot ラベルは 9/3 の3本が最上位のままで、9/4 の新規はない
- 既報: 4モデルの 10/2 廃止告知と Gemini 3.8 Flash の Copilot 提供開始（9/3・09-04 のハイライト1）、Copilot Business / Enterprise の新規申込再開（9/3）
- 期限: **9/10** MAI-Code-1-Flash 廃止、9/28 チャット3面統合／code review 既定 Balanced 化／チャットのデータ保持がアカウント存続期間へ、10/1 既存顧客前払い必須、10/2 Gemini 3.5 / 3.6 Flash・Kimi K2.7 Code・Claude Opus 4.7 の廃止、12/31 Fable 5.1 / Fable 5 の ZDR 暫定免除終了と Gemini 3.8 Flash 導入価格終了

### Microsoft 365 Copilot / Copilot Studio / Power Platform

- Microsoft が Power Automate メーカーポータルの PVA ヘルプチャットボットを 9/9 に削除する（ハイライト2参照）
- Microsoft が SharePoint の全テナントに「AI 向け HTML ガイダンス」ページを用意した（一次は SharePoint Blog の月次記事・**9/2 23:26Z** 公開）。`https://[tenantname].sharepoint.com/_html` を Cowork / Scout / GitHub Copilot / Copilot Studio に渡すと、SharePoint のサンドボックスで動く HTML を生成でき、SharePoint リストにライブ連結したレポートも作れる
  - 狙いは「AI アシスタントは標準的な Web HTML を生成するが、それが SharePoint で期待どおり動くとは限らない」点の解消で、SharePoint の要件を毎回説明する手間をなくすことにある。テナントで新しい機能が使えるようになると内容が自動更新される
  - 同記事は他に3系統を挙げる。個人スキルが全 SharePoint サイトで使えるようになる ／ 手で指示文を書き直す代わりに Copilot にテストと評価基準の作成・測定付きの修正提案まで依頼できる ／ ライブラリ内の画像を1枚ずつ開かずに機器やラベルの特定と可視テキスト抽出をまとめて依頼できる
  - ワークフローは2種で、ファイル追加・メタデータ更新を契機に Teams のチャット／チャネルへ投稿する通知と、ファイルやリストの文脈に紐づけたまま回す承認ルーティングである。利用条件は Microsoft 365 Copilot ライセンスで、管理者の追加設定は記載されていない
- Microsoft が SharePoint ニュース投稿の Viva Engage クロス投稿を提供開始した（9/3）。ストーリーラインまたはコミュニティへ配信でき、SharePoint 側と Engage 各面のコメント・返信・リアクションは1つの会話として同期される。⚠️ Copilot 固有の機能ではない
- M365 Roadmap の 9/3 22:50Z バッチは3件で、Copilot Studio / M365 Copilot の項目は含まれない（総項目数 **1,782**）
  - **570445** Microsoft Purview: 自動ラベル付けのスケーラビリティ・ポリシー管理・レポートを拡張する。より大きな SharePoint スコープに対応する（Preview 2026年9月 / GA 2026年10月）
  - **570443** Microsoft Edge: タブと Workspace のグルーピング・命名・ラベルを提案する。管理者は `TabServicesEnabled` ポリシーで制御する（GA 2026年10月）
  - **570439** Microsoft Teams: 外部送信者のメッセージに含まれる QR コード画像を既定でぼかし、閲覧前に明示操作を求める（GA 2026年10月）
- Release Wave の 9/3 リネーム後5ページはいずれも 200 で取得でき、`updated_at` 2026-09-03T14:35:00Z・`git_commit_id` `06b3b6ba` から動いていない。緑チェックの増減もなく、9/4 に確定した未達7行に変化はない
- ⚠️ 定点の停滞が続いている。Copilot Studio の What's New は July 2026 節が最新のままで、June 節の GitHub Copilot ハーネスは GA（8/3）から **33日連続**で `(Production-ready preview)` と書かれている。9/2 の Copilot Blog 記事が「now generally available」と明記した状態との食い違いは解消していない
  - Released Versions は Copilot Studio Build **2026.6.3**（6/30 初出）のままで空白は **67日**に達した。ページ本文は「This page is updated each week on Tuesday.」と書いたままで、次の定例日は 9/8 である
  - Copilot Studio の Roadmap 項目は19件で全件 `In development` のまま増減がない。566997 は GA 期日「August CY2026」未達、562221 は GA 期日 2026年6月から超過4か月目である
  - Copilot Tuning の一次は停止発効（8/20）から **16日**たっても停止も退役も記載していない（`updated_at` 2026-08-18T17:48Z）
- M365 Copilot の Release Notes は **August 25, 2026** バッチが最新のままで、10節・全19項目に増減はない。隔週傾向どおりなら次バッチは 9/8 前後である
- ⚠️ AI at Work roadmap の Latest announcements は 7/24 の Opus 5 告知が先頭のままで、8月に続いて9月も追加がない。9/2 に告知された Claude Fable 5.1 は、Opus 5・GPT-5.6・Sonnet 5 と同じ「Available today」型の発表でありながら広報枠に載っていない
- ⚠️ Copilot Studio のモデル可用性一覧（`authoring-select-agent-model`）は `updated_at` 2026-08-03T14:59Z から1か月以上動かず、Fable 5.1 の行は本日も存在しない
- Tech Community の「What's New in Microsoft Copilot | August 2026」は board RSS 上の `pubDate` が 9/3 16:04Z へ再び移動した。8/31 17:51Z → 9/2 18:43Z に続く2度目の移動で、内容は 9/2 に掲載済みの既報である
- Partner Center の9月ページは `updated_at` 2026-09-03T16:03Z・掲載3件のままで、9/4 から追記がない

### OpenAI / Codex / ChatGPT

- OpenAI が GPT-6 Astra の単価と仕様を一次で公開した（ハイライト3参照）
- OpenAI が Responses API に3つの制御を追加した（9/3）。長時間動くエージェントの待ち時間と手戻りを減らす方向の追加になっている
  - async tool calling: アプリ側が function / custom tool を実行している間もモデルが作業を続け、結果は揃い次第返す
  - mid-turn steering: 応答の生成中に WebSockets 経由で追加指示を送り、モデルが訂正を取り込める
  - mid-conversation reasoning effort: キャッシュされたプロンプト prefix を保ったまま effort を上げ下げできる
- OpenAI が Codex CLI の安定版を3版出した。`0.153.1`（9/3 21:02 UTC）／ `0.153.2`（9/3 23:53 UTC）／ `0.153.3`（9/4 19:01 UTC）で、いずれも GPT-6-Astra 対応まわりのホットフィックスである
  - `0.153.3` は **Amazon Bedrock** のモデルピッカーへ GPT-6-Astra を追加し（Mantle と Runtime の global / US ルート）、非同期の clarification 質問がテキストのみを受け付けることをガイダンスへ反映した
  - pre-release は `0.154.0-alpha.2`（9/3 21:58 UTC）と `0.154.0-alpha.3`（9/4 00:57 UTC）の2版だが、⚠️ いずれも本文が展開されず内容は未確定である
- GPT-5.6 の Sol / Terra / Luna 全ティアの単価は **12日連続で据え置き**である。Sol は入力 $4／出力 $20、Batch / Flex は50%引きで、Sol の期間限定価格は「少なくとも 11/21 まで」の記載が続く。本日の変化は既存単価ではなく掲載範囲の側にある
- ⚠️ Cyber 節の3世代は前日から変わっていない。`gpt-5.6-cyber` は入力 $12.50／出力 $75.00、`gpt-5.5-cyber` はキャッシュ書込のみ空欄、`gpt-5.4-cyber` は単価欄がすべて空のままで、09-04 に「次アクション」として挙げた欄の充足は起きていない
- OpenAI の Deprecations ページに新規告知はない（最新は 8/26 の文字起こし4モデル・停止 2027-02-26）。**GPT-6 Astra の登場に伴う退役告知も出ていない**。⚠️ 今月中に 9/24 の Videos API / Sora 2 系と 9/28 の旧 GPT-3.5 系4モデルの2件が到来する
  - ⚠️ 11/30 の Evals 廃止の代替として一次が挙げるのは Promptfoo という外部OSSで、Agent Builder の代替は Agents SDK または ChatGPT Workspace Agents である。**OpenAI 内の後継が用意されていない廃止**が混じっている
- `community.openai.com` の Announcements RSS が 9/3 の GPT-6-Astra 告知で10日ぶりに動いた。ChatGPT Plus / Pro / Business / Enterprise への展開と AWS 経由の API 提供、コンテキスト 1.05M / 最大出力 128K を一次で確認できる
- `learn.chatgpt.com` 経由（WebSearch）で 8/31〜9/4 の記載を2件拾えた。GPT-6-Astra Fast tier の説明が「1.5x」から「2x speed, increased usage」へ訂正され、既定モデルを変えずモデルピッカーにも出さずに API 経由で GPT-6-Astra を設定できるようになった。⚠️ ゲートウェイ拒否のため一次未読で、個々の公開日も単独では確定できない

### Google

- Google が `gemini-3.8-flash` を 9/2 に一般提供へ移した（03 が `ai.google.dev` の changelog で確認）。用途として長時間の software engineering・自律エージェント・複雑なエンタープライズワークフローを挙げる。GitHub Copilot 側の提供開始（9/3）はこの GA の翌日にあたる
  - ⚠️ 01 は本日「Google 単体の発表ではなく Copilot 側の changelog でしか確認できていない」と書いており、03 の記述と食い違う（改善メモ参照）
- Google が `lyria-3.5` を 9/3 に公開した。フル長楽曲の生成に対応し 44.1kHz ステレオ音声を出力する。⚠️ 音楽生成は 01・03 とも関心領域の除外対象にあたるため、定点の変化の記録として1行に留める
- Gemini API changelog の日付列は 9/3 → 9/2 → 9/1 → 8/27 → 8/26 → 8/13 で連続しており、9/4 の追加はない
- HF の `google` org は `timesfm-3.0-pytorch`（作成 8/24）が最新のままで、9/3・9/4 の新規作成も更新もない
- 既報: `gemini-3.8-flash` の入力 $0.75 / 出力 $3.75 は **12/31 まで**で 2027-01-01 から $1.50 / $7.50、9/1 の agentic video understanding（長尺で最大88%のトークン削減）、旧 `gemini-omni-flash-preview` は 9/30 廃止、Gemini 3.5 Pro GA は未ローンチ継続
- ⚠️ 登録済み Google 系5ソースはゲートウェイ拒否が継続しており、`ai.google.dev` だけが到達できる Google 一次である

### オープンウェイト / MCP / Cursor / xAI / Devin

- 追跡8 org のいずれにも 9/3・9/4 の新規公開はない。`Qwen`/`moonshotai`/`deepseek-ai`/`meta-models`/`mistralai`/`zai-org`/`openai`/`google` を `createdAt` 降順と `lastModified` 降順の両方で確認した
  - `lastModified` が 9/4 に動いたのは `zai-org` の GLM-5.3 系4リポジトリ（06:38〜06:45 UTC）で、作成日は全て 8/25 のままなのでカード更新にあたる
  - HF の追跡8リポジトリは全て `private: false` / `gated: false` で公開状態に変化がない。⚠️ `downloads` は30日ローリングで増減するため前日比の増分は記録しない。09-03 に観測した「全件同値」の日次バッチ遅延は本日も再現していない
- `blog.modelcontextprotocol.io` は 8/22 の「The New MCP Roadmap」が最上位のままで、**14日間**新規がない
- WebMCP Challenge の提出締切 9/4 は UTC で経過した。受賞発表は 9/23 で賞金総額 $35,000 である。⚠️ WebMCP は MCP 公式ブログ側に一切言及がなく、OpenAI 発の別系統として扱われている
- Cursor の changelog は 9/2 の Self-hosted machines が最上位のままで、9/3・9/4 の追加はない。フォーラム Announcements も 9/2 の Grok Bot Android 版が最上位のままである
- ⚠️ Grok 4.7 の公開予定日は二次で **9/11〜9/12** のまま新しい材料がない。`docs.x.ai` のモデル一覧は依然 grok-4.6 が上限で、モデル ID・価格・コンテキスト長・ベンチマークカードはいずれも存在せず、出所は Musk の X 投稿のみである。公式提供中の最新は Grok 4.6（8/12・context 50万トークン・$2/$6）
- ⚠️ 01 が Devin の CLI changelog ホスト `cli.devin.ai` を本日はじめて試行し、ゲートウェイ拒否だった。`docs.devin.ai` と同じ扱いになる。二次が挙げる更新（`devin doctor` によるサブエージェント frontmatter 検査、dead code の cleanup スキャン、Agent Plugins 1.0.0 互換ほか）は公開日を特定できないため新着扱いしない
- A2A（Agent2Agent）の AAIF 参加は未確定のままで、一次3ホストはゲートウェイ拒否が継続している

### 料金 / 企業動向 / 市場データ

- Microsoft AI が MAI-Transcribe-2 を Azure Speech の public preview で公開した（9/3）。導入価格は **12/31 まで**1音声時間あたり **$0.10** で、前世代 MAI-Transcribe-1 の launch price $0.36/時から約72%安い
  - FLEURS ベンチマークの60言語平均で単語誤り率 5.2% とし、Gemini 3.5 Transcribe・GPT-Transcribe・Whisper V3-Large・Scribe V2 を上回るとする。話者ダイアライゼーションと単語単位タイムスタンプに対応し、長尺音声で最大10倍高速とされる
  - ⚠️ 一次 `microsoft.ai` はゲートウェイ拒否で、数値は複数の二次スニペットの突き合わせによる。⚠️ 期間限定価格の終了日が OpenAI Sol（11/21）・Copilot の Gemini 3.8 Flash（12/31）と並び、**年末に単価が動く前提が3件そろった**
- Anthropic がリボルビング・クレジット・ファシリティの **$150億**への拡大を詰めているとされる（9/3）。昨年確保した $25億の6倍にあたり、当初目標とされた約 $100億も上回る
  - Morgan Stanley が主導し、Goldman Sachs / JPMorgan Chase / Citigroup が主要な役割を担うとされる
  - ⚠️ リボルビング枠の確定は IPO の直前手続きにあたる。Anthropic は SpaceX の $750億（オーバーアロットメント込み $862億）と同等以上の調達を狙うとされる。⚠️ 一次未読で、PYMNTS / Seeking Alpha / Yahoo Finance / Investing.com の二次一致で採った
- Anthropic が Nvidia 出資の Lambda と約 **$350億**のクラウド契約を結んだとされる（8/31〜9/1 報・01 が本日はじめて検出）
  - 対象は Hut 8 が開発するテキサス州 Nueces County のデータセンターで規模は約 350MW。Lambda が Nvidia チップを設置し、Nvidia 自身がデータセンターのリースを保有する
  - ⚠️ これで Anthropic の直近クラウド契約は計 $1,750億とされる（Nscale $450億 / Fluidstack $500億 / SpaceX $450億 / Lambda $350億）。⚠️ 一次未読で Bloomberg / WSJ 発の二次一致による
- OpenAI が GPT-6 Astra のサイバー能力を段階提供にしたとされる。まず重要インフラ防護に責任を持つ個人・組織（米政府、trusted access プログラム参加者）の alpha テスターへ、次に Daybreak Blue 経由で防御目的の利用者へ広げるとされる
- Business Insider Japan が主要8サービスの2026年9月版料金早見表を公開した。8月は主力プランの価格が概ね据え置かれた一方、Google が18歳以上の大学生へ Google AI Plus（月額725円相当）を無償提供するとされる。エージェント関連では SpaceX AI の Grok Bot、Perplexity の Computer in Email、Google の Gemini Spark が挙がっている。⚠️ 一次 `www.businessinsider.jp` はゲートウェイ拒否のため内容は検索スニペット経由である
- 市場データは国内・グローバルとも新規公表がない。IDC / IDC Japan・MM総研・Similarweb・NRC のいずれにも新しい調査発表はなく、引用可能な最新値は Gartner の「AI モデル・プラットフォームへの世界エンドユーザー支出 2026年 $64B（前年比 +63.4%）」（7/20 公表）、「AI セキュリティ市場 2027年 $4.8B（前年比 +68.7%）」（8/26 公表）、Similarweb の生成AI ウェブトラフィックシェア（ChatGPT 約53%・Gemini 約27〜28%・Claude 約9%・2026年5月時点）で据え置きである。⚠️ いずれも本日の新規公表ではないため、鮮度を明示したうえで使う
- 既報: 国防総省による supply-chain risk 指定の継続表明（9/3）、米司法省の statement of interest（9/1）、GenAI.mil への ChatGPT Mil / Grok for Government 追加（9/1・Anthropic は非参加）、Anthropic の IPO 観測（10月・$2T 超）、年換算 run-rate $650億（7月末）、SpaceX による Cursor 買収完了（8/14・$60B）

### Apple / クラウド

- `developer.apple.com` は 9/1 の「Upcoming changes to Rosetta support for Intel-based macOS apps」が最上位のままで、9/2〜9/4 の新規はない。macOS 26.4 以降は Intel 専用アプリの起動時にシステム通知が出て、**macOS 27 が Rosetta を載せる最後のリリース**になる
- ⚠️ Apple の AI 関連の最新は 6/11 の ImageCreator クラス廃止告知のままである（8/5 の App Store creative assets 以降に新規なし）
- ⚠️ 01 が `azure.microsoft.com` を本日はじめて試行し、ゲートウェイ拒否だった。GPT-6 Astra の Microsoft Foundry 提供は同ホストのブログが一次だが読めず、二次の記述に留まる
- AWS Bedrock は Codex CLI `0.153.3` 経由で GPT-6-Astra を扱えるようになった（OpenAI 節参照）
- 既報: 8/26 の特別イベント告知（**9/9 10:00 PT**）、8/24 Sign in with Apple 新ドメイン（`private.icloud.com`）、8/18 EU 向けビジネス条件変更（発効 2026-10-01）

## 直近の注目予定

- **9/5（本日）**: **`gh` の Linux パッケージ署名鍵が失効**
- **9/7**: 週次復旧チェック（月曜）／ ppweekly・課金レート表の週次確認
- **9/8**: M365 Copilot Release Notes の次バッチ見込み ／ Copilot Studio Released Versions の定例更新日
- **9/9**: **Power Automate メーカーポータルの PVA ヘルプチャットボット削除** ／ Apple 特別イベント（10:00 PT）／ GLM-5.3-Flash の Z.ai 経由50%割引が終了 ／ Microsoft の月次パートナースキリングセッション開始
- **9/10**: MAI-Code-1-Flash が全 Copilot 体験から廃止 ／ 非推奨一覧の週次確認（発効日の翌日）
- **9/12**: Grok 4.7 の公開予定（Musk の X 投稿のみが出所・公式の裏づけなし）
- **9/13**: **Claude Code の週次上限50%増が終了**
- **9/14**: Claude Code の標準週次上限が恒久的に +25%（現行比では17%減）
- **9/17**: OpenAI DevDay Exchange の応募締切
- **9/21**: Anthropic ウェルビーイング研究助成の応募締切
- **9/23**: WebMCP Challenge の受賞発表
- **9/24**: OpenAI の Videos API と Sora 2 系が退役（代替モデルの提示なし）
- **9/28**: Copilot のチャット3面統合 ／ code review の既定 effort が Lite → Balanced ／ チャットのデータ保持がアカウント存続期間へ ／ OpenAI の `gpt-3.5-turbo-instruct` / `babbage-002` / `davinci-002` / `gpt-3.5-turbo-1106` が停止
- **9/29 以降**: `claude-sonnet-4-5-20250929` の暫定退役日（確定日ではない）
- **9/30**: Gemini の旧 `gemini-omni-flash-preview` エンドポイント廃止 ／ Power Platform 2026 Wave 1 の対象期間終了
- **9 月**: iOS 27 / macOS 27 GA ／ Claudeforce のオープンベータ ／ Copilot Studio の Roadmap 11件が GA 期日 ／ Copilot Tuning の Public Preview 再開 ／ Release Plans on Learn の新規掲載停止 ／ 570445 Purview 自動ラベル付けの Preview ／ App Store の Social Media 年齢レーティング回答が必須化 ／ OpenAI の IPO 観測
- **10/1**: Copilot Business・Enterprise の既存顧客が前払い必須に ／ Apple の EU 向け新ビジネス条件が発効 ／ Ask Gemini in Chat のプロモーション上限が終了
- **10/2**: **Copilot から Claude Opus 4.7 / Gemini 3.5 Flash / Gemini 3.6 Flash / Kimi K2.7 Code が廃止**（残り27日）
- **10/5**: Anthropic ウェルビーイング研究助成の full proposal 提出期限（採択者）
- **10/15 以降**: `claude-haiku-4-5-20251001` の暫定退役日（確定日ではない）
- **10/16–11/11**: OpenAI DevDay Exchange 8都市（東京は 10/20）
- **10/23**: OpenAI のレガシースナップショット退役（`gpt-3.5-turbo-0125` / `gpt-4-0613` / `o1-2024-12-17` / `o4-mini-2025-04-16` とファインチューン版）
- **10/27〜29**: Power Platform Community Conference 2026（ラスベガス MGM Grand）
- **10/31**: OpenAI の既存 evals が読み取り専用になる
- **10 月**: Copilot Studio 569474（app-first なエージェント作成）GA ／ 570433 MCP Apps の Preview ／ 569475 エージェント共有 GA ／ 570445 / 570443 / 570439 の GA ／ Anthropic の IPO 予定（$2T 超の評価額を目標と報道）／ 韓国 App Store のコンテンツ記述子2件が All → 12+
- **秋**: Anthropic の Enterprise Frontier Safeguards が段階的に提供開始（二次情報）
- **11 月**: 570433 MCP Apps の GA ／ 570468 録画・文字起こしポリシー整合の GA
- **11/15**: Release Planner 退役
- **11/21**: GPT-5.6 Sol の暫定値下げが有効とされる期限
- **11/24 以降**: `claude-opus-4-5-20251101` の暫定退役日（確定日ではない）
- **11/30**: OpenAI の Reusable prompts・Evals プラットフォーム・Agent Builder が停止
- **12/1**: OpenAI の GPT Image 系が停止（`gpt-image-1-mini` / `gpt-image-1.5` / `chatgpt-image-latest` → `gpt-image-2`）
- **12/2**: EU AI Act の生成コンテンツ標識義務、8/2 以前に市場投入済みシステムへの猶予終了
- **12/11**: OpenAI の旧スナップショット退役（`gpt-5-2025-08-07` / `o3-2025-04-16` / `o3-pro-2025-06-10` 等）
- **12/31**: Gemini 3.8 Flash と 3.7 Flash の導入価格が終了（$0.75/$3.75 → $1.50/$7.50。Copilot 経由分も同日終了）／ **GitHub Copilot の Fable 5.1 / Fable 5 に対する ZDR 暫定免除が終了** ／ MAI-Transcribe-2 の導入価格 $0.10/時が終了
- **年内**: Anthropic の新データ保持方式（顧客自身のクラウドでの30日保持）投入予定 ／ OpenAI の Jalapeño チップの初期展開
- **2027-01-06**: OpenAI で大半のユーザーの新規ファインチューニングジョブ作成が終了
- **2027-01-20**: OpenAI の audio / realtime 系退役（`gpt-realtime` / `gpt-audio` / `gpt-4o-audio` と mini 系）
- **2027-02-05 以降 / 02-17 以降**: `claude-opus-4-6` / `claude-sonnet-4-6` の暫定退役日（確定日ではない）
- **2027-02-26**: OpenAI の文字起こし4モデル退役（`whisper-1` / `gpt-4o-transcribe` / `gpt-4o-mini-transcribe` / `gpt-4o-transcribe-diarize`）
- **2027-03-01 / 2028-10-01**: SharePoint クラシックページ退役のフェーズ1 / フェーズ2
- **2027-04-16 / 05-28 / 06-09 / 06-30 / 07-24 / 09-01 以降**: `claude-opus-4-7` / `claude-opus-4-8` / `claude-fable-5` / `claude-sonnet-5` / `claude-opus-5` / `claude-fable-5-1` の暫定退役日（確定日ではない）
- **2027-06-30**: Claude for Teachers の学区登録期限
- **2027年末**: Anthropic が借りる Nscale West Virginia データセンター（460MW）の稼働開始見込み
- **2028-06**: 米国 K-12 教職員向け ChatGPT for Teachers の無料提供期限

## 改善メモ

- 3ソースの当日分（01 Master / 02 Copilot / 03 industry）はいずれも取得できた。前日 09-04 分にも欠損記録はなく、欠損リカバリの対象はない
- ⚠️ **Gemini 3.8 Flash の GA 検知が 01 と 03 で割れた** — 03 は `ai.google.dev/gemini-api/docs/changelog` を出典に「Google が 9/2 に GA へ移した」と書くのに対し、01 は「Google 単体の発表ではなく Copilot 側の changelog でしか確認できていない」と書く。本サマリー 09-03 は既に 03 側の情報で GA を収録済みで、**01 の記述が誤りである**。同じ `ai.google.dev` を両者が到達可としながら結論が割れており、changelog の読み取り範囲の差と見られる
- ⚠️ **Claude Code 2.1.259 の差し戻しを 01 が拾っていない** — 03 は「Bash の `Read()` 拒否ルールをオプション値のファイルにも適用する」変更が 2.1.260 で撤回されたと明記するが、01 の 2.1.260 項に差し戻しの記載はない。本サマリー 09-04 はこれを統制の強化として記録しているため、本日訂正した
- ⚠️ **`openai.com` の到達性が 01 と 03 で逆になっている** — 01 は `openai.com/index/path-to-astra/` を「オリジン403のため未読」と記録する一方、03 は `openai.com/index/gpt-6-astra/` を出典欄に挙げている。09-03 に記録した同ホストの到達性矛盾の再発で、3日ぶり2度目である
- **01 の 09-04 セッションの取りこぼしは本サマリーに影響していない** — 01 は「9/3 の3エントリのうち signups 再開の1本しか拾えず、Copilot 4モデル廃止と Gemini 3.8 Flash を1日遅れで検出した」と自己記録するが、本サマリー 09-04 は 03 の収録分でこの2件をハイライト1に載せている。**ソース間で補完が効いた形**である
- 同様に 03 も「09-04 収録では Claude Platform が 9/1 付から動いていないとしたが、9/3 付の `ant apply` を取りこぼしていた」と自己記録している。本日は 01・03 の両方が同項目を収録した
- **Cowork 組み込みブラウザは 8/26 公開分の9日遅れ検出である** — 01 は同日公開の `claude-in-chrome-generally-available` が 08-27 のダイジェストに載っている点を挙げ、「同一日の2件目以降が落ちる形」が `claude.com/blog` で9日間放置された事例として B-060 を起票した
- **新規の改善提案は4件** — B-059（01: `deploymentsafety.openai.com` を OpenAI の system card 一次として登録）、B-060（01: `claude.com/blog` の取得プロンプトを日付フィルタ付きから全 href 列挙へ固定）、B-058（02: 非推奨一覧 `important-changes-coming` の確認頻度を週次から毎日へ引き上げ）、B-031（03: リリースノート系ソースを「最新版だけ」でなく前回確認日以降の全エントリで差分判定する）
  - ⚠️ B-058 の番号は 01 の台帳では別提案（OpenAI Blog / News 項の検索キーワード拡張・09-04 起票）に割り当てられている。**台帳はリポジトリごとに独立しているため、番号だけでは提案を特定できない**
- ⚠️ **継続提案の計数が引き続き安定しない** — 本日は 01 が17件（最多 B-013・38回目）、02 が46件（最多 B-011・47回目）、03 が13件（最多 B-004・68回目）で計 **76件**。前日は 01: 38件 / 02: 23件 / 03: 12件の計64件で、01 が −21、02 が +23 と両方向に大きく振れている。09-02 以降4日連続で記録している計数基準の不安定は解消していない
- **到達性の変化** — 01 が `deploymentsafety.openai.com` の到達（200）を本日はじめて確認し、GPT-6 Astra の system card を一次で読めるようになった。一方で `cli.devin.ai` と `azure.microsoft.com` を新規のゲートウェイ拒否として記録している。02 では Microsoft Copilot Blog の RSS（`copilot-studio/feed/`）が 403 から 200 に復旧したが、⚠️ `lastBuildDate` は 2026-07-21T23:56Z・全10エントリで、HTML 一覧に出る 9/2 記事を含まない。03 は `microsoft.ai` を新規のゲートウェイ拒否として追加した
- ⚠️ **長期化している一次未読・接続障害**: Anthropic の8月 Risk Report が20日連続で一次未読（01）、`mc.merill.net` の拒否が29日連続（02）、Copilot Studio What's New への GA 未反映が33日連続（02）、Released Versions の空白が67日（02）、Copilot Tuning 一次の未更新が16日（02）、`aka.ms` の拒否が26日（02）、`www.ppweekly.com`（02）、`learn.chatgpt.com` / xAI 一次3ホスト（01）、Google 系5ソースの拒否（01）、`www.businessinsider.jp`（03）。いずれも解消の見込みが立っていない
- **本サマリーの生成環境について（3日連続）** — 本日の実行でも GitHub MCP のリポジトリスコープが `kit1132/05_ai-news-daily` のみに設定されており、入力3リポを MCP 経由で読めなかった。公開リポの `raw.githubusercontent.com` から読み取り専用で取得して生成した（入力3リポへの書き込みは行っていない）。⚠️ **3日連続で同じ回避を要している**ため、取得経路を raw に固定するか実行環境のスコープへ入力3リポを追加するかを決める必要がある
- **未解決の要 kit 対応（08-07 確定・継続）**: 08-06 追加の許可ドメイン13件は新規起動セッションでも全件未到達。① 保存先環境とスケジュールタスク実行環境の同一性確認 ② `.google` TLD 3件の個別指定確認 ③ 次回追加対象に `api-docs.deepseek.com` / `www.deepseek.com` ほかを含める
