# AI News Daily Summary — 2026-11-10

Anthropic が 11/9 に Claude Fable 5.2 / Mythos 5.2 を出し、最上位モデルの単価を 5.1 比で2割下げた。同じ日に GitHub は Copilot CLI の安定版 v1.0.108 で JSON 出力とローカル MCP の環境変数の扱いを変え、Microsoft は Copilot コネクタの書き込み操作を Copilot Chat と Cowork で GA にした。

## 今日のハイライト

### 1. [料金+新機能] Anthropic が Claude Fable 5.2 / Mythos 5.2 を出し、単価を $10/$50 から $8/$40 に下げた — 最上位モデルの試算は引き直しになるが、5.1 から API で移ると 400 になる変更が4つある

**要点**: Anthropic が 11/9 に Fable 5.2（`claude-fable-5-2`）と、検証済み組織だけが使える Mythos 5.2 を出した。単価は 5.1 比2割安い入力 $8・出力 $40 で、最上位モデルの費用試算は引き直しになる。API で 5.1 から乗り換えると400エラーになる変更が4つある。

**詳細**:
- 仕様: 1M コンテキスト（既定かつ最大）、出力 128k、adaptive thinking は常時オン。effort は5段階で API の既定は `high`。出力は最大30%速い
- 料金（USD / 100万トークン）:
  - 標準: 入力 $8 / 5分キャッシュ書込 $10 / 1時間キャッシュ書込 $16 / キャッシュ読取 $0.20 / 出力 $40
  - Batch: 入力 $4 / 出力 $20
  - fast mode（最大2.5倍速）: 入力 $16 / 出力 $80。ベータヘッダーなしの `speed: "fast"` で使え、Claude Code でも使える
  - US 内だけの推論は 1.1倍
- 提供先: Claude API、Claude Platform on AWS、Google Cloud、Microsoft Foundry。Pro / Max / Ultra / Team / Enterprise で使える。Mythos 5.2 は Cyber / Life Sciences Verification Program の検証済み組織だけ
- 5.1 から API で乗り換えると壊れる4点:
  - prefix check: system・tools・過去のメッセージを書き換えて thinking block を送り返すと、アカウントの作成日を問わず 400 になる
  - thinking block: 5.2 の block は 5.2 と Mythos 5.2 しか読まない。他のモデルへ戻すとその分の推論は落とされる（リクエストは成功する）
  - computer use: `computer_20251124` を宣言すると 400 になる。`computer_toolset_20260801` へ移す
  - advisor tool（beta）: 5.2 の executor は 5.2 か Mythos 5.2 の advisor しか受けない
- Claude Code・claude.ai・Managed Agents・Agent SDK が組むリクエストは影響を受けない
- データ保持: 2モデルとも30日保持の Covered Models で、ZDR では使えない（Anthropic が明示に認めた場合を除く）
- ベンチマーク（Anthropic 発表）: FrontierCode 2.0 49.1%（5.1 32.4%・Opus 5.5 45.5%・GPT-6 Astra 42.8%）、OSWorld 2.1 89.3%
- 退役: Fable 5.2 の暫定退役日は「Not sooner than November 9, 2027」。Fable 5.1 / Mythos 5.1 は Active のままで、下限は 2027-09-01
- ローンチ特典: Pro と Team の標準席は 11/16 23:59 PT まで Fable を週の上限の50%まで含め、リセットが1回付く。Max / Ultra と premium 席のリセットは 2027-03-08 23:59 PT に失効する
- Copilot・Cursor の提供告知は本日の時点で見つからない

出典:
- https://www.anthropic.com/claude-fable-and-mythos-5-2
- https://platform.claude.com/docs/en/models/fable-5-2/whats-new-fable-5-2
- https://platform.claude.com/docs/en/release-notes/overview
- https://platform.claude.com/docs/en/about-claude/pricing
- https://platform.claude.com/docs/en/about-claude/model-deprecations
- https://support.claude.com/en/articles/17506494

### 2. [破壊的変更+新機能] GitHub が Copilot CLI v1.0.108 で JSON 出力とローカル MCP の環境変数の扱いを変えた — 出力を機械で読むスクリプトと MCP 設定が、更新後に動かなくなりうる

**要点**: GitHub が 11/9 に Copilot CLI の安定版 `v1.0.108` を出した。`-p --output-format json` の出力にセッションイベントが加わり、ローカル MCP の環境変数の値は書いたまま渡すようになった。イベントの種類を固定と見るパーサーと、値にホストの環境変数を書いた MCP 設定は見直しが要る。

**詳細**:
- 挙動が変わるもの:
  - JSON 出力: `-p --output-format json` にセッションの開始・再開・モデル変更のイベントが入る
  - ローカル MCP: 対話セッションでは環境変数の値を書いたまま渡す。ホストの環境変数は `${NAME}` で参照する
  - SDK: 同じ名前のカスタムツールを2つ渡すとエラーになる
  - headless resume: 別の Copilot プロセスが使っているセッションの再開はエラーを返す
  - Autopilot: MCP の入力・同意の要求を自動で断らず、ユーザーの応答を待つ
- 非推奨（削除はまだ）: `/experimental on|off` と `/theme <mode>`。`/settings` に移る
- 追加: Windows 向けの `sandbox.userPolicy.filesystem.enumeratePaths`、`/index` コマンド（共有の tgrep 索引が既定でオン）

出典:
- https://github.com/github/copilot-cli/releases

### 3. [新機能] Copilot コネクタの書き込み操作が Copilot Chat と Cowork で GA になった — Copilot から外部システムへの書き戻しが、既定で使える機能になった

**要点**: 利用者は Copilot Chat と Cowork で、MCP ベースの Copilot コネクタを通じて Jira・Notion・Canva などのデータを会話から作成・更新・削除できるようになった。書き込みツールは既定で「Needs approval」だが、「Always allow」を選ぶと確認なしで動く。

**詳細**: TC の Microsoft Copilot Blog（11/9 20:51Z）。Office アプリの Copilot は「近日対応」。
- 承認の選択肢: Allow once / Allow for conversation / Always allow / Cancel。許可はツール単位で、発行元がツールを変えると Needs approval に戻る
- 実行の範囲: 利用者本人の権限で接続先に対して実行し、データは M365 に索引されない。Researcher では読み取り専用のまま
- 管理者: M365 管理センターでコネクタごとに書き込みツールを確かめられ、操作は Purview で監査できる
- 記事が挙げる接続先: Atlassian Rovo（Jira / Confluence）・Notion・Canva・G2・iManage・BioRender

出典:
- https://techcommunity.microsoft.com/t5/microsoft-copilot-blog/turn-copilot-insights-into-action-with-connector-write/ba-p/4571160
- https://learn.microsoft.com/en-us/microsoft-365/copilot/connectors/federated-connectors-overview

## カテゴリ別まとめ

### Anthropic / Claude

- **Claude Fable 5.2 / Mythos 5.2**（ハイライト1参照）
- [セキュリティ] **Claude Code の settings.local.json 経由の秘密情報漏えい** — Apiiro が、Claude Code の「次回から表示しない」でパスワード入りのコマンドが設定ファイルに残り、GitHub の公開リポジトリから秘密情報 2,539件が見つかったと公表した。Anthropic の修正はまだ出ていない（GIGAZINE 11/9 経由。Apiiro の一次は未確認）（industry）
  - 規模: `.claude/settings.local.json` 104,185件のうち1,122件から1,379件。Git 履歴・共有設定・会話記録からさらに1,160件見つかった
  - 検出の難しさ: 1,122件のうち215件は、2種類のスキャナのどちらでも検出されなかった
  - 対応: Claude Code 責任者の Boris Cherny 氏が 11/7 に、認証情報の検出などの対策案を試作中だと Hacker News に書いた。`.gitignore` は一度コミットしたファイルを守れない
  - https://gigazine.net/news/20261109-claude-code-leak-secrets/
- [動向] **Claude による電子機器の設計** — Anthropic が 11/9 の研究記事で、Fable 5.2 に Diode Computers と組んで電子機器3台（スピーカーフォン・音声アシスタントのハブ・携帯型の仮想ペット）を設計させた結果を出した。回路は手直しなしで動いたが、記事は試作品であり耐久性と商用認証の通過は分からないとしている（Master）
  - https://www.anthropic.com/research/claude-electronics-design
- [据え置き] **Claude Code と Anthropic の一覧** — Claude Code の changelog の最上位は `2.1.319`（11/6）のままで、npm も stable 2.1.311 / latest 2.1.319 で変わっていない。`/news` の一覧、`claude.com/resources/articles`、support の release notes にも新しい記事はない（Master・industry）
  - https://code.claude.com/docs/en/changelog

### GitHub Copilot / Microsoft 開発ツール

- **Copilot CLI v1.0.108**（ハイライト2参照）
- [据え置き] **GitHub Copilot changelog** — `github.blog/changelog/label/copilot/` の最上位は 11/6（UTC 11/7）の code review API 管理のままで、Fable 5.2 の Copilot 提供告知はまだない（Master）
  - https://github.blog/changelog/label/copilot/

### Microsoft 365 Copilot

- **Copilot コネクタの書き込み操作**（ハイライト3参照）
- [観測] **Roadmap API の総項目数** — Microsoft の Roadmap API の総項目数が 2,297 から 2,296 に減った。新しいバッチはなく、RSS の項目数も 2,296 で一致した。前回の一覧がないため、消えた項目は特定できない（Copilot）
  - https://www.microsoft.com/releasecommunications/api/v1/m365
- [据え置き] **Roadmap・Message Center・Partner Center** — Roadmap の RSS は 11/6 23:04Z、Message Center のアーカイブは 11/7 00:00Z から動いていない。Partner Center 11月ページは 11/9 に改訂されたが、追記はパートナーのマーケティング機能の案内1件で、Copilot のライセンス・価格の変更はない。Release Notes（先頭 November 4）・Cowork What's New も改訂されていない（Copilot）
  - https://learn.microsoft.com/en-us/partner-center/announcements/2026-november

### Copilot Studio / Power Platform

- [新機能] **Power Pages の認証統制（preview）** — 管理者は PPAC で、OpenID Connect・SAML 2.0・WS-Federation・OAuth 2.0 の各プロトコル、Google・Microsoft・Facebook の ID プロバイダー、ローカル認証をサイトごとに許可・禁止できるようになった。禁止は既にその方式を使っているサイトにも効き、利用者はその方式でサインインできなくなる（Copilot）
  - 設定の場所: Manage > Products > Power Pages > Settings > Authentication。既定はすべて許可
  - 確定の前: 管理センターが影響を受けるサイトを一覧にし、サイトの所有者と管理者にメールが届く
  - https://www.microsoft.com/en-us/power-platform/blog/power-pages/new-authentication-governance-controls-in-power-pages/
- [動向] **Microsoft Copilot ハーネスの本番数値** — Microsoft の製品チームが 11/9 のブログで、評価タスクの合格率が OpenAI のモデルで 78%、Anthropic のモデルで 89% になり、標準ハーネス比で最大22ポイント上がったと公表した。Excel Online（Business）コネクタは読み取り専用の補助ツールを足したことで、成功率が 85.6% から 96.3% に上がった（7〜8月の本番テレメトリー）（Copilot）
  - https://www.microsoft.com/en-us/copilot/blog/copilot-studio/how-the-microsoft-copilot-harness-in-copilot-studio-helps-agents-finish-the-job/
- [据え置き] **Copilot Studio の Learn** — What's New・課金レート表・課金3本・モデル表3本・ガイダンスハブ・非推奨一覧・Purview は改訂されていない。Released Versions は 2026.6.3 のまま132日たつ（Copilot）
  - https://learn.microsoft.com/en-us/power-platform/released-versions/copilotstudio

### OpenAI / Codex / ChatGPT

- [据え置き] **OpenAI の一次** — Codex CLI は安定版 `0.167.0`（11/6）と `0.169.0-alpha.3`（11/7）のままで、API changelog・deprecations（いずれも 11/5）・ChatGPT & Codex changelog（11/6）も前回から動いていない。11/9 の OpenAI の発表は検索で見つからない（Master・industry）
  - https://github.com/openai/codex/releases

### Google

- [動向] **TPU の派生版2種** — Google が機密計算用の TPU 8tx と、TPU 8i を2枚1パッケージにした TPU 8i Max を発表し、1年で4システムを出したと The Decoder（11/9）が報じた。外部の TPU 顧客は約100社で、提供時期は書かれていない（industry）
  - https://the-decoder.com/google-ships-four-tpu-variants-in-one-year-as-it-ramps-up-competition-with-nvidia/
- [新機能] **Agent Substrate と gVisor の CNCF 寄贈** — Google がエージェント実行基盤 Agent Substrate と gVisor を CNCF に寄贈し、GKE 版の正式提供を始めたと Publickey（11/10）が報じた。Agent Substrate はアイドル中のエージェントをスナップショットに退避し、Google は従来比10倍の密度で動かせると主張しているが、独立した検証はない（industry）
  - https://www.publickey1.jp/blog/26/googlekubernetes10aiagent_sustrategvisorcncf.html
- [観測] **Gemini API の一次に届かない** — `ai.google.dev/gemini-api/docs/changelog` は本日も `aistudio.google.com` への 301 で、転送先はゲートウェイ拒否だった。11/17 の Live / TTS preview 停止と 12/1 の Argon 値上げは一次で再確認できていない（Master・industry）
- [据え置き] **Google の他ソース** — Workspace Updates、The Keyword の AI RSS（11/5 Gemini Omni 1.2 Flash）、Gemini アプリの release notes（2026.10.13）に新しい項目はない（Master）
  - https://blog.google/technology/ai/

### Cursor / 開発ツール / エージェント

- [新機能] **Orca v1.4.254 / v1.4.255** — Stably AI が 11/8・11/9 に Orca を更新し、利用者は Git Graph タブでブランチ・コミットを見てチェックアウト・cherry-pick・revert ができるようになった。会話を分けて横の質問をする `/btw`・`/fork` も加わり、`orca serve` は既定で公開インターネットのアドレスを拒む（Master）
  - https://github.com/stablyai/orca/releases
- [新機能] **Meta Muse Ember** — Meta がエージェントの定型作業向けの小型モデル Muse Ember を公開し、開発者は入力 $0.10・出力 $0.50（100万トークン）で Meta Model API と Muse Code から使えるようになった。コンテキストは1M。Meta はドル当たり性能が Haiku 5.5・GPT-6 Luna より高いとするが、FrontierCode 2.0-AA では Haiku 5.5 の34.9%に対し27.2%だった（industry）
  - https://the-decoder.com/meta-launches-muse-ember-a-small-ai-model-built-for-the-repetitive-work-agents-actually-do/
- [据え置き] **Cursor・xAI・Devin・MCP・Hugging Face** — Cursor の changelog（11/6）とフォーラム（10/12）、xAI（11/2）、Devin（11/6）、MCP blog（10/30）は動いておらず、Hugging Face の8 org にも新しいリポジトリはない（Master）

### 業界・市場

- [動向] **CrowdStrike の AI セキュリティ2社買収** — CrowdStrike が Fiddler AI と Dreadnode を合計約 $495M で買収すると 11/3 に発表した（金額は WSJ 報道で、CrowdStrike は非公表）。Fiddler のエージェント監視は Falcon Observe として組み込まれ、完了は同社 FY27 Q4 の見込み（industry）
  - https://securityweek.com/crowdstrike-reportedly-paying-495-million-for-ai-security-firms-fiddler-dreadnode
- [据え置き] **Anthropic の上場と未決の買収協議** — Anthropic の上場日・ロードショー開始を確定する報道はなく、価格帯入りの S-1/A も確認できていない。Amazon × Decart、Nvidia × Reflection AI の協議にも続報はない（industry）

### 日本語コミュニティ

- [動向] **Qiita の Copilot Studio / Power Automate 記事** — Qiita に、Copilot Studio のエージェントが止まらないときの再試行・終了条件の設計と、Power Automate のフロー設計で費用が膨らむ3つのパターンの記事が 11/9 に出た（Copilot）
  - https://qiita.com/tags/copilotstudio/feed

## 直近の注目予定

- **11/10**: Amazon Bedrock の Mythos 5 / Opus 4.7 / Sonnet 4.6 へのテキスト透かしの展開が完了予定 ／ Claude Desktop の管理ポリシーの扱いが変わる（中身は未公表）
- **11/12**: Anthropic の改定 Usage Policy が発効 ／ Copilot Studio の GPT-4.1 / GPT-5 系と、Microsoft Copilot ハーネスの GPT-5 Chat・GPT 5.6 Sol / Luna が退役（MC1506318） ／ OpenAI → Cursor のモデル供給停止予定（一次未読）
- **11/13**: Excel と Cowork の会計機能が GA（MC1536053）
- **11/15**: Dataverse for Teams 環境とアンマネージド開発者環境の新規作成が停止 ／ Copilot Studio のカスタム採点器ライブラリが GA
- **11/16**: Copilot から Claude Opus 4.8 / Opus 5 / GPT-5.6 Terra を廃止 ／ Teams の旧 GitHub アプリが退役 ／ `pull_request_target` の2回目の試験ブロック ／ Fable 5.2 ローンチ特典の Pro・Team 標準席の枠が 23:59 PT に終了 ／ Cowork / Autopilot の Engage プラグインが GA
- **11/17**: Gemini API の Live / TTS preview モデルが停止（4〜5種。一次未再確認） ／ Gems が Gemini アプリの設定パネルへ移動 ／ Intelligent call delegation が従量課金のパブリックプレビューに移行
- **11/17〜20**: Microsoft Ignite
- **11/18**: MODS の Workforce Insights エンドポイントが退役（MC1542066）
- **11/20**: Copilot Studio のコスト管理を M365 管理センターへ移す機能が GA（MC1530368） ／ Conductor のクラウド版が終了（二次）
- **11/24 以降**: `claude-opus-4-5-20251101` の暫定退役日（確定日ではない）
- **11/29**: OpenAI が Daybreak Blue のセッションデータの学習利用を開始（二次）
- **11/30**: `claude-sonnet-4-5-20250929` が退役 ／ Opus 4.8 の fast mode を削除 ／ OpenAI の Evals・`v1/prompts`・Agent Builder が停止 ／ App Builder のアプリが開けなくなる ／ vibe.powerapps.com と Power Automate のデザイナーの Copilot が退役 ／ Gemini 4 Argon の導入価格が終了
- **12/1**: Gemini 4 Argon の単価が $4/$20 に倍増 ／ Copilot の前提サブスク不要オファーが開始
- **12/2**: GitHub が公開リポジトリの `pull_request_target` を既定でブロック ／ Power Platform のプロンプトから Anthropic・Grok・旧 GPT 系モデルが退役（MC1536101）
- **12/4**: Copilot Studio エージェントの指標とアラートが GA（MC1538998）
- **12/11**: Power Apps の式の生成・Power Apps Ideas などが退役（MC1532421・MC1532426）
- **12/14**: claude.ai/design の単体サイトが閉鎖
- **12/31**: Claude Security の無償クレジットの対象期間が終了 ／ Partner Center の Copilot in 30 プロモーションが終了
- **2027-01-06**: OpenAI `tts-1` / `tts-1-hd` / `gpt-4o-mini-tts` 2版が停止
- **2027-01-14**: OpenAI `gpt-4o` 2版 / `gpt-4o-mini` / `gpt-4.1` / `gpt-4.1-mini` が停止
- **2027-01-15**: Claude Code Review の Enterprise 向けクレジット請求期限
- **2027-01-30**: ChatGPT Classic（旧デスクトップアプリ）が終了（二次）
- **2027-02-01**: OpenAI `gpt-5.5-cyber-preview` が停止
- **2027-03-08**: Fable 5.2 ローンチ特典のリセット（Max / Ultra / premium 席）が失効
- **2027-04-01**: OpenAI `gpt-5.1` / `gpt-5.3-codex` / `gpt-5.4-nano` が停止

## 改善メモ

- 3ソースとも新規提案・障害の変化なし。継続提案は Master 7件（最多 B-036、12回目）、Copilot 5件（最多 B-080、15回目）、industry 7件（最多 B-040、16回）
- Master は Fable 5.2 を B-086（Platform release notes RSS）と B-087（Privacy Center の `dateModified`）の経路で検出でき、両提案の実例として台帳に記録した
- ソース間の差異: Fable 5.2 の提供先を Master は「Claude Platform on AWS」、industry は「Bedrock」を含めて書き、`computer_20251124` の 400 も industry は「Bedrock 以外」と限定している。本サマリーは Master の記載に寄せ、Bedrock の扱いは一次で再確認が要る
- ソース間の差異: Gemini API の 11/17 停止モデル数を Master は「4モデル（5本目は未確定）」、industry は「5種」と書いている。一次に届かないため本サマリーは「4〜5種」とした
- 前日（11/9）分に欠損ソースはなく、欠損リカバリは不要
