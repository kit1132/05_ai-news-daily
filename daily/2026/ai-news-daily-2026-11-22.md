# AI News Daily Summary — 2026-11-22

Claude Code 2.1.330 は `deniedMcpServers` の名前指定を1コネクタだけに狭め、Enterprise Admin Console の組織へのサインインを足した。npm の `stable` は 2.1.311 から 2.1.323 に進み、stable に固定した組織にもプロキシとサンドボックスの変更が届く。Microsoft は Copilot デスクトップアプリと Edge の同期を12月中旬に始める。

## 今日のハイライト

### 1. [破壊的変更+新機能] Claude Code 2.1.330 で `deniedMcpServers` の名前指定が1コネクタしか止めなくなった — Enterprise Admin Console の組織にサインインすれば、組織の設定とプロバイダーが端末に届く

**要点**: Anthropic が Claude Code `2.1.330`（11/20）で、名前で書いた `deniedMcpServers` の拒否を、その名前の claude.ai コネクタだけに狭めた。名前だけで同じ URL をまとめて塞いでいた組織では遮断が効かなくなる。あわせて、管理コンソールの組織へのサインインで設定を配る経路が加わった。

**詳細**: 一次（code.claude.com の changelog）で確認した（Master・industry）。
- `deniedMcpServers`: 同じ URL のコネクタをすべて止めるには、URL を正確に指定して拒否する
- Admin Console へのサインイン: サインイン後は組織の設定を適用し、組織が指定したクラウドプロバイダーかゲートウェイを使う。設定が効くのはその組織でサインインしたときだけで、サインインは強制できない。受け付ける設定キーは固定の一覧で、一覧外のキーは無視される
- 定期タスクと `/loop`: セッションが動いている間は最長30日動く（これまでは7日）。この版より前に作ったタスクは7日で終わる
- `rm`: ルート・ホーム・最上位フォルダー・作業フォルダーを狙うコマンドの多くに承認が要るようになり、応答できる人がいない環境では拒否される
- `max_tokens`: 2.1.329 で外した自動再試行を元に戻した。前日のサマリーで案内した `CLAUDE_CODE_MAX_OUTPUT_TOKENS` の設定は必須ではなくなった（industry）
- その他: グラフを描く組み込み mod「easel」（`/config` で自動描画を切れる）、`CLAUDE_CODE_FULL_SIGN_IN_LINK=1`、self-hosted runner の `--start-dir` と `/metrics` 2種、compact 直後の固まりと WebFetch の停止の修正
- 2.1.327 が予告した課金付き分類フォールバックの削除は、今回も書かれていない（industry）

出典:
- https://code.claude.com/docs/en/changelog
- https://claude.com/docs/third-party/claude-desktop/admin-console-claude-code.md

### 2. [破壊的変更] Claude Code の npm `stable` が 2.1.311 から 2.1.323 に進んだ — stable に固定した組織にも、12版分のプロキシ・サンドボックス・管理設定の変更が一度に届く

**要点**: npm の `stable` タグが 11/21 時点の `2.1.311` から `2.1.323` に進んだ。stable に固定した組織では、`ALL_PROXY` だけの構成で組織ポリシーの取得がプロキシを通らなくなり、サンドボックス内の `git worktree` 操作も失敗するようになる。

**詳細**（`2.1.323` までの changelog から、何もしないと挙動が変わるもの。Master）:
- プロキシ: 組織設定とポリシーのリクエストは `ALL_PROXY` だけのプロキシを使わない。必要なら `HTTPS_PROXY` を設定する
- 管理設定: `policyHelper` はユーザー設定と `--settings` ファイルの環境変数を受け取らない。必要な値は管理設定の `env` か起動シェルで渡す
- サンドボックス（macOS / Linux）: `git worktree add` / `move` / `remove` は読み取り専用で失敗し、開始時以外の worktree でのコミットも失敗する
- MCP: v1 クライアントを削除した。`MCP_SDK_GENERATION=v1` は v2 クライアントの互換モードで動く
- 削除・非推奨: `subagentStatusLine` を削除し、プラグインの `agent` 設定を非推奨にした
- 範囲外: 2.1.329 の予約タスクの再登録と 2.1.330 の `deniedMcpServers` の変更は stable にはまだ来ていない
- npm: `{stable: 2.1.323, latest: 2.1.330, next: 2.1.330}`

出典:
- https://registry.npmjs.org/@anthropic-ai/claude-code
- https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md

## カテゴリ別まとめ

### Anthropic / Claude

- **Claude Code `2.1.330`**（ハイライト1参照）
- **Claude Code npm `stable` 2.1.323**（ハイライト2参照）
- [据え置き] **Anthropic のその他の一次** — Claude Platform の release notes（11/17）、モデル退役一覧（Active 17件）と廃止履歴（9/30）、`support.claude.com`（11/20 の computer use）、`claude.com/resources/articles`（11/17）、`/news`（11/20 ipo-close）、`/research`（11/17）は動いていない。Opus 4.5 の下限日 11/24 を確定する告知もない（Master・industry）
  - https://platform.claude.com/docs/en/about-claude/model-deprecations

### OpenAI / Codex / ChatGPT

- [仕様] **GPT-6.2 の移行パラメーター** — 11/18 既報。新しいのはプロンプトの指針だけ。Astra は既定で簡潔に答えるので「簡潔に」の指示は外す。新しく組むなら推論の強さは `medium` から始める。最上位の `instructions` の固定指示を `input` 先頭の developer メッセージに移すとキャッシュの対象になる。The Decoder（11/21）が同じガイドのプロンプト指針を報じている（industry）
  - https://developers.openai.com/api/docs/guides/latest-model?model=gpt-6.2-astra
  - https://the-decoder.com/openai-shares-new-prompting-tips-for-gpt-6-2-astra-and-sol-to-fix-brief-answers-and-unnecessary-questions/
- [破壊的変更] **AI ゲートウェイとモデルルーターの事前審査** — OpenAI の改定 Usage Policies が 11/20 に発効し、第三者に OpenAI モデルへの直接アクセスを提供するサービスは、提供前に OpenAI の審査と承認が要るようになった（10/21 公表、これまで未掲載）。`openai.com` はオリジン403で条文は一次未読で、ポリシーページの「Effective: November 20, 2026」と二次報道で確認した（Master）
  - https://openai.com/policies/usage-policies/
  - https://www.eweek.com/news/openai-ai-gateway-approval-rules/
- [セキュリティ] **GPT-6.2 の推論抽出攻撃** — The Decoder（11/20）によると、OpenAI の社内の自動攻撃テストで、前のリクエストの推論を抜き出す攻撃の成功率は GPT-6 Astra の 54.0% から GPT-6.2 Astra の 0.2% に下がった。現在のリクエストの推論は 22.9% から 0.9% に下がり、組織的な抽出には週に数千〜数万アカウントを停止している（industry）
  - https://the-decoder.com/openai-makes-it-much-harder-for-attackers-to-extract-how-its-latest-ai-models-think/
- [版更新] **Codex `0.173.0-alpha.2`〜`alpha.4`** — OpenAI が Codex の pre-release を 11/20〜21 に刻んだ。安定版は `0.171.0`（11/20）のままである（Master）
  - https://github.com/openai/codex/releases
- [観測] **GPT-5.6 Sol の期間限定価格の終了日** — OpenAI の料金ページは 11/22 時点でも「until November 30, 2026」と書き、changelog の「少なくとも 11/21 まで」は直っていない（industry）
  - https://developers.openai.com/api/docs/pricing
- [据え置き] **OpenAI のその他の一次** — API changelog（11/19 GPT-Live-1.1）、deprecations（11/18 告知の EU データレジデンシー優先処理）、`learn.chatgpt.com` changelog（11/20）、community Announcements（11/20）、Deployment Safety Hub（11/17）、misalignment reports（First posted 11/18）は動いていない（Master・industry）

### GitHub Copilot / GitHub

- [版更新] **Copilot CLI `v1.0.115-3`〜`-5`** — GitHub が pre-release（11/20〜21）で、フォーム対応の ACP エディターに構造化された確認質問を出せるようにし、長時間のローカルセッションのディスク使用と再開時間を減らした。安定版は `v1.0.114` のままである（Master）
  - https://github.com/github/copilot-cli/releases
- [新機能] **セキュリティアドバイザリーの権限のカスタムロール** — GitHub が 11/20 に GA にし、組織のオーナーが、アドバイザリーの閲覧・作成と編集・非公開の脆弱性報告の受理・公開と CVE 申請を、必要なリポジトリだけ別の人に渡せるようになった。対象はカスタムリポジトリロールを使えるプランで、一時的な非公開フォークのマージには引き続き管理者かセキュリティマネージャーが要る（industry）
  - https://github.blog/changelog/2026-11-20-security-advisory-permissions-are-now-generally-available
- [据え置き] **GitHub Copilot Changelog** — `github.blog/changelog` の Copilot ラベルは 11/18 のコネクタ8件より上に新しい項目が無い（Master）

### Microsoft 365 Copilot

- [予定] **Copilot デスクトップアプリと Edge の同期（MC1562269・11/20）** — 利用者が、Windows と Mac の Copilot デスクトップアプリと Edge でパスワード・個人情報・設定・閲覧履歴を同期できるようになる（12月中旬〜12月末に GA で展開）。同期は利用者が自分でオプトインし、支払い情報は同期しない。止めるためのポリシー名は MC に書かれておらず、詳細は展開開始時に公開するとしている。前日のアプリ内ブラウズの既定オン（MC1560922）と合わせると、Copilot アプリがブラウザーと同じ機微なデータを持つ（Copilot）
  - https://mc.merill.net/message/MC1562269
- [予定] **Copilot ライセンスの無い利用者の検索画面（MC1562275・11/20）** — M365 のライセンスだけを持つ利用者は、11月下旬から Microsoft 365 Copilot アプリで新しい検索画面を既定で使うことになり、元の画面にはトグルで戻せる。Deferred release は12月下旬から2027年1月中旬で、組織が接続ソースを構成していれば他社のコンテンツも検索できる（Copilot）
  - https://mc.merill.net/message/MC1562275
- [予定] **Teams のチャネル単位の Copilot（MC1562277・11/20）** — 利用者が、チャネルの右上から Copilot を開き、チャネル全体の最近の投稿と返信について質問や要約ができるようになる。パブリックプレビューは12月上旬〜12月末で、GA の時期は別に告知する（Copilot）
  - https://mc.merill.net/message/MC1562277
- [予定] **Work IQ: Listen（Roadmap 570867）** — エージェントが、Work IQ がサポートするイベントを待ち受けて変化に応答できるようになる。11/20 に In development で起票され、プレビューは2026年11月、GA は2027年1月の予定である（Copilot）
  - https://www.microsoft.com/microsoft-365/roadmap?id=570867
- [新機能] **Copilot Notebooks の成果物の提案（Roadmap 566870）** — OneNote の Copilot Notebooks が、ノートブックの内容と M365 のナレッジから Word・Excel・PowerPoint の成果物を提案して作るようになった。状態が Launched になったのは 11/21 である（Copilot）
  - https://www.microsoft.com/microsoft-365/roadmap?id=566870
- [据え置き] **GPT-6.2 Sol / Astra の TC 告知** — TC 4574229（11/20）が提供開始を告知したが、提供面と Frontier の条件は 11/21 に掲載した MC1560916 と同じで、Cowork のモデル表（`75f8dadb`）にはまだ載っていない（Copilot）
  - https://techcommunity.microsoft.com/t5/microsoft-copilot-blog/available-today-openai-s-gpt-6-2-sol-and-gpt-6-2-astra-in-microsoft-copilot/ba-p/4574229

### Copilot Studio / Power Platform

- [予定] **Developer Plan と Dataverse for Teams の退役（MC1515303 / MC1515294・11/20 更新、再告知）** — Microsoft が2つの MC を更新したが、日程は既報と同じである。アンマネージドの開発者環境は 12/15 から削除が始まり（残り23日）、2027/1/15 から完全に削除される。Dataverse for Teams は 2027/9/15 から削除が始まる（Copilot）
  - https://mc.merill.net/message/MC1515303
  - https://mc.merill.net/message/MC1515294
- [据え置き] **Copilot Studio・Power Platform・ライセンスの一次** — Copilot Studio What's New（`1e58d09d`）、モデル表（`5d702e92` / `1e3f96ce`）、レート表、PPAC 容量管理、非推奨一覧、M365 Copilot Release Notes（`03f66d22`）、Purview・Cowork・Partner Center のページは前日のまま変わっていない。Roadmap は総項目数 2,401（前日 2,389）で、Copilot Studio タグは33件のままである（Copilot）
  - https://learn.microsoft.com/en-us/microsoft-copilot-studio/whats-new

### Google

- [新機能] **Workspace の AI 関連5本（11/20）** — Google が、Apps Script の Gemini サイドパネルと、自然言語の分類指示を組織全体に適用する Drive のデータ分類を GA にした（Master）
  - Apps Script の Gemini: 組織の利用者が、平易な言葉の依頼でスクリプトの作成・修正・不具合調査をできる
  - Drive のデータ分類: 管理者が自然言語の分類指示を一括で展開でき、自動分類の判断の見え方も加わった
  - Gemini アプリのスキル: 共有できるようになり、Drive・Gemini Notebook・Google フォトのファイルを含められる
  - Google Chat のアプリとエージェント: 開発者が説明と最大3件の推奨プロンプトを設定でき、DM を開いた利用者に表示される
  - Workspace Studio: フローの共同作業を制御する管理者設定が加わった
  - https://workspaceupdates.googleblog.com/
- [観測] **Gemini API changelog に届かない** — Gemini API changelog は転送先 `aistudio.google.com` に届かず、WebSearch でも 10/27 より新しい項目を確かめられない。Gemini アプリ（11/19）と `blog.google` AI RSS（11/19）は動いていない（Master）

### Cursor / Devin / xAI / その他エージェント

- [新機能] **Devin Bots と Access and Sharing** — Cognition が 11/19 に Devin Bots を出し、固有のアイデンティティ・記憶・権限を持つ常駐の Devin が作業を分けて並列セッションを走らせられるようにした。11/20 の Access and Sharing（段階展開・既定オフ）では、環境とセッション単位の共有設定、GitHub / GitLab の権限の不一致チェック、ユーザーグループでの権限管理が加わった（Master）
  - https://docs.devin.ai/release-notes/overview
- [新機能] **Orca `v1.4.267`〜`v1.4.269`** — Stably AI が、Bots を動かせるエージェントに Cursor・GitHub Copilot・Hermes・Kiro・Gemini CLI・Goose などを足した（11/20〜21）。各 bot にエージェント共通のスキルフォルダーが付き、`orca slack` に予約投稿（`--at`）が加わった（Master）
  - https://github.com/stablyai/orca/releases
- [廃止] **xAI `grok-build-0.1` の提供終了** — xAI が、`grok-build-0.1` が 11/19 に end of life を迎え API で配信されなくなったと release notes で告げた。5/15 以降は `grok-code-fast-1` へのリクエストもこのモデルへ回していた。後継の指定は無い（Master）
  - https://docs.x.ai/developers/release-notes
- [据え置き] **Cursor と TypeSafe AI** — Cursor の changelog（11/6）とフォーラム（10/12）、TypeSafe AI（`sitemap.xml` の9件）は動いていない（Master）

### MCP / オープンウェイト

- [新機能] **Thinking Machines の Inkling 2 Mini** — Thinking Machines が、ループ構造のオープンウェイトモデル Inkling 2 Mini を Apache 2.0 で公開した（11/20〜21・二次）。The Decoder によると総パラメーター 264億・アクティブ 54億の MoE で、文脈長は100万トークン、メモリ 32GB 以上の Mac で動き、DeepSWE v1.1 は 48.2% である。重みの所在は二次で割れている（改善メモ参照）（Master・industry）
  - https://the-decoder.com/new-open-model-inkling-2-mini-thinks-in-loops-to-solve-problems-with-fewer-words-and-still-runs-on-a-laptop/
  - https://www.testingcatalog.com/thinking-machines-releases-inkling-2-mini-looped-open-model/
- [据え置き] **MCP・Hugging Face・Obsidian** — MCP blog（11/11）は動いておらず、Hugging Face の登録8 org に新しいリポジトリは無い。Obsidian（11/12 の 1.15.1）も変わっていない（Master）

### 市場・企業

- [動向] **Nasdaq 100 がコロナ禍以来で最悪の週** — FT を引く The Decoder（11/21）によると、Nasdaq 100 は週間で 10.4% 下げ、11/20 は −5.6%、半導体指数は −10.7% だった。Anthropic 株は上場2日目に 9.1% 下げた。Nvidia の SEC 調査と下落率は報道で割れている（industry）
  - https://the-decoder.com/us-technology-stocks-suffer-their-worst-weekly-loss-since-the-pandemic-as-ai-doubts-pile-up/
- [動向] **Amazon と Decart の買収交渉** — FT（11/21）が、Amazon が Decart を $75億で買う合意に近づいていると報じた。両社とも発表しておらず、未成立である（industry）
  - https://fourweekmba.com/ai-amazon-nears-7b-decart-deal-1-75x-its-may-valuation/
- [据え置き] **Nvidia の買収協議** — Nvidia × Inception、Nvidia × Reflection AI の協議に続報はなく、Nvidia の後任 CEO も未定のままである（industry）

## 直近の注目予定

- **11/23**: Power Platform Monitor の1時間単位のアラートがパブリックプレビューに入る（MC1560951）
- **11/24 以降**: `claude-opus-4-5-20251101` の暫定退役日（確定日ではない・告知なし）
- **11月下旬**: Copilot ライセンスの無い利用者の検索画面が新しくなる（MC1562275）。Copilot Code のローカル Sandbox が既定でオンになる（MC1519871）
- **11/29**: OpenAI が Daybreak Blue のセッションデータの学習利用を始める（二次）
- **11/30**: `claude-sonnet-4-5-20250929` が Claude API から退役し、Opus 4.8 の fast mode が削除される。OpenAI の `/v1/prompts`・Evals・Agent Builder が停止する。Power Automate デザイナーの Copilot が退役する。GPT-5.6 Sol の期間限定価格が終わる（料金ページ記載）
- **12/1**: OpenAI `gpt-image-1-mini` / `gpt-image-1.5` / `chatgpt-image-latest` が停止する。Gemini 4 Argon・Carbon の単価が $4/$20 に倍増する。Copilot Studio のワークフローの Code ノードが GA になる
- **12/2**: GitHub が公開リポジトリの `pull_request_target` を既定でブロックする。Power Platform のプロンプトから Anthropic・Grok・旧 GPT 系が退役する（MC1536101）
- **12月上旬**: Teams のチャネル単位の Copilot がパブリックプレビューに入る（MC1562277）
- **12/8**: GitHub が活動の無いリポジトリの Dependabot アラートを停止する。Dataverse のエージェントユーザーが GA になる
- **12/9**: EU / EFTA で Claude モデルが既定で有効になる（MC1546438）
- **12/11**: OpenAI `gpt-5` 系 / `o3` / `o3-pro` が停止する
- **12/14**: Copilot から Claude Fable 5 / Haiku 4.5 / Gemini 3.8 Flash / Gemini 4 Argon / Grok 4.6 / Kimi K3 が廃止される。claude.ai/design の単体サイトが閉鎖する
- **12/15**: アンマネージドの開発者環境の削除が始まる（MC1515303）
- **12月中旬**: Copilot デスクトップアプリと Edge の同期が展開される（MC1562269）。Chat と Office のモデルの従量課金が GA になる（MC1557754）
- **12/18**: Copilot から MAI-Code-1.1-Flash が廃止される
- **12/31**: Copilot の Fable 5 系の ZDR 例外が終わる
- **2027-01-03**: Copilot デスクトップアプリのアプリ内ブラウズの既定オンに備える期限（MC1560922）
- **2027-01-14**: OpenAI `gpt-4o` / `gpt-4o-mini` / `gpt-4.1` / `gpt-4.1-mini` が停止する
- **2027-01-15**: アンマネージドの開発者環境が完全に削除される
- **2027-02-15**: Copilot Studio の Claude Opus 4.8・Opus 5・Sonnet 4.6・Sonnet 5 が退役する
- **2027-03-01**: GPT-6.2 Astra・Sol の Ultrafast が Standard の3倍から6倍になる

## 改善メモ

- 本サマリーはセーフティネット（ローカル `ai-news-digest-safety-net`）がバックフィルした。07:00 JST の本番ルーチンが 08:31 時点で当日分を出していなかった
- Master: B-091（OpenAI Usage Policies の発効日を追う）を新規起票。継続提案 8件（最多: B-088 Gemini API changelog の URL 差し替え、19回目）
- Copilot: 新規提案なし。継続提案 5件（最多: B-080 Cowork の Learn URL の移設、24回目）
- industry: 新規提案なし。継続提案 7件（最多: B-040・B-048、20回目）
- ソース間の違い: Claude Code 2.1.330 の `deniedMcpServers` の変更と `max_tokens` 自動再試行の復活は industry にだけあり、Master は Admin Console のサインインを主に書いた。Inkling 2 Mini は Master が「26B・HF の登録 org に無く一次未確認」、industry が「総 264億・アクティブ 54億、重みは Hugging Face にある」と書いており、規模の表し方と重みの所在が割れている
</content>
</invoke>
