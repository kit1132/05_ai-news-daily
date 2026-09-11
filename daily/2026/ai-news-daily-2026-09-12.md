# AI News Daily Summary — 2026-09-12

エージェントを動かす単位と、それを統制する場所が同時に動いた日である。Cursor は計画専任の coordinator が数千の subagent を従える Projects を全ユーザーへ開放し、OpenAI は Codex のハーネスそのものを Agents API として外に出した。Microsoft 側では Copilot Cowork のアクセス制御とネットワーク要件の一次ページが初めて把握でき、支出ポリシーがアクセス付与そのものだったことが判明している。Anthropic は閉鎖型とオープンウェイトを横断した危険能力測定を公開し、OpenAI は拘束力ある連邦 AI 安全規制を求める側に回った。

## 今日のハイライト

### 1. Cowork のアクセスを決めているのは支出ポリシーだけだった — 上限を絞って使わせない運用は成立しない

**要点**: 管理者が Cowork のアクセスを制御できるのは、Cowork を選択したスペンディングポリシーの適用範囲だけだと一次が明記した。上限1クレジットの全社ポリシーでも全員にアクセスが開くため、上限で実質的に止める設計が前提から崩れる。

**詳細**: `cowork-access`「Determine access controls for Copilot Cowork」が本日の巡回ではじめて把握できた（`ms.date` 2026-08-21・ページ表記の Last updated は 2026-09-08。全 digest で掲載歴ゼロ）。判定は5段で規定される。

- スペンディングポリシーの適用範囲: これがアクセス付与そのものにあたる。M365 管理センターの Copilot > Cost Management > Configuration でユーザーを直接または セキュリティグループ経由で含み、かつ Select agents and services で Cowork を選んだポリシーが1つでもあればアクセスがある
- ディスカバリー設定: 可視性だけを制御し、ポリシーに含まれるユーザーはディスカバリーが無効でもアクセスできる
- 複数ポリシーの重複: より制限的なポリシーが優先されることはなく、優先順位が決めるのは適用される上限だけである
- テナントのモデル設定: 表示モデルを制御するだけで、Anthropic ファミリーを無効化してもアクセスは残る
- クレジット上限への到達: 消費と上限の評価が非同期のため、上限到達後もタスクを開始できることがある

掲載例が要点を示す。パイロットに 5,000クレジット、All users に1クレジットの2ポリシーを置くとテナント全員が Cowork を使える。パイロット限定にするなら全社ポリシーから Cowork を外すか、パイロット以外をどのポリシーにも含めない。あわせて `cowork-admin-governance`（`ms.date` 2026-09-10）が、Frontier / Preview 期のエージェントベースのアクセス制御を**非推奨**と明記した。

- https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-access
- https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-admin-governance

### 2. Cursor が Projects をベータで全ユーザーに開放した — エージェント利用の単位がセッションからプロジェクトへ移る

**要点**: Cursor が、計画と委譲だけを担う coordinator が数千の subagent に実装を流す Projects を全ユーザーへ展開した。「1セッション1タスク」を前提にした使い方と工数見積もりが引き直しになる。

**詳細**: coordinator 自身はコードを書かず、計画を立てて実装エージェントへ委譲し、完成した作業を利用者へ返す。subagent は coordinator が作成・管理し、必要に応じて並列実行される。クラウド実行なのでラップトップを閉じても継続し、全エージェント間でファイルが同期され「学習情報」が蓄積されることで coordinator の効率が上がるとされる。Slack チャネルの監視・スケジュール実行・PR 追跡を subscription として登録でき、プロンプトなしの定期実行ができる。対象は機能追加・マイグレーション・フルアプリ開発のような、数ヶ月単位でコンテキストを保つ必要がある作業。⚠️ **対象プランと価格の記載がページに無く**、「本日より全ユーザーにロールアウト中」とベータ表記のみである。⚠️ 前日 09-11 は「changelog は 9/2 が最上位のまま」と記録しており、本項は1日遅れの検出にあたる。

- https://cursor.com/changelog

### 3. OpenAI が Agents API をパブリックベータで公開した — Codex のハーネスが自社アプリから呼べる部品になった

**要点**: OpenAI が Codex の管理ハーネスを Agents API として開放し、セッション管理・コンテキスト圧縮・復旧を自社側で持つようにした。エージェント基盤を自前で組む前提が変わる。

**詳細**: オーケストレーション・長時間セッション・コンテキスト管理を OpenAI 側が処理し、開発者はエージェント固有の部分に集中する構成になる。hosted sandbox ではエージェントがコード実行・ファイル操作・アーティファクト生成を行い、ファイルの供給とパッケージ・スキル・プラグインの追加は利用者が、プロビジョニングと管理は OpenAI が担う。自前のサンドボックスを使う場合は Blaxel AI・Cloudflare Dev・Daytona・DigitalOcean・E2B・Modal・Oracle Cloud・Runloop AI・Vercel と統合できる。料金はトークンとツール利用のみで追加料金はなく、hosted sandbox は standard container rates で課金される。⚠️ **ベータの制限と既存の Responses API との使い分けは告知に書かれていない**。⚠️ 前日 09-11 は同じ 9/10 の changelog から GPT-Live 1 だけを記録しており、本項とプロジェクト API キーの有効期限設定の2件が落ちていた。

- https://community.openai.com/t/introducing-the-agents-api-and-hosted-sandboxes/1396481
- https://developers.openai.com/api/docs/changelog

## カテゴリ別まとめ

### Anthropic / Claude

- **Claude Code `2.1.268`**: Anthropic が 9/10 公開分の内容を本日確定させた。前日は npm への publish だけが取れており changelog 未掲載だった
  - WebFetch が応答を無限に待つ問題を修正し、300秒のデッドラインを設けた（`CLAUDE_CODE_WEBFETCH_DEADLINE_MS` で上書き可）
  - Anthropic 互換エンドポイント（`ANTHROPIC_BASE_URL`）の HTTP 400 と、シンボリックリンクディレクトリで権限ルールが効かない問題を直した
  - 追加: Claude apps gateway の `pricing:` 設定／`gatewayInternalNetworks` managed 設定／`claude self-hosted-runner --remove-session-state`／プラグイン管理コマンド5種への `--json`
  - ⚠️ プラグインのエラーが git URL 内のパスワードやトークンを表示していた問題も、この版で解消している
  - https://code.claude.com/docs/en/changelog
- **`2.1.269` の扱いはソース間で食い違う**: 01 は 9/11 18:12 UTC の publish を確認しつつ changelog 未掲載で内容未確定とし、03 は `claude plugin eval`（採点付き・再現可能な eval スイート実行と JSON / HTML レポート）と `/output-style [name]` による出力スタイルの一覧・切り替えを同版の内容として記録した。本サマリーは両論併記とし、改善メモに記録する
  - ⚠️ npm の `dist-tags` は `{stable: 2.1.236, latest: 2.1.268, next: 2.1.269}` で、stable と latest の差は**32版**へ拡大した（前日31版）
- **危険能力測定の論文**: Anthropic が 9/10 に `/research` へ公開した測定で、閉鎖型（Mythos Preview / Mythos 5 / Opus 5 / Sonnet 5）とオープンウェイト（Kimi K3 / GLM 5.2）を横断して情報ターゲティングと通常兵器の能力を測った
  - 位置特定: 写真から Mythos Preview が中央値 **37km**（人間の上位層は151km）。テキストからは全ユーザーの8%が1km 以内で特定できた
  - ドローン: Opus 5 が静止目標で命中率80%・移動目標で47%。ペイロード投下は Opus 5 のみが風下環境で28%成功した
  - 政策的含意として、閉鎖型での検出・遮断分類器、オープンウェイト安全性研究の緊急性、計算資源の保護、既存法制度の更新を挙げる
  - ⚠️ この記事は `/news` の一覧には出ない（01 が B-068 として起票）
  - https://www.anthropic.com/research
- **Smart reports**: Claude Enterprise の管理者が、チームの Claude 利用を分析したレポートを受け取れるようになった（9/10・ベータ）。進んだ仕事・費用・セッションが詰まった箇所・共有スキルとして切り出す価値のある反復パターンを報告する。前日のセッションはこの項目を落としていた
- **脅威インテリジェンスレポート**（既報・本日一次確定）: 03 が 9/11 公開分を `www.anthropic.com` から一次取得した。同ホストは 2026-04-02 以降の障害が復旧したもので、163日ぶりの本文到達にあたる。ShinyHunters 系列（GTG-50014）が Android アプリ180万本を資格情報探索目的でダウンロードし、サプライチェーン侵害1件が下流約200社へ波及した事例を含む
  - https://www.anthropic.com/threat-intelligence-report-september-2026
- **据え置きの確認**: モデル退役ページは Active 11件のままで新規告知がなく、Platform API release notes も 9/10 の Managed Agents 権限ポリシー `auto` が最上位のままである。`claude.com/blog` の 9/10 は2本（T. Rowe Price の展開事例と小規模事業者1,000社の調査）だった
- ⚠️ **未追跡の残件**: 8月 Risk Report は**27日連続**で一次未読である。`www.anthropic.com` が復旧しても本日の `/research` 一覧に現れず、WebSearch でも一次 URL を特定できていない

### OpenAI / ChatGPT / Codex

- **Agents API とホステッドサンドボックス**: （ハイライト参照）
- **プロジェクト API キーの有効期限**: 管理者が、組織またはプロジェクトのレベルで最大キー有効期間を強制できるようになった（9/10）
- **ChatGPT for Financial Services**: OpenAI が GPT-6 Astra 上で動く ChatGPT Work の専用体験を投入した（9/10）。Morgan Stanley と Evercore が設計に関与している
  - 対象は投資銀行業務とエクイティリサーチ寄りで、企業調査・バリュエーション・LBO モデリング・買い手スクリーニング・決算分析・ピッチブック作成を挙げる
  - 内蔵データは Daloopa・PitchBook・LSEG News・Crunchbase。提供対象は適格な金融機関で、⚠️ **価格は二次にも出ていない**
- **Codex CLI**: 安定版 `python-v0.154.0` が 9/10 19:51 UTC に出た。推論努力に `max` と `ultra` を追加し、ターン操作の `ExternalMessage`、resume / fork の `include_turns`、ターンごとの `service_tier` に対応した。⚠️ `HookMetadata` がハンドラを `.root` プロパティで包む形に変わる移行を伴う
  - pre-release は 9/11 に `rust-v0.155.0-alpha.3` 系が6版刻まれた。⚠️ rust 側の安定版は `rust-v0.154.0`（9/9）のままで、本日の `python-v0.154.0` は同一リポジトリの別パッケージである
- **一次料金ページ**: 03 が `gpt-live-1` の行を一次で確認し、音声セッション **$0.05／分**の秒課金を確定させた。主要モデルの単価は19日連続で据え置きで、GPT-5.6 Sol の期間限定価格が「少なくとも 2026年11月21日まで」の記載も不変である。⚠️ `gpt-5.4-cyber` は**9日連続**で単価欄が空のままで、同節の `gpt-5.6-cyber` / `gpt-5.5-cyber` には $12.50／$75 が入っている
  - https://developers.openai.com/api/docs/pricing
- **廃止一覧**: 新規告知は15日連続で出ておらず、最新は 2026-08-26 の転写系4件（停止 2027-02-26）のままである。Agents API と GPT-Live 1 の登場に伴う退役告知はどちらも無い
- ⚠️ **`learn.chatgpt.com` はゲートウェイ拒否が継続**する。`site:` 付き WebSearch で返るのは 8/31〜9/4 の GPT-6 Astra 関連までで、**9/5 以降の ChatGPT アプリ側と Codex アプリ / プラグインの更新は本日も確認できていない**

### Microsoft / GitHub Copilot

- **Cowork のアクセス制御**: （ハイライト参照）
- **Cowork のネットワーク要件**: 管理者が `*.gateway.prod.island.powerapps.com:443` を許可リストへ入れる必要があると一次が公開した（`cowork-network-endpoints`・`ms.date` 2026-09-04。全 digest で掲載歴ゼロ）。⚠️ ページ自身が「Power Apps インフラの一部で、Power Apps を使っていない組織では既存の許可リストに無いかもしれない」と書いている
  - SSL/TLS 検査: 当該ホストでは非対応で、復号・再暗号化を挟むと長時間の SSE 接続が切れタスクが停止する
  - 長時間接続: `/v1/subscribe` と `/v1/mru/subscribe` はタイムアウト無しまたは最低30分が必要で、⚠️ 絶対寿命タイムアウトを課すプロキシは通信中でも切断する
  - 条件付きアクセス: 全サービス要求のトークン対象は単一アプリ `6ab48b67-cd74-4ad4-81af-5932984589be`（Weave / M365 Host App）で、ここをブロックしていないことを確認する
  - IP ベースが必要な場合は Azure のサービスタグ `PowerPlatformInfra` を参照する（週次更新・新レンジは利用開始の1週間以上前に掲載）
  - https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-network-endpoints
- **GitHub Copilot の週次リリース（9/7 分）**: 利用者が Jira issue を共有キャンバスへ取り込むと、Copilot app が調査・実装・プルリクエスト準備まで引き継ぐようになった（9/10 公開）
  - Copilot CLI: Project HydraFusion が実験的機能として入り、ローカル・クラウド・複合モデル間でタスクごとに自動セマンティックルーティングする
  - VS Code 1.137: エージェントタスクの時間単位・日単位・週単位の自動実行がパブリックプレビューに入り、音声モードが実験的機能になった
  - JetBrains: エンタープライズ管理者が、ファイルシステム・ネットワーク・プロキシのサンドボックス動作をポリシーで集中管理できる（パブリックプレビュー）
  - ⚠️ 記事は対象プラン（Business / Enterprise）を明示していない
  - https://github.blog/changelog/
- **GitHub changelog の 9/10 は6件だった**: 前日に3件と記録した残り3件を本日捕捉した。AI Scan for pull request の REST API がパブリックプレビューに入り、組織単位とリポジトリ単位で有効・無効を読み書きできる。⚠️ 組織側で無効にした状態はリポジトリ設定で上書きできない。対象は github.com の GitHub Advanced Security 契約者で、Enterprise Server は対象外。リポジトリの PR ページ刷新もパブリックプレビューに入った
- **Microsoft 365 Roadmap**: 起票2件が 9/10 23:01Z に入り、うち1件が Copilot 対象である。**570469** では利用者が、Word / Excel / PowerPoint の埋め込み画像に含まれるテキストを Copilot Chat の検索で引き当てられるようになる（GA 2026年10月）。⚠️ 総項目数は 1,773 → 1,769 と4件減っており、総数差分では新規件数を判定できない
  - Copilot Studio 項目は19件すべて `In development` で、GA 期日が September CY2026 の9件は今月末が期日にあたる。**566997** は August CY2026 を超過、**562221** は超過4か月目である
- **Copilot CLI**: pre-release `v1.0.84-4`（9/10 17:23 UTC）が最新のままで、安定版 `v1.0.83`（9/4）は7日間据え置きである
- **停滞の継続**: M365 Copilot Release Notes は先頭が August 25, 2026 のままで、隔週の期日 9/8（UTC）を4回見送っている。Copilot Studio What's New は July 2026 節が最新で、GitHub Copilot ハーネスの GA（8/3）が40日連続で未反映である。Released Versions は 2026.6.3 のまま**73日**動いていない
- ⚠️ **Purview 側の未掲載**: Cowork 向け DLP の Roadmap 項目 **570845**（Preview 9月 / GA 10月）は、本日も Purview の What's New に現れていない。先頭節は August 2026 のままである

### Google

- **Gemini の Windows 版ネイティブアプリ**: 利用者が Alt + Space で任意のアプリの上に Gemini を呼び出せるようになった（9/10 提供開始・Windows 10 / 11 対象）。個人エージェントの Gemini Spark が Connected Apps へアクセスして多段の依頼を処理し、Gmail と Google Drive を参照して文脈の取り込みと文書要約を行う。⚠️ macOS 版（2026年4月）から約5カ月遅れの提供で、インストーラーは `gemini.google/desktop` から直接配布される
  - https://thewincentral.com/google-gemini-app-windows-alt-space/
- **Gemini API changelog**: 最上位は 9/3 の Lyria 3.5 public preview のままで、**8日間**追加がない。料金改定の告知もなく、`gemini-omni-flash-preview` の 9/30 廃止と Gemini 3.7 Flash の導入価格 12/31 終了の記載は不変である
- ⚠️ **到達できる Google 一次は `ai.google.dev` のみという状態が続く**。登録済み5ソース（Workspace Updates / Gemini App Release Notes / The Keyword / DeepMind Blog / Workspace Admin Release Calendar）はゲートウェイ拒否が継続している

### Cursor / xAI / Devin

- **Cursor Projects のベータ開放**: （ハイライト参照）
- ⚠️ **Cursor は GPT-6 Astra の提供開始を告知しないまま9日目である**（9/3 GA）。Copilot は 9/4 に GA、Codex CLI は `0.153.1` 以降で対応済みで、changelog とフォーラムの両方を確認したうえでの不在にあたる
- **Grok 4.7 は公開予定日の当日でも二次情報のままである**。本日 9/12 が Musk の 9/2 の X 投稿による公開見込み日で、パラメータ 2.1兆（4.6 の1.5兆から40%増）とされる。⚠️ xAI はローンチページ・API モデル ID・価格・モデルカードのいずれも未公開で、一次3ホストはゲートウェイ拒否が継続する。公式提供中の最新は Grok 4.6（8/12・context 50万トークン・$2/$6）である
- **Devin は一次・代替一次のいずれからも読めない状態が続く**（`docs.devin.ai` / `cli.devin.ai` ともゲートウェイ拒否）

### 企業構造 / GTM 動向

- **OpenAI が拘束力ある連邦 AI 安全規制を求める側に回った**: chief global affairs officer の Chris Lehane が、自主コミットメントは不十分だとして能力ベースの国家規制を議会に求めた（9/9）。規制に抵抗してきた同社の立場が反転している
  - 求める内容は共通の試験基準・最先端モデルの独立評価・サイバーセキュリティ要件の強化・重大インシデントの報告義務・モデル不整合の継続監視・配備前のアライメント評価ゲート
  - 適用対象は最も高性能なシステムを開発する少数のラボに限り、スタートアップ・小規模開発者・フロンティアから遠い研究者は対象外とする。12月の議会閉会前の立法を求めている
  - ⚠️ **一次未読**で、`openai.com/index/ai-policy-window/` は本日も HTTP 403 である。出来事の日付は 9/9 で、9/10・9/11 付けの報道は後追いにあたる
  - https://www.euronews.com/next/2026/09/11/openai-makes-u-turn-and-calls-for-binding-national-ai-safety-rules
- **Sam Altman が開発減速の選択肢を社内に示したと報じられた**（9/11）。他の AI 企業も同調することを期待しているとされる。⚠️ **一次未読**で出所は Bloomberg 1本であり、上の規制要求と結びつける公式の説明はない
- **Oracle の AI クラウド受注残が $664B に達した**: Oracle が 9/11 に FY27 Q1 決算を発表した。残存履行義務は前年同期比 $209B 増で、クラウドインフラ売上は121%増の $73.88億、非GAAP EPS は $1.92（予想 $1.74）だった。四半期中に 850MW のデータセンター容量を追加している。⚠️ 期中の $300億超の新規 AI 契約は大半が前払いや顧客持ち込みハードウェアで、Oracle 側の追加資本を要しないとされる
  - https://erp.today/oracle-q1-fy27-results-664b-backlog-ai-contracts
- **Microsoft がデータセンター容量を2032年に 38GW 超へ引き上げる計画を示した**（9/10）。現在の約12GW から3倍超で、計画の約3分の1が AI 専用チップ向けを想定する。⚠️ 動機は需要ではなく**供給制約**で、Azure の容量ボトルネックにより2025〜2026年に有償顧客の受け入れを断っていたとされる。2026暦年の設備投資とファイナンスリースは調整ベースで約 $1,750億の見通しである
  - https://techbriefly.com/2026/09/11/microsoft-triple-data-center-capacity-38-gigawatts/
- **Salesforce が Trusted Enterprise AI Harness を先行公開した**（9/10）。6つの「信頼できる能力」と新設の AI Control Plane からなり、同層で MCP サーバーと LLM サーバーを管理してエージェントのレジストリとしても機能する。⚠️ 9/15〜17 の Dreamforce に先行するプレビューで、**全顧客への提供は来年初め**である。料金・パッケージング・提供地域はいずれも GA 時期に近づいてから公表するとしている
  - https://venturebeat.com/orchestration/companies-already-run-3-agent-platforms-salesforces-new-enterprise-ai-harness-wants-govern-all-them
- **追跡中の未確定案件に進展はない**: Salesforce による Listen Labs 買収（約 $2B・9/10 報道）は交渉初期のまま、DeepSeek の上海 STAR 上場は年内説と2027年説が割れたまま、Anthropic の S-1 公開（9月下旬見込み）も確認できていない

### MCP / オープンウェイト / 市場データ

- **MCP 公式ブログは 8/22 の「The New MCP Roadmap」が最上位のままで、21日間**新規がない。WebMCP Challenge は提出締切 9/4 を経過し、受賞発表は 9/23・賞金総額 $35,000 である
- **オープンウェイトは 8 org のいずれにも前回チェック日以降の新規公開がない**。`createdAt` 降順と `lastModified` 降順の両方で確認し、更新された2件（`mistralai/Mistral-Large-3-675B-Instruct-2512-NVFP4` と `zai-org/GLM-OCR`）はどちらもカード更新のみだった
  - 既報の `deepseek-ai/DeepSeek-V4.1-Flash`（9/10 作成・MIT・safetensors 約763GB）は、オフピークのキャッシュ読み取りが $0.003／1M で、50万トークンの再利用プレフィックスを100リクエストで使い回す試算ではオフピーク約 $0.15 に対し GPT-5.6 Sol が $20・Claude Opus 5 が $25 になる
- **市場データの定点ソースに新規公表はない**: IDC・MM総研・NRC・Similarweb のいずれも本日の公表を検知できなかった。Similarweb は8月分（ChatGPT 55.5%・Gemini 25.6%・Claude 9.3%）が最新で、次回は10月上旬の9月分投稿を待つ
- **Apple Developer News の AI 関連エントリは 6/11 の ImageCreator クラス廃止告知のまま**で3ヶ月動いていない。⚠️ 「新しい Siri は Google Gemini で動く」は引き続き二次のみで、Apple の公式説明は Apple Foundation Models と Private Cloud Compute の枠組みにとどまる

## 直近の注目予定

- **9/12**: Grok 4.7 の公開予定（Musk の X 投稿のみが出所・公式の裏づけなし）
- **9/13**: **Claude Code の週次上限50%増が終了**
- **9/14**: iOS 27 / iPadOS 27 の配信（二次情報）／ **Claude Code の標準週次上限が恒久的に +25%**（現行比では17%減）／ 週次復旧チェック（月曜）
- **9/15–17**: Salesforce Dreamforce
- **9/17**: OpenAI DevDay Exchange の応募締切 ／ Anthropic Startup Grant Program の配分年度締切（二次のみ）／ Power Platform 非推奨一覧の定例確認
- **9/18**: 新 iPhone と AirPods 5 の発売
- **9/21**: Anthropic ウェルビーイング研究助成の応募締切
- **9/23**: WebMCP Challenge の受賞発表
- **9/24**: OpenAI の Videos API と Sora 2 系が退役（代替モデルの提示なし）
- **9/28**: Copilot のチャット3面統合 ／ code review の既定 effort が Lite → Balanced ／ チャットのデータ保持がアカウント存続期間へ ／ **OpenAI の `gpt-3.5-turbo-instruct` / `babbage-002` / `davinci-002` / `gpt-3.5-turbo-1106` が停止**
- **9/29 以降**: `claude-sonnet-4-5-20250929` の暫定退役日（確定日ではない）
- **9/30**: Gemini の旧 `gemini-omni-flash-preview` エンドポイント廃止 ／ OpenAI の現行 OneGov 契約（$1/年）が失効 ／ Copilot Studio の Roadmap 9件の GA 期日
- **9月**: macOS 27 GA ／ Claudeforce のオープンベータ（二次情報）／ Cowork 向け Purview DLP の Preview
- **10/1**: **OpenAI の OneGov トークン課金50%割引が開始** ／ Copilot Business・Enterprise の既存顧客が前払い必須に ／ CSP ソフトウェア価格改定が発効 ／ Apple の EU 向け新ビジネス条件が発効
- **10/2**: **GitHub Copilot が Gemini 3.5 Flash / Gemini 3.6 Flash / Kimi K2.7 Code / Claude Opus 4.7 を全体験から廃止**
- **10/5**: Anthropic ウェルビーイング研究助成の full proposal 提出期限（採択者）
- **10/15 以降**: `claude-haiku-4-5-20251001` の暫定退役日（確定日ではない）
- **10/16–11/11**: OpenAI DevDay Exchange 8都市（東京は 10/20）
- **10/23**: OpenAI のレガシースナップショット退役（`gpt-3.5-turbo-0125` / `gpt-4-0613` / `o1-2024-12-17` / `o4-mini-2025-04-16`）
- **10/27–29**: Power Platform Community Conference 2026（ラスベガス）
- **10/31**: OpenAI の既存 evals が読み取り専用になる
- **10月下旬まで**: METR による Anthropic のインシデント独立調査の初回8週間（9/9 起点）
- **10月**: Anthropic の IPO 観測（上場日は未確定）／ Salesforce の AI Control Plane 統合体験は来年初めのロールアウト開始
- **11/15**: Release Planner の退役。Release Wave の緑チェックに依存する GA 検知経路がこの日までに失われる
- **11/21**: GPT-5.6 Sol の暫定値下げが有効とされる期限
- **11/24 以降**: `claude-opus-4-5-20251101` の暫定退役日（確定日ではない）
- **11/30**: OpenAI の Reusable prompts・Evals プラットフォーム・Agent Builder が停止
- **12/1**: OpenAI の GPT Image 系が停止（→ `gpt-image-2`）
- **12/2**: EU AI Act の生成コンテンツ標識義務、8/2 以前に市場投入済みシステムへの猶予終了
- **12/11**: OpenAI の旧スナップショット退役（`gpt-5-2025-08-07` / `o3-2025-04-16` / `o3-pro-2025-06-10` 等）
- **12月まで**: OpenAI が連邦 AI 安全立法を求める議会会期の期限（同社の要求であって審議の予定ではない）
- **12/31**: **Gemini 3.8 Flash と 3.7 Flash の導入価格が終了**（$0.75／$3.75 → $1.50／$7.50）／ **GitHub Copilot の Fable 5.1 / Fable 5 に対する ZDR 暫定免除が終了**
- **年内**: Anthropic の新データ保持方式（顧客自身のクラウドでの30日保持）投入予定 ／ OpenAI の Jalapeño チップの初期展開
- **2027-01-06**: OpenAI で大半のユーザーの新規ファインチューニングジョブ作成が終了
- **2027-01-20**: OpenAI の audio / realtime 系退役（`gpt-realtime` / `gpt-audio` / `gpt-4o-audio` と mini 系）
- **2027-02-26**: OpenAI の文字起こし4モデル退役（`whisper-1` ほか）
- **2027-04**: **Apple の最小 SDK 要件が iOS 27 世代へ上がる**
- **2027-06-30**: Claude for Teachers の学区登録期限
- **2028-03**: OpenAI が「automated AI researcher」の実現目標とする時期

## 改善メモ

- ソース間の矛盾: Claude Code `2.1.269` の内容について、01 は「changelog 未掲載・内容未確定」、03 は「`claude plugin eval` と `/output-style [name]` を含む」と記録しており正面から食い違う。publish 時刻（9/11 18:12 UTC）は一致するため、差は changelog 掲載前に別経路で内容を取ったかどうかにある可能性が高い
- 新規提案: 01 が B-068（`www.anthropic.com/research` を `/news` とは別の一次一覧として登録）、02 が B-064（Copilot Cowork の追跡が6ページ固定で同一サブツリーの残り16ページを未読）を起票した。03 は新規提案なし
- 継続提案は 01 が9件（最多 B-024 changelog の取りこぼし検出手順・38回目）、02 が32件（最多 B-011 Power Platform Blog のトピック記事照合・53回目）、03 が4件（最多 B-004 取得方法欄の WebSearch 化・75回目）
- 障害の変化: 03 が `thehackernews.com` を新規のゲートウェイ拒否として台帳に追加した（既収録の内容のみで実害なし）。`www.anthropic.com` は01・03とも2日連続で本文取得に成功し、復旧が定着している
- 3ソースで同一日に「1日遅れの検出」が3件（Cursor changelog の 9/11 分、OpenAI changelog の Agents API と API キー有効期限、GitHub changelog の 9/10 の3件）重なった。いずれも降順ページの最上位取りこぼしで、01 の B-024 と同型である
