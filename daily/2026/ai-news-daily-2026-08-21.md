# AI News Daily Summary — 2026-08-21

金曜は、エージェントに「誰の資格情報で動くか」を書き込む側の変更が3件そろった日である。Copilot Studio の What's New に2か月ぶりの新節が入り、その先頭で新規エージェントへの Entra Agent ID が必須になった——既存エージェントに自動移行経路はない。Roadmap 側では、メーカー資格情報での実行を塞ぐ機能の GA 期日が今月に置かれていた。Anthropic は 8/19 に Computer Use・Files API・Agent Skills を GA し Browser Use を新設していたが、本サマリーは昨日 Admin API の GA しか拾えていない。手元のツールでは Claude Code が v2.1.236 / v2.1.237 を出し、macOS sandbox の read-deny をリネームで迂回する抜け道が塞がった。Grok 4.6 は Amazon Bedrock で GA した。

## 今日のハイライト

### 1. Copilot Studio の新規エージェントに Entra Agent ID が必須になった — 後から付け足せない属性へ変わった

**要点**: Copilot Studio が全新規エージェントに Entra Agent ID を強制するようになり、環境レベルのオプトアウトが消えた。既存エージェントに自動移行経路はなく、統制の前提が「有効化する機能」から「作成時にしか付けられない属性」へ変わった。

**詳細**: Copilot Studio の What's New に2か月ぶりの新節（July 2026）が入り、その先頭に本件が載った。ページの `updated_at` は **2026-08-20T19:04Z**（JST 8/21 04:04）で、前日までは June 節が最新だった。仕様は次のとおり。

- 付与: Copilot Studio が新規エージェントごとに Agent ID を自動作成し、テナントに「Microsoft Copilot Studio agent identity blueprint」（Blueprint ID `25664c89-cea5-4ab6-b924-a54fd8a19ae0`）を追加する。全 Agent ID はこのブループリントの子になる
- 権限の可視化: メーカーが公開すると、エージェントが使う Power Platform コネクタごとの API アクセス許可が Agent ID に付く。Entra 管理者は Power Platform 管理センターを開かずに権限を確認でき、条件付きアクセス（ネットワーク場所・デバイス準拠・リスク条件）の対象にできる。スコープは実行時に ACP と DLP で再検証されるため、統制の迂回には使えない
- 確認方法: エージェントの Settings > Advanced > Metadata の Entra Agent ID に GUID が出る
- 削除: Copilot Studio でエージェントを削除すると Agent ID も削除される

⚠️ **既存エージェントの移行には自動経路がない。**Entra 側の移行ドキュメントは、in-place 変換も再発行も Agent ID を生成しないと明記し、新規エージェントを作って手で再構成し旧エージェントを廃止する recreate-and-deprecate 方式だけを示している。使用量別の指示は次のとおり。

- 低使用（30日以上サインインなし・下書き）: 移行せずそのまま廃止してよい
- 中使用: 作り直したうえで、新エージェントを本番で **10〜14日**監視してから旧サービスプリンシパルを廃止する
- 高使用（日次会話・本番業務・Teams 連携）: 公式の自動移行経路が出るまで作り直さない

作り直しで壊れるものは、Teams アプリマニフェストと Web チャット埋め込みが参照するアプリケーション ID、コネクタの再認可、旧サービスプリンシパルを参照する Power Automate フロー、そして移植されないトピック・ナレッジソース・設定である。旧サービスプリンシパルの発見にはタグ `AgentCreatedBy:CopilotStudio` / `AgenticApp` / `power-virtual-agents-{agent-id}` を使い、削除は Copilot Studio 側でエージェントを非公開化してから行う（順序を誤ると認証が壊れる）。

⚠️ Agent ID そのものは全 Entra 顧客が使えるが、条件付きアクセスなど Entra のセキュリティ機能をエージェントへ広げるには **Microsoft Agent 365** ライセンスが要る（M365 E7 に同梱、E5 / A5 / Business Premium にはアドオン）。

⚠️ 一次2本で開始時期が食い違っている。Copilot Studio 側は「Starting in July 2026」と書くが、Entra 側は自動作成の開始を **2026-03-18** と書いている。What's New 自身も November 2025 節と May 2026 節に同機能を Preview として載せており、開始時期を一次から一意に決められない。

- https://learn.microsoft.com/en-us/microsoft-copilot-studio/whats-new
- https://learn.microsoft.com/en-us/microsoft-copilot-studio/admin-use-entra-agent-identities
- https://learn.microsoft.com/en-us/entra/agent-id/migrate-copilot-studio-agents-to-agent-id

### 2. メーカー資格情報でエージェントを動かすことを塞ぐ機能の GA 期日が今月だった — 残り10日

**要点**: Copilot Studio の Roadmap に、メーカーの資格情報でエージェントを動かすことを塞ぐ機能が3件並んでいた。うち 566997 は GA 期日が今月で残り10日であり、「作った人の権限でそのまま動かす」設計は今月から順に通らなくなる。

**詳細**: 3件はいずれも `In development`・Worldwide (Standard Multi-Tenant)・Web で、本サマリーには一度も掲載がなかった。

- **566997** メーカー資格情報の使用ブロック: 管理者が、AI エージェントによるメーカー資格情報の使用を禁止できる。Preview は 2025年9月、GA 期日は **2026年8月**。狙いはメーカーの資格情報が届く機微システムへの不正アクセス防止と、GDPR / HIPAA 等での認可済み ID のみの利用担保である
- **566873** 資格情報オーバーシェアの検出: 公開時と共有時に、安全でない ID（メーカー資格情報等）に依存するエージェントとフローの共有そのものをブロックする。Preview は 2026年7月、GA 期日は 2026年9月
- **567894** 自律エージェントの Run-Only 共有: メーカーが、編集権限も所有権も渡さずに自律エージェントをエンドユーザーへ共有できる。Preview は 2026年8月、GA 期日は 2027年1月。従来は自律エージェントをメーカーしか使えなかった

⚠️ 3件とも Copilot Studio What's New にも Release Notes にも Release Wave にも載っておらず、Feature ID 単位で Roadmap を読む経路（昨日 02 が起票した B-040）でしか検出できなかった。昨日の Dataverse / Azure SQL / Agent Readiness の3件に続き、この経路が2日連続で未掲載項目を拾っている。

- https://www.microsoft.com/en-us/microsoft-365/roadmap （Feature ID 566997 / 566873 / 567894）
- https://learn.microsoft.com/en-us/microsoft-365/admin/manage/mrc-mcp

### 3. Claude API で Computer Use・Files API・Agent Skills が GA し Browser Use が新設された — beta ヘッダ前提の見送り理由が消えた

**要点**: Anthropic が 8/19 に Computer Use・Files API・Agent Skills を GA し、Browser Use を新設した。`anthropic-beta` ヘッダの送信が不要になり、「beta だから本番に載せない」という保留理由がなくなった。

**詳細**: 昨日の本サマリーは同じリリースノートから Enterprise Admin API の GA だけを収録しており、残り4本は本日はじめて確定した。内訳は次のとおり。

- Computer Use GA: 新 toolset 名 `computer_toolset_20260801` として一般提供された。バッチ操作（1ターンで複数アクション）・`zoom` の既定有効・`configs` によるメンバー別設定に対応する。旧 beta 版も継続して使え、移行手順は `computer_20251124` からの migration ガイドに集約されている。対応モデルは Claude Fable 5 / Mythos 5 / Opus 5 / Sonnet 5 / Opus 4.8
- Browser Use 新設: `browser_toolset_20260801` として同日に新規公開された。デスクトップ全体ではなくブラウザビューポート内で動くクライアント側 toolset で、ページのアクセシビリティツリー・要素・フォーム・タブを読み取り、要素参照・フォーム入力・タブ管理・ダウンロード報告・オプトインのファイルアップロードを screenshot-and-click 制御の上に載せる。対応モデルは Computer Use と同じ5系統
- Files API GA: `files-api-2025-04-14` ヘッダが不要になった。アップロード時に `expires_in_seconds` を指定でき file オブジェクトが `expires_at` を返すほか、`/v1/files` の一覧に `page` / `next_page` ページングと `ids[]` フィルタが加わった
- Agent Skills GA: `/v1/skills` と Messages API の `container` 経由の Skills 読み込みで `skills-2025-10-02` ヘッダが不要になった
- Enterprise Admin API GA（昨日収録済み）: members / invites / groups / custom roles で `ce-user-management-2026-07-13` ヘッダが不要になった

互換性はいずれも同じ設計で、beta ヘッダを送り続けるリクエストは従来形式のまま動くため既存コードの改修は要らない。ただし Computer Use だけは toolset 名が変わりリクエスト形状も変わるため、GA 前提へ寄せるかどうかは個別の判断になる。

- https://platform.claude.com/docs/en/release-notes/api
- https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool
- https://platform.claude.com/docs/en/agents-and-tools/tool-use/browser-use-tool
- https://platform.claude.com/docs/en/build-with-claude/files
- https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview

## カテゴリ別まとめ

### Anthropic / Claude

- Claude API の GA 4本と Browser Use の新設はハイライト3を参照。
- Claude Code が **v2.1.236**（8/19）と **v2.1.237**（8/20）を公開した。macOS sandbox で `**/.env` のようなワイルドカード read-deny ルールが許可読み取り領域の内側でも優先されるようになり、「deny 対象ファイルをリネームすれば読める」抜け道が塞がった
  - `ANTHROPIC_DEFAULT_MODEL`: 新規セッションの開始モデルを指定する。`/model` の選択が上書きし、再起動をまたいで保持される点が `ANTHROPIC_MODEL` と違う
  - `notify_when_idle`: 同一マシン上の別 Claude Code セッションへ「次に idle になったとき1回だけ通知」を依頼できる（opt-in・macOS / Linux）
  - auto mode: `Monitor` の allow ルールを auto mode 稼働中は退避し、Monitor コマンドを Bash と同じ経路で審査する。Bedrock / Vertex AI / Foundry とテレメトリ無効時も Claude API と同じ既定（severity スコア付き分類）を使う
  - `/usage` に Team / Enterprise メンバー向けの usage-credits 支出行が追加された
  - v2.1.237 は2項目のみで、LLM ゲートウェイ / カスタム base URL 使用時のプロンプトキャッシュ修正と、Concise 出力スタイルの追加である（`/config` の Output style で選択。前置きと実況を省き結果から書く）
  - https://code.claude.com/docs/en/changelog
- npm の `dist-tags` は `{stable: 2.1.228, latest: 2.1.237, next: 2.1.238}` だった（8/21 実測）。`next` の v2.1.238 は 8/20 18:01 UTC publish で changelog に未掲載のため、リリース済みとしては扱わない（changelog 未掲載版が配布経路に先行する形の5例目）。`stable` は 2.1.227 → 2.1.228 と1版進んだが、`latest` との差は8版から **9版**に広がった
- Anthropic が Claude Managed Agents の `web_search` / `web_fetch` にドメイン制限を追加した（8/19）。`agent_toolset_20260401` の `configs` 配列にある各ツールのエントリへ `allowed_domains` または `blocked_domains` を設定する形で、`web_fetch` は `max_content_tokens`、`web_search` は `user_location` も受け付ける。`configs` の各エントリは `name` で識別され `type` は任意なので、`name` / `enabled` / `permission_policy` だけを渡す既存リクエストはそのまま動く
  - ⚠️ 同一エージェント内で `web_search` と `web_fetch` に別々のリストを付けられるか、`permission_policy` とどちらが優先されるかは告知に明記がなく、実装時の確認事項として残る
  - https://platform.claude.com/docs/en/managed-agents/tools#restrict-web-search-and-web-fetch-domains
- Anthropic が Managed Agents の self-hosted サンドボックスに memory store を接続できるようにした（8/19）。Python / TypeScript / Go の SDK ワーカーが起動時に各ストアを `mount_path` へダウンロードし、エージェントの変更をストアへ書き戻す。従来はクラウド側サンドボックスに限られていた永続メモリが、データレジデンシー要件でセルフホストを選んだ組織にも開いた
  - https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes#use-memory-stores
- Anthropic が Claude Console の session viewer を再設計した（8/19）。タイムラインのミニマップ、モデルリクエスト単位でグルーピングしたトランスクリプト、Inspector パネル（セッション詳細・コスト・生イベント・ツール別統計・マウント済みリソース・スレッド別アクティビティ）が入った
  - https://platform.claude.com/docs/en/managed-agents/events-and-streaming#console-observability
- Bloomberg が、Anthropic は高性能モデルのデータ保持ポリシーを変更する計画だと報じた（8/20）。30日保持そのものは維持しつつ、保持先を Anthropic のインフラではなく顧客自身のクラウドにできる選択肢を、今年後半に投入する新しい安全システムで提供するという内容である
  - ⚠️ **公式発表ではない。**一次の `privacy.claude.com/en/articles/15425996` は WebFetch 200 だが **7/9 更新のまま**で、記載は現行ポリシー（全プラットフォームで30日保持。Bedrock は AWS 内、Google Cloud Agent Platform は GCP 内、Azure Foundry は Azure サブスクリプション単位で保持先が決まる）に留まる。Anthropic 直の API 利用分について自社クラウドを選べるという記述は無い
  - 6/9 発効の現行ポリシーは ZDR 契約が Fable 5 / Mythos 5 に及ばないと定めており、「Fable 5 / Mythos 5 では ZDR が効かない」を理由に導入を止めている場合、その保留の前提が年内に変わる可能性がある。ただし発効日も対象プランも未確定である
- Anthropic が Claude Academy を公開した（8/20）。社内オンボーディングで使っている教材を外部提供する形で、4D AI Fluency Framework を中心に据える。設計原則は「機能ではなく人間の主体性を広げる」「今日の AI は今後で最も出来が悪い AI という捉え方を教える」「いつ使うか・開示の倫理・スキル維持まで含める」「演習と振り返りを入れる」「Claude 自体を学習パートナーにする」の5点で、部門別のユースケースと Claude Academy Skill によるスキル推薦を伴う
- Anthropic が The Claude Code guide for startups を公開した（8/20）。10社超への取材に基づく5つの運用原則で、数値は ClickHouse が機能出荷 **+30%**（自作エージェント2体がリポジトリへの貢献者2位・3位）、Omni がエンジニア生産性 2〜3倍、Clay がバグトリアージの 100% 自動化、Artemis Security が週 6,000+ PR である
  - 原則は5つで、①全員が出荷する（MCP / CLI の接続・四半期ショーケース・共有スキルライブラリ）、②退屈な作業を自動化する、③信頼するが検証する（golden eval セット・決定的チェック・停止条件付きループ）、④作り直す前提で作る、⑤プロトタイプ → 社内ドッグフード → 製品化、である。④の例として Commure は「全体公開済みの feature flag を削除する PR を開く」スキルで移行を数時間で完了させた
- Anthropic が monday.com の事例を公開した（8/20）。プラットフォームを人とエージェントが協働する agent-first 構成へ転換した経緯を扱う
- `support.claude.com` の Release Notes は 8/6 の skill / plugin セキュリティスキャン beta が最上位のままで、**15日連続**で動きがない
- `www.anthropic.com` はオリジン403が継続している。01 は規定の検索5本＋日付入り1本を全て実行したうえで、8/20 付けの新規発表がデータ保持の報道のみであることを確認した。安全性・評価インシデント系（7/30 cybersecurity evals・8/14 Risk Report）と研究助成に新規はない
- 既報: Claude Code の週次上限50%増は **8/31** まで延長済み（対象は Pro / Max / Team とシート課金のレガシー Enterprise）、下院民主党22名の監督書簡（回答期限 **8/24**）、Claude Sonnet 5 の 9/1 値上げ撤回はリリースノートで維持されている

### Copilot Studio / Power Platform

- Entra Agent ID の必須化はハイライト1を、資格情報ガバナンス3件はハイライト2を参照。
- Copilot Studio のエージェントトレースを Power Platform 管理センターから Azure Application Insights へ**環境単位**でエクスポートできるようになった〔Preview〕。監視の設定箇所がエージェント個別からマネージド環境1点へ移り、メーカーの設定漏れが監視の穴にならなくなる。対象は標準ハーネスと GitHub Copilot ハーネスの両方で、マネージド環境限定である
  - 出力形式: OpenTelemetry の GenAI セマンティック規約に沿ったスパンで、`dependencies` テーブルに `InvokeAgent` / `ExecuteTool` / `OutputMessages` の3種として書かれる。1ターンが1トレース（共有 `operation_Id`）で、`InvokeAgent` がルート、残り2種がその子になる
  - 紐づけ: 会話をまたぐ紐づけは `gen_ai.conversation.id` で行い、サブエージェントは親の会話 ID に `_` 付きのサフィックスが付く。`customDimensions` にモデル名（`gen_ai.request.model`）・ツール名と引数と戻り値・テナント ID・チャネル名・ユーザー ID が入る
  - 閲覧: Kusto を書かずに見る経路として Application Insights の Agents (preview) ブレード（Agent Runs / Tools / Models）が使える
  - ⚠️ 制約が多い。宣言型エージェントのログは出ず、`TopicStart` / `TopicAction` / `TopicEnd` のトピック系イベントは環境レベルテレメトリでは取れない。クラシックエージェントのトレースには `duration` が入らず、エージェントとツールの実行エラーがトレースのステータスに正しく反映されない。対象リソースでローカル認証が有効である必要があり、エクスポートはトランザクショナルではないため障害時に少量の欠損が起こりうる。新規構成の反映には最大24時間かかる
  - https://learn.microsoft.com/en-us/microsoft-copilot-studio/advanced-environment-level-agent-telemetry
- Copilot Studio の What's New に July 2026 節が加わり、6項目が公開された（`ms.date` 2026-08-18 / `updated_at` 2026-08-20T19:04Z）。ハイライト1と上記テレメトリを除く4件は次のとおり
  - MCP サーバーをツールとして追加〔Preview〕: GitHub Copilot ハーネス製エージェントの Build タブから MCP サーバーを登録すると、そのサーバーが公開する全ツールが会話中に呼べるようになる。⚠️ 1会話で同時実行できる MCP サーバー数に上限があり、超過分はそのターンでスキップされる（数値は非公開）。各サーバーはエージェントのツール総数にも計上される
  - ワークフローをツールとして追加〔Preview〕: マルチステップの自動処理を同じくツールとして持てる
  - リアルタイムエージェントの digital messaging 対応: 同一エージェントを音声とデジタルメッセージングの両チャネルへ展開できる（デジタルメッセージングは Preview）。モデルに GPT-5-Chat (Preview) を選べ、Application Insights で監視できる
  - 添付ファイルと生成ファイル〔Preview〕: ユーザーが会話にファイルを添付でき、エージェントが作成したファイルを閲覧できる（GitHub Copilot ハーネス製のみ）
- 添付ファイルの制限値が公開された。添付は1ファイル **16 MiB** まで、会話中の保持は最終アクティビティから **28日**で、期限後は削除されエージェントから参照できなくなる。対応形式は画像（.png / .jpg / .gif / .webp）・PDF・テキスト（.txt / .csv / .html / .md）と公開到達可能な URL で、URL は30秒でタイムアウトするとそのターンではスキップされる。処理できない添付があっても残りは処理され、メッセージ自体は送信される。⚠️ 添付はナレッジソースの代替ではなくターン単位のユーザー入力であり、利用・構築・テスト・評価のいずれも Copilot Credits を消費する
- MCP サーバーの Microsoft 認証プロセスが変わった〔Preview〕。発行元は Partner Center のオファー種別 Apps and Agents for M365 and Copilot から申請する。⚠️ **旧経路は 2026年7月末で終了済み**で、既に期限を過ぎている（認証済みサーバーは Microsoft 側が新経路へ移すため再申請は不要）。パッケージ要件にマニフェスト・ツールファイル・`intro.md`・Azure Key Vault 認証構成が加わり、Key Vault にはサービスプリンシパル `8e91e74f-afe9-41cd-8c3f-17a9562a74ea` へ Key Vault Secrets User 相当の読み取り権限が要る。認証済みサーバーは Copilot Studio に加えて Azure Foundry でも提供される。⚠️ 申請できるのは検証済み発行元かつエンドポイントの所有者に限られ、サービスを所有しない独立発行元は直接申請できない
- Copilot Studio What's New は、8/3 に GA した GitHub Copilot ハーネスをいまも June 節で `(Production-ready preview)` と書いている（GA から **18日連続**の未反映）。⚠️ 本日は性質が変わった——これまでは「ページが更新されていない」ことで説明できたが、July 節の追加でページは 8/20 に編集されており、編集の機会がありながら GA の表記だけが直っていない
- Copilot Studio の Released Versions に新ビルドは出ておらず、Build は 2026.6.3（6/30 初出）のままで空白が **7週間と2日**に達した。リージョン分布（11 / 5 / 3 の3段）も UX 版 26.06.21-24 も据え置きで、次の定例日は 8/25（火）である
- Release Wave の `power-automate` / `power-apps` / `power-platform-governance-administration` の3ページは 8/20 と完全に同一で、緑チェックの追加・期日変更・行の増減はいずれも発生していない（`updated_at` はそれぞれ 2026-08-12T23:07Z / 2026-08-12T23:07Z / 2026-07-23T15:20Z）。期日超過は延べ6行、8月期日は10件、9月期日は6件のままである
- PPAC の Usage ページは Public preview が 2026-02-13〔緑チェック済み〕で GA 期日が今月のまま動いておらず、残り10日で緑チェックは付いていない。運用状態の異常検知とソースコード統合の GitHub 対応も Preview 期日が Aug 2026 のまま未チェックである
- 非推奨一覧に新規項目は追加されておらず、先頭は Power Automate モバイルアプリの廃止（**2026-08-31** 発効・残り10日）のままである。廃止後はアプリがストアから削除されプッシュ通知とホーム画面ウィジェットが止まるが、既存のクラウドフローは通常どおり動く
- Power Platform Blog / Power Automate Blog / Power Apps Blog は3ページとも先頭が 8/13 の PPCC 2026 登録記事のままで、本日の新規はない。⚠️ 8/6 公開の月次合併号が一覧に現れない不完全レンダリングも継続している

### Microsoft 365 Copilot / パートナー

- M365 Copilot Release Notes の最新セクションは「August 11, 2026」のままで、本日の新バッチはない。対象期間 7/28〜8/11・全12項目・節構成7本（extensibility 2 / SharePoint 1 / Outlook 2 / Microsoft 365 Copilot 1 / PowerPoint 4 / Viva Insights 1 / Word 1）で 8/20 と一致する。見出しの並びは August 11 → July 29 → July 15 → July 01 → June 16 → June 2 で、隔週傾向どおりなら次は **8/25** 前後である
- Roadmap **569607**（8/19 起票・GA 期日 2026年9月）で Copilot Studio のエージェント評価体験が拡張される。評価説明の詳細化、エージェントの推論トレース、引用ナレッジソースの表示、実行間の比較、大規模データセット対応、テスト生成のカスタマイズ、ナレッジソースからのデータセット生成が入り、実行前に構成の問題を潰すための検証とガイダンスも追加される
- Roadmap の広報枠（Latest announcements）の先頭は 7/24 の「Available today: Anthropic's Claude Opus 5 in Microsoft 365 Copilot」のままで新規がない。Coming soon の Researcher の Critique / Council、Frontier 枠4件（Cowork のモデル選択・browser use、Microsoft Scout アプリ、Copilot Notebooks、Word の Legal Agent）にも変化はない
- Tech Community / M365 Blog / Copilot Blog / Developer Blog はいずれも新規記事がない。TC M365 Copilot Blog は 8/13、M365 Blog は 7/30、Copilot Blog は 7/21、Developer Blog は 8/13 が最新のままである。⚠️ TC の board RSS の並びが投稿日の降順になっておらず、順序の乱れが**8日連続**で再現した
- Partner Center の8月アナウンスは 8/14 付の14件目までで、**6日連続**の追記なしとなった。既報14件（IT Nation Connect ANZ〔8/27 セッション〕/ Copilot アプリの URL 移行〔8/18 発効済み・デスクトップの広範展開は9月中旬〕/ MAICPP 月次〔契約更新条項が 9/1 自動発効・Frontier Partner バッジは 2027年6月末で廃止〕/ CSP Copilot Partner Council コンテスト〔応募期限 8/31〕/ マルチテナントのエージェント管理〔Public Preview・Agent 365 ライセンスが必要〕/ CSP ソフトウェアの5%資本コスト上乗せ〔10/1 発効〕/ M365 E7 プロモーションの 10/1 新規取引停止〔対象購入は 9/30 まで〕ほか）に変化はない
- Microsoft Purview の8月節は 8/15 検知分から変化がない（`updated_at` 2026-08-14T07:32Z）。掲載は Sensitivity labels の2件（自動ラベル付けポリシーのシミュレーションモード、ポリシー詳細パネルの Insights タブ）のみで、⚠️ Copilot 固有の項目は含まれていない
- Agent 365 Blog と SharePoint Blog はどちらも新規記事がない。Agent 365 は 8/6 の「What's new in Agent 365 – July 2026」、SharePoint は 8/6 の「What's New in Copilot in SharePoint: August 2026」が最新のままである

### GitHub Copilot / 開発ツール

- Copilot CLI の pre-release **v1.0.81-6** が出た（8/20 17:59）。管理設定まわりが実務に効く内容である
  - `defaultMode` / `defaultPermissionMode`: 新規の対話セッションが開始するモードと承認挙動を設定で指定できる
  - `--with-token`: `copilot login` が stdin から認証トークンを読む。CI での非対話ログインが素直に書ける
  - 管理設定の優先: `enabledPlugins` と `extraKnownMarketplaces` がエントリ単位で管理設定側を採るようになり、組織がピン留めしたプラグイン / マーケットプレイスをローカル設定で上書きできなくなった
  - ACP クライアントがサブエージェント ID・生イベントの購読・タイトル / モード / コマンド / プランの逐次更新を受け取る。Canvas ウィンドウはターミナルのフォーカスを奪わず背後で開く
- v1.0.81-5（8/19 23:16）は1件のみで、エージェント処理中に送ったプロンプトが応答後にトランスクリプトへ二重の pending として残る不具合を修正した
- ⚠️ 前日「内容未確定」とした3版のうち確定できたのは **0件**のままである。v1.0.81-2 / -3 / -4 は個別タグページを再度当たっても本文が空で、`raw.githubusercontent.com` の `changelog.md` にも v1.0.81 系のエントリが無い。一方で -5 / -6 は個別タグページから本文を取得できたので、空本文は恒常ではなく版ごとに揺れる
- Copilot CLI の安定版は **v1.0.80**（8/14）据え置きで、7日間更新がない
- GitHub Code Quality に GitHub Actions の専用パスが追加された（8/20 公開）。分析実行を Actions ワークフローとして別パスで宣言できるようになり、既存の CI パイプラインと衝突せず段階的にオンにできる。8/19 収録の組織横断トレンドタブと同じ Code Quality ダッシュボードの延長で、分析実行の管理面と可視化面が同じ週にそろって強化された。⚠️ 対象プランと有効化手順は告知の見出しレベルにとどまる
  - https://github.blog/changelog/
- `github.blog/changelog/label/copilot/` は 8/18 の JetBrains 管理設定が最上位のままで、8/19〜8/20 の追加はない
- Cursor の changelog は 8/19 の Cloud Agents / Harness 更新が最上位のままで、8/20 の追加がない（RSS 実測 200 / `application/rss+xml` / item 50件）。フォーラム Announcements も 8/17 の Origin Code Hosting が最上位のままである
- Devin は 8/15 の release notes が最新のままで、8/16〜8/20 の新規項目は二次でも確認できない。既報は Devin Coach（8/14）、Devin Review の差分無変更 PR のスキップ、Slack スレッド購読による再メンション不要化、CLI の org / エージェント / セッション処理改善である。⚠️ `docs.devin.ai` はゲートウェイ拒否が継続し一次未確認である
- 期限: 既定モデル有効化ポリシー発効（**8/26**）、GitHub Spark 退役（**8/31**）、モデル廃止（**9/1**）、MAI-Code-1-Flash 廃止（**9/10**）

### OpenAI

- Codex CLI の pre-release が 8/19〜8/20 に4版刻まれた。0.149.0-alpha.2（8/19 22:36 UTC）／ -alpha.3（8/20 02:27）／ -alpha.4（8/20 09:39）／ -alpha.7（8/20 18:29）で、⚠️ **4版とも本文は `Release <version>` の1行のみ**のため変更内容が分からない。安定版は 0.148.0（8/18）据え置きである
- `developers.openai.com/api/docs/changelog` は 8/13 の Ultrafast モードが最上位のままで、8/14〜8/20 の追加がない。⚠️ 課金レートは依然として未確定である
- `community.openai.com` の Announcements RSS は 8/18 の DevDay Exchange 告知が最上位のままで、8/19〜8/20 の追加投稿はない（応募締切 **9/17**・東京は 10/20）
- `learn.chatgpt.com` は WebSearch 経由で確認したが、8/19〜8/20 付けの新規項目は検出できなかった。返ったのは既報分（GPT-5.4 / 5.4 mini の 8/31 Codex 除外＝代替は `gpt-5.6-terra` / `gpt-5.6-luna`・Computer History・Linux デスクトップアプリ preview・Record & Replay の EU / 英国 / スイス拡大・ChatGPT Voice のファイル / Projects 対応）である
- ⚠️ 8/10 公開の ChatGPT レストラン予約対応を **11日間**検出できていなかった。OpenTable（全世界）・Resy（米国）・Yelp（米国 / カナダ・ウェイトリスト対応）の3ネットワークで、人数・日時・連絡先とベジタリアンメニュー等の要望を会話内で渡して予約を確定できる。変更とキャンセルは各プロバイダ側で行い、提供は web / モバイル / デスクトップである。登録ソースの `help.openai.com` と `openai.com` がどちらも到達不可のため、ChatGPT エンドユーザー機能の検出経路が実質存在しない状態が続いている
- 到達性は前日と同じである。`community.openai.com`（RSS）と `developers.openai.com/api/docs/changelog` は 200、`openai.com` / `help.openai.com` / `platform.openai.com` はオリジン403継続、`learn.chatgpt.com` はゲートウェイ拒否継続（WebSearch では本文相当が取れる）である

### Google / DeepMind

- Gemini API の changelog は 8/13 の Gemini 3.7 Flash GA が最上位のままで、8/14〜8/20 の追加がない
- Google が TIPS v1 の視覚表現モデル6本を Hugging Face に公開した（8/19）。`google/tipsv1-{s14,b14,l14,so400m14,g14,g14-lowres}` の6リポジトリで、DL は最大 43・likes は最大 2（8/21 実測）と反応はまだ小さい。⚠️ 画像**生成**ではなく表現学習側のモデルであり、直接使える製品ではないため参考扱いに留める
- Gemini API の単価は 8/20 収録分から変更がない。3.7 Flash と 3.6 Flash の両方に入力 **$0.75** / 出力 **$3.75** の導入価格が掲載された状態が続き、有効期限は 2026年12月31日で 2027年1月1日以降は $1.50 / $7.50 になる。3.5 Flash（$1.50 / $9.00）・3.5 Flash-Lite（$0.30 / $2.50）・2.5 Flash（$0.30 / $2.50）・2.5 Pro（$1.25 / $10.00・200k超は $2.50 / $15.00）・3.1 Pro Preview（$2.00 / $12.00・200k超は $4.00 / $18.00）も据え置きである。`ai.google.dev` の WebFetch は **19日連続**で成功した
  - https://ai.google.dev/gemini-api/docs/pricing
- 退役側は Imagen 4 の各生成エンドポイント（8/17 停止）・Gemini 2.0 Flash / 2.0 Flash-Lite（6/1）から追加がない。`gemini-robotics-er-1.6-preview` の停止日は **8/31** である
- Gemini 3.5 Pro は未 GA が継続している（I/O 発表後 6月 → 7月 → 7/17 と3回スリップ）
- ⚠️ 登録済み Google 系5ソースはゲートウェイ拒否が継続しており、`ai.google.dev` が唯一到達できる Google 一次である状態が続く。`ai.google.dev/gemini-api/docs/changelog` は `daily-sources.md` 未登録のままである（回数8）

### モデル・料金 / オープンウェイト

- xAI の **Grok 4.6** が Amazon Bedrock で一般提供された（8/19）。Bedrock が提供される全 AWS リージョンでクロスリージョン推論に対応し、xAI と個別契約せずに既存の IAM / CloudTrail / コスト管理の枠内で Grok を評価できるようになった。推論プロファイルは、データ所在地要件向けの US Geo とスループット優先の Global の2つである
  - 呼び出しは `bedrock-runtime` エンドポイント経由で、Bedrock 既存の監視・ログ・コスト管理ツールがそのまま効く。モデル側の仕様は 8/12 の発表どおり context 500K・reasoning effort 4段（low / medium / high / xhigh）で、長時間稼働エージェントと視覚的 / インタラクティブな作業を主眼に置く。価格は入力 **$2** / 出力 **$6**（per MTok）である
  - ⚠️ 一次のうち `aws.amazon.com` の what's-new は日付（Aug 19, 2026）とリージョン・プロファイルを確定できたが、同ページに価格と context 長の記載がない。`x.ai/news/grok-4-6-amazon-bedrock` はゲートウェイ拒否継続のため、価格と context 長は 8/12 の既報値と二次一致で採った。ベンダー一次3ホスト（`x.ai` / `docs.x.ai` / `grok.com`）が塞がったままクラウド側の一次で代替できた例にあたる
  - https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-bedrock-grok-4-6/
  - https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-xai-grok-4-6.html
- 8/19〜8/20 に新規公開されたオープンウェイト LLM はない。`Qwen` / `moonshotai` / `deepseek-ai` / `meta-models` / `mistralai` / `zai-org` / `openai` / `google` の計8 org で作成日降順一覧を実行し、8/13 の `Qwen/Qwen3.8-27B-FP8` と `deepseek-ai/DeepSeek-V4-Pro-0813` より新しい LLM が1件も無いことを確認した（`google` org のみ 8/19 に TIPS v1 6本が入った）
  - 実測（8/21）: `Qwen/Qwen3.8-27B` は DL **1,373,584** / likes 11,700（前日 1,006,235 / 11,425）、FP8 版は DL 1,517,643 / likes 628 である
  - `deepseek-ai/DeepSeek-V4-Pro-0813` は DL 43,287 / likes 674（前日 37,583 / 625）で、`deepseek-ai/DeepSeek-V4-Flash-0731` は DL 2,547,549 / likes 3,574 と **V4-Pro の約59倍**である。ダウンロードは Flash 側に大きく偏っている
- DeepSeek の課金区分別の新単価は本日も一次で確定できていない。`api-docs.deepseek.com` のゲートウェイ拒否が継続しており、8/16 16:00 UTC 発効の値上げについて課金区分ごとの確定単価を一次料金表で確認できない状態が**5日**続く。二次では V4-Pro の出力が peak $3.96 / off-peak $1.98（旧一律 $0.87 比で peak +355%）、off-peak 帯は「01:00-04:00 / 06:00-10:00 UTC 以外」と報じられているが、提案資料に DeepSeek の現行単価を確定値として書かない
- GitHub Copilot のモデル追加は 8/14 の Grok 4.6 から変化がない
- 既報: DeepSeek Harness v0.1.0-rc.7（8/17・MIT・developer preview）、DeepSeek の新 API 料金は JST 8/17 01:00 発効済み、Meta の Muse Code / Muse Spark 1.2（8/5）、Muse-Glimmer-30B（8/9）

### MCP

- MCP ブログに新着はなく、RSS 最新は 7/28 の `The 2026-07-28 Specification` のままで **24日連続**で動きがない
- 実装側の新規は4件である。Claude Managed Agents の `web_search` / `web_fetch` にドメイン制限が入り、Copilot CLI の管理設定がエントリ単位で組織側を採るようになり、Copilot Studio が MCP サーバーをツールとして登録できるようになり、MCP サーバーの Microsoft 認証申請が Partner Center 経由へ移った。前2件はエージェントの外部到達をポリシーで縛る方向、後2件は MCP サーバーを製品の統制下に置く方向である
- `blog.modelcontextprotocol.io`（RSS `index.xml`）は 200 で、`modelcontextprotocol.io` 本体はゲートウェイ拒否が継続している

### 企業・市場・国内

- OpenAI の公開 S-1 は本日時点でも EDGAR に出ていない。6/8 に SEC へ機密扱いの草案を提出済みで、公開版の掲載は8月下旬〜9月上旬が見込まれるとされる。SEC の機密審査は通常60〜90日で複数回のコメントラウンドを伴い、公開後15日以上経ってからロードショーが始まるという規則から逆算した推定であり、確定した日程ではない。⚠️ 流通している評価額（直近ラウンドの $852B）と財務値（月間売上 約 $2B・売上1ドルあたり約1.22ドルの損失）はいずれも公開文書に基づかないため、提案資料に確定値として引かない
- 国内の市場データ定点は新規リリースがない。引用可能な基準値は IDC の2026年3月予測（国内 AI 市場支出額 2025年 2兆3,725億円 → 2029年 6兆8,897億円・CAGR **36.0%**）、総務省 令和8年版情報通信白書（企業の生成AI業務利用 86.4%）、MM総研の個人利用率 21.8%（2025年8月時点・利用者数1,597万人）のままである。Similarweb も 8/3 収録の生成AIトラフィックシェアから確定値の更新がない
- Apple の `developer.apple.com` は 200 で、8/18 の EU 向けビジネス条件変更2本が最上位のままである。8/19〜8/20 の追加はない（Core Technology Fee を廃止しデジタル取引の5%を課す Core Technology Commission へ置換／ Developer Program License Agreement に Attachment 14 追加・発効 **2026-10-01**）。⚠️ AI 関連の内容ではなく、AI 関連の最新は依然 8/5 の「Get ready for new creative assets on the App Store」である。iOS 27 / iPadOS 27 は developer beta 4（7/20・ビルド 23G71）が最新で、GA は9月（予想 9/14 前後）である
- Qiita / Zenn は本日も取得できず、WebSearch で代替した。索引に出るのは Copilot Studio のライセンス・課金解説が中心で、厳選掲載に値する新規記事は検出していない。⚠️ Copilot Credit の USD 単価を具体的に書く記事があるが、いずれも一次（Learn）に存在しない数値のため採用しない
- X トレンドは日本語圏・英語圏とも突出した新規バズがない。英語圏の二次記事は 8/3 のハーネス GA と Run-Only 共有の Preview を扱うものが中心である

## 直近の注目予定

- **8/22**: M365 Copilot アプリのチャット中心 UI が Deferred リングへ展開開始（MC1325422）
- **8/23**: PnP・Power CAT・拡張機能 What's New・モデル可用性一覧の週次確認
- **8/23–24**: Manus が Meta 買収後（2025-12-29 以降）のユーザーデータを削除（8/23 08:00 SGT 開始・復元は 8/25 から）
- **8/24**: **ChatGPT Ads が欧州31市場で開始** ／ **Anthropic / OpenAI が下院民主党の監督書簡へ回答する期限** ／ MS-4005・Power Platform Weekly の週次確認 ／ 01 の週次復旧チェック
- **8/25**: M365 Copilot Release Notes の次バッチ見込み（隔週サイクルどおりなら） ／ Copilot Studio Released Versions の定例更新日（火） ／ Copilot Studio 課金ドキュメントの週次確認
- **8/26**: OpenAI Assistants API 廃止 / o3 退役 / GPT-4.5 完全廃止 ／ Copilot 既定モデル有効化ポリシー発効
- **8/27**: IT Nation Connect ANZ の Microsoft セッション
- **8/30**: 公式 DALL·E GPT の退役
- **8/31**: **Claude Code の週次上限50%増が終了** ／ GitHub Spark の既存ユーザーアクセス終了 ／ `gemini-robotics-er-1.6-preview` 停止 ／ GPT-5.4・5.4 mini が Codex から除外 ／ Claude for Government の $1/機関プログラム終了 ／ Power Automate モバイルアプリ廃止 ／ CSP Copilot Partner Council コンテストの応募期限
- **8月下旬**: Planner Agent チャットの基本プラン展開開始（MC1443514） ／ スペシャライゼーション監査の Partner Center からの取り下げ対応
- **8月中**: **Roadmap 566997（メーカー資格情報のブロック）の GA 期日** ／ PPAC Usage ページの GA 期日 ／ Release Wave の8月期日10件と持ち越し6行 ／ Copilot Studio の Dataverse・Azure SQL が Preview ／ 政府クラウドでの MCP エージェント UI ウィジェット GA
- **9/1**: GitHub Copilot の全体験でモデル廃止 ／ OpenAI Daybreak で全アカウントにハードウェアセキュリティキー必須化 ／ MAICPP 契約の更新条項が自動発効
- **9/2〜9/3**: Windows 365 Frontline 名称での購入最終日（9/2）と Windows 365 Flex への改称（9/3）
- **9/10**: MAI-Code-1-Flash が全 Copilot 体験から廃止
- **9/17**: **OpenAI DevDay Exchange の応募締切**
- **9 月**: Roadmap 566873（資格情報オーバーシェアの検出）GA ／ Roadmap 569607（エージェント評価体験の拡張）GA ／ Copilot Tuning の新体験が Public Preview ／ Copilot Studio の Dataverse・Azure SQL ナレッジソース GA ／ Agent Readiness GA ／ Federated Copilot Connectors GA ／ 組織プロンプトの公開権限委任 GA ／ Plus メニューからのエージェント追加 GA ／ ガバナンス Release Wave の9月期日2件 ／ iOS 27 / macOS 27 GA ／ 9月中旬に Copilot デスクトップアプリの広範な展開開始 ／ 9月末に 2026 Wave 1 の対象期間終了 ／ 9/30 に M365 E7 プロモーションの対象購入最終日 ／ OpenAI の IPO 観測
- **10/1**: Apple の EU 向け新ビジネス条件が発効（Core Technology Commission へ移行） ／ M365 E7 プロモーションの新規取引停止 ／ CSP ソフトウェアの5%上乗せ発効
- **10/16–11/11**: OpenAI DevDay Exchange 8都市（**東京は 10/20**）
- **10 月**: Anthropic の IPO 予定（$2T 超の評価額を目標と報道） ／ Copilot Notebooks の CSV / TSV・JPG / PNG 参照 GA ／ 10/20〜22 に SMB Copilot Partner Council（NYC） ／ 10/25〜30 に PPCC 2026 本編とワークショップ
- **11/1**: パートナー特典の有効期限がオファー購入日基準へ移行
- **12/2**: EU AI Act の生成コンテンツ標識義務、8/2 以前に市場投入済みシステムへの猶予終了
- **12 月**: Copilot Tuning の新体験が GA ／ 12/31 に Gemini 3.6 Flash / 3.7 Flash の導入価格終了（$0.75 / $3.75 → $1.50 / $7.50）と M365 E3 プロモーション・Copilot in 30・Purview Suite 50%オフの提供終了
- **年内**: Anthropic の新しいデータ保持方式（顧客自身のクラウドでの30日保持）投入予定と Bloomberg が報道
- **2027年1月**: Roadmap 567894（自律エージェントの Run-Only 共有）GA
- **2027年6月末**: Frontier Partner バッジの廃止
- **2027年7月**: 退役資格の有効期限（2026-07-30 発効分）

## 改善メモ

- 本サマリー自身の取りこぼしが1件確定した。8/20 分は `platform.claude.com/docs/en/release-notes/api` を出典に引きながら Enterprise Admin API の GA だけを収録し、同じ 8/19 の日付ブロックに並ぶ Computer Use・Browser Use・Files API・Agent Skills を落としていた。01 も同じ形で3本しか拾えておらず（Computer Use と Browser Use が漏れた）、**同一日付ブロック内の項目取りこぼし**が2リポで同時に起きている。03 はこれを「今日のリリースノートの当日エントリを1本ずつ通読する」手順の欠落として B-008 / B-027 の根拠に追加した
- ソース間で GA の本数が割れた。01 は「8/19 だけで GA が3本」（Files API / Agent Skills / Admin API）と書き、03 は「GA 4本立て＋新規1本」（Computer Use を含み Browser Use を新設として数える）と書いている。本サマリーは網羅性の高い 03 の数え方を採り、ハイライト3で5本すべてを列挙した
- Roadmap の Feature ID 単位の読み取り（B-040）が2日連続で未掲載項目を拾った。本日は資格情報ガバナンス3件（566997 / 566873 / 567894）で、うち 566997 は GA 期日が今月である。What's New・Release Notes・Release Wave のいずれにも載っていないため、この経路がなければ期日当月まで検出できなかった
- 一次2本の食い違いが1件ある。Entra Agent ID の自動作成開始日が Copilot Studio 側「July 2026」と Entra 側「2026-03-18」で割れており、02 は突合手順を `fetch-flow.md` に追記する提案として **B-041** を起票した
- 検知遅れが1件ある。8/10 公開の ChatGPT レストラン予約対応を 11日遅れで初捕捉した。`help.openai.com` と `openai.com` がどちらも到達不可のため、ChatGPT エンドユーザー機能には一次の検出経路が存在しない状態が続いている
- 本文が取れないリリースが2系統ある。Copilot CLI の v1.0.81-2 / -3 / -4 は個別タグページの本文が空のままで、-5 / -6 は取得できた（版ごとに揺れる）。Codex CLI の 0.149.0-alpha.2 / -3 / -4 / -7 は4版とも本文が `Release <version>` の1行のみである
- 障害の変化はない。01 の WebFetch は本日全て成功し新規の到達不可ホストはなく、02 の `mc.merill.net`（14日連続）・Qiita / Zenn、03 の `api-docs.deepseek.com` / `the-decoder.com` / `venturebeat.com` / `gigazine.net` / 全RSSフィード一括403 はいずれも既知分の継続である
- 各ソースの改善提案は 01 が新規1件（B-040: `privacy.claude.com` をデータ保持・ZDR の一次に追加）で継続20件、02 が新規1件（B-041）で継続20件、03 が新規なしで継続10件である
