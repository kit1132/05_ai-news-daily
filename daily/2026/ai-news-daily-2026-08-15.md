# AI News Daily Summary — 2026-08-15

土曜は、待っていた期限が前倒しで消え、書き留めた単価が誤りだったと判明した日である。8/16 の公開期限を待っていた Qwen3.8-27B の重みは2日早い 8/14 に Apache 2.0 で出ており、本サマリーが2日連続で「未公開が継続」と書いた記録は誤りだった。Gemini 3.6 Flash も同じ形で、08-14 に「据え置き」と記録した単価は実際には半額の導入価格に下がっていた。Microsoft 側は業務用 Copilot の Web URL が 8/18 から `copilot.cloud.microsoft` へ移り、許可リストの確認期限が3日後に迫っている。手元のツールでは Claude Code v2.1.232 が `/fork` の意味を入れ替え、Copilot CLI がセッションを CLI プロセスからホスト常駐へ移した。

## 今日のハイライト

### 1. 業務用 Copilot の Web URL が 8/18 から copilot.cloud.microsoft へ移る — 許可リストの確認期限は3日後

**要点**: Microsoft が業務用 Copilot の Web URL を `m365.cloud.microsoft` から `copilot.cloud.microsoft` へ移し、自動リダイレクトを 8/18 に開始する。前提が「新旧どちらの URL でも届く」から「新 URL をブロックしている組織はリダイレクトが効かない」へ変わる。

**詳細**: Partner Center の8月アナウンスに 8/14 付で追記された。2026-08-18 から Web・デスクトップ・モバイルの Microsoft Copilot アプリが更新され、職場アカウントと個人アカウントを見分けやすくする変更が入る。セキュリティ・コンプライアンス・ガバナンスの制御は変更されない。

- アカウント表示: アカウントラベル、Microsoft Entra 職場アカウントを示す緑の盾、背景の描き分けが追加される
- 名称とアイコン: 「Microsoft Copilot」に簡素化される
- Web の URL: `copilot.cloud.microsoft` へ移り自動でリダイレクトされる。ただし組織側で新 URL がブロックされている場合はリダイレクトされない
- 求められている確認は3点: `copilot.cloud.microsoft` がネットワーク・プロキシ・ファイアウォール・アクセスポリシーでブロックされていないこと、`*.cloud.microsoft` を許可リストへ追加すること、移行に向けた接続性の検証

Windows / Mac デスクトップアプリは 8/18 に早期プレビューが始まり、広範な展開は9月中旬からになる。⚠️ 8/22 に予定されている M365 Copilot アプリのチャット中心 UI の Deferred リング展開（**MC1325422**）とは別の変更で、あちらは画面構成、こちらはアプリの統合と URL の移設である。8月後半に2つが重なる。

- https://learn.microsoft.com/en-us/partner-center/announcements/2026-august
- https://learn.microsoft.com/en-us/copilot/manage

### 2. Gemini 3.6 Flash も導入価格に下がっていた — 08-14 の「据え置き」記録を訂正する

**要点**: Google は 3.7 Flash の GA と同時に 3.6 Flash も同一の導入価格へ下げていた。本サマリーが 08-14 に「3.6 Flash は $1.50 / $7.50 のまま据え置き」と書いた前提は誤りで、Flash 系の試算は引き直しになる。

**詳細**: 一次料金ページ（`ai.google.dev/gemini-api/docs/pricing`）は本日、Gemini 3.6 Flash と 3.7 Flash の両方に同一の導入価格を掲載している。単価は入力 **$0.75** / 出力 **$3.75**（100万トークン）で、有効期限は **2026-12-31**。2027年1月1日以降は入力 $1.50 / 出力 $7.50 の標準価格へ戻る。二次報道も「3.7 Flash の公開と同じタイミングで 3.6 Flash を静かに同一の導入価格へ下げた」と明示しており、一次・二次の双方が一致した。

- 3.6 Flash の実効単価は記録していた値の半額にあたる（出力は $7.50 → $3.75）
- 据え置きが続くのは 3.5 Flash（$1.50 / $9.00）のみで、Flash 系の中で最も高い出力単価になった
- 3.6 と 3.7 が同単価のため、両者の選択は価格差ではなく性能差だけで決まる
- 導入価格は期限付きのため、2027年以降を含む試算は倍額（$1.50 / $7.50）で置く

3.1 Flash-Lite（$0.25 / $1.50）が 3.5 Flash-Lite（$0.30 / $2.50）より安い逆転関係と、3.1 Pro Preview のプロンプト長連動（入力 $2.00〜$4.00 / 出力 $12.00〜$18.00）はいずれも変化していない。⚠️ 08-14 の判断は「一次ページの要約では 3.6 Flash にも導入価格が付いて見えるが、二次確認で据え置きと確定した」として二次側を採ったものだった。一次と二次が食い違い二次が誤っていた初の事例にあたる。

- https://ai.google.dev/gemini-api/docs/pricing
- https://venturebeat.com/technology/googles-gemini-3-7-flash-targets-coding-and-agents-with-a-50-introductory-price-cut

### 3. Qwen3.8-27B の重みが Apache 2.0 で公開された — 期限より2日早く、ローカル 27B がエージェント用途に届いた

**要点**: Alibaba が Qwen3.8-27B の重みを Apache 2.0 で公開した。単体 GPU 級の 27B が OSWorld-Verified 84.3 / Terminal-Bench 2.1 73.0 に達し、「エージェント用途はクラウド API 前提」という置き方が崩れた。公開は待っていた 8/16 ではなく 8/14 だった。

**詳細**: Hugging Face API の実測で `Qwen/Qwen3.8-27B` は `private: false` / `gated: false`、safetensors 18シャード、総パラメータ 27,781,427,952（BF16）、`lastModified` は 2026-08-14T15:00 UTC である。FP8 版 `Qwen/Qwen3.8-27B-FP8`（8/13 作成・66シャード）も同時に読める。ライセンスはどちらも apache-2.0。

- アーキテクチャ: vision encoder を持つ dense モデルで、Gated DeltaNet と Gated Attention のハイブリッド 64層。テキスト・画像・動画を入力に取る
- コンテキスト: 262,144 トークンがネイティブで、スケーリングにより 1,000,000 まで拡張できる
- テキスト系ベンチ: Terminal-Bench 2.1 73.0 / SWE-bench Pro 61.7 / QwenSWEBench 79.0 / LiveCodeBench 90.3 / GPQA Diamond 89.2
- VL 系ベンチ: OSWorld-Verified（コンピュータ操作）84.3 / AndroidWorld 81.9
- 第三者の量子化が 8/14 中に大量に出た（`-GGUF` / `-AWQ` / `-MLX-6bit` / `-SmoothQuant-W8A8-INT8` 等）ため、当日から手元で動かせる形が揃っている

⚠️ 本サマリーは 08-13・08-14 と2日連続で「Qwen3.8-27B は未公開が継続」と記録したが、実際には 8/14 に公開されていた。検出できたのは、製品名からリポジトリ ID を推測せず `?author=Qwen&sort=createdAt` で作成日降順を全件見る手順（ソース側 B-032）による。

- https://huggingface.co/Qwen/Qwen3.8-27B
- https://huggingface.co/Qwen/Qwen3.8-27B-FP8

## カテゴリ別まとめ

### Anthropic / Claude

- Anthropic が Claude Code **v2.1.232** を公開し、`/fork` の意味を入れ替えた（8/13 23:29 UTC）。全49件の変更のうち破壊的変更1件・セキュリティ修正12件・新機能6件という内訳で、既存の手順書は書き換えが要る
  - `/fork`: 作業を続けたまま会話を新しい背景セッションへ複製する。複製先は `claude agents` に独立した行として並ぶ
  - `/subtask`: 従来 `/fork` が起動していたセッション内サブエージェントは、こちらへ改名された
  - subagent forking が既定オンになり、`subagent_type: "fork"` のサブエージェントは会話全体とプロンプトキャッシュを継承する。対話セッションでの非 teammate エージェント起動も既定で背景実行になった
  - セッション横断: プロンプトに `@` を打つと他の Claude セッションを名前で指名でき、Claude が `SendMessage` で直接届ける。同一マシンで名前が衝突すると `name-word-word` 形式の変種が自動で割り当てられる。`/config` に「Dialog expiry」と「Messages from your other sessions」の2行が加わった
  - 権限バイパスの修正が3件入った。PowerShell の変数書き込みパラメータが `$PSDefaultParameterValues` を黙って上書きして後続コマンドのファイルアクセス先を差し替えられた件、Windows の Git Bash が Cygwin 形式のシンボリックリンクを追ってパス検証を通していた件、ネストした git リポジトリが親ディレクトリの trust を継承していた件で、後2者はリンク経由の書き込みとリポジトリごとの trust 確認が必要になった
  - GitLab 対応: トークン9系統（`glrt-` / `gloas-` / `glptt-` 等）の redaction が入り、ルーティング可能な `glpat-` / `gldt-` は全体を伏せる。`glab` CLI の設定ストアが `gh` と同じサンドボックス保護の対象になり、マーケットプレースが `gitlab.com` の裸リポジトリ URL を clone できる
  - 設定名の別名: `additionalMarketplaces` / `allowedMarketplaces` が `extraKnownMarketplaces` / `strictKnownMarketplaces` として受理される
  - ゲートウェイの boot 検証が厳しくなり、`desktop:` オーバーレイの未知・不正キー、`managed.policies[].match.groups` や `admin.admin_groups` の空要素、不正な `email_domain` は boot に失敗する
  - Fable アクセスを持つ組織で Fable 5 が `/advisor` のアドバイザーとして再提供される（利用クレジットの同意は `/model fable` で行う）
  - ⚠️ npm の `next` タグには **v2.1.233**（8/14 18:50 UTC）が出ているが、GitHub releases にも changelog にも未掲載である。`stable` タグは v2.1.223 のままで `latest` の v2.1.232 とは9版ぶんの差がある
- Anthropic が Claude Code のセッション費用の倍率を公開した（8/14）。製品変更ではなく運用ガイドだが、課金に直結する数値が明記され、トークン費用の議論が体感論から計算可能な設計問題に変わる
  - 単価倍率: キャッシュ読み取りは入力の **0.1倍**、キャッシュ書き込みは最大2倍、出力トークンは入力の約5倍
  - プロンプトキャッシュの有効期間はサブスクリプションが **1時間**、API キー利用が5分。30,000字を超える出力は自動でファイルへ退避される
  - 推奨される操作は、タスクの切れ目で `/clear` を打つ、モデルと effort をセッション開始時に固定する（途中変更はキャッシュを失効させ会話全体を定価で再充填する）、ファイルはパスではなく `@` で添付して Read 呼び出しを省く、出力の多いコマンドは quiet フラグかサブエージェントで走らせる、離席前に `/compact` を通す、の5点である。新規セッションで `/context` を1回打つと常時読み込まれている内容を点検できる
- Anthropic が JetBrains による Claude Fable 5 の評価・導入事例を公開した（8/13）。自社製品でのホワイトボックス脆弱性テストに frontier モデルを使う点まで踏み込んでいる
  - 社内評価の Python pass rate は Fable 5 が **44.3%**、Opus 4.8 が **28.2%** で16ポイント差である
  - 直接比較では Fable 5 が Opus の落とした Python タスク18件を解き、逆に落としたのは2件だった。解に到達するまでのステップ数は Opus 4.8 比で約22%少ない
  - 評価は自社 monorepo を含むプライベートリポジトリの大規模評価セットで行い、品質・タスク単価・速度のリーダーボードを維持している。公開ベンチマークではなく実作業で動くかを見る方針である
- Claude API release notes は 8/11 が最上位のままで 8/12〜8/14 の追加がない。`support.claude.com` の Release Notes も 8/6 の skill / plugin セキュリティスキャン beta から9日連続で動きがない
- `www.anthropic.com` はオリジン403が継続している。日付入りの WebSearch で返ったのは auto mode 既定化の再掲のみで、新規の製品発表はなかった
- 既報: auto mode の既定化（8/14 から Pro / Max / Team の新規セッション）、Chrome 拡張サイドパネルの Cowork 化（8/12）、Claude Tag のチャンネル文脈対応（8/13）、Decart AI 買収交渉と10月 IPO の報道（8/13）
- 期限: Claude Code の週次上限50%増は **8/19 23:59 PT** で終わる

### Google / DeepMind

- Gemini 3.6 Flash も導入価格に下がっていた（ハイライト2参照）
- Gemini API changelog は 8/13 の Gemini 3.7 Flash GA が最上位のままで、8/14 の追加はない
- 3.7 Flash のコーディング系ベンチ数値が二次で判明した。3.6 Flash 比で FrontierCode 1.1 Main が **34.4% → 43.6%**、DeepSWE v1.1 が **49% → 65.3%** である。⚠️ 一次 changelog にこの数値はなく、二次報道由来にとどまる
- Gemini 3.5 Pro の GA は未ローンチが継続している（I/O 発表後に 6月 → 7月 → 7/17 と3回スリップした）
- ⚠️ 登録済みの Google 系5ソース（`blog.google` / `workspaceupdates.googleblog.com` / `support.google.com` / `deepmind.google` / `docs.cloud.google.com`）はゲートウェイ拒否が続いており、到達できる Google 一次は未登録の `ai.google.dev` だけである
- 既報: `gemini-robotics-er-1.6-preview` の 8/31 停止、Imagen 4.0 系3本の 8/17 停止

### Microsoft / GitHub

- GitHub が Copilot CLI に Agent Host Protocol（AHP）を入れ、セッションを CLI プロセスからホスト常駐へ移した。複数の端末が同じセッションにアタッチしてターンをライブで追えるようになり、CLI を閉じると作業が終わる前提が消えた。pre-release v1.0.80-0（8/13 19:37 UTC）で導入され、安定版 v1.0.80 は 8/14 02:28 UTC にモデル構成の更新1点で出ている
  - セッション操作: `/ahp sessions|attach|new` がホスト側のセッション一覧を扱い、`/ahp start [port]` / `/ahp stop` / `/ahp restart` で daemon を CLI 内から管理する。`/ahp connect <url>` でホストを動的に足せる
  - 入力の扱いはローカルと同じで、Enter が実行中のターンにプロンプトを差し込み、Ctrl+Q が次ターンへキューし、Ctrl+C で取り出す
  - Sessions タブがホストごとの健全性を表示し、`h` で複数の AHP daemon ソースを切り替える。複数 CLI がぶら下がっているセッションは「2 clients」のように表示される
  - リモート連携: Codespaces は `/ahp codespace <name>` でトンネル転送し、Mission Control 環境は Sessions タブに `CLOUD` として出る。ローカル daemon の探索は `COPILOT_AHP_DISCOVER` で制御する
  - 接続トークンがログから redaction されるようになり、ホスト側の skills がリレー再接続をまたいで保持される
  - ⚠️ Claude Code のセッション横断メンションと24時間以内に出ており、両者とも「1セッション＝1端末」を外す方向に動いている
- GitHub が Grok 4.6 を Copilot に追加した（8/14）。対象は Pro / Pro+ / Max / Business / Enterprise で、VS Code・Visual Studio・Copilot CLI・クラウドエージェント・Copilot アプリ・JetBrains・Xcode・Eclipse の8面のモデルピッカーから選べる。課金はプロバイダー定価での従量課金である。⚠️ Business / Enterprise は既定オフで、管理者が Copilot 設定で有効化するまで選択肢に出ない。展開は段階的で可用性にも差が出る
- 8/13 付で公開された 8/10 週の weekly releases に、モデルと CLI の変更がまとまって載っている（本サマリーは2日遅れの捕捉）
  - 全プラン共通: Kimi K3 が全プラン層へ展開され、MAI-Code-1.1-Flash がネイティブ画像理解とコーディング品質改善つきで提供される。Agent Plugins 1.0 が GA（既報）
  - Copilot CLI: `/tasks` でサブエージェントを管理でき、エージェント実行中もプロンプトとコマンドをキューできる。`--plan` と `--mode autopilot` の併用でヘッドレスに計画生成から実行まで通り、`/rewind` が git 操作なしで変更を戻し、`/app` がセッションとフォルダ文脈を保ったままデスクトップアプリを起動する
  - Copilot アプリ: プラグインのバージョン確認と個別／一括更新が設定からできるようになり、エージェントからの質問に本題を止めず答えるサイドチャットが加わった
  - VS Code 1.133: セッション途中で Claude BYOK と Copilot 内蔵モデルを切り替えられ、長い会話でプロンプトをピン留めできる。内蔵ブラウザが HTML の変更を手動更新なしで反映する
  - JetBrains: Copilot memory と Ollama の BYOK 対応が入った（既報）
- M365 Copilot Release Notes は August 11, 2026 バッチのままで本日の新バッチはない。節構成7本が 8/14 と一致することを本文取得で確認済みで、次バッチは隔週傾向どおりなら 8/25 前後の見込みである
- Microsoft 365 Roadmap・Microsoft 365 Blog（本体）・M365 Developer Blog・Tech Community の M365 Copilot Blog は、いずれも本日の新規がない
- ⚠️ Message Center の一次取得は8日連続でできていない（ゲートウェイ拒否）。WebSearch 照合で MC1454386「Simplified access to Copilot Chat on the Microsoft 365 Copilot mobile app」が索引に出たが、本サマリーに一度も掲載がない。モバイルアプリからの Copilot Chat 到達の簡素化を扱うとみられ、ハイライト1のアプリ統合と同じ方向を向いているが、取得できているのは二次サイトのスニペットのみのため掲載内容と展開時期は採用していない
- 期限: Copilot 既定モデル有効化ポリシー発効（**8/26**）、GitHub Spark 退役（**8/31**）、モデル廃止と Claude Sonnet 4.6 の非推奨（**9/1**）、MAI-Code-1-Flash 廃止（**9/10**）

### Copilot Studio / Power Platform

- Power CAT が Copilot Agent Kit August 2026 を公開し、Agent Review Tool が GitHub Copilot ハーネス製エージェントに対応した（8/14・タグ `CopilotStudioAccelerator-August2026`）。8/3 の GA 以降「ハーネスで作ったエージェントは既存のガバナンスツールの外にある」状態が続いていたが、レビューと変更追跡の対象に入った
  - Agent Change Tracker: エージェントの変更を継続的に追跡し、バージョン付きのタイムラインと変更したメーカーの情報を残す。誰がいつ何を変えたかを後から辿れる
  - Agent Library: MCP Apps ギャラリーが追加され、Skills と Automations をアップロードできる
  - Agent Inventory Settings: 検出と監視の設定を構成でき、メタデータ抽出が多言語に対応した
  - Bulk Actions はモデル駆動アプリからのエージェント一括検疫に、Agent Debugger は新しいエージェント種別に対応し、Agent Value Summary は日次スキャンを最適化して AI クレジットの消費を抑えた
  - ⚠️ Copilot Studio の What's New は同じハーネスをいまも `(Production-ready preview)` と書いており、GA から12日連続の未反映である。一次ドキュメントより先に周辺ツール側が GA に追いついた形になる
- Copilot Studio の Released Versions は **2026.6.3**（6/30 初出）のままで、6週間半にわたって新ビルドが出ていない。ページ本文の「This page is updated each week on Tuesday.」という記述と実態が食い違ったままで、次の定例は 8/18 である
- Power Platform の Release Wave（`power-automate` / `power-apps` の `planned-features`）は 8/14 と完全に同一で、緑チェックの追加・期日変更・行の増減はいずれも発生していない。期日超過は延べ6行、8月期日は10件、9月期日は6件のままである
- ⚠️ Power Platform Blog の親ページの一覧先頭に、8/13 の PPCC 2026 登録記事が現れた。B-010 の不完全レンダリングは 4/27 で停止した状態が7月から続いていたため、親ページに8月の記事が出たのは今回がはじめてである。ただし 8/6 公開の月次合併号は依然として一覧に現れず、不完全レンダリング自体は解消していない
- Power Automate Blog / Power Apps Blog は 8/13 の PPCC 2026 登録記事が先頭のままである。⚠️ 標準価格での登録期限は **8/18** である
- Power Platform の非推奨一覧の先頭は Power Automate モバイルアプリの廃止（**8/31** 発効・残り16日）のままで、次回確認は 8/20 である

### ガバナンス・ライセンス

- Microsoft が Low Code App Development と Intelligent Automation のスペシャライゼーションを **Agentic Business Solutions** へ統合した（2026-07-31 付・8/13 の月次 MAICPP アップデートで判明）。性能要件に Copilot Studio の実績だけで到達する経路が加わり、前提が「Power Apps と Power Automate の本番導入実績が必須」から変わる。既存の登録パートナーは同じ更新日で新スペシャライゼーションへ自動的に移されている
  - 経路1: 新規導入の顧客2社。うち1社は Power Automate のフローが本番稼働、もう1社は Power Apps アプリを最低5ユーザーで本番稼働（関連付けは PAL）
  - 経路2: Copilot Studio の新規導入2社・各 **$10,000 TTM** 以上（非経常。関連付けは CPOR / CSP T1 / CSP T2 / CSPCPOR）
  - スキル要件: Power Platform Functional Consultant Associate・Intelligent App Builder・AI Agent Builder Associate のいずれかを5名以上、Power Platform Developer Associate または Power Automate RPA Developer Associate を2名以上、Agentic AI Business Solutions Architect を2名以上
  - サービス要件: Power Apps / Power Automate / Copilot Studio / Power Virtual Agents のコンサルティングサービスを Microsoft Marketplace に1件以上公開し、対象製品をタグ付けする
  - ⚠️ Frontier Partner バッジは **2027年6月末**で廃止される。FY27 中は要件を満たす限り使えるが、以降は取得時期にかかわらず使用できない。後継の Frontier Partner スペシャライゼーションは FY27 中に Partner Center へ登場する予定である
- Partner Center の8月アナウンスは掲載が10件から **14件**に増えた。新規4件のうち3件は Copilot アプリの更新（8/14）と MAICPP 月次（8/13）で、残る2件は IT Nation Connect ANZ 2026 での Microsoft セッション告知（8/14・8/27 開催・エージェントの野放図な増加や権限誤用への統制を扱う）と、Windows Server 2016 ESU の CSP 価格表の月中再公開（8/13・Copilot 系は対象外）である。⚠️ 8/14 に「本日は追記なし」と記録した翌日に4件が一度に増えており、月内は日次巡回が要る
- Microsoft Purview の `whats-new` に8月節が新設された（`updated_at` 2026-08-14T07:32Z）。掲載は Sensitivity labels の2件で、自動ラベル付けポリシーを適用前にシミュレーションモードで走らせて対象範囲を確認できるようになったことと、ポリシー詳細パネルの Insights タブでポリシーの挙動を一覧できるようになったことである。⚠️ Copilot 固有の項目は含まれていない
- Copilot Studio の課金レート表は 8/14 の一次確認から変わっておらず（`updated_at` 2026-08-03T14:59Z）、次回確認は 8/18 である。⚠️ USD 単価は依然として取得できない PDF にしかない。Qiita / Zenn には「$0.01 / クレジット」「キャパシティパック $200 / 月」「事前購入プラン P3」と具体的に書く記事があるが、いずれも一次（Learn）に存在しない数値のため採用していない

### OpenAI

- OpenAI の Ultrafast モードが一次で確定した。`developers.openai.com/api/docs/changelog` に 8/13 付エントリとして掲載され、最上位になっている。GPT-5.6 Sol を Standard の最大14倍速で動かす API サービス階層で、限定プレビューとして一部顧客に提供される。⚠️ 課金レートは changelog にも記載がなく未確定のままである（一次 `openai.com/index/previewing-ultrafast/` はオリジン403、Cerebras 側2ホストはゲートウェイ拒否）
- Codex CLI の pre-release は **0.148.0-alpha.16**（8/14 17:18 UTC）が最新で、前回記録の alpha.12（8/13 06:43 UTC）から4版進んだ。安定版は 0.147.0（8/7 01:41 UTC）に据え置かれ、0.148.0 の安定版は未リリースである。⚠️ alpha 各版の個別リリースノートはページ側のエラーで表示されず、内容は2日連続で未確認である
- Codex が可搬な Agent Plugins のインストールに対応し、ローカル / 個人 / ワークスペース / リモートのカタログを横断検索できるようになった。あわせて opt-in で MCP 2026-07-28（ページング付き discovery・多段リクエスト・非ブロッキングなサーバー起動）に対応した。⚠️ 掲載日は未確定である
- ChatGPT Enterprise / Edu の個人ユーザー単位の同期接続は 8/14 に無効化され、同期済みデータの削除が始まった（既報）。管理者管理の同期は影響を受けない
- `community.openai.com` の Announcements RSS は 8/10 の Daybreak 拡大告知が最新のままで追加がない
- 到達性: `community.openai.com` と `developers.openai.com/api/docs/changelog` は 200。`openai.com` / `help.openai.com` / `platform.openai.com` はオリジン403が継続し、`learn.chatgpt.com` はゲートウェイ拒否が継続している

### モデル・料金の動き

- DeepSeek の値上げ実施まで1日となった。**8/16 16:00 UTC**（日本時間 8/17 1:00）に切り替わり、V4-Flash 出力は $0.28 の定額からピーク $1.32 / オフピーク $0.66 へ、V4-Pro 出力は $0.87 からピーク $3.96 / オフピーク $1.98 へ移る。ピーク帯は UTC 01:00〜04:00 と 06:00〜10:00（日本時間 10:00〜13:00 と 15:00〜19:00）で、⚠️ 日本のオフィス時間はピーク帯とほぼ重なる。一次料金表は本日もゲートウェイ拒否で到達できていない
- 米メディアが 8/14 の総括で、OpenAI と Anthropic の値下げを「推論費用を抑えたい企業が DeepSeek や Moonshot AI へ流れる圧力への対応」と位置づけた。既収録の実例は OpenAI が 7/30 付で GPT-5.6 Luna を80%下げて $0.20 / $1.20・Terra を20%下げて $2 / $12 としたことと、Anthropic が 7/24 公開の Claude Opus 5 を $5 / $25（Fable 5 の半額）に置いたことである。本日の Gemini 3.6 / 3.7 Flash の導入価格も同じ流れに並ぶ
- 中国2社が資本市場へ向かっている。Moonshot AI は **$50B** の評価額でプレIPO ラウンドの打診を始めたと報じられ、DeepSeek は上海市場への上場を早ければ 2027年 Q2 に見込む。Moonshot の Kimi K3（2.8兆パラメータ）は自社インフラでの実行を選べる形で提供されている。⚠️ いずれも一次発表ではなく報道段階で、評価額と時期は確定していない

### Cursor / xAI / その他開発ツール

- Framer がキャンバス上のエージェントを外部 CLI へ接続できるようにした（8/14）。キャンバス上でエージェントにサイトの設計・執筆・分析・整理をさせる機能に加え、Claude Code や Codex を自前で接続できる経路が用意された。ほかに公開前に案を試すためのブランチ機能とコミュニティ機能が入っている。デザインツール側がコーディングエージェントの受け口を持つ形で、Agent Plugins による配布標準化と方向が揃う
- Devin が Side Chats を追加した（8/12・二次）。セッションの任意の時点に紐づけた別会話を開始し、Devin の本作業を止めずに質問や詳細確認ができる。⚠️ `docs.devin.ai` はゲートウェイ拒否が継続しており一次未確認で、3日遅れの検出にあたる
- Cursor の changelog は 8/13 の Cloud Agents Builds が最上位のままで追加がない。フォーラムも 8/12 の Grok 4.6 関連2件が最新である
- ⚠️ xAI は一次に到達できない状態が継続している（`x.ai` / `docs.x.ai` がゲートウェイ拒否）。二次では Grok 4.7（2.1T パラメータ）が数週間内、Grok 5 が2026年内という観測と、`grok-voice-think-fast-2.0` が 8/5 から `grok-voice-latest` のルーティング先になったという記述が出ているが、いずれも一次未確認である

### MCP / オープンウェイト

- MCP 公式ブログは新着がなく、RSS 最新は 7/28 の `The 2026-07-28 Specification` のまま18日連続で動きがない。Tier 1 SDK にも変化はない（TypeScript `@modelcontextprotocol/server` / `client` ともに 2.0.0、Python `mcp` 2.0.0、C# v2.0、Go は v2 未発行で `go-sdk` v1.7.0 が仕様対応）
- 一方で実装側は動いている。Codex が opt-in で 2026-07-28 に対応し、Claude 側も stateless core・OAuth / OIDC 強化・Apps / Tasks の versioned extensions まで対応を広げたと二次で報じられている
- Kimi K3 が GitHub Copilot の全プラン層へ展開された。モデル自体は 7/16 の API 公開・7/27 の重み公開で既報だが、Copilot からの利用は今回が初になる。HF の `moonshotai/Kimi-K3` は likes 10,655 / DL 1,974,635 である
- Qwen3.8-27B は本日のハイライト3を参照。Qwen3.8-Max（8/8 公開）と Meta の `meta-models/Muse-Glimmer-30B`（Apache 2.0・8/10 告知）は既報である

### 市場・その他

- Apple が中国向けの独自 LLM を Alibaba の支援で訓練したと報じられた（8/14）。中国政府が独自 AI モデルの提供を承認した初の外国企業にあたり、従来は中国国内モデルに依存して生成AI機能を届ける方針だったため戦略の転換になる。対象は中国で販売する iPhone・iPad・Mac・Vision Pro で、AI 機能の展開は今後数カ月内の見込みである。米国では Apple が自社技術と組み合わせて使う Claude や ChatGPT は中国では利用できず、Huawei 等の国内勢との競争が背景にある。⚠️ Reuters 系の取材ベースで、Apple・Alibaba 双方の公式発表ではない
- `developer.apple.com` は 200 で、8/12 の年齢レーティング更新以降に新規がない。AI 関連の最新は 8/5 のままである。iOS 27 / iPadOS 27 は developer beta 4（7/20・ビルド 23G71）が最新で、GA は9月（予想 9/14 前後）の見込みである

## 直近の注目予定

- **8/16**: DeepSeek V4-Flash / V4-Pro の新単価が発効（16:00 UTC ＝ 日本時間 8/17 1:00）
- **8/17**: Claude Console 旧 Workbench 退役と実験的プロンプトツール API 廃止 ／ Gemini API の Imagen 4.0 系3本停止 ／ Gemini in Classroom のモバイル開放
- **8/18**: 業務用 Copilot の URL 移行開始とデスクトップ早期プレビュー ／ PPCC 2026 の標準価格での登録期限 ／ Copilot Studio Released Versions の次回定例
- **8/19**: Claude Code の週次上限50%増が終了（23:59 PT）
- **8/20**: Gemini Enterprise Agent Platform の Grok 4.1 ファミリー停止（一次未確認） ／ Pixel 11 系の出荷開始
- **8/22**: M365 Copilot アプリのチャット中心 UI が Deferred リングへ展開開始（MC1325422）
- **8/25 前後**: M365 Copilot Release Notes の次バッチ（隔週サイクルどおりなら）
- **8/26**: OpenAI Assistants API 廃止 / o3 退役 / GPT-4.5 完全廃止 ／ Copilot 既定モデル有効化ポリシー発効
- **8/27**: IT Nation Connect ANZ の Microsoft セッション
- **8/30**: 公式 DALL·E GPT の退役
- **8/31**: GitHub Spark の既存ユーザーアクセス終了 ／ `gemini-robotics-er-1.6-preview` 停止 ／ GPT-5.4・5.4 mini が Codex から除外 ／ Claude for Government の $1/機関プログラム終了 ／ Power Automate モバイルアプリ廃止 ／ CSP Copilot Partner Council コンテストの応募期限
- **9/1**: GitHub Copilot の全体験でモデル廃止（Claude Sonnet 4.6 が非推奨） ／ OpenAI Daybreak で全アカウントにハードウェアセキュリティキー必須化 ／ MAICPP 契約の更新条項が自動発効
- **9/2〜9/3**: Windows 365 Frontline 名称での購入最終日（9/2）と Windows 365 Flex への改称（9/3）
- **9/10**: MAI-Code-1-Flash が全 Copilot 体験から廃止
- **9 月**: iOS 27 / macOS 27 GA ／ auto mode の既定化を Enterprise・API・各クラウドへ拡大予定 ／ 9月中旬に Copilot デスクトップアプリの広範な展開開始 ／ 9/30 に M365 E7 プロモーションの対象購入最終日と M365 E5・E3 の CSP 割引終了
- **10 月**: Anthropic の IPO 予定（$2T 超の評価額を目標と報道） ／ 10/1 に CSP ソフトウェアの5%上乗せ発効 ／ 10/20〜22 に SMB Copilot Partner Council（NYC） ／ 10/25〜30 に PPCC 2026 本編とワークショップ
- **11/1**: パートナー特典の有効期限がオファー購入日基準へ移行
- **12/2**: EU AI Act の生成コンテンツ標識義務、8/2 以前に市場投入済みシステムへの猶予終了
- **12/31**: Gemini 3.6 Flash / 3.7 Flash の導入価格終了（$0.75 / $3.75 → $1.50 / $7.50） ／ M365 E3 プロモーション・Copilot in 30・Purview Suite 50%オフの提供終了
- **2027年6月末**: Frontier Partner バッジの廃止

## 改善メモ

- 本サマリーの記録の訂正が本日2件出た。いずれもソース側の再確認によるもので、日付の古い記録ほど検証されにくい構造が残っている
  - Qwen3.8-27B: 08-13・08-14 と2日連続で「未公開が継続」と記録したが、実際には 8/14 に公開されていた。原因は製品名からリポジトリ ID を推測していたことにあり、org 一覧 API の全件走査（B-032）で検出できた
  - Gemini 3.6 Flash: 08-14 に「二次確認により据え置き」と記録したが、一次ページの読み取りが正しく二次が誤りだった。ソース側は B-005 に「一次と二次が食い違い二次が誤っていた初の事例」として追加している
- ソース間の食い違いが1件ある。JetBrains の Claude Fable 5 評価事例について、01_ai-news-Master は記事本文を取得して定量値（pass rate 44.3% / 28.2%、ステップ数22%減）まで記録しているが、03_ai-news-industry は本日 WebFetch が 404 で本文未確認としている。本サマリーは Master 側の取得結果を採用した
- 取得できていないソースは次のとおり。Message Center は8日連続で一次取得できず、MC1454386 が未掲載のままである。Codex CLI の alpha 各版リリースノートはページ側エラーで2日連続未確認である。Copilot Studio の課金レート USD 単価は取得できない PDF にしかない
- 障害の新規登録が2件あった。`support.microsoft.com` がゲートウェイ拒否を返し（Copilot アプリ統合の一次解説がここに置かれているため、掲載根拠は Partner Center のアナウンスに寄せている）、`techstartups.com` もゲートウェイ拒否として記録された
- 継続提案は Master 15件（最多: B-013 許可ドメイン追加、19回目）、Copilot 17件（最多: B-011 Power Platform Blog のトピック記事照合、27回目）、industry 8件（最多: B-004 取得方法欄の WebSearch 優先化、47回目）である。Master は新規に B-035（Claude Code の版検出に npm dist-tags を加える）を追加した
