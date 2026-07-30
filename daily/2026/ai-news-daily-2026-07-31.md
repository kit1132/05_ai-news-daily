# AI News Daily Summary — 2026-07-31

> 本サマリーは 01_ai-news-Master・02_ai-news-Copilot・03_ai-news-industry の3ソース（7/31分）を統合して作成。

金曜の主題は3つ。OpenAI が GPT-5.6 の安価帯を最大80%値下げして API の単価前提が崩れ、GitHub が Copilot code review の agent skills / MCP を GA にしてチームの基準と社内ツールをレビューに持ち込めるようになり、Power Automate の3機能が2週間前に GA 済みだったことが判明した。

## 今日のハイライト

### 1. OpenAI が GPT-5.6 の下位2モデルを値下げした — 安価帯の単価前提が崩れる

**要点**: OpenAI が GPT-5.6 Luna の API 価格を **80%**、Terra を 20% 引き下げ、Codex と ChatGPT Work の利用量カウントにも反映した。

**詳細**: 7/30 の発表で、Luna は入力 $1 / 出力 $6 から **$0.20 / $1.20** へ、Terra は入力 $2.50 / 出力 $15 から $2 / $12 へ下がった（いずれも100万トークンあたり）。最上位の Sol は据え置きだが、API に fast option が加わり、標準の最大2.5倍の速度を2倍の価格で選べるようになった。OpenAI は値下げの理由を GPT-5.6 の内製開発で得た効率化——本番コードをモデル自身に書き換え・最適化させたことと、トークン生成の改善——と説明している。値下げは API だけで完結せず Codex と ChatGPT Work の利用量カウントにも反映されるため、同じ契約のまま実行できる量が増える。一次発表（`openai.com/index/`）はソース側の実行環境から到達できず、金額は複数の二次報道（CNBC / Axios / Yahoo Finance）が一致した値を採っている。

**意味**: 安価帯を主戦場にしている構成では、月次のトークン単価前提を引き直す必要がある。Luna は5分の1になったので、これまで「LLM に投げると高くつく」として除外していた分類・抽出・要約のバッチ処理が再検討の対象に戻る。Sol の fast option は速度2.5倍に対し価格2倍なので、単価ではなくレイテンシが律速になっている用途に限れば正味の得になる。社内展開の頭打ちを価格で説明していた場合は、Codex / ChatGPT Work 側の枠も緩むため前提が変わる。

- https://openai.com/index/gpt-5-6/
- https://www.cnbc.com/2026/07/30/open-ai-price-cut-gpt.html
- https://www.axios.com/2026/07/30/openai-cuts-prices-gpt-terra-luna5
- https://finance.yahoo.com/technology/ai/articles/openai-cuts-gpt-5-6-173045044.html

### 2. GitHub が Copilot code review の agent skills と MCP を GA にした — レビュー基準を1か所に集約できる

**要点**: GitHub が Copilot code review の agent skills / MCP サーバー対応を正式提供に切り替え、Pro から Enterprise までの全有料プランで使えるようにした。

**詳細**: 7/29 の GA で、レビュー時に2種類の外部文脈を差し込めるようになった。agent skills は `.github/skills` 配下のサブディレクトリに `SKILL.md` を置くと、リポジトリや組織に固有のコーディング標準・社内ツールをレビュー中に呼び出せる仕組みで、Claude Code や Codex CLI が使う skills と同じ配置規約に沿う。MCP サーバー接続は課題管理・ドキュメント・サービスカタログなど既存の社内基盤から文脈を引くもので、**GitHub MCP と Playwright MCP** が既定で有効になっている。安全側の制約として、code review が行う MCP のツール呼び出しは読み取り専用に限定される。skills や MCP の文脈を使って生成されたコメントには、その旨が併記される。

**意味**: これまでレビュー観点の統一は CONTRIBUTING や lint ルールに書き下す必要があったが、`SKILL.md` 形式なら Claude Code 側の資産と置き場所の規約を揃えられる。複数のエージェント CLI を併用している環境では、レビュー基準を1か所に集約する現実的な足場になる。MCP 呼び出しが読み取り専用に固定されている点は、情報システム部門への説明材料としてそのまま使える。

- https://github.blog/changelog/2026-07-29-copilot-code-review-agent-skills-and-mcp-now-generally-available/

### 3. Power Automate デスクトップフローの3機能が 7/16 に GA 済みだった — 2週間の取りこぼしを回収した

**要点**: PGP 暗号化・復号、時間/コスト削減の自動計測、デスクトップフローチェッカーの管理者通知の3つが、いずれも **7/16** に GA していた。

**詳細**: Release Wave 2026 Wave 1 の Power Automate 計画機能テーブルを精査したところ、General availability 列に Jul 16, 2026 の実日付（緑チェック）が付いた3機能が未収録だった。① PGP による暗号化・復号は、OpenPGP 互換の公開鍵・秘密鍵を使うアクションがアクションピッカーに追加されたもので、受信者の公開鍵でファイルやペイロードを暗号化し、対応する秘密鍵とパスフレーズで復号する。標準 PGP フォーマット対応のため PGP 前提の外部システムと相互運用でき、自動有効化ではなくアクションを追加して鍵とパスフレーズを設定する使い方になる。② 時間・コスト削減の自動計測は、成功実行を基に節約時間を算出する組み込みルールで、手作業時の所要時間を定義するとフロー実行データから節約時間が計算され、時間単価や独自の金額ベースラインを当てると実行回数に比例したコスト削減額が出る。③ デスクトップフローチェッカーの管理者通知は、ポータルのチェッカーが持つルールベース静的解析を環境内の全デスクトップフローに広げ、違反時の通知種別（エラー / 警告 / 情報）・重大度・しきい値・再発条件・スコープを管理者が設定できるようにしたもので、フロー初期化・解析時と同じルールエンジンを使い既定ルールとカスタムルールの両方を読み込む。Power Automate Blog も Power Platform Blog も7月の更新記事を出しておらず、この3件は Release Wave の緑チェックだけが唯一の一次シグナルだった。

**意味**: 3件とも「実行の失敗や支援エスカレーションが起きる前に品質と効果を可視化する」系で、CoE 運用にそのまま効く。とくに②は、RPA の投資対効果の説明を Excel の手集計でしのいでいる現場に対して、プラットフォーム標準で置き換えられる提案材料になる。③はメーカー任せになりがちなデスクトップフローの品質を管理者側の統制ラインに乗せられるため、研修カリキュラムのガバナンス回に追加する候補になる。

- https://learn.microsoft.com/en-us/power-platform/release-plan/2026wave1/power-automate/planned-features
- https://learn.microsoft.com/en-us/power-platform/release-plan/2026wave1/power-automate/encrypt-decrypt-data-pgp
- https://learn.microsoft.com/en-us/power-platform/release-plan/2026wave1/power-automate/measure-time-cost-savings-desktop-flows
- https://learn.microsoft.com/en-us/power-platform/release-plan/2026wave1/power-automate/configure-notifications-desktop-checker-admin-portal

## カテゴリ別まとめ

### コーディングエージェント / 開発ツール

- **GitHub Copilot code review** — （ハイライト参照）
- **Copilot CLI v1.0.76** — GitHub が安定版を v1.0.75（7/24）以来6日ぶりに更新した（7/30）。`/plugins` からプラグイン・instructions・エージェント・LSP サーバー・フックを個別に有効化／無効化できるようになり、モデルとして **grok-4.5** に対応した。複数の同時セッションを切り替え・生成・監視する Sessions サイドバー、キュー済みメッセージを並べ替え・編集できるキューマネージャ、AI クレジット上限を予測する `/limits predict`、macOS / Windows での音声モードの一時停止と再開も入った。サンドボックスは相対パスとシンボリックリンクを含む拒否パスを macOS / Linux で強制するようになり、管理者は MDM 経由の managed settings で制限的ポリシーを組織に適用できる。フックの出力は1回あたり10 MiB に上限が付き、MCP ツールは定義スコープのスナップショット経由で読み込みが速くなった。翌日には pre-release v1.0.77-0 が出ており、対話端末の既定ログインをブラウザ OAuth に変更している（リモート／ヘッドレスは device code のまま）。
  https://github.com/github/copilot-cli/releases
- **Cursor の iPad 対応** — Cursor が iPad 版を全有料プランに開放し、iPhone と共通の受信箱を追加した（7/29）。レビュー画面は差分だけでなく PR 全体——コメント・チェック・承認——を扱うよう作り直され、レビュアーの追加や変更、コメントを読んでエージェントに解決を指示する操作ができる。iPad 版はサイドバーのチャットを固定して複数エージェントの実行を並べて監視でき、分割画面でレビューとチャットを併置できる。スクリーンショットを添付して任意の位置にコメントを落とす、または Apple Pencil で直接描き込む操作にも対応した。1つのチャットが複数の PR を作った場合に、最後の1件だけでなく全てを開けるようになっている。
  https://cursor.com/changelog/ipad
- **Codex CLI と Claude Code は据え置き** — OpenAI は pre-release を 0.147.0-alpha.2（7/30）まで1本刻んだだけで、安定版は 7/29 の 0.146.0（Agent Plugins・追加マーケットプレイスに Amazon Bedrock と Claude Code）から動いていない。Anthropic 側も Claude Code が v2.1.220（7/25）のままで、7/26〜31 の7日間に新バージョンが出ていない。Claude Platform の release notes も最新エントリが 7/24 のままである。
  https://github.com/openai/codex/releases
  https://code.claude.com/docs/en/changelog

### Copilot Studio / Power Platform

- **Power Automate の3機能 GA** — （ハイライト参照）
- **統合 Power Apps は GA 未反映のまま7月が終わった** — Microsoft は本日 GA 予定と見込まれていた「Build better forms with integrated Power Apps」を、Release Wave 上で緑チェックなしの「Jul 2026」表記に据え置いている（二次ソースは 7/31 GA と報じていた）。この機能は有人デスクトップフローの入力 UI としてキャンバスアプリをそのまま使えるようにするもので、指定アプリがユーザー端末で開き、フロー側からコンテキスト・状態・値を渡して事前入力でき、ユーザーの入力値はフローに戻って後続ステップを駆動する。ボタンクリック等のアプリ側イベントから特定のサブフローを呼べるため、逐次実行ではなくイベント駆動の構成が組める。Public preview は 5/29 に済んでいる。同様に7月 GA 予定だった「ワークキュー項目の CSV エクスポート」「マシンとフローの稼働率をダッシュボード表示」、Power Apps 側の「code apps のコネクタを CLI で検出・作成・接続」「FetchXML エディターでのオフラインプロファイル構成」も未反映で、いずれも8月にずれ込む前提で見ておく方が安全になる。
  https://learn.microsoft.com/en-us/power-platform/release-plan/2026wave1/power-automate/build-better-forms-integrated-power-apps
- **Copilot Studio の基盤ビルドは7月ゼロ更新で確定した** — Microsoft は Released Versions の基盤ビルドを 2026.6.3（6/30 初出）に据え置いたまま、火曜定例の 7/7・7/14・7/21・7/28 のいずれでも新ビルドを出さずに7月を終えた。リージョン分布も無変化で、2026.6.3 が11リージョン、UK / Asia / UAE / Japan / Europe が 2026.6.2、Australia / US 本体 / GCC が 2026.6.1 にとどまる。次の定例更新は 8/4（火）にあたる。
- **Microsoft 一次ソースは全面据え置き** — Copilot 側の定例ソースは 7/31 時点でいずれも動いていない。Copilot Studio What's New は節構成が June 2026 のままで7月節が未公開、M365 Copilot Release Notes も「July 15, 2026」が最新のままで 7/29 見込みだった次バッチが出ておらず（次は 8/5 前後の見込み）、M365 Roadmap の最新アナウンスは 7/9 の GPT-5.6 から動いていない。Power Platform Blog の月次「What's New in Power Platform: July 2026」は7月中に公開されずに終わり、最新は 6/11 の June Feature Update のままである。Message Center も本日の新規検知はない。
  https://learn.microsoft.com/en-us/microsoft-copilot-studio/whats-new

### AI モデル / プロダクト

- **Grok 4.6 と 4.7 のパラメータ規模が分離した** — 二次報道は Musk が 7/28 に示した内容として、Grok 4.6 を **1.5T** パラメータ（SFT と RL を大幅改善）、Grok 4.7 を **2.1T** パラメータと書き分けている。当サマリーは 07-30 時点で 4.6 について「2T 説と 1.5T 説が併存」と記録していたが、2T 相当の数字は 4.7 側を指していた可能性が高い。時期は 4.6 が 8/7 前後、4.7 がその数週間後（8月下旬〜9月上旬）で、いずれも公式ドキュメントでの確認は取れていない。
  https://www.roic.ai/news/musk-signals-rapid-grok-rollout-46-in-two-weeks-47-a-month-later-07-28-2026
- **Google Docs のコメント支援に Gemini が入った** — Google が Google Docs にコメント支援のワークフローを追加し、Gemini が文書全体のコメントを読んで要約し、返信の下書きまで行えるようにした。あわせて Docs の生成機能の対応言語を11言語（北京語・オランダ語・マレー語・ヘブライ語・ポーランド語・トルコ語・チェコ語・インドネシア語・スウェーデン語・デンマーク語・ノルウェー語）拡大している。7/22 に告知された Gemini Alpha → Gemini Beta の改称は、7/30 から Scheduled Release ドメインへの全面展開に入った。
  https://workspaceupdates.googleblog.com/2026/
- **Gemini 3.5 Pro は未 GA が続いている** — Google は 3.5 Pro を Vertex AI の限定 preview に留めたままで、7/30 に確認した範囲でも新しい GA 告知はない。公開 API の GA 済みフラッグシップは Gemini 3.1 Pro から動いていない。前日サマリーで触れた「Polymarket が 7/31 の発表を約81%と見込む」節目は、本日時点で外れる方向にある。
- **Alibaba が Qwen3.7 Flash を公開した** — Alibaba が Qwen3.7 Flash を 7/27 に公開し、7/29 に LLM Gateway へ登録された。上位の Qwen3.8-Max-Preview は選定済みのホスト製品経由での提供に留まり、オープンウェイト版は「今後」とされている。いずれも集約サイト経由の情報で、一次のモデルカードには到達できていない。Kimi K3 側は 7/29〜31 で新しい動きがない。
  https://llmgateway.io/timeline

### 規制・政策

- **EU デジタルオムニバス（AI Act 改正）が発効した** — Regulation (EU) 2026/1744 が 7/24 に EU 官報へ掲載され、8/2 期限が迫るため異例の「緊急」扱いで3日後の 7/27 に発効した。Annex III の高リスク AI（採用選考・与信スコアリング・法執行の意思決定支援・国境管理）の適用開始が **2027年12月2日** へ約16カ月延期され、Annex I（医療機器・機械・民間航空機器・昇降機などの安全部品として組み込まれる AI）は 2028年8月2日 になる。一方で **8月2日の透明性義務の期限は据え置き**で、さらに 2026年12月から合意なき性的画像（NCII）・CSAM 生成機能の禁止が追加された。EU 圏の採用・与信領域での AI 導入提案はコンプライアンス期限を2027年末基準に引き直せる一方、透明性表示は来週が期限で猶予がない。
  https://lawandtechnology.eu/en/digital-omnibus-on-ai-official-journal-regulation-2026-1744/
  https://www.gibsondunn.com/eu-ai-act-omnibus-agreement-postponed-high-risk-deadlines-and-other-key-changes/
- **ホワイトハウスのフロンティアモデル自主フレームワークは 8/1 期限が目前に来ている** — 6/2 大統領令の60日期限が 8/1 に満了し、それに合わせて OpenAI / Anthropic / Google DeepMind との自主フレームワーク公表が見込まれる段階のままである。内容は公開前に最大30日の政府セキュリティレビュー枠を設けるもので、Meta は参加要請を受けつつ未合意にとどまる。現行案がクローズド API の3社を前提に設計されている点も既収録から変化していない。次回ダイジェストで正式発表の有無を確認する。
  https://www.techtimes.com/articles/321497/20260724/voluntary-paper-mandatory-practice-white-house-ai-review-hits-august-1-deadline.htm

### AI セキュリティ

- **Claude の共有チャットが検索エンジンにインデックスされた** — Claude の Share 機能で生成した会話ページと Artifacts が、検索エンジンの除外設定不備で公開インデックスされていた。7/25 に Reddit で `site:claude.ai/share` により閲覧できると指摘されて表面化し、露出内容には健康・医療記録、子どもの氏名と電話番号、暗号資産ウォレットの鍵、企業の社内文書が含まれた。Anthropic は robots.txt を更新し、7/27 までにインデックス済みコンテンツの大半を削除して、利用者に共有リンクの棚卸しを推奨している。ChatGPT（約1万件）・Grok（約37万件）に続く主要ベンダー3例目で、**製品の脆弱性ではなく共有機能の既定設定**に起因する点が共通している。エンタープライズ提案では、モデル選定や API 権限とは別に「共有リンクの発行可否・失効・棚卸し」を管理項目として明示する必要がある。
  https://admina.moneyforward.com/jp/blog/claude-shared-chat-google-index

### 運用 / エンタープライズ

- **GitHub が Copilot の既定モデル有効化ポリシーを導入した** — GitHub が Copilot Business / Enterprise 向けに、GA になったモデルを管理者の手動操作なしで既定有効にするポリシーを追加し、厳格な統制が要る組織向けに単一のオプトアウトを用意した（7/29）。最初の **28日間**は設定は可能だが実効はなく、利用者側は何も変わらない。**8/26** にポリシーが発効し、明示設定されていないモデルの表示が「unconfigured」から「inherits default」に変わってポリシー設定に従い始める。モデル選定を組織で統制している場合、この28日が実質の猶予になる。
  https://github.blog/changelog/2026-07-29-default-model-enablement-for-copilot-business-and-enterprise/
- **Meta のインフラ VP が「追いつくのに20カ月」と述べた** — VB Transform 2026 のセッションで Meta の VP of Engineering Barak Yagour が、同社データ基盤に到達するエージェント由来のクエリが半期で **30倍**に増え、キャパシティ・ID・速度が同時に破綻しつつあると説明した。既存のエンタープライズ基盤は人間の利用を前提に構築されており、追いつくための猶予は約20カ月との見立てになる。2月に投入した agentic data apps は3カ月で社内公開ダッシュボードの63%が新ツール製になった。既収録の「57%が誤答をコンテキスト欠落に特定・統制されたコンテキストレイヤの本番稼働は25%」と同じ方向で、エージェント導入の隘路がモデルではなくデータ基盤側にあることを示す供給側の実データにあたる。
  https://venturebeat.com/data/we-have-maybe-20-months-to-rebuild-for-ai-agents-metas-infrastructure-vp-tells-vb-transform-2026

### 市場・決算 / インフラ

- **Apple の FY26 Q3 決算で Cook が Siri の Gemini 依存を追認した** — Apple が売上$111.2B（+16.6%、市場予想$109.7B 超）、希薄化後 EPS $2.01、粗利率49.3%、Services が過去最高の$30.98B を計上した（7/30）。Tim Cook にとって最後の決算コールで、9/1 に John Ternus が CEO に就任する。AI 面では第3世代 Apple Foundation Models が Google の Gemini モデル技術との協業で構築され、オンデバイスの約30億パラメータモデルからクラウド側まで一貫すると説明し、Cook は Q&A で「Google との協業は順調」と述べた。7/10 の Apple × OpenAI 提訴・Siri の Gemini 切替が、決算の場で公式に既定路線として確認された形になる。
  https://www.cnbc.com/2026/07/30/apple-earnings-live-updates.html
- **Amazon の FY26 Q2 は確報値を確認できていない** — Amazon が 7/30 17:00 ET に決算を発表・電話会議を行ったが、一次 IR ページと CNBC 記事本文がいずれも403でソース側から確報値を確認できていない。二次情報も数値が割れており、売上$181.52B（+16.6%）・EPS $2.78・AWS +28% とする記述と、会社ガイダンス$194–199B／コンセンサス$196.9B を前提とする記述が混在する。前者はガイダンス下限を大きく下回って整合しないため採用しない。確定している事前情報は、会社ガイダンスが売上$194–199B（+16〜19%）、AWS のコンセンサスが$40.6B（+31.6%）、2026年 capex 計画が約$200B（BofA 等はメモリ価格上昇を理由に$210B への上方修正を想定）。AWS 成長率と capex ガイダンスは 08-01 分で確報を追う。
- **AMD と Anthropic が最大2GW の MI450 提携を結んだ** — Anthropic が AMD Instinct MI450 シリーズ（MI455X）を Helios ラックスケールで最大2GW 導入し、第1GW を2027年上期に配備開始する（7/22 発表・取りこぼし収録）。AMD は Anthropic へ最大 **$5B** の戦略的出資を行うが、一括ではなく配備マイルストーン連動で支払う。構成は EPYC「Venice」CPU・Pensando ネットワーキング・ROCm になる。これで Anthropic の計算基盤は Nvidia / Google TPU / AWS Trainium / AMD Instinct の4ベンダー構成になり、Meta からの最大$10B リース協議（7/17）・Samsung との独自チップ協議（7/2）と合わせて「調達先の分散」が同社の一貫した方針として確認できる。単一アクセラレータ前提のコスト試算は前提を置き直す必要がある。
  https://ir.amd.com/news-events/press-releases/detail/1292/amd-and-anthropic-announce-strategic-partnership-to-deploy-up-to-2-gigawatts-of-amd-instinct-mi450-series-gpus

### 国内動向 / 新興ツール

- **ソフトバンクが「GaranAI」のベータ版を始めた** — ソフトバンクが、日本のコンテンツ産業と生成 AI 開発の両立を狙うデータエコシステム基盤のベータ版を開始した（7/22）。共同通信社・毎日新聞社・産経新聞社に加え、信濃毎日新聞社・デーリー東北新聞社などの地方紙を含む **30社超**がデータ提供を表明している。多段階の加工で著作物を保護しつつ、コンテンツホルダーへの収益還元と AI 開発事業者への良質な学習データ供給を両立させる設計で、専任チームが収集から加工まで一貫して担当し、約半年のベータ運用でデータ品質監視と加工ロジックを改善する。2027年1月以降に正式提供（名称変更予定）となる。国内の学習データ調達・権利処理を外部化する選択肢として、コンテンツ系クライアントの提案材料になる。
  https://www.softbank.jp/corp/news/press/sbkk/2026/20260722_01/
- **Product Hunt のローンチがエージェントの埋め込み型に寄った** — 7月のローンチは開発者向けインフラとエージェント特化ツールが中心で、汎用チャットボットから組み合わせ可能な部品への移行が続いている。AnySearch（エージェント向けのリアルタイム構造化データ取得、560票超）、Sim（エージェントとワークフローを構築・管理する OSS ワークスペース）、Framer AI Agents（キャンバス上のエージェントがサイトの設計・執筆・分析を担当）、PlugThis（対話で Chrome 拡張を生成）が目立つ。GitHub Trending 側も同様に、コーディング／ペンテスト／取引の各エージェントとそれを繋ぐ MCP サーバー・AI ゲートウェイが上位を占める。
  https://www.producthunt.com/leaderboard/monthly/2026/7

## 直近の注目予定

- 7/31（本日）: Devin classic 環境設定 read-only 参照終了 ／ Copilot から Gemini 2.5 Pro・Gemini 3 Flash 廃止
- 8/1: covered frontier model 60日 EO 期限 ／ Copilot in 30（SMB 向けトライアル）の CSP 提供開始
- 8/2: EU AI Act の透明性義務 適用期限（オムニバス改正でも据え置き）
- 8/3: 旧「Claude in Slack」退役
- 8/4: Released Versions・Release Wave・非推奨一覧・拡張機能 What's New の定例更新
- 8/5: Opus 4.1 Claude API 退役 ／ Cowork 倍増利用枠終了 ／ M365 Copilot Release Notes 次バッチ見込み
- 8月第1週: Power Platform Weekly の夏季休刊明け
- 8/7 前後（推定）: Grok 4.6（1.5T）
- 8/9: ChatGPT Atlas シャットダウン
- 8/17: Claude Console 旧 Workbench 退役 ＋ 実験的プロンプトツール API 廃止
- 8/26: OpenAI Assistants API 廃止 ／ o3 退役 ／ GPT-4.5 完全廃止 ／ Copilot 既定モデル有効化ポリシー発効
- 8月下旬: Purview DLP 外部メール除外の GA 展開完了予定
- 8月下旬〜9月上旬（推定）: Grok 4.7（2.1T）
- 8/31: Sonnet 5 促進価格終了（→ $3/$15） ／ Power Automate モバイルアプリ廃止
- 8月見込み: 統合 Power Apps GA ／ ワークキュー項目の CSV エクスポート ／ マシン・フロー稼働率のダッシュボード表示
- 9/1: Apple CEO が John Ternus に交代
- 9月: iOS 27 / macOS 27 GA（AFM 3 本番）
- 時期未定（数週間内）: Cowork 1 提供開始
- 2027年1月以降: ソフトバンク GaranAI の正式提供
- 2027-12-02: EU AI Act Annex III（高リスク）の適用開始
- 2028-08-02: EU AI Act Annex I の適用開始

## 改善メモ

- **前日（07-30）分の欠損リカバリを実施した**: 07-30 サマリー生成時に未取得だった 02_ai-news-Copilot の 07-30 分ダイジェストが本日は取得できたため、`daily/2026/ai-news-daily-2026-07-30.md` を3ソース統合で再生成して上書きした（別コミット）。回収した主な内容は Copilot Studio「エージェント提案」の 7/30 GA、Foundry IQ 接続・Teams Phone Agent 連携・条件グループの各 Preview、Purview DLP × Entra Global Secure Access、Cowork のモデル／ブラウザー統制。ソース側ルーチンの失敗ではなく、想定の 06:10 頃に間に合わずコミットが遅れた形になる。
- **提案番号 B-018 が2ソースで衝突している**: Master の B-018（OpenAI 系5ソースの到達不可を `daily-sources.md` に明記）と Copilot の B-018（Release Wave の GA 済みチェックマークを日次で差分監視）が同じ番号を使っている。台帳がソースごとに独立しているため実害はないが、本サマリーから横断参照するときは必ずソース名とセットで書くこと。
- **Grok のパラメータ規模の記述を整理した**: 07-30 サマリーは Grok 4.6 について「2T 説と 1.5T 説が併存」と記録していたが、Master の 07-31 分は 4.6 = 1.5T / 4.7 = 2.1T と書き分けており、2T 相当の数字は 4.7 側を指していた可能性が高い。いずれも二次報道のみで公式確認は取れていない。
- **Amazon の決算確報が未確認である**: industry が一次 IR と CNBC の両方で403に当たり、二次情報も数値が割れているため本サマリーでも確報値を採用していない。08-01 分で確報を追う。
- industry: 新規提案 B-008（週1回の取りこぼし検知スイープ、TLDR AI を高優先へ）。継続提案4件（最多は B-004 取得方法欄の WebSearch 優先化、32回目）。新規の障害なし。
- Copilot: 継続提案8件を再確認（最多は B-011 Power Platform Blog のトピック記事照合、12回目）。障害の変化として `www.ppweekly.com/feed` の WebFetch 403 を新規登録（夏季休刊中のため影響は限定的だが、8月の再開時に改めて疎通確認する）。
- Master: 継続提案5件（最多は B-013 403 の2分類記録、5回目）。障害の変化として `openai.com` / `help.openai.com` / `developers.openai.com` / `x.ai` の4ホストを、従来の「403」記録から**ゲートウェイ拒否**（CONNECT 403）へ再判定した。`www.anthropic.com` は curl で HTTP 403 が返るためオリジン 403 のままで、B-013 の2分類の区別が実際に働いた例にあたる。
