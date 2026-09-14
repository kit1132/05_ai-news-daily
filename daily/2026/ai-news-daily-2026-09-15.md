# AI News Daily Summary — 2026-09-15

フロンティア各社が「速度を落とす」側で揃った日である。Amodei の論考に Altman と Musk が公に同調し、Microsoft は MAI モデルの行動規範案を公開して6週間の協議に入った。手元の道具では GitHub Copilot の auto モデル選択にコストと品質のティアが入り、Copilot Studio には Copilot Credits を環境単位で統制する手順が出ている。国内では、ソニー銀行と富士通が銀行の勘定系という最も適用が遅いとされた領域で工程別の定量値を開示した。

## 今日のハイライト

### 1. フロンティア3社が減速側で揃った — 各社が競争速度を前提に動くという読みが崩れる

**要点**: Anthropic の Amodei が能力向上ペースの抑制を求める論考を公開し、Altman と Musk が公に同調、Microsoft は MAI モデルの行動規範案を公開した。速度を落とさない前提で置いたモデル更新見通しと導入計画は、引き直しの対象になる。

**詳細**: Amodei は 9/12 に約3,800語の論考「We Must Pace the Frontier」を個人サイトへ公開した。夏以降に考えを変えた理由として、モデルが次世代モデルの構築を担う再帰的自己改善が業界全体の進歩を加速させている点と、エージェント群のインシデントが「より高性能な不整合エージェント群が6〜12ヶ月以内に壊滅的なサイバー被害を起こしうる」警告にあたる点を挙げている。臨界的な能力水準までに1〜2年の猶予を稼ぐという主張で、提案は3段階に分かれる。

- 埋め込み評価者: METR 型の第三者チームに従業員相当のアクセスを常時与え、安全慣行の検証・インシデント報告・訓練中のアラインメント評価を担わせる
- 民主主義国間の共通安全基準の整備
- 再帰的自己改善など危険能力に対する最終的な国際的制限

同日 Altman は X で「Dario の言うとおり frontier のペースを整える必要がある」と述べ、独立した評価者に従業員並みのアクセスを与える案を「great idea」と評した。Musk も「Dario is right」と応じている。Microsoft AI は 9/14 に37ページの「Humanist AI Code of Conduct」草案を公開し、**6週間**の公開協議を開始した（終了は 10月下旬）。草案は MAI モデルに対し、停止への抵抗・自前の目標設定・人間の監査者に対する思考連鎖の秘匿を禁じ、サイバー攻撃の支援・核兵器の支援・ディープフェイクも禁止対象に挙げる。モデルは「意識を持たず、意識を模倣するよう設計されるべきでもない」と明記されている。現時点ではモデルの訓練に使われておらず、協議結果を反映した改訂版を年末に出して2027年以降の開発指針とする位置づけである。

⚠️ 一次は未読である。`darioamodei.com` と `microsoft.ai` はいずれもゲートウェイ拒否で本文取得できず、Washington Post・TechCrunch・GeekWire 等の二次一致で採っている。

- https://www.darioamodei.com/essay/we-must-pace-the-frontier
- https://microsoft.ai/news/mai-code-of-conduct/
- https://techcrunch.com/2026/09/12/anthropic-ceo-outlines-plan-to-pace-the-frontier/
- https://www.geekwire.com/2026/microsoft-floats-rules-for-its-own-ai-models-as-industry-debates-a-slowdown/

### 2. Copilot の auto モデル選択に3ティアが入った — auto は「選べない代わりに制御もできない」ものではなくなる

**要点**: GitHub が auto model selection に Efficiency / Balance / Intelligence の3ティアを追加し、VS Code・Copilot CLI・Copilot アプリで展開を始めた。auto に任せるとコストも品質も制御できないという前提が、今日から設定項目に変わる。

**詳細**: 9/14 の changelog で公開された。auto はプロンプト単位でモデルを評価する仕組みで、ティアはその評価の重みづけを動かす。

- Efficiency: コストを最優先し、速く単純なタスク向け
- Balance: コスト・品質・レイテンシを総合し、日常業務向け
- Intelligence: 品質を最優先し、複雑なタスク向け

3ティアはいずれも同じモデルプールから選ぶため、Intelligence を選んでも単純な依頼には小さく速いモデルが当たりうる。課金は**ティアではなく auto が実際に選んだモデル**の単価で行われ、有料プラン利用者への auto 経由10%割引は維持される。⚠️ **既定のティアは changelog に明記されていない**ため、組織として既定値を前提にした試算は置かないほうがよい。09-12 収録の Project HydraFusion（安いモデルを先に試して品質不足なら上位へ escalate するカスケード方式）と同方向の製品化で、「どのモデルを使うか」の判断がユーザーからルーターへ移り、方針だけが設定項目として残る形になる。

- https://github.blog/changelog/2026-09-14-configure-cost-and-quality-in-copilot-auto-model-selection/
- https://docs.github.com/en/copilot/concepts/models/auto-model-selection

### 3. ソニー銀行が勘定系の実開発に生成AIを適用した — 基幹系は適用外という前提が崩れた

**要点**: ソニー銀行と富士通が銀行の勘定系システムの実開発に生成AIを本格適用し、工数 40% 削減・開発期間 30% 短縮を実測した。前提が「基幹系は生成AI適用の対象外」から「国内の銀行勘定系で工程別の定量実績が出ている」へ変わる。

**詳細**: 両社が 9/14 に発表した。適用開始は 2025年9月で、2026年7月時点の実績として基本設計から結合テストまでの開発期間を従来比 **30% 短縮**、同じ範囲の工数を **40% 削減**する効果を確認している。工程別では、基本設計の影響調査工数が最大 90% 削減、詳細設計の設計書作成工数が最大 40% 削減、製造工程のソースコード生成率が 99%、結合テストのテスト実行工数が最大 90% 削減となる。技術構成は **Amazon Bedrock 上の Claude** を中核とする AI エージェントで、設計書・ソースコード・テスト資産を工程横断で流用し、最終判断と品質保証は人が担う建て付けとされる。両社は2026年4月までに勘定系の全機能開発へ適用する計画を示している。PoC ではなく実開発の実績値として引用できる。⚠️ 一次の富士通プレスリリースと詳報の `enterprisezine.jp` はゲートウェイ拒否で到達できず、工程別の数値は複数の二次報道の突き合わせによる。対象システムの規模と2026年4月以降の展開条件は未確認である。

- https://www.nikkei.com/article/DGXZRSP712547_U6A910C2000000/
- https://global.fujitsu/ja-JP/pr/news/2026/09/14-01
- https://enterprisezine.jp/news/detail/25073

---

## カテゴリ別まとめ

### Microsoft 365 Copilot / Copilot Studio

- **Copilot Credits の統制ガイダンス**: 管理者が Copilot Credits の消費を環境単位で統制する手順が新規公開された（`govern-credit-consumption`・9/14）。消費は公開前のビルド・プレビュー段階から始まるため、公開後にエージェントを絞る形では間に合わない。ガイダンスハブの新規記事は 8/28 以来17日ぶりになる
  - 統制は4層: テナント（購入済み容量と割り当て権限）／環境（前払い割当・テナントプールからの引き当て・従量課金）／エージェント（月次上限・通知しきい値・ハードストップ）／運用プロセス（コスト責任者・アラートのトリアージ・例外承認）
  - 環境は3分類する: 探索とプロトタイピング／テストと検証／資金付き本番。分類ごとに承認済みの容量姿勢と例外プロセスを定義する
  - ⚠️ PPAC にテナント全体の既定エージェント上限は無く、標準の上限を課すには定期実行か自動化で個別に適用するしかない
  - ⚠️ 環境管理者に割り当てを許可すると、担当環境だけでなくテナント内の全環境への割り当て権限を得る。ページは割り当てをテナント管理者に限定するよう明記している
  - ⚠️ エージェント単位の上限は環境の合計消費を抑えない。前払いの消費を封じるには割当額を定めたうえで「テナントの利用可能な容量から引き当てる」を無効にする。従量課金の環境では Azure の予算はアラートを出すだけで消費を止めない（9/1 に開発環境と試用環境が従量課金へ移行済み）
  - https://learn.microsoft.com/en-us/microsoft-copilot-studio/guidance/govern-credit-consumption
- **PowerPoint の Brand Kit / Skills**: Microsoft 365 Copilot ライセンスを持つ利用者が当日から使えるようになり、管理者は承認済み Skill をユーザー・グループ・組織全体へ発行できる（9/14 の Tech Community 記事で GA 告知）。ブランド準拠とレビュー手順が各自の運用から配布される標準へ変わる
  - Brand Kit: 組織のテンプレート・画像・アイコン・フォント等を作成体験に取り込み、承認済みキットを前提にスライドを生成・更新する。ブランド管理者が厳格モードを有効にすると、Copilot は独自レイアウトを提案せず承認済みレイアウトだけに従う
  - 組み込み Skill: `@Prepare for Questions` と `@Review Presentation` が GA、`@Visualize Slide` はスライド内容を図版やインフォグラフィックへ変換する
  - ⚠️ Release Notes に本件の GA は載っておらず、Roadmap 項目も無い。二次メディアは1か月以上前から「展開中」と報じており、8/17 に「空振り」と判定した件を今回の一次告知が追認する形になった
  - https://techcommunity.microsoft.com/t5/microsoft-copilot-blog/brand-kit-and-skills-in-copilot-in-powerpoint/ba-p/4554932
- **Cowork のモデル記述の食い違いが解消した**: `cowork-admin-governance` の Manage models 節がモデル名の列挙をやめ、`cowork-models` へ委譲する書き方に改訂された（9/14）。8/27 にピッカーから消えた Sonnet+Opus Advisor を現行として残し、GPT 5.6 Sol / Terra と GPT 6 Astra を欠いていた記述は消えている
  - 新設の Model availability versus access 節は、モデル設定が「見えるモデル」を決めるだけでアクセスとは別だと明記する。アクセスを与えるのは Cowork を選択したスペンディングポリシーである
  - モデルピッカーは8件（Auto / GPT 5.5 (Frontier) / GPT 5.6 Sol / GPT 5.6 Terra / GPT 6 Astra / Opus 5 / Claude Sonnet 5 / Claude Fable 5.1）で増減はない。⚠️ 9/12 告知の Grok はこの一覧にも Copilot Studio 側にも現れない
- **M365 Copilot Release Notes**: 新バッチは追加されておらず、先頭は **August 25, 2026** のままである。隔週の期日 9/8 から7日、前バッチからは21日が過ぎた。Copilot Studio の What's New も July 2026 節が最新で、GitHub Copilot ハーネスは GA（8/3）から43日間 `(Production-ready preview)` 表記のまま残る
- **Roadmap の起票**: Release Communications RSS に 9/12・9/13（UTC）の新規起票はゼロで、最新は 9/11 22:10Z のままである。⚠️ 広報枠は 7/24 の Opus 5 記事から53日動かず、Fable 5.1・GPT-6 Astra・Grok の3件が「Available today」型でありながら未掲載である

### Claude / Anthropic

- **Claude for Financial Advisors が GA した**: Anthropic が金融アドバイザー向けのコネクタ群と8種類のワークフロースキルを一般提供した（9/14）。重要な判断には人間の承認を要求する設計で、自動化は調査・準備・記録の側に置かれている。導入には Enterprise プランが要る
  - カストディ・ポートフォリオ基盤: Addepar / BlackRock / Charles Schwab / Envestnet / Orion / SS&C Black Diamond / Vanguard
  - 専門領域ツール: iCapital（オルタナティブ投資）/ Wealth.com（相続・税務）/ Wealthbox（CRM）/ Zocks（AI 会議アシスタント）
  - 汎用業務基盤: Salesforce / Microsoft 365 / DocuSign / Box / FactSet / S&P Global / Morningstar
  - ⚠️ **2026年9月末**までに新規ライセンスを申請した企業に一度限りの利用クレジットが付く条件が示されており、検討するなら期限がある
  - https://claude.com/blog/claude-for-financial-advisors
- **エージェント導入で CI が詰まった経緯を Anthropic が公開した**: 社内のテスト影響分析サービスを作り直した過程が定量値つきで公開された（9/14）。エージェント導入時の負荷見積もりに直接効く
  - CI ジョブ数は6ヶ月で **25倍**、エンジニア1人あたりの四半期出荷コード量は2021〜2025年比で8倍、そのコードの **80% を Claude が書いている**。テスト数は10倍に増えた
  - 場当たりの対処は寿命が急速に縮み、1つ目のパッチは70日、2つ目は29日、3つ目は1日ももたなかった
  - 最終的にデータストアを挟んで listener を stateless・水平スケール可能にし、journal をテスト履歴へ数秒ごとに巻き取る consumer を分離した。作り直しはエンジニア1人・3週間で終わっている
  - https://claude.com/blog/agentic-coding-is-straining-ci-heres-how-we-scaled-test-impact-analysis-at-anthropic
- **Claude Code の日次リリースが2日間止まった**: changelog の最上位は `2.1.270`（9/12）のままで、9/13・9/14 の新規リリースが無い。npm の `dist-tags` も動いておらず、9/8 から毎日刻まれていた publish が途切れた形になる。`stable` と `latest` の34版差も据え置きである
- **Anthropic の一次はニュース・研究とも新規なし**: `anthropic.com/news` は本文取得に成功したうえで 9/13・9/14 の新規公表がなく、Platform API の release notes も 9/10 の Managed Agents 権限ポリシー `auto` が最上位のまま据え置かれている。モデル退役ページの Active は11件で変化がない

### OpenAI / Codex / ChatGPT

- **OpenAI が競合 AI の広告を ChatGPT から締め出した**: OpenAI が画像生成・音声生成の競合プロダクトの広告を出稿できないよう広告ポリシーを変更したと The Information が報じた。⚠️ 公表ではなく広告パートナーへの個別通知で伝えられ、初期パイロットに参加していた Adobe が影響を受けている。締め出しの対象は同社が ChatGPT Images 2.5 と ChatGPT Live を投入した領域と一致し、動画生成ツールの広告は引き続き許可されている。同社の広告事業は年換算売上 **$2.4B** を目標に置くとされる
  - https://searchengineland.com/openai-reportedly-blocks-rival-ai-tools-from-advertising-in-chatgpt-488019
- **API 料金は22日連続で据え置きとなった**: 主要モデルの単価に変化はなく、料金ページの全節を2日連続で列挙したところ前日の記録に無い列が3件見つかった（長文脈とキャッシュの列）。`gpt-5.6-terra` 長文脈は入力 $4／キャッシュ入力 $0.40／キャッシュ書込 $5／出力 $18、`gpt-5.6-luna` 長文脈は $0.40／$0.04／$0.50／$1.80 である。GPT-5.6 Sol の期間限定価格は「少なくとも 2026年11月21日まで」の記載が続く
  - https://developers.openai.com/api/docs/pricing
- **廃止一覧は 9/11 から動いていない**: 撤回・延期・新規追加のいずれも検知していない。直近は 9/24 の Videos API と Sora 2 系（代替の記載なし）、9/28 の `gpt-3.5-turbo-instruct` ほか3件、10/1 の `gpt-5.4-cyber` である。Evals は 10/31 に読み取り専用へ移り 11/30 に停止する2段構成で、代替は外部 OSS の Promptfoo とされている
- **Codex CLI は pre-release が進んだ**: pre-release は `rust-v0.155.0-alpha.4`（9/14）が最新で、安定版は rust 側 `rust-v0.154.0`（9/9）・python 側 `python-v0.154.0`（9/10）のままである。⚠️ releases ページの並び順は日付降順ではないため、`tags` との突き合わせで最新を確定している。`learn.chatgpt.com` は2日連続で本文取得に成功し、最上位は 9/11 の Pets / Appshots のままである

### Google

- **Gemini API changelog は12日連続で静止した**: 最上位は 9/3 の Lyria 3.5 public preview のままで、料金改定の告知も出ていない。`gemini-3.8-flash` の導入価格は入力 $0.75／出力 $3.75 が **2026-12-31** までで、2027-01-01 から $1.50／$7.50 になる点も変わらない
  - https://ai.google.dev/gemini-api/docs/changelog
- **Workspace Updates は 9/11 で止まっている**: 9月分は全22件で、最新は 9/11 の3本（週次リカップ・Microsoft からの移行支援・Gemini デスクトップアプリの Windows 提供）である。9/12 は金曜だが投稿がなく、Gemini 関連の新規は週明けまで動かない見込みである

### 開発ツール（Cursor / xAI / Devin）

- **Cursor は GPT-6 Astra の提供告知を出さないまま12日目になった**: changelog は 9/10 の Projects が最上位、フォーラム Announcements は 9/2 の Grok Bot Android 版のまま13日間動いていない。両方を毎日取得したうえでの不在で、**11/12** に予定される OpenAI からのモデル供給停止と併せて読む必要がある
- **Grok 4.7 は公開予定日を過ぎて3日目も未公開である**: Musk は 9/2 に「約10日後」と述べ 9/11 に延期を表明したが、新しい日程は示されていない。xAI 公式にローンチ投稿・モデルページ・価格・ベンチマークのいずれも無く、提供中の最新は Grok 4.6（8/12）のままである。⚠️ 2.1兆パラメータという規模はいずれも Musk の X 投稿が出所で、一次文書では確認できていない
- **オープンウェイトは8 org で4日間新規がない**: `Qwen` ほか8 org を作成日降順と更新日降順の両方で確認したが、9/12〜9/14 に作成・更新されたリポジトリは1件も無い。直近で最も新しい作成は `deepseek-ai/DeepSeek-V4.1-Flash`（9/10）である。MCP 公式ブログも 8/22 の「The New MCP Roadmap」から24日間新規がない

### 市場データ / 企業構造・GTM

- **Anthropic が上場先に Nasdaq を選んだ**: Anthropic が10月の上場を目標に置き、今四半期も調整後営業利益が黒字になると投資家に説明したと Financial Times が 9/14 に報じた。実現すれば2期連続の黒字になる。想定される上場時評価額は **$2兆**以上とされ、粗利率は80%超、7月時点の年換算売上は $65B という水準が示された。⚠️ 調整後営業利益は GAAP 純利益ではなく、調整項目の範囲を確認せずには引用できない。一方 OpenAI の Altman は 9/12 公開の Fortune インタビューで2026年内の上場を明確に否定しており、先に上場するのがどちらかが入れ替わった。S-1 の公開は本日時点でも確認できていない
  - https://ca.investing.com/news/stock-market-news/anthropic-tells-investors-it-will-post-second-straight-quarterly-profit--ft-4837314
  - https://fortune.com/2026/09/12/sam-altman-openai-ipo-delay-ill-advised-moment-safety-concerns/
- **主要3社が AI 安全基準の業界団体設立を協議している**: Anthropic・OpenAI・Google が標準化・監査を担う業界団体の設立を少なくとも7月から協議していると報じられた（9/13〜9/14）。推進役は Amodei で、狙いはフロンティアモデルの技術的テストとリリース前監査に置かれている。⚠️ 3社の立場は一致しておらず、Anthropic は政府との協調に寄り、OpenAI は連邦の動きが無い場合のラボ主導・自主規制型を支持している。各社の公式発表は無く、一次も未読である
  - https://www.cnn.com/2026/09/14/tech/ai-standards-body
- **Similarweb の年次推移が確定した**: 8月分の内訳に対応する過去時点の値が判明し、Claude が1年で約5倍・Gemini が倍増していることが確認できる。「ChatGPT 一強」を前提にした提案構成は1年で成立しなくなっている
  - 2026年8月: ChatGPT 55.5%・Gemini 25.6%・Claude 9.3%・DeepSeek 3.4%・Grok 2.4%・Copilot 1.6%
  - 12カ月前: ChatGPT 73.3%・Gemini 12.9%・DeepSeek 4.0%・Grok 2.6%・Copilot 2.0%・Claude 1.9%
  - https://www.similarweb.com/top-websites/ai-chatbots-and-tools/
- **国内の市場データ系は新規公表がない**: IDC・MM総研・NRC のいずれにも本日の新規公表を検知していない。⚠️ IDC Japan「国内AIシステム市場予測」はプレスリリースの所在を特定したものの、`www.idc.com` のゲートウェイ拒否により公表日を確定できていない（数値は 2024年 1兆3,412億円 → 2029年 4兆1,873億円・CAGR 25.6%）

---

## 直近の注目予定

- **9/17**: OpenAI DevDay Exchange の応募締切 ／ Copilot Studio 版アプリ生成の公開プレビュー（9/10 告知の「over the next week」）
- **9/18**: 新 iPhone と AirPods 5 の発売
- **9/21**: Anthropic ウェルビーイング研究助成の応募締切
- **9/22 前後**: M365 Copilot Release Notes の次バッチ
- **9/23**: WebMCP Challenge の受賞発表 ／ Partnering for Success Together の初回開催
- **9/24**: OpenAI の Videos API と Sora 2 系が退役（代替モデルの提示なし）
- **9/28**: OpenAI の `gpt-3.5-turbo-instruct` / `babbage-002` / `davinci-002` / `gpt-3.5-turbo-1106` が停止 ／ Copilot のチャット3面統合 ／ code review の既定 effort が Lite → Balanced ／ チャットのデータ保持がアカウント存続期間へ
- **9/29**: OpenAI DevDay 本体（サンフランシスコ Fort Mason）
- **9/30**: Gemini の旧 `gemini-omni-flash-preview` エンドポイント廃止 ／ OpenAI の現行 OneGov 契約（$1/年）が失効 ／ M365 E7 プロモ最終日 ／ E5・E3 の CSP 割引終了
- **9 月末**: Claude for Financial Advisors の新規ライセンス申請に付く一度限りの利用クレジットの期限
- **9 月中**: macOS 27 GA ／ Copilot Tuning の Public Preview 再開 ／ DLP for Microsoft Cowork の Preview（570845）
- **10/1**: OpenAI の `gpt-5.4-cyber` が API から削除 ／ OneGov トークン課金50%割引が開始 ／ Copilot Business・Enterprise の既存顧客が前払い必須に ／ Microsoft CSP ソフトウェア価格改定が発効 ／ Apple の EU 向け新ビジネス条件が発効
- **10/2**: GitHub Copilot が Gemini 3.5 Flash / Gemini 3.6 Flash / Kimi K2.7 Code / Claude Opus 4.7 を全体験から廃止
- **10/5**: GPT-Rosalind の課金が開始 ／ Anthropic ウェルビーイング研究助成の full proposal 提出期限
- **10/16–11/11**: OpenAI DevDay Exchange 8都市（東京は 10/20）
- **10/23**: OpenAI のレガシースナップショット退役（`gpt-3.5-turbo-0125` / `gpt-4-0613` / `o1-2024-12-17` 等）
- **10/26 頃**: Microsoft AI の MAI モデル行動規範に対する公開協議が終了
- **10/31**: OpenAI の既存 evals が読み取り専用になる
- **10 月**: Anthropic の IPO 観測（Nasdaq・$2兆超の評価額を目標と報道・上場日は未確定）／ DLP for Microsoft Cowork の GA
- **11/12**: OpenAI が Cursor へのモデル供給を停止する予定日
- **11/15**: Microsoft Release Planner が退役
- **11/21**: GPT-5.6 Sol の暫定値下げが有効とされる期限
- **11/30**: OpenAI の Reusable prompts・Evals プラットフォーム・Agent Builder が停止
- **12/1**: OpenAI の GPT Image 系が停止（→ `gpt-image-2`）
- **12/2**: EU AI Act の生成コンテンツ標識義務、8/2 以前に市場投入済みシステムへの猶予終了
- **12/11**: OpenAI の旧スナップショット退役（`gpt-5-2025-08-07` / `o3-2025-04-16` 等）
- **12/31**: Gemini 3.8 Flash と 3.7 Flash の導入価格が終了 ／ GitHub Copilot の Fable 5.1 / Fable 5 に対する ZDR 暫定免除が終了
- **年末**: Microsoft AI の MAI モデル行動規範の改訂版公開予定
- **2027**: OpenAI の IPO がありうる時期（CFO は「2027年、事業が伸び続ければそれより早く」と説明）

---

## 改善メモ

- 新規提案3件: `B-072`（01: 政策・ガバナンス文書の一次を CEO 個人サイトとベンダー別ドメインまで広げる）／ `B-067`（02: Partner Center アナウンス URL が `<月>-<年>` から `<年>-<月>` へ変わり旧パスが404）／ `B-036`（03: 国内エンタープライズ AI 導入事例の定点ソース追加）
- 継続提案は3ソース合計77件（01 が16件・02 が55件・03 が6件。最多は 03 の B-004 取得方法欄の WebSearch 化、78回目）
- 障害の変化: 新規ゲートウェイ拒否が8件（`darioamodei.com` / `microsoft.ai` / `www.geekwire.com` / `www.irishtimes.com` / `global.fujitsu` / `enterprisezine.jp` / `bizaidea.com` / `aka.ms`）。01 は 09-14 に復旧した5ホストのうち3件で2日目の本文取得を確認した
- ソース間の差: 減速論と標準化団体の2件は、01 がハイライト・本文で採録した一方、03 は「AI の倫理・規制の議論」の除外規定により不採録としている。本サマリーは 01 側を採った。標準化団体の報道元も 01 は The Information、03 は Washington Post・Bloomberg と食い違う
