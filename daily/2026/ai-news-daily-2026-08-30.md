# AI News Daily Summary — 2026-08-30

日曜は、8月末の期限が実際に切れる直前の最後の平日前日にあたる。明日 8/31 と明後日 9/1 に、費用・権限・モデル可用性の期限が計12件重なる。エージェント CLI では Codex CLI が権限プロファイルとサンドボックスの抜けを3件塞ぎ、8/28 の Claude Code v2.1.251 にも6件目の権限修正が判明して、2日のうちに別ベンダーの2製品が同じ層の欠陥を公表した形になった。GitHub は Copilot CLI の実行基盤を Rust ネイティブへ載せ替え、VS Code 1.135 で他アプリの Claude セッションを継続できるようにしたが、どちらも週次まとめエントリにしか出ていない。Power Platform 側は Release Wave の8月コミット10件が緑チェックゼロのまま最終日を迎え、未達が確定した。Google Cloud は Gemini Enterprise の業種別パッケージ（法務・金融）を初めて出した。

## 今日のハイライト

### 1. 8/31 と 9/1 に期限が12件重なる — 動かないままだと費用と権限の条件が48時間で入れ替わる

**要点**: 明日 **8/31** に Claude Code の週次上限50%増の終了など7件、**9/1** に Copilot 新規シートの前払い必須など5件の期限が並ぶ。前提が「8月の枠と設定のまま9月に入る」から「48時間で費用・権限・使えるモデルが替わる」へ変わる。

**詳細**: 3ソースの期限一覧を突き合わせると、2日間に12件が集中している。うち Claude Code の週次上限だけが「延長されるかもしれない」枠で、残る11件は告知済みの確定期限である。

- 8/31（7件）
  - Claude Code の週次上限50%増が終了する見込みで、延長の告知は本日も検出できていない。5/13 開始で延長は3回、直近の告知は 8/19。失効すると週次枠が約3分の1減る。⚠️ 一次は `x.com`（ゲートウェイ拒否）のため二次一致にとどまる
  - GPT-5.4 / 5.4 mini が Codex（ChatGPT サインイン）から除外される。保存済み設定・カスタムエージェント・スケジュールタスクは `gpt-5.4` → `gpt-5.6-terra`、`gpt-5.4-mini` → `gpt-5.6-luna` へ自分で置き換える必要がある
  - GitHub Spark の既存ユーザーアクセスが終了する
  - Power Automate モバイルアプリの廃止が発効する
  - `gemini-robotics-er-1.6-preview` が停止する
  - Claude for Government の $1/機関プログラムが終了する
  - Release Wave の8月期日10件が未達のまま確定する（後述「Copilot Studio / Power Platform」節）
- 9/1（5件）
  - Copilot Business / Enterprise の新規シートが前払い必須になり、席の期中増減で調整する見積もりが成立しなくなる（既存顧客は 10/1）
  - GitHub Copilot の全体験でモデル廃止が実施され、global model policy の全 enterprise 適用が完了する
  - OpenAI Daybreak の全個人アカウントでハードウェアセキュリティキーが必須になる。攻撃側の Red だけでなく防御側の Blue も対象に入る。⚠️ Amazon Bedrock 経由（US East バージニア北部・`bedrock-mantle` エンドポイント）にも同要件が掛かるかは、一次・二次のいずれでも明示を確認できていない。9/1 以降にアクセスが止まる前提で確認しておく必要がある
  - MAICPP の更新条項が自動発効する

- https://github.blog/changelog/2026-08-28-upcoming-changes-to-github-copilot-policies-and-billing
- https://developers.openai.com/api/docs/deprecations
- https://ai.google.dev/gemini-api/docs/changelog

### 2. Codex CLI 0.151.0 が権限境界のすり抜けを3件塞いだ — 「設定した権限は効いている」が2日連続で崩れた

**要点**: `/cd` がサンドボックス制限を弱められる、権限状態の変更後も古い Guardian 判定が実行を承認できる等が同時に修正された。8/28 の Claude Code **v2.1.251** にも6件目の権限修正が判明し、前提が「設定してあれば守られる」から「版を上げるまで守られない」へ移った。

**詳細**: `rust-v0.151.0` は 8/29 09:55 UTC 公開で、8/27 の `0.150.1` から2日ぶりの安定版にあたる。Bug Fixes に並んだ権限・サンドボックス系は次の3件である。

- 復元した権限プロファイルが TUI のターンをまたいで保たれるようになり、`/cd` がサンドボックス制限を弱められる経路が塞がれた
- リモートサンドボックスの強制を、実行側の実際のホームディレクトリ・OS・パス規約に基づいて行うよう改めた
- 権限状態が変わった後に古い Guardian 分類が操作を承認してしまう問題を修正した

同版の機能追加は3件で、任意 MCP サーバーのツール検出に猶予期間を設定でき、拡張が MCP ツールの結果をモデルに渡る前に検査・置換でき、プラグインカタログがリポジトリ単位の設定を統合するようになった。ほかにモデル切替・フォールバック時のツール可用性と reasoning effort の整合、app-server 応答での構造化 MCP エラーの保持、入れ子サブエージェントのトークン使用量を root ゴールの予算へ算入する修正が入っている。

Claude Code 側では本日、8/29 の収録に含めていなかった権限修正が1件確認できた。**Bash の権限チェック**が、整数シェル変数への算術式代入（`OPTIND=1/0`・`RANDOM=2+2` 等）を自動承認していたもので、既報の5件（ファイルツールの symlink 差し替え・Grep / Glob への `Read(...)` 拒否ルール未適用・プラグインコマンドのパストラバーサル・プロジェクト設定によるベータトレーシング制限の迂回・Workflow ツールの `scriptPath`）と合わせ、v2.1.251 の権限関連修正は計6件になる。⚠️ Claude Code の npm `dist-tags` は `{stable: 2.1.236, latest: 2.1.251}` で **15版差のまま**動いておらず、stable 固定の組織へはこの6件が届いていない。

- https://github.com/openai/codex/releases/tag/rust-v0.151.0
- https://code.claude.com/docs/en/changelog

### 3. VS Code 1.135 が他アプリで始めた Claude のエージェントセッションを継続できる — IDE 側の変更は週次まとめにしか出ない

**要点**: Copilot CLI の実行基盤が Rust ネイティブへ移り（TUI は TypeScript のまま）、VS Code 1.135 は他アプリケーションで開始した Copilot / **Claude のエージェントセッション**を引き継げるようになった。前提が「IDE の変更は個別 changelog を見れば拾える」から「週次まとめを開かないと丸ごと落ちる」へ変わる。

**詳細**: 8/28 に `GitHub Copilot weekly releases — August 24` と `GitHub Copilot in Visual Studio — August update` の2本が公開され、本日新たに確定した。前者から読み取れる項目は次のとおりである。

- Copilot CLI: 「Copilot CLI runs on a native Rust runtime, while its terminal interface remains built in TypeScript」と明記された。8/27 の `v1.0.81` 本文には記載がない
- VS Code 1.135: 他アプリの Copilot / Claude セッションの継続、補完モデルによるセカンドオピニオン、単一ペインの Agents レイアウト、チャットターンごとのモデル別使用量表示
- Copilot App: Azure DevOps の issue / PR から Copilot セッションを起動、WSL 対応（実験的）、タブの分割と移動、ブラウザプレビューの外部ブラウザ送出

Visual Studio の8月更新は全プラン（Free〜Enterprise）が対象で、内容は5系統である。組織 / enterprise のオーナーがカスタムエージェントを公開でき、エージェントピッカーが説明と出所を自動表示する。対応モデルでは Low / Medium / High の思考レベルを選べる。モデルのピン留め・非表示と、能力・コンテキスト長・料金の比較ビューが加わった。Git エージェントは PR 作成前に未コミット変更と個別コミットをレビューし（GitHub / Azure DevOps 対応）、提案をエディタと Git Changes 一覧へ出す。プロンプトボックスからプラン詳細と使用量を確認でき、上限接近時に通知する。⚠️ IDE（VS Code / Visual Studio / JetBrains）のリリース内容は Copilot ラベルの個別エントリに立たないため、まとめエントリを開かないと全量が落ちる。

- https://github.blog/changelog/2026-08-28-github-copilot-weekly-releases-august-24
- https://github.blog/changelog/2026-08-28-github-copilot-in-visual-studio-august-update-2

## カテゴリ別まとめ

### Anthropic / Claude

- **Claude Code に 8/29〜8/30 の新規リリースはない**。changelog の最上位は `2.1.251`（8/28 15:34 UTC）のままで、npm の実 publish 記録とも一致する。権限修正の6件目はハイライト2参照
- **npm `dist-tags` は 15版差のまま動いていない** — 実測値は `{stable: 2.1.236, latest: 2.1.251, next: 2.1.251}`（8/30・curl）で、`next` == `latest` の収束は継続している。stable 固定の組織には v2.1.251 の権限境界修正が届いていない
- **Anthropic が社内での Claude Tag の使い方を公開した**（8/28・`claude.com/blog` 一次）。Claude Tag は Slack 等で `@Claude` にメンションするとスレッドの文脈・記憶・常設指示を読んでタスクを実行し、結果をスレッドへ返す。提供状態は **Team / Enterprise の public beta** で、設定は `claude.ai/admin-settings/claude-tag`。権限はチャネル・文書単位で付与された範囲に限られ、参照できない箇所は Claude 側が申告する
  - マーケティング: 15メッセージの Slack スレッドから2ページのブリーフを 45分で作成した
  - セールスオペレーション: 散在した機能要望を集約し、24アカウントの一覧を 26分で生成した（約120件の指摘を未解決23件・解決済み14件へ整理）。担当者は従来なら1週間かかる作業と見積もっている
  - 法務レビュー: 専用チャネルで Claude がマーケティング資材を事前審査する運用にし、弁護士レビューまでの所要が1日超から資材あたり 30分へ短縮した
  - ⚠️ **社内導入率も利用者数も記事に無く**、自社事例である点も含めて定量根拠としては弱い。08-25 収録の社内マーケター事例と同じ扱いで、「非エンジニアの部門担当が自分で仕組みを組む」型の実在例として使う
  - https://www.claude.com/blog/how-anthropic-employees-use-claude-tag
- **モデル退役ページに新規告知はない**。現行16行の Active は全て据え置きで、同ページは公開モデルの退役を最低60日前に通知すると明記している
  - 暫定退役日で最も近いのは `claude-sonnet-4-5-20250929` の 9/29 以降、次いで `claude-haiku-4-5-20251001` の 10/15 以降、`claude-opus-4-5-20251101` の 11/24 以降である。⚠️ いずれも「not sooner than」で確定日ではない
  - 同ページの日付は Anthropic 運営（Claude API / Claude Platform on AWS / Microsoft Foundry）にのみ適用され、**Amazon Bedrock と Google Cloud は独自スケジュール**である旨が明記されている
- **Claude Platform / Claude Apps のリリースノートは更新がない**。Platform 側の最上位は 8/27 のまま（SDK 6言語のベータヘッダー廃止・Console の個人キーとサービスアカウントキー。いずれも 08-29 収録済み）で、日付列は 8/27 → 8/26 → 8/20 → 8/19 と連続しており欠落は起きていない。`support.claude.com` Release Notes も 8/25 の memory 更新が最上位のまま5日間動いていない
- **8/29 付けの Anthropic の新規発表を検出できなかった**。規定5本に加えて日付入り1本を実行し、8/26〜8/28 の既報（Claudeforce・国防総省訴訟の判決・Model Hardware Standard・Claude for Teachers）以外は出ていない
- ⚠️ **8月 Risk Report は14日連続で一次未読が続いている**（初出 08-17）。本日の二次でも misalignment の very low → low 引き上げと、その理由が「新たな失敗ではなくサイバー評価インシデントを受けた不確実性の高まり」である点は 08-29 の記載から変わっていない
- **AWS Bedrock の Anthropic モデル追加は 7/24 の Claude Opus 5 が最新のまま**で、8月の新規提供開始を検出できなかった

### GitHub Copilot / 開発ツール

- **Copilot CLI の Rust ランタイム化と VS Code 1.135 はハイライト3参照**
- **Copilot CLI に 8/29 の新規リリースはない**。最新は pre-release `v1.0.82-1`（8/28 17:28・認証失敗時に `401 Bad credentials` 等の具体的理由を表示）で、**安定版は 8/27 の `v1.0.81` のまま**据え置きである。`github.blog/changelog` の Copilot ラベルも 8/28 の3本が最上位のまま動いていない
- **Cursor changelog は 8/27 の「Start from scratch, without a repo」が最上位のまま**で 8/28〜8/29 の追加がない（RSS 200 / item 取得済み）。フォーラム Announcements は 8/17 の Origin Code Hosting から13日間動いていない
- **Devin は一次に到達できない状態が続いている**。`docs.devin.ai` のゲートウェイ拒否が継続しており、二次が挙げる項目（Devin Coach の入力欄サジェスト、差分不変な PR の再レビュー省略、Slack スレッドの購読と返信ルーティング、nested `AGENTS.md` と小文字 `agents.md` の探索）は公開日を特定できず既報との切り分けができないため新着扱いしていない
- **`devblogs.microsoft.com/commandline` は 8/25 の PowerToys 0.101 が最上位のまま**動いていない。Intelligent Terminal は 8/10 の 0.2 が最新である

### OpenAI / Codex / ChatGPT

- **Codex CLI 安定版 `0.151.0` はハイライト2参照**。次系列の `rust-v0.152.0-alpha.1`（8/29 10:47 UTC）も出ているが、本文は `Release 0.152.0-alpha.1` の1行のみで内容は未確定である
- **ChatGPT & Codex changelog で本日5件を新たに確定した**（`learn.chatgpt.com` はゲートウェイ拒否のため WebSearch 経由・一次未読）
  - スレッドの共有スナップショット: macOS デスクトップアプリからローカル Codex スレッドを読み取り専用スナップショットとして共有できる。スナップショットは元スレッドが変わっても更新されない。⚠️ **個人アカウントのリンクは**リンクを知る全員が開ける（ワークスペースアカウントのリンクは発行元ワークスペースのメンバーに限定）。確認と失効は ChatGPT のデータ制御「Shared links」から行う
  - ピン留めスレッドの統一: デスクトップアプリと iOS で同じピン留めチャットを共有する
  - Site の URL 変更: Plus / Pro の Site オーナーが再デプロイなしで URL を変更でき、旧アドレスは新アドレスへリダイレクトされる
  - Computer History の対象地域が EEA・スイス・英国へ拡大した
  - 複数 Google アカウントの併用: Gmail / Calendar / Contacts で複数アカウントを1つの会話に接続できる
  - Codex 側にはポータブルな Agent Plugins、会話セクションの永続化、承認の自動化、**MCP 2026-07-28 の opt-in 対応**が入った
- **ChatGPT Enterprise / Edu が長文ペーストを添付へ自動変換するようになった**（8/28 から）。コンポーザーへ **1万文字**を超える内容を貼り付けると、本文へ挿入する代わりに添付ファイルへ変換される。長文ペーストが文脈枠を使い切る事象を避ける狙いである。⚠️ 一次 `help.openai.com` はオリジン403で本文に到達できず二次スニペットによる
- **ChatGPT の公式 DALL·E GPT が本日 8/30 に終了する**。終了するのは GPT という面であって画像生成機能そのものではなく、利用者は ChatGPT Images へ集約される。自作の画像生成付きカスタム GPT は影響を受けない。⚠️ 当該 GPT 経由で保存した画像は事前のダウンロードが必要とされる。API 側の `dall-e-2` / `dall-e-3` は 2026-05-12 に削除済みで、本件は消費者向け面の後追いにあたる
- **GPT-5.6 の単価は6日連続で据え置きになっている**。1M トークンあたり Sol は入力 $4・キャッシュ $0.40・キャッシュ書込 $5.00・出力 $20（長文脈側 $8／$0.80／$10／$30）、Terra は $2／$0.20／$2.50／$12、Luna は $0.20／$0.02／$0.25／$1.20 である。Batch と Flex は標準単価の50%引き、Fast モードは倍額という構成も不変で、**Sol の期間限定価格**は「少なくとも 2026-11-21 まで」の記載が変わっていない
- **退役期限8件は6日連続で変更がない**。撤回・延期・新規追加のいずれも無いことを一次で確認した。次の期限は 9/24（Videos API と Sora 2 系）で残り25日である
- `developers.openai.com/api/docs/changelog` は 8/21 の2件が最上位のままで9日間追加がない。`community.openai.com` Announcements RSS も 8/25 の WebMCP 2本のままである

### Microsoft 365 Copilot / Copilot Studio / Power Platform

- **Teams 管理センターから、導入済みサードパーティアプリに対応するエージェントを発見・有効化できるようになる** — Release Communications の RSS に 8/28 起票で **569608**「Microsoft Teams: Enable agents for existing applications in your organization」が現れた。状態は `In development`、GA 期日は 2026年10月で Preview 期日の記載はない。全 digest を grep して掲載歴がゼロであることを確認した
  - 発見と有効化を Teams 管理センターの中で完結させる。対象は組織で既に使われているサードパーティアプリに対応するエージェントである
  - 管理者は価値の高いエージェントの推奨を受け取る。候補を自力で棚卸しする前提ではない
  - 有効化のワークフローの中で、必要になる構成変更が可視化される
  - ⚠️ **現時点の一次はこの Roadmap 項目だけ**で、Learn にも Release Notes にも Message Center にも対応する記載はない。ライセンス条件・対象クラウド・「推奨」の母集団はいずれも本項目に書かれていない
  - https://www.microsoft.com/microsoft-365/roadmap?id=569608
- **Release Wave の8月コミット10件が未達のまま確定する** — 3ページは `updated_at` 2026-08-27T17:04Z・同一の `git_commit_id`（`b92ae441`）で 8/28 から動いておらず、8月期日の行は再ビルド後も1件も緑チェックを得ていない。期日最終日は 8/31 である
  - power-automate 5件: ライセンスダッシュボードの改善〔GA〕、デスクトップフローの直接スケジュール〔PP〕、デスクトップフローのフローチャート表示〔PP〕、オブジェクト中心プロセスマイニングの Fabric エクスポート〔GA〕、正規化スキーマインポート〔GA〕
  - power-apps 1件: キャンバスアプリのオンラインモードで Dataverse へアクセス〔PP〕
  - ガバナンス2件: GitHub によるソースコード統合〔PP〕、PPAC の Usage ページ〔GA・Public preview は 2026-02-13 に緑チェック済み〕
  - Roadmap 側2件: **566997**（メーカー資格情報の使用ブロック・GA 期日 August CY2026）と、`In development` のまま超過が2か月を超えた **562221**（ワークフローでの MCP 準拠ツール・GA 期日 2026年6月）
  - ⚠️ **この未達の判定根拠そのものが 11/15 に消える**。Release Wave は 2026年9月に新規掲載を停止し、Release Planner は 11/15 に退役するため、緑チェックの差分監視で GA を検知する現在の運用は年内に成立しなくなる
  - https://learn.microsoft.com/en-us/power-platform/release-plan/2026wave1/power-automate/planned-features
- **Copilot Studio の What's New は July 2026 節が最新のまま**で、8月節が作成されていない。July 節6項目・June 節10項目とも増減はなく、`updated_at` も 2026-08-20T19:04Z から動いていない。⚠️ **June 節の GitHub Copilot ハーネス**は本日も `(Production-ready preview)` の表記のままで、GA（8/3）から27日連続の未反映である
- **Copilot Studio のビルドは 2026.6.3（6/30 初出）から動かず、空白が8週間を超えた**。リージョン分布（11 / 5 / 3 の3段）と UX 版 26.06.21-24 も据え置きで、次回の定例更新日は 9/1 である
- ⚠️ **ガイダンスハブの索引表記が記事の `<title>` と一致しない**。索引のリンク表記「Prevent duplicate messages with context-aware design」に対し、当該ページの `<title>` は「Context distribution in the standard harness」で、記事名での掲載歴チェックは索引側の表記では空振りする。索引の `updated_at` は 8/28 中に再ビルドで動いたが新規記事は増えていない
- **M365 Copilot Release Notes は August 25, 2026 バッチが最新のまま**で、10節・全19項目に増減はない。Cowork What's New の August 2026 節（ローカルブラウザーの GA・プラグインのワークスペースファイル入力・イベント駆動タスク）も 8/29 から変化がない
- ⚠️ **Copilot Tuning は停止発効（8/20）から10日たっても一次に停止も退役も書かれていない**。`copilot-tuning-overview` の `updated_at` は 2026-08-18T17:48Z から動かず、退役したはずの Optimization エージェントを現行機能として載せたままである
- **Purview の What's New は 8月節に増減がない**（Sensitivity labels 2件 + Data Loss Prevention 2件）。⚠️ 8/23 に Roadmap で検知した 569612（Copilot メモリの Purview 保持・GA 2026年9月）は本日も Purview 側に未掲載である
- **Copilot Agent Kit に新規リリースはない**（本日が週次確認日）。最新は 8/17 の「August 2026 Update 1」のままで、⚠️ 同エントリの `updated` だけが 8/26 へ動いており、`updated` の降順で先頭を見ると新規リリースと誤読する
- ⚠️ **`mc.merill.net` は23日連続 `EGRESS_BLOCKED`** で、Message Center 本文の一次確認は本日も不成立である。`pnp.github.io` と `www.ppweekly.com` も接続そのものが塞がれている
- ⚠️ **英語圏の「8月の新機能」系記事は8例目の空振りだった**。Excel のテーマデザインスキルと AutoSave 無効ブックでの Copilot 利用は Release Notes の全バッチに存在せず、ブランドキットは July 15 バッチ由来、Excel の Power BI グラウンディングは April 7 / May 5 / January 27 の3バッチにしか現れない。いずれも 7/31 付の Tech Community 月次記事が7月の機能として挙げたものである

### Google

- **Google Cloud が Gemini Enterprise の法務版と金融版を preview で公開した**（8/25）。Gemini Enterprise としては初の業種別パッケージで、医療・ライフサイエンス版も予告されている。業種特化 AI の流通経路が個別 SI 契約からベンダーの既製パッケージへ移る動きにあたる
  - 法務版のスキル: 契約レビューとレッドライン・プレイブック作成・規制の地平線スキャン・法務調査・DSAR 対応・封印申立て向けの文書墨消し・NDA 起草
  - 法務版の接続先: iManage・NetDocuments・Docusign・Everlaw・RelativityOne・Thomson Reuters HighQ・CourtListener・Harvey・Legora ほか。Deloitte の契約要約／レッドラインエージェントと Eudia Knowledge のエージェントが同梱される
  - 法務版のローンチ事務所: Cleary Gottlieb・Freshfields・Weil・Williams & Connolly
  - 金融版: Financial Research エージェントに **50超のスキル**を同梱し、信頼度スコア・手法の明示・監査用のデータスナップショット・出典引用で説明可能性を担保する。**16のコネクタ**（FactSet・LSEG・Moody's・MSCI・PitchBook・S&P Global・SEC EDGAR ほか）を持ち、設計パートナーは Deutsche Bank と CME Group で、当初は資本市場と法人銀行業務が対象である
  - ⚠️ **料金は両版とも未公表**で、工数削減率や ROI といった定量値も告知に無い
  - https://cloud.google.com/blog/products/ai-machine-learning/introducing-gemini-enterprise-for-legal
  - https://cloud.google.com/blog/products/ai-machine-learning/introducing-gemini-enterprise-for-financial-services
- **Gemini アプリがインタラクティブな可視化の生成に対応し、8/26 からロールアウトが始まっていた**（本日初検出）。従来は文章と静的な図が中心だった応答に、表・グリッド・シミュレーションを質問に合わせて生成して差し込む。3D 構造を回転・ズームして確認する形の応答が例に挙がっている。Rapid / Scheduled の両ドメインが対象で、機能が見えるまで最大15日かかる。⚠️ 一次はゲートウェイ拒否で二次一致である
- **Google Meet のハードウェアタッチコントローラから「Take notes for me」を操作できるようになる**（8/31 ロールアウト開始）。会議室内の参加者が Companion モードに入らずに Gemini のメモ取りを開始・停止・管理できる。⚠️ 同じく二次一致である
- **Gemini API changelog は 8/27 の Gemini Omni Flash GA が最上位のまま**で 8/28〜8/29 の追加がない。`gemini-omni-1.1-flash` は video extension・画像間の interpolation・4K までの `resolution` 指定に対応し、**旧 `gemini-omni-flash-preview` は 9/30 廃止**である
- **Gemini API 料金は更新日も含めて完全に据え置きになっている**（一次の最終更新は 8/28 UTC）。3.7 Flash / 3.6 Flash は入力 $0.75・出力 $3.75（2026-12-31 まで。2027-01-01 から $1.50／$7.50）、3.5 Flash $1.50／$9.00、3.5 Flash-Lite $0.30／$2.50、3.1 Pro Preview $2.00／$12.00、2.5 Pro $1.25／$10.00 で変化はない
- **Gemini 3.5 Transcribe の分あたり単価が一次料金表で確定している**（08-27 収録の続報）。非ストリーミング版は入力 $2.00／出力 $12.00 per 1M トークン・音声換算で入力 $0.003/分、ストリーミング版は入力 $3.50／出力 $21.00・音声換算で入力 $0.005/分である。⚠️ **提供区分が一次と二次で食い違う**（一次のモデル一覧は Stable、二次報道は public preview）ため、一次優先で Stable として扱いつつ差を記録する
- HF `google` org は `timesfm-3.0-pytorch`（作成 8/24 / 更新 8/28 15:16 UTC / DL 0 / likes 14）が最新で、8/19 の TIPS v1 6本は据え置きである。**Gemini 3.5 Pro GA は未ローンチが継続**している

### オープンウェイト / MCP

- **8/29〜8/30 に新規公開されたオープンウェイト LLM はない**。8 org（`Qwen` / `moonshotai` / `deepseek-ai` / `meta-models` / `mistralai` / `zai-org` / `openai` / `google`）を `createdAt` 降順と `lastModified` 降順の両方で確認した。`zai-org/GLM-5.3` は 8/29 09:51 UTC に更新されたが公開状態は変わっていない（`private: false` / `gated: false` / ファイル154件）
- **HF の `downloads` が 08-29 に同値だったのは集計の未反映だったことが確定した**。8/30 04:20 JST の実測では7リポジトリすべてが大きく増えている
  - `Qwen/Qwen3.8-27B-FP8` 4,606,343（likes 720）／`Qwen/Qwen3.8-27B` 4,028,839（likes 13,235）
  - `DeepSeek-V4-Flash-0731` 4,330,482（likes 3,803）／`DeepSeek-V4-Pro-0813` 111,121（likes 781）
  - `Qwen3.8-Flash-Next` 52,341（likes 4,265）／`Qwen3.8-Flash-Next-FP8` 44,281（likes 154）
  - `GLM-5.3-Flash` 189,793（likes 1,601）／`GLM-5.3` 8,804（likes 1,252）
  - ⚠️ **日次バッチの反映待ちを「伸びが止まった」と読んではいけない**という根拠が、実測2点で揃った
- **MCP 仕様 2026-07-28 の実装側の取り込みが本日2件進んだ**。Codex CLI `0.151.0` が MCP ツール検出の猶予期間と拡張によるツール結果の検査・置換を追加し、ChatGPT / Codex 側は同仕様への opt-in 対応を入れた。8/27 の Copilot CLI `v1.0.81` に続く動きで、**仕様公開から約1ヶ月**で主要3クライアントが揃ったことになる
- `blog.modelcontextprotocol.io` は 8/22 の「The New MCP Roadmap」が最上位のまま新規がない。A2A の AAIF 参加は一次3ホストのゲートウェイ拒否が継続し、本日も裏取り材料が出ていない
- **xAI の新規発表を検出できなかった**。Grok 5 は未リリースが継続し、8/12 の Grok 4.6（context 50万トークン・reasoning effort 4段）と 8/26 の Microsoft Foundry Models への public preview 提供から進展がない。一次3ホストは到達不可が継続している

### 規制・訴訟 / 企業動向

- **連邦地裁が国防総省による Anthropic の supply chain risk 指定を違憲として恒久的に差し止めた**（08-29 収録の続報として、判断内容の詳細が確定した）。カリフォルニア州北部地区連邦地裁の Rita Lin 判事が 8/27 夜に **59ページ**の判断を出している
  - 認定: 国防総省の指定は、Anthropic が自社モデルの軍事利用に条件を付けその立場を公にしたことへの報復であり、修正第1条（表現に対する報復）と修正第5条（適正手続）に違反する
  - 命令: `§3252` に基づく指定を取り消し、防衛関連事業者に Anthropic との取引を禁じた長官指示を含め、当該権限で出した指示をすべて撤回するよう政府に命じた
  - 経緯: 2025年7月締結の $200M 契約をめぐり、Anthropic が自律型致死兵器と国内大規模監視への利用を契約で禁じるよう求めて国防総省が拒否した。交渉決裂後、本来は外国事業者向けの区分が同社へ適用された。2026年3月には同じ判事が仮処分を出している
  - ⚠️ **確定していない**。政府は争う見込みで、Anthropic は民生分野の政府調達に関わる別の指定をめぐる訴訟をワシントン DC の連邦控訴裁でも継続している。一次の裁判所文書と主要二次6件はいずれもゲートウェイ拒否で、内容は検索スニペットの突き合わせによる
  - https://www.npr.org/2026/08/28/nx-s1-5947761/judge-pentagon-anthropic-illegal
- **Claude for Teachers が米国 K-12 の学校・学区向けに無償の Enterprise 提供として開放された**（08-29 収録）。**2027-06-30** までに申し込んだ組織は1年間無償で、超過課金は管理者が明示的に有効化しない限り既定で無効である。学区単位で FERPA に沿う条項と K-12 向けデータ処理契約が用意され、データはモデル学習に使われない。デトロイト市公立学校が 2026年秋にパイロットを開始する
- **Microsoft Partner Center の8月分に AI 関連の新規告知はない**。8/25〜8/27 の3件（Eligibility Dashboard・Partner Compliance Readiness 研修・成長マージンと API の更新）はいずれもパートナープログラムの事務手続である
- **Apple の AI 関連の最新は依然 8/5 の App Store creative assets** で25日間新規がない。`developer.apple.com` の最上位は 8/27 の税・価格更新記事のままである

### 市場データ・調査

- **ガイドラインを整備した企業でもシャドーAI 利用率は 46.9% で下がっていない** — 角川アスキー総研の国内調査（『AI白書2026』8/20 発売掲載）による。標本は上場企業または従業員300人以上の非上場企業に勤める経営者・役員および従業員 **310人**で、インターネットアンケート方式である
  - シャドーAI（会社公認でない AI ツールの業務利用）は課長以上の管理職が 46.5%、係長以下の一般社員が 38.1% で、管理職のほうが 8.4ポイント高い
  - 「ルールやガイドラインが現場の実態に追いついていない」と答えた割合も管理職 57.4%・一般社員 47.1% で、管理職側が10ポイント以上高い
  - AI 投資を「増やす」と見込む企業と「横ばい」の企業のいずれも、間接部門の人員が「減少する」と見込む割合は約 14% で差がない。AI 投資の拡大が人員削減に直結する構図は確認されていない
  - ⚠️ **一次に未到達**（`prtimes.jp` と `group.kadokawa.co.jp` がゲートウェイ拒否）で、数値は複数の二次スニペットの一致による。ガイドライン未整備企業の利用率という比較対象は二次に載っておらず確定できていない
  - https://www.jiji.com/jc/article?k=000000264.000017610&g=prt
- **市場データ定点に更新はない**。IDC・MM総研・NRC・Similarweb のいずれも新規公表を検知できなかった。参照可能な最新値は IDC の国内AI市場予測（2025年 2兆3,725億円 → 2029年 6兆8,897億円・CAGR 36.0%、2026年3月公表）と MM総研の個人利用経験率 21.8%（2025年8月時点）である

## 直近の注目予定

- **8/31（明日・7件が重なる）**: Claude Code の週次上限50%増が終了 ／ GitHub Spark の既存ユーザーアクセス終了 ／ GPT-5.4・5.4 mini が Codex（ChatGPT サインイン）から除外 ／ `gemini-robotics-er-1.6-preview` 停止 ／ Claude for Government の $1/機関プログラム終了 ／ Power Automate モバイルアプリの廃止発効 ／ Release Wave の8月期日10件が未達で確定。あわせて CSP Copilot Partner Council コンテストの応募期限、Google Meet ハードウェア制御のロールアウト開始、週次確認（ppweekly / MS-4005 / 課金レート表）
- **8月末**: Anthropic が IPO を公開申請する可能性（Bloomberg 報道）
- **9/1**: Copilot Business・Enterprise の新規シートが前払い必須に ／ GitHub Copilot の全体験でモデル廃止 ／ Copilot global model policy の全 enterprise 適用完了 ／ OpenAI Daybreak 全アカウントでハードウェアセキュリティキー必須化 ／ MAICPP 更新条項の自動発効 ／ Copilot Studio Released Versions の定例更新日
- **9/3**: Power Platform 非推奨一覧の週次確認
- **9/4**: WebMCP Challenge の提出締切 ／ 拡張機能 What's New とモデル可用性一覧の週次確認
- **9/9**: Apple 特別イベント（10:00 PT）／ GLM-5.3-Flash の Z.ai 経由50%割引が終了
- **9/10**: MAI-Code-1-Flash が全 Copilot 体験から廃止
- **9/17**: OpenAI DevDay Exchange の応募締切
- **9/21**: Anthropic ウェルビーイング研究助成の応募締切
- **9/23**: WebMCP Challenge の受賞発表
- **9/24**: OpenAI の Videos API と Sora 2 動画生成モデルが退役（代替モデルの提示なし）
- **9/28**: Copilot のチャット3面統合（これより前には実施しない）／ Copilot code review の既定 effort が Lite → Balanced ／ OpenAI の `gpt-3.5-turbo-instruct`・`babbage-002`・`davinci-002`・`gpt-3.5-turbo-1106` 退役
- **9/29 以降**: `claude-sonnet-4-5-20250929` の暫定退役日（確定日ではない）
- **9/30**: Gemini の旧 `gemini-omni-flash-preview` エンドポイント廃止
- **9 月**: iOS 27 / macOS 27 GA ／ Claudeforce のオープンベータ（二次情報）／ Release Plans on Learn の新規掲載停止と AI at Work roadmap への掲載開始 ／ 569612・569930・569607・569928 の GA ／ Copilot Tuning の Public Preview 再開 ／ App Store の Social Media 年齢レーティング回答が必須化 ／ OpenAI の IPO 観測
- **10/1**: Copilot Business・Enterprise の既存顧客が前払い必須に ／ Apple の EU 向け新ビジネス条件が発効（Core Technology Commission へ移行）／ Ask Gemini in Chat のプロモーション上限が終了 ／ CSP growth margins の本番提供開始
- **10/5**: Anthropic ウェルビーイング研究助成の full proposal 提出期限（採択者）
- **10/15 以降**: `claude-haiku-4-5-20251001` の暫定退役日（確定日ではない）
- **10/16–11/11**: OpenAI DevDay Exchange 8都市（**東京は 10/20**）
- **10/23**: OpenAI のレガシースナップショット退役（`gpt-3.5-turbo` / `gpt-4-0613` / `gpt-4-turbo` とファインチューン版、`o1` / `o1-pro` / `o3-mini`）
- **10 月**: Anthropic の IPO 予定（$2T 超の評価額を目標と報道）／ SPFx 1.24 GA と Copilot Components の GA・課金モデル確定 ／ 569608・569475・568937 の GA ／ 韓国 App Store のコンテンツ記述子2件が All → 12+
- **11/15**: Release Planner の退役
- **11/21**: GPT-5.6 Sol の暫定値下げが有効とされる期限
- **11/24 以降**: `claude-opus-4-5-20251101` の暫定退役日（確定日ではない）
- **11/30**: OpenAI の Evals・Agent Builder・`v1/prompts` 退役
- **12/1**: OpenAI の GPT Image 系退役
- **12/2**: EU AI Act の生成コンテンツ標識義務、8/2 以前に市場投入済みシステムへの猶予終了
- **12/11**: OpenAI の旧スナップショット退役（`gpt-5-2025-08-07` / `o3-2025-04-16` / `o3-pro-2025-06-10` 等）
- **12/31**: Gemini 3.7 Flash の導入価格終了（$0.75/$3.75 → $1.50/$7.50）
- **年内**: Anthropic の新データ保持方式（顧客自身のクラウドでの30日保持）投入予定と Bloomberg が報道 ／ OpenAI の Jalapeño チップの初期展開
- **2027-01-20**: OpenAI の audio / realtime / transcription 系退役（`gpt-realtime` / `gpt-audio` / `gpt-4o-audio` と mini 系）
- **2027-06-30**: Claude for Teachers の学区登録期限（この日までに登録すれば1年間無料）
- **2027年末**: Anthropic が借りる Nscale West Virginia データセンター（460MW）の稼働開始見込み
- **2028-06**: 米国 K-12 教職員向け ChatGPT for Teachers の無料提供期限

## 改善メモ

- 3ソースの当日分（01 Master / 02 Copilot / 03 industry）はいずれも取得できた。前日 08-29 分にも欠損記録はなく、欠損リカバリの対象はない
- **新規の改善提案は3件** — B-052（01）: GitHub Copilot Changelog の注目点に「weekly releases まとめエントリ」を明示し、IDE 側の変更経路として扱う ／ B-051（02）: ガイダンスハブの新規記事判定を索引ページの `updated_at` で行わない ／ B-029（03）: Google の一次ソース2件（`cloud.google.com/blog`・`ai.google.dev/gemini-api/docs/changelog`）を `daily-sources.md` へ登録
- **継続提案は3ソース計67件**（01: 32件・最多は B-013 の32回目、02: 24件・最多は B-011 の41回目、03: 11件・最多は B-004 の62回目）
- **ゲートウェイ拒否が8ドメイン新規に発生した**（03 側）: `group.kadokawa.co.jp` / `trends.codecamp.jp` / `www.axios.com` / `www.nbcnews.com` / `thehill.com` / `www.notus.org` / `storage.courtlistener.com` / `www.googlecloudpresscorner.com`。あわせて `www.anthropic.com` がオリジン403からゲートウェイ拒否へ分類変更された
- **`cloud.google.com` が WebFetch で初成功した**（03 側）。Gemini Enterprise 法務版・金融版の一次本文を取得できており、Google Cloud Blog を一次として扱える見込みが立った
- **同じ Claude Tag 記事を 01 と 03 が別の粒度で扱っている**。01 は所要時間3件（45分 / 26分 / 1日→30分）のみ、03 は各事例の作業内容と件数（24アカウント、約120件の指摘を23/14へ整理）まで拾っており、本サマリーは 03 側をベースにした。定量値の粒度差は今後も 03 側が細かい可能性が高い
- **Claude Code v2.1.251 の権限修正件数が 01 と 03 で食い違う**。01 は5件、03 は6件（Bash の算術式代入の自動承認を追加）で、03 側が本日新たに確定した1件を含む。本サマリーは6件を採った
- ⚠️ **8月 Risk Report の一次未読が14日連続**（01）、`mc.merill.net` の EGRESS_BLOCKED が23日連続（02）、Copilot Tuning 一次の未更新が10日連続（02）。いずれも解消の見込みが立っていない
