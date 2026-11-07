# AI News Daily Summary — 2026-11-08

Microsoft は、EU / EFTA でリージョン間のデータ移動をオフにしている環境の Copilot ハーネスの GPT-5 Chat を 11/30 に終えると明記し、MODS の Workforce Insights エンドポイントを 11/18 に退役させる。Cowork の Power Platform コネクタは M365 管理センターで統制し、PPAC の DLP は効かないと告知した。GitHub は Copilot CLI `v1.0.107` で `alwaysApply: false` のプラグインルールを既定で読み込まないようにし、Copilot code review の設定を API で管理できるようにした。

## 今日のハイライト

### 1. [廃止] EU / EFTA の一部の環境で、Copilot ハーネスの GPT-5 Chat が 11/30 に終わる — 「期限なしで当面使える」とされていた例外に、延長できない期限がついた

**要点**: EU / EFTA でリージョン間のデータ移動をオフにしている環境のメーカーは、Microsoft Copilot ハーネスの GPT-5 Chat を 11/30 までしか使えなくなる。11/4 時点のモデル表は当面使えると書いていたが、EU AI Act の要件による期限で、延長できないと明記された。

**詳細**: `agents-experience/authoring-agent-model-availability`（11/7 07:03Z `87b278ff`・`ms.date` 11/6）で確認した（Copilot）。題名は「(GitHub Copilot)」のまま。

- 退役の表: GPT-5 Chat・GPT-5.6 Sol・GPT-5.6 Luna は 11/12、EU / EFTA でデータ移動オフの環境の GPT-5 Chat は 11/30。移行先は GPT-6 Luna（GPT-5.6 Sol は GPT-6.1 Sol）
- 対象外: 英国の環境にはこの制限がかからない。FedRAMP 環境の GPT-5 Chat は追って通知があるまで使える
- 求められる対応: 11/30 までに GPT-6 Luna でエージェントをテストする。データ移動の設定は「Move data across regions for Copilots, AI agents, and generative AI features」で確かめられる
- モデル表には GA のモデルが18件と、Mistral Medium 3.5（Experimental・欧州の早期アクセス環境だけ）が載っている

- https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-experience/authoring-agent-model-availability

### 2. [廃止] MODS の Workforce Insights エンドポイントが 11/18 に退役する — カスタム属性の送り先が M365 プロファイルのエンドポイントに一本化される

**要点**: 11/18 から、組織データソースの管理者は MODS の Workforce Insights エンドポイントにカスタム属性を送れなくなる。Workforce Insights エージェント（Frontier プレビュー）へのデータは M365 プロファイルのエンドポイント経由だけになり、非公開属性を使う組織は期限までに切り替えが要る。

**詳細**: MC1542066（11/6 公開・Act by 11/18）で確認した（Copilot）。

- 公開属性: M365 プロファイル経由の取り込みが既に GA になっている
- 非公開属性: プライベートプレビューに参加して、期限までに切り替える必要がある
- 対象外: 今このエンドポイントに属性を送っていない組織は対応しなくてよい

- https://mc.merill.net/message/MC1542066

### 3. [新機能+仕様] Cowork で Power Platform コネクタが使えるようになり、可否は M365 管理センターで決まる — PPAC の DLP ポリシーでは Cowork のコネクタ利用を止められない

**要点**: 管理者は、Cowork が使う Power Platform コネクタを M365 管理センターの Agents > Tools で許可・ブロックするようになる。Power Platform の統制は PPAC の DLP が前提だったが、MC1542062 は PPAC の DLP が Cowork に適用されないと明記した。展開は11月中旬に終わる。

**詳細**: MC1542062（11/6 公開・Feature update / Admin impact）で確認した（Copilot）。

- 対象: プラグインとして公開された Power Platform コネクタ。M365 管理センターへのコネクタの追加は順次続き、追加されたものから Cowork で使えるようになる
- 設定の効き方: Cowork は接続の作成と操作の実行のどちらでも設定に従う。ブロックする前に作った接続にも効き、Cowork Automations にも同じポリシーがかかる
- 変わらないもの: メール・予定表・Teams・ファイルの既存の M365 機能
- 求められる対応: Agents > Tools で使えるコネクタを確かめ、PPAC の DLP が効かないことを踏まえて統制要件を見直す

- https://mc.merill.net/message/MC1542062

## カテゴリ別まとめ

### GitHub Copilot

- [破壊的変更+新機能] **Copilot CLI v1.0.107** — GitHub が 11/6、前日の `v1.0.106` に続けて Copilot CLI の安定版 `v1.0.107` を出し、`alwaysApply: false` のプラグインルールは `/instructions` で有効にするまで読み込まれなくなった。これまでは `/instructions` か `/plugins` を開くまで全セッションに掛かっていたので、ルールが効いている前提の運用は更新後に挙動が変わる（Master）
  - 既定の変更: `/statusline` の `quota` 項目は既定でオフ（`ai-used` はオン）。macOS では `copyOnSelect` が既定でオン
  - 安全側の修正: `/session delete --yes=false` や打ち間違えた `--yes=<値>` で現在のセッションが消えなくなった。`copilot login --device-code` は `http://` のホストを拒否する。プラグインが有効な間はローカル marketplace を削除できない（`--force` で一緒に外す）
  - 新機能: `/code` で現在のセッションを VS Code で開ける。`/settings` の統合ダッシュボードを全ユーザーに開放した。アカウントで使えれば GPT-6.1 Terra を選べ、`copilot config` に Fusion tier の設定が加わった。拡張のプロセスをサンドボックス内で動かす設定も加わった
  - 挙動の修正: レビューや分析だけを頼んだのに Autopilot が推奨を実装し始める問題を直した。pre-release は `v1.0.108-1`（11/7）まで進んだ
  - https://github.com/github/copilot-cli/releases
- [新機能] **Copilot code review の API 管理** — GitHub が 11/6、Copilot code review の有効化・既定の effort・runner を、enterprise・organization・repository の各階層で REST / GraphQL API から読み書きできるようにした。上位が管理する設定は下位で上書きできない（Master・industry）
  - ⚠️ 認証の制約: enterprise と organization の設定エンドポイント（runner を含む）は GitHub Apps と fine-grained PAT に対応しない。repository の設定は両方に対応し、読みに Administration: read、書きに Administration: write が要る
  - 出力の識別: レビューとコメントに Copilot の帰属フィールドが付き、使った effort とコメントの根拠になった skill・MCP サーバー・カスタム指示を取れる
  - そのほか: Balanced effort は3つのレビューモデルの指摘を別のモデルがまとめる形になった。消費した AI credits をセッションに出し、失敗・タイムアウトは1回自動で再試行する。自動レビューのリポジトリルールが bypass list に対応した
  - 対象: Copilot Pro / Pro+ / Max / Business / Enterprise。料金の改定は書かれていない
  - https://github.blog/changelog/2026-11-06-copilot-code-review-api-management-and-review-overview-updates
- [新機能] **Slack と Teams の @GitHub が GA** — GitHub が 11/6、Slack と Teams から Copilot に作業を頼む @GitHub を GA にし、利用者はバグ調査から Issue・PR 作成までを会話の中で進められるようになった。Teams では Canvas で実装計画・コード変更・プレビューを会話の横で確認できる（Master・industry）
  - 開始と記録: メッセージからリポジトリを特定して選び直さずにセッションを始め、作った Issue と PR の説明に「Created from a Slack/Teams conversation with @username」が入る
  - 対象プランと AI クレジットの扱いは書かれていない
  - https://github.blog/changelog/2026-11-06-github-copilot-in-slack-and-teams-is-generally-available
- [新機能] **Copilot 週次まとめ（11/2 週）** — GitHub が 11/6 の週次まとめで、利用者が Copilot app の PR から Agent Merge を設定できるようにしたと公開した。必須チェックが保留中でも設定は有効のまま残る（Master・industry）
  - Copilot app: 確認なしで許可するツール呼び出しを、個人の指示で決められる（opt-in・ローカルセッションのみ）
  - VS Code 1.145: ローカルの automation が cron 式とワークスペースのカスタムエージェントに対応した。Agents window でリモートのアプリのプレビューと canvas を使える（preview）
  - JetBrains Air: 既存の Copilot サブスクリプションで、複数のエージェントセッションをローカルかクラウドで動かせる
  - https://github.blog/changelog/2026-11-06-github-copilot-weekly-releases-november-2
- [仕様] **Copilot impact dashboard の集計対象** — GitHub が 11/6、Agent adoption チャートに Copilot Chat と VS Code の Agents window を加え、集計対象を9機能にした。「Passive users」は「Chat-first users」に改めたが、API 上は No Cohort のままで人数も変わらない（Master）
  - 28日レポートの `copilot_feature_engagement.totals_by_feature` に `chat` と `vscode_agent` が加わる。変更前の期間は従来の7機能だけ
  - https://github.blog/changelog/2026-11-06-copilot-impact-dashboard-adds-chat-and-vs-code-agent-usage

### Microsoft 365 Copilot

- **EU / EFTA の GPT-5 Chat の終了**（ハイライト1参照）
- **MODS の Workforce Insights エンドポイントの退役**（ハイライト2参照）
- **Cowork の Power Platform コネクタ**（ハイライト3参照）
- [予定] **外部メールを Copilot から外す Purview DLP の GA 延期** — Microsoft が MC1301714（11/6 更新・Roadmap 561552）で、管理者が外部ドメインからのメールを M365 Copilot と Copilot Chat の参照・要約・根拠づけから外す DLP の GA を、2027年1月下旬〜2月下旬から6月上旬〜下旬に延ばした。パブリックプレビューは2026年6月から続いている（Copilot）
  - https://mc.merill.net/message/MC1301714
- [新機能] **Cowork の OneNote 対応** — Microsoft が Cowork What's New の November 節（11/7 01:03Z `7a597bb3`）で、利用者が Cowork にノートブックを探させ、ページを要約させ、承認のうえでページを更新・追加させられるようにした（Copilot）
  - 編集の範囲: 段落の追加・置き換え・削除、表の追加、ページ名の変更、ノートタグの更新。ノートブックとセクションは作れない
  - ⚠️ 承認すると下書きではなくノートブックが直接変わる。「Always allow」はその会話の中だけで有効で、段落を置き換えるとリンクや混在した書式が消えることがある
  - https://learn.microsoft.com/en-us/copilot/cowork/use-cowork#work-with-onenote-notebooks
- [新機能] **Purview DLP for Cowork が Launched** — Microsoft が Roadmap 570845（GA October CY2026）を Launched にし、データセキュリティ管理者は M365 Copilot と Cowork を1本の DLP ポリシーで統制できるようになった。10/21 に Rolling out になった項目の展開が終わった（Copilot）
  - https://www.microsoft.com/releasecommunications/api/v1/m365
- [予定] **Roadmap 11/6 23:04Z バッチ** — Microsoft が Roadmap に新規12件を足し、そのうち Copilot 関連の3件で Work IQ と Teams Facilitator の機能を予告した。残る9件は Dynamics 365 で、総項目数は 2,302 になった（Copilot）
  - 570866 Work IQ Execute（Recipes）: エージェントが再利用できる Work IQ のレシピを実行できるようになる。GA November CY2026
  - 570670 Work IQ Federated connectors: Work IQ がフェデレーテッドコネクタでほかの業務データソースにアクセスできるようになる。GA November CY2026
  - 566523 Teams Facilitator follow-up mode: 利用者が毎回タグづけせずに Facilitator と話せるようになる。GA December CY2026
  - https://www.microsoft.com/releasecommunications/api/v2/m365/rss
- [廃止] **Roadmap 502543 が Cancelled** — Microsoft が、Copilot Chat でサードパーティのコンテンツの詳しい引用と横並びのプレビューを見られるようにする拡張機能を、提供しないことにした。11/7 の 502546 / 502547 と同じく「正確でなくなったため Roadmap から外す」としている（Copilot）
  - https://www.microsoft.com/releasecommunications/api/v1/m365
- [予定] **MC の展開時期の延期2件** — Microsoft が 11/6、管理者主導の Copilot オンボーディング（MC1486291・Frontier）の完了を11月上旬から11月下旬に、Windows の Copilot Notebooks のマルチモーダルキャプチャ（MC1405506）の開始・完了を10月末から11月末に延ばした（Copilot）
  - https://mc.merill.net/message/MC1486291
- [新機能] **Partner Center の Copilot in 30 支援** — Microsoft が Partner Center の11月ページ（11/6 23:03Z `21f6b4af`）で、CSP パートナーが ASPX の Copilot in 30 Trial Recommendations で試用中の顧客ごとに次の打ち手を見られるようにした。Copilot in 30 のプロモーションは 12/31 までである（Copilot）
  - CloudAscent: Business SKU 50席以上で有償の Copilot がない顧客を、30日試用の優先先として示す
  - ASPX: Trial Days Remaining と、管理者設定の推奨（Usage-Based Billing・Teams の文字起こし・Copilot コネクタ）が加わった
  - https://learn.microsoft.com/en-us/partner-center/announcements/2026-november
- [据え置き] **その他の M365 Copilot** — M365 Copilot Release Notes・拡張機能 What's New・`cowork-models`・`cowork-admin-governance`・`opal-settings-manage`（UBB と支出ポリシーの記載はまだない）は改訂されておらず、Copilot ブログと TC の各 board にも新しい記事はない（Copilot）
  - https://www.microsoft.com/en-us/copilot/blog/

### Copilot Studio / Power Platform

- [動向] **Microsoft Copilot ハーネスの論文** — Copilot Studio のチームが 11/7、標準ハーネスと Microsoft Copilot ハーネスを同じ評価タスク・同じモデルで比べた結果を公開した。Microsoft Copilot ハーネスは1タスクあたりのモデル呼び出しが2倍になるが、キャッシュのヒットが平均40ポイント上がり、コスト換算のトークン消費は15〜21%減ったとしている（Copilot）
  - 評価の合格率: GPT-5.5 Chat で10.8ポイント、Opus 4.8 で22.1ポイント上がった。呼び出しあたりの遅延は10〜36%下がった
  - 本番での挙動: ツール呼び出しの失敗後も作業を続けた割合は84〜91%で、標準ハーネスは7%未満だった
  - 業務プロセスのベンチマーク: 65% 対 36%（比較相手は「大手の競合」とだけ書かれている）
  - https://techcommunity.microsoft.com/t5/copilot-studio-blog/paper-how-utilizing-the-microsoft-copilot-harness-in-copilot/ba-p/4571157
- [据え置き] **Learn とブログ** — Copilot Studio What's New・課金レート表・`billing-licensing`・標準ハーネスのモデル表・ガイダンスハブ・非推奨一覧・Purview は改訂されていない。Released Versions は 2026.6.3 のまま130日たち、Power Platform ブログにも新しい記事はない（Copilot）
  - https://learn.microsoft.com/en-us/microsoft-copilot-studio/whats-new

### Anthropic / Claude

- [仕様] **エージェントのメモリの解説** — Anthropic が 11/6、エージェントのメモリの組み立て方を解説する記事を公開し、Claude Code の auto memory が `MEMORY.md` の先頭200行か 25KB までしか読み込まないと明記した（Master）
  - 公開した資料: Managed Agents のセッションをまたぐメモリディレクトリ、memory tool、過去ログをオフラインで見直してメモリを直す「dreaming」と知識 wiki の cookbook
  - 数値: CL-Bench のデータベース課題で、Claude Opus 5.5 の平均報酬はメモリありで 0.655 → 0.838。社内文書コーパスでは wiki＋検索が128回の dreaming で 54% → 61% になり、1問あたり約2万トークンを減らした
  - https://www.anthropic.com/research/components-of-agent-memory
- [据え置き] **Claude Code・API・退役ページ** — Claude Code の最上位は `2.1.319`（11/6）のままで、npm も `{stable: 2.1.311, latest: 2.1.319, next: 2.1.319}` で変わらない。Platform の release notes の最上位は 11/5、退役ページは Active 15件・Deprecation history 最新 9/30 のままで、Opus 4.5（下限 11/24）の告知も無い。`/news`・`claude.com/resources/articles`・Privacy Center にも動きはない（Master・industry）
  - https://platform.claude.com/docs/en/about-claude/model-deprecations

### OpenAI / Codex / ChatGPT

- [据え置き] **Codex CLI と OpenAI の一次** — Codex CLI の安定版は `0.167.0`（11/6）のままで、pre-release は `0.169.0-alpha.2`（11/6）まで進んだ。API changelog・deprecations（いずれも最上位 11/5）・Deployment Safety Hub・community Announcements・misalignment reports・ChatGPT & Codex changelog は前回のままで、xAI のモデル一覧も grok-4.7 が最新のまま（Master・industry）
  - https://github.com/openai/codex/releases
  - https://developers.openai.com/api/docs/deprecations

### Cursor / 開発ツール

- [新機能] **Cursor Voice Chat** — Cursor が 11/6、利用者がエージェントとリアルタイムの音声通話で話しながら作業を任せられる Voice Chat を出した。音声エージェントが話を聞いてコーディングはチャットのエージェントに渡し、作業中も差分や進捗を声で尋ねられる。音声は xAI の Grok Voice が処理し、Privacy Mode ではゼロデータ保持で動く（Master）
  - 使える場所: Agents Window・IDE・Web・Cursor for iOS。エージェントが待機中で入力欄が空のとき、送信ボタンの位置の波形ボタンで通話を始める
  - iOS: 「Hey Siri, call Cursor」で通話を始め、ロック画面の Live Activity でミュート・終了できる
  - 既存機能との関係: 音声入力（旧称 Voice Mode、IDE では Cmd+Shift+Space）は別機能として残る
  - https://cursor.com/changelog/voice-chat
- [破壊的変更+新機能] **Orca v1.4.252** — Stably AI が 11/7 に Orca のデスクトップ版 `v1.4.252` を出し、利用者は Claude と Codex のチャットで Plan mode を使えるようになった。完了した応答のどこからでもチャットを分岐でき、Codex の承認には変更されるファイルと差分が出る（Master）
  - ⚠️ 互換性: macOS の最低要件が 13.4 になった（以前は 12）。Zipformer EN の音声入力モデルを削除し、選んでいた人は Parakeet v2 に移る。ローカルのブラウザ制御プロキシはセッションごとのトークンを要する。`v1.4.251` に戻すと Plan mode のチャットは再度更新するまで開けない
  - 同日の `v1.4.253` は小改善のみ
  - https://github.com/stablyai/orca/releases
- [新機能] **Baseten の Grid と Sandboxes** — TLDR AI（11/4）経由の同社ブログによると、Baseten がモデル振り分けの「Grid」と、VM で分けられ再開できるエージェント実行環境「Sandboxes」を出した。教師ありファインチューニングと強化学習をサーバーレスで回す Loops は GA になり、学習した重みは顧客のものになる（industry）
  - https://www.baseten.co/blog/the-building-blocks-of-the-open-frontier
- [観測] **Gemini API の一次ページ** — `ai.google.dev/gemini-api/docs/changelog` と deprecations は本日も 301 で `aistudio.google.com` に移り、転送先はこの環境から届かない（6日連続）。11/17 の Live / TTS preview モデルの停止と 12/1 の Argon 値上げは、本日も一次で確かめられていない（Master・industry）
- [据え置き] **Google・その他のエージェント・MCP** — Workspace Updates の 11/6 週次まとめは既報の項目が中心で、Gemini アプリの release notes は 2026.10.13 のまま。Cursor フォーラム（10/12）と Devin（11/2）は動いておらず、TypeSafe AI は `jev-1.14.0` のまま、MCP blog は 10/30 のまま、Hugging Face の8 org に新規は無い（Master）

### 業界・市場

- [動向] **Anthropic の IPO の評価額** — The Decoder（11/7）が FT をもとに、Anthropic が評価額を下げても感謝祭前の上場を進めると伝えた。調達額は $80B〜$100B、評価額は $1.25T〜$1.75T の範囲とされ、直近の $965B は上回るが一部の投資家が期待した $2T には届かない。年換算の売上は約 $81B（7月末は約 $65B）（industry）
  - 評価額は前日の報道（$1.1T〜$1.5T）とずれており、引き続き割れている
  - https://the-decoder.com/anthropic-pushes-ahead-with-pre-thanksgiving-ipo-despite-tech-selloff-accepts-lower-valuation/
- [動向] **OpenAI の $11B 調達** — The Decoder（11/7）が Bloomberg（11/6）をもとに、OpenAI が評価額 $1.25T で $11B を調達し終え、当初の評価額 $1.4T・$30B の目標を下げたと伝えた。ラウンド全体は最大 $20B まで広がる可能性があり、投資銀行を通じて富裕層の個人投資家にも声をかけている（industry）
  - https://the-decoder.com/openai-lands-an-11-billion-funding-round-but-has-to-court-dentists-for-more-capital/
- [セキュリティ] **オープンモデルのサイバー攻撃能力** — The Decoder（11/7）によると、Vals AI の CyberOffense ベンチマークで Deepseek V4.1 Flash の達成率は72.8%、OpenAI の Daybreak 限定の GPT-6 Sol は80.8% だった。1回あたりの費用は Deepseek が約 $3、GPT-6 Sol が約 $22 で、英 AISI は両者の差が 6〜10カ月から 4〜7カ月に縮まったとしている（industry）
  - https://the-decoder.com/the-gap-between-open-and-closed-ai-models-in-cyber-capabilities-keeps-shrinking/
- [据え置き] **買収協議と国内調査** — Amazon × Decart、Nvidia × Reflection AI の買収協議に続報はなく、Anthropic の S-1/A の本文も未確認のまま。IDC Japan・MM総研・NRC の新しい公表も無い（industry）

## 直近の注目予定

- **11月**: GitHub の cloud sandbox の課金が開始（日付は明記なし） ／ Work IQ Execute（Recipes）と Work IQ Federated connectors が GA（Roadmap 570866・570670）
- **11/9**: Opal（Frontier）で UBB と支出ポリシーが前提になる（MC1540330） ／ GitHub が公開リポジトリの `pull_request_target` を試験ブロック（16:00〜18:00 UTC） ／ 2,001席以上の組織で、ライセンスのない Copilot Chat 利用者の上限拡大が開始 ／ Dataverse のみのテナントでストレージ検証が開始（MC1483529）
- **11/10**: Amazon Bedrock の Mythos 5 / Opus 4.7 / Sonnet 4.6 へのテキスト透かし展開が完了予定 ／ Claude Desktop の管理ポリシーに関わる変更（中身は一次未確認）
- **11/12**: Copilot Studio の GPT-4.1 / GPT-5 系と、Copilot ハーネスの GPT-5 Chat・GPT-5.6 Sol / Luna が退役（MC1506318） ／ Anthropic Usage Policy 改定版が発効 ／ OpenAI → Cursor のモデル供給停止予定（一次未読）
- **11/13**: Excel と Cowork の会計機能が GA（MC1536053）
- **11/15**: Dataverse for Teams 環境とアンマネージド開発者環境の新規作成が停止 ／ Copilot Studio のカスタム採点器ライブラリが GA（MC1531932）
- **11/16**: GitHub Copilot が Claude Opus 4.8・Opus 5・GPT-5.6 Terra を廃止 ／ Teams の旧 GitHub アプリが退役 ／ `pull_request_target` の2回目の試験ブロック ／ Cowork / Autopilot の Engage プラグインが GA（MC1530609） ／ Claude Opus 4.6・Opus 4.5・Sonnet 4.5・Haiku 4.5 に透かしが入る（二次）
- **11/17**: Intelligent call delegation が従量課金のパブリックプレビューへ移行（MC1537490） ／ Sales Agent のセマンティックモデルが GA（MC1540293） ／ Gems が Gemini アプリの設定パネルへ移動 ／ Gemini API の TTS・Live プレビューモデルが停止（最短日。一次未確認）
- **11月中旬**: 単体の Word / Excel / PowerPoint エージェントの撤去が開始（MC1536062） ／ Office in Copilot の展開が完了（MC1530611） ／ Learning Agent のプレイリスト（MC1537495） ／ Cowork の Power Platform コネクタの展開が完了（MC1542062）
- **11/17〜20**: Microsoft Ignite
- **11/18**: MODS の Workforce Insights エンドポイントが退役（MC1542066）
- **11/20**: Conductor のクラウド版が終了（二次） ／ Copilot Studio のコスト管理を M365 管理センターへ移す機能が GA（MC1530368）
- **11/24 以降**: `claude-opus-4-5-20251101` の暫定退役日（確定日ではない）
- **11月下旬**: Work IQ API で Copilot コネクタのデータが使えるようになる（MC1538999） ／ Cowork の Planner Plugin の GA 展開が完了（MC1540339） ／ 管理者主導の Copilot オンボーディングの展開が完了（MC1486291）
- **11/29**: OpenAI が Daybreak Blue のセッションデータの学習利用を開始（二次）
- **11月末**: Word の Top of Doc 要約の廃止が完了（MC1454113） ／ Notebooks の Power BI 参照の GA が開始（MC1474458） ／ Windows の Copilot Notebooks のマルチモーダルキャプチャ（MC1405506）
- **11/30**: EU / EFTA でデータ移動オフの環境の GPT-5 Chat（Copilot ハーネス）が終了 ／ Power Automate のデザイナーの Copilot がサポート終了（MC1540258） ／ Power Automate の Describe it to design it が退役（MC1537406） ／ モデル駆動アプリの説明文の AI 生成が退役（MC1540110） ／ App Builder と vibe.powerapps.com が退役 ／ `claude-sonnet-4-5-20250929` が Claude API から退役 ／ Opus 4.8 の fast mode を削除 ／ OpenAI の Evals・`v1/prompts`・Agent Builder が停止 ／ Gemini 4 Argon の導入価格が終了
- **12/1**: M365 Copilot の前提サブスク不要オファー開始 ／ Business Central + Copilot Business のバンドルが CSP の価格表プレビューに載る ／ Gemini 4 Argon の単価が $4/$20 に倍増 ／ Google スライドの複数スライド作成の上限引き上げ優待が終了しうる
- **12/2**: Power Platform のプロンプトから Anthropic・Grok・旧 GPT 系のモデルが退役し自動移行（MC1536101） ／ GitHub が公開リポジトリの `pull_request_target` を既定でブロック
- **12/4**: Copilot Studio エージェントの指標とアラートが GA（MC1538998）
- **12月上旬**: UBB モデル（GPT-6 Astra / Claude Fable 5.1）の Chat と Word / Excel / PowerPoint での GA が開始（MC1519122） ／ Teams 会議の MeetingAI ポリシーの Targeted Release が開始（MC1532253） ／ Work IQ MCP のメモリーの読み取り（MC1539004）と Planner Agent の拡張（MC1539002）が開始
- **12月**: Teams Facilitator follow-up mode が GA（Roadmap 566523） ／ ChatGPT と Codex の利用枠が Plus・Pro・Business で1つの予算に統合（日付未公表・二次）
- **12/11**: Power Apps の式の生成・Power Apps Ideas・Copilot によるコントロール名の変更が退役（MC1532421・MC1532426）
- **12/14**: claude.ai/design の単体サイトが閉鎖
- **12/31**: Power Platform の環境間のコメントのインポート・エクスポートが終了 ／ Claude Security の無償クレジット（月 $25,000×2か月）の対象期間が終了 ／ Partner Center の Copilot in 30 プロモーションが終了
- **2026年末まで**: Copilot の Claude モデルの処理が EU Data Boundary の内側に移る
- **2027-01-06**: OpenAI `tts-1` / `tts-1-hd` / `gpt-4o-mini-tts` 2版が停止
- **2027年1月**: Targeted release が退役 ／ Business Central + Copilot Business のバンドルの販売が開始（1/1） ／ SharePoint / OneDrive の Copilot Search の GA 展開が開始（1月中旬・MC1540513）
- **2027-01-14**: OpenAI の GPT-4o・GPT-4o mini・GPT-4.1・GPT-4.1 mini が API から削除（→ `gpt-6-luna`）
- **2027-01-15**: Claude Code Review の Enterprise 向けクレジット請求期限
- **2027-01-30**: ChatGPT Classic（旧デスクトップアプリ）が終了（二次）
- **2027年1〜3月**: CSP の Copilot Business 新規購入で従量課金が既定オン
- **2027-02-01**: OpenAI の `gpt-5.5-cyber-preview` が API から削除
- **2027-03-01 以降**: Gems 廃止（Business / Enterprise）
- **2027年春**: Siri AI 対応アプリの App Store 提出受付が開始
- **2027-04-01**: OpenAI `gpt-5.1` / `gpt-5.3-codex` / `gpt-5.4-nano` が停止
- **2027年6月**: 外部メールを Copilot の処理から外す Purview DLP が GA（MC1301714。旧予定は2027年1〜2月）

## 改善メモ

- 新規提案: 3ソースとも新規起票なし
- 継続提案: Master は継続7件（最多 B-036 DeepSeek 登録、12回目。B-088 Gemini API Changelog の URL 差し替えは5回目） ／ Copilot は継続4件（最多 B-080 Cowork の Learn URL 差し替え、13回目。B-081 はモデル表の題名が「GitHub Copilot」のままで11回目） ／ industry は継続7件（最多 B-040 セキュリティ開示の定点、15回。見送り候補 B-036）
- 障害の変化: 3ソースとも変化なし
- 欠損リカバリ: 前日（11/7）分は3ソース揃っており、対象なし
- ソース間の差分・矛盾:
  - ハイライトの顔ぶれが割れた。Master は Copilot CLI `v1.0.107`・code review API・Cursor Voice Chat、industry は code review API・Slack / Teams の @GitHub をハイライトにした。本サマリーは選定基準の順（1 期限 → 2 前提の変化 → 3 手が動く）に従い、期限のある GPT-5 Chat（11/30）と MODS（11/18）、前提が変わる Cowork の DLP を採り、GitHub と Cursor の3件はカテゴリに置いた
  - Copilot code review のタグが、Master は `[新機能]`、industry は `[新機能+仕様]` で割れた。API 管理の追加が主旨で、明文化された上限は副次的なため、本サマリーは `[新機能]` を採った
  - Copilot impact dashboard の更新は、Master が `[仕様]` で載せ、industry は小規模として見送った。本サマリーは Master に合わせて載せた
  - Copilot CLI の `/settings` ダッシュボードは Master の `v1.0.107` と industry の週次まとめの両方に出たため、`v1.0.107` の項目に寄せた
