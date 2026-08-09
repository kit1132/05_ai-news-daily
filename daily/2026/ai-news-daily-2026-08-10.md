# AI News Daily Summary — 2026-08-10

月曜は「止め方」と「払い方」の前提が同時に動いた。Anthropic は Fable 5 の生物学 fallback を約85%削り、健康・学習の質問が下位モデルへ落ちる前提を外した。Cursor は Router の本番実測を公開し、モデルを人手で指名するほど良いという前提へコスト面から反証を出している。払う側では Rippling が自社のトークン支出を R&D 人件費予算の40%まで膨らませた経緯をそのまま製品化し、AI 費用をシート単価ではなく人件費比で見る材料を出した。制度側は米エネルギー省がオープンウェイトの供給主体に回り、ホワイトハウスの審査枠組みが米国製オープンウェイトを対象外にした事実と対になっている。国内では JDLA の第三者認証が一般申請を開始した。Microsoft 側は動きが薄く、Copilot Studio のビルドは7月ゼロのまま8月に入っている。

## 今日のハイライト

### 1. Fable 5 の生物学セーフガードが緩和された — 「健康の質問は下位モデルに落ちる」前提が消える

**要点**: Anthropic が Fable 5 の生物学 fallback を約 **85%** 削減した。前提は「臨床・学習の問い合わせは分類器に止められ Opus 5 へ落ちる」から「dual-use 3分野を除けばそのまま通る」へ変わった。

**詳細**: 公開は 8/7。fallback は分類器が保護対象と判定した問い合わせを、より能力の低いモデルへ回す仕組みを指す。生物学分の削減が総 fallback 量に及ぼす影響は製品面ごとに差がある。

- Claude.ai: 総 fallback が **67%** 減
- Cowork: 55% 減
- Claude Code: 17% 減 ／ Claude Platform: 7% 減（開発用途はもともと生物学分類器に当たる頻度が低い）
- 引き続き Opus 5 へフォールバックする領域: virology・toxicology・molecular design の dual-use 3分野

実装は分類器の constitution（何を保護対象とみなすかの規則集）を書き直し、良性ユースケースの例外を細かく定義したうえで訓練データを再生成して再学習する方式である。Anthropic は「安全マージンとして念のため止めていた、ほぼ確実に良性の要求」を通す側へ境界を動かしたと説明している。

⚠️ 一次 `www.anthropic.com` はオリジン403で本文を読めず、上記の数値は二次報道の一致で採っている。8/7 公開分を本日3日遅れで初検出した。

- https://www.anthropic.com/news/improving-fable-5-s-biology-safeguards （一次・403で未読）
- https://www.unite.ai/anthropic-retunes-fable-5s-biology-safeguards-cutting-blocked-queries-85/
- https://thenextweb.com/news/anthropic-claude-fable-5-biology-safeguards-fallbacks-dual-use

### 2. Cursor が Router の本番実測を公開した — モデルを人手で指名する運用がコストの根拠を失う

**要点**: Cursor が Router の実測を示し、Auto Intelligence が Fable 5 級の満足度を **68%** 低いコストで出すと公開した。前提は「良いモデルを指名するほど品質が上がる」から「振り分けが同等品質を安く出す」へ変わった。

**詳細**: 8/6 公開の research 記事である。7/22 の Router ローンチ以降も本番トラフィックから学習を続けており、数値はすべて Opus 4.8 基準の相対値になっている。

- Auto Intelligence: Fable 5 級の満足度を 68% 低いコストで出す。ローンチ時点からさらに 18% 下げた
- Auto Balance: Opus 4.8 超えの満足度を 41% 低いコストで出す。ローンチ時点からコストを 8% 下げ、満足度も 3% 上げた
- 振り分けの仕組み: 要求の複雑度を Compass で予測し、モデルごとの得手不得手を学習した重みと突き合わせる。新モデル追加時は再学習で追随する設計で、記事中でも Opus 5 を混成へ加えたと述べている
- 対象プラン: Teams / Enterprise

- https://cursor.com/blog/how-cursor-router-works

### 3. Rippling が自社の AI トークン支出を公開した — 費用の見方が「シート単価」から「人件費に対する比率」へ移る

**要点**: Rippling が 8/7 に AI Spend Console を投入し、トークン支出が R&D 人件費予算の **40%** を食う軌道にあったと明かした。前提は「AI 費用はツールのシート単価で積む」から「人件費予算の何割かで見る」へ変わる。

**詳細**: 同社は2026年初に従業員へ Cursor / OpenAI / Anthropic の利用を積極的に勧めていた。3月に CFO が経営陣へ示した数字が製品化の契機になっている。

- トークン支出が R&D 人件費予算の40%を食う軌道に乗っていた
- 月次支出は前月比80%増で伸び、放置すれば年間費用が同予算のほぼ90%に達する見込みだった
- 1人のエンジニアが1カ月で **$50,000** 分のトークンを消費していた

対策後、トークン支出は R&D 人件費予算の40%から約15%へ下がった一方、利用量そのものはピーク近辺のまま推移している（4月6,050億トークン→7月6,000億トークン）。削ったのは利用量ではなく単価と配分という点が、この数字の使いどころにあたる。製品側は Rippling Data Cloud と Employee Graph の上に構築され、Claude・Cursor・Codex などのモデル利用を従業員・部署・職種の識別子へ紐づけて、GitHub や Salesforce の成果物と並べて表示する。管理者はトークン支出と利用可能モデルにポリシーを課し、要求を費用対効果の高いモデルへ回せる。現時点ではウェイトリスト受付である。

⚠️ `rippling.com` はゲートウェイ拒否で一次ブログに到達できず、数値は二次報道の突き合わせで構成した。

- https://techcrunch.com/2026/08/07/after-rippling-blew-millions-on-ai-in-months-it-built-an-employee-roi-tool/
- https://www.rippling.com/blog/introducing-ai-spend-console
- https://www.analyticsinsight.net/news/rippling-launches-ai-spend-console-after-spending-millions-on-tokens

## カテゴリ別まとめ

### Anthropic / Claude

- Anthropic が Fable 5 の生物学セーフガードを緩和した（ハイライト1参照）
- Claude Code は **v2.1.226**（8/8）が最新のままで、8/9 の新版はない。`code.claude.com/docs/en/changelog` と GitHub の `CHANGELOG.md` の2ソースで最上位が一致することを確認して確定した
- Claude API の release notes は 8/7 が最上位のままで、8/8・8/9 の追加はない（既報の Managed Agents 4件: セッション予算 / advisor / `inference_geo` / GitHub リポジトリからの skill 読み込み）
- `support.claude.com` の Release Notes は 8/6 の skill / plugin セキュリティスキャン beta が最上位のままで動きがない。`claude.com/blog` も 8/7 の auto mode 2本が最上位のままである
- Claude Code の既定権限モードは 8/14 に auto mode へ切り替わる（Pro / Max / Team・8/7 告知の既報）。残り4日で、自分で既定を設定済みなら一度だけ切替確認が出る
- Claude の利用枠は期限が2つ走っている。週次上限50%増は 8/19 まで、Sonnet 5 の促進価格 $2/$10 は 8/31 に終了する（→ $3/$15）
- https://code.claude.com/docs/en/changelog ／ https://claude.com/blog/auto-mode-default-in-claude-code

### OpenAI / Codex / ChatGPT

- OpenAI が **Sign in with ChatGPT** のベータを 8/2 に開始していた（本日初検出）。ChatGPT アカウントを外部サービスの ID として使える認証レイヤーで、初期パートナーは Airtable / GitLab / HubSpot / Notion / Supabase / Vercel の6社である。連携先へ渡るのは氏名・メールアドレス・プロフィール画像のみだが、実メールが既定で共有されるため、組織導入時は横断的な名寄せが起きうる点を踏まえて判断する必要がある
- Codex CLI 0.147.0（8/7・08-08 収録の既報）が追加のプラグイン・マーケットプレイスとして Amazon Bedrock と Claude Code を扱うと分かった。Anthropic は Agent Plugins の Core Maintainer に入っていないが、Claude Code 側のプラグイン資産は Codex から参照できることになる
- Codex CLI は安定版 0.147.0（8/7）据え置きで、pre-release も 0.148.0-alpha.5（8/8 02:26 UTC）のまま 8/9 の新規はない。0.148.0 の安定版は未リリースである
- `developers.openai.com/changelog` は 8/5 の Fast mode long-context 対応が最上位のままで、8/6 以降の追加がない。`community.openai.com` の Announcements も 7/30 の GPT-5.6 値下げ告知から11日間動いていない
- ChatGPT Atlas は予定どおり 8/9 でシャットダウンした。ブックマーク・タブ・履歴は自動移行せず、Cookie とパスワードのみ ChatGPT デスクトップアプリへ書き出せる
- OpenAI が ChatGPT の仕事利用データを公表した（8/6 のレポート「From asking to doing」）。Q2 2026 の個別メッセージを分類した結果で、仕事の文脈では執筆・コーディング・分析などのタスクを完了させる用途が仕事以外の文脈の2倍以上を占める。35歳超の利用者が送るメッセージのシェアはほぼすべての国で上昇し、12カ月前より5ポイント高い。⚠️ `openai.com` はオリジン403で本文に到達できず、内容は検索スニペットの突き合わせによる
- https://help.openai.com/en/articles/20001410-sign-in-with-chatgpt ／ https://openai.com/index/how-the-world-is-putting-chatgpt-to-work/

### Cursor / 開発ツール

- Cursor が Router の運用実測値を公開した（ハイライト2参照）
- Cursor が **Mixture-of-Kittens** を 8/4 にオープンソース化していた（本日初検出）。NVL72 向けの MoE 訓練メガカーネルで、MoE 層の通信と計算を単一の決定論的カーネルに融合する。同社の agentic コーディングモデル Composer の訓練では MoE 層が end-to-end 時間の半分以上を占めるボトルネックだったと述べており、現在は数万 GPU 規模の Composer 訓練を支えている
- Cursor の changelog は 8/3 の Google Workspace Plugins が最新のままで、Announcements フォーラムも 7/28 の Cursor Start のままである。Devin も 8/5 の更新から動いていない
- Grok 4.6 は一次確認が依然できない。二次サイトは「8/7 ローンチ・1.5T パラメータ・SWE Marathon 29.0%」と書くが、同じ記事群が「xAI はベンチマークもモデルカードも未公開で、出回っている数値は推測」とも書いており、正面から食い違ったままである
- https://cursor.com/blog/mixture-of-kittens

### GitHub Copilot

- `github.blog/changelog` は 8/7 の5件が最上位のままで、8/8・8/9 の新規エントリはない。Copilot ラベル外まで含めても最上位は同日で、AI 関連の追加はなかった
- Copilot CLI は pre-release **1.0.79-9**（8/7 23:39）が最新で、安定版 1.0.78（8/3）は据え置きである。週末は pre-release も刻まれていない
- 期限は3つが既報のまま動いていない。GitHub Spark の既存ユーザーアクセス終了が 8/31、既定モデル有効化ポリシーの発効が 8/26、全体験でのモデル廃止が 9/1 である
- https://github.blog/changelog/label/copilot/

### Microsoft 365 Copilot / Copilot Studio

- ドメイン除外の撤回告知（記事ID 4543648）は本文を変えないまま投稿日だけが動いていた。`pubDate` と `dc:date` のいずれも 8/7 18:54Z を返すが、本ダイジェストが最初に扱った 8/6 時点の記録は 8/4 である
  - 検知手順の穴: 8/8・8/9 はいずれも board RSS 3本を巡回して「`Update:` 系の新規記事なし」と記録したが、この照合は新しい記事が増えたかどうかしか見ておらず、既存エントリの日付や本文が動いても引っかからない
  - 一次ページの状態: Learn の `copilot/domain-exclusion` は本日も削除も注記もされずに残り、`updated_at` は撤回前の 2026-07-30T21:25Z のままである
  - 本日の取得では同ページに `ROBOTS: NOINDEX, NOFOLLOW` が付いていた。検索経由では辿り着けず直接 URL でしか読めない状態だが、過去の取得ではメタデータを記録しておらず、撤回に伴って付いたのかは判定できない
- Copilot Studio の What's New は June 2026 の節構成のままで、7月節も8月節も追加されていない。新エージェント体験（GitHub Copilot ハーネス）は 8/3 に GA 済みなのに `(Production-ready preview)` の表記が残ったままで、未反映が7日連続になった
- Copilot Studio のビルドは **2026.6.3**（6/30 初出）のままで、7月ビルドがゼロのまま8月に入っている。次の定例更新日は 8/11 で、ここでも更新がなければ空振りは4回目になる
- クレジット枯渇時のエンフォースメント仕様を一次で再確認し、`updated_at` が 2026-08-03T14:59Z のまま変化していないことを確かめた。クレジットが尽きるとエンドユーザー側はエージェントが応答を停止し、メーカー側は自然言語オーサリング・プレビュー/テスト・評価生成が止まる。単価は依然として Learn 側に存在せず、金額を載せた Licensing Guide の PDF は 403 のままである。二次には「1クレジット = $0.01」とする記述が出回っているが、一次未確認のため採用しない
- M365 Copilot の Release Notes は先頭が July 29, 2026 バッチのままで、8/9 から変化がない。節構成5本・全10項目が一致することを確認した。次バッチは隔週傾向どおりなら8月中旬見込みである
- 二次メディアの「8月の大型アップデート」は3例目の空振りになった。英語圏の記事と動画が挙げる「Word の変更履歴を使ったリライト」「Cowork のイベントスケジューリング」は July 29 バッチにどちらも収録されておらず、前者は 2026-04-16・04-27 に掲載済みの既報である
- Microsoft 365 Roadmap は 7/9 の GPT-5.6 告知が Latest announcements の最新のままで、Tech Community も 8/5 の ICYMI 記事、Microsoft 365 Blog 本体も 7/30 の記事から動いていない。M365 Developer Blog は 8/6 の Work IQ Developer Tools プレビューが最新である
- https://techcommunity.microsoft.com/blog/microsoft365copilotblog/update-domain-exclusion-for-microsoft-365-copilot/4543648 ／ https://learn.microsoft.com/en-us/copilot/domain-exclusion

### Power Platform / ライセンス

- Release Wave（全体版）は緑チェックの追加・期日の変更・行の削除がいずれも発生しておらず、期日超過は 8/9 に数え直した延べ **12行** のまま2日連続で同一だった（`ms.date` 8/4 / `updated_at` 8/7 20:59Z も据え置き）
  - GA 列が当月より前の月表記のまま: 7件（統合 Power Apps によるフォーム UI / マシン・フロー稼働率のダッシュボード / ワークキュー項目の CSV エクスポート / code apps のコネクタ CLI 対応 / FetchXML エディターでのオフラインプロファイル構成 / カスタムブランドアプリのプッシュ通知〔Jun〕/ デスクトップ版の以前のプロンプト参照〔May〕）
  - Public preview 列が当月より前の月表記のまま: 6件（デスクトップフローの直接スケジュール実行 / フローチャート表示 / 現行 Python 実行 / PowerPoint 操作の4件が Jul、ローカル AI モデル接続と code apps のコネクタ CLI 対応が Jun）
  - 8月に期日がある7件（ライセンスダッシュボード改善〔GA〕/ デスクトップフローのカスタムダッシュボードタイル〔Preview〕/ Process Intelligence Studio〔Preview〕/ Fabric セマンティックモデルへのエクスポート〔GA〕/ 正規化スキーマインポート〔GA〕/ Dataverse オンラインモード〔Preview〕/ ヘッダーとナビゲーションの刷新〔GA〕）はいずれも未達のままである
- Power Platform Blog の月次記事は 8/6 の July/August 2026 合併号が最新のままで、前月号・当月号・合併号の3通りで照合しても新規はなかった。親ページの WebFetch は本日も 4/27 で止まる不完全レンダリングだった
- Power Automate Blog / Power Apps Blog も子カテゴリページ上の最新が 4/8 と 5/13 のままで、これも不完全レンダリングによる。GA の検知は引き続き Release Wave の緑チェックに依存する
- Partner Center の8月アナウンスは 8/7 付の7件目「Invoice generation delayed for some partners」までで、公開（8/4〜8/5）以来はじめて月内追記のない日になった
- Microsoft Purview の `whats-new` は7月節に Copilot 関連の新規追加がなく、8月節は未作成である。Copilot in SharePoint も 8/6 の月次記事が最新のままである

### Google

- **Gemini in Classroom** が本日 8/10 から全年齢の生徒へ開放される（web）。管理者が既に Gemini in Classroom / Gemini / Gemini Notebook へのアクセスを付与済みの K-12・高等教育の生徒が対象で、モバイルは 8/17 である
- Gemini API の changelog は 7/30 の Gemini Robotics ER 2 public preview が最上位のままで、8月の追加はない。`gemini-robotics-er-1.6-preview` の 8/31 停止予定も据え置きである
- Gemini API の単価は8日連続で据え置きだった。3.6 Flash（$1.50／$7.50）と 3.5 Flash（$1.50／$9.00）の出力単価の逆転、3.1 Flash-Lite（$0.25／$1.50）が 3.5 Flash-Lite（$0.30／$2.50）より安い関係のいずれも継続している
- Gemini 3.5 Pro の GA は未ローンチのまま継続している。8/12 のリーク報道はあるが Google 自身は未発表で、I/O（5/19）以降のスリップは3回目に入った
- Workspace Studio の Gemini Notebooks 自動ソース追加は 8/6 から段階ロールアウトに入っている（既報）
- https://ai.google.dev/gemini-api/docs/changelog ／ https://ai.google.dev/gemini-api/docs/pricing

### 規制・政策

- 米エネルギー省が **Genesis Open Models Initiative** を 8/7 に始めた。米政府が後ろ盾となる初のオープンウェイト AI プログラムにあたる
  - 第1弾: Arcee AI と共同で構築する Genesis-Science-1（GS1）で、材料科学・核融合・地球システムモデリング・高エネルギー物理を対象領域に置く。単体のモデルではなく、科学計算ワークフローを完遂しつつ再現可能な作業記録を残す governed research harness と位置づけている
  - 役割分担: Arcee AI がモデル開発を主導し、参加する国立研究所の研究者が査読済み資料の提供・研究タスクの定義・評価の設計・結果の検証を担う
  - 締切: DOE が寄与プログラムのポータルを開設しており、第1次の応募締切は 8/14 である
- ホワイトハウスの自主フレームワークは米国製オープンウェイトを対象外にしていた。covered frontier model の定義は「クローズドソースかつ最先端能力かつ安全保障リスクを持つもの」で、公開後のオープンモデルを制限しないと枠組み自体に明記されている。ただし「最先端」と「安全保障リスク」の定義は示されず、枠組みは非公開のまま参加企業にしか共有されない。同じ政府が審査対象からオープンウェイトを外す一方で供給主体にも回った形になる
- Anthropic が初代の対外政策責任者を置いた（8/4 発表）。元カリフォルニア州最高裁判事の Mariano-Florentino (Tino) Cuéllar が初代 Chief Global Affairs Officer に就き、社長の Daniela Amodei へ直属して各国政府・政策当局・国際機関との関係を統括する。直前までカーネギー国際平和財団の理事長を務めていた
- https://www.energy.gov/undersecretaryforscience/articles/us-department-energy-launches-genesis-open-models-initiative ／ https://www.axios.com/2026/08/04/trump-ai-framework-open-models ／ https://www.anthropic.com/news/tino-cuellar

### 国内

- 日本ディープラーニング協会が **C認証** の一般申請受付を 8/4 に開始した。正式名称は C認証（AI Governance Core Certification）で、法人単位の認証・有効期間2年である。業種・規模を問わず AI を開発・提供・利用する組織が対象で、民間企業だけでなく自治体も含む。ガバナンス体制のコア要素に絞って評価する設計のため最短約2カ月で取得できるとしており、費用は企業規模によって変わる
  - 取得の流れ: JDLA 指定の認定コンサルティング企業による現状確認と体制整備支援を受け、書類を JDLA へ提出し、審査を経て認証委員会が付与する
  - 体制構築で実施すること: 利用している AI の把握・組織体制の整備・リスクアセスメント・リスク対応の4点
  - 認定コンサルティング企業: 先行して認証を取得した6社が登録済みで、ABEJA・Elith・Algomatic・キカガク・EY新日本有限責任監査法人・Rosso が名を連ねる
  - ⚠️ `jdla.org` はゲートウェイ拒否で一次プレスリリースに到達できず、内容は制度ページの二次紹介と取得企業のリリースで構成した
- https://www.jdla.org/ai-governance/certification/ ／ https://ai.watch.impress.co.jp/docs/news/2130828.html

### MCP / オープンウェイト

- MCP 公式ブログは 7/28 の `The 2026-07-28 Specification` が最新のままで、13日連続で動きがない。Tier 1 SDK の版も変化がなく、TypeScript / Python はともに 2.0.0、C# は v2.0、Go は v2 未発行で `go-sdk` v1.7.0 である
- 8/8〜8/9 に公開されたフロンティア級のオープンウェイトモデルはない。Hugging Face の作成日降順・trending 上位をともに走査したが、直近の新顔は MiniMax-H3 の派生（8/5〜8/7）に集中しており、いずれも動画生成系で対象外である
- trending 上位は変化がない: `moonshotai/Kimi-K3`・`MiniMaxAI/MiniMax-H3`・`deepseek-ai/DeepSeek-V4-Flash-0731`

## 直近の注目予定

- **8/10**: Gemini in Classroom が全年齢の生徒へ開放（web）
- **8/11**: Copilot Studio Released Versions の定例更新 ／ 非推奨一覧・拡張機能 What's New の週次確認
- **8/12**: Made by Google ／ Gemini 3.5 Pro ローンチの噂（Google 未発表）
- **8/14**: Claude Code の既定権限モードが auto mode へ（Pro / Max / Team）／ Copilot Success Planner の提供開始 ／ DOE Genesis 寄与プログラムの第1次応募締切
- **8/17**: Claude Console 旧 Workbench 退役 ＋ 実験的プロンプトツール API 廃止 ／ Gemini API の Imagen 4.0 系3本停止 ／ Gemini in Classroom のモバイル開放
- **8/18〜9/8**: M365 Copilot Agent's Playbook ライブストリーム（各回 9AM PT）
- **8/19**: Claude Code 週次上限50%増の終了
- **8/20**: Gemini Enterprise Agent Platform の Grok 4.1 ファミリー停止（一次未確認）
- **8/22**: M365 Copilot アプリのチャット中心 UI が Deferred リングへ展開開始
- **8/26**: OpenAI Assistants API 廃止 / o3 退役 ／ Copilot 既定モデル有効化ポリシー発効
- **8/30**: 公式 DALL·E GPT の退役
- **8/31**: GitHub Spark の既存ユーザーアクセス終了（エクスポート期限） ／ Sonnet 5 促進価格終了（→ $3/$15） ／ `gemini-robotics-er-1.6-preview` 停止 ／ GPT-5.4・5.4 mini が Codex から除外 ／ Power Automate モバイルアプリの廃止
- **9/1**: GitHub Copilot の全体験でモデル廃止
- **9/2**: Windows 365 Frontline 名称での購入最終日 ／ **9/3**: Windows 365 Flex へ改称
- **9/30**: M365 E7 プロモーションの対象購入最終日 ／ M365 E5 / E3 の CSP 割引終了 ／ **10/1**: E7 プロモーションの新規取引停止
- **10/27〜29**: Power Platform Community Conference 2026（MGM Grand ラスベガス）
- **11/1**: パートナー特典の有効期限がオファー購入日基準へ移行
- **12/2**: EU AI Act の生成コンテンツ標識義務、8/2 以前に市場投入済みシステムへの猶予終了
- **12/31**: M365 E3 プロモーション ／ Copilot in 30 ／ Purview Suite 50%オフの提供終了
- **8月中旬**: M365 Copilot Release Notes の次バッチ見込み
- **9月**: iOS 27 / macOS 27 GA ／ auto mode の既定化を Enterprise・API・各クラウドへ拡大予定
- **時期未定**: ドメイン除外の再提供 ／ Cowork 1 の提供開始 ／ Copilot Studio What's New への7月・8月節の追加とハーネス GA の反映

## 改善メモ

- Master: 新規提案 B-028（Anthropic Blog / News の検索キーワードに日付を含む形を必須化）と B-029（WebFetch が 5xx を返したとき `curl` 直接取得をフォールバックに加える）を追加した。継続提案は7件で、最多は B-013（403の2分類記録・14回目）である
- Copilot: 新規提案はない。board RSS の既存エントリが再投稿される事象は B-024 の追記として台帳へ反映した（回数5）。継続提案は19件で、最多は B-011（Power Platform Blog のトピック記事照合・22回目）である
- industry: 新規提案 B-023（JDLA を国内定点ソースに追加）を出した。継続提案は5件で、最多は B-004（取得方法の WebSearch 優先化・42回目）である
- 障害の変化: `cursor.com/changelog` と `/changelog/rss.xml` が WebFetch にのみ 503 を返す状態を新規記録した（`curl` は 200 で item 50件を取得できた）。`www.anthropic.com` は WebFetch が `EGRESS_BLOCKED`・`curl` が 403 を返し、B-027 の前提（`EGRESS_BLOCKED` ならゲートウェイ拒否と確定してよい）に対する反例になっている
- 障害の変化: `venturebeat.com` と `the-decoder.com` をゲートウェイ拒否として種別確定した（いずれも industry 側の最優先ソース）。`www.rippling.com` / `www.jdla.org` / `learn.chatgpt.com` の3ドメインも新規登録された
- 週次復旧チェック（月曜）では、既知のゲートウェイ拒否8ソースが1件も復旧していない（`www.testingcatalog.com` / `simonwillison.net` / `obsidian.md` / `blog.google` / `workspaceupdates.googleblog.com` / `x.ai` / `docs.devin.ai` / `learn.chatgpt.com`）
- Power Platform Weekly は 8/10（月）の休刊明け確認ができなかった。`ppweekly.com` の疎通そのものが環境側で塞がれており、新号が出たかどうかを判定する手段が現在ない
- ソース間の重複・矛盾: `learn.chatgpt.com` のゲートウェイ拒否を Master と industry が別々の文脈で記録している（Master は 308 転送先として、industry は新規ドメイン登録として）。また Codex CLI 0.147.0 の Agent Plugins 対応は 08-08 に収録済みだが industry が本日ハイライト級で扱っており、本サマリーでは新規部分（マーケットプレイスに Amazon Bedrock と Claude Code を含む点）だけをカテゴリへ落とした
