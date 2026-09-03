# AI News Daily Summary — 2026-09-04

9月3日は、期限が1本増え、前日の判定が1本覆った日である。GitHub は Claude Opus 4.7 と Gemini 3.5 / 3.6 Flash、Kimi K2.7 Code を 10/2 に Copilot 全面から廃止すると告知し、モデル名を設定に書いた組織に28日の猶予が付いた。同じ日に Gemini 3.8 Flash が Copilot で開放されたが、既定の向きは前日の Fable 5.1 と逆で、モデルごとに棚卸しの前提が違う。Anthropic は Enterprise Frontier Safeguards を公表し、ゼロデータ保持の意味を「Anthropic に残らない」から「顧客のクラウドに残り検出ロジックが読む」へ動かした。Power Platform 側では、前日「404 で消滅した」と判定した Release Wave の製品別ページがリネームだったと判明し、GA 判定の経路は生きていることが確認された。統制面では国防総省が Anthropic の supply-chain risk 指定の有効を再表明し、前日の商務長官発言による読みが1日で覆っている。

## 今日のハイライト

### 1. Copilot が4モデルを 10/2 に廃止する — モデル名を固定した設定は28日以内に書き換えが要る

**要点**: GitHub が Claude Opus 4.7・Gemini 3.5 Flash・Gemini 3.6 Flash・Kimi K2.7 Code の廃止を 9/3 に告知した。`managed.json` にモデル名を書いた組織は、期日を過ぎると新規会話の既定が壊れる。

**詳細**: 影響範囲は「all GitHub Copilot experiences」で、Copilot Chat・inline edits・ask モード・agent モード・コード補完のすべてを含む。一次告知は移行先を4組で明示している。

- Gemini 3.5 Flash / Gemini 3.6 Flash → Gemini 3.8 Flash
- Kimi K2.7 Code → Kimi K3
- Claude Opus 4.7 → Claude Opus 5

⚠️ 一次告知は「Copilot Enterprise / Business の管理者は、移行先モデルへのアクセスをモデルポリシーで有効化する必要があるかもしれない」と書いており、**移行先が自動で使えるとは限らない**。前日収録の「管理者が `managed.json` の `model` キーで新規会話の既定モデルを指定できる」機能と組み合わせると、廃止対象を既定に指定した組織は期日までの書き換えが必須になる。

同じ 9/3 に **Gemini 3.8 Flash** が Copilot で提供開始された。対象は Copilot Pro / Pro+ / Max / Business / Enterprise で、VS Code・Visual Studio・Copilot CLI・GitHub Copilot cloud agent・Copilot アプリ・JetBrains・Xcode・Eclipse から選べる。課金は 12/31 まで introductory provider pricing の従量である。⚠️ 管理者既定の向きが前日の Fable 5.1 と逆で、Gemini 3.8 Flash は「管理者がグローバル既定を切っているか明示的に無効化していない限り自動で有効」になる。**モデルごとに既定の向きが違う**前提で棚卸しする必要がある。

- https://github.blog/changelog/2026-09-03-upcoming-deprecation-of-selected-github-copilot-models
- https://github.blog/changelog/2026-09-03-gemini-3-8-flash-is-now-available-in-github-copilot

### 2. Anthropic が Enterprise Frontier Safeguards を出した — ZDR が「残らない」から「顧客のクラウドに残り読まれる」へ変わる

**要点**: 監視用の活動ログを顧客所有の S3 / Azure Blob / GCS に顧客の鍵で置く方式が示された。ZDR は「Anthropic に一切渡らない」状態ではなくなり、ZDR 前提の社内審査と 12/31 の Copilot 免除期限の扱いが引き直しになる。

**詳細**: EFS はゼロデータ保持の秘匿性と不正利用検知を両立させる仕組みで、アクティビティログを顧客所有クラウドに顧客の暗号鍵・アクセスポリシー・監査ログの下で保管し、Anthropic は検出ロジックだけをそこに対して動かす。人によるコンテンツ閲覧は行わないと説明されているが、検出のために Anthropic 側が読む余地は残るため、一般的な ZDR の語感とは一致しない。

- 検知対象は2種類に絞られる: 攻撃的なサイバー能力または生物学的能力の構築の試みと、盗まれた／漏洩した認証情報の兆候。自動処理がトラフィックのローリングウィンドウを解析する形をとる
- 設計は金融・医療・製造・通信・法務・小売・公共の**100社超**と、AWS / Google Cloud / Microsoft Azure との協業による
- 費用は顧客持ちで、ストレージ・読み書き・データ egress は顧客のクラウド事業者から請求される。機能自体は任意で、モデルの挙動と単価は変わらない
- 提供は**今秋から段階的**で、それまでの間、適格顧客は Fable 5 / Fable 5.1 で ZDR を受けられる

⚠️ この暫定措置は GitHub Copilot 側の期限とつながっている。Copilot は 9/1 の Fable 5.1 GA 告知で「適格 enterprise の ZDR 暫定免除は暦年末まで、以後は EFS が必要」と明記しており、**12/31 の期限は EFS の展開時期に依存する**。⚠️ 一次（`anthropic.com/news`）は3ソースともゲートウェイ拒否で未読で、発表日も 9/1 と 9/2 でソース間が割れている（改善メモ参照）。

- https://www.anthropic.com/news/enterprise-frontier-safeguards （一次・未読）
- https://www.csoonline.com/article/4217538/anthropic-introduces-zero-retention-ai-safety-monitoring-for-enterprises.html
- https://www.helpnetsecurity.com/2026/09/02/anthropic-enterprise-frontier-safeguards/
- https://github.blog/changelog/2026-09-01-claude-fable-5-1-generally-available-in-github-copilot

### 3. Release Wave の製品別ページは消えていなかった — 404 の正体はリネームで、GA 判定の経路は生きている

**要点**: 前日「4本が 404 で消滅し GA 検知の主経路が失われた」とした本サマリーの判定は誤りだった。GA 判定を Roadmap の `status` へ緊急に移す必要はなく、期限は 11/15 の Release Planner 退役に戻る。

**詳細**: `power-platform/release-plan/2026wave1/` の索引ページ（HTTP 200）を読むと、各製品へのリンクから `microsoft-` 接頭辞が4本で外れていた。新パスは `planned-features` まで含めて5本とも 200 で取得でき、5ページとも `updated_at` **2026-09-03T14:35:00Z**・`git_commit_id` `06b3b6ba` で、8/28 から7日据え置かれていた `b92ae441` からの再ビルドが 9/3 に入っている。

- リネームの対応: `microsoft-power-automate` → `power-automate`、`microsoft-power-apps` → `power-apps`、`microsoft-power-pages` → `power-pages`、`microsoft-dataverse` → `data-platform`。`power-platform-governance-administration` だけは元からこの形で、前日1本だけ 200 だった理由もこれで説明がつく
- ⚠️ 旧パスは 301 も 308 も返さず親ごと 404 になる。転送先が示されないため、リダイレクト追跡でも WebSearch でも新パスには辿り着けず、**索引ページのリンクを読むまで判別できない**

再ビルド後の表で、8月期日の決着も確定した。緑チェックが付いたのは GitHub によるソースコード統合の1件だけで、Public preview 期日が「Aug 2026」から Aug 31, 2026 の確定日付に変わっている。8/31 に「8月期日8件に緑チェックがゼロ」と記録したのは、当時の表が再ビルド前だったためである。

- 未達で9月へ持ち越すのは7件で、Power Automate 4件・Power Apps 1件・ガバナンス2件の内訳になる
- ⚠️ PPAC の Usage ページ（GA 期日 Aug 2026）は達成でも未達でもなく、行そのものが表から削除された。Roadmap 側にも対応項目がなく、この機能の GA 状態を追う一次が無くなった
- ⚠️ 期日が後ろへ書き換わった行がある。「統合 Power Apps によるフォーム」の GA 期日は Jul 2026 → Sep 2026 で、9/3 まで「期日超過」と数えていたが超過ではなく延期だった
- ガバナンス表は 12行 → 17行に増え、評価機能6行（Evaluation for AI node・Safety grader・Latency Evaluation Checks・Evaluation viewer role・Overall score・Multi-grader comparison）が新規に載った。Latency Evaluation Checks と Evaluation viewer role は既に緑チェック済みである

- https://learn.microsoft.com/en-us/power-platform/release-plan/2026wave1/
- https://learn.microsoft.com/en-us/power-platform/release-plan/2026wave1/power-automate/planned-features
- https://learn.microsoft.com/en-us/power-platform/release-plan/2026wave1/power-platform-governance-administration/planned-features

## カテゴリ別まとめ

### Anthropic / Claude

- Anthropic が **Enterprise Frontier Safeguards** を公表した（9/1〜9/2・ハイライト2参照）
- Anthropic が Claude Code `2.1.259` をリリースした（9/2 21:21 UTC）。統制面の追加が2件あり、組織が全ユーザーへ HTTP / SSE の MCP サーバーを配れる `managedMcpServers` 設定と、ヘッドレス・無人ホスト向けに権限プロンプトを自動拒否する `--permission-prompts none` が入った
  - `allowedMcpServers` の意味が変わり、ユーザーが自分で追加したサーバーだけを統制する設定になった。組織配布分は別枠として扱われる
  - リモート・スケジュール実行に効く修正が3件入った: コネクタツールの権限承認をセッション一時停止中に通しても何も起きない不具合、ブラウザ側の MCP サーバーページが消えた後にリモートセッションの起動が60秒かかる問題、`--resume` がペイロードの無い添付エントリで失敗する問題
  - 権限まわりでは、Bash の `Read()` 拒否ルールがオプション値・git オペランド・複合コマンド内のファイルを覆うようになり、`Read` / `Edit` 拒否が `< file` リダイレクトにも掛かるようになった
  - そのほか、管理設定ファイルがパースできないと黙って未適用になる不具合、Stop がバックグラウンドのエージェントとワークフローを止めていない不具合、複数セッションが `~/.claude.json` を互いに巻き戻す不具合、frontmatter の `model:` が無視される不具合を修正した
  - ⚠️ 03 は「スケジュール実行環境は 2.1.258 に続き2版連続で修正対象になっている」と記録している
- ⚠️ npm の `stable` タグは `2.1.236` のまま据え置かれており、`latest` / `next` が 2.1.259 で合流したことで差が **23版**に開いた。8/28 の 2.1.251 に入った symlink 経由の権限境界修正群は、stable 固定の組織へ7日経っても届いていない
- Claude Platform API と `support.claude.com` の Release Notes はいずれも 9/1 の Fable 5.1 / Mythos 5.1 が最上位のままで、9/2・9/3 の追加はない。モデル退役ページにも新規告知はなく、Active は11件で据え置きである
- `claude.com/blog` の最新は 9/2 の commerce agents 2本で、9/3 の新規はない
- 既報: 週次上限50%増の 9/13 終了と 9/14 からの恒久 +25%（現行比17%減・一次は X 投稿のまま）、Fable 5.1 / Mythos 5.1 の GA（9/1）、Claudeforce（オープンベータは9月中）、Claude for Teachers、ウェルビーイング研究助成 $5M（締切 9/21）

### GitHub Copilot / 開発ツール

- GitHub が Copilot Business / Enterprise の新規申し込みを再開する（9/3）。クレジットカード・PayPal 決済の顧客が対象で、段階的に開放される
  - 再開後はシート割り当てごとに前払いが必要になり、支払い完了までユーザーは Copilot にアクセスできない。使用量が含有枠を超えた場合は追加の支払いが要る
  - 価格設定・日割り計算・超過分の追加購入は変更がなく、既存顧客への請求変更適用は **10/1** で据え置きである
  - ⚠️ 開放期間と停止理由の書きぶりが 01 と 03 で割れている（改善メモ参照）
- コンテンツ除外ポリシーが Copilot アプリと Copilot CLI で GA した（9/2・Business / Enterprise）。enterprise / organization / repository の各管理者が指定した除外ファイルは、エージェント型ワークフローを含め Copilot のコンテキスト生成に使われなくなる
- Copilot CLI に pre-release `v1.0.83-4` が出た（9/3 16:55 UTC）。MCP の OAuth サインインで CIMD（Client ID Metadata Document）に対応し、既定でセッション復元プロンプトなしに起動するようになった。修正はサンドボックス下のファイルツールが開発者ツールパスを読む件、タイムアウトしたシェルコマンドの停止、オートパイロット実行中に入力したプロンプトが消える件である
- ⚠️ Copilot CLI の安定版は `v1.0.82`（8/29）のままで、8/30〜9/3 の安定版リリースはない
- 既報: 管理者が新規会話の既定モデルを指定できる機能の GA（9/2・`managed.json` の `model` キー・`team-mappings.json` でチーム別に差し替え）

### Microsoft 365 Copilot / Copilot Studio / Power Platform

- Microsoft が Copilot Studio のエージェント作成をアプリ起点に作り替える（Roadmap **569474**・`In development`・GA 2026年10月・Worldwide / Web・9/2 22:56Z 起票）。これまでの「エージェントを作ってから知識とツールを足す」順序から、対象アプリの選択を起点に必要な機能を構成する順序へ変わり、ツールと知識がより統合された体験にまとめられる。研修教材と社内手順書の作成フローは10月に書き直しが要る
- 同じバッチで **570433**（MCP Apps・Preview 2026年10月 / GA 2026年11月）が起票された。UI 対応ツールを持つ MCP サーバーに対し、ソート可能なテーブルやドリルダウンを会話内に直接描画する。UI を描画できない配置面にはプレーンテキストのフォールバックが返り、メーカー側の作業は準拠 MCP サーバーを接続するだけとされる。M365 Copilot の宣言型エージェントが 2026年3月から持つ OpenAI Apps SDK 経由の UI ウィジェットと同じ層を、Copilot Studio 側が持つ形になる
- 同バッチには Teams 2件も含まれる: **570468**（GA 11月）は会議の開催者に、自組織のポリシーで許可された自動録画・文字起こしの選択肢だけを表示し、文字起こしなしで録画だけを自動開始する `Record only` を追加する。**570467**（GA 10月）は管理者が、ライブ文字起こしと保存済み文字起こしの不適切語マスクを会議ポリシーで制御できるようにする
- Copilot Studio 製品チームが月次まとめ記事「New and improved: GitHub Copilot harness, agent skills, and richer context」を 9/2 付で公開した。6月〜7月の更新の総括で、ハーネスを「AI モデルとエージェントの間に位置し、いつモデルを呼ぶか・どの文脈を渡すか・どのツールや MCP サーバーや接続エージェントを使うかを決める層」と定義する
  - ⚠️ 記事は GitHub Copilot ハーネスを Generally Available と明記しており、Learn の What's New が June 節で `(Production-ready preview)` と書いたままなのと食い違う
  - ⚠️ 02 は前日この記事を検知できていない。登録 RSS が 403 を返し WebSearch フォールバックでも索引に出なかったためで、本日は HTML 一覧ページの WebFetch で検知した（B-057 起票）
- Microsoft が Power Platform Community Conference 2026 の告知記事を 9/3 付で公開した。会期は **10/27〜29**・ラスベガス MGM Grand で、基調講演は 10/27 に Charles Lamanna 氏が務める。200超のセッションと24のハンズオンワークショップ、認定試験が用意され、NFL が Copilot Studio と Power Platform で試合当日の運用を刷新した事例が取り上げられる
- ⚠️ 定点の停滞が続いている: Copilot Studio の What's New は July 2026 節が最新のままで June 節のハーネス表記が **32日連続**で `(Production-ready preview)`、Released Versions は 2026.6.3 のままで空白が **66日**（次の定例日は 9/8）、Copilot Tuning の一次は停止発効から15日更新がない
- Copilot Studio のモデル可用性表に **Fable 5.1 の行は本日も無い**（`updated_at` は 2026-08-03T14:59Z から不動）。GPT-4.1 が既定、Claude Sonnet 5 が GitHub Copilot ハーネス限定、GPT-4o と Claude Sonnet 4.5 が `Retired` のままで、米国政府クラウドの表は GPT-4o の1行だけである
- M365 Copilot の Release Notes は August 25, 2026 バッチが最新のままで、拡張機能 What's New も July 2026 節から動いていない。M365 Roadmap の総項目数は 1,782 で、Latest announcements の先頭は 7/24 のままである
- Purview / Cowork / ガイダンスハブはいずれも `updated_at` が 8/28 から動いていない。8/23 に Roadmap で検知した 569612（Copilot メモリの Purview 保持・GA 2026年9月）は Purview 側に未掲載のままである
- Partner Center の9月ページに 9/3 付で「Join Partnering for Success Together」が追加された（掲載2件 → 3件）。9/9 開始の月次パートナースキリングセッションの案内で、⚠️ Copilot 固有のライセンス変更ではない

### OpenAI / Codex / ChatGPT

- OpenAI が `gpt-5.6-cyber` の単価を一次料金ページで公開した。入力 **$12.50**／キャッシュ入力 $1.25／キャッシュ書込 $15.625／出力 **$75.00**（100万トークンあたり・長文脈の単価は掲載なし）で、08-29 に「二次のみのため提案には引かない」と保留した数値が確定した。キャッシュ書込 $15.625 は二次に出ていなかった値である
  - 同節には `gpt-5.5-cyber`（入力 $12.50／出力 $75.00）と `gpt-5.4-cyber`（単価欄すべて空）が並び、`gpt-daybreak-blue-latest` / `gpt-daybreak-red-latest` がそれぞれ Sol 系・Cyber 系のエイリアスと記載される
  - ⚠️ 単価が公開されていることと買えることは別である。Cyber 系への到達経路は Daybreak Red のみで、9/1 から Daybreak Blue / Red の全個人アカウントにハードウェアセキュリティキーが必須になっている
  - ⚠️ 前日の「最上位のサイバー能力は API 調達の対象から外れた」という整理はベンダーで分かれる。OpenAI は単価を公開したうえで審査経路に閉じ、Google の Gemini 3.8 Flash Cyber は Fairwind Program 限定で単価の公表自体がない。審査枠へ移った点は共通だが、価格の可視性は逆方向である
  - https://developers.openai.com/api/docs/pricing
- GPT-5.6 の Sol / Terra / Luna 全ティアの単価は11日連続で据え置かれている。Sol は入力 $4／出力 $20、Terra $2／$12、Luna $0.20／$1.20 で、Batch / Flex は50%引き、Sol の期間限定価格は「少なくとも 11/21 まで」の記載が続く
- OpenAI が Codex CLI の安定版 `0.153.0` を出した（9/3 01:37 UTC）。Vim モードの undo（`u`）/ redo（`Ctrl+R`）に対応し、プラグイン CLI がリモートマーケットプレイスからのリスト・インストール・削除を扱えるようになった。TUI 履歴が完全なパッチと個別の完了コマンドを表示し、Guardian のレビュー履歴が圧縮・再起動後も保持され、MCP の承認はアプリアカウント単位にスコープされる
- Codex CLI に pre-release 3版が出た（`0.153.0-alpha.5.1` / `0.154.0-alpha.1` / 既出の `0.153.0-alpha.6`）。⚠️ いずれも本文が展開されず内容は未確定である
- OpenAI が ChatGPT Health を Epic の電子カルテに接続した（9/1）。Epic を使う医療機関が患者記録を ChatGPT for Healthcare に持ち込めるようになり、Epic から認可された患者コンテキストを会話へ取り込む形と、Epic の画面内に ChatGPT を埋め込む形の2つが用意される。⚠️ アクセスは読み取り専用でカルテへ書き戻せない。Epic は米国の病院の約4割で臨床業務を動かし3億2,500万人超の患者データを保持する。4,300件超の評価で 99.1% が臨床環境で安全と判定されたとされ、UCSF Health が初期パイロット先に入る
- ChatGPT の Gmail / Google カレンダー / Google 連絡先の各プラグインが複数アカウント接続に対応したとされる。個人と業務のアカウントを同じ会話に持ち込み、複数カレンダーの横断確認や複数受信箱の横断検索ができる。⚠️ 一次未読で公開日も確定できていない
- `developers.openai.com/api/docs/changelog` は 9/2 の API エラーコード分離が最上位のままで、退役ページも 9件で変更がない。`community.openai.com` の Announcements RSS は 8/25 から10日間動きがない

### Google

- Google が Lyria 3.5 を public preview で提供開始した（9/3・`lyria-3.5-clip-preview` と `lyria-3.5-pro-preview`）。30秒クリップ・ループ向けと、フル長楽曲生成向けの2種である。⚠️ 音楽生成は 01・03 とも関心領域の除外対象にあたるため、定点の変化の記録として1行に留める
- Gemini API changelog の日付列は 9/3 → 9/2 → 9/1 → 8/27 → 8/26 → 8/13 で連続しており、9/2 の `gemini-3.8-flash` GA 以降、開発者向けのモデル追加はない
- 既報: 9/1 の agentic video understanding（3.7 Flash / 3.6 Flash / 3.5 Flash-Lite・長尺で最大88%のトークン削減）、旧 `gemini-omni-flash-preview` の 9/30 廃止、Gemini 3.5 Pro GA は未ローンチ継続
- ⚠️ 登録済み Google 系5ソースはゲートウェイ拒否が継続しており、`ai.google.dev` だけが到達できる Google 一次である

### セキュリティ / フロンティアモデルの統制

- Anthropic が 7/30 のサイバー評価インシデントへの追跡投稿を出したとされる（9/1）。セキュリティ変更・アラインメント研究・インフラ強化の内容で、二次は EFS と1本の流れとして報じている。⚠️ 一次未読である
- ⚠️ 二次報道が**ヒューマンフィードバック経路の分類器欠落**を併せて報じている。2025年5月〜2026年4月の11ヶ月、約5万人・約1.33億件のやり取りが生物兵器分類器を通らず、Sonnet 5 の遡及走査で1,197件を高リスク判定、非内部の62件と無作為30件を人手確認して明確な誤用は無かったとされる。8月 Risk Report が19日連続で一次未読のため、Risk Report との関係は確定できない
- 既報: OpenAI が Astra について Preparedness Framework の Critical サイバー閾値到達を公表したとされる件（9/1・ExploitBench 満点・未知の脆弱性2件の自律発見と連鎖・提供先は重要インフラ防護の責任を持つ個人と組織に限定）

### オープンウェイト / MCP / Cursor / xAI

- Qwen が `Qwen-Drive-1.0-4B` を公開している（作成 8/27 / 最終更新 9/2）。`Qwen3.5-4B` をベースにした自動運転向けの vision-language モデルで、apache-2.0・safetensors 4シャード（総パラメータ約45.4億）、tags は autonomous-driving / motion-planning / 3d-perception / visual-question-answering である
  - ⚠️ 01 は前日まで検出できていなかった。**非公開で作成して後日公開へ切り替えると `createdAt` が過去日のまま一覧に出現する**ため、「前回チェック日以降に作成されたもの」だけを見ると落ちる
- 追跡8 org のいずれにも 9/3 の新規公開はない。HF の `downloads` は追跡8リポジトリすべてで動いており、前日の「全件同値」（日次バッチ遅延の疑い）は再現しなかった。⚠️ `DeepSeek-V4-Flash-0731` と `Kimi-K3` は前日記録より減っているが、`downloads` は30日ローリングのため増減する
- WebMCP Challenge の提出締切は**本日 9/4**（賞金総額 $35,000・受賞発表は 9/23）。`blog.modelcontextprotocol.io` は 8/22 の The New MCP Roadmap が最上位のままで13日間新規がなく、⚠️ WebMCP は MCP 公式ブログ側に一切言及がない別系統として扱われている
- Cursor が self-hosted machines に対応した（9/2）。ツール実行を自社インフラ内に完全に留められるようになり、チームプールがワーカーのキューとして機能して需要に応じて拡張・縮小する。実行先は AWS Lambda / Coder / Cloudflare / Daytona / Modal などのサンドボックスで、自ホストワーカーは Linux と Mac でデスクトップ操作とブラウザ制御に対応する
- Cursor が Grok Bot の Android 版を公開した（9/2）。モバイルからボットにタスクを指示してデスクトップで続行でき、ロック中も稼働して承認が必要な時点でのみ通知する。Google Play から無料で入手でき、適格な Cursor / SuperGrok プランに含まれる
- Musk が Grok 4.7 の公開日を **9/12** と述べたとされる（9/2 の X 投稿）。パラメータ2.1兆（Grok 4.6 の1.5兆から40%増）で SpaceX のエンジニアリングデータを追加学習に取り込んだとされ、提供は 4.6 より遅い代わりにトークン効率が上がると説明される。⚠️ `docs.x.ai` のモデル一覧は grok-4.6 が上限のままで、モデル ID・価格・コンテキスト長のいずれも存在しない

### 企業動向 / 規制 / 市場データ

- 国防総省の研究工学担当次官 Emil Michael が、Anthropic を supply-chain risk と指定した決定は引き続き有効だと 9/3 に X で述べた。⚠️ 前日 9/2 の商務長官 Howard Lutnick の「we trust Anthropic」「back on the right side」発言への事実上の打ち消しにあたり、**前日サマリーが「数ヶ月の対立を経ての転換」として載せた読みは1日で覆った**。経緯は Anthropic が自律兵器と大規模監視への Claude 利用を防ぐ社内セーフガードの削除を拒んだことに端を発し、8/27 に連邦地裁が「国防総省は政府批判を理由に違法かつ根拠なく制裁した」と判断しているが、D.C. の訴訟は継続中で決着までは指定そのものが残る
- 米司法省が NYT 対 OpenAI の著作権訴訟で OpenAI / Microsoft 側に立つ statement of interest を提出したとされる（9/1・南部ニューヨーク地区連邦地裁）。著作物での LLM 学習は fair use にあたるとし、反対の判断は著作権法を歪め、イノベーションを抑え、米国の競争力と国家安全保障を弱めると主張した
  - 対象は OpenAI に対する複数地区統合訴訟（MDL）で、NYT の主張に直接答えつつ、書籍著者・出版社の関連訴訟にも同じ論理が及ぶとしている
  - ⚠️ statement of interest は拘束力を持たず、政府が当事者にならずに立場を示す手続きである。一次未読で、NYT は司法省の姿勢を強く批判しており、司法省が OpenAI への出資を交渉中である点との利益相反を指摘する報道もある
- Bloomberg が、Devin を提供する Cognition の調達交渉が約 $1B・評価額 **$47B** で最終段階にあると 9/2 に報じた。5月の調達時は $26B 評価で、08-12 収録の観測値 $40B から3週間で切り上がったことになる。年換算売上は5月下旬の $492M から $900M 超へ伸び、投資家の関心表明は $10B 近くに達したとされる。⚠️ 交渉は継続中で条件は変わりうるうえ、数値はいずれも関係者取材にもとづく二次情報である
- 市場データは国内・グローバルとも新規公表がない。IDC / IDC Japan・MM総研・Similarweb・NRC のいずれにも新しい調査発表はなく、参照可能な最新値は IDC の国内AI市場予測（2025年 2兆3,725億円 → 2029年 6兆8,897億円・CAGR 36.0%）と MM総研の個人利用経験率 21.8% で据え置きである
- 既報: GenAI.mil への ChatGPT Mil / Grok for Government 追加（9/1・Anthropic は非参加）、Anthropic の IPO 観測（10月・$2T 超）、Anthropic × Nscale 約 $45B・6年、SpaceX による Cursor 買収完了（8/14・$60B）

### Apple / クラウド

- `developer.apple.com` は 9/1 の Rosetta サポート変更告知が最上位のままで、9/2・9/3 の新規はない。macOS 27 が Rosetta を載せる最後のリリースになる
- ⚠️ AI 関連の最新は 6/11 の ImageCreator クラス廃止告知のままである
- 既報: 8/26 の特別イベント告知（**9/9 10:00 PT**）、Sign in with Apple の新ドメイン（`private.icloud.com`）、EU 向けビジネス条件変更（発効 2026-10-01）

## 直近の注目予定

- **9/4（本日）**: WebMCP Challenge の提出締切
- **9/6**: PnP コミュニティコール ／ Power CAT リリース（週次）
- **9/7**: 週次復旧チェック（月曜）／ ppweekly・MS-4005 コレクション・課金レート表の週次確認
- **9/8**: M365 Copilot Release Notes の次バッチ見込み ／ Copilot Studio Released Versions の定例更新日
- **9/9**: Apple 特別イベント（10:00 PT）／ GLM-5.3-Flash の Z.ai 経由50%割引が終了 ／ Microsoft の月次パートナースキリングセッション開始
- **9/10**: MAI-Code-1-Flash が全 Copilot 体験から廃止
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
- **9 月**: iOS 27 / macOS 27 GA ／ Claudeforce のオープンベータ ／ Copilot Studio の Roadmap 項目が GA（570434 ツール呼び出しの人間承認ほか）／ Copilot Tuning の Public Preview 再開 ／ Release Plans on Learn の新規掲載停止 ／ App Store の Social Media 年齢レーティング回答が必須化 ／ OpenAI の IPO 観測
- **10/1**: Copilot Business・Enterprise の既存顧客が前払い必須に ／ Apple の EU 向け新ビジネス条件が発効 ／ Ask Gemini in Chat のプロモーション上限が終了
- **10/2**: **Copilot から Claude Opus 4.7 / Gemini 3.5 Flash / Gemini 3.6 Flash / Kimi K2.7 Code が廃止**（残り28日）
- **10/5**: Anthropic ウェルビーイング研究助成の full proposal 提出期限（採択者）
- **10/15 以降**: `claude-haiku-4-5-20251001` の暫定退役日（確定日ではない）
- **10/16–11/11**: OpenAI DevDay Exchange 8都市（東京は 10/20）
- **10/23**: OpenAI のレガシースナップショット退役（`gpt-3.5-turbo-0125` / `gpt-4-0613` / `o1-2024-12-17` / `o4-mini-2025-04-16` とファインチューン版）
- **10/27〜29**: Power Platform Community Conference 2026（ラスベガス MGM Grand）
- **10/31**: OpenAI の既存 evals が読み取り専用になる
- **10 月**: Copilot Studio 569474（app-first なエージェント作成）GA ／ 570433 MCP Apps の Preview ／ 569475 エージェント共有 GA ／ 570467 文字起こしフィルター制御 GA ／ Anthropic の IPO 予定（$2T 超の評価額を目標と報道）／ 韓国 App Store のコンテンツ記述子2件が All → 12+
- **秋**: Anthropic の Enterprise Frontier Safeguards が段階的に提供開始（二次情報）
- **11 月**: 570433 MCP Apps の GA ／ 570468 録画・文字起こしポリシー整合の GA
- **11/15**: Release Planner 退役
- **11/21**: GPT-5.6 Sol の暫定値下げが有効とされる期限
- **11/24 以降**: `claude-opus-4-5-20251101` の暫定退役日（確定日ではない）
- **11/30**: OpenAI の Reusable prompts・Evals プラットフォーム・Agent Builder が停止
- **12/1**: OpenAI の GPT Image 系が停止（`gpt-image-1-mini` / `gpt-image-1.5` / `chatgpt-image-latest` → `gpt-image-2`）
- **12/2**: EU AI Act の生成コンテンツ標識義務、8/2 以前に市場投入済みシステムへの猶予終了
- **12/11**: OpenAI の旧スナップショット退役（`gpt-5-2025-08-07` / `o3-2025-04-16` / `o3-pro-2025-06-10` 等）
- **12/31**: Gemini 3.8 Flash と 3.7 Flash の導入価格が終了（$0.75/$3.75 → $1.50/$7.50）／ Copilot の Gemini 3.8 Flash の introductory provider pricing が終了 ／ **GitHub Copilot の Fable 5.1 / Fable 5 に対する ZDR 暫定免除が終了**
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

- 3ソースの当日分（01 Master / 02 Copilot / 03 industry）はいずれも取得できた。前日 09-03 分にも欠損記録はなく、欠損リカバリの対象はない
- **本サマリー 09-03 のハイライト3を本日訂正した** — 「Release Wave の製品別ページ4本が 404 で消えた — GA 判定の主経路が 11/15 を待たず失われた」は誤りで、実体は `microsoft-` 接頭辞が外れたリネームだった。02 は同じ判定に基づく B-055 の根拠も訂正し、新パスへの差し替えを B-056 として起票している。⚠️ 旧パスが 301 / 308 を返さない以上、**404 を見た時点で同一サブツリーの索引を読む**手順が無ければ当日には判別できない
- ⚠️ **EFS の発表日が 01 と 03 で割れた** — 01 は 9/1、03 は 9/2 と書く。両者とも一次 `anthropic.com/news/enterprise-frontier-safeguards` に到達できておらず、同じ URL を出典欄に挙げている。二次（helpnetsecurity / marktechpost）はいずれも 9/2 付である。本サマリーは日付を断定せず「9/1〜9/2」と記した
- ⚠️ **Copilot 申込再開の記述が 01 と 03 で割れた** — 段階開放の期間は 01 が「今後数週間」、03 が「今後2週間ほど」。停止理由は 01 が「理由そのものは明記されておらず、記事は『可用性と信頼性の改善のため』とだけ述べている」とするのに対し、03 は「停止中にアカウント審査と請求まわりを強化したとしている」と書く。本サマリーは期間を断定せず「段階的に」とし、理由には触れなかった
- ⚠️ **`www.csoonline.com` の到達性が 01 と 03 で逆になっている** — 01 は EFS の出典として同ホストの記事 URL を挙げ、03 は同ホストを新規のゲートウェイ拒否として台帳に追加した。09-03 に記録した `openai.com` の到達性矛盾と同型の再発である。01 は `www.securityweek.com` / `securityaffairs.com` / `www.theregister.com` を、03 は `www.csoonline.com` / `www.securityweek.com` を新規拒否として記録しており、**securityweek は両者で一致する**
- **`claude.com` による `www.anthropic.com` の迂回は news 系に効かないと確定した**（03 記録）— `claude.com/news/enterprise-frontier-safeguards` と `claude.com/blog/enterprise-frontier-safeguards` がともに 404 だった。09-03 のコマース blueprint は `claude.com/blog/` で取得できていたため、blog 系のみ有効という切り分けになる
- **新規の改善提案は4件** — B-058（01: OpenAI Blog / News 項の検索キーワードを1本から4本へ増やし、安全性・Preparedness 系の検出軸を加える）、B-056（02: Release Wave 系ソース URL を新パスへ差し替え）、B-057（02: Microsoft Copilot Blog の新着判定に HTML 一覧ページの WebFetch を毎日併用。登録 RSS が 403）、B-030（03: 定点の一次ページを読む際に節の全列挙を求める）
- ⚠️ B-058 の起票根拠（OpenAI Astra の Critical 到達を 01 が3日間検出できなかった）は、本サマリーでは影響が出ていない。**03 が先に収録しており、ソース間で補完されていた**
- ⚠️ **継続提案の計数が引き続き安定しない** — 本日は 01 が38件（最多 B-013・37回目）、02 が23件（最多 B-011・46回目）、03 が12件（最多 B-004・67回目）で計 **73件**。前日は 01: 24件 / 02: 28件 / 03: 12件の計64件で、01 が +14、02 が −5 と両方向に振れている。09-02 以降3日連続で記録している計数基準の不安定は解消していない
- ⚠️ **長期化している一次未読・接続障害**: Anthropic の8月 Risk Report が19日連続で一次未読（01）、`mc.merill.net` の拒否が28日連続（02）、Copilot Studio What's New への GA 未反映が32日連続（02）、Released Versions の空白が66日（02）、Copilot Tuning 一次の未更新が15日（02）、`www.ppweekly.com`（02）、`learn.chatgpt.com` / `docs.devin.ai` / xAI 一次3ホスト / `www.axios.com` の拒否（01）、Google 系5ソースの拒否（01）。いずれも解消の見込みが立っていない
- **本サマリーの生成環境について（2日連続）** — 本日の実行でも GitHub MCP のリポジトリスコープが `kit1132/05_ai-news-daily` のみに設定されており、入力3リポを MCP 経由で読めなかった。公開リポの `raw.githubusercontent.com` から読み取り専用で取得して生成した（入力3リポへの書き込みは行っていない）。⚠️ 2日連続で同じ回避を要しているため、取得経路を raw に固定するか実行環境のスコープへ入力3リポを追加するかを決める必要がある
- **未解決の要 kit 対応（08-07 確定・継続）**: 08-06 追加の許可ドメイン13件は新規起動セッションでも全件未到達。① 保存先環境とスケジュールタスク実行環境の同一性確認 ② `.google` TLD 3件の個別指定確認 ③ 次回追加対象に `api-docs.deepseek.com` / `www.deepseek.com` ほかを含める
