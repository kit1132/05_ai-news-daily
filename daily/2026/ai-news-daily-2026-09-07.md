# AI News Daily Summary — 2026-09-07

週末明けで一次の新規告知が乏しく、3ソースとも「据え置きの確認」が本体になった日である。Microsoft 側は Roadmap の新規起票がゼロで、Release Notes・Copilot Studio What's New・各公式ブログとも動いていない。GitHub changelog も OpenAI changelog も 9/3〜9/4 が最上位のままである。その中で 03 が Nvidia による Hugging Face 買収の確定を4日遅れで捕捉し、08-28 に「報道が割れる」として保留した案件が $12.93B の定義契約として決着していた。Claude Code は `stable` の遅れが27版に拡大し、権限まわりの修正3件が固定組織へ10日届いていない。9/9 の PVA ヘルプチャットボット削除と 9/13・9/14 の Claude Code 週次上限の切り替えが今週の確定期限である。

## 今日のハイライト

### 1. Nvidia の Hugging Face 買収が確定した — オープンウェイトを「ベンダー非依存の選択肢」と説明する前提が引き直しになる

**要点**: Nvidia が Hugging Face を **$12.93B** で買う定義契約を9/2に締結した。08-28 に「報道が割れる」として保留した案件が確定へ決着し、モデル調達を「特定ベンダーに依存しない」と説明してきた前提を引き直す段階に入る。

**詳細**: 定義契約の締結は9月2日、発表は9月3日で、クローズ見込みは **2027年上半期**である。規制当局の承認を含む通例のクロージング条件が付く。取引条件は複数の二次で一致している。

- 総額 $12,930,300,000。うち株主への対価が約 $11.9B、Hugging Face 側の従業員向け株式リテンションが最大約 $1.0B
- 中立性の約束: Hugging Face はブランドを維持したままオープンなプラットフォームとして運営を続け、開発者はモデル・フレームワーク・クラウド・推論プロバイダー・計算基盤を従来どおり選べる。⚠️ Hugging Face 上での構築とデプロイに Nvidia のハードウェアは必須にしないとし、マルチクラウド・マルチアクセラレータ対応を継続するとしている
- プラットフォーム規模: 開発者・研究者 1,800万人超、法人ユーザー 20万超、公開モデル 300万超、データセット 50万超、アプリケーション 100万超

⚠️ **Hugging Face は2025年後半に Nvidia からの $500M 出資を断っていた。**当時 CEO の Clement Delangue は権力集中への対抗をオープンウェイトの意義として挙げており、1年足らずで買収を受け入れた形になる。⚠️ 一次の `blogs.nvidia.com` はゲートウェイ拒否で本文に到達できず、上記の数値と文言はすべて二次複数件の突き合わせによる。買収は未完了のため、提案では「2027年上半期クローズ見込みの合意」までを事実として扱い、統合後の挙動は前提に置かない。

⚠️ **本サマリーとしても4日遅れの捕捉である。**08-28 収録時点では The Information が合意成立、Business Insider が破談の可能性ありと報じて成立段階そのものが割れており、当時は「成立すれば」の条件付きで記録していた。保留を解く材料は9月3日に出ていたが、09-03〜09-06 のいずれの回でも検知できなかった。

- https://blogs.nvidia.com/blog/nvidia-to-acquire-hugging-face/
- https://techcrunch.com/2026/09/03/nvidia-confirms-it-will-buy-hugging-face-for-12-9-billion/
- https://www.cnbc.com/2026/09/03/nvidia-agrees-to-buy-hugging-face-for-almost-13-billion-ai-expansion.html
- https://www.theregister.com/ai-and-ml/2026/09/03/nvidia-buys-hugging-face-for-129b-promises-not-to-squeeze-too-hard/5294208
- https://www.storagereview.com/news/nvidia-to-acquire-hugging-face-for-12-93b-pledges-the-platform-stays-open-and-hardware-neutral

### 2. Claude Code の `stable` 遅れが27版に拡大した — 権限まわりの修正が固定組織に10日届いていない

**要点**: Anthropic が 9/6 に `2.1.263` を publish した一方、npm の `stable` は **2.1.236** で止まり差は **27版**に開いた。`stable` 固定の組織の前提は「数日遅れる」から「権限とセキュリティの修正を受け取れない」へ変わっている。

**詳細**: npm `dist-tags` の実測（09-07）は `{stable: 2.1.236, latest: 2.1.263, next: 2.1.263}` で、`next` == `latest` の合流は前日から継続している。`stable` に届いていない修正のうち、権限・セキュリティに関わるものは3件ある。

- `2.1.251`（8/28）: ファイル系ツールが差し替えられた symlink を追跡してしまう境界を修正した
- `2.1.260`（9/3）: 括弧を含む権限ルールが無効として破棄される不具合を修正し、危険な `rm` の確認プロンプトが `rm -rf` を捕捉するようにした
- `2.1.263`（9/6 02:07 UTC）: changelog の記載が「バグ修正と信頼性の改善」の1行のみで、内容が未確定である

欠番は `2.1.244` / `2.1.249` / `2.1.253`〜`2.1.256` に `2.1.262` が加わり計7件になった。いずれも npm の `time` にも changelog にも存在しないため取りこぼしではない。⚠️ 直前の `2.1.261`（9/4）が VS Code 分を含め70項目超を列挙していたのと対照的で、版ごとの粒度を一次 changelog だけで追う運用には抜けが生じうる。⚠️ 03 は `2.1.258` から4版続いていたスケジュール／クラウド実行環境の不具合修正が5版連続になったかを、記載が無いため判定できないと記録している。

- https://code.claude.com/docs/en/changelog
- https://registry.npmjs.org/@anthropic-ai/claude-code

## カテゴリ別まとめ

### Anthropic / Claude

- Anthropic が Claude Code `2.1.263` を 9/6 02:07 UTC に publish した（ハイライト参照）
- Claude Code changelog の最上位8版は 2.1.263（9/6）→ 2.1.261（9/4）→ 2.1.260（9/3）→ 2.1.259（9/2）→ 2.1.258（9/1）→ 2.1.257（9/1）→ 2.1.252（8/31）→ 2.1.251（8/28）で、日付列に飛びはない
- **モデル退役ページ**: Anthropic は新規の退役告知を出していない。Active は11件で据え置き、直近告知は 2026-06-05 の Opus 4.1（8/5 に退役済み）のままである
  - 暫定退役日は全11件が「not sooner than」表記で確定日ではない。最短は `claude-sonnet-4-5-20250929` の 9/29、次が `claude-haiku-4-5-20251001` の 10/15 である（全件は「直近の注目予定」を参照）
  - 表の外の Note ブロックで `claude-mythos-preview` が deprecated 扱いのままである（移行先 `claude-mythos-5`）。Active 一覧には現れない
  - 日付は Anthropic 運営（Claude API / Claude Platform on AWS / Microsoft Foundry）にのみ適用され、Amazon Bedrock と Google Cloud は独自スケジュールを持つ
  - `temperature` / `top_p` / `top_k` が Opus 4.7 以降で 400 エラーになる扱いも据え置きである（Python SDK v1.0 では `TypeError`）
- **Claude Platform API release notes**: 9/3 の `ant` CLI 1.30.0（`ant apply`）が最上位のままで、9/4〜9/6 の追加はない。日付列は 9/3 → 9/1 → 8/27 → 8/26 → 8/20 と連続している
- `claude.com/blog` は 9/2 の commerce agents 2本が最上位のままで、9/3〜9/6 の新規はない。`support.claude.com` の Release Notes も 9/1 の Fable 5.1 / Mythos 5.1 が最上位である
- ⚠️ **Startup Grant の締切 9/17 は一次に記載がない** — 二次2件（`grantedai.com` / `creditforstartups.com`）が「2025年12月〜2026年11月の配分年度が 9/17 に締まる」と書くが、一次の `claude.com/programs/startups` には締切日もクレジット額も無い。同ページが挙げる条件は「設立4年以内」「機関投資家からの出資あり」「過去に Anthropic のスタートアップクレジット未受領」の3点である。**プログラム自体の締切ではなく配分年度の区切りを指している可能性があり、確定した期限としては扱わない**
- ⚠️ Anthropic の8月 Risk Report は **22日連続**で一次未読である（初出 08-17）。二次の内容に変化はない

### OpenAI

- **API 単価は14日連続で据え置かれた** — OpenAI が一次料金ページの単価を動かしていない。GPT-6 Astra は短文脈で入力 $10／出力 $50、長文脈で $20／$75、Fast mode は短文脈 $20／$100 である。GPT-5.6 Sol は $4／$20 で、期間限定価格は「少なくとも 2026年11月21日まで」の記載のままである
  - 注記3点にも変更はない: 地域処理の10%アップリフト（2026年3月5日以降リリースのモデルが対象）、EU データレジデンシーでの Astra Fast mode 不可、長文脈の 272K トークン境界
  - ⚠️ `gpt-5.4-cyber` の単価欄は4日連続で空のままで、Cyber 系の調達単価は依然として見積もれない
- **廃止期限は10日連続で動いていない** — OpenAI が一次 deprecations ページに撤回・延期・新規追加を出していない。⚠️ 今月2件が到来する（9/24 の Videos API と Sora 2 系、9/28 の 4モデル停止）。⚠️ **GPT-6 Astra 登場に伴う退役告知は依然として無い**。同ページは登録ソースに無い（01 の B-055・回数7）
- `developers.openai.com/api/docs/changelog` は 9/3 の2本（GPT-6 Astra のリリース／Responses API の非同期ツール呼び出し・ターン途中のステアリング・reasoning effort 変更）が最上位のままである
- OpenAI は Codex CLI を 9/5・9/6 にリリースしていない。安定版は `0.153.4`（9/4 23:25 UTC）、pre-release は `0.154.0-alpha.3`（9/4 00:57 UTC）が最新である
- ⚠️ **「Astra が全 ChatGPT ユーザーに開放された」とする二次1件（9/5）は採らない** — 一次の community 告知と他の二次（CNBC / Al Jazeera / Bloomberg）はいずれも Plus / Pro / Business / Enterprise の有料プラン限定の段階提供と書いており、Free プランはロールアウト対象に含まれていない。同告知はコンテキスト 1,050,000 トークン・最大出力 128,000 トークンを明記している
- 到達性: `developers.openai.com`（changelog・deprecations・blog とも）と `community.openai.com` RSS は 200 を返す。`openai.com` / `help.openai.com` はオリジン403、`learn.chatgpt.com` はゲートウェイ拒否が継続している

### Google / DeepMind

- Gemini API changelog は 9/3 の Lyria 3.5 public preview が最上位のままで、9/4〜9/6 の追加はない。日付列は 9/3 → 9/2 → 9/1 → 8/27 → 8/26 → 8/13 と連続している
  - ⚠️ Lyria 3.5 は音楽生成なので `interests/ai-tools.md` の除外基準に該当し、内容は追わない
- 旧 `gemini-omni-flash-preview` エンドポイントの廃止日 **9/30**（本日から23日後）に変更はない
- HF の `google` org は `timesfm-3.0-pytorch`（作成 8/24）が最新のままで、9/3〜9/6 の新規作成も `lastModified` の更新もない
- 既報: 9/2 GA の `gemini-3.8-flash` は入力 $0.75 / 出力 $3.75 が 2026-12-31 までで 2027-01-01 から $1.50 / $7.50 になる、9/1 の agentic video understanding（長尺で最大88%のトークン削減）、**Gemini 3.5 Pro GA は未ローンチが継続**している
- 登録済み Google 系5ソースはゲートウェイ拒否が継続しており、`ai.google.dev` だけが到達できる Google 一次である

### Microsoft / GitHub Copilot

- ⚠️ **Microsoft の一次情報に本日の新規発表はない** — 02 は Roadmap の新規起票がゼロで、Release Notes・Copilot Studio What's New・各公式ブログとも据え置きだと記録した。Roadmap RSS の `pubDate` を全件パースした結果、**9/3 22:50Z より新しい起票はゼロ**で、9/4〜9/7 の4バッチが空振りである
  - ⚠️ `lastBuildDate` は `Fri, 04 Sep 2026 22:03:41 Z` から3日連続で動かず、総項目数は 1,774 → **1,770** と4件減っている。どちらの指標も新規件数を表さないため、判定は `pubDate` の全件パースで行った
  - `Microsoft Copilot Studio:` で始まる項目は19件で、全件が `In development` のままである。**566997**（メーカー資格情報の使用ブロック）は GA 期日「August CY2026」を超過し、**562221**（ワークフローでの MCP 準拠ツール）は GA 期日 2026年6月から超過4か月目に入った
- `github.blog/changelog` の Copilot ラベルは 9/4 の2本が最上位のままで、9/5〜9/7 の新規はない。最上位10件は 9/4 の2本 → 9/3 の3本 → 9/2 の2本 → 9/1 の3本である。既収録の **10/2 の Copilot 4モデル廃止**（本日から25日後）にも撤回・延期の告知は出ていない
- GitHub は Copilot CLI の pre-release・安定版とも 9/5・9/6 に出していない。最新は pre-release が `v1.0.84-1`（9/4 23:20 UTC・GPT-6 Astra 対応）、安定版が `v1.0.83`（9/4 15:38 UTC）である
- **M365 Copilot Release Notes**: August 25, 2026 バッチが最新のままで、`## ` 見出しの並びも August 25 → August 11 → July 29 → July 15 → July 01 → June 16 → June 2 で不変である。`updated_at` は 2026-09-03T19:39Z から動いておらず、次バッチは隔週傾向なら **9/8 前後**である
- **Tech Community（M365 Copilot Blog）**: board RSS の全20エントリを突合したが新規はない。先頭3件は 9/4 の GPT-6 Astra、9/3 の月次「What's New in Microsoft Copilot | August 2026」、9/2 の Claude Fable 5.1 で、いずれも掲載済みである
- **Cowork**: What's New は August 2026 節が最新で `updated_at` 2026-08-28T05:15Z から動かず、ローカルブラウザーの GA・プラグインのワークスペースファイル入力・イベント駆動タスクの3件に増減はない
- **拡張機能 What's New**: `updated_at` が 2026-07-29T20:23Z のままで、更新が止まって **40日**になる。最新は宣言型エージェント manifest 1.8 を含む July 2026 節である（次回確認は 9/11）
- **Purview**: `whats-new` の `updated_at` は 2026-08-28T07:31Z で変化がない。⚠️ 569612（Copilot メモリの Purview 保持・GA 2026年9月）は本日も Purview 側に未掲載で、9/3 起票の 570445（自動ラベル付けの拡張）も反映されていない（02 の B-042・回数16）
- `devblogs.microsoft.com/commandline` の AI 関連の最新は 8/10 の Intelligent Terminal 0.2 のままである（01 の B-042・回数13）

### Copilot Studio / Power Platform

- ⚠️ **PVA ヘルプチャットボットの削除まで2日である** — Power Automate メーカーポータル左下の PVA ヘルプチャットボットが **9/9** に全ページから消える。一次は `power-platform/important-changes-coming` の先頭節で「Effective September 9, 2026」と発効日を明記している
  - 9/9 以降に起きることは3点である: 左下のチャットボットが消える、メーカーはそこから Power Automate について質問できなくなる、右上の Help (?) メニューはヘルプ参照とサポート要求の作成を含めてそのまま残る
  - Microsoft は削除理由を「旧来のサポート体験で内容が古くほとんど保守されていない」ためとし、導線を1箇所へ集約すると説明する
  - ⚠️ クラウドフロー・デスクトップフロー・コネクタなど Power Automate の機能そのものには影響しない。管理者側の作業は不要で、必要なのは利用者への周知と内部ドキュメントの更新だけである
  - ページ自体は `updated_at` 2026-09-04T19:03Z から動いておらず、`## ` 見出しの本数にも増減がないため、新規の非推奨項目はゼロだった
  - https://learn.microsoft.com/en-us/power-platform/important-changes-coming
- ⚠️ **モデル提供開始を Learn の一覧で判定する運用は本日も戻らなかった** — Claude Fable 5.1（9/2）と GPT-6 Astra（9/4）は、Roadmap 広報枠・モデル一覧2本・Copilot Studio What's New のどれにも載らないまま3日目に入った。02 は一次4本をすべて再取得して本文を検索したうえで不在を確認している
  - `authoring-select-agent-model` は 9/5 に1か月ぶりの再ビルドを受けたまま `updated_at` 2026-09-05T01:02Z で、本文に `Fable` も `Astra` も1回も現れない
  - `cowork-models` は `updated_at` 2026-09-02T17:33Z で、ピッカーの表記が告知の「Fable 5.1」ではなく「Claude Fable 5 (Preview)」のままである。⚠️ 「before this page is published」で始まる編集者向けの未公開指示も本日の本文に残っている
  - Roadmap の Latest announcements は先頭が 7/24 の Claude Opus 5 で、8月に続き9月も1件も追加されないまま **45日**が経った
  - ⚠️ 提供開始を当日に掴める経路は Tech Community の `Available today:` 記事1本だけで、一覧を根拠に「まだ来ていない」と読むと2件続けて外す（02 の B-059）
- **Copilot Studio What's New**: 最新は July 2026 節のままで、8月節・9月節とも作成されていない。`updated_at` は 2026-08-20T19:04Z から動かず、June 節の GitHub Copilot ハーネスは `(Production-ready preview)` の表記で、GA（8/3）から **35日連続**の未反映である（B-023 回数34）
- **ハーネス概要**: `harnesses-overview` の `updated_at` が 2026-09-05T01:02Z で、モデル一覧と同じタイミングで再ビルドされていた。ただし3ハーネス（GitHub Copilot / 標準 / Copilot chat）の説明に変更はなく、GA / Preview の別を示す語はページ本文に無い
- **Released Versions**: Copilot Studio Build は 2026.6.3（6/30 初出）のままで空白が **69日**に達した。ページの `updated_at` は 2026-07-01T15:55Z で、本文の「This page is updated each week on Tuesday.」と実態が食い違ったままである（B-037 回数21）。日本リージョンは 2026.6.2 で据え置き、次の定例更新日は 9/8 である
- **課金レート表（週次・本日実施）**: `requirements-messages-management` の `updated_at` は 2026-08-03T14:59Z で、消費レート・エンフォースメント・免除の記載に変化はない
  - 機能別レート: クラシック回答 1 / 生成回答 2 / エージェントアクション 5 / テナントグラフグラウンディング 10 / エージェントフローアクション 13（100アクションあたり）
  - 生成 AI ツール（10応答あたり）: basic 1 / standard 15 / premium 100。コンテンツ処理ツールは1ページ 8
  - 音声（1分あたり）: クラシック 10 / GenAI 35 / プレミアム GenAI 75
  - エンフォースメント: テナント前払い容量の 125% でカスタムエージェントを無効化する。エージェントフローは容量枯渇時点で新規実行のみブロックし、親エージェントの非フロー対話は継続する
  - M365 Copilot ライセンスユーザーの B2E 利用は無償だが、⚠️ CUA（Computer-Using Agents）は対象外である
- **課金ドキュメント3本**: `agents-experience/` 配下の3本はいずれも `updated_at` 据え置きで、USD 単価は本日も Learn 側に存在しない
- **Copilot Tuning**: 停止発効（8/20）から18日が経っても、一次 `microsoft-365/copilot/copilot-tuning-overview` は停止も退役も書いていない。⚠️ 本文は「Access through Frontier is planned for April 2026」という既に過ぎた予定を現在形で残している（B-024 回数31）
- **Release Wave**: リネーム後の5ページはいずれも HTTP 200・`updated_at` 2026-09-03T14:35Z・`git_commit_id` 06b3b6ba で、9/3 から4日連続で再ビルドされていない。緑チェックの増減もない（B-018 回数39・B-038 回数20）
  - 索引ページが張る製品リンクは power-apps / power-pages / power-automate / data-platform / governance-administration の5本のままで、Copilot Studio は依然として含まれない
  - ⚠️ `2026wave1/toc.json` は先頭ノード1件だけを返し、200 で取得できる5ページがナビゲーションから外れている（過去の取得記録がないため、いつからかは判定できない）
  - 登録 URL `release-plan/2026wave1/microsoft-copilot-studio/planned-features` は本日も `aka.ms/MCStoM365Roadmap` へ 301 で、`aka.ms` はゲートウェイ拒否のため転送先に到達できない（B-012 回数28）
- **Power Platform Blog**: 親カテゴリの先頭は 9/3 の「PPCC 2026」で既報である。子カテゴリは Power Apps が 9/1 のキャンバス共同編集エージェント GA、Power Automate が 8/13 の PPCC 登録記事で、どちらも新規はない。⚠️ 一覧に 8/6 公開の月次合併号が現れない状態は本日も続いている（B-010 回数44）
- **Partner Center**: 9月ページは掲載4件・`updated_at` 2026-09-04T22:04Z のままで追記がない。内容は 9/4 の Business Applications roadmap 移行（11/15 の Release Planner 退役を含む）、9/3 の Partnering for Success Together（初回 **9/9**）、9/2 の CSP サンドボックス、9/1 の Marketplace 購入発注マッピングである（B-013 回数39）

### Cursor / 開発ツール

- ⚠️ **Cursor は GPT-6 Astra の提供開始を告知していない** — 9/3 GA から4日が経ち、Copilot（9/4 GA）と Codex CLI（`0.153.1`〜`0.153.4`）が既に対応している一方、Cursor は changelog・フォーラム Announcements のどちらにも記載を出していない。`daily-sources.md` が「モデル提供開始告知はフォーラム側にしか出ない」と規定しているとおりフォーラムを確認したうえでの不在である
- Cursor changelog は 9/2 の Self-hosted machines が最上位のままである（RSS 200 / item 50件）。フォーラム Announcements も 9/2 の Grok Bot Android 版が最上位である
- **Grok 4.7 は二次情報のままで動きがない** — 予告の出所は 9/2 の Musk の X 投稿で、公開見込み 9/11〜9/12、パラメータ 2.1兆（4.6 の1.5兆から40%増）とされる。⚠️ xAI はローンチページ・API モデル ID・価格・モデルカードのいずれも公開しておらず、一次3ホスト（`x.ai` / `docs.x.ai` / `grok.com`）はゲートウェイ拒否が継続している。公式提供中の最新は Grok 4.6（8/12・context 50万トークン・$2/$6）である
- Devin は一次・代替一次のいずれからも読めない状態が継続している（`docs.devin.ai` / `cli.devin.ai` ともゲートウェイ拒否）

### MCP / エージェント標準

- `blog.modelcontextprotocol.io`（RSS `index.xml`）は 200 を返すが、8/22 の「The New MCP Roadmap」が最上位のままで新規はない（**16日間**）
- WebMCP Challenge は提出締切 9/4 を経過した。受賞発表は 9/23、賞金総額は $35,000 である
- A2A（Agent2Agent）の AAIF 参加は未確定のままである。一次3ホスト（`aaif.io` / `www.linuxfoundation.org` / `developers.googleblog.com`）はゲートウェイ拒否が継続している

### オープンウェイト / ローカル LLM

- 追跡8 org のいずれにも 9/5・9/6 の新規公開はない。`createdAt` 降順と `lastModified` 降順の両方で確認した
  - 各 org の最新作成: `Qwen-Drive-1.0-4B` 8/27 ／ `DeepSeek-V4-Flash-Vision-Exp` 8/31 ／ `GLM-5.3-Flash-BF16` 8/25 ／ `timesfm-3.0-pytorch` 8/24 ／ `Muse-Glimmer-30B-ExecuTorch-PTE` 8/10 ／ `Shieldstral-1.0-3B` 7/16 ／ `Kimi-K3` 6/13 ／ `privacy-filter` 4/17
  - `lastModified` の最新は `zai-org` の GLM-5.3 系4件（9/4 06:38〜06:45 UTC）だが、作成日は全て 8/25 なのでカード更新である
- HF `downloads` の実測（2026-09-06 19:09 UTC 取得・追跡8リポジトリは全て `private: false` / `gated: false`）
  - `Qwen/Qwen3.8-27B-FP8` 6,610,521 ／ `Qwen/Qwen3.8-Flash-Next` 432,966 ／ `DeepSeek-V4-Flash-0731` 4,486,631 ／ `DeepSeek-V4-Pro-0813` 154,525 ／ `DeepSeek-V4-Flash-Vision-Exp` 209,191 ／ `GLM-5.3-Flash` 761,364 ／ `GLM-5.3` 410,074 ／ `moonshotai/Kimi-K3` 2,460,430
  - ⚠️ `DeepSeek-V4-Flash-0731` が前回記録（4,565,650）から減った。30日ローリングなので減少は異常ではない（B-050・回数9）

### 資本・M&A・市場データ

- Nvidia が Hugging Face の買収で定義契約を締結した（ハイライト参照）
- **Wonderful が $550M を調達し評価額 $5B に乗せた** — オランダ・イスラエル拠点の Wonderful が9月2日に Series C を公表した（本サマリーとしては5日遅れの捕捉である）。Insight Partners が主導し、**Salesforce が初めて出資**、既存の Index Ventures・IVP・Vine Ventures・9Yards・Bessemer Venture Partners が参加した。⚠️ 2026年3月の Series B 時点の評価額 $2B から6カ月弱で **2.5倍**である。同社はカスタマーサービス向け AI エージェントから出発し、現在は「エンタープライズ AI OS」を名乗る。Series B 以降で展開市場は35超、従業員は650名に増えた。⚠️ 一次の `www.wonderful.ai` はゲートウェイ拒否のため、数値は二次複数件の突き合わせによる
- 定点の市場調査ソース（IDC / IDC Japan・Gartner・MM総研・NRC・Similarweb）に本日の新規公表はない。引用可能な最新値は既収録から不変で、Gartner の世界 AI 支出 2026年 $2.59兆・前年比 +47%（5/19 公表）、AI-optimized IaaS $42B・+96%（8/10 公表）、AI モデル・プラットフォーム $64B・+63.4%（7/20 公表）の3階層が引き続き使える。⚠️ いずれも本日の新規公表ではないため鮮度を明示して使う
- ⚠️ **1年前の Gartner 予測が「最新」として流通している** — 検索面に「エンタープライズアプリの40%が2026年末までにタスク特化型 AI エージェントを搭載する（2025年は5%未満）」が日付なしで浮上したが、一次のプレスリリースは **2025年8月26日公表**であり1年前の予測である。二次の集計記事が公表日を落とすため、Gartner の数値は必ず一次プレスリリースの URL に含まれる日付で鮮度を確認してから引く
- 企業構造・規制の新規はない。9/5・9/6 付けの提携・組織再編・規制の一次確定は検出できなかった
- 既報（一次未読を含む）: Anthropic のリボルビング枠 $150億拡大観測（9/3・Morgan Stanley 主導）、Anthropic × Lambda 約 $350億（テキサス州 Nueces County・約350MW）、直近クラウド契約は計 $1,750億とされる、国防総省による supply-chain risk 指定の継続表明（9/3）、米司法省の statement of interest（9/1）、GenAI.mil への ChatGPT Mil / Grok 追加（9/1・**Anthropic は非参加**）、Anthropic の IPO 観測（10月・$2T 超）、SpaceX による Cursor 買収完了（8/14・$60B）

### Apple / クラウド

- `developer.apple.com` は 200 を返し、9/1 の「Upcoming changes to Rosetta support for Intel-based macOS apps」が最上位のままである。9/2〜9/6 の新規はない
  - macOS 26.4 以降は Intel 専用アプリの起動時にシステム通知が出る。**macOS 27 が Rosetta を載せる最後のリリース**である
- ⚠️ Apple の AI 関連の最新は 6/11 の ImageCreator クラス廃止告知のままである（8/5 の App Store creative assets 以降に新規なし）
- 既報: 8/26 の特別イベント告知（**9/9 10:00 PT**）、8/24 Sign in with Apple 新ドメイン（`private.icloud.com`）、8/18 EU 向けビジネス条件変更（発効 2026-10-01）
- `azure.microsoft.com` はゲートウェイ拒否のままである

## 直近の注目予定

- **9/8**: M365 Copilot Release Notes の次バッチ（隔週傾向）／ Copilot Studio Released Versions の定例更新日
- **9/9**: Apple 特別イベント（10:00 PT）／ Power Automate の PVA ヘルプチャットボット削除が発効 ／ Partnering for Success Together 初回 ／ GLM-5.3-Flash の Z.ai 経由50%割引が終了
- **9/10**: MAI-Code-1-Flash が全 Copilot 体験から廃止
- **9/11**: 拡張機能 What's New とモデル可用性一覧の週次確認
- **9/12**: Grok 4.7 の公開予定（Musk の X 投稿のみが出所・公式の裏づけなし）
- **9/13**: **Claude Code の週次上限50%増が終了** ／ Power CAT・PnP の週次確認
- **9/14**: **Claude Code の標準週次上限が恒久的に +25%**（Pro / Max / Team / シート課金 Enterprise。現行比では17%減）／ ppweekly・MS-4005・課金レート表の週次確認
- **9/17**: OpenAI DevDay Exchange の応募締切 ／ Anthropic Startup Grant Program の配分年度締切（**二次のみ・一次に記載なし**）
- **9/21**: Anthropic ウェルビーイング研究助成の応募締切
- **9/23**: WebMCP Challenge の受賞発表
- **9/24**: OpenAI の Videos API と Sora 2 系が退役（代替モデルの提示なし）
- **9/28**: Copilot のチャット3面統合 ／ code review の既定 effort が Lite → Balanced ／ チャットのデータ保持がアカウント存続期間へ ／ OpenAI の `gpt-3.5-turbo-instruct` / `babbage-002` / `davinci-002` / `gpt-3.5-turbo-1106` が停止（代替 `gpt-5.6-terra`）
- **9/29 以降**: `claude-sonnet-4-5-20250929` の暫定退役日（確定日ではない）
- **9/30**: Gemini の旧 `gemini-omni-flash-preview` エンドポイント廃止 ／ M365 E7 プロモーション最終日 ／ E5・E3 の CSP 割引終了 ／ 2026 Wave 1 の対象期間終了
- **9 月**: iOS 27 / macOS 27 GA ／ Claudeforce のオープンベータ（二次情報）／ Release Plans on Learn の新規掲載停止 ／ Copilot Tuning の Public Preview 再開 ／ Copilot デスクトップアプリの広範展開（中旬）／ Eligibility Dashboard の展開完了（中旬）／ Copilot Studio の Roadmap 項目が GA 期日 ／ App Store の Social Media 年齢レーティング回答が必須化 ／ OpenAI の IPO 観測 ／ OpenAI の Private Safety Processing の広域展開と技術白書（二次情報）
- **10/1**: Copilot Business・Enterprise の既存顧客が前払い必須に ／ Apple の EU 向け新ビジネス条件が発効 ／ CSP software の価格改定 ／ Ask Gemini in Chat のプロモーション上限が終了
- **10/2**: **GitHub Copilot が Gemini 3.5 Flash / Gemini 3.6 Flash / Kimi K2.7 Code / Claude Opus 4.7 を全体験から廃止**
- **10/5**: Anthropic ウェルビーイング研究助成の full proposal 提出期限（採択者）
- **10/15 以降**: `claude-haiku-4-5-20251001` の暫定退役日（確定日ではない）
- **10/16–11/11**: OpenAI DevDay Exchange 8都市（東京は 10/20）
- **10/23**: OpenAI のレガシースナップショット退役（`gpt-3.5-turbo-0125` / `gpt-4-0613` / `o1-2024-12-17` / `o4-mini-2025-04-16` とファインチューン版）
- **10/31**: OpenAI の既存 evals が読み取り専用になる
- **10 月**: Anthropic の IPO 予定（$2T 超の評価額を目標と報道）／ 韓国 App Store のコンテンツ記述子2件が All → 12+
- **秋**: Anthropic の Enterprise Frontier Safeguards が段階的に提供開始（二次情報）
- **11/15**: Microsoft の Release Planner が退役し、Learn 上の Release Plans がアーカイブされる
- **11/21**: GPT-5.6 Sol の暫定値下げが有効とされる期限
- **11/24 以降**: `claude-opus-4-5-20251101` の暫定退役日（確定日ではない）
- **11/30**: OpenAI の Reusable prompts・Evals プラットフォーム・Agent Builder が停止（代替に外部OSS の Promptfoo を挙げる点も不変）
- **12/1**: OpenAI の GPT Image 系が停止（`gpt-image-1-mini` / `gpt-image-1.5` / `chatgpt-image-latest` → `gpt-image-2`）
- **12/2**: EU AI Act の生成コンテンツ標識義務、8/2 以前に市場投入済みシステムへの猶予終了
- **12/11**: OpenAI の旧スナップショット退役（`gpt-5-2025-08-07` / `o3-2025-04-16` / `o3-pro-2025-06-10` 等）
- **12/31**: Gemini 3.8 Flash と 3.7 Flash の導入価格が終了（$0.75/$3.75 → $1.50/$7.50。GitHub Copilot 経由の Gemini 3.8 Flash 導入価格も同日終了）／ GitHub Copilot の Fable 5.1 / Fable 5 に対する ZDR 暫定免除が終了
- **年内**: Anthropic の新データ保持方式（顧客自身のクラウドでの30日保持）投入予定 ／ OpenAI の Jalapeño チップの初期展開
- **2027-01-06**: OpenAI で大半のユーザーの新規ファインチューニングジョブ作成が終了
- **2027-01-20**: OpenAI の audio / realtime 系退役（`gpt-realtime` / `gpt-audio` / `gpt-4o-audio` と mini 系）
- **2027-02-05 以降 / 02-17 以降**: `claude-opus-4-6` / `claude-sonnet-4-6` の暫定退役日（確定日ではない）
- **2027-02-26**: OpenAI の文字起こし4モデル退役（`whisper-1` / `gpt-4o-transcribe` / `gpt-4o-mini-transcribe` / `gpt-4o-transcribe-diarize`）
- **2027-03-01 / 2028-10-01**: SharePoint クラシックページ退役のフェーズ1・フェーズ2
- **2027-04-16 / 05-28 / 06-09 / 06-30 / 07-24 / 09-01 以降**: `claude-opus-4-7` / `claude-opus-4-8` / `claude-fable-5` / `claude-sonnet-5` / `claude-opus-5` / `claude-fable-5-1` の暫定退役日（確定日ではない。⚠️ `claude-opus-4-7` は Copilot では 10/2 に消える）
- **2027-06-30**: Claude for Teachers の学区登録期限
- **2027年末**: Anthropic が借りる Nscale West Virginia データセンター（460MW）の稼働開始見込み
- **2028-06**: 米国 K-12 教職員向け ChatGPT for Teachers の無料提供期限
- **2027年上半期**: Nvidia による Hugging Face 買収のクローズ見込み（ハイライト参照）

## 改善メモ

- 3ソースの当日分（01 Master / 02 Copilot / 03 industry）はいずれも取得できた。前日 09-06 分にも欠損記録はなく、欠損リカバリの対象はない
- ⚠️ **Nvidia × Hugging Face は3ソースのうち 03 だけが捕捉した** — 発表は9月3日で、01 は本日も HF を「オープンウェイトのホスティング先」としてのみ扱い、org 単位の新規公開とダウンロード数を追うにとどまっている。**追跡8 org の母体そのものが買収対象になった事実が、01 の観測枠に入っていない**。01 側で HF の企業側の動きを拾う経路を持つかを決める必要がある
- ⚠️ **本日は「据え置きの確認」がハイライト候補を上回った** — 3ソース合計の項目のうち、新規事実を含むものは Nvidia/HF・Wonderful・Claude Code 2.1.263 の3件だけで、残りは日付・`updated_at`・件数の不変を確認した記録である。03 自身も「週末明けで新規の一次告知が乏しい」としてハイライトを1件に絞っており、本サマリーも選定基準を緩めず **2件**にとどめた
- ⚠️ **PVA ヘルプチャットボット削除はハイライトから外した** — 09-05・09-06 に続く3日連続の掲載で、本日の 02 も「期限が近づいた項目」と自ら位置づけており、続報が無い。⚠️ ただし発効は **9/9（2日後）**で不可逆な期限であるため、カテゴリ別まとめと注目予定の両方に残した
- **提案番号の衝突が3日連続で発生している** — 本日の新規提案は B-062（01: `main` の履歴が孤立コミットで置き換えられた場合の復旧手順を `CLAUDE.md` に規定）、B-060（02: 既知の取得障害の行を最終確認から14日で疎通確認し復旧を台帳へ反映）、B-033（03: 「未確定」と記録した案件の成立確認を追跡する手順）の3件である。⚠️ **B-060 は 01 の台帳では別提案**（`claude.com/blog` の全 href 列挙）に割り当てられており、09-05 の B-058、09-06 の B-032 に続く3件目の衝突である。台帳がリポジトリごとに独立しているため、番号だけでは提案を特定できない
- **継続提案の計数**: 01 が24件（最多 B-024・33回目）、02 が35件（最多 B-011・49回目）、03 が15件（最多 B-004・70回目）で計 **74件**である。前日の計65件から +9 で、⚠️ 内訳では 01 が +6・02 が +2・03 が +1 と 01 が大きく振れている。前日は 02 が −13 で振れており、**2日連続で別のリポジトリの計数が跳ねている**
- **週次復旧チェック（月曜・01 が実施）は復旧0件で5週連続の全滅だった** — 対象8ホスト（`www.testingcatalog.com` / `simonwillison.net` / `obsidian.md` / `blog.google` / `workspaceupdates.googleblog.com` / `x.ai` / `docs.devin.ai` / `learn.chatgpt.com`）は全件 `EGRESS_BLOCKED` のままである
  - B-049 の分類再実測も変更なしだった。オリジン403 は `openai.com/news` / `help.openai.com` / `api.github.com`、ゲートウェイ拒否は `*.anthropic.com` 4ホストである
  - ⚠️ `daily-sources.md` の Anthropic Blog / News 項は依然「オリジン403」と記載しており、記載と実測が食い違ったままである（修正は kit の判断待ち）
  - **未解決の要 kit 対応（08-07 確定・継続）**: 08-06 追加の許可ドメイン13件は新規起動セッションでも全件未到達である。① 保存先環境とスケジュールタスク実行環境の同一性確認 ② `.google` TLD 3件の個別指定確認 ③ 次回追加対象の確定
- **到達性の変化** — 02 で `learn.microsoft.com` の直接取得が復旧した（配下12 URL すべて 200）。⚠️ **台帳の 403 行は最終確認が 2026-08-06 のまま32日間放置されており、解消済みの障害が継続扱いで残っていた**。02 はこれを受けて B-060 を起票している。Microsoft Copilot Blog の `copilot-studio/feed/` も2日連続で 200 かつ内容が最新である
  - 一方 03 は `blogs.nvidia.com` / `www.gartner.com` / `www.wonderful.ai` / `www.unite.ai` / `aiweekly.co` の5件を新規のゲートウェイ拒否として起票した。⚠️ **`www.gartner.com` は `daily-sources.md` の年次レポート枠に登録済みの定点ソース**であり、市場データの一次確認経路が1本減っている
- ⚠️ **長期化している一次未読・接続障害**: Anthropic の8月 Risk Report が22日連続で一次未読（01）、`mc.merill.net` の拒否が31日連続（02）、Copilot Studio What's New への GA 未反映が35日連続（02）、Released Versions の空白が69日（02）、拡張機能 What's New の停止が40日（02）、Roadmap 広報枠の空白が45日（02）、MCP ブログの空白が16日（01）、`www.ppweekly.com` の失敗が5回連続（02）、`aka.ms` / `pnp.github.io` / `qiita.com` / `zenn.dev`（02）、`learn.chatgpt.com` / xAI 一次3ホスト / Google 系5ソース / Devin 一次（01）。いずれも解消の見込みが立っていない
- **本サマリーの生成環境について（5日連続）** — 本日も GitHub MCP のリポジトリスコープが `kit1132/05_ai-news-daily` のみに設定されており、入力3リポを MCP 経由で読めなかった。公開リポの `raw.githubusercontent.com` から読み取り専用で取得して生成した（入力3リポへの書き込みは行っていない）。⚠️ **5日連続で同じ回避を要している**ため、取得経路を raw に固定するか実行環境のスコープへ入力3リポを追加するかを決める必要がある
  - ⚠️ さらに本日は 07:00 JST の自動実行が生成に至らず、後刻の手動依頼で生成した。⚠️ **自動実行の側でこの回避が働かないと、以後も当日分が空振りする。**上記の判断は先送りできない段階にある
  - ⚠️ 03 は Claude Code のスケジュール／クラウド実行環境の不具合修正が `2.1.258` から4版続いたと記録し、「本ダイジェストの生成環境そのものが該当する系統」と指摘している。本サマリーの実行環境も同じ系統である
