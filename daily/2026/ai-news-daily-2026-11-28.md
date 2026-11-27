# AI News Daily Summary — 2026-11-28

GitHub は Copilot CLI の安定版 `v1.0.117` を出し、TLS を中継する社内プロキシの下でも sandbox 内のコマンドが追加の CA を信頼できるようにした。Stably AI は Orca `v1.4.280` で、使用量の確認やコミットメッセージの作成に Antigravity の `agy` を使うのをやめた。米国の感謝祭明けで、Anthropic・OpenAI・Google・Microsoft の一次ソースはほぼ動いていない。

## 今日のハイライト

### 1. [新機能] GitHub が Copilot CLI `v1.0.117` で sandbox に社内 CA を渡せるようにした — TLS を中継する企業プロキシの下で sandbox を切って使う前提が変わる

**要点**: GitHub が 11/27 に Copilot CLI の安定版 `v1.0.117` を出した。`sandbox.userPolicy.network.extraCaCertificates` をユーザー設定か管理設定に書くと、sandbox 内のコマンドが追加の CA 証明書を信頼する。社内プロキシが TLS を中継する組織でも、sandbox を有効にしたまま通信できる。

**詳細**: 前の安定版は `v1.0.116`（11/25）で、pre-release `v1.0.117-0`〜`-5` の内容をまとめた版である。リリース本文に「破壊的変更」の表記は無い（Master）。
- 権限: MCP サーバーの名前が組み込みの権限種別と同じでも、そのツールの承認で組み込みの要求まで承認されなくなった。autopilot で始めると、拡張を起動する前に1件ずつ確認する（従来は承認者がいないとして全て拒否していた）
- sandbox: 書き込める git worktree の中でも、リポジトリの設定ファイルは sandbox のコマンドとエージェントの編集から読み取り専用になる。リンクした worktree での commit・branch 作成・stash が再び動く
- カスタムエージェント: 使うツールを選んで有効にできる。サブエージェントは、プロンプトが無いエージェントファイルでもツール一覧に従う
- モデル: リポジトリが使えない提供元のモデルを固定しているとき、黙って提供元を切り替えずにエラーを出す。`/model` の選択画面にサービスの告知と退役予定の印が出る
- Assisted Permissions: plan mode ではブランチ作成とパッケージのインストールの前に確認する

出典:
- https://github.com/github/copilot-cli/releases/tag/v1.0.117

### 2. [破壊的変更+新機能] Stably AI が Orca `v1.4.280` で、使用量の表示・bot のアバター・コミットメッセージの生成に `agy` を使うのをやめた — Antigravity は CLI とチャットからだけ使う前提に変わった

**要点**: Stably AI が 11/27 に Orca `v1.4.279` と `v1.4.280` を出した。`v1.4.280` は使用量メーターの残量確認、bot のアバター生成、コミットメッセージなどソース管理の文面の作成に `agy` を使わなくした。前日の Gemini CLI 削除に続き、Orca は Google 系エージェントの使い道を絞っている。

**詳細**: Master による。
- `v1.4.280`（11/27・Latest）の Bot: グループのルームとスレッドをタブから名前変更できる。使用上限で止まった bot に琥珀色のゲージが付き、Slack では依頼を受けたスレッドか DM に結果を返す
- `v1.4.280` のチャット: エージェントの質問が入力欄の上に出る。Antigravity のチャットは最初のメッセージ前から `/` でコマンドとスキルが出て、上限で止まるとリセット時刻を示し、その後に再開できる
- `v1.4.280` の WSL: Codex のモデルとプラグインの変更が Linux ディストリビューション側に保存される。予告としてサイドバーと PR レビューの作り直し、アカウントの自動切り替え、入力欄でのハーネスの切り替えを挙げた
- `v1.4.279`（11/27）: 設定を読み直したときに Codex / Cursor / Copilot / Kiro の既存フックを認識し、Droid のカスタムフックを残す。Git レビューの配置とブラウザ注釈パレットが移った

出典:
- https://github.com/stablyai/orca/releases

## カテゴリ別まとめ

### GitHub Copilot / GitHub

- **Copilot CLI `v1.0.117`**（ハイライト1参照）
- [据え置き] **github.blog の Copilot ラベル** — GitHub の changelog は 11/25 の code review 課金の告知が最上位のままで、新しい記事は無い（Master・industry）
  - https://github.blog/changelog/label/copilot/

### 開発ツール・エージェント

- **Orca `v1.4.280`**（ハイライト2参照）
- [新機能] **Devin の共有と Bot の更新** — Cognition が Devin に 11/26 付の更新を入れ、Enterprise 管理者は「Creator only」に制限されたセッションにも書き込み権限つきで自分を足せるようになった（11/25 付では読み取り専用だった）（Master）
  - 共有: 共有ダイアログが所有者と実際のアクセス権を表示し、アカウントのポリシーが共有を禁じるときは共有を隠す
  - Bot: Enterprise Grid では「Slack ワークスペースの誰でも」に設定した Bot に DM とメンションが届く
  - Automations: v3 API の `notifications.slack` で、起動状況の通知を Slack チャンネルに流せる
  - その他: Oncall の応答とインシデント設定で応答言語を選べる。削除したファイルの中身を Changes ペインで見られる
  - https://docs.devin.ai/release-notes/overview
- [据え置き] **Cursor・xAI・TypeSafe AI・MCP・Hugging Face・Obsidian・Apple** — Cursor の changelog（11/6）とフォーラム（10/12）、xAI（11/19）、TypeSafe AI（9件）、MCP blog（11/24）、Obsidian（1.15.1）、Apple Developer News（11/18）は動いていない。Hugging Face の8 org にも新しいリポジトリは無い（Master）

### Anthropic / Claude

- [新機能] **Claude Duet の日本提供** — Anthropic の製品ページが Claude Duet の提供地域を米国・インド・インドネシア・ブラジル・日本と記載し、日本の Pro・Max・Ultra 利用者もウェイトリストに申し込めるようになった。10/21 の公開時は米国のみだった。Team・Enterprise は対象外で、リサーチプレビューのままである。日本の開始日は製品ページに書かれていない（CNET Japan が「日本上陸」と報じた）（industry）
  - https://claude.com/product/claude-duet
- [据え置き] **Anthropic の一次** — Claude Code（`2.1.332`・npm `stable` は `2.1.326`）、Platform release notes（11/23 付6項目）、モデル退役一覧（Active 16件・最新告知 11/23 Opus 4.5）、`/news`（11/20）、`/research`（11/25）、`claude.com/resources/articles`（11/24）、`support.claude.com`（11/24）は動いていない（Master・industry）

### OpenAI / Codex / ChatGPT

- [動向] **業務データの意味層「Athena」** — The Decoder（11/27）は The Information の報道として、OpenAI が売上や顧客数などの指標の定義をエージェントに与えるデータ基盤「Athena」を開発していると報じた。ChatGPT Work のデータ分析エージェントの精度が足りないとした顧客がいたという。初期開発段階で、時期・料金は未公表である（industry）
  - https://the-decoder.com/openai-is-building-athena-data-platform-to-cut-down-on-ai-agent-guesswork/
- [版更新] **Codex の pre-release `0.174.0-alpha.9`** — OpenAI の Codex は安定版 `0.172.0`（11/24）のまま、pre-release が `0.174.0-alpha.9`（11/27）に進んだ。alpha のリリース本文は版番号だけである（Master）
  - https://github.com/openai/codex/releases
- [据え置き] **OpenAI の一次** — API changelog（11/24）、deprecations、community Announcements（11/20）、`openai.com/news`（11/24）、ChatGPT release notes（11/23）、ChatGPT & Codex changelog（11/24）、Deployment Safety Hub（11/23）、misalignment reports（First posted 最新 11/18・29件）は動いていない（Master・industry）

### Google

- [仕様] **Workspace の REST API 経由のエージェントの扱い** — GIGAZINE（11/27）は、2027-02-01 以降に REST API へ直接アクセスする AI エージェントの利用上限が、有料プランでも無料プランと同じ水準になると報じた。Google Cloud ブログ（11/25）にこの記述は無く、出典の開発者ドキュメントには到達できていない。GA と 2/1 の MCP 移行の強制、4/1 の利用枠の課金は 11/25 のサマリーに収録済みである（industry）
  - Gmail MCP: 送信・返信・下書き編集をパートナー限定としていた注記が、GIGAZINE によると 11/27 に開発者ドキュメントから削除された
  - 人の承認: メール送信・Drive の共有権限の変更・一括編集の前に、利用者の明示的な確認を求める（ブログ）
  - https://cloud.google.com/blog/products/identity-security/deploying-agents-safely-in-your-enterprise
  - https://gigazine.net/news/20261127-google-workspace-ai-tools-mcp/
- [予定] **Antigravity の Bundles とエージェント作成画面** — TestingCatalog が、Google が Antigravity にワークフローや職種ごとのプラグインをまとめる Bundles とエージェントの作成画面を用意しているとの観測を報じた（二次・未公開・リリース日なし）。Google の Varun Mohan 氏は X で、使用量のリセットを貯めて使う仕組みを作っていると書いた（Master）
  - https://www.testingcatalog.com/google-develops-bundles-and-agent-creation-for-antigravity/
- [据え置き] **Gemini アプリ・The Keyword・Workspace Updates** — Gemini アプリ（11/19）と The Keyword の AI カテゴリ（11/24）は動いていない。Workspace Updates の 11/27 付週次まとめは既報の再掲だった。Gemini API changelog は転送先 `aistudio.google.com` に届かないままである（Master）

### Microsoft 365 Copilot / Copilot Studio / Power Platform

- [観測] **Copilot Studio のハーネス概要ページの再ビルド** — Learn が `harnesses-overview` を 11/27 19:03Z に `828ea3ea` へ差し替えたが、`ms.date` は 11/13 のままである。本文の3種類のハーネスの比較表は 11/18 に載せた構成と変わらず、前回の本文が残っていないため差分は特定できない（Copilot）
  - https://learn.microsoft.com/en-us/microsoft-copilot-studio/harnesses-overview
- [据え置き] **Message Center・Roadmap・Learn・ブログ** — Message Center は 11/25 23:41Z の MC1568702 より新しい通知が無く、Roadmap も 11/26 00:16Z のバッチ以降は動いていない（総項目数 2,420）。M365 Copilot Release Notes（先頭 November 17）、Cowork のページ群、Partner Center 11月、Purview、Copilot Studio の What's New と課金・モデル表、非推奨一覧は前日から変わっていない。Partner Center の12月ページはまだ 404 である（Copilot）
  - https://www.microsoft.com/releasecommunications/api/v2/m365/rss

### 市場・企業

- [動向] **SAP の1万人削減の報道** — The Decoder（11/27）は Bloomberg の報道として、SAP が AI への再編で少なくとも1万人（全世界の従業員11万人超の9%以上）を削減する方向だと報じた。製品開発・エンジニアリング・営業が中心で、人数は労使交渉で変わりうる。SAP はコメントしていない（industry）
  - https://the-decoder.com/sap-plans-to-cut-at-least-10000-jobs-as-it-pivots-to-ai/
- [動向] **OpenAI による Apple の反訴** — The Decoder（11/27）は Financial Times の報道として、OpenAI がカリフォルニア州の裁判所で Apple を企業秘密の窃取で反訴し、両社に納入するサプライヤーを Apple が威圧したと主張したと報じた。夏に Apple が元社員による情報漏えいで OpenAI を訴えたことへの対抗である（industry）
  - https://the-decoder.com/openai-countersues-apple-over-trade-secret-theft-and-alleged-coercion-of-shared-suppliers/
- [据え置き] **Nvidia × Inception、Nvidia × Reflection AI** — 2件の買収協議に続報はない。MM総研と IDC Japan の新しい公表も見つからなかった（industry）

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
- **2027-03-01**: GPT-6.2 Astra・Sol の Ultrafast が Standard の3倍から6倍になる。Gems が廃止される（Business / Enterprise・この日以降）
- **2027-03-08**: Fable 5.2 ローンチ特典のリセット（Max / Ultra / premium 席）が失効する
- **2027-03-30**: MCP 仕様 `2027-03-30` 版のリリース予定
- **2027年3月**: Dataverse の Filter-based Security（Roadmap 581895）
- **2027-03-31**: Copilot in 30 の試用オファーと M365 E7 AI Activation Offer が終わる
- **2027-04-01**: Google Workspace の AI エージェント向け利用枠の課金が始まる（標準枠超過のプロジェクトは指定しないと上限が戻る）。OpenAI `gpt-5.1` / `gpt-5.3-codex` / `gpt-5.4-nano` が停止する
- **2027-05-17**: GitHub Copilot の MAI Code 2・MAI Code 2 Flash の導入価格が終わり、単価が倍になる
- **2027-09-15**: Dataverse for Teams 環境の削除が始まる（MC1515294）

## 改善メモ

- Master: 新規提案・障害の変化なし。継続提案の最多は B-088（Gemini API changelog の URL 差し替え、25回目）
- Copilot: 新規提案 B-085（追跡中の Learn ページの本文を保存し、`ms.date` 据え置きの再ビルドでも差分を特定できるようにする）。継続提案 6件（最多: B-080 Cowork の Learn URL の移設、30回目）
- industry: 継続提案 7件（最多: B-048 Gemini 一次 URL、26回目）。見送り候補 B-036
- ソース間の差: Master の注目スケジュールは、OpenAI のファインチューニングの新規ジョブ作成の制限を 2027-01-06 のまま載せている（2日連続）。industry は廃止ページで 2026-12-15 への前倒しを確認しており、本サマリーは 12/15 を採った
- ソース間の差: Google Workspace の REST API 経由のエージェントの扱いは、industry がハイライトにしたが、2/1 の強制と 4/1 の課金は 11/25 のサマリーに収録済みのため、本日は GIGAZINE が報じた新しい事実だけを `[仕様]` で載せた
