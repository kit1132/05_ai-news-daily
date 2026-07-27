# AI News Daily Summary — 2026-07-27

> 本サマリーは 01_ai-news-Master・02_ai-news-Copilot・03_ai-news-industry の3ソース（7/27分）を統合して作成。

月曜の実務ネタは「移行した瞬間に落ちる API 変更」と「Microsoft 側のモデル世代交代」。提案資料の側では総務省が令和8年版情報通信白書を公開し、国内の生成AI利用率が1年で倍増した。注目されていた Kimi K3 の重み公開は本日ではなく 7/28 0:00 JST で、前版の「9:00 JST 公開」は誤りだった。

## 今日のハイライト

### 1. Claude API に破壊的変更2件（7/24） — Opus 5 に差し替えた瞬間に 400 で落ちる条件がある

**要点**: Opus 5 は effort `xhigh`／`max` での thinking 無効化が **400 エラー**に。Opus 4.7 の fast mode も同日廃止。

**詳細**: Opus 5 リリースと同じ 7/24 の Platform release notes に、モデル本体以外の実務項目が4件入っていた。破壊的変更は2件。① `thinking: {"type":"disabled"}` を effort `xhigh` / `max` と併用すると 400 が返る。無効化が許されるのは effort `high` 以下で、Opus 4.8 からの挙動変更。effort は low / medium / high / xhigh / max の5段で、Opus 5 の主操作系と位置づけられている。② **Opus 4.7 の fast mode** を廃止。`claude-opus-4-7` に `speed:"fast"` を投げるとエラーになり、Opus 4.6 と違って標準速度へのフォールバックもしない（Opus 4.7 自体は標準速度で継続提供）。beta も2件で、③ 会話途中のツール差し替えが Fable 5 / Mythos 5 / Opus 4.8 / Opus 5 で提供され、プロンプトキャッシュを保持したままターン間でツールを追加・削除できる（`mid-conversation-tool-changes-2026-07-01` ヘッダ）。④ `fallbacks` パラメータに `"default"` モードが追加され、拒否カテゴリ別に推奨フォールバックモデルが自動適用される（`server-side-fallback-2026-07-01` ヘッダ）。

**意味**: 既存の Strands / Bedrock 実装で effort と thinking を両方明示している箇所は、Opus 5 に差し替えた瞬間に落ちる。逆に③は、長いエージェントループの途中でツール構成を切り替えるとキャッシュが飛ぶ問題への直接の回答になる。

- https://platform.claude.com/docs/en/release-notes/api

### 2. Opus 5 が M365 Copilot と Copilot Studio のモデルセレクターに（7/24） — Learn 側はまだ追随していない

**要点**: Microsoft が Opus 5 を Copilot の6サーフェスに投入。Copilot Studio も対象で、外部モデル選択が最新世代に追いついた。

**詳細**: 7/24 の Microsoft 365 Copilot Blog（Tech Community）で告知。対象は Word / Excel / PowerPoint / Copilot Chat / Copilot Cowork / Copilot Studio の6つ。Opus 4.8 比でエージェント型コーディング・専門知識業務・長期推論を改善したとしている。ロールアウトはリージョンとテナント構成で差があり、Copilot Studio で Anthropic モデルを使う場合は Microsoft 365 管理センターでのオプトインが前提になる。learn.microsoft.com 側はまだ追随しておらず、Copilot Studio What's New は6月節のままで GA 表記の最新は Claude Sonnet 5 と GPT-5.5 Chat、M365 Copilot Release Notes の 7/15 バッチにも本件の記載がない。前版の当サマリーは「**Opus 5 は未追加**」としていたが、ブログ一次で覆った。

**意味**: Copilot Studio 案件でのモデル選定は「ブログ告知済み・Learn 未反映」の段階にある。実機のモデルセレクターに出る選択肢は、テナント側で Anthropic モデルのオプトインが済んでいるかどうかで変わる。

- https://techcommunity.microsoft.com/blog/Microsoft365CopilotBlog/available-today-anthropic-claude-opus-5-in-microsoft-365-copilot/4540524
- https://learn.microsoft.com/en-us/microsoft-copilot-studio/whats-new （Learn 側は6月節のまま）

### 3. 令和8年版 情報通信白書が公開 — 国内の生成AI利用率が1年で2倍強に

**要点**: 総務省が 7/24 に令和8年版を公開。個人の生成AI利用率は **58.8%** で、前年調査の 26.7% から倍増した。

**詳細**: 4カ国比較は中国 **93.6%**・米国 68.8%・ドイツ 59.2%・日本 58.8%。日本はドイツにほぼ並ぶ水準まで上がったが依然4カ国中最下位。利用頻度では「ほぼ毎日」が約3割、「ほぼ毎日1時間以上」は1割超にとどまる。特集テーマは「AIの進展がもたらす多面的影響〜人間とAIが健全に協働するデジタル社会の実現に向けて〜」で、個人・企業の利用実態、企業の先進事例、研究動向を扱う。白書は第54版（初版は昭和48年）。

**意味**: これまで提案書で使ってきた令和7年版の「日本 26.7%／米国 68.8%／中国 81.2%」は本日で旧版になった。差し替えが必要。あわせて「日本は使っていない」という導入の枕が使えなくなり、「使ってはいるが浅い」（毎日1時間以上は1割）へ論の立て方を変えられる。

- https://www.soumu.go.jp/menu_news/s-news/01tsushin02_02000184.html
- https://www.soumu.go.jp/johotsusintokei/whitepaper/ja/r08/summary/summary01.pdf
- https://internet.watch.impress.co.jp/docs/news/2127686.html

## カテゴリ別まとめ

### Anthropic / Claude

- Opus 5 の第三者評価が出そろった — Artificial Analysis Intelligence Index で **61** と1位（Fable 5 が60、GPT-5.6 Sol が59）。OSWorld 2.0 は全価格帯で首位、ライフサイエンス系評価も Opus 4.8 超え、ARC-AGI-3 は 30.2%。価格は $5／$25（100万トークン）で Opus 4.8 と同額据え置き、Fable 5（$10／$50）の半額。fast mode は約2.5倍速で2倍価格。Auto Mode 併用時のブラウザ経由プロンプトインジェクションは129シナリオで成功率 **0%**（非併用時 3.7%）。値上げなしの世代交代なので、Opus 4.8 前提の見積りは価格そのままで性能だけ上げられる。 https://the-decoder.com/anthropics-claude-opus-5-costs-well-below-fable-5-while-matching-or-beating-it-across-most-benchmarks/ / https://simonwillison.net/2026/Jul/24/introducing-claude-opus-5/
- Opus 5 のサイバー系ポリシー — ソースコード上の脆弱性発見は許可、バイナリ走査・侵入テスト・エクスプロイト生成はブロック。フラグが立ったリクエストは Claude AI / Claude Code / Cowork で Opus 4.8 に振られる。Anthropic は Opus 5 を意図的にサイバータスクで訓練しておらず、脆弱性の「発見」は Mythos 5 に迫るが「悪用」は大きく劣後する。 https://www.testingcatalog.com/anthropic-launched-claude-opus-5-across-all-platforms/
- Claude Security プラグインが public beta（7/22・catch-up）— Claude Code のターミナルから `/claude-security` で Scan codebase / Scan changes / Suggest patches の3モードを実行。複数エージェントがコードベースのマッピング → 脅威の洗い出し → ファイル横断・業務ロジック横断の関連付け → findings の独立再検証 → 修正パッチ付きレポートと分業する。要件は有料プラン＋**v2.1.154 以降**、`/config` で dynamic workflows 有効化、PATH 上に `python3`（3.9.6+）と Git。組織単位の有効化は `claude.ai/admin-settings/claude-code`。 https://claude.com/product/claude-security
- Claude API の破壊的変更2件＋beta 2件（ハイライト参照）
- LLM トークンの「リレー市場」調査（7/26）— 集めた API キーをプールし正規価格より大幅に安く LLM アクセスを転売する市場の実態調査。原資は無料トライアルの乱用、保護されていないサポートボット経由のプロキシ、盗難クレジットカード。プロキシ基盤には OSS の one-api とフォークの new-api がそのまま使われ、キープール間でロードバランスしている。買い手の動機は安価なトークン・地域制限の回避・蒸留用データの収集。公開エンドポイントを持つ LLM アプリには、金額しきい値で止まる厳密なキャップがベンダー側に要るという指摘。 https://simonwillison.net/2026/Jul/26/relay-market/

### Microsoft / Copilot Studio

- Opus 5 の6サーフェス投入（ハイライト参照）
- Microsoft 365 Admin agent が GA（**MC1436831**・7/22）— 管理センターと Copilot Chat の双方から同一エージェントを呼び、自然言語で M365 サービスの探索・構成・トラブルシュート・ガバナンスを実行できる。対象は Entra の組み込み管理者ロール全般で、既存の RBAC に従い変更を伴う操作には管理者の承認を挟む。利用の制限と監視は管理センター側の設定。顧客テナントに「Copilot が管理操作まで実行する」構成が既定で入ってくるため、ガバナンス設計では実行権限の紐付けと無効化の設定場所が確認事項になる。 https://mc.merill.net/
- SharePoint Copilot Apps が公開プレビュー（7/9）— SPFx 1.24 プレビューの一部で、フィルタ可能なデータグリッド・複数ステップのフォーム・チャート・KPI ダッシュボード・スケジューラ・承認パネルを Copilot キャンバス内で直接操作できる。開発ツール（Copilot Workbench）は 7/9 から、エンドユーザー向け全世界展開は 7/20 頃完了見込み。プレビュー中の配布はテナント/組織スコープのみで、ストア配布と GA は **2026年秋**。アダプティブカードより自由度の高い UI が選べる一方、外販や複数顧客への横展開を前提にした提案には現時点では乗らない。 https://devblogs.microsoft.com/microsoft365dev/sharepoint-copilot-apps-now-in-public-preview-from-intent-to-action-in-microsoft-365-copilot/
- Office アドインの統合マニフェストが GA（7/17）— Word / Excel / PowerPoint が Outlook に続いて対応。Teams アプリ・Office アドイン・Copilot エージェントを単一マニフェストで扱う方向に統一され、既存アドイン向けに変換ツールが提供される。 https://devblogs.microsoft.com/microsoft365dev/unified-manifest-for-office-add-ins-now-ga/
- Microsoft 一次のドキュメント系はすべて据え置き — Copilot Studio What's New は June 2026 節が最新（ms.date は 7/15 だが Notable changes は6月止まり）、M365 Copilot Release Notes は `July 15, 2026` バッチが最新で 7/22・7/29 は未公開、Released Versions は Copilot Studio Build **2026.6.3**（6/30 初出）でリージョン分布も無変化、非推奨一覧は新規なし（直近の発効は Visio → Power Automate エクスポート廃止・7/14）。 https://learn.microsoft.com/en-us/power-platform/released-versions/copilotstudio
- Release Wave のソース移行を一次確認 — `release-plan/2026wave1/microsoft-copilot-studio/planned-features` が **301** で `aka.ms/MCStoM365Roadmap` を経由し、M365 Roadmap の Copilot Studio フィルタ URL へ転送される。7/2 告知の「Copilot Studio / Sales・Finance・Service Agent のロードマップを M365 Roadmap へ移行」がドキュメント側に適用されたことが HTTP ステータスで裏付けられた。Power Platform 全体版 `release-plan/2026wave1/` は従来どおり。 https://learn.microsoft.com/en-us/power-platform/release-plan/2026wave1/microsoft-copilot-studio/planned-features
- Message Center 7/15〜7/22 の回収分 — Copilot Chat のブロック時ポリシー案内リンクと Web グラウンディングのドメイン除外（MC1434583 / MC1411435・7/20）、OneDrive 上のカスタムスキルを PowerPoint の Copilot（Mac / Web）から利用（MC1434581-580・7/20）、Outlook のメール下書き協働と Excel のブランドキットスキル（MC1430542 / MC1430537・7/17）、デスクトップフローのフローチャート可視化と PowerPoint 自動化（MC1429626 / MC1428573・7/16・7/15）、D365 の Sales Opportunity Agent / Customer Intent Agent 強化（MC1429683 / MC1429563・7/16）。 https://mc.merill.net/
- 100万ドキュメント規模のコネクタ実装記（7/23）— 約100万ドキュメント・月間10万ユーザー・**300超のエージェント**を支える Microsoft 社内コネクタの技術記事。Azure Blob Storage を真実の情報源とし、変更フィードで Azure Functions を起動して Graph API へ一方向に流す。インデックス済みコンテンツは Copilot Chat・Office アプリ・Copilot Studio エージェント・Retrieval API から横断利用される。スキーマ設計を最も影響の大きい判断とし、評価基盤を初日から用意すること、コネクタの健全性をパイプラインと分けて監視することを推奨に挙げている。 https://techcommunity.microsoft.com/blog/Microsoft365CopilotBlog/1-million-documents-to-300-agents-building-an-enterprise-scale/4540155
- Power Platform 周辺 — 7月分の「What's New in Power Platform」は未公開（最新は 6/11 の June）。Dataverse 7月更新（7/6・既報）は Power Pages の Native Dataverse Authorization 公開プレビュー、プラグインのコーディングエージェント向け配布拡大、パートナー MCP の認定、社内 MCP のガバナンス統制。Copilot Agent Kit は `June 2026`（7/9 更新）が最新。Microsoft Copilot Blog に D365 Sales を MCP で外部データ・パートナーツールへ接続する記事（7/21）。 https://www.microsoft.com/en-us/power-platform/blog/2026/07/06/dataverse-july2026/
- 日本語コミュニティ — Copilot Studio は選択する言語モデルによって Copilot クレジット消費が1倍から **100倍** まで変動する点を実測ベースで注意喚起する記事（Qiita・7/24）。研修や PoC のコスト見積もりに直結する。ほかに非構造化ナレッジの検証2部作（7/16・7/21）、Copilot Studio × Power Automate の FAQ 自動追記（7/20）。Zenn は 7/3 以降の新規なし。 https://qiita.com/tags/copilotstudio

### 開発ツール（Cursor / Codex / CLI）

- Cursor が Opus 5 を提供開始（7/24）— フォーラム告知（17:12 UTC）。CursorBench のデフォルト effort で Opus 5 が **66.7%**、Fable 5 が 66.5% で、Cursor 側は「Fable 5 に匹敵して価格は半分」と表現。Fable 5 と違って **ZDR 対応**である点を明示しており、モデルピッカーから選ぶだけで使える。データを残さない条件が入る案件では Cursor 側の frontier モデルが実質使えなかったので、チーム導入時のモデル選定をやり直す価値がある。なお changelog 側には出ておらず（RSS 全50件で `Opus 5` は0件）、フォーラム RSS でのみ捕捉できる。 https://forum.cursor.com/t/claude-opus-5-now-available/166583 / https://cursor.com/evals
- Cursor のエージェント・スウォームが刷新 — プランナーとワーカーを分離。ドキュメントのみから SQLite を Rust で再実装して全テストを通過した（旧構成はマージ競合で失敗）。コーディング作業の大半を安価モデルに寄せられるなら、エージェント運用のトークン単価の前提が変わる。 https://the-decoder.com/cursors-agent-swarm-suggests-cheaper-models-can-handle-most-coding-when-frontier-models-plan-the-work/
- Codex に ChatGPT Voice とローカルプロジェクトの複数フォルダ対応（7/23）— ChatGPT デスクトップアプリのローカルプロジェクトに複数フォルダを登録でき、Edit project でプライマリフォルダを指定する。新規チャット・Git 操作・`AGENTS.md` / skills / `config.toml` の自動探索はプライマリ基準で、セカンダリはファイル検索・読み書きの対象として残る。音声側は GPT-Live ベースで、Chat / Work / Codex のスレッドを横断して指示できる。 https://developers.openai.com/codex/changelog
- 主要 CLI は据え置き — Claude Code **v2.1.220**（7/25・バグ修正と信頼性改善のみ）、GitHub Copilot CLI v1.0.75（7/24）、Codex CLI 安定版 0.145.0（7/21）。Codex の pre-release も `0.146.0-alpha.10.1`（7/25 20:29 UTC）以降の新規ビルドなし。 https://github.com/openai/codex/releases

### 市場データ・調査

- 6月のシェアデータが出そろった — Similarweb（グローバルWeb）は ChatGPT **52.7%**／Gemini 27.3%／Claude 8.9%／DeepSeek 3.6%／Grok 2.5%／Copilot 2.0%／Perplexity 1.1%。1年前は ChatGPT 約76%・Gemini 約9%で、12カ月で 23.7ポイント失った。国内は NRC デイリートラッキング6月調査（7/10公開・20〜69歳・日次約150サンプル）で現在利用率が **50.4%** と初の5割超、サービス別は ChatGPT 現在 30.3% / Gemini 現在 29.0% で差は1.3ポイント、3カ月の伸びは Gemini +5.7pt が ChatGPT +3.9pt を上回る。Copilot は現在利用約15.0% で3番手。「ChatGPT 前提」で組んだ研修・ガイドライン・提案テンプレは Gemini 併記に更新しないと利用実態と合わない。 https://ppc.land/chatgpt-drops-to-52-7-as-claude-triples-its-ai-traffic-share/ / https://www.nrc.co.jp/report/260710.html
- Stanford SIEPR の政策ブリーフ「What is really happening to jobs?」が 7/25 に HN で246ポイント。新卒の失業率は2026年初で **5.6%**（3年前比 +1.6ポイント）。ソフトウェア開発・カスタマーサポートなどAI露出の高い職種で若手の雇用が減る一方、同職種の年長層は横ばい〜増加。ただし高露出職種全体で雇用や求人が押し下げられている証拠は乏しい、というのが結論。AI代替論を数字で薄める側の一次ソースとして押さえておく価値がある。 https://siepr.stanford.edu/publications/policy-brief/what-really-happening-jobs-separating-ai-hype-reality
- テック業界の2026年人員削減は集計元により 14.2万〜16.8万人（Oracle の約3万人が単年最大、Meta / Amazon / Microsoft が続く）。一方 Amazon・Microsoft・Alphabet・Meta の2026年 capex ガイダンス合計は約 **$700B** で2025年実績のほぼ倍。AI を理由に挙げた削減発表の比率は 1月7% → 5月40% と急上昇しており、理由の後付けが混じる点は割り引いて読む必要がある。 https://techcrunch.com/2026/07/06/the-running-list-major-tech-layoffs-in-2026-where-employers-cited-ai/
- a16z「Top 100 Gen AI Consumer Apps」は第6版（2026年1月データ・3月公開）が最新で7月版は未公開。半年更新のため7〜8月に第7版が出る可能性があり継続確認。第6版の要点は ChatGPT が Web で2位 Gemini の2.7倍・モバイルで2.5倍、Claude の有料購読が前年比 +200%、Gemini が同 +258%。 https://a16z.com/100-gen-ai-apps-6/

### 料金・ビジネスモデル・インフラ投資

- Nvidia が OpenAI のデータセンター賃借に約 **$250B** の保証を出す方向で協議中と WSJ が 7/26 報道。対象は SoftBank のエネルギー子会社がオハイオ州南部で開発中の 10GW 案件で、孫正義は総事業費が約$500Bに達しうると述べている。Reuters は独自確認できておらず現時点は協議段階。同じ週末、NAVER・Nvidia・Brookfield が韓国の国家AIファクトリーを200MW（Nvidia GPU 約10万基相当）へ拡張する $10B 計画を発表（Brookfield が最大$9B、Nvidia が NAVER 株を約$1Bで引き受け4.5%取得）。ただし Brookfield 分は非拘束のタームシートで、Nvidia の出資も他ソースからの$9B確定調達が前提。GPU/クラウドのコスト前提を顧客に説明する場面で「その供給能力が誰の信用で立っているか」まで示せる材料になる一方、稼働時期を前提にした試算は割り引くべき条件付き合意が多い。 https://www.bloomberg.com/news/articles/2026-07-26/nvidia-in-talks-on-250-billion-backing-for-openai-hub-wsj-says / https://www.globenewswire.com/news-release/2026/07/25/3333160/0/en/NAVER-NVIDIA-and-Brookfield-to-Expand-Korea-s-National-AI-Factory-Infrastructure-Buildout.html
- Business Insider Japan の2026年7月版・生成AI主要8サービス料金早見表（$1=160円換算）。6月に Google がエントリープラン Google AI Plus を月¥1,200 → **¥725** へ値下げ、Genspark は Pro の最低価格を $249.99 → $49.99 へ大幅改定。ChatGPT Plus（¥3,000）・Claude Pro（$20・約¥3,200）は据え置き。他は ChatGPT Go ¥1,400、Google AI Pro ¥2,900、Copilot Personal ¥2,130、Perplexity Pro $20、Felo Pro ¥2,099、SuperGrok $30。エントリー層の価格競争は Google が仕掛けている。 https://www.businessinsider.jp/article/2607-how-much-did-major-generative-ai-service-fees-become-in-july-2026/
- Cloudflare が AI ボットを Search / Agent / Training の3分類に分け、分類ごとに許可・拒否を設定できる制御を導入。**9/15** 以降に登録される新規ドメインは、広告掲載ページに限り Training と Agent をデフォルト拒否、Search は許可となる。robots.txt 拡張の Content Use Signals、検証済みボットDB の BotBase、仲介経由のボット認証 Transitive Trust も併せて提供。自社サイトをエージェントに読ませる前提の設計は、この分類に合わせた見直しが要る。 https://blog.cloudflare.com/content-independence-day-ai-options/

### エンタープライズ導入事例

- SUBARU のパワートレイン設計部門が、月予算 **10万円** 規模から生成AIの内製に着手。OSS の GenU で RAG を構築し、マルチエージェントは軽量SDK の **Strands Agents** で実装している。非IT系エンジニアが「使う側」から「作る側」に回った国内製造業の事例で、kit の常用スタックがそのまま出てくる。 https://codezine.jp/article/detail/28873
- Netflix が2026年に約 **300作品** で生成AIワークフローを使用。ドキュメンタリー「The American Experiment」のAI補助映像17分は従来手法比で制作速度2倍・コスト半分。用途はポストプロダクション（編集・仕上げ）が最多で、インドの犯罪スリラー「Glory」の群衆シーンや歴史的戦闘シーンの生成にも使用。予算・時間の制約で断念していたカットを実現できた点を効果に挙げている。 https://www.itmedia.co.jp/news/articles/2607/17/news065.html

### 規制・地政学

- Kimi K3 のオープンウェイト公開は **7/28 0:00 JST** — Hugging Face の `moonshotai/Kimi-K3` ページのメタデータが `releaseDate: 2026-07-27T15:00:00.000Z` を示しており、7/27 10:45 JST 時点でも「Upcoming release」表示・カウントダウン残り13時間14分・779アカウントが通知待ちだった。前版の「7/27 9:00 JST 公開」は誤り。予告されている中身は Kimi Delta Attention と Attention Residuals による新アーキテクチャ、ツール呼び出し・ブラウジング・多段プランニングのネイティブ対応、リポジトリ規模のコード理解を狙った長コンテキスト。Moonshot は「世界初のオープン 3T 級モデル」と称している（二次情報では 2.8兆パラメータ）。配布サイズは MXFP4 で約594GB 説と約1.4TB 説に割れ、公式値は未確定。自前ホストの検証に着手できるのは 7/28 以降。 https://huggingface.co/moonshotai/Kimi-K3
- トランプ政権は中国製オープンウェイトモデルへの一律禁止ではなく特定モデルを狙う選択的規制を志向していると NYT が 7/25 報道。Anthropic と OpenAI は非公開でロビイングを継続する一方、Microsoft と Google は自社サービス経由で中国製オープンモデルへのアクセスを販売しており立場が割れている。7/24 のオープンウェイト書簡（50社署名）と合わせ、業界の分断が政策の形を決めつつある。 https://the-decoder.com/us-reportedly-favors-selective-bans-over-blanket-restrictions-on-chinese-open-weight-models-citing-security-concerns/

### Google

- Workspace の AI ブランドを Gemini 側へ再統合 — NotebookLM を「**Gemini Notebook**」に改称（7/16 ロールアウト開始）、「Gemini Alpha」プログラムを「Gemini Beta」に改称（7/22 開始・最大15日で段階展開）。Gemini CLI → Antigravity CLI 統合（6/18 停止）と同じ方向で、開発者向け・ナレッジ向けツールがブランド単位で畳まれ続けている。 https://workspaceupdates.googleblog.com/2026/07/notebooklm-now-gemini-notebook.html
- **Gemini 3.5 Pro** は未発表が継続 — 7/21 に公開された3モデル（3.6 Flash / 3.5 Flash-Lite / Flash Cyber）に Pro は含まれず、7/16 Bloomberg の「数カ月遅れ」報道から状況変化なし。公開APIは gemini-3.5-flash / gemini-3.1-pro-preview のまま。 https://techcrunch.com/2026/07/21/google-releases-three-new-gemini-models-but-no-3-5-pro/

## 直近の注目予定

- **7/28 0:00 JST**: Kimi K3 オープンウェイト公開（7/27 15:00 UTC）
- **7/28（火）**: Copilot Studio Released Versions の定例更新（2026.7.x の反映見込み）
- **7/29 前後**: M365 Copilot Release Notes の次バッチ（Opus 5 の記載有無を確認）
- **7/30 前後**: M365 Copilot 拡張機能 What's New の次月次、Copilot Agent Kit と MS-4005 の週次確認
- **7/31**: Devin classic 環境設定 read-only 参照終了
- **8/1**: covered frontier model 60日 EO 期限
- **8/3**: 旧「Claude in Slack」退役
- **8/5**: Claude Opus 4.1 の Claude API 退役 / Cowork 倍増利用枠終了
- **8月第1週**: Power Platform Weekly の夏季休刊明け
- **8/9**: ChatGPT Atlas シャットダウン
- **8/17**: Claude Console 旧 Workbench 退役 ＋ 実験的プロンプトツール API（`/v1/experimental/generate_prompt`・`improve_prompt`・`templatize_prompt`）廃止
- **8/26**: OpenAI Assistants API 廃止 / o3 退役 / GPT-4.5 完全廃止
- **8/31**: Sonnet 5 促進価格終了（→ $3/$15）
- **9/15**: Cloudflare の新規ドメインで Training / Agent がデフォルト拒否に
- **9月**: iOS 27 / macOS 27 GA（AFM 3 本番）
- **2026年秋**: SharePoint Copilot Apps の GA と SharePoint ストア配布
- **7〜8月**: a16z「Top 100 Gen AI Consumer Apps」第7版の公開可能性

## 改善メモ

- **不一致: Kimi K3 の公開時刻**: Master は Hugging Face ページのメタデータ `releaseDate: 2026-07-27T15:00:00.000Z`（＝7/28 0:00 JST）を実測、industry は「7/27 00:00 UTC＝9:00 JST 公開予定」と記載。一次メタデータのある Master 側を採用し、本文は 7/28 0:00 JST とした。前版（当サマリー 07-27 初版）の「本日 9:00 JST 公開予定」も同時に訂正。
- **不一致: Kimi K3 の配布サイズ**: Master は「594GB 説と 1.4TB 説に割れ公式値は未確定」、industry は「MXFP4 で約594GB」。両論併記とした。
- **不一致: ARC-AGI-3 の倍率**: Master は「他モデルの約3倍」、industry は「従来記録の約4倍」。スコア 30.2% は一致するが比較対象が異なるため、本文では倍率を書かず実数のみとした。
- **不一致: Opus 5 の Copilot Studio 提供状況**: Tech Community ブログ（7/24）は6サーフェスへの提供開始を告知、learn.microsoft.com の What's New は6月節のままで GA 最新は Sonnet 5 / GPT-5.5 Chat。一次同士が食い違うため両方を本文に明記した。
- **02 の担当範囲変更の影響**: 02 が Microsoft 専任に改訂されたため、前版に載っていた Cursor Router（7/22）と Devin マルチリポジトリスキャン（7/17）は本日分から外れた（Master 側にも当日掲載なし）。代わりに 7/9〜7/24 の Microsoft 一次が複数回収されている。
- **台帳番号の衝突**: Master の B-012（Cursor 等のソース追加）と Copilot の B-012（Release Wave のソース定義見直し）は別台帳の同番号。横断参照時に混同しないこと。
- Master: 新規提案 B-013（403 を「ゲートウェイ拒否」と「オリジン403」に分類して記録）、B-014（Claude Code Changelog のフォールバック URL を `raw.githubusercontent.com` へ変更）。
- Copilot: B-012 を推定から一次確認に格上げ（Release Wave の 301 転送を HTTP ステータスで実測）。継続提案5件（最多は B-011 Power Platform Blog のトピック記事照合、8回目）。
- industry: 継続提案1件（B-004 取得方法の WebSearch 優先化、28回目）。
- **障害の変化: Master**: `cursor.com` / `forum.cursor.com` / `www.testingcatalog.com` / `simonwillison.net` / `community.openai.com` の5ホストがゲートウェイ拒否（CONNECT 403）と判明。前4者は 07-26 に B-012 でローカル curl 200 を根拠に追加したソースだが、クラウド定期実行からは到達不可。サイト側の復旧待ちでは解消せず実行環境の許可リスト対応が必要（B-013）。`code.claude.com/docs/en/changelog` は一時 503（同一セッション内で raw フォールバックにより取得完了・継続障害ではない）。
- **障害の変化: industry**: 主要ニュースドメインの記事本文 WebFetch が広範に403（Forbes / ITmedia / Publickey 記事ページ / MLQ / buildfastwithai）。本日は WebSearch のスニペットで代替。
- **週次復旧チェック**（月曜）実施: `developers.openai.com/changelog`・`codex/changelog`・`www.anthropic.com/news` はいずれも 403 継続・未復旧。
- 前日（07-26）分の欠損リカバリは対象なし（3ソース統合で生成済み）。
