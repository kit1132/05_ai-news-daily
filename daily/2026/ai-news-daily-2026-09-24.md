# AI News Daily Summary — 2026-09-24

前日に出たモデル2系統を各社が自社製品へ流し込んだ日である。GitHub は GPT-6 Sol / Luna を Copilot に入れ、Microsoft は Opus 5.5 と GPT-6 Sol を M365 Copilot・Copilot Studio へ展開し始めた。並行して、調達と接続の前提を変える告知が3件出た。Anthropic は Claude Marketplace でパートナー製品を自社コミット額で買えるようにし、CSP の Copilot プロモーションは 9/30 で終わる。GitHub は SSH の `ssh-rsa` 退役日程を確定させた。

## 今日のハイライト

### 1. [料金] CSP の M365 E5 / E7 / Copilot プロモーションが 9/30 で終わる — 10/1 から割引は成長マージンに一本化される

**要点**: Microsoft Partner Center が、CSP 経由の M365 E5・E7・Copilot のプロモーションを **9/30** で終え、**10/1** から成長マージンへ切り替えると告知した。プロモーション価格で組んだ CSP 経由の Copilot 見積もりは、残り6日で前提が失効する。

**詳細**: 9/23 付の Partner Center 告知による。成長マージンの一般提供日は 10/1 で変更なく、それに先立ち 9/23 00:00 UTC からディストリビューターと直接請求パートナーに2機能が先行開放された。

- 資格確認 API: 顧客が成長マージンの対象かを API で確認できる
- Pricing ワークスペース: 対象 SKU と最低シート数をダウンロードできる

成長マージンの制度自体は7月に予告済みだが、**プロモーション終了日が一次で明示されたのは今回がはじめて**である。同じ 10/1 には CSP ソフトウェア価格改定（月次請求への5%上乗せ）も発効する。Partner Center の告知一覧はこれで17件になった。

- https://learn.microsoft.com/en-us/partner-center/announcements/2026-september

### 2. [廃止+破壊的変更] GitHub が SSH の `ssh-rsa` と旧鍵交換を退役させる — 10/14 から段階的に接続できなくなる

**要点**: GitHub が SHA-1 署名の `ssh-rsa` と `diffie-hellman-group-exchange-sha256` の退役日程を確定させた。10/14 から 3072 ビット未満の RSA 鍵は新規登録できず、古い Git クライアントや CI ランナーの SSH 接続はブラウンアウト日（11/4・12/9）に実際に失敗し始める。

**詳細**: 9/22 付の changelog による。前日のサマリーでは件名だけを記録していた。

- 10/14: 新規 RSA 鍵は 3072 ビット以上が必須になり、耐量子の鍵交換 `mlkem768x25519-sha256` が有効になる
- 11/4: `ssh-rsa` と `diffie-hellman-group-exchange-sha256` の1回目のブラウンアウト
- 12/9: 2回目のブラウンアウト
- 完全削除: 原文は「January 13, 2026」と書いている。10月以降の日程の後に置かれており時系列上は2027年の誤記とみられるが、一次の表記のまま示す

影響を受けるのは SSH と認証なし Git プロトコルの利用者だけで、HTTPS は対象外である。既存の RSA 鍵は、クライアントが `rsa-sha2-256` / `rsa-sha2-512` に対応していれば再生成しなくてよい。GitHub は Ed25519 鍵への切り替えを推奨している。

- https://github.blog/changelog/2026-09-22-security-improvements-for-ssh

### 3. [新機能] Anthropic が Claude Marketplace を開いた — サードパーティの Claude 搭載製品を Anthropic のコミット額で買える

**要点**: Anthropic が 9/23 に Claude Marketplace を公開し、Cursor・Harvey・Snowflake などの Claude 搭載製品を、Anthropic と結んだコミット額の一部で購入できるようにした。「サードパーティの AI 製品は別契約・別予算」という調達の前提が、Anthropic 契約の枠内へ寄せられる形に変わる。

**詳細**: 置き場所は `claude.com/platform/marketplace` で、3区分で構成される。

- コネクタ / プラグイン: Atlassian・Google・Microsoft・Notion・Salesforce など **2,000件超**
- エージェント / 製品: CrowdStrike・Cursor・Harvey・Legora・Lovable・Snowflake などの Claude 搭載ソフトウェア
- サービスパートナー: Claude Partner Network 経由のコンサル・SI（Accenture・BCG・Deloitte）

同日に、CodeRabbit・Power Digital・ThoughtSpot が Snowflake / Vercel と組んで Marketplace 上で拡販する事例記事も出た。⚠️ 管理者の購入制御・対象リージョン・コミット額に充当できる上限割合は本文に書かれていない。

- https://claude.com/blog/claude-marketplace
- https://claude.com/blog/how-coderabbit-power-digital-and-thoughtspot-scale-with-snowflake-and-vercel-on-claude-marketplace

## カテゴリ別まとめ

### Claude / Anthropic

- [セキュリティ+新機能] **Claude Code `2.1.281`** — Anthropic が、削除対象をコマンド置換だけで決める再帰 `rm`（`rm -rf "$(pwd)"` 等）を auto mode と `--dangerously-skip-permissions` でも確認するよう修正した（9/23）。Bash の allow ルールがあっても確認し、`CLAUDE_CODE_DISABLE_SUBSTITUTION_RM_PROMPT=1` で従来動作に戻せる。
  - 権限の修正: NUL バイトを含む権限ルールがワイルドカード展開されていた問題と、macOS の `/.vol`・`/.nofollow`・`/.resolve` 配下を承認前に読んでいた問題を直した
  - Claude apps gateway: Bedrock 上流に `assume_role`（STS で別アカウントの IAM ロールを引き受ける）と `guardrail`（全リクエストに Bedrock ガードレールを適用）が加わり、`blockedMarketplaces` でプラグインマーケットプレイスをドメイン単位で拒否できるようになった
  - `"attribution": false` でコミット／PR の署名行を一括で消せる。⚠️ この値を書いた settings ファイルは旧バージョンの CLI では丸ごと読み飛ばされるため、共有ファイルではオブジェクト形式を使う
  - 配布: npm の `next` タグで 9/23 17:01 UTC に公開され、`latest` は `2.1.280`、`stable` は `2.1.267` で15日連続据え置きになっている
  - https://code.claude.com/docs/en/changelog
- [動向] **酵素系の発見** — Anthropic が、Claude のエージェント約950体を21時間並列で動かし、CRISPR に似た繰り返し配列を持つ新しい酵素系（ART）を見つけたと発表した（9/23）。ファージ由来の逆転写酵素20万件超から候補を20件へ絞り、使ったトークンは **2億1,000万**である。https://www.anthropic.com/news/claude-discovers-novel-enzyme-system
- [動向] **コード近代化の準備手順** — Anthropic が Claude ブログで、AI 主導のコード近代化案件に入る前の準備手順を公開した（9/23）。https://claude.com/blog/how-to-prepare-for-ai-driven-code-modernization-projects
- [据え置き] **API release notes・廃止ページ** — Claude Platform の release notes に 9/22 の Opus 5.5 より新しい記載は無い。廃止ページでは `claude-sonnet-4-5-20250929` が Active のままで廃止通知が出ておらず、60日前通知の約束から 9/29 に止まることはない。https://platform.claude.com/docs/en/about-claude/model-deprecations
- [観測] **上場報道** — WSJ を引いた二次報道が、Anthropic は第3四半期決算を示して10月中旬から投資家向け販売を始め、11月の米中間選挙前に上場を終える日程だと報じた。2028年売上の社内見込みは $1,900億〜$2,000億とされる。⚠️ 一次未確認で、Anthropic の一次告知は 6/1 の S-1 機密提出に留まる。https://www.pymnts.com/news/investment-tracker/ipo/2026/anthropic-targets-november-ipo-revenue-surges/

### GitHub Copilot

- [新機能] **Copilot アプリのローカルサンドボックス** — GitHub が 9/23 に public preview で公開した。既定はオフで、プロジェクト単位または `/sandbox on` で有効にする。
  - ファイルシステム: 読み書き許可リスト・読み取り専用フォルダー・拒否ディレクトリ
  - ネットワーク: 外向きインターネットとローカルネットワークの可否
  - 資格情報: Git の HTTPS 資格情報と GitHub CLI 認証の受け渡し
  - OS がポリシーを強制できない場合はエラーで止まり、Enterprise の管理設定はプロジェクト設定より厳しく強制できる。クラウドサンドボックスとリモートホストには適用されない
  - https://github.blog/changelog/2026-09-23-local-sandboxing-in-the-github-copilot-app
- [新機能] **Copilot アプリの OpenTelemetry 出力** — Enterprise 管理者が `managed-settings.json` の `telemetry` で出力先を指定すると、モデルへのリクエストとツール利用を既存の監視基盤へ送れるようになった（9/22）。**プロンプトと応答の本文は既定で除外**される。https://github.blog/changelog/2026-09-22-opentelemetry-in-the-github-copilot-app
- [新機能] **GPT-6 Sol / Luna** — GitHub が 9/22 に両モデルを Copilot に入れた。Sol は Pro+ / Max / Business / Enterprise、Luna は **Pro も対象**で、管理者がグローバル既定を切っていない限り自動で有効になる。https://github.blog/changelog/2026-09-22-openais-gpt-6-sol-and-gpt-6-luna-now-available
- [新機能] **Copilot for JetBrains 1.18.0** — GitHub が、低リスクのツール呼び出しを自動承認する「AI 支援ツール承認」を public preview にした（9/22）。過去メッセージの再編集・組織共有のスキル・Codex エージェントの plan モード・組み込み GitHub MCP Server のオン・オフが GA になり、JetBrains IDE のサポートは 2026.1 以降へ移る。https://github.blog/changelog/2026-09-22-new-features-and-improvements-in-copilot-for-jetbrains
- [新機能] **Copilot CLI `v1.0.88`** — 安定版が上がり（9/22）、OSC 777 通知や実行中ターンからの `/fork` を含む。pre-release `v1.0.89-0` で `claude-opus-5.5` に対応した。https://github.com/github/copilot-cli/releases
- [廃止+破壊的変更] **CodeQL の全プラットフォーム版バンドル** — GitHub が 2027年3月中旬の削除を告知した（9/22）。`codeql-bundle.tar.gz` / `.tar.zst` を取得している CI は OS・アーキテクチャ別バンドルへ切り替える必要がある。https://github.blog/changelog/2026-09-22-deprecation-notice-all-platform-codeql-bundle
- [新機能] **C++ コード理解** — GitHub がコードベース全体のインデックスで C++ のコードインテリジェンスを高速化した（9/22）。https://github.blog/changelog/2026-09-22-faster-c-code-intelligence-with-whole-codebase-indexing
- [セキュリティ] **Plugin4Shell** — 開示7日目でも Microsoft は GitHub Copilot の修正を出しておらず、CVE も未採番のままである。二次媒体は暫定策として GitHub ホストのマーケットプレイスに限定し、サードパーティ製プラグインの自動更新を止めることを挙げる。一次の `www.air.security` はゲートウェイ拒否が続く。https://thehackernews.com/2026/09/plugin4shell-lets-repository-owners.html

### Microsoft 365 Copilot / Copilot Studio

- [新機能] **Opus 5.5 と GPT-6 Sol の展開** — Microsoft Copilot ブログが、両モデルを Word / Excel / PowerPoint / Chat / Cowork / Copilot Studio の6面へ展開し始めたと告知した（9/22 21:34Z）。ただし Learn のモデル表（`cowork-models`・Copilot Studio の `authoring-select-agent-model`）と Release Notes には両モデルの記載がまだ無い。Anthropic モデルの M365 管理センター許可と PPAC の External Models 設定という既存の2段統制は変わっていない。https://techcommunity.microsoft.com/blog/microsoft-copilot-blog/more-models-one-copilot/4559035
- [予定] **フェデレーテッドコネクタの書き込み対応（570964）** — MCP 型のフェデレーテッド Copilot コネクタで、ユーザーが作成・更新・削除のツールを Copilot Chat から使えるようになる（GA October CY2026・In development）。Copilot はユーザー本人の権限で動き、書き込みは毎回ユーザーの明示確認を経る。管理者は M365 管理センターで読み取りツールと書き込み／削除ツールを個別に確認し、コネクタを無効化できる。https://www.microsoft.com/microsoft-365/roadmap?id=570964
- [仕様] **Cowork アプリケーションカード** — Microsoft が Responsible AI のアプリケーションカード（`ms.date` 9/22）で、Cowork の運用上の上限を1ページにまとめた。
  - 入力上限: プロンプト 25万字・添付1件 200 MB
  - カスタムスキル: 最大50個（OneDrive の `Documents/Cowork/skills/{name}/SKILL.md`）
  - できないこと: ローカルファイルへのアクセス・OneDrive / SharePoint の削除・権利保護ファイルの読み取り
  - 「Don't ask again」はその会話内だけに効く。⚠️ 搭載モデルの節は「Claude Sonnet 4.6 and Claude Opus 4.7」と書いており、現行ピッカーとも本日の展開告知とも食い違う
- [予定] **Copilot Studio の9月 GA 期日** — Roadmap の Copilot Studio 起票22件は全件 `In development` のままで、GA 期日 September CY2026 の **14件**は残り6日になった。What's New は July 2026 節が最新で、GitHub Copilot ハーネスの GA（8/3）は52日反映されていない。
- [据え置き] **Release Notes** — M365 Copilot Release Notes は `updated_at` が 9/23 に動いたが、先頭は August 25 バッチのままで、9月分は1回も追加されていない（前バッチから30日）。https://learn.microsoft.com/en-us/microsoft-365/copilot/release-notes
- [予定] **Copilot Dev Camp Summit** — Microsoft が M365 Copilot 拡張開発者向けの四半期オンラインイベントを 9/30 8:00（PT、日本時間 10/1 0:00）に初開催する。宣言型エージェント・Copilot UX コンポーネント・Microsoft IQ の各セッションに製品チームとの討議枠が付く。https://devblogs.microsoft.com/microsoft365dev/join-the-copilot-dev-camp-summit-fall-edition-on-september-30/
- [据え置き] **Power Platform** — Power Platform ブログ3本・Release Wave・Released Versions（Copilot Studio 2026.6.3）はいずれも据え置きで、新規は無い。

### OpenAI / Codex

- [新機能] **Codex CLI `0.156.1`** — OpenAI が 9/23 に出し、モデルピッカーから GPT-6 Sol / Luna を選べるようにした。レート制限時の切り替え提案も GPT-6 Luna を勧める。`0.156.0`（9/22）はフルスクリーン TUI・音声会話の既定オン・`/usage` の利用分析を入れていた。https://github.com/openai/codex/releases/tag/rust-v0.156.1
- [据え置き] **料金ページ** — OpenAI の一次料金ページは据え置きで、長文コンテキスト単価が揃って取れた。GPT-6 Astra $20/$75・GPT-5.6 Sol $8/$30・Terra $4/$18・Luna $0.40/$1.80 で、地域データレジデンシーは対象モデルで10%上乗せされる。GPT-6 Astra の追随値下げは無い。https://developers.openai.com/api/docs/pricing
- [廃止] **廃止ページ** — OpenAI の最新告知は 9/11 の `gpt-5.4-cyber` のままで追加は無い。本日 9/24 の Videos API と `sora-2` 系5件の停止は予定どおりである。https://developers.openai.com/api/docs/deprecations

### Google

- [新機能] **Gemini 3.8 Flash TTS / Flash-Lite TTS** — Google が Gemini API で両モデルを GA にした（9/22）。ボイスデザイン・声の複製・150種超の音声を含む。https://ai.google.dev/gemini-api/docs/changelog
- [破壊的変更] **Meet「Take notes for me」の新設定** — Google が、3人以上の会議だけ自動メモを取る設定を 9/29 に有効にする。Business Standard / Plus は既定オン、Enterprise 系は既定オフで、9/29 以降は利用者が管理者の既定を上書きできる。https://workspaceupdates.googleblog.com/2026/09/new-google-meet-take-notes-for-me-settings-for-admins-and-end-users-take-effect-September-29th.html
- [新機能] **study notebooks** — Workspace アカウントでも Gemini の study notebooks が使えるようになった（Rapid Release は 9/17 から段階展開・EEA は未提供）。管理者が Gemini アプリと Gemini Notebook の両方を有効にした組織部門が対象である。https://workspaceupdates.googleblog.com/2026/09/study-notebooks-in-gemini-are-now-available-for-Google-Workspace-accounts.html

### Cursor / xAI / オープンウェイト

- [据え置き] **Cursor** — Cursor は Opus 5.5 と GPT-6 Sol / Luna の提供開始をどちらも告知していない（Copilot は公開当日に両方を告知した）。changelog とフォーラム Announcements も新規は無い。Cursor は一方で Claude Marketplace の掲載先に入っている。
- [観測] **xAI** — Musk が 9/23 に新機能を予告する投稿をしただけで、一次は未読のままである。
- [据え置き] **オープンウェイト** — 登録8 org で 9/22〜9/23 に作成されたリポジトリは無い。

### 市場データ

- [動向] **ビデオリサーチの生成AI利用率** — ビデオリサーチ「ひと研究所」が、12〜69歳 12,026人の直近1カ月の生成AI利用率が 2025年の 38% から2026年は **60%**（速報値）になったと公表した。調査期間は 2026年4〜6月で、利用目的は「調べ物・情報収集」が最多である。モバイル社会研究所（15〜69歳で 51%）とは対象と定義が異なるため横に並べない。⚠️ 一次（`www.videor.co.jp`）はゲートウェイ拒否で、二次スニペットの一致で構成している。https://www.kknews.co.jp/news/20260915o01
- [据え置き] **定点データ** — Similarweb・IDC・MM総研・NRC はいずれも新規公表が無い。

## 直近の注目予定

- **9/24（本日）**: OpenAI の Videos API と `sora-2` 系5件が停止
- **9/25**: Microsoft Partner Center の Check Inventory API が退役
- **9/28**: Copilot のチャット3面統合 ／ code review の既定 effort が Balanced へ ／ チャットのデータ保持変更 ／ OpenAI の `gpt-3.5-turbo-instruct` / `babbage-002` / `davinci-002` / `gpt-3.5-turbo-1106` が停止 ／ Anthropic × Adaptyv コンペ開始
- **9/29**: OpenAI DevDay ／ Google Meet「Take notes for me」の新設定が有効化
- **9/29 以降**: `claude-sonnet-4-5-20250929` の暫定退役日（廃止通知は未発出）
- **9/30**: CSP の M365 E5 / E7 / Copilot プロモーション終了 ／ Gemini の `gemini-omni-flash-preview` が停止 ／ Copilot Studio の Roadmap 14件が GA 期日 ／ Copilot Dev Camp Summit ／ Clinical Applications スペシャライゼーションの受付開始 ／ OpenAI の現行 OneGov 契約が失効
- **10/1**: CSP 成長マージンの一般提供 ／ Microsoft CSP ソフトウェア価格改定が発効 ／ OpenAI の `gpt-5.4-cyber` が API から削除 ／ Copilot Business・Enterprise の既存顧客が前払い必須に ／ ChatGPT for Word の Word アクセスが既定オンへ
- **10/2**: GitHub Copilot が4モデルを廃止 ／ Gemini の `gemini-2.5-flash-image` が停止
- **10/5**: Gemini の `antigravity-preview-05-2026` が停止 ／ GPT-Rosalind の課金開始
- **10/13**: Office / Project / Visio LTSC 2021 のサポート終了
- **10/14**: GitHub SSH の新規 RSA 鍵が 3072 ビット以上必須に ／ OpenAI の `gpt-5.5` が ChatGPT / Codex から退役（API は対象外）
- **10/19**: GitHub Copilot が5モデルを廃止（Gemini 3.7 Flash / GPT-5.5 / GPT-5.4 / GPT-5.4 mini / Grok 4.5）
- **10/23**: OpenAI のレガシースナップショット12件が退役
- **10 月中**: 570964 フェデレーテッドコネクタの書き込み対応 GA
- **10/27〜29**: PPCC 2026
- **10/31**: OpenAI の既存 evals が読み取り専用に
- **11/2**: GitHub Actions の `pull_request_target` 既定無効化が公開リポジトリで強制開始 ／ M365 Copilot Business の従量課金が既定オン
- **11/4**: GitHub SSH `ssh-rsa` の1回目のブラウンアウト
- **11/12**: OpenAI が Cursor へのモデル供給を停止する予定日（一次未読）
- **11/15**: Microsoft Release Planner 退役
- **11/17〜20**: Microsoft Ignite
- **11/21**: GPT-5.6 Sol の期間限定価格の下限
- **11/30**: OpenAI の Reusable prompts・Evals・Agent Builder が停止
- **12/1**: OpenAI の GPT Image 系が停止
- **12/9**: GitHub SSH `ssh-rsa` の2回目のブラウンアウト
- **12/11**: OpenAI の GPT-5 / o3 系スナップショットが停止
- **12/31**: Gemini 3.8 Flash と 3.7 Flash の導入価格が終了 ／ GitHub Copilot の Fable 5.1 / Fable 5 に対する ZDR 暫定免除が終了
- **数週間内**: Claude Sonnet 5.5 と Claude Haiku 5.5 のリリース（日付未提示）
- **2027年3月中旬**: CodeQL 全プラットフォーム版バンドルの削除

## 改善メモ

- 新規提案: 3ソースとも無し。継続提案は Master 11件を再確認（最多 B-024・50回目）／ industry 6件を再確認（最多 B-004・87回目）／ Copilot は変化なし
- 障害の変化: industry で `edu.watch.impress.co.jp`・`www.kknews.co.jp`・`markezine.jp`・`www.videor.co.jp` のゲートウェイ拒否を新規記録した。Copilot の `mc.merill.net` は48日連続で拒否が続く
- ソース間の差分・矛盾:
  - Claude Code `2.1.281` は、Master（04:10 JST 頃の実行）が「changelog 未記載」、industry（05:10 JST 頃の実行）が changelog 本文から内容を取っている。取得時刻の差で、本サマリーは industry の内容を採った
  - 10/19 の GitHub Copilot 廃止モデル数は industry が本日も「6モデル」のままで、Master の 9/18 告知本文に基づく **5モデル**を引き続き採る
  - Copilot Dev Camp Summit は industry が「一次未確認・二次のみ」、Copilot が M365 Developer Blog の一次を取得済みである。本サマリーは一次 URL を採った
  - industry は本日の抽出で OpenAI の 9/24・9/28 停止と Gemini の 10/2 停止が廃止ページの列挙から落ちたと記録している（撤回告知は無く、期限は保持）
