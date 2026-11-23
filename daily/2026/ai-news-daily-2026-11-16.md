# AI News Daily Summary — 2026-11-16

OpenAI が ChatGPT Enterprise を AWS Marketplace で売り始め、AWS のコミットを導入費に充てられるようになった。M365 の UBB 機能は、既定のままだと全利用者が支出ポリシーを申請できる。Orca 1.4.259 は、終わったワークスペースをルールで自動削除できるようにした。

## 今日のハイライト

### 1. [新機能] ChatGPT Enterprise を AWS Marketplace で買えるようになった — AWS のコミット消化に充てられ、調達の経路が AWS 契約の中に入った

**要点**: OpenAI が 11/9 に ChatGPT Enterprise を AWS Marketplace で提供し始めた。対象の支出は AWS のコミットに算入できるため、AWS と大口契約を持つ企業では、ChatGPT の導入が新規ベンダーとの契約から既存の AWS 予算の使い道の1つに変わった。

**詳細**: industry が TLDR AI の週次スイープ（11/10号）で7日遅れで検知した。一次（`openai.com`）はオリジン403のため、複数の二次報道で突き合わせている。
- 対象: Chat・ChatGPT Work・Codex・dots の一式。ChatGPT for Healthcare・for Financial Services も対象の顧客に提供し、機能は OpenAI と直接契約した場合と同じとしている
- 価格: プライベートオファーで個別に決める。定価は公表されていない
- コミット算入: 対象の支出が算入できるが、顧客と AWS の契約条件による
- 留保: AWS 経由で買ってもデータが AWS 上に留まる保証はない（データ処理者は OpenAI のまま）。ChatGPT 内のクレジット消費が AWS の請求にどう反映されるかは説明されていない

出典:
- https://openai.com/index/chatgpt-enterprise-aws-marketplace/
- https://ppc.land/aws-customers-can-now-buy-chatgpt-enterprise-against-cloud-commitments/

### 2. [仕様] UBB の機能を許可されていない利用者は、既定で全員が支出ポリシーを申請できる — 申請を管理者が受けるか止めるかを、M365 管理センターで先に決める必要がある

**要点**: 支出ポリシーが割り当てられていない利用者が Cowork などの UBB 機能を開いたとき、管理者に申請できるかを決める設定の手順ページが Learn に出た。既定は「All users」なので、何もしなければ全員が申請を出せる。変更には Global Administrator が要る。

**詳細**: `copilot/implement/request-access-usage-based-billing-experiences`（`ms.date` 11/12・`424bb856`）で一次確認した（Copilot）。設定そのものは MC1546354（11/11 既報・11月中旬に提供開始）で告知済みで、本日新たに分かったのは既定値・必要なロール・反映時間の3点。
- 場所: Copilot > Settings > All Settings > Access to usage-based billing experiences
- 選択肢: All users（既定）、Specific users and groups、No users（No users では Advanced AI experiences の Learn more リンクが出る）
- 反映: 最大24時間かかる。申請を受けても、Cost Management で UBB を構成するまで利用はできない

出典:
- https://learn.microsoft.com/en-us/copilot/implement/request-access-usage-based-billing-experiences
- https://mc.merill.net/message/MC1546354

### 3. [新機能] Orca 1.4.259 が終わったワークスペースを自動で消す設定を加えた — worktree の後片付けを手でやる前提が、プロジェクトごとのルールで任せられる形に変わった（既定はオフ）

**要点**: Stably AI が 11/14 に Orca `v1.4.259` を出した。設定に Workspace Cleanup が加わり、自動実行が終わったワークスペースや解放済みワーカーのワークスペースを、プロジェクトごとのルールで自動削除できる。ルールは既定でオフで、オンにすると確認から数秒で消える。

**詳細**: GitHub releases で一次確認した（Master）。
- Workspace Cleanup: Settings → Workspace Cleanup で該当するワークスペースを一覧で確かめてから有効にする。マージ済み・変更なしの作業も対象になる。ペアリングしたデスクトップで未保存の編集があるものは残し、`.env` など無視リストのローカルファイルを消す前には警告を出す。アーカイブの操作は無い
- サブエージェント: 1つのサブエージェントのタスク・進行中の手順・最終回答を専用ビューで開き、元の会話へ戻れる
- Kimi Code: チャットで Kimi のモデル選択・権限制御・`/compact` が使える（Kimi Code 2.5.0 以上とサインインが必要）
- Claude Code / Codex: ノート PC がスリープしても Claude チャットの開始を拒まなくなった。Codex のフック確認画面に Orca のフックが名前つきで出る（macOS / Linux）
- そのほか: 音声入力に Nemotron 3.5 と Parakeet Unified EN を追加した（AI による整形は既定でオフ）。モバイル版とつなぐ場合は電話側のアプリ更新と再接続が要る

出典:
- https://github.com/stablyai/orca/releases/tag/v1.4.259

## カテゴリ別まとめ

### Anthropic / Claude

- [据え置き] **Claude Code と Claude Platform** — Anthropic の Claude Code changelog は `2.1.325`（11/13）が最上位のままで、npm も `{stable: 2.1.311, latest: 2.1.325, next: 2.1.325}` から動いていない。Platform の release notes（11/12）、モデル退役一覧（Active 17件）、廃止履歴（9/30）も変わらない（Master・industry）
  - https://platform.claude.com/docs/en/about-claude/model-deprecations
- [据え置き] **Anthropic の他の一次** — `/news`（11/10 IPO ロードショー）、`/research`（11/13）、`claude.com/resources/articles`（11/13 の2本）、`support.claude.com`（11/12）、Privacy Center（11/9）は動いていない（Master）

### OpenAI / Codex / ChatGPT

- **ChatGPT Enterprise の AWS Marketplace 提供**（ハイライト1参照）
- [新機能] **ChatGPT Wallet** — 9to5Mac などによると、OpenAI が 11/13、エージェント dots が利用者の承認を得て買い物をする ChatGPT Wallet を発表し、まず米国の ChatGPT Pro 利用者に提供する。購入ごとにカードネットワークが1回限りのトークンを発行するため、加盟店にもエージェントにも本物のカード番号は渡らず、購入のたびに Face ID などで承認する（industry）
  - 提携: American Express・Mastercard・Visa。支出上限と事前承認は今後の予定で、時期は示されていない
  - https://9to5mac.com/2026/11/13/openai-launches-chatgpt-wallet-enabling-dot-agents-to-make-purchases/
- [新機能] **MCP Extensions** — OpenAI が、ChatGPT 専用の機能を MCP サーバーに足す MCP Extensions を TypeScript と Python のパッケージとしてオープンソースで公開した。サイドバーの入口や独自のファイルビューアなどを追加できる（TLDR AI 11/12号で検知・industry）
  - https://github.com/openai/mcp-extensions
- [版更新] **Codex CLI 0.171.0-alpha.6** — OpenAI の Codex CLI は安定版が `0.169.0`（11/13）のままで、pre-release が `0.171.0-alpha.6`（11/15）まで進んだ。alpha の本文は版番号だけである（Master）
  - https://github.com/openai/codex/releases
- [観測] **Cursor へのモデル直接提供の終了は一次未確認** — OpenAI が 8/28 に告げた Cursor へのモデル直接提供の終了（11/12）が実際に行われたかを、Master は一次で確かめられなかった。検索で返るのは事前の解説記事とフォーラムの質問だけで、Cursor の changelog とフォーラムの告知（10/12 が最上位）にも言及が無い（Master）
  - https://forum.cursor.com/t/i-heard-openai-is-about-to-cut-off-gpt-access-for-cursor-is-this-true/169876
- [据え置き] **OpenAI の他の一次** — ChatGPT & Codex changelog（11/13）、API changelog（11/5 `gpt-6-cyber`）、deprecations（11/10 GPT Image 2）、Deployment Safety Hub（11/5）、community Announcements（11/10）、misalignment reports（11/12）は動いていない（Master・industry）
  - https://developers.openai.com/api/docs/deprecations

### Google

- [新機能] **Antigravity の `/swarm`** — Google が Antigravity に、複数のエージェントを並列で動かす `/swarm` を加えた。名前付きのエージェントがタスクを分担して共有のメッセージボードで調整し、Google AI Pro・Ultra で App と CLI の両方から使える。ワーカーごとに別のエージェントとして動くため、クォータの消費は単一の会話より速い（TLDR AI 11/11号で検知・industry）
  - https://antigravity.google/docs/swarm/
- [観測] **Gemini API の一次に届かない** — Gemini API changelog の転送先 `aistudio.google.com` に本日も届かず、検索で見える最新は 10/26〜10/27 の項目である。Live / TTS preview の停止日は deprecations 表のキャッシュでしか確かめられない（11/23 訂正: 一次では 11/17 に止まるモデルは無い）。Gemini アプリ（2026.10.13）、Workspace Updates（11/13）、The Keyword（11/12）も動いていない（Master・industry）
  - https://ai.google.dev/gemini-api/docs/deprecations

### GitHub Copilot / Microsoft 開発ツール

- [据え置き] **Copilot changelog と Copilot CLI** — GitHub の Copilot changelog は 11/13 の12月6モデル廃止告知が最上位のままで、Copilot CLI も安定版 `v1.0.112`（11/13）から進んでいない。Windows Command Line ブログは 11/4 の Intelligent Terminal 0.3 が最新のまま（Master）
  - https://github.blog/changelog/label/copilot/

### Microsoft 365 Copilot

- **UBB の利用申請の既定値**（ハイライト2参照）
- [仕様] **Cowork の役割別・業種別プラグインの一覧** — Learn の `cowork-available-plugins`（`ms.date` 11/13）に、8つのプラグインと含まれるスキルが載った。Capital Markets・Finance・Legal の3つは 10/30 に既報で、残りの5つが初出になる（Copilot）
  - Accounting for Cowork（Frontier）: 照合・予算と予測・財務プレゼン資料などのスキル
  - Education / Sales / Service / HR Documents & Policies for Cowork: アクセシビリティ監査・商談準備・ケースの選別・人事文書のテンプレート起案などのスキル
  - https://learn.microsoft.com/en-us/copilot/cowork/cowork-available-plugins
- [据え置き] **その他の M365 Copilot** — Release Notes（先頭 November 4）、Cowork What's New、`cowork-models`・`cowork-admin-governance`、前提条件3本、拡張機能 What's New は改訂されていない。Fable 5.2 は本日もモデル表に載っておらず、TC・M365・SharePoint・Agent 365・M365 Developer の各ブログにも新しい記事は無い（Copilot）
  - https://learn.microsoft.com/en-us/microsoft-365/copilot/release-notes

### Copilot Studio / Power Platform / ライセンス

- [仕様] **Microsoft Copilot ハーネスのワークフローツールは呼び出した利用者の接続で動く** — Learn の `agents-experience/tools-add-workflow`（`ms.date` 11/12・preview）によると、「When an agent calls the flow」で始まるワークフローでは、ツールの Shared account 設定はコネクタのアクションに効かない。利用者はそれぞれ、ワークフローが使うサービスの権限と自分の接続を用意する必要があり、接続がなければエージェントが接続を求める（Copilot）
  - https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-experience/tools-add-workflow
- [仕様] **Computer use の Cloud PC プールの試用枠** — Copilot Studio の作成者は、Windows 365 for Agents の課金プランなしで1テナントに Cloud PC プールを2つまで作れる（`use-cloud-pc-pool` ほか6ページ・11/14 改訂・preview）。埋め込みのテストチャットからの実行は課金されず、公開済みエージェントの自律実行には1テナントあたり50時間の無料枠がある。改訂で何が変わったかは特定できていない（Copilot）
  - 上限: 1環境に5プール、1プールは最大10台まで自動で増える。CMK は非対応
  - https://learn.microsoft.com/en-us/microsoft-copilot-studio/use-cloud-pc-pool
- [据え置き] **Copilot Studio・Power Platform の Learn と Partner Center** — Copilot Studio What's New、課金、モデル表3本、ガイダンスハブ、PPAC の容量管理、非推奨一覧（`602fb731`）は前日から動いていない。プロンプトのモデル表の 12/2 の移行先（Basic は GPT-6 Luna、Standard は ChatGPT-latest、Premium は GPT-6 Reasoning）は MC1536101 の既報と同じ。Released Versions は 2026.6.3 のまま138日たつ。Partner Center 11月ページと Purview What's New にも新しい項目は無い（Copilot）
  - https://learn.microsoft.com/en-us/microsoft-copilot-studio/prompt-model-availability

### Cursor / 開発ツール / エージェント

- **Orca 1.4.259**（ハイライト3参照）
- [新機能] **Cloudflare Kitesurf** — Publickey（11/16）によると、Cloudflare が AI エージェント専用のヘッドレスブラウザ Kitesurf を Apache 2.0 でオープンソース化した（告知は 11/13）。タブ・拡張機能などの人間向け機能を省き、Chromium と比べて CPU とメモリの効率が3〜7倍としている。主に Rust で書かれ、WebAssembly にコンパイルして Cloudflare Workers 上で動き、CDP に対応するため Puppeteer などから接続できる（industry）
  - https://www.publickey1.jp/blog/26/cloudflareaikitesurf.html
- [据え置き] **Cursor・xAI・Devin・TypeSafe AI・MCP・Hugging Face** — Cursor の changelog（11/6）とフォーラム（10/12）、xAI（grok-4.7）、Devin（11/13）、TypeSafe AI（`jev-1.14.0`）、MCP blog（11/11）は動いておらず、Hugging Face の8 org に新しいリポジトリは無い。Obsidian・Apple Developer News・TestingCatalog も動いていない（Master・industry）
  - https://docs.devin.ai/release-notes/overview

### オープンウェイト / 他社モデル

- [新機能] **Meituan LongCat-2.5** — The Decoder（11/15）によると、Meituan が 1.6兆パラメータ（アクティブ約480億）のエージェント型モデル LongCat-2.5 を MIT ライセンスで公開した。自社評価では Terminal Bench v2.1 が 88.4（Claude Opus 5 は 89.1）、BrowseComp が 91.9 だった。API は OpenAI・Anthropic 両形式に対応し、期間限定価格は入力 €0.27・出力 €1.07（100万トークンあたり）。学習は中国製ハードウェアだけで行ったという（industry）
  - https://the-decoder.com/meituan-releases-a-1-6-trillion-parameter-agent-model-that-never-touched-an-nvidia-gpu/

### 業界・市場

- [動向] **Similarweb 10月分で Claude が 11.5%** — FourWeekMBA によると、Similarweb が 11/10 に公表した10月分で、Claude のシェアが 9.6% から 11.5% へ1か月で 1.9ポイント伸び、Gemini は 24.2% まで下がって5か月連続で低下した。Similarweb の投稿には届かず一次未確認で、Web トラフィックの推計のためアプリと API の利用は含まない（industry）
  - 10月分: ChatGPT 55.7%、Gemini 24.2%、Claude 11.5%、DeepSeek 3.4%、Grok 2.2%、Copilot 1.1%、Perplexity 0.8%
  - 9月分: ChatGPT 56.4%、Gemini 25.0%、Claude 9.6%
  - https://fourweekmba.com/ai-claude-gains-1-9-points-of-ai-web-share-in-a-month-to-11-5/
- [動向] **Airbnb の AI アシスタントでサポート費用が17%超減** — Customer Experience Dive によると、Airbnb の AI アシスタントが Q3 の問い合わせの約40%を人の担当者なしで解決し、予約1件あたりのサポート費用を17%超削減した（TLDR AI 11/12号で検知・industry）
  - https://www.customerexperiencedive.com/news/airbnb-reduces-customer-support-cost-per-booking-17/874307
- [動向] **PostgreSQL 19 のリリースが 11/19 に** — Publickey（11/15）によると、PostgreSQL 19 のリリースが 11/19 にずれ込み、LLM によるコードレビューで見つかった不具合が一因とされた。β4 で SQL/PGQ など6項目が取り下げ・削除され、コミッターの Peter Eisentraut 氏は LLM 支援のレビューで約40件の不具合報告が短期間に集まったと述べた（industry）
  - https://www.publickey1.jp/blog/26/postgresql_194ai.html
- [据え置き] **Anthropic の IPO と未決の買収協議** — Anthropic の IPO は 11/18 の価格決定を待つ段階で、仮条件（$70〜78）の変更は報じられていない。Amazon × Decart、Nvidia × Reflection AI の協議に続報はなく、Nvidia の後任 CEO も未定である。IDC Japan・MM総研・NRC の新しい公表も無い（industry）

### 日本語コミュニティ

- [据え置き] **Qiita / Zenn** — Copilot Cowork の学習記録（Qiita・11/15）が出たが、一次の既報の範囲として Copilot ソースが掲載を見送った（Copilot）

## 直近の注目予定

- **11/16（本日）**: Copilot から Claude Opus 4.8 / Opus 5 / GPT-5.6 Terra を廃止 ／ Teams の旧 GitHub アプリが退役 ／ `pull_request_target` の2回目の試験ブロック ／ Claude Opus 4.6・Opus 4.5・Sonnet 4.5・Haiku 4.5 に透かし ／ **Fable 5.2 ローンチ特典の Pro・Team 標準席の枠が 23:59 PT に終了** ／ Cowork / Autopilot の Engage プラグインが GA（MC1530609） ／ Workforce Intelligence プラグインが Frontier でプレビュー（MC1552389） ／ PPAC のフィードバックフォームの既定ポリシーが GA（MC1545686）
- **11月中**: GitHub の cloud sandbox の課金が開始（日付は明記なし）
- **11月中旬**: Copilot デスクトップアプリのタブ参照と、Chat からのモード切り替え提案（Standard）の展開が開始（MC1552386・MC1536065） ／ 単体の Word / Excel / PowerPoint エージェントの撤去が開始（MC1536062） ／ UBB の利用申請の設定が入る（MC1546354）
- **11/17**: Gemini API の Live / TTS preview はこの日には止まらない（11/23 訂正: TTS preview 3種は 12/18、ネイティブ音声 preview は 2027-03-31、Live preview は停止日未発表） ／ Gems が Gemini アプリの設定パネルへ移動 ／ Plugin Catalog が公開 ／ Intelligent call delegation が従量課金のパブリックプレビュー（MC1537490） ／ Claude for Manufacturing の技術ウェビナー
- **11/17〜20**: Microsoft Ignite
- **11/18**: Anthropic の IPO 価格決定（11/19 取引開始の見込み・報道） ／ MODS の Workforce Insights エンドポイントが退役（MC1542066）
- **11/19**: Claude Enterprise で Claude Data が既定でオン ／ PostgreSQL 19 のリリース予定
- **11/20**: Copilot Studio のコスト管理を M365 管理センターへ移す機能が GA（MC1530368） ／ Conductor のクラウド版が終了（二次）
- **11/24 以降**: `claude-opus-4-5-20251101` の暫定退役日（確定日ではない）
- **11月下旬**: 新しい Copilot Pages と Notebooks の OneDrive 保存の展開が全世界で完了（MC1449182） ／ Teams モバイルの Queues アプリの Copilot が Targeted Release（MC1552391）
- **11/29**: OpenAI が Daybreak Blue のセッションデータの学習利用を開始（二次）
- **11/30**: `claude-sonnet-4-5-20250929` が退役 ／ Opus 4.8 の fast mode を削除 ／ OpenAI の Evals・`v1/prompts`・Agent Builder が停止 ／ Gemini 4 Argon の導入価格が終了 ／ Power Apps のアプリ説明の AI 生成と、Plans・モデル駆動アプリの在席表示が終了 ／ App Builder のアプリが開けなくなる ／ vibe.powerapps.com・Describe it to design it・Power Automate デザイナーの Copilot が終了
- **12/1**: Gemini 4 Argon の単価が $4 / $20 に倍増 ／ Google スライドの複数スライド作成の上限引き上げ優待が終了しうる
- **12/2**: GitHub が公開リポジトリの `pull_request_target` を既定でブロック ／ Power Platform のプロンプトから Anthropic・Grok・旧 GPT 系モデルが退役（MC1536101）
- **12/7**: Purview DSPM のパートナー連携の一部が退役（MC1545691）
- **12/8**: GitHub Actions のホステッドランナーで ARM32 ジョブのサポートが終了 ／ 1年活動のないリポジトリの Dependabot アラートを停止 ／ M365 Copilot in Power BI が既定でオン（MC1546429）
- **12/9**: EU / EFTA で Claude モデルが既定で有効になり、「M365 アプリの Copilot だけで許可」が退役（MC1546438）
- **12/11**: Power Apps の式の生成・Power Apps Ideas などが退役（MC1532421・MC1532426）
- **12月中**: ChatGPT と Codex の利用枠が Plus・Pro・Business で1つの予算に統合（二次）
- **12/14**: **Copilot から Claude Fable 5 / Haiku 4.5 / Gemini 3.8 Flash / Gemini 4 Argon / Grok 4.6 / Kimi K3 を廃止** ／ claude.ai/design の単体サイトが閉鎖
- **12月中旬**: GCC 系で新しい Copilot Pages の OneDrive 保存の展開が完了（MC1449182） ／ Chat からのモード切り替え提案が Deferred に到達（MC1536065） ／ Outlook モバイルの Copilot Chat の刷新が開始（MC1551148） ／ UBB の Learn more に独自 URL を設定可能に（MC1546354）
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
- **2027 春**: Siri AI 対応アプリの App Store 提出受付が開始
- **2027-04-01**: SharePoint の tempauth URL が退役し、それに頼る Power Apps / Power Automate が停止（MC1551122・MC1492958） ／ OpenAI `gpt-5.1` / `gpt-5.3-codex` / `gpt-5.4-nano` が停止
- **2027-11-12**: Purview Data Governance のサポート終了

## 改善メモ

- Master: 新規提案 B-089（Orca の要約 URL を `orca.dev/changelog` へ改め、許可ドメインに `orca.dev` を足す）。障害の変化として `www.onorca.dev` が 307 で `orca.dev` へ転送され、転送先がゲートウェイ拒否になった（新規）。継続提案7件（最多 B-036・B-037、12回目。B-088 は13回目）。週次復旧チェックは復旧0件・分類の変化0件
- Copilot: B-082（週次突合の目次一覧の保存）に実例を追記（3回目）。computer use の6ページは前回の本文が無く差分を特定できなかった
- industry: 新規提案・障害の変化なし。継続提案7件（最多 B-040、17回目）。見送り候補は B-036
- ソース間の差異: 11/17 に停止する Gemini API の Live / TTS preview を、Master は4モデル（5本目は未確定）、industry は5種とする。どちらも一次未確認のため引き続き「4〜5種」とした。11/23 訂正: 一次の deprecations 表では 11/17 に止まるモデルは無い
- 前日（11/15）分に欠損ソースはなく、欠損リカバリは不要
