# AI News Daily Summary — 2026-08-05

水曜は期限の告知が重なった。GitHub Spark は 8/31 でエクスポートごと閉じ、M365 E7 の割引は 9/30 の購入分で終わる。Claude Opus 4.1 は予告どおり本日 Claude API から退役した。ツール側では Claude Code が10日ぶりの更新で承認プロンプトの迂回2件を塞ぎ、Cursor のエージェントは Gmail と Calendar に書けるようになった。Alibaba は Qwen3.8-Max を $2/$6 で正式公開し、来週のオープンウェイト化を予告している。Copilot Studio のハーネスは 8/3 に GA していたが、Learn の What's New は今も Preview 表記のままである。

## 今日のハイライト

### 1. GitHub Spark が退役する — 8/31 を過ぎるとコードを取り出せなくなる

**要点**: GitHub が Spark の提供終了を告知した。8/4 で新規作成が止まり、**8/31** に既存ユーザーのアクセスとエクスポートが同時に終わる。前提は「コードはいつでも取り出せる」から「8/31 までの手動退避が唯一の手段」へ変わる。

**詳細**: 期限は2段階に分かれている。8/4 時点で新規ユーザー受け入れと新規アプリ作成が停止済みで、8/31 に既存ユーザーのアクセスとエクスポートの両方が終了する。デプロイ済みアプリは 8/31 以降も動き続けるが、`llm()` を使っているアプリは推論基盤の GitHub Models が 7/30 に退役済みのため既に動作していない。`llm()` を使い続けるには別の推論プロバイダへ載せ替え、自分の API キーとコストを持つ必要がある。

エクスポートは Spark workbench を開き、メニューから「Create repository」を選ぶ。GitHub は退役理由として、AI モデルとエージェント型開発ツールの進歩により VS Code・Copilot CLI・GitHub Copilot アプリ内の統合ワークフローのほうが適した代替になったことを挙げている。

- https://github.blog/changelog/2026-08-04-upcoming-deprecation-of-github-spark-on-github-com/

### 2. Microsoft 365 E7 の割引が 10/1 に終わる — Copilot 同梱 SKU の見積もりは 9/30 が実質の期限

**要点**: Microsoft が E7 の販売促進割引3本を **10/1** で打ち切る。対象購入の最終日は 9/30 である。割引前提で組んだ Copilot 同梱 SKU の提案は、定価へ引き直すか9月中に確定させるかの二択に変わる。

**詳細**: Partner Center の8月アナウンスページが公開された（掲載3件・いずれも 8/3 付）。8/4 時点では 404 で未公開だった。M365 のプロモーションは E7 と E3 で逆方向に動いている。

- 終了する E7 プロモーション3本: 10% off 1年 / 15% off 1年 / 15% off 3年。対象顧客の購入は 9/30 まで可能で、10/1 以降は新規のプロモーション取引ができない。**購入済みのサブスクリプションは契約条件どおり継続**する
- 延長される E3 プロモーション2本: 10% off 3年（新規向け）と 20% off 1年（ターゲット向け）が、いずれも 12/31 まで利用できる

Microsoft は理由として、プロモーション取引中心の投資から「growth margin」（継続利用と展開成功に報いる仕組み）への移行を挙げている。E7 は M365 E5 に Copilot を同梱した SKU で、5/1 に Agent 365 とあわせて GA した。Copilot の全社展開を E7 の割引前提で見積もっている場合に影響が出る。

- https://learn.microsoft.com/en-us/partner-center/announcements/2026-august

### 3. Claude Code v2.1.221 が承認プロンプトの迂回2件を塞いだ — v2.1.220 以前は「承認したものだけが実行される」が成立していなかった

**要点**: Anthropic が Claude Code を10日ぶりに更新し、zsh の `[[ ]]` 条件式に隠したコマンドが Bash の権限チェックを迂回できる欠陥を塞いだ。「承認を通ったものだけが実行される」という前提は、**v2.1.220** 以前では成立していなかった。

**詳細**: 39件の変更を含む。セキュリティ関連の修正は2件で、いずれも該当コマンドが今後は承認を求めるようになる。

- zsh が `[[ ]]` 正規表現条件の内側で隠しコマンドを実行できた、Bash ツールの権限チェックバイパス
- Windows で PowerShell の権限チェックが引用符を含むパスを誤処理していた問題

サンドボックス側にも新しい防御が入った。Linux / WSL で資格情報ファイルに `mode: "mask"` を指定すると、サンドボックス内のコマンドはセンチネル値の複製（ファイル全体、または `extract` 正規表現が捕捉した範囲だけ）を読み、サンドボックスプロキシが egress 時に実物へ差し替える。macOS ではファイルマスキングは `deny` にフォールバックする。

- https://code.claude.com/docs/en/changelog
- https://github.com/anthropics/claude-code/releases/tag/v2.1.221

## カテゴリ別まとめ

### Anthropic / Claude

- Claude Opus 4.1（`claude-opus-4-1-20250805`）が本日 8/5 に Claude API から退役する — 推奨移行先は `claude-opus-4-8` である。6/5 の予告どおりで、公式の deprecation ページで一次確認した。対象は Anthropic 運営プラットフォーム（Claude API / Claude Platform on AWS / Microsoft Foundry）で、Amazon Bedrock と Google Cloud は独自スケジュールを持つ。
- Claude Code の利用枠は、期限が3本ばらばらに切れる状態が続いている — Cowork の倍増枠は本日 8/5 で終了し、週次上限50%増は 8/19 まで、Sonnet 5 の促進価格 $2/$10 は 8/31 まで（以降 $3/$15）である。
- Claude API release notes に 8/1 エントリが存在した（前日記録の訂正）— 内容は Dreams（research preview）が Claude Opus 5 に対応したことである。前日 08-04 は「7/24 が最新のまま／11日間追加なし」と記録していたが、本日同じ URL を取得すると 8/1 エントリが 7/24 の直上に載っている。⚠️ 8/1 エントリが 08-04 時点でページに存在したかは事後確認できず、「前日の取りこぼし」と「後日追記」のどちらかは確定しない（B-024 を起票）。
- Anthropic は本日も新規発表を出していない — `www.anthropic.com/news` はオリジン403が継続しており、規定の WebSearch 5本をすべて実行しても 8/4〜8/5 の新規発表は検出できなかった。`claude.com/blog` の最新は 7/28「Bringing MCP 2026-07-28 to Claude」、`support.claude.com` の Release Notes の最新は 7/24 の Opus 5 で、いずれも8月分の追加はない。
- MCP の公式ブログにも新着はない — RSS の最新は 7/28 の `The 2026-07-28 Specification` のままで、8日連続で動きがない。仕様 `2026-07-28` と Tier 1 SDK の対応状況（TypeScript / Python / C# が 2.0 系、Go は v1.7.0）も 08-04 の確定内容から変化していない。

### OpenAI / Codex

- OpenAI が ChatGPT アプリと Codex CLI の Auto-review を GPT-5.4 から **GPT-5.6 Luna** へ切り替えていた（7/30・本日初検出）— 7/30 の80%値下げと合わせ、Auto-review のコストは従来の約1/10 になる見込みだと OpenAI 自身が述べている。レビュー対象を絞っていた運用は、絞り込み条件を見直せる。
  - 原資は Luna の入力 $1→$0.20／出力 $6→$1.20（-80%）で、Terra は $2.50/$15→$2/$12（-20%）。新単価は Codex と ChatGPT Work の利用量カウントにも反映される
  - 値下げの根拠として OpenAI は、GPT-5.6 Sol の GA 後に Sol 自身を Codex 上で走らせて推論基盤の GPU カーネルを最適化させた自己最適化ループを挙げ、提供コスト-20%・トークン生成効率+15%超と説明している
  - 単価改定と Fast mode 追加は 08-01 収録の既報で、今回の初出は Auto-review の実行モデルが変わった点である
  - https://x.com/OpenAI/status/2082878180478910571
- Codex CLI の pre-release は 0.147.0-alpha.7 が最新である（8/4 11:50 UTC）— 8/3〜8/4 で alpha.6 → alpha.6.1 → alpha.7 と3回刻まれたが、いずれもリリースノートが付いていない。安定版は 0.146.0（7/29）で据え置きである。
- OpenAI が公式 DALL·E GPT を 8/30 に退役させる — 利用者は ChatGPT Images に誘導される。画像生成そのものは対象外だが、GPT Store 上の公式 GPT が畳まれる事例として記録する。
- 一次ソースの状態は据え置きである — `developers.openai.com/changelog` の最新は 7/30、`community.openai.com` の Announcements RSS の最新も 7/30 で、8月の新規はない。`openai.com` / `help.openai.com` / `learn.chatgpt.com` は本日も到達できず、Auto-review の件は二次情報（OpenAI 公式 X 投稿の引用）に依存している。

### Google / xAI

- Gemini API の単価は据え置きで、旧世代の 3.5 Flash が上位の 3.6 Flash より高い状態になっている — `ai.google.dev` の料金ページを一次取得し、08-04 収録分から変更がないことを確認した（WebFetch 成功は3日連続）。
  - Gemini 3.6 Flash が入力 $1.50／出力 $7.50 なのに対し、**Gemini 3.5 Flash は出力 $9.00** で20%高い
  - Gemini 3.1 Pro Preview: 入力 $2.00〜$4.00（プロンプト長で変動）／出力 $12.00〜$18.00
  - Gemini 2.5 Pro: 入力 $1.25〜$2.50／出力 $10.00〜$15.00、2.5 Flash は $0.30／$2.50
  - Batch API は全モデルで50%減で、処理を優先させる Priority ティアが別建てで存在する
  - 3.5 Flash に留まる価格上の理由はなく、8/4 に Gemini Enterprise の global リージョンからこのモデルが削除された動きとも整合する
  - https://ai.google.dev/gemini-api/docs/pricing
- Gemini API の changelog は 7/30 が最新のままで、8月の追加はない — 8/17 の Imagen 4.0 系3本停止と 8/31 の `gemini-robotics-er-1.6-preview` 停止は 7/30 時点で一次確認済みである。
- Gemini Enterprise アプリの global リージョンからの Gemini 3.5 Flash 除外（8/4）は、一次未確認のまま残っている — `docs.cloud.google.com` の release notes が本日も取得できず、二次情報の記述に留まる。
- Gemini 3.5 Pro の GA は未ローンチが続いており、Vertex AI 限定の preview のままである — 公開 API で GA 済みのフラッグシップは引き続き Gemini 3.1 Pro である。
- xAI の Grok 4.6 は 8/5 時点でも未公開のままである — 8/7 前後という目標（1.5T・Grok 4.5 と同じ V9 基盤の再利用＋SFT / RL 改善）は 7/28 の Musk 発言から変わっていない。⚠️ SEO 系サイトが「8月7日に launched」と完了形で書く状態が続いているが、xAI はモデルカード・API ドキュメント・価格・ベンチマークのいずれも出していない。

### GitHub Copilot

- GitHub が Copilot CLI を安定版 v1.0.78 に上げた（8/3 23:30 UTC）— 7/30 の v1.0.77 以来の安定版で、pre-release の 78-0〜78-3 をまとめて取り込んだ内容にあたる。
  - タイムラインヘッダーにツール呼び出しの所要時間が表示される
  - プラグインが自動更新されるようになった
  - 実験的な `/new-worktree`（worktree を作成しその中で新しい会話を開始する）が入った
  - ローカル端末のログインがブラウザベースになり、サンドボックスがビルドに対してツールチェーンのキャッシュへ既定でアクセスを許可するようになった
- GitHub が Copilot cloud agent の reasoning level をユーザーに選ばせるようにした（8/3 GA）— タスクを委任するときにモデルと並べて選択する。高い水準ほど複雑な問題の回答は良くなるが、トークン消費＝クレジット消費が増えるというトレードオフが明記されている。対象は Copilot Pro / Pro+ / Business / Enterprise / Max である。
- GitHub が managed settings のチーム単位適用を GA にした（8/3）— 企業全体で1つのポリシーファイルを配る運用から、チームごとに別ファイルを割り当てる運用へ変えられる。
  - `copilot/managed-settings.json` で個別キーを overridable と指定でき、チーム側が値を上書きしても未設定キーは企業レベルの値がフォールバックとして残る
  - `team-mappings.json` でチームやチームグループごとに適用するポリシーファイルを対応づける。1ファイルを複数チームに割り当ててもよい
  - `enabledPlugins` と `extraKnownMarketplaces` は加算的で、企業ベースラインが全体に効きつつチームが役割別の拡張を足せる
  - overridable にしなかったキーは企業レベルの上限として固定され、コンプライアンス要件をチーム設定から守れる
  - 対応クライアントは VS Code・Copilot CLI・Copilot App・Copilot cloud agent で、残りのクライアントの SDK 対応は開発中である
- GitHub が Issue / PR へのコメントで Copilot automations を起動できるようにした（8/3 GA）— 起動条件にするコメント文字列を automation 側で指定し、リポジトリの Agents タブ → サイドバーの Automations から設定する。想定用途としてドキュメント生成、スタックトレースやエラーログの調査、リファクタリングの follow-up issue 作成が挙げられている。Business / Enterprise は管理者が Copilot cloud agent ポリシーを有効にしている必要がある。
- GitHub Spark の退役（ハイライト参照）
- 既報: Copilot Billing Preview app の廃止（8/3）、統合 Copilot「super app」表明（7/29 決算コール・M365 Copilot 有料シート3,000万超）、既定モデル有効化ポリシーの 8/26 発効

### Copilot Studio / Power Platform

- GitHub Copilot ハーネスとワークフローデザイナーが 8/3 付で GA していた — 昨日は techcommunity が 403 で記事本文を取得できず課金仕様だけを確認していたが、本日 403 が解けて発表記事を一次で読めた。前提が「Preview を評価する段階」から「本番投入してよい段階」へ変わる。
  - GA の対象は2つで、GitHub Copilot ハーネス本体（本番利用可）と、ワークフローデザイナー（ビジュアルキャンバス、エージェントノードの追加、ワークフロー評価の実行）である
  - 稼働モデルとして **Opus 5・GPT-5.6 Sol・Fable 5** が挙げられ、ハーネスは GitHub Copilot SDK を基盤とする
  - 標準ハーネスとの比較テストで、マルチツール利用・ファイル解析・コード解析・ナレッジ品質の4点で改善が出たとしている
  - 課金は M365 Copilot ライセンスの有無にかかわらず使用量ベースで、自然言語オーサリングと評価も消費対象に含まれる（8/4 掲載の課金仕様と一致）。自然言語での複数ターン対話によるオーサリングは「coming soon」で未提供である
  - ⚠️ Learn の Copilot Studio What's New は本日時点でも June 2026 節に `(Production-ready preview)` と書いたままで、GA が反映されていない。**文言だけで提供段階を判定すると誤る**（B-023 を起票）
  - https://techcommunity.microsoft.com/blog/copilot-studio-blog/more-powerful-agents-and-workflows-for-autonomous-business-processes-introducing/4542969
- Learn の `harnesses-overview` が3ハーネスの比較表を掲載し、選定基準を一次で読めるようになった — 用途は GitHub Copilot ハーネスが複雑な多段階業務、標準ハーネスがルールベースのエージェントと定型会話、Copilot チャットハーネスが M365 Copilot Chat への社内ナレッジ接続である。ファイル操作（Word / Excel / PowerPoint / PDF の作成・編集）と Skills / Memory に対応するのは GitHub Copilot ハーネスのみで、他の2つは「Not a focus」と明記されている。公開先は前2者が社内・社外の両方、Copilot チャットハーネスは社内のみに限られる。
  https://learn.microsoft.com/en-us/microsoft-copilot-studio/harnesses-overview
- Microsoft が自律エージェントを「実行専用」で配布できる共有モデルを公開した — 正式名称は「Share Autonomous Agents to End Users」で、**2026年8月にプレビュー・2027年1月に GA** の予定である。対象は Copilot Studio Web と worldwide の標準マルチテナントクラウドで、エンドユーザーの資格情報で動くトリガーを作成でき、受け取った側は所有者・編集者・共同編集者にならずに成果だけを受け取る。これまでは自律エージェントを広く配ると受領者にメーカー相当の権限を渡すことになり、社内展開の最大の障壁になっていた。配布設計を作る側と使う側で分離できる前提に変わる。
  https://learn.microsoft.com/en-us/power-platform/release-plan/2026wave1/microsoft-copilot-studio/planned-features
- Release Wave の全行照合で、7月 GA 未達が7件ではなく **9件**であることが分かった（前日までの計上の訂正）— Process mining の2件が計上漏れだった。GA 列に新しい緑チェックは付かず、直近の GA は 7/16 の3機能から動いていない。ページの `ms.date` も 7/21 のままである。
  - 計上漏れだった2件: オブジェクト中心プロセスマイニングの Fabric セマンティックモデルへのエクスポート／データ取り込みの正規化スキーマインポート対応
  - 8月予定も4件ではなく6件だった。Power Automate はライセンスダッシュボード改善（GA）・デスクトップフローのカスタムダッシュボードタイル（Preview）・プロセスインテリジェンスのカスタム KPI（GA）、Power Apps は Dataverse オンラインモードのキャンバスアプリ対応（Preview）・ヘッダーとナビゲーションの刷新（GA）・モデル駆動アプリの行要約強化（GA）
- Copilot Studio Build は 2026.6.3（6/30 初出）が最新のまま動かず、7月ビルドがゼロの状態が続いている — リージョン分布も変化がなく、UK・Asia・UAE・Japan・Europe が 2026.6.2、Australia・US 本体・GCC が 2026.6.1 のままである。UX 版も 26.06.21-24 で据え置きである。
- Copilot Studio のライセンスガイドに August 2026 版が存在することを確認した — ただし配信元 CDN が 403 を返すため本文を取得できず、一次未確認である。Learn の課金ページからは `aka.ms/CopilotCredits/LicensingGuide` としてリンクされている。
- 月次「What's New in Power Platform」は7月号が公開されないまま8月に入った — 最新は 6/11 の June Feature Update のままで、子カテゴリのトピック記事も 7/6 の Dataverse 記事から動いていない。Power Automate Blog（4/8 が最新）と Power Apps Blog（5/13 が最新）にも新規はない。

### Microsoft 365 Copilot / ガバナンス

- CSP パートナー向けの Copilot in 30 が GA になった — パートナーが従業員300人未満の顧客に M365 Copilot Business の試用を提供できるようになる。25ユーザー・30日間の試用に、優先ユーザーの特定とユースケース検証の手順をあわせた「パートナー主導」の型である。CSP New Commerce での取り扱いは 12/31 までの期間限定となる。
  - 取引開始は 8/1 で、製品 ID は `CFQ7TTC0MM8R`、SKU ID は `006Z`
  - 顧客向け評価ツールが8月中旬に追加され、業種を選ぶと業務に即したプロンプトとシナリオが提示される
  - パートナー向けの Copilot Success Microskilling は 8/3 開始、Copilot Success Planner は 8/14 提供
- パートナーの特典償還プロセスが変わった — Partner Center 上のガイド付き体験と 0 USD の購入フローで償還する方式になる。GitHub Enterprise と GitHub Copilot Enterprise 向けの Azure クレジットも対象で、ユーザー割り当て・アクティベーションリンクのコピー・新規 Azure サブスクリプション作成の手順が不要になり、請求プロファイルへ直接入金される。**11/1 以降は有効期限がオファー購入日基準**へ揃う（従来は初回償還日基準）。償還できるのは MCA 請求アカウント配下のテナントに限られ、サードパーティテナントでは償還できない。
- M365 Copilot Release Notes は「July 29, 2026」節が最新のままで、本日も新バッチは追加されていない — 対象期間 7/15〜7/29 の全10項目とアプリ別5節の構成に増減はない。次バッチは隔週傾向どおりなら8月中旬の見込みである。
- SharePoint Blog の board RSS が復旧し、取りこぼしていた記事2件が判明した — いずれも Copilot in SharePoint の実践寄りの記事で、製品変更の告知ではない。
  - 7/28「SharePoint Showcase: 10 Custom AI Skills Every SharePoint Site Owner Should Build」— サイト所有者向けのカスタム AI スキル10種
  - 7/21「Beyond Benchmarks: The Lifecycle of Measuring Agentic Quality in AI Content Management」— エージェント品質の測定サイクル
  - 月次記事「What's New in Copilot in SharePoint: July 2026」の公開日は 7/16 だった（従来は日付未特定のまま扱っていた）
- Microsoft 側の定例ソースはそれ以外ほぼ据え置きである — Tech Community 月次ブログは 7/31 の July 2026 号、M365 Blog 本体は 7/30「The next measure of AI momentum is work transformed」、M365 Roadmap の Latest announcements は 7/9、M365 Developer Blog は 7/17 の統合マニフェスト GA 記事が最新で、いずれも8月の新規記事はない。Purview の What's new も7月節に Copilot 関連の追加はなく、8月節はまだ立っていない。
- M365 E7 / E3 プロモーションの変更（ハイライト参照）

### 開発ツール

- Cursor のエージェントが Google Workspace に書き込めるようになった（8/3 公開・本日初検出）— Drive / Gmail / Calendar のプラグイン3種が出て、読むだけでなく書ける。コーディングエージェントの権限境界がリポジトリ内から業務メールと予定表まで広がるため、承認範囲を決める単位が変わる。
  - Google Drive: ファイルとフォルダの検索、コンテンツの閲覧とダウンロード、ファイルの作成と整理
  - Gmail: メールの検索と閲覧、下書き作成と送信、ラベル適用とスレッド管理
  - Google Calendar: 予定の閲覧、イベントの作成と更新、空き時間の検索
  - 導入は Cursor Marketplace、または Cursor 内の Customize ページから行う。⚠️ 公開ページに対象プラン・利用上限・追加料金の記載がなく、これらは未確定である
  - https://cursor.com/changelog/google-workspace-plugins
- Claude Code v2.1.221 はセキュリティ以外にも挙動が変わった（ハイライト3の残りの変更）— エージェントの動き方と表示の両方に手が入っている。
  - バックグラウンドセッションは作業を保全するため commit と push を行い、draft PR はタスクが要求するときだけ開き、CLAUDE.md の git 指示に従い、最後に必ず作業場所を報告する
  - `/fork` したセッションは元セッションのチェックアウトを共有せず、自前の worktree を作る
  - VSCode に Focus view が入った（`Ctrl+Alt+F` または「Claude Code: Toggle Focus」）。ツール実行のログをターンごとの折りたたみ要約の裏に隠し、実行中インジケータだけを出す
  - `claude-api` skill に `prompt-audit` サブコマンドが加わり、旧世代モデル向けに書かれたプロンプトとツール説明を検出できる
  - 不具合修正では、thinking 無効かつ effort `xhigh` / `max` で WebSearch が 400 を返す問題と、print mode（`-p`）で `--mcp-config` の MCP サーバーが初回ターン前に接続されずツール呼び出しが文字列として出力される問題が直った。auto mode の権限チェックは会話プレフィックスのキャッシュを再利用するようになり、プロンプトキャッシュ費用が下がる
- Cursor の Announcements フォーラム側に8月の新規投稿はない — 最新は Cursor Start（₹649/月・7/28）のままである。
- Devin は本日も日付を確定できる新規リリースを確認できなかった — `docs.devin.ai` / `devin.ai` / `cognition.com` はゲートウェイ拒否が続いており、WebSearch でも7月分（SWE-1.7、Devin Security Swarm、FedRAMP High、Devin Outposts）以降の新着は出てこない。

### モデル / オープンウェイト

- Alibaba が Qwen3.8-Max を正式公開し、Max 級が **$2/$6** に降りてきた（8/3）— 総パラメータ2.4兆・1トークンあたりアクティブ 95B のスパース MoE で、文脈長100万トークン、出力上限13.1万トークン、テキスト/画像/動画入力に対応する。100万トークンの文脈全域が同一単価で、明示キャッシュは作成 $2.50・読み出し $0.17 である。7/19 のプレビュー時は独立ベンチ非公表・オープンウェイト日程未定だったため、単価・ベンチ・公開日程が確定したのは今回が初めてである。
  - OSWorld-Verified（OS・アプリのエージェント操作）: 86.1 で GPT-5.6 Sol Max 83.2・Fable 5 85.0 を上回り首位
  - Terminal-Bench 2.1: 86.6 で Claude Opus 4.8 / Fable 5 の 84.6 を上回るが、GPT-5.6 Sol（max）88.8 に及ばない
  - SWE-bench Pro は 67.7 に対し Fable 5 が 80.0、FrontierSWE は 73.5 に対し 88.8 で、ソフトウェア工学系は明確に劣後する
  - オープンウェイトは Qwen3.8-Max と Qwen3.8-27B の2本を来週 Hugging Face / ModelScope で公開予定。⚠️ **ライセンスは未公表**で、7/16 の Kimi K3（revenue-tiered 独自ライセンス）と 7/31 の K-EXAONE 2.0（Apache 2.0）のどちらに寄るかで調達上の扱いが変わる。2.4兆パラメータ版はマルチノード前提のため、自己ホストの現実解は 27B 側になる
  - https://venturebeat.com/technology/qwen3-8-max-arrives-with-a-bold-claim-it-outperforms-gpt-5-6-sol-max-and-fable-5-on-agentic-computer-use
- 8/4〜8/5 に作成された注目すべきオープンウェイト LLM はない — Hugging Face の trending 上位40件を照会したが、8/3 以降に作成されたリポジトリは `MiniMax-H3` 系の量子化・変換（動画生成のため対象外）と `Qwen3-VL-32B` 派生のコミュニティ版のみだった。トップは引き続き `deepseek-ai/DeepSeek-V4-Flash-0731`（7/31 作成）で、ダウンロードは前日 236,076 から 433,284 へ1.8倍に伸びている。
- 既報: Thinking Machines の Inkling-Small（7/30）、DeepSeek V4 の GA（7/20）、Qwen3.7 Flash（7/27）、Kimi K3（7/17）

### 規制・政策

- オープンウェイト擁護書簡の署名が **270社超**に達した（8/3 時点）— 7/24 に Nvidia / Microsoft / Meta / IBM / Dell / Palantir / a16z / Hugging Face / Y Combinator ら25社で始まった「Open Weights and American AI Leadership」が10倍超に拡大した。趣旨はオープンウェイトモデルへの新たな規制がかえって対中国での米国の立場を弱めるとして、拙速な制限に反対するものである。内訳はチップメーカー・サーバーベンダー・クラウド事業者・エンタープライズソフト・セキュリティ企業・VC に広がっている。OpenAI と Anthropic は依然として不参加で、07-30 収録の「Anthropic がオープンウェイト論争で孤立」の構図は変わっていない。ベンダー選定でオープンウェイト方針を論点にする場合、業界の多数派と主要2ラボの立場が割れている前提で説明する必要がある。
  https://www.microsoft.com/en-us/corporate-responsibility/topics/open-weight/
- EO 14409 の自主フレームワークは4日連続で未公表のままである — 6/2 大統領令が課した60日期限は 8/1 に満了したが、本日時点でも Federal Register 告示・NIST / CISA 公表・OSTP 声明のいずれも確認できていない。議会調査局（CRS）の解説では、この期限は AI 企業側のコンプライアンス期限ではなく政府機関側の設計期限であることが改めて整理されている。作成対象は covered frontier model を判定する機密ベンチマークプロセスと、公開前最大30日の政府アクセスを含む自主フレームワークの2点である。
  https://www.congress.gov/crs-product/IF13268

### 市場・エコシステム

- エージェントの本番拡大が統制を追い越している — Domino Data Lab の第5回 Enterprise AI Report（2026年4月・北米/英国/欧州大陸の年商 $100M 以上の組織のディレクター職以上 **639人**）で、統制された本番でエージェントを稼働させている組織が43%、統制が伴わないまま拡大中29%・パイロット中12%の計 **41%** だった。拡大がパイロットを2倍以上上回っている。
  - 2026年の組織的優先事項の首位は「エージェント利用の拡大」（38.5%・業務ユーザーのリスキリングと同率）で、ガバナンス基盤への投資を含むあらゆる投資項目を上回った
  - ガバナンスが AI 活動に完全に追随できている組織に限れば、統制下の本番稼働は 67.5% まで上がる
  - 投資額を上回るリターンが出ていない企業は 57% で2025年から不変、一方で本番化能力の改善を報告した企業は93%（前年88%）。地域差があり、リターンが出ていない割合は北米 51.1% に対し英国 66.9%・欧州 67.0%
  - ⚠️ 7/22 公表を14日間取りこぼしており、B-008 の根拠に追加された
  - https://www.computerweekly.com/blog/CW-Developer-Network/Domino-Data-Lab-Agentic-AI-is-scaling-faster-than-governance-the-split-explained
- AI 向け電力と推論チップに1日で $1.3B が入った（8/3 発表分）— AI の物理層への大型調達が2件重なった。
  - Valar Atomics: Sequoia 主導の Series B $10億、評価額$60億（数カ月前の$20億から3倍）。別途 Erebor Bank が管理代理人、J.P. Morgan 参加の $2億のクレジットファシリティを締結し計$12億。ヘリウム冷却の高温ガス炉を「建設プロジェクト」でなく「量産品」として作る方針で、6/18 に臨界達成、その1週間後に NVIDIA Blackwell への直接給電を実施した（先進炉が AI インフラへ直接給電した初例）
  - OLIX（ロンドン）: Series B $3.12億、評価額$33億で、欧州企業の半導体 VC ラウンドとして過去最大。Fundomo 主導で Arm・Hudson River Trading・Reed Hastings・英国政府 Sovereign AI Fund が参加。光を使う Optical Tensor Processing Unit（OTPU）で、HBM を使わずオンチップ SRAM にモデルを保持する設計。顧客提供は2027年下期の予定
  - 08-04 収録の「AI データセンター向け HBM への生産能力再配分が消費者向け PC の納期に出た」件と表裏で、HBM を前提にしない推論アーキテクチャと自前電源に資本が向かっている
- Ai4 2026 のメインステージに Hinton・Fei-Fei Li・Ng が本日登壇する — 8月4〜6日にラスベガス The Venetian で開催中で、3氏の対談は本日 8/5、モデレーターは Washington Post 副編集長の Yun-Hee Kim である。規模は85カ国超から12,000人超、登壇者1,000人超、出展400社弱。Hinton と Ng は AI の実存的リスクをめぐって公然と正反対の立場を取っており、Hinton は AI 開発が人類絶滅に寄与する確率を10〜20%と見積もったうえで、企業のガバナンス構造では自主的な対応で安全性問題は解決できないと主張している。セッション構成の最大クラスタは「大規模なエージェント運用」で、上記 Domino 調査はその需要側の裏づけにあたる。

## 直近の注目予定

- **8/5（本日）**: Claude Opus 4.1 の Claude API 退役 ／ Cowork 倍増利用枠の終了 ／ Ai4 2026 で Hinton・Fei-Fei Li・Ng の対談
- **8/6**: ChatGPT Business の利用無償期間終了
- **8/7 前後（推定）**: Grok 4.6（1.5T）
- **8/9**: ChatGPT Atlas シャットダウン
- **8/10**: Power Platform Weekly の夏季休刊明け ／ 週次復旧チェック（月曜）
- **8/12**: Made by Google
- **8/14**: Copilot Success Planner の提供開始
- **8/17**: Claude Console 旧 Workbench 退役 ＋ 実験的プロンプトツール API 廃止 ／ Gemini API の Imagen 4.0 系3本停止
- **8/18〜9/8**: Microsoft 365 Copilot Agent's Playbook ライブストリーム（各回 9AM PT）
- **8/19**: Claude Code 週次上限50%増の終了
- **8/20**: Gemini Enterprise Agent Platform の Grok 4.1 ファミリー停止（一次未確認）
- **8月中旬**: M365 Copilot Release Notes の次バッチ見込み ／ Copilot in 30 の顧客向け評価ツール追加
- **8/26**: OpenAI Assistants API 廃止 / o3 退役 / GPT-4.5 完全廃止 ／ Copilot 既定モデル有効化ポリシー発効
- **8/30**: 公式 DALL·E GPT の退役
- **8/31**: GitHub Spark の既存ユーザーアクセス終了（エクスポート期限） ／ Sonnet 5 促進価格終了（→ $3/$15） ／ `gemini-robotics-er-1.6-preview` 停止 ／ Power Automate モバイルアプリの廃止
- **8月内**: Qwen3.8-Max / Qwen3.8-27B のオープンウェイト公開（来週予定） ／ Copilot Studio 自律エージェントの run-only 共有プレビュー ／ Release Wave の8月予定6件と7月持ち越し9件
- **9 月**: iOS 27 / macOS 27 GA ／ App Store の新規申請・更新で Social Media 年齢レーティング回答が必須化
- **9/30**: Microsoft 365 E7 プロモーションの対象購入最終日
- **10/1**: Microsoft 365 E7 プロモーションの新規取引停止
- **11/1**: パートナー特典の有効期限がオファー購入日基準へ移行
- **12/2**: EU AI Act の生成コンテンツ標識義務、8/2 以前に市場投入済みシステムへの猶予終了
- **12/31**: Microsoft 365 E3 プロモーションと Copilot in 30 の提供終了
- **2027/1**: Copilot Studio 自律エージェントの run-only 共有が GA 予定

## 改善メモ

- B-024（Master・新規）: 日付降順の changelog / release notes を WebFetch する際、最新エントリの取りこぼしを防ぐ確認手順を追加する
- B-023（Copilot・新規）: Copilot Studio の Preview→GA 移行を What's New の文言だけで判定すると取りこぼす（ハーネス GA が現に未反映）
- Industry: 新規提案なし
- 継続提案: Master 9件（最多 B-013 9回目）、Copilot 14件（最多 B-011 17回目）、Industry 5件（最多 B-004 37回目）
- 障害の変化（復旧）: Copilot 側で techcommunity の記事 HTML 本文と SharePoint Blog の board RSS が復旧した。Industry 側は `ai.google.dev` の WebFetch 成功を3日連続で確認した
- 障害の変化（新規・継続）: Copilot Studio ライセンスガイド PDF の配信 CDN が 403 で新規登録された。Master 側は新規発生・復旧とも0件で、`www.anthropic.com` / `openai.com` / `help.openai.com` / `learn.chatgpt.com` / `docs.devin.ai` / `docs.cloud.google.com` は到達不可のまま。`news.google.com` の RSS も403が続く
- 前日からの訂正2件
  - Claude API release notes: 08-04 は「7/24 が最新のまま・11日間追加なし」と記録したが、本日取得すると 8/1 エントリ（Dreams が Opus 5 対応）が載っていた。取りこぼしか後日追記かは確定しない（カテゴリ参照）
  - Release Wave の7月 GA 未達: 従来7件と数えていたが、Process mining の2件が計上漏れで実際は9件だった。8月予定も4件ではなく6件である（カテゴリ参照）
- ソース間の重複: Codex / ChatGPT の Auto-review が GPT-5.6 Luna へ切り替わった件は Master と Industry の両方が本日初検出として記録した。値下げの原資と自己最適化ループの説明は Industry 側が詳しいため、そちらをベースにした。Claude Code v2.1.221 は Master がリリース内容の全体、Industry が VSCode の Focus ビューに絞って収録しており、両方を統合した
- ソース間の矛盾: 本日は確認されなかった
