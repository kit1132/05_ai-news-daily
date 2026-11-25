# AI News Daily Summary — 2026-11-26

Microsoft はテナント App Catalog への app-only 書き込みに 2027-01-31 から新しい SharePoint 権限を求め、SPFx を CI/CD で配る仕組みは権限の追加が要る。Claude Code `2.1.332` は Foundry の既定モデルを Sonnet 5.5 に変え、デプロイしていない組織は起動時のモデルが使えない。OpenAI は ChatGPT の Sites を 2027-02-01 から課金し、無料で置いてきたサイトに月の枠が掛かる。

## 今日のハイライト

### 1. [破壊的変更] Microsoft がテナント App Catalog への app-only 書き込みに新しい権限を求める — SPFx パッケージを自動配布する仕組みは、2027-01-31 までに `SharePointTenantSettings.ReadWrite.All` を足さないと拒否されうる

**要点**: Microsoft が 11/25、app-only 認証でテナント App Catalog にパッケージを追加・更新する処理に、2027-01-31 から SharePoint の `SharePointTenantSettings.ReadWrite.All` が要ると告知した。`Sites.ReadWrite.All` だけで動いてきた CI/CD の配布は、期限後に止まりうる。11/25 に載せた Copilot UX コンポーネントの配布もこの確認を通る。

**詳細**: M365 Developer Blog（11/25）による（Copilot）。
- 権限の種類: Office 365 SharePoint Online 側の権限で、SharePoint のアクセストークンに入っている必要がある。同じ名前の Microsoft Graph 側の権限では代わりにならない
- 対象の操作: Apps for SharePoint へのパッケージの追加・更新と、Tenant-Wide Extensions の追加・更新。テナント全体の拡張を登録しないパッケージでも、アップロード時に確認される
- 対象外: 管理者の UI 操作、委任認証の PnP PowerShell、読み取りと削除、展開済みの SPFx ソリューションの実行
- 手順: Entra のアプリ登録に権限を付け、テナント管理者の同意を得てトークンを取り直し、アップロード・更新を再テストする。既存のサイト権限は外さない

出典:
- https://devblogs.microsoft.com/microsoft365dev/action-required-update-app-only-permissions-for-sharepoint-tenant-app-catalog-writes/

### 2. [破壊的変更+新機能] Anthropic が Claude Code `2.1.332` を出した — Foundry の既定モデルが Sonnet 5.5 に変わり、Desktop の OTel `service.name` も変わったので、クラウド経由の配備と監視の絞り込みは見直しが要る

**要点**: Anthropic が Claude Code `2.1.332` を npm `latest` にした。Microsoft Foundry の既定モデルと `opus` エイリアスが 5.5 世代へ移り、`claude-sonnet-5-5` をデプロイしていない組織は起動時のモデルが使えない。Desktop の Code タブの OTel `service.name` も `claude-code-desktop` に変わり、`claude-code` で絞る集計は更新した時点でずれる。

**詳細**: Claude Code changelog による（Master・industry）。npm の公開は 2026-11-24T22:06Z（JST 11/25 07:06）。
- Microsoft Foundry: 既定モデルが Sonnet 5.5、`opus` が Opus 5.5 になった。`claude-sonnet-5-5` をデプロイするか、`ANTHROPIC_DEFAULT_SONNET_MODEL` にデプロイ済みのモデルを設定する。Sonnet 4 / Opus 4 / 4.1 は退役扱いになった
- Google Cloud Agent Platform: `sonnet` が Sonnet 5.5 になり、`VERTEX_REGION_CLAUDE_5_5_SONNET` を読む（`4_5` の変数だけだと `CLOUD_ML_REGION` か `us-east5` へ）
- Amazon Bedrock: `sonnet` は Sonnet 4.5 のまま。Bedrock Mantle の `sonnet` が Haiku 4.5 を指していた不具合は Sonnet 5 に直り、Sonnet 5 を有効にしていないアカウントではエラーになる
- 既定モード: Bedrock Mantle / Agent Platform / Foundry で Sonnet 5 / 5.5 に移ったセッションは、モード未設定なら auto mode で始まる。止めるには `disableAutoMode` を `"disable"` にする
- 運用: Self-hosted runner の `CLAUDE_CODE_OAUTH_TOKEN` に `oat02-` 接頭辞が加わり、`oat01-` で照合するプロキシ規則やログのマスクは更新が要る。旧 `service.name` を保つには `OTEL_SERVICE_NAME` を使う
- 追加: MCP サーバー由来のスキル（beta、`/` メニューに `server:skill` で出る）、スキルの読み込み時のシェルコマンドを拒否できる `PreSkillShellCommand` フック、起動ヘッダーの Cyber Verification Program 階層表示
- そのほか: macOS で computer use が有効なとき `computer-use` は予約スキル名になる。Claude apps gateway の組み込み一覧の2番目が Sonnet 5.5 になった。npm の `stable` は `2.1.325` から `2.1.326` に進んだ

出典:
- https://code.claude.com/docs/en/changelog
- https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md

### 3. [料金+予定] OpenAI が ChatGPT の Sites を 2027-02-01 から課金する — 無料で置けたサイトやアプリに月のクレジット枠が掛かり、データベースを持つサイトは空でも1件ごとに枠を使う

**要点**: OpenAI が Sites（ChatGPT で作ったサイトやアプリを公開する機能）の料金を公開した。ホスティングは 2027-01-31 まで無料で、2/1 から Plus・Pro・Business の月間枠を超えた分が課金される。空のデータベースでも1件につき月 25 クレジットを使うため、無料前提で置いてきた社内ツールは件数で費用が決まるようになる。

**詳細**: Sites の料金ページによる（industry）。利用量は 2027-01-01 からアプリ上に表示される。
- 月間枠（利用者のサイト全体で共有）: Plus 125 クレジット、Pro 375、Business は1席あたり 125。Enterprise は契約したクレジットから引かれ、ドル建ての契約なら Codex のトークンと同じ契約額から別単価で引かれる
- 消費の目安: ストレージなしのサイトは 0。ストレージありのサイトは1件につき月 25、通信 10万リクエストごとに 15、データベース保存 1GiB・月ごとに 150、ファイル保存 1GiB・月ごとに 3.75、独自ドメインは1件につき月 25（取得費は別）
- Enterprise のみ: サイトとトンネルの接続は30日ごとに 125（日割り）
- 枠を超えたときの扱いと、Edu の枠は書かれていない

出典:
- https://learn.chatgpt.com/codex/sites/usage-and-cost
- https://learn.chatgpt.com/docs/sites

## カテゴリ別まとめ

### Anthropic / Claude

- **Claude Code `2.1.332`**（ハイライト2参照）
- [新機能] **artifact のデスクトップアプリ化** — Anthropic が 11/24、Claude の artifact を Claude for Mac / Windows から独立したアプリとして入れる機能を全プランで beta にした。Team は既定オン（全面的なコンピューターアクセスはオフ）、Enterprise はオーナーが有効にするまでオフで、管理者が何もしなければ Team では社員が作ったアプリが端末に入る（Master・industry）
  - 権限は3段: 既定（ブラウザーでできることだけ）、アプリ権限（最前面ウィンドウ・グローバルショートカット・通知）、全面的なコンピューターアクセス（確認なしでプログラムを実行し、ファイルを読み書き・削除する）
  - 全面アクセスは自作のアプリか、Team / Enterprise では組織内で作られたアプリに限る。更新（自分の編集を含む）のたびに権限を確認し直す。Anthropic はインストール前にアプリを審査しない
  - 対象外: HIPAA 対応組織、ハイブリッド配備、Claude Docs / Slides / Sheets の artifact。アプリから Claude への要求はプランの利用上限に数えられる
  - 同日の release notes には、接続アプリとの間でファイルを送受信する機能（beta。Pro / Max / Ultra へ順次、Team / Enterprise はオーナーが有効化）もある
  - https://claude.com/resources/articles/install-as-app
  - https://support.claude.com/en/articles/12138966-release-notes
- [仕様] **Enterprise Analytics API の数え漏れの修正** — Anthropic が Platform release notes の 11/23 付に3項目を足し、List User Activity の `web_search_count` と Get Connector Usage の利用者数の数え漏れを直した。Get Chat Project Usage の修正は 11/24 に入り、修正後の値は以前より大きくなりうる（Master）
  - https://platform.claude.com/docs/en/release-notes/overview
- [動向] **Messages API の Rust 移行** — Anthropic が 11/25、Messages API の中核を Python から Rust へ移したと公表した。リクエストあたりの CPU が約70%、メモリが80%超減り、最初のトークンまでの時間の中央値が約20%縮んだ。公開 API の挙動とドキュメントは変えていない（Master）
  - https://www.anthropic.com/research/migrating-api-to-rust
- [観測] **Claude Opus 5.6 の A/B テスト** — TestingCatalog が、Anthropic が Claude Opus 5.6 を A/B テストしているとの観測を報じた（二次・公式未確認）。モデル一覧の現行は Fable 5.2 / Opus 5.5 / Sonnet 5.5 / Haiku 5.5 のままである（Master）
  - https://www.testingcatalog.com/testers-share-early-results-possible-claude-opus-5-6/
- [据え置き] **Anthropic のその他の一次** — モデル退役一覧（Active 16件・最新告知 11/23 Opus 4.5）と `/news`（11/20）は動いていない（Master・industry）

### OpenAI / Codex / ChatGPT

- **ChatGPT Sites の課金**（ハイライト3参照）
- [予定] **Private Inference の企業試験** — The Decoder（11/25）によると、Sam Altman が、最上位モデルへの問い合わせを OpenAI が中身を読めない形で処理する Private Inference を、最初の企業顧客で試していると述べた。処理は第三者が安全性を検証できる隔離ハードウェアで行い、一般提供の時期と料金は示されていない（industry）
  - https://the-decoder.com/openai-wants-companies-to-trust-it-with-sensitive-work-by-promising-not-to-look-at-their-data/
- [動向] **GPT-6 系のタンパク質設計の研究** — OpenAI が 11/24、GPT-6 系のモデルがタンパク質設計の能力を持つことを示す研究を公開した（Master）
  - https://openai.com/index/gpt-6-models-demonstrate-intrinsic-protein-design-capabilities/
- [版更新] **Codex の pre-release `0.174.0-alpha.5`** — OpenAI の Codex は安定版 `0.172.0`（11/24）のまま、pre-release が `0.174.0-alpha.5`（11/25）に進んだ。alpha のリリース本文は版番号だけである（Master）
  - https://github.com/openai/codex/releases
- [据え置き] **OpenAI のその他の一次** — API changelog（11/24）、deprecations（最新告知 11/18）、community Announcements（11/20）、ChatGPT release notes（11/23）、ChatGPT & Codex changelog（11/24）、Deployment Safety Hub（11/23）、misalignment reports（First posted 最新 11/18・報告26件）は動いていない（Master・industry）

### GitHub Copilot / GitHub

- [破壊的変更] **Copilot CLI `v1.0.116`** — GitHub が 11/25 に安定版を出し、計画の承認画面で fleet を選べなくした（`/fleet` は残る）。実験的拡張の設定は Enabled / Disabled の2値になり、既存の「Load Only」は無効へ移るので、拡張を前提にした環境は再設定が要る（Master）
  - サンドボックス: コマンドを止めたとき、Copilot は実行を利用者に戻さずに止まり、ポリシーが許せばセッション単位でサンドボックスを外すよう提案する
  - ACP: シェル承認は説明文ではなく実行するコマンドそのものを表示し、エディターでコンテキスト長を選べるようになった
  - MCP: `-i` のプロンプト・起動プロンプト・復元したスケジュールは、信頼で起動した MCP サーバーを最大30秒待つ。組織管理の MCP サーバーの警告は起動時の要約にまとまる
  - 追加: Copilot が起動する全プロセスに環境変数を渡す `env` 設定。pre-release は `v1.0.116-5`（11/25）まで刻まれた
  - https://github.com/github/copilot-cli/releases
- [据え置き] **GitHub changelog の Copilot ラベル** — `github.blog/changelog` の Copilot ラベルは 11/18 から動いていない（Master）

### Copilot Studio / Power Platform

- [仕様] **M365 管理センターでの Copilot Studio のコスト管理** — TC の Copilot Studio ブログ（11/24）によると、管理者は M365 管理センター（MAC）で、エージェント単位・環境単位のスペンディングポリシーを Copilot Studio に掛けられる（パブリックプレビュー）。ポリシーの上限は前払いと従量課金の両方に効き、MAC のポリシーを作った環境では PPAC の割り当てだけで上限を管理する前提が成り立たない（Copilot）
  - ロール: Power Platform / Dynamics 365 の管理者は、ポリシーの設定に AI 管理者ロールが要る。自動では付与されない。環境管理者が使用量を見るには AI 閲覧者ロールが要る
  - 優先順位: 対象の使用量では MAC が PPAC より優先される。エージェントのリソース／環境ポリシーが ID ポリシーより先に効き、2つの予算は合算されない
  - 移行: ポリシーを作って環境をリンクするまで何も変わらない。環境単位の割り当て、エージェントの上限、Draw from tenant credit pool のルールは PPAC に残る
  - 提供状態: 本記事はパブリックプレビュー、MC1530368 は 11/20 GA、Roadmap 577834 は `In development` で、一次どうしが一致しない。ユーザー・グループ単位の予算は「近日提供」、推奨上限などは2027年初めの計画
  - https://techcommunity.microsoft.com/t5/copilot-studio-blog/how-to-manage-costs-for-copilot-studio-agents/ba-p/4576413
- [料金] **課金レート表の改訂** — Microsoft が `requirements-messages-management`（11/25 01:03Z `ed8d14af`、`ms.date` 10/30 → 11/24）を改訂した。本文は、フローを開始しなかったポーリングトリガーの評価失敗もエージェントフローの1アクションと同じ料金（100アクションで 13 クレジット）で課金すると書いている。前回の本文を残していないため、今回加わった記述かは特定できない（Copilot）
  - https://learn.microsoft.com/en-us/microsoft-copilot-studio/requirements-messages-management
- [観測] **標準ハーネスのモデル表の改訂** — Microsoft が `authoring-select-agent-model`（11/25 01:03Z `c6619e9c`）を改訂したが、既定は GPT Chat Latest のままで、GPT-4.1・GPT-5 Chat は可用性表に GA のまま残っている。どの記述が変わったかは特定できない（Copilot）
  - https://learn.microsoft.com/en-us/microsoft-copilot-studio/authoring-select-agent-model
- [予定] **PPAC のインベントリのデータエクスポートの停止** — Microsoft が MC1567221（11/24）で、非推奨一覧と同じく 12/1 にインベントリのエクスポートを止めると告知した。使用量と環境のエクスポートは当面続き、エクスポート済みのデータはデータレイクに残る（Copilot）
  - https://mc.merill.net/message/MC1567221
- [据え置き] **Copilot Studio と Power Platform のその他の一次** — Copilot Studio What's New（`1e58d09d`）、ハーネスと課金のページ、PPAC 容量管理（`93396aaf`）、ガイダンスハブ（`fb3f2a93`）、非推奨一覧（`a406dde7`）、Released Versions（2026.6.3）は前日のまま変化がない（Copilot）
  - https://learn.microsoft.com/en-us/microsoft-copilot-studio/whats-new

### Microsoft 365 Copilot

- **SPFx の app-only 権限の追加**（ハイライト1参照）
- [予定] **Copilot のタスクバー固定の通知** — Microsoft が MC1567263（11/24）で、Intune 管理者が選んだグループに Copilot をタスクバー固定するとき、Open Copilot ボタン付きの1回限りの通知を組織メッセージで送れるようになると告知した。既定では無効で、展開は11月下旬から12月下旬までである（Copilot）
  - https://mc.merill.net/message/MC1567263
- [予定] **Viva Insights の GitHub Copilot 指標の既定オンの延期** — Microsoft が MC1523085（11/24 更新）で、GitHub Copilot 指標を Consumption ダッシュボードに既定表示する展開を11月中旬開始から12月中旬開始（完了は2027年1月中旬）に延ばした。オプトイン設定は削除され、管理者は表示を止められなくなる（Copilot）
  - https://mc.merill.net/message/MC1523085
- [新機能+予定] **Clipchamp のプロンプトからの動画作成の Video Hub への移行** — Microsoft が MC1566260（11/24）で、利用者が Video Hub でプロンプトから動画を作れるようにした。2027年2月末までに新しい体験に置き換わり、既存のプロジェクトと MP4 は OneDrive / SharePoint に残る（Copilot）
  - https://mc.merill.net/message/MC1566260
- [観測] **Roadmap の新規バッチ** — Release Communications の API と RSS は 2,411 項目を返し、前日の 2,401 から10件増えた。11/25 00:10Z のバッチ14件は Teams・SharePoint・Dynamics 365 が中心で、Copilot と Copilot Studio の起票は無い（Copilot）
  - https://www.microsoft.com/releasecommunications/api/v1/m365
- [据え置き] **Release Notes・Purview・Cowork・Partner Center** — M365 Copilot Release Notes（先頭 November 17）、Purview・拡張機能・Cowork の What's New は前日のまま変化がない。Partner Center 11月ページは `21bbee60` に改訂されたが、加わった項目は Copilot のライセンス条件に触れない（Copilot）
  - https://learn.microsoft.com/en-us/partner-center/announcements/2026-november

### Google

- [仕様] **Workspace の MCP サーバーの無料枠** — Publickey（11/26）によると、11/24 に GA した Workspace の MCP サーバーと CLI の無料枠は製品ごとに1日 5,000 リクエストで、送信や共有の前に人の確認を挟む。GA と 2027-02-01 の MCP 移行の強制は前日のサマリーに収録済みで、この数値は一次で確認していない（industry）
  - https://www.publickey1.jp/blog/26/google_workspace_mcpgoogle_workspace_cli.html
- [観測] **Gemini API changelog と `developers.google.com` に届かない** — Gemini API changelog は転送先 `aistudio.google.com` に届かないままで、`developers.google.com` も新たにゲートウェイ拒否になった。Workspace Updates（11/24）と Gemini アプリ（11/19）は動いていない（Master・industry）

### 開発ツール・エージェント

- [版更新] **Orca `v1.4.274`** — Stably AI が 11/24 に出し、新規利用者は App Rail（アイコンのナビゲーション）が既定オンになった。対応エージェントの追加と破壊的変更は無い（Master）
  - https://github.com/stablyai/orca/releases
- [据え置き] **Cursor・xAI・Devin・TypeSafe AI・MCP・Hugging Face・Obsidian・Apple** — Cursor の changelog（11/6）とフォーラム（10/12）、xAI（11/19・grok-4.7）、Devin（11/23）、TypeSafe AI（9件）、MCP blog（11/24）、Obsidian（1.15.1）、Apple Developer News（11/18）は動いていない。Hugging Face の8 org にも新しいリポジトリは無い（Master・industry）

### 市場・企業

- [動向] **Anthropic の「Working with AI」** — Anthropic の Economics チームが 11/23、米国のエンタープライズ顧客58社への66件の聞き取りをまとめた。約300件の導入の多くはコスト削減ではなく産出の増加で価値を出し、約3分の2の企業が AI を理由に採用を減らした（Master・industry）
  - The Decoder の集計: 55% が生産量か品質を上げ、19% はまだ事業価値を出していない。障害は出力の量が人の確認能力を超えること（49）、従業員の抵抗（43）、専門家のレビューと試験（42）の順
  - 社内ツール100件の80%は手作業の自動化、20%は既存ソフトの置き換え。AI ネイティブのスタートアップ6社は、AI が無ければ約4倍の人員が要ると見積もった。標本は無作為ではない
  - https://www.anthropic.com/research/working-with-ai
- [動向] **Anthropic の株価** — Reuters が 11/25 の見出しで、AI 株の売りが広がり Anthropic が公開価格 $83 を下回る $74 まで下げたと報じた。見出しのみで、本文と正確な終値は確認していない（industry）
- [動向] **TOPIX100 の生成AI運用** — aiagent-navi.com が公開資料（2023年10月〜2026年11月）を集計し、TOPIX100 のうち66社が生成AIを本番運用し、AI エージェントの本番運用は6社（試験中・計画中を含め26社）だったとした。第三者機関の調査ではない（industry）
  - https://aiagent-navi.com/?p=26591
- [据え置き] **Nvidia × Inception、Nvidia × Reflection AI** — 2件の買収協議に続報はない。MM総研と IDC Japan の新しい公表も見つからなかった（industry）

## 直近の注目予定

- **11月下旬**: Copilot ライセンスの無い利用者の検索画面が新しくなる（MC1562275）。Copilot Code のローカル Sandbox が既定でオンになる（MC1519871）。Copilot のタスクバー固定の通知の展開が始まる（MC1567263）
- **11月中**: GitHub の cloud sandbox の課金が始まる（日付は明記なし）
- **11/29**: OpenAI が Daybreak Blue のセッションデータの学習利用を始める（二次）
- **11/30**: `claude-sonnet-4-5-20250929` が退役し、Opus 4.8 の fast mode が削除される。OpenAI の `/v1/prompts`・Evals・Agent Builder が停止する。Power Automate デザイナーの Copilot と Copilot Studio の Mistral Medium 3.5 が退役する。GPT-5.6 Sol の期間限定価格と Gemini 4 Argon・Carbon の導入価格が終わる。この日以降の Claude Code で managed マーケットプレイスの自動更新が既定でオンになる。Link to Fabric の Update connection が全リージョンに行き渡る
- **12/1**: GitHub の使用量レポートに `user_id` 列が加わる。PPAC のデータエクスポートがインベントリを出力しなくなる（MC1567221）。OpenAI `gpt-image-1-mini` / `gpt-image-1.5` / `chatgpt-image-latest` が停止する。Gemini 4 Argon・Carbon の単価が $4/$20 に倍増する。Copilot Studio のワークフローの Code ノードが GA になる
- **12/2**: GitHub が公開リポジトリの `pull_request_target` を既定でブロックする。Power Platform のプロンプトから Anthropic・Grok・旧 GPT 系が退役する（MC1536101）
- **12/3**: Agent ノードからのファイル生成が GA になる（MC1561859）
- **12月上旬**: Teams のチャネル単位の Copilot がパブリックプレビューに入る（MC1562277）。Mac の PowerPoint の Copilot のプラグインの展開が終わる（MC1556095）
- **12/8**: GitHub が活動の無いリポジトリの Dependabot アラートを停止し、ARM32 ジョブのサポートを終える。Dataverse のエージェントユーザーが GA、M365 Copilot in Power BI が既定でオンになる
- **12/9**: EU / EFTA / UK で Claude モデルが既定で有効になる（MC1546438）
- **12/11**: OpenAI `gpt-5` 系 / `o3` / `o3-pro` が停止する。ChatGPT の Advanced / Standard 音声モードが退役する（二次）
- **12/14**: Copilot から Claude Fable 5 / Haiku 4.5 / Gemini 3.8 Flash / Gemini 4 Argon / Grok 4.6 / Kimi K3 が廃止される。claude.ai/design の単体サイトが閉鎖する
- **12/15**: アンマネージドの開発者環境の削除が始まる（MC1515303）
- **12月中旬**: Copilot デスクトップアプリと Edge の同期が展開される（MC1562269）。Chat と Office のモデルの従量課金が GA になる（MC1557754）。Viva Insights の GitHub Copilot 指標の既定オンが始まる（MC1523085）
- **12月中**: ChatGPT と Codex の利用枠が Plus・Pro・Business で1つの予算に統合される（二次）
- **12/17**: Copilot Studio のワークフローのサービスプリンシパル認証が GA になる（MC1557509）
- **12/18**: Copilot から MAI-Code-1.1-Flash が廃止される
- **12月下旬**: Copilot のタスクバー固定の通知の展開が終わる（MC1567263）
- **12/31**: Copilot の Fable 5 系の ZDR 例外が終わる（以後は EFS が必要）。Claude Security の無償クレジットの対象期間が終わる。OpenAI の医療向けモデル構成の期間限定価格が最短でこの日に終わる。MCP の File Uploads 拡張を安定版にする目標
- **2027-01-01**: Anthropic の新しい開示期限（高・重大度30日）が、この日以降の報告に適用される。ChatGPT Sites の利用量がアプリに表示される
- **2027-01-03**: Copilot デスクトップアプリのアプリ内ブラウズの既定オンに備える期限（MC1560922）
- **2027-01-06**: OpenAI `tts-1` / `tts-1-hd` / `gpt-4o-mini-tts` が停止し、セルフサービスの fine-tuning ジョブ作成が制限される
- **2027-01-11**: OpenAI の EU データレジデンシーで GPT-5.2 / 5.4 / 5.4 mini の `fast` / `priority` 処理が停止する
- **2027-01-14**: OpenAI `gpt-4o` / `gpt-4o-mini` / `gpt-4.1` / `gpt-4.1-mini` が停止する
- **2027-01-15**: アンマネージドの開発者環境が完全に削除される。Claude Code Review / Claude Ship の Enterprise 向けクレジットの請求期限
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
- **2027-04-01**: Google Workspace API の Scaled 枠の課金が始まる（標準枠超過のプロジェクトは指定しないと上限が戻る）。OpenAI `gpt-5.1` / `gpt-5.3-codex` / `gpt-5.4-nano` が停止する
- **2027-05-17**: GitHub Copilot の MAI Code 2・MAI Code 2 Flash の導入価格が終わり、単価が倍になる
- **2027-09-15**: Dataverse for Teams 環境の削除が始まる（MC1515294）

## 改善メモ

- Master: 新規提案・障害の変化なし。継続提案の最多は B-088（Gemini API changelog の URL 差し替え、23回目）。11-25 に artifact のアプリ化（11/24）と `/research` の「Working with AI」（11/23）を取りこぼしたため、本サマリーでも本日はじめて載った
- Copilot: 新規提案・障害の変化なし。継続提案 5件（最多: B-080 Cowork の Learn URL の移設、28回目）
- industry: `developers.google.com` がゲートウェイ拒否（新規）。継続提案 7件（最多: B-048 Gemini 一次 URL、24回目）。見送り候補 B-036
- ソース間の差: Claude Code `2.1.332` の日付を Master は 11/24、industry は 11/25 とした。npm の公開は 2026-11-24T22:06Z（JST 11/25 07:06）で、UTC と JST のどちらで数えたかの違いである。本サマリーはハイライトに公開時刻を併記した
- ソース間の差: Private Inference を industry は `[新機能]` としたが、最初の企業顧客での試験で一般提供の時期が無いため、本サマリーは `[予定]` を採った
- ソース間の差: Workspace の MCP サーバーの GA は前日のサマリーに収録済みのため、本日は industry が加えた無料枠の数値だけを `[仕様]` で載せた
- ソース間の差: GPT-6 系のタンパク質設計を Master は `[動向]` で載せ、industry は採録を見送った。本サマリーは Master に合わせて載せた
