# AI News Daily Summary — 2026-08-23

日曜は、払っている金額の前提が3系統で動いた日である。Claude Code v2.1.239 が、プロキシ経由 Bedrock で課金 API 呼び出しが黙って倍増する不具合を直し、心当たりのない請求増はバグだったと確定した。OpenAI は GPT-5.6 Sol を入力 -20% / 出力 -33% で下げたが、11/21 までの暫定措置である。Copilot 側では、統制の外にあった Copilot メモリが Purview の保持ポリシー対象へ入る計画が Roadmap に現れた。MCP はリードメンテナ2名が25日ぶりに公式ロードマップを出し、エージェント ID とサーバー起点イベントを優先領域に置いている。

## 今日のハイライト

### 1. Claude Code v2.1.239 が Bedrock の二重課金を修正した — 心当たりのない請求増は仕様ではなくバグだった

**要点**: Anthropic が 8/21 に **v2.1.239** を公開し、プロキシ経由 Bedrock で課金 API 呼び出しが毎ターン倍増する不具合を直した。US 限定推論の 1.1倍割増も `/cost` に載り、表示値と実額のズレが2系統とも消えた。

**詳細**: v2.1.239 は約65項目の大型リリースで、8/22 の v2.1.240 は bug fixes のみである。費用に効くのは2点ある。

- 二重課金: レスポンスの `Content-Type` ヘッダーを落とすプロキシの背後で Bedrock のストリーミングが失敗し、毎ターン非ストリーミングで再実行されて課金対象の API 呼び出しが **2倍**になっていた。Bedrock ＋ SSO プロファイル ＋ `awsAuthRefresh` の構成が HTTPS プロキシ下で起動時にハングする問題も、資格情報の事前チェックが `HTTPS_PROXY` を尊重する形で直った
- 費用表示: `/cost`・ステータスライン・`--max-budget-usd` が、データレジデンシー Workspace に掛かる **1.1倍**の US 限定推論割増を含めて計算するようになった。一次ドキュメントによると `inference_geo: "us"` は Claude 4.6 以降で入力・出力・キャッシュ書き込み・キャッシュ読み出しの全区分に 1.1倍が掛かり、Priority Tier では1トークンが 1.1トークンとして枠を消費する。Workspace geo は作成後に変更できず現状 `"us"` のみで、旧「グローバルルーティング opt-out」の組織は `allowed_inference_geos: ["us"]` へ自動移行済みである

費用以外では次が入った。

- `/claude-api upgrade`: Python プロジェクトの `anthropic` 0.x → 1.x 移行を実行できる（8/22 収録の SDK v1.0 に対応する導線にあたる）
- Claude Code on the web: Bash 等のツールから API 以外の anthropic.com ホスト（www・docs 等）への通信がセッションのネットワークプロキシを経由するようになり、環境側の許可ドメイン設定が効くようになった
- クラウドセッション: claude.ai から同期したプラグインが `name@synced` として表示され、`claude plugin enable/disable <name>@synced` で操作でき、同名で自分が入れたプラグインを上書きしなくなった
- OpenTelemetry: `PreToolUse` フックで遅延されたツール実行が元のターンのトレースに戻り、トレースの分断が解消した
- Windows でクロスセッションメッセージング（`SendMessage` / `ListAgents`）が macOS / Linux と同様に使えるようになった。`/goal` の長時間バックグラウンド作業の再確認は 30分→1時間→2時間ごとへバックオフする

- https://code.claude.com/docs/en/changelog
- https://platform.claude.com/docs/en/manage-claude/data-residency

### 2. OpenAI が GPT-5.6 Sol を20%超値下げした — フロンティア API の単価前提が11月までの期間限定で下がる

**要点**: OpenAI が 8/21 に GPT-5.6 Sol の API 単価を入力 **$5 → $4**・出力 **$30 → $20** へ下げた。promotional rate と明記され少なくとも 11/21 までとされるため、恒久単価ではなく「窓」として試算を引き直すことになる。

**詳細**: 内訳は100万トークンあたり入力 $5 → $4（-20%）、出力 $30 → $20（-33%）、キャッシュ入力 $0.50 → $0.40（-20%）である。適用範囲は従量課金 API・Codex クレジット・対象の ChatGPT Work プランで、Pro / Plus / Business の定額サブスクリプションは対象外である。7/30 に Terra / Luna 系の値下げと Sol の Fast モードを出して以来、Sol 本体の単価に手が入ったのは今回が初めてになる。

同日に API 側へもう1件入った。Global geography のプロジェクトで発行した API キーを接頭辞つきドメインと組み合わせると、リクエスト単位で処理リージョンを選べる。

- https://community.openai.com/t/20-price-reduction-for-gpt-5-6-sol-api-codex-credits-and-chatgpt-work/1391726
- https://developers.openai.com/api/docs/changelog

### 3. Copilot のメモリが Purview の保持ポリシー対象になる — 「メモリは統制の外」という前提が9月に崩れる

**要点**: Roadmap に **569612** が起票され、Copilot メモリを Purview のデータライフサイクル管理で保持・バージョン管理できるようになると分かった。メモリは Exchange メールボックスの隠しフォルダーにあり、保持・調査の対象外という前提が GA で変わる。

**詳細**: Feature ID 569612「Microsoft Purview: Data Lifecycle Management – Retention for Copilot Memory」は 2026-08-21 起票、状態 `In development`、GA 期日 **2026年9月**、Web、Worldwide (Standard Multi-Tenant) である。3ソースいずれも掲載歴はない。

- 対象データ: 保存されたメモリと、チャット履歴から推論された詳細の両方を含む。これらが Copilot のパーソナライズと文脈把握を支えている
- 保管場所: ユーザーの Exchange メールボックス内の隠しフォルダーに格納されると明記された。保持ポリシーの適用対象になり得る根拠がここにある
- 適用範囲: 保持とバージョン管理が効くのは非アクティブなメモリ項目で、アクティブなメモリは引き続き Copilot 体験の側が管理する
- 想定用途: セキュリティ・コンプライアンス・調査のためにメモリ項目の履歴バージョンを保全することを挙げている

⚠️ 現時点の一次は Roadmap 項目だけである。Purview の What's new にも M365 Copilot Release Notes にも記載がなく、管理者が実際に何を構成するのか（既存の保持ポリシーで拾えるのか、専用の場所が増えるのか）は読み取れない。

- https://www.microsoft.com/microsoft-365/roadmap?filters=&searchterms=569612

## カテゴリ別まとめ

### Anthropic / Claude

- **Claude Academy が一般公開された**（8/20）: Anthropic が社内の従業員向け AI 教育プログラムを外部へ開いた。中核は委任判断を扱う **4D AI Fluency フレームワーク**で、課題起点のコース・チュートリアル・演習、法務やサイバーセキュリティ等の部門別コレクション、進捗トラッキングとバッジを備える。Claude の画面内から推奨を出す Claude Academy Skill も用意されている。提供は `academy.claude.com` またはプロフィールメニュー経由である。⚠️ 料金の記載はなく、導入効果の定量値も示されていない
- **本番エージェント3 API の導入側定量値が初めて付いた**（8/20）: Anthropic が 8/19 GA の Computer Use / Skills / Files API を本番エージェントの構成として束ねた解説を出した。導入した Asteroid（医療・保険金請求）はプロンプトを変えずに**処理時間 32分→13分**、検証したワークフロー全体でコスト約30%減、完了率100% を報告している
  - Files API: 組織あたりストレージ 1TB、レート上限は従来比5倍、ファイルの自動失効あり。一度アップロードすれば ID 参照で再利用する
  - Computer Use: 1回の呼び出しで複数操作を1ターンにまとめられるようになり往復が減った。BAA の下で HIPAA 適格である
  - Skills API: 手順書・スクリプト・テンプレートを束ねたフォルダを Claude のコードサンドボックスで実行するためホスティングが不要で、バージョンを付けてリクエストに添付できる
  - 提供面: Skills API と Files API は Microsoft Foundry でも使え、Google Cloud の Vertex AI は近日対応とされる
- **Claude が de novo タンパク質結合体を15標的中14で成功させた**: Anthropic が 8/18 に技術報告を公開し、設計・プロンプト・測定データを併せて出した。48時間のセッションで Mythos Preview 26.7% / Opus 4.8 22.6% のヒット率、単一標的に絞った24時間セッションでは **35.1%** に達し、通常の設計キャンペーンの 10〜15% を上回った。15標的・1,320設計から354件の結合体を確認している。測定は Adaptyv Bio と Twist Bioscience の独立した2 CRO が、配列を改変せず異なる分子フォーマット・アッセイ条件で実施した。⚠️ Anthropic 自身が「結合体は医薬品ではない」と限界を明記しており、創薬の第一段階にとどまる
- **Anthropic の年換算売上が7月末時点で約 $650億 に達したと報じられた**: 8/21 の Bloomberg 報道（IPO 規模が SpaceX の記録に並ぶか上回る見込み）の続報にあたる。⚠️ 一次未確認である
- Anthropic の 8/22 付け公式アナウンスは検出できなかった。`support.claude.com` の Release Notes も 8/6 の skill / plugin セキュリティスキャン beta が最上位のままで、17日連続で動きがない
- 既報: Claude Code の週次上限50%増は 8/31 まで、下院民主党22名の監督書簡への回答期限は 8/24、Claude Security の Mythos 5 切り替え（8/21）

### Claude Code / 開発ツール

- Claude Code v2.1.239 / v2.1.240 の内容はハイライト1を参照。
- **npm の `next` 先行状態が解消した**: `dist-tags` は `{stable: 2.1.231, latest: 2.1.240, next: 2.1.240}` へ動いた（8/23 実測）。8/15 以降6例続いた「npm にだけ新版がある」形はいったん解消し、`stable` は 2.1.228 → **2.1.231** と3版進んで `latest` との差が10版から9版に縮んだ
- **Microsoft が Intelligent Terminal 0.2 を公開していた**（8/10・Windows Command Line ブログ）: Windows Terminal のエージェント統合フォークで、⚠️ 13日遅れの検出である
  - BYOM: Base URL と Model ID を指定して自前エンドポイントへ接続でき、Ollama 等でオフライン運用ができる
  - `/agent` コマンド: タブごとに別のエージェントを選べる（インストール済み・ポリシー許可済みから選択）
  - OpenCode が組み込みエージェントに昇格し、GitHub Copilot と並んで Agent Pane のチャット・Autofix・セッション再開に使える
  - WSL 内でエージェントを実行でき、プロファイル単位で Windows ホスト側 / ディストロ内エージェントを選べる
  - 入手は Microsoft Store・`winget install Microsoft.IntelligentTerminal`・GitHub リリースページである
- **xAI が Grok Bot の提供プランを拡大した**（8/21）: 8/11 のベータ時点では SuperGrok Heavy・Cursor Ultra（$200/月）・Cursor Teams Premium（$120/席/月）に限られていたが、SuperGrok Plus・Cursor Pro+・全 Cursor Teams プランへ広がった。それ以外のユーザーにも利用量を絞った無料トライアルが用意されている。Grok Bot は専用 VM を持つクラウド常駐型エージェントで、アプリへのサインイン・ファイル操作・ワークフロー完遂を担う。⚠️ 一次 `x.ai` はゲートウェイ拒否のため二次経由である
- **Copilot CLI は安定版が9日間更新されていない**: pre-release は v1.0.81-7（8/21 18:39 UTC）が最新のままで 8/22 の新版がなく、安定版は **v1.0.80**（8/14）据え置きである。⚠️ v1.0.81-2 / -3 / -4 の本文は4日連続で空のままで、releases 一覧・個別タグページ・`changelog.md` のいずれからも取得できない
- **Codex CLI は安定版 0.149.0 が据え置きである**（8/20 21:04 UTC）: 8/21 に pre-release が5版刻まれた（`0.150.0-alpha.2` / `-alpha.3` / `-alpha.5` / `-alpha.6`、`0.149.0-alpha.4.1` / `-alpha.7.1`）。⚠️ 本文はいずれも `Release <タグ名>` の1行のみで内容を確定できない
- Cursor の changelog は 8/19 の Cloud Agents / Cursor Harness 更新が最上位のままで、8/20〜8/22 の追加がない。フォーラム Announcements も 8/17 の Origin Code Hosting が最上位のままである
- Devin は `docs.devin.ai` のゲートウェイ拒否が続き一次に到達できない。二次では Devin Coach・Devin Review の再レビュー抑止・Slack スレッド購読による追従・Automation のキューイングが8月分として挙がるが、個別の公開日を一次で確定できないため日付なしで記録する
- `github.blog/changelog` の Copilot ラベルは 8/21 の Slack / Microsoft Teams 連携2本が最上位のままで、8/22 付けの新規エントリがない（いずれも既報）

### MCP

- **MCP のリードメンテナ2名が公式ロードマップを公開した**（8/22）: David Soria Parra と Den Delimarsky が、7/28 の仕様リリース以来25日ぶりのブログ更新で優先領域を5本立てた
  - エージェント向けメッセージング原語: request-response から脱し、サーバー起点イベント（webhook / channel）でクライアントのポーリングを不要にする。Tasks 拡張（SEP-2663）を仕様本体へ取り込む
  - HTTP ネイティブ transport の統一: 7/28 仕様を土台に、ローカルサーバーを stdio 上の Streamable HTTP で動かす形へデプロイモードを一本化する
  - エージェント ID とエンタープライズ向けセキュリティ: 手動 API キー管理を置き換える標準的なエージェント識別を進め、DPoP の採用とサブエージェントへの権限委譲のための Workload Identity Federation を OAuth / WIMSE の標準化団体と連携して固める
  - 原語の改善: ツール呼び出し結果の扱いを標準化し、ツール数が多いサーバーのスケール問題に progressive discovery で対処する
  - SDK 開発体験: 全対応言語での SDK エルゴノミクス・仕様適合テスト・ドキュメントへ投資する
- 実装側では Codex CLI が opt-in の MCP 2026-07-28 対応を 0.149.0 で入れている（既報）
- https://blog.modelcontextprotocol.io/posts/mcp-roadmap/

### Microsoft 365 Copilot / Copilot Studio

- Copilot メモリの保持ポリシー対象化（569612）はハイライト3を参照。
- **組織プロンプトの公開を管理者が委任できるようになる**: Roadmap の **569425**「Delegated prompt publishing for organization prompts」（8/18 起票・`In development`・GA 期日 2026年9月・Desktop / Web）で、個々のユーザー・Entra ID のセキュリティグループ・配布グループへ公開権限を渡せると分かった。委任された側は Prompt Lab からテナントレベルの組織プロンプトを作成・編集・削除でき、Microsoft 365 管理センターへのアクセスは不要である。管理者は従来どおり管理センター側で監視と監督を続けられる
- **Federated Copilot Connectors が政府クラウドへ GA する**: Roadmap の **569212**（8/18 起票・`In development`・GA 期日 2026年9月・Desktop / Mac / Web）は `cloudInstances` が GCC / GCC High / DoD の3つのみで、Worldwide を含まない（Worldwide 向けは 2026-05-05 の M365 Blog で公開済み）。MCP でサードパーティのソースからリアルタイムに取得し、顧客データを Microsoft 側に保存もインデックスもしない方式が規制環境の選択肢に入る。GA 時は Researcher エージェントと Microsoft 365 Chat の両方で使える
- **OneDrive Web の Copilot 強化が Roadmap に現れた**: **569215**（8/17 起票・Preview 期日 2026年8月 / GA 期日 2026年12月・Web）により、OneDrive Web のチャットからファイルの探索・データ分析・要約・ダッシュボードやプレゼンテーションの生成・結果の保存と共有までを一続きに行えるようになる
- **既報の Roadmap 2件が `Launched` へ動いた**: 567120（GCC High / DoD 向けの M365 Copilot 使用状況レポート）と 559021（Work IQ API の統合 REST エンドポイント）が 8/21 に更新された。GA 期日はそれぞれ 2026年7月・2026年6月で、既に過ぎている
- Release Notes の最新セクションは「August 11, 2026」（対象期間 7/28〜8/11）のままで、節構成7本にも増減がない。次バッチは隔週傾向どおりなら 8/25 前後の見込みである
- Message Center に本日新たに索引へ現れた MC はない。既報の MC1458470（Outlook）と MC1458472（Teams）は 8/21 に最終更新された記録が二次側に残るのみである。⚠️ `mc.merill.net` は本日も `EGRESS_BLOCKED` を返し、一次を取得できない状態が16日連続になった
- **Copilot Studio の What's New は8月節が未作成である**: July 2026 節は6項目、June 節は10項目のままで増減がない。⚠️ June 節の GitHub Copilot ハーネスは `(Production-ready preview)` のままで、GA（8/3）から**20日連続**の未反映である。ページ本体は 8/20 に編集済みのため、更新機会がありながら表記だけが取り残されている
- Copilot Studio の Released Versions は Build 2026.6.3（6/30 初出）のままで、空白が7週間と5日に達した。次の定例更新日（火曜）は 8/25 である
- Copilot Studio の Roadmap 全13件は状態・期日・件数のいずれにも変化がない。⚠️ 566997（メーカー資格情報の使用ブロック）は GA 期日が今月にもかかわらず `In development` のままで、月末まで残り8日である
- Copilot Agent Kit は 8/17 の August 2026 Update 1（タグ `CopilotStudioAccelerator-August2026.1`）から新規リリースがない。Tech Community 側も M365 Copilot Blog が 8/13、M365 Blog 本体が 7/30、M365 Developer Blog が 8/13、Copilot Studio Blog が 8/3 のままである

### Power Platform / ガバナンス

- Release Wave の3ページ（`power-automate` / `power-apps` / `power-platform-governance-administration`）は 8/22 と完全に同一で、緑チェックの追加・期日変更・行の増減がない。期日超過は延べ6行のまま（GA 列5件・Public preview 列1件）である
- ⚠️ **PPAC の Usage ページは GA 期日が今月なのに緑チェックが付いていない**: Public preview は 2026-02-13 で緑チェック済みだが、残り8日で GA 側に動きがない。8月に期日がある行は10件、9月は6件で、2026 Wave 1 の対象期間（4月〜9月）は残り約1か月である
- **Purview は7月節も全項目を突合したが変化はなかった**: 8月節は Sensitivity labels の2件のままで Copilot 固有の項目はなく、7月節も6分類・計16項目（Data Governance 2 / DLP 3 / Data lifecycle management 1 / Information Protection 6 / Insider Risk Management 3 / Shared capabilities 1）から動いていない
- Partner Center の8月アナウンスは15件のままで、8/20 付の Dragon Copilot Physician apps and agents から追記がない
- Power Platform Blog / Power Automate Blog / Power Apps Blog の3ページとも先頭は 8/13 の PPCC 2026 登録記事のままである。⚠️ 8/6 公開の月次合併号は依然として親ページの一覧に現れず、不完全レンダリングが続いている
- ⚠️ PnP 週次は本日が定例確認日にあたるが、`pnp.github.io` が `EGRESS_BLOCKED` のため本文を取得できなかった。索引では 8/10 週の Weekly Agenda が最新のままである

### OpenAI

- GPT-5.6 Sol の値下げとリクエスト単位のリージョン処理選択はハイライト2を参照。
- **ChatGPT / Codex changelog に 8/22 分が入った**: Site コラボレーションが使える環境で、オーナーが同一 Workspace のアクティブメンバーを編集者として招待できるようになった。編集者は Site のライブ DB データの読み取り・更新・バージョン保存・公開を行える。あわせて ChatGPT が会話中のローカル時刻をより正確に把握するようになり、Computer History の提供地域が拡大した。⚠️ `learn.chatgpt.com` はゲートウェイ拒否のため WebSearch 経由での確定である
- **o3 の ChatGPT 退役が 8/26 に迫る**: 08-07 に記録した期限は撤回・延期の告知がなく有効である。**対象は ChatGPT のみで API は別スケジュール**（API 側は 2026年12月まで）である。既存の o3 会話は対応する GPT-5 系モデルへ自動的に引き継がれ、複雑な推論用途の推奨代替は GPT-5.4 Thinking と o4 とされる。有料ユーザーがモデル設定から選べる状態が 8/26 で終わる
- `community.openai.com` の Announcements RSS は 8/21 の Sol 値下げ告知が最上位に更新された。8/18 の DevDay Exchange 告知（応募締切 9/17・東京 10/20）が2番手である

### Google

- **Gemini API の単価は据え置きである**: 一次料金ページを確認したところ、3.7 Flash / 3.6 Flash はいずれも入力 $0.75 / 出力 $3.75（2026-12-31 まで）で、2027/1/1 から $1.50 / $7.50 へ戻る記載も変わっていない。3.5 Flash $1.50 / $9.00、3.5 Flash-Lite $0.30 / $2.50、2.5 Flash $0.30 / $2.50、2.5 Flash-Lite $0.10 / $0.40 も前日から変化がない
- Gemini API changelog は 8/13 の Gemini 3.7 Flash GA が最上位のままで、8/14〜8/22 の追加がない（10日間動きなし）。Gemini 3.5 Pro の GA 未ローンチも継続している（6月 → 7月 → 7/17 と3度スリップ）
- 8/22 付けの Google の AI 発表は検出できなかった。直近は 8/12 の Made by Google（Pixel 11 / Gemini 機能）と、8/26 ロールアウト開始予定の Ask Gemini in Chat（既報）である
- Hugging Face の `google` org は 8/19 の TIPS v1 6本が最新のままで、DL は最大 231（`tipsv1-g14-lowres`）と依然として小さい

### モデル・料金 / オープンウェイト

- **8/22〜8/23 に新規公開されたオープンウェイト LLM はない**: `Qwen` / `moonshotai` / `deepseek-ai` / `meta-models` / `mistralai` / `zai-org` / `openai` / `google` の計8 org で作成日降順一覧を実行し、8/13 の `Qwen/Qwen3.8-27B-FP8` と `deepseek-ai/DeepSeek-V4-Pro-0813` より新しいものが1件もないことを確認した
- 実測（8/23）: `Qwen/Qwen3.8-27B` は DL **2,090,699** / likes 12,102（前日 1,726,651 / 11,912）、FP8 版は DL 2,306,777 / likes 662。`DeepSeek-V4-Pro-0813` は DL 54,566 / likes 716（前日 49,601 / 702）で、`DeepSeek-V4-Flash-0731` の DL 2,976,281 に対し約54分の1にとどまる（前日は約57分の1）
- **Business Insider Japan が2026年8月版の料金早見表を公開した**: 主要8サービスの月次早見表で、7月に新モデルの正式提供が相次いだ一方 **8月1日時点で明確な価格改定はない**とする。ドル建てサービスが多いため円安局面では実質負担が上がる点に注意を促している。⚠️ `www.businessinsider.jp` と転載先の `news.yahoo.co.jp` がいずれも本日ゲートウェイ拒否となり、本文を確認できず WebSearch のスニペットのみで記載している
- GitHub Copilot のモデル構成に追加はない。MAI-Code-1-Flash の 9/10 退役は予定どおり有効である

### 企業・市場・国内

- **Pinecone Nexus が GA になった**: 企業の独自データとワークフローを統制付きの知識層へコンパイルし、エージェントが1回の呼び出しで参照する構成にする。都度 raw ドキュメントから文脈を組み立てる RAG パイプラインの置き換えを狙っている。デプロイは顧客自身の AWS / Google Cloud / Azure 環境内で、オープンウェイトを含む任意のモデルを使え、Pinecone 側に常時のデータアクセスは生じない。対象を金融アナリスト・引受担当・弁護士・カスタマーサービスといった事業部門の実務者へ広げている。Sierra の公開ベンチ **τ-Knowledge** では、Nexus を知識層に据えたエージェントが OpenAI / Anthropic / Google のフロンティアモデルで組んだエージェントを上回り首位になったとする
  - ⚠️ **GA の日付が二次で割れている**（8/6 とする集計と、プレスリリース配信・報道が 8/18〜19 とする系統）。一次の `www.pinecone.io` と配信元 `www.prnewswire.com` がいずれもゲートウェイ拒否で確定できず、ベンチ結果もベンダー自己申告で第三者検証値はない
- 国内の市場データに新規公表はない。参照可能な最新値は IDC の国内 AI 市場予測（2025年 2兆3,725億円 → 2029年 6兆8,897億円・CAGR 36.0%）、MM総研の個人利用経験率 21.8%（2025年8月時点調査）、Similarweb の生成AIサイト訪問シェア（2026年5月時点で ChatGPT 53.9% / Gemini 27.9% / Claude 9.2%）のままで、いずれも既収録の値から動いていない
- Qiita / Zenn で厳選掲載に値する新規記事は検出できなかった。⚠️ Copilot Credit の USD 単価を具体的に書く記事があるが、一次（Learn）に存在しない数値のため採用しない
- Apple は 8/18 の EU 向けビジネス条件変更2本が最上位のままで、AI 関連の最新は 8/5 の App Store creative assets から18日間新規がない。iOS 27 / iPadOS 27 は developer beta 4（7/20・ビルド 23G71）が最新で、GA は9月（予想 9/14 前後）である
- 既報: Anthropic の IPO 規模が SpaceX の記録に並ぶか上回る見込みとの Bloomberg 報道（8/21）、Slack Code のマルチベンダー配信（Claude Code / GitHub Copilot / Devin / Vercel Agent / ChatGPT）、下院民主党22名の監督書簡

## 直近の注目予定

- **8/24**: ChatGPT Ads が欧州31市場で開始 ／ Anthropic / OpenAI が下院民主党の監督書簡へ回答する期限 ／ MS-4005 / ppweekly の週次確認
- **8/25**: M365 Copilot Release Notes の次バッチ見込み ／ Copilot Studio Released Versions の定例更新日 ／ Copilot Studio 課金・ハーネスドキュメントの週次確認
- **8/26**: OpenAI Assistants API 廃止 / o3 の ChatGPT 退役 / GPT-4.5 完全廃止 ／ Copilot 既定モデル有効化ポリシー発効 ／ Ask Gemini in Chat のロールアウト開始
- **8/27**: 非推奨一覧の週次確認 ／ IT Nation Connect ANZ の Microsoft セッション
- **8/30**: 公式 DALL·E GPT の退役
- **8/31**: Claude Code の週次上限50%増が終了 ／ GitHub Spark の既存ユーザーアクセス終了 ／ `gemini-robotics-er-1.6-preview` 停止 ／ GPT-5.4・5.4 mini が Codex（ChatGPT サインイン）から除外 ／ Claude for Government の $1/機関プログラム終了 ／ Power Automate モバイルアプリの廃止 ／ CSP Copilot Partner Council の応募期限
- **8月中**: PPAC Usage ページの GA 期日 ／ Roadmap `566997`（メーカー資格情報のブロック）と `564608`（政府クラウドの MCP ウィジェット）の GA 期日 ／ Anthropic が IPO を公開申請する可能性
- **9/1**: GitHub Copilot の全体験でモデル廃止 ／ OpenAI Daybreak 全アカウントでハードウェアセキュリティキー必須化 ／ MAICPP 契約更新条項の自動発効
- **9/3**: Windows 365 Frontline → Flex の発効
- **9月**: Copilot メモリの保持（569612）／ 組織プロンプトの公開委任（569425）／ Federated Copilot Connectors の政府クラウド GA（569212）／ 簡素化 Copilot 体験の Outlook・Teams 展開 ／ Self-serve sync connectors の GA ／ Writing Blocks・Code Blocks の GA ／ Copilot アプリのデスクトップ広範展開（中旬）／ iOS 27 / macOS 27 GA ／ OpenAI の IPO 観測
- **9/10**: MAI-Code-1-Flash が全 Copilot 体験から廃止
- **9/17**: OpenAI DevDay Exchange の応募締切
- **9月末**: 2026 Wave 1 の対象期間が終了
- **10/1**: Apple の EU 向け新ビジネス条件が発効（Core Technology Commission へ移行）／ Ask Gemini in Chat のプロモーション上限が終了 ／ M365 E7 プロモーションの新規取引停止
- **10/16–11/11**: OpenAI DevDay Exchange 8都市（東京は **10/20**）
- **10月**: Anthropic の IPO 予定（$2T 超の評価額を目標と報道）
- **11/21**: GPT-5.6 Sol の暫定値下げが有効とされる期限
- **年内**: Anthropic の新データ保持方式（顧客自身のクラウドでの30日保持）投入予定
- **12/2**: EU AI Act の生成コンテンツ標識義務、8/2 以前に市場投入済みシステムへの猶予終了
- **12/31**: Gemini 3.7 Flash の導入価格終了（$0.75 / $3.75 → $1.50 / $7.50）

## 改善メモ

- **Master B-042 起票**: `devblogs.microsoft.com/commandline`（Windows Command Line ブログ）をターミナル常駐エージェントの一次としてソース追加する提案である。Intelligent Terminal 0.2 の13日遅れ検出が根拠にあたる（同ドメインは 8/4 に到達性が回復していたが登録ソースではなかった）
- **Copilot B-043 起票**: Roadmap の Feature ID 単位の取得が MRC MCP サーバー頼みで、MCP が載らないセッションでは経路が消える。`releasecommunications` API の直接照会をプライマリに加え、製品別列挙と `created ge <前回確認日>` の横断列挙を併用する提案である
- **Master B-024 の連続記録が4日に伸びた**: Python SDK v1.0 は 8/20 付けのエントリだが、8/21・8/22 の Master セッションがいずれも同じ URL の同日ブロックから取りこぼしていた。本サマリーは 8/22 分で既に収録済みのため、本日のハイライトからは既報として外している
- **ソース間の切り口差**: Claude Code 2.1.239 は Master と industry の双方がハイライトに採った。Master は機能面（65項目の内訳）、industry は費用面（1.1倍割増と二重課金）から書いており、矛盾ではなく粒度の差とみて統合した
- **到達性の変化**: `www.businessinsider.jp` ／ `news.yahoo.co.jp` ／ `www.pinecone.io` ／ `www.prnewswire.com` ／ `www.storagenewsletter.com` の5ドメインが新規にゲートウェイ拒否となった。うち `www.businessinsider.jp` は industry の高優先登録ソースで、拒否の確認は本日が初である。⚠️ Copilot 側では MRC MCP サーバーがセッションに載らず Roadmap の Feature ID 照会が使えなかったが、これはゲートウェイ拒否ではなくセッション構成の差である
- 継続提案は Master 22件（最多: B-013 403の2分類記録・26回目）、Copilot 25件（最多: B-011 Power Platform Blog のトピック記事照合・34回目）、industry 4件（最多: B-004 取得方法欄の WebSearch 優先化・55回目）
