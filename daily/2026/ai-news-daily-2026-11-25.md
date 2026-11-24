# AI News Daily Summary — 2026-11-25

Google が Workspace の MCP サーバーと CLI を GA にし、外部 AI エージェントは 2027-02-01 から REST API を直接呼べなくなる。GitHub は 12/1 から使用量レポートに `user_id` 列を足し、列の位置で読む集計は12月分からずれる。Anthropic は PR のレビュー・修正・承認をまとめる Claude Ship を出し、Code Review は承認まで進める PR 運用の一部になった。

## 今日のハイライト

### 1. [破壊的変更+料金] Google が Workspace の MCP サーバーと CLI を GA にした — 外部 AI エージェントは 2027-02-01 から REST API を直接呼べなくなり、標準枠を超える利用は 4/1 から課金される

**要点**: Google が 11/24、Gmail・Drive・Docs など8サービスの Google ホスト MCP サーバーと Workspace CLI を全顧客に GA した。外部 AI エージェントは REST API ではなく MCP を使うことが求められ、2027-02-01 に技術的な強制が始まる。Workspace API を叩く自作エージェントは、2か月余りで経路の作り直しが要る。

**詳細**: Workspace Updates ブログ（11/24）による（Master）。
- MCP サーバー: Gmail / Drive / Docs / Sheets / Slides / Calendar / Chat / Tasks（Keep は近日）。Rapid / Scheduled Release とも2週間以内に展開する
- 利用枠: Standard（無料・公開レート上限。現行開発者の99%超が該当）と Scaled（高い上限）の2段。Scaled は 2027-04-01 から日次無料枠を超えた分だけ課金される（Gmail / Calendar / Drive / MCP サーバーから）
- 既存プロジェクト: Standard の上限を超えるプロジェクトは「組織内専用」に指定するか Scaled に切り替えないと、4/1 以降 Standard の上限に戻される
- 管理者: Admin console の Security > API Controls で外部 AI ツール・MCP・CLI・API のアクセス、機微な操作への人の確認ルール、エージェントの監査ログを扱える。既存のユーザー単位の DLP がエージェントにも掛かる
- 識別: 外部 AI エージェントは OAuth で自分を名乗る必要があり、OAuth クライアントに `is_agentic` を付けられる。新しい Workspace AI Tools Addendum は API 由来データの長期保存とスクレイピングを禁じる

出典:
- http://workspaceupdates.googleblog.com/2026/11/mcp-servers-cli-standardized-usage-tiers-now-available.html

### 2. [破壊的変更+予定] GitHub が 12/1 から使用量レポートに `user_id` 列を加える — 列の位置で読む Copilot の使用量集計は、残り6日で見出し名で読むよう直さないと12月分から列がずれる

**要点**: GitHub が 11/23、使用量レポートの `username` 列の隣に `user_id` 列を 12/1 から加えると告知した。後ろの列はすべて1つ右にずれる。Copilot の AI 使用量やプレミアムリクエストを列の位置で集計しているスクリプトは、12/1 までに見出し名で読むよう直す必要がある。

**詳細**: GitHub changelog（11/23）による（industry）。
- 対象レポート: 詳細使用量レポート、AI 使用量レポート、プレミアムリクエスト使用量レポート、REST API によるエクスポート。集計版の使用量レポートは対象外
- 対象プラン: GitHub Enterprise Cloud の全アカウント種別と、GitHub Team の単独組織
- ほかの変化: 削除済みアカウントの使用量は、空のユーザー名で1行にまとめず別々の行で出す。行ごとに丸めるため、合計値が小数点以下の末尾でわずかに変わることがある

出典:
- https://github.blog/changelog/2026-11-23-usage-reports-will-include-a-user-id-column-starting-december-1

### 3. [料金+新機能] Anthropic が Claude Ship を出した — Code Review は指摘を書く単体機能から、修正と承認まで進める PR 運用の一部になり、PR Steward は上限を設定するまで費用に上限がない

**要点**: Anthropic が Team / Enterprise の GitHub リポジトリ向けに Claude Ship を出した。Code Review（GA）に、CI 失敗やコンフリクトを直す PR Steward と、ポリシーファイルで定型の変更を承認する Claude Approvals（どちらも beta）が加わった。費用はプラン枠外のトークン課金で、既存の Code Review の設定も新しい画面に移った。

**詳細**: 製品ブログ（11/23）、Claude Code ドキュメントの「Claude Ship」ページ、The Decoder（11/24）による（Master・industry）。
- Code Review: レビューの深さを Quick / Standard / Deep からリポジトリごとに選ぶ。重大度順のインラインコメントで指摘する
- PR Steward: 失敗したチェック・マージ競合・レビューコメントに対して修正コミットを push し、push のたびに変更内容と戻し方をコメントする。`@claude` で指示、`@claude stop` で停止する。承認とマージはしない
- Claude Approvals: 既定ブランチの `.claude/approvals.yml` で、パスごとに必要な人数と Claude が承認してよい範囲を決める。観察モードで始め、そのあと branch protection で必須にする手順を推奨している。自動マージかマージキューと組み、人の承認を求めないポリシーにすると誰も操作しないままマージされる
- 課金: どのエージェントも使用量クレジット（プラン内の利用枠とは別）でトークン課金される。Code Review と PR Steward は管理者が支出上限を設定できる。Approvals は観察モードでも課金され、組織設定で使用量クレジットを止めても有効なエージェントは動き続ける
- 既存の Code Review 利用者: 設定は「Organization settings > Claude Ship」に移った。`approvals.yml` を置くと、`claude/code_review` を指定したルールがないパスでは自動レビューが止まる
- Claude Code / デスクトップアプリ: `/ship` で push・PR 作成・レビュー・修正を自分で回せる（11/23 から順次）
- 対象外: ZDR・HIPAA 構成・顧客管理の暗号鍵（CMEK）を使う組織。対象の Enterprise 組織は **$10,000** 以上のクレジットを 2027-01-15 まで請求でき、請求から30日以内に使う
- 実績: Claude Code チームでは 6〜9月にマージ済み PR が2倍超になり、revert の割合が40%超減った

出典:
- https://claude.com/resources/articles/introducing-claude-ship
- https://code.claude.com/docs/en/claude-ship
- https://the-decoder.com/anthropics-claude-ship-lets-ai-agents-review-fix-and-approve-pull-requests-on-their-own/

## カテゴリ別まとめ

### Anthropic / Claude

- **Claude Ship の公開**（ハイライト3参照）
- [新機能+予定] **Claude Code `2.1.331`** — Anthropic が changelog を公開し、Code Mode が Bedrock / Google Cloud Agent Platform / Microsoft Foundry / Claude Platform on AWS の端末セッションで使えるようになった。npm の `latest` も `2.1.331` に進み、`stable` は `2.1.323` から `2.1.325` に進んだ。課金付き分類フォールバックの削除は今回も書かれていない（Master・industry）
  - 管理設定: managed の `extraKnownMarketplaces` に載せたマーケットプレイスが、11/30 以降の版で既定で自動更新になる。外すには該当エントリに `"autoUpdate": false`
  - Windows: レジストリの `HKLM` ポリシーは `managed-settings.json` より優先され、壊れた値は起動を止める。日本語など非 ASCII を含むレジストリ設定で起動しない不具合も直した
  - Claude apps gateway: `oidc.groups_jsonpath` と `CLAUDE_GATEWAY_IDP_CONNECT_BY_HOSTNAME=1` を追加した
  - 運用: `claude doctor` に API 疎通の節、OTel の `claude_code.llm_request` に `gen_ai.usage.*` を追加した。プラグイン manifest に `optionalDependencies` が入った
  - VS Code: VS Code を Node として動かすラッパー・フック・MCP サーバーは `ELECTRON_RUN_AS_NODE=1` の設定が必要になった。`allowManagedPermissionRulesOnly` 下の許可カードは Yes / No だけになった
  - https://code.claude.com/docs/en/changelog
- [新機能] **Skills over MCP と MCP の Tasks・Elicitation** — Anthropic が 11/24、MCP サーバーが Claude にスキルを配れる Skills over MCP を Claude と Claude Code で public beta にし、Tasks（長時間処理を裏で走らせ後で結果を取る）と Elicitation（途中でフォームやリンクで利用者に確認する）を GA にした。Pro / Max / Ultra は既定オン、Team は管理者が有効化し、Enterprise は近日である（Master・industry）
  - 規模: MCP SDK の月間ダウンロードは7億超、Claude 向けコネクタは1万超。Tool Search は複数サーバー構成でコンテキストの使用量を85%超減らせるという
  - File Uploads（PDF や表をコンテキストを経由せずサーバーへ送る）は近日
  - https://claude.com/resources/articles/skills-over-mcp-tasks-and-more
- [新機能] **月次の振り返り（Reflect）の正式提供** — Anthropic が 11/24、Settings の Reflect を Free / Pro / Max / Ultra で beta から正式にした。Claude Code のセッションとクラウドの Cowork タスクも振り返りの材料になり、保存された振り返りを削除できる（Master）
  - https://support.claude.com/en/articles/12138966-release-notes
- [据え置き] **Anthropic のその他の一次** — Platform release notes（最上位 11/23）、モデル退役一覧（Active 16件・廃止履歴 11/23 の Opus 4.5）、`/news`（11/20）、`/research`（11/17）は動いていない。`claude.com` の 11/23 付「coding agents の守り方」ガイドと KPMG インタビューは新しい発表を含まない（Master・industry）

### OpenAI / Codex / ChatGPT

- [料金+新機能] **Responses API の医療向けモデル構成** — OpenAI が 11/24、臨床の質問向けの harness と組んだ Healthcare model configurations を出した。web search は医療情報源の専用インデックスを引く。単価（100万トークンあたり・短いコンテキスト）は期間限定価格で、少なくとも 2026-12-31 まで続く（Master・industry）
  - `gpt-6.2-astra-healthcare`: $8 / $40（長いコンテキストは $16 / $60）
  - `gpt-6.2-sol-healthcare`: $2 / $10（同 $4 / $15）
  - `gpt-6-astra-healthcare` と `gpt-6.1-sol-healthcare`: $10 / $50 と $2 / $10
  - 同日 API の `chat-latest` も ChatGPT の現行モデル（11/23 の GPT-6.2）に更新された（$5 / $30）
  - https://developers.openai.com/api/docs/changelog
- [新機能] **Codex CLI `0.172.0`** — OpenAI が 11/24 に安定版を出し、スラッシュコマンドの引数を Tab で補完できるようになった。ツール一覧をキャッシュした stdio MCP サーバーは初回のツール呼び出しで起動するのが既定になり、Code Mode は全接続を gRPC にして `code_mode_host_grpc` 設定を非推奨にした（Master）
  - 接続アプリのツールごとに承認者を `config.toml` で設定でき、app-server のクライアントは Amazon Bedrock Runtime を選べる
  - `codex exec resume` が保存済みのサンドボックス権限・作業ディレクトリ・workspace roots を復元する
  - Codex アプリ（11/23）は CSV のテーブル表示を足した。pre-release は `0.174.0-alpha.2`（11/24）
  - https://github.com/openai/codex/releases
- [セキュリティ] **OpenAI と Cisco の OSS「Shirudo」** — OpenAI と Cisco が 11/23、パッチ適用までの間 eBPF で稼働中の Linux サービスを守る Shirudo を公開した。攻撃が必要とする挙動だけを再起動なしで止める「shield」を入れ、Elasticsearch への攻撃向け shield は Codex で生成した。ライセンスは BSD 2-Clause（Master・industry）
  - https://openai.com/index/introducing-shirudo/
- [動向] **Dots の EU 提供と GPT-6.2 の system card** — TestingCatalog が、OpenAI が Dots を EU で提供し始めたと報じた（二次・一次未確認）。11/23 には Deployment Safety Hub に「GPT-6.2 in ChatGPT System Card」が加わった（Master）
  - https://deploymentsafety.openai.com/gpt-6-2-chatgpt
- [据え置き] **OpenAI のその他の一次** — deprecations（最新告知 11/18）、community Announcements（11/20）、ChatGPT release notes（11/23 GPT-6.2）、misalignment reports（First posted 最新 11/18）は動いていない。GPT-5.6 Sol の期間限定価格は「until November 30, 2026」のままである（Master・industry）

### GitHub Copilot / GitHub

- **使用量レポートへの `user_id` 列の追加**（ハイライト2参照）
- [破壊的変更+新機能] **Copilot CLI `v1.0.115`** — GitHub が 11/24 に安定版を出し、空の `--available-tools=` の意味が「全ツール」から「ツールなし」に反転した。Windows のサンドボックスではパッケージ照会が既定オンになり、CLI を自動化で呼ぶ設定は挙動が変わる（Master）
  - `--max-ai-credits` と `--resume` / `--continue` の併用: 再開したセッションの上限として効くようになった（以前は無視）
  - フックの許可確認で Esc: ターンを止めるようになった（以前はエージェントが続行）
  - Windows サンドボックス: パッケージ照会を止めるには `sandbox.userPolicy.capabilities` を `[]` にする。拒否パスの glob が100件を超えて一致するとコマンドが起動に失敗する
  - 追加: `/model` でカスタムプロバイダーのモデルを管理でき、Gemini 4 Hydrogen・GPT-6.2 Astra・MAI-Code-2-Flash を picker に加えた。pre-release は `v1.0.116-0`（11/24）
  - https://github.com/github/copilot-cli/releases
- [据え置き] **GitHub changelog の Copilot ラベル** — `github.blog/changelog` の Copilot ラベルは 11/18 から動いていない（Master）

### Copilot Studio / Power Platform

- [仕様] **ガイダンスハブの Microsoft Copilot ハーネス移行記事** — Microsoft が Copilot Studio のガイダンスハブ11月節（11/24 19:06Z `fb3f2a93`）に新規記事を加え、うち15本が本日はじめて載った。移行の記事は、Adaptive Cards の表示・入力、システムトピックによるメッセージの横取り、グラウンディング限定のトグルに代わる機能が Copilot ハーネスに無いと明記し、移行は部品の置き換えではなく作り直しとして扱う（Copilot）
  - `migrate-harness`: システム変数が無く、利用者の部署・役割はツールで取りに行く。Power Fx はサンドボックスのコード（Python・bash）かワークフローに移す
  - 標準ハーネスに残す条件: 決まった会話順序と決定的な引き継ぎ、Adaptive Cards が中心の対話、応答の速さが推論の深さより大事な大量対話
  - `workflows-credit-consumption`: 1アクションごとに 0.13 クレジットを消費し、AI ノードは従量課金がその上に乗る。Copilot ノードは利用者が M365 Copilot ライセンスを持っていればライセンスで賄われる
  - `technical-readiness`: 旧来のエージェント種別の説明を、ハーネスの選び方とエージェント／ワークフローの選び方に置き換えた
  - https://learn.microsoft.com/en-us/microsoft-copilot-studio/guidance/whats-new
- [仕様] **クレジット枯渇時の挙動ページの改訂** — Microsoft が `enforcement-policy-credits`（11/24 19:06Z `75df1f39`）を改訂した。環境のクレジットが尽きると利用者への応答が止まり、メーカーも自然言語での作成・プレビューとテスト・評価の生成ができなくなると本文が書いている。前回の本文を残していないため、どの記述が加わったかは特定できない（Copilot）
  - https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-experience/enforcement-policy-credits
- [新機能] **Link to Fabric のリージョン横断** — Microsoft が 11/24、Dataverse 環境と Fabric ワークスペースのリージョンが違っても Link to Fabric を作れるようにした（GA）。既存リンクの接続を作り直さずに差し替える Update connection も、11月末までに全リージョンへ展開する（Copilot）
  - https://www.microsoft.com/en-us/power-platform/blog/2026/11/24/now-available-cross-region-link-to-fabric-and-update-connection/
- [据え置き] **Copilot Studio と Power Platform のその他の一次** — Copilot Studio What's New（`1e58d09d`）、ハーネスと課金のページ、レート表、PPAC 容量管理、モデル表、非推奨一覧（`a406dde7`）は前日のまま変化がない。Released Versions も 2026.6.3 のままである（Copilot）
  - https://learn.microsoft.com/en-us/microsoft-copilot-studio/whats-new

### Microsoft 365 Copilot

- [新機能] **SPFx の Copilot UX コンポーネントを Cowork のプラグインで配布** — Microsoft が 11/24、開発者が SPFx で作った Copilot UX コンポーネントをスキルとともにプラグインにまとめ、通常の Copilot チャットと Cowork に出せるようにした。管理者は M365 管理センターの Agents > Tools で全社・ユーザー・グループ単位に配布・許可・ブロックでき、社内 UI の配布単位が宣言型エージェントからプラグインに移る（Copilot）
  - 制約: 現時点ではプラグインのパッケージを手作業で組む。利用者には Microsoft Copilot ライセンスが必要
  - 次の予定: SharePoint の単一ページアプリ（SPA）モデルが SPFx 1.25 でプレビューに入る計画。開発者アンケートは 12/2 まで
  - https://devblogs.microsoft.com/microsoft365dev/copilot-ux-components-now-available-in-cowork-with-plugins-spfx-roadmap-update-for-november-2026/
- [予定] **Office の Copilot のメモリによる個人化** — Microsoft が Roadmap 580889（11/24 起票）で、Word・Excel・PowerPoint と Workspaces の Copilot がメモリで利用者の作業パターンを学ぶと告知した。プレビュー・GA とも November CY2026 で、状態は `In development` である（Copilot）
  - https://www.microsoft.com/microsoft-365/roadmap?id=580889
- [予定] **Message Center の展開日程の更新** — Microsoft が 11/24 に既報の4件を更新し、Mac の PowerPoint の Copilot のプラグイン（MC1556095）と低評価フィードバックのカテゴリ選択（MC1530595）の展開完了を12月上旬とした。MC1550540 と MC1558023 の日程は変わっていない（Copilot）
  - https://mc.merill.net/message/MC1556095
- [観測] **Roadmap の新規バッチ** — Release Communications の API と RSS は 2,401 項目を返し、前日の 2,389 から12件増えた。11/24 00:13Z のバッチで Copilot 関連の起票は 580889 の1件だけで、Copilot Studio タグは33件のままである（Copilot）
  - https://www.microsoft.com/releasecommunications/api/v1/m365
- [据え置き] **Release Notes・Purview・Cowork・Partner Center** — M365 Copilot Release Notes（先頭 November 17）、Purview・拡張機能・Cowork の What's New、Cowork のモデル・管理者統制、Partner Center 11月ページは前日のまま変化がない。Copilot ブログと TC の各 board にも新しい記事は無い（Copilot）
  - https://learn.microsoft.com/en-us/microsoft-365/copilot/release-notes

### Google

- **Workspace の MCP サーバーと CLI の GA**（ハイライト1参照）
- [新機能] **Gemini Notebook の Flashcards** — Google が 11/24、Gemini Notebook の Flashcards に学習向けの機能を追加した（Master）
  - http://workspaceupdates.googleblog.com/2026/11/new-study-enhancements-for-flashcards-in-Gemini-Notebook.html
- [観測] **Gemini API changelog に届かない** — Gemini API changelog は転送先 `aistudio.google.com` に届かないままである。Gemini アプリ（11/19 Computer use）は動いていない（Master・B-088）

### 開発ツール・エージェント

- [新機能] **Devin の 11/23 更新** — Cognition が、管理者がマーケットプレイスのプラグインを「必須」ではなく「提供」にでき、MCP ツールの承認カードでそのツールをセッション中ずっと許可できるようにした。新しいカスタム MCP サーバーは自動認証が既定になり、コードスキャンを誰が取り消したかを監査ログに残す（Master）
  - https://docs.devin.ai/release-notes/overview
- [版更新] **Orca `v1.4.273`** — Stably AI が 11/24 に出し、Claude のプラン名表示を Max / Ultra に直し、zcode-app-cli と Droid にステータスフックを足した。対応エージェントの追加と破壊的変更は無い（Master）
  - https://github.com/stablyai/orca/releases
- [動向] **MCP の2周年** — MCP blog が 11/24、MCP の2周年を振り返る記事を出した。公開以来のコントリビューターは2,500人を超え、仕様や拡張の新しい発表は含まない（Master）
  - https://blog.modelcontextprotocol.io/posts/mcp-turns-two/
- [据え置き] **Cursor・xAI・TypeSafe AI・Hugging Face・Obsidian** — Cursor の changelog（11/6）とフォーラム（10/12）、xAI（11/19・grok-4.7）、TypeSafe AI（9件）、Obsidian（1.15.1）は動いていない。Hugging Face の8 org にも新しいリポジトリは無い（Master・industry）

### 市場・セキュリティ

- [セキュリティ] **ARTEX のエージェントによる API キー窃取** — Amazon の脅威インテリジェンスが AWS Security Blog で、攻撃者が ARTEX（OSS の AI ペネトレーションテスト基盤）のエージェントで公開された AI アプリから上流プロバイダーの API キーを抜き取り、検証して共有プールへためていたと報告した。標的は LiteLLM・One API・Veloera などの LLM ゲートウェイと FastGPT・Dify などで、観測期間は 10/3〜11/5 である。Ars Technica は「ゼロデイを見つけて悪用した」と書く一方、Amazon は「手口に新しいものはない」と述べたとされ、報道は割れている。AWS ブログの本文は未確認（industry）
  - https://aws.amazon.com/blogs/security/amazon-threat-intelligence-observes-threat-actors-running-cybercrime-campaigns-with-artex-ai-agents/
- [据え置き] **Nvidia × Inception、Nvidia × Reflection AI** — 2件の買収協議に続報はない。AP は 11/24、Nvidia や Anthropic などの AI 株が再び下げたと報じた。MM総研・IDC Japan の新しい公表も見つからなかった（industry）

## 直近の注目予定

- **11月下旬**: Copilot ライセンスの無い利用者の検索画面が新しくなる（MC1562275）。Copilot Code のローカル Sandbox が既定でオンになる（MC1519871）。Link to Fabric の Update connection が全リージョンに行き渡る
- **11月中**: GitHub の cloud sandbox の課金が始まる（日付は明記なし）
- **11/29**: OpenAI が Daybreak Blue のセッションデータの学習利用を始める（二次）
- **11/30**: `claude-sonnet-4-5-20250929` が退役し、Opus 4.8 の fast mode が削除される。OpenAI の `/v1/prompts`・Evals・Agent Builder が停止する。Power Automate デザイナーの Copilot と Copilot Studio の Mistral Medium 3.5 が退役する。GPT-5.6 Sol の期間限定価格と Gemini 4 Argon・Carbon の導入価格が終わる。この日以降の Claude Code で managed マーケットプレイスの自動更新が既定でオンになる
- **12/1**: GitHub の使用量レポートに `user_id` 列が加わる。PPAC のデータエクスポートがインベントリを出力しなくなる。OpenAI `gpt-image-1-mini` / `gpt-image-1.5` / `chatgpt-image-latest` が停止する。Gemini 4 Argon・Carbon の単価が $4/$20 に倍増する。Copilot Studio のワークフローの Code ノードが GA になる
- **12/2**: GitHub が公開リポジトリの `pull_request_target` を既定でブロックする。Power Platform のプロンプトから Anthropic・Grok・旧 GPT 系が退役する（MC1536101）
- **12/3**: Agent ノードからのファイル生成が GA になる（MC1561859）
- **12月上旬**: Teams のチャネル単位の Copilot がパブリックプレビューに入る（MC1562277）。Mac の PowerPoint の Copilot のプラグインの展開が終わる（MC1556095）
- **12/8**: GitHub が活動の無いリポジトリの Dependabot アラートを停止し、ARM32 ジョブのサポートを終える。Dataverse のエージェントユーザーが GA、M365 Copilot in Power BI が既定でオンになる
- **12/9**: EU / EFTA / UK で Claude モデルが既定で有効になる（MC1546438）
- **12/11**: OpenAI `gpt-5` 系 / `o3` / `o3-pro` が停止する。ChatGPT の Advanced / Standard 音声モードが退役する（二次）
- **12/14**: Copilot から Claude Fable 5 / Haiku 4.5 / Gemini 3.8 Flash / Gemini 4 Argon / Grok 4.6 / Kimi K3 が廃止される。claude.ai/design の単体サイトが閉鎖する
- **12/15**: アンマネージドの開発者環境の削除が始まる（MC1515303）
- **12月中旬**: Copilot デスクトップアプリと Edge の同期が展開される（MC1562269）。Chat と Office のモデルの従量課金が GA になる（MC1557754）
- **12月中**: ChatGPT と Codex の利用枠が Plus・Pro・Business で1つの予算に統合される（二次）
- **12/17**: Copilot Studio のワークフローのサービスプリンシパル認証が GA になる（MC1557509）
- **12/18**: Copilot から MAI-Code-1.1-Flash が廃止される
- **12/31**: Copilot の Fable 5 系の ZDR 例外が終わる（以後は EFS が必要）。Claude Security の無償クレジットの対象期間が終わる。OpenAI の医療向けモデル構成の期間限定価格が最短でこの日に終わる
- **2027-01-01**: Anthropic の新しい開示期限（高・重大度30日）が、この日以降の報告に適用される
- **2027-01-03**: Copilot デスクトップアプリのアプリ内ブラウズの既定オンに備える期限（MC1560922）
- **2027-01-06**: OpenAI `tts-1` / `tts-1-hd` / `gpt-4o-mini-tts` が停止し、セルフサービスの fine-tuning ジョブ作成が制限される
- **2027-01-11**: OpenAI の EU データレジデンシーで GPT-5.2 / 5.4 / 5.4 mini の `fast` / `priority` 処理が停止する
- **2027-01-14**: OpenAI `gpt-4o` / `gpt-4o-mini` / `gpt-4.1` / `gpt-4.1-mini` が停止する
- **2027-01-15**: アンマネージドの開発者環境が完全に削除される。Claude Code Review / Claude Ship の Enterprise 向けクレジットの請求期限
- **2027-01-20**: OpenAI `gpt-realtime` / `gpt-audio` 系が停止する
- **2027-01-22**: `claude-opus-4-5-20251101` / `claude-opus-4-5` が Claude API から退役する
- **2027-01-30**: ChatGPT Classic（旧デスクトップアプリ）が終了する（二次）
- **2027-02-01**: Google Workspace で外部 AI エージェントの MCP 利用の強制が始まる（REST の直接呼び出し不可）。OpenAI `gpt-5.5-cyber-preview` が停止する
- **2027年2月**: VS Code の Copilot から Local harness が削除される
- **2027-02-10**: OpenAI `gpt-image-2` が停止する。Claude Meetings の成果物の無料期間が終わる
- **2027-02-15**: Copilot Studio の Claude Opus 4.8・Opus 5・Sonnet 4.6・Sonnet 5 が退役する
- **2027-02-26**: OpenAI `/v1/audio/translations` が停止する
- **2027-03-01**: GPT-6.2 Astra・Sol の Ultrafast が Standard の3倍から6倍になる
- **2027-03-30**: MCP 仕様 `2027-03-30` 版のリリース予定
- **2027-04-01**: Google Workspace API の Scaled 枠の課金が始まる（標準枠超過のプロジェクトは指定しないと上限が戻る）。OpenAI `gpt-5.1` / `gpt-5.3-codex` / `gpt-5.4-nano` が停止する
- **2027-05-17**: GitHub Copilot の MAI Code 2・MAI Code 2 Flash の導入価格が終わり、単価が倍になる
- **2027-09-15**: Dataverse for Teams 環境の削除が始まる（MC1515294）

## 改善メモ

- Master: 新規提案・障害の変化なし。継続提案の最多は B-088（Gemini API changelog の URL 差し替え、22回目）。11-24 に `claude.com` 一覧の 11/23 付 Claude Ship を取りこぼしたため、本サマリーでも前日には載らず本日はじめて載った
- Copilot: 新規提案・障害の変化なし。継続提案 5件（最多: B-080 Cowork の Learn URL の移設、27回目）
- industry: `thehackernews.com` がゲートウェイ拒否（新規）。継続提案 7件（最多: B-048 Gemini 一次 URL、23回目）。見送り候補 B-036
- ソース間の差: Claude Ship の公開日を Master は 11/23（製品ブログ）、industry は 11/24（The Decoder の報道日）とした。本サマリーは一次の 11/23 を採った。タグは Master が `[新機能]`、industry が `[料金+新機能]` で、本サマリーは新製品の付随課金として `[料金+新機能]` を採った
- ソース間の差: 医療向けモデル構成を Master は `[新機能]`、industry は `[料金]` とした。本サマリーは新しい提供面に単価が付く型として `[料金+新機能]` を採った
- ソース間の差: ChatGPT の GPT-6.2 は前日のサマリーに収録済みのため、本日は API の `chat-latest` 更新だけを医療向けモデル構成の項目に添えた
