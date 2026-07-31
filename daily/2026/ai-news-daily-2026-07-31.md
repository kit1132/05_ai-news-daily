# AI News Daily Summary — 2026-07-31

> 本サマリーは 01_ai-news-Master・02_ai-news-Copilot・03_ai-news-industry の3ソース（7/31分）を統合して作成。

金曜の主題は3つ。OpenAI が GPT-5.6 の安価帯を最大80%値下げして API の単価前提が崩れ、EU の AI Act 改正が発効して高リスク義務は16カ月延びた一方で 8/2 の透明性義務だけが据え置かれ、GitHub が Copilot の既定モデル有効化ポリシーを 8/26 発効で導入した。

## 今日のハイライト

### 1. OpenAI が GPT-5.6 の下位2モデルを値下げした — 安価帯の単価前提が崩れる

**要点**: OpenAI が GPT-5.6 Luna の API 価格を80%、Terra を20%引き下げた。Luna は5分の1になり、単価を理由に見送っていた分類・抽出・要約のバッチ処理が採算に乗り直す。

**詳細**: 7/30 の発表で、Luna は入力 $1 / 出力 $6 から **$0.20 / $1.20** へ、Terra は入力 $2.50 / 出力 $15 から $2 / $12 へ下がった（いずれも100万トークンあたり）。最上位の Sol は据え置きだが、API に fast option が加わり、標準の最大2.5倍の速度を2倍の価格で選べるようになった。OpenAI は値下げの理由を GPT-5.6 の内製開発で得た効率化——本番コードをモデル自身に書き換え・最適化させたことと、トークン生成の改善——と説明している。値下げは API だけで完結せず **Codex と ChatGPT Work** の利用量カウントにも反映されるため、同じ契約のまま実行できる量が増える。Sol の fast option は速度2.5倍に対し価格2倍なので、単価ではなくレイテンシが律速になっている用途に限れば正味の得になる。一次発表（`openai.com/index/`）はソース側の実行環境から到達できず、金額は複数の二次報道（CNBC / Axios / Yahoo Finance）が一致した値を採っている。

- https://openai.com/index/gpt-5-6/
- https://www.cnbc.com/2026/07/30/open-ai-price-cut-gpt.html
- https://www.axios.com/2026/07/30/openai-cuts-prices-gpt-terra-luna5
- https://finance.yahoo.com/technology/ai/articles/openai-cuts-gpt-5-6-173045044.html

### 2. EU デジタルオムニバス（AI Act 改正）が発効した — 高リスクは16カ月延びたが 8/2 の透明性義務だけ動かない

**要点**: EU が AI Act 改正を 7/27 に発効させ、高リスク AI の適用開始を2027年12月へ約16カ月延期した。ただし **8/2 の透明性義務は据え置き**で、こちらは猶予が4日しかない。

**詳細**: Regulation (EU) 2026/1744 が 7/24 に EU 官報へ掲載され、8/2 期限が迫るため異例の「緊急」扱いで3日後の 7/27 に発効した。延期の対象は2種類に分かれる。

- **Annex III**（高リスク AI）: 採用選考・与信スコアリング・法執行の意思決定支援・国境管理が対象で、適用開始が **2027年12月2日** へ約16カ月延期された
- **Annex I**（安全部品に組み込まれる AI）: 医療機器・機械・民間航空機器・昇降機などが対象で、2028年8月2日へ延期された

一方、**8月2日の透明性義務の期限は動いていない**。さらに 2026年12月から、合意なき性的画像（NCII）と CSAM の生成機能の禁止が追加された。EU 圏の採用・与信領域での AI 導入提案はコンプライアンス期限を2027年末基準に引き直せる一方、透明性表示だけは来週が期限で猶予がない。

- https://lawandtechnology.eu/en/digital-omnibus-on-ai-official-journal-regulation-2026-1744/
- https://www.gibsondunn.com/eu-ai-act-omnibus-agreement-postponed-high-risk-deadlines-and-other-key-changes/

### 3. GitHub が Copilot の既定モデル有効化ポリシーを導入した — 8/26 発効で最初の28日が実質の猶予

**要点**: GitHub が Copilot Business / Enterprise で、GA になったモデルを管理者操作なしに既定有効へ切り替えるポリシーを追加した。モデル選定を統制している組織は 8/26 までに設定を入れる必要がある。

**詳細**: 7/29 の追加で、厳格な統制が要る組織向けに単一のオプトアウトが用意された。**最初の28日間**は設定は可能だが実効はなく、利用者側の見え方も変わらない。**8/26** にポリシーが発効すると、明示設定されていないモデルの表示が「unconfigured」から「inherits default」に変わり、ポリシー設定に従い始める。つまりモデル選定を組織で統制している場合、この28日が設定を入れ直す実質の猶予になる。

- https://github.blog/changelog/2026-07-29-default-model-enablement-for-copilot-business-and-enterprise/

## カテゴリ別まとめ

### コーディングエージェント / 開発ツール

- GitHub が Copilot code review の agent skills と MCP を GA にした（7/29）— Pro から Enterprise までの全有料プランで使えるようになり、レビュー基準を1か所に集約する足場ができた。差し込める外部文脈は2種類ある。
  https://github.blog/changelog/2026-07-29-copilot-code-review-agent-skills-and-mcp-now-generally-available/
  - `agent skills`: `.github/skills` 配下に `SKILL.md` を置くと、リポジトリや組織に固有のコーディング標準・社内ツールをレビュー中に呼び出せる。Claude Code や Codex CLI が使う skills と同じ配置規約に沿う
  - `MCP サーバー接続`: 課題管理・ドキュメント・サービスカタログなど既存の社内基盤から文脈を引く。GitHub MCP と Playwright MCP が既定で有効になっている
  - ツール呼び出しは**読み取り専用**に限定され、skills や MCP を使って生成されたコメントにはその旨が併記される
- Copilot CLI が組織統制の対象になった（v1.0.76・7/30）— GitHub が MDM 経由の managed settings を追加し、管理者が制限的ポリシーを組織へ適用できるようにした。安定版の更新は v1.0.75（7/24）以来6日ぶりになる。
  https://github.com/github/copilot-cli/releases
  - サンドボックスが拒否パス（相対パス・シンボリックリンクを含む）を macOS / Linux で強制するようになった
  - `/plugins` からプラグイン・instructions・エージェント・LSP サーバー・フックを個別に有効化／無効化できるようになり、モデルとして **grok-4.5** に対応した
  - 複数セッションを切り替え・監視する Sessions サイドバー、キュー済みメッセージを並べ替え・編集できるキューマネージャ、AI クレジット上限を予測する `/limits predict`、音声モードの一時停止と再開も入った
  - フックの出力に1回あたり10 MiB の上限が付き、MCP ツールは定義スコープのスナップショット経由で読み込みが速くなった
  - 翌日の pre-release **v1.0.77-0** は、対話端末の既定ログインをブラウザ OAuth に変更している（リモート／ヘッドレスは device code のまま）
- Cursor が iPad 版を全有料プランに開放した（7/29）— あわせて PR レビュー画面を差分だけでなく PR 全体を扱う形に作り直し、iPhone と共通の受信箱を追加した。
  https://cursor.com/changelog/ipad
  - レビュー画面はコメント・チェック・承認を扱えるようになり、レビュアーの追加や変更、コメントを読んでエージェントに解決を指示する操作ができる
  - iPad ではサイドバーのチャットを固定して複数エージェントの実行を並べて監視でき、分割画面でレビューとチャットを併置できる
  - スクリーンショットを添付して任意の位置にコメントを落とす操作と、Apple Pencil での直接の描き込みに対応した
  - 1つのチャットが複数の PR を作った場合に、最後の1件だけでなく全てを開けるようになった
- Codex CLI と Claude Code はいずれも据え置きだった — OpenAI は pre-release を 0.147.0-alpha.2（7/30）まで1本刻んだだけで、安定版は 7/29 の 0.146.0（Agent Plugins・追加マーケットプレイスに Amazon Bedrock と Claude Code）から動いていない。Claude Code も v2.1.220（7/25）のままで、7/26〜31 の7日間に新バージョンが出ていない。Claude Platform の release notes も最新エントリが 7/24 のままである。
  https://github.com/openai/codex/releases

### Copilot Studio / Power Platform

- Power Automate デスクトップフローの3機能が 7/16 に GA 済みだったことが判明した（取りこぼし回収）— Release Wave の計画機能テーブルで General availability 列に **Jul 16, 2026** の実日付（緑チェック）が付いており、2週間ぶんの取りこぼしを回収した。3件とも「失敗や支援エスカレーションが起きる前に品質と効果を可視化する」系で、CoE 運用にそのまま効く。
  https://learn.microsoft.com/en-us/power-platform/release-plan/2026wave1/power-automate/planned-features
  - `PGP 暗号化・復号`: OpenPGP 互換の公開鍵・秘密鍵を使うアクションがアクションピッカーに加わった。受信者の公開鍵で暗号化し、対応する秘密鍵とパスフレーズで復号する。標準フォーマット対応のため PGP 前提の外部システムと相互運用できる
  - `時間・コスト削減の自動計測`: 成功実行を基に節約時間を算出する組み込みルール。手作業時の所要時間を定義すると節約時間が計算され、時間単価を当てると実行回数に比例したコスト削減額が出る。RPA の投資対効果を Excel の手集計でしのいでいる現場を、プラットフォーム標準で置き換えられる
  - `デスクトップフローチェッカーの管理者通知`: ポータルのチェッカーが持つルールベース静的解析を環境内の全デスクトップフローに広げ、通知種別（エラー / 警告 / 情報）・重大度・しきい値・再発条件・スコープを管理者が設定できるようにした
- Power Platform の7月 GA 予定5件が8月ずれ込みの前提になった — Microsoft は本日 GA と見込まれていた「Build better forms with integrated Power Apps」を、Release Wave 上で緑チェックなしの「Jul 2026」表記に据え置いたまま7月を終えた（二次ソースは 7/31 GA と報じていた）。Public preview は 5/29 に済んでいるので、検証だけ先行させる判断はできる。
  https://learn.microsoft.com/en-us/power-platform/release-plan/2026wave1/power-automate/build-better-forms-integrated-power-apps
  - 統合 Power Apps は、有人デスクトップフローの入力 UI としてキャンバスアプリをそのまま使えるようにするもの。フロー側からコンテキスト・状態・値を渡して事前入力でき、ユーザーの入力値はフローに戻って後続ステップを駆動する。アプリ側のボタンクリック等のイベントから特定のサブフローを呼べるため、逐次実行ではなくイベント駆動の構成が組める
  - Power Automate 側で同じく未反映: ワークキュー項目の CSV エクスポート、マシンとフローの稼働率のダッシュボード表示
  - Power Apps 側で同じく未反映: code apps のコネクタを CLI で検出・作成・接続、FetchXML エディターでのオフラインプロファイル構成
- Copilot Studio の基盤ビルドは7月ゼロ更新で確定した — Microsoft は Released Versions の基盤ビルドを **2026.6.3**（6/30 初出）に据え置いたまま、火曜定例の 7/7・7/14・7/21・7/28 のいずれでも新ビルドを出さずに7月を終えた。リージョン分布も無変化で、2026.6.3 が11リージョン、UK / Asia / UAE / Japan / Europe が 2026.6.2、Australia / US 本体 / GCC が 2026.6.1 にとどまる。次の定例更新は 8/4（火）にあたる。
- Microsoft の Copilot 系一次ソースは 7/31 時点で全て据え置きだった（Copilot Studio What's New は7月節が未公開 / M365 Copilot Release Notes は「July 15, 2026」が最新 / M365 Roadmap は 7/9 の GPT-5.6 が最新 / Power Platform Blog は7月の月次記事を出さずに終了 / Message Center は本日の新規検知なし）。次の定例は 8/4・8/5。
  https://learn.microsoft.com/en-us/microsoft-copilot-studio/whats-new

### AI モデル / プロダクト

- Grok 4.6 と 4.7 のパラメータ規模が分離して整理された — 二次報道は Musk が 7/28 に示した内容として、Grok 4.6 を **1.5T** パラメータ（SFT と RL を大幅改善）、Grok 4.7 を **2.1T** パラメータと書き分けている。当サマリーは 07-30 時点で 4.6 について「2T 説と 1.5T 説が併存」と記録していたが、2T 相当の数字は 4.7 側を指していた可能性が高い。時期は 4.6 が 8/7 前後、4.7 がその数週間後（8月下旬〜9月上旬）で、いずれも公式ドキュメントでの確認は取れていない。
  https://www.roic.ai/news/musk-signals-rapid-grok-rollout-46-in-two-weeks-47-a-month-later-07-28-2026
- Google が Google Docs のコメント対応に Gemini を組み込んだ（7/30）— Gemini が文書全体のコメントを読んで要約し、返信の下書きまで行えるようになった。同日に周辺の変更が2件入っている。
  https://workspaceupdates.googleblog.com/2026/
  - 生成機能の対応言語を11言語拡大した（北京語・オランダ語・マレー語・ヘブライ語・ポーランド語・トルコ語・チェコ語・インドネシア語・スウェーデン語・デンマーク語・ノルウェー語）
  - 7/22 に告知された Gemini Alpha → **Gemini Beta** の改称が、7/30 から Scheduled Release ドメインへの全面展開に入った
- Gemini 3.5 Pro は未 GA が続いている — Google は 3.5 Pro を Vertex AI の限定 preview に留めたままで、7/30 に確認した範囲でも新しい GA 告知はない。公開 API の GA 済みフラッグシップは Gemini 3.1 Pro から動いていない。前日サマリーで触れた「Polymarket が 7/31 の発表を約81%と見込む」節目は、本日時点で外れる方向にある。
- Alibaba が Qwen3.7 Flash を公開した（7/27）— 7/29 に LLM Gateway へ登録された。上位の Qwen3.8-Max-Preview は選定済みのホスト製品経由での提供に留まり、オープンウェイト版は「今後」とされている。いずれも集約サイト経由の情報で、一次のモデルカードには到達できていない。Kimi K3 側は 7/29〜31 で新しい動きがない。
  https://llmgateway.io/timeline

### AI セキュリティ

- Claude の共有リンクが検索エンジンにインデックスされていた（7/25 表面化・7/27 までに大半削除）— 原因はモデルの脆弱性ではなく共有機能の既定設定で、AI 導入提案の管理項目に「共有リンクの発行可否・失効・棚卸し」が加わった。ChatGPT（約1万件）・Grok（約37万件）に続く主要ベンダー3例目にあたる。
  https://admina.moneyforward.com/jp/blog/claude-shared-chat-google-index
  - Claude の Share 機能で生成した会話ページと Artifacts が、検索エンジンの除外設定不備で公開インデックスされていた。7/25 に Reddit で `site:claude.ai/share` により閲覧できると指摘されて表面化した
  - 露出内容には健康・医療記録、子どもの氏名と電話番号、暗号資産ウォレットの鍵、企業の社内文書が含まれた
  - Anthropic は robots.txt を更新し、7/27 までにインデックス済みコンテンツの大半を削除して、利用者に共有リンクの棚卸しを推奨している

### 規制・ガバナンス

- ホワイトハウスのフロンティアモデル自主フレームワークは 8/1 期限が目前に来ている — 6/2 大統領令の60日期限が 8/1 に満了し、それに合わせて OpenAI / Anthropic / Google DeepMind との自主フレームワーク公表が見込まれる段階のままである。内容は公開前に最大30日の政府セキュリティレビュー枠を設けるもので、Meta は参加要請を受けつつ未合意にとどまる。現行案がクローズド API の3社を前提に設計されている点も既収録から変化していない。次回ダイジェストで正式発表の有無を確認する。
  https://www.techtimes.com/articles/321497/20260724/voluntary-paper-mandatory-practice-white-house-ai-review-hits-august-1-deadline.htm

### 運用 / エンタープライズ

- Meta のインフラ VP が「追いつくのに20カ月」と述べた — VB Transform 2026 のセッションで VP of Engineering の Barak Yagour が、エージェント導入の隘路はモデルではなくデータ基盤側にあると説明した。供給側の実データとして提案の根拠に使える。
  https://venturebeat.com/data/we-have-maybe-20-months-to-rebuild-for-ai-agents-metas-infrastructure-vp-tells-vb-transform-2026
  - 同社データ基盤に到達するエージェント由来のクエリが半期で **30倍**に増え、キャパシティ・ID・速度が同時に破綻しつつある
  - 既存のエンタープライズ基盤は人間の利用を前提に構築されているため、追いつくための猶予は約20カ月との見立てになる
  - 2月に投入した agentic data apps は、3カ月で社内公開ダッシュボードの63%が新ツール製になった
  - 既収録の「57%が誤答をコンテキスト欠落に特定・統制されたコンテキストレイヤの本番稼働は25%」と同じ方向を向く

### 市場・決算 / インフラ

- Apple の FY26 Q3 決算で Cook が Siri の Gemini 依存を追認した（7/30）— 第3世代 Apple Foundation Models が Google の Gemini モデル技術との協業で構築され、オンデバイスの約30億パラメータモデルからクラウド側まで一貫すると説明した。7/10 の Apple × OpenAI 提訴・Siri の Gemini 切替が、決算の場で公式に既定路線として確認された形になる。業績は売上 **$111.2B**（+16.6%、市場予想 $109.7B 超）、希薄化後 EPS $2.01、粗利率49.3%、Services が過去最高の $30.98B。Tim Cook にとって最後の決算コールで、9/1 に John Ternus が CEO に就任する。
  https://www.cnbc.com/2026/07/30/apple-earnings-live-updates.html
- Amazon の FY26 Q2 は確報値を確認できていない（7/30 17:00 ET 発表）— 一次 IR ページと CNBC 記事本文がいずれも403で、ソース側から確報値に到達できていない。二次情報も数値が割れており、売上 $181.52B（+16.6%）・EPS $2.78・AWS +28% とする記述と、会社ガイダンス $194–199B ／コンセンサス $196.9B を前提とする記述が混在する。前者はガイダンス下限を大きく下回って整合しないため採用しない。確定している事前情報は、会社ガイダンスが売上 $194–199B（+16〜19%）、AWS のコンセンサスが $40.6B（+31.6%）、2026年 capex 計画が約 $200B（BofA 等はメモリ価格上昇を理由に $210B への上方修正を想定）。AWS 成長率と capex ガイダンスは 08-01 分で確報を追う。
- AMD と Anthropic が最大2GW の MI450 提携を結んだ（7/22 発表・取りこぼし収録）— Anthropic の計算基盤が Nvidia / Google TPU / AWS Trainium / AMD Instinct の4ベンダー構成になり、単一アクセラレータ前提のコスト試算は前提を置き直す必要がある。Anthropic は AMD Instinct MI450 シリーズ（MI455X）を Helios ラックスケールで最大2GW 導入し、第1GW を2027年上期に配備開始する。AMD は最大 **$5B** の戦略的出資を、一括ではなく配備マイルストーン連動で支払う。構成は EPYC「Venice」CPU・Pensando ネットワーキング・ROCm になる。Meta からの最大 $10B リース協議（7/17）・Samsung との独自チップ協議（7/2）と合わせて、調達先の分散が同社の一貫した方針として確認できる。
  https://ir.amd.com/news-events/press-releases/detail/1292/

### 国内動向 / 新興ツール

- ソフトバンクが「GaranAI」のベータ版を始めた（7/22）— 日本のコンテンツ産業と生成 AI 開発の両立を狙うデータエコシステム基盤で、国内の学習データ調達・権利処理を外部化する選択肢になる。
  https://www.softbank.jp/corp/news/press/sbkk/2026/20260722_01/
  - 報道機関 **30社超**がデータ提供を表明している（共同通信社・毎日新聞社・産経新聞社に加え、信濃毎日新聞社・デーリー東北新聞社などの地方紙を含む）
  - 多段階の加工で著作物を保護しつつ、コンテンツホルダーへの収益還元と AI 開発事業者への良質な学習データ供給を両立させる設計になっている
  - 専任チームが収集から加工まで一貫して担当し、約半年のベータ運用でデータ品質監視と加工ロジックを改善する。2027年1月以降に正式提供（名称変更予定）となる
- Product Hunt の7月ローンチがエージェントの埋め込み型に寄った — 開発者向けインフラとエージェント特化ツールが中心で、汎用チャットボットから組み合わせ可能な部品への移行が続いている。GitHub Trending 側も、コーディング／ペンテスト／取引の各エージェントとそれを繋ぐ MCP サーバー・AI ゲートウェイが上位を占める。
  https://www.producthunt.com/leaderboard/monthly/2026/7
  - `AnySearch`: エージェント向けのリアルタイム構造化データ取得（560票超）
  - `Sim`: エージェントとワークフローを構築・管理する OSS ワークスペース
  - `Framer AI Agents`: キャンバス上のエージェントがサイトの設計・執筆・分析を担当する
  - `PlugThis`: 対話で Chrome 拡張を生成する

## 直近の注目予定

- **7/31（本日）**: Devin classic 環境設定 read-only 参照終了 ／ Copilot から Gemini 2.5 Pro・Gemini 3 Flash 廃止
- **8/1**: covered frontier model 60日 EO 期限（ホワイトハウス自主フレームワーク公表見込み）／ Copilot in 30（SMB 向けトライアル）CSP 提供開始
- **8/2**: EU AI Act の透明性義務の期限（今回の改正で延期されていない）
- **8/3**: 旧「Claude in Slack」退役
- **8/4**: Released Versions・Release Wave・非推奨一覧・拡張機能 What's New の定例更新
- **8/5**: Opus 4.1 Claude API 退役 ／ Cowork 倍増利用枠終了 ／ M365 Copilot Release Notes 次バッチ見込み
- **8/7 前後（推定）**: Grok 4.6（1.5T）
- **8/9**: ChatGPT Atlas シャットダウン
- **8/17**: Claude Console 旧 Workbench 退役 ＋ 実験的プロンプトツール API 廃止
- **8/26**: OpenAI Assistants API 廃止 / o3 退役 / GPT-4.5 完全廃止 ／ Copilot 既定モデル有効化ポリシー発効
- **8/31**: Sonnet 5 促進価格終了（→ $3/$15）／ Power Automate モバイルアプリ廃止
- **8月見込み**: 統合 Power Apps GA、ワークキュー項目の CSV エクスポート、マシン/フロー稼働率のダッシュボード表示
- **9月**: iOS 27 / macOS 27 GA（AFM 3 本番）

## 改善メモ

- B-018（Master）: OpenAI 系5ソースが全て到達不可である実態を `daily-sources.md` に明記し、料金変更の検知手段を補う
- B-018（Copilot）: Release Wave の GA 済みチェックマークを日次で差分監視する手順を追加
- B-008（Industry）: 週1回の取りこぼし検知スイープ（TLDR AI を高優先へ）を新規起票
- 継続提案: Master 5件（最多 B-013 5回目）、Copilot 8件（最多 B-011 12回目）、Industry 4件（最多 B-004 32回目）
- 障害: `openai.com` 等4ホストをゲートウェイ拒否へ再判定（Master）、`www.ppweekly.com/feed` が 403（Copilot・新規）
