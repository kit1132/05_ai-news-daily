# AI News Daily Summary — 2026-08-31

月曜は、8月末の期限が実際に発効し、そのうち1件が期限そのものを取り下げた日である。本日発効したのは Power Automate モバイルアプリの廃止と、GitHub Spark・`gemini-robotics-er-1.6-preview`・Codex の GPT-5.4 系・Claude for Government $1 枠の4件で、前日まで5件目に数えていた Claude Code の週次上限だけが 9/13 へずれた。しかもその延長は増枠ではなく、9/14 から現行比17%減になる。供給側では OpenAI が SpaceX 傘下に入った Cursor へのモデル提供を 11/12 で打ち切ると通知し、ツールの選定条件に「親会社が誰か」が加わった。法務側では Sony と Warner Chappell の提訴で大手3社の出版部門が Anthropic と係争状態に入った。Power Platform は Release Wave の8月期日8件が緑チェックゼロで月を終え、期日超過分と合わせ13行が未達のまま9月へ入る。

## 今日のハイライト

### 1. Power Automate モバイルアプリの廃止が本日発効した — フローは成功したまま、通知だけが宛先を失う

**要点**: iOS / Android アプリの配布・更新・サポートが本日で終わった。前提が「アプリが消えるだけ」から「`Send me a mobile notification` を含むフローは成功のまま通知が届かなくなり、実行エラーの監視では検知できない」へ変わる。

**詳細**: 一次ページ `important-changes-coming` の先頭節が「Effective August 31, 2026, the Power Automate mobile app for iOS and Android is deprecated」と本日を発効日として明記している。ページの `updated_at` は **2026-08-14T01:04Z** から動かず、`## ` 見出しも90本で 8/27 の週次確認から増減がない。

- 本日以降に止まるもの
  - ストアからの配布・更新・サポートが終了する
  - `Send me a mobile notification` の届き先が失われる
  - iOS / Android のホーム画面ウィジェット（run a flow）が使えなくなる
- 止まらないもの: 既存のクラウドフロー（自動・スケジュール・インスタント）はすべて通常どおり実行され、アクション自体もフローデザイナーに残る
- 代替は用途別に3つが割り当てられている
  - 承認: Teams の Approvals アプリ
  - フローの表示・管理: モバイルブラウザーで開く Power Automate ポータル（`make.powerautomate.com`）
  - インスタントフローの実行: Power Apps mobile から呼び出す
- メーカー側の対応は `Send me a mobile notification` を Teams の `Post message in a chat or channel` かメール送信へ置き換えることである

⚠️ **アクションが残るためフローは失敗しない。** 実行履歴は成功のままで、受け取る側にだけ通知が届かなくなる。

- https://learn.microsoft.com/en-us/power-platform/important-changes-coming

### 2. Claude Code の週次上限が 9/13 まで延長され、9/14 から現行比17%減になる — 8月の消費実績で組んだ見積もりは引き直しになる

**要点**: 前日まで「本日 8/31 に失効」としていた50%増が 9/13 まで延び、9/14 に恒久 +25% へ移る。前提が「明日から枠が減る」から「2週間の猶予がつき、そのあと現行比で17%減る」へ変わる。

**詳細**: Anthropic が 8/29 に告知した。5/13 に始まった週次上限50%増は 8/31 期限のまま延長を重ねており、今回の告知で期限が 9/13 へ移った。9/14 からは **Pro / Max / Team / シート課金 Enterprise** で標準の週次上限を恒久的に25%引き上げる。ここまでは増枠の話だが、比較対象が違う。

- 元の標準枠を 100 とすると、現在は **150**（50%増）、9/14 以降は **125**（恒久 +25%）
- 促進前との比較では +25%、今日との比較では **-16.7%**。Anthropic 自身が「compared to today, this works out to a 17% reduction in weekly limits on Claude Code」と明記している
- Free プランと従量課金 Enterprise は対象外である。5時間枠の変更には言及がない
- Anthropic は最初の投稿を削除し、17%減を明記した形で投稿し直している

⚠️ **一次は `x.com` の @ClaudeDevs 投稿で、3ソースのいずれからも到達できていない**（`x.com` はゲートウェイ拒否）。数値・日付は BleepingComputer / Notebookcheck / MacObserver / ShiftDelete の二次一致で採っている。`support.claude.com` の利用上限ページ・`www.claude.com/pricing`・`claude.com/blog` のいずれにも本件の記載はなく、利用枠の変更が製品 changelog の外側でしか告知されない構図が再現している。

- https://x.com/ClaudeDevs/status/2093742321473065266
- https://www.bleepingcomputer.com/news/artificial-intelligence/anthropic-is-cutting-claude-codes-current-weekly-limits-by-17-percent/
- https://www.notebookcheck.net/Anthropic-announces-a-25-increase-to-Claude-Code-limits-but-there-s-a-17-catch.1382735.0.html

### 3. OpenAI が Cursor へのモデル提供を 11/12 で打ち切る — 供給が親会社の変更だけで切れる実例が出た

**要点**: OpenAI が 8/28 に change-of-control 条項を行使し、SpaceX 傘下に入った Cursor への提供終了を通知した。ツール選定の前提が「機能と価格で選ぶ」から「親会社が誰かでモデル供給が切れうる」へ変わる。

**詳細**: OpenAI が一次ページ「Our decision on Cursor following its acquisition by SpaceX」で公表した。

- 経緯: SpaceX は 6/16 に **$60B** の全株式交換で Cursor の親会社 Anysphere を買収すると発表し、8/14 に完了した。OpenAI はその2週間後の 8/28 に条項を行使し、SpaceX へ契約終了の意向を通知している
- 停止日: 遮断日は **2026-11-12** で、OpenAI は契約上の最大の予告期間を与えたとしている。移行猶予は約76日にあたる
- 理由: OpenAI は「Elon Musk の各社が契約に違反してきた経験」を挙げ、SpaceX が利用規約の範囲内で技術を使うと確信できないとした。契約の巻き取り中は今後の新モデルも Cursor へ提供しない
- 影響範囲: OpenAI モデルは Cursor の利用トラフィックの **約5%** にとどまり、Grok・Composer・Claude・Gemini は引き続き選べる。Cursor の有料開発者は100万人超とされる

⚠️ 一次の `openai.com` はオリジン403、`www.cnbc.com` ほか主要二次も本日ゲートウェイ拒否で、本文は検索スニペットの突き合わせによる。

- https://openai.com/index/our-decision-on-cursor-following-its-acquisition-by-spacex/
- https://www.cnbc.com/2026/08/29/openai-cursor-spacex-model-access.html
- https://forkast.news/openais-cursor-termination-turns-model-supply-into-a-competitive-weapon/

## カテゴリ別まとめ

### Anthropic / Claude

- **本日 8/31 で Claude for Government の $1/機関プログラムが終了する**。前日まで同日期限に数えていた Claude Code の週次上限はハイライト2のとおり 9/13 へずれたため、本日発効する Anthropic 側の期限はこの1件だけになった
- **Claude Code に 8/29〜8/30 の新規リリースはない**。changelog の最上位は `2.1.251`（8/28 15:34 UTC）のままで3日間動いておらず、npm の実 publish 記録とも一致する
- **npm `dist-tags` は15版差のまま据え置かれている** — 実測値は `{stable: 2.1.236, latest: 2.1.251, next: 2.1.251}`（8/31・curl）で、`next` == `latest` の収束は継続している。⚠️ v2.1.251 が塞いだ**承認範囲を破る欠陥6件**は stable 固定の組織へ依然届いておらず、未更新の環境では権限設定が想定どおり効いていない状態が続く
- **Claude Platform API のリリースノートは 8/27 が最上位のまま**で、8/28〜8/30 の追加がない。日付列は 8/27 → 8/26 → 8/20 → 8/19 → 8/18 と連続しており、隣接日付ブロックの欠落は起きていない。`support.claude.com` の Release Notes も 8/25 の memory 更新が最上位のまま6日間動いていない
- **モデル退役ページに新規告知はない**。現行16行の Active は全て据え置きである
  - 暫定退役日: `claude-sonnet-4-5-20250929` が 9/29 以降、`claude-haiku-4-5-20251001` が 10/15 以降、`claude-opus-4-5-20251101` が 11/24 以降。⚠️ いずれも「not sooner than」で確定日ではない
  - 同ページの日付は Anthropic 運営の3プラットフォーム（Claude API / Claude Platform on AWS / Microsoft Foundry）にのみ適用され、**Amazon Bedrock と Google Cloud は独自スケジュール**で動く
- **`claude.com/blog` は 8/28 の2本が最新のまま**で、8/29〜8/30 の追加がない。8/30 付けの新規発表も規定5本＋日付入り1本の検索で検出できなかった
- ⚠️ **8月 Risk Report は15日連続で一次未読である**（初出 08-17）。二次の内容は 08-30 の記載から変化していない
- **AWS Bedrock の Anthropic モデル追加は 7/24 の Claude Opus 5 が最新のまま**で、8月の新規提供開始を検出できなかった
- 既報: Claudeforce（Salesforce × Anthropic・8/26・一次未読）、Model Hardware Standard 研究プレビュー（8/27・一次未読）、ウェルビーイング研究助成 $5M（応募締切 9/21）、Claude for Teachers の米国 K-12 無料 Enterprise（登録期限 2027-06-30）

### GitHub Copilot / 開発ツール

- **本日 8/31 で GitHub Spark の既存ユーザーアクセスが github.com 上で終了する**（8/4 告知）
- **Copilot CLI が安定版 `v1.0.82` を出した**（8/29 23:39 UTC）。8/27 の `v1.0.81` から2日ぶりで、内容は3件にとどまる
  - `/worktree` / `/move` でワークツリー準備中に入力したメッセージが切り替えを中断しなくなった
  - Ctrl+E で計画承認カードを展開し、全文を読み直せるようになった
  - ログイン失敗時に `401 Bad credentials` など具体的な理由を表示するようになった（従来は `/login` プロンプトだけ）
  - ⚠️ この安定版は 8/29 の収録時点（19:20 UTC）より後の公開で、**取りこぼしではなく JST 実行による構造的な検出遅れ**にあたる。pre-release `v1.0.82-2`（8/29 19:59 UTC）も同様である
- **Zed が Delta を発表した**（8/17・本日初検出で14日遅れの捕捉）。エージェントと共同開発するためのマルチプレイヤー環境で、AI との対話履歴をコードの文脈として残す
  - 保存対象: チャット上の仕様とコードの議論、AI エージェントへの指示と出力、実際のコード変更を相互に関連付けて記録し、「なぜこのコードがこうなっているか」を後から文脈込みで辿れる
  - 基盤は `DeltaDB`（2025年に開発表明済みの記録機能）で、今回それを製品化した形にあたる
  - Claude Code などサードパーティ製のエージェントハーネスに接続でき、ターミナル上のセッションが Delta スレッドへリアルタイムに同期される
  - ⚠️ 料金・提供時期・オープンソース範囲は確認できた二次からは確定できていない
  - https://www.publickey1.jp/blog/26/zeddeltaai.html
- **`github.blog/changelog` の Copilot ラベルは 8/28 の3本が最上位のまま**で、8/29〜8/31 の追加が3日間ない
- **Cursor changelog は 8/27 の「Start from scratch, without a repo」が最上位のまま**で、8/28〜8/30 の追加がない（RSS 200 / item 取得済み）。フォーラム Announcements は 8/17 の Origin Code Hosting から14日間動いていない。OpenAI による供給打ち切りはハイライト3参照
- **Devin は一次に到達できない状態が続いている**。`docs.devin.ai` のゲートウェイ拒否が継続し、二次が挙げる項目（Devin Coach の入力欄サジェスト、差分不変な PR の再レビュー省略、Slack スレッドの購読と返信ルーティング、nested `AGENTS.md` の探索）は公開日を特定できず既報との切り分けができないため新着扱いにしていない
- **`devblogs.microsoft.com/commandline` は 8/25 の PowerToys 0.101 が最上位のまま**動いていない。Intelligent Terminal は 8/10 の 0.2 が最新である

### OpenAI / Codex / ChatGPT

- **本日 8/31 で GPT-5.4 / 5.4 mini が Codex（ChatGPT サインイン）から除外される**。API キー認証の Codex セッションと OpenAI API 側には残る。移行先は `gpt-5.4` → `gpt-5.6-terra`、`gpt-5.4-mini` → `gpt-5.6-luna` である。⚠️ ワークスペース既定・カスタムエージェント・スケジュールタスクを 5.4 系にピン留めしている場合はそれらも影響を受ける
- **ChatGPT / Codex changelog で本日2件を新たに確定した**（`learn.chatgpt.com` はゲートウェイ拒否・WebSearch 経由・一次未読）
  - Appshots: macOS の Codex アプリで Screen context を有効にすると、最前面ウィンドウのスクリーンショットと取得できたテキストをスレッドへ添付できる。トリガーは **Command キーの2度押し**で、Codex の設定から任意のホットキーに変更できる
  - スケジュールタスクのイベント起動: Gmail / Slack / GitHub で対応するイベントが起きたときにタスクを開始できるようになった（8/24〜8/28 の範囲で公開）。Codex は UTC の時刻リマインダーを受け取り、クライアント提供のクロック経由で現在時刻を直接照会できる
- **Codex CLI は安定版 `0.151.0`（8/29）が最新のまま**で、8/30 に pre-release `0.152.0-alpha.4`（13:56 UTC）が加わった。⚠️ 本文はビルドコミット `7ac2dff` の記載だけで変更内容が確定できない
- ⚠️ **`codex mcp-server` の deprecated 化に 8/24 という日付が二次で付いた**（移行先は Codex app server）。08-26 に「公開日を特定できず未確定」として保留した項目だが、一次未読の状態は変わらないので確定扱いにしていない
- **GPT-5.6 の単価は7日連続で据え置かれている**。1M トークンあたり Sol は入力 $4・キャッシュ $0.40・キャッシュ書込 $5.00・出力 $20（長文脈側 $8／$0.80／$10／$30）、Terra は $2／$0.20／$2.50／$12（長文脈側 $4／$0.40／$5／$18）、Luna は $0.20／$0.02／$0.25／$1.20（長文脈側 $0.40／$0.04／$0.50／$1.80）である。Batch と Flex は全モデルで標準単価の50%引き、Fast モードは倍額という構成も不変で、**Sol の期間限定価格**は「少なくとも 2026-11-21 まで」の記載が変わっていない
- **退役期限は7日連続で変更がない**。撤回・延期・新規追加のいずれも無いことを一次で確認した。次の期限は 9/24（Videos API と Sora 2 系）で**残り24日**である。08-24 収録の中間期限（10/31 に既存 evals が読み取り専用化）も変わっていない
- `developers.openai.com/api/docs/changelog` は 8/21 の2件が最上位のままで10日間追加がない。`community.openai.com` の Announcements RSS も 8/25 の WebMCP 2本のままである
- 到達性: `developers.openai.com` と `community.openai.com`(RSS) は 200。`openai.com` / `help.openai.com` は `curl` でオリジン403を再確認し、`learn.chatgpt.com` はゲートウェイ拒否が継続している

### Microsoft 365 Copilot / Copilot Studio / Power Platform

- **Power Automate モバイルアプリの廃止発効はハイライト1参照**
- **Release Wave の8月期日8件が緑チェックゼロで月を終えた** — 3ページは `updated_at` **2026-08-27T17:04Z**・同一の `git_commit_id`（`b92ae441`）で 8/28 から4日連続で再ビルドされていない。期日超過5行と合わせ13行が未達のまま9月へ入る
  - power-automate 5件: ライセンスダッシュボードの改善〔GA〕、デスクトップフローの直接スケジュール〔PP〕、デスクトップフローのフローチャート表示〔PP〕、オブジェクト中心プロセスマイニングの Fabric エクスポート〔GA〕、正規化スキーマインポート〔GA〕
  - power-apps 1件: キャンバスアプリのオンラインモードで Dataverse へアクセス〔PP〕
  - ガバナンス2件: GitHub によるソースコード統合〔PP〕、PPAC の Usage ページ〔GA・Public preview は 2026-02-13 に緑チェック済み〕
  - 期日超過のまま持ち越す5行: power-automate 2行（過去プロンプト参照〔GA・May〕/ 統合 Power Apps によるフォーム〔GA・Jul〕）、ガバナンス3行（Copilot Studio の秘密度ラベル表示〔GA・Jun〕/ コネクタの秘密度ラベル表示〔GA・Jun〕/ 環境へのゲストアクセス許可・拒否〔GA・May〕）
  - Roadmap 側2件も `In development` のまま動いていない: **566997**（メーカー資格情報の使用ブロック・GA 期日 August CY2026）と **562221**（ワークフローでの MCP 準拠ツール・GA 期日 2026年6月・超過3か月目）
  - 8月中に緑チェックが付いたのは power-apps の2行だけである（グリッド列の複数値フィルター、テーブルスコープによるグローバル検索の絞り込み。どちらも Public preview・8/7）。9月に期日がある行は3ページ計12件で、こちらは**掲載停止と期日が同じ月に重なる**
  - https://learn.microsoft.com/en-us/power-platform/release-plan/2026wave1/power-automate/planned-features
- **Copilot Studio の What's New は July 2026 節が最新のまま**で、8月節が作成されていない。July 節6項目・June 節10項目とも増減はなく、`updated_at` も 2026-08-20T19:04Z から動いていない。⚠️ June 節の GitHub Copilot ハーネスは本日も `(Production-ready preview)` の表記で、GA（8/3）から**28日連続の未反映**である
- **Copilot Studio のビルドは 2026.6.3（6/30 初出）から動かず、空白が62日に達した**。リージョン分布（11 / 5 / 3 の3段）と UX 版 26.06.21-24 も据え置きで、次回の定例更新日は明日 9/1 である
- **課金レート表の週次確認を本日実施し、消費レートに変化がないことを確認した**。クラシック回答 1 / 生成回答 2 / エージェントアクション 5 / テナントグラフグラウンディング 10、生成 AI ツールは10応答あたり basic 1 / standard 15 / premium 100、音声は1分あたりクラシック 10 / GenAI 35 / プレミアム GenAI 75 である。125% エンフォースメントと M365 Copilot ライセンスユーザーの B2E 無償（⚠️ **CUA は対象外**）も同一で、次回は 9/7
- **M365 Copilot Release Notes は August 25, 2026 バッチが最新のまま**で、10節・全19項目に増減はない。隔週傾向どおりなら次バッチは 9/8 前後になる
- ⚠️ **Copilot Tuning は停止発効（8/20）から11日たっても一次に停止も退役も書かれていない**。`copilot-tuning-overview` の `updated_at` は 2026-08-18T17:48Z から動かず、退役したはずの Optimization エージェントを「サポートされるシナリオ」節とテンプレート選択表の両方に現行機能として載せたままで、冒頭 Important も「Frontier 経由の提供は 2026年4月予定」で止まっている
- ⚠️ **Cowork What's New の登録 URL に誤りがあり、本日訂正した**。正しい URL は `learn.microsoft.com/microsoft-365/copilot/cowork/whats-new` で、状態ファイルが記録していた `microsoft-365-copilot/cowork/cowork-whats-new` は 404 を返す。August 2026 節（ローカルブラウザーの GA、プラグインのワークスペースファイル入力、イベント駆動タスク）の内容に変化はない
- **Purview の What's New は 8月節に増減がない**（Sensitivity labels 2件 + Data Loss Prevention 2件）。⚠️ 8/23 に Roadmap で検知した 569612（Copilot メモリの Purview 保持・GA 2026年9月）は本日も Purview 側に未掲載である
- ⚠️ **Release Communications RSS の `lastBuildDate` は鮮度判定に使えない**ことが確定した。HTTP 200・総項目数 **1,775** に対し、`lastBuildDate` は `Fri, 28 Aug 2026 21:59:29 Z` で3日連続動いていないのに、総項目数は前日記録の 1,779 から4件減っている。フィードの窓は入れ替わっているのにビルド日時が据え置かれる
- ⚠️ **既報エントリの `pubDate` が後から動く現象が SharePoint Blog でも起きた**。「What's New in Copilot in SharePoint: July 2026」（記事日 8/6）の board RSS 上の日付が 8/30 20:25Z へ動いていた。掲載済みのため実害はない
- ⚠️ **`mc.merill.net` は24日連続 `EGRESS_BLOCKED`** で、Message Center 本文の一次確認は本日も不成立である。`www.ppweekly.com` も週次確認日にあたる本日を含め4回連続でゲートウェイ拒否となり、夏季休刊が明けたかを確かめる手段がない
- ⚠️ **英語圏の「8月の新機能」系記事は9例目の空振りだった**。Excel のテーマデザインスキルと Power BI グラウンディングは Release Notes の August 25 / August 11 バッチに存在しない。日本語圏の「2026年8月に新しい UI とライセンス体系が発表」も対応する一次が見当たらず、8/30 に続いて採用していない
- **Microsoft Partner Center の8月分に新規告知はない**。`updated_at` は 2026-08-27T16:43Z で動かず、`## ` 見出しは22本のまま。先頭は 8/27 付の Eligibility Dashboard（8/28 掲載済み）である

### Google

- **本日 8/31 で `gemini-robotics-er-1.6-preview` のエンドポイントが停止する**。Gemini API 側の後継提示はない
- **Gemini API changelog は 8/27 の Gemini Omni Flash GA が最上位のまま**で、8/28〜8/31 の追加がない。日付列は 8/27 → 8/26 → 8/13 → 7/30 である
- **Gemini API 料金は更新日も含めて2日連続で据え置かれている**（一次の最終更新は 8/28 UTC）。3.7 Flash / 3.6 Flash は入力 $0.75・出力 $3.75（2026-12-31 まで。2027-01-01 から $1.50／$7.50）、3.5 Flash $1.50／$9.00、3.5 Flash-Lite $0.30／$2.50、3.1 Pro Preview $2.00／$12.00（20万トークン以下・超過時 $4.00／$18.00）、2.5 Pro $1.25／$10.00（同・超過時 $2.50／$15.00）で変化はない。08-30 に初収録した音声系も 3.5 Transcribe が $2.00／$12.00、3.5 Transcribe Live が $3.50／$21.00 で据え置きである
- **8/30 付けの Google の AI 発表を検出できなかった**。直近は 8/26 ロールアウト開始の Gemini アプリのインタラクティブ可視化と、本日 8/31 ロールアウト開始の Google Meet ハードウェアタッチコントローラからの「Take notes for me」操作で、いずれも既報である
- HF の `google` org は `timesfm-3.0-pytorch`（作成 8/24 / DL 0 / likes 17 / **`gated: manual`**）が最新のまま。8/19 の TIPS v1 6本も据え置きである。**Gemini 3.5 Pro GA は未ローンチが継続**している
- 登録済み Google 系5ソースはゲートウェイ拒否が継続し、`ai.google.dev`（`changelog.md.txt`）だけが到達できる Google 一次である

### オープンウェイト / MCP / xAI

- **8/30〜8/31 に新規公開されたオープンウェイト LLM はない**。8 org（`Qwen` / `moonshotai` / `deepseek-ai` / `meta-models` / `mistralai` / `zai-org` / `openai` / `google`）を `createdAt` 降順と `lastModified` 降順の両方で確認した
  - 作成日で最も新しいのは `zai-org` の GLM-5.3 系4本（8/24）と `Qwen/Qwen3.8-Flash-Next` 系2本（8/24）で、いずれも既報である。`lastModified` 降順でも最新は `zai-org/GLM-5.3` の 8/29 09:51 UTC である
  - 4 org（`moonshotai` / `mistralai` / `meta-models` / `openai`）に新規はない（最新はそれぞれ 6/13 の Kimi-K3、7/16 の Shieldstral-1.0-3B、8/10 の Muse-Glimmer-30B-ExecuTorch-PTE、4/17 の privacy-filter）
- **HF の `downloads` 実測（8/31 04:10 JST）** — ⚠️ 前日比は書かない運用に変わっている
  - `Qwen/Qwen3.8-27B-FP8` 5,129,402（likes 727）／`Qwen/Qwen3.8-27B` 4,511,348（likes 13,327）
  - `DeepSeek-V4-Flash-0731` 4,575,518（likes 3,819）／`DeepSeek-V4-Pro-0813` 127,009（likes 785）
  - `Qwen3.8-Flash-Next` 121,976（likes 4,368）／`GLM-5.3-Flash` 346,516（likes 1,692）／`GLM-5.3` 50,116（likes 1,331）
  - 追跡7リポジトリは全て `private: false` / `gated: false` で、公開状態に変化はない
- **`blog.modelcontextprotocol.io` は 8/22 の「The New MCP Roadmap」が最上位のまま**で9日間新規がない。仕様 2026-07-28 の実装側取り込みは 8/29 の Codex CLI `0.151.0` と ChatGPT / Codex 側の opt-in で3クライアントが揃っており、本日の追加はない
- **A2A（Agent2Agent）の AAIF 参加は未確定のままである**。一次3ホスト（`aaif.io` / `www.linuxfoundation.org` / `developers.googleblog.com`）のゲートウェイ拒否が継続し、新規の裏取り材料が出ていない
- **xAI の新規発表を検出できなかった**。**Grok 5 は未リリースが継続**し、8/12 の Grok 4.6（context 50万トークン・reasoning effort 4段）と 8/26 の Microsoft Foundry Models への public preview 提供から進展がない。一次3ホスト（`x.ai` / `docs.x.ai` / `grok.com`）は到達不可が続く

### 規制・訴訟 / 企業動向

- **Sony Music Publishing と Warner Chappell Music が Anthropic を提訴し、大手3社の出版部門が出揃った**（8/28・カリフォルニア州北部地区連邦地裁）。被告には法人のほか **Dario Amodei と Benjamin Mann** の2名が個人として名指しされている
  - 訴えの内容: Claude の学習のために著作物を大規模に不正取得（torrent・スクレイピング・ダウンロード）し、著作権管理情報を除去したというものである
  - 請求: 故意侵害1作品あたり最大 **$150,000** の法定損害賠償と、侵害複製物の廃棄・Claude の学習データの開示・陪審審理。対象曲には「Eye of the Tiger」「Ain't No Mountain High Enough」「Paper Rings」等が挙がる
  - 係争の全体像: Universal（2023年10月・2026年1月に $3B 超の第2訴訟）、BMG（2026年3月）、Round Hill Music（2026-08-17）に続く提訴で、大手3社すべての出版部門が Anthropic と係争状態に入った
  - ⚠️ **提訴段階であり判断は出ていない**。2025年6月の Bartz 判決は学習利用そのものを fair use としつつ海賊版の取得を争点として残し、後に **$1.5B** の和解で決着している
  - https://techcrunch.com/2026/08/29/sony-music-warner-sue-anthropic-alleging-a-brazen-campaign-of-intellectual-property-theft/
- **OpenAI Daybreak のハードウェアキー必須が明日 9/1 に到来する**。Daybreak Blue / Red の全個人アカウントが対象で、攻撃側向けの Red だけでなく防御側向けの Blue も含まれる。⚠️ 08-13 に挙げた宿題である「Amazon Bedrock 経由の利用にも同要件が掛かるか」は本日時点でも一次・二次のいずれでも明示を確認できておらず、Bedrock 経由（US East バージニア北部のみ・`bedrock-mantle` エンドポイント）の構成は明日以降アクセスが止まる可能性を前提に確認しておく必要がある
- **Apple の AI 関連の最新は依然 6/11 の ImageCreator クラス廃止告知である**。`developer.apple.com` の最上位は 8/27 の税・価格更新記事のままで動いていない。⚠️ **01 と 03 で「AI 関連の最新」の起点が食い違う**（01 は 6/11、08-30 の 03 系記載は 8/5 の App Store creative assets）ため、改善メモに記録する
  - 既報: 8/26 の特別イベント告知（**9/9 10:00 PT**）、8/24 Sign in with Apple の新ドメイン（`private.icloud.com`）、8/18 の EU 向けビジネス条件変更2本（発効 2026-10-01）、8/12 韓国 GRAC レーティング（2026年10月に2記述子が All → 12+）

### 市場データ・調査

- **市場データ定点に更新はない**。IDC・MM総研・NRC・Similarweb のいずれも新規公表を検知できなかった。参照可能な最新値は IDC の国内AI市場予測（2025年 2兆3,725億円 → 2029年 6兆8,897億円・CAGR 36.0%、2026年3月公表）と MM総研の個人利用経験率 21.8%（2025年8月時点）で、いずれも既収録から不変である。国内の統制系データは 08-30 収録の『AI白書2026』が最新のままである

## 直近の注目予定

- **8/31（本日・4件が発効）**: GitHub Spark の既存ユーザーアクセス終了 ／ `gemini-robotics-er-1.6-preview` 停止 ／ GPT-5.4・5.4 mini が Codex（ChatGPT サインイン）から除外 ／ Claude for Government の $1/機関プログラム終了。あわせて Power Automate モバイルアプリの廃止発効、Release Wave の8月期日8件が未達で確定、Google Meet ハードウェア制御のロールアウト開始、週次確認（ppweekly / MS-4005 / 課金レート表）
- **8月末**: Anthropic が IPO を公開申請する可能性（Bloomberg 報道）
- **9/1**: Copilot Business・Enterprise の新規シートが前払い必須に ／ GitHub Copilot の全体験でモデル廃止 ／ Copilot global model policy の全 enterprise 適用完了 ／ OpenAI Daybreak 全アカウントでハードウェアセキュリティキー必須化 ／ MAICPP 更新条項の自動発効 ／ Copilot Studio Released Versions の定例更新日 ／ ハーネス課金ドキュメントの週次確認
- **9/3**: Power Platform 非推奨一覧の週次確認
- **9/4**: WebMCP Challenge の提出締切 ／ 拡張機能 What's New とモデル可用性一覧の週次確認
- **9/6**: Power CAT の週次確認 ／ **9/7**: ppweekly・MS-4005・課金レート表の週次確認
- **9/8 前後**: M365 Copilot Release Notes の次バッチ（隔週傾向）
- **9/9**: Apple 特別イベント（10:00 PT）／ GLM-5.3-Flash の Z.ai 経由50%割引が終了
- **9/10**: MAI-Code-1-Flash が全 Copilot 体験から廃止
- **9/13**: **Claude Code の週次上限50%増が終了**（8/31 から延長・ハイライト2参照）
- **9/14**: **Claude Code の標準週次上限が恒久的に +25%**（Pro / Max / Team / シート課金 Enterprise。現行比では17%減）
- **9/17**: OpenAI DevDay Exchange の応募締切
- **9/21**: Anthropic ウェルビーイング研究助成の応募締切
- **9/23**: WebMCP Challenge の受賞発表
- **9/24**: OpenAI の Videos API と Sora 2 動画生成モデルが退役（代替モデルの提示なし）
- **9/28**: Copilot のチャット3面統合（これより前には実施しない）／ Copilot code review の既定 effort が Lite → Balanced ／ チャットのデータ保持が28日からアカウント存続期間へ ／ OpenAI の `gpt-3.5-turbo-instruct`・`babbage-002`・`davinci-002`・`gpt-3.5-turbo-1106` 退役
- **9/29 以降**: `claude-sonnet-4-5-20250929` の暫定退役日（確定日ではない）
- **9/30**: Gemini の旧 `gemini-omni-flash-preview` エンドポイント廃止 ／ M365 E7 プロモーションの対象購入最終日 ／ M365 E5・E3 の CSP 割引終了 ／ 2026 Wave 1 の対象期間終了
- **9 月**: iOS 27 / macOS 27 GA ／ Claudeforce のオープンベータ（二次情報）／ Release Plans on Learn の新規掲載停止と AI at Work roadmap への掲載開始 ／ Copilot Tuning の Public Preview 再開 ／ 569612・569930・569607・569928 の GA と 569475 の Preview ／ Release Wave の9月期日12件 ／ Copilot デスクトップアプリの広範展開（中旬）／ App Store の Social Media 年齢レーティング回答が必須化 ／ OpenAI の IPO 観測
- **10/1**: Copilot Business・Enterprise の既存顧客が前払い必須に ／ Apple の EU 向け新ビジネス条件が発効（Core Technology Commission へ移行）／ Ask Gemini in Chat のプロモーション上限が終了 ／ CSP software 価格改定の発効
- **10/5**: Anthropic ウェルビーイング研究助成の full proposal 提出期限（採択者）
- **10/15 以降**: `claude-haiku-4-5-20251001` の暫定退役日（確定日ではない）
- **10/16–11/11**: OpenAI DevDay Exchange 8都市（**東京は 10/20**）
- **10/23**: OpenAI のレガシースナップショット退役（`gpt-3.5-turbo` / `gpt-4-0613` / `gpt-4-turbo` とファインチューン版、`o1` / `o1-pro` / `o3-mini`）
- **10/31**: OpenAI の既存 evals が読み取り専用化
- **10 月**: Anthropic の IPO 予定（$2T 超の評価額を目標と報道）／ SPFx 1.24 GA ／ 569608・569475・568937 の GA ／ 韓国 App Store のコンテンツ記述子2件が All → 12+
- **11/12**: **OpenAI が Cursor へのモデル提供を停止**（ハイライト3参照）
- **11/15**: Release Planner の退役
- **11/21**: GPT-5.6 Sol の暫定値下げが有効とされる期限
- **11/24 以降**: `claude-opus-4-5-20251101` の暫定退役日（確定日ではない）
- **11/30**: OpenAI の Evals・Agent Builder・`v1/prompts` 退役
- **12/1**: OpenAI の GPT Image 系退役
- **12/2**: EU AI Act の生成コンテンツ標識義務、8/2 以前に市場投入済みシステムへの猶予終了
- **12/11**: OpenAI の旧スナップショット退役（`gpt-5-2025-08-07` / `o3-2025-04-16` / `o3-pro-2025-06-10` 等）
- **12/31**: Gemini 3.7 Flash の導入価格終了（$0.75/$3.75 → $1.50/$7.50）
- **12 月**: Copilot Tuning の新体験が GA
- **年内**: Anthropic の新データ保持方式（顧客自身のクラウドでの30日保持）投入予定と Bloomberg が報道 ／ OpenAI の Jalapeño チップの初期展開
- **2027-01-20**: OpenAI の audio / realtime / transcription 系退役（`gpt-realtime` / `gpt-audio` / `gpt-4o-audio` と mini 系）
- **2027-06-30**: Claude for Teachers の学区登録期限（この日までに登録すれば1年間無料）
- **2027年末**: Anthropic が借りる Nscale West Virginia データセンター（460MW）の稼働開始見込み
- **2028-06**: 米国 K-12 教職員向け ChatGPT for Teachers の無料提供期限

## 改善メモ

- 3ソースの当日分（01 Master / 02 Copilot / 03 industry）はいずれも取得できた。前日 08-30 分にも欠損記録はなく、欠損リカバリの対象はない
- **前日 08-30 の記載を2点訂正した** — ①「8/31 に Claude Code の週次上限50%増が終了」は 8/29 の告知で 9/13 へ延長されたため誤りで、本日 8/31 に発効する期限は7件ではなく4件（＋Power Automate モバイルアプリの廃止）である。②「Release Wave の8月コミット10件」は3ページの8月期日8件と Roadmap 2件の合算で、期日超過の5行を含めると未達は13行になる。02 側も 8/30 を「最終日」と書いた誤りを自ら訂正しており、8月の最終日は本日 8/31 である
- **新規の改善提案は1件** — B-053（01）: 利用枠・料金の変更を検知するため `x.com/@ClaudeDevs` 相当の告知経路を `daily-sources.md` に明示する。02・03 は新規提案なし
- **継続提案は3ソース計73件**（01: 33件・最多は B-013 の33回目、02: 28件・最多は B-011 の42回目、03: 12件・最多は B-004 の63回目）
- **週次上限の延長回数が 01 と 03 で食い違う**。01 は「8/31 期限のまま3回延長され、8/29 の告知が4回目」、03 は「以後4回延長されてきた。直近は 8/19 告知の 8/31 までぶん」と書いており、今回を何回目と数えるかが1回ずれる。本サマリーは回数に触れず、開始日（5/13）と現行期限（9/13）だけを記載した
- **Apple の「AI 関連の最新」の起点が 01 と 03 で食い違う**。01 は 6/11 の ImageCreator クラス廃止告知、08-30 収録の 03 系記載は 8/5 の App Store creative assets を起点にしている。本サマリーは本日 01 側の 6/11 を採り、差を記録する
- **ゲートウェイ拒否が12ドメイン新規に発生した**（03 側）: `www.engadget.com` / `xenospectrum.com` / `gihyo.jp` / `www.bleepingcomputer.com` / `devops.com` / `startupfortune.com` / `www.notebookcheck.net` / `www.macobserver.com` / `we-fix-pc.com` / `forkast.news` / `www.musicbusinessworldwide.com` / `www.digitalapplied.com`。⚠️ **うち10件はハイライト2・3の詳報**にあたり、同一主題の二次が同時に落ちる型が4度目の再発になった。01 側も `www.digitalapplied.com` を新規障害として記録している
- **週次復旧チェック（月曜・本日実施）で8ホスト全件が未復旧・4週連続だった**（01 側）。`*.anthropic.com` 4ホストは `curl` exit 56 が再現し**ゲートウェイ拒否と確定**した（B-049 の食い違いは解消）
- ⚠️ **長期化している一次未読・接続障害**: 8月 Risk Report が15日連続（01）、`mc.merill.net` の EGRESS_BLOCKED が24日連続（02）、Copilot Tuning 一次の未更新が11日連続（02）、`www.ppweekly.com` が週次確認日4回連続スキップ（02）。いずれも解消の見込みが立っていない
