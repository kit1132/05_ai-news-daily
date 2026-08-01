# AI News Daily Summary — 2026-08-02

日曜の主題は3つ。EU AI Act 第50条が本日発効して欧州委員会が執行を開始したこと、DeepSeek が価格も構成も据え置いたまま V4-Flash の知能指数を10点上げて安価ティアの前提を動かしたこと、そして OpenAI が次期ファミリー Astra を未解決問題10件の解答とともに公表し、エージェントの想定稼働時間を数時間〜数日へ引き上げたことである。Microsoft 側は一次ソースがほぼ全面据え置きで、7月 GA 予定だった Power Platform の7機能は8月に入って2日が経っても反映されていない。

## 今日のハイライト

### 1. EU AI Act 第50条が発効し欧州委員会が執行を開始した — 既存システムだけ 12/2 まで猶予される二段構えになった

**要点**: 透明性義務が本日 **8/2** に発効し、AI Office と各国当局が執行を始めた。本日以降に市場投入するものは今日が期限で、8/2 より前に出したシステムの標識義務だけが 12/2 まで残る。締切は1本ではなく2本になった。

**詳細**: 義務の中身（チャットボットであることの明示、生成コンテンツの機械可読な標識）は 08-01 掲載分から変わっていない。本日あらためて確定したのは執行体制と行動規範の署名状況である。

- 執行の担い手: AI Office と各国当局が本日から動きはじめた。義務の主体は提供者に限らず、当該システムを使うだけの企業・組織・公的機関（デプロイヤー）も含まれる
- 行動規範: 欧州委員会が 2026-06-10 に公開し、7月末までに IT・通信・教育・小売など約 **190 組織**が署名した。Google と Meta も署名を表明している
- 署名の効果: 今後の執行が規範の遵守監視に絞られ、EU 全域での予見可能性と法的確実性、事務負担の軽減が得られる。監督当局の所在地は問わない
- 技術的手段: 規範はデジタル署名付きメタデータと知覚不能な電子透かしの2系統を挙げている
- ガイドライン: 委員会が 7/20 に AI Office 案を承認済みで、条文の開放的な文言を埋める位置づけにある
- 制裁: 上限は €15M か全世界年間売上高の3%の高い方（第99条・既収録）

対象は4分野（人との直接対話、AI生成コンテンツ、感情認識・生体分類、ディープフェイクと公益に関わるAI生成テキスト）で、EU 域内の事業者に限らず EU の利用者に製品が届く提供者すべてに及ぶ。なお欧州委員会の告知ページ（`digital-strategy.ec.europa.eu`）と条文サイト（`artificialintelligenceact.eu`）は本日ゲートウェイ拒否と判定されており、上記は検索スニペットと二次情報を経由した内容で、一次を直接読めていない。

- https://digital-strategy.ec.europa.eu/en/news/commission-starts-enforcing-ai-act-rules-and-new-transparency-requirements-2-august
- https://digital-strategy.ec.europa.eu/en/news/strong-backing-code-practice-transparency-ai-generated-content
- https://artificialintelligenceact.eu/transparency-rules-article-50/
- https://blog.google/company-news/outreach-and-initiatives/public-policy/eu-ai-act-transparency-code-of-practice/

### 2. DeepSeek が V4-Flash をポストトレーニングのやり直しだけで刷新した — 同じ価格・同じ規模で知能指数が 40→50 に上がった

**要点**: DeepSeek が 7/31 に V4-Flash の 0731 ビルドを公開した。構成も単価も4月版のまま知能指数だけが **50** へ上がり、安価ティアの見直しは「値下げを待つ」から「同価格の性能更新を追う」へ変わる。

**詳細**: 284B 総パラメータ / トークンあたり 13B アクティブの MoE、1M コンテキストで、アーキテクチャも規模も 4/24 の Preview から変えていない。差分はコーディング・エージェント・推論・ツール利用に振り直したポストトレーニングだけである。

- ベンチマーク: SWE-bench Verified 79%、Terminal Bench 2.1 は 82.7（V4-Pro-Preview は 72.1）、DeepSWE 54.4（旧 Flash 7.3）、DSBench-FullStack 68.7（同 37.0）。自社フラッグシップの V4-Pro-Preview に9ベンチ全勝している
- 価格: 入力 $0.14 / 出力 $0.28（100万トークンあたり・据え置き）。キャッシュヒットは $0.0028 で98%引き
- 対 GPT-5.6 Luna: Artificial Analysis Intelligence Index は 50 で max の51 に1点差、タスク単価は約60%安い。7/30 の GPT-5.6 値下げ（既収録）を織り込んでもこの差が残る
- API: Responses API 形式に対応し、Codex への適応が済んでいる。投機的デコードモジュールを同梱する

数値の扱いには留保が要る。9本すべてが DeepSeek 自身の計測で、うち2本は社内ベンチ、ハーネスは社外に公開されていない。Artificial Analysis は出力が冗長である点を注記している。

0731 の重みがオープンウェイトとして公開されたかは、ソース間で記述が割れている。Industry 側は「MIT ライセンスでウェイト公開」とし、Master 側は「HF の MIT ライセンス重みは4月 Preview のままで 0731 は API 限定」とする二次情報と正面から矛盾していると記録した。`huggingface.co` / `www.deepseek.com` / `api-docs.deepseek.com` がいずれもゲートウェイ拒否で一次確認ができないため、本サマリーでは両論を併記して未確定として扱う。第三者の量子化リポジトリが `unsloth/DeepSeek-V4-Flash-0731-GGUF` の名前で存在する点は、重みが入手可能である側の傍証になる。

- https://the-decoder.com/new-deepseek-flash-model-matches-openais-gpt-5-6-luna-at-roughly-60-percent-lower-cost/
- https://artificialanalysis.ai/articles/deepseek-v4-flash-0731-scores-50-on-the-artificial-analysis-intelligence-index-10-points-above-previous-deepseek-v4-flash
- https://www.marktechpost.com/2026/07/31/deepseek-upgrades-deepseek-v4-flash-0731-with-major-agentic-and-coding-gains/
- https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-0731

### 3. OpenAI が次期ファミリー Astra を未解決問題10件の解答とともに公表した — エージェントの想定稼働単位が数分から数日へ延びる

**要点**: OpenAI が 8/1 に未公開の次期ファミリー **Astra** を公表し、10年以上未解決だった数学・理論計算機科学の10問を解いたと発表した。1リクエスト数分を前提にしたコスト試算・監視・権限設計は、数時間〜数日走る前提へ引き直す必要が出る。

**詳細**: 内部版が生成した結果を、機械検証可能な形で外部に出している。

- 対象領域: von Neumann 代数、球充填、回路計算量、Ramsey 理論など10件。いずれも10年以上（多くはそれ以上）進展がなかった問題である
- 検証: 全結果に Lean 4 の証明証明書を添付し、249ページの原稿とあわせて GitHub で公開した。要した API 計算コストは約 **$2,000**
- 設計: 複数のサブエージェントを並列に起動・調整して成果を統合し、計画・実行・検証・修正を長時間にわたって継続する構成を取る
- 位置づけ: GPT-6 として出すか GPT-5 系列に収めるかは未定である。Altman はワシントンで議員向けにデモ済み

公開時期は規制側の進捗にも左右される。6/2 大統領令 EO 14409 が求める公開前30日の政府レビュー枠組み（下記・本日時点で未公表）が最初に適用される対象になる見込みで、モデルの完成と公開日が直結しない。

- https://the-decoder.com/openai-announces-its-next-major-model-astra-by-dropping-ten-previously-unsolved-math-solutions/
- https://the-decoder.com/openai-is-reportedly-building-astra-a-model-family-designed-to-work-on-problems-for-hours-or-days/
- https://www.developersdigest.tech/blog/openai-ten-advances-mathematics-lean-2026

## カテゴリ別まとめ

### Anthropic / Claude

- Anthropic が Claude Code の週次上限50%増を 8/19 まで延長していたことが本日判明した — 当初は 7/19 が期限だったものを1ヶ月延ばした形で、Pro / Max / Team / seat-based Enterprise の対象アカウントに自動適用される。当リポジトリで未追跡だった分にあたる。適用が `/usage` に反映されないという報告もあるため、上限の実効値は画面表示ではなく実運用で確かめる必要がある。
  https://www.helpnetsecurity.com/2026/07/13/claude-code-weekly-limits-promotion-extended/
- Anthropic の AI for Science 希少疾患グラントは本日 8/2 が応募締切である（現地 23:59 PT ＝ 8/3 午後 JST）— 6ヶ月で最大 $50,000 分の Claude クレジットを提供する。基礎研究トラックと、希少疾患の臨床開発を速める初期段階バイオテック向けトラックの2本立てで、前者は Monarch Initiative が初期パートナーに入る。応募には研究機関または適格バイオテックへの所属が要る。
  https://www.anthropic.com/news/rare-disease-research-grants
- Anthropic は Claude Code を9日連続で更新していない — 最新は v2.1.220（7/25）のままである。Claude Developer Platform の release notes も 7/24 エントリが最新で、7/25 以降の追加はない。
  https://code.claude.com/docs/en/changelog

### OpenAI

- OpenAI が次期ファミリー Astra を公表した（ハイライト参照）
- OpenAI は Codex CLI を 7/31 から動かしていない — 安定版は 0.146.0（7/29）、pre-release も 0.147.0-alpha.4（7/31 17:54 UTC）が最新のままである。7/31 の SynthID 透かし開始（既収録）以降、新しい製品発表も出ていない。登録済み OpenAI 系5ソースは引き続き全て到達不可で、確認は WebSearch のみに依存している。
  https://github.com/openai/codex/releases

### Google / DeepMind・xAI

- Google が Gemini API のモデル廃止を8月に集中させている（一次未確認）— 画像生成モデル群を 8/17、`gemini-robotics-er-1.6-preview` を 8/31 に停止する。Gemini Enterprise 側では Grok 4.1 ファミリーを 8/20 に停止し、8/4 には global リージョンから Gemini 3.5 Flash を外す。`ai.google.dev` が本日ゲートウェイ拒否のため changelog 本体で裏を取れておらず、依存があるなら自分の環境で退役告知を確認したほうがよい。
  https://ai.google.dev/gemini-api/docs/changelog
- Google DeepMind の Gemini Robotics 2（7/30・既収録）は3モデル構成であることが本日補足された — Gemini Robotics 2 / Gemini Robotics ER2 / Gemini Robotics On-Device 2 の3本立てで、On-Device 2 はロボット側でローカル実行する VLA（視覚-言語-行動）モデルにあたり、数時間分のデータで未知の機体へ適応できる。Google は消費者向けロボットを近く投入する予定はないとしている。
  https://deepmind.google/blog/gemini-robotics-2-brings-whole-body-intelligence-to-robots/
- xAI の Grok 4.6 は 8/7 前後という見通しから動いていない — Grok 4.5 と同じ 1.5T の V9 基盤を再利用し、SFT と RL の改善で性能を上げる位置づけとされる。後続の Grok 4.7（2.1T）は数週間後になる。いずれも Musk の 7/28 発言の二次報道で、公式ドキュメントでの確認は取れていない。
  https://americanbazaaronline.com/2026/07/28/elon-musk-says-grok-4-6-is-weeks-away-grok-4-7-to-follow-soon-485356/

### Microsoft / Copilot Studio / Power Platform

- Microsoft が M365 Copilot の展開ベンチマークを一次公開した（7/30 記事・本日検知）— 有償3,000万シート自体は 7/30 ダイジェストで決算経由で収録済みだが、定着の速さと使われ方の実測値が出たのは今回が初めてである。導入の成否を測る物差しが「何席入れたか」から「月間アクティブ80%超に何日で届いたか・複数機能を併用しているか」へ移る。
  https://www.microsoft.com/en-us/microsoft-365/blog/2026/07/30/the-next-measure-of-ai-momentum-is-work-transformed/
  - 定着スピード: 月間アクティブ利用率80%超への到達に要する期間が、この1年で「数か月」から「数日」へ短縮した
  - 利用の深さ: ユーザーあたり会話数が前年比でほぼ2倍。複数機能を併用するユーザーは3桁%成長で、週次エンゲージメントは Outlook・Teams と同水準に並んだ
  - 大口: 5万シート超の顧客数が前年同期比7倍。情報労働者の過半へ展開した企業の数は前四半期比で約75%増
  - Cowork: 実行されたワークフローの49%が複数ステップの作業で、単発の分析タスク（29%）を上回った
  - 業種と事例: エージェント採用の伸びが最も速いのは自動車とヘルスケアで、稼働エージェント数の絶対値では製造・銀行・ソフトウェアが最上位のまま。Premera Blue Cross が900超のエージェントで契約処理を30〜45分から3分に短縮し、Eaton が対象業務のサイクルタイムを75%削減、Levi Strauss が1日で18,000タスクを棚卸しした
- 7月 GA 予定だった Power Platform の7機能は、8月に入って2日が経ってもいずれも GA が反映されていない。Release Wave の General availability 列を本日も差分確認したが、緑チェック（実日付）が付いた行は 7/16 の3機能（PGP 暗号化・復号、デスクトップフローの時間/コスト削減の自動計測、チェッカーの管理者通知）から増えていない。
  https://learn.microsoft.com/en-us/power-platform/release-plan/2026wave1/power-automate/planned-features
  - Power Automate（5件）: 削除したクラウドフローの復元、Process ライセンス容量の複数ワークフロー間での共有、統合 Power Apps によるフォーム UI、ワークキュー項目の CSV エクスポート、マシン・フロー稼働率のダッシュボード表示
  - Power Apps（2件）: code apps のコネクタ CLI 対応、FetchXML エディターでのオフラインプロファイル構成
  - 8月予定として列に載るのは、Power Automate ライセンスダッシュボードの改善（GA）、デスクトップフローのカスタムダッシュボードタイル（Public preview）、Dataverse オンラインモードのキャンバスアプリ対応（Public preview）、モデル駆動アプリの行要約強化（GA）である
- Microsoft の一次ソースは本日いずれも据え置きだった — M365 Copilot Release Notes は「July 29, 2026」節が先頭のままで新バッチが出ておらず（次バッチは隔週傾向なら8月中旬）、Copilot Studio What's New も June 2026 節から動いていない。Copilot Studio の基盤ビルドは 2026.6.3（6/30 初出）でリージョン分布も変わらず、次の火曜定例更新は 8/4 にあたる。M365 Roadmap の Latest announcements は 7/9 の GPT-5.6 のままで、Power Platform Blog は月次「What's New」の7月分を出さないまま8月に入った（最新は 6/11 の June Feature Update）。Message Center の新規 MC 検知もない。
  https://learn.microsoft.com/en-us/copilot/microsoft-365/release-notes
  - 一次未確認のため保留（7/31 以降同じ状態）: Copilot Dashboard の Power users insights が8月展開予定という情報を二次ソースで確認したが、Learn 側に該当記述がない
- Partner Center の8月アナウンスページ（`announcements/2026-august`）は本日時点でも 404 で未公開のままである — 8/1 に CSP 提供が始まった SMB 向けトライアル「Copilot in 30」（25ユーザー・30日）以降、新しい提供条件の変更は確認できていない。

### 開発ツール

- GitHub が Copilot CLI の pre-release v1.0.78-2 を公開した（8/1 04:18 UTC ＝ 8/1 13:18 JST）— 安定版は v1.0.77 のままで、内容は 7/31 の 78-0 で入った機能の不具合修正に寄っている。
  https://github.com/github/copilot-cli/releases
  - 分割ビューのサイドバー: 閉じる確認の文言を "x again to close" に改めた
  - 拡張機能のスラッシュコマンド: 1回の呼び出しにつき確実に1回だけ実行されるようにした
  - タイムラインをスクロールした後にインライン画像が描画されない不具合を直し、パイプ経由の stdin プロンプトでも `sessionEnd` フックが `-p` 指定時と同じ扱いになった
- GCC ステアリングコミッティが LLM 由来の重要なコード寄与を拒否する方針を採用した — Linux を支えるコンパイラ本体が、生成物由来のコードを著作権上の理由で明示的に締め出したことになる。OSS への寄与を伴う開発体制では、エージェント利用の可否がプロジェクト単位で分岐するため、寄与先のポリシー確認を開発フローへ組み込む必要が出る。次回見直しは2027年初頭に予定されている。
  https://lwn.net/Articles/1086041/
  - 対象: ChatGPT / Gemini / GitHub Copilot 等の出力そのものに加え、人間が後から編集・書き直したものも、最終的な寄与が生成物に基づく限り拒否される
  - 線引き: GNU プロジェクトのメンテナ指針にある「法的に重要（legally significant）」の閾値で、コード・テキストで約15行にあたる
  - 例外と許容用途: 些細な変更とメンテナが受け入れを選んだテストケースは対象外。アイデアの議論・既存コードの理解・不案内な領域の学習・一般的な調査への利用は認められる
- Supabase がコーディングエージェント評価ベンチ `supabase/evals` を Apache-2.0 で公開した — Claude Code / Codex / OpenCode を実際の Supabase タスク（スキーマ構築、Edge Function のデバッグ、壊れた RLS ポリシーの修正）で採点する仕組みで、公開リーダーボードと日次監視の社内回帰スイートを兼ねる。モデルの素の能力よりも Skills などの文脈供給の有無で差が埋まる構図が実測で出ており、エージェント導入提案ではモデル選定より社内ドキュメント整備の優先度が高いことの根拠に使える。
  https://supabase.com/blog/introducing-supabase-evals
  - Build 段階の素点は Opus 5 と Kimi K3 が100%
  - Skills を併用すると Sonnet 5 が 78%→100%、GPT-5.6 Sol が 89%→100%、GPT-5.4 mini が 78%→89% へ上がる
  - ドキュメント参照量は Codex / GPT-5.6 が1シナリオあたり約8ページ、Claude Code は約2ページ
- Cursor と Cognition の Devin はいずれも日付を確定できる新規リリースを確認できなかった — Cursor は iPad 対応と PR レビュー刷新（7/29）以降、Devin は7月分の集約更新以降で新しい動きがない。`cursor.com` と `docs.devin.ai` はゲートウェイ拒否のため、いずれも WebSearch が実質の一次になっている。Model Context Protocol のブログも 7/28 の仕様公開エントリから5日連続で動いていない。
  https://releasebot.io/updates/cursor
- Product Hunt の今週のローンチは既存画面への埋め込み型が中心である — 新しいアプリを開かせず、すでに使っている画面へ入り込む設計で共通している。Dune Keypad はキーボードに Claude 連携を組み込み、Mina Meeting Assistant はビデオ会議に、folk はテキストスレッドに埋め込む。AIエージェント分野の上位は音声・サポート・ワークフロー実行に寄っており、本番運用向けの音声スタックとして ElevenLabs と Vapi が目立つ。個別のローンチ日は特定困難のため幅を持たせている。
  https://www.producthunt.com/categories/ai-agents

### 規制・政策

- EU AI Act 第50条が発効し執行が始まった（ハイライト参照）
- ホワイトハウスのフロンティアモデル自主フレームワークは、8/1 の期限を越えた本日時点でも正式な公表が確認できていない — 6/2 大統領令 EO 14409 が課した60日期限は 8/1 に満了した。報道ベースでは OpenAI / Anthropic / Google と最終調整段階にあり、連邦政府に公開前30日のアクセスを与える内容とされる。作成を指示されたのは NSA / CISA / 財務省で、対象モデルの判定は NSA 長官の単独権限、レビューは商務省 CAISI と NSA が担う。Meta は不参加のままである。OpenAI の Astra（ハイライト参照）がこの枠組みを通る最初のモデルになる見込みで、公表の有無を次回も追う。
  https://vorplabs.com/ai-regulatory-updates/frontier-model-review-framework

### 資本・インフラ

- 欧州委員会が最大7拠点の AI ギガファクトリー入札を開始した（7/30 公告）— 公的資金（EU＋加盟国）最大 €10B に対し民間投資 €20B 以上を見込み、総額 €30B 超の計算基盤整備になる。稼働すれば EU 域内の計算能力は倍以上になる。
  https://digital-strategy.ec.europa.eu/en/news/eu-launches-ai-gigafactories-call-boost-europes-computing-capacity-and-unlock-more-eu30-billion
  - 日程: 締切は11月12日、採択は2027年初で着工も同年。契約締結後18カ月以内に建設・稼働を完了することが条件になる
  - 規模: 各拠点は先端AIチップを最低10万基備え、現在 EU 域内で稼働中のデータセンターの約4倍の性能を想定する
  - 応募主体: テクノロジー提供者・クラウド事業者・公的機関・投資家からなるコンソーシアムまたは SPV
  - 調達: 欧州委員会は AMD・Nvidia・Qualcomm と LOI を締結済みで、応札側のチップ調達経路を先に確保している

### 国内動向

- 令和8年版情報通信白書の企業側データが本日補足された — 7/27 ダイジェストで扱ったのは個人の利用率（58.8%・前年 26.7%）だったが、企業側は生成AIを1つ以上の業務で利用する割合が **86.4%**（2024年度 55.2%）に達している。国際比較で日本が明確に劣後しているのは利用率そのものではなく組織的な取組の有無で、「利用は広がったが業務変革の体制が無い企業が4社に1社」という定量根拠が新たに使える。
  https://www.soumu.go.jp/johotsusintokei/whitepaper/ja/r08/summary/summary01.pdf
  - 企業の方針: 「積極的に活用」または「領域を限定して活用」を定めている割合は日本 68.9%（前年 49.7%）。米国 90.9%・ドイツ 91.6%・中国 98.1%
  - 業務変革で「組織的な取組はない」と回答した割合は日本 **27.0%**、米国 1.4%、ドイツ 4.9%、中国 2.6%
  - 調査は2026年1〜2月に日本・米国・ドイツ・中国の4カ国で実施され、公表は 7/24 である

## 直近の注目予定

- **8/2（本日）**: EU AI Act 第50条の透明性義務発効 ／ Anthropic 希少疾患グラント応募締切（23:59 PT）
- **8/3**: 旧「Claude in Slack」退役 ／ 週次復旧チェック実施日（月曜） ／ iOS 27 developer beta 5（予想）
- **8/4**: Copilot Studio Released Versions・Release Wave・非推奨一覧・拡張機能 What's New の定例更新 ／ Gemini Enterprise の global リージョンから Gemini 3.5 Flash を除外（一次未確認）
- **8/5**: Opus 4.1 Claude API 退役 ／ Cowork 倍増利用枠終了
- **8/7 前後（推定）**: Grok 4.6（1.5T）
- **8/9**: ChatGPT Atlas シャットダウン
- **8/17**: Claude Console 旧 Workbench 退役 ＋ 実験的プロンプトツール API 廃止 ／ Gemini API 画像生成モデル停止（一次未確認）
- **8/19**: Claude Code 週次上限50%増の終了
- **8/20**: Gemini Enterprise Agent Platform の Grok 4.1 ファミリー停止（一次未確認）
- **8/26**: OpenAI Assistants API 廃止 / o3 退役 / GPT-4.5 完全廃止 ／ Copilot 既定モデル有効化ポリシー発効
- **8/31**: Sonnet 5 促進価格終了（→ $3/$15）／ Power Automate モバイルアプリ廃止 ／ `gemini-robotics-er-1.6-preview` 停止（一次未確認）
- **8月上旬**: Partner Center 8月アナウンスの公開（本日時点で 404）／ Power Platform Weekly 夏季休刊明け（#270・6/29 以降停止）
- **8月中旬**: M365 Copilot Release Notes 次バッチ見込み（7/29 バッチから隔週）
- **8月見込み**: 7月 GA 予定から持ち越した Power Platform 7機能 ／ Purview DLP 外部メール除外の GA 展開完了（下旬）
- **9月**: iOS 27 / macOS 27 GA（AFM 3 本番）
- **11/12**: EU AI ギガファクトリー入札の応募締切
- **12/2**: EU AI Act の生成コンテンツ標識義務、8/2 以前に市場投入済みシステムへの猶予が終了

## 改善メモ

- B-020（Master・新規）: 一次に到達できない状態でオープンウェイトの重み公開有無を判定する手順を `fetch-flow.md` に追加する。本日の DeepSeek 0731 で実際に判定できなかった項目にあたる
- B-020（Copilot・新規）: Microsoft 365 Blog 本体の新着判定に WebSearch 照合を併用する。7/30 記事を8/1 時点で 6/25 記事が最新と誤認していた原因にあたり、本日の唯一の一次検知はこの照合で拾えた
- B-010（Industry・新規）: 総務省 情報通信白書の確認頻度を、公開月（7月）は毎日へ引き上げる
- 継続提案: Master 5件（最多 B-013 7回目）、Copilot 9件（最多 B-011 14回目）、Industry 3件（最多 B-004 34回目）
- 障害: ゲートウェイ拒否として `ai.google.dev` / `digital-strategy.ec.europa.eu` / `artificialintelligenceact.eu` / `www.deepseek.com` / `api-docs.deepseek.com` / `x.com` の6ホストが新規判定された（Master・本日のハイライト2件とも一次に到達できず）。WebFetch 広範403 の対象には `soumu.go.jp`（白書概要PDF）と `innovatopia.jp` が加わった（Industry）
- ソース間の矛盾: DeepSeek V4-Flash 0731 の重み公開について、Industry は「MIT ライセンスでウェイト公開」、Master は「HF の重みは4月 Preview のままで 0731 は API 限定とする二次情報と割れている」と記録している。一次が全てゲートウェイ拒否のため未確定として両論併記した。次回、`huggingface.co` の疎通回復時に確定させる
- ソース間の差分: EU AI Act の発効について、Master は行動規範の署名組織数（約190）と署名者への執行の当たり方を、Industry は義務主体にデプロイヤーが含まれる点と対象4分野の内訳を持っていた。いずれも他方には無い情報のため両方を採用した
