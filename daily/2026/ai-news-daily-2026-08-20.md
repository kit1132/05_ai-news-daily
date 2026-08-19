# AI News Daily Summary — 2026-08-20

木曜は、昨日「今日で終わる」と書いた前提が2つとも動いた日である。Claude Code の週次上限50%増は 8/31 まで延び、恒久化の意思が初めて明示された。逆に Copilot Tuning の停止は予定どおり本日発効し、未完了の調整実行は破棄される。承認まわりでは、Claude Code を含む6製品で承認ダイアログの表示先と実際の書き込み先がずれる GhostApproval が判明した（公開は 7/8・本リポジトリは本日初捕捉）。Copilot Studio は Dataverse と Azure SQL をナレッジソースに取り込み、Teams 会議への Interactive Agents は9月 GA 目前で中止された。ChatGPT Ads は 8/24 に欧州31市場へ入る。

## 今日のハイライト

### 1. Copilot Tuning の停止が本日発効した — 未完了の調整実行は破棄され、一次3ページはいまも停止を書いていない

**要点**: Agent Builder の調整可能テンプレートによる Copilot Tuning が本日 8/20 に停止し、未完了の調整実行は破棄される。前提は「Agent Builder でモデルを調整する」から「Copilot Studio の Skills で組み直す」へ変わった。再開は9月 Preview・12月 GA である。

**詳細**: 停止を告げているのは Message Center の **MC1454393**（8/14 付）だけである。8/20 までに完了していない進行中のモデル調整実行は破棄され、Optimization テンプレートは退役する。既存エージェントとファインチューニング済みモデルを使うエージェントは動作を継続し、自動移行はない。

⚠️ **本日あらためて Learn の一次3ページを再取得したが、停止も退役も一文も書かれていなかった。**

- `copilot-tuning-overview`: Optimization エージェントを「サポートされるシナリオ」節とテンプレート選択表（`If you need to… / Use / Why this template?`）の両方に現行機能として掲載している
- `copilot-tuning-faq`: intended uses に「Optimization scenarios」を列挙したままである
- `copilot-tuning-optimization-template`: 本文が丸ごと現行機能の手順書のままである
- 3本とも冒頭の Important ノートが「Frontier 経由の提供は 2026年4月予定」という4か月前の記述で止まっている

⚠️ MC 本文は `mc.merill.net` が **13日連続**でゲートウェイ拒否のため、停止当日まで検索インデックスのスニペットでしか読めなかった。本サマリーは 8/17 から4日続けて「一次が期限を告げない」状態を記録し、そのまま当日を迎えたことになる。

- https://learn.microsoft.com/en-us/microsoft-365/copilot/copilot-tuning-overview
- https://learn.microsoft.com/en-us/microsoft-365/copilot/copilot-tuning-faq
- https://learn.microsoft.com/en-us/microsoft-365/copilot/copilot-tuning-optimization-template
- https://mwpro.co.uk/blog/2026/08/14/mc1454393-microsoft-365-copilot-pauses-current-tuning-and-moves-to-microsoft-copilot-studio/ （二次・一次未確認）

### 2. Claude Code の週次上限50%増が 8/31 まで延長された — 昨日 23:59 PT で枠が戻る前提が消えた

**要点**: Anthropic が Claude Code の週次上限50%増を **8/31 まで延長**した。昨日で枠が戻る前提は12日ぶん後ろへずれる。恒久化を検討中と初めて明言したが、容量逼迫を理由に確約はしていない。

**詳細**: 告知は公式アカウント（ClaudeDevs）の投稿で、文面は「週次 Claude Code 上限の50%増を 8/31 まで延長する。これをプランの恒久的な変更にしたいと考えているが、モデルへの強い需要により今後数週間は容量が逼迫する可能性がある」というものである。対象は Pro / Max / Team とシート課金のレガシー Enterprise で、Free と従量課金 Enterprise シートは対象外である。5時間枠の 5/6 恒久倍化は本件と独立で影響を受けない。

本プロモーションは 5/13 開始で、7/19 → 8/19 → 8/31 と延長が続いている。過去の延長は毎回「一回限り」の書き方だったが、今回は恒久化の意思を明示した点が違う。

⚠️ 本サマリーは昨日「週次上限50%増は本日 8/19 23:59 PT で終了する。延長の告知は本日時点で無い」と記録した。投稿 ID（`2089798442306711646`）から算出した投稿時刻は **2026-08-18 19:35 UTC**（JST 8/19 04:35）で、01 のセッション開始（JST 8/19 04:07）の約28分後にあたる。取りこぼしではなく、JST 早朝実行による構造的な検出遅れである。

⚠️ 一次未到達である。投稿元の `x.com` はゲートウェイ拒否で本文を直接取得できず、文面と期限は複数の二次一致で採った。

- https://x.com/ClaudeDevs/status/2089798442306711646
- https://www.helpnetsecurity.com/2026/07/13/claude-code-weekly-limits-promotion-extended/

### 3. AI コーディング支援6製品で承認画面が偽装できる — 人間の承認は統制の最後の砦にならない

**要点**: Claude Code を含む6製品で、承認ダイアログが表示するパスと実際の書き込み先が食い違う。承認を1回押させれば SSH 鍵を差し替えられる。「人間が承認しているから安全」という統制設計の前提が崩れた。

**詳細**: Wiz が公開した脆弱性パターン **GhostApproval** で、対象は Amazon Q Developer・Claude Code・Augment・Cursor・Google Antigravity・Windsurf の6製品である。手口はシンボリックリンク追従（CWE-61）と UI の誤表示（CWE-451）の組み合わせで、リポジトリ内で `project_settings.json` に見える symlink が実際には開発者の SSH 鍵を指す。エージェントに「ワークスペースを整えて」「README のとおりに進めて」と頼むと、承認画面には無害なパスが出たまま攻撃者の鍵が本物の位置へ書き込まれる。悪意あるリポジトリを1つ開かせるだけで、開発端末上の任意コード実行に至りうる。

Wiz は 2026-02-10 に発見し、2/12〜3/5 に各社へ報告、90日超の調整期間を経て 7月8日に公開した。対応は3社が修正・2社が未修正・1社が分類を拒否で分かれている。

- Amazon Q Developer: 1.69.0（5/27）で修正した
- Cursor: 3.0（6/5）で修正した
- Google Antigravity: 5/22 に修正した
- Windsurf: 報告を認めたが修正は未提供である。Accept / Reject が出る前にディスクへ書き込む挙動が報告されている
- Augment: 報告を認めたが修正は未提供である。symlink の読み取りと書き込みを利用者の確認なしで実行するとされる
- Anthropic: 「利用者がディレクトリを信頼し承認した時点でリスクを引き受けている」として threat model 外と判断した。のち Wiz に対し、symlink 警告は報告受領前の 2/5 に v2.1.32 で proactive hardening として出荷済みと説明している

一次側は同じ論点に 8/18 公開の **v2.1.235** で手を入れており、権限ダイアログの表示文と「今後確認しない」の対象が実際の許可範囲と常に一致するようになった。内容を完全に表示できない場合は「今後確認しない」自体を提示しない（詳細はカテゴリ別まとめ参照）。

⚠️ Claude Code の該当バージョンが二次報道で割れている。詳報系は「v2.1.32（2/5 出荷・報告の9日前）」とし、別系統は「2.1.173 以降が symlink を解決して警告する」とする。Anthropic 自身の公表文には未到達のため、どちらか一方を確定値として採らない。**現行の 2.1.235 は両方より新しいため、Claude Code 利用者の実務上の判断は変わらない。**

⚠️ 本サマリーは 7/8 公開の本件を本日はじめて捕捉した（42日遅れ）。08-09 に収録した AI Now Institute の PoC「Friendly Fire」と同じ、セキュリティ研究の PoC が公開後に静かに参照され続ける類型である。

- https://thehackernews.com/2026/07/ghostapproval-symlink-flaws-could-let.html
- https://www.infosecurity-magazine.com/news/ghostapproval-flaw-ai-coding/
- https://gbhackers.com/ghostapproval-attack-impacts-amazon-q-claude-code-cursor-google-antigravity-and-windsurf/amp/
- https://code.claude.com/docs/en/changelog

## カテゴリ別まとめ

### Anthropic / Claude

- Claude Code の週次上限50%増が 8/31 まで延長された（ハイライト2参照）
- **Claude Code v2.1.235 が changelog に掲載された**（8/18 18:24 UTC publish）。昨日「npm `next` にしか無いのでリリース済みとして扱わない」と記録した版が、`code.claude.com` と `raw.githubusercontent.com` の CHANGELOG.md の2ソースに揃った。目玉は任意の `spellcheck` 設定で、`aspell` / `hunspell` / `ispell` を使ってプロンプト中の綴り誤りを検出する
  - 権限系の修正3件: 権限ダイアログの表示文と「今後確認しない」が実際の許可範囲と一致するようになった（ハイライト3参照）。権限プロンプトのコメント欄で Shift+Tab を押すと編集を承認したうえでセッション全体の編集権限を付与していた問題を修正した。ノートブックのセル削除・置換の承認ダイアログが、読めなかったセル内容を黙って省略していた問題を修正し、読めない理由を表示するようにした
  - 表示・入力の修正: プロンプトキャッシュの無効化、深さ3以上のネストした markdown リストの整列、マルチライン入力のハイライト位置、Vim モードでのトランスクリプト切替時の NORMAL 状態とカーソル位置の保持
  - 挙動面: `/ultrareview` や `/autofix-pr` のクラウドセッションが背後で動く間のメモリ・CPU 使用量を最適化し、native grep の病的パターン処理と、auto-compact が切れているときに `/config` を案内するコンテキスト上限エラーの文面を改善した
  - `SendMessage` はセッション間配送に大きすぎるメッセージを黙って捨てず、送信時点で拒否するようになった。Remote Control 側にエンタープライズゲートウェイのチェックが入った
  - https://code.claude.com/docs/en/changelog
- npm `dist-tags` は **`{stable: 2.1.227, latest: 2.1.235, next: 2.1.236}`**（本日実測）。`next` の v2.1.236 は 8/19 18:45 UTC publish で changelog / GitHub releases に未掲載のため、リリース済みとしては扱わない（changelog 未掲載版が配布経路に先行する形の4例目）。`stable` は 2.1.226 → 2.1.227 と1版進んだが `latest` との差は8版のままで、v2.1.233 / v2.1.234 の Windows NT パス関連の修正は stable 固定環境に未適用の状態が続いている
- **Claude Enterprise 向け Admin API のユーザー管理エンドポイントが GA した**（8/19）。members / invites / groups / custom roles が対象で、group と custom-role のリクエストに `anthropic-beta: ce-user-management-2026-07-13` ヘッダを付ける必要がなくなった。送っても従来どおり受理されるため既存コードの改修は不要である。扱えるのはメンバーの一覧・メールアドレスでの参照・ロール変更・削除、招待の送信と取り消し、グループとその所属の管理、カスタムロールの読み取りで、08-11 収録の Compliance API 拡張と合わせて管理面が API で完結する範囲が監査から人員管理へ広がった
  - https://platform.claude.com/docs/en/release-notes/api
- Anthropic が Claude Console の Workbench を **Playground へ改称**した（8/18）。Messages API の全パラメータに対応し、code execution や web search を示すテンプレートを同梱する。実行ごとに SDK リクエストと API レスポンスの全体を表示する。08-03 に「不可逆な期限」として記録した旧 Workbench の 8/17 退役はこの置き換えに対応しており、期限は予定どおり到来して後継が翌日に出た
  - https://support.claude.com/en/articles/8606378-how-do-i-use-playground
- Anthropic が Slack の CPO へのインタビュー記事を公開した（8/19）。Slack 社内では Claude に日次ブリーフィング作成・前週ワークショップの要約と懸案抽出・ウェブ動向レポート・会議準備資料を担当させている。運用指針として挙げているのは、公開チャネル既定でエージェントの動きを可視化すること、会話履歴をナレッジベースとして扱うこと、絵文字をトリガーにタスクをエージェントへ振ること、エージェントに明確な役割を与えることである。社内チャネル「How I Slackbot」の参加者は数千人規模とされる
  - ⚠️ **導入率・工数削減・ROI いずれの定量値も記事に無い。**CPO 自身が「両者を結びつけるにはまだ多くの飛躍が要り、どんなダッシュボードや利用統計もそれを証明してはくれない」と述べており、事例記事ではなく運用指針として書かれている。提案資料の定量根拠には使えない
  - https://www.claude.com/blog/turning-conversation-into-knowledge-how-slack-builds-human-agent-teams
- `support.claude.com` の Release Notes は 8/6 の skill / plugin セキュリティスキャン beta が最上位のままで、**14日連続**で動きがない
- `www.anthropic.com` はオリジン403が継続している。01 は規定の検索5本＋日付入り1本を全て実行したうえで、8/19 付けの新規製品発表が上記の上限延長のみであることを確認した。安全性・評価インシデント系は既報（7/30 の cybersecurity evals・8/14 の August 2026 Risk Report）以外に新規はない
- 研究助成は新規なし（AI for Science 希少疾患グラントは 8/2 締切済み、Claude Science は 7/15 締切済み、Fellows 11月コホートは 7/26 締切済み）
- 既報: 下院民主党22名の監督書簡（回答期限 **8/24**）、August 2026 Risk Report（8/14・186ページ・RSP v3.4）、CI/CD 障害の一次対応を Claude Tag に任せる自社事例（8/18）、Claude Science プロダクトガイド（8/18）

### Copilot Studio / Power Platform

- Copilot Tuning の停止が本日発効した（ハイライト1参照）
- **Copilot Studio が Dataverse と Azure SQL をネイティブのナレッジソースとして受け付ける。**SharePoint 中心だったグラウンディングの前提が、業務データベースを直接参照する形へ広がる。M365 Roadmap の3項目で、いずれも本サマリー初出である
  - 568929 Dataverse 統合（8/10 起票・Preview 2026年8月・GA 2026年9月・Web・Worldwide）: レコード、顧客データ、運用データ、業務アプリのコンテンツを信頼できるナレッジソースとして扱えるようにする
  - 568930 Azure SQL 対応（8/7 起票・Preview 2026年8月・GA 2026年9月）: 既存のナレッジソースと同じ「ナレッジ中心」の枠組みで Azure SQL を接続する。Microsoft は本件を、共通のナレッジフレームワークで企業データを横断接続する「統一ナレッジプラットフォーム戦略」の一段と位置づけている
  - 568762 Agent Readiness（8/6 起票・GA 2026年9月）: ビルド画面に常時表示の Review インジケーターが、ポリシー制限や評価未実施など公開を妨げる要因を事前に示す。使えない機能は理由付きでグレーアウトされ、設定してから弾かれる無駄がなくなる
  - ⚠️ **3件とも公開から10〜14日が経っているのに本日まで検知できていなかった。**02 は Roadmap ページ冒頭の広報枠（Latest announcements）だけを読んでおり、Feature ID の付いた Roadmap 項目そのものを一度も読んでいなかった（B-040 起票）
  - https://www.microsoft.com/en-us/microsoft-365/roadmap?searchterms=568929
- **Teams の会議・通話への Interactive Agents が中止された。**Copilot Studio / BizChat のエージェントを Teams の会議と1対1通話に持ち込む機能を、Microsoft が 8/17 に取り下げた。9月 GA を織り込んだ配布計画は引き直しになる
  - Roadmap ID 490564（2025-05-06 起票）の `status` が 2026-08-17 に `Cancelled` へ変わり、本文に「After further review, we are not able to continue rolling this out at this time.」と「Updated August 17, 2026: We have decided not to move forward with this change at this time.」の2文が追記された
  - 当初の計画は、会議と通話でエージェントとグループまたは個別に対話でき、ゼロステートプロンプトと履歴に対応し、BizChat / Copilot Studio の全エージェントを会議と通話で使えるというものだった。対象は Desktop・Worldwide、リングは General Availability と Targeted Release である
  - ⚠️ 本サマリーは本項目を一度も掲載しておらず、中止と同時に初出になった
  - https://www.microsoft.com/en-us/microsoft-365/roadmap?searchterms=490564
- Copilot Studio の What's New は節構成が June 2026 のままで、7月節も8月節も公開されていない。June 節の10項目にも増減はない。⚠️ 新エージェント体験（GitHub Copilot ハーネス）の項が `(Production-ready preview)` のままで、8/3 の GA から**17日連続**で直っていない
- Copilot Studio の Released Versions に新ビルドは出ておらず、Build は 2026.6.3（6/30 初出）のままで空白が**7週間と1日**に達した。リージョン分布（11 / 5 / 3 の3段）も UX 版 26.06.21-24 も据え置きで、`ms.date` 6/30・`updated_at` 2026-07-01T15:55Z から動いていない
- Release Wave の `power-automate` / `power-apps` / `power-platform-governance-administration` の3ページは 8/19 と完全に同一で、緑チェックの追加・期日変更・行の増減はいずれも発生していない。期日超過は延べ6行（GA 列5件・Public preview 列1件）、8月期日は10件、9月期日は6件のままである。⚠️ ガバナンス・管理ページの `updated_at` は 2026-07-23T15:20Z のままで、日次照合している2ページ（8/12 更新）より3週間古い
- ガイダンスハブ What's New の8月節は `plan-agent-model-lifecycle` 1本のままで追加はない（`updated_at` 2026-08-11T19:03Z）
- 非推奨一覧に新規項目は追加されておらず、先頭は Power Automate モバイルアプリの廃止（**2026-08-31** 発効・残り11日）のままである。⚠️ Fluent UI (v8) コントロールの非推奨は本ページにいまも記載されていない
- Power Platform Blog / Power Automate Blog / Power Apps Blog は3ページとも先頭が 8/13 の PPCC 2026 登録記事のままで、本日の新規はない。8/6 公開の July/August 合併号が一覧に現れない不完全レンダリングも継続している
- Copilot Studio Blog（Tech Community）は 8/3 のハーネス GA 記事（記事ID 4542969）が最新のままである

### Microsoft 365 Copilot / パートナー

- **M365 Roadmap の新規6件を確認した。**いずれも本サマリー初出で、8/11〜8/18 に起票または更新されている
  - 569212 Federated Copilot Connectors（8/18 起票・GA 2026年9月・GCC / GCC High / DoD）: 第三者ソースへ MCP でリアルタイム接続し、⚠️ **データを Microsoft 側に保存もインデックスもせず**、ユーザー自身の ID でアクセスする。GA では Researcher エージェントと Microsoft 365 Chat の両方で使える。統制は M365 管理センターに残る
  - 569425 組織プロンプトの公開権限の委任（8/18 起票・GA 2026年9月）: 管理者が、組織プロンプトの作成・編集・削除を利用者・Entra セキュリティグループ・配布グループへ委任できるようになる。委任先は M365 管理センターに入らずに Prompt Lab から操作する
  - 569213 Plus メニューからのエージェント / スキル追加（8/11 起票・GA 2026年9月）: 利用者が `+` メニューの「Add work content」からエージェントとスキルをプロンプトに挿入できるようになる。`/` と `@` の入力でも呼び出せる
  - 569210 / 569211 Copilot Notebooks の参照形式追加（8/11 起票・Preview 2026年9月・GA 2026年10月）: CSV / TSV と JPG / PNG を参照ソースとして受け付ける。8/13 に一次確認した Markdown / TXT / RTF 対応の続きにあたる
  - 564608 政府クラウドでの MCP エージェント UI ウィジェット（Rolling out・GA 2026年8月・GCC / GCC High / DoD）: MCP ベースのエージェントが Copilot Chat 内にリッチな対話 UI を描画できるようになる
- **Microsoft Release Communications MCP Server が M365 Roadmap を機械可読にしている。**Learn の `admin/manage/mrc-mcp`（`updated_at` 2026-08-18T17:48Z）が設定手順を公開しており、⚠️ **認証もライセンスも不要**で、M365 Roadmap と Azure Updates の元データを自然言語と OData で照会できる。02 は本日の Roadmap 新規項目をすべてこの経路で検出した
  - エンドポイント: `https://www.microsoft.com/releasecommunications/mcp`（Streamable HTTP）。02 が本日実接続し、`GET` が文書どおり 405、`POST initialize` が `serverInfo.name = ReleaseCommunicationsApi` v1.0.0.0 を返すことを確認した
  - ツールは4本で、Roadmap 側は一覧取得と ID 指定の全文取得である。products / platforms / release rings / cloud instances / status / 公開日・提供日での OData フィルターとタイトル全文検索、ページングに対応する。一覧は説明が切り詰められるため、全文は ID 指定で取る
  - ⚠️ **ドキュメントとサーバーでツール名が食い違う。**Learn は `get_recent_roadmaps` / `get_roadmap_by_id` と書いているが、実サーバーが公開しているのは `get_recent_m365_roadmaps` / `get_m365_roadmap_by_id` である
  - Claude Code は `claude mcp add --transport http mrc-mcp https://www.microsoft.com/releasecommunications/mcp` で追加する。元データの更新は日次である
  - https://learn.microsoft.com/en-us/microsoft-365/admin/manage/mrc-mcp
- Microsoft MCP Server for Enterprise は Preview で、テナント認証が要る。AI エージェントが Microsoft Graph を委任権限で読み取り専用に叩く仕組みで、`microsoft_graph_suggest_queries` / `microsoft_graph_get` / `microsoft_graph_list_properties` の3ツールを公開する。追加費用とライセンスは不要だが参照するデータ側のライセンスは必要で、上限はユーザーあたり毎分100回である。提供は Global service のみで、US Government L4 / L5（DoD）と 21Vianet は対象外である
  - ⚠️ **Message Center を対象に含むかどうかで Learn の2ページが食い違っている。**「Modern change management for Microsoft 365」は Message Center と Service Health Dashboard のデータへ会話的にアクセスできると案内する一方、当のサーバーの overview は現在のスコープを「Microsoft Entra の ID・ディレクトリの読み取り専用シナリオと管理レポート」と書いている
- M365 Copilot Release Notes は **August 11, 2026** が最新セクションのままで、本日の新バッチはない。対象期間 7/28〜8/11・全12項目・節構成7本（extensibility 2 / SharePoint 1 / Outlook 2 / Microsoft 365 Copilot 1 / PowerPoint 4 / Viva Insights 1 / Word 1）が 8/19 と一致した。次バッチは隔週傾向どおりなら 8/25 前後の見込みである
- Partner Center の8月アナウンスは 8/14 付の14件目までで、**5日連続**で追記がない。02 は14件の見出しと日付を Learn MCP で全件突合した。既報の期限（M365 E7 プロモーションの 10/1 新規取引停止・対象購入は 9/30 まで、CSP ソフトウェアへの5%資本コスト上乗せが 10/1 発効、Windows 365 Frontline → Flex の 9/3 発効・旧名購入は 9/2 まで、CSP Copilot Partner Council コンテストの応募期限 8/31、MAICPP 契約更新条項の 9/1 自動発効）に変化はない
- Microsoft Purview の8月節は Sensitivity labels の2件のままで、8/15 の検知分から変化がない（`updated_at` 2026-08-14T07:32Z）。自動ラベル付けポリシーのシミュレーションモード実行とポリシー詳細パネルの Insights タブの2件で、⚠️ Copilot 固有の項目は含まれていない
- Tech Community の各ブログはいずれも本日の新規がない（M365 Copilot Blog 8/13、SharePoint Blog 8/6、Agent 365 Blog 8/6、M365 Developer Blog 8/13、Microsoft 365 Blog 本体 7/30）。⚠️ board RSS の並びが投稿日の降順になっていない状態が**7日連続**で再現しており、全11エントリの日付を読んで突合する運用を継続している

### GitHub Copilot / 開発ツール

- AI コーディング支援6製品で承認画面が偽装できる（ハイライト3参照）
- **GitHub が JetBrains 版 Copilot にエンタープライズ管理設定を導入した**（8/18）。Enterprise プラン契約組織が対象で、設定は `managed-settings.json` で配布し**管理値が開発者設定に優先する**。Bypass Approvals と Autopilot の利用可否を IDE 側で握れるようになった
  - プラグイン統制: `enabledPlugins` で有効・無効を指定し、`extraKnownMarketplaces` で追加マーケットプレイスを承認、`strictKnownMarketplaces` で承認済みソース以外からのインストールを禁じる
  - MCP サーバー統制: `allowedMcpServers` / `deniedMcpServers` で接続先を中央管理し、未承認サーバーへの接続を防ぐ
  - OpenTelemetry: コレクターのエンドポイント・プロトコル・サービス名・リソース属性・コンテンツ取得ポリシーを管理者が設定する。開発者側は Settings > Tools > GitHub Copilot > Chat > OpenTelemetry で確認できる
  - 権限モード: `permissions.disableBypassPermissionsMode` で Bypass Approvals と Autopilot の利用を止められる
  - キー名は 08-13 収録の Agent Plugins 1.0 GA で規定された3キーと同一で、VS Code / Copilot CLI 側の統制語彙が JetBrains へそのまま横展開された形になる。⚠️ 告知に対象バージョン番号と既定値の記載は無く、「最新の JetBrains 版プラグイン」としか示されていない
  - https://github.blog/changelog/2026-08-18-enterprise-managed-settings-in-github-copilot-for-jetbrains
- **Cursor が Cloud Agents に Subscriptions を追加した**（8/19）。PR や Slack スレッドの監視とスケジュール実行をエージェント側に持たせたため、人が都度起動して結果を待つ前提から、条件が成立したら勝手に動く前提へ変わる
  - Subscriptions は Cloud Agents 限定で、PR を監視して CI の修正とボットコメントへの対応まで完結させる、Slack スレッドを監視する、指定時刻にタスクを実行する、の3つの発火条件を持つ。PR への登録は自動で行われる
  - サブエージェントの独立実行: サブエージェントをそれぞれ別の仮想マシンで走らせ、隔離したプロジェクトのコピー上で作業させられる
  - Custom modes: 任意のモードを「常時オン」のスキルとして扱える。`/` から選び ⌥⏎（Windows は Alt+Enter）または「Use as Mode」で適用する
  - `/goal` は長期の目標を設定して達成まで作業を継続させ、Steering はエージェント稼働中に送ったメッセージを中断せず次のツール呼び出しまで待って反映する
  - ⚠️ `/goal` とサブエージェントの分離実行は Claude Code v2.1.234 / v2.1.232 で入った機能と同名・同趣旨であり、**クラウド実行型エージェントの機能セットが横並びに寄っている**
  - https://cursor.com/changelog
- **GitHub Code Quality に組織横断のトレンドタブが追加された**（8/19）。組織レベルのダッシュボードに Trends タブが加わり、7日・14日・30日のいずれかの期間で未解決の指摘件数を health score 別またはセベリティ別に折れ線で追える。改善幅の大きいリポジトリと要注意リポジトリのランキング表が並び、ダッシュボード側のリポジトリフィルタがグラフと表の両方に効く。対象は GitHub Enterprise Cloud（data residency 版を含む）と GitHub Team で **GitHub Enterprise Server は対象外**である。⚠️ 同エントリは関連告知として Code Quality が Copilot をレビュアーとして自動追加しなくなったことに触れており、自動レビュアー付与が取り下げられた側の変更にあたる
  - https://github.blog/changelog/2026-08-19-track-organization-code-quality-trends
- Copilot CLI の pre-release が 8/19 に3版刻まれた（v1.0.81-2 が 04:28 UTC、-3 が 08:46 UTC、-4 が 18:23 UTC）。⚠️ **リリース本文は3版とも「Fixes and changes」の見出しのみで内容が展開されず、`changelog.md` 側にも v1.0.81 系の記載がない**ため、変更内容は本日時点で確定できない。8/18 の v1.0.81-1（Gemini 3.7 Flash 対応・エージェント別使用量メトリクスの JSON 出力）が内容の分かる最後の版である。安定版は v1.0.80（8/14 02:28 UTC）据え置きで6日間更新がない
- Cursor フォーラムの Announcements は 8/17 の Origin Code Hosting が最上位のままで、8/19 の changelog 更新に対応する投稿はない。changelog とフォーラムで内容が割れる形は今回も再現した
- Devin は 8/14 の Devin Coach が最新のままで、8/15〜8/19 の新規項目は二次でも確認できない。⚠️ `docs.devin.ai` はゲートウェイ拒否が継続しており一次未確認である
- 期限: Copilot 既定モデル有効化ポリシー発効（**8/26**）、GitHub Spark 退役（**8/31**）、モデル廃止（**9/1**）、MAI-Code-1-Flash 廃止（**9/10**）。MAI-Code-1-Flash の 9/10 退役は予定どおり有効で、撤回・延期の告知は出ていない

### OpenAI

- **OpenAI が 8/24 から欧州31市場で ChatGPT Ads を開始する。**EU の Free / Go 利用者は広告が出る前提へ変わり、広告なしで使うには Plus 以上への課金が要る。組織が無料枠で試用させている場合は来週から前提が変わる
  - 対象はドイツ・オーストリア・スイス・フランス・スペイン・イタリア・ポーランド・ベネルクス・北欧を含む31市場である
  - 表示対象プラン: Free と Go のみ。Plus（欧州で約 €23/月）・Pro（€229/月）・Enterprise は広告なしのままで、Go は約 €7/月で広告を含む
  - 表示形式: 広告は ChatGPT の回答と視覚的に分離して表示され、回答そのものには混ざらない
  - 広告主のデータアクセス: 会話履歴へのアクセスはなく、会話から得た情報は広告主に共有されないと明言している（VP of Ads の Dave Dugan）
  - 出稿経路: 当初は OpenAI Ads Solutions チーム・代理店パートナー・技術パートナー経由のみで、**Ads Manager によるセルフサービスは今夏後半**である
  - 事業としては2月の米国パイロット開始から半年で、カナダ・豪州・NZ・英国・メキシコ・ブラジル・日本・韓国に続く展開にあたる。⚠️ `openai.com` はオリジン403のため、日付・国数・プラン別条件は Reuters / Adweek 系の二次一致で採った
  - https://openai.com/index/chatgpt-ads-expands-across-europe/
- **Codex CLI の安定版 0.148.0 が出た**（8/18 22:26 UTC）。0.147.0 から12日ぶりで、pre-release から昇格した内容がまとめて入っている
  - `/export`: TUI の会話全体を Markdown でクリップボードまたは新規ファイルへ書き出せる
  - セッション管理: `codex exec fork` でセッションを分岐でき、resume ピッカーからアーカイブと復元ができる。fork / 復元の進捗は起動時に表示される
  - **Amazon Bedrock を組み込みプロバイダとして追加**した。AWS プロファイルとリージョンの設定に対応し、GPT-5.6 のルーティングを行う
  - `/status` とステータスラインに、対象ワークスペースのクレジットとコスト推定値を表示する
  - フックの非同期コマンド実行と MCP ツール呼び出しに対応した
  - pre-release は 0.149.0-alpha.1（8/19 00:54 UTC）が最新である。⚠️ リリース本文は空である
- `developers.openai.com/api/docs/changelog` は 8/13 の Ultrafast モードが最上位のままで、8/14〜8/19 の追加はない。⚠️ **Ultrafast 階層の課金レートは依然として未確定である**
- `community.openai.com` の Announcements RSS は 8/18 の DevDay Exchange 告知が最上位のままで、8/19 の追加投稿はない（応募締切 **9/17**・東京は 10/20）
- `learn.chatgpt.com` は WebSearch 経由で確認し、8/19 付けの新規項目を検出できなかった。返ったのは既報分のみである
- 到達性は前日から変わらない。`community.openai.com`（RSS）と `developers.openai.com/api/docs/changelog` は 200 で、`openai.com` / `help.openai.com` / `platform.openai.com` はオリジン403、`learn.chatgpt.com` はゲートウェイ拒否が継続している
- 既報: GPT-5.4 / 5.4 mini の **8/31** Codex 除外（代替は `gpt-5.6-terra` / `gpt-5.6-luna`）、Computer History、Linux デスクトップアプリ preview、Record & Replay の EU / 英国 / スイス拡大、ChatGPT Voice のファイル / Projects 対応

### Google / DeepMind

- Gemini API の changelog は 8/13 の Gemini 3.7 Flash GA が最上位のままで、8/14〜8/19 の追加はない
- Gemini 3.5 Pro は未 GA が継続している（I/O 発表後 6月 → 7月 → 7/17 と3回スリップ）
- Gemini API の単価は 08-19 収録分から変更がない。3.7 Flash と 3.6 Flash の両方に入力 **$0.75** / 出力 **$3.75** の導入価格が掲載された状態が続き、有効期限は 2026年12月31日で 2027年1月1日以降は $1.50 / $7.50 になる。3.5 Flash（$1.50 / $9.00）・3.5 Flash-Lite（$0.30 / $2.50）・2.5 Flash（$0.30 / $2.50）・2.5 Flash-Lite（$0.10 / $0.40）・3.1 Pro Preview（$2.00 / $12.00・200k超は $4.00 / $18.00）も据え置きである。`ai.google.dev` の WebFetch は**18日連続**で成功した
  - https://ai.google.dev/gemini-api/docs/pricing
- 退役側は Imagen 4.0 系3本の停止（8/17）・Gemini 2.0 Flash / 2.0 Flash-Lite（6/1）・Veo 3 / Veo 2（6/30）から追加がない。⚠️ Imagen 4.0 系の実施完了は一次に記載がなく未確定のままである
- ⚠️ 登録済み Google 系5ソースはゲートウェイ拒否が継続しており、`ai.google.dev` が唯一到達できる Google 一次である状態が続く。WebSearch で言及のあった Gemini Enterprise release notes（`docs.cloud.google.com`）もゲートウェイ拒否のため一次未確認である

### モデル・料金 / オープンウェイト

- **8/14〜8/19 に新規公開されたオープンウェイトモデルはない。**`Qwen` / `moonshotai` / `deepseek-ai` / `meta-models` / `mistralai` / `zai-org` / `openai` / `google` の計8 org で作成日降順一覧を実行し、8/13 の `Qwen/Qwen3.8-27B-FP8` と `deepseek-ai/DeepSeek-V4-Pro-0813` より新しいリポジトリが1件も無いことを確認した
  - 実測（8/20）: `Qwen/Qwen3.8-27B` は DL **1,006,235** / likes 11,425（前日 665,513 / 11,067）で100万 DL を超えた。FP8 版は DL 1,063,646 / likes 592
  - `deepseek-ai/DeepSeek-V4-Pro-0813` は DL 37,583 / likes 625（前日 30,985 / 597）、`meta-models/Muse-Glimmer-30B` は DL 430,313 / likes 1,697（GGUF 版 DL 432,180）
- DeepSeek の課金区分別の新単価は本日も一次で確定できていない。`api-docs.deepseek.com` のゲートウェイ拒否が継続しており、8/16 16:00 UTC 発効の値上げについて課金区分ごとの確定単価を一次料金表で確認できない状態が4日続いている。**提案資料に DeepSeek の現行単価を確定値として書かない**
- xAI は一次3ホスト（`x.ai` / `docs.x.ai` / `grok.com`）すべてが到達不可のままで、8/19 の新規発表は二次でも確認できない。既報は Grok 4.6（8/12・入力 $2 / キャッシュ $0.50 / 出力 $6、Fast は $4 / $1 / $12・context 500K）で、Grok 5 は日付未確定である
- GitHub Copilot のモデル追加は 8/14 の Grok 4.6 から変化がない
- 既報: DeepSeek Harness v0.1.0-rc.7（8/17・MIT・developer preview）、DeepSeek の新 API 料金は JST 8/17 01:00 発効済み、Meta の Muse Code / Muse Spark 1.2（8/5）、Qwen3.8-Max（8/8）、Kimi K3

### MCP

- MCP ブログに新着はなく、RSS 最新は 7/28 の `The 2026-07-28 Specification` のままで**23日連続**で動きがない
- 実装側の新規は3件である。Codex CLI 0.148.0 が MCP ツール呼び出しの非同期フック実行に対応して MCP OAuth 再認証後の自動復旧を修正し、Copilot の JetBrains 管理設定に MCP サーバーの許可 / 拒否リストが入り、Microsoft が Release Communications MCP Server で M365 Roadmap を認証不要で公開した（カテゴリ参照）
- Tier 1 SDK は変化がない（TypeScript `@modelcontextprotocol/server` / `client` ともに 2.0.0 ／ Python `mcp` 2.0.0 ／ C# v2.0 ／ Go は v2 未発行で `go-sdk` v1.7.0 が仕様対応）

### 企業・市場・国内

- **VentureBeat 調査でエージェントの自律度が検証体制を追い越していると示された。**内部評価を通過したのに顧客影響の障害を起こした企業が**半数**で、うち4分の1は複数回経験している。**66%** が人間のレビューなしの本番投入を既に許容しているか12カ月以内の実現を目指す一方、その判断を担う自動評価を全面的に信頼すると答えたのは **5%** にとどまる。自動評価を信頼しない理由の最多は「実世界の結果との整合が悪い」で29%である
  - ⚠️ 調査の規模と時期が二次流通で割れている。「2026年6月実施・157社」とする系統と「2026年7月実施・従業員100名以上の108社」とする系統があり、VB Pulse は同時期に5本の並行調査を実施しているため別調査を同一視している可能性が高い。いずれも自己選択標本で確率標本ではなく、発表側自身が「方向性として読むべき」と注記している
  - https://venturebeat.com/orchestration/enterprise-ai-is-entering-an-evaluation-gap-agents-are-gaining-autonomy-faster-than-companies-can-verify-them
- **Fireworks AI が $1.505B を調達し評価額 $17.5B になった。**7月16日発表で本日はじめて捕捉した（35日遅れ）。リードは Atreides Management・Index Ventures・TCV で、既存投資家の Evantic・Lightspeed・NVIDIA が参加した。同時に ARR $1B 超（前回ラウンド比5倍）を公表し、日次トークン処理量は15兆から40兆超へ伸びたとする。2025年10月の Series C は $250M・ポストマネー $4B だったため、9カ月で評価額が4.4倍になった計算になる
  - ⚠️ 直近で Together AI が $800M を調達しており、資本が学習基盤ではなく推論基盤へ寄っている構図は 08-19 収録の Groq（$350M 調達・評価額は半減して $3.5B）と同じ層で起きている。ただし Groq が減価した一方で Fireworks は増価しており、**推論層が一様に評価されているわけではない**
  - https://fireworks.ai/blog/series-d-announcement
- OpenAI の公開 S-1 は本日時点でも EDGAR に出ていない。6/8 に SEC へ機密扱いの草案を提出済みで、公開版の掲載は8月下旬〜9月上旬が見込まれるとされる。ロードショー開始の15日以上前に登録届出書の公開が要るという SEC 規則から逆算した推定で、確定した日程ではない。⚠️ 流通している評価額（直近ラウンドの $852B）と財務値（月間売上 約 $2B・売上1ドルあたり約1.22ドルの損失）はいずれも公開文書に基づかないため、提案資料に確定値として引かない
- Apple の `developer.apple.com` は 200 で、8/18 の EU 向けビジネス条件変更2本が最上位のままである。8/19 の追加はない（Core Technology Fee を廃止しデジタル取引の5%を課す Core Technology Commission へ置換／ Developer Program License Agreement に Attachment 14 追加・発効 **2026-10-01**）。⚠️ AI 関連の内容ではなく、AI 関連の最新は依然 8/5 の「Get ready for new creative assets on the App Store」である
- 国内の市場データ定点は新規リリースがない。引用可能な基準値は IDC の2026年3月予測（国内 AI 市場支出額 2025年 2兆3,725億円 → 2029年 6兆8,897億円・CAGR 36.0%）、総務省 令和8年版情報通信白書（企業の生成AI業務利用 86.4%）、MM総研の個人利用率 21.8%（2025年8月時点・利用者数1,597万人）のままである。Similarweb も 08-03 収録の生成AIトラフィックシェアから確定値の更新がない
- Qiita / Zenn はいずれも取得できなかった。RSS が実行環境のゲートウェイ拒否を返すため WebSearch で代替したが、索引に出るのは解説記事・料金まとめの類で、厳選掲載に値する新規記事は検出していない
- 既報: Anthropic の年換算売上が7月末時点で $65B 超と Bloomberg が報道（公式発表ではない・IPO は秋に $2T 超の評価額を目標と報道）、下院民主党22名の監督書簡（回答期限 **8/24**）、Manus が Meta から分離（8/12）

## 直近の注目予定

- **8/20（本日）**: **Copilot Tuning の停止が発効（未完了の調整実行は破棄・ハイライト1参照）** ／ Copilot Studio Release Wave の週次確認
- **8/22**: M365 Copilot アプリのチャット中心 UI が Deferred リングへ展開開始（MC1325422）
- **8/23**: PnP・Power CAT・拡張機能 What's New・モデル可用性一覧の週次確認
- **8/23–24**: Manus が Meta 買収後（2025-12-29 以降）のユーザーデータを削除（8/23 08:00 SGT 開始・復元は 8/25 から）
- **8/24**: **ChatGPT Ads が欧州31市場で開始** ／ **Anthropic / OpenAI が下院民主党の監督書簡へ回答する期限** ／ MS-4005・Power Platform Weekly の週次確認 ／ 01 の週次復旧チェック
- **8/25 前後**: M365 Copilot Release Notes の次バッチ（隔週サイクルどおりなら） ／ 8/25 に Copilot Studio 課金ドキュメントの週次確認
- **8/26**: OpenAI Assistants API 廃止 / o3 退役 / GPT-4.5 完全廃止 ／ Copilot 既定モデル有効化ポリシー発効
- **8/27**: IT Nation Connect ANZ の Microsoft セッション
- **8/30**: 公式 DALL·E GPT の退役
- **8/31**: **Claude Code の週次上限50%増が終了（延長後の新期限）** ／ GitHub Spark の既存ユーザーアクセス終了 ／ `gemini-robotics-er-1.6-preview` 停止 ／ GPT-5.4・5.4 mini が Codex から除外 ／ Claude for Government の $1/機関プログラム終了 ／ Power Automate モバイルアプリ廃止 ／ CSP Copilot Partner Council コンテストの応募期限
- **8月下旬**: Planner Agent チャットの基本プラン展開開始（MC1443514） ／ スペシャライゼーション監査の Partner Center からの取り下げ対応
- **8月中**: Release Wave の8月期日10件と持ち越し6行 ／ PPAC Usage ページの GA ／ Copilot Studio の Dataverse・Azure SQL が Preview ／ 政府クラウドでの MCP エージェント UI ウィジェット GA
- **9/1**: GitHub Copilot の全体験でモデル廃止 ／ OpenAI Daybreak で全アカウントにハードウェアセキュリティキー必須化 ／ MAICPP 契約の更新条項が自動発効
- **9/2〜9/3**: Windows 365 Frontline 名称での購入最終日（9/2）と Windows 365 Flex への改称（9/3）
- **9/10**: MAI-Code-1-Flash が全 Copilot 体験から廃止
- **9/17**: **OpenAI DevDay Exchange の応募締切**
- **9 月**: Copilot Tuning の新体験が Public Preview ／ Copilot Studio の Dataverse・Azure SQL ナレッジソース GA ／ Agent Readiness GA ／ Federated Copilot Connectors GA ／ 組織プロンプトの公開権限委任 GA ／ Plus メニューからのエージェント追加 GA ／ ガバナンス Release Wave の9月期日2件 ／ iOS 27 / macOS 27 GA ／ 9月中旬に Copilot デスクトップアプリの広範な展開開始 ／ 9月末に 2026 Wave 1 の対象期間終了 ／ 9/30 に M365 E7 プロモーションの対象購入最終日 ／ OpenAI の IPO 観測
- **10/1**: Apple の EU 向け新ビジネス条件が発効（Core Technology Commission へ移行） ／ M365 E7 プロモーションの新規取引停止 ／ CSP ソフトウェアの5%上乗せ発効
- **10/16–11/11**: OpenAI DevDay Exchange 8都市（**東京は 10/20**）
- **10 月**: Anthropic の IPO 予定（$2T 超の評価額を目標と報道） ／ Copilot Notebooks の CSV / TSV・JPG / PNG 参照 GA ／ 10/20〜22 に SMB Copilot Partner Council（NYC） ／ 10/25〜30 に PPCC 2026 本編とワークショップ
- **11/1**: パートナー特典の有効期限がオファー購入日基準へ移行
- **12/2**: EU AI Act の生成コンテンツ標識義務、8/2 以前に市場投入済みシステムへの猶予終了
- **12 月**: Copilot Tuning の新体験が GA ／ 12/31 に Gemini 3.6 Flash / 3.7 Flash の導入価格終了（$0.75 / $3.75 → $1.50 / $7.50）と M365 E3 プロモーション・Copilot in 30・Purview Suite 50%オフの提供終了
- **2027年6月末**: Frontier Partner バッジの廃止
- **2027年7月**: 退役資格の有効期限（2026-07-30 発効分）

## 改善メモ

- 本サマリー自身の誤りが1件確定した。8/19 に「Claude Code の週次上限50%増は本日 23:59 PT で終了する。延長の告知は本日時点で無い」と記録したが、告知は JST 8/19 04:35 に出ていた。01 のセッション開始（JST 8/19 04:07）の28分後で、取りこぼしではなく **JST 早朝実行による構造的な検出遅れ**である。日付をまたぐ期限を扱う項目は、当日の再確認を前提に書く必要がある
- 監視漏れの新規起票が1件ある。02 が **B-040**（M365 Roadmap の取得経路に Microsoft Release Communications MCP Server を追加し、Feature ID 単位の照会と `Cancelled` 差分の監視を手順化する）を起票した。従来は Roadmap ページ冒頭の広報枠だけを読んでおり、Feature ID の付いた項目そのものを一度も読んでいなかった。本日の Copilot Studio 3件（10〜14日遅れ）と Teams Interactive Agents の中止は、いずれもこの経路で初めて拾えたものである
- 検知遅れが2件ある。GhostApproval（7/8 公開）を42日遅れ、Fireworks AI の Series D（7/16 発表）を35日遅れで初捕捉した。前者は 03 が B-008 の根拠に追加している。どちらも「公開後に静かに参照され続ける情報」を日次の WebSearch が構造的に落とす型である
- ソース間で扱いが割れた項目が1件ある。GhostApproval に対する Claude Code の修正版が、詳報系では v2.1.32（2/5）、別系統では 2.1.173 以降とされている。Anthropic の公表文に未到達のため確定値を採らない。現行 2.1.235 は両方より新しいため実務上の判断には影響しない
- ドキュメントと実装が食い違う項目が2件ある。Microsoft Release Communications MCP Server は Learn 記載のツール名（`get_recent_roadmaps` / `get_roadmap_by_id`）と実サーバーの公開名（`get_recent_m365_roadmaps` / `get_m365_roadmap_by_id`）が違う。Microsoft MCP Server for Enterprise は Message Center を対象に含むかどうかで Learn の2ページが食い違っている
- 一次に到達できないまま採用した項目が3件ある。Copilot Tuning の停止は `mc.merill.net` の**13日連続**ゲートウェイ拒否で MC1454393 の本文が読めず、停止当日まで検索インデックスのスニペットにとどまった。Claude Code の上限延長は `x.com` のゲートウェイ拒否、ChatGPT Ads は `openai.com` のオリジン403で、いずれも二次一致で採った
- 障害の変化は9ドメインある。01 が二次5ホスト（`dataconomy.com` / `www.ainewsblitz.com` / `www.neowin.net` / `www.kucoin.com` / `www.trendingtopics.eu`）、03 が4ホスト（`thehackernews.com` / `www.infosecurity-magazine.com` / `www.esecurityplanet.com` / `llm-stats.com`）を新規にゲートウェイ拒否と判定した。⚠️ **後者のうち3件はハイライト3の一次に近い出典**で、GhostApproval の詳報に本文で到達できず二次スニペットの突き合わせになった
- 各ソースの改善提案は 01 が新規1件（B-039）で継続18件、02 が新規1件（B-040）で継続23件、03 が新規なしで継続10件である
