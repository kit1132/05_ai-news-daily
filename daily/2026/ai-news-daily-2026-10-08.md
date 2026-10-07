# AI News Daily Summary — 2026-10-08

Anthropic は Claude Haiku 5.5 を出して小型モデルの単価を Haiku 4.5 の10分の1に下げ、Max / Team に毎月の API クレジットを付けた。GitHub は Copilot のローカルサンドボックスを GA にした。Microsoft は M365 Copilot Release Notes に約2週間ぶりの10/6 バッチを載せ、Copilot Studio で Foundry IQ 連携を GA にした。

## 今日のハイライト

### 1. [料金+新機能] Anthropic が Claude Haiku 5.5 を出し、Haiku の単価を 4.5 の10分の1に下げた — 小型枠は「安いが弱い」から「GPT-6 Luna と同単価で OSWorld 72.4%」に変わった

**要点**: Anthropic が `claude-haiku-5-5` を API と主要3クラウドで公開した（10/7）。10万トークン以下は入力 $0.10・出力 $0.50 で Haiku 4.5（$1 / $5）の10分の1、GPT-6 Luna と同じ単価になった。Claude Code も既定の Haiku を 5.5 に切り替えた。

**詳細**:

- 価格（100万トークンあたり）: 10万トークン以下は入力 $0.10 / 出力 $0.50 / キャッシュ読み取り $0.01。10万超は入力 $0.50 / 出力 $2.50。Batch はさらに半額。Anthropic は新トークナイザーの増加分を織り込んでも平均で約75%安いとしている
- 仕様: 1M コンテキスト・最大出力 128k・adaptive thinking と effort（既定 `medium`）。知識カットオフ 2026年6月、退役は「Not sooner than October 7, 2027」
- ベンチマーク（Haiku 5.5 / Haiku 4.5 / Sonnet 5.5）: OSWorld 2.1 オフライン 72.4% / 15.7% / 83.9%、Terminal-Bench 4.0 39.2% / 0.0% / 70.6%。GPT-6 Luna は OSWorld 48.9%・Terminal-Bench 16.4%
- Haiku 4.5 からの破壊的変更: `budget_tokens` の手動 extended thinking、`temperature` / `top_p` / `top_k` の非既定値、assistant の prefill がいずれも 400 になる。`computer_20250124` は `computer_toolset_20260801` へ置き換えが必要
- 挙動の変化: 応答が `thinking` ブロックから始まることがある。新トークナイザーで同じ文が約30%多く数えられる。安全分類器が `stop_reason: "refusal"` を返すことがある
- 提供先: Claude API・Amazon Bedrock・Claude Platform on AWS・Google Cloud・Microsoft Foundry。Claude Code は `2.1.293` で既定の Haiku を 5.5 にした
- `claude-haiku-4-5-20251001` は Active・「Not sooner than October 15, 2026」のままで、退役告知は出ていない

- https://www.anthropic.com/claude-haiku-5-5
- https://platform.claude.com/docs/en/models/haiku-5-5/whats-new-haiku-5-5
- https://platform.claude.com/docs/en/release-notes/overview
- https://platform.claude.com/docs/en/about-claude/pricing

### 2. [料金] Anthropic が Max と Team に毎月の API クレジットを付け、Sonnet 5.5 のキャッシュ読み取りを半額にした — 「チャットのサブスクと API は別予算」という前提が変わった

**要点**: Anthropic が Max 5x に月 $100、Max 20x に月 $200、Team に最大月 $500 の Claude Platform クレジットを付けた（10/7）。Console の組織を1つ紐づければ、小規模な PoC やエージェントの検証費をサブスクの月額に含められるようになった。

**詳細**:

- Team: Standard 席 $20・Premium 席 $100 を合算し、上限 $500 でプールする。月初時点の席数で決まる
- 対象: Claude API・Managed Agents・Agent SDK・Playground。Claude Code とアプリの追加利用分、Bedrock など他クラウドでは使えない
- 失効: 請求期間ごとに失効し繰り越さない。購入クレジットより先に消費される
- 受け取り: claude.ai の Settings > Billing（Team は Organization settings > Billing）で Console 組織を紐づける。1プランにつき1組織で、後から自分では変えられない。新規契約は7日後から。Free / Pro / Enterprise は対象外
- 利用上限: クレジットが月 $200 を超える組織は Build ティア以上になるが、クレジットの消費は上位ティアへの昇格条件に数えない
- Sonnet 5.5 のキャッシュ読み取りを $0.20 → $0.10（基本入力の0.05倍）に下げた。Anthropic は大半のエージェント作業で約20%安くなるとしている。料金ページのモデル別表は本日時点で $0.20 のままで、同じページの本文とリリースノートの $0.10 と食い違っている

- https://platform.claude.com/docs/en/about-claude/api-credits-for-subscribers
- https://support.claude.com/en/articles/12138966-release-notes
- https://platform.claude.com/docs/en/about-claude/pricing

### 3. [新機能] GitHub が Copilot のローカルサンドボックスを GA にした — エージェントの自律実行の前提が「信頼するか」から「境界内で動かすか」に変わった

**要点**: GitHub が、Copilot が手元で実行するツールやコマンドのファイル・ネットワーク・認証情報へのアクセスをポリシーで制限する機能を一般提供にした（10/7）。追加料金は無く、Enterprise の管理側が必須にしたポリシーは開発者が緩められない。

**詳細**:

- 対象: Copilot CLI、Copilot アプリ、Agent Host を使う VS Code のセッション
- 基盤: Microsoft eXecution Container（MXC）が共通ポリシーを Windows / macOS / Linux のネイティブ制御へ変換する
- 制御できるもの: 読み書きできるディレクトリ、インターネットとローカルネットワーク、Git と GitHub CLI の認証情報。対応していればローカル MCP と言語サーバーにも掛かる
- Copilot CLI 安定版 `v1.0.93`（10/7）で `/sandbox` と `--sandbox` が全ユーザーに開放された。既定でオンかどうかは記載が無い

- https://github.blog/changelog/2026-10-07-local-sandboxing-for-github-copilot-now-generally-available
- https://github.com/github/copilot-cli/releases

## カテゴリ別まとめ

### Claude / Anthropic

- **Haiku 5.5 と既定 Haiku の切替**（ハイライト参照・1）
- **Max / Team の API クレジットと Sonnet 5.5 キャッシュ値下げ**（ハイライト参照・2）
- [セキュリティ+新機能] **Claude Code 2.1.293** — Anthropic が Claude Code `2.1.293` を npm の `latest` / `next` に出し、`claude agents` がバックグラウンドのセッションでは効かない権限バイパスを提示していた不具合を直した（10/7 17:18 UTC）。`stable` は `2.1.285` のまま。
  - 同意の確認: `.claude/settings.local.json` や `--settings` のファイルにしか同意が保存されていない場合は、先に確認するようにした
  - `subagentStatusLine`: ペイロードに `agentType` が入り、カスタムサブエージェントの種別を区別できる
  - mods の `$.tool.register`: `isDeferred: false` でツールのスキーマを最初からプロンプトに載せられる
  - 修正: コンパクション前の操作を未完了と誤認してやり直す問題、HTTP MCP 接続のメモリリーク、Bash の `cat` / `grep` でファイルを見たときにパス指定ルールと入れ子の CLAUDE.md が読み込まれない問題
  - 2.1.281 の auto mode 拒否メッセージ変更と、2.1.290 のクラウドセッション復帰修正を取り消した
  - https://code.claude.com/docs/en/changelog
- [破壊的変更] **Managed Agents の `allowed_hosts`** — Anthropic が Managed Agents の `limited` ネットワーク環境で、`allowed_hosts` を `web_search` / `web_fetch` にも適用するようにした（10/7）。許可外ホストへの `web_fetch` は `url_not_allowed` を返し、`allowed_hosts` が空なら両ツールとも何も返さない。`allowed_hosts` 外の `allowed_domains` があるとセッション作成・更新が 400 になり、`["example.com"]` は `docs.example.com` を含まないため `*.example.com` を使う。https://platform.claude.com/docs/en/release-notes/overview
- [新機能] **SDK の browser use / computer use クラス** — Anthropic が Python / TypeScript SDK に、browser use ツールと computer use ツールのベータのクラスを入れた（10/7）。クラスを継承してツールごとに1メソッドを書けば、ツールループ・ブラウザの URL / ファイルポリシー・承認コールバックは SDK が回す。https://platform.claude.com/docs/en/release-notes/overview
- [新機能] **Compliance API の統合チャット対応** — Anthropic が Compliance API のチャット系エンドポイントで、統合後の Claude 体験のチャットも返すようにした（10/8・Enterprise 向けベータ）。既存の Compliance Access Key で使える。https://platform.claude.com/docs/en/manage-claude/compliance-content-data
- [新機能] **Models API の能力フィールド** — Anthropic が Models API に `capabilities.server_tools`（10/6）と `capabilities.thinking.types.disabled`（10/5）を足した。各モデルが web search / code execution を受け付けるか、thinking を無効にできるかを API から判定できる。https://platform.claude.com/docs/en/release-notes/overview
- [動向] **platform.claude.com の障害2件** — Anthropic の platform.claude.com で、使用量データ読み込みのエラー（10/7 02:33 UTC 解決）と全般のエラー率上昇（10/7 17:28 UTC 解決）が起き、いずれも解消した。https://status.claude.com/incidents/978mjkgw6mh7
- [動向] **TPU リース向け $60B 融資** — Bloomberg が、Broadcom と組む銀行団が Anthropic の TPU リースを支える $60B のチップ融資を集め始めたと報じた（10/2）。10/6 に Bank of America・Citigroup・Morgan Stanley がシンジケーションを始め、シニア担保付き $42B と Blackstone が $9B を出すジュニア $18B の2層構造になる。正式発表は無く両社ともコメントしていない（二次のみ）。https://www.bloomberg.com/news/articles/2026-10-02/broadcom-starts-amassing-60-billion-to-fund-chips-for-anthropic
- [据え置き] **Anthropic news・Claude blog** — `www.anthropic.com/news` は 10/6 の Cyber Verification Program、`claude.com/blog` は 10/6 の Google Workspace 対応が最上位のままである。Haiku 5.5 の発表は `/news` ではなく `www.anthropic.com/claude-haiku-5-5` に出た。

### OpenAI / Codex / ChatGPT

- [新機能] **GPT-6 と Intelligent UI の全プラン展開** — OpenAI が、回答の中にグラフ・ボタン・フォームを組み込む Intelligent UI を GPT-6 と合わせて ChatGPT の全プランに広げた（10/7）。有料プランから順に展開し、Free と Go には 10/8 に届く。同じ日に API の `chat-latest` も ChatGPT の最新モデルを指すように更新され、本番用途には GPT-6 系を推奨している。OpenAI は ChatGPT の週間利用者を12億人超としている。https://openai.com/index/gpt-6-for-everyone/ / https://developers.openai.com/api/docs/changelog
- [料金+新機能] **Decisions API のベータ** — OpenAI が分類専用の Decisions API（`v1/decisions`）を `gpt-6-luna` でパブリックベータにした（10/6）。述語の確率・選択肢の選択・段階評価の3種の型付き出力を返し、Responses API 経由より最大10倍速いとしている。料金は入力 $0.10 / 100万トークンのみで、出力とキャッシュの課金は無い。画像は base64 埋め込みに限り、GA は「数週間以内」の予定。https://community.openai.com/t/decisions-api-is-now-available-in-public-beta/1403877 / https://developers.openai.com/api/docs/guides/decisions
- [破壊的変更] **Codex CLI 0.161.0** — OpenAI が Codex CLI の安定版 `0.161.0` で既定モデルを GPT-6.1 Sol に変えた（10/7）。Bedrock でのマルチエージェント v2、ターミナル内の `/mcp login <name>`、セッションごとのサイバーアクセスプログラム指定も入った。pre-release は `0.162.0-alpha.18` まで進んだ。https://github.com/openai/codex/releases
- [新機能] **ChatGPT for iOS の Codex 対応** — OpenAI が ChatGPT for iOS で Codex タスクのリンクを直接開けるようにし、承認ピッカーを作り直した（10/7）。応答内のページプレビュー、長いスレッドのストリーミング高速化、デスクトップと同じ checkout に揃う worktree 対応も入った。https://learn.chatgpt.com/docs/changelog

### GitHub Copilot / GitHub

- **ローカルサンドボックスの GA**（ハイライト参照・3）
- [新機能] **Copilot CLI v1.0.93** — GitHub が Copilot CLI の安定版 `v1.0.93` を出した（10/7）。エンタープライズの `permissions.limitTo` でネットワーク要求の宛先を管理ドメインに縛れるようになり、MCP サーバー設定の変更が再起動なしでターン間に反映される。ユーザー設定は `~/.copilot/settings.json` だけを読み、`config.json` 内のユーザー設定キーは無視されるようになった。https://github.com/github/copilot-cli/releases
- [新機能] **Copilot CLI の Ollama ローカルモデル** — GitHub が Copilot CLI `1.0.94-0` 以降の `/model` で、起動中の Ollama のローカルモデルを見つけて選べるようにした（10/7）。ツール呼び出しとストリーミングに対応するモデルに限り、ローカルモデルを選んでもオフラインモードにはならずテレメトリも止まらない。https://github.blog/changelog/2026-10-07-discover-local-models-in-github-copilot-cli
- [料金+新機能] **シークレット検出の専用モデル** — GitHub が、周辺コードから形式の無いパスワードまで推定するシークレット検出専用の微調整モデルに切り替えた（10/7）。既存の AI 検出アラートは新モデルへ自動で移り GHSP / GHAS に含まれたままだが、新たに加わる push protection と `/security-review` のシークレット検査は AI Credits の従量課金になる。push protection の課金はブロックしなくても発生してリポジトリ所有組織に付き、予算アラートだけでは止まらないため「予算上限で利用停止」の設定が要る。GHES 3.23 にも AI 検出アラートがパブリックプレビューで入る。https://github.blog/changelog/2026-10-07-purpose-built-model-for-leaked-secret-detection
- [観測] **利用状況メトリクスのエージェント過少計上** — GitHub が、Copilot SDK に移った IDE のエージェントセッションが利用状況メトリクスから漏れ、一部が CLI として数えられていたと公表した（10/6）。課金には影響しない。VS Code は 1.139.0 以降で直り、Visual Studio は10月中、JetBrains は10月下旬、Eclipse と Xcode は11月までに修正版が出る。欠けた期間のデータは後から復元できない。https://github.blog/changelog/2026-10-06-update-your-ide-to-restore-agent-activity-in-copilot-usage-metrics
- [新機能] **スタック型プルリクエストの GA** — GitHub が github.com の全プランでスタック型 PR を GA にした（10/6）。コードが変わらなければリベース後も承認が残り、マージキューもスタック単位で通る。`gh stack` 拡張は Git worktree に対応した。https://github.blog/changelog/2026-10-06-stacked-pull-requests-generally-available <!-- ai_unrelated -->

### Microsoft 365 Copilot / Copilot Studio / Power Platform

- [新機能] **M365 Copilot Release Notes の10/6 バッチ** — Microsoft が Release Notes に 9/22〜10/6 分の7項目を加え、先頭 H2 が September 23 から October 06, 2026 に変わった。利用者は Copilot Search の結果を起点にチャットで追質問でき、管理者はコネクタの設定を作成後に自分で直せるようになった。
  - Copilot Search と Chat の統合（512429・Windows / Web）: 検索結果をもとにチャットペインで追質問・要約・コンテンツ生成ができる
  - Regenerate（Web）: 応答末尾の「More options」から Try Again と Switch Model を選べる
  - Copilot コネクタ: 管理者が M365 管理センター > 設定 > Search & intelligence > Data sources で、作成済み接続のクエリ文字列とユーザー ID マッピングを編集できる。従来は作成時に固定され、変更にはサポート依頼が必要だった
  - SharePoint（561038）: SharePoint Advanced Management の管理者が、Everyone 系に付与された権限をアイテム単位で一覧するレポートを Data access governance reports から出力できる
  - PowerPoint: Windows は Copilot ペインからカスタムスキルを作成でき、Mac（555897）はプロンプトで挙げた SharePoint / OneDrive のファイルを添付なしで参照する
  - Viva Insights（567005）: Copilot ダッシュボードと Consumption ダッシュボードに Cowork の利用・効果の指標が加わった
  - https://learn.microsoft.com/en-us/microsoft-365/copilot/release-notes
- [新機能] **Foundry IQ 連携の GA** — Microsoft が Copilot Studio の9月アップデート記事（10/7）で、Foundry IQ 連携の GA を告知した。Azure AI Foundry の1つのナレッジベースを複数のエージェントから引用付きで参照でき、プライベートネットワーク経由でも接続できる。GitHub Copilot ハーネスのエージェントに限られ UBB（Copilot Credits）の対象で、接続は1エージェントにつき1つまで。認証は API キー・クライアント証明書・サービスプリンシパル・Entra ID 統合から選び、検索精度の調整は Foundry 側で行う。手順ページ `foundry-iq-connect`（`ms.date` 6/23）はまだ GA に合わせて改訂されていない。https://www.microsoft.com/en-us/copilot/blog/copilot-studio/new-and-improved-build-apps-extend-agents-and-transform-business-processes-in-microsoft-copilot-studio/ / https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-experience/foundry-iq-connect
- [新機能] **Copilot Studio の Review パネル GA** — Microsoft が、メーカーが公開前に阻害要因と警告を重大度順に確認できる Review パネルを GA にした（9月アップデート記事）。評価を一度も実行していないエージェントや、モデル変更で評価結果が古くなったエージェントにも警告が出る。同じ記事は評価のタスク完了・ツール精度の指標、Custom Graders Library、plugin registry の Copilot Studio 対応（今後数週間で展開）も挙げている。https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-experience/authoring-agent-status
- [仕様] **接続エージェントの制約** — Microsoft が `authoring-add-other-agents` を改訂し（`ms.date` 10/6）、GitHub Copilot ハーネスで接続できるのは Copilot Studio 製エージェントだけと明記した。委任時はオーケストレーターがユーザーの依頼を言い換えることがあり、ハンドオフにはペイロード上限がある。https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-experience/authoring-add-other-agents
- [仕様] **ファイル入力の上限** — Microsoft が `image-input-analysis` を改訂し（`ms.date` 10/7）、標準ハーネスではコードインタープリターが無いと Office 文書の抽出テキストは合計3万字までで、超えたファイルは破棄されると明記した。Word のテキストボックス・SmartArt・ヘッダーは読まれない。旧版と比べられず、どこが今回の追加かは特定できていない。https://learn.microsoft.com/en-us/microsoft-copilot-studio/image-input-analysis
- [新機能] **デスクトップフローのスケジュールトリガー（573278）** — Microsoft が Power Automate で、中継用のクラウドフローを作らずに自動化センターからデスクトップフローの定期実行を直接設定できるようにした。Roadmap は 10/6 起票で Launched（Preview September / GA October CY2026）である。https://www.microsoft.com/microsoft-365/roadmap?id=573278
- [予定] **デスクトップフローのフローチャートモード（573292）** — Microsoft が Roadmap に、デスクトップフローをノード図で作成・編集するフローチャートモードを起票した（10/6）。Preview October / GA November CY2026 の予定である。https://www.microsoft.com/microsoft-365/roadmap?id=573292
- [観測] **Learn の一括再ビルドと製品名の変更** — Microsoft が 10/7 に Copilot Studio のセキュリティ・統制系約45ページとガイダンス系約15ページを再ビルドしたが、`ms.date` はどれも動いていない。データ統制の展開ガイド `configure-secure-governed-data-foundation-microsoft-365-copilot`（`ms.date` 10/6）は題名と本文の製品名が「Microsoft Copilot」になり、前提ライセンスに Microsoft 365 E7 が書かれたが、旧版との差分は特定できていない。https://learn.microsoft.com/en-us/microsoft-365/copilot/configure-secure-governed-data-foundation-microsoft-365-copilot
- [据え置き] **Power Platform の定点** — Power Platform の親 RSS は先頭が 10/1 の PPCC 告知記事のまま、Release Wave の製品別5ページは 9/3 のままで、Copilot Studio の最新ビルドも 2026.6.3 のまま99日である。

### Google / Cursor / その他

- [新機能] **Cursor の Remote control** — Cursor が iOS アプリから手元のローカルエージェントの状況を見て返信できる Remote control を出した（10/6）。エージェントはクラウドへ移らずローカルで動き続け、デスクトップ側でペアリングを承認する。Enterprise は既定で無効で、管理者が Security and identity で有効にする。https://cursor.com/changelog/remote-control-local-agents
- [据え置き] **Gemini API・Gemini アプリ** — Google の Gemini API changelog の最上位は 10/6 の画像生成モデル `gemini-nano-banana-2.1` の GA で、画像生成のため対象外である。Gemini アプリ無料枠の Flash-Lite 限定（10/9 発効の報道）は一次がまだ確認できていない。
- [据え置き] **Cursor フォーラム・xAI・MCP・HF・Apple** — Cursor フォーラム Announcements は 9/21 の Grok 4.7 が最上位のままで、xAI の新しい発表も見つからない。登録8 org の Hugging Face 一覧に新しいリポジトリは無く、`blog.modelcontextprotocol.io` は 8/22、`developer.apple.com/news/` は 10/5 が最上位のままである。
- [据え置き] **市場データ** — IDC Japan・MM総研・NRC・Similarweb はいずれも新規公表が無く、Similarweb の9月分トラッカーも未検知のままである。

## 直近の注目予定

- **10/8**: Copilot Studio の学習ウェビナー（Skill up on Microsoft Copilot Studio） ／ ChatGPT の Free / Go に GPT-6 と Intelligent UI が届く
- **10/9**: Gemini アプリの無料ユーザーが Flash-Lite のみ、AI Plus が Pro を失う（報道）
- **10/13**: Gemini アプリで skills の展開開始 ／ Office / Project / Visio LTSC 2021 のサポート終了 ／ 新しい Copilot の Partner Digital Airlift
- **10/14**: GitHub SSH の新規 RSA 鍵が 3072 ビット以上必須に ／ GPT-5.5 が ChatGPT / Codex から退役 ／ Anthropic の pre-IPO investor day（報道）
- **10/15 以降**: `claude-haiku-4-5-20251001` の暫定退役日（告知はまだ無い）
- **10月**: Copilot Chat の UBB モデル選択 GA（571400） ／ デスクトップフローのスケジュールトリガー GA（573278） ／ スキルカタログ GA（571880） ／ 自己学習 GA（570432） ／ Reflection AI Beam の重み公開（予定） ／ Visual Studio の Copilot メトリクス修正版
- **10/19**: GitHub Copilot が5モデルを廃止 ／ Workspace の skills 展開開始（Scheduled Release）
- **10/21**: GitHub Copilot の新機能既定ポリシーの設定期限（10/22 発効）
- **10/23**: OpenAI のレガシースナップショット12件が停止
- **10/27〜29**: PPCC 2026（ラスベガス）
- **10/30**: ChatGPT Pro 200 の Work / Codex 利用枠が変更（二次）
- **10/31**: MCP サーバー認定の旧申請経路が終了 ／ OpenAI Evals が読み取り専用化
- **11/1**: Codex の28日間「改善かリセット」の終了（二次）
- **11/2**: GitHub Actions の `pull_request_target` 既定無効化が公開リポジトリで強制開始
- **11/4**: GitHub SSH `ssh-rsa` の1回目のブラウンアウト
- **11月**: フローチャートモード GA（573292） ／ Eclipse / Xcode の Copilot メトリクス修正版
- **11/12**: OpenAI → Cursor のモデル供給停止予定（一次未読）
- **11/15**: Microsoft Release Planner 退役
- **11/17**: Gems が Gemini アプリの設定パネルへ移動
- **11/17〜20**: Microsoft Ignite
- **11/30**: `claude-sonnet-4-5-20250929` が Claude API から退役 ／ OpenAI の `v1/prompts`・Evals・Agent Builder が停止
- **12/1**: Copilot Business の従量課金が既定オン
- **12/31**: Gemini 3.8 Flash の導入価格が終了 ／ 非営利向け M365 Copilot の併用プロモーション終了
- **2027-01-06**: OpenAI `tts-1` / `tts-1-hd` / `gpt-4o-mini-tts` 2版が停止
- **2027-03-01 以降**: Gems 廃止（Business / Enterprise）
- **2027-04-01**: OpenAI `gpt-5.1` / `gpt-5.3-codex` / `gpt-5.4-nano` が停止
- **2027-10-07 以降**: `claude-haiku-5-5` の退役下限日

## 改善メモ

- 新規提案: 3ソースとも無し
- 継続提案: Master は B-035 npm dist-tags（53回目）・B-079 HF の ID 集合差分（7回目）・B-082 最上位エントリ基準の差分判定（14回目）を再確認 ／ Copilot は B-074（docset 全件突合・1,630ページ）・B-076（差分特定不可・2ページ）・B-037（99日）を更新 ／ industry は2件を更新（最多 B-004・100回目）。B-031 に OpenAI changelog 10/6 分（Decisions API）の取りこぼしを追記
- 障害の変化: 3ソースとも無し
- ソース間の差分・矛盾:
  - Haiku 5.5 は Master が [料金+新機能]、industry が [料金] で割れた。単価改定が主旨で新モデル公開を伴うため [料金+新機能] に揃えた
  - Claude Code 2.1.293 は Master が [新機能]、industry が [セキュリティ+新機能] で割れた。権限バイパス提示と同意確認の修正が入っているため [セキュリティ+新機能] を採った
  - シークレット検出モデルは Master が [料金]、industry が [セキュリティ+料金] で割れた。製品名の Security は判定に使わず、新モデル導入と従量課金化の同梱として [料金+新機能] にした
  - Copilot 利用メトリクスの過少計上は Master が [観測]、industry が [破壊的変更] で割れた。既存の設定・挙動を壊すものではなく計上の誤りの公表のため [観測] を採った
  - Decisions API は Master が [新機能]、industry が [料金+新機能] で割れた。優先順に従い [料金+新機能] とした
  - industry は Compliance API と SDK のツールクラス、スタック型 PR と Copilot CLI の Ollama 対応をそれぞれ1項目にまとめていた。1項目1リリースのため分けた
  - industry の Claude for Startups 拡大（10/6）は 10/7 の本サマリーで既報のため再掲しなかった。提供価値の合計は TechRadar が最大 $7,000、Inc. が最大 $7,500 と割れている
  - Sonnet 5.5 のキャッシュ読み取り単価は、料金ページの表（$0.20）と本文・リリースノート（$0.10）で一次どうしが食い違っている（Master・industry とも指摘）
