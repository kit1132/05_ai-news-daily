# AI News Daily Summary — 2026-10-09

Anthropic は単体の Claude Design を 12/14 に閉じると告知し、Docs / Slides / Design を全プランで正式提供にした。Usage Policy の改定版（11/12 発効）も出した。Microsoft は Business Applications in Work IQ を既存環境でも11月から既定オンにすると明記し、Sales Development Agent の課金開始を 11/16 と告知した。Google は Claude も選べる業務用の Gemini agent を発表した。

## 今日のハイライト

### 1. [廃止+新機能] Anthropic が単体の Claude Design を 12/14 に閉じ、Docs / Slides / Design を全プランで正式提供にした — 単体版のチャットとコメントは移行されない

**要点**: Anthropic が claude.ai/design の単体サイトを 12/14 で閉じると告知した（10/8）。Design は会話内の機能に一本化され、単体版のチャット・コメント・公開リンクは閉鎖とともに失われる。「別 URL で使い続けられる」前提が期限付きに変わった。

**詳細**:

- 単体版の閉鎖: 12/14 まで claude.ai/design で動く。組織のデザインシステムは Artifacts ページの「Migrate team design systems」で一括移行できる。チャットとコメントは移行対象外で、単体版プロジェクトの公開リンクも止まる
- 正式提供: Docs / Slides / Design のベータ表記を外し、Free を含む全プランで使えるようにした。Artifacts の CMEK 対応、管理者による Artifact テンプレートの選択、組織外への共有（管理者が許可した場合）、PowerPoint / PDF 書き出しと Google Slides への直接出力、モバイル編集が入った。作成数は累計4,500万件超としている
- Claude Dashboards（有料プランでベータ）: BigQuery / Databricks / Snowflake / Salesforce などのコネクタに自然文で問い合わせ、データに合わせて更新されるダッシュボードを作る。数値ごとに裏のクエリと最終更新時刻を表示する
- Claude Motion（Team / Enterprise でベータ）: 文字・グラフ・図形・画像をコードでアニメーションにし、MP4 で書き出す。動画生成モデルは使わない

- https://claude.com/resources/articles/dashboards-and-motion

### 2. [破壊的変更] Business Applications in Work IQ が既存環境でも11月から既定オンになる — Dataverse のデータが、何もしなければ M365 Copilot Chat と MCP クライアントから使える

**要点**: 管理者が何もしなければ、Power Apps / Dynamics 365 のデータは M365 Copilot Chat・Cowork・MCP クライアントから使える状態になる。新規の本番環境は 9/30 から既定オンで、既存環境も2026年11月から同じになる。オプトインだった前提が、止めたい環境を管理者が自分でオフにする前提へ変わった。

**詳細**: Microsoft が `power-platform/admin/business-applications-work-iq/default-settings` を 10/8 に改訂した（`ms.date` 10/7）。同サブツリーは全ダイジェストで掲載歴が無く、今回の追加箇所は特定できていない。

- 例外: EEA / EU の環境（GA 時に有効化）、政府系クラウドの利用歴があるテナント、試用・サンドボックス・開発者環境
- 既定でオンになる3設定: M365 管理センターの Dataverse データ共有（テナント）、PPAC の Work IQ（環境）、Power Apps の「Enable Copilot in model-driven apps」（アプリ）
- 副作用: 検索インデックスのぶん Dataverse の容量を余分に使う。FedRAMP 環境ではデータが認可境界の外の M365 へ出て、米国外で処理されることがある
- 止め方: M365 管理センター > Copilot > Settings の「Business Applications data in Work IQ available to Copilot」（既定は All users）か、PPAC > 環境 > Settings > Product > Features の Work IQ をオフにする

- https://learn.microsoft.com/en-us/power-platform/admin/business-applications-work-iq/default-settings

### 3. [料金] Sales Development Agent が 11/16 から Copilot Credits の消費を始める — プレビュー中の無償利用が従量課金に変わる

**要点**: Microsoft が Copilot ブログの 10/8 記事で、Public Preview 中の Sales Development Agent が 2026-11-16 から Copilot Credits を消費すると告知した。検証目的で動かしているテナントでも、この日から費用が発生する。

**詳細**: Sales Development Agent は Teams から管理し、専用の Exchange アカウントからメールを送る。同じ記事の他の告知は次のとおり。

- Dynamics 365 の事前構築スキル30本: Cowork では GA、Autopilot はプライベートプレビュー、Code は Frontier 経由
- Dynamics 365 CRM in the flow of Teams: Public Preview に入り、Teams チャネルに会議前ブリーフ・ケース通知・取引先の更新が届く
- Service Agent in Microsoft 365: 一部の Frontier 顧客向けのプライベートプレビューで、CRM のケースを自律的に作成する

- https://www.microsoft.com/en-us/copilot/blog/2026/10/08/bringing-crm-into-the-flow-of-work-and-agents-into-business-process-for-sales-and-service-teams/

## カテゴリ別まとめ

### Claude / Anthropic

- **Claude Design 単体版の閉鎖と Dashboards / Motion**（ハイライト参照・1）
- [セキュリティ] **Claude Code 2.1.294** — Anthropic が Claude Code `2.1.294` を npm の `latest` に出し、指示文で書いた `prompt` / `agent` フックがブロック対象の操作を通してしまう不具合を直した（10/8）。Stop / SubagentStop の `prompt` フックの判定も改めた。npm は `{stable: 2.1.286, latest: 2.1.294, next: 2.1.295}` で、`stable` が 2.1.285 から進んだ。https://code.claude.com/docs/en/changelog
- [セキュリティ+新機能] **Claude Code 2.1.295** — Anthropic が `next` の `2.1.295` で、フックのガード迂回3件を直し、コマンド・HTTP フックに `onFailure: "block"` を追加した（10/8）。フックが起動しない・タイムアウトする・異常終了するときに操作を止められる。
  - 修正: 深い入れ子のツール入力が切り詰められたままフックに渡りガードが中身を見ずに通していた問題、mod 再読み込み中の呼び出しが他の mod のガードを迂回していた問題、改ざんされた設定キャッシュで個人プラグインが組織管理として扱われていた問題
  - 既定の変更: tool search で読む MCP ツール説明の上限を 2,048字から 16,384字に広げ、claude.ai のコネクタは MCP プロトコル 2026-07-28 を既定にした（`MCP_PROTOCOL_NEGOTIATION=legacy` で戻せる）
  - https://code.claude.com/docs/en/changelog
- [破壊的変更] **Managed Agents の `web_fetch` 制限** — Anthropic が Managed Agents の `web_fetch` で取得できる URL を、ユーザーのメッセージ・`web_search` の結果・取得済みページに出てきたものに限った（10/7）。それ以外は `url_not_in_prior_context` を返すため、URL を組み立てて取りに行くエージェントは止まる。取得させたい URL は `user.message` で送る。前日掲載の `allowed_hosts` 改定と同じ日付の項目で、industry が1日遅れで捕捉した。https://platform.claude.com/docs/en/release-notes/overview
- [仕様] **Usage Policy 改定（11/12 発効）** — Anthropic が2026年版の Usage Policy を公開した（10/8）。自律的に物理動作する機器への接続に、有資格の操作者が観察・停止できることと切断時に安全状態を保てることを求めるようにした。
  - 新設: 偽装・人工的な拡散を扱う「Do Not Engage in Deceptive Campaigns or Artificial Activity」節
  - 選挙節を「Do Not Undermine Democratic Processes」に改名し、個別化した投票・選挙運動ターゲティングの一律禁止を外した
  - 武器（誘導・制御ソフトウェア、自律移動体の武装）と監視・法執行（同意のない追跡、捜査対象の決定や推奨）の禁止を明記した
  - https://www.anthropic.com/news/2026-usage-policy-update
- [新機能] **Anthropic Cyber Mission と OSS Scanner** — Anthropic がオープンソース向けに無料の脆弱性スキャン OSS Scanner を出した（10/8）。登録プロジェクトに最上位モデルが定期スキャンをかけ、PoC・説明・修正案つきの報告を人手の確認なしで送る。制御系（OT）事業者向けの重要インフラ防御プログラム（CIDP）も始め、創設パートナーは Accenture / CrowdStrike / Palo Alto Networks など11社。https://www.anthropic.com/news/anthropic-cyber-mission
- [動向] **Genesis Mission に $150M** — Anthropic が米政府の Genesis Mission に3年で **$150M** を拠出すると発表した（10/8）。NASA・NIH・NSF など15超の機関の研究プロジェクトに Claude・Claude Code・API クレジットを提供する。https://www.anthropic.com/news/genesis-mission-commitment
- [セキュリティ] **利用上限処理の障害** — Anthropic の利用上限処理の不具合で、一部の組織が上限未到達でも一時停止され、Claude API・Claude.ai・Claude Code・Cowork のリクエストが拒否された（10/7 21:23 UTC 解決）。https://status.claude.com/incidents/vmys9qn874h4
- [観測] **Sonnet 5.5 のキャッシュ単価の食い違い解消** — Anthropic の料金ページのモデル別表で、Sonnet 5.5 のキャッシュ読み取りが $0.10 に直り、本文・リリースノートと一致した（前日は表だけ $0.20）。`claude-haiku-4-5-20251001` は Active のままで退役告知は出ていない。https://platform.claude.com/docs/en/about-claude/pricing

### OpenAI / Codex / ChatGPT

- [料金+新機能] **GPT-6.1 Sol の Ultrafast モード** — OpenAI が GPT-6.1 Sol の Ultrafast モードを API・Codex・ChatGPT Work に出した（10/8）。API は `service_tier: "ultrafast"` で、Sol Standard の最大8倍速い。単価は入力 $12・キャッシュ読み $0.60・出力 $60（100万トークンあたり・27.2万以下）で標準の6倍。Codex / ChatGPT Work は Pro 500・対象の従量制 Enterprise（管理者が有効化）・クレジット制 Edu が対象で、米国・EU のデータレジデンシーに対応する。https://developers.openai.com/changelog / https://community.openai.com/t/ultrafast-is-rolling-out-today-for-gpt-6-1-sol-in-the-api-codex-and-chatgpt-work/1404475
- [新機能] **Codex CLI 0.162.0** — OpenAI が Codex CLI の安定版 `0.162.0` を出した（10/8）。信頼済みローカルプロジェクトで管理された Git worktree を作成・一覧するツール、Command Center のタスクのピン留め、`/copy` による transcript のコピーが入った。Windows 向けの署名つき PowerShell インストーラーも含む。https://github.com/openai/codex/releases
- [新機能] **Free / Go への GPT-6 Luna 展開** — OpenAI が 10/8 に ChatGPT の Free / Go を GPT-6 Luna に切り替え、全プランの既定モデルが GPT-6 世代になった（Intelligent UI は前日掲載）。Web 検索が必要な質問で、GPT-6 Instant は GPT-5.6 Instant より平均44%早く回答を始めるとしている。https://community.openai.com/t/gpt-6-and-intelligent-ui-in-chatgpt/1404139
- [セキュリティ] **Wikimedia への大量自動リクエスト** — Wikimedia 財団が、OpenAI が運用するとみられる AI エージェントが公開 API に数百万件、Wikidata Query Service に数十万件の問い合わせを送ったと公表した（10/5）。5月の同サービスの部分停止に「寄与した可能性がある」とし、承認なしのウィキ編集も確認した。侵害は確認されておらず、OpenAI はコメントしていない（二次のみ）。https://www.helpnetsecurity.com/?p=386959

### GitHub Copilot / GitHub

- [新機能] **Claude Haiku 5.5 の Copilot GA** — GitHub が Copilot の Pro / Pro+ / Max / Business / Enterprise で Claude Haiku 5.5 を GA にした（10/7）。従量課金のプロバイダー定価で、VS Code・Copilot CLI・cloud agent・JetBrains などに順次出る。Business / Enterprise は既定のモデル有効化設定を切っていなければ自動で有効になる。https://github.blog/changelog/2026-10-07-claude-haiku-5-5-in-github-copilot
- [新機能] **ドラフト PR を上限に含める設定** — GitHub が、書き込み権限の無いユーザーの同時オープン PR 数の上限にドラフトも数えられるようにした（10/8）。6月の導入時はドラフトを数えず、ドラフトなら無制限に出せた。https://github.blog/changelog/2026-10-08-draft-pull-requests-count-toward-pull-request-limits
- [版更新] **Copilot CLI v1.0.94-5** — GitHub が Copilot CLI の pre-release を `v1.0.94-5`（10/8）まで進めた。`1.0.94-3` で Haiku 5.5 をモデル選択に足し、`1.0.94-4` で assisted permissions が表示されたシェルコードを権限判定に渡すようにした。https://github.com/github/copilot-cli/releases

### Microsoft 365 Copilot / Copilot Studio / Power Platform

- **Work IQ の既定オン**（ハイライト参照・2）
- **Sales Development Agent の課金開始**（ハイライト参照・3）
- [仕様] **スキルのマーケットプレイス共有** — Microsoft が `agents-experience/skills-manage` を改訂し（`ms.date` 10/8）、GitHub Copilot ハーネスのメーカーが自作スキルを指定ユーザー・グループに共有し、「Browse skills (preview)」から追加できると明記した。追加したスキルはスナップショットとして取り込まれ、元が更新されると通知が出る。読み込みに失敗したスキルは飛ばされ、エージェントの他の部分は読み込まれる。https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-experience/skills-manage
- [仕様] **GitHub Copilot ハーネスの tool search** — Microsoft が Copilot Studio Blog の 10/8 記事で、ツールが多いときハーネスは外部ツールの定義を全部は文脈に載せず必要なものだけ読み込むと説明した。呼ばれないツールも定義ぶんトークンを消費するとし、ツール・ワークフロー・スキル・接続エージェントの役割分担を設計指針に挙げている。https://techcommunity.microsoft.com/t5/copilot-studio-blog/are-bigger-agents-better-how-to-design-agents-that-scale/ba-p/4559073
- [観測] **評価結果ページの改訂** — Microsoft が `analytics-agent-evaluation-results` を改訂し（`ms.date` 10/7）、Review パネルの評価警告が公開を妨げないことを明記した。Review パネル自体は前日掲載済みである。https://learn.microsoft.com/en-us/microsoft-copilot-studio/analytics-agent-evaluation-results
- [据え置き] **Release Notes / Roadmap / Power Platform の定点** — M365 Copilot Release Notes の先頭は October 06, 2026 のまま、Release Communications RSS は総項目数 1,900 のままである。Release Wave の製品別5ページは 9/3 のまま、Copilot Studio の最新ビルドも 2026.6.3 のまま（100日）である

### Google / Cursor / 市場・その他

- [予定+動向] **Google Cloud の Gemini agent** — Google Cloud が Gemini at Work 2026（10/8）で、作業ごとに Gemini と Anthropic の Claude から適したモデルを選ぶ業務用エージェント「Gemini agent」を発表した。提供開始日と価格は書かれていない。
  - 接続先: Workspace に加え Microsoft 365・Slack・Jira・Salesforce・ServiceNow・BigQuery・Snowflake と任意の MCP サーバー
  - 統制: エージェントごとに Workspace アカウントを持たせて監査ログに残し、実行は Agent Sandbox、通信は Agent Gateway でポリシーを当てる。Cloud Billing Console でプロジェクトごとに AI 支出の上限を置ける
  - 導入事例（Google 公表）: Commerzbank は文書レビューを20時間から1時間に短縮し、SOMPO は従業員3.4万人で1万超のカスタムエージェントを動かしている
  - https://cloud.google.com/blog/products/ai-machine-learning/welcome-to-gemini-at-work-2026
- [据え置き] **Gemini API・Gemini アプリ** — Gemini API changelog の最上位は 10/6 の画像生成モデル GA のままで、Gemini アプリ無料枠の Flash-Lite 限定（10/9 発効の報道）は一次で確認できていない
- [据え置き] **Cursor・xAI・MCP・HF・Apple** — Cursor changelog は 10/6 の Remote control、フォーラム Announcements は 9/21 の Grok 4.7 が最上位のままで、登録8 org の Hugging Face 一覧と MCP ブログにも新規は無い
- [据え置き] **市場データ** — IDC Japan・MM総研・NRC・Similarweb はいずれも新規公表が無く、Similarweb の9月分トラッカーも未検知のままである

## 直近の注目予定

- **10/9**: Gemini アプリの無料ユーザーが Flash-Lite のみになる（報道）
- **10/13**: Gemini アプリで skills の展開開始 ／ Partner Digital Airlift（新しい Copilot）
- **10/14**: GPT-5.5 が ChatGPT / Codex から退役 ／ Anthropic の pre-IPO investor day（報道）
- **10/15 以降**: `claude-haiku-4-5-20251001` の暫定退役日（告知はまだ無い）
- **10月**: Copilot Chat の UBB モデル選択（571400） ／ デスクトップフローのスケジュールトリガー GA（573278） ／ スキルカタログ GA（571880） ／ 自己学習 GA（570432）
- **10/19**: GitHub Copilot が5モデルを廃止
- **10/22**: Copilot Business / Enterprise の機能既定有効化が発効
- **10/27〜29**: PPCC 2026（ラスベガス）
- **10/30**: ChatGPT Pro 200 の Work / Codex 利用枠が変更（二次）
- **10/31**: MCP サーバー認定の旧申請経路が終了
- **11/1**: Codex の28日間「改善かリセット」の終了（二次）
- **11月**: Business Applications in Work IQ が既存環境で既定オン
- **11/12**: Anthropic Usage Policy 改定版が発効 ／ OpenAI → Cursor のモデル供給停止予定（一次未読）
- **11/16**: Sales Development Agent が Copilot Credits の消費を開始
- **11/17**: Gems が Gemini アプリの設定パネルへ移動
- **11/17〜20**: Microsoft Ignite
- **11/30**: `claude-sonnet-4-5-20250929` が Claude API から退役
- **12/1**: Copilot Business の従量課金が既定オン
- **12/14**: claude.ai/design の単体サイトが閉鎖（チャット・コメント・公開リンクが失われる）
- **2027-01-06**: OpenAI `tts-1` / `tts-1-hd` / `gpt-4o-mini-tts` 2版が停止
- **2027-03-01 以降**: Gems 廃止（Business / Enterprise）
- **2027-04-01**: OpenAI `gpt-5.1` / `gpt-5.3-codex` / `gpt-5.4-nano` が停止

## 改善メモ

- 新規提案: 3ソースとも無し
- 継続提案: Master は B-035 npm dist-tags（54回目）・B-079 HF の ID 集合差分（8回目）・B-082 最上位エントリ基準の差分判定（15回目）を再確認 ／ Copilot は B-074（docset 全件突合）・B-076（差分特定不可・Work IQ 既定設定ページ）・B-037（100日）を更新 ／ industry は2件を更新（最多 B-004・101回目）。B-031 に Managed Agents `web_fetch` 制限（10/7）の取りこぼしを追記
- 障害の変化: 3ソースとも無し
- ソース間の差分・矛盾:
  - Claude Code は Master が 2.1.294 のみ [セキュリティ]、industry が 2.1.294 / 2.1.295 を1項目で [セキュリティ+新機能] にしていた。1項目に2リリースを同居させない補則に従い、2.1.294 を [セキュリティ]、2.1.295 を [セキュリティ+新機能] に分けた
  - GPT-6.1 Sol Ultrafast は Master が [新機能]、industry が [料金+新機能] で割れた。単価が標準の6倍という新しいティアの公開で、優先順（料金 ＞ 新機能）に従い industry と同じ [料金+新機能] とした
  - 利用上限処理の障害は Master が [動向] だったが、可用性障害の事後報告として [セキュリティ] とした
  - GPT-6 と Intelligent UI は Master がハイライト3にしたが、日次では 10/7 に掲載済みのため、Free / Go への展開だけをカテゴリに置いた
  - Ultrafast の説明は Master が「最大8倍の速さ」、industry が「出力トークン間の待ち時間を縮める」で、どちらも一次（changelog）を出典にしている。矛盾ではなく表現の違いとして併記した
