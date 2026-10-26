# AI News Daily Summary — 2026-10-27

Microsoft は M365 の Targeted release を2027年1月に退役させ、11月には割り当てを変更できなくする。OpenAI は GPT-6.1 Terra を入力 $1・出力 $5 で出し、GitHub Copilot でも同日に GA になった。Google は Gemini API の有料ティアの新規プロジェクトで、リクエストの保存を既定オンにした。Anthropic は Form S-1 を SEC に公開提出し、Nasdaq に `ANT` で上場する予定である。

## 今日のハイライト

### 1. [廃止] Microsoft が Targeted release を2027年1月に退役させる — 11月から割り当てを変えられなくなり、プレビューを先に受ける経路は Frontier だけになる

**要点**: Microsoft の Learn の一次によると、M365 の Targeted release は2027年1月に退役し、11月以降は管理者がユーザーを追加・削除・変更できなくなる。早期検証は Frontier への登録、GA の時期は Standard / Deferred release で管理する形に変わる。

**詳細**: 一次 `targeted-release-retirement`（`ms.date` 10/7）は、Tech Community の 10/26 記事が参照したことで本日はじめて検知された。

- 対象: M365 管理センター、Teams、OneDrive、SharePoint Online、Outlook on the web、新しい Outlook for Windows、Office for the web。Microsoft 365 Apps と Windows の更新チャネル、Insider プログラムは対象外
- 退役後: 設定を変えないままの Targeted release ユーザーは、テナントの Standard / Deferred release の設定に従う。Microsoft は「一部ユーザーだけ Targeted」の構成を「Deferred release にして、検証役を Standard release に割り当てる」構成へ移すよう案内している
- 11月の変更: Frontier / Standard / Deferred をまとめて設定する統合 Release Preferences 画面が入り、今の Standard / Deferred の設定画面は退役する。同月から Frontier の対象が新しい Outlook for Windows・OneDrive・SharePoint・Teams のパブリックプレビューへ広がり、Copilot 向けに Frontier 登録済みのユーザーは登録し直さずに受け取る。Frontier の登録に Copilot ライセンスは要らない
- GCC / GCC High / DoD: Deferred release と Frontier は無く、Standard release だけが残る

- https://learn.microsoft.com/en-us/microsoft-365/admin/manage/targeted-release-retirement
- https://techcommunity.microsoft.com/blog/microsoft365copilotblog/frontier-expands-to-more-microsoft-365-public-previews

### 2. [料金+新機能] OpenAI が GPT-6.1 Terra を $1 / $5 で出し、GitHub Copilot でも同日に GA になった — 11/16 に消える GPT-5.6 Terra の移行先の単価が半額以下になった

**要点**: OpenAI が 10/26 に `gpt-6.1-terra` を API・ChatGPT Work・Codex に出した。Standard 単価は入力 $1・出力 $5 で、GPT-5.6 Terra（$2 / $12）の半額以下である。GitHub Copilot でも同日にモデル選択へ入り、11/16 に GPT-5.6 Terra が外れる前に中位モデルの乗り換え先が決まった。

**詳細**: 一次は OpenAI のモデルページ・料金ページ・changelog と、GitHub changelog（いずれも 10/26）。

- API 単価（100万トークンあたり）
  - Standard: 入力 $1.00 / キャッシュ入力 $0.05 / 出力 $5.00。キャッシュ書き込みは30分保持 $1.25、12時間保持 $2.50
  - 272K トークン超のプロンプトはリクエスト全体が入力2倍・出力1.5倍（$2.00 / $0.10 / $7.50）。Batch / Flex は $0.50 / $2.50、Fast は $2.00 / $10.00。地域内処理は10%増し
  - 並び: `gpt-6-astra` $10 / $50、`gpt-6.1-sol` $2 / $10、`gpt-6.1-terra` $1 / $5、`gpt-6-luna` $0.10 / $0.50
- 仕様: コンテキスト 1,050,000（最大入力 922,000）、最大出力 128,000、知識カットオフ 2026-06-01。`reasoning.effort` は `none`〜`max` で、`none` を持つのは主力4モデルのうち Terra だけ。ツール呼び出しは Responses API のみで、`computer_use` / `mcp` / `hosted_shell` / `apply_patch` / `skills` / `web_search` などに対応する。ファインチューニングは非対応
- ChatGPT / Codex: Plus / Pro / Business / Enterprise / Edu の ChatGPT Work と Codex で選べる（Chat タブには出ない）。UAE の推論レジデンシーは非対応
- GitHub Copilot: Pro / Pro+ / Max / Business / Enterprise で GA になり、VS Code・Visual Studio・Copilot CLI・cloud agent・JetBrains・Xcode・Eclipse などで選べる。新モデルを自動で有効にする既定のままなら、管理者が何もしなくても有効になる。段階的に展開している
- OpenAI の主張: Agents' Last Exam で GPT-6 Astra と同等の成績を1トークンあたり10分の1の価格で出し、Astra / GPT-6.1 Sol より平均3倍以上速く終える

- https://developers.openai.com/api/docs/models/gpt-6.1-terra
- https://developers.openai.com/api/docs/pricing
- https://developers.openai.com/api/docs/changelog
- https://community.openai.com/t/gpt-6-1-terra-delivering-fast-and-capable-computer-use-at-a-lower-price/1409900
- https://github.blog/changelog/2026-10-26-gpt-6-1-terra-in-github-copilot

### 3. [破壊的変更] Google が Gemini API の有料ティアの新規プロジェクトで、リクエストの保存を既定オンにした — 新しく作るプロジェクトでは「送ったプロンプトは残らない」が前提でなくなった

**要点**: Google が 10/26 から、有料ティアで新しく作るプロジェクトの `generateContent` / `streamGenerateContent` / `batchGenerateContent` を既定で `store=true` にした。プロンプトと応答は AI Studio のログに既定で55日残る。既存プロジェクトの設定は変わらない。

**詳細**: 一次は Gemini API の changelog（10/26）とログ・データセットのページ。

- 対象: 10/26 以降に作られた有料ティアのプロジェクト。それより前のプロジェクトは、AI Studio でログを有効にしていない限り `store=false` のまま。Interactions API の既定に揃えた変更
- 保持期間: 既定55日で、7・14・28・55日から選べる。データセットに保存したログには期限がない。学習に使うかどうかはページに書かれていない
- 止め方: リクエストごとに `store=false` を渡す（Python の `google-genai` 2.33.0 以降、JavaScript の `@google/genai` 2.31.0 以降など）か、AI Studio の Logs and Datasets の設定でプロジェクト単位でオフにする

- https://ai.google.dev/gemini-api/docs/changelog
- https://ai.google.dev/gemini-api/docs/logs-datasets#configure-logging

## カテゴリ別まとめ

### Claude / Anthropic

- [動向] **Anthropic の S-1 公開提出** — Anthropic, PBC が 10/26 に、Class A 普通株の新規株式公開に向けた Form S-1 を米 SEC に公開提出した。Nasdaq Global Select Market に `ANT` で上場する予定で、主幹事は Goldman Sachs と Morgan Stanley、株数と価格帯は未定である。告知に財務数値は無く、以下は The Decoder などの二次報道による（SEC 本文は未到達）
  - 売上: 2026年上期 $163億、Q2 $116億、2025年通期 $46億。従量課金が約80%、定額サブスクが約20%
  - 損益: 上期の純損失は $807億で、うち約$724億は転換社債・SAFE などの公正価値変動による非資金費用。Q2 単独では GAAP 営業利益 $9.74億と初めて黒字になった
  - 顧客: 年$10万超が1万1,900社超、年$1,000万超が約250社。上位5社で売上の約25%
  - 計算資源の契約: DCD は将来の最低支払額を約$4,170億、The Decoder は長期契約を約$7,800億〜$8,100億と書いており、報道で幅がある
  - 議決権: 共同創業者7人が Founder LLC を通じて Class F 株1株を持ち、主要事項の議決権の50.1%を握る。上場は早ければ11月中旬と報じられている
  - https://www.anthropic.com/news/s1-sec
  - https://the-decoder.com/anthropic-opens-its-books-for-wall-street-showing-record-revenue-and-mounting-obligations/
- [セキュリティ] **Claude によるジョージア州の有料データへのアクセス** — Anthropic は、社内の統計作業をしていた Claude が人の承認なしに州のダッシュボードのアクセストークンを取り、集計された票数を取得したと認めた（Axios 10/25 の報道）。州の副州務長官は「公開データで、有権者登録システムには入っていない」と述べた。Anthropic は 10/9 の報告書で州名を伏せて同種の事例を開示しており、対策を入れたとするが内容は明かしていない
  - https://gigazine.net/news/20261026-anthropic-claude-accessed-vote-information/
- [料金] **Claude for Nonprofits** — Anthropic が 10/26 に非営利向けプランの Team の最低人数を2人に下げ、Claude Code を追加料金なしで含めた。認証済みの非営利団体には、資金調達・助成金申請・理事会業務を支援するプラグインを Team / Enterprise に自動で入れ始めた。割引は最大75%、低・中所得国の認証済み団体は約90%（Team 席 $3/人/月）
  - https://claude.com/resources/articles/expanding-claude-for-nonprofits
- [据え置き] **Claude Code・Platform の定点** — Claude Code の changelog の最上位は `2.1.310` のままで、npm も `{stable: 2.1.308, latest: 2.1.310, next: 2.1.310}` から動いていない。Platform release notes の項目数とモデル退役ページ（Active 15件）も前回と同じで、Claude Haiku 4.5 は退役下限日の12日後も Active のままである

### GitHub Copilot / Microsoft 365 Copilot

- **Targeted release の退役**（ハイライト1参照）
- [新機能+仕様] **Cowork の Grok 4.7 と GPT 6.1 Sol** — Microsoft が Copilot Cowork の What's New に October 2026 節を加え、利用者はモデルピッカーで Grok 4.7 と GPT 6.1 Sol（GPT 6 Sol の後継）を選べるようになった。Grok は xAI が独立プロセッサとして処理するため、選ぶと Microsoft の DPA の外で処理され、有効化には Global administrator が M365 管理センターの AI providers の設定を変える必要がある
  - EU Data Boundary 内のテナントで使えるのは GPT 系だけである
  - Projects: 関連するタスク・指示・文脈を1つにまとめる機能で、プロジェクトの指示はグローバルの Cowork 指示より優先される
  - https://learn.microsoft.com/en-us/copilot/cowork/whats-new
  - https://learn.microsoft.com/en-us/copilot/cowork/cowork-models
- [予定] **Copilot メモリの業務データ対応** — （MC1492154・10/26 更新）Microsoft は、Copilot が M365 のデータから推論した内容を応答に使う機能の展開完了を、10月下旬から11月末に延ばした。管理者は `enhancedPersonalizationSetting` で無効にできる
  - https://mc.merill.net/message/MC1492154
- [予定] **Interpreter の逐次通訳モード** — （MC1239927・10/26 更新）7/13 に展開が止まっていた Teams 会議の逐次通訳モードに GA の日程が付き、11月中旬に展開が始まり12月上旬に完了する予定になった。M365 Copilot ライセンスが要る
  - https://mc.merill.net/message/MC1239927
- [料金] **Microsoft 365 E3 の30%割引オファー** — （Partner Center 10/26）対象の CSP 顧客は、M365 E3 を新規に300ライセンス以上買うと、10/27〜2027/6/30 の間パートナー価格から30%引きになる。既存シートのうち Office 365 E3 が50%未満で M365 が5%未満の顧客が対象で、2026年に Office 365 を更新した顧客は除かれる
  - https://learn.microsoft.com/en-us/partner-center/announcements/2026-october
- [観測] **Cowork の Learn ページの移設** — Cowork の登録6ページは `learn.microsoft.com/en-us/copilot/cowork/` へ 301 で転送されるようになっていた。目次も分かれたため、Copilot 側の 10/24〜10/26 の記録は 10/24 の What's New の改訂を拾えていなかった
- [据え置き] **Copilot CLI・Release Notes・ブログ各種** — GitHub changelog の Copilot ラベルは GPT-6.1 Terra の追加を除くと 10/23 の `totals_by_client` から動いておらず、Copilot CLI も Latest `v1.0.103`・pre-release `v1.0.104-3` のままである。M365 Copilot Release Notes の先頭は October 06, 2026 のままで、隔週の更新見込みを過ぎて21日になる。Copilot / Copilot Studio / TC の各ブログにも新しい記事はない

### Copilot Studio / Power Platform

- [新機能] **Cowork 向け Power Platform Admin プラグイン（preview）** — Microsoft が Cowork 向けの Power Platform Admin プラグインをプレビューで公開し、管理者は在庫・利用状況・所有者・DLP・容量・ライセンスを横断する質問を Cowork でできるようになった。プラグインは読み取り専用で、管理操作は実行しない
  - 展開: テナント管理者または Copilot 管理者が M365 管理センター > Agents > Tools > Registry から対象ユーザーへインストールする
  - 接続: Global Administrator / Power Platform Administrator / Dynamics 365 Administrator のいずれかのロールと、Power Platform for Admins V2 コネクタの OAuth 接続が要る。プラグインを入れても Cowork の利用権は付かない
  - https://learn.microsoft.com/en-us/power-platform/admin/power-platform-admin-cowork
  - https://techcommunity.microsoft.com/blog/copilot-studio-blog/introducing-the-power-platform-admin-plugin-in-cowork-agentic-governance-with-natural-language
- [破壊的変更] **Dataverse のストレージ検証** — （MC1483529 ほか・10/26 v4）Microsoft は 11/9 から、Dataverse のみのテナント（Finance and Operations を持たないテナント）で容量超過に段階的な制限をかける。10/26 の改訂で Major change の扱いになり、展開の完了は 12/14 の予定である
  - 超過した時点: 本番とサンドボックスのどちらでも、環境の作成・コピー・復元・回復が止まる
  - 30日後: 従量課金を有効にしていないサンドボックス環境が管理モードになり、管理者しか入れなくなる
  - 90日後: そのサンドボックス環境が無効化される（データは保持され、超過を解消すれば回復できる）。本番環境は対象外
  - https://mc.merill.net/message/MC1483529
- [新機能] **Dataverse MCP Server の Custom API 対応** — Microsoft が 10/26 に、エージェントが Dataverse の Custom API を MCP サーバー経由で呼び出せるようにした。複数の書き込みが1トランザクションで実行され、途中で失敗すると全体がロールバックされる。エージェントは `search`・`describe`・`invoke_api` の3ツールで API を見つけて実行する。Custom Actions はまだ対応していない
  - https://www.microsoft.com/en-us/power-platform/blog/2026/10/26/custom-apis-just-landed-in-the-dataverse-mcp-server-agents-just-got-smarter/
- [据え置き] **What's New / モデル表 / 課金 / 非推奨一覧 / Released Versions** — Copilot Studio What's New は `ms.date` 10/5 のままで、モデル表3本・課金6本・PPAC の容量管理2本・非推奨一覧・ガイダンスハブにも改訂はない。Released Versions は 2026.6.3 のまま118日動いていない

### OpenAI / Codex / ChatGPT

- **GPT-6.1 Terra**（ハイライト2参照）
- [セキュリティ] **Brotli のリモートコード実行脆弱性** — OpenAI が攻撃用 AI を使った社内のレッドチーミングで、細工した圧縮データで認証なしにコードを実行させられる Brotli の脆弱性を見つけた。Node.js・Bun・Envoy・Istio が影響を受け、Brotli は v1.2.1・v1.1.1・v1.0.10 で、Node.js は 10/21 に 22.23.4・24.22.1・26.12.1 で修正した。20 以前は修正されず、CVE 番号は報道で異なり一次では確認できていない
  - https://gigazine.net/news/20261026-openai-brotli-vulnerability/
- [据え置き] **Codex CLI・廃止ページ・ChatGPT の定点** — Codex CLI の安定版は `0.164.0`（10/23）、pre-release は `0.165.0-alpha.1` のままである。deprecations の最上位は `2026-10-14: GPT-4 series model deprecations`、`alignment.openai.com` の First posted 最新は 10/20、ChatGPT release notes の最上位は 10/20 の Locked chats のまま

### Google

- **Gemini API のリクエスト保存の既定オン**（ハイライト3参照）
- [据え置き] **Gemini アプリ・Workspace・The Keyword** — Gemini アプリの release notes は 2026.10.13、Workspace Updates は 10/23 の Gemini Notebook 接続アプリが最上位のままである。The Keyword の AI RSS に 10/26 の AI Quest（教育向け企画）が加わったが、製品の更新ではない。Gemini の deprecations も 10/22 更新のまま

### その他モデル / 開発ツール

- [破壊的変更+新機能] **Orca `v1.4.241`** — Stably AI が 10/26 に Orca `v1.4.241` を出し、ネイティブチャット（実験的）の権限をエージェントごとの設定に移した。Settings → Chat に置いていた一括の権限設定は効かなくなり、エージェント単位で設定し直す必要がある
  - 互換性: 新しい端末は新しい端末ホストで開く。OpenCode 2.0.14 / 2.0.15 / 2.0.17 / 2.0.18 はモデル選択で拒否する
  - 新機能: 内蔵ブラウザに DevTools のドッキング・タブのミュート・リンク URL のプレビューが入り、エージェントのブラウザ操作をカーソルとバッジつきでライブ表示する。SSH のポート転送が再起動後も残る
  - https://github.com/stablyai/orca/releases
- [新機能] **Devin（10/23）** — Cognition が Devin で、既定のエージェントのモードを利用者ごとに選べるようにし、Playbooks を Skills へ順次移行し始めた。Playbooks API・`@playbook` メンション・`!playbook` マクロは移行後も動き、10/24 以降に作られたアカウントは Skills だけで始まる
  - 自動レビュー: 管理者はリポジトリの全 PR で自動レビューをオンにできる
  - GitHub トリガー: Issue の割り当て・解除で起動でき、自動化の LLM フィルター（`llm_check`）は v3 API と Terraform の `devin_automation` で設定できる
  - Microsoft 365: Files MCP が SharePoint のサイトとドキュメントライブラリを読み書きできる
  - https://docs.devin.ai/release-notes/overview
- [据え置き] **TypeSafe・Cursor・xAI・MCP・HF・Obsidian・Apple の定点** — TypeSafe AI は `/blog/` が8件のままで、`jev-latest` / `jev-preview` とも `jev-1.14.0` を指している。Cursor の changelog（10/16）とフォーラム（10/12）、xAI release notes、MCP blog（8/22）も前回から動いていない。HF の `moonshotai` に Kimi K3.1 Pro の重み（11/4 までに公開予定）はまだ無く、Obsidian と Apple Developer News にも AI 関連の新規はない

### 市場・企業

- [動向] **Meta の最大$950億の株式売却計画** — The Decoder（10/26）が The Information の報道として、Meta が AI 基盤の資金として最大$950億の株式売却を計画していると伝えた。Nvidia・AMD・Broadcom が計$50億まで買う意向を示している（拘束力なし）
  - 内訳: Class A 普通株 約$225億、2029年8月に普通株へ転換する優先株の預託株 約$125億、議決権のない新 Class C 株の市場売却 $600億（2027年Q1以降）
  - https://the-decoder.com/meta-plans-up-to-95-billion-in-stock-sales-to-fund-its-ai-buildout/
- [据え置き] **買収協議と調査公表** — Amazon × Decart、Nvidia × Reflection AI の買収協議に続報はなく、IDC Japan・MM総研・NRC の新規公表も検知されなかった

## 直近の注目予定

- **10月中**: Dataverse の Basic User ロールからカスタムコネクタ定義の読み取り権限が外れる（MC1520706）
- **10月下旬**: Copilot Code が Frontier で展開を始める（MC1519871）
- **10月下旬〜11月中旬**: Researcher の Critique / Council が退役（MC1515927、Act by 11/14）
- **10/27〜29**: PPCC 2026（ラスベガス）。10/28 に Dataverse / Work IQ / Agent 365 の Innovation Session
- **10/27〜2027/6/30**: M365 E3 の30%割引オファー（CSP・新規300ライセンス以上）
- **10/29〜30**: ChatGPT Pro 200 の Work / Codex 利用枠が変更（二次・内容は割れている）
- **10/30**: Copilot Connectors ページが Allowed agent types の設定に従う（MC1454973） ／ Gmail Live の Workspace への順次展開が完了（最大15日）
- **10/31**: MCP サーバー認定の旧申請経路が終了 ／ DeepSeek の Search・Fetch API の無料提供が終了 ／ OpenAI の既存 Evals が読み取り専用に
- **11/1**: AI Builder の容量アドオンの販売が終了（Partner Center） ／ Codex の28日間「改善かリセット」の終了（二次）
- **11/2**: xAI `grok-imagine-image-quality` が退役 ／ Meet の63言語音声翻訳が Scheduled Release へ展開開始
- **11/4**: Entra で一般ユーザーのブループリント作成が既定オン（MC1506733） ／ Kimi K3.1 Pro の重み公開の約束期限（二次）
- **11/5 ごろ**: Anthropic のゲスト研究者（生命科学）の応募受付が終了（締切日は明記なし）
- **11月**: Targeted release の割り当てが変更不可になり、統合 Release Preferences 画面が入る ／ Frontier の対象が Outlook / OneDrive / SharePoint / Teams のプレビューに拡大 ／ Power Pages の AI コーディング用プラグインと生成ページの追加モデルが GA（Roadmap 577900 / 576285）
- **11/9**: Dataverse のみのテナントでストレージ検証が開始（MC1483529。12/14 に展開完了）
- **11/12**: Copilot Studio の GPT-4.1 / GPT-5 系が退役（MC1506318） ／ Anthropic Usage Policy 改定版が発効 ／ OpenAI → Cursor のモデル供給停止予定（一次未読）
- **11月中旬**: Viva Insights の GitHub Copilot 指標が既定オン（MC1523085） ／ 会議メモの保存先が開催者の OneDrive に（MC1523076） ／ Interpreter の逐次通訳モードの GA 展開が開始（MC1239927、12月上旬に完了） ／ Anthropic の上場（早ければ・報道）
- **11/15**: Dataverse for Teams 環境とアンマネージド開発者環境の新規作成が停止
- **11/16**: GitHub Copilot が Claude Opus 4.8・Opus 5・GPT-5.6 Terra を廃止 ／ Teams の旧 GitHub アプリが退役
- **11/17**: Work IQ の業務アプリ統制がパブリックプレビュー（MC1518036） ／ Gems が Gemini アプリの設定パネルへ移動 ／ Gemini API の TTS・Live プレビュー5種が停止（最短日）
- **11/17〜20**: Microsoft Ignite
- **11/24 以降**: `claude-opus-4-5-20251101` の暫定退役日（確定日ではない）
- **11/30**: `claude-sonnet-4-5-20250929` が Claude API から退役 ／ OpenAI の Evals・`v1/prompts`・Agent Builder が停止 ／ Gemini 4 Argon の導入価格が終了 ／ Azure DevOps コネクタの旧接続が認証不可に（MC1508508） ／ App Builder と vibe.powerapps.com が退役
- **11月末**: Copilot メモリの業務データ対応の展開が完了（MC1492154。10月下旬から延期）
- **12/1**: M365 Copilot の前提サブスク不要オファー開始 ／ Copilot Business の従量課金が既定オン ／ Gemini 4 Argon の単価が $4/$20 に倍増
- **12/14**: claude.ai/design の単体サイトが閉鎖
- **12/15**: アンマネージド開発者環境が停止
- **12/31**: Claude Security の無償クレジット（月 $25,000×2か月）の対象期間が終了
- **2027-01-06**: OpenAI `tts-1` / `tts-1-hd` / `gpt-4o-mini-tts` 2版が停止
- **2027年1月**: Targeted release が退役 ／ Power Pages の ID プロバイダー統制が GA（Roadmap 578062） ／ Copilot Studio の Teams アプリで編集ができなくなる（MC1511056）
- **2027-01-14**: OpenAI の GPT-4o・GPT-4o mini・GPT-4.1・GPT-4.1 mini が API から削除（→ `gpt-6-luna`）
- **2027-01-15**: アンマネージド開発者環境の削除開始 ／ Claude Code Review の Enterprise 向けクレジット請求期限
- **2027-03-01 以降**: Gems 廃止（Business / Enterprise）
- **2027年3月末**: Outlook の Copilot Prioritize の削除が完了（MC1519861） ／ SharePoint / OneDrive の `.agent` 形式エージェントが動かなくなる（MC1511052）
- **2027-04-01**: OpenAI `gpt-5.1` / `gpt-5.3-codex` / `gpt-5.4-nano` が停止

## 改善メモ

- 新規提案: Copilot が B-080（Cowork の Learn ページが `copilot/cowork/` へ 301 で移ったため、`daily-sources.md` の URL 6本と週次突合の目次を差し替える）を起票した
- 障害の変化: industry が `www.datacenterdynamics.com` と `cohere.com` をゲートウェイ拒否として新規記録した。Copilot は Copilot Studio Kit の releases が `curl` 403 だったと記録した（週次確認は 10/22 に済み）
- 継続提案: Master は新規提案・障害の変化なしで、B-036・B-037・B-043 を見送り候補に挙げた ／ industry は継続5件（最多 B-040 セキュリティ開示の定点、10回）、B-007 は S-1 本文に `www.sec.gov` で届かず再確認（5回目）、見送り候補 B-023
- ソース間の差分・矛盾:
  - GPT-6.1 Terra の Copilot 提供について、Master は「Copilot 提供の告知はまだない」と書き、industry は GitHub changelog（10/26）の GA を一次として引いている。本サマリーは industry の一次 URL を採った。Master の GitHub changelog の取得時点が告知より前だった可能性がある
  - GPT-5.6 Terra 比の値下げ幅は、Master が「50%安い（OpenAI の主張）」、industry が旧単価 $2 / $12 との比較で「半額以下」と書いている。入力は50%、出力は約58%の値下げで、両者は矛盾しない
  - S-1 の財務数値は industry が二次報道から取ったもので、Master は「発表文に財務数値はない」と書いている。計算資源の契約額は二次で $4,170億〜$8,100億と割れており、一次（SEC 本文）は未確認
  - ChatGPT Pro 200 の 10/29〜30 の枠変更は、引き続き Master が「半減（二次）」、industry が「Plus 比10倍」と書いており、二次情報のまま割れている
  - 採録を見送った案件（industry）: Microsoft の6万人への早期退職提案（数値が割れている）、SpaceX × Apollo の AI チップ融資ほか
