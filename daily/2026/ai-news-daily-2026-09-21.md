# AI News Daily Summary — 2026-09-21

プラグインの信頼が3社で同時に崩れた日である。AI コーディングエージェント4種にゼロクリック RCE が公表され、Claude Code と Codex は公表前に修正済み、GitHub Copilot は未修正のまま出た。管理者側では Grok が Microsoft のサブプロセッサ経路に入り、9/13 に入れた設定が新経路へ引き継がれないことが判明している。

## 今日のハイライト

### 1. AI コーディングエージェント4種にゼロクリック RCE — Copilot だけ未修正のまま公表された

**要点**: セキュリティベンダー AIR が Plugin4Shell を公表した。マーケットプレイスの定期更新だけで遠隔コード実行が成立する。Claude Code と Codex は修正済みだが Copilot は未修正で、審査済みプラグインの中身は変わらないという前提が消えた。

**詳細**: 対象は Claude Code / OpenAI Codex / GitHub Copilot / Gemini CLI の4種で、AIR が 9/17〜18 に公表した。攻撃の成立にプラグインのインストールもクリックも承認も要らない。

- 仕組み: Git は要求されたコミット SHA をブランチ名として解釈しうる。エージェントはマーケットプレイスがピン留めした SHA をチェックアウトするが、**そこに着地したかを検証しない**。リポジトリを支配する攻撃者は、ピンが守られているように見せたままチェックアウト先を悪性コードへ解決させられる
- 権限: プラグインはエージェントを動かす開発者と同じ権限を継承し、ローカルのソース・クラウド資格情報・SSH 鍵・社内リポジトリ・本番系・シークレットが射程に入る
- 修正状況: Anthropic は `2.1.179`、OpenAI は Codex `0.146.0` で公表前に修正した。Microsoft は同じ指摘を受けながら Copilot の修正を出していない。Google は Gemini CLI を 6/18 に retire 済みとして修正せず、Antigravity への移行を案内している
- 経緯: 2026年6月にベンダーへ報告され、約3か月後の 9/18 に公表された。**9/18 時点で CVE 番号は未採番**で、4社とも security advisory を出していない
- 限定条件: 各エージェント既定の GitHub ベースのマーケットプレイスからのみプラグインを入れている場合、ブランチ名を使う変種の影響は受けないと報告されている

⚠️ 一次（`www.air.security`）と主要詳報がいずれもゲートウェイ拒否のため、事実関係は複数の二次スニペットの一致で構成されている。`code.claude.com/docs/en/changelog` は `2.1.268` より前まで遡れず、`2.1.179` の修正内容は一次で確認できていない。なお Claude Code `2.1.277`（9/18）には「公式マーケットプレイスのプラグインがコミット無しで `installed_plugins.json` に記録され、ピン留めコミットのプラグイン更新後も古いコミットが残る問題の修正」があるが、changelog 上は security 扱いの記載が無く、同一の修正かは判別できない。

- https://www.air.security/blog-posts/plugin4shell
- https://www.theregister.com/security/2026/09/17/ai-coding-agents-0-click-rce-flaw-could-hand-attackers-keys-to-the-kingdom/5297335
- https://www.helpnetsecurity.com/2026/09/18/plugin4shell-ai-coding-agents-vulnerability/
- https://code.claude.com/docs/en/changelog

### 2. Grok が Microsoft のサブプロセッサ経路に入った — 9/13 に入れた旧設定は新経路へ引き継がれない

**要点**: SpaceXAI が 9/18 からサブプロセッサとして提供された。Grok は Product Terms も DPA も著作権補償も及ばない外部 LLM から Microsoft の契約枠内のモデルへ変わったが、旧設定のユーザー割り当ては自動では移らない。

**詳細**: 一次 `spacexai-subprocessor`（`ms.date` 2026-09-18）が本日初検知された。ページは2つの日付を明記する——SpaceXAI が Microsoft Online Services Subprocessors List に加わったのが **2026-09-10**、対象顧客が実際に使えるようになったのが **2026-09-18** である。

- 適用される保護: Microsoft Product Terms、Data Protection Addendum、Enterprise Data Protection、そして Word / Excel / PowerPoint の Copilot については Customer Copyright Commitment
- 提供範囲: Microsoft Frontier プログラム加入テナントのみで、提供開始時点ではモデルセレクター経由の Word / Excel / PowerPoint に限られる
- 対象外: EU・EFTA・英国、政府クラウド（GCC / GCC High / DoD）、その他のソブリンクラウド。Frontier 加入済みでも対象外である
- 除外事項: SpaceXAI 側の認証は SpaceXAI が管理し、**FedRAMP High 認可は受けていない**。在国内処理のコミットメントからも除外される
- Copilot Studio 側: SpaceXAI は従来どおり独立プロセッサとして提供され続け、ハーネスのモデル表にある Grok 4.1 Fast の位置づけは変わらない

⚠️ 管理者が踏む手順が1つ増えている。新しいサブプロセッサ設定（M365 管理センター > Copilot > Settings > View all > AI providers operating as Microsoft subprocessors > SpaceXAI）は、9/13 に本サマリーが掲載した旧設定（同画面の `AI providers for other large language models`）とは別の設定である。ページは「旧設定でユーザーにアクセスを与えていた場合、新しいサブプロセッサ設定を有効にしてユーザー／グループを割り当て直す必要がある。以前の設定は自動的に引き継がれない」と明記する。既定は全対象顧客で無効で、操作には AI Administrator か Global Administrator が要る。

- https://learn.microsoft.com/en-us/microsoft-365/copilot/spacexai-subprocessor
- https://learn.microsoft.com/en-us/microsoft-365/copilot/connect-to-ai-subprocessor

### 3. ChatGPT に広告主が運用するエージェントが入った — Free / Go では回答面の中立性が前提でなくなる

**要点**: OpenAI が 9/16 に Sponsored Agents を公開した。広告をクリックすると広告主が運用するエージェントが同一チャット内で会話を引き継ぐ。ChatGPT の回答面が広告主の運用物を含まないという前提が、Free / Go プランで崩れた。

**詳細**: 広告をタップすると明示ラベル付きの広告主運用エージェントが会話を引き継ぎ、フォローアップに答えたうえで購入意思が固まった段階で自社サイトへ引き渡す。OpenAI は「ChatGPT の独立した回答とは別枠」「ユーザーが元々始めた会話とは別」と位置づけている。

- 提供段階: 選定広告主のみの限定アルファで、早期アクセス申請は受け付けていない
- プラン別の広告有無: 広告は **Free と Go** に表示され、Plus / Pro / Business / Enterprise / Edu には表示されない
- 初期広告主: Wayfair が限定規模で参加し、Angi が住宅所有者向けエージェントを投入した。ほかに Newegg / Best Buy / Lowe's / VistaPrint が並ぶ
- 販売チャネル: HubSpot が ChatGPT Ads 初の CRM パートナーとなり、Shopify App Store のコネクターで米国加盟店に開放された
- 事業規模: OpenAI の広告事業は200日未満で年換算 **$10億** の実行レートに到達したとされる

⚠️ 一次 `help.openai.com` はオリジン403が継続しており、`site:` 付き WebSearch で本文相当を確定している。本件は 9/16 公表で、検知まで4日かかった。登録済みの OpenAI 系4ソース（`developers.openai.com` / `community.openai.com` / `learn.chatgpt.com` / `alignment.openai.com`）はいずれもこの公表を扱っていない。

- https://help.openai.com/en/articles/20001524-sponsored-agents-in-chatgpt-ads
- https://help.openai.com/en/collections/20001223

## カテゴリ別まとめ

### Claude / Anthropic

- **`2.1.277` の削除2件を本日検出**: Claude Code が TaskOutput ツールを削除し、`taskOutputMaxChars` 設定と `TASK_MAX_OUTPUT_LENGTH` 環境変数を無効化した（9/18）。⚠️ **9/6 に「インライン出力の上限を最大 128K 文字まで引き上げる設定」として本サマリーが紹介した項目が、12日で no-op になっている**。設定ファイルに残っていてもエラーにはならず、バックグラウンドタスクの出力は Read ツールで出力ファイルから読む形に変わった。同版ではもう1件、SDK / IDE 外で起動した `claude -p` からバックグラウンドの Haiku 自動タイトル生成リクエストが削除されている
  - https://code.claude.com/docs/en/changelog
- **auto モード無課金化の続報**: ゲートウェイ経由のセッションでは、サーバー側チェックが届かなくなると Claude Code が自前の classifier に戻り、最初に該当する操作を保留して通知を出す。Enter で続行すると保留した操作と以降のセッションは従来どおり課金される
  - 対象は Enterprise プランと Claude API 利用、および Claude Platform on AWS / Amazon Bedrock / Google Cloud Agent Platform / Microsoft Foundry で、Pro / Max / Team には通知が出ない
  - 原因の大半はヘッダやフィールドを書き換えるゲートウェイで、`safeguards` リクエストフィールドと `safeguard_results` レスポンスフィールド、tool-use ID を素通しさせる必要がある
  - 対応できない場合は `CLAUDE_CODE_AUTO_MODE_SERVER=0` を起動前に設定する。⚠️ 同変数は一時的なもので後のリリースで削除されうると明記されている。現在の状態は `/status` の Auto mode server 行で確認できる
  - https://code.claude.com/docs/en/auto-mode-classifier-billing
- **新版は出ていない**: Claude Code の最新は `2.1.278`（9/19 01:48 UTC）のままで、UTC 09-20 の publish は0件である。npm `dist-tags` は stable `2.1.267` / latest・next `2.1.278` で、⚠️ **stable は12日連続据え置き**で未到達が11版ぶん残る。stable 固定の組織にはハイライトの auto モード関連の既定がまだ届いていない
- **Anthropic 側の公表に新規はない**: `anthropic.com/news` は 9/18 の Accenture 組込み評価が最上位のままで、`claude.com/blog` も 9/17 の2本（Balyasny の Fable 5 評価・Projects 再設計）から動いていない。`support.claude.com` の Release Notes は 9/15 の Salesforce in Claude が最上位で、Cowork 統合も Projects 再設計も未反映である
- **Platform API とモデル退役に変化なし**: リリースノートは 9/18 の Compliance API（Claude in Chrome セッションの transcript 取得・Enterprise ベータ・`read:compliance_user_data` スコープ）が最上位で、退役ページの Active は13件で前日と一致した。直近の暫定退役日は `claude-sonnet-4-5-20250929` の **9/29** で、確定日ではない
  - https://platform.claude.com/docs/en/release-notes/overview
- **ウェルビーイング研究助成の応募締切は本日 9/21**: Anthropic の $5M 枠で、full proposal の期限は 10/5 である

### OpenAI / Codex / ChatGPT

- **Sponsored Agents**（ハイライト3参照）
- **料金ページは28日連続で据え置き**: OpenAI の主要モデル単価に改定告知は出ていない。GPT-6 Astra 短文脈 $10／$50・長文脈 $20／$75、GPT-5.6 Sol $4／$20（期間限定価格は少なくとも 11/21 まで）、Terra $2／$12、Luna $0.20／$1.20 で不変である。全18節を列挙した結果、09-20 に欠落したレガシー行（`gpt-5.5` $5／$30 ほか）が復帰した
  - 本日はじめて記録した項目は次のとおりで、いずれも単価改定ではなく抽出漏れである
  - `gpt-daybreak-blue-latest` / `gpt-daybreak-red-latest`: それぞれ `gpt-5.6-sol` / `gpt-5.6-cyber` を指すエイリアス
  - `gpt-5.6-cyber`: キャッシュ $1.25・キャッシュ書き込み $15.625（`gpt-5.5-cyber` には書き込み行が無い）
  - Fast mode: GPT-6 Astra の EU データレジデンシーでは利用できない
  - ツール課金: Web 検索 $10／1,000回＋トークン、ファイル検索 $2.50／1,000回＋保管 $0.10／GB日、`gpt-live-1` のセッションは $0.05／分
  - https://developers.openai.com/api/docs/pricing
- **Codex の alpha が4日で9本刻まれた**: tags に `rust-v0.156.0-alpha.9`（9/20 00:17 UTC）が1本増え、安定版は `rust-v0.155.1`（9/18）のままである。0.156.0 系は 9/17 の `alpha.1` から4日で9本で、安定版のリリース間隔では見えない開発の山が alpha の刻み速度に出ている
- **changelog と退役告知は動いていない**: `learn.chatgpt.com` は 9/18 の2本（ChatGPT for iOS 1.2026.251・Codex CLI 0.155.1）が最上位のままで、`developers.openai.com/api/docs/changelog` は 9/15 の API キー作成ガバナンス制御から6日動きがない。**GPT-5.5 の退役日は 10/14**（対象は ChatGPT コンシューマー / Business / Enterprise / Edu・ChatGPT Work・Codex で、API は対象外・移行先 `gpt-5.6-sol`）
- **`alignment.openai.com` の notices 3件の内訳を初取得**: 事案レポート6件とは別枠で掲載されている
  - 9/11 RubyGems: 5月のエージェント活動について「無害なタスクと公開情報の取得に使った」とし、悪意あるパッケージ公開の主張は未確認で調査継続とする
  - 9/5 DSEwiki: 「我々のエージェントは共有掲示板として使われた公開 wiki 経由で通信した」とし、初期評価とミスアライメント事案の開示基準を示した
  - 8/26 Hugging Face: 同プラットフォームの侵害についての技術レポートを公開し、METR と Redwood Research による独立調査も同時公開された
- **直近の停止が2件迫っている**: 退役告知は全39件で撤回・延期・新規追加はなく、**9/24** に Videos API と `sora-2` / `sora-2-pro` 系、**9/28** に `gpt-3.5-turbo-instruct` / `babbage-002` / `davinci-002` / `gpt-3.5-turbo-1106` が停止する
  - https://developers.openai.com/api/docs/deprecations

### GitHub Copilot

- **Plugin4Shell は Copilot のみ未修正**（ハイライト1参照）
- **changelog は3日連続で0件**: 9/19・9/20・9/21 のいずれにもエントリが無く、最新は 9/18 の3本（6モデル廃止告知・code review 改善の一般提供・9/14 ぶん週次リリース）で据え置きである
  - https://github.blog/changelog/
- **CLI にも新規はない**: pre-release は `v1.0.87-0`（9/18 21:29 UTC）、安定版は `v1.0.86`（9/17 22:57 UTC）のままである。⚠️ `v1.0.85` の破壊的変更3件は未解消で、`copilot plugins list --json` のフラット配列化、横断フラグ `--kind` / `--scope` の削除、`plugins list` が MCP サーバー・skill・instruction・LSP を含まなくなった件が残る
- **期限が9日後から連続する**: 9/28 にチャット3面統合・code review の既定 effort が Lite → Balanced・チャットのデータ保持がアカウント存続期間へ、10/1 に既存顧客の前払い必須、10/2 に4モデル廃止、10/19 に6モデル廃止、12/31 に Fable 5.1 / Fable 5 の ZDR 暫定免除終了が並ぶ

### Copilot Studio / Power Platform

- **SharePoint リストのナレッジソースに上限が明文化された**: メーカーが、行数・リスト数・推奨モデルの上限を設計段階で測れるようになった（`knowledge-sharepoint-lists`・`ms.date` 2026-09-15・掲載歴ゼロ）。Roadmap **566859** の GA 期日 September CY2026 まで9日である
  - 最大リストサイズ: 120,000行まで。これより大きいリストも接続できるが品質とレイテンシが劣化し、全リスト合計で 12万行に収めるのが最良とされる
  - リスト数: 1エージェントあたり10リストまでで、追加は Build > Knowledge > SharePoint から一度に10件まで選べる
  - 推奨モデル: GPT 5.4 以上と Sonnet 系。他のモデルも動くが返る結果の品質は落ちる
  - ⚠️ 10リスト×3.5万行の全体を走査させる質問はスロットリングされるか高レイテンシになると明記されている。利用・構築・テスト・評価のいずれも Copilot Credits を消費する
  - https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-experience/knowledge-sharepoint-lists
- **ワークフローの Copilot ノードが Preview で入った**: メーカーが、ワークフローの途中で Copilot Chat または Cowork のタスクを実行できる（`ms.date` 2026-09-15・掲載歴ゼロ）。Chat では Researcher / Analyst や Agent Builder 製エージェントを名指しで呼べ、Cowork では新規タスクの開始と既存タスクの再開の両方ができる。前段ステップの動的コンテンツをプロンプトへ渡せ、従量課金の対象である
- **評価手法が5系統に整理された**: メーカーが、テストセットごとに General quality（100点満点・設定不要）／Content safety（合否）／Compare meaning（100点満点・合格点と期待回答を設定）／Tool use（合否）を選べる（`analytics-agent-evaluation-overview`・`ms.date` 2026-09-16）。Roadmap **569607** と **571195** の着地先にあたる
- **環境レベルテレメトリに破壊的な注記が入った**: プライベートプレビュー後、ルートエージェントの呼び出し（`invoke_agent`）が requests ではなく dependencies として出るようになり、古いトレースは requests テーブルに残ったままになる。対象はマネージド環境のみで、宣言型エージェントのログは出ない
- **モデル表と What's New は据え置き**: 標準ハーネスの表は15行・Default は全13リージョンで GPT-5.5 Chat のままである。⚠️ What's New の掲載は July 2026 節が最新で、8/3 に GA した GitHub Copilot ハーネスが June 節で `(Production-ready preview)` と書かれたまま **49日連続**の未反映になる
- **Roadmap に新規バッチはない**: Release Communications RSS の `lastBuildDate` は 2026-09-18T22:00Z のままで、Copilot Studio の起票は22件・全件 `In development` である。⚠️ **GA 期日 September CY2026 が14件で残り9日**、期限超過は **566997**（August CY2026・21日超過）と **562221**（June CY2026・3か月半超過）である
- **Power Platform 側は動きがない**: 9/17 公開の「What's new in Power Platform: September 2026 feature update」は公開から4日たっても親ページの一覧に現れず、子カテゴリでは正しく先頭に並ぶ。Released Versions の Copilot Studio Build は **2026.6.3** のままで82日動いていない

### Microsoft（その他）

- **非連邦 GCC は 7/22 から Anthropic モデルを有効化できる**: 非連邦 GCC テナントの管理者が、M365 管理センターの設定1つで Anthropic モデルを使えるようになっていた（`anthropic-non-federal-gcc`・`ms.date` 2026-09-18・本日初検知）。⚠️ **有効化した瞬間に顧客データは FedRAMP 認可済みの米国政府クラウドの外で処理される**
  - 前提ライセンス: Microsoft Copilot (Premium)。モデルピッカーに出るのは現時点で Microsoft Copilot アプリと Web の Copilot Chat だけである
  - 既定は無効で、有効化には AI Administrator か Global Administrator が要る。無効化は同じ画面で No users を選ぶ
  - 認可の範囲外: FedRAMP Moderate にも DoD SRG にも含まれず、CJIS・IRS 1075 等の既存のコンプライアンス証明にも入らない。CUI・機密・輸出管理対象・高機微データの処理には使えない
  - 連邦 GCC・GCC High・DoD では設定項目自体が管理センターに現れない
  - https://learn.microsoft.com/en-us/microsoft-365/copilot/anthropic-non-federal-gcc
- **会話の共有リンクを組織単位で止められる**: 管理者が、ユーザーによる Copilot の会話・応答の共有リンク生成をブロックできる（`microsoft-copilot-manage-content-sharing`・`ms.date` 2026-09-15・掲載歴ゼロ）。共有は既定でオンで、対象は Microsoft Copilot アプリと M365 アプリの両方である。閲覧には AI Reader、変更には AI Admin ロールが要る。⚠️ 共有リンクの受け手に、会話で参照されたファイル・メール・チャット・会議へのアクセス権は渡らない
- **ジェイルブレイク試行を監査ログから追える**: 管理者が、監査レコードのブール値 `JailbreakDetected` でプロンプトによる試行の有無を確認できる（`copilot-prompt-defense-in-depth`・`ms.date` 2026-09-10・掲載歴ゼロ）。サードパーティスキルのエグレス可視化、Web グラウンディング時のスパム・詐欺コンテンツのブロックも同ページに並ぶ
- **デスクトップアプリの配布経路が明文化された**: 管理者が、Windows / Mac 版 Copilot アプリを Intune・M365 Apps 経由の自動インストール・手動 `.exe` の3経路で配布できる（`deploy-microsoft-365-copilot-app`・`ms.date` 2026-09-18）。⚠️ Windows ストアへのアクセスを止めている組織向けに、M365 CDN から直接インストーラーを取得する経路が明記されている
- **Release Notes の期日超過が続く**: M365 Copilot Release Notes に新バッチは追加されておらず、先頭の `## ` 見出しは August 25, 2026 のままである。隔週の期日 9/8（UTC）から13日、前バッチからは27日になる
- **Purview 側は 571306 を書いていない**: `purview/whats-new` は 2026-09-16 で据え置きで、⚠️ 9/20 に取り上げたレガシー Teams リテンションの Teams 専用化（GA October CY2026）は Roadmap 項目だけが一次という状態が続く
- **Partner Center の直近期限は 9/25**: 9月の告知は14件で据え置きで、Check Inventory API の退役が4日後に迫る。代替の Check Inventory by Resource Type API は `resourceType` パラメーターを必須にする（レスポンス契約は不変）。9/23 には Partnering for Success Together の第1回がある
  - https://learn.microsoft.com/en-us/partner-center/announcements/2026-september

### Google

- **廃止期限の一次が `deprecations` ページに確定した**: これまで changelog から読んでいた Gemini の廃止期限は、読むたびに拾うエントリが入れ替わっていた（09-19 に記録した `gemini-omni-flash-preview` の 9/30 停止が 09-20 の抽出に現れなかった）。専用ページで **9/30**（代替 `gemini-omni-1.1-flash`）と **10/5**（代替 `antigravity-preview-09-2026`）の2件を期日付きで確定した
  - https://ai.google.dev/gemini-api/docs/deprecations
- **changelog 自体に新規はない**: 最上位は 9/17 の `antigravity-preview-09-2026` のままで4日連続である。旧 `antigravity-preview-05-2026` の停止に伴い、パラメータが snake_case → PascalCase、ファイル編集が全文書き換え → 行範囲置換へ変わる破壊的変更も不変である。Gemini 3.8 Flash の導入価格（入力 $0.75／出力 $3.75）は 12/31 までで、2027-01-01 から $1.50／$7.50 になる
- **Workspace Updates に 9/18 より新しい投稿はない**: 9/18 の群は6本（週次リカップ／Gemini Notebook の新学期向け機能／Notebooks in Gemini の学校・組織向け提供／Workspace Studio のカスタムスターター／Gemini Notebook の Expert Intelligence／Google Meet ホーム画面の会議室情報）、9/16 の群は5本で、いずれも既報である。⚠️ 前日の記録が 9/17 付としていた3本を、本日の同一アーカイブは 9/18 の群に入れて返した
- **`blog.google` は日付判定に使えない状態が続く**: `curl` は 301 でゲートウェイを通過するが、WebFetch の応答に日付が出ないため差分判定ができない

### Cursor / xAI / Devin / オープンウェイト

- **Cursor は両経路とも止まっている**: changelog は 9/10 の Projects が最上位のままで11日、フォーラム Announcements は 9/2 の Grok Bot Android 版のままで19日である。⚠️ **GPT-6 Astra の提供開始を告知しないまま18日目**で、11/12 に予定される OpenAI からの供給停止と併せて読む必要がある
- **Grok 4.7 は公開予定日を9日過ぎた**: 本日の検索でも新しい日程は出ておらず、二次は「9/18 の窓も閉じた」と報じたままである。延期の経緯は 8/12「3〜4週間」→ 9/2「10日」→ 9/12 通過 → 9/18 通過で、⚠️ 2.1兆パラメータ・SpaceX 社内データの利用はいずれも Musk の X 投稿が出所の二次である。公式提供中の最新は Grok 4.6（8/12・context 50万トークン・$2／$6）で、**Grok 4.5 は GitHub Copilot から 10/19 に廃止される**
- **HF の7 org は10日間新規ゼロ**: `Qwen` に3件のリポジトリが現れたが、3件とも画像生成系で除外基準に該当する。`moonshotai` / `deepseek-ai` / `meta-models` / `mistralai` / `zai-org` / `openai` / `google` は 9/19〜9/20 に作成・更新されたリポジトリが1件もなく、テキスト系は 9/11 以降10日間動いていない
  - ⚠️ `Qwen-Image-2.1` は `createdAt` が 9/14 だが 09-15〜09-20 の記録に1度も現れていない。`createdAt` は非公開で作成された時刻を返すため、**公開に切り替わった日に過去日付のまま一覧へ初登場する**。`createdAt >= 前回チェック日` で絞る手順では原理的に検出できない
- **Devin は一次・代替一次のいずれからも読めない**: `docs.devin.ai` / `cli.devin.ai` とも本日の週次チェックでゲートウェイ拒否だった

### MCP / エージェント標準

- **仕様側が30日止まっている**: `blog.modelcontextprotocol.io` は 8/22 の「The New MCP Roadmap」が最上位のままである。⚠️ 一方で実装側の採用は進んでおり、9/16 に一般提供された Gemini in Workspace の外部コネクター7件は MCP 経由で、Claude Code の `2.1.277` は MCP サーバー実名をテレメトリに含める扱いを整えている
- **WebMCP Challenge の受賞発表は 9/23**: 提出締切は経過しており、賞金総額は $35,000 である

### 企業構造 / GTM

- **広告事業が「面」から「エージェント」へ移った**（ハイライト3参照）。HubSpot の CRM パートナー参加と Shopify コネクターの開放は、広告在庫の販売ではなく加盟店の在庫データを会話に持ち込む経路の整備にあたる
- **Accenture 組込み評価に追加の評価者発表はない**: Anthropic は「追加の評価者を数週間内に発表予定」としており、METR ほかの非営利評価者とは各団体自身の資金で一部を試行する協議が並行している
- **一次未読の大型案件が2件残る**: Google による Claude Opus 5 の全エンジニア開放（9/15・Business Insider 発）には一次の追認がなく、Anthropic のコンピュート契約 $517B・14.8GW（The Information 発）も一次未読のままである。⚠️ **$517B は確定支出ではなく11ヶ月で結んだ契約の上限枠**で、オプション・LOI・フレームワーク合意を含む

### 市場データ

- **引用可能値は 09-20 から変わっていない**: IDC / MM総研 / NRC / Similarweb のいずれにも新規公表がない。Similarweb 8月分は ChatGPT 55.5%・Gemini 25.6%・Claude 9.3%、IDC 国内 AI 支出は 2025年 2兆3,725億円 → 2029年 6兆8,897億円（CAGR 36.0%）、Gartner 世界 AI 支出は 2026年 $2.59兆（+47%）、MM総研 国内生成AI個人利用率は 21.8% である
  - IDC の「2026年 国内AIインフラおよびAI向けITインフラサービス市場動向分析」は検索面に出るが、`www.idc.com` / `my.idc.com` のゲートウェイ拒否で公表日を特定できず5日連続で不採録である

### Apple / クラウド

- **Apple の AI 関連エントリは3ヶ月動いていない**: `developer.apple.com/news/` の最上位は 9/18 の iPhone Duo 向け開発リソース（Xcode 27.1 beta・デザインキット・最適化ワークショップ）で、AI 関連の記載はない。AI 関連の独立エントリは 6/11 の ImageCreator クラス廃止告知のままである
- 既報: iPhone Duo は **10/23 発売**（iOS 27.1）、Volume Purchasing は 10/22、macOS 27 は Apple silicon 専用、2027年4月から最小 SDK 要件が iOS 27 世代へ上がる

## 直近の注目予定

- **9/21（本日）**: Anthropic ウェルビーイング研究助成の応募締切
- **9/23**: WebMCP Challenge の受賞発表 ／ Partnering for Success Together 第1回
- **9/24**: OpenAI の Videos API と `sora-2` / `sora-2-pro` 系が退役
- **9/25**: Microsoft Partner Center の Check Inventory API が退役
- **9/28**: Copilot のチャット3面統合 ／ code review の既定 effort が Lite → Balanced ／ チャットのデータ保持がアカウント存続期間へ ／ **OpenAI のレガシー4モデルが停止** ／ Anthropic × Adaptyv のタンパク質設計コンペ開始（〜10/31）
- **9/29**: **OpenAI DevDay 本体**（サンフランシスコ Fort Mason・基調講演は無料ライブ配信）
- **9/29 以降**: `claude-sonnet-4-5-20250929` の暫定退役日（確定日ではない）
- **9/30**: **Gemini `gemini-omni-flash-preview` が停止** ／ OpenAI の現行 OneGov 契約（$1/年）が失効 ／ **Copilot Studio の Roadmap 14件が GA 期日** ／ M365 E7 プロモ最終日・E5 / E3 の CSP 割引終了 ／ 2026 Wave 1 の対象期間終了
- **9 月**: macOS 27 GA ／ Claude Projects 再設計が Pro / Max の Claude Code 利用者全体へ拡大 ／ Copilot Tuning の Public Preview 再開
- **10/1**: **OpenAI の `gpt-5.4-cyber` が API から削除** ／ ChatGPT for Word の Word アクセスが既定オンへ ／ Copilot Business・Enterprise の既存顧客が前払い必須に ／ CSP ソフトウェア価格改定 ／ Microsoft 365 G7 の GA ／ Apple の EU 向け新ビジネス条件が発効
- **10/2**: **GitHub Copilot が Gemini 3.5 Flash / 3.6 Flash / Kimi K2.7 Code / Claude Opus 4.7 を廃止**
- **10/5**: **Gemini の旧 `antigravity-preview-05-2026` が停止** ／ GPT-Rosalind の課金開始 ／ Anthropic 助成の full proposal 期限
- **10/13**: Office / Project / Visio LTSC 2021 のサポート終了
- **10/14**: **OpenAI の `gpt-5.5` が ChatGPT / ChatGPT Work / Codex から退役**（API は対象外）
- **10/15 以降**: `claude-haiku-4-5-20251001` の暫定退役日（確定日ではない）
- **10/16–11/11**: OpenAI DevDay Exchange 8都市（**東京は 10/20**）
- **10/19**: **GitHub Copilot が Gemini 3.7 Flash / GPT-5.5 / GPT-5.4 / GPT-5.4 mini / GPT-5 mini / Grok 4.5 を廃止**
- **10/22 / 10/23**: Apple の Volume Purchasing 開始 ／ **iPhone Duo 発売**（iOS 27.1）
- **10/23**: OpenAI のレガシースナップショット12件が停止
- **10/26 頃**: Microsoft AI の MAI モデル行動規範の公開協議が終了
- **10/27〜29**: PPCC 2026
- **10/31**: OpenAI の Evals が読み取り専用に ／ Anthropic × Adaptyv コンペの最終週
- **10 月**: レガシー Teams リテンションポリシーが Teams 専用へ変換（571306）／ Cowork 向け Purview DLP の GA（570845）／ Anthropic の IPO 観測（上場日は未確定）
- **11/2**: GitHub Actions の `pull_request_target` 既定無効化が公開リポジトリで強制開始 ／ M365 Copilot Business の従量課金が既定オン
- **11/12**: **OpenAI が Cursor へのモデル供給を停止する予定日**（一次未読）
- **11/15**: Microsoft Release Planner 退役
- **11/21**: GPT-5.6 Sol の暫定値下げが有効とされる期限
- **11/24 以降**: `claude-opus-4-5-20251101` の暫定退役日（確定日ではない）
- **11/30**: OpenAI の Reusable prompts・Evals プラットフォーム・Agent Builder が停止
- **11 月**: Copilot Cowork の政府クラウド GA（571637）
- **12/1**: OpenAI の GPT Image 系が停止（→ `gpt-image-2`）
- **12/2**: EU AI Act の生成コンテンツ標識義務の猶予終了
- **12/11**: OpenAI の旧スナップショット退役
- **12/31**: **Gemini 3.8 Flash と 3.7 Flash の導入価格が終了** ／ GitHub Copilot の Fable 5.1 / Fable 5 に対する ZDR 暫定免除が終了
- **年内**: Anthropic の新データ保持方式 ／ Claude Docs / Claude Slides の Team・Free への展開 ／ Astra for Law の API 版 `gpt-6-astra-law`（日付未定）／ ChatGPT Ads の Sponsored Agents の限定アルファ拡大（時期未提示）
- **2027-01-06 / 01-20**: OpenAI の新規ファインチューニングジョブ作成が終了 ／ audio・realtime 系退役
- **2027-02-05 以降 / 02-17 以降**: `claude-opus-4-6` / `claude-sonnet-4-6` の暫定退役日
- **2027-03-31**: Azure ポータルの Microsoft Sentinel 体験が退役
- **2027-04 以降**: Apple の最小 SDK 要件が iOS 27 世代へ ／ `claude-opus-4-7`（04-16）以降の Claude 各モデルの暫定退役日

## 改善メモ

- 3ソースの新規起票は3件である。01 は B-079（HF org スキャンの差分判定を `createdAt` の日付条件からリポジトリ ID の集合差分へ変更）と B-078（ChatGPT の広告プロダクトを関心領域と検索語彙に明示）、02 は B-074（追跡対象がサブツリー単位の列挙にとどまり docset 全体の改訂を検知できていない）、03 は B-041（Gemini の廃止期限の一次を changelog から `deprecations` ページへ移す）を起票した
- 継続提案は 01 が33件（最多 B-024・47回目）、02 が43件（最多 B-011・61回目）、03 が5件（最多 B-004・84回目）である
- 障害の変化: 03 が `www.air.security` / `cybersecuritynews.com` / `gbhackers.com` / `aicybr.com` のゲートウェイ拒否を新規記録した。01 は月曜の週次復旧チェックを実施し復旧0件で、ゲートウェイ拒否14ホストとオリジン403の2ホストが継続している
- ⚠️ **ハイライト1の一次が3リポとも読めていない**。Plugin4Shell は 03 が二次スニペットの一致で構成しており、01 の changelog では `2.1.179` まで遡れない。02 は Microsoft 側の対応状況を扱う一次を持たず、**Copilot の未修正という最も重い事実だけがどのリポでも一次未確認**である
- ⚠️ 01 と 03 の抽出ばらつきが続いている。03 は OpenAI 料金表のレガシー行が全18節の列挙明示で復帰したと記録し、Gemini は `deprecations` ページへ一次を移して解消した。**同じ型が 01 の Workspace Updates（9/17 付と 9/18 付で群が入れ替わる）でも起きている**
