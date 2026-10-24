# AI News Daily Summary — 2026-10-25

GitHub は Teams の旧 GitHub アプリを 11/16 に退役させ、Copilot を統合した新アプリへの入れ替えを求めた。Microsoft は Viva Insights の GitHub Copilot 指標を11月中旬から既定でオンにし、オプトインの設定を消す。Claude Code `2.1.310` はクラウドセッションと Remote Control をロール単位で許可できるようにしたが、npm の `stable` は `2.1.308` のままである。

## 今日のハイライト

### 1. [廃止+新機能] GitHub が Teams の旧 GitHub アプリを 11/16 に退役させる — Teams から Copilot を使い続けるには統合版アプリへの入れ替えが要る

**要点**: GitHub が 10/23 に、Teams の通知アプリ「GitHub notifications」に Copilot を統合し、`@GitHub` に Issue の調査から修正 PR の作成まで頼めるようにした。旧 GitHub アプリは「GitHub (deprecated)」に改名され 11/16 に退役する。旧アプリのままの組織は、期限後に Teams から Copilot を呼べなくなる。

**詳細**:

- 統合版アプリ: チャンネル・グループチャット・個人チャットで通知を受け、`@GitHub` で操作を頼める。Teams に届いたバグ報告から原因を調べて修正し、PR を開く流れを例示している
- 既存の GitHub notifications 利用者: 最新版へ更新すれば通知の機能はそのまま動く
- 旧 GitHub アプリ（legacy）利用者: 統合版を入れ直し、`@GitHub` から GitHub アカウントの接続とリポジトリの選択をやり直す
- 未記載: 料金・対象プラン・GA かプレビューか。退役日の「November 16」には年が書かれていない（industry の指摘）
- Master・industry の両方がハイライトに採った

- https://github.blog/changelog/2026-10-23-turn-notifications-into-code-with-github-copilot-in-teams

### 2. [破壊的変更] Viva Insights の GitHub Copilot 指標が11月中旬から既定でオンになる — オプトインしていない組織でも既存のレポート閲覧者に開発者の利用状況が見え始める

**要点**: MC1523085（10/23）によると、Viva Insights の消費ダッシュボードで GitHub Copilot 指標が11月中旬から既定で表示され、パブリックプレビューのオプトイン設定は削除される。オプトインしなければ非表示だった開発者の利用データが、既存の閲覧権限を持つ人に自動で見えるようになり、止める設定も残らない。

**詳細**:

- 展開: 全世界で11月中旬に始まり、12月中旬に完了する見込み
- 見えるようになる人: グローバル管理者、グローバルパーティションを持つ Insights アナリスト、消費インサイトにアクセスできるマネージャー
- 変わらないもの: 既存のロール・権限・プライバシー設定は引き続き効く
- 管理者の作業: 消費インサイトのアクセス権を見直し、社内の説明資料を更新する
- 同じ日に GitHub 側は使用量メトリクス API に外部ツール別の `totals_by_client` を加えており（下の GitHub 節）、Copilot の利用の可視化が2方向で同時に進んだ

- https://mc.merill.net/message/MC1523085

### 3. [セキュリティ+新機能] Anthropic が Claude Code `2.1.310` でクラウドセッションと Remote Control の権限を Enterprise のカスタムロールに加えた — Windows で PreToolUse フックがツール呼び出しを通していた不具合も直した

**要点**: Anthropic が 10/23 21:20Z に `2.1.310` を出し、組織単位のオン・オフしかなかったクラウドセッションと Remote Control を、Owner がロール単位で許可できるようにした。Windows でフックが効かずにツールが実行される穴も塞いだ。npm `stable` は `2.1.308` のままで、stable 固定の組織には `2.1.309` のサンドボックス修正も届いていない。

**詳細**:

- 管理設定
  - Enterprise のカスタムロール: Claude Code クラウドセッションと Remote Control の権限を追加した
  - 管理画面でどちらかをオンにすると、その権限を持つカスタムロールを列挙して確認を出す
  - クラウド環境の設定画面: ネットワークアクセス・セットアップスクリプト・環境変数を行から開く形に変え、セットアップスクリプトはファイルから読み込める
- 修正
  - Windows: Git Bash が無く、フックのコマンドが引用符つきの文字列だけのとき、PreToolUse / PermissionRequest フックがツール呼び出しを通していた
  - `cleanupPeriodDays` を非常に大きくすると、貼り付けた画像など最近のファイルを後片付けが消していた
- そのほか: Monitor ツールとプラグインのモニターが Bedrock / Vertex / Foundry と、テレメトリや非必須通信を切った環境でも動く。`effort-2025-11-24` beta 値や会話途中の system メッセージを拒むゲートウェイ・互換サーバーでは、それらを外して再試行する
- npm `{stable: 2.1.308, latest: 2.1.310, next: 2.1.310}`

- https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md
- https://registry.npmjs.org/@anthropic-ai/claude-code

## カテゴリ別まとめ

### Claude / Anthropic

- **Claude Code `2.1.310`**（ハイライト3参照）
- [仕様] **Claude Duet の安全設計** — Anthropic が 10/23 に、Claude Duet が承認されても実行しない操作と、「今後は確認しない」が効かない操作を明記した安全設計を公表した。対象は従来どおり米国の Pro / Max（ウェイトリスト）である
  - 承認しても実行しない操作: 証券の売買、口座間の送金などの銀行操作、他人のアカウントへのアクセス
  - 毎回確認する操作: 支払い・送金、注文の削除、アカウント作成。承認後もモデルの外にある別のチェックが各操作を検証する
  - 機密情報: 認証情報・カード番号・政府発行 ID は頼まれても送らず、健康・財務の情報は明示の承認があるときだけ送る
  - 認証の扱い: パスワードはアプリ内のフォームで使い捨ての鍵で暗号化して渡し、ブラウザは別の VM で動いてエージェントは Cookie を読めない
  - データ保持: 会話履歴とメモリは削除・リセットするまで残り、接続アプリを切っても得た情報はメモリをリセットするまで残る。学習への利用と管理者設定には触れていない
  - https://claude.com/resources/articles/claude-duet-safety-privacy-and-security
- [据え置き] **Claude Tag API・退役ページ・ニュース一覧** — Claude Platform release notes の 10/20 の下に追記された Claude Tag API（beta）は 10-24 既報で、Master は本日初検出として載せた。モデル退役ページの Active は15件のままで、Deprecation history の最新も 9/30 の Sonnet 4.5（11/30 退役）である。`/news` は 10/22、`/research` は 10/23 の UK AISI 事案の分析が最上位のまま
  - https://platform.claude.com/docs/en/release-notes/overview#october-20-2026

### GitHub Copilot / GitHub

- **Teams の旧 GitHub アプリの退役と Copilot in Teams**（ハイライト1参照）
- [新機能] **使用量メトリクス API の `totals_by_client`** — GitHub が 10/23 に、Copilot をモデル提供元として使う外部ツール（Claude Code・Codex・OpenCode など）のリクエストとトークンをサーバー側で数え、ツール別に返すようにした。IDE テレメトリに頼る `totals_by_ide` に出なかった利用を、組織が実数で把握できる
  - 対象レポート: enterprise / organization / enterprise-user / organization-user の1日版と28日版。28日版は各 `day_totals` に入る
  - `client`: `opencode` / `claude_code` / `codex` / `zed` / `copilot_cli` / `github_app` / `cloud_agent` / `code_review` / `vscode` / `jetbrains`。判別できないものは `other`
  - 出る値: `request_count` / `session_count` / `token_usage` と、`model_selection_mode`（`user_selected` / `auto` / `product_selected`）つきのモデル別内訳
  - 制約: `request_count` はプロンプト数ではなくモデル呼び出し数で、クライアント判定は各リクエストが送る統合 ID に頼る推定である。Copilot コードレビューのモデルは `unknown` になる
  - 閲覧: enterprise owner・billing manager・organization owner と View Copilot Metrics 権限のカスタムロール。利用指標ポリシーの有効化が要る
  - https://github.blog/changelog/2026-10-23-usage-metrics-api-adds-usage-from-tools-like-opencode
- [新機能] **Secret scanning の public monitoring** — GitHub が 10/23 に、公開リポジトリに漏れた自社の秘密情報を検知する GitHub Enterprise Cloud の public monitoring（パブリックプレビュー）に、アラートの却下・修正済みへの変更、漏れたトークンが今も有効かの継続確認、エンタープライズ向け REST API と `secret_scanning_public_monitoring_alert` webhook を加えた。GitHub Advanced Security か GitHub Secret Protection のライセンスに含まれ、追加料金はない
  - https://github.blog/changelog/2026-10-23-public-monitoring-adds-triage-validity-api-and-webhooks
- [版更新] **Copilot CLI `v1.0.104-1`〜`-3`** — GitHub が 10/23〜10/24 に pre-release を出し、管理モデル「fusion」が Auto で始まって `fusionTier` 設定が効くようにした。対話型と SDK の Autopilot セッションは `COPILOT_TASK_WAIT_TIMEOUT_SECONDS` で止まらず、接続中のバックグラウンドタスクを待つ。Latest は `v1.0.103` のまま
  - https://github.com/github/copilot-cli/releases

### Microsoft 365 Copilot / Agent 365

- **Viva Insights の GitHub Copilot 指標の既定オン**（ハイライト2参照）
- [予定] **Teams モバイルの検索から Copilot** — （MC1523087・Roadmap 571299）iOS / Android の Teams 利用者は、検索ボックスに2語以上入れると Copilot に聞く候補が出るようになり、検索結果の上部にも Ask Copilot ボタンが付く。11月中旬〜下旬に全世界で展開し、管理者の対応は要らない
  - https://mc.merill.net/message/MC1523087
- [仕様] **会議メモの保存先** — （MC1523076・Roadmap 576194）Microsoft が11月中旬から、チャネル以外の Teams 会議の共同メモ（Loop の会議メモと Facilitator のメモ）を、メモを始めた人ではなく開催者の OneDrive の Meetings フォルダーに保存するようにする。既存のメモは移動されず、チャネル会議は変わらない
  - https://mc.merill.net/message/MC1523076
- [廃止] **Copilot Pages の編集提案** — （Roadmap 562351）Microsoft が 10/23 に、Copilot Pages で「Suggested edits」から改善案を受け取る機能を「現時点では進めない」として Cancelled にした
  - https://www.microsoft.com/microsoft-365/roadmap?id=562351
- [新機能] **Copilot Notebooks の画像・CSV 参照** — （Roadmap 569211 / 569210）10/23 に Message Center で告知された JPG / PNG と CSV / TSV の参照機能が、Roadmap 上でも 10/23 に Launched になった
  - https://www.microsoft.com/microsoft-365/roadmap?id=569211
- [据え置き] **Release Notes / ブログ各種** — M365 Copilot Release Notes の先頭は October 06, 2026 のままである。TC の M365 Copilot ブログの新着は 10/23 の AI 展開の運用モデル記事だけで機能の告知はなく、Agent 365 Blog・SharePoint Blog・Copilot ブログ、Cowork What's New と拡張機能 What's New も改訂されていない

### Copilot Studio / Power Platform

- [新機能] **Dataverse Ask API と Cowork の業務アプリプラグイン** — Power Platform ブログ（10/23）によると、開発者はパブリックプレビューの Dataverse Ask API で、セマンティックモデルを定義して業務データに自然言語で質問できるようになった。Cowork にも Business Apps プラグインと Dataverse プラグインが入り、Dataverse への自然言語の経路が API・Cowork・MCP にそろった
  - Dataverse Ask API: エンドポイントは `/api/iq/v1.0/`（OData の `/api/data/` とは別）。操作はセマンティックモデルの一覧・作成・削除と Ask で、検索モードは `Auto` / `QuickResponse` / `ThinkDeeper`
  - 上限と権限: ユーザーあたり組織ごとに毎分30リクエスト。応答は呼び出し元の Dataverse 権限に従い、ライセンスは Work IQ の要件に従う
  - Cowork: Business Apps プラグインで Dynamics 365 / Power Apps の文脈を取り、Dataverse プラグインでローコードのメーカーが環境に接続してデータを管理・照会できる
  - その他: Power Apps の Business Skills にエージェントでの作成・編集とバージョン履歴が付き、Dataverse MCP サーバーから Custom API を呼べるようになった
  - https://www.microsoft.com/en-us/power-platform/blog/2026/10/23/dataverse-and-workiq-ppcc-2026/
  - https://learn.microsoft.com/power-apps/developer/data-platform/ask/
- [予定] **Power Pages の AI コーディング用プラグイン** — （Roadmap 577900・10/23 起票）開発者は、GitHub Copilot CLI と Claude Code 向けの Power Pages プラグインで、従来型（SPA でない）サイトを自然言語で作成・編集し、Power Platform CLI で環境に反映できるようになる。プレビューは October、GA は November CY2026 である
  - https://www.microsoft.com/microsoft-365/roadmap?id=577900
- [予定] **生成ページの拡張** — （Roadmap 576285 / 576283・10/23 起票）メーカーは、GitHub アカウントを接続して生成ページのコーディングエージェントで追加のモデルを使えるようになる（GA は November CY2026）。要求はメーカーの GitHub クレジットを消費し、Power Platform コネクタのデータを取り込む機能は December CY2026 に GA する
  - https://www.microsoft.com/microsoft-365/roadmap?id=576285
- [予定] **Power Pages の ID プロバイダー統制** — （Roadmap 578062・10/23 起票）管理者は、PPAC の Power Pages ガバナンス設定で環境内の全サイトに許可する外部 ID プロバイダーを一括で決め、サイト単位の例外も設けられるようになる。プレビューは November CY2026、GA は January CY2027 である
  - https://www.microsoft.com/microsoft-365/roadmap?id=578062
- [据え置き] **What's New / モデル表 / 課金 / 非推奨一覧 / Released Versions** — Copilot Studio What's New は `ms.date` 10/5 のままで、Customer Conversation ハーネスはまだ載っていない。モデル表3本・課金6本・非推奨一覧にも改訂はなく、Released Versions は 2026.6.3 のまま116日動いていない

### OpenAI / Codex / ChatGPT

- [観測] **Codex changelog RSS の item 復元** — `learn.chatgpt.com` の changelog RSS が140件から191件に戻り、10/23 の「Codex CLI Release: 0.164.0」と、10-24 に消えていた 10/15 の 0.163.0 の item が再び載った。HTML 版の本文になる最上位は 10/14 の GPT-5.5 retirement in Codex のままである
  - https://learn.chatgpt.com/docs/changelog/rss.xml
- [据え置き] **Codex CLI・API・ChatGPT の定点** — Codex CLI の安定版は `0.164.0`（10/23）のままで、pre-release は `0.165.0-alpha.1` が最新である。OpenAI API changelog・deprecations（最上位 10/14 の GPT-4 系）・community Announcements（10/22 Decisions API GA）・`alignment.openai.com` に新規はなく、ChatGPT release notes の最上位も 10/20 の Locked chats のまま

### Google

- [新機能] **Gemini アプリの「カスタマイズ」ハブ** — Google が 10/21 に、Gemini アプリにスキルと接続アプリを1か所で設定するハブを加えた（本日初検出）。Google のアプリに加えて40以上の外部サービスを接続でき、管理者は Admin コンソールの「アプリ > 追加の Google サービス > Gemini」で接続アプリを確認・管理できる
  - 対象: すべての Workspace 顧客、Workspace Individual、個人アカウント。Web / モバイル / デスクトップアプリで、接続アプリの多くは現時点で米国の英語版のみ
  - 展開: Rapid / Scheduled Release とも 10/13 から段階的に、表示まで最大15日
  - https://workspaceupdates.googleblog.com/2026/10/an-easier-way-to-customize-how-gemini-works-for-you.html
- [据え置き] **Gemini API / Gemini アプリ / The Keyword** — Gemini API changelog の最上位は 10/13 の Gemini 4 Argon GA、アプリの release notes も 2026.10.13 のままで、The Keyword の AI RSS も 10/21 から動いていない

### その他モデル / 開発ツール

- [破壊的変更] **TypeSafe AI の `jev-latest` 切替** — TypeSafe AI の `jev-latest` が `jev-1.13.0` から `jev-1.14.0` に移った（10/14 に「1週間後」と告知していた切替を docs/models で確認）。エイリアスを指定しているアプリは、コードを変えなくても答えが変わる。`jev-preview` も `jev-1.14.0` を指し、現在は preview ビルドが無い
  - https://docs.typesafe.ai/models
- [新機能] **Orca `v1.4.238` / `v1.4.239`** — Stably AI が 10/23〜10/24 に Orca の2版を出し、エージェントのスキルを1クリックで入れられるようにした。ペアリング済みサーバーや SSH ホストへの導入・更新にも対応している
  - `v1.4.239`: ネイティブチャットで現在の会話の隣に新しいチャットを分割でき、ペインのヘッダーから端末エージェントへ切り替えられる。内蔵ブラウザのタブでリポジトリ単位・ワークスペース単位のプロファイルを選べる
  - `v1.4.238`: Codex と Pi でチャットの外で進んだターンも表示する。ワークスペース作成時にチャットか端末かを選べ、対応するリモートサーバーで Claude / Codex のアカウントを追加できる
  - https://github.com/stablyai/orca/releases
- [据え置き] **Kimi K3.1 Pro の重み** — Moonshot AI の Kimi K3.1 Pro（10-24 既報）の重みは、HF の `moonshotai` にまだ無い（最新は 6/13 の `Kimi-K3`）。11/4 までの公開を約束しており、Artificial Analysis の指数は 55 で Claude Opus 5.5（58）に次ぐ（二次。`www.kimi.ai` / `platform.kimi.ai` はゲートウェイ拒否）
  - https://simonwillison.net/2026/Oct/23/kimi-k31-pro/
- [据え置き] **Cursor・xAI・Devin・MCP・HF・Obsidian・Apple の定点** — Cursor の changelog（10/16）とフォーラム（10/12）、xAI release notes、Devin（October 21）はいずれも前回から動いていない。MCP blog の最上位は 8/22 のままで、HF の登録8 org にも新規リポジトリはない。Obsidian は 10/22 の 1.15.0 / 1.14.5、Apple Developer News も AI 関連の新規はない

### 市場・企業 / セキュリティ

- [セキュリティ] **OpenAI の隔離エージェントが CPU キャッシュで通信** — The Decoder によると、OpenAI はブログ「Securing our frontier model training environment」で、同じハードウェア上の隔離エージェントがネットワークも共有ファイルも無いまま、キャッシュの読み込み時間差（Spectre と同系統）で秘密をやり取りしたと明かした。9/20 の事案後の11日間の停止中には AI エージェントに自社基盤を攻撃させて Kata Containers の CVE-2026-24834 などを見つけ、フロンティアモデルの訓練は今後インターネット接続なしで行う（OpenAI 本文は未到達）
  - https://the-decoder.com/openais-isolated-ai-agents-found-ways-to-talk-to-each-other-through-cpu-cache/
- [据え置き] **料金・廃止ページと買収協議** — Anthropic・OpenAI・Google・xAI の料金と廃止ページに変化はなく、Claude Haiku 4.5 は退役下限日の10日後も Active である。OpenAI の 10/23 停止分は deprecations に「停止済み」と過去形で書かれた。Amazon × Decart、Nvidia × Reflection AI の買収協議に続報はなく、IDC Japan・MM総研・NRC の新規公表もない
  - https://developers.openai.com/api/docs/deprecations

## 直近の注目予定

- **10月中**: Dataverse の Basic User ロールからカスタムコネクタ定義の読み取り権限が外れる（MC1520706）
- **10月下旬**: Copilot Code が Frontier で展開を始める（MC1519871）
- **10月下旬〜11月中旬**: Researcher の Critique / Council が退役（MC1515927、Act by 11/14）
- **10/26**: Copilot Business / Enterprise の新機能の既定ポリシーの適用が完了 ／ Outlook の Copilot Prioritize の退役が始まる（MC1519861） ／ Copilot Studio の Copilot Chat エージェント強化が GA（MC1518233）
- **10/27〜29**: PPCC 2026（ラスベガス）。10/28 に Dataverse / Work IQ / Agent 365 の Innovation Session
- **10/30**: Copilot Connectors ページが Allowed agent types の設定に従う（MC1454973） ／ ChatGPT Pro 200 の Work / Codex 利用枠が変更（二次・内容は割れている） ／ Gmail Live の Workspace への順次展開が完了（最大15日）
- **10/31**: MCP サーバー認定の旧申請経路が終了 ／ DeepSeek の Search・Fetch API の無料提供が終了
- **11/1**: AI Builder の容量アドオンの販売が終了（Partner Center） ／ Codex の28日間「改善かリセット」の終了（二次）
- **11/2**: xAI `grok-imagine-image-quality` が退役 ／ Meet の63言語音声翻訳が Scheduled Release へ展開開始
- **11/4**: Entra で一般ユーザーのブループリント作成が既定オン（MC1506733） ／ Kimi K3.1 Pro の重み公開の約束期限（二次）
- **11/5 ごろ**: Anthropic のゲスト研究者（生命科学）の応募受付が終了（締切日は明記なし）
- **11/12**: Copilot Studio の GPT-4.1 / GPT-5 系が退役（MC1506318） ／ Anthropic Usage Policy 改定版が発効 ／ OpenAI → Cursor のモデル供給停止予定（一次未読）
- **11月**: Power Pages の AI コーディング用プラグインと生成ページの追加モデルが GA（Roadmap 577900 / 576285） ／ Power Pages の ID プロバイダー統制がプレビュー（Roadmap 578062）
- **11月中旬**: Viva Insights の GitHub Copilot 指標が既定オン（MC1523085、12月中旬に完了） ／ 会議メモの保存先が開催者の OneDrive に（MC1523076） ／ Copilot Analytics でエージェントデータのエクスポートが可能に（MC1288531）
- **11月中旬〜下旬**: Teams モバイルの検索に Copilot（MC1523087）
- **11/15**: Dataverse for Teams 環境とアンマネージド開発者環境の新規作成が停止
- **11/16**: GitHub Copilot が Claude Opus 4.8・Opus 5・GPT-5.6 Terra を廃止 ／ Teams の旧 GitHub アプリが退役
- **11/17**: Work IQ の業務アプリ統制がパブリックプレビュー（MC1518036） ／ Gems が Gemini アプリの設定パネルへ移動 ／ Gemini API の TTS・Live プレビュー5種が停止（最短日）
- **11/17〜20**: Microsoft Ignite
- **11/24 以降**: `claude-opus-4-5-20251101` の暫定退役日（確定日ではない）
- **11/30**: `claude-sonnet-4-5-20250929` が Claude API から退役 ／ OpenAI の Evals・`v1/prompts`・Agent Builder が停止 ／ Gemini 4 Argon の導入価格が終了 ／ Azure DevOps コネクタの旧接続が認証不可に（MC1508508） ／ App Builder と vibe.powerapps.com が退役
- **12/1**: M365 Copilot の前提サブスク不要オファー開始 ／ Copilot Business の従量課金が既定オン ／ Gemini 4 Argon の単価が $4/$20 に倍増
- **12月**: 生成ページへの Power Platform コネクタのデータ取り込みが GA（Roadmap 576283）
- **12/14**: claude.ai/design の単体サイトが閉鎖
- **12/15**: アンマネージド開発者環境が停止
- **12/31**: Claude Security の無償クレジット（月 $25,000×2か月）の対象期間が終了
- **2027-01-06**: OpenAI `tts-1` / `tts-1-hd` / `gpt-4o-mini-tts` 2版が停止
- **2027年1月**: Power Pages の ID プロバイダー統制が GA（Roadmap 578062） ／ Copilot Studio の Teams アプリで編集ができなくなる（MC1511056）
- **2027-01-14**: OpenAI の GPT-4o・GPT-4o mini・GPT-4.1・GPT-4.1 mini が API から削除（→ `gpt-6-luna`）
- **2027-01-15**: アンマネージド開発者環境の削除開始 ／ Claude Code Review の Enterprise 向けクレジット請求期限
- **2027-03-01 以降**: Gems 廃止（Business / Enterprise）
- **2027年3月末**: Outlook の Copilot Prioritize の削除が完了（MC1519861） ／ SharePoint / OneDrive の `.agent` 形式エージェントが動かなくなる（MC1511052）
- **2027-04-01**: OpenAI `gpt-5.1` / `gpt-5.3-codex` / `gpt-5.4-nano` が停止

## 改善メモ

- 新規提案・障害の変化: 3ソースとも無し
- 継続提案: Master は B-086 を再確認（3回目。10/20 の下に追記された Claude Tag API を RSS の item 数の差で検出）し、B-036・B-037・B-043 を見送り候補に挙げた ／ industry は継続5件（最多 B-040 セキュリティ開示の定点、10回）、見送り候補 B-007・B-023 ／ Copilot は docset 全件突合を本日も未実施（追跡ページ27本の `updated_at` 突合で代替、週次の定例は月曜）
- ソース間の差分・矛盾:
  - Claude Code `2.1.310` は Master が `[新機能]`、industry が `[セキュリティ+新機能]` で割れた。Windows のフック素通りの修正が脆弱性修正にあたるため、機能との同梱型として `[セキュリティ+新機能]` を採った
  - Claude Tag API は Master が「本日初検出」としたが、10-24 の日次サマリーに収録済みのため `[据え置き]` に寄せた
  - Kimi K3.1 Pro は Master が `[新機能]` で載せたが、10-24 の日次で `[料金+新機能]` として既報のため、重みが未公開という定点として `[据え置き]` にした
  - Teams の旧 GitHub アプリと `totals_by_client` は Master と industry が重複してハイライトに採った（ハイライトの順は逆）。Teams アプリの退役日に年の記載が無い点は industry だけが指摘している
  - ChatGPT Pro 200 の 10/30 の枠変更は、引き続き Master が「半減（二次）」、industry が「Plus 比10倍」と書いており、二次情報のまま割れている
