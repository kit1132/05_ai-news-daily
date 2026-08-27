# AI News Daily Summary — 2026-08-28

金曜は、モデルを「誰が選ぶか」の所在が3層で動いた日である。GitHub の global model policy が GA になり、Copilot のモデルは管理者が止めない限り既定で使える側へ反転した。Salesforce は Claudeforce で Slack と Agentforce の既定モデルを Claude に置き、CRM 側からモデルを選ぶ余地を外へ出した。Copilot CLI は13日ぶりの安定版 v1.0.81 で `/plugins` を削除し、MCP 2026-07-28 仕様の実装取り込み1件目になった。数字の側では Nvidia の FY27 Q2 が $96.2B でガイダンスを $5B 超え、Anthropic は Nscale と6年 $45B の計算契約を結んだ。Nvidia による Hugging Face 買収は報道が成立段階で割れている。

## 今日のハイライト

### 1. GitHub Copilot の global model policy が GA になった — 「棚卸ししていないモデルは使われない」前提が反転する

**要点**: GA 済み Copilot モデルが既定で有効に変わり、8/26 から **9/1** にかけて全 enterprise へ順次適用される。管理者が明示的に無効化しない限り新モデルが自動で使える側に回るため、モデルの棚卸しを前提に組んだ運用は 9/1 までに引き直しになる。

**詳細**: GitHub が 8/26 に「Global model policy generally available」を公開した。対象は Copilot Business と Copilot Enterprise で、適用時刻は enterprise ごとに異なる。管理者は global default policy（既定は有効）を置き、個別モデルで上書きできる。7/29 の default model enablement、7/31 の enterprise teams model policy targeting public preview に続く GA にあたる。

- モデルの状態: Enabled / Disabled / 企業チーム・アプリ・組織へ委譲 / 既定ポリシーへ委譲 の4種で、企業レベルと組織レベルの設定は階層的に継承される
- 未設定だったモデル: 「既定ポリシーへ委譲」というポリシー追随の状態へ移り、明示的に選択済みの設定はそのまま保持される
- ⚠️ 既定オンの例外: オープンウェイトモデル（DeepSeek・Kimi K2）と、GitHub がデータ保持契約を持たないモデル（Fable 5）は、global の設定にかかわらず既定で無効のままである
- GitHub は将来的に global policy の状態を推論ではなく明示的な選択にし、「Delegate to default policy」を廃止する方向を検討していると書いている

- https://github.blog/changelog/2026-08-26-global-model-policy-generally-available/

### 2. Claudeforce で Claude が Salesforce の既定モデルになった — CRM 提案の前提が「画面に AI を足す」から「Claude 側から CRM を操作する」へ移る

**要点**: Salesforce と Anthropic が Claudeforce を発表し、Claude が Slack の既定モデルと Agentforce の推論モデルになった。CRM の入口が Salesforce の画面から Claude 側へ移るため、モデル選定の議論そのものが Salesforce 環境の外側に出る。

**詳細**: 8/26 に両社が戦略提携の拡張として公表した。Salesforce のデータ・ワークフロー・業務ロジック・ガバナンスを、働く場所を問わずエージェントから安全に呼べるようにする枠組みで、基盤は MCP サーバー・API・CLI で業務データをエージェントへつなぐ AIforce である。管理者が一度接続すれば認証と権限がチーム全体へ適用され、利用者ごとの初期設定はいらない。構成は4つに分かれる。

- Salesforce in Claude: Cowork 向けプラグインで、商談準備・案件の健全性レビュー・パイプライン管理など **37 のプリビルト営業スキル**を同梱する。営業担当は Salesforce の画面を開かずにライブの CRM データを照会・更新できる
- Slack: Claude が既定モデルになり、Slackbot を含む各層の推論を担う
- Agentforce: Atlas Reasoning Engine の推論モデルとして使え、Agentforce Vibes と Agentforce Coworker を既定で駆動する。Agent Builder でも選択できる
- 配置: Amazon Bedrock 経由で Salesforce Trust Boundary の内側に置かれ、規制業種でもデータと AI ワークロードを境界内に保てる

提供時期は、Salesforce in Claude が現時点でパイロット顧客限定で、**2026年9月にオープンベータ**を予定する。⚠️ 一次の `www.salesforce.com` プレスリリースはゲートウェイ拒否で本文に到達できておらず、**対象プラン・追加料金・利用上限はいずれも未確認**である。8/25 の Bain との Global Premier 提携と合わせ、Anthropic は同月に業務アプリとコンサルの双方で販路を確保した形になる。

- https://www.salesforce.com/news/press-releases/2026/08/26/salesforce-and-anthropic-announce-claudeforce/
- https://venturebeat.com/orchestration/salesforce-just-put-its-entire-crm-inside-claude-and-says-youll-never-need-its-app-again
- https://www.cnbc.com/2026/08/26/salesforce-anthropic-partnership-claudeforce.html

### 3. Nvidia の FY27 Q2 売上が $96.2B でガイダンスを $5B 超えた — 「AI インフラ投資は減速へ向かう」前提が当四半期では支持されない

**要点**: Nvidia の FY27 Q2 は売上 **$96.2B**・データセンター $89.0B で、Q3 ガイダンスは $108.0B になった。減速の兆しで AI インフラ需要を語る余地が当面なくなり、投資見通しを前提にした試算は上振れ側へ引き直すことになる。

**詳細**: 米国時間 8/26 の市場終了後に発表された。08-27 収録時点では検索インデックスに未反映で確報値を取得できておらず、本日その宿題を閉じた項目にあたる。

- 売上は $96.2B で前四半期比 +18%・前年同期比 +106%。会社ガイダンスの $91.0B（±2%）とコンセンサスの $92.07B をいずれも上回った
- データセンターは $89.0B で前年同期比 +117%・前四半期比 +18%。StreetAccount 集計の予想 $86.33B を超えており、伸びは Blackwell Ultra 基盤の立ち上がりによる
- 粗利率は GAAP・non-GAAP ともに 75.0%、希薄化後 EPS は GAAP $2.46・non-GAAP $2.22
- Q3 ガイダンスは $108.0B（±2%）で、Jensen Huang は FY2028 の売上成長を約70%と見通した

四半期の売上に占めるデータセンターの比率は約93%で、Nvidia の業績がエンタープライズ AI 投資の代理指標として機能する構図は変わっていない。⚠️ 一次の `nvidianews.nvidia.com` / `investor.nvidia.com` / `www.sec.gov` / `www.globenewswire.com` がいずれもゲートウェイ拒否で、**8-K にもプレスリリース本文にも到達経路がない**。数値は複数の二次スニペットの突き合わせによる。

- https://www.cnbc.com/2026/08/26/nvidia-nvda-earnings-report-q2-2027-live-updates.html
- https://www.sec.gov/Archives/edgar/data/0001045810/000104581026000073/q2fy27pr.htm

## カテゴリ別まとめ

### Anthropic / Claude

- **Claude Code v2.1.247** の changelog が公開された（npm publish は 8/26 18:02 UTC で、前日は npm 先行の状態だった）。組織運用に効く変更が3系統ある
  - `spinnerTipsOverride`: `{id, text, cooldownSessions, priority}` 形式のエントリ・`tipsFile`・`label` を置けるようになり、組織が自前の tips を組み込みのものと並べてローテーションできる
  - `SendFeedback`: セッション中に問題が起きたとき Claude がフィードバック報告を起草し、利用者が `/feedback` で確認してから送れる（`feedbackDrafts` 設定で無効化できる）
  - `/claude-api cost-optimize`: 既存プロジェクトの Claude API 支出をプロファイルし、キャッシュ・トークン衛生・batch・effort・モデル選択のコストレバーを1つずつ計測しながら回す。`/claude-api` skill には Admin API のカバレッジ（organization members・invites・workspaces・API keys・rate limit reports・workload identity federation・CMEK）が加わった
  - Sonnet 5 の既定 auto-compact 窓が 1M context 全体に変わり、1M 窓のセッションは約934Kトークンではなく**約967Kトークン**で auto-compact する
  - 修正では、サブエージェントが初回呼び出しのモデル 404 で死ぬ問題（セッションの fallback チェーンを使う形へ変更し、親に返すエラーに error type・status・request id・モデル名が入る）と、hook やバックグラウンドエージェントが数MBのエラー出力を吐くと「Prompt is too long」でセッションが固着する問題が実運用に効く
  - Bash サンドボックスの後処理が dotfile 管理（nix / home-manager / stow）の `~/.claude/settings.json` シンボリックリンクを削除する問題、Bedrock / Vertex / Foundry セッションで MCP サーバーの接続失敗が Claude に伝わらない問題も直った。プラグインマーケットプレイスは制御文字・不可視文字を含む名前を拒否するようになった
- ⚠️ **npm の `stable` は 2.1.231 のまま15日間動かず**、`latest` との差は16版に拡大した（本日実測 `{stable: 2.1.231, latest: 2.1.247, next: 2.1.247}`）。⚠️ v2.1.246 で入った「第三者ゲートウェイ用の API キーが Anthropic 宛テレメトリに載る欠陥」の修正は、**stable 固定の組織に3日経っても届いていない**
- **Cowork に隔離された内蔵ブラウザが載った**。デスクトップアプリの中で Claude が自分専用のブラウザを開き、サイトの巡回・ページの読み取り・フォーム入力を代行するため、コネクタの無い社内ポータルを拡張機能なしで自動化できるようになった（8/26 公開）
  - ⚠️ 8/27 収録の Claude in Chrome とは**別物**である。Chrome 版が利用者の既存ブラウザとログイン状態をそのまま使うのに対し、Cowork 版は個人の閲覧環境から分離された領域で動き、タブ・ブックマーク・パスワードを見ない
  - ログイン情報は Chrome / Edge / Firefox からサイト単位でインポートし、**銀行・メール・SSO のサイトは既定で除外**される
  - 提供は Pro / Max / Team の macOS / Windows / Linux（beta）版へ今週から順次で、Enterprise は管理者が Organization settings で即時に有効化できる。web / モバイルから使う場合もデスクトップアプリが必要になる
  - https://claude.com/blog/cowork-built-in-browser
- **Anthropic が英 Nscale と約 $45B・6年の計算資源契約を結んだ**（8/26 報道）。米ウェストバージニア州の旗艦データセンターから約 **460MW** を借り、供給チップは Nvidia の Vera Rubin である。施設の稼働は 2027年末、Anthropic のサービスを支え始めるのは 2027年後半の見込みで、8月上旬の Volta $10B・7月の AMD $5B に続く。⚠️ 両社の公式発表は確認できておらず**二次一致**である
- **ウェルビーイング研究助成に $5M** — Anthropic が AI のウェルビーイング影響を調べる独立研究へ助成プログラムを開始した（8/25）。採択者には資金・モデルアクセス・技術サポートを提供し、成果はオープンソースの評価として公開させる。⚠️ **応募締切は 9/21**、採択者への full proposal 提出依頼は 10/5 である。一次は到達不可で二次一致
- ⚠️ **8月 Risk Report は12日連続で一次未読**である（`www.anthropic.com/aug-2026-risk-report`）。本日の二次検索で、**bioweapon の安全策分類器が約1年にわたり無効化されたまま 133,000,000 件の human-feedback 会話を処理していた**という開示が新たに判明した。既報の misalignment・化学／生物兵器の脅威モデル引き上げと合わせ、いずれも一次未読のままである
- **Compliance / 退役の定点**: Claude Platform API release notes は 8/26 が最上位のままで追加なし。`support.claude.com` Release Notes も 8/25 の memory 更新が最上位である。モデル退役ページに新規告知はなく、現行モデルは全て Active。同ページは公開モデルの退役を**最低60日前に通知する**と明記している
- **Claude Code 週次上限50%増の期限は 8/31 のまま**で、延長告知は検出できなかった。対象は Pro / Max / Team とレガシーのシート型 Enterprise で、Free と従量型 Enterprise シートは対象外である。⚠️ 一次は `x.com`（ゲートウェイ拒否）のため二次一致

### GitHub Copilot / 開発ツール

- **Copilot CLI が13日ぶりに安定版 v1.0.81 を出した**（8/27 17:10 UTC）。8/14 の v1.0.80 以降は pre-release だけが続いていた。⚠️ **`/plugins` コマンドが削除された**ため、スクリプトや手順書に書いている場合は `/plugin`・`/mcp`・`/skills` への置き換えが今日から必要になる
  - Added: plugins ダッシュボードの全ユーザー開放、**MCP 2026-07-28 仕様のサポート**（CLI / SDK / IDE / in-memory クライアント）、hooks が OpenTelemetry のトレースコンテキストを受け取り相関スパンを出せる、Windows で Entra ID 保護のリモート MCP に OS 認証ブローカー経由でサインイン
  - Added（続き）: Grok 4.6 の xhigh reasoning effort、Gemini 3.7 Flash 対応、クラッシュ・再起動後のセッション復元、`models.list` のモデルごと `infoMessages` / `warningMessages`、`copilot app` コマンド、`defaultMode` / `defaultPermissionMode` 設定、`copilot login --with-token`
  - Removed: `/plugins` コマンド、レガシーの skills ピッカー、`PLUGINS_DASHBOARD` opt-out フラグ、hooks と LSP サーバーの有効・無効トグル
  - Fixed: リポジトリプラグインがある環境で起動時に無限ロードする問題、エンタープライズ managed-settings が未知の値でポリシーを拒否する問題、非対話実行で agents / skills / MCP サーバーが落ちる問題
  - https://github.com/github/copilot-cli/releases/tag/v1.0.81
- **エンタープライズ managed settings が plugin marketplace の `autoUpdate` に対応した**（8/26 GA）。`extraKnownMarketplaces` のエントリに `"autoUpdate: true"` を置くと、対応クライアントがそのマーケットプレイス由来のインストール済みプラグインを自動更新する。対象は Copilot Business / Copilot Enterprise で、GitHub Copilot app・Copilot CLI・Visual Studio Code に効く。⚠️ 当該マーケットプレイスが `strictKnownMarketplaces` の許可リストに残っていることが条件である
- （global model policy GA はハイライト1参照）
- **Cursor の Cloud Agents が SCM 接続なしで開始できるようになった**（8/27・changelog が8日ぶりに動いた）。リポジトリピッカーで「Start from scratch」を選ぶとすぐプロンプトを書き始められ、Origin リポジトリがバックグラウンドで自動作成される。「Create repo」で名前と可視性（private / internal）を指定して永続化でき、ライブプレビューがクラウドエージェント環境をブラウザへポートフォワードする。⚠️ 公開 URL の発行には **Vercel 接続が必須**である
- **Devin の automations 関連の更新群を本日確定した**（8月分）。⚠️ `docs.devin.ai` はゲートウェイ拒否継続のため**二次一致・一次未読**で、日付も未確定である
  - キューイング: automation ごとに同時実行数の上限とキュー深度を設定でき、events テーブルでキューのライフサイクル状態を見られる。concurrency group は公開 v3 API でも使える
  - API: automations API が beta から本番 v3 API 仕様へ昇格し、セッションを `automation_id` で絞り込めるようになった。Devin Terraform provider に `devin_automation` リソースが入った
  - トリガー: GitLab の issue・issue note・push・pipeline に対応し、issue トリガーでは返信もできる。webhook を自動管理する GitLab サービスアカウント接続にも対応した
- xAI / Grok の新規発表は検出できず、**Grok 5 は未リリース継続**である。8/12 の Grok 4.6（context 50万トークン・reasoning effort 4段）から進展はない。⚠️ その Grok 4.6 は本日 Copilot CLI v1.0.81 側で xhigh effort に対応した

### Microsoft 365 Copilot / Copilot Studio / Power Platform

- **SharePoint Copilot Apps が Copilot Components に改称された**。SPFx 1.24 Beta 3 で公開プレビューに入り、GA は **2026年10月**に置かれた。⚠️ プレビュー中は Copilot ライセンス不要かつ従量課金なしで動くが、**GA 時のライセンスモデルは「10月までに確定する」としか書かれておらず、金額も課金単位も一次に存在しない**。無償で検証できる期間は残り約2か月である
  - 実装は React と標準 JavaScript ライブラリで、MCP Apps 経由で接続し、Copilot の会話にインラインまたは全画面で描画される
  - SPFx 1.24 Beta 3（2026年8月・出荷済み）: Copilot Components の公開プレビュー更新と SPFx ソリューションの React 18 対応
  - SPFx 1.24 GA（2026年10月）: Copilot Components の GA 目標時期でもあり、React 18 対応が本展開に入る
  - SPFx 1.25（2026年12月〜2027年1月）: SPFx CLI が GA して Yeoman ジェネレーターを置き換え、ナビゲーションカスタマイザーが加わる
  - https://devblogs.microsoft.com/microsoft365dev/sharepoint-framework-spfx-roadmap-update-august-2026/
- **コネクタの会話内設定**（Roadmap **569930**・8/26 起票）: メーカーが、エージェントに必要なコネクタをチャット内のサインインだけで設定できるようになる。従来の設定画面を開く操作を置き換えるもので、状態は `In development`、GA 期日は 2026年9月である
- **Release Wave 3ページに廃止・移行の注記が入った**。`power-automate` / `power-apps` / `power-platform-governance-administration` の3ページとも、冒頭の Important に「Release Plans will no longer be published starting in September 2026」と AI at Work roadmap への移行が明記された。⚠️ 8/26・8/27 の2セッションは「注記が一文も入っていない」と記録しており、**「これから止まるページが現行として載る」状態は本日解消した**
- ⚠️ **ガバナンス・管理ページで Preview 期日が2件後ろ倒しされた**。Agentic Center of Enablement の Public preview が Jul 2026 → **Sep 2026**、運用状態の異常検知が Aug 2026 → **Sep 2026** へ動いていた。行の増減と緑チェックの追加はない。⚠️ 昨日は「期日変更なし」と記録していたため、**変更が本日なのか見落としなのかは判定できない**
- ⚠️ **PPAC の Usage ページは GA 期日まで残り3日で緑チェックが付いていない**（GA は「Aug 2026」のまま）。Copilot Studio のエージェントセッション数を Power Apps のアクティブユーザー数・Power Automate のフロー実行数と同じ画面で追える唯一の管理者向け画面である
- **資格情報ガバナンスの GA も期日まで残り3日**で、Roadmap **566997**（メーカー資格情報の使用ブロック）は本日も `In development` である。⚠️ **562221**（ワークフローでの MCP 準拠ツール利用）は GA 期日 2026年6月のまま `In development` で、**超過が2か月を超えた**
- **定点は据え置き**: M365 Copilot Release Notes は August 25 バッチが最新のまま（10節・全19項目に増減なし）。Cowork のモデル一覧と What's New も 8/27 から動いていない。拡張機能 What's New に8月節は作成されず、Copilot Studio What's New も July 2026 節が最新で、June 節の GitHub Copilot ハーネスは GA（8/3）から**25日連続**で `(Production-ready preview)` の表記のままである。Copilot Studio Build は 2026.6.3 のまま空白が8週間を超え、次回定例更新日は 9/1 である
- ⚠️ **Copilot Tuning は停止発効から8日たっても一次が停止を書いていない**。`copilot-tuning-overview` は Optimization エージェントを現行機能として載せたままで、冒頭の Important も「Frontier 経由の提供は 2026年4月予定」で止まっている
- **CSP 認可要件が一元ダッシュボードに載る**（Partner Center 8/27 付）。CSP direct bill パートナーが、直接請求の認可要件の充足状況・必要な対応・期限を Eligibility Dashboard の1画面で追えるようになる。提供は direct bill パートナーへ**9月中旬までに段階展開**され、間接リセラーとディストリビューター向けの時期は今後の告知になる。本リリースは登録とセキュリティ要件を**テナント単位**で検証する
- ⚠️ **Purview 側に 569612 が現れないまま29回目になった**。8/23 に Roadmap 側で検知した Copilot メモリの Purview 保持（GA 2026年9月）は、Purview の What's new に本日も掲載がない

### OpenAI / Codex / ChatGPT

- **Codex CLI と IDE 拡張に GPT-5-Codex-Mini が追加された**。GPT-5-Codex の小型・低コスト版で、**ChatGPT サブスクリプションの枠内で最大4倍の利用量**が得られる。OpenAI は「比較的容易なソフトウェアエンジニアリング作業」と「レート上限に近づいたとき」に選ぶことを推奨している。API 提供は近日で、⚠️ 一次はゲートウェイ拒否のため二次一致である
- **Codex CLI が安定版 `0.150.0`（8/26）と `0.150.1`（8/27）を出した**。前日まで安定版は `rust-v0.149.1`（8/24）据え置きだった
  - New Features: `@` メンションで他の Codex タスクを参照でき、ターミナルからエージェントにタスクの読み取り・作成・メッセージ送信を頼める / `/copy` が全文・個別コードブロック・引用のピッカーを出す / 無名タスクに説明的なタイトルが自動で付き `/rename` が候補を提案する / 権限モードを巡回するショートカットを割り当てられ、Vim モードで `.` が直前の編集を繰り返す / **`Interrupt` hook** を新設した
  - Bug Fixes: 信頼されていないプロジェクトが `AGENTS.md` の指示を供給しなくなり、権限変更後も managed の deny-read ルールが維持される / リモート MCP の bearer トークン参照と必須サーバー起動を修正 / Windows の昇格サンドボックスと Unicode ユーザーパス配下の起動エイリアスを修正 / Amazon Bedrock モデルでの会話 compaction とマルチエージェント互換性を修正
  - `0.150.1`: リモート compaction が保持中の画像をトークン予算に算入し、必要に応じて古い画像を削る挙動が既定になった
  - ⚠️ pre-release の `0.151.0-alpha.2`〜`.6` と `0.150.0-alpha.12.2` は本文が空で、変更内容は未確定である
- **Codex changelog で3件を本日確定した**: **Appshots**（macOS の Codex アプリでホットキーによりアプリウィンドウをスレッドに添付でき、スクリーンショットと取得可能なテキストを渡す）、Codex チャットの読み取り専用共有リンク（リンクを知っていれば誰でも開ける静的スナップショットで、ツール呼び出しとシェルの入出力は含まない）、ピン留めチャットの ChatGPT デスクトップ / iOS 同期
- **Assistants API の退役が Past deprecations 区分へ移った**。08-27 の収録時点では停止済みにもかかわらず Upcoming に残っており、区分の更新を本日の宿題としていた項目である。本文にも「officially sunset on August 26, 2026」と明記された。⚠️ **一次ページの区分は停止の事実に対しておおむね1日遅行する**という観測が、この1件で裏づけられた
- **ChatGPT for Teachers が 55 校区へ拡大した**（8/26 発表）。累計で30州・100超の K-12 組織・30万人超の教職員が無料アクセスと研修の対象になる。⚠️ **16州にまたがるデータプライバシー協定**を同時に発表しており、各校区が生徒データ要件に照らして評価する共通枠組みになる。米国の認証済み K-12 教職員は **2028年6月まで無料**である
- **料金と期限は据え置き**: GPT-5.6 の単価は4日連続で変わらず（Sol は入力 $4・出力 $20、Sol の期間限定価格は「少なくとも 2026年11月21日まで」）。残る退役期限8件も4日連続で撤回・延期・新規追加なしで、直近では **9/24** が次の期限である。API changelog は 8/21 の2件が最上位のまま7日間追加がない
- ⚠️ **`platform.openai.com/docs/changelog` は 403 ではなく 301 で `developers.openai.com/api/docs/changelog` へ転送されていた**。2026-04-14 以降「403 継続」と記録してきたのは誤りで、`developers.openai.com/codex/models` も 308 で `learn.chatgpt.com/docs/models` へ移設されている

### Google

- **Gemini Omni Flash が GA になった**（8/27）。モデル ID は `gemini-omni-1.1-flash` で、既存動画の延長と2枚の画像の間を遷移する動画の生成に対応した。**resolution パラメータ**を新設し 360p〜4K を出力できる（1080p と 4K はアップスケーリング）。⚠️ **旧 `gemini-omni-flash-preview` エンドポイントは 2026-09-30 に廃止される**
- **Gemini API 料金はまた更新日だけが動いた**。一次ページの最終更新が 8/26 → **8/27 UTC** へ変わった一方、単価は全モデルで据え置きである（3.7 Flash / 3.6 Flash は入力 $0.75・出力 $3.75、3.5 Flash $1.50 / $9.00、3.1 Pro $2.00 / $12.00）。値上げの起点が「2026年12月31日まで」から「2027年1月1日から」という書き方へ変わったが、指す日付は同じである
- 既報の据え置き: Gemini 3.5 Transcribe 2種は GA で料金の記載なし、Ask Gemini in Chat のプロモーション枠は 10/1 まで、`gemini-robotics-er-1.6-preview` は 8/31 停止、**Gemini 3.5 Pro GA は未ローンチ継続**である

### オープンウェイト / 資本

- ⚠️ **Nvidia による Hugging Face 買収の報道が成立段階で割れている**。The Information は 8/26 に **$12.9B** での合意成立と報じたのに対し、Business Insider は署名済みの契約には至っておらず破談の可能性が残ると報じ、CNBC の取材源も「継続中の協議の一部であることは確認できる」水準にとどまる。両社ともコメントを出していない。金額は 2023年8月 Series D 時点の評価額 $4.5B の約3倍で、**当時のラウンドには Nvidia 自身が出資していた**。成立すればオープンウェイトを「特定ベンダーに依存しない選択肢」と位置づけてきた説明が見直しの対象になるため、確度が定まるまで金額・時期を提案に引かない
- **`zai-org/GLM-5.3-Flash-BF16` が新たに出ていた**（作成 8/25 / 最終更新 8/27 / DL 24 / likes 36）。8/26 公開の GLM-5.3-Flash は FP8 主体だったため、BF16 版の追加公開にあたる。⚠️ `createdAt` は 8/25 で前回チェック以前のため、**`lastModified` 降順を併用していなければ本日も検出できていなかった**
- 実測（前日比）: `Qwen/Qwen3.8-27B-FP8` DL 3,974,725（+177,187）、`Qwen/Qwen3.8-27B` DL 3,457,687（+159,118）、`DeepSeek-V4-Flash-0731` DL 3,959,575（+102,435）。8/26 公開の新規2本は `Qwen3.8-Flash-Next` が DL 4,810（+2,259）/ likes 3,916 に対し、⚠️ **`GLM-5.3-Flash` は likes 1,277（+595）と伸びているのに DL が 34 とほぼ動いていない**（約321GB / FP8 主体という規模が効いていると見られるが公式の言及はない）
- `moonshotai` / `mistralai` / `meta-models` / `openai` / `google` の5 org に新規はない

### MCP / エージェント標準 / その他

- **MCP 仕様 2026-07-28 の実装側の取り込みが本日1件進んだ**。Copilot CLI v1.0.81 が CLI / SDK / IDE / in-memory クライアントで同仕様に対応したもので、仕様公開が 7/28 なので**約1ヶ月遅れの取り込み**にあたる。`blog.modelcontextprotocol.io` は 8/22 の「The New MCP Roadmap」が最上位のままである
- `developer.apple.com` は 8/26 の「Surprise and shine」（**9/9 10:00 PT** の特別イベント告知）が最上位のままで、iOS 27 / macOS 27 GA は例年どおりこのイベント後の見込みである
- **市場データ定点は更新なし**。IDC・MM総研・NRC・Similarweb のいずれも新規公表を検知できなかった。参照可能な最新値は IDC の国内AI市場予測（2025年 2兆3,725億円 → 2029年 6兆8,897億円・CAGR 36.0%）と MM総研の個人利用経験率 21.8%（2025年8月時点）である
- AWS Bedrock の Anthropic モデル追加は 7/24 の Claude Opus 5 が最新のままで、8月の新規提供開始は検出できなかった

## 直近の注目予定

- **8/29 前後**: 拡張機能 What's New・モデル可用性一覧の週次確認
- **8/30**: 公式 DALL·E GPT の退役 ／ PnP・Power CAT の週次確認
- **8/31**: Claude Code の週次上限50%増が終了 ／ GitHub Spark の既存ユーザーアクセス終了 ／ `gemini-robotics-er-1.6-preview` 停止 ／ GPT-5.4・5.4 mini が Codex から除外 ／ Claude for Government の $1/機関プログラム終了 ／ **Power Automate モバイルアプリの廃止** ／ CSP Copilot Partner Council コンテストの応募期限
- **8月末（残り3日）**: Copilot Studio 566997 と PPAC Usage ページの GA 期日 ／ Release Wave の8月期日と持ち越し3行 ／ Word の Legal Agent GA〔二次のみ〕 ／ Anthropic が IPO を公開申請する可能性
- **9/1**: GitHub Copilot の全体験でモデル廃止 ／ **Copilot global model policy の全 enterprise 適用完了** ／ MAICPP 契約の更新条項が自動発効 ／ OpenAI Daybreak でハードウェアセキュリティキー必須化 ／ Released Versions の次回定例日
- **9/2・9/3**: Windows 365 Frontline 名称での購入最終日 ／ Windows 365 Flex へ改称
- **9/4**: WebMCP Challenge の提出締切
- **9/9**: Apple 特別イベント（10:00 PT）／ GLM-5.3-Flash の 50%割引が終了
- **9/10**: MAI-Code-1-Flash が全 Copilot 体験から廃止
- **9/17**: OpenAI DevDay Exchange の応募締切
- **9/21**: **Anthropic ウェルビーイング研究助成の応募締切**
- **9/23**: WebMCP Challenge の受賞発表
- **9/24**: OpenAI の Videos API と Sora 2 動画生成モデルが退役（代替モデルの提示なし）
- **9/28**: 旧 GPT スナップショット4種が退役（代替は `gpt-5.6-terra`）
- **9/29 以降**: `claude-sonnet-4-5-20250929` の暫定退役日（確定日ではない）
- **9/30**: **Gemini の旧 `gemini-omni-flash-preview` エンドポイント廃止** ／ 2026 Wave 1 の対象期間終了 ／ M365 E7 プロモーションの対象購入最終日・M365 E5 / E3 の CSP 割引終了
- **9月**: **Salesforce in Claude のオープンベータ** ／ AI at Work roadmap への掲載開始と Release Plans on Learn の新規掲載停止 ／ Copilot Tuning の新体験が Public Preview ／ Copilot メモリの Purview 保持（569612）／ コネクタの会話内設定（569930）／ Agentic CoE と運用状態異常検知の Public preview ／ iOS 27 / macOS 27 GA ／ ChatGPT Ads Manager のセルフサービス提供
- **9月中旬**: CSP Eligibility Dashboard の direct bill 向け展開完了 ／ Copilot デスクトップアプリの広範な展開開始
- **10/1**: Apple の EU 向け新ビジネス条件が発効 ／ CSP ソフトウェアの5%上乗せ発効 ／ CSP growth margins の本番提供開始 ／ M365 E7 プロモーションの新規取引停止 ／ Ask Gemini in Chat のプロモーション上限が終了
- **10/5**: Anthropic ウェルビーイング研究助成の full proposal 提出期限（採択者）
- **10/15 以降**: `claude-haiku-4-5-20251001` の暫定退役日（確定日ではない）
- **10/16–11/11**: OpenAI DevDay Exchange 8都市（**東京は 10/20**）／ **10/20〜22**: SMB Copilot Partner Council イベント（NYC）／ **10/25〜30**: PPCC 2026
- **10/23**: OpenAI のレガシースナップショット12種とファインチューン版5種が退役
- **10月**: **SPFx 1.24 GA と Copilot Components の GA 目標**（課金モデルの確定を含む）／ Anthropic の IPO 予定（$2T 超の評価額を目標と報道）／ 韓国 App Store のコンテンツ記述子2件が All → 12+
- **11/1**: パートナー特典の有効期限がオファー購入日基準へ移行
- **11/15**: Release Planner の退役と AI at Work roadmap への移行完了
- **11/21**: GPT-5.6 Sol の暫定値下げが有効とされる期限
- **11/24 以降**: `claude-opus-4-5-20251101` の暫定退役日（確定日ではない）
- **11/30**: OpenAI Evals プラットフォーム・Agent Builder・`v1/prompts` が退役
- **12/1**: OpenAI の GPT Image 系が退役
- **12/2**: EU AI Act の生成コンテンツ標識義務の猶予終了
- **12/11**: `gpt-5-2025-08-07` 系と `o3-2025-04-16` / `o3-pro-2025-06-10` が退役
- **12/31**: Gemini 3.7 Flash の導入価格終了（$0.75/$3.75 → $1.50/$7.50）／ Copilot in 30・M365 E3 プロモーション・Purview Suite 50%オフの提供終了
- **12月**: Copilot Tuning の新体験が GA ／ SPFx 1.25（SPFx CLI GA）
- **2027/1/6**: OpenAI のファインチューニング新規ジョブ作成が全面終了
- **2027/1/20**: OpenAI の旧 audio / realtime / transcription 系が退役
- **2027年6月末**: Frontier Partner バッジの廃止
- **2027年末**: Anthropic が借りる Nscale ウェストバージニア DC（460MW）の稼働開始見込み
- **2028/6**: 米国 K-12 教職員向け ChatGPT for Teachers の無料提供期限

## 改善メモ

- **登録 URL の陳腐化が2件同時に判明した**。Copilot は M365 Copilot Release Notes の登録 URL が **301 恒久リダイレクト**（`copilot/microsoft-365/release-notes` → `microsoft-365/copilot/release-notes`）で、Learn MCP が転送先の本文をそのまま返すため取得は毎日成功しており症状が出ていなかった（B-049）。Master は `platform.openai.com/docs/changelog` の 301 と `developers.openai.com/codex/models` の 308 を確認した（B-048）。⚠️ **いずれも取得障害ではないため「既知の取得障害」には記録しない**
- **昨日の宿題2件はどちらも本日閉じた**。Nvidia FY27 Q2 の確報値（ハイライト3）と、OpenAI 退役ページで Assistants API が Past deprecations へ移った件である
- **Copilot の Preview 期日変更が「本日の変更か見落としか」判定できない**。ガバナンス・管理ページの2件（Agentic CoE・運用状態異常検知）は 8/19 の一次記録との差分で検知したが、8/26・8/27 は「期日変更なし」と記録していた。日次の一次記録が全行を保存していないと、この型の差分は起点を特定できない
- **一次未読のまま採用した項目**: Claudeforce の詳細（`www.salesforce.com` 拒否）、Nvidia FY27 Q2 の全数値（IR 系4ドメイン全滅）、Anthropic の8月 Risk Report と ウェルビーイング助成（`www.anthropic.com` 拒否）、Nscale $45B（両社の公式発表なし）、Devin automations 群（`docs.devin.ai` 拒否）、GPT-5-Codex-Mini（`learn.chatgpt.com` 拒否）
- **未確定として保留した項目**: Nvidia による Hugging Face 買収の成立可否と金額（The Information と Business Insider で報道が割れる）、Codex CLI `0.151.0-alpha` 系の変更内容（本文が空）、Similarweb 7月当月のシェア（二次で2系統に割れる）
- **障害の変化**: industry が **GlobeNewswire（`www.globenewswire.com`）を新規のゲートウェイ拒否**として登録し、一次財務開示への4本目の経路も塞がった。Master は `www.anthropic.com` / `www-cdn.anthropic.com` / `status.anthropic.com` / `alignment.anthropic.com` の4ホストがオリジン403ではなく**ゲートウェイ拒否**（`curl` exit 56）だったと判明し、台帳の分類と食い違うため許可ドメイン要請リストへ追加した（B-049）。Copilot は M365 Blog 本体の RSS が **200 に復旧**し、B-020 の二重確認が本日は成立した
- **解消した提案**: Copilot の B-046（Release Wave 3ページに廃止・移行の注記がない）は、3ページとも冒頭 Important に注記が入ったことで解消した
- 継続提案は Master 26件（最多: B-013 403の2分類判定・31回目）、Copilot 37件（最多: B-011 Power Platform Blog のトピック記事照合・39回目）、industry 11件（最多: B-004 取得方法欄の WebSearch 優先化・60回目）
