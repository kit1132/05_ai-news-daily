# AI News Daily Summary — 2026-09-01

9月の初日は、発効が6件重なり、そのうち1件は「上がらなかったこと」が確定した日である。本日発効したのは GitHub Copilot ハーネスの開発者環境・トライアル環境の従量課金化、Copilot の全体験でのモデル廃止、global model policy の全 enterprise 適用完了、Copilot Business / Enterprise の新規申込受付再開、OpenAI Daybreak のハードウェアキー必須化、MAICPP 更新条項の自動発効の6件で、予定されていた Sonnet 5 の $3/$15 への値上げだけが当日に撤回のまま維持された。前日サマリーが 9/1 に置いた「新規シートの前払い必須化」は一次の読み直しで 10/1 の既存顧客向けと判明したため、本サマリーで訂正する。セキュリティ側では Anthropic が、インフォスティーラーに窃取されたセッション Cookie による Claude アカウントの乗っ取りを公表した。移行計画には OpenAI の未追跡だった期限4件と、SharePoint クラシックページの2段階退役が新たに加わる。

## 今日のハイライト

### 1. インフォスティーラーが Claude のログインセッションを乗っ取った — 2FA を通過した後の状態ごと複製される

**要点**: 盗まれたのはパスワードではなくセッション Cookie で、攻撃者は2FA を一度も経ずに有料の利用枠を消費した。防御の前提が「2FA があれば足りる」から「端末が汚染された時点で認証済み状態ごと持ち去られる」へ変わった。

**詳細**: Anthropic は 2026-08-30 に対象ユーザーへの連絡を開始し、複数のセキュリティメディアが 8/31 に報じた。

- 経緯: 利用者の PC に感染したインフォスティーラーが、ブラウザに保存された**有効なセッション Cookie** を窃取した。攻撃者はその Cookie でアカウントへ入るため、パスワード入力も2要素認証も経ずに有料枠を消費できる
- Anthropic の対応3件: 影響を受けたセッションの強制サインアウトによる Cookie の無効化、保存済み支払い方法の削除、不正と判定した課金の返金
- 確認されたマルウェア: Windows 側が Vidar・LummaC2・StealC・RedLine・Acreed、Mac 側が Atomic Stealer（AMOS）。いずれも汎用のインフォスティーラーで、非正規のダウンロードや悪質なアプリに同梱されて入り、保存済みパスワード・Cookie・他アプリの資格情報をまとめて複製する
- 兆候: 使っていないのに**週次枠が減る**挙動がこれにあたる。影響ユーザー数は本日時点で公表されていない
- ⚠️ Claude 本体・インフラの侵害ではない。Anthropic はマルウェアが Claude 自体・その基盤・プラットフォーム上の利用者操作とは無関係であると明示している
- ⚠️ 強制サインアウトはマルウェアを除去しない。端末に残ったままなら次回ログインのセッションが同じ経路で盗まれるため、研究者は再ログイン前のフルスキャン、アカウントに紐づくメールのパスワード再設定と2要素認証の有効化、ブラウザ保存の資格情報の更新を推奨している
- ⚠️ 一次の `www.anthropic.com` はゲートウェイ拒否が継続し、`support.claude.com` の Release Notes にも本件の記載がない。日付・対応内容・マルウェア名は BleepingComputer / The Register / SecurityWeek / Help Net Security / Security Affairs の二次一致で採った

- https://www.bleepingcomputer.com/news/artificial-intelligence/anthropic-warns-infostealer-malware-is-hijacking-claude-sessions-to-drain-usage/
- https://www.theregister.com/security/2026/08/31/anthropic-cracks-down-on-hijacked-user-accounts-mining-ai-tokens/
- https://www.helpnetsecurity.com/2026/08/31/claude-accounts-compromised-through-infostealer/
- https://securityaffairs.com/198166/ai/infostealers-are-hijacking-claude-sessions-and-draining-subscriptions.html

### 2. GitHub Copilot ハーネスの開発者環境とトライアル環境が本日から従量課金に入った — 「作って試すだけなら無料」が終わった

**要点**: 開発者環境・トライアル環境のハーネスが本日 9/1 から Copilot Credits を消費する。前提が「公開したら課金」から「作り始めた瞬間から課金」へ変わり、PoC 用の Dev 環境をコスト見積りの外に置いていた組織は引き直しになる。

**詳細**: 一次は 8/28 付で新設された Learn ページ `power-platform/admin/manage-usage-github-copilot-harness`（`updated_at` 2026-08-29T01:04Z）で、末尾の「Prepare for the end of preview billing」節が「Developer environments and trial environments move to usage-based billing September 1, 2026」と本日を発効日として明記する。02 側が全 digest を grep したところ、本ページの掲載歴はゼロだった。

- ライセンスでカバーされる範囲が表で整理された
  - 標準ハーネスのエージェント: Microsoft 365 チャネル内では M365 Copilot ライセンスでカバーされ、無ライセンスユーザーまたは M365 外チャネルでのみ課金される
  - ワークフローとプロンプト: ライセンスユーザーが標準ハーネスのエージェント内で実行する場合のみカバーされ、それ以外は課金される
  - コンピューター使用（CUA）と GitHub Copilot ハーネスのエージェント: カバー対象外で全利用が課金される。後者は**作成時のアクティビティ**も実行時と同じく課金される
- 管理者向けの統制6経路も同ページに集約された: 環境への前払いクレジット割当、テナントプールからの引き当てオフ、エージェント単位の月次上限（通知＋`Stop usage`）、環境グループの `Cost controls` ルール、Power Platform API による一括割当、PAYG 環境の Azure 予算・アラート
- ⚠️ 環境への割当は境界にならない。テナント容量からの引き当てか PAYG 課金が生きていれば、割当を超えても消費は続く
- ⚠️ Azure の予算とアラートは通知するだけで Copilot Studio の消費を止めない。実際の停止点はエージェント単位の `Stop usage` だけである
- 可視化はいまのところ2経路にとどまる。PPAC のエージェントインベントリに `Harness` 列（`GitHub Copilot` / `Standard` / `Copilot Chat`）が入って課金対象を絞り込めるようになり、本日以前の消費は Manage Agents の `Non-billed Copilot Credits` とダウンロード可能な消費レポートで方向感だけ確認できる。Microsoft は後者を請求見積りでも将来コストの保証でもないと明記している
- ⚠️ Message Center 側の一次は読めていない。該当 MC の存在は検索索引で確認できるが `mc.merill.net` と `m365admin.handsontek.net` がともにゲートウェイ拒否のため、二次が伝える「8/3 より前に作成されたエージェント／ワークフローも 9/1 から対象」というスコープは一次未確認である。USD 単価も本日 Learn 側に存在しない（B-022 継続）

- https://learn.microsoft.com/en-us/power-platform/admin/manage-usage-github-copilot-harness
- https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-experience/billing-credit-overview
- https://learn.microsoft.com/en-us/microsoft-copilot-studio/harnesses-overview

### 3. OpenAI の退役ページに未追跡の不可逆な期限が4件あった — 登録ソースを回るだけでは期限が落ちていた

**要点**: 文字起こしモデル4種の 2027-02-26 停止（告知 8/26）を含む4件が、いずれも「注目スケジュール」から欠けていた。移行計画の前提が「登録ソースを回れば期限は追えている」から「退役ページを直に読まないと落ちる」へ変わる。

**詳細**: 01・03 の両ソースが `developers.openai.com/api/docs/deprecations` を WebFetch（200）で取得し、全件を過去の記録と突き合わせて確定した。未追跡だった期限は次の4件である。

- **2026-11-30**: Reusable prompts・Evals プラットフォーム・Agent Builder が停止する（告知 6/3。移行先はアプリケーションコード／Promptfoo／Agents SDK）
- **2026-12-01**: GPT Image 系が停止する（`gpt-image-1-mini`・`gpt-image-1.5`・`chatgpt-image-latest` → `gpt-image-2`。告知 6/2）
- **2027-01-06**: 大半のユーザーで新規ファインチューニングジョブの作成が終了する（告知 5/7）
- **2027-02-26**: 文字起こし4モデルが停止する（`whisper-1`・`gpt-4o-transcribe`・`gpt-4o-mini-transcribe`・`gpt-4o-transcribe-diarize` → `gpt-live-transcribe` または `gpt-transcribe`。告知 8/26）

⚠️ 2027-02-26 分は 2027-01-20 の audio / realtime 系退役とは別の告知である。`gpt-4o-mini-transcribe-2025-03-20` は 1/20 側、`gpt-4o-mini-transcribe` は 2/26 側に入っており、同名系列でも期限が分かれる。音声認識だけが約5週間あとに第2の期限を持つ構成にあたる。既存8件の期限は撤回・延期のいずれも無く、次の期限は 9/24（Videos API と Sora 2 系）で残り23日である。同ページは 01 の登録ソースに無いため B-055 として起票された。

- https://developers.openai.com/api/docs/deprecations

## カテゴリ別まとめ

### Anthropic / Claude

- インフォスティーラーによるセッション乗っ取りが起きた（ハイライト1参照）
- **Sonnet 5 の 9/1 値上げは実施されなかった** — 本日が当該日にあたるため一次の料金ドキュメントで確定させた。Sonnet 5 は入力 $2／出力 $10（100万トークン）のままで、ページ上の注記も「導入価格として告知した $2/$10 が現在の標準価格であり、2026年9月1日に予定していた $3/$15 への引き上げは実施しない」と明記している。8/10 のリリースノートによる撤回告知（08-18 収録）が当日まで維持された形である
  - ⚠️ 複数の価格比較アグリゲータは本日時点でも「9月1日に $3/$15 へ上がる」と記載したままで、当日になっても訂正されていない（08-24 に指摘した状態が是正されないまま期日を迎えた）。試算に二次の早見表を使っている場合は当該行を差し替える必要がある
  - https://platform.claude.com/docs/en/about-claude/pricing
- **Claude Code `2.1.252` の扱いが 01 と 03 で割れた** — 03 は一次 changelog で 8/31 付の新版として確認し、内容は不具合修正4件のみとしている。01 は同じ日に「npm に `2.1.252` が publish された（8/31 17:07 UTC）が changelog には載っていない」と記録し、`dist-tags` を `{stable: 2.1.236, latest: 2.1.251, next: 2.1.252}` と実測した。取得時刻が約1時間ずれており、その間に changelog へ反映された可能性が高い。本サマリーは新しい 03 側の内容を採り、差を改善メモに記録する
  - 修正4件: 一部の Mac で Bash コマンドが `task output swap refused` で失敗する問題、`.claude/settings.local.json` が未作成のプロジェクトで「常に許可」が保存されない問題、Claude Desktop / VS Code がホストする Remote Control セッションが接続劣化時にツール完了後も数分停止する問題、失敗出力が非常に大きい場合にバックグラウンドタスク通知が API リクエストのサイズ上限を超える問題
- ⚠️ **`stable` は `2.1.236` のまま15版差で据え置かれている**。8/28 の `2.1.251` に入った権限境界まわりの修正群（symlink 差し替えによる作業ディレクトリ外の読み書き、marketplace プラグインのディレクトリ外参照、Workflow の `scriptPath` 検証タイミング、symlink 経由の Grep / Glob での deny ルール無視）は stable 固定の組織へ届いておらず、未更新の環境では権限設定が想定どおり効かない
- **Claude Platform API のリリースノートは 8/27 が最上位のまま**で、8/28〜8/31 の追加がない。日付列は 8/27 → 8/26 → 8/20 → 8/19 → 8/18 と連続しており、隣接日付ブロックの丸ごと欠落（B-024）は起きていない。`support.claude.com` の Release Notes も 8/25 の memory 更新が最上位のまま7日間動いていない
- **モデル退役ページに新規告知はない**。直近告知は 2026-06-05 の Opus 4.1（8/5 退役済み）で、Active 全10モデルの暫定退役日も据え置きである。最も近いのは `claude-sonnet-4-5-20250929` の 9/29 以降で、⚠️ いずれも「not sooner than」であり確定日ではない
- **`claude.com/blog` は 8/28 の2本が最新のまま**で、8/29〜8/31 の追加がない。⚠️ 8月 Risk Report は16日連続で一次未読である（初出 08-17）
- **AWS Bedrock の Anthropic モデル追加は 7/24 の Claude Opus 5 が最新のまま**で、8月の新規提供開始は検出できなかった
- 既報: 週次上限50%増の 9/13 まで延長と 9/14 からの恒久 +25%（現行比では17%減）、Claudeforce（Salesforce × Anthropic・8/26・一次未読）、Model Hardware Standard 研究プレビュー（8/27・一次未読）、ウェルビーイング研究助成 $5M（応募締切 9/21）、連邦地裁による国防総省の指定違法判断（8/27）

### OpenAI / Codex / ChatGPT

- 退役予定4件を新たに確定した（ハイライト3参照）
- **OpenAI Daybreak のハードウェアキー必須が本日発効した** — Daybreak Blue / Red の全個人アカウントで FIDO 準拠の物理セキュリティキーが必須となり、攻撃側向けの Red だけでなく防御側向けの Blue も対象に入る。OpenAI は Yubico と組んで割引価格の YubiKey を提供するが、FIDO2 準拠であれば他社製でも受け付ける
  - ⚠️ 08-13 に挙げた宿題「Amazon Bedrock 経由の利用にも同要件が掛かるか」は本日も決着しなかった。AWS の一次告知（8/13 付）を全文確認したがハードウェアセキュリティキーへの言及は無く、記載は Daybreak Red 向けの「より強固な本人確認・監視・アクセス制御」と、登録には OpenAI か AWS の担当へ問い合わせる必要があるという一般的な記述にとどまる。Bedrock 経由（US East バージニア北部のみ・`bedrock-mantle` エンドポイント）の構成は、要件が掛かる前提で確認しておく必要がある
  - https://aws.amazon.com/about-aws/whats-new/2026/08/openai-daybreak-red-and-blue-on-amazon-bedrock/
- **OpenAI が mTLS と X.509 ワークロード ID フェデレーションを GA にした**（8/29）。証明書と ID プロバイダを Platform コンソールから直接管理でき、ロールベースのアクセス制御が掛かる。API キーを配らずに機械同士を認証する経路が公式に開いた形である
  - ⚠️ 前回チェック（08-31）は同 changelog の最上位を 8/21 と記録しており、8/26 の文字起こしモデル退役告知とあわせて2件を落としていた。降順ページからの取りこぼし（B-024）にあたる
- **GPT-5.6 の単価は8日連続で据え置かれている**。100万トークンあたり Sol は入力 $4・キャッシュ $0.40・キャッシュ書込 $5.00・出力 $20（長文脈側 $8／$0.80／$10／$30）、Terra は $2／$0.20／$2.50／$12（長文脈側 $4／$0.40／$5／$18）、Luna は $0.20／$0.02／$0.25／$1.20（長文脈側 $0.40／$0.04／$0.50／$1.80）である。Batch と Flex が標準の50%引き、Fast モードが倍額という構成も不変で、Sol の期間限定価格が「少なくとも 2026-11-21 まで」という記載も変わっていない
- **Codex CLI に pre-release が3版加わった**（`0.152.0-alpha.5` 8/31 01:11 / `alpha.6` 8/31 02:12 / `alpha.7` 8/31 16:18・いずれも UTC）。⚠️ 本文は `Release <タグ名>` の1行のみで変更内容は未確定である（B-039 と同型）。安定版は `0.151.0`（8/29）据え置き
  - ⚠️ 一覧の表示名は `0.152.0-alpha.7` だが実タグは `rust-v0.152.0-alpha.7` である。個別タグへ進むときは一覧の href を使うこと（B-041）
- **`community.openai.com` の Announcements RSS は 8/25 の WebMCP 2本が最上位のまま**で、8/26 以降の追加がない。WebMCP Challenge の提出締切は 9/4、受賞発表は 9/23 である
- 8/30 に公式 DALL·E GPT が ChatGPT から退役し、8/31 に GPT-5.4 / 5.4 mini が Codex（ChatGPT サインイン）から除外された。いずれも既報の期限どおりに発効している
- 到達性: `developers.openai.com`（changelog・deprecations・pricing とも）は 200。`openai.com` は `curl` で HTTP 403（オリジン403）を再確認した。`learn.chatgpt.com` はゲートウェイ拒否が継続し、`site:` 付き WebSearch でも9月分の新規エントリは返らなかった

### GitHub Copilot / 開発ツール

- ⚠️ **本日到来した Copilot の変更は「前払い化」ではなく新規申込の再開だった** — 03 が一次の告知本文を読み直して確定した。08-31 のサマリーと 01 の本日分は 9/1 を「新規シート前払い化」と記載しているが、これは誤りである。一次によれば 9/1 はクレジットカード／PayPal による Copilot Business / Enterprise の**新規申込受付を再開**する日で、あわせてアカウント審査が強化される。全アサイン済みシートを請求サイクル開始時に前払いする変更は 10/1 の既存顧客向けであり、対象も日付も別である
  - あわせて本日発効するのは、Copilot の全体験でのモデル廃止と global model policy の全 enterprise 適用完了の2件である
  - 9/28 以降のチャット3面統合・データ保持のアカウント存続期間への延長・コードレビュー既定の Lite → Balanced は変更なく残る
  - https://github.blog/changelog/2026-08-28-upcoming-changes-to-github-copilot-policies-and-billing/
- **GitHub Copilot の VS Code 8月分がまとめて公開された** — GitHub が 8/31 に、VS Code v1.132〜v1.135 の Copilot 関連変更を1エントリで告知した
  - エージェント運用: 複数チャットの左右並列配置とレイアウト復元、コンテキストとプロンプトキャッシュを共有する `/btw` の傍らの会話、特定時点と関連ファイル変更を辿るプロンプトタイムライン
  - 権限・サインイン: **GitHub サインイン無し**での Agents ウィンドウ起動が実験機能として入った（API キーを使用）。Anthropic 契約と Copilot 契約のモデルを切り替えられる
  - 移植性: Agent Plugins 1.0 準拠のポータブルなエージェントプラグインに対応し、他アプリのエージェントセッションを表示・継続できるようになった
  - 補助機能: チャット全文の正規表現検索、モデル種別ごとのトークン使用量表示、統合ブラウザでの HTML 要素注釈と自動リロード、ディクテーションの多言語オンデバイス判定
  - https://github.blog/changelog/2026-08-31-github-copilot-in-vs-code-august-2026-releases/
- **Copilot CLI に pre-release `v1.0.83-0` が出た**（8/31 14:46 UTC）。安定版は `v1.0.82`（8/29 23:39 UTC）のままである
  - HTTPS プロキシの mTLS クライアント証明書を、モデル要求と Web 要求の両方で自動的に使えるようになった
  - ターミナルマルチプレクサの判別が herdr と tmux を区別するようになり、Kitty キーボードプロトコルと通知が有効になる
  - `/sandbox` のポリシー表示がパス許可を付与元ごとにグループ化するようになった
  - 入力欄より上に出力が隠れる不具合と、セッションエクスポートが最新の実行分しか含まなかった不具合を修正した
- **`github.blog/changelog` の Copilot ラベルは 8/28 の3本が最上位のまま**で、VS Code の8月分エントリを除けば 8/29〜8/31 の追加が4日間ない
- **Cursor changelog は 8/27 の「Start from scratch, without a repo」が最上位のまま**で、8/28〜8/31 の追加が5日間ない（RSS 200）。フォーラム Announcements も 8/17 の Origin Code Hosting が最上位のまま15日間動いていない
- **Devin は一次に到達できない状態が続いている**。`docs.devin.ai` のゲートウェイ拒否が継続し、⚠️ 二次が挙げる MCP コネクタ48件超の追加と beta 42件の GA 昇格は公開日を特定できず、既報との切り分けができないため新着扱いにしていない

### Microsoft 365 Copilot / Copilot Studio / Power Platform

- **GitHub Copilot ハーネスの従量課金化はハイライト2参照**
- **SharePoint のクラシックページが2段階で読み取り専用になる** — SharePoint Blog に 8/31 付で「Upcoming changes to classic experiences in SharePoint Online」（記事ID 4549091）が出て、一次の Learn 記事 `sharepoint/classic-user-created-page-deprecation`（`updated_at` 2026-08-28T22:04Z）が公開された。全 digest に掲載歴はない。⚠️ 前提の変化は日程より理由の側にあり、Microsoft は「クラシックページは Copilot を支えるコンテンツ形式に十分に含まれず、応答の網羅性と精度を下げる」と初めて明記した
  - フェーズ1（**2027-03-01 開始**）: 全テナントでクラシック発行サイトの新規作成とクラシック発行機能の有効化が停止し、`AllowClassicPublishingSiteCreation` が `False` で固定される。同日以降に作成された新規テナントは追加でクラシックページの新規作成が不可になり、`DenyAddAndCustomizePages` が `True` で固定される
  - フェーズ2（**2028-10-01 開始**）: 上記の制限が既存の全テナントへ広がり、クラシックのユーザー作成ページが読み取り専用になる
  - 対象: wiki ページ／Web パーツページ／ブログページ／発行ページ／SharePoint Designer・サードパーティ製のカスタム ASPX ページ。リストとライブラリのビュー、リストフォームページは範囲外だが、そこに埋め込まれた custom script は対象になる。対象クラウドは GCC / GCC High / DoD・エアギャップ環境・21Vianet 運用版を含む全環境である
  - 止まらないもの: Microsoft がコンテンツを削除・変更することはなく、既存ページは閲覧可能なまま残る。モダンページと SPFx 製のカスタムソリューションは影響を受けない
  - 本日から着手できるのは棚卸しである。Purview 監査の SharePoint Classic Activities カテゴリ（Audit Standard に含まれ全組織が使える）の `ClassicPageCreated` / `ClassicPageEdited` / `ClassicPageViewed` イベントで実利用を特定し、Microsoft 365 Assessment Tool で近代化の可否を評価する。⚠️ 移行支援の SharePoint Page Migration Agent（Preview）はオープンソースで Microsoft のサポート SLA がなく、高度にカスタマイズされたページは再設計か手作業での作り直しが必要になるとされている
  - フェーズ1では10種類の発行系サイトテンプレート（`BLANKINTERNETCONTAINER#0`・`CMSPUBLISHING#0`・`ENTERWIKI#0` 等）の新規作成が塞がるため、SharePoint Server からの as-is 移行も同日以降は成立しない。ブログ側は対象機能の利用が月間アクティブテナントの5%未満だとしている
  - https://learn.microsoft.com/sharepoint/classic-user-created-page-deprecation
- ⚠️ **Copilot Studio の課金ページ3本が移設され、旧パスが 404 を返す** — `billing-credit-overview` / `billing-manage-buy-credits` / `enforcement-policy-credits` の3本が `microsoft-copilot-studio/` 直下から `agents-experience/` 配下へ移り、旧パスは 301 リダイレクトではなく 404 になる。`billing-credit-overview` は `updated_at` 2026-08-31T19:03Z で本文も更新され、タスク複雑度別のクレジット消費レンジ図と Copilot Credits 見積りツールへのリンクが加わった（B-052 起票）
- **Release Wave の3ページは 8/28 から5日連続で再ビルドされていない** — `power-automate` / `power-apps` / `power-platform-governance-administration` の3ページとも `updated_at` 2026-08-27T17:04Z・同一 `git_commit_id`（`b92ae441`）である。8月期日8件と期日超過5行を合わせた13行が緑チェックのないまま9月へ入り、9月に期日がある行は3ページ計12件ある
  - 冒頭 Important の移行注記（2026年9月から Release Plans の新規掲載を停止し AI at Work roadmap へ移す）は3ページとも入ったままで、本日はその「9月」の初日にあたる。掲載停止と期日が同じ月に重なる
  - Roadmap 側は Copilot Studio 製品の15件がすべて `In development` のままである。⚠️ 566997（メーカー資格情報の使用ブロック）は GA 期日「August CY2026」を満たせないまま9月に入り、562221（ワークフローでの MCP 準拠ツール）は GA 期日 2026年6月から超過4か月目に入った
- ⚠️ **Copilot Studio の What's New は July 節が最新のまま**で、8月節がいまも作成されていない。July 節6項目・June 節10項目とも増減がなく、`updated_at` は 2026-08-20T19:04Z から動いていない。June 節の GitHub Copilot ハーネスは本日も `(Production-ready preview)` のままで、GA（8/3）から**29日連続の未反映**である
- **Copilot Studio のビルドは `2026.6.3`（6/30 初出）のまま空白が63日に達した**。本日は火曜＝ページ本文が宣言する定例更新日にあたるが新ビルドは出ず、定例日の空振りは9回連続になった。リージョン分布（11 / 5 / 3 の3段）と UX 版 26.06.21-24 も据え置きである
- ⚠️ **Copilot Tuning は停止発効（8/20）から12日たっても一次に停止も退役も書かれていない**。`copilot-tuning-overview` の `updated_at` は 2026-08-18T17:48Z から動かず、Optimization エージェントは「サポートされるシナリオ」節とテンプレート選択表の両方に現行機能として残り、冒頭 Important も「Frontier 経由の提供は 2026年4月予定」で止まっている
- **M365 Copilot Release Notes は August 25, 2026 バッチが最新のまま**で、10節・全19項目に増減がない。`updated_at` は 2026-08-25T20:41Z で、隔週傾向どおりなら次バッチは 9/8 前後になる
- ⚠️ **AI at Work Roadmap の広報枠は8月に1件も追加されないまま9月へ入った**。Latest announcements の先頭は 7/24「Available today: Anthropic's Claude Opus 5 in Microsoft 365 Copilot」のままである。Microsoft 365 Blog 本体も RSS 200 で先頭が 7/30 のまま変わらず、WebSearch 照合でも8月以降の新規記事は確認できなかった
- **Purview の What's New は 8月節4件（Sensitivity labels 2件＋Data Loss Prevention 2件）のまま増減がない**。⚠️ 569612（Copilot メモリの Purview 保持）は本日も Purview 側に掲載がない。Copilot Studio ガイダンスハブも索引の `updated_at` が 2026-08-28T19:03Z で動かず、新規記事はゼロである
- **Cowork What's New の August 2026 節は3件のまま増減がない**（プラグインツールへのワークスペースファイル入力、ローカルブラウザー使用の GA 昇格、イベント駆動タスク）
- **MAICPP 契約の更新条項が本日自動発効した** — Partner Center の 8/13 付「Monthly Microsoft AI Cloud Partner Program update」内の節が、7/1 に公開された更新版の条項が 2026-09-01 から自動的に効力を持つと明記している。署名も承諾操作も不要で、パートナー側の作業は発生しない
  - ⚠️ Partner Center の9月ページ（`announcements/2026-september`）はまだ 404 で未作成である。8月ページは `updated_at` 2026-08-27T16:43Z で `## ` 見出し22本のまま追記がなく、先頭は 8/27 の Eligibility Dashboard である
- **その他の一次ソースに変化はない**: Microsoft Copilot Blog（7/21 が最新）、Copilot Studio Blog（8/3 の新ハーネス記事が最新・board RSS の並び順の乱れは19日連続）、Tech Community M365 Copilot Blog（8/13 が先頭）、M365 Developer Blog（8/27 の SPFx roadmap・1.24 GA は 2026年10月予定で据え置き）、Agent 365 Blog（8/6 が最新）、Power Platform Blog（親ページ先頭は 8/25 の roadmap 移行記事）
- ⚠️ 取得できなかったソース: `mc.merill.net` が `EGRESS_BLOCKED` で25日連続、`www.ppweekly.com/feed` が5回連続スキップ（8/10・8/17・8/24・8/31 に続き休刊明けの判定ができない）、`pnp.github.io` も `EGRESS_BLOCKED`（週次確認は 8/30 に実施済みで期限内）、Copilot Studio Release Wave の登録 URL は `aka.ms` へ 301 する先がゲートウェイ拒否である

### Google

- **Gemini API changelog は 8/27 の Gemini Omni Flash GA が最上位のまま**で、8/28〜9/1 の追加がない。日付列は 8/27 → 8/26 → 8/13 → 7/30 → 7/21 → 7/6 である
- **Gemini API 料金は3日連続で据え置かれている**（一次の最終更新は 8/28 UTC）。3.7 Flash / 3.6 Flash は入力 $0.75・出力 $3.75（2026-12-31 まで。2027-01-01 から $1.50／$7.50）、3.5 Flash $1.50／$9.00、3.5 Flash-Lite $0.30／$2.50 で変化はない
- **8/31 付けの Google の AI 発表は検出できなかった**。登録済み Google 系5ソースはゲートウェイ拒否が継続し、`ai.google.dev` の `changelog.md.txt` だけが到達できる一次である
- 既報: 旧 `gemini-omni-flash-preview` は 9/30 廃止、`gemini-robotics-er-1.6-preview` は 8/31 に停止済み。**Gemini 3.5 Pro の GA は未ローンチが継続**している

### オープンウェイト / MCP / xAI

- **DeepSeek が V4-Flash-Vision-Exp の重みを MIT で公開した** — 8/21 に API 限定で始まった実験的マルチモーダルモデルの重みが、8/31 に Hugging Face 上へ公開された。画像を読むエージェント基盤の選択肢が「API を呼ぶ」から「自社環境に置ける」へ動いた
  - 一次確認値: `createdAt` 2026-08-31T06:16 UTC / `lastModified` 同日 12:23 UTC / `private: false` / `gated: false` で、safetensors 48シャードを含む全84ファイルが公開されている
  - `config.json` は `DeepseekV4ForCausalLM`・`expert_dtype: fp4`・`quantization_config.quant_method: fp8`・`num_experts_per_tok: 6` で、pipeline は `image-text-to-text` である
  - モデルカードのベンチマークは ApexBench 36.5、Agents' Last Exam 27.3、Chartography 64.3、ZeroBench 35.0、Terminal Bench 83.9 で、テキスト単体の性能は V4-Flash と同等を維持したままマルチモーダルエージェント性能を伸ばしたと説明されている
  - ⚠️ 総パラメータ 284B と context 100万トークンは二次のみで、一次では確認できていない。⚠️ API 提供開始（8/21）を10日間検出できていなかった（一次の `api-docs.deepseek.com` はゲートウェイ拒否かつ登録ソース外・B-054 起票）
  - https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-Vision-Exp
- **他の7 org に 8/31 の新規公開はない**。8 org（`Qwen` / `moonshotai` / `deepseek-ai` / `meta-models` / `mistralai` / `zai-org` / `openai` / `google`）を `createdAt` 降順と `lastModified` 降順の両方で確認した。`lastModified` 降順で 8/31 に動いたのは `Qwen/Qwen3.8-Flash-Next-FP8`・`zai-org/GLM-5.3`・`GLM-5.3-Flash`・`GLM-5.3-Flash-BF16`・`google/timesfm-3.0-pytorch` で、いずれも既存リポジトリのカード更新である
- **HF `downloads` の実測**（2026-08-31 19:10 UTC 取得。⚠️ 前日比は書かない運用）
  - `Qwen/Qwen3.8-27B-FP8` 5,303,437／likes 739　`Qwen3.8-Flash-Next` 158,598／likes 4,503　`Qwen3.8-Flash-Next-FP8` 84,954／likes 173
  - `DeepSeek-V4-Flash-0731` 4,561,861／likes 3,839　`DeepSeek-V4-Pro-0813` 134,723／likes 791　`DeepSeek-V4-Flash-Vision-Exp` 0／likes 299
  - `GLM-5.3-Flash` 379,271／likes 1,801　`GLM-5.3` 66,195／likes 1,409　`GLM-5.3-Flash-BF16` 8,648／likes 52　`GLM-5.3-BF16` 2,354／likes 29
  - 追跡リポジトリは全て `private: false` / `gated: false` で公開状態に変化はない
- **`blog.modelcontextprotocol.io` は 8/22 の「The New MCP Roadmap」が最上位のまま**で10日間新規がない。WebMCP は MCP 公式ブログ側に依然として言及がなく、OpenAI 発の別系統として扱う状態が続いている。A2A の AAIF 参加も未確定のままで、一次3ホストのゲートウェイ拒否が継続する
- **xAI が Grok Build を 8/30 に更新したとされる**。エージェントが続行前に承認を求められるようになり、中断した応答の継続・一時エラーの再試行・セッション保存と外部ツール接続の改善が入ったと報じられている。Grok Build は `grok-build-0.1` を主モデル、Grok 4.5 を控えとして動き、Grok 4.6 も選べる。⚠️ 一次3ホスト（`x.ai` / `docs.x.ai` / `grok.com`）は到達不可で、内容は二次のみである。**Grok 5 は未リリースが継続**する

### 市場データ・調査 / 企業動向

- **McKinsey State of AI 2026 が公開された**（8/25・03 側で7日遅れの捕捉） — 世界・全業種の専門家およびビジネスリーダー1,719名を対象とした調査で、提案の論点が導入率から成果寄与へ移る
  - エージェントのスケール: 大企業で1機能以上へスケールした割合が **27%→40%** へ伸びた一方、中小企業は 22% で横ばいだった。少なくとも実験段階にある組織は 62% にのぼる
  - ソフトウェア購買の代替: 32% が、agentic coding ツールで内製できることを理由にソフトウェア製品・機能の購入を少なくとも1件見送った。業種別ではテクノロジー 41%、医療ペイヤー／プロバイダー 39% が続く
  - 成果への寄与: 何らかの EBIT 影響を認めるのは 37% で 2025年調査とほぼ同水準にとどまり、EBIT の5%以上を AI に帰属させる「AI 高パフォーマー」は 6% しかいない。高パフォーマーは、ワークフローを AI 向けに抜本的に再設計している割合とある機能でエージェントをスケールしている割合が、いずれも他社の3倍にあたる
  - 障壁: 完全なスケールを阻む最上位の要因は約3分の2が挙げるセキュリティ・リスク懸念で、規制の不確実性や技術的制約を上回る
  - ⚠️ 一次 `www.mckinsey.com` は本日新規にゲートウェイ拒否となり、数値は複数の二次の突き合わせによる。EBIT 寄与は「37%（何らかの影響）」と「39%（企業レベル）」の2系統が二次に混在しており、引用時はどちらの定義かを確認する必要がある
  - https://www.theregister.com/ai-and-ml/2026/08/25/mckinsey-says-enterprise-ai-is-finally-on-the-road-to-roi/
- **IBM と Together AI が $240M の推論クラスタ契約を結んでいた**（8/11・03 側で20日遅れの捕捉）。IBM Cloud 上に NVIDIA HGX B300 と Spectrum-X Ethernet で構成する専用クラスタを構築し、Together AI がオープンモデルの推論提供に使う。IBM Cloud で推論向けに構築される初の大規模専用クラスタで、稼働は 2027年 Q1 を見込む。学習ではなく**推論**への大型投資である点が、既収録の Anthropic × Nscale $45B 等の計算契約と性格を分ける
  - https://newsroom.ibm.com/2026-08-11-IBM-and-Together-AI-Sign-Multi-Year-Agreement-to-Scale-Open-Source-AI-Inference-with-NVIDIA-AI-Infrastructure-on-IBM-Cloud
- **Google・OpenAI・Anthropic を含む100社超が、AI を使ったサイバー攻撃への「防御の総動員」を求める公開書簡に署名した**（8/27 公開・01 側で本日初検出）
  - 署名企業には Microsoft・Capital One・Mastercard・Visa・Adobe・Oracle・IBM・Hugging Face・Cisco・SAP が含まれる
  - 書簡は「今後数ヶ月で AI を使った攻撃が大幅に広範かつ高度になる」と述べ、重要インフラ周辺のセキュリティが歴史的に手薄であると指摘している
  - 政府には病院・水道事業者への防御用 AI と検証の提供を、フロンティア AI 企業には責任あるモデル提供・資金・訓練・実地支援を求めている
  - ⚠️ 一次は `openai.com/collective-cyberdefense` だが、`openai.com` はオリジン403のため一次未読である
  - https://gizmodo.com/google-openai-and-over-100-companies-call-for-more-action-on-ai-driven-cyberattacks-2000804091
- **市場データ定点に更新はない**。IDC・MM総研・NRC・Similarweb のいずれも新規公表を検知できなかった。参照可能な最新値は IDC の国内AI市場予測（2025年 2兆3,725億円 → 2029年 6兆8,897億円・CAGR 36.0%、2026年3月公表）と MM総研の個人利用経験率 21.8%（2025年8月時点）で、いずれも既収録から不変である
- 既報: Sony Music Publishing と Warner Chappell Music による Anthropic 提訴（8/28）で大手3社の出版部門が出揃った、連邦地裁による国防総省の指定違法判断（8/27）、Claudeforce（8/26）、SpaceX による Cursor 買収完了（8/14・$60B）、OpenAI が Cursor へのモデル提供を 11/12 で打ち切り

### Apple / クラウド

- `developer.apple.com` は 200 で、**8/27 の「Tax and price updates for apps, In-App Purchases, and subscriptions」が最上位のまま**である。8/28〜8/31 の追加はない
- **AI 関連の最新は 6/11 の ImageCreator クラス廃止告知**のままで、8/5 の App Store creative assets 以降に新規がない
- 既報: 8/26 の特別イベント告知（9/9 10:00 PT）、8/24 の Sign in with Apple 新ドメイン、8/18 の EU 向けビジネス条件変更（発効 10/1）、8/12 の韓国 GRAC レーティング（10月に2記述子が All → 12+）

## 直近の注目予定

- **9/1（本日・6件が発効）**: GitHub Copilot ハーネスの開発者環境・トライアル環境が従量課金へ ／ Copilot の全体験でモデル廃止 ／ Copilot global model policy の全 enterprise 適用完了 ／ Copilot Business・Enterprise の新規申込受付再開（審査強化。前払い化ではない）／ OpenAI Daybreak 全アカウントでハードウェアセキュリティキー必須化 ／ MAICPP 更新条項の自動発効。あわせて Sonnet 5 の $3/$15 値上げが撤回のまま当日を通過し、Copilot Studio Released Versions の定例更新日は9回連続の空振りになった
- **9/3**: Power Platform 非推奨一覧の週次確認
- **9/4**: WebMCP Challenge の提出締切 ／ 拡張機能 What's New とモデル可用性一覧の週次確認
- **9/6**: Power CAT（Copilot Agent Kit）の週次確認
- **9/7**: 週次復旧チェック（月曜）／ ppweekly・MS-4005・課金レート表の週次確認
- **9/8 前後**: M365 Copilot Release Notes の次バッチ（隔週傾向）
- **9/9**: Apple 特別イベント（10:00 PT）／ GLM-5.3-Flash の Z.ai 経由50%割引が終了
- **9/10**: MAI-Code-1-Flash が全 Copilot 体験から廃止
- **9/13**: Claude Code の週次上限50%増が終了
- **9/14**: Claude Code の標準週次上限が恒久的に +25%（Pro / Max / Team / シート課金 Enterprise。現行比では17%減）
- **9/17**: OpenAI DevDay Exchange の応募締切
- **9/21**: Anthropic ウェルビーイング研究助成の応募締切
- **9/23**: WebMCP Challenge の受賞発表
- **9/24**: OpenAI の Videos API と Sora 2 が退役（代替モデルの提示なし・残り23日）
- **9/28**: Copilot のチャット3面統合 ／ code review の既定 effort が Lite → Balanced ／ チャットのデータ保持が28日からアカウント存続期間へ ／ OpenAI の `gpt-3.5-turbo-instruct`・`babbage-002`・`davinci-002`・`gpt-3.5-turbo-1106` 退役
- **9/29 以降**: `claude-sonnet-4-5-20250929` の暫定退役日（確定日ではない）
- **9/30**: Gemini の旧 `gemini-omni-flash-preview` エンドポイント廃止 ／ M365 E7 プロモーション最終日 ／ M365 E5・E3 の CSP 割引終了 ／ 2026 Wave 1 の対象期間終了
- **9 月**: iOS 27 / macOS 27 GA ／ Claudeforce のオープンベータ（二次情報）／ Release Plans on Learn の新規掲載停止と AI at Work roadmap への掲載開始 ／ Copilot Tuning の Public Preview 再開 ／ 569612・569930・569607・569928 の GA と 569475 の Preview ／ Release Wave の9月期日12件 ／ Copilot デスクトップアプリの広範展開（中旬）／ Eligibility Dashboard の展開完了（中旬）／ App Store の Social Media 年齢レーティング回答が必須化 ／ OpenAI の IPO 観測
- **10/1**: Copilot Business・Enterprise の既存顧客が前払い必須に ／ Apple の EU 向け新ビジネス条件が発効 ／ Ask Gemini in Chat のプロモーション上限が終了 ／ CSP software 価格改定の発効
- **10/5**: Anthropic ウェルビーイング研究助成の full proposal 提出期限（採択者）
- **10/15 以降**: `claude-haiku-4-5-20251001` の暫定退役日（確定日ではない）
- **10/16–11/11**: OpenAI DevDay Exchange 8都市（**東京は 10/20**）
- **10/23**: OpenAI のレガシースナップショット退役（`gpt-3.5-turbo` / `gpt-4-0613` / `gpt-4-turbo` とファインチューン版、`o1` / `o1-pro` / `o3-mini`）
- **10/31**: OpenAI の既存 evals が読み取り専用化
- **10 月**: Anthropic の IPO 予定（$2T 超の評価額を目標と報道）／ SPFx 1.24 GA ／ 569608・569475・568937 の GA ／ 韓国 App Store のコンテンツ記述子2件が All → 12+
- **11/12**: OpenAI が Cursor へのモデル提供を停止
- **11/15**: Release Planner の退役
- **11/21**: GPT-5.6 Sol の暫定値下げが有効とされる期限
- **11/24 以降**: `claude-opus-4-5-20251101` の暫定退役日（確定日ではない）
- **11/30**: OpenAI の Reusable prompts・Evals プラットフォーム・Agent Builder が停止（**本日追加**）
- **12/1**: OpenAI の GPT Image 系が停止（`gpt-image-1-mini` / `gpt-image-1.5` / `chatgpt-image-latest`。**本日追加**）
- **12/2**: EU AI Act の生成コンテンツ標識義務、8/2 以前に市場投入済みシステムへの猶予終了
- **12/11**: OpenAI の旧スナップショット退役（`gpt-5-2025-08-07` / `o3-2025-04-16` / `o3-pro-2025-06-10` 等）
- **12/31**: Gemini 3.7 Flash の導入価格終了（$0.75/$3.75 → $1.50/$7.50）
- **12 月**: Copilot Tuning の新体験が GA
- **年内**: Anthropic の新データ保持方式（顧客自身のクラウドでの30日保持）投入予定 ／ OpenAI の Jalapeño チップの初期展開
- **2027-01-06**: OpenAI で大半のユーザーの新規ファインチューニングジョブ作成が終了（**本日追加**）
- **2027-01-20**: OpenAI の audio / realtime 系退役（`gpt-realtime` / `gpt-audio` / `gpt-4o-audio` と mini 系）
- **2027-02-26**: OpenAI の文字起こし4モデル退役（`whisper-1` / `gpt-4o-transcribe` / `gpt-4o-mini-transcribe` / `gpt-4o-transcribe-diarize`。**本日追加**）
- **2027-03-01**: SharePoint クラシック退役フェーズ1（**本日追加**）
- **2027-06-30**: Claude for Teachers の学区登録期限
- **2027年末**: Anthropic が借りる Nscale West Virginia データセンター（460MW）の稼働開始見込み
- **2028-06**: 米国 K-12 教職員向け ChatGPT for Teachers の無料提供期限
- **2028-10-01**: SharePoint クラシック退役フェーズ2（**本日追加**）

## 改善メモ

- 3ソースの当日分（01 Master / 02 Copilot / 03 industry）はいずれも取得できた。前日 08-31 分にも欠損記録はなく、欠損リカバリの対象はない
- **前日 08-31 の記載を1点訂正した** — 9/1 を「Copilot Business・Enterprise の新規シートが前払い必須に」と書いたのは誤りである。03 が一次の告知本文を読み直し、9/1 は新規申込受付の再開（＋審査強化）、前払い化は 10/1 の既存顧客向けと確定した。⚠️ **01 の本日分も同じ誤りを残している**ため、次回以降も突合が必要になる
- ⚠️ **Claude Code `2.1.252` の changelog 掲載有無が 01 と 03 で食い違う** — 01（取得 8/31 19:20 UTC 頃）は「npm に publish されたが changelog には載っていない」、03（同 20:15 UTC 頃）は「一次 changelog で 8/31 付の新版を確認・修正4件」としている。取得時刻の約1時間差で反映されたとみて本サマリーは 03 側を採ったが、01 の `dist-tags` 実測（`next: 2.1.252`）とは矛盾しないため両論を残す
- **新規の改善提案は4件** — B-054（01: DeepSeek 公式 news `api-docs.deepseek.com/news/` をソース登録）、B-055（01: OpenAI 退役ページ `developers.openai.com/api/docs/deprecations` をソース登録）、B-052（02: Copilot Studio 課金3ページの URL 移設に伴う追跡 URL 差し替え）、B-053（02: `manage-usage-github-copilot-harness` を課金統制の一次として追跡対象に追加）。03 は新規提案なし
- **継続提案は3ソース計86件**（01: 34件・最多は B-013 の34回目、02: 40件・最多は B-011 の43回目、03: 12件・最多は B-004 の64回目）。⚠️ 02 の継続提案数が前日 28件から 40件へ12件増えており、内訳の変化は本日のダイジェストからは追えない
- **ゲートウェイ拒否が6ドメイン新規に発生した**（03 側）: `www.mckinsey.com` / `www.helpnetsecurity.com` / `www.cxtoday.com` / `securityaffairs.com` / `thecyberexpress.com` / `blog.gridinsoft.com`。⚠️ **`www.mckinsey.com` は `daily-sources.md` に年次レポート枠で登録済みの定点ソース**であり、公開想定月（3〜5月）は毎日確認する対象にあたる。到達不能が確定したため、次回の公開期は二次前提の運用になる。01・02 側は障害の変化なし
- **`platform.claude.com` の料金ページは WebFetch に成功した**（03 側）。Sonnet 5 の単価と 9/1 値上げ撤回の注記を一次で確定できている（`www.claude.com/pricing` は本文が途中で切れ API 単価まで届かない）
- ⚠️ **長期化している一次未読・接続障害**: 8月 Risk Report が16日連続（01）、`mc.merill.net` の EGRESS_BLOCKED が25日連続（02）、Copilot Tuning 一次の未更新が12日連続（02）、`www.ppweekly.com` が週次確認日5回連続スキップ（02）、Copilot Studio What's New への GA 未反映が29日連続（02）。いずれも解消の見込みが立っていない
