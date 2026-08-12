# AI News Daily Summary — 2026-08-13

木曜は、本サマリーが自ら書いた記録の訂正が2件重なった日である。「一次未確認・8/7 ローンチ」としていた Grok 4.6 は実際には 8/12 公開で、同日から Cursor で入力 $2 / 出力 $6 で使える。「未公開」としていた Qwen3.8-Max の重みは 8/8 に商用利用可のライセンスで出ていた。どちらも一次確認の手順そのものに原因があり、ソース側が改善提案を出している。Microsoft 側は M365 Copilot の Release Notes が13日ぶりに新バッチを載せ、8月の変更を一次で追える状態に戻った。GitHub は Agent Plugins 1.0 を Copilot 全面で GA にし、プラグインの統制点を `managed-settings.json` へ寄せている。

## 今日のハイライト

### 1. Grok 4.6 は 8/12 公開で Cursor から初日に使える — 「8/7 ローンチ・一次未確認」という記録は誤りだった

**要点**: SpaceXAI が Grok 4.6 を 8/12 に公開し、Cursor が同日に提供を始めた。GPT-5.6 Sol と同点の指数値が入力 $2 / 出力 $6 で使える。フロンティア級の選定は性能比較から、同性能内の価格比較へ移る。

**詳細**: Grok 4.6 は Grok 4.5 の後継で、長時間動くエージェントと視覚的・対話的な制作物を重点に置く。Artificial Analysis Intelligence Index は **61** で GPT-5.6 Sol と同点、Claude Fable 5 とは1点差である。パラメータ規模は 1.5T で、改善は SFT と RL が主体とされる。Cursor 側の条件は次のとおり。

- 価格: 入力 $2 / キャッシュ入力 $0.50 / 出力 $6（Fast は $4 / $1 / $12）
- effort: `xhigh` / `high`（既定）/ `medium` / `low` の4段
- 提供面: デスクトップ・cloud agents・iOS・CLI・SDK。個人／チームプランは初週のみ使用量2倍
- 併存: Grok 4.5 は継続提供され、Composer も日常コーディング向けとして残る

⚠️ 本サマリーは 08-12 に「二次サイトは 8/7 ローンチと書くが、`x.ai` / `docs.x.ai` / `openrouter.ai` がゲートウェイ拒否で裏取り経路がない」と記録していた。実際の公開は 8/12 で、Cursor 公式フォーラム（投稿者は Cursor スタッフ）と複数の二次報道が一致している。SpaceX による Anysphere 買収後、xAI と Cursor が同一告知内で「together with SpaceXAI」と共同リリースを名乗る形はこれが初の確認になる。

- https://forum.cursor.com/t/grok-4-6-is-now-live/168189
- https://cursor.com/docs/models/grok-4-6
- https://www.unite.ai/spacexai-launches-grok-4-6-for-long-running-agents/

### 2. Qwen3.8-Max の重みは 8/8 に公開済みだった — 「未公開」という記録が5セッション続いていた

**要点**: Qwen3.8-Max の重みは `Qwen/Qwen3.8-2.4T-A95B` として 8/8 に公開されていた。2.446T パラメータが商用利用を許すライセンスで入手できる。8/16 の公開期限を待つという前提は消え、既に手元で動かせる段階にある。

**詳細**: Hugging Face の API で一次確認した。BF16 版と FP8 版の2本がいずれも公開・非 gated で、`createdAt` は 2026-08-08、`lastModified` は 2026-08-12 である。仕様は次のとおり。

- 規模: safetensors は各 213 シャード、`safetensors.total` が 2,446,182,725,504（≒2.446T）でアクティブ 95B の MoE という既報の仕様と一致する
- 構成: `config.json` は 92 層・512 エキスパート・アクティブ10・語彙 248,320
- コンテキスト: `max_position_embeddings` は **262,144** で、API 版が謳う 1M とは異なる
- ライセンス: `license_name: qwen3.8-max` の独自ライセンスで、使用・改変・再配布・ホスティング・ファインチューニング・商用販売を許諾したうえで、著作権表示の保持と商用利用時の条件を課す MIT 派生の書き方になっている
- 第三者量子化: `unsloth/Qwen3.8-2.4T-A95B-GGUF` と `RadixArk/Qwen3.8-2.4T-A95B-NVFP4` が出ている

⚠️ 見落としの原因はリポジトリ名の推測にある。08-08 以降のセッションは `Qwen/Qwen3.8-Max` と `Qwen/Qwen3.8-27B` を直接叩き、401（存在しないリポジトリと同じ応答）を根拠に「未公開」と判定していた。実際の公開名は仕様を含む `Qwen3.8-2.4T-A95B` 形式で、org 一覧を取れば初日に検出できていた。なお Qwen3.8-27B は現在も未公開で、Qwen org の作成日降順一覧に 8/8 の2本以外の8月分は存在しない。二次サイトは本日時点でも「HF 未公開・ライセンス未開示」と書いており、一次と食い違っている。

- https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B
- https://huggingface.co/api/models/Qwen/Qwen3.8-2.4T-A95B

### 3. Agent Plugins 1.0 が Copilot 全面で GA になった — プラグイン統制がクライアント個別から組織一括へ移る

**要点**: GitHub が VS Code・CLI・アプリ・SDK の全面で GA にし、全サブスクリプションを対象にした。統制の前提は「クライアントごとに個別設定」から「`managed-settings.json` で組織一括」へ変わる。

**詳細**: 8/12 の Changelog である。08-08 収録の Agent Plugins 1.0.0 仕様公開（8/6）に対し、提唱側の GitHub が自社クライアントを揃えた形になる。標準化される構成要素は3種である。

- skills: プラグインに同梱するエージェント能力
- MCP サーバー: ツール統合とその設定
- Copilot 固有機能: カスタムエージェント・コマンド・ルール・フック・拡張。可搬性のため `com.github.copilot/` 名前空間に格納する

既定のカタログは **Awesome Copilot marketplace** で、VS Code・Copilot CLI・Copilot アプリで既定有効になる。Business / Enterprise の管理者が `managed-settings.json` から設定できるのは次の3点である。

- `enabledPlugins`: 特定プラグインの自動導入とブロック
- `extraKnownMarketplaces`: 参照先マーケットプレイスの追加
- `strictKnownMarketplaces`: 承認済みソースへ導入を限定

MCP 許可リストは URL・コマンド・名前の単位でサーバーを承認またはブロックする。08-10 収録の Codex CLI 0.147.0 が同仕様への対応第一弾だったのに対し、本件はクライアント側の実装が一巡した段階にあたる。

- https://github.blog/changelog/2026-08-12-agent-plugins-1-0-in-vs-code-copilot-cli-and-the-copilot-app/

## カテゴリ別まとめ

### Anthropic / Claude

- **Claude Code v2.1.228 が公開された**（8/11 19:50 UTC ＝ 8/12 04:50 JST）: 統制に効くのはスキル同期のセキュリティ強化で、claude.ai から同期したスキルがローカルのコマンドや MCP プロンプトを上書きできなくなった。同期経路からの実行系の乗っ取りを塞ぐ変更にあたる
  - Write ツール: 新しいモデルは既読でないファイルも上書きできるようになった（Edit ツールの規則に揃えた）
  - 修正: 内部レイアウトエラー後に再描画が止まる問題、Windows で親フォルダーから起動すると `git` / Git Bash が見つからない問題、`/model` 変更後に `/tui` が旧モデルへ戻る問題
  - 修正: Remote Control の `/resume` 中に会話タイトル・履歴が漏れる問題、セッションクリーンアップがプロジェクトのメモリフォルダを削除する問題、`SendMessage` の受信箱がクリーンインストール後に動かない問題
  - Vertex AI の資格情報が期限切れ・欠落の場合に早く失敗するようになった。⚠️ **8/14 の auto mode 既定化**へ向けた挙動変更は本リリースにも入っていない
- **self-hosted environments の条件がドキュメントで確定した**（08-08 収録の続報）: 8/6 告知の public beta について、境界の引かれ方が一次で読めるようになった。統制の前提は「自社ホストなら全部内部で完結する」ではなく「成果物は内部・会話とトランスクリプトは外部」である
  - 自社に残るもの: リポジトリのチェックアウト・ビルド成果物・シークレット・セッションが作成／変更したファイル
  - Anthropic へ送られるもの: プロンプト・応答・ツール結果。セッションのトランスクリプトは Anthropic 側に保存され、別の面から再開できる
  - 推論は Anthropic API に固定され、Amazon Bedrock・Google Cloud Agent Platform・Microsoft Foundry・LLM ゲートウェイ経由へは回せない。通信はすべて `api.anthropic.com` への outbound HTTPS で、Anthropic 側から社内への接続は発生しない
  - ⚠️ ZDR（Zero Data Retention）有効組織は利用できない。リポジトリは GitHub からのチェックアウトのみで、Claude Tag・Claude Security・Code Review は未対応である
  - runner は最初のセッションを取った時点でそのユーザーのアカウントへロックされ、約60秒ポーリングが途切れるとセッションは別 runner へ再投入される
  - https://code.claude.com/docs/en/self-hosted-environments
- Claude API release notes は 8/11 の Compliance API ローカルセッション対応が最上位のままで、8/12 の追加はない。8/10 の Sonnet 5 $2/$10 恒久化も据え置きである
- `support.claude.com` の Release Notes は 8/6 の skill / plugin セキュリティスキャン beta が最上位のままで、8/7〜8/12 の追加はない。`claude.com/blog` も 8/11 の Compliance API 記事が最新である
- 利用枠に残る期限は1つで、週次上限50%増は **8/19**（23:59 PT）までである

### GitHub Copilot

- Agent Plugins 1.0 の全面 GA（ハイライト参照）
- **JetBrains 版に Copilot memory と Ollama が入った（8/11）**: GitHub が JetBrains IDE 向けの Copilot に2機能を追加した
  - Copilot memory: エージェントチャットのセッションをまたいで情報を保持・再利用し、プロジェクトの前提や好みを毎回入力し直す必要をなくす。Copilot settings portal の Copilot Memory トグルで切り替える
  - Ollama: ローカルモデルを BYOK プロバイダーとして選べるようになり、IDE 内でプロバイダー設定とモデル選択ができる
  - 管理側は Enterprise managed settings でプラグインの可否と MCP サーバーへのアクセスをサーバー側から統制でき、権限バイパスの挙動と OpenTelemetry 設定も同じ経路で指定する
  - https://github.blog/changelog/2026-08-11-copilot-memory-and-ollama-in-github-copilot-for-jetbrains/
- MAI-Code-1-Flash の 9/10 廃止は 08-12 に収録済みである。本日は Master 側が1日遅れで検出したもので、移行先の MAI-Code-1.1-Flash が Business / Enterprise で既定オフという条件も変わっていない
- Copilot CLI は **v1.0.79**（8/10 16:19 UTC）が最新のままで、8/11・8/12 の新版も pre-release も出ていない
- 利用状況レポートのモデル別トークン内訳（8/11）と、破壊的変更2件（`allowDevToolCaches` → `allowDevToolAccess`、`sandbox.gitAuth` / `ghAuth` → `sandbox.auth.git` / `auth.gh`）はいずれも既報である
- ⚠️ Master 側は 8/11 の `github.blog/changelog` 4件のうち2件しか記録できておらず、MAI-Code-1-Flash 廃止と JetBrains の memory / Ollama を1日遅れで拾っている

### Microsoft 365 Copilot

- **Release Notes に13日ぶりの新バッチ「August 11, 2026」が入った**: Microsoft が8月分12項目を公開し、7/28〜8/11 の変更が一次で読めるようになった。7/29 バッチ以降「8月中旬見込み」と推測で扱っていた隔週サイクルが実際に戻ったことになる。節構成は7本である
  - SharePoint の Authoritative Sites（561323）: 管理者が特定の SharePoint サイトを「公式・信頼できる情報源」として指定すると、社内ニュースやポリシーが Copilot Search の結果で優先される。SharePoint 管理センターでサイトを選び「Mark as authoritative site」を実行する。グラウンディング結果の順位づけをテナント側の指定で動かせるようになった
  - extensibility（2件）: Copilot コネクタがコンテンツクロールと ID クロールを並列実行するようになり、取り込みから利用可能までの時間が短くなった（権限の正確性は維持される）。ServiceNow の Knowledge / Catalog コネクタは、従来のユーザー条件に加えて admin / knowledge manager / knowledge admin のロールに基づいてアクセス権を評価する
  - Outlook（2件）: Copilot がメールの下書き・編集・整形の最中にチャット側でコーチングを返すようになった（559418）。従来のキャンバス上での一括適用と違い、適用する提案を選べて絞り込みも指示できる。クラシック Outlook for Windows でも会議準備が使えるようになった（542186）
  - PowerPoint（4件）: Adobe Experience Manager 上の企業アセットを編集モードでの資料作成に使えるようになった（Web 516038 / Windows 516039・AEM 側の接続設定が必要）。Web アプリのホーム画面から直接作成を始められ（560537）、Web ソースを参照した作成もできる（555898）
  - Word（1件）: Copilot で文書を編集する際、OpenAI モデルに加えて Anthropic モデルを選べるようになった（558440・Web）
  - https://learn.microsoft.com/en-us/copilot/microsoft-365/release-notes
- **Copilot Credit の消費が Viva Insights の Consumption Dashboard に出るようになった（566302）**: 直属5人以上のマネージャー・Insights アナリスト・全体管理者が、Cowork と Work IQ API のクレジット消費を確認できるようになった。従量支出を把握できるのは管理センターを持つ人だけ、という前提が崩れる。ダッシュボードは既定で有効だが、⚠️ M365 管理センターの Cost Management で使用量ベース課金のセットアップを済ませていることが前提になる。テナント全体のリーダー向けアクセスは今回のリリースに含まれない。8/12 収録の Agent 365 のコスト管理と対象サービスが一致しており、制御側と可視化側が同じ2サービスで揃った形になる。Copilot Studio 側の課金は依然として別系統である
  - https://learn.microsoft.com/en-us/microsoft-365/copilot/usage-based-billing-overview-copilot-credits
- **Planner Agent が group-based の basic プランへ広がった（511820）**: M365 Copilot ライセンスを持つユーザーが、グループベースの Planner プランなら basic でも Planner Agent を使えるようになった。従来は premium プラン限定で、タスク実行や状況レポートがプラン階層に縛られていた。⚠️ MC1443514 が示す展開時期は8月下旬開始〜9月下旬完了で、Release Notes の掲載期間とは時間軸がずれている。テナントへの到達は8月下旬以降とみておくのが妥当である
- Message Center の一次取得はゲートウェイ拒否のため6日連続でできていない。⚠️ Word の Legal Agent の8月中旬 GA と、エンドユーザー資格情報で動く自律エージェントのトリガー（8月中旬）は今日も二次スニペットのみのため本文に採用していない
- M365 Roadmap の Latest announcements は 7/9 のままで、Coming soon の Researcher と Frontier 枠4件にも変化はない。ブログ側は M365 Copilot Blog が 8/5、M365 Blog 本体が 7/30、M365 Developer Blog が 8/6 で最新が動いていない

### Copilot Studio / Power Platform

- Copilot Studio の What's New は節構成が June 2026 のままで、7月節も8月節も追加されていない。⚠️ GitHub Copilot ハーネスは 8/3 に GA しているのに `(Production-ready preview)` の表記が残ったままで、未反映が10日連続になった
- Released Versions は **2026.6.3**（6/30 初出）が最新のままで、6/30 以降6週間にわたって新ビルドが出ていない。ページ本文には「毎週火曜更新」とあるが直近の火曜（8/11）も空振りで、次の定例は 8/18 である
- 課金レート表（`requirements-messages-management`）は 8/12 から記載に変化がない。内訳は次のとおり
  - 機能別: クラシック回答1 / 生成回答2 / エージェントアクション5 / テナントグラフグラウンディング10 / エージェントフローアクション13〔100アクション〕/ コンテンツ処理8〔1ページ〕
  - 生成 AI ツール: 10応答あたり basic 1 / standard 15 / premium 100 クレジット。推論モデルは二重課金になる
  - 枯渇時: カスタムエージェントは容量の 125% で無効化され、エージェントフローは新規実行のみブロックされる
- Power Platform の Release Wave（全体版）は緑チェックの追加・期日の変更・行の削除がいずれも発生せず、**5日連続で完全に同一**だった。期日超過は延べ12行のままで、8月に期日がある7件もすべて未達である。2026 Wave 1 の対象期間は9月までで残り約1か月半になる
- ⚠️ Power Platform Blog の照合で、WebSearch が上位に返した「Power Platform Developer Tools monthly release update (August Refresh)」の公開日は **2022-09-26** だった。月名だけで新着と判断すると誤検知になる（B-011 の照合で拾った初の年違い事例）。月次記事は 8/6 の July/August 合併号が最新のままである
- Copilot Studio の Release Wave ページは本日も M365 Roadmap への HTTP 301 恒久リダイレクトを返した。Power Automate / Power Apps Blog の子カテゴリページは 4/8 と 5/13 のままで、不完全レンダリングが続いている

### ガバナンス・ライセンス

- Partner Center の8月アナウンスは 8/12 と同じ9件で、本日の追記はない。直近の追加は 8/10 付のマルチテナントエージェント管理と CSP Copilot Partner Council コンテストの2件である
- 非推奨一覧に新規項目は追加されておらず、先頭は **Power Automate モバイルアプリの廃止**（2026-08-31 発効・残り18日）のままである。廃止時はアプリがストアから削除されて更新とサポートが止まるが、既存のクラウドフロー（自動・スケジュール・インスタント）は通常どおり動く。⚠️ Fluent UI (v8) コントロールの非推奨は本日も本ページに記載がない
- Microsoft Purview の `whats-new` は7月節に Copilot 関連の新規追加がなく、8月節は未作成である。Copilot in SharePoint は 8/6 の月次記事、Agent 365 Blog は 8/6 の月次記事が最新のままである

### OpenAI / Codex

- **ChatGPT の広告テストが日本を含む5カ国へ広がった**: OpenAI が英国・メキシコ・ブラジル・日本・韓国で広告を出すようになった。表示対象は Free と Go のみで、Plus / Pro / Business / Enterprise / Education は広告なしのままである。Free は使用上限と機能を下げる代わりに広告を消せる
  - 広告は応答の下にスポンサー表記付きで出て、回答内容には影響させないと明記されている。パーソナライズ有効時は現在の会話・過去のチャット・広告への反応が選定に使われるが、健康情報などのセンシティブ情報は使わないとしている
  - 日本では電通デジタル・博報堂 DY ONE・サイバーエージェントが仲介として広告の調達・配信・運用を担う
  - ⚠️ **開始時期の記載が2系統に割れている**。Master は「8/11 に5カ国へ拡大、2/9 の米国テストからの初の国外展開」とし、industry は国内報道を根拠に「5/7 に5カ国拡大を告知、日本での配信開始は 6/19、6/28 から `ads.openai.com` の Ads Manager で国内企業が直接出稿可能」とする。起点が3か月ずれるため、日付に触れる場合はどちらの系統かを併記する
  - https://www.sbbit.jp/article/cont1/185309
  - https://mlq.ai/news/openai-expands-chatgpt-ad-test-to-five-more-countries/
- **Daybreak Blue / Red が Amazon Bedrock で提供開始された（8/11）**: OpenAI と AWS が 08-12 収録の2モデルを Bedrock 上で出した。調達の前提は「OpenAI と直接契約する」から「既存の Bedrock 契約に載せる」へ変わる一方、利用審査は OpenAI 側に残る
  - Daybreak Blue: GPT-5.6 Sol を含むフロンティア汎用モデルへ、認可された防御側業務に合わせた安全機構の調整つきで到達する
  - Daybreak Red: 認可された脆弱性研究・エクスプロイト検証・セキュリティテスト向けの専用学習モデル GPT-5.6 Cyber を扱う
  - 稼働リージョンは US East（バージニア北部）のみで、利用には OpenAI の Trusted Access for Cyber 審査プログラムへの登録が要る。承認後は Bedrock コンソールか Responses API（`bedrock-mantle` エンドポイント）から呼び出す
  - ⚠️ 9/1 のハードウェアセキュリティキー必須化が Bedrock 経由の利用にも掛かるかは、本日時点で明示されていない
  - https://aws.amazon.com/blogs/machine-learning/accelerate-cyber-defense-with-openai-and-aws-daybreak-red-daybreak-blue-now-available-to-eligible-customers-on-amazon-bedrock/
- Codex CLI の pre-release は 0.148.0-alpha.9（8/12 01:35 UTC）まで進んだが、**安定版は 0.147.0**（8/7 01:41 UTC）で据え置きである
- `developers.openai.com/changelog` は `developers.openai.com/api/docs/changelog` へ 301 恒久リダイレクトするようになった。転送先の最上位は 8/7 の Daybreak エントリのままで、8/8 以降の追加はない。Announcements RSS も 8/10 の Daybreak 告知が最新である
- GPT-5.4 / 5.4 mini の Codex 除外（8/31・ChatGPT サインイン時）は既報で、移行先は `gpt-5.6-terra` と `gpt-5.6-luna` と明記されている

### Google / DeepMind

- **Made by Google 2026 で Pixel 11 系4機種と Pixel Watch 5・Pixel Tag が発表された（8/12）**: AI 面は端末内処理への寄せが中心で、クラウド側の新モデル発表はない
  - Tensor G6: TSMC 2nm 世代。TPU は演算 50% 増・メモリ帯域2倍で、端末内 AI は最大 3.5倍高速・消費電力は最大 3.5分の1になる
  - Gemini Nano 4: 上記 TPU 上で動く新しい端末内モデル
  - Gemini Intelligence: 複数手順のタスク自動実行、Chrome のページ要約、自然言語でのウィジェット生成、話し言葉を整える音声入力 Rambler を含む。動作要件はフラッグシップ SoC・RAM 12GB 以上
  - 手話をテキストに変換する SL2T が Gemini に入り、音声の代わりに手話で端末を操作できるようになる。通知シェード内では予定・フライト情報・メッセージスレッドをアプリ横断で要約する
  - 価格と時期: Pixel 11 が $899、Pixel Watch 5 が $399、Pixel 11 Pro Fold が $1,899（前世代比 +$100）。予約は 8/12 10:00 ET 開始で、出荷は 8/20 前後である
  - ⚠️ Pixel Watch 5 は Gemini を初日には載せない
- Gemini API の料金は 08-12 収録分から単価が動いていない。3.6 Flash（$1.50／$7.50）と 3.5 Flash（$1.50／$9.00）の出力単価の逆転、3.1 Flash-Lite（$0.25／$1.50）が 3.5 Flash-Lite（$0.30／$2.50）より安い関係はいずれも継続している。3.1 Pro Preview はプロンプト長に応じ入力 $2.00〜$4.00／出力 $12.00〜$18.00 である
- Gemini API の changelog は 7/30 の Gemini Robotics ER 2 public preview が最上位のままで、8月の追加はない。退役は **Imagen 4 系3本が 8/17 停止**で期限まで4日、`gemini-robotics-er-1.6-preview` は 8/31 停止である
- Gemini 3.5 Pro の GA は未ローンチが続いている。本日の Made by Google でも言及はなかった

### 資本・インフラ

- **Cognition が $40B 評価で調達交渉に入った**: Bloomberg が 8/11 に関係者の話として報じた。Devin を提供する同社は5月末に $26B（プレマネー $25B）で $1B を調達したばかりで、成立すれば3カ月足らずで評価額が50%超上がることになる。調達額は $1B 超が見込まれ、年換算売上ランレートは **$1B 近く**（前回調達時の約2倍）まで伸びている。⚠️ 初期段階の協議で条件・最終評価額は未確定であり、一次発表は出ていない
  - https://techcrunch.com/2026/08/12/ai-coding-startup-cognition-reportedly-already-in-talks-to-raise-at-40b-valuation/

### モデル / オープンウェイト

- Qwen3.8-Max の重み公開はハイライト2を参照
- Qwen3.8-27B は現在も未公開が続いている。Qwen org の作成日降順一覧で8月分は 8/8 の Max 系2本のみである
- Meta の `meta-models/Muse-Glimmer-30B`（Apache 2.0・8/10 告知）はサードパーティ量子化の積み増しが続いている
- DeepSeek が 8/6 に告知した「大幅値上げ」は、予告から7日が経っても幅・新単価・対象の課金区分・実施日のいずれも未公表である。現行 V4-Flash は入力 $0.14／出力 $0.28（100万トークン）で据え置きが続き、北京時間の平日ピーク時間帯（9〜12時・14〜18時）の単価2倍も未発動である。一次料金ページはゲートウェイ拒否のため、改定の検知は二次報道に依存している

### 開発ツール / MCP

- **Grok Bot が early beta で公開された（8/11 19:34 UTC）**: SpaceXAI と Cursor が、永続的なクラウドコンピュータ上で動く「AI の同僚」を名乗るエージェント製品を出した。ブラウザ・ファイルシステム・ターミナルを持ち、承認が要るときだけ人に戻る
  - 実行環境: 1台のクラウドコンピュータをユーザーの全 Bot が共有し、各 Bot が自分の画面を持って並列に動く。コネクタと MCP が使える場面ではそれを、無い場面では computer use を使う
  - 連携: Bot 同士がメッセージを送り合い、スレッドとグループチャットで文脈を共有し、担当を引き渡せる
  - ルーティン化: 複数システムをまたぐ手順を一度なぞらせると routine として保存し、オンデマンドまたはスケジュール実行できる
  - 対象は SuperGrok Heavy / Cursor Ultra / Cursor Teams Premium で、デスクトップと iOS から使える。Enterprise は waitlist である
  - ⚠️ **分離単位は Bot ではなくアカウント**で、置いたログイン情報とファイルは全 Bot から見える。公式がそう扱えと明記している
- Cursor changelog は 8/3 の Google Workspace Plugins が最上位のままで、8/4 以降の追加はない。Grok 4.6 のフィードバック募集スレッドは 8/12 に別途立った（長時間タスク・視覚的/対話的な制作物・Grok 4.5 や Composer との比較の3点を挙げている）
- Cognition の Devin は 8/7 の Automations Queueing Support 以降に新規の公開情報がない。Outposts の公開日は `docs.devin.ai` がゲートウェイ拒否のため依然として未確定である
- MCP 公式ブログは 7/28 の `The 2026-07-28 Specification` が最新のままで、**16日連続**で新着がない

### 市場データ

- IDC / MM総研 / Similarweb はいずれも新規公表がない。IDC の最新は2026年3月発行の Worldwide AI and Generative AI Spending Guide 2026V1（国内 AI 市場支出額は2025年 2兆3,725億円 → 2029年 6兆8,897億円・CAGR 36.0%）、MM総研の生成AI 個人利用状況調査は2025年8月時点（個人利用率 21.8%・ChatGPT 65.7%／Gemini 40.0%／Copilot 26.2%）のままである。Similarweb の生成AIトラフィックシェアも 08-03 収録分と同系統で、引用時は計測期間の明記を継続する

### Apple

- Apple Developer News の 8/12 更新は「Updates to Age Ratings for the Republic of Korea」で、AI 関連ではない。8/5 の App Store クリエイティブアセット以降、AI 関連の新規はない

## 直近の注目予定

- **8/14**: Claude Code の既定権限モードが auto mode へ（Pro / Max / Team）／ Copilot Success Planner のマイクロスキリング提供開始
- **8/16**: Alibaba が表明した Qwen3.8 重み公開の週の終わり（Max は 8/8 公開済み・27B は未公開）／ Power CAT・PnP の週次確認
- **8/17**: Claude Console 旧 Workbench 退役 ＋ 実験的プロンプトツール API 廃止 ／ Gemini API の Imagen 4.0 系3本停止 ／ Gemini in Classroom のモバイル開放 ／ MS-4005 の週次確認
- **8/18**: Copilot Studio Released Versions の次の定例更新日（更新がなければ空振り5回目）／ 拡張機能 What's New の週次確認
- **8/18〜9/8**: M365 Copilot Agent's Playbook ライブストリーム（各回 9AM PT）
- **8/19**: Claude Code 週次上限50%増の終了（23:59 PT）
- **8/20**: Pixel 11 系の出荷開始 ／ Gemini Enterprise Agent Platform の Grok 4.1 ファミリー停止（一次未確認）
- **8/22**: M365 Copilot アプリのチャット中心 UI が Deferred リングへ展開開始
- **8/25 前後**: M365 Copilot Release Notes の次バッチ（隔週サイクルどおりなら）
- **8/26**: OpenAI Assistants API 廃止 / o3 退役 / GPT-4.5 完全廃止 ／ Copilot 既定モデル有効化ポリシー発効
- **8/30**: 公式 DALL·E GPT の退役
- **8/31**: GitHub Spark の既存ユーザーアクセス終了 ／ `gemini-robotics-er-1.6-preview` 停止 ／ GPT-5.4・5.4 mini が Codex から除外 ／ Claude for Government の $1/機関プログラム終了 ／ Power Automate モバイルアプリの廃止 ／ CSP Copilot Partner Council コンテストの応募期限
- **8月下旬**: Planner Agent チャットの basic プラン展開開始（MC1443514・9月下旬完了）
- **9/1**: GitHub Copilot の全体験でモデル廃止 ／ OpenAI Daybreak 全アカウントでハードウェアセキュリティキー必須化
- **9/2**: Windows 365 Frontline 名称での購入最終日 ／ **9/3**: Windows 365 Flex へ改称
- **9/10**: GitHub Copilot の MAI-Code-1-Flash 退役
- **9/30**: 2026 Wave 1 の対象期間終了 ／ M365 E7 プロモーションの対象購入最終日 ／ M365 E5 / E3 の CSP 割引終了
- **10/1**: E7 プロモーションの新規取引停止 ／ OpenAI 対 Apple の営業秘密訴訟の審尋
- **10/20〜22**: SMB Copilot Partner Council イベント（ニューヨーク・当選20社）
- **10/27〜29**: Power Platform Community Conference 2026（MGM Grand ラスベガス）
- **11/1**: パートナー特典の有効期限がオファー購入日基準へ移行
- **12/2**: EU AI Act の生成コンテンツ標識義務、8/2 以前に市場投入済みシステムへの猶予終了
- **12/31**: M365 E3 プロモーション ／ Copilot in 30 ／ Purview Suite 50%オフの提供終了
- **8月中旬**: Word の Legal Agent GA（二次のみ）／ OpenAI の公開 S-1 掲載見込み
- **9月**: iOS 27 / macOS 27 GA ／ App Store の Social Media 年齢レーティング回答が必須化 ／ auto mode の既定化を Enterprise・API・各クラウドへ拡大予定
- **時期未定**: ドメイン除外の再提供 ／ Cowork 1 の提供開始 ／ Copilot Studio What's New への7月・8月節の追加とハーネス GA の反映 ／ Fluent UI (v8) コントロールの廃止日 ／ Bedrock Agents Classic の提供終了日

## 改善メモ

- 本サマリーの訂正2件: ①「Qwen3.8-Max / 27B の重みは未公開」（08-12 まで記載）は Max については誤りで、8/8 に公開済みだった。②「Grok 4.6 は二次サイトが 8/7 ローンチと書くが一次確認できていない」（08-12 記載）も誤りで、実際の公開は 8/12 である。いずれも本日分で訂正した
- Master: 新規提案2件を出した。B-032（HF の重み公開判定でリポジトリ ID の直接指定をやめ、org 一覧 API を一次手順にする）と B-033（`developers.openai.com/changelog` の 301 転送先へソース定義を差し替える）である。継続提案は11件で、最多は B-013（403の2分類記録・17回目）である
- Copilot: 新規提案なし。継続提案は17件で、最多は B-011（Power Platform Blog のトピック記事照合・25回目）である。⚠️ その B-011 の照合が初めて年違いの誤検知を拾った（2022年9月の記事を「August Refresh」の名で上位に返した）
- industry: 新規提案なし。継続提案は6件で、最多は B-004（取得方法欄の WebSearch 優先化・45回目）である
- ⚠️ 提案番号の重複が続いている。本日の Master B-032 は Copilot が 08-12 に採番した B-032（Agent 365 ブログの登録）と番号が重なる。台帳がソースごとに独立しているため、横断参照の際はソース名を添える必要がある
- ソース間の矛盾: ChatGPT 広告の開始時期が Master（8/11 に5カ国拡大）と industry（国内報道ベースで 5/7 告知・6/19 日本配信開始）で3か月ずれている。本サマリーでは両論併記した
- ソース間の重複: Copilot for JetBrains の memory / Ollama は Master と industry の両方にあり、管理者統制の記述が厚い industry 側をベースにした。Grok 4.6 は Master、Grok Bot は Master のみで扱われている
- 一次に無い数値の不採用（Copilot）: 日本語コミュニティ記事が Copilot Credit の単価を「$0.01 / クレジット」「キャパシティパック $200 で25,000クレジット/月」と書いていたが、Learn 側にあるのは消費レートだけで USD 価格は 403 の PDF にしかない。採用していない
- 障害の変化（Master）: `developers.openai.com/changelog` は WebFetch 503 → `curl` で 301 と判明した。5xx 時に `curl` を挟む B-029 が実効を示した2例目にあたる
- 障害の変化（Copilot）: `learn.microsoft.com` の WebFetch が4 URL で HTTP 503 を返した（同一セッションの `curl` と Learn MCP はいずれも成功、数分後の再試行で 200 に復帰）。8/11 に `www.microsoft.com` で観測した WebFetch 層の一時的失敗と同型である
- 障害の変化（industry）: `www.cnbc.com` / `www.watch.impress.co.jp` / `digiday.com` の3ドメインをゲートウェイ拒否として新規登録した
