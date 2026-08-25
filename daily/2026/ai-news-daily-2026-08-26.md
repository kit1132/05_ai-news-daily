# AI News Daily Summary — 2026-08-26

水曜は、期限が3本まとめて発効し、さらに期限が2本増えた日である。OpenAI の Assistants API と ChatGPT の o3 が本日停止し、GitHub Copilot の既定モデル有効化ポリシーも発効した。同じ退役ページからファインチューニングの新規作成が 2027年1月6日に全面終了することが本日はじめて判明し、3段階のうち2段階が既に発効済みだった。Microsoft 側では半期の Release Wave モデルが廃止され、Release Planner が 11/15 に退役する。Claude Code は組織側が契約単価とモデル一覧を握れる v2.1.243 が入り、M365 Copilot Release Notes には2週間ぶりの19項目バッチが出た。

## 今日のハイライト

### 1. 本日 8/26 に3件の期限が同時発効し、o3 の退役範囲が ChatGPT 限定と確定した — 「o3 が消える」から「ChatGPT からだけ消え、API は 12/11 まで残る」へ

**要点**: OpenAI の Assistants API が本日停止し、o3 が ChatGPT から退役した。ただし API の `o3-2025-04-16` は 12/11 まで残ると一次で確定したため、移行の締切が一本から二段に変わった。

**詳細**: 3件とも既報の予定だったが、本日はじめて一次で退役の範囲を確定できた。`developers.openai.com/api/docs/deprecations` で、Assistants API の停止が 2025-08-26 の告知から1年後の本日にあたること、o3 の扱いが ChatGPT と API で分かれていることを読めている。

- Assistants API: `/v1/assistants`・`/v1/threads`・`/v1/threads/runs` が縮退運転も猶予期間もなくエラーを返す。移行先は Responses API と Conversations API の組み合わせで、Threads → Conversations の自動移行ツールは提供されない。deep research・MCP・computer use は Responses 側に乗る
- o3: 90日のサンセットを終えて web とモバイルのモデルピッカーから外れた。既存の o3 会話は対応する GPT-5 系へ引き継がれ、推奨代替は GPT-5.4 Thinking と o4 である。⚠️ **API 側は本日の影響を受けない**
- GitHub Copilot: Business / Enterprise で未設定の GA モデルのラベルが `unconfigured` から `inherits default` に変わり、ポリシーの既定値に従うようになった。個別に承認したい組織は本日より前にポリシーを disabled にしておく必要があった

⚠️ 停止が実際に反映されたかは JST 本日午前時点で未確認である。一次ページは本項を「Upcoming deprecations」の区分に置いたままで、反映の確認は 8/27 に回る。

- https://developers.openai.com/api/docs/deprecations
- https://docs.github.com/en/copilot/concepts/models/default-availability
- https://help.openai.com/en/articles/6825453-chatgpt-release-notes

### 2. OpenAI がファインチューニングの新規作成を畳む — 「自社データでモデルを微調整する」構成が 2027/1/6 以降は選べなくなる

**要点**: OpenAI が新規ファインチューニングジョブの作成を **2027年1月6日**に全面終了することが、退役ページの再確認で本日判明した。3段階のうち2段階は既に発効済みで、条件に外れた組織は現時点で作成できない。

**詳細**: 締切は単日ではなく3段階に分かれており、2段階が既に過ぎている。

- **2026年5月7日**（実施済み）: ファインチューニングを一度も実行したことがない組織は、新規の学習ジョブを作成できない
- **2026年7月2日**（実施済み）: 過去60日以内にファインチューニング済みモデルで推論を実行していない組織は、新規の学習ジョブを作成できない
- 2027年1月6日: 稼働中の既存顧客も新規の学習ジョブを作成できなくなる

推論側の扱いは別で、作成済みのファインチューニング済みモデルの推論は、基となるベースモデルが退役するまで動き続ける。止まるのは「新しく作ること」であって既存資産が即日使えなくなるわけではないが、9/28 と 10/23 に旧 GPT スナップショットが停止するため、古いベースモデル上の資産から順に効いてくる。OpenAI 側の理由づけは「新しいベースモデルは指示と書式の追従が十分に良くなり、ファインチューニングの多くが不要になった」である。

⚠️ 5月7日の告知そのものは3ソースいずれも未収録で、本日はじめて一次ページで全体像を確認した（発生から約3.5か月遅れ）。Anthropic / Google 側に同種の選択肢が残るかは別途確認を要する。

- https://developers.openai.com/api/docs/deprecations
- https://community.openai.com/t/openai-s-self-serve-fine-tuning-availability/1380481

### 3. Release Wave が廃止され、Power Platform の計画情報が AI at Work roadmap へ移る — GA 判定を Learn の緑チェックに置く前提が 11/15 に消える

**要点**: Microsoft が半期の release wave 1 / wave 2 モデルを廃止し、9月以降の新規リリース計画を Learn に載せなくなる。**11/15** に Release Planner が退役するため、計画を追う場所そのものが変わる。

**詳細**: Power Platform Blog と Dynamics 365 Blog に 8/25 付で Richard Riley（General Manager, Agents and Low Code）名義の記事が出た。Dynamics 365 / Power Platform / Dataverse のロードマップ情報を AI at Work roadmap へ統合し、計画が固まった時点で随時開示する方式へ移す。半期の発表タイミングまで保留されなくなる。日程は3段階である。

- 2026年9月: 新機能の AI at Work roadmap への掲載を開始し、同月から Release Plans on Learn への新規掲載を停止する
- 2026年9月〜11月: Preview / GA 期日が 2026-06-01 以降の既存項目を移行する
- 2026年11月15日: 移行を完了し Release Planner を退役させる。個人保存ビューは退役後に使えなくなる

移行先は製品とクラウド環境でのフィルター、全件または絞り込み結果の CSV エクスポート、RSS 購読、Release Communications MCP Server 経由でのデータ取り込みに対応する。製品のリリース日程・Message Center 通知・Microsoft Learn のドキュメントは変更されない。

⚠️ 移行先の URL は本ダイジェスト群が毎日巡回している `microsoft.com/en-us/microsoft-365/roadmap` と同一で、ページ表題は既に「AI at Work Roadmap」になっている。消えるのは Learn の Release Plans と Release Planner の側である。⚠️ **本日取得した Learn の Release Wave 3ページには、廃止・移行の注記が一文も入っていない。**

- https://www.microsoft.com/en-us/dynamics-365/blog/business-leader/2026/08/25/one-always-on-roadmap-dynamics-365-power-platform-and-dataverse-join-the-ai-at-work-roadmap/
- https://www.microsoft.com/en-us/microsoft-365/roadmap

## カテゴリ別まとめ

### Anthropic / Claude

- **Claude Code に約90項目の v2.1.243 が入り、組織が握れる範囲が広がった。** Anthropic が今月最大のリリースを公開し、契約単価・`/model` の並び・API キー無しのサインインを管理設定で指定できるようにした。8/22 の v2.1.240 と 8/23 の v2.1.241 が2版連続で Bug fixes のみだった後の更新にあたる（https://code.claude.com/docs/en/changelog ）
  - `modelPricing`: 組織の契約済みモデル単価と割引率を `/cost`・ステータスライン・テレメトリのコスト表示へ反映させる。従来はリスト価格しか出なかったため、費用集計が推定から実額へ変わる
  - `modelPicker`: `/model` ピッカーに出すモデルを順序とラベル付きで curate する。Vertex / Bedrock の ID 表記も指定でき、既定ラインナップへの追加と置き換えの両方ができる
  - Console アカウントでのキーレスサインイン: `/login` に「Sign in with your Console account」が加わり、API キーの発行を認めていない組織でもサインインできる
  - `promptCacheTtl` / `subagentPromptCacheTtl`: メイン会話は1時間・サブエージェントは5分といった組み合わせを、API キー利用者とクラウドプロバイダ利用者が指定できる
  - `/status` の `Skipped sources`: `managed-settings.json` などが存在しながら優先度の高い管理ソースに負けている場合、その一覧が出る
  - ⚠️ `modelPricing` と `modelPicker` はいずれも managed setting で個人設定ではない。単価表の書式と Bedrock / Vertex 経由を含むかは changelog の記載では確定できない
- ⚠️ **Sonnet 5 の $2/$10 が期間限定プロモではなく標準のリスト価格として表示されるようになった。** `/model` ピッカーと同梱の `claude-api` skill の両方で扱いが変わっており、試算の前提に「いつか元に戻る価格」を置いていた場合は引き直しになる
- v2.1.243 には運用の挙動を変える修正も入った。API がレスポンスを開始しない場合、従来は10分以上無音のままだったが約3分でタイムアウトして1回リトライし `API Error: No response from API` を表示する。sandbox の Bash ツールのプロンプトは許可ネットワークホストを列挙しなくなり、未列挙のホストへも試行して都度承認を求める形に変わった。Windows でクロスセッションメッセージング（`SendMessage` / `ListAgents`）が使えるようになり、切断したリモート MCP サーバーが再接続しない不具合と `/resume` の直近50件制限も解消された
- `/usage` に Loops の内訳（ループごとの実行回数・総トークン・1回あたりトークン・最終実行）が加わり、暴走した `/loop` タスクを特定できるようになった。`/tasks` とエージェント詳細ダイアログには各サブエージェントが動いたモデルと effort が出る
- 配布まわりも縮んだ。ネイティブインストールと自動更新のバイナリが zstd 圧縮になり **Linux x64 で約340MB → 約75MB**、コードのオンデマンド読み込みでセッションあたり約40〜70MB のメモリ削減が入っている
- v2.1.245（8/25）は1項目のみで、glibc 2.44 を積むディストリビューション（Arch Linux・CachyOS・Fedora Rawhide）の起動時クラッシュを修正した
- ⚠️ **npm の `stable` は 2.1.231 のままで、`latest` との差が14版に開いた**（前日10版）。`dist-tags` は `{stable: 2.1.231, latest: 2.1.245, next: 2.1.245}` で、v2.1.243 の Bedrock 系・sandbox 系の修正も v2.1.245 の Linux 起動クラッシュ修正も stable 固定の環境には届いていない。v2.1.242 は npm にだけ存在し changelog にも CHANGELOG.md にも無い（5例目）、v2.1.244 はどちらにも無い
- **Claude の memory が chat と Cowork で1つになり、中身を開いて直せるようになった。** Anthropic が 8/25 に公開し、Cowork がクラウドでタスクを走らせるときに chat 側で覚えた内容を使えるようにした。更新方式も会話終了後の要約から会話中の逐次更新へ変わっている（https://claude.com/blog/claudes-memory-works-everywhere-and-you-decide-whats-in-it ）
  - Topics 設定に保存済み項目が一覧で並び、1件ずつ読み・編集・削除ができる。1箇所直すと以後の全会話に反映される
  - 既定で除外: 健康・人種・民族・宗教的信条・政治・ジェンダーアイデンティティ。オプトインすれば含められるが、保存のたびに通知が出て、オプトイン以前に遡っては取らない
  - 恒久的に除外: 社会保障番号・政府発行 ID・犯罪歴・移民ステータス。オプトインしても対象外である
  - プラン差: Free / Pro / Max は web・desktop・mobile で既定オン。⚠️ **Team / Enterprise は管理者が組織として可否を決め、個人側は有効化するまでオフ**である
  - ⚠️ 本発表に Claude Code への言及はない。統合の対象は chat と Cowork の2面にとどまる
- `support.claude.com` の Release Notes が19日ぶりに動き、8/25 付けで memory の項目が最上位に入った（前回最上位は 8/6 の skill / plugin セキュリティスキャン beta）。Claude Platform の API release notes は 8/20 の Python SDK v1.0 が最上位のままで6日間新規がない
- モデル退役ページに新規の告知はない。現行モデルはすべて Active で、暫定退役日のうち最も近いのは `claude-sonnet-4-5-20250929` の 9/29 以降だが、いずれも「not sooner than」表記で確定日ではない
- ⚠️ **二次サイトの「Anthropic が投資家に $30兆超の売上見通し」は桁が3桁違うため採らない。** Bloomberg / CNBC / TechCrunch が 8/17 に報じた確立値は7月末時点の年換算 run-rate が $650億、2026年着地見込みが $1,000〜1,200億である
- 既報の期限: Claude Code の週次上限50%増は **8/31 まで**（Pro / Max / Team とシート課金の Enterprise が対象。Free と従量課金 Enterprise は対象外）

### Microsoft 365 Copilot / Copilot Studio

- **M365 Copilot Release Notes に「August 25, 2026」バッチが出た。** Microsoft が2週間ぶりに更新し、節構成が7本から **11本**、項目が12から **19** に増えた。対象期間は 8/11〜8/25 で、2026年後半では最大のバッチにあたる（https://learn.microsoft.com/en-us/copilot/microsoft-365/release-notes ）
  - Copilot Notebooks の参照ソース拡張: Outlook メール（Roadmap 564910）と Teams 会議（560706）を知識ソースに取れる。会議は文字起こし・メモ・チャット・共有ファイルまで含み、8/13 の Markdown / TXT / RTF 対応に続く2段目である
  - Web チャットと Work チャットの統合: タブ切り替えが廃止され、チャット UI 左上の Work IQ ボタンで業務データへのアクセスを切り替える（既定はオン）
  - Excel の Edit with Copilot が Python 実行に対応し、統計・シミュレーション・高度な可視化の結果をブックへ直接出力する。既存のセキュリティと実行制御はそのまま効く
  - Word のモデルメニューに Sonnet 5 が入り、既定の推論レベルが引き上げられた
  - ほかに Viva Engage のプライベートコミュニティとイベントがグラウンディング対象に加わり（515144・閲覧権限のある範囲のみ）、Copilot Search の右ペインから Copilot Chat を使え（537281）、Researcher のモデルとモードをチャット内で選べるようになった。PowerPoint はプレゼン作成時にメールを参照でき（555888）、PowerPoint Live の参加者がスライド上のテキストの解説を求められる（557256）。クラシック Outlook for Windows のチャットから会議のスケジュール・会議室予約・アジェンダ下書き・招待送信までを担う（542185・M365 Copilot ライセンス必須）
  - ⚠️ Cowork の画像生成が **ChatGPT Images 2.0** に変わっている（7/30 の一次確認時点の記載は Imagen 2 だった）
- ⚠️ **Work IQ ボタンのオン/オフの意味が Microsoft の一次2本で正反対になっている。** Release Notes は「Work data is on by default; enable or disable work data access as needed by selecting the button」と書き、`which-copilot-for-your-organization` は「オフのとき Entra アカウントがアクセスできる結果に**加えて**インターネットの結果も表示する」と書く。前者は業務データの可否、後者は Web 結果の追加可否を切り替えると説明しており、オフにしたときの挙動が噛み合わない
  - 8/24 に「一次 vs 二次の食い違い」と記録した見立ては誤りで、食い違いは Learn の一次どうしにあった
  - ⚠️ 突合先の `support.microsoft.com` は `EGRESS_BLOCKED`、MC 本文の一次である `mc.merill.net` も19日連続で拒否のため、第3の一次で決着させる手段が現時点でない
- ⚠️ **Copilot Tuning の一次は停止を一文も書いていない。** 停止の発効（8/20）から6日たっても `copilot-tuning-overview` は停止も退役も書いておらず、Optimization エージェントは「サポートされるシナリオ」節とテンプレート選択表の両方に現行機能として載ったままである。冒頭の Important も「Frontier 経由の提供は 2026年4月予定」で止まっている
- Copilot Studio の What's New は July 2026 節が最新のままで、8月節は作成されていない。⚠️ June 節の GitHub Copilot ハーネスは本日も `(Production-ready preview)` と書かれており、GA（8/3）から**23日連続**で反映されていない。Released Versions の Build も 2026.6.3（6/30 初出）のままで空白が8週間を超えた
- **Roadmap に掲載歴のない Copilot Studio 項目を6件回収した。** Release Communications の RSS 経路で全15件を列挙し、全 digest に一度も載っていない6件を検出した。いずれも状態は `In development` である
  - 566859 SharePoint リストのナレッジソース化: 構造化データをデータ移動なしでエージェントの根拠に使う（Preview 2026年7月 / GA 2026年9月）
  - 566998 / 562222 エージェントノードでのエージェント呼び出し: ワークフローの1ステップ内で推論・ツール呼び出し・応答を完結させる（Preview 2026年4月 / GA 2026年9月・同一内容で2件が並存）
  - 566999 フローの express mode（Preview 2025年11月 / GA 2026年11月）と 562220 ワークフローへの computer use 組み込み（Preview 2026年4月 / GA 2026年10月）
  - ⚠️ 562221 ワークフローでの MCP 準拠ツール利用は、**GA 期日 2026年6月を2か月超過**しながら状態が `In development` のままである
- ⚠️ Purview の8月節は Sensitivity labels の2件のままで Copilot 固有の項目はない。Roadmap 側で 8/21 に起票された 569612（Copilot メモリの Purview 保持・GA 2026年9月）は本日も現れていない
- ⚠️ 英語圏の「8月の新機能8件」系が挙げる Excel の `@theme-design` スキル・Excel の Power BI グラウンディング・AutoSave 無効ブックでの Copilot 利用は、本日出た August 25 バッチを含め Release Notes の全バッチに存在しなかった（**7例目の空振り**）。同記事群の「Jira / Confluence コネクタの DoD 提供開始」も該当がなく、最も近い一次は Roadmap 569212（Federated Copilot Connectors・GA 2026年9月）である

### Power Platform / ガバナンス

- Release Wave の廃止と Release Planner の 11/15 退役はハイライト3を参照
- Release Wave の3ページ（`power-automate` / `power-apps` / ガバナンス・管理）は 8/25 と完全に同一で、緑チェックの追加・期日変更・行の増減はない。期日超過は延べ6行、8月期日10件、9月期日6件、ガバナンス面12行のまま据え置きである
- 今月が GA 期日で未達の項目は2件残る。Copilot Studio の 566997（メーカー資格情報の使用ブロック・`In development`）と、PPAC の Usage ページ（Release Wave の GA 列が「Aug 2026」で緑チェック未付与）が**残り5日**で動いていない
- 課金・容量管理の4ページ（`manage-copilot-studio-copilot-credits-capacity` / `billing-credit-overview` / `billing-manage-buy-credits` / `requirements-messages-management`）は `updated_at` がいずれも 8/25 から動いていない。⚠️ FAQ の「Copilot credit はユーザーとエージェントの1回のやり取り」という定義と消費レート表（生成回答 2 / エージェントアクション 5 / テナントグラフグラウンディング 10 等）の粒度の食い違いも未解消である
- Power Platform Blog は親ページの先頭に 8/25 のロードマップ統合記事が現れたが、子カテゴリの Power Automate / Power Apps はどちらも 8/13 の PPCC 2026 登録記事が先頭のままで、統合記事が子カテゴリ側に出ない不完全レンダリングが続いている（32回目）
- Partner Center の8月アナウンスは17件のままで、8/24 付けの2件（Copilot Success Planner・FY27 の co-op 資金案内）から追記はない
- Web グラウンディングのドメイン除外は、撤回告知（記事ID 4543648）の `pubDate` が `2026-08-07T18:54:00Z` のままで、再提供の時期も条件も示されないまま19日が経過した

### GitHub Copilot / 開発ツール

- 既定モデル有効化ポリシーの本日発効はハイライト1を参照
- Copilot CLI に 8/25 の新規リリースはない。最新は pre-release の v1.0.81-9（8/24・`/model` ピッカーへのデータ保持警告表示）で、⚠️ **安定版は v1.0.80（8/14）のまま12日間据え置き**である。8/19 以降の -5 から -9 までの5版はすべて pre-release 側にとどまる
- `github.blog/changelog` の Copilot ラベルは 8/21 の Slack / Microsoft Teams 連携2本が最上位のままで、8/22 以降の追加が5日間ない。8/25 の2件（セキュリティアドバイザリからのユーザーブロック、ルールセットの push ルールへのパス例外追加）はいずれも AI 関連ではない
- OpenAI が Codex CLI の pre-release を2版公開した（`0.150.0-alpha.8`・8/24、`0.150.0-alpha.9`・8/25）。⚠️ **変更内容は未確定である。** 本文はいずれも `Release <タグ名>` の1行のみで、タグ間比較も GitHub 側が生成できず空振りした（`rust-v0.149.1...alpha.9` は 207コミット / 1,147ファイル、隣接する `alpha.8...alpha.9` でも 35コミット / 433ファイルで "This comparison is taking too long to generate" が返る）。安定版は `rust-v0.149.1`（8/24）据え置きである
- ⚠️ 二次の「`codex mcp-server` が deprecated になり Codex app server に置き換わる」は、公開日を特定できず一次でも裏が取れないため未確定として扱う（`learn.chatgpt.com` はゲートウェイ拒否継続）
- Cursor の changelog は 8/19 の Cloud Agents / Harness 更新が最上位のままで7日間動きがなく、フォーラムの Announcements も 8/17 の Origin Code Hosting のまま9日間止まっている。xAI / Grok は新規発表を検出できず **Grok 5 は未リリース継続**で、Devin も `docs.devin.ai` のゲートウェイ拒否で一次に到達できない
- `blog.modelcontextprotocol.io` は 8/22 の「The New MCP Roadmap」が最上位のままで新規はない。⚠️ **A2A の AAIF 参加は本日も未確定**で、一次3ホスト（`aaif.io` / `www.linuxfoundation.org` / `developers.googleblog.com`）のゲートウェイ拒否が続き、MCP 側の一次も A2A に言及していない
- ⚠️ `devblogs.microsoft.com/commandline` に 8/25 付けで PowerToys 0.101 が入ったが AI / エージェント関連ではない。Intelligent Terminal は 8/10 の 0.2 が最新のままである
- 期限: GitHub Spark の既存ユーザーアクセス終了（**8/31**）、モデル廃止（**9/1**）、MAI-Code-1-Flash の廃止（**9/10**）

### OpenAI

- Assistants API の停止・o3 の ChatGPT 退役・ファインチューニングの終了はハイライト1と2を参照
- **退役期限に 9月28日分が新たに判明した。** 旧 GPT スナップショット4種（`gpt-3.5-turbo-instruct`・`babbage-002`・`davinci-002`・`gpt-3.5-turbo-1106`）が停止し、代替はいずれも `gpt-5.6-terra` が案内されている。告知は2025年9月26日と1年前で、10月23日に停止する旧スナップショット12種（＋ファインチューン版5種）とは別枠にあたる。08-24 の一覧化では拾えていなかった項目である（https://developers.openai.com/api/docs/deprecations ）
- GPT-5.6 Sol の値下げ単価は一次で据え置きを確認した。入力 $4 / キャッシュ入力 $0.40 / 出力 $20、長文脈側（入力 272K トークン超）の $8 / $30、Terra $2 / $0.20 / $12、Luna $0.20 / $0.02 / $1.20 も不変で、期限の記載も「少なくとも 2026年11月21日まで」のままである（https://developers.openai.com/api/docs/pricing ）
- `developers.openai.com/api/docs/changelog` は 8/21 の2件が最上位のままで5日間追加がなく、`community.openai.com` の Announcements RSS も 8/21 の Sol 値下げ告知が最上位である。2番手は 8/18 の DevDay Exchange（応募締切 9/17・東京 10/20）
- ChatGPT / Codex changelog の8月分として挙がるのは 8/17〜8/21 の GitLab beta 対応（全 ChatGPT プランで Codex cloud に GitLab プロジェクトを接続し、issue や merge request から `@codex` でタスクを開始できる）と 8/10〜8/14 の Computer History / Linux 版デスクトップ preview で、いずれも 8/22 以降の新着ではない
- 期限: 公式 DALL·E GPT の退役（**8/30**）、GPT-5.4 / 5.4 mini が Codex（ChatGPT サインイン）から除外（**8/31**）

### Google / モデル・オープンウェイト

- Gemini API の changelog は 8/13 の Gemini 3.7 Flash GA が最上位のままで13日間動きがない。料金ページの最終更新も 8/13 のままで、3.7 Flash / 3.6 Flash はいずれも入力 $0.75・出力 $3.75（2026年12月31日まで）、2027/1/1 から $1.50 / $7.50 へ戻る記載も不変である（https://ai.google.dev/gemini-api/docs/pricing ）
- 8/25 付けの Google の AI 発表は検出できなかった。直近は 8/12 の Made by Google（Pixel 11 / Pixel Watch 5 と Gemini 機能）で、8/26 ロールアウト開始予定の Ask Gemini in Chat も既報から進展がない。`gemini-robotics-er-1.6-preview` の 8/31 停止と Gemini 3.5 Pro の GA 未ローンチ（3回スリップ）も続いている
- 8/25〜8/26 に新規公開されたオープンウェイト LLM はない。8 org で作成日降順の一覧を実行したが、8/13 の `Qwen/Qwen3.8-27B-FP8` と `deepseek-ai/DeepSeek-V4-Pro-0813` より新しいものが1件もなかった。HF の `google` org も 8/19 の TIPS v1 6本が最新のままである
- 実測（8/26・カッコ内は前日比）: `Qwen/Qwen3.8-27B-FP8` は DL **3,363,900**（+358,960）、`Qwen/Qwen3.8-27B` は DL 2,945,415（+300,189）で伸びが突出する。`DeepSeek-V4-Flash-0731` は DL 3,528,373（+254,244）、`DeepSeek-V4-Pro-0813` は DL 74,707（+11,649）で **Flash 版の約47分の1**にとどまる

### 市場データ・導入事例

- **Claude Code の業務利用 39% が GitHub Copilot の 21% を逆転した。** JetBrains が Developer Ecosystem Survey 2026 の AI コーディングエージェント編を8月に公開した。母集団は世界のプロ開発者1万5,000名超、調査期間は 2026年5月〜7月である。ツール選定の根拠に引ける直近の横断データにあたる（https://blog.jetbrains.com/research/2026/08/ai-coding-agent-adoption-2026/ ）
  - 全体: 週1回以上 AI コーディングエージェントを業務で使う開発者が **90%**、毎日使うのが 68%
  - Claude Code: 業務利用が 2026年1月の 18% から 5〜7月に 39% へ拡大し、主に使うツールとして挙げたのは 31%（利用者の約8割が主用途に転換）
  - GitHub Copilot: 1年前の 29% から 21% へ低下して首位を明け渡した。Google Antigravity は採用率 6% で横ばいだが認知は 29% → 47% へ伸びた
  - 満足度は Claude Code が CSAT 91%・NPS 54 で調査中最高、Cursor が主利用と満足度で並ぶ
  - ⚠️ 一次の `blog.jetbrains.com` はゲートウェイ拒否で本文に到達できず、数値は複数の二次系統の一致で構成した。1件の二次は 39% を「Copilot 利用者のうち JetBrains IDE で使う割合」と取り違えており、**この読み違いのまま引用しないこと**
- **清水建設が1年半で利用者 8,800名・アシスタント 8,000個超に達した。** Lightblue が 8/20 に公表した。利用者数は 2025年4月の約1,200名 → 半年で 4,700名 → 約1年半で 8,800名と推移し、社内で作成された AI アシスタントは 8,000個超が作業所・支店・本社部門にまたがって使われる。用途は技術文書の照合・社内規程の参照・書類作成・問い合わせ対応で、拡大の要因は**利用者自身が業務に合わせて作れる市民開発型の環境**にある。横展開として「生成AI事例共有会」を2回開催し延べ3,000名が視聴した。⚠️ **工数削減率と ROI の数値は公表に含まれない**ため、定量根拠ではなく到達規模と展開速度の実例として使う（https://prtimes.jp/main/html/rd/p/000000095.000038247.html ）
- **Toyota North America が50超のエージェントを本番稼働させている。** LangGraph ベースの社内基盤で、エージェント提供までのリードタイムを **6か月 → 4日**へ短縮したと LangChain のイベント Interrupt 26 の講演で明らかにした。各エージェントをカスタム開発ではなく設定ファイルとして定義し、LangSmith を全エージェント横断の可観測性基盤として製造現場の用語を借りた「アンドン」として運用する。代表例 GearPull は北米の全工場を対象にベクトルDB上の数テラバイト規模のデータを参照し約10秒で回答を返す。⚠️ **効果は「数百万ドル規模の節減」という表現にとどまり削減率も算定根拠も公開されていない**。一次はゲートウェイ拒否で、講演も7月開催のため本日の新規発表ではない
- **Nvidia の FY27 Q2 決算はまだ出ていない。** 発表は米国時間 8月26日の市場終了後で、JST では 8月27日早朝になる。会社ガイダンスは約 **$91.0B**、アナリスト40名の予想は売上 $91.85B・EPS $2.08 で、いずれも前年同期（$46.74B・$1.05）の約2倍にあたる。FY27 Q1 のデータセンター売上は $75.2B（前四半期比 +21%・前年同期比 +92%）で、ハイパースケーラーと AI クラウド／エンタープライズの比率がほぼ半々である
- 市場データ定点は IDC / MM総研 / Similarweb / NRC のいずれも新規公表を検知できなかった。参照可能な最新値は国内AI市場予測（2025年 2兆3,725億円 → 2029年 6兆8,897億円・CAGR 36.0%）、個人利用経験率 21.8%、生成AIサイト訪問シェア（ChatGPT 53.9%・Gemini 27.9%・Claude 9.2%）で据え置きである

### 企業・市場

- **Bain & Company が Claude Partner Network の Global Premier partner になった。** Anthropic が 8/25 に発表し、frontier モデルと Bain 側の変革支援を組み合わせて AI 戦略・技術モダナイゼーション・AI 対応オペレーションの3領域を対象とする。Bain 側の AI / データ / アナリティクス / アーキテクチャ / エンジニアリング専門家は1,500人超である（https://www.bain.com/about/media-center/press-releases/2026/bain-company-announces-partnership-with-anthropic-to-accelerate-clients-enterprise-ai-transformations/ ）
  - 自社導入の規模: 全社 **19,000人**に Claude.ai / Cowork / Claude Code / Claude for Excel / Claude for Microsoft 365 を展開した
  - 立ち上がり: パイロット段階でアクセス付与から数週間のうちに 7,000人超（全社の3分の1超）が実利用に至り、参加者の3分の2が Claude for Excel を使った
  - 成果として提示された数値: レガシーコードベースを含む複数のクライアント案件で **30〜50% の生産性向上**
  - 展開の型: 技術提供とオンボーディング資料・研修・ウェビナー・専門家サポートを組み合わせ、利用者フィードバック調査でガバナンスを追跡する方式を、そのままクライアントにも勧めるとしている
  - 大手戦略ファームがフロンティアモデルベンダーの最上位区分に入る動きは、エンタープライズ AI 導入の提供経路がベンダー直販から総合ファーム経由へ広がっていることを示す。⚠️ 契約金額と対象業種の内訳は公表に含まれない
- 既報: Anthropic の年換算 run-rate $650億（8/17 報道）と IPO 規模報道（8/21）、SpaceX による Cursor 買収完了（8/14・$60B）、OpenAI の CRO に Dali Rajic 就任報道（8/17）、Manus が Meta から分離（8/12）

### Apple / クラウド

- `developer.apple.com` は 8/24 の「New domain for Sign in with Apple」が最上位のままで、8/25 の追加はない。AI 関連の最新は依然 8/5 の App Store creative assets で **21日間**新規がない
- 既報: EU 向けビジネス条件2本（Core Technology Fee 廃止 → Core Technology Commission 5%／DPLA に Attachment 14。発効 2026-10-01）、iOS 27 / iPadOS 27 developer beta 4（7/20・ビルド 23G71）で GA は9月見込み
- AWS Bedrock への Anthropic モデル追加は 7/24 の Claude Opus 5 が最新のままで、8月の新規提供開始は検出できなかった

## 直近の注目予定

- **8/26（本日）**: **OpenAI Assistants API 完全停止** ／ o3 が ChatGPT から退役（API の `o3-2025-04-16` は 12/11 まで存続）／ GitHub Copilot の既定モデル有効化ポリシー発効 ／ Ask Gemini in Chat のロールアウト開始 ／ Nvidia FY27 Q2 決算（米国市場終了後・JST 8/27 早朝）
- **8/27**: Nvidia 決算の確報確認 ／ Assistants API 停止の反映確認 ／ IT Nation Connect ANZ の Microsoft セッション ／ 非推奨一覧の週次確認
- **8/29 前後**: 拡張機能 What's New・モデル可用性一覧の週次確認
- **8/30**: 公式 DALL·E GPT の退役 ／ PnP・Power CAT の週次確認
- **8/31**: Claude Code の週次上限50%増が終了 ／ GitHub Spark の既存ユーザーアクセス終了 ／ `gemini-robotics-er-1.6-preview` 停止 ／ GPT-5.4・5.4 mini が Codex から除外 ／ Claude for Government の $1/機関プログラム終了 ／ Power Automate モバイルアプリの廃止 ／ CSP Copilot Partner Council コンテストの応募期限
- **8月末（残り5日）**: Copilot Studio 566997 と PPAC Usage ページの GA 期日 ／ Release Wave の8月期日10件と持ち越し6行 ／ Anthropic が IPO を公開申請する可能性
- **9/1**: GitHub Copilot の全体験でモデル廃止 ／ MAICPP 契約の更新条項が自動発効 ／ OpenAI Daybreak でハードウェアセキュリティキー必須化
- **9/3**: Windows 365 Frontline が Windows 365 Flex へ改称
- **9/10**: MAI-Code-1-Flash が全 Copilot 体験から廃止
- **9/17**: OpenAI DevDay Exchange の応募締切
- **9/24**: OpenAI の Videos API と Sora 2 系が退役（代替モデルの提示なし）
- **9/28**: 旧 GPT スナップショット4種が退役（`gpt-3.5-turbo-instruct` / `babbage-002` / `davinci-002` / `gpt-3.5-turbo-1106`・代替は `gpt-5.6-terra`）
- **9/29 以降**: `claude-sonnet-4-5-20250929` の暫定退役日（確定日ではない）
- **9月**: AI at Work roadmap への掲載開始と Release Plans on Learn の新規掲載停止 ／ Outlook と Teams のチャット中心 UI と Work IQ コントロールの既定有効化 ／ Copilot Tuning の新体験が Public Preview ／ Copilot メモリの Purview 保持（569612）／ Federated Copilot Connectors の政府クラウド GA（569212）／ iOS 27 / macOS 27 GA ／ Defender Advantage Fund のパイロット助成の詳細公開
- **9月中旬**: Copilot デスクトップアプリの広範な展開開始
- **9月末 / 9/30**: 2026 Wave 1 の対象期間終了 ／ M365 E7 プロモーションの対象購入最終日 ／ M365 E5・E3 の CSP 割引終了
- **10/1**: Apple の EU 向け新ビジネス条件が発効 ／ CSP ソフトウェアの5%上乗せ発効 ／ M365 E7 プロモーションの新規取引停止 ／ Ask Gemini in Chat のプロモーション上限が終了
- **10/15 以降**: `claude-haiku-4-5-20251001` の暫定退役日（確定日ではない）
- **10/16–11/11**: OpenAI DevDay Exchange 8都市（**東京は 10/20**）／ **10/20〜22**: SMB Copilot Partner Council イベント（NYC）／ **10/25〜30**: PPCC 2026
- **10/23**: OpenAI のレガシースナップショット12種とファインチューン版5種が退役
- **10月**: Anthropic の IPO 予定（$2T 超の評価額を目標と報道）
- **11/1**: パートナー特典の有効期限がオファー購入日基準へ移行
- **11/15**: Release Planner の退役と AI at Work roadmap への移行完了
- **11/21**: GPT-5.6 Sol の暫定値下げが有効とされる期限
- **11/24 以降**: `claude-opus-4-5-20251101` の暫定退役日（確定日ではない）
- **11/30**: OpenAI Evals プラットフォーム・Agent Builder・`v1/prompts` が退役
- **12/1**: OpenAI の GPT Image 系（`gpt-image-1-mini` / `gpt-image-1.5`）が退役
- **12/2**: EU AI Act の生成コンテンツ標識義務の猶予終了
- **12/11**: `gpt-5-2025-08-07` 系と `o3-2025-04-16` / `o3-pro-2025-06-10` が退役
- **12/31**: Gemini 3.7 Flash の導入価格終了（$0.75/$3.75 → $1.50/$7.50）／ Copilot in 30・M365 E3 プロモーション・Purview Suite 50%オフの提供終了
- **12月**: Copilot Tuning の新体験が GA
- **2027/1/6**: OpenAI のファインチューニング新規ジョブ作成が全面終了
- **2027/1/20**: OpenAI の旧 audio / realtime / transcription 系が退役
- **2027年6月末**: Frontier Partner バッジの廃止

## 改善メモ

- **ソース間の日付の食い違い**: Claude Code v2.1.243 の公開日を Master は 8/24、industry は 8/25 と書いている。npm の `dist-tags` 実測（8/26）は両ソースとも `latest: 2.1.245` で一致するため版数に争いはなく、公開日のみ確定できない。本サマリーは日付を断定せず「8/25 に v2.1.245 が追随した」点だけを採った
- **Copilot B-046 起票**: Release Wave 廃止に伴い、計画系ソース3本を AI at Work roadmap へ統合する提案である。監視方式そのものが9月以降に前提を失うため、11/15 までに巡回先の入れ替えが要る
- **Copilot B-047 起票**: Release Communications の RSS 経路を Feature ID 単位取得のプライマリに追加する提案である。`features` エンドポイントの HTTP 204 は 8/25 から継続する一方、同ホストの `/rss` は HTTP 200 を返すことが確認され、本日の未掲載6件の回収はこの経路で成立した
- **Master B-045 起票**: Claude Code Changelog 項の注目点に「管理設定・組織ポリシー系の追加変更」を明示する提案である。本日の `modelPricing` / `modelPicker` / `Skipped sources` が根拠にあたる
- **一次未確認のまま採用した項目が4件ある**: JetBrains の開発者調査（`blog.jetbrains.com` がゲートウェイ拒否・二次系統の一致で構成）、Toyota North America の50体運用（`www.langchain.com` 拒否）、Bain の提携詳細（`www.bain.com` と claude.com の個別記事に到達できず）、清水建設の事例（`prtimes.jp` 拒否）
- **未確定として保留した項目**: A2A / AAIF のガバナンス変更（一次3ホストが拒否継続）、Codex CLI の 0.150.0-alpha 2版の変更内容（本文1行・タグ間比較が GitHub 側で生成不能）、`codex mcp-server` の deprecated 化（公開日を特定できず）、Grok 4.7 の観測（公式未確認）
- **障害の変化**: industry で **Google News RSS（`news.google.com`）がゲートウェイ拒否として新規登録**された。`daily-sources.md`「最優先」の筆頭で、ブロック中4媒体（TechCrunch / The Verge / ITmedia AI+ / テクノエッジ）の間接取得経路も同時に失われ、最優先9ソースの拒否は8件目になった。あわせて `hnrss.org` / `www.langchain.com` / `blog.jetbrains.com` / `www.bain.com` / `prtimes.jp` の5ドメインも新規登録された。Master は新規障害なし・復旧なしである
- 継続提案は Master 25件（最多: B-013 許可ドメイン追加・29回目）、Copilot 29件（最多: B-011 Power Platform Blog のトピック記事照合・37回目）、industry 5件（最多: B-004 取得方法欄の WebSearch 優先化・58回目）
