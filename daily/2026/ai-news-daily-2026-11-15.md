# AI News Daily Summary — 2026-11-15

GitHub は 12/14 に Copilot から Claude Fable 5・Gemini 4 Argon など6モデルを外し、11/16 の3モデルと合わせて1か月で9モデルが入れ替わる。Power Apps のアプリ説明の AI 生成と共同編集の在席表示は 11/30 に終わる。Claude Code 2.1.325 はサンドボックス内の Bash を権限確認の対象に戻し、無人実行が確認待ちで止まりうるようになった。

## 今日のハイライト

### 1. [廃止] GitHub が Copilot から Claude Fable 5・Gemini 4 Argon など6モデルを 12/14 に廃止すると告知した — 11/16 の3モデル廃止に続き、Copilot で選べるモデルが1か月で9つ入れ替わる

**要点**: GitHub が 11/13、Copilot の全機能から6モデルを **12/14** に外すと告げた。Gemini 4 Argon は 10/13 の GA から2か月で外れ、12/1 の倍額化に続いて Copilot でも使えなくなる。廃止モデルを名指しした構成は、後継への書き換えが値上げ対策から必須作業に変わった。

**詳細**: GitHub changelog（11/13）で一次確認した（Master・industry）。
- 廃止するモデルと後継（6件）:
  - Claude Fable 5 → Claude Fable 5.2
  - Claude Haiku 4.5 → Claude Haiku 5.5（年額プランの個人契約者には残す）
  - Gemini 3.8 Flash → Gemini 4 Hydrogen
  - Gemini 4 Argon → Gemini 4 Carbon
  - Grok 4.6 → Grok 4.7
  - Kimi K3 → 未定
- 対象機能: Copilot Chat、インライン編集、ask・agent モード、コード補完
- 管理者の作業: Business / Enterprise は既定のモデル有効化がオンなら後継が自動で有効になる。全体の既定をオフにしている組織は、モデルポリシーで後継を有効にしないとモデル選択に出ない
- 前段: 11/16 には Claude Opus 4.8 / Opus 5 / GPT-5.6 Terra が Copilot から外れる（既報）

出典:
- https://github.blog/changelog/2026-11-13-upcoming-deprecation-of-selected-github-copilot-models-in-december

### 2. [廃止] Power Apps のアプリ説明の AI 生成と、共同編集中の在席表示が 11/30 に終わる — 残り15日の期日が、非推奨一覧に予告なしで4件加わった

**要点**: 発行ダイアログとアプリデザイナーの「Create descriptions using AI」が、モデル駆動アプリとキャンバスアプリの両方で 11/30 に消える。Plans とモデル駆動アプリのレコードの在席表示も同日に終わり、Plans の複数作成者による同時編集はサポート対象外になる。

**詳細**: Power Platform の非推奨一覧が 11/14 01:06Z に `602fb731` へ改訂され、`## ` 見出しが4本増えた（`ms.date` は 11/2 のまま）。対応する Message Center の通知は確認できていない（Copilot）。
- AI-generated descriptions（モデル駆動・キャンバス）: 既存の説明は残り、手で書き直せる。代わりの手段として model app-builder スキルと外部の AI コード生成ツールが案内されている
- Plans の在席表示: 一度に1人だけが Plan を編集するよう、Plan の外で調整する必要がある
- モデル駆動アプリのレコード単位の在席表示: 同じレコードを開いている人の表示とプレゼンスカードが消える。レコードの共有と、グリッド・検索の写真・状態表示は変わらない

出典:
- https://learn.microsoft.com/en-us/power-platform/important-changes-coming

### 3. [破壊的変更+セキュリティ] Claude Code 2.1.325 がサンドボックス内の Bash を既定で権限確認の対象に戻した — サンドボックスがあれば確認なしで動いていた無人実行やスケジュールタスクが、確認待ちで止まることがある

**要点**: Anthropic が 11/13 に Claude Code 2.1.325 を出した。サンドボックス内の Bash は通常の権限確認を通り、スケジュールタスクと `/loop` は `allowed-tools` か hooks を持つスキルの実行前に確認を取る。サンドボックスの存在を、確認なしで動かせる前提にできなくなった。

**詳細**: Claude Code changelog で一次確認した（Master・industry）。
- 元に戻す設定:
  - サンドボックス: `sandbox.autoAllowBashIfSandboxed: true`。管理設定でサンドボックスを有効にしている組織は、最上位の管理ソースに置く
  - スケジュールタスク / `/loop`: スキルを無人で動かすには `permissions.allow` に `Skill(name)` を足す
  - 読み取り専用の git: プロジェクト外の信頼していないリポジトリでは確認を取る。確認なしにするには `additionalDirectories` 設定ではなく `--add-dir` で指定する
- ほかの挙動変更: Desktop・IDE・SDK の「Always allow」は、ルールを保存して同じコマンドが再び許可される場合だけ出す。`ALL_PROXY` しか設定していないとプラグインのダウンロードは CONNECT トンネルを使い、CONNECT を拒むプロキシでは失敗する。管理設定の `pluginDigests` は deprecated になり無視される
- セキュリティ修正: zstd 圧縮レスポンスのデコード、Bash の権限チェックの穴（一部の複合コマンドが確認なしで動いた・allow ルールが別のプログラムを動かしえた）、Bedrock のトークン計数が `allowedProviders` に反して会話を送っていた問題
- その他の修正: サードパーティのゲートウェイや Foundry で毎ターン context length エラーになる問題（2.1.323 の 1M 既定化の副作用）を直した
- 版: npm は `{stable: 2.1.311, latest: 2.1.325, next: 2.1.325}`。changelog は 2.1.323 の次が 2.1.325 で、2.1.324（11/13）は載っていない

出典:
- https://code.claude.com/docs/en/changelog
- https://registry.npmjs.org/@anthropic-ai/claude-code

## カテゴリ別まとめ

### Anthropic / Claude

- **Claude Code 2.1.325**（ハイライト3参照）
- [仕様] **Opus 5.5 のプロンプトの書き方** — The Decoder（11/14）によると、Anthropic が Claude Opus 5.5 向けに「think hard」などの推論指示は不要だと案内し、指示を外すと品質を落とさずに応答の開始が速くなったとした。社内テストでは Medium の Opus 5.5 が High の Opus 5 と同等で、Sonnet を Extra High・Max で動かすと Opus 5.5 とほぼ同じ費用になるという。料金の変更は無い（industry）
  - https://the-decoder.com/anthropic-says-outdated-prompting-habits-are-slowing-down-claude-opus-5-5/
- [動向] **常時動くエージェントの設計記事** — Anthropic が 11/13、常時動くエージェントの設計を解説する記事を出した。新機能や料金の発表ではなく、auto memory・auto mode・MCP Apps の承認カード・hooks による実行の保留を組み合わせる手順をまとめている（Master）
  - https://claude.com/resources/articles/building-always-on-agents
- [据え置き] **Claude Platform と Anthropic の他の一次** — Claude Platform の release notes は 11/12（self-hosted Managed Agents）が最上位のままで、モデル退役一覧の Active も17件で変わらない。廃止履歴は 9/30 のままで、Opus 4.5 の下限 11/24 の告知も無い。`/news`（11/10）、`/research`（11/13）、`support.claude.com`（11/12）、Privacy Center も動いていない（Master・industry）
  - https://platform.claude.com/docs/en/about-claude/model-deprecations

### GitHub Copilot / Microsoft 開発ツール

- **Copilot の 12/14 の6モデル廃止**（ハイライト1参照）
- [据え置き] **Gemini 4 Hydrogen の Copilot GA は既報** — GitHub が 11/13、Gemini 4 Hydrogen を Copilot の Pro・Pro+・Max・Business・Enterprise で GA にした。11/14 分で既報で、本日 Master も収録した。課金は提供元の定価による従量課金で、管理者はモデルポリシーで止められる（Master）
  - https://github.blog/changelog/2026-11-13-gemini-4-hydrogen-in-github-copilot
- [仕様] **Copilot CLI v1.0.112** — GitHub が 11/13 の安定版 `v1.0.112` で、組織のポリシーで MCP サーバーを止めると組み込みの GitHub MCP サーバーも使えないようにした。`--additional-mcp-config` で渡したサーバーは `copilot mcp remove` / `/mcp delete` で消せず、理由を表示する（Master）
  - `/model plan` は余分な引数を受け付けなくなった。サブエージェントもセッションの AI クレジット上限に従う。ほかは表示崩れと貼り付けの修正が大半
  - https://github.com/github/copilot-cli/releases

### Microsoft 365 Copilot

- [仕様] **Copilot Pages と Notebooks の保存先が OneDrive に** — 利用者が Copilot Chat・M365 Copilot アプリ・Copilot Notebooks で新しく作る Pages と Notebooks の成果物は、利用者の OneDrive for Business に保存されるようになる（MC1449182・8/6 公開・11/13 に日程更新）。既存のファイルは移らず、Purview の保持・DLP・ライフサイクル管理が OneDrive の他のファイルと同じ扱いで掛かる（Copilot）
  - 展開: 全世界は10月中旬〜11月下旬、GCC / GCC High / DoD は11月中旬〜12月中旬
  - https://mc.merill.net/message/MC1449182
- [新機能] **What's New in Microsoft Copilot 10月号** — Microsoft が 11/13、TC に月次のまとめを公開した。既報を除くと次の項目が初出になる（Copilot）
  - Word: Markdown のショートカットを使え、Web 版で .md と .docx を相互変換できる（10月展開）。20以上の法務スキルを持つ legal プラグインも入った
  - Teams: 文字起こしを保存せずにインテリジェント要約を使う設定が10月に全世界へ展開された
  - Excel: 会計スキル（照合・仕訳・財務分析）は11月に全世界へ広がる。データクリーニングのスキルは10月に展開された
  - PowerPoint: スキルの記録、インタラクティブなスライド、Brand Kit の公開・非公開の操作が10月に展開された
  - https://techcommunity.microsoft.com/t5/microsoft-copilot-blog/what-s-new-in-microsoft-copilot-october-2026/ba-p/4568528
- [廃止] **PDF のスマート目次を取りやめ** — Microsoft が、OneDrive と SharePoint の Web 版 PDF ビューアーで目次のない PDF に Copilot が目次を作る機能の提供を取りやめた（MC1486295・11/13 更新）。Targeted Release と GA（全世界・GCC・GCCH・DoD）の両方を取り消した（Copilot）
  - https://mc.merill.net/message/MC1486295
- [予定] **Workforce Intelligence プラグイン** — Frontier テナントのリーダーと管理職は、Cowork で組織構造・人員構成・スキルを自然言語で調べられるようになる（MC1552389・11/13）。パブリックプレビューは 11/16 に始まり、管理者による Workforce Insights の構成とプラグインの公開が前提になる（Copilot）
  - https://mc.merill.net/message/MC1552389
- [予定] **Copilot デスクトップアプリのタブ参照** — 利用者は、組み込みブラウザーで開いているタブの内容について Copilot に質問・要約を頼めるようになる（MC1552386・11/13）。参照は現在の会話に限られ、展開は11月中旬〜下旬（Copilot）
  - https://mc.merill.net/message/MC1552386
- [予定] **Teams モバイルの Queues アプリの Copilot** — 通話担当者とスーパーバイザーは、モバイルの共有通話履歴から録音済みの通話について Copilot に質問できるようになる（MC1552391・11/13）。Teams Premium と M365 Copilot の両ライセンスが要り、GA は12月上旬〜中旬（Copilot）
  - https://mc.merill.net/message/MC1552391
- [予定] **Chat からのモード切り替え提案の日程** — Microsoft が 11/4 に既報の提案カードについて、Standard の展開を11月中旬〜下旬、Deferred の展開を12月中旬〜下旬と明記した（MC1536065・11/13 更新）（Copilot）
  - https://mc.merill.net/message/MC1536065
- [据え置き] **その他の M365 Copilot** — Release Notes（先頭 November 4）、Cowork What's New、`cowork-models`・`cowork-admin-governance`、前提条件3本は改訂されていない。拡張機能 What's New は 11/13 に `aac3cc6c` へ改訂されたが、節の構成と項目は変わらない。Fable 5.2 は本日もモデル表に載っていない（Copilot）
  - https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/whats-new

### Copilot Studio / Power Platform / ライセンス

- **Power Apps の4機能の 11/30 終了**（ハイライト2参照）
- [新機能] **ワークフローのクレジット消費の可視化** — Copilot Studio の作成者は、ワークフローデザイナーの実行の詳細と Monitor タブで、Copilot Credits の推定消費を実行単位・ステップ単位で確かめられるようになった（MC1552503・11/14 公開・11/11 GA）。上限が近づくと警告バナーが出て、クレジットが尽きるとテスト実行がブロックされる（Copilot）
  - https://mc.merill.net/message/MC1552503
- [廃止] **Release Planner が本日退役** — Microsoft が 11/15 に Release Planner を退役させ、Dynamics 365・Power Platform・Copilot Studio のロードマップは AI at Work roadmap だけで追う形になった（MC1461529・11/14 更新）。年2回の Release Wave の告知もやめ、製品の提供状況は新しい Learn ページで確認する（Copilot）
  - https://mc.merill.net/message/MC1461529
  - https://learn.microsoft.com/dynamics365/get-started/product-availability
- [据え置き] **Copilot Studio・Power Platform の Learn と Partner Center** — Copilot Studio What's New・課金・モデル表3本・ガイダンスハブ・PPAC の容量管理は 11/12 の一括改訂から動いていない。Released Versions は 2026.6.3 のまま137日たつ。Partner Center 11月ページ（`056e5a49`）と Purview What's New にも新しい項目は無い（Copilot）
  - https://learn.microsoft.com/en-us/microsoft-copilot-studio/whats-new

### OpenAI / Codex / ChatGPT

- [版更新] **Codex CLI 0.171.0-alpha.5** — OpenAI の Codex CLI は安定版が `0.169.0`（11/13）のままで、pre-release が `0.171.0-alpha.5`（11/14）まで進んだ。alpha の本文は版番号だけである（Master）
  - https://github.com/openai/codex/releases
- [据え置き] **OpenAI の他の一次** — ChatGPT & Codex changelog（11/13）、API changelog（11/5 `gpt-6-cyber`）、deprecations（11/10 GPT Image 2）、Deployment Safety Hub（11/5）、community Announcements（11/10）、misalignment reports（11/12）は動いていない（Master・industry）
  - https://developers.openai.com/api/docs/deprecations

### Google

- [動向] **Gemini 4 Carbon が MathArena で首位** — The Decoder（11/14）によると、Gemini 4 Carbon（high）が MathArena で 85.4% を取り首位に立ったが、費用は GPT-6.1 Sol の約15倍だった。Claude Fable 5.2（max）は 82.8%・$40.20、GPT-6.1 Sol（max）は 80.6%・$1.07、Carbon は $15.70 で、費用の単位は記事に書かれていない（industry）
  - https://the-decoder.com/gemini-4-carbon-takes-the-matharena-crown-but-costs-15-times-more-than-gpt-6-1-sol/
- [観測] **Gemini API の一次に届かない** — Gemini API changelog の転送先に本日も届かず、検索で見える最新は 10/27 で Hydrogen の項目は確認できない。Gemini アプリの release notes（2026.10.13）、Workspace Updates（11/13）、The Keyword（11/12）は最上位が変わらない（Master）
  - https://ai.google.dev/gemini-api/docs/changelog

### Cursor / 開発ツール / エージェント

- [破壊的変更+新機能] **Devin のファイル編集が手動保存に** — Cognition が Devin の 11/13 版で、セッションのファイル編集を自動保存から Cmd/Ctrl+S での保存に変えた。未保存のタブには印が付き、保存したファイルは Devin に伝わる（Master）
  - 画面: 作業タブは自動で開かなくなり、PR・差分・プレビューなどの成果物はチャット右のレールに並ぶ。Agent / Ask の切り替えは入力欄のドロップダウンへ移った
  - Devin Review: GitLab のマージトレインに MR を追加でき、Analytics > Review で指摘の行方をカスタムレビューアごとに見られる
  - https://docs.devin.ai/release-notes/overview
- [据え置き] **Cursor・xAI・Orca・TypeSafe AI・MCP・Hugging Face** — Cursor の changelog（11/6）とフォーラム（10/12）、xAI（grok-4.7）、Orca（`v1.4.258`）、TypeSafe AI（`jev-1.14.0`）、MCP blog（11/11）は動いておらず、Hugging Face の8 org に新しいリポジトリは無い。Obsidian と Apple Developer News も動いていない（Master・industry）
  - https://github.com/stablyai/orca/releases

### 業界・市場

- [動向] **Anthropic の支払い義務が約 $9,010億** — The Decoder（11/14）が提出書類をもとに、Anthropic の契約上の支払い義務が約 $9,010億に達し、うち約 $710億が 2027年9月までに期限を迎えると伝えた。大半は計算資源とチップの契約で、年換算売上は10月末に $810億（9月末から $100億増）。価格決定は 11/18、取引開始は 11/19 の予定で、仮条件の変更は報じられていない（industry）
  - https://the-decoder.com/anthropic-ceo-amodei-admits-theres-a-huge-uncertainty-in-whats-going-to-happen-next-year-days-before-a-record-ipo/
- [据え置き] **未決の買収協議と国内調査** — Amazon × Decart、Nvidia × Reflection AI の協議に続報はなく、Nvidia の後任 CEO も決まっていない。IDC Japan・MM総研・NRC の新しい公表も無い（industry）

### 日本語コミュニティ

- [据え置き] **Qiita / Zenn** — Agent Builder と Copilot Studio のハーネス3種を比べる定点観測の記事（Qiita・11/14）が出たが、一次の既報の範囲として Copilot ソースが掲載を見送った（Copilot）

## 直近の注目予定

- **11/15（本日）**: Release Planner が退役（MC1461529） ／ Dataverse for Teams 環境とアンマネージド開発者環境の新規作成が停止 ／ Copilot Studio のカスタム採点器ライブラリが GA（MC1531932）
- **11/16**: Copilot から Claude Opus 4.8 / Opus 5 / GPT-5.6 Terra を廃止 ／ Teams の旧 GitHub アプリが退役 ／ `pull_request_target` の2回目の試験ブロック ／ Claude Opus 4.6・Opus 4.5・Sonnet 4.5・Haiku 4.5 に透かし ／ Fable 5.2 ローンチ特典の Pro・Team 標準席の枠が 23:59 PT に終了 ／ Cowork / Autopilot の Engage プラグインが GA（MC1530609） ／ Workforce Intelligence プラグインが Frontier でプレビュー（MC1552389） ／ PPAC のフィードバックフォームの既定ポリシーが GA（MC1545686）
- **11月中**: GitHub の cloud sandbox の課金が開始（日付は明記なし）
- **11月中旬**: Copilot デスクトップアプリのタブ参照と、Chat からのモード切り替え提案（Standard）の展開が開始（MC1552386・MC1536065） ／ 単体の Word / Excel / PowerPoint エージェントの撤去が開始（MC1536062）
- **11/17**: Gemini API の Live / TTS preview モデルが停止（4〜5種・一次未確認） ／ Gems が Gemini アプリの設定パネルへ移動 ／ Plugin Catalog が公開 ／ Intelligent call delegation が従量課金のパブリックプレビュー（MC1537490） ／ Claude for Manufacturing の技術ウェビナー
- **11/17〜20**: Microsoft Ignite
- **11/18**: Anthropic の IPO 価格決定（11/19 取引開始の見込み・報道） ／ MODS の Workforce Insights エンドポイントが退役（MC1542066）
- **11/19**: Claude Enterprise で Claude Data が既定でオン
- **11/20**: Copilot Studio のコスト管理を M365 管理センターへ移す機能が GA（MC1530368） ／ Conductor のクラウド版が終了（二次）
- **11/24 以降**: `claude-opus-4-5-20251101` の暫定退役日（確定日ではない）
- **11月下旬**: 新しい Copilot Pages と Notebooks の OneDrive 保存の展開が全世界で完了（MC1449182） ／ Teams モバイルの Queues アプリの Copilot が Targeted Release（MC1552391）
- **11/29**: OpenAI が Daybreak Blue のセッションデータの学習利用を開始（二次）
- **11/30**: `claude-sonnet-4-5-20250929` が退役 ／ Opus 4.8 の fast mode を削除 ／ OpenAI の Evals・`v1/prompts`・Agent Builder が停止 ／ Gemini 4 Argon の導入価格が終了 ／ **Power Apps のアプリ説明の AI 生成と、Plans・モデル駆動アプリの在席表示が終了** ／ App Builder のアプリが開けなくなる ／ vibe.powerapps.com・Describe it to design it・Power Automate デザイナーの Copilot が終了
- **12/1**: Gemini 4 Argon の単価が $4 / $20 に倍増 ／ Google スライドの複数スライド作成の上限引き上げ優待が終了しうる
- **12/2**: GitHub が公開リポジトリの `pull_request_target` を既定でブロック ／ Power Platform のプロンプトから Anthropic・Grok・旧 GPT 系モデルが退役（MC1536101）
- **12/7**: Purview DSPM のパートナー連携の一部が退役（MC1545691）
- **12/8**: GitHub Actions のホステッドランナーで ARM32 ジョブのサポートが終了 ／ 1年活動のないリポジトリの Dependabot アラートを停止 ／ M365 Copilot in Power BI が既定でオン（MC1546429）
- **12/9**: EU / EFTA で Claude モデルが既定で有効になり、「M365 アプリの Copilot だけで許可」が退役（MC1546438）
- **12/11**: Power Apps の式の生成・Power Apps Ideas などが退役（MC1532421・MC1532426）
- **12月中**: ChatGPT と Codex の利用枠が Plus・Pro・Business で1つの予算に統合（二次）
- **12/14**: **Copilot から Claude Fable 5 / Haiku 4.5 / Gemini 3.8 Flash / Gemini 4 Argon / Grok 4.6 / Kimi K3 を廃止** ／ claude.ai/design の単体サイトが閉鎖
- **12月中旬**: GCC 系で新しい Copilot Pages の OneDrive 保存の展開が完了（MC1449182） ／ Chat からのモード切り替え提案が Deferred に到達（MC1536065） ／ Outlook モバイルの Copilot Chat の刷新が開始（MC1551148）
- **12/31**: Power Platform 版のスケジュール済みプロンプトが退役（MC1550533） ／ Copilot の Fable 系の ZDR 例外が終了 ／ Claude Security の無償クレジットの対象期間が終了 ／ Copilot Studio の会話内での接続設定が GA（MC1548034） ／ MCP の File Uploads 拡張を安定版にする目標
- **2027-01-01**: Microsoft Commercial Cloud の現地通貨価格が5通貨で改定（日本円は対象外）
- **2027-01-06**: OpenAI `tts-1` / `tts-1-hd` / `gpt-4o-mini-tts` 2版が停止
- **2027-01-14**: OpenAI `gpt-4o` 2版 / `gpt-4o-mini` / `gpt-4.1` / `gpt-4.1-mini` が停止
- **2027-01-15**: Claude Code Review の Enterprise 向けクレジット請求期限
- **2027年1月中旬**: Power BI の単体の Copilot が退役（MC1546429）
- **2027年1月末**: UBB の入口が既定で表示され旧設定が退役（MC1546354） ／ ChatGPT Classic（旧デスクトップアプリ）が終了（1/30・二次）
- **2027-02-01**: OpenAI `gpt-5.5-cyber-preview` が停止
- **2027-02-10**: Claude Meetings の成果物の無料期間が終了 ／ OpenAI `gpt-image-2` / `gpt-image-2-2026-04-21` が停止
- **2027-03-01 以降**: Gems が廃止（Business / Enterprise）
- **2027-03-08**: Fable 5.2 ローンチ特典のリセット（Max / Ultra / premium 席）が失効
- **2027-03-30**: MCP 仕様 `2027-03-30` 版のリリース予定
- **2027-04-01**: SharePoint の tempauth URL が退役し、それに頼る Power Apps / Power Automate が停止（MC1551122・MC1492958） ／ OpenAI `gpt-5.1` / `gpt-5.3-codex` / `gpt-5.4-nano` が停止
- **2027-11-12**: Purview Data Governance のサポート終了

## 改善メモ

- 3ソースとも新規提案・障害の変化なし。継続提案は Master 7件（最多 B-036・B-037、12回目。B-088 も12回目）、industry 7件（最多 B-040、17回目）。見送り候補は Master が B-078・B-043・B-036、industry が B-036
- ソース間の差異: 11/17 に停止する Gemini API の Live / TTS preview を、Master は4モデル（5本目は未確定）、industry は5種とする。どちらも一次未確認のため前日に続き「4〜5種」とした
- 重複の統合: Copilot の 12/14 の6モデル廃止と Claude Code 2.1.325 は Master と industry の両方がハイライトにしていたため、それぞれ1件に寄せた。後継の書き方は Master、対象機能と Argon の値上げとの関係は industry から取った
- Gemini 4 Hydrogen の Copilot GA は 11/14 分で既報のため、Master の本日収録分は短く残した
- 前日（11/14）分に欠損ソースはなく、欠損リカバリは不要
