# AI News Daily Summary — 2026-11-05

Teams の Intelligent call delegation は 11/17 に従量課金のパブリックプレビューへ移り、支出ポリシーを作らないと止まる。CSP の Copilot Business の従量課金の既定オンは、12/1 から2027年1〜3月へ再び延びた。開発ツールでは、Claude Code 2.1.318 で `deniedMcpServers` の URL 指定が Anthropic 提供のコネクタにも効くようになり、Copilot Studio が MCP サーバーを出して Claude Code や Codex からエージェントを作れるようになった。

## 今日のハイライト

### 1. [破壊的変更+料金] Teams の Intelligent call delegation が 11/17 から従量課金のパブリックプレビューに移り、支出ポリシーがないと止まる — Frontier で無償だった着信の振り分けに、管理者の課金設定が要るようになる

**要点**: AI が着信を確かめて文脈を集め、Bookings で折り返しも予約する Intelligent call delegation は、早ければ 11/17 に Frontier からパブリックプレビュー（Ring 3.6）へ移る。課金は Copilot Credits の従量課金で、管理者が支出を構成するまで始まらないが、Frontier で使っていたテナントでは着信の振り分けが止まる。

**詳細**: MC1537490（11/3 公開・New feature / Admin impact・Roadmap 565216）。パブリックプレビューは11月中旬〜12月中旬、GA は2027年1月中旬〜下旬の見込み（Copilot）。

- 求められる対応: M365 管理センターで支出ポリシーを作り、エージェントとサービスで Intelligent call delegation だけを選び、対象のユーザー・グループに割り当てる。必要に応じて M365 Copilot のユーザーライセンス（USL）も確かめる
- 対象: Frontier プレビューで使っていたテナントと、Ring 3.6 で使い始めるテナント。対応製品は Teams・M365 Copilot（Premium）・Bookings 連携

- https://mc.merill.net/message/MC1537490

### 2. [料金+予定] Copilot Business の従量課金の既定オンが、12/1 から2027年1〜3月へ再び延期された — 12/1 に課金設定が自動で入る前提が消えた

**要点**: CSP で新規購入する Copilot Business の従量課金（UBB）が既定で有効になる時期は、12/1 から Microsoft の FY27 Q3（2027年1〜3月）に移った。11/2 予定だった Partner Center のサンドボックスも延び、新しい日付は未定である。12/1 に合わせた準備は時期を引き直すことになる。

**詳細**: Partner Center 11月アナウンスの「Availability update」（11/3 付、ページ改訂は 11/4 18:46Z）。延期は 10/2 に続いて2回目（11/2 → 12/1 → FY27 Q3）（Copilot）。

- 変わらない点: 既定の支出上限は1ユーザーあたり月 **4,000 Copilot Credits** で、管理者が変えられる。課金方式の既定は従量課金。新規購入の時点で、同じテナントの既存 Copilot Business ライセンスにも UBB が有効になる
- 対象になる体験: Copilot Cowork、Work IQ API、GitHub Copilot ハーネス
- サンドボックス: 新しい日付は Partner Center で告知され、GA の少なくとも30日前から試せる
- 対象市場: 新しい時期は全市場に適用される。初回は対象外だったオーストラリア・ドイツ・フランス・インド・韓国などの11か国も含む

- https://learn.microsoft.com/en-us/partner-center/announcements/2026-november

### 3. [破壊的変更+新機能] Claude Code 2.1.318 で `deniedMcpServers` の URL 指定が Anthropic 提供のコネクタまで止めるようになり、IDE 拡張の自動導入が終わった — URL で書いた拒否リストの効く範囲が広がった

**要点**: Anthropic が出した Claude Code `2.1.318` では、管理設定 `deniedMcpServers` の URL エントリが、上流 URL の一致する Anthropic 提供サーバーとクラウド / self-hosted runner のコネクタにも効く。これまで素通りしていたコネクタも止まる前提に変わり、IDE のターミナルで起動しても拡張は入らなくなった。

**詳細**: 公開日は Master が 11/3、industry が 11/4 と書いている。npm は `{stable: 2.1.311, latest: 2.1.318, next: 2.1.318}`（Master・industry）。

- 拒否の範囲: URL エントリはコネクタ自身の URL を渡されるクラウドセッションと self-hosted runner でも一致判定する。それ以外の環境でコネクタを止めるには名前で拒否する
- IDE 拡張: IDE 内のターミナルから起動しても、拡張のインストール・更新をしない。外部ターミナルの `/ide` か、エディタの拡張ビューから入れる
- サインイン期限: `claude auth status` に `loginExpiresAt`、`claude -p` の JSON に `credential_expires_at` が加わり、`claude -p` は保存したサインインの期限10日前から stderr に警告を出す
- gateway: `mantle` upstream に `assume_role` が加わり、別 AWS アカウントのロールで開発者ごとの AWS 費用を按分できる
- 挙動の変更: Managed Agents の `/claude-api managed-agents-onboard` が組み込みツールに `auto` 権限ポリシーを既定で付ける。background subagent のシェルコマンドを3分でバックグラウンドへ移す動作が全プロバイダに広がった。cloud sessions はリポジトリを選ばずに始められる
- self-hosted runner: orchestrator のログで `nack session=…` の末尾に `reason=…` が付く。`retryable=true:` / `retryable=false:` に一致させているスクリプトは直す必要がある

- https://code.claude.com/docs/en/changelog
- https://registry.npmjs.org/@anthropic-ai/claude-code

## カテゴリ別まとめ

### Anthropic / Claude

- **Claude Code 2.1.318**（ハイライト3参照）
- [仕様+予定] **Claude のテキスト透かしの対象拡大** — Anthropic が 11/3 の Platform release notes で、Claude Mythos 5 / Opus 4.7 / Sonnet 4.6 の生成テキストにも透かしを入れると載せた。API 利用者へのメールでは、11/16 から Opus 4.6・Opus 4.5・Sonnet 4.5・Haiku 4.5 にも入れると伝えた（The Decoder 11/4 によるメール内容の紹介。リリースノートには未記載）（Master・industry）
  - 付く条件: Mythos 5・Opus 4.7 は設定にかかわらず付く。Sonnet 4.6 と第2弾の4モデルは、`temperature` / `top_p` / `top_k` が既定値のときだけ付く
  - Amazon Bedrock: 第1弾の3モデルへの展開は 11/10 までに終える予定。第2弾は数日遅れる場合がある
  - 理由と検出: 12月の EU AI Act の期限が理由とされる。ファイルの Content Credentials は無料の Claude Content Checker で確かめられ、テキスト透かしの検出は private preview
  - https://platform.claude.com/docs/en/release-notes/overview
  - https://the-decoder.com/anthropics-text-watermark-is-easy-to-bypass-on-several-older-claude-models/
- [動向] **FlashProve** — Anthropic の Frontier Red Team が 11/2、応答が公開済みの重みから生成されたことを、重みを明かさずに zkSNARK で証明する試作を Apache 2.0 で公開した。製品や API への組み込みは無い研究プロトタイプである（Master・industry）
  - 性能: Llama 4 Maverick（400B MoE・4bit）を H100 1枚で約110トークン/秒で証明する。GPU 時間は推論の約70〜95倍、1,024トークンの証明は約19MB、検証は CPU で約17秒
  - 制約: greedy デコードの整数版の重みが対象で、サンプリング出力は対象外。コンテキストは1,024トークンまで
  - https://www.anthropic.com/research/provable-inference
- [据え置き] **退役ページ・ニュース一覧** — モデル退役ページの Active は15件のままで、Deprecation history の最新は 9/30（Sonnet 4.5）である。Haiku 4.5 は退役下限日（10/15）を21日過ぎても Active にあり、Opus 4.5（下限 11/24）の告知も無い。`www.anthropic.com/news`・`claude.com/resources/articles`（11/2）・`support.claude.com`（10/21）・Privacy Center（`dateModified` 10/30）も動いていない（Master・industry）
  - https://platform.claude.com/docs/en/about-claude/model-deprecations

### GitHub Copilot

- [新機能] **Copilot usage metrics API の BYOK 内訳** — GitHub が 11/3、Copilot usage metrics API で BYOK の利用を Copilot ホストのモデルと分けて読めるようにした。管理者は自前キーとローカルモデルの利用量を、組織・Enterprise のレポートで追える（Master・industry）
  - `totals_by_local_byok`: セッション・リクエスト・プロンプト・トークンを `byok_kind`（`local_managed` / `local_user` / `local_auto` / `remote_user`）と `surface`（`copilot_cli` / `copilot_app`）で分ける
  - `is_custom_enterprise_model`: Enterprise / 組織で設定したカスタムモデルの利用を、IDE を含む全クライアントで示す
  - 注意: ローカル BYOK はクライアントのテレメトリ由来の下限値で、テレメトリを切った利用者は数えない。過去日への遡及は無い
  - https://github.blog/changelog/2026-11-03-byok-and-enterprise-custom-models-in-the-copilot-usage-api
- [新機能] **GitHub Copilot Dreaming** — Publickey（11/5）によると、GitHub は Universe 2026 で、Copilot が過去の会話と PR レビューをバックグラウンドで振り返り、古くなった指示ファイルや Copilot Memory を更新する機能をパブリックプレビューにした。更新案は PR で届く。対象プランと料金は記事に書かれていない（industry）
  - https://www.publickey1.jp/blog/26/github_copilot_dreaminggithub_universe_2026.html
- [料金] **GitHub Enterprise に Copilot の利用権が付く** — Partner Center（11/4）が転載した GitHub Universe の発表によると、GitHub Enterprise の利用者は追加料金なしで Enterprise のシートから GitHub Copilot を使えるようになった。AI の利用分は AI Credits で課金される（Copilot）
  - https://learn.microsoft.com/en-us/partner-center/announcements/2026-november
- [版更新] **Copilot CLI の pre-release 3版** — GitHub が Copilot CLI の `v1.0.106-7`〜`-9` を 11/3〜11/4 に出した。セッションを VS Code で開く `/code` が加わり、`--resume` / `--continue` での再開時にも `--yolo` / `--allow-all` が効くようになった。Windows ではローカルモデルのダウンロード時に llama.cpp を自動で入れる。安定版は `v1.0.105`（10/28）のまま（Master）
  - https://github.com/github/copilot-cli/releases

### OpenAI / Codex / ChatGPT

- [動向] **OpenAI の Pierre Computer Company 買収** — The Decoder（11/4）によると、OpenAI は Codex で使っている Trees・Diffs・Highlights の開発元で、Git ベースのコード保管サービス Code Storage を持つ同社を買収する。金額は非公表で、規制当局の承認が要る。オープンソースのプロジェクトは公開を続け、OpenAI は社内のバージョン管理バックエンド Pando も明らかにした（industry）
  - https://the-decoder.com/openai-acquires-pierre-computer-company-to-make-git-keep-up-with-ai-coding-agents/
  - https://gigazine.net/news/20261104-openai-git-pando/
- [版更新] **Codex の pre-release 2版** — OpenAI が Codex の `0.167.0-alpha.5` と `0.168.0-alpha.1` を 11/4 に出した（どちらもリリース本文なし）。安定版は `0.166.0`（10/29）のまま（Master）
  - https://github.com/openai/codex/releases
- [据え置き] **API・ChatGPT の一次ページ** — API changelog（10/30 gpt-6-rosalind）、deprecations（10/14 の GPT-4 系）、Deployment Safety Hub（10/30）、community Announcements（10/28）、`learn.chatgpt.com` の changelog（10/29）、`alignment.openai.com`（First posted 10/20）は動いていない（Master・industry）
  - https://developers.openai.com/api/docs/changelog

### Microsoft 365 Copilot

- [新機能] **SharePoint tools in Work IQ** — 開発者は、Work IQ MCP サーバー経由で、60を超える SharePoint の操作（リスト・ライブラリ・ファイル・検索・承認・版管理など）をパブリックプレビューで任意のエージェントから呼べるようになった（SharePoint Blog・11/3）（Copilot）
  - 権限: 呼び出しはサインインしたユーザーとして動き、新しいスコープ `WorkIQ.Read` と `WorkIQ.Act` が要る。既存の `WorkIQAgent.Ask` だけのエージェントには SharePoint のパスが見えない
  - 管理者の統制: テナントで Work IQ を有効にし、アプリに同意し、Work IQ のテナントポリシーで許すパスと操作を選ぶ
  - 課金: Work IQ の従量課金（Copilot Credits）で、M365 Copilot ライセンスとは独立している。社内評価ではタスクの合格率が 70.1% から 84.6% に上がり、トークンは16%減った
  - https://techcommunity.microsoft.com/blog/spblog/introducing-sharepoint-tools-in-work-iq/4569917
- [仕様] **無償の Copilot Chat の上限拡大の開始日** — Partner Center（11/4）によると、M365 Copilot ライセンスのない Copilot Chat 利用者の上限拡大（前日ハイライト3）は、席数2,000以下の組織では 11/2 に始まっていた。2,001席以上の組織では 11/9 に始まる。MC1536163 は 11/9 だけを書いていた（Copilot）
  - https://learn.microsoft.com/en-us/partner-center/announcements/2026-november
- [新機能] **Cowork を Home タブから開く** — Frontier の利用者は、Copilot アプリの Home タブの入力欄にある Chat / Cowork の切り替えから Cowork を使えるようになった。Cowork What's New の10月節に追記された（Copilot）
  - https://learn.microsoft.com/en-us/copilot/cowork/whats-new
- [予定] **Teams 会議の AI ポリシーの切り替えの延期** — Microsoft が MC1532253 を 11/3 に更新し、MeetingAI / TranscriptionWithMeetingAI への切り替えを延ばした。Targeted Release は12月上旬開始・12月中旬完了、GA は2027年1月上旬開始・1月中旬完了になった（Copilot）
  - https://mc.merill.net/message/MC1532253
- [予定] **Learning Agent の AI Skills Navigator プレイリスト** — 利用者は、M365 Copilot の Learning Agent で、役割・製品・スキル別のプレイリストを自然言語で探せるようになる。11月中旬に全世界で展開し、AI Skills Navigator の Credentials か Microsoft YouTube 動画の設定がオフだとプレイリストは出ない（MC1537495）（Copilot）
  - https://mc.merill.net/message/MC1537495
- [予定] **Roadmap 11/4 バッチ** — Microsoft 365 Roadmap に 11/4 00:02Z のバッチで35件が入り、総項目数は 2,273 になった。大半は Dynamics 365 である（Copilot）
  - Copilot 関連の新規: 571296（Teams の Facilitator が会議の発言・チャット・共有ファイルから PowerPoint を作る）、578859（Teams の Queues アプリのモバイル版に Copilot）、576280（Power Apps のフォーム入力支援が M365 のファイルを参照元に使う）
  - `Launched` になったもの: 545063（Purview のインサイダーリスク管理がエージェントに対応）、558286（文字起こしを保存しなくても Intelligent Recap）、561026（SharePoint のフォームから文書を生成する Power Automate アクション・preview）
  - https://www.microsoft.com/releasecommunications/api/v2/m365/rss
- [据え置き] **Release Notes / ブログ各種** — M365 Copilot Release Notes の先頭は October 27, 2026 のままで、Copilot ブログ（先頭 10/29）と Agent 365 Blog（9/30）に新しい記事はない。Purview と拡張機能 What's New も前日のまま（Copilot）

### Copilot Studio / Power Platform

- [新機能] **Copilot Studio MCP サーバーと10月アップデート** — 開発者は、Copilot Studio MCP サーバーを使い、GitHub Copilot・Claude Code・OpenAI Codex などからエージェントとワークフローの作成、テストと評価、公開、トラブルシューティングまでを自然言語で行えるようになった。アクセスは組織の権限とポリシーに従う（Copilot ブログ 11/4）（Copilot）
  - Work IQ: Copilot Studio で GA になった。メール・会議・ファイル・会話・組織関係を横断してエージェントの文脈に使える
  - ワークフローの GA 3件: Copilot Chat / Cowork の呼び出し、抽出ノード（文書・メール・画像から値を取り出す）、複数作成者での共同編集
  - Frontier: Cowork の Copilot Studio スキル（M365 ライセンスの利用者が Cowork からエージェント・アプリ・ワークフローを作る）と、エージェントが自分の資格情報とスコープで動くエージェントアカウント（プライベートプレビュー）
  - コスト: メーカーが構築・テスト中の Credits 消費を見られるようになり、ワークフローの実行・ノード単位のレポートも加わった
  - https://www.microsoft.com/en-us/copilot/blog/copilot-studio/new-and-improved-agents-that-are-persistent-agents-for-customer-conversations-and-improved-maker-experience-in-microsoft-copilot-studio/
- [予定] **Describe it to design it の退役の正式告知** — Microsoft が MC1537406（11/3）で、11/30 以降は Power Automate の Describe it to design it で新しいクラウドフローを作れなくなると告知した。既存のフローは残る。代わりとして GitHub Copilot CLI と Claude Code 向けの Power Automate プラグインを案内している。非推奨一覧から一度消えた節（10/30）は撤回ではなかった（Copilot）
  - https://mc.merill.net/message/MC1537406
- [観測] **Learn ページの改訂と移設** — Copilot Studio What's New が 11/4 19:08Z に改訂されたが、節は September 2026 が最新のままで差分は特定できない。Web 検索の統制ページ `manage-public-web-access` は HTTP 301 で `copilot/plan/` 配下へ移った（Copilot）
  - https://learn.microsoft.com/en-us/copilot/plan/manage-public-web-access
- [版更新] **Copilot Agent Kit October 2026 HotFix 2** — Power CAT が 11/3、October 2026 版の2つ目の修正版を出した（Copilot）
  - https://github.com/microsoft/Power-CAT-Copilot-Studio-Kit/releases
- [据え置き] **課金・モデル表・非推奨一覧** — Copilot Studio の課金・ハーネスのページ、課金レート表、PPAC の容量管理、モデル表3本、ガイダンスハブ、非推奨一覧に改訂はない。Released Versions は 2026.6.3 のまま127日たつ（Copilot）
  - https://learn.microsoft.com/en-us/power-platform/important-changes-coming

### Google / オープンウェイト / その他の開発ツール

- [新機能] **Kimi K3.1 Pro の重み公開** — Moonshot AI が `moonshotai/Kimi-K3.1-Pro` を Hugging Face に公開した（`private: false` / `gated: false`）。10/23 の API 提供時に約束した 11/4 までの重み公開が守られた。総 2.8T / 活性 104B の MoE で、コンテキストは100万トークン、重みは MXFP4、vLLM と SGLang のレシピが案内されている（Master）
  - MaaS 条項: 第三者に推論・ファインチューニングを提供する事業で、直近12か月の売上が **$20M** を超える場合は商用利用の前に別契約が要る
  - 表示義務: 月間アクティブ1億人超、または月売上 $20M 超の製品は UI に「Kimi K3.1-Pro」を表示する。内部利用と公式製品・認定推論パートナー経由の利用には掛からない
  - https://huggingface.co/moonshotai/Kimi-K3.1-Pro
  - https://huggingface.co/moonshotai/Kimi-K3.1-Pro/blob/main/LICENSE
- [新機能] **Classroom の課題に Guided Learning** — Google が 11/4、Google Classroom の課題に Gemini アプリの Guided Learning を組み込める機能を、Gemini 対応の全言語で世界に展開し始めた。教員は Classroom の資料を文脈に指定でき、生徒の進捗も見られる（Master）
  - https://workspaceupdates.googleblog.com/
- [新機能] **Orca v1.4.248** — Stably AI がデスクトップ版 `v1.4.248` を 11/4 に出し、コミットメッセージ・PR 説明・ブランチ名・チャット名の生成に使うモデルと effort を Source Control の設定で選べるようにした。更新の遅延（0〜30日）と1回だけのスキップも選べる。Claude Code / Codex 連携の変更と非互換の記載は無い（Master）
  - https://github.com/stablyai/orca/releases
- [観測] **Gemini API の一次ページに届かない** — `ai.google.dev/gemini-api/docs/changelog` は本日も `aistudio.google.com` へ 301 を返し、転送先はこの実行環境から到達できない。WebSearch でも 10/30 より新しい項目は見つからず、11/17 の停止と 12/1 の Argon 値上げは3日続けて一次未確認である（Master・industry）
- [据え置き] **その他の定点** — Cursor の changelog（10/20）とフォーラム（10/12）、xAI（11/2）、Devin（11/2）、MCP blog（9/29）、The Keyword（11/2）、Gemini アプリの release notes（2026.10.13）は動いていない。TypeSafe AI の `jev-latest` は `jev-1.14.0` のままである（Master）

### 業界・市場

- [動向] **Synergy の Q3 2026 クラウドシェア** — Publickey（11/5）が紹介した Synergy Research の推計では、2026年第3四半期のクラウドインフラ市場は **$168B**（前年同期比55%増）で、伸び率は過去最高になった。シェアは AWS 26%（2pt 減）・Microsoft 19%（1pt 減）・Google 16%（1pt 増）。提案資料で使っている Q1 2026 の値（AWS 28%・Azure 21%・GCP 14%）は更新が要る（industry）
  - 上位3社に続く層: Oracle・CoreWeave・Crusoe・Nebius など。今年事業を始めた SpaceXSI が売上上位10社に入った
  - 一次未確認: `www.srgresearch.com` はゲートウェイ拒否で、数値は Publickey の記事だけによる。比較の起点（前期比か前年比か）も記事に書かれていない
  - https://www.publickey1.jp/blog/26/aws26google_cloud1620263synergy_research.html
- [動向] **Revolut のコーディング支援の費用を約10分の1に** — GIGAZINE（11/4）によると、Revolut は Gemini と Claude Code から、Z.ai の GLM（5.1→5.3）を自社の NVIDIA B200 56基で動かす形に移った。GLM-5.1 は100万トークンあたり約 $0.30 で、コーディング時間が約60%、作業開始からマージ準備までが約70%改善した。品質の数値は示されておらず、画像の理解が要る作業は Gemini を使い続けている（industry）
  - https://gigazine.net/news/20261104-revolut-cut-ai-cost/
- [動向] **GitHub Octoverse 2026** — GitHub は、開発者が2億2,500万人に達し、日本は715万人で5位だったと発表した（Publickey 11/5）。TypeScript が2年連続でコントリビューター数1位になり、PR の伸びが最も大きかったのは Rust だった。急成長した OSS の上位は CC Switch と Awesome MCP Servers である（industry）
  - https://www.publickey1.jp/blog/26/github2typescriptrustosscc_switchomarchygithub_octoverse_2026.html
- [据え置き] **買収協議・国内調査** — Amazon × Decart、Nvidia × Reflection AI の買収協議に続報はなく、Anthropic の S-1/A の本文も未確認のままである。IDC Japan・MM総研・NRC の新しい公表も無かった（industry）

## 直近の注目予定

- **11/5**: Apple Intelligence の開発者向けラボ（Siri AI の質疑。18〜19時 PT） ／ PnP の Community call
- **11/5 ごろ**: Anthropic のゲスト研究者（生命科学）の応募受付が終了（締切日は明記なし）
- **11月**: GitHub の cloud sandbox の課金が開始（日付は明記なし） ／ Targeted release の割り当てが変更不可になり、統合 Release Preferences 画面が入る
- **11/9**: GitHub が公開リポジトリの `pull_request_target` を試験ブロック（16:00〜18:00 UTC） ／ 2,001席以上の組織で、ライセンスのない Copilot Chat 利用者の上限拡大が開始（2,000席以下は 11/2 開始済み） ／ Dataverse のみのテナントでストレージ検証が開始（MC1483529）
- **11/10**: Amazon Bedrock の Mythos 5 / Opus 4.7 / Sonnet 4.6 へのテキスト透かし展開が完了予定
- **11/12**: Copilot Studio の GPT-4.1 / GPT-5 系と、GitHub Copilot ハーネスの GPT-5 Chat・GPT 5.6 Sol / Luna が退役（MC1506318） ／ Anthropic Usage Policy 改定版が発効 ／ OpenAI → Cursor のモデル供給停止予定（一次未読）
- **11/13**: Excel と Cowork の会計機能が GA（MC1536053）
- **11/15**: Dataverse for Teams 環境とアンマネージド開発者環境の新規作成が停止 ／ Copilot Studio のカスタム採点器ライブラリが GA（MC1531932）
- **11/16**: GitHub Copilot が Claude Opus 4.8・Opus 5・GPT-5.6 Terra を廃止 ／ Teams の旧 GitHub アプリが退役 ／ `pull_request_target` の2回目の試験ブロック ／ Cowork / Autopilot の Engage プラグインが GA（MC1530609） ／ Claude Opus 4.6・Opus 4.5・Sonnet 4.5・Haiku 4.5 に透かしが入る（二次）
- **11/17**: Teams の Intelligent call delegation が従量課金のパブリックプレビューへ移行（MC1537490。支出ポリシーがないと停止） ／ Gems が Gemini アプリの設定パネルへ移動 ／ Gemini API の TTS・Live プレビュー5種が停止（最短日。一次未確認）
- **11月中旬**: 単体の Word / Excel / PowerPoint エージェントの撤去が開始（MC1536062、12月下旬に完了） ／ Office in Copilot の展開（MC1530611） ／ Chat からのモード切り替え提案（MC1536065） ／ Learning Agent のプレイリスト（MC1537495） ／ 低評価フィードバックのカテゴリ選択（MC1530595） ／ Agent Builder のプロンプトのスケジュール実行（MC1302906） ／ Viva Insights の GitHub Copilot 指標が既定オン（MC1523085）
- **11/17〜20**: Microsoft Ignite
- **11/20**: Copilot Studio のコスト管理を M365 管理センターへ移す機能が GA（MC1530368）
- **11/24 以降**: `claude-opus-4-5-20251101` の暫定退役日（確定日ではない）
- **11月下旬**: Copilot アプリの Home の Projects / Workspaces が Deferred release に出る（MC1535647） ／ PowerPoint の営業向けスキルの展開完了
- **11/29**: OpenAI が Daybreak Blue のセッションデータの学習利用を開始（二次）
- **11月末**: Word の Top of Doc 要約の廃止が完了（MC1454113） ／ Notebooks の Power BI 参照の GA が開始（MC1474458）
- **11/30**: Power Automate の Describe it to design it が退役（MC1537406） ／ Opus 4.8 の fast mode を削除 ／ `claude-sonnet-4-5-20250929` が Claude API から退役 ／ Power Apps のモデル駆動アプリの説明文の AI 生成などが退役 ／ OpenAI の Evals・`v1/prompts`・Agent Builder が停止 ／ Gemini 4 Argon の導入価格が終了 ／ Azure DevOps コネクタの旧接続が認証不可に（MC1508508） ／ App Builder と vibe.powerapps.com が退役
- **12/1**: M365 Copilot の前提サブスク不要オファー開始 ／ Gemini 4 Argon の単価が $4/$20 に倍増 ／ Google スライドの複数スライド作成の上限引き上げ優待が終了しうる
- **12/2**: Power Platform のプロンプトから Anthropic・Grok・旧 GPT 系のモデルが退役し自動移行（MC1536101） ／ GitHub が公開リポジトリの `pull_request_target` を既定でブロック
- **12月上旬**: Copilot アプリのタスクバー固定にライセンス別の選択肢が入る（MC1530612） ／ Teams 会議の MeetingAI / TranscriptionWithMeetingAI ポリシーの Targeted Release が開始（MC1532253）
- **12月中（日付未公表）**: ChatGPT と Codex の利用枠が Plus・Pro・Business で1つの予算に統合（二次）
- **12/11**: Power Apps の式の生成・Power Apps Ideas・Copilot によるコントロール名の変更が退役（MC1532421・MC1532426）
- **12/14**: claude.ai/design の単体サイトが閉鎖
- **12/15**: アンマネージド開発者環境が停止
- **12月下旬**: Purview DLP の Microsoft 以外のアプリ対応が GA（MC1449180） ／ 単体 Word / Excel / PowerPoint エージェントの撤去が完了（MC1536062）
- **12/31**: Power Platform の環境間のコメントのインポート・エクスポートが終了 ／ Claude Security の無償クレジット（月 $25,000×2か月）の対象期間が終了 ／ Gemini 4 Carbon の導入価格の割引が終了
- **2027-01-06**: OpenAI `tts-1` / `tts-1-hd` / `gpt-4o-mini-tts` 2版が停止
- **2027年1月**: Targeted release が退役 ／ Copilot Studio の Teams アプリで編集ができなくなる（MC1511056） ／ Teams の会議メモリーファイルの生成が開始（MC1429018） ／ Teams 会議の MeetingAI ポリシーの GA（MC1532253、上旬開始・中旬完了）
- **2027年初頭**: GitHub のリポジトリ書き込み基盤の全ユーザー移行が完了
- **2027-01-14**: OpenAI の GPT-4o・GPT-4o mini・GPT-4.1・GPT-4.1 mini が API から削除（→ `gpt-6-luna`）
- **2027-01-15**: アンマネージド開発者環境の削除開始 ／ Claude Code Review の Enterprise 向けクレジット請求期限
- **2027年1月中旬〜下旬**: 旧来の Teams 保持ポリシーが Copilot の対話に効かなくなる（MC1481313） ／ Intelligent call delegation が GA（MC1537490）
- **2027年1〜3月**: CSP の Copilot Business 新規購入で従量課金が既定オン（12/1 から延期・Partner Center）
- **2027-02-01**: Microsoft が `usage_ai-training` トークンへの対応を開始
- **2027-03-01 以降**: Gems 廃止（Business / Enterprise）
- **2027年3月**: Purview の DSPM classic / DSPM for AI classic が退役（MC1481315）
- **2027年3月末**: Outlook の Copilot Prioritize の削除が完了（MC1519861） ／ SharePoint / OneDrive の `.agent` 形式エージェントが動かなくなる（MC1511052）
- **2027年春**: Siri AI 対応アプリの App Store 提出受付が開始
- **2027-04-01**: OpenAI `gpt-5.1` / `gpt-5.3-codex` / `gpt-5.4-nano` が停止

## 改善メモ

- 新規提案: Copilot が B-084（Web 検索の統制ページ `manage-public-web-access` の追跡 URL を `copilot/plan/` 配下へ差し替える）を起票した。Master と industry は新規起票なし
- 継続提案: Master は継続6件（最多 B-036 DeepSeek 登録、12回目。B-088 Gemini API Changelog の URL 差し替えは2回目） ／ Copilot は継続4件（最多 B-080 Cowork の Learn URL 差し替え、10回目。B-081 ハーネス改名は8回目、B-083 は2回目） ／ industry は継続7件（最多 B-040 セキュリティ開示の定点、14回。見送り候補 B-036）
- 障害の変化: industry が `www.srgresearch.com`（Synergy Research）のゲートウェイ拒否を新規に記録した
- 欠損リカバリ: 前日（11/4）分は3ソース揃っており、対象なし
- ソース間の差分・矛盾:
  - Claude Code 2.1.318 の公開日が、Master は 11/3、industry は 11/4 で割れた。本サマリーは公開日を断定せず両方を記した。タグは両ソースとも `[破壊的変更+新機能]` で一致し、Master がハイライトの軸にした `deniedMcpServers` の範囲拡大を industry は書いていない
  - 透かしの対象を、Master はリリースノートの3モデル（Bedrock は 11/10 完了予定）だけ、industry は 11/16 の第2弾4モデル（メールの二次報道）まで書いた。事実の矛盾ではなく、第2弾はリリースノートに未記載のため「二次」として扱った
  - Copilot Business の従量課金の既定オンは、前日のサマリーで 12/1 としていたが、Copilot の本日分で FY27 Q3 への延期を反映した。直近の注目予定の 12/1 から外し、2027年1〜3月へ移した
