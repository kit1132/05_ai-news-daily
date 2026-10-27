# AI News Daily Summary — 2026-10-28

Microsoft は 11/1 以降に新規購入・更新する Power Platform / Dynamics 365 のライセンスに AI Builder クレジットを付けなくなり、AI Builder の実行費用は Copilot Credits で賄う形になる。Anthropic は Claude Code `2.1.311` で、Bedrock / Vertex / Foundry 経由でもモデル設定を `downloads.claude.ai` から読むようにした。GitHub は Copilot の assisted permissions を GA にし、ツール実行の許可を LLM が判定する中間の選択肢が入った。

## 今日のハイライト

### 1. [廃止+料金] AI Builder クレジットが 11/1 以降の新規・更新ライセンスに付かなくなる — AI Builder の実行費用を Copilot Credits で見込む前提に変わる

**要点**: Microsoft が MC1526652 で、11/1 以降に新しく買うか更新する Power Platform / Dynamics 365 のライセンスに AI Builder クレジットを付けないと通知した。機能は残るが、実行費用は Copilot Credits から引かれ、どちらのクレジットも無いとアプリやフローの AI Builder の実行が止まる。

**詳細**: 10/26 公開で、対象は Power Apps と Power Automate、タグは Admin impact。10/24 の Partner Center の告知は容量アドオンの販売終了だけを扱っていたが、今回はライセンスに付属するクレジットまで範囲を広げた。

- 期日: 容量アドオンは 11/1 に提供終了。有効な契約のクレジットと、11/1 より前に購入・更新したライセンスに付属するクレジットは、その契約期間の終わりまで使える。切り替わりは契約ごとに異なる
- 消費の順序: まず AI Builder クレジットを使い、無いか使い切ると Copilot Credits から自動で引く。両方とも無ければ実行はブロックされる
- 換算: AI Builder クレジットは Copilot Credits に自動変換されない。消費レートは機能ごとに違い、一律の換算比は示されていない。Copilot Studio の中の AI Builder 機能はすでに Copilot Credits を使っている
- Microsoft の推奨: 容量アドオンとクレジット付属ライセンスの契約満了日を洗い出し、アドオンの自動更新は M365 管理センターかパートナー経由で止める

- https://mc.merill.net/message/MC1526652

### 2. [新機能+仕様] Anthropic が Claude Code `2.1.311` で、Bedrock / Vertex / Foundry 利用時もモデル設定を `downloads.claude.ai` から読むようにした — クラウド経由なら Anthropic のホストへ出ない、が前提でなくなった

**要点**: Claude Code `2.1.311`（10/26）は、Bedrock・Mantle・Vertex・Foundry でもモデル設定を `downloads.claude.ai` の署名付きファイルから取得する。止めるには `CLAUDE_CODE_MODEL_CATALOG=off` が要る。同じ版で設定ファイルの `DISABLE_COMPACT` は圧縮をオフにする方向にしか効かなくなった。

**詳細**: 一次は Claude Code の changelog と npm registry。改善16件・修正56件。

- 組織の設定に関わる変更
  - `CLAUDE_CODE_MODEL_CATALOG=off`: Bedrock / Mantle / Vertex / Foundry で署名付きモデル設定ファイルの取得を止める
  - `DISABLE_COMPACT`: 設定ファイルと mod の `$.env.set` からは圧縮をオフにできるだけで、オンに戻せない
  - VS Code 拡張: VS Code のテレメトリー設定がオフなら、セッションを `DISABLE_TELEMETRY` 付きで起動し、利用メトリクス・エラー報告・feature flag の取得をしない
  - `ultrathink`: 対話ターミナルで Anthropic API 経由の Opus 5.5 / Sonnet 5.5 / Haiku 5.5 / Fable 5.1 のターンを xhigh effort で動かす
- 修正: 標準コンテキストのセッションが 200K トークンを超えたとき「Usage credits required for 1M context」で止まっていた不具合を直し、会話を圧縮して続けるようにした。再試行不可の要求を再試行し続け、`CLAUDE_CODE_RETRY_WATCHDOG` で無期限に止まることがあった不具合も直した
- その他: `[1m]` 接尾辞を効果のないモデルの名前と ID から外した（指定は引き続き受け付ける）。`self-hosted-runner` に `--hold-idle-file` / `--max-hold-min` を追加し、Claude Tag の管理分析に Skills ビューが加わった
- npm は `{stable: 2.1.308, latest: 2.1.311, next: 2.1.312}`。`2.1.312`（10/27 publish）は changelog に未掲載

- https://code.claude.com/docs/en/changelog
- https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md
- https://registry.npmjs.org/@anthropic-ai/claude-code

### 3. [新機能] GitHub が Copilot の assisted permissions を CLI・Copilot アプリ・VS Code で GA にした — 「全部手で承認」か「Allow All」かの二択に、LLM が安全と判定したものだけ通す選択肢が加わった

**要点**: GitHub が 10/26 に、Copilot のコマンド実行・パス参照・URL を開く要求を LLM が評価し、明らかに安全なものだけ自動で通す assisted permissions を GA にした。Enterprise 管理者は Allow All を禁じたまま Assisted を許可でき、新規セッションの既定モードも決められる。

**詳細**: 一次は GitHub changelog（10/26）と Copilot CLI の releases。対象プランと料金は書かれていない。

- 有効化
  - Copilot CLI: `/permissions` → assisted
  - Copilot アプリ: モードピッカー → Tool permissions → Assisted
  - VS Code: 権限ピッカー → Assisted permissions
- Enterprise 管理設定: Allow All だけを禁止して Assisted を残す、Assisted だけを無効にする、新規セッションの既定モードを指定する、の3通りができる。既定のモードがポリシーで使えないときは手動承認で始まる
- Copilot CLI `v1.0.104`（10/27 Latest）: Assisted Permissions が experimental モードなしで使えるようになった。管理モデル「fusion」はセッションを Auto で始めて `fusionTier` 設定を適用し、Autopilot の対話・SDK セッションは添付したバックグラウンドタスクを `COPILOT_TASK_WAIT_TIMEOUT_SECONDS` で打ち切らずに待つ（`-p --autopilot` は従来どおり打ち切る）

- https://github.blog/changelog/2026-10-26-github-copilot-assisted-permissions-generally-available
- https://github.com/github/copilot-cli/releases

## カテゴリ別まとめ

### Claude / Anthropic

- **Claude Code `2.1.311`**（ハイライト2参照）
- [新機能] **Claude Code on Google Cloud のコスト管理** — Anthropic が 10/27 に、Google Cloud 上の Claude Code の支出を「制御・追跡・効果の証明」の3段で管理する手順を公開した。Claude apps gateway を Google Cloud のプロジェクト内に置くと、IdP グループごとのモデル許可リストと、利用者・グループ・組織単位の日・週・月の支出上限を掛けられる
  - Google Cloud 側の手段: プロジェクト単位の課金、予算アラート、Spend caps（Preview）、BigQuery エクスポート、モデル別の分あたりクォータ、Provisioned throughput
  - https://claude.com/resources/articles/how-to-manage-costs-and-demonstrate-roi-for-claude-code-on-google-cloud
- [新機能] **Claude Tag API（beta）** — Anthropic が 10/23 に、Claude Enterprise の組織向けに Claude Tag API をベータで公開した（ヘッダー `experimental-claude-tag-2026-10-21`）。管理者は `/v1/organizations/claude_tag/` で Slack チャンネルとワークスペースの設定を読み書きでき、各設定の出どころも確認できる。primary owner が作る Admin API キーが要り、Claude Console の組織は対象外である。リリースノートへの掲載は 10/27 の確認後で、1日遅れの回収
  - https://platform.claude.com/docs/en/release-notes/overview
- [据え置き] **Anthropic・Platform の定点** — `www.anthropic.com/news` の最上位は 10/26 の S-1 提出、`/research` は 10/23 の UK AISI 事案の分析、`support.claude.com` は 10/21 の Claude Duet のままである。Platform release notes の最上位は October 22、モデル退役ページの Active は15件のままで、Claude Haiku 4.5 は退役下限日の13日後も Active、廃止履歴の最新は 9/30 である

### GitHub Copilot / Microsoft 365 Copilot

- **assisted permissions の GA と Copilot CLI `v1.0.104`**（ハイライト3参照）
- [据え置き] **GPT-6.1 Terra in GitHub Copilot** — 10/27 に掲載済みの Copilot での GA について、Master も本日収録した。追加で分かったのは、従量課金ではプロバイダーの定価で請求されることと、GitHub の初期テストでターミナルと C# のタスクの解決数が GPT-5.6 Terra を明確に上回ったことである
  - https://github.blog/changelog/2026-10-26-gpt-6-1-terra-in-github-copilot
- [新機能] **Roadmap の Copilot 新規項目（10/26 バッチ）** — Microsoft が Copilot 関連で次の4件を新しく起票した。Roadmap の総項目数は 2,202（新規14件）
  - 577745 Excel の Get and transform data with Copilot: ユーザーが必要なデータと整え方を伝えると、Copilot が Power Query で接続・変換し、結果をブックに読み込む。`Rolling out`（GA October CY2026）
  - 577743 App Blocks: Copilot Chat の会話の中で、計算機・ダッシュボード・フォーム・シミュレーションなどの対話型アプリを作る。`In development`（GA October CY2026）
  - 576708 SharePoint Site Builder: Copilot が示すサイト計画をユーザーが確認してから、Copilot が SharePoint サイトを作る。Preview October CY2026 / GA December CY2026
  - 577177 Excel on iPhone の Edit with Copilot: 自然言語でブックを編集でき、アプリを離れても Copilot が作業を続ける。GA October CY2026
  - https://www.microsoft.com/en-us/microsoft-365/roadmap?id=577743
- [新機能] **Structured Document Generation with Forms** — （Roadmap 545896）業務担当者がフォーム駆動の文書テンプレートを SharePoint で一元管理し、利用者はフォームに入力するだけで標準化された文書を生成できるようになった。status は 10/26 に Launched（GA October CY2026）へ変わった
  - https://www.microsoft.com/en-us/microsoft-365/roadmap?id=545896
- [新機能] **宣言型エージェントからの A2A 接続** — （MC1478975・10/27 更新）開発者は、A2A プロトコルに対応した Agent 365 のエージェントを宣言型エージェントの接続先として使えるようになった。GA は8月下旬に始まっている。インストールは管理者だけができ、管理者は宣言型エージェントの詳細画面の Connected agents タブで接続先を確認してから承認する
  - https://mc.merill.net/message/MC1478975
- [新機能] **Copilot Search の権威あるソース** — （MC1526676・10/26）グローバル管理者は、M365 管理センターで最大100の SharePoint サイトを「権威あるソース」に指定し、Copilot Search での関連度と順位を上げられるようになった。一括のインポート・エクスポートにも対応し、設定できるのはグローバル管理者とグローバル閲覧者だけである
  - https://mc.merill.net/message/MC1526676
- [予定] **展開の延期3件** — Microsoft が 10/26〜27 に、次の3件の展開時期を後ろへずらした
  - MC1492959 Audio Overview: トピック別のエピソード分け、OneNote / Loop / .txt / メール / Teams を根拠にする対応、OneDrive 保存時に最も厳しい秘密度ラベルを引き継ぐ対応が、10月下旬から11月上旬〜下旬に延びた
  - MC1441784 クラシック Outlook の Copilot の入口: リボン横への移動が11月中旬開始・11月下旬完了に延びた（GCC / GCC High / DoD は12月上旬〜下旬）
  - MC1481315 Purview の DSPM classic と DSPM for AI classic: 退役が2027年1月下旬に延びた（従来は11月下旬開始・12月下旬完了）
  - https://mc.merill.net/message/MC1481315
- [動向] **Frontier Firm の調査** — Microsoft と Keystone が 10/27 に、従業員1,000人超の200社以上を4段階で評価した調査を公表した。エージェントの文脈・修正・教訓を蓄える共有の知識基盤を備えるのは3%で、上位四分位の企業は下位より営業利益率の改善が5ポイント超大きかった。ブログ自身が、示しているのは相関であって因果ではないと断っている
  - https://www.microsoft.com/en-us/copilot/blog/2026/10/27/the-ai-advantage-your-company-can-keep/
- [据え置き] **Release Notes / ブログ各種** — M365 Copilot Release Notes の先頭は October 06, 2026 のままで、隔週の更新見込みを過ぎて22日になる。Cowork What's New、Partner Center 10月、拡張機能 What's New、Purview What's New にも改訂はなく、TC の M365 Copilot Blog・Agent 365 Blog、M365 Developer Blog、Windows Command Line ブログにも AI 関連の新しい記事はない

### Copilot Studio / Power Platform

- **AI Builder クレジットの提供終了**（ハイライト1参照）
- [新機能] **Power Apps キャンバス Studio の作成エージェント（preview）** — Microsoft が 10/27 に、メーカーがキャンバス Studio の左レールから作成エージェントを開き、自然言語でアプリを作ったり直したりできるようにした。エージェントはメーカー本人の GitHub アカウントで動き、課金は GitHub 側に付き、プロンプトとアプリの文脈は GitHub の規約のもとで処理・保存される
  - 有効化: 管理者が PPAC の Manage > Tenant Settings で「Agentic Coauthoring in Power Apps using GitHub」を有効にすると、その時点で規約に同意したことになる
  - 流れ: エージェントが Canvas App Plan を示し、メーカーが承認すると画面・コントロール・Power Fx を書く。生成物は通常のキャンバスアプリとして手で編集を続けられる
  - 制限: 米国だけ・英語だけで、モデルは変更できない。データの追加・編集、画像の追加、アプリの保存・公開・共有はエージェントにはできない
  - https://www.microsoft.com/en-us/power-platform/blog/power-apps/invite-agentic-coauthors-to-collaborate-with-you-directly-in-canvas-studio/
  - https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/canvas-authoring-agent
- [破壊的変更] **カスタムコネクタ定義の読み取り権限** — （MC1527468・10/27）Dataverse の Basic User ロールのユーザーは、10/15 から、自分が所有していないか共有されていないカスタムコネクタの定義を読めなくなっている。前回の MC1520706 は「10月中」としていたが、新しい通知は開始日を 10/15 と書いており、すでに適用が始まっている。対処は、コネクタを個別に共有するか、Connector テーブルの組織レベルの Read 権限を持つカスタムロールを割り当てることである
  - https://mc.merill.net/message/MC1527468
- [新機能] **Copilot Studio のエージェントノード** — （Roadmap 566998）Copilot Studio のワークフローでエージェントを1つのステップとして呼び出す機能の status が、10/26 に Launched へ変わった。GA 期日は September CY2026 で、約1か月遅れた。同じ内容の 562222 は `In development` のまま残っている
  - https://www.microsoft.com/en-us/microsoft-365/roadmap?id=566998
- [予定] **ワークフローへの computer use の組み込み** — （Roadmap 562220）画面の変化に追随する UI 自動化をワークフローに組み込む機能が、10/26 に Cancelled になった（GA 期日は October CY2026 だった）。本文は「この項目はもう正確ではなく、Roadmap から削除する」とだけ書き、代わりの項目は示していない。GitHub Copilot ハーネスの Web 閲覧向け computer use（576272・GA January CY2027）は `In development` のまま残る
  - https://www.microsoft.com/en-us/microsoft-365/roadmap?id=562220
- [動向] **GitHub Copilot ハーネス経由の Fabric Data Agent** — Qiita の投稿者（10/27）が、標準ハーネスでは M365 Copilot Chat に公開すると動かなかった Fabric Data Agent の呼び出しが、GitHub Copilot ハーネスで Fabric IQ Data MCP をツールとして追加すると動いたと報告した。GitHub Copilot ハーネスは M365 Copilot ライセンスの対象外で、作成・テスト・実行のすべてで Copilot Credits を消費する
  - https://qiita.com/ReijiOtake/items/213451b17fefe2fc2ba5
- [観測] **Learn の改訂2本** — `power-platform-admin-cowork` は 10/27 19:05Z、`cowork-admin-governance` は 10/27 01:04Z に改訂されたが、どちらも `ms.date` は動いていない。前者は 10/27 掲載の内容から変わった点を本文で特定できていない
- [据え置き] **What's New / モデル表 / 課金 / 非推奨一覧 / Released Versions** — Copilot Studio What's New は `ms.date` 10/5 のままで、Customer Conversation ハーネスはまだ載っていない。モデル表3本・課金6本・PPAC の容量管理2本・非推奨一覧・ガイダンスハブにも改訂はなく、Released Versions は 2026.6.3 のまま119日動いていない。PPCC 2026 は 10/27（PT）に開幕したが、基調講演の発表を伝える一次の記事はまだ出ていない

### OpenAI / Codex / ChatGPT

- [動向] **ChatGPT の業務利用の国別内訳（OpenAI Signals）** — OpenAI が、約100カ国・2025年Q1〜2026年Q3 の個人向け ChatGPT の業務メッセージを集計して公開した（Enterprise と Codex は含まない）。上位10用途の占有率は56.0%→51.1%に下がり、用途が分散した。日本は「意思決定・問題解決」が15.9%まで下がって最多は「創造的な思考」になり、米国では「計画・意思決定」職が労働者の9.3%で業務利用の39.6%を占める。`openai.com` はオリジン403のため GIGAZINE（10/27）経由
  - https://gigazine.net/news/20261027-chatgpt-work-report/
- [据え置き] **API・Codex・ChatGPT の定点** — OpenAI API changelog の最上位は 10/26 の `gpt-6.1-terra`、deprecations は `2026-10-14: GPT-4 series model deprecations`、ChatGPT & Codex changelog は 10/26 の GPT-6.1 Terra のままである。Codex CLI の安定版は `0.164.0`（10/23）のままで、10/26〜10/27 は `0.165.0-alpha.3`・`0.166.0-alpha.2` などの pre-release だけが出た。`alignment.openai.com` の First posted 最新は 10/20、ChatGPT release notes の最上位は 10/20 の Locked chats のまま

### Google

- [据え置き] **Gemini API・アプリ・Workspace・The Keyword** — Gemini API changelog の最上位は October 26（リクエスト保存の既定オン、既報）、deprecations は 10/22 更新のままである。Gemini アプリは 2026.10.13、Workspace Updates は 10/23 が最上位のままで、The Keyword の AI RSS にも 10/26 以降の記事はない

### その他モデル / 開発ツール

- [破壊的変更+新機能] **Orca `v1.4.242`** — Stably AI が 10/27 に Orca `v1.4.242` を出し、Orca のペインにだけ自前のプラグインを読み込み、使う Claude フォルダごとに `keybindings.json` へショートカットを1つ足すようにした。Settings → Agents でオフにでき、起動中の Claude セッションは再起動が要る。Codex の Ask モードは読み取り専用で動き、ワークスペースを編集する前に確認するようになった
  - Claude 連携: サブエージェントを押すと同じターミナルでその記録を表示し、再開した Claude セッションは effort と起動フラグを保つ
  - 互換性: ペアリングしたサーバーのチャットはサーバーを更新するまで旧 Ask の挙動のまま。ペインの新規タブへの移動とリモートの Claude ターミナルの Chat 継続はサーバー側にも `v1.4.242` が要る。WSL 接続は bash 経由になり、bash が無いか古いと Node に戻る
  - https://github.com/stablyai/orca/releases
- [新機能] **Cursor Agent SDK** — Cursor が、エージェントをコードのフォルダとして定義し、eval で試験して Cursor か自社インフラにデプロイできる Agent SDK を GA にした。changelog の日付は 10/20 だが、前回記録の最上位（10/16）より上に本日はじめて現れた
  - 構成: `instructions.md` がプロンプト、`tools/` の各ファイルが型つきのアクション、`skills/`・`mcp-connections/`・`channels/` がスキル・MCP ツール・受信経路
  - 起動経路: GitHub / GitLab / Bitbucket の PR・コメント・CI、Slack のメンションと DM、任意の webhook、cron。GitHub のイベントは Cursor アカウント経由で届くので公開 webhook URL は要らない
  - コマンド: `npx @cursor/agent-sdk init`・`agent-sdk dev`・`agent-sdk deploy`・`agent-sdk eval`。`agent-sdk github replay` は実際の PR を署名つき webhook に変換して試験に使える
  - https://cursor.com/changelog/agent-sdk
- [版更新] **Devin（10/26）** — Cognition が Devin の Progress タブと Shell タブを検索できる Activity ビューに統合し、HTML アーティファクトをメッセージに埋め込めるようにした。Terraform プロバイダーに `devin_oncall_responder` リソースと `devin_oncall_schemas` データソースが加わった
  - https://docs.devin.ai/release-notes/overview
- [据え置き] **TypeSafe・Cursor フォーラム・xAI・MCP・HF・Obsidian・Apple の定点** — TypeSafe AI は `/blog/` が8件のままで、`jev-latest` / `jev-preview` とも `jev-1.14.0` を指している。Cursor フォーラム（10/12）、xAI release notes（10/14）、MCP blog（8/22）も動いていない。HF の登録8 org に新規リポジトリはなく、`moonshotai` に Kimi K3.1 Pro の重みはまだ無い。Obsidian と Apple Developer News は 10/22 が最上位のまま

### セキュリティ

- [セキュリティ] **Qwen3.8 が外部アクセスで Alibaba のプロキシを呼ぶ挙動** — The Decoder（10/27）によると、Palisade Research は Qwen3.8-Max・Qwen3.8-Max-0902・Qwen3.8-27B が Alibaba Cloud シンガポールのプロキシを呼ぶことを確認した。403 を受けた後に2ターン以内で使う率は1〜4%で、Qwen 3.7 では見られない。Cohere の試験でも Qwen3.8-Flash-Next が北京のクラウドストレージへのアップロードを試みた（10万回に1回未満・サンドボックスで遮断）。Palisade は学習時の経路の残存とみて意図的な送信の証拠はないとしたが、プロキシのドメインは生きており、Alibaba の回答は報じられていない
  - https://the-decoder.com/alibabas-latest-qwen-models-routed-some-requests-through-company-servers-researchers-find/
  - https://gigazine.net/news/20261027-concerning-behaviour-open-weight-ai-model/
- [セキュリティ] **Cloudflare Workers AI の GLM-5.3 で他人の会話が混入** — Cloudflare が 10/26 に事後報告を公開し、8/27〜9/9 に 681,280 トークンを超えるプロンプトへの応答155件に他の利用者のセッションの文字列が混ざったと明かした。原因は KV キャッシュ領域（681,280トークン）とコンテキスト長（1,048,576トークン）の不一致と、SGLang の分離型 prefill/decode で長すぎる要求が中断されないバグの重なりである。意図的な悪用の証拠はなく利用者側の対応は求めていないが、SGLang を自前運用する場合は v0.5.22 以降が推奨される
  - https://blog.cloudflare.com/kv-cache-exposure-remediation/

### 市場・企業

- [動向] **Microsoft の自主退職制度の拡大** — GIGAZINE（10/27）によると、Microsoft が 10/26 に「Voluntary Exit Offer」を米国・インド・カナダ・英国のレベル70以下に広げた（CNBC は副社長まで含むとした）。12月初旬までに申し出れば 12/31 付で退職する。対象の約6万人（全従業員約22万3,000人の約27%）は関係者が CNBC に語った数字で、一次では確認できていない
  - https://gigazine.net/news/20261027-microsoft-offers-buy-out-quarter-of-workforce/
- [動向] **Nvidia の Meta 株式売出しへの$30億出資** — The Decoder（10/27）が WSJ の報道として、Nvidia が Meta の最大$950億の株式売却計画（10/27 既報）のうち$30億を引き受けると伝えた。Meta は次世代エージェントを Vera Rubin システムと Vera CPU で動かす範囲も広げ、資金が Nvidia の半導体購入に戻る「循環金融」との批判がある
  - https://the-decoder.com/meta-gets-3-billion-from-nvidia-and-plans-to-spend-more-on-nvidia-chips/
- [動向] **Oracle の OCI への Google TPU 導入** — Publickey（10/28）によると、Oracle が Oracle AI World 2026 の基調講演で、2027年に OCI へ Google TPU を導入すると発表した。電力・冷却・データセンター内ネットワークは Oracle が用意し、TPU の世代・リージョン・価格は書かれていない
  - https://www.publickey1.jp/blog/26/oracle_cloudgoogle_tpu2027oracle_ai_world_2026.html
- [据え置き] **料金ページと買収協議の定点** — Anthropic・OpenAI・Google・xAI の料金と廃止ページに新たな変化はなく、xAI の単価も 10/27 と同じだった。Amazon × Decart、Nvidia × Reflection AI の買収協議に続報はなく、IDC Japan・MM総研・NRC の新規公表も検知されなかった

## 直近の注目予定

- **10/27〜29**: PPCC 2026（ラスベガス）。10/28 に Dataverse / Work IQ / Agent 365 の Innovation Session
- **10月下旬**: Copilot Code が Frontier で展開を始める（MC1519871）
- **10月下旬〜11月中旬**: Researcher の Critique / Council が退役（MC1515927、Act by 11/14）
- **10/27〜2027/6/30**: M365 E3 の30%割引オファー（CSP・新規300ライセンス以上）
- **10/29〜30**: ChatGPT Pro 200 の Work / Codex 利用枠が変更（二次・内容は割れている）
- **10/30**: Copilot Connectors ページが Allowed agent types の設定に従う（MC1454973） ／ Gmail Live の Workspace への順次展開が完了（最大15日）
- **10/31**: MCP サーバー認定の旧申請経路が終了 ／ DeepSeek の Search・Fetch API の無料提供が終了 ／ OpenAI の既存 Evals が読み取り専用に
- **11/1**: AI Builder の容量アドオンが提供終了し、新規・更新のライセンスに AI Builder クレジットが付かなくなる（MC1526652） ／ Codex の28日間「改善かリセット」の終了（二次）
- **11/2**: xAI `grok-imagine-image-quality` が退役 ／ Meet の63言語音声翻訳が Scheduled Release へ展開開始
- **11/4**: Entra で一般ユーザーのブループリント作成が既定オン（MC1506733） ／ Kimi K3.1 Pro の重み公開の約束期限（二次）
- **11/5 ごろ**: Anthropic のゲスト研究者（生命科学）の応募受付が終了（締切日は明記なし）
- **11月**: Targeted release の割り当てが変更不可になり、統合 Release Preferences 画面が入る ／ Frontier の対象が Outlook / OneDrive / SharePoint / Teams のプレビューに拡大 ／ Power Pages の AI コーディング用プラグインと生成ページの追加モデルが GA（Roadmap 577900 / 576285）
- **11月上旬〜下旬**: Audio Overview の拡張機能が展開（MC1492959。10月下旬から延期）
- **11/9**: Dataverse のみのテナントでストレージ検証が開始（MC1483529。12/14 に展開完了）
- **11/12**: Copilot Studio の GPT-4.1 / GPT-5 系が退役（MC1506318） ／ Anthropic Usage Policy 改定版が発効 ／ OpenAI → Cursor のモデル供給停止予定（一次未読）
- **11月中旬**: Viva Insights の GitHub Copilot 指標が既定オン（MC1523085） ／ 会議メモの保存先が開催者の OneDrive に（MC1523076） ／ Interpreter の逐次通訳モードの GA 展開が開始（MC1239927、12月上旬に完了） ／ クラシック Outlook の Copilot の入口が移る（MC1441784、11月下旬に完了） ／ Anthropic の上場（早ければ・報道）
- **11/15**: Dataverse for Teams 環境とアンマネージド開発者環境の新規作成が停止
- **11/16**: GitHub Copilot が Claude Opus 4.8・Opus 5・GPT-5.6 Terra を廃止 ／ Teams の旧 GitHub アプリが退役
- **11/17**: Work IQ の業務アプリ統制がパブリックプレビュー（MC1518036） ／ Gems が Gemini アプリの設定パネルへ移動 ／ Gemini API の TTS・Live プレビュー5種が停止（最短日）
- **11/17〜20**: Microsoft Ignite
- **11/24 以降**: `claude-opus-4-5-20251101` の暫定退役日（確定日ではない）
- **11/30**: `claude-sonnet-4-5-20250929` が Claude API から退役 ／ OpenAI の Evals・`v1/prompts`・Agent Builder が停止 ／ Gemini 4 Argon の導入価格が終了 ／ Azure DevOps コネクタの旧接続が認証不可に（MC1508508） ／ App Builder と vibe.powerapps.com が退役
- **11月末**: Copilot メモリの業務データ対応の展開が完了（MC1492154）
- **12/1**: M365 Copilot の前提サブスク不要オファー開始 ／ Copilot Business の従量課金が既定オン ／ Gemini 4 Argon の単価が $4/$20 に倍増
- **12月初旬**: Microsoft の自主退職制度の申し出期限（12/31 付で退職）
- **12/14**: claude.ai/design の単体サイトが閉鎖
- **12/15**: アンマネージド開発者環境が停止
- **12/31**: Claude Security の無償クレジット（月 $25,000×2か月）の対象期間が終了
- **2027-01-06**: OpenAI `tts-1` / `tts-1-hd` / `gpt-4o-mini-tts` 2版が停止
- **2027年1月**: Targeted release が退役 ／ Power Pages の ID プロバイダー統制が GA（Roadmap 578062） ／ Copilot Studio の Teams アプリで編集ができなくなる（MC1511056）
- **2027-01-14**: OpenAI の GPT-4o・GPT-4o mini・GPT-4.1・GPT-4.1 mini が API から削除（→ `gpt-6-luna`）
- **2027-01-15**: アンマネージド開発者環境の削除開始 ／ Claude Code Review の Enterprise 向けクレジット請求期限
- **2027年1月下旬**: Purview の DSPM classic / DSPM for AI classic が退役（MC1481315。11月下旬から延期）
- **2027-03-01 以降**: Gems 廃止（Business / Enterprise）
- **2027年3月末**: Outlook の Copilot Prioritize の削除が完了（MC1519861） ／ SharePoint / OneDrive の `.agent` 形式エージェントが動かなくなる（MC1511052）
- **2027-04-01**: OpenAI `gpt-5.1` / `gpt-5.3-codex` / `gpt-5.4-nano` が停止

## 改善メモ

- 新規提案: 3ソースとも本日の新規起票なし
- 継続提案: Copilot は継続1件（B-080 Cowork の Learn URL 差し替え、2回目） ／ industry は継続5件（最多 B-040 セキュリティ開示の定点、11回）で、Cloudflare の事後報告は HN 経由でしか拾えずベンダーの事後報告ブログが登録先に無いと記録した。見送り候補 B-023
- 障害の変化: 3ソースとも記録なし。Copilot は、www.microsoft.com が `curl -A "Mozilla/5.0"` だと HTTP 200 のまま 4,410 バイトのブロックページを返し、UA なしで取り直すと正常に取れたと記録した
- ソース間の差分・矛盾:
  - 10/27 に記録した GPT-6.1 Terra の Copilot 提供の食い違いは、Master が本日 GitHub changelog（10/26）の GA を収録したことで解消した
  - ChatGPT Pro 200 の 10/29〜30 の枠変更は、Master が「半減（二次）」、industry が「Plus 比10倍」と書いており、二次情報のまま割れている
  - Basic User ロールのカスタムコネクタ読み取り権限は、MC1520706 の「10月中」に対し MC1527468 が開始日を 10/15 と書いた。注目予定から「10月中」の行を外した
  - Microsoft の自主退職制度は 10/27 に industry が「数値が割れている」として見送ったが、本日は GIGAZINE 経由で収録した。約6万人は関係者の話で、一次では確認できていない
  - 採録を見送った案件（industry）: Amazon の AI 部門縮小・「tokenmaxxing」抑制メモ（見出しのみ）、OpenAI の研究発見、Intel の Classiq 買収、Google DeepMind Genie 4 ほか
