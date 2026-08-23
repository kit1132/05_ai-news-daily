# AI News Daily Summary — 2026-08-24

月曜は、期限と統制の輪郭が一次で固まった日である。OpenAI の退役ページが 8/26 の Assistants API 停止に続く半年ぶんの退役日を確定させ、o3 系 API は 12/11、Evals と Agent Builder は 11/30 と分かった。Copilot 側では Web 検索統制の一次2本が 8/18 に書き換わっていたことが本日はじめて判明し、ドメイン除外の撤回後に残る粒度は3段だけと確定した。あわせて Microsoft 365 Copilot が Microsoft Copilot へ改称されている。Cloudflare が 8/6 に出していた Chromium 非依存のエージェント専用ブラウザ Kitesurf も18日遅れで検出した。ChatGPT の広告は予告どおり本日から欧州31市場に入る。

## 今日のハイライト

### 1. OpenAI の退役カレンダーが一次で確定した — 2日後の Assistants API 停止に続く半年ぶんの日付が幅から確定日に変わった

**要点**: OpenAI の Assistants API が2日後の **8/26** に止まり、Threads を Conversations へ移す自動移行ツールは提供されない。同じ退役ページで o3 系 API は **12/11**、Evals と Agent Builder は **11/30** と確定し、幅で見ていた期限が日付に変わった。

**詳細**: `/v1/assistants` と `/v1/threads` は縮退運転も延長もなくエラーを返す。告知は 2025-08-26 で12カ月の予告期間があった。代替は Responses API と Conversations API の組み合わせで、Responses 側には deep research・MCP・computer use が乗るため機能面では上位互換だが、Assistant と Thread のオブジェクトモデルが無くなるため呼び出しの組み立てを書き直すことになる。

同じ一次ページに、提案の前提に効く退役日が半年ぶんまとまっていた。

- 8/26: Assistants API（告知 2025-08-26）
- 9/24: Videos API と Sora 2 系の全モデル（告知 2026-03-24）
- 10/23: 旧 GPT スナップショットとそのファインチューン版（`gpt-3.5-turbo-0125`・`gpt-4-turbo`・`gpt-4o-2024-05-13`・`o1`・`o3-mini`・`o4-mini` 等）
- 11/30: Evals プラットフォーム・Agent Builder・再利用プロンプト（`v1/prompts`）の3点。Evals ダッシュボードは 10/31 から読み取り専用になり、Agent Builder の移行先は Agents SDK か ChatGPT Workspace Agents。ChatKit は存続する
- 12/11: `gpt-5-2025-08-07` 系と `o3-2025-04-16` / `o3-pro-2025-06-10`。代替はいずれも GPT-5.6 Sol（pro は `reasoning.mode: pro` 付き）
- 2027/1/20: 旧 audio / realtime / transcription 系

予告期間の方針も明記された。一般提供モデルは**最低6カ月前**、プレビューモデルは**最短2週間前**の通知で退役しうる。プレビュー版を構成に組み込む場合、2週間で消える前提を見込むことになる。o3 の ChatGPT 側退役は 8/26 のままで、2日前の再確認でも延期・撤回の告知は出ていない。

- https://developers.openai.com/api/docs/deprecations
- https://developers.openai.com/api/docs/assistants/migration

### 2. Copilot の Web 検索統制が3段に確定した — ドメイン単位の絞り込みは戻らず、製品名も Microsoft Copilot へ改称された

**要点**: Web 検索統制を規定する Learn 2本が 8/18 に更新されていたことを本日はじめて確認した。ドメイン除外の撤回後に何が残るかは「再提供待ち」ではなく「テナント／モード／ユーザーの3段しかない」に確定した。

**詳細**: `manage-public-web-access` は `updated_at` **2026-08-18T22:40Z**、`which-copilot-for-your-organization` は **2026-08-18T17:48Z** である。読み取れる統制は以下にとどまる。

- 管理者: Cloud Policy service の `Allow web search in Copilot` のみが一次の統制点で、選択肢は3つ（両方で有効／両方で無効／Copilot Work モードだけ無効）。⚠️ 3つ目を選ぶと Researcher と Cowork の Web 検索も落ちる
- 未構成時: Web 検索は既定で使える。`Allow the use of additional optional connected experiences in Office` を Disabled にすれば止まるが、その設定は Copilot 以外の多数の体験も巻き込む
- 政府クラウド: GCC / GCC High / DoD は Web 検索が既定オフで、ポリシーを構成しない限りオフのまま
- ユーザー: Web content トグル（管理者が有効化していれば既定オン・端末とクライアントをまたいで保持）。⚠️ Researcher は入力ボックスにトグルを持つが、Analyst と Cowork にはユーザー向けトグルが無い
- 監査: 生成された検索クエリは引用として表示され（Copilot Chat 限定・スレッド内24時間）、監査ログ・eDiscovery・Purview DSPM for AI の activity explorer から実際の検索語を追える
- ⚠️ 生成検索クエリには **DPA も HIPAA も EU Data Boundary も適用されない**（プロンプトと応答には適用される）。Microsoft は当該クエリについてデータ管理者として振る舞う

あわせて両ページ冒頭に、Microsoft 365 Copilot が **Microsoft Copilot** へ、Microsoft 365 Copilot Chat が **Microsoft Copilot Chat** へ改称された旨の注記が入った。移行期間中はライセンス表記や機能名に旧称が残るとしており、セキュリティ・コンプライアンス・プライバシーの扱いは変わらない。8/15 に掲載した Partner Center の「アプリ名/アイコンの簡素化」はアプリ側の話で、本件は製品名そのものの改称にあたる。

⚠️ 両ページとも 02 の登録ソースに入っておらず、8/19〜08-23 の5セッションが更新を検知していない（B-044 起票）。

- https://learn.microsoft.com/en-us/microsoft-365/copilot/manage-public-web-access
- https://learn.microsoft.com/en-us/microsoft-365/copilot/which-copilot-for-your-organization

### 3. Cloudflare が Chromium を使わないエージェント専用ブラウザを出していた — エージェントに Web を見せる資源コストの前提が変わる

**要点**: Cloudflare が 8/6 に **Kitesurf** を公開していたことを本日はじめて検出した。V8 isolate 上で動き CPU・メモリは Chromium の3〜7分の1で、CDP 互換のため既存の Playwright / Puppeteer / MCP 統合は書き換えずに切り替えられる。

**詳細**: Kitesurf は Cloudflare Workers の V8 isolate 内で完結するブラウザランタイムで、Browser Run サービス経由で提供される。タブ・テーマ・ピクセル単位の忠実なレンダリングといった人間向けの機能を落とし、スクリーンショットや HTML 抽出などエージェントの定型作業に必要な分だけを残している。開発期間は12週間とされる。

- 互換性: **Chrome DevTools Protocol** を話すため、既存の Puppeteer / Playwright / CDP / MCP ベースの統合は `browser=kitesurf` の指定だけで切り替えられる
- 資源効率: スクリーンショットと HTML 抽出で CPU・メモリとも Chromium の**3〜7分の1**
- 速度: 同じ作業の所要時間は Chromium の約1.7倍で遅い。ラスタライズと画像エンコードを最適化中とされる
- 提供条件: beta・無料で、アカウント単位の上限がある
- 非対応: 動画再生、WebGL、実 TLS フィンガープリントを要するボット検査の通過、永続状態を要する認証済みセッション

⚠️ 本項は18日遅れの初検出で、Anthropic が 8/19 に computer use を GA・browser use を投入した直後の時期にあたる。原因は到達性ではなくソース未登録である（B-043 起票）。⚠️ `blog.cloudflare.com` / `developers.cloudflare.com` はいずれも本日の実測でゲートウェイ拒否のため、上記の数値・条件はすべて二次一致で採っており一次未確認である。

- https://blog.cloudflare.com/kitesurf/
- https://developers.cloudflare.com/changelog/post/2026-08-06-kitesurf/
- https://techcrunch.com/2026/08/07/cloudflare-launches-kitesurf-a-browser-built-for-ai-agents/

## カテゴリ別まとめ

### Anthropic / Claude

- Claude Code の changelog 最上位が **v2.1.241（8/23）** に更新されたが、内容は bug fixes and reliability improvements のみで、v2.1.240（8/22）と同じ形になる。中身の列挙がない版が2回続いている。08-23 に収録した v2.1.239 の課金是正以降、権限・料金に関わる変更は出ていない（https://code.claude.com/docs/en/changelog ）
- npm の `dist-tags` は `{stable: 2.1.231, latest: 2.1.241, next: 2.1.241}` で、`latest` と `next` が一致する状態が2日続いた。8/15 以降6例続いた「npm にだけ新版がある」形は解消したままである。一方 `stable` は 2.1.231 で据え置きのため、`latest` との差が9版から**10版**へ広がった
- Claude Platform API のリリースノートは **8/20 の Python SDK v1.0** が最上位のままで、4日間新規がない。`support.claude.com` の Release Notes も 8/6 の skill / plugin セキュリティスキャン beta が最上位で、**18日間**動きがない
- 8/23 付けの Anthropic 公式アナウンスは検出できなかった。`www.anthropic.com` のオリジン403が継続しているため、規定5本に日付入りの検索1本を加えた計6本を実行したが新規0件だった
- 既報の期限のみ再確認した。Claude Code の週次上限50%増は **8/31** まで、下院民主党22名の監督書簡への回答期限は**本日 8/24** である

### 開発ツール / エージェント基盤

- **Copilot CLI のローカルプラグインが編集即反映になった**。GitHub が 8/23 に pre-release **v1.0.81-8** を公開し、パス由来のプラグインを実ディレクトリからライブで読み込むよう変えた。編集は `/restart` か新セッションで反映され、`/plugin update` は不要になる（https://github.com/github/copilot-cli/releases/tag/v1.0.81-8 ）
  - `--add-dir` で追加したディレクトリからも skills と custom agents が探索されるようになった
  - Grok 4.6 で `xhigh` reasoning effort が使えるようになり、8/13 時点で effort 4段を持っていた Cursor に追いついた
  - サインアウト時にキャッシュ済みのエンタープライズ管理設定が破棄されるよう修正された。従来はサインインし直しても旧ポリシーが再適用されることがあった
  - 安定版は **v1.0.80（8/14）** のまま10日間据え置きで、上記はいずれも pre-release 側の変更である。⚠️ v1.0.81-2 / -3 / -4 の本文は5日連続で空のままになっている
- Codex CLI の安定版は **0.149.0（8/20）** で据え置き、4日間更新がない。8/22 に pre-release 2版が出たが、⚠️ 本文はいずれも `Release <タグ名>` の1行のみで変更内容を確定できなかった
- Cursor changelog は 8/19 の Cloud Agents / Cursor Harness 更新が最上位のままで、8/20〜8/23 の追加はない。フォーラム Announcements も 8/17 の Origin Code Hosting が最上位で、7日間動きがない
- MCP の `blog.modelcontextprotocol.io` は 8/22 の「The New MCP Roadmap」が最上位のままで新規はない。周辺の実測として Tier 1 SDK の月間ダウンロードが5億回近くに達し、TypeScript / Python の両 SDK が累計10億を超えたとされる。⚠️ ロードマップ本文ではなく二次経由の数値で一次未確認である
- xAI / Grok と Devin はいずれも新規発表を検出できなかった。一次ホスト（`x.ai` / `docs.x.ai` / `grok.com` / `docs.devin.ai`）は到達不可が継続している

### Microsoft 365 Copilot / Copilot Studio

- **Work IQ トグルの意味が一次と二次で逆になっている。** Learn は「オンで Graph 限定・オフで Web も加わる」と書き、**MC1458470**（Outlook・8/21 最終更新）を扱う二次記事は「オンで Web グラウンディング併用・オフでエンタープライズデータが無効」と伝えており、オフ側で失われるものが正反対である。掲載内容そのものは 8/22 に Teams 側（MC1458472）で拾った分と同一で、提供は **2026年9月**、サービス更新の一部として既定で有効になり管理者の構成操作を要しない
  - ⚠️ `mc.merill.net` が17日連続 `EGRESS_BLOCKED` で、MC 本文を扱う二次3本も同じ拒否のため一次で突き合わせる手段が無い
  - Work IQ REST API 側の一次は挙動が別で、エンタープライズ検索と Web 検索のグラウンディングを既定で両方使い、Web 検索のオフは**シングルターン動作**と明記している。UI のトグルと API のパラメーターを同じものとして説明しないこと
- ⚠️ **Copilot Tuning の一次は停止を一文も書いていない。** 停止の発効（8/20）から4日が経ったが、本日 `copilot-tuning-overview` を再取得したところ Optimization エージェントは「サポートされるシナリオ」節とテンプレート選択表の両方に現行機能として載ったままで、冒頭の Important ノートも「Frontier 経由の提供は 2026年4月予定」で止まっていた。本日この一次だけを読んだ管理者は、4日前に退役したテンプレートで着手してしまう。再開は Public Preview が 2026年9月・GA が 2026年12月で、自動移行はない
- M365 Copilot Release Notes は「August 11, 2026」が最新セクションのままで、新バッチは出ていない。対象期間 7/28〜8/11・節構成7本で 8/23 と一致する。次バッチは隔週傾向どおりなら **8/25 前後**の見込みである
- Copilot Studio の What's New は July 2026 が最新のままで、8月節は作成されていない。⚠️ June 節の GitHub Copilot ハーネスは `(Production-ready preview)` のままで、GA（8/3）から**21日連続**の未反映である。ページ本体は 8/20 に編集されているため、更新を待てば直るという前提は成立しない
- Copilot Studio の Released Versions は Build 2026.6.3（6/30 初出）のままで、空白が**8週間**に達した。次の定例更新日（火曜）は **8/25** である
- Copilot Studio の Release Wave 全13件は状態変化・期日変更・件数増減のいずれも発生していない。⚠️ 今月が GA 期日の **566997**（メーカー資格情報の使用ブロック）は `In development` のままで残り7日である
- Roadmap の `created ge 2026-08-21` 横断照会は3件を返したが、Copilot 関連は 569612（Copilot メモリの保持・Purview・GA 2026年9月）のみで 8/23 に掲載済みである。`modified ge 2026-08-22` は0件だった
- Purview の What's new は8月節が Sensitivity labels の2件のままで、Copilot 固有の項目はない。⚠️ `updated_at` は 8/14 から 8/21 へ動いているが本文に変化は見当たらず、569612 も What's new には現れていない

### Power Platform / ガバナンス

- Release Wave 3ページ（`power-automate` / `power-apps` / `power-platform-governance-administration`）は 8/23 と完全に同一で、緑チェックの追加・期日変更・行の増減はいずれも発生していない
  - 期日超過は延べ6行のままで、GA 列5件と Public preview 列1件の内訳も変わらない
  - 8月に期日がある行は10件、9月は6件で据え置きである。2026 Wave 1 の対象期間は9月末までで残り約1か月になる
  - ⚠️ PPAC の Usage ページは GA 期日が今月なのに緑チェックが付かないまま残り7日である
- Power Platform / Power Automate / Power Apps の3ブログとも新規記事はない。月次記事は 8/6 の July/August 合併号が最新で、親ページの一覧に合併号が現れない不完全レンダリングも続いている
- 非推奨一覧の先頭は **Power Automate モバイルアプリの廃止**（2026-08-31 発効・残り7日）のままで、次回の週次確認は 8/27 である
- Partner Center の8月アナウンスは 8/20 付の15件目までのままで、本日の追記はない
- ⚠️ Power Platform Weekly は本日の週次確認をスキップした（`www.ppweekly.com` が `EGRESS_BLOCKED`）。疎通そのものが塞がれており、#270（6/29）以降の夏季休刊が明けたかを確かめる手段が無い。次回は 8/31 になる

### OpenAI

- **ChatGPT の広告が本日 8/24 に欧州31市場で始まる。**（ハイライトの選定からは既報として外した。詳細は 08-20 に収録済み）提供国は35カ国になり、Free と Go の利用者には広告が出る前提へ変わる。本日の新規情報は出稿とプライバシーの2点になる（https://openai.com/index/chatgpt-ads-expands-across-europe/ ）
  - 出稿経路: 開始時点でセルフサービスは無く、OpenAI Ads Solutions か代理店・技術パートナー経由になる。Publicis・Omnicom・WPP・Havas・Dentsu・MediaPlus の名が挙がっている
  - GDPR 対応: パーソナライズ配信は明示的な同意ベースで、8/14 に EU 向けプライバシーポリシーを新規公開した。⚠️ オプトアウトで変わるのは「どの広告が出るか」であって「広告が出るかどうか」ではないと報じられている
  - ⚠️ 一次告知はオリジン403で本文を確認できず、複数の二次スニペットの一致で構成した。今回の31市場に日本は含まれない
- **GPT-5.6 Sol の値下げは 11/21 までの暫定措置である**（ハイライト参照＝08-23 に収録済み）。本日は一次の料金ページで現行単価を再確定した。入力 $4・キャッシュ入力 $0.40・出力 $20 で、⚠️ **入力 272K トークン超**の要求はリクエスト全体に入力2倍・出力1.5倍が掛かるため、長文脈前提では実効 $8／$30 と値下げ前を上回る領域が残る。同世代の Terra（$2／$0.20／$12）と Luna（$0.20／$0.02／$1.20）は据え置きである（https://developers.openai.com/api/docs/pricing ）
- `developers.openai.com/api/docs/changelog` は 8/21 の2件が最上位のままで、8/22・8/23 の追加はない。`community.openai.com` の Announcements RSS も 8/21 の Sol 値下げ告知が最上位である
- ⚠️ **Goal mode の GA と Appshots は本日の新着ではない。** 検索結果に8月分として現れたが、一次を当たると Codex app 26.519（2026-05-21）の項目で3ヶ月前の既報だった。二次の集約ページが月をまたいで再掲する形になっている

### Google / モデル・オープンウェイト

- Gemini API changelog は **8/13 の Gemini 3.7 Flash GA** が最上位のままで、11日間動きがない。料金ページの最終更新も 8/13 から変わらず、3.7 Flash / 3.6 Flash はいずれも入力 $0.75・出力 $3.75（**2026-12-31 まで**）で、2027/1/1 に $1.50／$7.50 へ戻る記載も同じである（https://ai.google.dev/gemini-api/docs/pricing ）
- 8/23 付けの Google の AI 発表は検出できなかった。直近は 8/12 の Made by Google と、8/26 ロールアウト開始予定の Ask Gemini in Chat でいずれも既報である。`gemini-robotics-er-1.6-preview` の 8/31 停止と Gemini 3.5 Pro の GA 未ローンチ（3回スリップ）も継続している
- 8/23〜8/24 に新規公開されたオープンウェイト LLM はない。8 org で作成日降順一覧を実行したが、8/13 の `Qwen/Qwen3.8-27B-FP8` と `deepseek-ai/DeepSeek-V4-Pro-0813` より新しいものが1件もなかった
- 実測（8/24）: `Qwen/Qwen3.8-27B` は DL **2,358,347**（前日 2,090,699）、`DeepSeek-V4-Pro-0813` は DL 57,928（前日 54,566）である。`DeepSeek-V4-Flash-0731` の DL 3,089,709 は V4-Pro の約53倍で、この開きが続いている
- ⚠️ 二次のモデル追跡サイトが 8/17 の `GLM-5.2 Turbo` を挙げているが、`zai-org` の HF org は 6/16 の GLM-5.2 が最新のままで該当する重みが存在しない。API 限定か誤記かを一次で確定できないため本日は記載しない

### 企業・市場

- **Cognition が $40B 評価で調達交渉に入ったと報じられた。** Bloomberg が 8/12 に報じ、複数媒体が追随した。Devin を開発する Cognition は5月に $26B 評価で $1B を調達したばかりで、3カ月経たずに次ラウンドを協議していることになる。ARR は前回調達時の約2倍で $1B に迫るとされ、$40B なら売上倍率は約40倍と $26B 時点の約52倍から下がる計算になる。⚠️ 交渉段階の報道で成立しておらず、ARR も当事者の公表値ではない。12日遅れの捕捉にあたる（https://techcrunch.com/2026/08/12/ai-coding-startup-cognition-reportedly-already-in-talks-to-raise-at-40b-valuation/ ）
- Anthropic の IPO 関連に新規の動きはない。既報の IPO 規模報道（8/21・今月末にも公開申請）と年換算売上 約$650億 の報道から進展していない
- 市場データ定点は IDC / IDC Japan・MM総研・Similarweb・NRC のいずれも新規公表を検知できなかった。参照可能な最新値は国内AI市場予測（2025年 2兆3,725億円 → 2029年 6兆8,897億円・CAGR 36.0%）、個人利用経験率 21.8%、生成AIサイト訪問シェア（ChatGPT 53.9%・Gemini 27.9%・Claude 9.2%）で据え置きである
- ⚠️ **Futurum Group の企業AI ROI 調査は不採用とした。** 提案の切り口に直結する数値を持つ830名規模の調査だが、プレスリリースの公表日は **2026-02-25** と判明した。本日の検索で新着として浮上したのは二次媒体の再掲載によるもので、半年前のデータにあたる

### Apple / その他

- `developer.apple.com` は 8/18 の EU 向けビジネス条件変更2本が最上位のままで、8/19〜8/23 の追加はない（Core Technology Fee 廃止 → Core Technology Commission へ・発効 **2026-10-01**）。⚠️ AI 関連ではない
- AI 関連の最新は 8/5 の App Store creative assets のままで、19日間新規がない。iOS 27 / iPadOS 27 は developer beta 4（7/20）が最新で、GA は9月（予想 9/14 前後）である
- AWS Bedrock 側の Anthropic モデル追加は 7/24 の Claude Opus 5 が最新のままで、8月の新規提供開始は検出できなかった
- `devblogs.microsoft.com/commandline` は 8/10 の Intelligent Terminal 0.2 が最上位のままで、08-23 に13日遅れで検出した分から動きはない。ホストは本日も 200 で読めるが登録ソースには入っていない

## 直近の注目予定

- **8/24（本日）**: ChatGPT Ads が欧州31市場で開始 ／ Anthropic / OpenAI が下院民主党の監督書簡へ回答する期限
- **8/25**: M365 Copilot Release Notes の次バッチ見込み ／ Copilot Studio Released Versions の定例更新日（8週間ぶりの新ビルドが出るか）
- **8/26**: **OpenAI Assistants API 停止** ／ o3 の ChatGPT 退役 ／ GPT-4.5 完全廃止 ／ Copilot 既定モデル有効化ポリシー発効 ／ Ask Gemini in Chat のロールアウト開始
- **8/27**: IT Nation Connect ANZ の Microsoft セッション ／ 非推奨一覧の週次確認
- **8/30**: 公式 DALL·E GPT の退役
- **8/31**: Claude Code の週次上限50%増が終了 ／ GitHub Spark の既存ユーザーアクセス終了 ／ `gemini-robotics-er-1.6-preview` 停止 ／ Power Automate モバイルアプリの廃止 ／ CSP Copilot Partner Council コンテストの応募期限 ／ Claude for Government の $1/機関プログラム終了
- **8月末**: Copilot Studio 566997 と PPAC Usage ページの GA 期日 ／ Anthropic が IPO を公開申請する可能性
- **9/1**: GitHub Copilot の全体験でモデル廃止 ／ MAICPP 契約の更新条項が自動発効 ／ OpenAI Daybreak でハードウェアセキュリティキー必須化
- **9月**: Outlook と Teams の Copilot チャット中心 UI と Work IQ コントロールが既定で有効化 ／ Copilot メモリの Purview 保持（569612）／ Copilot Tuning の新体験が Public Preview ／ iOS 27 / macOS 27 GA
- **9/10**: MAI-Code-1-Flash が全 Copilot 体験から廃止
- **9/17**: OpenAI DevDay Exchange の応募締切
- **9/24**: OpenAI Videos API と Sora 2 系の全モデルが退役
- **9月末**: 2026 Wave 1 の対象期間終了 ／ M365 E5・E3 の CSP 割引終了
- **10/1**: Apple の EU 向け新ビジネス条件が発効 ／ CSP ソフトウェアの5%資本コスト上乗せ発効
- **10/16–11/11**: OpenAI DevDay Exchange 8都市（**東京は 10/20**）／ **10/20〜22**: SMB Copilot Partner Council イベント（NYC）／ **10/25〜30**: PPCC 2026
- **10/23**: 旧 GPT スナップショットとそのファインチューン版が退役
- **10/31**: OpenAI Evals ダッシュボードが読み取り専用へ
- **11/21**: GPT-5.6 Sol の暫定値下げが有効とされる期限
- **11/30**: OpenAI Evals プラットフォーム・Agent Builder・`v1/prompts` が退役
- **12/2**: EU AI Act の生成コンテンツ標識義務の猶予終了
- **12/11**: `gpt-5-2025-08-07` 系と `o3-2025-04-16` / `o3-pro-2025-06-10` が退役
- **12/31**: Gemini 3.7 Flash の導入価格終了（$0.75/$3.75 → $1.50/$7.50）
- **2027/1/20**: OpenAI の旧 audio / realtime / transcription 系が退役

## 改善メモ

- **Master B-043 起票**: Cloudflare（`blog.cloudflare.com` / `developers.cloudflare.com`）をエージェント実行基盤の一次としてソース追加する提案である。Kitesurf の18日遅れ検出が根拠にあたり、B-042（Windows Command Line）・B-037（Meta）と同型の欠落になる
- **Copilot B-044 起票**: Web グラウンディング統制の一次2本（`manage-public-web-access` / `which-copilot-for-your-organization`）が `daily-sources.md` 未登録で、8/18 の更新を5セッション連続で検知できなかった。全 digest を grep して掲載歴ゼロが確認されている
- **industry B-028 起票**: `developers.openai.com` を OpenAI の一次ソースとして登録する提案である。本日の退役カレンダー確定が同ドメイン経由で、⚠️ 退役カレンダー自体を03は一度も収録していなかった
- **ソース間の切り口差**: GPT-5.6 Sol の値下げは Master が「一次に旧単価の記載がない」点を、industry が「272K 超の長文割増で実効 $8／$30 になる」点を書いており、矛盾ではなく粒度の差とみて統合した
- **一次未確認のまま採用した項目が2件ある**: Cloudflare Kitesurf（`blog.cloudflare.com` / `developers.cloudflare.com` がゲートウェイ拒否）と ChatGPT Ads の欧州展開（`openai.com` がオリジン403）で、いずれも二次一致で採った
- **到達性の変化**: 新規ゲートウェイ拒否が11ドメイン（`blog.cloudflare.com` / `developers.cloudflare.com` / `docs.cloud.google.com` / `releasebot.io` / `winbuzzer.com` / `www.storyboard18.com` / `www.neowin.net` / `www.cloudzero.com` / `www.techtimes.com` / `aiagentstore.ai` / `futurumgroup.com`）で、うち `docs.cloud.google.com` は industry B-024 が登録を提案している Google Cloud 退役ドキュメントのホストにあたる。⚠️ `www.microsoft.com` の M365 Blog RSS は **オリジン403**（ゲートウェイ拒否ではない）を返したため、HTML 一覧ページと WebSearch の2経路で照合した
- **週次復旧チェック（月曜）**: 対象8ホストは1件も復旧せず**3週連続**である（`www.testingcatalog.com` / `simonwillison.net` / `obsidian.md` / `blog.google` / `workspaceupdates.googleblog.com` / `x.ai` / `docs.devin.ai` / `learn.chatgpt.com`）
- 継続提案は Master 23件（最多: B-013 403の2分類記録・27回目）、Copilot 27件（最多: B-005 Qiita の WebSearch 前提化・34回目）、industry 5件（最多: B-004 取得方法欄の WebSearch 優先化・56回目）
