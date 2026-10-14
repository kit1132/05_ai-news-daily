# AI News Daily Summary — 2026-10-15

Copilot Studio の GPT-4.1 / GPT-5 系が 11/12 に退役し、App Builder と vibe.powerapps.com も 11/30 に退役すると Message Center で告知された。Claude Code は `2.1.299` / `2.1.300` で MCP 許可ルールを完全一致に改めた。業界では Character.ai が Chapter 11 を申請した。

## 今日のハイライト

### 1. [廃止] Copilot Studio の GPT-4.1 / GPT-5 系が 11/12 に退役する — 既定モデルが特定版から「最新版に追従する別名」に変わる

**要点**: MC1506318 によると、標準ハーネスの GPT-4.1・GPT-4.1 Mini・GPT-5 Chat / Auto / Reasoning は **11/12** に「GPT Chat Latest」へ自動移行する。既定モデルは、決まった版から、同じメジャー版の中で更新され続ける別名に変わる。

**詳細**: 通知は 10/13 公開・10/14 更新で、タグは Retirement。Learn の `authoring-select-agent-model` も 10/14 に改訂され、全13リージョンで Default が GPT-5.5 Chat から GPT Chat Latest に入れ替わった。

- 移行先: 標準ハーネスはすべて GPT Chat Latest に移る。GitHub Copilot ハーネスでは GPT-5 Chat が GPT 5.6 Terra に、GPT 5.6 Sol / Luna が GPT 6 Sol / Luna に移る
- 例外: 米国外でリージョンをまたぐデータ移動を制限している環境では、GPT-4.1 と GPT-5 は退役しない
- GPT Chat Latest の扱い: 同じメジャー版の中のスナップショット更新は自動で反映され、メジャー版が上がるときは **30日以上前**に告知される
- 影響の洗い出し: PPAC の Manage > Copilot Studio でエージェントをハーネスとモデルごとに確認できる。ただしモデル欄はプレビューで、公開済みの構成しか反映されない
- 続報: Claude Opus / Sonnet の旧版の退役日は別途告知される。標準ハーネスの実験枠は Grok 4.1 Fast から Grok 4.2（米国の早期アクセス環境のみ）に替わった

- https://mc.merill.net/message/MC1506318
- https://learn.microsoft.com/en-us/microsoft-copilot-studio/authoring-select-agent-model

### 2. [廃止] App Builder エージェントと vibe.powerapps.com が 11/30 に退役する — 10月中旬から新しいアプリは作れない

**要点**: MC1505609 によると、M365 Copilot の App Builder エージェントと vibe.powerapps.com は **11/30** に退役し、10月中旬から新規作成ができなくなる。自然言語でアプリを作る入口は Copilot Cowork と Copilot Studio の2つにまとめられる。

**詳細**: 10/12 公開で、Act by は 11/30 である。移行しなかったアプリは、11/30 以降は退役した画面から開けなくなる。

- 日程: 10月中旬に製品内の移行機能が提供され、同時に新規作成が止まる。11/30 に退役する
- 移行先: Cowork のアプリは 9/8 から Frontier で提供されている。Copilot Studio のアプリは10月上旬からパブリックプレビューで展開中である（MC1469329）
- 管理者の対応: 利用している作成者を特定し、残したいアプリは 11/30 までに移行を終える

- https://mc.merill.net/message/MC1505609

### 3. [破壊的変更+新機能] Anthropic が Claude Code `2.1.299` / `2.1.300` で MCP の許可ルールを完全一致にした — 前方一致に頼った設定は更新しただけで効かなくなる

**要点**: Anthropic が 10/14 に2版を出し、`mcp__a` のような許可ルールが `a__b` という別サーバーに一致しなくなった。`claude remote-control` の `--sandbox` は削除されてエラー終了になる。既存の settings.json やスクリプトは、更新後に許可が外れたり起動に失敗したりしうる。

**詳細**: npm の公開は `2.1.299` が 10/14 00:23 UTC、`2.1.300` が 10/14 14:27 UTC。dist-tags は `{stable: 2.1.292, latest: 2.1.300}`。

- MCP 許可ルール（2.1.299）: サーバー名全体で一致させる。配下をまとめて許可するには `mcp__<サーバー名>__*` と書く。エージェント定義の `tools:` も同じ扱いになる
- フック: `UserPromptSubmit` がスキル展開の前に走るようになった（2.1.299）。PreToolUse・PermissionRequest の `updatedInput` は未知のキーが落とされ、ツールが拒む入力は呼び出しの拒否になる（2.1.300）
- `remote-control`（2.1.300）: `--sandbox` / `--no-sandbox` を渡すとエラー終了する。設定の `sandbox.enabled` で指定する
- MCP プロトコル: クラウドセッションと Remote Control の MCP コネクタは既定で `2026-07-28` を交渉する（`MCP_PROTOCOL_NEGOTIATION=legacy` で旧方式）
- 新機能: 20万トークン以上の会話を約54分放置すると、1時間のプロンプトキャッシュが切れる前に自動で圧縮する（`"idleCompaction": false` で無効）。Claude in Slack が Slack Connect チャンネルに対応した（既定は無効）

- https://code.claude.com/docs/en/changelog

## カテゴリ別まとめ

### Claude / Anthropic

- **Claude Code `2.1.299` / `2.1.300`**（ハイライト参照・3）
- [新機能] **Claude Platform の OpenTelemetry トレース出力（ベータ）** — Anthropic が 10/14 に、Messages API と Claude Managed Agents のリクエストを OpenTelemetry のトレースとして外部の監視基盤へ送れるようにした。これまで OTel で追えたのは Claude Code と Cowork だけだった。送信先は Claude Console で追加し、Claude SDK（Python / TypeScript / C# / Go / Java / PHP / Ruby）はスパンを自動で出す。料金の記載は無い。事例として Ramp がトークン使用量を10〜20%減らしたとしている。https://platform.claude.com/docs/en/release-notes/api
- [動向] **シンガポール拠点と政府との覚書** — Anthropic が 10/14 にアジア太平洋で5拠点目となるシンガポール事務所を開き、デジタル開発情報省（MDDI）と AI の安全性・評価、導入研究、官民の導入支援で覚書を結んだ。GovTech Singapore の技術職1,500人超が Claude Code を導入し、Grab の営業支援 BriX は四半期あたり約40,000時間を削減したという（Anthropic の公表値）。https://www.anthropic.com/news/singapore-office-opening
- [据え置き] **Claude Haiku 4.5 は退役下限日を迎えても Active** — Anthropic の廃止ページは `claude-haiku-4-5-20251001` を「Not sooner than October 15, 2026」の Active のまま表示し、退役告知は出ていない。60日以上前の通知の約束から、最短でも12月中旬までは使える。https://platform.claude.com/docs/en/about-claude/model-deprecations

### OpenAI / Codex / ChatGPT

- [廃止] **GPT-5.5 の ChatGPT サインイン版 Codex からの退役（発効）** — OpenAI が 10/14 正午 PDT（19:00 UTC）に、ChatGPT サインインで使う Codex から GPT-5.5 を退役させた。API と API キー認証の Codex は対象外である。公式 changelog は、使えるなら GPT-6.1 Sol（`gpt-6.1-sol`）へ移るよう案内している。https://learn.chatgpt.com/docs/changelog
  - 見直す箇所: ワークスペースの既定、保存済みのモデル設定、管理設定、カスタムエージェント、スケジュールタスク、`gpt-5.5` を指定しているスクリプト
- [据え置き] **Codex CLI と OpenAI の定点** — OpenAI は Codex CLI の安定版を `0.162.1`（10/9）のまま据え置き、pre-release を `0.163.0-alpha.11`（10/14）まで進めた。API changelog は 10/8、Announcements は 10/9、廃止ページは 10/14 の GPT-4 系削除告知が最上位のままである。https://developers.openai.com/api/docs/deprecations

### GitHub Copilot / GitHub

- [新機能] **GitHub Actions のワークフロー lockfile（パブリックプレビュー）** — GitHub が 10/14 に、アクションと推移的依存・再利用ワークフローのコミットを `.github/workflows/actions.lock` に固定できるようにした。タグやブランチが後から動いても記録したコミットで実行される。生成と鮮度検査は `gh actions-lock` で行い、管理者は「Require lockfile」ポリシーで必須化できる。既定の挙動は変わらない。https://github.blog/changelog/2026-10-14-github-actions-workflow-lockfiles-in-public-preview
- [版更新] **Copilot CLI pre-release** — GitHub は Copilot CLI の安定版を `v1.0.97` のまま据え置き、pre-release `v1.0.98-1`（10/14）で Gemini 4 Argon に対応した。`v1.0.98-2` は `/ask` の回答を Ctrl+E で展開、Ctrl+Y で全文コピーできるようにした。https://github.com/github/copilot-cli/releases

### Microsoft 365 Copilot / Entra / Purview

- [破壊的変更] **Entra のエージェントのブループリント作成が一般ユーザーに既定オン（11/4）** — MC1506733 によると、11/4 から Entra のロールを持たない一般ユーザーもエージェントのブループリントを作れるようになる。止めたいテナントは、展開前に Entra ID > Users > User settings の「Users can create agent blueprints」をオフにする必要がある。https://mc.merill.net/message/MC1506733
  - 展開: 11月上旬に始まり11月下旬に完了する。トグルは今変更でき、展開の開始時に有効になる
  - 関連（MC1506728）: 11/4 からブループリントに `AgentIdentity.CreateAsManager` が自動付与されなくなり、エージェントが ID を作るには管理者の同意が要る
- [セキュリティ] **間接プロンプトインジェクション対策（CVE-2026-55145）** — Microsoft が 10/13 の Tech Community 記事で、M365 Copilot は外部メールなどの信頼できないコンテンツを隔離経路で変換してから主モデルに渡すと説明した。この保護は管理者が Outlook の外部送信者タグ付け（`Set-ExternalInOutlook`）を有効にしないと働かない。https://techcommunity.microsoft.com/t5/microsoft-copilot-blog/building-trust-aware-controls-for-ai-differentiated-handling-of/ba-p/4562160
- [廃止] **`Search-UnifiedAuditLog` の退役** — MC1505599 によると、Purview 監査の検索は Graph の AuditLogQuery API が10月に GA し、`Search-UnifiedAuditLog` コマンドレットは 2027/10/15 に退役する。
- [料金] **Agent 365 の可観測性データ** — MC1506727 によると、11月下旬から管理者は Agent 365 ライセンスがなくても、Microsoft 製や Microsoft プラットフォーム上のエージェントの利用状況を M365 管理センターで見られるようになる。サードパーティ製エージェントのライセンスは変わらない。https://mc.merill.net/message/MC1506727
- [新機能] **Cowork の Business apps プラグイン（preview）** — 管理者が M365 管理センターの Agents > Tools > Plugins でプラグインを入れると、利用者は Cowork から Dataverse・Dynamics 365・Power Apps のデータを自然言語で検索・更新できるようになった。アクセスは既存のロールと権限の範囲に限られる。https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-work-iq
- [予定] **Work IQ ほか Roadmap 10/13 バッチ** — Microsoft が Roadmap に17件を起票し、うち Work IQ が5件だった。
  - Retrieve（570673）・REST endpoint tools（570868）・A2A / MCP の長時間タスク（570851）・elicitation（570852）: Preview は October、GA は November CY2026
  - Microsoft IQ（570870）: 組織の知識を横断して使う統合レイヤーで、Preview は November CY2026、GA は January CY2027
  - Agent Builder のスケジュール実行（MC1302906）: 11月までに全世界で提供され、既定で有効になる
  - Outlook の共有・代理メールボックスでの Copilot Chat（573698）: GA は November CY2026
- [観測] **Copilot DLP の管理単位対応で一次が食い違っている** — MC1486284（10/9）は Copilot 向け DLP への管理単位の対応を「進めない」と告げた一方、10/13 の Roadmap 575287 は同じ委任管理を Preview October / GA November CY2026 で新たに起票した。
- [据え置き] **Release Notes / ブログ各種** — M365 Copilot Release Notes の先頭は October 06, 2026 のままで、Copilot ブログ・Agent 365 Blog にも新規記事は出ていない。

### Copilot Studio / Power Platform

- **Copilot Studio の GPT-4.1 / GPT-5 系退役**（ハイライト参照・1）
- **App Builder / vibe.powerapps.com の退役**（ハイライト参照・2）
- [新機能] **GitHub Copilot ハーネスの接続エージェントが4種類に** — 作成者は Copilot Studio 製に加えて、Foundry・A2A・M365 Agents SDK のエージェントも接続先に追加できるようになった（Learn 10/14 改訂）。Foundry は現行ポータル製のみが対象で、Activity プロトコル（既定オフ）の有効化が要る。外部エージェントのデータの流れや品質の確認は利用者の責任と明記された。https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-experience/authoring-add-other-agents
- [廃止+予定] **モデル駆動型アプリの AI 設定の集約** — Microsoft が Roadmap 574104 で、モデル駆動型アプリの AI 設定を Maker Studio の「Copilot and AI」タブと PPAC の Copilot Hub の2か所に集約し、PPAC の Environment > Settings にある従来のスイッチを退役させると告知した。GA は October CY2026（版 2610.3）である。
- [新機能] **Power Pages プラグインの多言語化** — 開発者が、GitHub Copilot CLI と Claude Code 向け Power Pages プラグインの `/add-localization` から、React / Vue / Angular の SPA サイトに43以上の言語の UI を追加できるようになった（10/14）。https://www.microsoft.com/en-us/power-platform/blog/power-pages/go-multilingual-with-the-power-pages-plugin/
- [新機能] **Copilot Agent Kit October 2026** — Power CAT がキットの10月版を公開し、標準ハーネスのエージェントも Agent Map に表示されるようになった。Agent Review Tool は GCC / GCC High / DoD のサポート対象から外れた。https://github.com/microsoft/Power-CAT-Copilot-Studio-Kit/releases
- [据え置き] **What's New / Released Versions / 非推奨一覧** — Copilot Studio What's New は `ms.date` 10/5 のまま、Released Versions は 2026.6.3 のまま、非推奨一覧も 10/5 から変わっていない。

### Cursor / Google / その他エージェント

- [新機能] **Orca `v1.4.225`** — Stably AI が Orca のデスクトップ版 `v1.4.225` を出し、Kiro エージェントの状態表示と履歴でのセッション一覧に対応した（10/14）。Claude のアカウント別フォルダー対応も不具合を直して入れ直した。https://github.com/stablyai/orca/releases
- [据え置き] **Cursor・Google・MCP・TypeSafe の定点** — Cursor の changelog は 10/13、フォーラムは 10/12 が最上位のままである。Gemini API changelog は 10/13 の Gemini 4 Argon GA が最上位で、`blog.modelcontextprotocol.io` も 8/22 のまま。TypeSafe AI は `jev-1.13.0`・入力 $0.042 / 100万トークンから変わっていない。

### 市場・企業

- [動向] **Character.ai が Chapter 11 を申請** — 親会社 Character Technologies が 10/13 にデラウェア州の破産裁判所へ申請し、資産売却を進めると発表した。Disney が $20M で知的財産の非独占・永続ライセンスを得るストーキングホース入札者になり、競売は11〜12月の見込み。負債・資産はいずれも $50M〜$100M で、買い手が運営を続けなければサービスは終了する。https://www.cnbc.com/2026/10/13/character-ai-chapter-11-disney-bid.html
- [動向] **Arena が評価額 $3.1B で $200M を調達** — TechCrunch によると、LLM 比較サイト Arena（旧 LMArena）が 10/8 に Lightspeed と Khosla Ventures 主導のシリーズB を発表した。評価額は1月の $1.7B から約1.8倍で、年換算売上は1月 $30M → 6月 $100M だった。https://techcrunch.com/2026/10/08/popular-ai-leaderboard-arena-nearly-doubles-valuation-to-3-1b-valuation-in-10-months/
- [動向] **Manus が $500M 超を調達** — CNBC によると、Meta との買収解消後の Manus が Boyu Capital と IDG Capital の主導で $500M 超を調達した（10/8）。評価額は非開示である。https://www.cnbc.com/2026/10/08/manus-fund-raise-meta-muse-tencent.html
- [動向] **Similarweb 9月分で Gemini のシェアが4カ月連続低下** — OfficeChai が伝えた Similarweb の9月データで、生成AI サイトの訪問シェアは Gemini 25.0%（8月 25.6%）・Claude 9.6%（同 9.3%）だった。Web 訪問のみで、Similarweb の一次投稿は未確認である。https://officechai.com/ai/geminis-traffic-share-falls-for-fourth-straight-month-as-chatgpt-regains-ground-similarweb-data/
- [据え置き] **買収協議・国内市場データ** — Amazon × Decart と Nvidia × Reflection AI の買収協議に 10/10〜11 以降の続報は無く、IDC Japan・MM総研・NRC・Business Insider Japan（10月版）も新規公表が無い。

## 直近の注目予定

- **10月中旬**: App Builder / vibe.powerapps.com で新規作成が停止し、移行機能が提供される（MC1505609）
- **10月**: Work IQ の Retrieve / REST endpoint tools / 長時間タスク / elicitation の Preview ／ モデル駆動型アプリの AI 設定集約 GA（574104） ／ Copilot メモリの業務データ対応の展開完了（MC1492154・10月下旬）
- **10/15 以降**: `claude-haiku-4-5-20251001` の暫定退役日（告知はまだ無い）
- **10/19**: GitHub Copilot が5モデルを廃止（`gpt-5.5`・Gemini 3.7 Flash を含む）
- **10/22**: Copilot Business / Enterprise の機能既定有効化が発効 ／ Gemini API の Veo 3.1 プレビュー3種と `gemini-omni-flash-preview` が停止（最短日）
- **10/23**: Gemini API の `deep-research-pro-preview-12-2025` が停止 ／ OpenAI のレガシー GPT スナップショットが停止
- **10/27〜29**: PPCC 2026（ラスベガス）
- **10/30**: ChatGPT Pro 200 の Work / Codex 利用枠が変更（二次）
- **10/31**: MCP サーバー認定の旧申請経路が終了
- **11/1**: Codex の28日間「改善かリセット」の終了（二次）
- **11/4**: Entra で一般ユーザーのブループリント作成が既定オン ／ `AgentIdentity.CreateAsManager` の自動付与が停止
- **11/12**: Copilot Studio の GPT-4.1 / GPT-5 系が退役し GPT Chat Latest へ自動移行 ／ Anthropic Usage Policy 改定版が発効 ／ OpenAI → Cursor のモデル供給停止予定（一次未読）
- **11/16**: Sales Development Agent が Copilot Credits の消費を開始
- **11/17**: Gems が Gemini アプリの設定パネルへ移動
- **11/17〜20**: Microsoft Ignite
- **11/24**: `claude-opus-4-5-20251101` の退役下限日（告知なし）
- **11月下旬**: Agent 365 の可観測性データがライセンス不要に（MC1506727）
- **11/30**: App Builder エージェントと vibe.powerapps.com が退役 ／ `claude-sonnet-4-5-20250929` が Claude API から退役 ／ OpenAI の Evals・`v1/prompts`・Agent Builder が停止 ／ Gemini 4 Argon の導入価格が終了
- **12/1**: Gemini 4 Argon の単価が $4/$20 に倍増 ／ Copilot Business の従量課金が既定オン
- **12/14**: claude.ai/design の単体サイトが閉鎖
- **2027-01-06**: OpenAI `tts-1` / `tts-1-hd` / `gpt-4o-mini-tts` 2版が停止
- **2027-01-14**: OpenAI の GPT-4o・GPT-4o mini・GPT-4.1・GPT-4.1 mini が API から削除
- **2027-03-01 以降**: Gems 廃止（Business / Enterprise）
- **2027-04-01**: OpenAI `gpt-5.1` / `gpt-5.3-codex` / `gpt-5.4-nano` が停止
- **2027-10-15**: Purview の `Search-UnifiedAuditLog` コマンドレットが退役

## 改善メモ

- 新規提案: 3ソースとも無し
- 継続提案: Master は B-082 最上位エントリ基準の差分判定（21回目） ／ Copilot は B-074（docset 全件突合・1,492ページ）・B-070・B-037（106日）を更新 ／ industry は3件を更新（最多 B-004・107回目）し、B-043 に Haiku 4.5 下限日当日の確認、B-031 に Claude Code 2版同日リリースの捕捉を記録
- 障害の変化: Copilot で mc.merill.net（8/8 から68日のゲートウェイ拒否）と Qiita / Zenn / Power Platform Weekly が復旧し、未掲載の Message Center 通知がまとめて見つかった（本日のハイライト1・2はここから）。Master は 10-14 登録の `www.onorca.dev` / `typesafe.ai` / `docs.typesafe.ai` にクラウドから到達できた。industry は変化なし
- ソース間の差分・矛盾:
  - GPT-5.5 の Codex 退役を、Master は発効済み（[廃止]）、industry は「一次が未来形のまま」として [予定] で載せた。本サマリーは 19:00 UTC 発効済みの Master を採り [廃止] にした。移行先は Master が参照した changelog の `gpt-6.1-sol` を書いた（前日の本サマリーが記録した models ページの `gpt-6-sol` / `gpt-6-luna` とは異なる）
  - 10/30 の ChatGPT Pro 200 の枠変更は、Master が「半減」、industry が「Plus 比10倍」で二次どうしの割れが続いている。予定欄は「変更（二次）」のままにした
  - Copilot Studio のモデル表では実験枠が Grok 4.2 に替わった一方、Important 注記は Grok-4.1 Fast を名指ししたままである（Copilot 側の記録どおり）
  - Claude Code の2版は Master と industry がともにハイライトにした。本サマリーは選定基準1（退役2件）を先に採り、3件目に置いた
