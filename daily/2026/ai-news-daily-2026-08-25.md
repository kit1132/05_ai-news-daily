# AI News Daily Summary — 2026-08-25

火曜は、エージェントを動かす土台の側に穴が見つかった日である。Check Point が主要なエージェント基盤6種に11件の脆弱性を Black Hat で公表していたことが本日判明し、IBM の Langflow の未認証 RCE が CISA KEV に収録済みであることも分かった。攻める側だけでなく守る側の供給も動き、Anthropic は Mythos 5 を防御側ベンダーの製品へ載せる経路を4本に広げ $35M のオープンソース基金を付けている。Copilot 側では Copilot Credits の容量管理を書いた一次を本日はじめて確認し、クレジット枯渇時の挙動が管理者の選択であると分かった。明日 8/26 は OpenAI Assistants API の停止日で、撤回・延期の告知は出ていない。

## 今日のハイライト

### 1. エージェント基盤6種に11件の脆弱性が公表されていた — 守る対象がモデルへの入力からオーケストレーション層の実装へ移る

**要点**: Check Point が LangChain・CrewAI など主要なエージェント基盤6種に11件の脆弱性を Black Hat USA 2026（8/5）で公表していたことが本日判明した。基盤の選定基準が「プロンプトインジェクション対策の有無」から実装品質そのものへ移る。

**詳細**: 研究者 Yarden Porat と Shahar Tal が1年間の調査結果として講演「No Tools Required」で公表した。対象は **LangChain**・LangGraph・**CrewAI**・AutoGen・Microsoft Agent Framework・Google ADK の6種で、いずれもエンタープライズのエージェント内製で使われる層にあたる。脆弱性の種別は安全でないデシリアライズ・SSRF・パストラバーサル・use-after-free で、プロンプトの書き方とは無関係な古典的バグ類型である。中核の指摘は、攻撃者が制御した内容が信頼された基盤ロジック側へ越境しうる点にある。文書・メール・チャットに仕込まれた内容がモデルを騙すにとどまらず、オーケストレーション・メモリ・状態・システム指示に到達する。

- Microsoft Agent Framework: プロンプトインジェクションを起点にリモートコード実行へ至る Critical 判定の不具合
- Google ADK: 既定のクラウド構成で未認証のコード実行と資格情報の窃取が成立する
- 安全でないデシリアライズ: エージェントが信頼できないチェックポイントデータを読み込み、コード実行に至る

⚠️ **CVE 番号・修正版数・各ベンダーの対応状況は確定できていない。** 一次の `research.checkpoint.com` は 8/8 からゲートウェイ拒否が続き、本日は `blog.checkpoint.com` と `www.theregister.com` も拒否されたため、本項は複数の二次スニペットの一致で構成した。同じ Black Hat 週の Check Point 研究2件（Claude Code の Hooks を悪用する `CVE-2025-59536` ほか、Cloudflare `workerd` の5件）は 08-08 に収録済みで、本件は第3の発表にあたる。20日遅れの捕捉である。

- https://www.theregister.com/security/2026/08/05/prompt-injection-isnt-the-bug-ai-agent-frameworks-are/5283585
- https://blog.checkpoint.com/research/black-hat-2026-check-point-research-takes-the-stage

### 2. Anthropic が Mythos 5 を防御側ベンダーの製品へ出し始めた — 調達先が「Claude を契約する」から「使っている製品に載ってくる」へ動く

**要点**: Mythos 5 を防御側へ届ける経路が4本あり **$35M** の基金が付くことを、8/21 の一次を本日はじめて読んで確認した。08-22 に載せた Claude Security のスキャン切り替えは、この4本のうち1本でしかなかった。

**詳細**: 発表は「Mythos 5 の cyber 能力を防御側に届ける経路を4本に増やす」という構成になっており、既報はそのうち1本だけだった。

- パートナー製品への組み込み: セキュリティベンダーが自社製品に Mythos 5 を埋め込む。利用者が受け取るのはパッチやアラートといった出力であって、モデルそのものへのアクセスではない。関心表明フォームが開いており、統合の詳細と料金は未公表である
- **Defender Advantage Fund**（0xDAF）: オープンソースの脆弱性対応に $35M 相当のクレジットを配る。用途は3方向で、広く使われている OSS の実稼働中の脆弱性を塞ぐこと、スキャンとパッチ適用を自動化して他プロジェクトへ横展開できる形にすること、攻撃手法のクラスごと無効化する設計を試すことにあたる。パイロット助成が先行し、応募条件と期限は「数週間内」に示すとされる
- Cyber Verification Program の拡大: 審査済みの防御側に対し、Opus / Sonnet で dual-use 能力の開放幅を広げる。Mythos クラスの提供はその後に続くとされ、日付は示されていない
- Claude Security のスキャンが Mythos 5 で動く（Enterprise の public beta・追加契約なし・通常のトークン課金）。この1本のみ 08-22 に報告済みである

⚠️ 08-22 のセッションは一覧でこの記事の存在を掴んでいたが、slug 推測が 404 になった後 WebSearch のスニペットで本文を代替し、隣接記事の内容で1項目を立てて終えていた。「一次に到達できずスニペットで書いた項目」を後日読み直す仕組みが無いため、Master が B-044 を起票している。

- https://claude.com/blog/bringing-claude-mythos-5-to-more-defenders
- https://www.securityweek.com/anthropic-expands-mythos-5-access-to-more-defenders-unveils-35m-open-source-fund/

### 3. Copilot Credits の枯渇時の挙動は管理者が事前に選べる — クレジット切れ＝即停止という前提が、決めておく設定に変わる

**要点**: 管理者が Copilot Credits の超過分を「テナントの空き容量から引く」か「従量課金プランに回す」かで選べると、PPAC の一次で本日はじめて確認した。枯渇したら止まるという前提が、事前に決めておく設定の問題へ変わる。

**詳細**: Power Platform 管理センターの `manage-copilot-studio-copilot-credits-capacity`（`ms.date` 2026-08-14 / `updated_at` 2026-08-19T01:04Z）を一次取得した。⚠️ 本ページは 02 の `daily-sources.md` 未登録で、全 digest を grep したところ掲載歴がゼロだった（B-045 起票）。ここにしかない運用情報は次のとおりである。

- 管理面の範囲: PPAC は Copilot chat / 標準 / GitHub Copilot の3ハーネス横断の統一キャパシティ管理面として位置づけられ、エージェント単位と環境単位の消費を同じ画面で見る
- Overage management: 割当容量を超えたとき、テナントに残る空き容量から引くか、紐付けた従量課金プランに超過分を課金するかを選択する
- Manage Agents の月次上限に付くガードレールは通知とハードストップの2つで、通知は環境とテナント両方の管理者へ上限接近時に届き、ハードストップは上限到達でエージェントを自動的にオフにする。状態表示は Nearing limit / Over limit / Within limit の3種である
- 消費データの粒度: 当月の月初来と直近2か月ぶんが日次、過去12か月ぶんが月次で、環境単位の日次は最大3か月である
- エージェントフロー: 前払い容量が尽きると新規実行だけがブロックされ、親エージェントは非フロー対話を続ける。メーカーには設計時に警告が出る

⚠️ 同ページの FAQ は「Copilot credit はユーザーとエージェントの1回のやり取り＝1単位」と定義しており、`requirements-messages-management` の消費レート表（生成回答 2 / エージェントアクション 5 / テナントグラフグラウンディング 10 等）と粒度が食い違う。見積もりに使えるのはレート表のほうである。⚠️ USD 単価は本日も Learn 側に存在しない。

- https://learn.microsoft.com/en-us/power-platform/admin/manage-copilot-studio-copilot-credits-capacity
- https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-experience/billing-credit-overview

## カテゴリ別まとめ

### AIセキュリティ / エージェント統制

- **Langflow の未認証 RCE が CISA KEV に収録済みと判明した。** IBM が保守するローコードのエージェント構築基盤 Langflow に、未認証の攻撃者が既定構成でリモートコード実行に至る `CVE-2026-9198`（**CVSS 9.8**）が存在する。CISA は 8/4 に Known Exploited Vulnerabilities カタログへ追加し、実際の悪用を確認したとしている（https://thehackernews.com/2026/08/cisa-flags-langflow-rce-tomcat-and-n.html ）
  - 影響範囲と修正: 影響は 1.0.0〜1.10.0 で、修正は **1.10.1**。IBM は 7/17 に公表と同日修正を出している
  - 経路: `/api/v1/auto_login` が認証を強制せずループバックにも束縛されていないため、ネットワーク越しの任意の呼び出し元へ SUPERUSER トークンを発行してしまう
  - ⚠️ 悪用試行の規模（7/6 以降 650件・244 IP・41カ国）は KEVIntel 由来の二次値で一次未確認である
  - Langflow は GitHub Trending の常連（08-03 に星14.6万として収録）で、社内 PoC 環境が公開エンドポイントのまま放置されていないかの確認対象にあたる。2025年の `CVE-2025-3248` に続く2件目の KEV 収録で、21日遅れの捕捉である
- ハイライト1のエージェント基盤6種11件とあわせ、本日の2件はいずれも「モデルの外側の実装」に起因する。プロンプト対策の有無ではなく、基盤のバージョンと公開範囲を点検する対象になる

### Anthropic / Claude

- Mythos 5 の防御側展開と $35M の Defender Advantage Fund はハイライト2を参照
- Claude Code の changelog は **v2.1.241（8/23）が最上位のまま**で、8/24 付けの新規リリースはない。npm の `dist-tags` も `{stable: 2.1.231, latest: 2.1.241, next: 2.1.241}` で前日から変化がなく、`2.1.241` の公開は 8/22 23:58 UTC のため約2日半にわたって新版が出ていない。`latest` と `next` の一致は3日続いている
- `stable`（2.1.231）と `latest`（2.1.241）の差は10版のまま縮んでいない。`stable` チャネルを使っている場合、8/21 の v2.1.239 に入った約65項目（コスト表示への US-only-inference 1.1倍反映、Bedrock ストリーミングの二重課金修正など）はまだ届いていない
- Claude Platform API のリリースノートは 8/20 の Python SDK v1.0 が最上位のままで5日間新規がなく、`support.claude.com` の Release Notes も 8/6 の skill / plugin セキュリティスキャン beta のままで19日間動きがない
- **Anthropic の社内マーケターが Claude Code で営業向け週次配信を自動化した事例が公開された**（8/24）。BigQuery を情報源に HubSpot・Clay・Salesforce のデータを束ね、担当地域と担当口座に応じて内容を変えた Slack メッセージを毎週月曜に配信する。構成は Claude Code と MCP で、プロンプトは GitHub でバージョン管理する。初期は営業担当10名で試し、その後 営業・事業開発・カスタマーサクセス・アライアンスへ広げた。効果として挙がるのは日曜夜のスライド作成が不要になったことと、経営層向け会食の申込が1週間で倍増した事例である。⚠️ **工数削減の絶対値も ROI も記事に無い**ため、非エンジニアがエージェントを組む実在例としては使えるが定量根拠には使えない（https://claude.com/blog/how-an-anthropic-field-marketer-uses-claude-code-to-send-weekly-personalized-updates-to-every-sales-rep ）
- 8/24 付けの Anthropic 公式アナウンスは検出できなかった。`www.anthropic.com` のオリジン403が継続しているため、規定5本に日付入りの検索を加えて実行したが新規は0件だった
- Claude Tag の「会話全体を見て発言する」変更を VentureBeat が 8/24 に報じたが、機能そのものは 8/13 提供開始分で 08-16 に収録済みであり、新しい事実は確認できなかった
- 既報の期限: Claude Code の週次上限50%増は **8/31 まで**（5/13 開始・3度目の延長。Pro / Max / Team とシート課金の Enterprise が対象）

### GitHub Copilot / 開発ツール

- **Copilot CLI がモデル選択の画面でデータ保持の条件を出すようになった。** GitHub が 8/24 に pre-release **v1.0.81-9** を公開し、`/model` ピッカーにモデルごとのデータ保持警告とリンクを表示するよう変えた。どのモデルが自社の保持要件に合うかを、別途ドキュメントを引かずに選択の場で判断できる（https://github.com/github/copilot-cli/releases/tag/v1.0.81-9 ）
  - 本版の変更はこの1項目のみで、8/21 の v1.0.81-7 が入れた「`models.list` にモデル単位のサービス公開情報と警告メッセージを含める」の続きにあたる。API 側に出した情報を対話 UI へ回した形になる
  - Copilot CLI は Grok 4.6・Gemini 3.7 Flash・Fable 5 など提供元の異なるモデルを1つのピッカーに並べており、保持条件は提供元ごとに違う。組織で使う場合はここが選択の制約になる
  - 安定版は **v1.0.80（8/14）のまま11日間据え置き**で、8/19 以降の -5 から -9 までの5版はすべて pre-release 側の変更である
- **OpenAI が Codex CLI の安定版 `rust-v0.149.1` を公開した**（8/24 00:28 UTC）。0.149.0（8/20）以来4日ぶりの安定版で、リリース本文は比較リンク1行のみのため差分から内容を確定した
  - `--thread-source`: 新規スレッドとフォークしたスレッドに呼び出し元の分類を伝播させるグローバルオプションが追加された（既定値は `user`）
  - リモート compaction で保持する画像のサイズを見積もって予算に算入するようになり、画像の多い履歴が意図した context 予算を超える問題が塞がれた
  - detached な memory 要求のスレッド種別が `memory_consolidation` として記録されるようになった
- `github.blog/changelog` の Copilot ラベルは 8/21 の Slack / Microsoft Teams 連携2本が最上位のままで、8/22〜8/24 の追加はない
- Cursor の changelog は 8/19 の Cloud Agents / Cursor Harness 更新が最上位のままで、フォーラムの Announcements も 8/17 の Origin Code Hosting のまま8日間動いていない。xAI / Grok と Devin も新規発表を検出できず、一次ホスト（`x.ai` / `docs.x.ai` / `grok.com` / `docs.devin.ai`）への到達不可が続いている
- `blog.modelcontextprotocol.io` は 8/22 の「The New MCP Roadmap」が最上位のままで新規はない
- ⚠️ **A2A（Agent2Agent）が Agentic AI Foundation へ入ったとする報道は確定できない。** 二次の一方は「8/19〜8/20 に Google の A2A が Linux Foundation 傘下の AAIF へ正式参加し、MCP と同じ中立ガバナンス下に入った」と報じ、他方は「A2A は AAIF 傘下ではなく別の LF プロジェクトのままで、今回は連携強化にすぎない」と正面から矛盾する。一次（`aaif.io` / `www.linuxfoundation.org` / `developers.googleblog.com`）はいずれも本日ゲートウェイ拒否で、MCP 側の一次も A2A に言及していないため、どちらか一方を採らず未確定として記載する
- ⚠️ `devblogs.microsoft.com/commandline` は 8/10 の Intelligent Terminal 0.2 が最上位のままで、本日も WebFetch 200 だが登録ソースには入っていない
- 期限: Copilot の既定モデル有効化ポリシー発効（**8/26＝明日**）、GitHub Spark の既存ユーザーアクセス終了（8/31）、モデル廃止（9/1）、MAI-Code-1-Flash の廃止（9/10）

### Microsoft 365 Copilot / Copilot Studio

- **Copilot Success Planner が無償で公開された。** Microsoft が 8/24 に Partner Center の8月アナウンスへ追記し、Copilot in 30 トライアル（25ユーザー×30日・従業員300人未満対象・2026年12月31日まで）向けの学習プラン生成ツールを出した。スポンサーが業種・優先課題・働き方を短い誘導形式で答えると、参加25名それぞれの30日プランとスポンサー用ロードマップが生成される（https://learn.microsoft.com/en-us/partner-center/announcements/2026-august ）
  - 週割り: 第1週が Outlook、第2週が Teams と会議、第3週が Word・Excel・PowerPoint、第4週がエージェントで、Cowork を有効のままにすると第3・4週に Cowork のプロンプトが加わる
  - 各アクションには使うアプリ名・コピーして使える推奨プロンプト・該当するサポート記事へのリンクが付く
  - スポンサー向けロードマップは事前設定・週次チェックポイント・試用後の経営層向け価値サマリーで構成される
  - **無償かつサインイン不要**のため、体験版を商談として成立させる前に共有できる。⚠️ 定着率・転換率の実績値は告知に無い
- M365 Copilot の Release Notes は「August 11, 2026」が最新セクションのままで、⚠️ **隔週傾向から「8/25 前後」と見込んでいた次バッチは本日時点で出ていない**。対象期間 7/28〜8/11・節構成7本・全12項目は 8/24 と一致している
- Copilot Studio の Released Versions は本日が定例更新日（火曜）にあたるが、新ビルドは出なかった。Build は 2026.6.3（6/30 初出）のままで、空白が**8週間**に達し定例日を8回またいだ
- Copilot Studio の What's New は July 2026 節が最新のままで8月節は作成されていない。⚠️ June 節の GitHub Copilot ハーネスは本日も `(Production-ready preview)` と書かれており、GA（8/3）から**22日連続**で反映されていない
- ⚠️ **Copilot Tuning の一次は停止を一文も書いていない。** 停止の発効（8/20）から5日たっても `copilot-tuning-overview` は停止も退役も書いておらず、Optimization エージェントは現行機能として載ったままである。本日は同ページの `updated_at` が 2026-08-18T17:48Z で、停止2日前のビルドに乗りながら停止の記載だけが入らなかったことが確認された
- ⚠️ 8/23 に Roadmap 側で検知した **569612**（Copilot メモリの Purview 保持・GA 2026年9月）は、本日も Purview の What's new に現れていない。Purview の8月節は Sensitivity labels の2件のままで Copilot 固有の項目はない
- Message Center は本日新たに索引へ現れた MC がない。⚠️ `mc.merill.net` が18日連続 `EGRESS_BLOCKED` のため、到達手段は WebSearch の索引スニペットだけである
- **Dragon Copilot に第三者アプリとエージェントの出品枠ができた。** Microsoft が 8/20 に告知し、医療ソフトウェア事業者が専用の出品タイプで AI アプリ・エージェントを公開し、臨床医の使う Dragon Copilot の画面内へ直接組み込めるようになった。対象は米国のパートナーで、発見・調達・履行は Microsoft Marketplace の既存基盤に乗る。⚠️ 収益配分・出品審査の条件は告知に無い。5日遅れの捕捉である
- ⚠️ 英語圏の「8月の新機能8件」系の二次記事が挙げる Excel のテーマデザインスキル・Excel の Power BI グラウンディング・Cowork のワークフロータブは、Release Notes の全バッチを検索しても存在しなかった（6例目の空振り）

### Power Platform / ガバナンス

- Copilot Credits の容量管理と Overage management はハイライト3を参照
- `billing-credit-overview` と `billing-manage-buy-credits` の `updated_at` が 2026-08-03T14:59Z → **2026-08-24T19:07Z** へ動いたが、本文は 2026-08-04 に掲載した内容（従量課金メーターと1年前払いの CCCU プールの2経路）と一致し、新しい記述は確認できなかった
- Release Wave の3ページ（`power-automate` / `power-apps` / ガバナンス・管理）は 8/24 と完全に同一で、緑チェックの追加・期日変更・行の増減はいずれも発生していない
  - 期日超過は延べ6行のままで、GA 列5件と Public preview 列1件の内訳も変わらない
  - 8月に期日がある行は10件（Power Automate 6件 / Power Apps 4件）、9月は6件で据え置きである。2026 Wave 1 の対象期間は9月末までで残りは約1か月になる
  - ⚠️ ガバナンス側の PPAC Usage ページは GA 期日が今月なのに、残り6日になっても緑チェックが付いていない
- ⚠️ **Release Communications API が全クエリで空応答を返すようになった。** `releasecommunications/api/v2/m365/features` は HTTP 204・本文0バイトで、8/24 に13件を返した製品フィルターも同じ応答になる。ゲートウェイ拒否ではなくオリジン応答であり、Feature ID 単位の状態確認ができない。今月が GA 期日の **566997**（メーカー資格情報の使用ブロック）の進捗は本日確認できていない
- Power Platform / Power Automate / Power Apps の3ブログとも新規記事はない。月次記事は 8/6 の July/August 合併号が最新のままで、親ページの一覧に合併号が現れない不完全レンダリングも続いている
- Partner Center の8月アナウンスは 15件 → **17件**に増えた。1件は Copilot Success Planner で、もう1件「Drive more marketing ROI in FY27」は FY27 の co-op 資金ガイダンスの案内で Copilot 固有の変更を含まない

### OpenAI

- **OpenAI Assistants API の停止が明日に迫っている。** 期限1日前に一次ドキュメントで再確認し、撤回・延期の告知がないことを確かめた。`/v1/assistants` `/v1/threads` `/v1/threads/runs` は 8/26 に縮退運転も猶予期間もなくエラーを返し、Threads → Conversations の自動移行ツールは提供されない。代替は Responses API と Conversations API の組み合わせになる（退役カレンダー全体は 08-24 のハイライト参照）（https://developers.openai.com/api/docs/deprecations ）
- **同じ退役ページに 12/1 の期限が新たに確認できた。** GPT Image 系（`gpt-image-1-mini` / `gpt-image-1.5`）が停止する。08-24 に一覧化した他の期限（9/24 Videos API・Sora 2 系、10/23 旧 GPT スナップショット、11/30 Evals / Agent Builder / `v1/prompts`、12/11 `gpt-5-2025-08-07` と o3 系、2027/1/20 旧 audio / realtime 系）はいずれも変更がない
- GPT-5.6 Sol の値下げ単価は一次で据え置きを確認した。入力 $4 / 出力 $20 が料金ページに載ったまま変わらず、長文脈側（入力 272K トークン超）の $8 / $30、キャッシュ入力 $0.40、Terra $2 / $12、Luna $0.20 / $1.20 も不変で、期限の記載も「少なくとも 2026年11月21日まで」のままである（https://developers.openai.com/api/docs/pricing ）
- `developers.openai.com/api/docs/changelog` は 8/21 の2件が最上位のままで 8/22〜8/24 の追加はなく、`community.openai.com` の Announcements RSS も 8/21 の Sol 値下げ告知が最上位である
- ChatGPT / Codex changelog の8月分として **Computer History**（macOS で許可したアプリ・サイトの操作を検索可能なタイムラインと memory に変換し、ChatGPT と Codex から参照できる）と Linux 版デスクトップアプリの preview が挙がるが、いずれも 8/22 以降の新着ではなく、Computer History は 8/13 に Chronicle の後継として出たものである。⚠️ 対象は米国の Pro / Business / Enterprise の macOS 利用者に限られ、EEA・スイス・英国は初期提供の対象外になる。既定はオフで、スクリーンショット・画面録画・音声は取らずクリック / 入力 / ショートカット / アプリ切替のイベントを記録する
- ⚠️ 二次検索が「OpenAI DevDay 2026 は 9/29 サンフランシスコ」と返すが、登録済み一次が扱っているのは DevDay Exchange の8都市開催（10/16–11/11・東京 10/20）であり、別イベントか誤記かが未確定のため注目予定には本体側を追加しない

### Google / モデル・オープンウェイト

- Gemini API の changelog は **8/13 の Gemini 3.7 Flash GA が最上位のまま**で、12日間動きがない。料金ページの最終更新も 8/13 のままで、3.7 Flash / 3.6 Flash はいずれも入力 $0.75・出力 $3.75（2026年12月31日まで）、2027/1/1 から $1.50 / $7.50 へ戻る記載も不変である（https://ai.google.dev/gemini-api/docs/pricing ）
- 8/24 付けの Google の AI 発表は検出できなかった。直近は 8/12 の Made by Google（Pixel 11 / Gemini 機能）で、8/26 ロールアウト開始予定の Ask Gemini in Chat も既報から進展がない。`gemini-robotics-er-1.6-preview` の 8/31 停止と Gemini 3.5 Pro の GA 未ローンチ（3回スリップ）も続いている
- 8/24〜8/25 に新規公開されたオープンウェイト LLM はない。8 org で作成日降順の一覧を実行したが、8/13 の `Qwen/Qwen3.8-27B-FP8` と `deepseek-ai/DeepSeek-V4-Pro-0813` より新しいものが1件もなかった
- 実測（8/25）: `Qwen/Qwen3.8-27B` は DL **2,645,226** / likes 12,480（前日 2,358,347）で1日28.7万 DL 増と伸びが続く。`DeepSeek-V4-Pro-0813` は DL 63,058 / likes 745（前日 57,928）で、`DeepSeek-V4-Flash-0731` の DL 3,274,129 は V4-Pro の約52倍という開きが続いている
- ⚠️ 二次のモデル追跡サイトが挙げる 8/17 の `GLM-5.2 Turbo` は、本日も `zai-org` の HF org に該当する重みが存在しない（最新は 6/16 の GLM-5.2 のまま）。API 限定か誤記かを一次で確定できないため記載しない

### 企業・市場

- **Alibaba が香港市場で $10.2B を調達し AI へ全額投入する。** 8/23 発表で、新株7億1,000万株を1株 HK$112.70 で米国外の投資家へ割り当て、800億香港ドルを調達する。香港上場企業として過去最大の株式売出しにあたり、同社にとって2019年の香港上場以来はじめての増資になる。調達額の全額をフルスタックの AI 能力（AI インフラの拡張と強化を含む）へ投じるとしている。機関投資家の需要は募集額の約3倍に達した一方、株価は 8/24 に **8.5%下落**し2025年初頭以来の下げ幅となった（https://asia.nikkei.com/business/technology/alibaba-to-raise-10bn-via-new-hong-kong-shares-to-fund-ai-investments ）
- **Nvidia が Perplexity へ $30B 超の評価で出資を協議していると報じられた。** 8/23 に The Information が報じ Reuters が追随した。数十億ドル規模のラウンドに Nvidia が出資候補として加わっており、成立すれば1年前の約 $20B から50%超の切り上がりになる。Perplexity の年換算売上は年初の $250M 未満から $750M 超へ伸び、伸びの一因はクラウド型エージェント Perplexity Computer にあるとされる。⚠️ **交渉段階の報道で両社とも確認していない**（https://www.investing.com/news/stock-market-news/nvidia-discusses-perplexity-investment-at-30-billionplus-valuation-the-information-reports-4872594 ）
- **Nvidia の FY27 Q2 決算が明日 8/26 に出る。** 対象四半期は 2026年7月27日締めで、会社ガイダンスは約 $91.0B、市場予想は $93B〜$95B（前年同期比約96%増）のレンジにある。FY27 Q1 のデータセンター売上は $752.46億（前四半期比 +21%）だった。AI インフラ投資の減速有無を市場データとして引く際の直近の一次値になる。⚠️ 予想値は二次集計である
- 企業構造・規制の新規の動きは検出できなかった。既報は Anthropic の IPO 規模報道（8/21）と年換算売上 約$650億、下院民主党22名の監督書簡（回答期限は 8/24 で、回答の有無は本日時点で確認できず）、SpaceX による Cursor 買収完了（8/14・$60B）である
- **1組織あたりの稼働エージェントが15カ月で 5体→13体 になった。** Salesforce の Agentic Enterprise Index 第2版による。基礎データは Agentforce 上の数千社の集計利用データ（観測期間 2025年2月〜2026年4月）と 2026年5月実施の 4,689名調査の2本立てで、作成時間は平均53%減、エージェント1体あたりの業務アクションは1年で2種→6種、顧客サービスは有人対応なしで解決するチャットが10件中7件とされる。⚠️ **ベンダー自身の顧客基盤の集計であり市場全体の導入率ではない**ため、IDC・MM総研の市場データと横に並べるときは母集団の違いを明記する必要がある。⚠️ 一次はゲートウェイ拒否で公開日も確定できていない（二次報道は 8/10 付）
- 市場データ定点は IDC / MM総研 / Similarweb / NRC のいずれも新規公表を検知できなかった。参照可能な最新値は国内AI市場予測（2025年 2兆3,725億円 → 2029年 6兆8,897億円・CAGR 36.0%）、個人利用経験率 21.8%、生成AIサイト訪問シェア（ChatGPT 53.9%・Gemini 27.9%・Claude 9.2%）で据え置きである

### Apple / その他

- Apple が 8/24 に「New domain for Sign in with Apple」を公開し、Sign in with Apple の新規アドレスを `privaterelay.appleid.com` から **`private.icloud.com`** へ切り替えると告知した（既存アドレスは継続利用可、iCloud+ の Hide My Email は `icloud.com` のまま）。⚠️ AI 関連ではないが、`developer.apple.com` の最上位が 8/18 から動いたことの記録として残す
- AI 関連の最新は依然 8/5 の App Store creative assets で、20日間新規がない。iOS 27 / iPadOS 27 は developer beta 4（7/20・ビルド 23G71）が最新で、GA は9月（予想 9/14 前後）である
- AWS Bedrock への Anthropic モデル追加は 7/24 の Claude Opus 5 が最新のままで、8月の新規提供開始は検出できなかった

## 直近の注目予定

- **8/26（明日）**: **OpenAI Assistants API 停止** ／ o3 の ChatGPT 退役 ／ GPT-4.5 完全廃止 ／ Copilot 既定モデル有効化ポリシー発効 ／ Ask Gemini in Chat のロールアウト開始 ／ Nvidia FY27 Q2 決算
- **8/27**: IT Nation Connect ANZ の Microsoft セッション ／ 非推奨一覧の週次確認
- **8/30**: 公式 DALL·E GPT の退役 ／ PnP・Power CAT の週次確認
- **8/31**: Claude Code の週次上限50%増が終了 ／ GitHub Spark の既存ユーザーアクセス終了 ／ `gemini-robotics-er-1.6-preview` 停止 ／ Power Automate モバイルアプリの廃止 ／ CSP Copilot Partner Council コンテストの応募期限 ／ GPT-5.4・5.4 mini が Codex から除外 ／ Claude for Government の $1/機関プログラム終了
- **8月末（残り6日）**: Copilot Studio 566997 と PPAC Usage ページの GA 期日 ／ Release Wave の8月期日10件と持ち越し6行 ／ Anthropic が IPO を公開申請する可能性
- **9/1**: GitHub Copilot の全体験でモデル廃止 ／ MAICPP 契約の更新条項が自動発効 ／ OpenAI Daybreak でハードウェアセキュリティキー必須化
- **9/2 / 9/3**: Windows 365 Frontline 名称での購入最終日 ／ Windows 365 Flex へ改称
- **9月**: Outlook と Teams のチャット中心 UI と Work IQ コントロールが既定で有効化 ／ Copilot メモリの Purview 保持（569612）／ Copilot Tuning の新体験が Public Preview ／ iOS 27 / macOS 27 GA ／ Defender Advantage Fund のパイロット助成の詳細公開（「数週間内」）
- **9/10**: MAI-Code-1-Flash が全 Copilot 体験から廃止
- **9/17**: OpenAI DevDay Exchange の応募締切
- **9/24**: OpenAI Videos API と Sora 2 系の全モデルが退役
- **9月末 / 9/30**: 2026 Wave 1 の対象期間終了 ／ M365 E7 プロモーションの対象購入最終日 ／ M365 E5・E3 の CSP 割引終了
- **10/1**: Apple の EU 向け新ビジネス条件が発効 ／ CSP ソフトウェアの5%資本コスト上乗せ発効 ／ M365 E7 プロモーションの新規取引停止
- **10/16–11/11**: OpenAI DevDay Exchange 8都市（**東京は 10/20**）／ **10/20〜22**: SMB Copilot Partner Council イベント（NYC）／ **10/25〜30**: PPCC 2026
- **10/23**: 旧 GPT スナップショットとそのファインチューン版が退役
- **10/31**: OpenAI Evals ダッシュボードが読み取り専用へ
- **10月**: Anthropic の IPO 予定（$2T 超の評価額を目標と報道）
- **11/21**: GPT-5.6 Sol の暫定値下げが有効とされる期限
- **11/30**: OpenAI Evals プラットフォーム・Agent Builder・`v1/prompts` が退役
- **12/1**: OpenAI の GPT Image 系（`gpt-image-1-mini` / `gpt-image-1.5`）が退役
- **12/2**: EU AI Act の生成コンテンツ標識義務の猶予終了
- **12/11**: `gpt-5-2025-08-07` 系と `o3-2025-04-16` / `o3-pro-2025-06-10` が退役
- **12/31**: Gemini 3.7 Flash の導入価格終了（$0.75/$3.75 → $1.50/$7.50）／ Copilot in 30 の提供終了
- **2027/1/20**: OpenAI の旧 audio / realtime / transcription 系が退役

## 改善メモ

- **Master B-044 起票**: 一次に到達できず二次スニペットで書いた項目を「一次未読」として記録し、後日読み直す手順を `fetch-flow.md` に規定する提案である。本日の Mythos 5 の取りこぼし（一覧で存在を掴みながらスニペットで代替し、隣接記事の内容で1項目を立てていた）が根拠にあたる
- **Copilot B-045 起票**: Copilot Credits の容量管理を規定する PPAC の一次（`manage-copilot-studio-copilot-credits-capacity`）が `daily-sources.md` 未登録で、掲載歴がゼロだった
- **一次未確認のまま採用した項目が3件ある**: Check Point のエージェント基盤11件（`research.checkpoint.com` / `blog.checkpoint.com` / `www.theregister.com` がゲートウェイ拒否）、Salesforce の Agentic Enterprise Index（`www.salesforce.com` が拒否・公開日も未確定）、Langflow の悪用試行規模（KEVIntel 由来の二次値）で、いずれも二次一致で採った
- **ソース間の粒度差**: Copilot Success Planner は 02 が「サインイン不要で商談前に配れる」点を、03 が「試用支援が自作資料から既製プログラムへ移る」点を書いており、矛盾ではなく切り口の差とみて統合した。Anthropic の営業向け週次配信の事例も、Master が「製品仕様の変更ではない」と扱い 03 が定量根拠としての限界を明記しており、後者を採って統合した
- **未確定として保留した項目**: A2A / AAIF のガバナンス変更（二次が正面から矛盾し、一次5ホストがいずれもゲートウェイ拒否）、`GLM-5.2 Turbo`（HF org に重みが存在しない）、OpenAI DevDay 2026 の 9/29 開催説（登録済み一次は DevDay Exchange のみを扱う）
- **障害の変化**: Release Communications API（`releasecommunications/api/v2/m365/features`）が全クエリで HTTP 204・本文0バイトを返すようになり、Feature ID 単位の状態確認ができなくなった。ゲートウェイ拒否ではなくオリジン応答である。新規ゲートウェイ拒否は Master 3件（`www.linuxfoundation.org` / `aaif.io` / `developers.googleblog.com`）と industry 8ドメイン（うち `mshibanami.github.io` は `daily-sources.md`「最優先」の GitHub Trending 非公式RSS で、最優先ソースの拒否は7件目）。⚠️ 一方 8/24 にオリジン403だった M365 Blog の RSS は本日 200 に復旧した
- 継続提案は Master 24件（最多: B-013 403の2分類記録・28回目）、Copilot 26件（最多: B-005 Qiita の WebSearch 前提化・35回目）、industry 6件（最多: B-004 取得方法欄の WebSearch 優先化・57回目）
