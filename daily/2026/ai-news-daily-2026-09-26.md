# AI News Daily Summary — 2026-09-26

管理者の既定値と課金の前提が動いた日である。GitHub は Copilot Business / Enterprise で未設定の機能を 10/22 から「新機能の既定ポリシー」に従わせると告知した。Microsoft は Copilot を Home / Code / Autopilot で組み直し、定額 USL に利用上限を設けて委任型の作業を Copilot Credits の従量へ分けた。Anthropic は Compliance API の Activity Feed からファイル名とタイトルを過去分まで外した。アプリ実行基盤の Copilot Managed Runtime は Public Preview に入り、Claude ディレクトリにはプラグイン申請ポータルが開いた。

## 今日のハイライト

### 1. [破壊的変更] GitHub が Copilot Business / Enterprise の未設定機能を 10/22 から既定ポリシーに従わせる — 「設定していない機能はオフのまま」の前提が26日後に崩れる

**要点**: GitHub が 9/24 に、Copilot Business / Enterprise で明示的に設定していない GA 機能とクライアント機能を 10/22 から「新機能の既定ポリシー」に従わせると告知した。新機能を1つずつ承認する運用の組織は、10/21 までに既定値を選ばないと組織方針と無関係に切り替わる。

**詳細**: 9/24 付の changelog による。設定期間は28日で、9/24 に始まった。前日のサマリーはこの告知を取りこぼしており、本日はじめて載せる。

- 対象: 「Features & clients」ページの未設定の GA 機能と対応クライアント機能、Copilot Code Review のポリシー、MCP サーバーのポリシー
- 選択肢:
  - Enabled: 現行と将来の対象機能を既定でオンにする
  - Disabled: 現行機能はオフのままで、将来の機能は承認制にする
  - Let organizations decide: 下位の Organization 管理者に委ねる
- 設定場所: AI Controls → Copilot → 「Default policy for new features」
- 変わらないもの: 明示的に有効化・無効化した機能は上書きしない。preview 機能は引き続きオプトインである。料金への言及は無い

- https://github.blog/changelog/2026-09-24-default-enablement-of-copilot-features-for-copilot-business-and-enterprise

### 2. [料金+新機能] Microsoft が Copilot の課金を「上限付き定額 USL」と「Copilot Credits の従量」に分けた — 定額は無制限ではなくなり、委任型の作業は従量が前提になる

**要点**: Microsoft が、日常業務の AI をユーザー単位の定額（USL）、Cowork / Code / Autopilot などの委任型の作業とフロンティアモデルを従量（UBB）と整理し直した。USL には利用上限（fair use）が入り、「1ユーザー定額で全部入り」の費用試算は従量分を上乗せして引き直しになる。

**詳細**: Tech Community の Microsoft Copilot Blog が **9/25**「Evolution of the Copilot pricing model」で告知した。9/23 の顧客向けレターは2本立てを概念として示しただけで、上限と範囲が書かれたのは本日が初めてである。

- USL の範囲: Chat と Word / Excel / PowerPoint などの日常作業。GPT-5.6 と Sonnet 5 は込みで、Opus 5 などの新モデルは上限付きで含む
- 上限に達したとき: 警告のあと、Auto へ切り替える（追加費用なし）か Copilot Credits へ移るかを選ぶ。上限の数値は示されていない
- UBB の範囲: Cowork / Code / Autopilot、SharePoint の高度な機能、Fable と Astra などのフロンティアモデル。UBB は USL が前提で、エンタープライズ顧客では管理者がスペンディングポリシーを作るまで無効かつ無課金である
- 本日から展開する FinOps 機能: コスト管理の対象に Code と Managed Runtime が加わる（Copilot Studio エージェントは10月予定）。ほかにグループ単位のモデルファミリー制御、Cowork の消費インサイト、Graph API によるスペンディングポリシー管理、利用者本人のクレジット残高表示が入る

⚠️ Learn の `usage-based-billing-overview-copilot-credits`（`ms.date` 2026-09-25）は、対象サービスを Cowork・Cowork のアプリ・Work IQ API の3つと書いたままで、Code と Managed Runtime を載せていない。同ページではスペンディングポリシーの Auto-apply new services が既定で有効である。二次報道は Copilot Credits を $0.01/credit、前払い割引を5〜20% としているが、一次に単価は無い。

- https://techcommunity.microsoft.com/blog/microsoft-copilot-blog/evolution-of-the-copilot-pricing-model/4559416
- https://learn.microsoft.com/en-us/microsoft-365/copilot/usage-based-billing-overview-copilot-credits

### 3. [破壊的変更] Claude の Compliance API がファイル名とタイトルを返さなくなった — 過去の記録にもさかのぼって適用される

**要点**: Anthropic が Compliance API の Activity Feed で、ファイル名・プロジェクト文書名・アーティファクトのタイトルを返さないようにした。過去の activity も対象になる。監査ログをファイル名で突き合わせていた Enterprise の監査連携は、名前を使わない照合へ作り替えが要る。

**詳細**: Claude Platform の release notes が 9/24 付の3項目のうち2つとして掲載した。前日のサマリーは同日付の拒否課金だけを載せ、この2項目を取りこぼしていた（industry が再読で捕捉）。

- Activity Feed: `filename` と `title` が空か省略になる
- ローカルセッション用エンドポイント: Excel / PowerPoint / Word / Outlook の Claude for Microsoft 365 セッション（`product_surface` が `office_agents` で始まるもの）でベータを終えた

- https://platform.claude.com/docs/en/release-notes/overview

## カテゴリ別まとめ

### Claude / Anthropic

- [新機能] **Claude ディレクトリのプラグイン申請ポータル** — Anthropic が 9/25 に、有料 Claude プランの開発者が MCP コネクタ単体、または MCP サーバーとスキルをまとめたプラグインを Claude ディレクトリへ申請できるようにした。承認されると Claude と Claude Code の両方のディレクトリに載る。
  - 申請先: `claude.ai/directory/manage/new`
  - ポータルの機能: 申請時の自動セーフティスキャンと検証、審査状況の追跡と修正推奨、公開後の製品サーフェス別インストール数・表示回数・検索露出の分析
  - 対応拡張: MCP 2.0 の MCP Apps と Enterprise Managed Auth
  - https://claude.com/blog/build-plugins-for-claude
- [新機能] **Claude Tag の個人コネクタ** — Team プランの利用者が、Slack のチャンネル内で自分の Drive・カレンダー・CRM などの個人コネクタを使えるようになった（9/24。Enterprise は後日）。
  - 名義: 個人コネクタでの操作は本人のアカウント名義、チャンネルの作業はサービスアカウント名義で記録される
  - 投稿前の扱い: auto モード（機微な内容を Claude が確認する）か手動レビューかを選ぶ
  - 管理者: 共有エージェント ID のツール・個人コネクタのみ・ツールごとの判断から選べる。Enterprise では全員にレビューを必須化できる
  - https://claude.com/blog/claude-tag-now-supports-personal-connectors-in-channels
- [版更新] **Claude Code `2.1.283`** — Anthropic が 9/25 18:46 UTC に npm の `next` へ publish したが、changelog にはまだ載っておらず内容は不明である。npm は `stable: 2.1.274` / `latest: 2.1.282` / `next: 2.1.283`（9/26 実測）で3つとも前日から1版ずつ進み、`stable` は Opus 5.5 を既定にした `2.1.280` 以降にまだ届いていない。https://www.npmjs.com/package/@anthropic-ai/claude-code
- [動向] **Fable 5.1 による9ループ振幅の計算** — Anthropic が、Fable 5.1 が Claude Science 上で N=4 超対称ヤン＝ミルズ理論の9ループ振幅を総額 $1,000〜2,000 で計算したと報告した（9/25）。Lance Dixon が結果を検証し、「新しい物理の発見ではなく既存手法の適用」と位置づけている。https://www.anthropic.com/research/yes-claude-can-do-nine-loops
- [動向] **Project Swap** — Anthropic が、社員201人の本の交換を Claude エージェントに交渉させた社内実験の結果を公開した（9/24）。選好の順位付けが本人と一致したのは 61%（ランダム 50%）で、到達点は最適 0.89 に対し平均 0.55、差の 85% は選好の伝達で生じた。交換効率は Opus が 0.88、Haiku が 0.75 だった。https://www.anthropic.com/research/project-swap
- [観測] **S-1 公開版** — 9月下旬とされた Anthropic の S-1 公開版の提出は、9/25 時点で報じられていない。11月上場の日程報道は変わっていない。
- [据え置き] **モデル退役ページ・ニュース面** — Anthropic のモデル退役ページに新しい告知は無く、`claude-sonnet-4-5-20250929` は Active のままで廃止通知も出ていない。Sonnet 5.5 / Haiku 5.5 もモデル表に載っておらず、`anthropic.com/news` は 9/23 の酵素系発見、`support.claude.com` は 9/22 の Opus 5.5 が最上位のままである。https://platform.claude.com/docs/en/about-claude/model-deprecations

### GitHub Copilot / GitHub

- [新機能] **Copilot for Slack / Microsoft Teams** — GitHub が 9/25 に Business / Enterprise 向けの public preview で、会話の文脈を読み、会話の途中でモデルを切り替えられるようにした。
  - 取り込める文脈: Slack はファイル・添付・メッセージリンク、Teams はインライン画像・転送メッセージ・チャンネルとスレッドの履歴
  - モデル切替: 選んだモデルはそのスレッドの残りで保持され、Slack はチャンネル単位で既定モデルも決められる
  - Issue 作成: 作成前に重複を確認し、元の会話へのリンクを残す
  - 利用分は既存の権利とクラウドエージェントの予算から引かれる。管理者がクラウドエージェントのポリシーを有効にし、GitHub アプリを導入・更新する必要がある
  - https://github.blog/changelog/2026-09-25-updates-to-github-copilot-for-slack-and-microsoft-teams
- [新機能] **高影響操作の前の再認証** — GitHub が 9/24 に、IdP に Microsoft Entra ID を使う EMU の Enterprise 向けにプレビューを出した。トークン作成・webhook 編集・Organization のセキュリティ設定変更・リカバリーコード表示の前に IdP での再認証か MFA を求め、認証後2時間は再要求しない。盗まれたセッション cookie への対策である。https://github.blog/changelog/2026-09-24-require-proof-of-presence-for-high-impact-actions
- [破壊的変更] **期限切れ artifact の非表示** — GitHub Actions の UI と REST（list artifacts for a repository / get an artifact）が、期限切れの artifact を返さなくなった。保持期間と課金は変わらない。
- [破壊的変更] **ワークフロー run 検索の件数上限** — GitHub Actions が、ワークフロー run の検索結果が2,500件を超えると件数を「2,500+」と表示するようにした（9/25）。1ページ最大1,000件は変わらず、2,500件を超えて取得するスクリプトは日付範囲などで絞り込む必要がある。https://github.blog/changelog/2026-09-25-changes-to-query-results-in-the-github-actions-api-and-ui
- [新機能] **agentic autofix と Copilot Memory** — GitHub が 9/25 に、agentic autofix がセキュリティアラートを直すときに Copilot Memory を読み書きするようにした（どちらも public preview）。保存した修正パターンは code review とクラウドエージェントでも使われ、Copilot Memory を有効にしている顧客では自動でオンになる。https://github.blog/changelog/2026-09-25-agentic-autofix-now-uses-copilot-memory
- [新機能] **9/21 週の Copilot 週次まとめ** — GitHub が 9/25 にまとめを出し、VS Code と JetBrains の新機能とモデルのプラン別提供範囲を1か所に揃えた。
  - VS Code 1.139: SSH / Tunnel / WSL ホストの Dev Containers 内でエージェントが動く（段階展開）。セッションの絞り込みと改名ができる Compact View が入った
  - JetBrains: 低リスクのツール呼び出しを自動承認する Assisted Approvals（public preview）、巻き戻し付きのメッセージ編集、組織・Enterprise で共有するスキルとカスタム指示
  - プラン別: Claude Opus 5.5 と GPT-6 Sol は Pro+ / Max / Business / Enterprise、GPT-6 Luna と Grok 4.7 は Pro 以上
  - https://github.blog/changelog/2026-09-25-github-copilot-weekly-releases-september-21
- [版更新] **Copilot CLI pre-release `v1.0.89-3`** — GitHub が pre-release を 9/24 21:18 UTC の `v1.0.89-3` まで進め、`v1.0.89-2` で MCP の OAuth スコープに対応し Windows の localhost 接続を改善した。安定版は `v1.0.88` のままである。https://github.com/github/copilot-cli/releases
- [セキュリティ] **Plugin4Shell は開示9日目でも Copilot 未修正** — 二次報道の突き合わせで、Microsoft が GitHub Copilot の修正を出しておらず CVE も未採番のままであることを確認した。修正済みは Claude Code 2.1.179 以降と Codex 0.146.0 以降で、Gemini CLI は修正しない。https://www.helpnetsecurity.com/2026/09/18/plugin4shell-ai-coding-agents-vulnerability/

### Microsoft 365 Copilot / Copilot Studio

- [予定] **新しい Copilot（Home / Code / Autopilot）** — Microsoft が 9/25 に Copilot を3構成で組み直すと発表した。Home と Code は数週間以内に Frontier プログラムで展開を始め、Autopilot は9月末に Private Preview を広げる。
  - Home: Chat と Cowork を1か所にまとめ、Word / Excel / PowerPoint を Copilot の中で使える（Office in Copilot）
  - Code: 知識労働者が自然言語でアプリ・トラッカー・ダッシュボードを作る。二次報道によると GitHub Copilot と同じ基盤で動く
  - Autopilot: 独自のエージェント ID とメモリを持ち、クラウドで常時動く個人エージェント（二次報道では旧称 Scout）
  - Frontier は M365 管理センターの Copilot > Settings > Copilot Frontier で有効にし、既定は No access である。パートナー向けの Partner Digital Airlift は 10/13
  - ⚠️ 公式ブログ（`blogs.microsoft.com`）はゲートウェイ拒否で未読で、一次本文は Partner Center 9月ページの 9/25 付項目（同ページ19件目）による
  - https://learn.microsoft.com/en-us/partner-center/announcements/2026-september
- [新機能] **Copilot Managed Runtime の Public Preview** — Microsoft が、Cowork・Copilot Code・Copilot Studio で作ったアプリを M365 テナント内で動かす実行基盤を Public Preview にした（9/25）。SDK と CLI を使えば他社ツールで作ったアプリも載せられる。
  - 作成経路の既定値: Copilot Studio は On（M365 管理センターで管理）、CLI は Off、Cowork は Frontier 参加テナントでのみ On
  - 既定で無効な制御: Allow public GitHub repository と External artifacts
  - 課金: ビルドは作成した製品側で課金される。実行時の課金は M365 管理センターで利用者単位に設定し、Copilot Studio エージェントの環境単位の課金モデルは使わない
  - 統制: Entra 認証、条件付きアクセス、DLP、高度なコネクタポリシー、共有制限がアプリ作成時点から掛かり、棚卸しは Apps > All apps で行う
  - https://www.microsoft.com/en-us/copilot/blog/copilot-studio/build-where-you-want-run-with-confidence-now-microsoft-hosts-and-manages-the-code-created-by-copilot/
- [料金+予定] **Copilot in SharePoint の GA** — Microsoft が Copilot in SharePoint を GA とし、**9/30** から Worldwide テナントへ展開を始める。質問応答・コンテンツ作成・スキル作成・メタデータ付与と決定的ワークフローは M365 Copilot ライセンスに含まれ、大規模コンテンツへの処理・画像生成・サイト分析レポート・準リアルタイムのメタデータ自動入力には Copilot Credits が要る。https://techcommunity.microsoft.com/blog/spblog/sharepoint-ai-innovations-hit-ga-powering-new-copilot-app-and-agents/4555724
- [新機能] **Cowork の既存 Office ファイル編集** — Cowork が OneDrive / SharePoint 上の Word・Excel・PowerPoint ファイルを、共有状態と既存の版履歴を保ったまま編集できるようになった（Cowork What's New の September 2026 節・9/25 更新）。https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/whats-new
- [観測] **Cowork のモデル表** — `cowork-models` は 9/14 更新のままで、9/22 に告知された Opus 5.5 と GPT-6 Sol が本日も載っていない。
- [観測] **非営利向け割引の計算方法** — Partner Center の本文は「既存の15%に15/20/30/40%を上乗せ」のままで、足すのか掛け合わせるのかが書かれていない。二次のスニペットは掛け算（40%枠で合計49%）とも読めるが出典を特定できず、FAQ とキットはゲートウェイ拒否で読めない。
- [予定] **Copilot Studio の9月 GA 期日（残り4日）** — Roadmap の Copilot Studio 起票22件は全件が `In development` のままで、GA 期日 September CY2026 の **14件**は残り4日になった。What's New は July 2026 節が最新で、GitHub Copilot ハーネスの GA（8/3）は54日反映されていない。
- [据え置き] **Release Notes・Power Platform・Roadmap** — M365 Copilot Release Notes は 9/23 バッチが最新のままで、Power Platform ブログ3本・Release Wave・Released Versions（Copilot Studio 2026.6.3）も更新が無い。Roadmap の 9/24 22:58Z バッチ10件は Field Service 7件などで対象外、Qiita / Zenn にも掲載に値する新規記事は無い。

### OpenAI / Codex / ChatGPT

- [新機能] **Codex `rust-v0.157.0`** — OpenAI が 9/25 に Codex の安定版を出し、GPT-6 Sol / Luna を Amazon Bedrock 経由でも使えるようにした。
  - 既定の変更: フルスクリーンのトランスクリプトが既定でオンになり、対象の対話セッションではバックグラウンドサーバーが自動で起動する
  - 追加: 下書きとキュー済みプロンプトを保つ会話フォークのショートカット、バックグラウンドサーバーでの `/import`
  - 修正: ネットワーク制限がリダイレクトと HTTP / WebSocket 通信にも掛かるようになった
  - pre-release は `0.159.0-alpha.1`（9/25）まで進んだ
  - https://github.com/openai/codex/releases
- [新機能] **ChatGPT for iOS のホーム刷新** — OpenAI が 9/23 に ChatGPT for iOS を更新し、iPad の横向きでタスク一覧と開いたタスクを並べて表示できるようにした。サイドチャットには添付・選択テキスト・レビューコメントが引き継がれる。https://developers.openai.com/codex/changelog/#codex-2026-09-23-mobile
- [動向] **豪 Medicare 不正アクセスの続報** — ABC News・NPR によると、アルトマン CEO が首相との電話で対応が「不十分だった」と認め、首相は法的措置に言及した。OpenAI は「調査中で、患者記録へのアクセスの証拠はない」とコメントしたが、自社ブログでの説明は出ていない。https://www.npr.org/2026/09/24/g-s1-144835/openai-breach-australia
- [観測] **Deep research の ChatGPT Work / Codex 対応** — ChatGPT Work と Codex で Deep research が使えるようになったとする二次情報がある。公開日は確認できず、`learn.chatgpt.com` の changelog RSS にも載っていない。
- [据え置き] **料金・廃止・API changelog** — OpenAI の一次料金ページは前日から据え置きで、GPT-6 Astra $10/$50・Sol $2/$10・Luna $0.10/$0.50 を再確認した。API changelog と Developer Community は 9/22 の GPT-6 Sol / Luna が最上位のままで、廃止ページでは 9/28 の4モデル停止を再確認した。DevDay は 9/29 にサンフランシスコで開かれる。https://developers.openai.com/api/docs/deprecations

### Google

- [新機能] **Workday for Google Sheets** — Google が 9/25 の Workspace 週次まとめで、Workday Adaptive Planning のデータを CSV を介さず Sheets / Slides に取り込めるアドオンを載せた（Rapid / Scheduled とも）。http://workspaceupdates.googleblog.com/2026/09/weekly-recap-09-25-2026.html
- [観測] **Gemini 4 の時期** — Google DeepMind の Koray Kavukcuoglu が 9/23 の登壇で、Gemini 4 は post-training 中で「年末よりずっと早く」出すと述べた。日付は示していない。https://9to5google.com/2026/09/24/google-says-gemini-4-release-is-coming-as-soon-as-possible/
- [据え置き] **Gemini API** — changelog は 9/22 の 3.8 Flash TTS / Flash-Lite TTS GA が最上位のままで、廃止ページでは 9/30 の `gemini-omni-flash-preview`、10/2 の `gemini-2.5-flash-image`、10/5 の `antigravity-preview-05-2026` の停止を再確認した。https://ai.google.dev/gemini-api/docs/deprecations

### Cursor / xAI / オープンウェイト

- [据え置き] **Cursor** — changelog は 9/23 の Rollouts and Security Review が最上位のままで、フォーラム Announcements も 9/21 の Grok 4.7 から動かず、Opus 5.5 と GPT-6 Sol / Luna の提供開始は4日目も告知されていない。
- [観測] **xAI / Devin** — `x.ai` と `docs.devin.ai` はゲートウェイ拒否のままで、9/24〜25 付の一次は確認できていない。
- [据え置き] **MCP・オープンウェイト・Apple** — MCP ブログは 8/22 の「The New MCP Roadmap」が最上位のままで、Hugging Face の登録8 org にも前回記録にない新規リポジトリは無い。`developer.apple.com/news/` も 9/18 の iPhone Duo 向けリソースから動いていない。

### 市場・企業

- [動向] **Anthropic × Akamai の7年 $11.6B 契約** — Akamai が 9/24（米国時間）に、Anthropic の CPU ワークロードを担う同社史上最大の契約を発表した。Akamai は Anthropic に最大約5%（行使価格 $111.33）のワラントを発行し、うち約2%は今回確定、残る約3%は最大 $9B の追加購入 $3B ごとに約1%ずつ確定する。⚠️ SEC Form 8-K の存在は確認したが本文は TechCrunch のスニペットによる。https://techcrunch.com/2026/09/25/anthropic-to-pay-akamai-11-6-billion-over-seven-years-in-cloud-deal/
- [動向] **Stargate ニューメキシコ拠点の不可抗力通知** — Oracle が開発者の Blue Owl 系会社に不可抗力通知を送ったと TechCrunch・CNBC が 9/24 に報じた。電力確保の遅れで2028年の稼働目標に届かない場合の支払い猶予を確保する狙いとされ、拠点は1,400エーカー・銀行融資 $18B の規模である。Oracle は「計画どおり」とだけコメントした。https://techcrunch.com/2026/09/24/oracle-sends-force-majeure-notice-on-its-new-mexico-stargate-data-center/
- [動向] **Gartner の世界 AI 支出予測** — Gartner が 9/16 に、2026年の世界 AI 支出を $2.7T（前年比 +49.5%）と予測した。未収録だったため10日遅れで載せる。https://www.gartner.com/en/newsroom/press-releases/2026-09-16-gartner-forecasts-worldwide-ai-spending-to-grow-49-point-5-percent-in-2026
- [動向] **Ando の $20M シード** — Ando が、人とエージェントが同じワークスペースで働くチームメッセージングアプリを公開し、Accel などから $20M を調達した（9/24）。エージェントは独自の ID と受信箱を持つメンバーとして参加し、Codex・Claude・Grokbot などに対応する。https://techcrunch.com/2026/09/24/ando-eyes-slack-as-it-builds-team-messaging-platform-for-humans-and-agents-to-work-together/
- [予定] **Dataiku Agent Management** — Dataiku が 9/24 に、複数プラットフォームのエージェントを一覧化して KPI とリスク階層を管理する単体製品を発表し、10月に GA する予定とした（二次のみ）。
- [据え置き] **定点データ** — IDC・MM総研・NRC・Similarweb はいずれも新規公表が無い。NRC の9月調査は10月公開の見込みである。

## 直近の注目予定

- **9/28**: Copilot のチャット3面統合 ／ code review の既定 effort が Balanced へ ／ チャットのデータ保持変更 ／ OpenAI の `gpt-3.5-turbo-instruct` / `babbage-002` / `davinci-002` / `gpt-3.5-turbo-1106` が停止 ／ Anthropic × Adaptyv コンペ開始
- **9/29**: OpenAI DevDay（サンフランシスコ） ／ Google Meet「Take notes for me」の新設定が有効化
- **9/29 以降**: `claude-sonnet-4-5-20250929` の暫定退役日（廃止通知は未発出）
- **9/30**: Copilot in SharePoint の GA 展開開始 ／ Autopilot の Private Preview 拡大 ／ CSP の M365 E5 / E7 / Copilot プロモーション終了 ／ Gemini の `gemini-omni-flash-preview` が停止 ／ Copilot Studio の Roadmap 14件が GA 期日 ／ Copilot Dev Camp Summit ／ Clinical Applications スペシャライゼーションの受付開始 ／ OpenAI の現行 OneGov 契約が失効
- **10/1**: CSP 成長マージンの一般提供 ／ Microsoft CSP ソフトウェア価格改定が発効 ／ OpenAI の `gpt-5.4-cyber` が API から削除 ／ Copilot Business・Enterprise の既存顧客が前払い必須に ／ ChatGPT for Word の Word アクセスが既定オンへ
- **10/2**: GitHub Copilot が4モデルを廃止 ／ Gemini の `gemini-2.5-flash-image` が停止
- **10/5**: Gemini の `antigravity-preview-05-2026` が停止 ／ GPT-Rosalind の課金開始
- **10/13**: Office / Project / Visio LTSC 2021 のサポート終了 ／ 新しい Copilot の Partner Digital Airlift
- **10/14**: GitHub SSH の新規 RSA 鍵が 3072 ビット以上必須に ／ OpenAI の `gpt-5.5` が ChatGPT / Codex から退役（API は対象外）
- **10/16〜11/10**: OpenAI DevDay Exchanges（東京を含む8都市）
- **10/19**: GitHub Copilot が5モデルを廃止（Gemini 3.7 Flash / GPT-5.5 / GPT-5.4 / GPT-5.4 mini / Grok 4.5）
- **10/21**: GitHub Copilot の新機能既定ポリシーの設定期限（10/22 発効）
- **10/23**: OpenAI のレガシースナップショット12件が退役
- **10 月中**: 570964 フェデレーテッドコネクタの書き込み対応 GA ／ 569018 Brand Kit スキル GA ／ Copilot Studio エージェントがコスト管理の対象に ／ Dataiku Agent Management GA
- **10/27〜29**: PPCC 2026
- **10/31**: OpenAI の既存 evals が読み取り専用に
- **11/2**: GitHub Actions の `pull_request_target` 既定無効化が公開リポジトリで強制開始 ／ M365 Copilot Business の従量課金が既定オン
- **11/4**: GitHub SSH `ssh-rsa` の1回目のブラウンアウト
- **11/12**: OpenAI が Cursor へのモデル供給を停止する予定日（一次未読）
- **11/15**: Microsoft Release Planner 退役
- **11/17〜20**: Microsoft Ignite
- **11/21**: GPT-5.6 Sol の期間限定価格の下限
- **11 月中**: 572682 モデル駆動型アプリの表示密度 GA
- **11/30**: OpenAI の Reusable prompts・Evals・Agent Builder が停止
- **12/1**: OpenAI の GPT Image 系が停止
- **12/9**: GitHub SSH `ssh-rsa` の2回目のブラウンアウト
- **12/11**: OpenAI の GPT-5 / o3 系スナップショットが停止
- **12/31**: 非営利向け M365 Copilot の併用プロモーション終了 ／ Gemini 3.8 Flash と 3.7 Flash の導入価格が終了 ／ GitHub Copilot の Fable 5.1 / Fable 5 に対する ZDR 暫定免除が終了
- **数週間内**: Claude Sonnet 5.5 と Claude Haiku 5.5 のリリース（日付未提示） ／ 新しい Copilot の Home / Code が Frontier で展開開始
- **2027年3月中旬**: CodeQL 全プラットフォーム版バンドルの削除

## 改善メモ

- 新規提案: Copilot が2件を起票した。B-077 は www.microsoft.com のブログ RSS がクエリ無し URL でキャッシュ版（9/14・9/19）を返して当日の新着を落とす件、B-078 は環境ルーティングの管理者ページが Copilot Managed Runtime 名の URL へ 301 移設された件である。Master・industry は新規なし
- 継続提案: Master 5件を再確認（最多 B-035 npm dist-tags・41回目。`2.1.283` が changelog 未記載のまま `next` に publish）／ industry 10件を再確認（最多 B-004・89回目）
- 障害の変化: Master の `cursor.com/changelog/rss.xml` が復旧した（9/26 に curl 200 / `application/rss+xml`）。Copilot の `mc.merill.net` は50日連続で拒否が続く
- 本サマリーの取りこぼし: 前日のサマリーは 9/24 付の GitHub changelog 3件（Copilot 既定ポリシー・再認証・期限切れ artifact）と Claude Platform の 9/24 付2項目（Compliance API）を落としていた。いずれも後から掲載・再読で捕捉されたもので、本日のハイライト1・3とカテゴリに収めた
- ソース間の差分・矛盾:
  - Claude Code は industry が「2.1.282 から版が上がっていない」、Master が `2.1.283` の `next` publish を記録している。changelog 未記載の publish なので両者は矛盾しないが、本サマリーは Master の npm 実測を採った
  - npm の `stable` は前日のサマリーが `2.1.273`、本日の Master が `2.1.274` で、1日で1版進んだものとして扱う
  - 10/19 の GitHub Copilot 廃止モデル数は industry が本日も「6モデル」のままで、Master の 9/18 告知本文に基づく **5モデル**を引き続き採る
  - Copilot の既定ポリシーは Master が発効日 10/22、industry が設定期限 10/21 で書いており、同じ事実の表現差である
  - 新しい Copilot の課金単価は industry が二次（$0.01/credit・前払い割引5〜20%）を併記し、Copilot は一次に上限の数値も単価も無いとしている。本サマリーは一次に無い旨を注記して二次の値を残した
  - industry が前日「抽出から落ちた」とした OpenAI の 9/28 停止4モデルと Gemini の 10/2 停止は、本日の一次で再確認された
  - 新しい Copilot は industry が料金、Copilot が予定としてハイライトに置いた。本サマリーは課金整理（料金+新機能）と製品発表（予定）を別項目に分けた
