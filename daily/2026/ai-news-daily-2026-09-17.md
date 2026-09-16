# AI News Daily Summary — 2026-09-17

期限が3つ同時に動いた日である。M365 Copilot Business は 11/2 から従量課金が既定オンになり、OpenAI は `gpt-5.5` を 10/14 に ChatGPT と Codex から退役させ、Office LTSC 2021 は 10/13 でサポートが終わる。いずれも見積もりや提案の前提を置き換える種類の変更で、告知を見送ると後から引き直せない。製品側では Anthropic が Cowork と chat を1つの Claude に統合し、GitHub Copilot CLI の安定版はスクリプトを壊す変更3件を含んだまま出た。

## 今日のハイライト

### 1. M365 Copilot Business の従量課金が既定オンになる — ライセンス費だけの見積もりが成り立たなくなる

**要点**: 11/2 以降、CSP 経由で新規購入する M365 Copilot Business は従量課金が既定で有効になる。ライセンス費だけを見積もる前提が崩れ、1人あたり月$10 の消費枠込みで見積もることになる。

**詳細**: Partner Center の9月アナウンスに **2026-09-16** 付で「Usage-based billing will be default-on for new Microsoft 365 Copilot Business licenses starting November 2, 2026」が追加された。ページの掲載件数は9件から11件へ増えている。従量課金に必要な Azure サブスクリプションのセットアップが新規ライセンスに同梱され、パートナー側の多段階の課金構成作業が不要になる。Microsoft は狙いを「導入支援に時間を振り向けられること」と「初期利用から消費拡大・アップセルへの導線ができること」と説明している。

- 発効日: 2026-11-02。対象は CSP 経由の**新規購入**（単体・バンドルとも）で、既存ライセンスへの遡及は告知に記載がない
- 既定の上限: USD $10/ユーザー/月。上限の変更と前払いクレジットの追加は顧客側でできる
- ⚠️ **対象体験の一覧が一次と告知で食い違う**。告知は Copilot Cowork / Work IQ API / GitHub Copilot ハーネスの3つを挙げるが、Learn ページ（`ms.date` 2026-09-10）が挙げるのは Cowork / Cowork で作ったアプリ / Work IQ API で、GitHub Copilot ハーネスを含まない
- Learn 側には支出ポリシーの「新しいサービスを自動適用」が**既定で有効**と明記されている。明示的に無効化しない組織では、今後追加されるサービスが自動でポリシー対象に入る
- 9/14 に検知したクレジット統制ガイダンスは統制を4層（テナント / 環境 / エージェント / 運用プロセス）で設計するよう求めていたが、そこでの最初の関門は課金経路の有効化そのものだった。11/2 以降の新規購入ではその関門が無くなる

出典:
- https://learn.microsoft.com/en-us/partner-center/announcements/2026-september
- https://learn.microsoft.com/en-us/microsoft-365/copilot/usage-based-billing-overview-copilot-credits

### 2. GPT-5.5 が 10/14 に ChatGPT と Codex から退役する — API だけが対象外という非対称が残る

**要点**: OpenAI が `gpt-5.5` の 10/14 退役を告知した。対象は ChatGPT・ChatGPT Work・Codex で **API は含まれない**。同じモデル名なら同じ期限という前提が崩れ、面ごとに期限を確認することになる。

**詳細**: 告知は 9/14 付で、3ソースを通じて本日はじめて検出した（前日までは同ソースの最上位を 9/11 のままと記録していた）。退役はコンシューマー・Business・Enterprise・Edu の全プランに及び、移行先は `gpt-5.6-sol` である。OpenAI が移行対象として挙げているのは、ワークスペース既定・保存済みモデル設定・管理下の構成・カスタムエージェント・スケジュールタスク・スクリプトである。

- ⚠️ API 側の退役ページには `gpt-5.5` の記載がなく、最上位は 9/11 告知の `gpt-5.4-cyber`（削除 10/1・移行先 `gpt-5.6-cyber`）のままである
- `gpt-5.4-cyber` は料金ページの一覧からも外れており、停止（10/1）まで14日を残したまま掲示されていない状態が続く

出典:
- https://learn.chatgpt.com/docs/changelog
- https://developers.openai.com/api/docs/deprecations

### 3. Office LTSC 2021 が 10/13 でサポート終了する — オンプレ版 Office は Copilot の対象外と明記された

**要点**: Microsoft が Office / Project / Visio LTSC 2021 のサポート終了を 10/13 と告知した。Copilot はライセンスを足せば使えるという前提が崩れ、オンプレ版 Office のままでは対象外だと一次で確定した。

**詳細**: Partner Center の9月15日付告知である。終了後は更新・セキュリティ修正・技術サポートのいずれも提供されない。告知本文は **Microsoft 365 Copilot がクラウドバックされたアプリでのみサポートされる**と明記し、永続版 Office 向けの Azure Information Protection ラベリングクライアントも退役済みとしている。LTSC を使い続けている顧客には、Copilot 提案の前段としてスイート移行が必要になる。

- 企業向けの第一推奨は Microsoft 365 E3 で、代替は Office 365 E3 または Microsoft 365 Apps for enterprise である
- 300ユーザー未満は Microsoft 365 Business Premium / Business Standard / Apps for business が挙げられている
- クラウドへ移れない場合の受け皿として Office LTSC 2024 / Project LTSC 2024 / Visio LTSC 2024 が示されているが、この経路を採る限り Copilot は使えない
- Project LTSC / Visio LTSC の後継はそれぞれ Planner and Project Plan 3 / Visio Plan 2 で、スイートに重ねて追加する

出典:
- https://learn.microsoft.com/en-us/partner-center/announcements/2026-september

## カテゴリ別まとめ

### Claude / Anthropic

- **Cowork と chat の統合**: Anthropic が Cowork と chat を1つの Claude に統合し、Claude Docs と Claude Slides をベータ公開した（9/16）。ユーザーは用件を書くだけでよく、その場の回答で済ませるか調査・レポート・表計算・プレゼンとして引き受けるかは Claude 側が判断する。返るファイルには数式が生きた表計算と PowerPoint で開けるプレゼンが含まれる
  - 対象プラン: Pro / Max へ数週間かけて展開し、Team / Free は「近日」。Enterprise は変更の**30日前に管理者へ通知**し、有効化の時期は管理者が選ぶ
  - 引き継がれるもの: チャット・プロジェクト・アーティファクト・コネクター・スキルはそのまま使える。Claude Design は独立プロダクトから会話内の機能になった
  - Claude Docs / Claude Slides / Claude Design はいずれも有料プランのベータで、料金改定の記載はない
  - https://claude.com/blog/cowork-is-now-claude
- **Claude Code 2.1.273**: changelog に `2.1.273`（9/15）が載り、組織統制と権限チェックの修正が5件の `Changed` 行とともに公開された。⚠️ 統制面の2件は「設定したのに効いていなかった」型なので、Claude Code を組織配布している場合は現行バージョンの確認が要る
  - MDM / `managed-settings.json` の `allowManagedMcpServersOnly`・`deniedMcpServers`・`disableClaudeAiConnectors` が、サーバー管理設定と併存すると無視されていた
  - 組織が claude.ai 側で Skills を無効化しても同期済みスキルが使え続けていた。復元可能なゴミ箱へ移動するよう修正された
  - `permissions.blockReadsOutsideWorkingDirectories` 下で、完全に解析できない Bash コマンドが確認を飛ばしていた。bypass モードでサブシェルが危険な `rm` を隠す経路も塞がれた
  - 自動コンパクトがアドバイザーツールのターンを実サイズの約2倍で数え、実ウィンドウの**約半分**で発火していた
  - auto モードが Bedrock / Vertex / Foundry では当面ローカル classifier を既定で使う（`CLAUDE_CODE_AUTO_MODE_SERVER=1` でサーバー側へ）
  - https://code.claude.com/docs/en/changelog
- **npm の `stable` が31版昇格**: stable 固定の組織に `2.1.236` から `2.1.267` までの差分が一度に届くようになった。09-17 実測の `dist-tags` は `{stable: 2.1.267, next: 2.1.273, latest: 2.1.273}` で、前日の `stable: 2.1.236` から動いた。⚠️ `2.1.271` の権限修正5件と `Changed` 7件は `2.1.267` より新しいため、stable 固定組織には未到達のままである
- **一次の据え置き**: `support.claude.com` の Release Notes は 9/15 の Salesforce in Claude が最上位のままで、Cowork 統合はまだ反映されていない。`www.anthropic.com/news` も 9/10 の脅威インテリジェンスレポートが最新で、9/11 以降の新規公表はない。単価・レート上限の改定告知も出ていない

### OpenAI / Codex / ChatGPT

- **GPT-5.5 の退役**: ハイライト2を参照。
- **Codex CLI の pre-release**: OpenAI が `rust-v0.155.0-alpha.12`（9/16）まで進め、`alpha.9`〜`alpha.12` と `rusty-v8-v152.2.0` が同じ 9/16 に刻まれて1日で5タグ増えた。⚠️ 並びに `rust-v0.155.0-alpha.2.5` が混ざっており、`tags` 側でしか見えない不規則な採番になっている
- **料金は24日連続で据え置き**: OpenAI は主要モデルの単価を変えていない。GPT-6 Astra 短文脈 $10／$50、GPT-5.6 Sol 短文脈 $4／$20、Terra 短文脈 $2／$12、Luna 短文脈 $0.20／$1.20 はいずれも不変で、Sol の期間限定価格は「少なくとも **2026年11月21日**まで」の記載のままである
  - `gpt-daybreak-blue-latest` / `gpt-daybreak-red-latest`: 現在は `gpt-5.6-sol` / `gpt-5.6-cyber` を指すエイリアスで、新モデル公開に伴い指し先と単価が更新される。**エイリアス指定は単価の固定を意味しない**
  - EU データレジデンシー: GPT-6 Astra の Fast mode は使えず標準処理になる。対象モデルの10%上乗せとは別建ての制約である
  - `gpt-rosalind-research`: 10/5 の課金開始に加え、キャッシュ書き込み単価が適用されないことと、trusted-access 経由の承認済み内部研究に限られることが記載されている
- **その他の一次は動かず**: `developers.openai.com/api/docs/changelog` は 9/10 の3本（プロジェクト API キーの有効期限設定・Agents API パブリックベータ・GPT-Live 1 GA）が最上位のままで、`community.openai.com` の Announcements RSS も 9/10 から6日間動きがない。⚠️ `openai.com` のオリジン403は継続しており、本日も一次には到達できていない

### Google

- **Workspace の外部コネクター7件**: Gemini in Google Workspace が Asana・Atlassian Rovo・HubSpot・Intuit Mailchimp・Intuit QuickBooks・Monday・Salesforce へ MCP 経由で接続できるようになった（9/15）。既定は **ON**（Gemini for Google Workspace 保有ユーザー）で、管理コンソールの Third-Party Connectors からドメイン・OU・グループ単位に制御する。利用箇所は Docs / Sheets / Slides の Gemini サイドパネルと Google Chat である
- **Workspace Updates の新規6本**: 9/16 に2本、9/15 に4本が加わった。9/16 は Google Meet ホーム画面での会議室・会場情報の表示と Google Apps Script のデータリージョン対応 GA で、9/15 は上記コネクターのほか **Gmail 検索の AI Overviews が全世界で利用可能に**、Meet ハードウェアのルームコード接続 GA、Drive の共有境界を統合データ保護ルールで設定する4本である
- **Gemini API changelog は据え置き**: Google は 9/15 の `gemini-3.8-live` / `gemini-3.8-live-extended-thinking` GA を最上位のまま維持しており、9/16〜17 の追加はない。Gemini 3.8 Flash の導入価格が **2026-12-31 まで**である点と、`gemini-omni-flash-preview` の 9/30 廃止（後継 `gemini-omni-1.1-flash`）も不変である。Gemini 3.5 Pro は未 GA が継続している

### Microsoft 365 Copilot / 基盤

- **従量課金の既定オン**: ハイライト1を参照。
- **Microsoft 365 G7 が 10/1 GA**: 政府機関向けの新スイート Microsoft 365 G7 が一般提供される（Copilot Blog・9/15）。G5 の上に AI とエージェント機能を重ねた GCC 向け Frontier スイートで、Agent 365 と Microsoft Entra Suite を含む。提供は各ワークロードが GCC の認可マイルストーンを満たした順に段階展開され、Work IQ のメモリ・Office アプリ横断の Edit with Copilot・Copilot Cowork は後続になる。価格は未開示である
- **Graph PowerShell が Windows PowerShell 5.1 を退役させる**: Microsoft Graph PowerShell が 5.1 向けの保守を今後約12か月で打ち切り、Q4 CY2026 に出る v3.0.0 は 5.x を明示的にサポートしない（9/16 公開）。退役の意味は互換性ではなく**保守**の打ち切りで、v2.x は期間を通じて 5.1 互換を宣言し続ける
  - 退役期間中: v2.x は必要に応じてセキュリティ修正を受けるが、新機能・バグ修正・検証は PowerShell 7.x 以降が対象になり、5.x 固有の問題は調査も修正もされない
  - 記事は「今日切り替えるスイッチではなく計画された移行」と明記し、5.1 利用者に 7.x への移行計画着手を求めている
  - https://devblogs.microsoft.com/microsoft365dev/investing-in-a-more-reliable-microsoft-graph-powershell-experience/
- **Purview のネットワークデータセキュリティが GA**: 管理者が Entra Global Secure Access と連携してネットワーク層で DLP を適用できるようになり、ChatGPT・Gemini・Claude 等への送信を監査またはブロックできる。Purview What's New に **September 2026** 節が新設された（9月節の掲載はこの1件のみ）
  - アクティビティ4種（テキスト送信・ファイルアップロード・テキスト受信・ファイルダウンロード）に Audit only と Block の2アクションが用意され、Entra GSA は全組み合わせに対応する
  - ライセンス: GSA 連携は **Microsoft 365 E7** 単独、または Purview E5 相当 + Entra Internet Access 相当。非 Microsoft の SASE 連携は Purview の従量課金が要る。⚠️ E7 のプロモーション最終日は **9/30** である
  - 制約: B2B ゲストには適用されない。インライン評価の上限はテキスト 4 MB・ファイル 3 MB で、ポリシー配布に最大24時間かかる
  - ⚠️ 未管理クラウドアプリとして扱われるのは Microsoft Copilot の消費者版だけで、企業版 Copilot は本機能の対象外である（保護は既存の Enterprise data protection 側に載る）
  - https://learn.microsoft.com/en-us/purview/whats-new
- **Release Notes は August 25 のまま**: M365 Copilot Release Notes に新バッチは追加されていない。H2 は83本・`updated_at` 2026-09-03T19:39Z も不変で、⚠️ 隔週の期日（9/8 UTC）から9日、前バッチからは23日が経った
- **Partner Center の9月ページ**: 掲載が11件になり、9/16 付の追加はハイライト1の従量課金既定オンと Windows Server 2016 ESU の CSP 価格表再公開（8月価格表の誤記訂正・対象は DG7GMGF0HPVV と DG7GMGF0HPVW）の2件である。8月版を訂正前にダウンロードしたパートナーは再取得が必要になる

### Copilot Studio / Power Platform

- **ロードマップにコスト可視化3件が起票された**: メーカーが消費コストをどこで見られるかを3面に分けて埋める内容で、GA 期日はいずれも **September CY2026** である（9/15 23:00Z・掲載歴ゼロ）。9/14 のクレジット統制ガイダンスが指摘した「エージェント単位の可視性が無い」欠落に正面から対応する
  - `571196` Cost visibility in Monitor tab: Monitor タブでエージェント単位の消費コストと、オーサリング・テスト・評価・本番利用の内訳を見られるようにする
  - `571195` Cost visibility in Agent Evaluations: 評価に紐づく消費を、評価生成・テスト実行・モデルによる採点の内訳付きで見られるようにする
  - `571194` Cost visibility in Preview Chat and History: プレビュータブとエージェント履歴で、テスト利用分と過去の全実行分のコストを見られるようにする
- **Purview も同バッチで3件起票された**: `571397`（Entra 管理デバイス向けインライン保護の強化）・`571396`（未管理アプリ向けインライン保護の拡大）・`571157`（DSPM の Copilot Readiness と Data Explorer）がいずれも掲載歴ゼロで加わり、本日 GA したネットワークデータセキュリティと同じ方向に並ぶ
- **What's New は July 節のまま**: Copilot Studio の What's New は8月節・9月節とも未作成で、`updated_at` は 2026-08-20T19:04Z から28日動かない。⚠️ June 節の GitHub Copilot ハーネスは `(Production-ready preview)` のままで、GA（8/3）から **45日連続**の未反映である
- **課金レート表とバージョンは据え置き**: 機能別レート（クラシック 1 / 生成 2 / エージェントアクション 5 / テナントグラフ 10）・125% エンフォースメント・CUA 非免除に変化はない。⚠️ USD 単価は本日も Learn 側に存在しない。Copilot Studio Build は全リージョン **2026.6.3** のままで、`released-versions` の `updated_at` は78日動いていない
- **Power Platform の各ブログは新規なし**: 親ページ・子カテゴリとも更新がなく、Power Automate は 8/13 の PPCC 告知から **34日**新規がない。`important-changes-coming` にも新規の非推奨項目は追加されていない
- **Release Plans は9月以降 published されない**: 製品別5ページの冒頭 Important が、新機能は AI at Work roadmap へ移り既存の release plan は履歴参照用として残ると明記している。9/6 に Partner Center が告知した archive 方針がページ側にも載った形である

### GitHub / 開発ツール

- **Copilot CLI の安定版 `v1.0.85`**: 9/16 02:44 UTC に出た12日ぶりの安定版で、その間の pre-release 9本ぶんがまとまっている。⚠️ **スクリプトを壊す変更が3件**あり、`github.blog/changelog` には載らずリリース本文にしかない
  - `copilot plugins list --json` の出力が `{ plugins, errors }` オブジェクトから**フラット配列**に変わった
  - 横断フラグ `--kind` / `--scope` が**削除**され、`copilot mcp` と `copilot skill` に分かれた
  - `copilot plugins list` が plugins だけを返すようになり、MCP サーバー・skill・instruction・LSP サーバーを含まなくなった
  - 追加の主なもの: `/vim` の全ユーザー開放 ／ `/config` の設定サイドバー ／ `transcriptView` を `concise` にするとツール活動が折りたためる ／ `/sandbox` がプロキシ設定を置き換えずにホスト許可・拒否を書ける ／ GPT-6-Astra 対応
  - コマンドライン解析が Commander から Rust の文法実装へ移り、エラーメッセージとヘルプの文面が変わった。pre-release は `v1.0.86-0`（9/16 12:59 UTC）が最新で、トランスクリプト破損からの復旧と autopilot の意図しない継続を直している
- **AI Scan が CodeQL 既定セットアップ不要になった**: GitHub がプルリクエスト向け AI Scan を CodeQL 既定セットアップから独立させ、リポジトリ／組織／エンタープライズのいずれかでコードスキャンと AI Scan が有効なら対象リポジトリ全体で動くようにした（9/16）。⚠️ 提供状態は **public preview** で、対象は GitHub Advanced Security の契約者に限られる。GitHub Enterprise Server は対象外で、権限階層にも変更はない
- **github.blog の Copilot ラベル**: 9/15 の custom properties 提案が最上位で、9/16 の新規はない。Copilot が repository のカスタムプロパティ定義時に許可値を提案する機能で、Business と Enterprise のパブリックプレビューである
- **Cursor は7日間新規なし**: changelog は 9/10 の Projects が最上位のままで、フォーラム Announcements も 9/2 から15日動いていない。⚠️ **Cursor は GPT-6 Astra の提供開始を告知しないまま14日目**である（9/3 GA）。11/12 の OpenAI による供給停止予定と併せて読む必要がある
- **Grok 4.7 は公開予定日を5日超過**: xAI は公開予定日 9/12 を過ぎても Grok 4.7 を公開していない。Musk は 9/11 に「あと数日必要」と述べ、報酬設計が応答長を過度に罰したと説明したが、新しい日程は示されていない。⚠️ 2.1兆パラメータと SpaceX 社内データの利用はいずれも Musk の X 投稿が出所で、xAI 一次では未確認である。公式提供中の最新は **Grok 4.6**（8/12・context 50万トークン・$2/$6）。Devin は一次・代替一次のいずれからも読めない状態が続く

### MCP / オープンウェイト

- **MCP 仕様は26日間動かず、実装側だけ進む**: `blog.modelcontextprotocol.io` は 8/22 の「The New MCP Roadmap」が最上位のままである。⚠️ 一方で本日の Gemini in Workspace の外部コネクター7件は MCP 経由の接続で、仕様の停滞と採用の進行が分かれている。WebMCP Challenge は提出締切を過ぎ、受賞発表は 9/23・賞金総額は $35,000 である
- **HF の8 org は6日間ゼロ**: `Qwen` / `moonshotai` / `deepseek-ai` / `meta-models` / `mistralai` / `zai-org` / `openai` / `google` のいずれにも 9/12〜9/16 に作成または更新されたリポジトリが1件もない。`createdAt` 降順と `lastModified` 降順の両方で確認しており、⚠️ 9/11 以降の空白が前日の5日間から1日伸びた

### 市場データ / 企業構造・GTM

- **Accenture と Google Cloud が Gemini Enterprise 専任組織を設立**: 両社が 9/8 に Accenture Gemini Enterprise Business Group の発足を発表し、**フォワードデプロイドエンジニア 1,000人規模**の体制を新設する。定量成果として示されたのは YouTube の事例で、NFL Sunday Ticket の需要急増時に Gemini Enterprise エージェントを投入し **顧客感情 +11%・平均処理時間 −37%** を得たとされる。大手 SI が単一ベンダーの AI プラットフォーム専任組織を千人規模で立てた事例として、提案での体制比較に使える
- **Anthropic の S-1 は一次でも機密提出のまま**: 一次告知ページの記載は「Form S-1 の草案を SEC に機密提出した」（6/1）に留まり、**上場先・株数・価格・日程のいずれも書かれていない**。⚠️ 二次では Nasdaq・10月上場目標・調達額 $600億超が流通しているが、これらは FT 系の報道であって一次の記載ではない。二次で新たに現れた数値は Series H $650億調達・ポストマネー評価額 $9,650億と、年換算売上の 2025年末 約$90億 → 5月 約$470億 → 7月末 $650億超という推移である
- **Google の Opus 5 全エンジニア開放に一次の追認はない**: 9/15 の報道（初出 09-16）は Business Insider 発の二次が引かれ続けている状態で、Google・Anthropic のどちらからも公式発表が出ていない。Anthropic のコンピュート契約 $517B・14.8GW（The Information）も一次未読で、⚠️ **$517B は確定支出ではなく上限枠**である（オプション・LOI・フレームワーク合意を含む）
- **定点の市場データに新規公表なし**: IDC / MM総研 / NRC / Similarweb のいずれにも新規公表がない。Similarweb 8月分は ChatGPT 55.5%・Gemini 25.6%・Claude 9.3%・DeepSeek 3.4%・Grok 2.4%・Copilot 1.6% で、12カ月前比では Claude 約5倍・Gemini 約2倍になる。⚠️ IDC Japan の「2026年 国内AIインフラ投資は8,000億円超」という新しい見出しは検索面に出ているが、`www.idc.com` のゲートウェイ拒否により本文も公表日も確認できないため数値は採録していない
- **Apple が EU 向けの App Tracking Transparency を変更する**: Apple が一部の国で代替のシステムプロンプトを選べるようにすると告知した（9/16）。⚠️ AI 関連の独立エントリは 6/11 の ImageCreator クラス廃止告知のままで3ヶ月動いていない

## 直近の注目予定

- **9/18**: 新 iPhone と AirPods 5 の発売
- **9/21**: Anthropic ウェルビーイング研究助成の応募締切 ／ 週次復旧チェック（月曜）
- **9/23**: WebMCP Challenge の受賞発表 ／ Partnering for Success Together 第1回
- **9/24**: OpenAI の Videos API と Sora 2 系が退役（代替モデルの提示なし）
- **9/28**: Copilot のチャット3面統合 ／ code review の既定 effort が Lite → Balanced ／ **OpenAI の `gpt-3.5-turbo-instruct` / `babbage-002` / `davinci-002` / `gpt-3.5-turbo-1106` が停止**
- **9/29**: **OpenAI DevDay 本体**（サンフランシスコ Fort Mason・基調講演はライブ配信）
- **9/30**: **M365 E7 プロモ最終日** ／ E5・E3 の CSP 割引終了 ／ Gemini の旧 `gemini-omni-flash-preview` 廃止 ／ OpenAI の現行 OneGov 契約（$1/年）が失効
- **9 月末**: Claude for Financial Advisors の利用クレジットの期限 ／ Copilot Studio のコスト可視化3件が GA 期日 ／ macOS 27 GA
- **10/1**: **OpenAI の `gpt-5.4-cyber` が API から削除**（移行先 `gpt-5.6-cyber`） ／ **Microsoft 365 G7 の GA** ／ Microsoft CSP ソフトウェア価格改定が発効 ／ Copilot Business・Enterprise の既存顧客が前払い必須に ／ Apple の EU 向け新ビジネス条件が発効
- **10/2**: **GitHub Copilot が Gemini 3.5 Flash / Gemini 3.6 Flash / Kimi K2.7 Code / Claude Opus 4.7 を全体験から廃止**
- **10/5**: `gpt-rosalind-research` の課金が開始 ／ Anthropic ウェルビーイング研究助成の full proposal 提出期限
- **10/13**: **Office LTSC 2021・Project LTSC 2021・Visio LTSC 2021 のサポート終了**（ハイライト参照）
- **10/14**: **OpenAI の `gpt-5.5` が ChatGPT / ChatGPT Work / Codex から退役**（API は対象外・ハイライト参照）
- **10/16–11/11**: OpenAI DevDay Exchange 8都市（東京は 10/20）
- **10/23**: OpenAI のレガシースナップショット退役（`gpt-3.5-turbo-0125` / `gpt-4-0613` / `o1-2024-12-17` 等）
- **10/26 頃**: Microsoft AI の MAI モデル行動規範に対する公開協議が終了
- **10/27〜29**: PPCC 2026
- **10/31**: OpenAI の既存 evals が読み取り専用になる
- **10 月**: Anthropic の IPO 観測（$2兆超の評価額を目標と報道・**上場日は未確定**）
- **11/2**: **M365 Copilot Business の従量課金が既定オン**（$10/ユーザー/月の枠つき・ハイライト参照）
- **11/12**: OpenAI が Cursor へのモデル供給を停止する予定日（一次未読）
- **11/15**: Microsoft Release Planner が退役（Release Plans は Learn でアーカイブ）
- **11/21**: GPT-5.6 Sol の暫定値下げが有効とされる期限
- **11/30**: OpenAI の Reusable prompts・Evals プラットフォーム・Agent Builder が停止
- **12/1**: OpenAI の GPT Image 系が停止（→ `gpt-image-2`）
- **12/2**: EU AI Act の生成コンテンツ標識義務、8/2 以前に市場投入済みシステムへの猶予が終了
- **12/11**: OpenAI の旧スナップショット退役（`gpt-5-2025-08-07` / `o3-2025-04-16` 等）
- **12/31**: **Gemini 3.8 Flash と 3.7 Flash の導入価格が終了**（$0.75/$3.75 → $1.50/$7.50） ／ GitHub Copilot の Fable 5.1 / Fable 5 に対する ZDR 暫定免除が終了
- **Q4 CY2026**: **Graph PowerShell v3.0.0**（Windows PowerShell 5.x のサポートなし）
- **年内**: Anthropic の新データ保持方式の投入予定 ／ Claude Docs / Claude Slides の Team・Free への展開 ／ Claude for Small Business の連携パートナーウェビナー14社
- **2027-01-06 / 01-20**: OpenAI のファインチューニングジョブ作成停止 ／ audio・realtime 系の退役
- **2027-02-26**: OpenAI の文字起こし4モデル退役（`whisper-1` 等）
- **2027-03-31**: Azure ポータルの Microsoft Sentinel 体験が退役
- **2027-04**: Apple の最小 SDK 要件が iOS 27 世代へ上がる
- **2027-06-30**: Claude for Teachers の学区登録期限
- **2028-03**: OpenAI が「automated AI researcher」の実現目標とする時期

## 改善メモ

- 新規提案 3件: **B-074**（Master）Copilot CLI Releases 項の注目点に「安定版本文の破壊的変更（フラグ削除・JSON 出力形状）」を明示 ／ **B-070**（Copilot）M365 Blog 本体と Microsoft Copilot Blog の登録 RSS 2本が 301 恒久リダイレクトのため `daily-sources.md` の URL 差し替えを起票 ／ **B-037**（industry）M365 Copilot の使用量課金ドキュメントを料金定点ソースに追加
- 継続提案: Master 16件（最多 B-024 取りこぼし検出・43回目）／ Copilot 27件（最多 B-005 Qiita フィードの WebSearch 恒久化・55回目）／ industry 5件（最多 B-004 取得方法欄の WebSearch 化・80回目）
- 障害の変化: 3ソースとも新規発生・復旧なし（industry は `www.idc.com` の EGRESS_BLOCKED を再確認し台帳の最終確認日のみ更新）
- ソース間の重複・矛盾: 従量課金の**対象体験の一覧が一次と告知で食い違う**（Copilot 側は Cowork / Work IQ API / GitHub Copilot ハーネスの3つ、industry 側は Learn ページが Cowork / Cowork 製アプリ / Work IQ API で GitHub Copilot ハーネスを含まないと指摘）。本サマリーは両論併記とした。Claude Code `2.1.273` は Master が changelog 掲載、industry がハイライトとして扱ったが内容の矛盾はなく、統制修正の詳細が厚い industry 側をベースに統合した
