# AI News Daily Summary — 2026-09-16

既定が黙って入れ替わった日である。Claude Code は auto モードの `!` 実行と Monitor の常駐監視の既定を変え、Microsoft のアプリ生成は環境ルーティングを全テナントで強制的に有効にする。どちらも管理者・利用者の側で操作せずに変わる種類の変更で、告知だけを追っていると前提だけがずれる。Google は Gemini 3.8 Live を GA し、リアルタイム音声の単価が OpenAI 比で一桁下がった。

## 今日のハイライト

### 1. Claude Code の既定が4件入れ替わった — 上げれば同じ挙動のまま速くなるという前提が崩れる

**要点**: Claude Code が 9/14〜9/15 に `2.1.271` と `2.1.272` を出し、auto モードの `!` 実行・Monitor の常駐監視・動的ワークフローの既定サイズが変わった。前提は「上げれば同じ挙動で速くなる」から「上げる前に既定の変更4件を確認する」へ変わる。

**詳細**: `2.1.271`（9/14）は約90行の大型エントリで、うち挙動・既定の変更が4件ある。`2.1.272`（9/15）は不具合修正と安定性改善のみ。

- auto モード（inline シェル）: スキルとスラッシュコマンドの `!` シェルコマンドが、安全性 classifier ではなく default モードの権限ルールに従うようになった。どのルールも判定しないコマンドはツール呼び出しとして審査される
- Monitor: watch に必ず期限が付き（最大30分、単発の `-p` 実行では10分）、期限なしの `persistent` オプションが廃止された
- 動的ワークフロー: 既定サイズが Pro プランで small になり、medium の目安が 15→10 エージェントへ下がった
- auto モード（サブエージェント）: サブエージェントの復帰が専用のハンドバック呼び出し経由になり、最終メッセージを事後審査する方式をやめた

追加側では Bash / PowerShell / Monitor へのコマンド単位 `allowed_domains`、エージェント frontmatter の `omitClaudeMd`、`claude plugin install --accept-command <sha256>` が入った。権限まわりの修正は5件で、`fmt` / `column` 等が読むファイルの見落とし、ワイルドカード展開先の読み飛ばし、シェル変数宣言フラグによる実コマンドの偽装、`blockReadsOutsideWorkingDirectories` 下で `cd` 2回・サブシェル・`cd`+`git` 連鎖がプロンプトを飛ばす問題が含まれる。⚠️ npm の `dist-tags` は `{stable: 2.1.236, latest: 2.1.272, next: 2.1.273}` で、`2.1.273` は 9/15 18:06 UTC に publish 済みだが changelog には未掲載。`stable` は `latest` と36版差のまま据え置かれている。

- https://code.claude.com/docs/en/changelog
- https://registry.npmjs.org/@anthropic-ai/claude-code

### 2. アプリ生成が環境ルーティングを全テナントで強制有効にする — 管理者が無効化できない

**要点**: Cowork のアプリ生成は環境ルーティングを全テナントで自動的に有効にし、管理者はこの設定を変更できない。前提は「ルーティングは任意で入れる統制機能」から「アプリ生成を許した時点で入る既定」へ変わる。

**詳細**: 一次は `power-platform/admin/apps-default-environment-routing`（`ms.date` 2026-09-08）で、ページは冒頭で「この設定は変更できない」と明記している。9/8 の MC1469329 と 9/10 の告知ブログはいずれも掲載済みだったが、どちらも本ページを参照しておらず、告知を載せても統制の前提が載らない状態が8日続いていた。

- ルーティング規則が無いテナント: *Everyone* をメーカー個人の開発者環境へ流す規則が1本自動作成され、Default Environment Group も同時に作られる
- ⚠️ 既存のルーティング規則があるテナント: 新しい規則は追加されない。ページは「一部のメーカーがアプリを使えないことがある」と書き、管理者が *Everyone* 向けの規則を自分で作るよう求めている
- 規則そのものの制約: *Everyone* を対象にする規則は削除できず、1本しか持てず、優先順位の最後に置く必要がある
- ライセンス: アプリ用の個人開発者環境は既定でマネージド環境になる。Power Apps / Power Automate のリソースを作らない限りプレミアムライセンスは不要だが、作る場合は該当ライセンスが要り自動クレームの対象になる

ルーティングが有効になる範囲は他製品には広がらない。アプリ単独でルーティングが入ったテナントのメーカーは、Power Apps / Power Automate のメーカー画面を開いても個人開発者環境へは流されない。

- https://learn.microsoft.com/en-us/power-platform/admin/apps-default-environment-routing
- https://learn.microsoft.com/en-us/power-platform/admin/default-environment-routing

### 3. Gemini 3.8 Live が GA した — リアルタイム音声の単価前提が一桁変わった

**要点**: Google が音声対話モデル Gemini 3.8 Live を GA した。音声入力の単価は OpenAI `gpt-realtime-2.1` の約10分の1で、前提は「リアルタイム音声は高価」から「テキスト並みで試算できる」へ変わる。

**詳細**: 12日間止まっていた Gemini API changelog が 9/15 に動いた。公開されたのは低遅延の音声エージェント向けの `gemini-3.8-live` と、背景推論を強化した `gemini-3.8-live-extended-thinking` の2つで、いずれも Stable（GA）扱いになっている。⚠️ 9/2 GA の `gemini-3.8-flash` は Live API に非対応で音声をファイルとして受け取るだけだったため、双方向の音声ストリームを扱える GA モデルが Gemini 側に揃ったのは本日が初めてにあたる。

- 音声入力: Gemini $3.00／1M（$0.005／分）に対し OpenAI `gpt-realtime-2.1` は $32.00／1M — 約10.7倍の開き
- 音声出力: Gemini $12.00／1M（$0.018／分）に対し OpenAI は $64.00／1M — 約5.3倍の開き
- テキスト入出力: Gemini $0.75／$4.50 に対し OpenAI は $4.00／$24.00 — 入出力とも約5.3倍の開き
- 廉価版では差が縮む: OpenAI `gpt-realtime-2.1-mini` は音声 $10.00／$20.00 で、音声入力 約3.3倍・音声出力 約1.7倍にとどまる

⚠️ 課金単位の建て付けは同一ではない。OpenAI 側には `gpt-live-1` の $0.05／分というセッション課金の系統も併存し、Gemini 側は分課金とトークン課金が併記される。単価差を引く場合はどちらで比べたかを明示する必要がある。⚠️ Gemini 3.8 Flash の導入価格には 12/31 の期限が付くのに対し、Live 系の単価に期限の注記は見当たらない。

- https://ai.google.dev/gemini-api/docs/changelog
- https://ai.google.dev/gemini-api/docs/pricing
- https://developers.openai.com/api/docs/pricing

## カテゴリ別まとめ

### Claude / Anthropic

- **Claude Code の changelog**: `2.1.272`（9/15）と `2.1.271`（9/14）が載った（ハイライト1参照）。ハイライトに入らなかった追加分として、Remote セッション（クラウド / セルフホストランナー）で fast mode が使えるようになり、`modelPricing` 管理設定とゲートウェイの `pricing` ブロックが 1超〜10 までの `multiplier` を受け付けて社内チャージバックの上乗せ率を表現できるようになった。`--resume` が 1M コンテキスト（`[1m]`）を落とす問題と、VSCode 拡張の Attach Open File 設定の追加も入っている
- **Messages API のオンデマンドコンパクション**: 開発者が、会話の圧縮を任意のタイミングで実行できるようになった（9/14）。ベータヘッダー `compact-2026-09-04` で `compaction` パラメータを送ると署名つきの `compaction` ブロックが返り、後続リクエストで元のメッセージ列を置き換えられる。圧縮リクエストはバックグラウンドで走らせることができ、直近のターンを逐語で残す指定もできる。⚠️ 削減幅を示す数値は一次に記載がない
- **Salesforce in Claude**: 全ての有料 Claude プランの利用者が、ベータとして Salesforce 連携を使えるようになった（9/15）。8/26 に予告された「9月中のオープンベータ」が期日内に着地した形になる。37スキルを同梱し、アカウント調査・商談準備・パイプラインレビューと予測・CRM 更新・ディールスコアリングを扱う。権限は既存の Salesforce 権限の中で動き、既定では変更前に承認を求める。導入実績として 7,000名の Salesforce セラーが利用中とされる
- **Claude for Small Business**: Anthropic が 43ワークフローと27連携の追加を発表した（9/15）。コネクターは Shopify / TikTok / Atlassian / Zoom / Xero / Gusto / Square / Stripe / Zapier を含めて計37件になり、インストールは 90万回超に達している
- **Anthropic のコンピュート契約**: The Information が、Anthropic は11ヶ月で $517B・14.8GW のコンピュート契約を結んだと報じた。内訳は Amazon と Alphabet で合わせて約11GW・10年 $300B 超、Microsoft が Azure 約1GW に最低 $30B、SpaceX / Colossus が約 $45B、AMD が MI450 の2GW。⚠️ $517B は確定支出ではなくオプション・LOI を含む上限枠で、一次未読。Anthropic の公式発表も無い。Amodei の減速論（9/12）の3日後にあたる
- **モデル退役・単価**: Anthropic は退役ページにも単価にも新規の告知を出していない。直近告知は 2026-06-05 の Opus 4.1 で Active は11件のまま、単価は 9/1 の Fable 5.1 / Mythos 5.1（$10／$50・キャッシュ読み取り $0.25/MTok）以降変わっていない。`anthropic.com/news` は13件のままで、9/15 の新規公表は無かった
  - https://platform.claude.com/docs/en/release-notes/overview

### OpenAI / Codex / ChatGPT

- **Codex CLI**: OpenAI が pre-release を `rust-v0.155.0-alpha.7` まで進めた（9/15）。`alpha.6` も同日、`alpha.5` と `alpha.4` が 9/14 で、検出は `github.com/openai/codex/tags` の上位突き合わせによる
- **changelog・API**: ChatGPT & Codex changelog は 9/11 の Pets / Appshots の Windows 展開が最上位のままで 9/12〜9/15 の新規は無い。`developers.openai.com/api/docs/changelog` も 9/10 の3本（プロジェクト API キーの有効期限設定・Agents API パブリックベータ・GPT-Live 1 の GA）が最上位のまま動いていない
- **料金ページで未記録の2点を検出**: 全節の再列挙により、これまで記録に無かった注記が2件見つかった。⚠️ いずれも本日追加されたものか従来からあったものかは一次からは判別できない
  - ファインチューニング基盤の縮小: 「OpenAI is winding down the fine-tuning platform」と明記され、既存ユーザーは当面ジョブを作成でき、作成済みモデルは推論で使い続けられるとされる。廃止一覧の「2027年1月6日にジョブ作成停止」と整合する
  - `gpt-rosalind-research` の課金開始: ライフサイエンス向けの同モデルが入力 $5.00／キャッシュ $0.50／出力 $25.00 で掲載され、課金開始は 2026年10月5日と注記されている
- **主要モデルの単価は23日連続で据え置き**: GPT-6 Astra 短文脈 $10／$50、GPT-5.6 Sol 短文脈 $4／$20、Terra 短文脈 $2／$12、Luna 短文脈 $0.20／$1.20 はいずれも不変で、Batch・Flex の50%、Fast mode の2倍という倍率も変わらない。⚠️ 9/14 に消滅を確認した `gpt-5.4-cyber` の行は本日も不掲載で、停止（10/1）まで15日を残したまま一覧から外れた状態が続く

### Google

- **Gemini 3.8 Live**: 2モデルが GA した（ハイライト3参照）
- **Workspace 側**: Google は 9/12〜9/15 に Workspace Updates の新規投稿を出していない。9月アーカイブは 9/11 の6本が最新のままで、Gemini 関連の新規はデスクトップアプリの Windows 提供・Sheets の Android 対応・Notebook の外部共有管理で止まっている
- **Google が競合モデルを社内開放**: Google が社内 IDE の Antigravity 経由で全エンジニアに Claude Opus 5 を使わせ始めたと報じられた。これまで Claude へのアクセスは DeepMind の一部チームと優先案件に限られ、Claude Code と OpenAI Codex は社内で遮断されていた。従業員ごとの利用枠を付けた併用の位置づけで、Google は「Gemini remains our primary and foundational model for internal development」とコメントしている。⚠️ 一次未読で、出所は Business Insider。Google と Anthropic のどちらからも公式発表は出ていない
  - https://www.techmeme.com/260915/p5

### Microsoft 365 Copilot / Cowork

- **アプリ資産の管理面が Microsoft 365 管理センターに集約された**: 管理者が、Copilot Studio と Cowork で作られたアプリを棚卸し・コスト統制・作成経路の3軸で扱えるようになった（Copilot Studio Blog・9/15 20:09Z）。公開済みアプリは管理センターに一覧化され、作成者・ライフサイクル状態・データソースとコネクタ・適用ポリシー・稼働メトリクスが並び、同じ画面から停止・無効化・コネクタ削除・退役ができる。ビルドとランタイムは別サービスとして計量され、ランタイムは Power Apps Premium の既存リクエスト上限を超えた分が Copilot Credits で課金される。上限はユーザー単位で、環境単位の上限は「今後来る」とされる
  - ⚠️ プレビュー中は利用者が途中で遮断される。Learn の `microsoft-365/admin/manage/apps/` は「クレジット要件を満たさない利用者はまず警告を受け、20 操作または5分の利用のいずれか早い方でアクセスが遮断される」と規定する
  - ⚠️ 一次が片方の経路しか書いていない。Learn 側は表題からして「Apps overview for admins (Frontier)」で Cowork 経路しか記述しておらず、ブログが「既定で有効・推奨」と書く Copilot Studio 経路の Learn ページは本日時点で存在しない
  - https://techcommunity.microsoft.com/t5/copilot-studio-blog/managing-apps-built-in-copilot-studio/ba-p/4556774
- **従量課金の対象サービス**: 管理者が、Cowork・Cowork で作ったアプリ・Work IQ API の3つを管理センターの Copilot > Cost management から統制できるようになっている。⚠️ Cowork の有効化と無効化はアプリ生成機能も既定で同時に切り替える。スペンディングポリシーの Auto-apply new services は既定で有効なため、今後追加されるサービスとエージェントは既存ポリシーに自動で載る
- **Cowork の一次**: `cowork/` 配下18ページのうち5本が再ビルドされ、`updated_at` が 2026-09-15T02:43Z へ動いた（`use-cowork` / `get-started` / `cowork-faq` / `cowork-customize` / `cowork-available-plugins`）。モデルピッカーの8件と effort 5段に増減はなく、9/12 告知の Grok は Cowork 側にも Copilot Studio 側にも現れていない
- **Release Notes**: 新バッチは追加されていない。先頭見出しは August 25, 2026 のままで、隔週の期日 9/8（UTC）から8日、前バッチからは22日が経過した

### Copilot Studio / Power Platform

- **What's New**: 新しい月次節は追加されていない。July 2026 節が最新のままで8月節・9月節とも未作成、`updated_at` は 2026-08-20T19:04Z から27日動いていない。June 節の GitHub Copilot ハーネス表記も `(Production-ready preview)` のままで、GA（8/3）から44日連続の未反映になる
- **ガイダンスハブ**: 管理者向けの `manage-checklist`（`ms.date` 2026-09-14・掲載歴ゼロ）を本日はじめて把握した。前日ハイライトの `govern-credit-consumption` をチェックリスト化した内容で、Billing and capacity 節が環境の3分類・環境へのクレジット割当・探索用エージェントへの既定上限・上限アラートの承認経路・新規環境とエージェントの定期検出を求めている。⚠️ `guidance/toc.json` の相対 href は実際には170件あり、前日の突合が対象とした58ページは実体の3分の1だった
- **Released Versions**: 定例更新は入っていない。Copilot Studio Build は 2026.6.3 のままで、`released-versions/copilotstudio` の `updated_at` は 2026-07-01 から77日動いていない
- **Release Wave**: リネーム後の5ページはいずれも `updated_at` 2026-09-03T14:35Z で、9/3 から13日連続の据え置きになる。緑チェックの増減もない。Power Platform の非推奨一覧にも新規項目は追加されていない
- **Roadmap**: 新規起票が4日ぶりに動いた。Release Communications RSS の `lastBuildDate` は 2026-09-14T23:03Z で、最新は同時刻の2件である。⚠️ `Microsoft Copilot Studio:` で始まる項目は19件のまま全件 `In development` で、`Power Apps:` / `Power Automate:` / `Microsoft Dataverse:` の起票はいずれもゼロが続く
  - 571297（Teams: 疑わしいゲスト招待の報告・GA 2026年11月）: 利用者が想定外または悪意の可能性があるゲスト招待を Teams から直接 IT 管理者へ報告できるようになる
  - 571199（Outlook: 新しい Cloud Policy 制御・GA 2026年10月）: 管理者が Outlook on the web と新しい Outlook for Windows の対応設定に既定値を与え、利用者による変更可否を選べるようになる
- **Power Platform Blog**: 親ページ・子カテゴリとも新規記事はない。親の先頭は 9/3 の PPCC 2026 記事、Power Apps は 9/1、Power Automate は 8/13 で33日が経過している

### GitHub / 開発ツール

- **Copilot CLI**: GitHub が pre-release `v1.0.84-8` を出した（9/15 00:45 UTC）。`transcriptView` を `concise` にするとツール活動が折りたためる作業サマリーにまとまり、Agent Factory の実行を一時停止・再開できるようになった。⚠️ 安定版は `v1.0.83`（9/4）のまま11日間据え置きで、pre-release だけが日次で刻まれている
- **GitHub changelog に 9/15 付で3件**: GitHub が Advanced Security の設定強制・Copilot によるカスタムプロパティ提案・SHA-1 の廃止を掲載した。設定強制では、エンタープライズ管理者がエンタープライズ階層のセキュリティ設定をリポジトリ管理者に加えて組織管理者にも上書きさせないよう指定できる（3段階・GA）。SHA-1 の HTTPS 接続からの廃止は 4/20 の予告を経て 9/15 に実施済みで、GitHub Enterprise Server は対象外。⚠️ Copilot ラベル側は 9/14 の auto model selection 3ティアが最上位のままで、9/15 の新規は無い
- **Cursor**: changelog は 9/10 の Projects が最上位のままで6日間動きが無く、フォーラム Announcements も 9/2 の Grok Bot Android 版のまま14日間変化が無い。⚠️ Cursor は GPT-6 Astra の提供開始を告知しないまま13日目に入った（9/3 GA）。11/12 の OpenAI による供給停止予定と併せて読む必要がある
- **Grok 4.7**: xAI は公開予定日 9/12 を過ぎて4日目も Grok 4.7 を公開しておらず、新しい日程も示していない。⚠️ 2.1兆パラメータと SpaceX の社内エンジニアリングデータ利用はいずれも Musk の X 投稿が出所で、xAI 一次にはローンチページ・モデル ID・価格・ベンチマーク表のいずれも無い。公式提供中の最新は Grok 4.6（8/12・context 50万トークン・$2/$6）
- **Intelligent Terminal 0.2.2572**: `devblogs.microsoft.com/commandline` に 8/31 付で速度・安定性の改善版が出ていることを本日はじめて把握した。前回までの記録は「AI 関連の最新は 8/10 の Intelligent Terminal 0.2」だったので、2週間ぶんの取りこぼしを回収したことになる
- **Devin**: Cognition の一次・代替一次はいずれも読めない状態が続いている（`docs.devin.ai` / `cli.devin.ai` ともゲートウェイ拒否）

### MCP / オープンウェイト

- **MCP 公式ブログ**: Model Context Protocol は 8/22 の「The New MCP Roadmap」が最上位のまま25日間新規が無い。その前は 7/28 の 2026-07-28 仕様にあたる。WebMCP Challenge は提出締切を経過し、受賞発表 9/23・賞金総額 $35,000 を待つ状態が続く
- **オープンウェイト8 org**: 登録8 org のいずれにも 9/12〜9/15 に作成または更新されたリポジトリは1件も無かった。`createdAt` 降順と `lastModified` 降順の両方で確認しており、直近の最新作成は `deepseek-ai/DeepSeek-V4.1-Flash`（9/10）のまま、9/11 以降5日間は新規作成も更新もゼロである

### 市場データ / 企業構造・GTM

- **定点ソースに新規公表なし**: IDC / MM総研 / NRC / Similarweb のいずれにも新規公表は無く、引用可能な値は前日から変わらない。Similarweb の8月分は ChatGPT 55.5%・Gemini 25.6%・Claude 9.3%・DeepSeek 3.4%・Grok 2.4%・Copilot 1.6% で、12カ月前の ChatGPT 73.3%・Gemini 12.9%・Claude 1.9% と比べると1年で Claude が約5倍・Gemini が約2倍になる
- **Anthropic の S-1 は非公開のまま**: Anthropic は 2026年6月1日に Form S-1 の草案を機密提出しており、公開版の提出は本日時点で確認できない。株数と価格は未設定のままである。⚠️ 二次記事に「10月上場が決定済み」と読める表現が散見されるが、機密提出は上場日程の確定を意味しない
- **Partner Center**: Microsoft は 9/10 から新規の告知を出していない。9月告知は9件のままで6日連続の追加なしになる。既収録の CSP ソフトウェア価格改定（10/1 発効）にも変更の告知は無い
- 既報: Amodei の論考「We Must Pace the Frontier」（9/12）と Altman・Musk の同調、Microsoft AI の MAI モデル行動規範草案（9/14・公開協議は 10/26 頃まで）、Altman の年内 IPO 否定（9/12）、OpenAI → Cursor のモデル供給停止（遮断予定 11/12）、SpaceX による Cursor 買収完了（8/14・$60B）

## 直近の注目予定

- **9/17**: OpenAI DevDay Exchange の応募締切 ／ Anthropic Startup Grant Program の配分年度締切（二次のみ）／ Copilot Studio 版アプリ生成の公開プレビュー
- **9/18**: 新 iPhone と AirPods 5 の発売
- **9/21**: Anthropic ウェルビーイング研究助成の応募締切 ／ 週次復旧チェック（月曜）
- **9/22 前後**: M365 Copilot Release Notes の次バッチ
- **9/23**: WebMCP Challenge の受賞発表 ／ Partnering for Success Together の初回開催
- **9/24**: OpenAI の Videos API と Sora 2 系が退役（代替モデルの提示なし）
- **9/28**: OpenAI の `gpt-3.5-turbo-instruct` / `babbage-002` / `davinci-002` / `gpt-3.5-turbo-1106` が停止 ／ Copilot のチャット3面統合 ／ code review の既定 effort が Lite → Balanced ／ チャットのデータ保持がアカウント存続期間へ
- **9/29**: OpenAI DevDay 本体（サンフランシスコ Fort Mason・基調講演はライブ配信）
- **9/30**: Gemini の旧 `gemini-omni-flash-preview` エンドポイント廃止 ／ OpenAI の現行 OneGov 契約（$1/年）が失効 ／ M365 E7 プロモ最終日 ／ E5・E3 の CSP 割引終了 ／ 2026 Wave 1 の対象期間終了
- **9 月末**: Claude for Financial Advisors の新規ライセンス申請に付く一度限りの利用クレジットの期限
- **9 月中**: macOS 27 GA ／ Copilot Tuning の Public Preview 再開 ／ DLP for Microsoft Cowork の Preview（570845）／ Release Plans の新規掲載停止
- **10/1**: OpenAI の `gpt-5.4-cyber` が API から削除（移行先 `gpt-5.6-cyber`）／ OneGov トークン課金50%割引が開始 ／ Copilot Business・Enterprise の既存顧客が前払い必須に ／ Microsoft CSP ソフトウェア価格改定が発効 ／ Apple の EU 向け新ビジネス条件が発効
- **10/2**: GitHub Copilot が Gemini 3.5 Flash / Gemini 3.6 Flash / Kimi K2.7 Code / Claude Opus 4.7 を全体験から廃止
- **10/5**: `gpt-rosalind-research` の課金が開始 ／ Anthropic ウェルビーイング研究助成の full proposal 提出期限
- **10/16–11/11**: OpenAI DevDay Exchange 8都市（東京は 10/20）
- **10/23**: OpenAI のレガシースナップショット退役（`gpt-3.5-turbo-0125` / `gpt-4-0613` / `o1-2024-12-17` 等）
- **10/26 頃**: Microsoft AI の MAI モデル行動規範に対する公開協議が終了
- **10/31**: OpenAI の既存 evals が読み取り専用になる
- **10 月**: Anthropic の IPO 観測（$2兆超の評価額を目標と報道・上場日は未確定）／ DLP for Microsoft Cowork の GA ／ 571199（Outlook の Cloud Policy 制御）の GA
- **11/12**: OpenAI が Cursor へのモデル供給を停止する予定日
- **11/15**: Microsoft Release Planner が退役
- **11/21**: GPT-5.6 Sol の暫定値下げが有効とされる期限
- **11/30**: OpenAI の Reusable prompts・Evals プラットフォーム・Agent Builder が停止
- **11 月**: 571297（Teams の疑わしいゲスト招待の報告）の GA
- **12/1**: OpenAI の GPT Image 系が停止（→ `gpt-image-2`）
- **12/2**: EU AI Act の生成コンテンツ標識義務、8/2 以前に市場投入済みシステムへの猶予終了
- **12/11**: OpenAI の旧スナップショット退役（`gpt-5-2025-08-07` / `o3-2025-04-16` 等）
- **12/31**: Gemini 3.8 Flash と 3.7 Flash の導入価格が終了 ／ GitHub Copilot の Fable 5.1 / Fable 5 に対する ZDR 暫定免除が終了
- **年末**: Microsoft AI の MAI モデル行動規範の改訂版公開予定
- **2027-01-06**: OpenAI でファインチューニングのジョブ作成が終了
- **2027-01-20**: OpenAI の audio / realtime 系が退役
- **2027-02-26**: OpenAI の文字起こし4モデルが退役
- **2027-03-01 / 2028-10-01**: SharePoint クラシック体験の退役

---

## 改善メモ

- 新規提案 3件: **B-073**（Master）Claude Code Changelog 項の注目点に「`Changed` で始まる行を既定・挙動の変更として別枠で拾う」を明記 ／ **B-069**（Copilot）アプリ生成の管理者向け一次3本が `daily-sources.md` 未登録で掲載歴ゼロ ／ **B-068**（Copilot）ガイダンスハブの `ms.date` 全件突合の対象リストが実体の3分の1
- 継続提案: Master 16件（最多 B-013 403の2分類記録・44回目）／ Copilot 56件（最多 B-011 Power Platform Blog の取得方法変更・57回目）／ industry 4件（最多 B-004 取得方法欄の WebSearch 化・79回目）
- 障害の変化: 3ソースとも新規発生・復旧なし
- ソース間の重複・矛盾: Claude Code `2.1.271` / `2.1.272` と Messages API のコンパクションを Master と industry が同日に扱ったが、内容の矛盾はなく本サマリーでは Master 側の項目数の多い記述をベースに統合した。⚠️ industry は同2件を 09-15 時点で「掲載なし」と記録しており、掲載の遅れ側に原因がある可能性を指摘している
