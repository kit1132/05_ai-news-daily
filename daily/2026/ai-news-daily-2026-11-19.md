# AI News Daily Summary — 2026-11-19

Claude Code 2.1.327 は auto mode の有料分類器フォールバックを次の版で外すと予告した。M365 Copilot は Chat と Office でもライセンス上限の先をクレジット課金で使えるようにし、自動適用の支出ポリシーには何もしなくても入る。GitHub は GPT-6.2 Astra / Sol を Copilot で GA にし、既定の有効化が生きている組織では自動で使える状態になった。

## 今日のハイライト

### 1. [破壊的変更+セキュリティ] Claude Code 2.1.327 が auto mode の有料分類器フォールバックを次の版で外すと予告し、権限確認を厳しくした — 「判定できなければ有料の分類器で通す」前提が、「確認か拒否に落ちる」に変わる

**要点**: Anthropic が Claude Code `2.1.327` を出し、npm の `latest` / `next` にした。auto mode の通知に、課金される分類器へのフォールバックを次の版で外すと書いた。外れると、判定できない操作は承認待ちか拒否になり、無人で回す auto mode は止まる場面が増える。

**詳細**: code.claude.com の changelog で一次確認した（Master・industry）。全体は173項目（[VSCode] の10項目を含む）。
- 権限まわり:
  - auto mode: `Bash(pnpm dlx *)` のように任意のパッケージを走らせる allow ルールと、`/usr/bin/npm run:*` などパスや版を付けた形を無視し、安全性チェックに判定を任せる
  - `permissions.blockReadsOutsideWorkingDirectories`: bypass / auto mode で確認する Bash コマンドが増え、Read / Edit の deny ルール配下のパスを指すコマンドは確認ではなく拒否になる
  - 作業ディレクトリの内側とみなす範囲が変わり、一部のシンボリックリンクはパス検査で拒否する。変数展開で非常に長くなる Bash コマンドも拒否する
  - `ExitWorktree`: 保存していない作業がありそうな worktree を消す前に確認し、答える人がいなければ拒否する
- セキュリティ上の注意: 最初の Bash コマンドを速くするため、承認前にシェルの起動ファイルが走るようになった（拒否しても走る）。止めるには `CLAUDE_CODE_DISABLE_SHELL_HEAD_START=1` を設定する
- 管理設定・組織向け:
  - `attributionProject`: `admin.billing_group_tag` を設定した Claude apps ゲートウェイで、セッションの請求グループに名前を付ける
  - `claude mcp add-json <name> -`: サーバーの JSON を標準入力から読み、トークンをコマンドラインに出さずに済む
  - `/status`: 壊れたエージェント・スキル定義と、効いていないフックを一覧する
- 修正: Remote Control の worktree モードで、サーバー停止時に `.env` など git 管理外のファイルを消していた不具合を直した
- npm: `{stable: 2.1.311, latest: 2.1.327, next: 2.1.327}`。stable は動いていない

出典:
- https://code.claude.com/docs/en/changelog
- https://registry.npmjs.org/@anthropic-ai/claude-code

### 2. [料金] M365 Copilot の Chat と Office でも、ライセンスの上限を超えたらクレジット課金でモデルを使い続けられる — 「新サービスを自動で適用」をオンにした既存の支出ポリシーは、何もしなくても課金の対象になる

**要点**: これまで Copilot Chat と Word / Excel / PowerPoint のモデルはライセンスの上限で止まっていた。今後は支出ポリシーで許可されたユーザーが Copilot Credits を払って同じモデルを使い続けられる。自動適用の設定のポリシーにはこのサービスが自動で入るので、上限で止まる前提の費用見積もりは引き直しになる。

**詳細**: MC1557754（11/17）で確認した（Copilot）。Frontier では展開が始まっており、全世界の GA は2026年12月上旬の予定。
- 上限に達したとき: Auto に切り替えればクレジットを消費せずに続けられる。UBB が有効なユーザーは、選んだモデルのままクレジットを消費して続けられる
- 管理者の設定: 支出ポリシーに新サービス「Models with usage-based billing in Chat and Office」が加わる。「Auto-apply new services」が有効なポリシーには自動で入り、無効なポリシーには管理者が追加する
- 利用者の画面: 塗りつぶしのクレジットアイコンは課金対象、白抜きは対象外を示す。プロンプトに `/cost` と入れるとセッションの消費が見られる
- 関連: MC1483844 の 11/17 更新で、OpenAI をサブプロセッサーとして無効にしたテナントの Cowork でも、Azure 上の GPT-6.1 Sol が GA になり GPT-5.5 を置き換える

出典:
- https://mc.merill.net/message/MC1557754

### 3. [料金+新機能] GitHub が GPT-6.2 Astra / Sol を Copilot で GA にした — Business / Enterprise では既定のモデル有効化が生きていれば自動で使える状態になり、従量課金でそのまま請求される

**要点**: GitHub が 11/17、OpenAI の GPT-6.2 Astra と Sol を Copilot Pro+ / Max / Business / Enterprise で GA にした。どちらも提供元の定価で従量課金される。既定のモデル有効化を切っていない組織では自動で有効になるので、使わせない場合はモデルポリシーで止める必要がある。

**詳細**: GitHub changelog で一次確認した（Master・industry）。
- 対応画面: VS Code・Visual Studio・Copilot CLI・coding agent・Copilot アプリ・github.com・GitHub Mobile・JetBrains・Xcode・Eclipse。段階的に展開する
- GitHub の評価: Astra は GPT-6 Astra より code review で多くの問題を見つけ、少ないトークンでエージェント作業を終えた。Sol は code review で GPT-6.1 Sol の約2倍の実問題を見つけた
- 単価（Standard・100万トークンあたり）: Astra $8 / $40、Sol $2 / $10（API 側は 11/18 既報）
- 有効化の書き方はソースで割れている。Master は「既定の有効化が生きていれば自動」、industry は「管理者がポリシーで有効にする」と書いた（改善メモ参照）

出典:
- https://github.blog/changelog/2026-11-17-openais-gpt-6-2-astra-and-gpt-6-2-sol-now-available

## カテゴリ別まとめ

### Anthropic / Claude

- **Claude Code `2.1.327`**（ハイライト1参照）
- [新機能] **Claude Desktop のリリースチャネル** — Anthropic が Claude Desktop で更新の受け取り方を選べるようにした（11/17）。既定の Stable は検証を重ねた版を間隔をあけて受け取り、Latest はほぼ毎日新しい版を受け取る（Master）
  - https://support.claude.com/en/articles/12138966-release-notes
- [動向] **理論物理の未解決問題** — Anthropic が、Claude がブラックホールと量子重力に関する理論物理の未解決問題を2つ解いたとする研究記事を `/research` に載せた（11/17）（Master）
  - https://www.anthropic.com/research/claude-black-hole-physics
- [据え置き] **Anthropic のその他の一次** — Claude Platform の release notes（11/17 Linked billing）、モデル退役一覧（Active 17件）と廃止履歴（9/30）は動いておらず、Opus 4.5 の下限日 11/24 を確定する告知もない。`/news`（11/10）と Privacy Center（11/9）も変わらない（Master・industry）
  - https://platform.claude.com/docs/en/about-claude/model-deprecations

### OpenAI / Codex / ChatGPT

- [新機能] **Codex CLI `0.170.0`** — OpenAI が Codex CLI の安定版を `0.170.0`（11/18）に上げた。TUI のリアルタイム音声通話に WebRTC 接続を加え、OpenTelemetry の HTTP エクスポーターで認証ヘッダーを自動更新するようにした。環境をまたいで同名の MCP サーバーを使う実験的な対応も入った。pre-release は `0.172.0-alpha.1` まで進んだ（Master）
  - https://github.com/openai/codex/releases
- [予定] **11/30 に停止する API 機能の再告知（残り11日）** — OpenAI の deprecations ページで、`/v1/prompts`・Evals・Agent Builder が 11/30 に停止することを Master が再確認した（告知は 6/3）（Master）
  - `/v1/prompts`: プロンプト本文をアプリのコードへ移す
  - Evals: 読み取り専用になる。移行先は Promptfoo
  - Agent Builder: Agents SDK か ChatGPT Workspace Agents へ移る。ChatKit は残る
  - https://developers.openai.com/api/docs/deprecations
- [動向] **外部監査4団体の受け入れ** — The Decoder（11/18）によると、OpenAI が Apollo Research・METR・Transluce・Goodfire を社内に入れ、未公開モデル・ソースコード・学習データ・監視システムを調べさせる。結果は各団体が公表するが、OpenAI は機密部分を伏せて公表を遅らせられる。2027年初めに Transluce と8週間の追加レビューを行う（industry）
  - https://the-decoder.com/openai-opens-its-ai-systems-to-four-independent-on-site-auditors-for-the-first-time/
- [据え置き] **OpenAI のその他の一次** — API changelog（11/17 GPT-6.2）、Deployment Safety Hub（11/17 GPT-6.2 System Card）、community Announcements（11/17）、misalignment reports（First posted 11/12）は動いていない（Master・industry）

### GitHub Copilot / GitHub

- **GPT-6.2 Astra / Sol の Copilot GA**（ハイライト3参照）
- [新機能] **チーム単位のプラグイン既定** — GitHub が Copilot のチームカスタマイズを GA にした（11/18）。Organization のチームメンテナーとオーナーが、承認済みの Agent Plugins をチームの既定に選べる。VS Code・Copilot アプリ・Copilot CLI で直属メンバーに既定で有効になり、子チームには継承されない。Enterprise / Organization のポリシーが優先し、対象は Copilot Business / Enterprise（Master・industry）
  - https://github.blog/changelog/2026-11-18-customize-github-copilot-for-your-team
- [新機能] **GitHub Team のセキュリティリスク評価** — GitHub が、GitHub Team の組織でセキュリティのリスク評価を自動で走らせるようにした（11/18）。組織の管理者とセキュリティ管理者は、無料の評価で露出した認証情報とコードの脆弱性を確かめられる（industry）
  - https://github.blog/changelog/2026-11-18-security-risk-assessments-run-automatically-on-github-team/
- [版更新] **Copilot CLI `v1.0.114`** — GitHub が Copilot CLI の安定版を `v1.0.114`（11/18）にした。リリース本文は「Fixes and changes」だけで、個別の項目は載っていない（Master）
  - https://github.com/github/copilot-cli/releases

### Microsoft 365 Copilot

- **Chat と Office のモデルの従量課金**（ハイライト2参照）
- [新機能] **M365 アカウントで GitHub Copilot CLI** — MC1519871 の 11/17 更新で、M365 Copilot ライセンスを持つ Frontier の利用者が、GitHub アカウントなしで GitHub Copilot CLI にサインインし、Copilot Credits の従量課金でモデルを使えるようになった。既定はオフで、管理者が M365 管理センターの Copilot 設定で有効にする（Copilot）
  - Copilot Code のモバイル（iOS / Android）: クラウドセッションの開始・継続、承認依頼への応答、結果の確認ができる。ローカルセッションは使えない
  - Copilot Code の Mac: Microsoft Copilot デスクトップアプリで使える
  - Windows のローカル Sandbox: Copilot Code と、Code が起動したプロセスのファイル・ネットワークアクセスを許可した範囲に制限できる
  - https://mc.merill.net/message/MC1519871
- [新機能] **Release Notes の November 17 バッチ** — Microsoft が M365 Copilot Release Notes を2週間ぶりに改訂し、11/3〜11/17 の9項目を載せた（Copilot）
  - Outlook: カスタムエンジンエージェントをエージェントウィンドウから直接実行できる
  - Confluence Cloud コネクタ: 管理者が、取り込むスペースの指定か CQL でインデックス対象を絞れる（Roadmap 503571）
  - Tableau コネクタ: 利用者が Tableau のダッシュボードを自然言語で読み解ける
  - Organizational Data Service: 管理者が、選んだカスタム組織属性を M365 のユーザー情報に共有できる。既定はオフで、共有した属性はゲストを含むテナント全員に見える
  - https://learn.microsoft.com/en-us/microsoft-365/copilot/release-notes
- [新機能] **Cowork の Ignite 追加分** — Microsoft が Cowork で、自社の色・フォント・文体で資料を作る Brand Kit、Planner と Viva Engage のプラグイン、Sales プラグインの19スキル、Edge for Business での Cowork を GA にした（TC 11/17）。サブタスクを複数モデルのサブエージェントに分ける Auto と Work IQ による次のタスクの提案は Frontier で、GCC は今月展開を始める（Copilot）
  - https://techcommunity.microsoft.com/t5/microsoft-copilot-blog/what-s-new-in-copilot-cowork-at-ignite-2026/ba-p/4572242
- [新機能] **Agent Builder の Dataverse 参照** — 作成者が、モデル駆動型アプリと Dynamics 365 の Dataverse データを Agent Builder の宣言型エージェントのナレッジにできるようになった（MC1558817・11/17 GA）。PPAC の Work IQ 機能で有効になり、政府クラウド・EU/EFTA・FedRAMP 以外の新しい環境では自動で有効になる（Copilot）
  - https://mc.merill.net/message/MC1558817
- [新機能] **PowerPoint の Sales スキル** — 営業担当者が、Sales プラグインを有効にすると提案資料・パイプライン確認・バトルカード作成などのスキルを PowerPoint の Copilot で使えるようになる（MC1558023・11/17）。11月中旬から下旬に展開する（Copilot）
  - https://mc.merill.net/message/MC1558023
- [予定] **Pages のレポートとダッシュボード** — Microsoft が Roadmap に、利用者がプロンプトから対話型のレポートとダッシュボードを作り、コメントで部分的な編集を頼める Pages の機能を載せた（580445 / 580449・GA December CY2026）（Copilot）
  - https://www.microsoft.com/microsoft-365/roadmap?id=580445
- [観測] **Cowork のモデル表に GPT-6.2 が未掲載** — `cowork-models`（11/18 改訂）の選択肢は Auto＋7モデル（GPT 6.1 Sol・GPT 6 Astra・GPT 5.6 Terra・Claude Opus 5.5・Claude Sonnet 5.5・Claude Fable 5.2・Grok 4.7）のままで、TC の Cowork 記事が「この1週間で追加」と書いた GPT-6.2 Astra / Sol は表に無い（告知済み・表未掲載）（Copilot）
  - https://learn.microsoft.com/en-us/copilot/cowork/cowork-models

### Copilot Studio / Power Platform

- [新機能+仕様] **Copilot Studio の Ignite 発表** — Microsoft が Customer Conversation ハーネス、Copilot Studio と Cowork のアプリ作成、複数作成者の共同編集を GA にした（Copilot Studio ブログ 11/18）。ワークフローの分類ノードは判定スコアリングモデルが既定になり、メール振り分けなどの判定結果が前と変わる可能性がある。切り替え時期と旧挙動へ戻す方法は書かれていない（Copilot）
  - パブリックプレビュー: Cowork と Copilot Code から自然言語でエージェントとワークフローを作る機能、コマンドラインツールと Copilot Studio MCP
  - 2026年12月: エージェント専用アカウント（管理された資格情報で承認済みのリソースにアクセスする）がパブリックプレビューに入る
  - MC1557509: ワークフローの所有者をサービスプリンシパル（Entra のアプリ登録）にできる。GA は 12/17 まで
  - https://www.microsoft.com/en-us/copilot/blog/copilot-studio/build-and-manage-business-processes-with-microsoft-copilot-studio/
- [仕様] **Copilot Studio のモデル表** — Microsoft が Microsoft Copilot ハーネスのモデル表を再改訂した（11/18・`ms.date` 11/17）。提供中は19モデルで、Claude Haiku 5.5（GA）と Mistral Large 4（Preview）が載った。Claude Fable 系は「Anthropic models with data retention」設定（既定オフ）で別に有効にする。EU/EFTA でデータの地域間移動をオフにした環境の GPT-5 Chat は 11/30 で使えなくなる（Copilot）
  - https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-experience/authoring-agent-model-availability
- [新機能] **Copilot Credits の Reporting API** — 管理者が、Copilot Studio のクレジット消費をリソース・環境・ユーザー・機能の単位で Power Platform API から読めるようになった（MC1558020・パブリックプレビュー）。Roadmap 579968 では GA が January CY2027 で、旧来の非サポートの取得方法を置き換える（Copilot）
  - https://mc.merill.net/message/MC1558020
- [新機能] **キャンバスアプリの Copilot** — アプリの利用者が、過去の会話やエージェントを含む Copilot をキャンバスアプリの中で使えるようになる（Power Platform Blog 11/18・11月に GA）。アプリのデータアクセスと権限の範囲で動く（Copilot）
  - https://www.microsoft.com/en-us/power-platform/blog/2026/11/18/turn-ai-ambition-into-real-business-value-with-power-platform/
- [予定] **Frontier Tuning のプライベートプレビュー拡大** — Frontier プログラムの顧客が、自社の評価基準でスキルやモデルを調整する Frontier Tuning に申し込めるようになった（M365 Dev Blog 11/18）。調整対象は GPT 6 Luna と MAI Code 2 Flash で、プレビュー中は無料。Copilot Studio にも近く入る（Copilot）
  - https://devblogs.microsoft.com/microsoft365dev/frontier-tuning-opens-to-more-customers-with-new-tools-for-your-teams/
- [据え置き] **その他の Copilot Studio と Power Platform** — Copilot Studio What's New、課金3本、レート表、PPAC の容量管理、非推奨一覧、Released Versions（2026.6.3）は前日のままで、ガイダンスハブにも新しい記事はない（Copilot）
  - https://learn.microsoft.com/en-us/microsoft-copilot-studio/whats-new

### Microsoft（MAI モデル・実行基盤）

- [新機能] **Copilot Managed Runtime の正式提供** — Publickey（11/19）によると、Microsoft が AI で作ったアプリを自社の M365 テナント内で動かす Copilot Managed Runtime を Ignite で正式提供した。Entra ID の認証・アクセス制御・監査ログが使え、Copilot Studio・GitHub Copilot・VS Code で作ったアプリを載せられる。料金は記事に書かれておらず、GA の展開は12月中旬に終わる（MC1558033）（industry・Copilot）
  - https://www.publickey1.jp/blog/26/aicopilot_managed_runtime.html
- [新機能] **MAI モデル7種** — The Decoder（11/18）によると、Microsoft が MAI モデルを7種まとめて出し、一部製品の外部モデルを置き換える。性能比較の数字はほぼ社内評価である（industry）
  - Microsoft-Decision-1.1: Copilot のリクエスト振り分け用。Gemma 4 26B ベースで入力 $0.042・出力無料。Foundry・OpenRouter・Vercel で一般提供
  - MAI Cyber 2 Flash: $0.10 / $0.50。12月中旬にセキュリティ基盤 MDASH の既存モデルを自動で置き換える
  - MAI Work Flash: M365 と Fabric IQ で使い、Word では GPT-6.1 Sol 並みの性能を入力トークン約42%減で出すと説明した
  - https://the-decoder.com/microsoft-is-replacing-outside-ai-models-in-its-own-products-with-cheaper-in-house-alternatives/

### ライセンス・ガバナンス（Microsoft）

- [新機能] **M365 管理センターのマルチテナント管理** — 複数テナントを持つ組織の管理者が、Copilot・エージェント・AI コスト・テナント構成を1つの画面で管理できるようになる（MC1558024・パブリックプレビュー）。11月中旬から12月上旬に展開し、テナントは Entra のテナントガバナンスでリンクしておく必要がある（Copilot）
  - https://mc.merill.net/message/MC1558024
- [新機能] **Agent 365 Business Analytics と用途の分類** — 管理者が、Cowork を含む AI の支出をユーザー・モデル単位で掘り下げられるようになった（MC1557727・GA）。エージェントのセッションと Cowork の作業を6,000以上の用途に分類する機能は、対象の Frontier テナントで既定オンのパブリックプレビューとして11月下旬までに展開する（MC1557759）（Copilot）
  - https://mc.merill.net/message/MC1557759
- [予定] **Purview DLP のローカル AI エージェント対応** — 管理者が、対応するローカル AI エージェントのプロンプト・応答・ツール呼び出しに DLP ポリシーを適用できるようになる（MC1558037）。パブリックプレビューは2027年1月下旬から、GA は2027年3月下旬から4月下旬（Copilot）
  - https://mc.merill.net/message/MC1558037
- [仕様] **拡張機能 What's New の November 節** — Microsoft が Agent Registration API の `sourceAgentId` の扱いを明確にした（11/18）。作成時は必須で空白だけは不可、更新時に省略すると既存値を保持する（Copilot）
  - https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/whats-new
- [据え置き] **Partner Center の11月ページ** — `2026-november` は 11/13 のままで、新しい項目はない（Copilot）
  - https://learn.microsoft.com/en-us/partner-center/announcements/2026-november

### Google

- [新機能] **Drive の AI 分類の GA** — Google が Gemini で Drive のファイルに分類ラベルを付ける機能を GA にした（11/17）。管理者は自然言語の分類指示を Admin console で試してから展開でき、付いたラベルの件数と承認率をほぼリアルタイムで見られる。ラベルは DLP・保持ルール・監査調査に使える（Master）
  - https://workspaceupdates.googleblog.com/2026/11/gemini-powered-data-classification-in-Google-Drive-is-now-generally-available.html
- [新機能] **Gemini Notebook のサイト作成と Chat のエージェント設定** — Google が Workspace に2つの機能を出した（11/18 掲載、11/16 から展開）（Master）
  - Gemini Notebook: 「make me a site」と頼むと、ソースから対話型のサイト（解説・ダッシュボード・進捗表）を作って共有できる。18歳以上・Web が先行
  - Google Chat: 開発者がアプリとエージェントに説明文と最大3つのスターター プロンプトを Cloud コンソールで設定できる。エージェントの sessions は developer preview
  - https://workspaceupdates.googleblog.com/2026/11/transform-your-notes-and-research-into-dynamic-tools-with-Gemini-Notebook.html
  - https://workspaceupdates.googleblog.com/2026/11/starter-prompts-and-descriptions-for-Google-Chat-apps-and-agents.html
- [観測] **Gemini 4 Neon の SKU 掲載** — TestingCatalog が、Gemini 4 Neon が Google Cloud の SKU 一覧に入力 $3 / 出力 $15（100万トークンあたり）で載り、Antigravity CLI に Pro のオーケストレーターモデルとして現れたと報じた（11/18）。Google の発表は無く、Gemini API changelog は転送先に届かないまま（B-088）（Master）
  - https://www.testingcatalog.com/google-prepares-to-release-gemini-4-neon-model-on-apis/

### Cursor / その他エージェント

- [新機能] **Orca `v1.4.262` / `v1.4.263`** — Stably AI が Orca を2版進めた（11/17・11/18）（Master）
  - アカウント: 保存した Claude と Codex のアカウントに名前を付けられ、処理中の Claude セッションを選んだアカウントで再開できる
  - CLI: `orca agent installed` で入っているエージェント CLI を一覧でき、`orca linear connect` で Linear 連携を足せる
  - Workspace Cleanup: 削除済みワークスペースのチャットを消せる。既定オフで元に戻せない
  - https://github.com/stablyai/orca/releases
- [新機能] **Mistral Vibe のデスクトップアプリ** — Mistral が Vibe を macOS / Windows のデスクトップアプリとして出し、コーディングエージェントをローカルでもクラウドでも動かせるようにした。欧州では Vibe Pro を無料にした（TestingCatalog の ICYMI・一次未確認）（Master）
  - https://www.testingcatalog.com/icymi-mistral-launches-vibe-desktop-for-macos-and-windows/
- [据え置き] **Cursor・xAI・Devin・MCP ほか** — Cursor の changelog（11/6）とフォーラム（10/12）、xAI（11/2）、Devin（11/16）、TypeSafe AI（`jev-1.14.0`）、MCP blog（11/11）、Obsidian（1.15.1）は動いておらず、Hugging Face の8 org にも新しいリポジトリは無い。Apple Developer News の 11/17–11/18 の記事は AI 関連ではない（Master）

### セキュリティ

- [セキュリティ] **OpenJDK の Java4Shell（CVE-2026-114938・CVSS 9.2）** — GIGAZINE（11/18）によると、研究者 Quang Luong 氏（Calif）が OpenAI の Codex を使って OpenJDK の Base64 デコーダのメモリ破損を約1時間で見つけ、攻撃コードを約2時間・トークン費用 $200 未満で作った。Oracle は 11/17 に修正を出した。Keycloak・Jira・Confluence・Jenkins などの既定構成で、認証なしの遠隔コード実行が示された（industry）
  - 影響範囲: 未修正の OpenJDK 17.0.6 以降と、Amazon Corretto・Eclipse Temurin・Microsoft Build of OpenJDK・Oracle Java SE。AVX-512 VBMI 対応の x86-64 だけが対象で、ARM64 は影響を受けない
  - 当面の回避策: Base64 デコードの AVX-512 高速化を無効にする。修正版の番号は記事に書かれていない
  - https://gigazine.net/news/20261118-java4shell/

### 市場・企業・導入事例

- [動向] **KPMG の監査エージェント並走** — The Decoder（11/18）によると、KPMG 英国が FTSE 250 の上場企業1社の監査で、100体超の AI エージェントを通常の監査と並行して全工程に投入した。監査意見は従来の監査から出し、エージェントは個別の論点で深く掘った一方、規制と社内文書の突き合わせを誤る場面もあった。最大20件の大型監査へ広げる計画である（industry）
  - https://the-decoder.com/kpmgs-project-exponential-put-ai-agents-alongside-a-real-audit-team-and-found-the-bots-dug-deeper-on-individual-questions/
- [動向] **Nvidia の中国向け H200 販売終了** — GIGAZINE（11/18）によると、Nvidia の Colette Kress 暫定 CEO が中国向け H200 の販売を終えると発表した。会長は Jensen Huang 氏を CEO に戻す予定はないと述べた（industry）
  - https://gigazine.net/news/20261118-nvidia-ends-to-sell-chip-to-china/
- [据え置き] **Anthropic の IPO と未決の買収協議** — 検索時点で Anthropic の IPO 公開価格の発表は見つからず、仮条件は $70〜78 のまま（WSJ は $80 への引き上げの可能性を報道）。Amazon × Decart、Nvidia × Reflection AI の買収協議にも続報がなく、IDC Japan・MM総研・NRC の新しい公表もなかった（industry）

## 直近の注目予定

- **11/19**: Claude Enterprise で Claude Data が既定でオン ／ Anthropic が Nasdaq で取引開始の見込み（ティッカー ANT・報道） ／ Microsoft Ignite（〜11/20）
- **11/20**: Conductor のクラウド版が終了（二次） ／ Copilot Studio のコスト管理を M365 管理センターへ移す機能が GA（MC1530368）
- **11/21〜30**: GPT-5.6 Sol の期間限定価格が終了（一次どうしで日付が割れる）
- **11/24 以降**: `claude-opus-4-5-20251101` の暫定退役日（確定日ではない）
- **11月下旬**: PowerPoint の Copilot のプラグインが GA の展開に入る（MC1556104） ／ PowerPoint の Sales スキルの展開完了（MC1558023） ／ Agent 365 の用途分類（Frontier・既定オン）の展開完了（MC1557759）
- **11/29**: OpenAI が Daybreak Blue のセッションデータの学習利用を開始（二次）
- **11月中**: GitHub の cloud sandbox の課金開始（日付明記なし）
- **11月末**: M365 管理センターのリリース設定の統合が完了（MC1556082）
- **11/30**: `claude-sonnet-4-5-20250929` 退役 ／ Opus 4.8 の fast mode 削除 ／ OpenAI の Evals・`v1/prompts`・Agent Builder 停止 ／ Gemini 4 Argon の導入価格終了 ／ Power Platform のアプリ説明の AI 生成・Power Automate デザイナーの Copilot などが終了（MC1540258）、Describe it to design it と vibe.powerapps.com が退役 ／ EU/EFTA でデータの地域間移動をオフにした Copilot Studio 環境で GPT-5 Chat が使えなくなる
- **12/1**: OpenAI `gpt-image-1-mini` / `gpt-image-1.5` / `chatgpt-image-latest` 停止 ／ Gemini 4 Argon の単価が $4/$20 に倍増 ／ Google スライドの複数スライド作成の上限引き上げ優待が終了しうる
- **12/2**: GitHub が公開リポジトリの `pull_request_target` を既定でブロック ／ Power Platform のプロンプトから Anthropic・Grok・旧 GPT 系モデルが退役（MC1536101）
- **12月**: Copilot Code が GA ／ Agent 365 のアクションセンターがプライベートプレビュー ／ Copilot Studio のエージェント専用アカウントがパブリックプレビュー
- **12月上旬**: Chat と Office のモデルの従量課金が GA（MC1557754） ／ M365 管理センターのマルチテナント管理の展開完了（MC1558024） ／ Dataverse のストレージ検証の確定日程を告知（MC1483529）
- **12/8**: GitHub が非活動リポジトリの Dependabot アラートを停止、ホステッドランナーの ARM32 終了 ／ M365 Copilot in Power BI が既定でオン（MC1546429）
- **12/9**: EU / EFTA で Claude モデルが既定で有効に（MC1546438）
- **12/11**: OpenAI `gpt-5` / `gpt-5-mini` / `gpt-5-nano` / `gpt-5-pro` / `o3` / `o3-pro` 停止 ／ Power Apps の式の生成・Power Apps Ideas などが退役（MC1532421・MC1532426）
- **12/14**: Copilot から Claude Fable 5 / Haiku 4.5 / Gemini 3.8 Flash / Gemini 4 Argon / Grok 4.6 / Kimi K3 を廃止 ／ claude.ai/design の単体サイトが閉鎖
- **12月中旬**: Copilot Pages と Notebooks の OneDrive 保存の展開完了（MC1449182） ／ Learning Agent の GA 展開（MC1556094） ／ Copilot Managed Runtime の GA 展開完了（MC1558033） ／ MAI Cyber 2 Flash が MDASH の既存モデルを自動で置き換え（二次）
- **12/17**: Copilot Studio のワークフローのサービスプリンシパル認証が GA（MC1557509）
- **12/18**: Copilot から MAI-Code-1.1-Flash を廃止（→ 最新の MAI Code Flash）
- **12月中（日付未公表）**: ChatGPT と Codex の利用枠が Plus・Pro・Business で統合（二次）
- **12/31**: Claude Security の無償クレジット期間終了 ／ Copilot の Fable 5 系の ZDR 例外終了 ／ MCP File Uploads 拡張の安定版目標 ／ Power Platform 版のスケジュール済みプロンプト退役（MC1550533） ／ Copilot Studio の会話内での接続設定が GA（MC1548034）
- **2027-01-01**: Anthropic の新しい開示期限（高・重大度30日）を適用 ／ Commercial Cloud の現地通貨価格を5通貨で改定（日本円は対象外）
- **2027年1月**: Copilot Credits の Reporting API が GA（Roadmap 579968）
- **2027年1月以降**: Dataverse のみのテナントでストレージ検証開始（MC1483529）
- **2027-01-06**: OpenAI `tts-1` / `tts-1-hd` / `gpt-4o-mini-tts` 2版が停止 ／ セルフサービスの fine-tuning ジョブ作成が制限される
- **2027-01-14**: OpenAI `gpt-4o` 2版 / `gpt-4o-mini` / `gpt-4.1` / `gpt-4.1-mini` が停止
- **2027-01-15**: Claude Code Review の Enterprise 向けクレジット請求期限
- **2027年1月中旬**: Power BI の単体の Copilot が退役（MC1546429）
- **2027-01-20**: OpenAI `gpt-realtime` / `gpt-audio` / `gpt-4o-realtime` 系などが停止
- **2027年1月下旬**: UBB の入口が既定で表示され、旧設定が退役（MC1546354） ／ Purview DLP のローカル AI エージェント保護がパブリックプレビュー（MC1558037）
- **2027-01-30**: ChatGPT Classic（旧デスクトップアプリ）終了（二次）
- **2027-02-01**: OpenAI `gpt-5.5-cyber-preview` が停止
- **2027年2月**: VS Code の Copilot から Local harness を削除（`vscode.temporaryDefaultToLocalHarness` も廃止）
- **2027-02-10**: Claude Meetings の成果物の無料期間終了 ／ OpenAI `gpt-image-2` 停止
- **2027-03-01**: GPT-6.2 Astra / Sol の API の Ultrafast が Standard の3倍から6倍に
- **2027-03-01 以降**: Gems 廃止（Business / Enterprise）
- **2027-03-08**: Fable 5.2 ローンチ特典のリセットが失効
- **2027-03-30**: MCP 仕様 `2027-03-30` 版のリリース予定
- **2027年3月下旬〜4月下旬**: Purview DLP のローカル AI エージェント保護が GA（MC1558037）
- **2027 春**: Siri AI 対応アプリの App Store 提出受付が開始
- **2027-04-01**: OpenAI `gpt-5.1` / `gpt-5.3-codex` / `gpt-5.4-nano` 停止 ／ SharePoint の tempauth URL 退役（MC1551122・MC1492958）
- **2027-05-17**: GitHub Copilot の MAI Code 2 / MAI Code 2 Flash の導入価格が終わり、単価が倍に
- **2027-11-12**: Purview Data Governance のサポート終了

## 改善メモ

- Master: 新規提案・障害の変化なし。継続提案8件（最多 B-088 Gemini API changelog の URL 差し替え、16回目）
- Copilot: 新規提案・障害の変化なし。継続提案5件（最多 B-080 Cowork の Learn URL の移設、21回目）
- industry: 新規提案・障害の変化なし。継続提案7件（最多 B-040 セキュリティ開示の定点、17回目）
- ソース間の差異: GPT-6.2 Astra / Sol の Copilot での有効化を、Master は「既定のモデル有効化が生きていれば自動」、industry は「Business・Enterprise は管理者がポリシーで有効にする」と書いた。本サマリーは changelog の記述をより詳しく写した Master を採った
- ソース間の差異: industry はハイライト2に MAI-Code-1.1-Flash の 12/18 廃止（11/17 告知）を「新規」として挙げたが、本サマリーでは 11/18 のハイライト1で既報のため、注目予定にだけ残した
- 前日（11/18）分に欠損ソースはなく、欠損リカバリは不要
