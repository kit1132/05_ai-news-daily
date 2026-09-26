# AI News Daily Summary — 2026-09-27

週末で一次の動きは小さいが、既定値と前提が2つ動いた日である。Claude Code `2.1.283` が npm `latest` に上がり、サードパーティプロバイダ経由かテレメトリ無効の環境では権限モード未設定だと auto mode で起動するようになった。米 DC 巡回区控訴裁判所は国防総省による Anthropic の supply-chain risk 指定を適法と判断した。OpenAI は GPT-6 Sol / Luna の画像理解を落としていたバグを直し、画像系の評価の取り直しを勧めた。

## 今日のハイライト

### 1. [破壊的変更+新機能] Claude Code `2.1.283` は、Bedrock / Vertex 等やテレメトリ無効の環境で権限モード未設定なら auto mode で起動する — 「未設定なら毎回確認」の前提が外れた

**要点**: Anthropic が 9/25 に `2.1.283` の changelog を公開し、npm の `latest` も同版になった。サードパーティプロバイダ経由かテレメトリ無効の対話セッションは、権限モードを決めていないと承認プロンプトではなく auto mode で始まる。管理者向けにモデルを完全一致で固定する設定も入った。

**詳細**: 前日は changelog 未記載のまま `next` に publish されていた版で、本日内容が判明した。

- npm `dist-tags`: `{stable: 2.1.274, latest: 2.1.283, next: 2.1.283}`（9/27 実測）。`stable` 固定の組織にはまだ届いていない
- 既定の変更:
  - `Skill(anthropic-skills:<name>)` の deny ルールが Claude Desktop プラグインのスキルもブロックする
  - self-hosted runner の git: LFS の `pre-push` をスキップし、書き込み可能なシステム側 `core.hooksPath` を無視し、`--configure-git` なしでは署名しない
- 管理設定の追加:
  - `availableModelsMatch`: `"exact"` にすると `availableModels` に列挙した版だけを許可し、新モデルは列挙するまでブロックする
  - `deniedModels`: 特定モデルをブロックする
  - `/doctor prompt-audit`: CLAUDE.md・skills・agents・commands から旧モデル向けの書き方や矛盾する指示を検出する
- 修正: Windows の PowerShell ツールで保護フォルダを削除できた問題、サンドボックス内の git credential helper がプロキシのログイン情報を保存していた問題を直した。security とは明記していない
- 課金: Code Review が時間制限で止まった不完全なレビューに課金していた問題を直し、以後は課金せず1回再試行する

- https://code.claude.com/docs/en/changelog
- https://www.npmjs.com/package/@anthropic-ai/claude-code

### 2. [動向] 米控訴裁が国防総省による Anthropic の supply-chain risk 指定を 2対1 で適法と判断した — 8月の地裁判断で揺らいだ「軍と請負業者は Claude を使えない」状態が控訴審で固まった

**要点**: DC 巡回区控訴裁判所が 9/25、国防総省が3月に Anthropic を supply-chain risk に指定したことを適法とし、取消請求を退けた。指定は軍と請負業者による Claude の利用を禁じる。防衛系顧客への Claude 提案は、当面この指定が有効な前提で組むことになる。

**詳細**:

- 判決: 2対1。多数意見は Katsas 判事（Rao 判事が同調）、Henderson 判事が反対意見を書いた
- 多数意見は、自律型兵器と大規模監視への利用を Anthropic が拒んだことを理由とする指定を合理的とし、報復だとする主張を退けた
- 経緯: 8/27 に連邦地裁が並行訴訟で指定を違法と判断し、9/3 に国防総省が指定の有効性を再表明していた
- Anthropic は「数十億ドル規模の取引を失った」とし、大法廷での再審理や最高裁を含めて検討するとした
- 判決文と Anthropic の声明ページの一次は未読で、CNBC・Washington Post・CNN の同日報道に基づく

- https://www.cnbc.com/2026/09/25/pentagon-anthropic-ai-risk-appeals-court.html
- https://www.washingtonpost.com/technology/2026/09/25/federal-appeals-court-rules-pentagon-can-blacklist-anthropic/

### 3. [仕様] OpenAI が GPT-6 Sol / Luna の画像理解を落としていた画像エンコードのバグを直した — 9/22〜25 に取った画像・computer use の評価は実力より低く出ていた可能性がある

**要点**: OpenAI が 9/25 付の changelog で、GPT-6 Sol と Luna の画像エンコードのバグを修正したと公表した。対象は API と Codex の視覚タスクで computer use を含む。公開直後に行った画像系の比較評価は、修正後に取り直す前提へ変わった。

**詳細**:

- 対象モデル: `gpt-6-sol` / `gpt-6-luna`（9/22 公開）
- OpenAI は評価の再実行と、画像を使うワークフローの再試行を勧めている。バグの混入時期・影響期間・エンドポイントは書いていない
- 単価は変わらず、Sol $2／$10・Luna $0.10／$0.50 のまま（industry が一次の料金ページで確認）

- https://developers.openai.com/api/docs/changelog

## カテゴリ別まとめ

### Claude / Anthropic

- [新機能] **Claude Code の運用系の出力とゲートウェイ** — Anthropic が `2.1.283` で、監査とゲートウェイ運用に使える出力・設定を追加した。
  - OTel: `OTEL_LOG_TOOL_CONTENT=1` のとき `tool.output` に MCP ツール・WebFetch・WebSearch の出力が入る
  - Claude apps gateway: 送信せず定型応答を返す `load_test_mode` と、Amazon Bedrock の Mantle エンドポイントへつなぐ `mantle` upstream が加わった
  - Claude Tag: 管理者が「Channels Claude can search」で検索対象を Claude が参加している公開チャンネルに絞れる
  - Cloud の routine: 新規スケジュールの既定が「毎時ちょうど」から「毎時 N 分」になった
- [新機能] **Build plugins for Claude** — Anthropic が `support.claude.com` の Release Notes に 9/25 付でプラグイン申請ポータルを載せた。内容は前日のサマリーで報じた `claude.com/blog` の告知と同じである。https://support.claude.com/en/articles/12138966-release-notes
- [観測] **S-1 公開版** — Anthropic の S-1 公開版は 9/26 時点でも提出が確認されていない。一次の告知は6月1日の機密提出だけで、11月上場とする報道は変わっていない。https://www.anthropic.com/news/confidential-draft-s1-sec
- [据え置き] **Claude Platform とモデル退役ページ** — Claude Platform の release notes は 9/24 の出力前拒否の課金が最上位のままで、モデル退役ページに新しい告知は出ていない。`claude-sonnet-4-5-20250929` は Active で、60日前の通知が無いため暫定退役日 **9/29**（not sooner than）に止まることはない。Sonnet 5.5 / Haiku 5.5 もモデル表に載っていない。https://platform.claude.com/docs/en/about-claude/model-deprecations

### GitHub Copilot / GitHub

- [新機能] **Copilot managed settings のバリデーター** — GitHub が 9/25 に、Enterprise の AI controls ページで Copilot 管理設定ファイルを検証できるようにした（GA）。
  - 検査対象: `.github-private` の `copilot/managed-settings.json`、`copilot/team-mappings.json`、マッピングが参照するチーム設定ファイル
  - 表示内容: 不正な JSON・未対応の設定・不正なチームマッピングなど、ポリシー適用を止めるエラーをファイルと JSON パスつきで出す
  - 修正後は既定ブランチへコミットし、Agents ページを再読込すると再検査される
  - https://github.blog/changelog/2026-09-25-enterprise-managed-settings-in-product-validator
- [新機能] **usage metrics API の PR レビュー段階別時間** — GitHub が 9/25 に、Copilot usage metrics API の `repos-1-day` レポートで PR レビューの滞留時間を取れるようにした。
  - `pull_request_review_times`: レビュー依頼→初回レビュー、初回→最終レビュー、最終レビュー→マージの3段階で、それぞれ中央値と p90（分）
  - `authored_by` / `reviewed_by` と `total_merged`: 作成者・レビュアーの区分と集計対象のマージ済み PR 件数
  - データは 9/21 からで遡及しない。bot と作成者自身のレビューは数えない。閲覧は enterprise owner・billing manager・organization owner と `View Copilot Metrics` 権限のカスタムロールに限る
  - https://github.blog/changelog/2026-09-25-usage-metrics-api-adds-pull-request-review-stages
- [版更新] **Copilot CLI `v1.0.89-4`** — GitHub が Copilot CLI の pre-release を `v1.0.89-4`（9/25 21:13 UTC）まで進めた。安定版は `v1.0.88` のままである。Auto がルーティング階層を提案して切り替えられるようになり、直接インストールしたプラグインを有効／無効にできる。https://github.com/github/copilot-cli/releases
- [セキュリティ] **Plugin4Shell は開示10日目でも Copilot 未修正** — industry が二次報道を突き合わせ、Microsoft が GitHub Copilot の修正を出しておらず CVE も未採番のままであることを確認した。https://www.heise.de/en/news/Critical-flaw-in-Claude-Code-OpenAI-Codex-GitHub-Copilot-and-Gemini-CLI-11460259.html
- [観測] **GitHub changelog 9/25 分の件数訂正** — industry が 9/25 分を前日の5件から8件に訂正した。上の2件と、issue の個人用ビュー（「Relates to」関係の GA）が後から掲載された。9/26・9/27 分はまだない。https://github.blog/changelog/

### Microsoft 365 Copilot / Copilot Studio / Power Platform

- [新機能+予定] **Copilot Studio の Maker guidelines** — 管理者が、ブロックされた機能に当たったメーカーへ表示する案内文・リンク・連絡先を、環境または環境グループ単位で設定できるようになった（Preview）。Roadmap 570967 は GA を11月とし、「管理者に連絡してください」の既定文言を組織の案内に差し替えられる。
  - 設定場所: Power Platform 管理センター → Copilot → Settings → Copilot Studio 節の Maker guidance
  - 制約: プレーンテキスト **400字**まで、リンクは HTTPS のみ、多言語化されない。環境グループの設定が環境の設定より優先される
  - ⚠️ Roadmap は「問題が無いエージェントでも表示される」と書くが、Learn はブロックに当たったときの表示として説明しており、表示条件が一致していない
  - https://www.microsoft.com/microsoft-365/roadmap?id=570967
  - https://learn.microsoft.com/en-us/microsoft-copilot-studio/authoring-agent-status
- [予定] **PowerPoint の Copilot 非同期通知** — Mac の PowerPoint 利用者が、アプリを閉じたり端末を切り替えたりしても Copilot の処理完了や要対応を通知で受け取れるようになる（Roadmap 570436・GA October CY2026）。https://www.microsoft.com/microsoft-365/roadmap?id=570436
- [予定] **Copilot Autopilot の詳細** — Microsoft が 9/25 に発表した新しい Copilot（前日既報）の Autopilot について、二次報道が詳細を伝えた。所有者が名前・役割・目標を与えると、誰も使っていない間も M365 内で作業を続け、各エージェントに Entra ID とメール・カレンダー・OneDrive・Teams が付いて組織図に載る。private preview は月末までとしている。https://venturebeat.com/technology/microsoft-revamps-its-copilot-ai-with-a-persistent-autopilot-agent-and-hosting-for-ai-generated-apps
- [予定] **Copilot Studio の9月 GA 期日** — Roadmap の Copilot Studio 起票22件は全件 `In development` のままで、GA 期日が September CY2026 の **14件**は期日まで残り **3日**になった。
- [据え置き] **Release Notes・What's New・Release Wave** — M365 Copilot Release Notes の先頭は **September 23, 2026** のまま新バッチが無い。Copilot Studio What's New は July 2026 節のままで、GitHub Copilot ハーネスの GA（8/3）は55日反映されていない。Released Versions の Copilot Studio 最新ビルドは 2026.6.3 のまま、Power Platform の3ブログにも新規記事は無い。https://learn.microsoft.com/en-us/copilot/microsoft-365/release-notes
- [据え置き] **Partner Center 9月分** — Microsoft の Partner Center 9月分は 9/25 付の新 Copilot が最新のままで、新 Copilot の従量単価と非営利向け割引の計算方法は依然として一次に書かれていない。Check Inventory API は予告どおり 9/25 に退役日を迎えた。https://learn.microsoft.com/en-us/partner-center/announcements/2026-september

### OpenAI / Codex / ChatGPT

- [版更新] **Codex `rust-v0.157.1`** — OpenAI が Codex の安定版 `rust-v0.157.1` を 9/26 01:02 UTC に出した。リリースノートは空で変更点は分からない。pre-release は `0.159.0-alpha.5`（9/26 17:34 UTC）まで進んだ。https://github.com/openai/codex/releases
- [予定] **Responses API Playground の速度選択** — TestingCatalog が、OpenAI が Playground に Standard / Fast / Ultrafast の速度選択を用意していると報じた（9/26・未発表）。Ultrafast は GPT-5.6 Sol で最大 750 tok/s の限定プレビューとして公開済みで、**9/29** の DevDay 前後に対象を広げるとみている。https://www.testingcatalog.com/openai-prepares-to-expand-ultrafast-api-to-more-users/
- [観測] **DevDay（9/29）の議題** — OpenAI は公式の議題を出しておらず、二次報道はマネージドエージェントと GPT-6 Cyber のプレビューを予想している。基調講演は太平洋時間10時からで、料金の発表があるかが焦点になっている。https://openai.com/index/devday-2026/
- [据え置き] **一次料金ページ・廃止ページ** — OpenAI の料金ページは GPT-6 Astra $10／$50・Sol $2／$10・Luna $0.10／$0.50、GPT-5.6 Sol $4／$20（期間限定価格は「少なくとも11月21日まで」）のままである。廃止ページの最新告知は 9/11 のままで、Developer Community Announcements も 9/22 の GPT-6 Sol / Luna が最上位のまま。https://developers.openai.com/api/docs/deprecations

### Google

- [新機能] **Gemini 3.8 Live の Live Avatar** — Google Cloud が 9/24 付で、Gemini Enterprise の音声エージェントに口の動きを合わせた動画アバターを付ける機能を米国と EU のエンドポイントで GA にした。97言語に対応し、出力には SynthID の透かしが入る。自分の写真から作るアバターは許可リスト制で、Extended Thinking 版は private preview のまま。二次報道は単価を動画出力100万トークンあたり $1.00 としているが、一次のブログは料金ページへの案内のみである。https://cloud.google.com/blog/products/ai-machine-learning/gemini-3-8-live-with-live-avatar-is-now-generally-available
- [予定] **Gemini デスクトップアプリの限定テスト** — TestingCatalog が、Google が Gemini デスクトップアプリで Ask / Assign の切替、Obsidian 連携、Finder アクションを限定テストしていると報じた（9/25 頃）。trusted tester には Tasks モードが配られ始めた。https://www.testingcatalog.com/google-keeps-transforming-gemini-desktop-into-superapp/
- [据え置き] **Gemini API changelog** — Google の Gemini API changelog は 9/22 の 3.8 Flash TTS / Flash-Lite TTS GA が最上位のままで、料金改定の告知は無い。Workspace Updates にも 9/26 付の投稿は無い。https://ai.google.dev/gemini-api/docs/changelog

### Cursor / xAI / オープンウェイト

- [据え置き] **Cursor の新モデル告知** — Cursor の changelog は 9/23 の Rollouts and Security Review が最上位のままで、フォーラム Announcements も 9/21 の Grok 4.7 が最上位のまま。Opus 5.5 と GPT-6 Sol / Luna の提供開始は5日目も告知されていない。
- [観測] **xAI・Devin の一次** — `x.ai` と `docs.devin.ai` はゲートウェイ拒否のままで、9/25〜26 付の一次は確認できていない。
- [据え置き] **MCP・Hugging Face・Apple** — `blog.modelcontextprotocol.io` は 8/22 の「The New MCP Roadmap」が最上位のままで、Hugging Face の登録8 org にも新規リポジトリは無い。`developer.apple.com/news/` は 9/18 の iPhone Duo 向けリソースが最上位のまま。

### 市場・企業

- [動向] **Ema が $77M の Series B** — TechCrunch によると、HR・IT・財務の社内業務を複数の AI エージェントで自動化する Ema が 9/23 に Creaegis 主導で $77M を調達した。累計調達額は $140M、評価額は2024年の前回ラウンドの4倍超で、記事は「AI がエンタープライズソフトウェアと IT サービスの予算を取りに来ている」と位置づけている。https://techcrunch.com/2026/09/23/ema-raises-77m-as-ai-starts-eating-into-enterprise-software-and-services/
- [据え置き] **市場データ** — IDC・MM総研・NRC・Similarweb はいずれも新規公表が無い。Similarweb の9月分はまだ出ておらず、引用できるのは8月分（ChatGPT 55.5%・Gemini 25.6%・Claude 9.3%）のまま。

## 直近の注目予定

- **9/28**: Copilot のチャット3面統合 ／ code review の既定 effort が Balanced へ ／ チャットのデータ保持変更 ／ OpenAI の `gpt-3.5-turbo-instruct` / `babbage-002` / `davinci-002` / `gpt-3.5-turbo-1106` が停止
- **9/29**: OpenAI DevDay（サンフランシスコ） ／ Google Meet「Take notes for me」の新設定が有効化
- **9/29 以降**: `claude-sonnet-4-5-20250929` の暫定退役日（廃止通知は未発出）
- **9/30**: Copilot in SharePoint の GA 展開開始 ／ CSP の M365 E5 / E7 / Copilot プロモーション終了 ／ Gemini の `gemini-omni-flash-preview` が停止 ／ Copilot Studio の Roadmap 14件が GA 期日 ／ Copilot Dev Camp Summit ／ Clinical Applications スペシャライゼーションの受付開始
- **10/1**: CSP 成長マージンの一般提供 ／ Microsoft CSP ソフトウェア価格改定が発効 ／ OpenAI の `gpt-5.4-cyber` が停止 ／ Copilot 既存顧客の前払い必須化 ／ ChatGPT for Word の Word アクセスが既定オンへ
- **10/2**: GitHub Copilot が4モデルを廃止 ／ Gemini の `gemini-2.5-flash-image` が停止
- **10/5**: Gemini の `antigravity-preview-05-2026` が停止 ／ GPT-Rosalind の課金開始
- **10/13**: Office / Project / Visio LTSC 2021 のサポート終了 ／ 新しい Copilot の Partner Digital Airlift
- **10/14**: GitHub SSH の新規 RSA 鍵が 3072 ビット以上必須に ／ GPT-5.5 が ChatGPT / Codex から退役
- **10月**: Copilot Studio エージェントがコスト管理の対象に ／ PowerPoint の Copilot 非同期通知（Mac）GA
- **10/19**: GitHub Copilot が5モデルを廃止
- **10/21**: GitHub Copilot の新機能既定ポリシーの設定期限（10/22 発効）
- **10/23**: OpenAI のレガシースナップショット12件が停止
- **10/27〜29**: PPCC 2026（ラスベガス）
- **10/31**: OpenAI Evals が読み取り専用化
- **11月**: Copilot Studio の Maker guidelines（570967）GA
- **11/2**: GitHub Actions の `pull_request_target` 既定無効化が公開リポジトリで強制開始 ／ M365 Copilot Business の従量課金が既定オン
- **11/4**: GitHub SSH `ssh-rsa` の1回目のブラウンアウト
- **11/12**: OpenAI → Cursor のモデル供給停止予定（一次未読）
- **11/15**: Microsoft Release Planner 退役
- **11/17〜20**: Microsoft Ignite
- **11/21**: OpenAI GPT-5.6 Sol の期間限定価格の下限
- **11/30**: OpenAI の `v1/prompts`・Evals・Agent Builder が停止
- **12/1**: OpenAI `gpt-image-1-mini` / `gpt-image-1.5` / `chatgpt-image-latest` が停止
- **12/9**: GitHub SSH `ssh-rsa` の2回目のブラウンアウト
- **12/11**: OpenAI GPT-5 / o3 系スナップショットが停止
- **12/31**: 非営利向け M365 Copilot の併用プロモーション終了 ／ Gemini 3.8 Flash の導入価格が終了

## 改善メモ

- 新規提案: 3ソースとも無し
- 継続提案: Master は B-035 npm dist-tags が42回目（`2.1.283` が `latest` に上がり changelog にも載った）／ industry 10件を再確認（最多 B-004・90回目）。industry は B-031（GitHub changelog の後日掲載による件数訂正）と B-030（9/28 のレガシー4モデル停止が抽出から再び落ちた）に本日該当した
- 障害の変化: 無し。Copilot の `mc.merill.net` は51日連続でゲートウェイ拒否が続く
- ソース間の差分・矛盾:
  - Claude Code `2.1.283` の auto mode 起動の条件は、industry が「権限モード未設定の対話セッション全般」、Master が「サードパーティプロバイダ利用時かテレメトリ無効時」と書いており範囲が食い違う。本サマリーは changelog の Changed 節を項目単位で引いた Master を採った
  - GPT-6 の画像エンコード修正のタグは Master が仕様、industry が破壊的変更で割れた。既存の設定や手順は壊れず、評価の取り直しを促す修正なので、本サマリーは仕様を採った
  - Google の Live Avatar は industry が11語に無い `[新製品]` を付けていた。本サマリーは新機能とした
  - 10/19 の GitHub Copilot 廃止モデル数は industry が本日も「6モデル」のままで、Master の 9/18 告知本文に基づく **5モデル**を引き続き採る
- 手順の不整合: `daily-summary.md` はハイライト済み項目を `- **見出し**（ハイライトN参照）` と書くよう求め、ビューアもこの形（`/^（ハイライト([0-9０-９]+)参照）$/`）を読むが、`scripts/check-update-tags.py` は「ハイライト参照」の連続文字列しか除外しないため不合格になる。本日は参照行を置かずに生成した
