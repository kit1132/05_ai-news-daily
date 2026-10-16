# AI News Daily Summary — 2026-10-17

Power Platform の非推奨一覧に、Dataverse for Teams 環境とアンマネージド開発者環境の廃止が加わった。どちらも 11/15 に新規作成が止まる。Anthropic は Claude Code の Code Review を Team / Enterprise で GA にした。M365 Copilot では Legal Agent が退役し、Word デスクトップでは法務スキルが既定でオンになる。

## 今日のハイライト

### 1. [廃止+破壊的変更] Dataverse for Teams 環境の新規作成が 11/15 に止まり、アップグレードしない環境は 2027/10/30 に廃止される — Teams 内で作ったアプリ・フロー・エージェントが移行対象になった

**要点**: Teams の中でアプリやエージェントを作ると自動でできていた Dataverse for Teams 環境が非推奨になった。11/15 から新規作成ができず、アップグレードしない環境は 2027/10/30 に使えなくなる。アップグレード後は Power Platform 各製品のライセンスと Dataverse 容量が要る。

**詳細**: `power-platform/important-changes-coming` が 10/16 17:32Z に改訂された（`caf484d1`）。

- 3段階: 新規作成の停止 **11/15/2026**、環境の停止（suspend）、環境の廃止（decommission）**10/30/2027**
- 理由: 1環境 2GB の上限があり、API の直接アクセス・カスタムコネクタ・デスクトップフロー・AI Builder を使えないため、Dataverse に一本化するとしている
- 管理者の作業: PPAC の Manage > Environments で Type が Microsoft Teams の環境を洗い出し、要るものを Dataverse へアップグレードする。エージェントは Copilot Studio 側の `admin-upgrade-dataverse-teams` の手順に従う
- 影響しないもの: チーム・チャネル・チャット・SharePoint サイト・ファイルと、Dataverse 環境で作って Teams に追加したアプリ・フロー・エージェント
- ⚠️ 一次ページでは環境の停止日が **9/15/2026** と書かれ、新規作成停止日より前になっている。停止日は未確定として扱う

- https://learn.microsoft.com/en-us/power-platform/important-changes-coming#deprecation-of-microsoft-dataverse-for-teams-environments

### 2. [廃止+破壊的変更] アンマネージドの開発者環境が 12/15 に停止し、2027/1/15 から削除される — 無償の Developer Plan で作った個人の検証環境が対象になった

**要点**: 無償の Power Apps Developer Plan で作る環境を含め、マネージド環境でない開発者環境が非推奨になった。11/15 に新規作成が止まり、12/15 に停止、2027/1/15 から削除される。今後の開発者環境はマネージド環境だけで、1人1つまでになる。

**詳細**: ハイライト1と同じ改訂（`caf484d1`）で追加された。

- 対象外: マネージド環境の開発者環境（環境ルーティングが作る個人用を含む）と、運用・サンドボックス・試用・既定の各環境
- 管理者の作業: PPAC で Type が Developer、Managed が No の環境を洗い出し、残すものはマネージド環境に切り替えるか、ソリューションをサンドボックスへ移す。マネージド環境の利用権は Developer Plan に含まれないため、切り替えた環境でアプリやフローを動かすにはプレミアムライセンスが要る
- 作成者側: 12/15 より前にソリューションをエクスポートしておく。プレミアム機能を試すには標準の試用環境が引き続き使える

- https://learn.microsoft.com/en-us/power-platform/important-changes-coming#deprecation-of-unmanaged-developer-environments-and-the-power-apps-developer-plan

### 3. [新機能] Anthropic が Claude Code の Code Review を GA にした — research preview の PR レビューが、Team / Enterprise の管理者が有効化する正式機能になった

**要点**: Anthropic が 10/15 に、GitHub の PR を複数エージェントでレビューしてインライン指摘を付ける Code Review を research preview から外し、Team / Enterprise で GA にした。多くのレビューが約20分から6〜10分に縮み、深さをリポジトリごとに選べる。

**詳細**:

- レビューの深さ: Quick / Standard（既定）/ Deep を組織既定とリポジトリ単位で選ぶ。深いほど高コスト
- 導入: 管理者が Claude Code 設定で有効化し、GitHub App を入れて対象リポジトリを選ぶ。開発者側の設定は不要で、新しい PR に自動で走る
- クレジット: 対象の Enterprise 組織は **2027-01-15** までに $10,000 以上の Code Review クレジットを請求でき、請求から30日で失効する
- 使えない構成: Zero Data Retention・HIPAA 構成・CMEK の組織。モデルは選べない

- https://claude.com/resources/articles/code-review-is-now-generally-available
- https://code.claude.com/docs/en/code-review

## カテゴリ別まとめ

### Claude / Anthropic

- **Code Review GA**（ハイライト参照・3）
- [新機能] **Opus 5.5 fast mode の Microsoft Foundry 対応** — Anthropic が 10/15 付のリリースノートに、Azure ホストの Foundry デプロイで Opus 5.5 の fast mode を使えるという項目を足した。前日の本サマリーは「Foundry では使えない」と書いたが、使えないのは Anthropic ホストの Foundry デプロイと Claude Platform on AWS・Batch API・Priority Tier である。単価は入力 $8・出力 $40（/1M トークン）のまま。https://platform.claude.com/docs/en/build-with-claude/fast-mode
- [観測] **Compliance API の日付訂正** — Anthropic の Platform release notes が、前日 October 19, 2026 付で載っていた Compliance API の `user_preferences`（ベータ）を October 15 付に直した。内容は変わっていない。https://platform.claude.com/docs/en/release-notes/api
- [版更新] **Claude Code `2.1.301` の latest 昇格** — Anthropic が Claude Code `2.1.301`（前日掲載）を npm の `latest` に上げた。`next` は changelog 未掲載の `2.1.302`（10/16）、`stable` は `2.1.292` のままである。https://code.claude.com/docs/en/changelog
- [動向] **NIST ECDSA 曲線の seed の由来** — Anthropic の Frontier Red Team が 10/16 に、P-192〜P-521 の5曲線の seed が Unix タイムスタンプで初期化した C の `lrand48` の出力だったと、社内研究モデルで30分未満に特定したと公表した。Anthropic は暗号の破綻や新しい攻撃ではなく、対応は不要としている。https://www.anthropic.com/research/ecdsa-curve-origins
- [動向] **Claude による量子回路設計** — Anthropic が 10/16 に、平易な仕様と自動採点器だけを渡した Claude が、化学・最適化・物理シミュレーション・数論の量子回路8種で既存の最良設計を上回ったと公表した。一部は1桁以上の改善で、arXiv 論文がある。https://www.anthropic.com/research/designing-efficient-quantum-circuits
- [新機能] **Bun 1.4.3 の型チェッカー** — Anthropic が開発する Bun の 10/10 版が、Go で書いた型チェッカーを同梱したと Publickey が 10/15 に報じた。同じく Go へ移った TypeScript 7 の型チェックより3倍以上速いとしている。https://www.publickey1.jp/blog/26/anthropicbuntypescript_73typescriptbun143.html
- [据え置き] **Haiku 4.5 は退役下限日の2日後も Active** — Anthropic の廃止ページは `claude-haiku-4-5-20251001` を Active のまま表示し、廃止履歴の最新は 9/30 の Sonnet 4.5 のままである。`support.claude.com` の release notes も 10/7 の Haiku 5.5 が最上位のままである。https://platform.claude.com/docs/en/about-claude/model-deprecations

### GitHub Copilot / GitHub

- [新機能] **OSS ライセンス準拠チェック GA** — GitHub が 10/16 に、Enterprise 全体のライセンスポリシーで依存関係を検査する機能を正式提供した。ルールセットで「マージ前にライセンス準拠結果を必須」にでき、コーディングエージェントもこの判定で不適合パッケージを避けられる。対象は GitHub Enterprise Cloud で Code Security を有効にしたリポジトリで、料金の記載は無い。https://github.blog/changelog/2026-10-16-open-source-license-compliance-generally-available
  - PR チェック: 新規・変更された依存のうち不適合なものを注釈で示し、削除・置換・ポリシー修正・パッケージ例外で解消する
  - 承認ロール: 新設の「Enterprise Open-Source License Manager」が例外申請を審査し、ポリシー変更は監査ログに残る
  - データ: ライセンス情報が依存グラフと SBOM エクスポートにも載る
- [新機能] **Slack / Teams の Copilot で複数リポジトリ横断** — GitHub が 10/15 に、Slack / Teams の Copilot で1つの会話から複数リポジトリの PR・Issue・活動を尋ねられるようにした。`@GitHub` を文中のどこに書いても反応し、共有された Slack のメッセージやスレッドを文脈に使う。https://github.blog/changelog/2026-10-15-copilot-in-slack-and-teams-adds-model-and-repository-updates
- [版更新] **Copilot CLI `v1.0.99-3`** — GitHub は Copilot CLI の安定版を `v1.0.98`（10/14）のまま据え置き、pre-release に `v1.0.99-2` / `v1.0.99-3`（10/16）を足した。クライアントのテレメトリ送信を止めるフラグが加わり、オンラインセッションでセマンティックコード検索が既定オンになった。https://github.com/github/copilot-cli/releases

### OpenAI / Codex / ChatGPT

- [新機能] **Codex CLI `0.163.0`** — OpenAI が 10/15 に Codex CLI の安定版 `0.163.0` を出した。pre-release は `0.164.0-alpha.2`（10/16）まで進んだ。https://github.com/openai/codex/releases
  - `/config`: 設定をカテゴリ横断で検索してその場で変更でき、再起動が要る変更を示す
  - 操作: 応答中の追加メッセージで即座に軌道修正でき、`/keymap` にリーダーキー（既定 Ctrl+X）を設定できる
  - Daybreak: 対象アカウントで既定有効になり、`codex exec` でも API キーで選べる
  - 互換性: パッチ済み `zsh` の同梱をやめ、廃止したシェルフラグを使う設定には移行の通知が出る
- [新機能] **ChatGPT の Chrome 拡張がタブを操作** — OpenAI が 10/16 に、ChatGPT の Chrome 拡張が開いているタブを読み、Work モードではフォーム入力・メッセージ送信・ファイルのダウンロードまで代行できるようにした。`@chrome` で対象タブを指定でき、全プランで使える。OpenAI はページ内容を信頼しないよう注意を促しており、管理者向けの制御は記事に記載が無い。https://the-decoder.com/chatgpt-becomes-a-full-chrome-browser-assistant-that-reads-and-acts-on-your-open-tabs/
- [新機能] **GPT-Live-1.1 の展開** — OpenAI が 10/15 に、音声モデル GPT-Live-1.1 を ChatGPT・Codex・dots の全ユーザーに展開し始めた。13の新しい声が加わり、日本語を含む非英語の発音が良くなった。API は「近日」としている。https://community.openai.com/t/gpt-live-1-1-is-rolling-out-with-new-voices-and-better-accents/1406704
- [新機能] **GPT-Live の prompt-to-voice（API）** — OpenAI が 10/16 に、テキストの説明からカスタム音声を作る prompt-to-voice を全 API 顧客に開放した。作成は無料で、発話は通常の GPT-Live セッション課金である。日本語の Harema / Shida を含む9つのプリセット音声も加わり、10/15 には GPT-Live から Decisions API を直接呼べる統合も入った。https://developers.openai.com/changelog

### Microsoft 365 Copilot

- [廃止+新機能] **Legal Agent の退役と Word の法務スキル既定オン** — MC1509799（10/15）によると、Frontier で提供していた Legal Agent は退役し、既存の利用者はアクセスを失う。機能は Word と Cowork の法務プラグインに引き継がれ、Word デスクトップでは管理者が何もしなくても法務スキルが有効になる。退役日は書かれていない。https://mc.merill.net/message/MC1509799
  - 展開: GA は10月中旬に始まり12月中旬に完了する。対象は M365 Copilot の商用ライセンスを持つ利用者
  - 無効化: Word は Microsoft 365 Apps 管理センターの Legal Skills in M365 Copilot in Word、Cowork は M365 管理センターの Cowork for Legal をオフにする。Entra グループ単位で絞れるかは書かれていない
- [仕様] **13〜17歳向けの安全保護** — MC1509805 によると、Entra ID の `ageGroup` が teen の利用者に対し、Copilot は10月中旬から追加のコンテンツ安全保護を自動で有効にする。機微な話題への応答が制限され、管理者が切り替える設定は無い。教育機関テナントでのみ確認されている。https://mc.merill.net/message/MC1509805
- [予定] **SharePoint / OneDrive の Copilot Search** — Roadmap 573696 によると、SharePoint と OneDrive の検索が、自然言語検索・出典付きの AI 要約・Copilot への引き継ぎを備えた Copilot Search になる。プレビューは October CY2026、GA は January CY2027 である。
- [予定] **Facilitator の詐欺検知** — Roadmap 573450 によると、会議に参加した Facilitator が文字起こしから組織外参加者のソーシャルエンジニアリングを検知し、会議中に警告して会議の終了や情報共有の一時制限を選べるようになる。GA は November CY2027 である。
- [予定] **Planner Agent チャットの GA 延期** — MC1443514 によると、Copilot ライセンスを持つ利用者が基本プランで Planner Agent と対話できる機能は、GA の完了が9月下旬から10月末に延びた。
- [動向] **MAI-Base-2 の事前学習完了** — Microsoft が10月に、総パラメータ 2.8兆（アクティブ 800億）の MoE 基盤モデルの事前学習を終えたと発表した。GB200 1.6万基で38日間、50兆トークンを学習し、他社モデルからの蒸留はしていないとしている。提供時期とオープンウェイトかどうかは未発表である。https://gigazine.net/news/20261016-microsoft-mai-base-2/
- [据え置き] **Release Notes / ブログ** — M365 Copilot Release Notes の先頭は October 06, 2026 のままで、Copilot ブログ・Tech Community の各ブログ・Agent 365 Blog・M365 Developer Blog にも新規記事は出ていない。

### Copilot Studio / Power Platform

- **Dataverse for Teams 環境の廃止**（ハイライト参照・1）
- **アンマネージド開発者環境の廃止**（ハイライト参照・2）
- [新機能] **Dataverse のエージェントユーザー** — Roadmap 576843（Launched）によると、管理者が Entra のエージェント ID を持つ AI エージェントを Dataverse のエージェントユーザーとして作り、最小権限のセキュリティロールを割り当てられる。エージェントの操作はすべて監査される。https://learn.microsoft.com/en-us/power-platform/admin/create-users#agent-users-preview
- [新機能] **Power Apps CLI のコネクタコマンド** — Roadmap 576782（Launched）によると、開発者がコードアプリ向けにコネクタの検索と接続の作成をコマンドラインから行えるようになった。コーディングエージェント向けの `agent.md` も用意された。
- [予定] **Dataverse の管理用 MCP サーバー** — Roadmap 576752 によると、開発者とエージェントが、1,470 超のコネクタのアクションや組織のカスタム API を組み合わせて MCP サーバーを作れるようになる。GA は December CY2026 である。
- [予定] **プロンプト列の拡張** — Roadmap 570865 / 573279 によると、作成者が既存レコードにもプロンプト列の値を一括生成でき、出力を複数行テキストで保存できるようになる。GA はどちらも November CY2026 で、GCC / GCC High も対象になる。
- [観測] **Roadmap に169件が一括起票** — Microsoft が 10/16 19:08〜19:10Z に Roadmap へ169件を一括で起票し、総項目数は 1,923 から 2,086 に増えた。うち103件は起票時点で Launched の既出荷機能で、大半は Dynamics 365 である。
- [据え置き] **What's New / Released Versions / 課金レート表** — Copilot Studio What's New は `ms.date` 10/5 のまま、Released Versions は 2026.6.3 のまま108日動いておらず、課金レート表も変わっていない。

### その他エージェント / 開発ツール

- [新機能] **OpenRouter Armor（ベータ）** — OpenRouter が 10/16 に、エージェントの操作を別の AI で事前に検査し、ルール違反を自動で止める機能をベータ公開した。同日に Perplexity もエージェント用サンドボックス SPACE をオープンソース化した。https://gigazine.net/news/20261016-openrouter-armor/
- [版更新] **Orca `v1.4.227`** — Stably AI が 10/16 に Orca `v1.4.227` を GitHub に出し、Latest が `v1.4.224` から飛んだ（`v1.4.225` / `v1.4.226` は GitHub に出ないまま）。Codex チャットに Codex 0.136.0 以上が必要になり、速度オプションに Codex Ultrafast が加わった。https://github.com/stablyai/orca/releases
- [据え置き] **TypeSafe・Cursor・Google・MCP・Hugging Face の定点** — TypeSafe の `jev-latest` は `jev-1.13.0` のまま、Cursor の changelog は 10/13、Gemini API changelog は 10/13、`blog.modelcontextprotocol.io` は 8/22 が最上位のままである。Hugging Face の登録8 org の新しい ID は mistralai の時系列モデル `Timestral-5M` / `Timestral-209M`（10/14）だけだった。

### 市場・企業・規制

- [動向] **Accenture が Claude Enterprise を1人月 $29 に制限** — 404 Media によると、Accenture が10/1から Claude Enterprise を従量課金に切り替え、1人あたり月 $29 を超える分はプロジェクトやチームの負担にした。月 $1,000 使う社員もいた状態から予算枠方式に移ったという。社内通知の報道で、Accenture の公式発表ではない。https://gigazine.net/news/20261016-accenture-ai-limit/
- [動向] **中国が大規模モデルの重みを輸出管理へ（草案）** — 中国の商務省・科学技術省が 10/16 に、AI 技術23項目を輸出禁止・制限リストに加える改定草案を公表した。学習計算量 10^26 FLOPs 以上・2兆パラメータ以上・世界トップ10入りのいずれかに当たるモデルの重み・コード・学習手法が対象で、登録したオープンソース公開は自動許可、API・SaaS での利用は対象外である。施行日は記載が無い。https://the-decoder.com/china-plans-to-tighten-export-controls-on-open-weight-models-and-23-key-ai-technologies/
- [動向] **米銀が外部 AI エージェントの口座操作を拒否** — JPMorgan Chase が 10/13 に、外部の AI エージェントが個人顧客の代わりに送金・支払いをすることを認めないと CNBC に明らかにした。残高の読み取りは Plaid 等経由で引き続きできる。FT は 10/16 に Citi も同様の制限に動いたと報じたが、本文は未確認である。https://cybernews.com/security/jpmorgan-chase-blocks-outside-ai-agents/
- [据え置き] **買収協議・国内市場データ** — Amazon × Decart と Nvidia × Reflection AI の買収協議に続報は無く、IDC Japan・MM総研・NRC・Business Insider Japan（10月版）も新規公表が無い。

## 直近の注目予定

- **10月中旬〜12月中旬**: M365 Copilot の法務プラグイン GA 展開（MC1509799）。Legal Agent は退役
- **10月下旬**: Copilot ダッシュボードのデータエクスポートのパブリックプレビュー展開が完了（MC1173208） ／ claude.ai（米国）で Democracy Works の投票情報を表示
- **10/15 以降**: `claude-haiku-4-5-20251001` の暫定退役日（告知はまだ無い）
- **10/19**: GitHub Copilot が `gpt-5.5`・`gpt-5.4` 系・Gemini 3.7 Flash などを廃止
- **10/21 前後**: TypeSafe の `jev-latest` が `jev-1.14.0` へ移る
- **10/22**: Copilot Business / Enterprise の機能既定有効化が発効 ／ Gemini API の Veo 3.1 プレビュー3種と `gemini-omni-flash-preview` が停止（最短日）
- **10/23**: Gemini API の `deep-research-pro-preview-12-2025` が停止 ／ OpenAI のレガシー GPT スナップショットが停止
- **10/27〜29**: PPCC 2026（ラスベガス）
- **10/30**: ChatGPT Pro 200 の Work / Codex 利用枠が変更（二次）
- **10月末**: Planner Agent チャットの GA 完了（MC1443514）
- **10/31**: MCP サーバー認定の旧申請経路が終了
- **11/1**: Codex の28日間「改善かリセット」の終了（二次）
- **11/4**: Entra で一般ユーザーのブループリント作成が既定オン ／ `AgentIdentity.CreateAsManager` の自動付与が停止
- **11/9 の週**: Anthropic の IPO マーケティング開始の見込み（二次）
- **11/12**: Copilot Studio の GPT-4.1 / GPT-5 系が退役 ／ Anthropic Usage Policy 改定版が発効 ／ OpenAI → Cursor のモデル供給停止予定（一次未読）
- **11/15**: Dataverse for Teams 環境とアンマネージド開発者環境の新規作成が停止
- **11/16**: GitHub Copilot が Claude Opus 4.8・Opus 5・GPT-5.6 Terra を廃止 ／ Sales Development Agent が Copilot Credits の消費を開始
- **11/17**: Gems が Gemini アプリの設定パネルへ移動
- **11/17〜20**: Microsoft Ignite
- **11月中旬〜末**: Copilot ダッシュボードのデータエクスポートが GA
- **11/24**: `claude-opus-4-5-20251101` の退役下限日（告知なし）
- **11/26 まで**: Anthropic の取引開始の見込み（感謝祭前・二次）
- **11月下旬**: Agent 365 の可観測性データがライセンス不要に（MC1506727）
- **11/30**: Azure DevOps コネクタの旧接続が認証不可に（MC1508508） ／ App Builder エージェントと vibe.powerapps.com が退役 ／ `claude-sonnet-4-5-20250929` が Claude API から退役 ／ OpenAI の Evals・`v1/prompts`・Agent Builder が停止 ／ Gemini 4 Argon の導入価格が終了
- **12/1**: Gemini 4 Argon の単価が $4/$20 に倍増 ／ Copilot Business の従量課金が既定オン
- **12月上旬**: Teams の Facilitator が Targeted Release（GA は12月中旬〜1月中旬）
- **12/14**: claude.ai/design の単体サイトが閉鎖
- **12/15**: アンマネージド開発者環境が停止
- **2027-01-06**: OpenAI `tts-1` / `tts-1-hd` / `gpt-4o-mini-tts` 2版が停止
- **2027-01-14**: OpenAI の GPT-4o・GPT-4o mini・GPT-4.1・GPT-4.1 mini が API から削除
- **2027-01-15**: アンマネージド開発者環境の削除開始 ／ Claude Code Review の Enterprise 向けクレジット請求期限
- **2027-03-01 以降**: Gems 廃止（Business / Enterprise）
- **2027-04-01**: OpenAI `gpt-5.1` / `gpt-5.3-codex` / `gpt-5.4-nano` が停止
- **2027-10-15**: Purview の `Search-UnifiedAuditLog` コマンドレットが退役
- **2027-10-30**: アップグレードしていない Dataverse for Teams 環境が廃止

## 改善メモ

- 新規提案: industry が B-045（VentureBeat の RSS は到達できても最新項目が 8/27 で止まっているため、WebSearch 一次にして RSS の鮮度判定を加える）を起票した。Master と Copilot は無し
- 継続提案: Master は B-082 最上位エントリ基準の差分判定（23回目。前日最上位エントリの日付書き換えとその上の fast mode GA を位置比較で検出） ／ Copilot は B-037（Released Versions 108日）を更新し、docset 全件突合は本日未実施 ／ industry は3件を更新（最多 B-004・109回目）し、B-031 に Claude リリースノート 10/15 付エントリへの後日追記（Foundry の fast mode）を記録
- 障害の変化: industry で `venturebeat.com` がゲートウェイ拒否から復旧した（ただし RSS の内容は更新停止）。Master と Copilot は変化なし
- ソース間の差分・矛盾:
  - 前日の本サマリーは Opus 5.5 fast mode を「Foundry では使えない」と書いたが、Anthropic が 10/15 付エントリに Azure ホストの Foundry 対応を後から追記した。本日分で訂正した
  - 前日に記録した Compliance API の日付の割れ（Master: October 19 / industry: 10/15）は、一次が 10/15 付に直したことで解消した
  - Copilot の3モデル廃止（11/16）を Master が本日もハイライト1にしたが、前日の本サマリーでハイライト済みのため、本サマリーでは既報としてハイライト・カテゴリから外し注目予定にだけ残した
  - GPT-Live の prompt-to-voice は Master と industry の両方に載っていた。本サマリーは1件に寄せた
  - Copilot によると、Dataverse for Teams 環境の停止日が一次ページで 9/15/2026 と書かれ、新規作成停止の 11/15 より前になっている。一次側の不整合として停止日は未確定扱いにした
  - 10/30 の ChatGPT Pro 200 の枠変更は、Master が「半減」、industry が「Plus 比10倍」で二次どうしの割れが続いている
