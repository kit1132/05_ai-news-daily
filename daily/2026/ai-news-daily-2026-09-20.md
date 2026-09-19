# AI News Daily Summary — 2026-09-20

10月1日に効く既定変更が2本重なった日である。OpenAI は ChatGPT for Word の Word アクセスを 10/1 から既定オンにし、Microsoft は Teams のリテンションポリシーが Copilot 会話を暗黙に保持しなくなる変更を10月に予定した。どちらも「管理者が何もしなければ現状が続く」前提が反転する。手元では Claude Code `2.1.278` が auto モードの既定を4日前と逆に戻し、classifier のオーバーヘッド課金を止めた。

## 今日のハイライト

### 1. ChatGPT for Word の Word アクセスが 10/1 から既定オンになる — 止める判断を期日前に入れないと Word に ChatGPT が入る

**要点**: OpenAI が ChatGPT for Word を Enterprise / Edu へ提供し、**10月1日**から Word アクセスを既定オンにする。管理者が明示的に止めない限り Word に ChatGPT が入る前提へ変わる。

**詳細**: サイドバーからメモを元にした下書き、文書の要約、選択範囲の修正、見出しと書式の調整ができる。導入は Excel / PowerPoint と同じ Microsoft アドインを使う。

- 管理面: ChatGPT 管理コンソールで Word アクセスを on / off でき、加えて Microsoft 365 管理者側でも ChatGPT アドインを許可しないと Word 上に現れない。10/1 以降は既定が「オン」になる
- 課金: Business / Enterprise / Edu では Word の利用が使用モデルの **API 単価**でトークン課金される。座席料金に含まれる機能ではない
- 同時に、テナント全体の SCIM が API Platform に対応した。グローバル管理者が管理コンソールの Product access から同期済みグループを API 組織と選択したプロジェクトへ割り当てられ、メンバーは招待の承諾なしでアクセスを得る

⚠️ 一次（`help.openai.com`）はオリジン403で本文に到達できず、**公表日は 9/15〜9/19 の週内までしか特定できていない**。内容は複数の二次の一致で構成されている。なお ChatGPT for Word の一般提供そのものは、01 側が 9/17 の Astra for Law 発表に併記された項目として拾っている。

- https://help.openai.com/en/articles/10128477-chatgpt-enterprise-and-edu-release-notes
- https://help.openai.com/en/articles/20001526-chatgpt-for-word

### 2. Claude Code の auto モード既定が4日で反転した — classifier のオーバーヘッド課金が消える

**要点**: `2.1.278` が auto モードの既定をサーバー側 classifier へ戻し、**classifier のオーバーヘッドを課金しなくなった**。4日前の `2.1.273` はローカル classifier を既定にしていたので、`CLAUDE_CODE_AUTO_MODE_SERVER` の意味が反転している。

**詳細**: `2.1.278` は 9/19 01:48 UTC に publish された。auto モードでは、シェルコマンドやネットワークリクエストの実行前に classifier が安全チェックを走らせる。本版以降はこのチェックをセッション自身のモデルリクエストの一部としてサーバーに依頼し、サーバーが実施したぶんは課金されない。

- 対象: Claude API を使うアカウントと Enterprise プラン、および Claude Platform on AWS / Amazon Bedrock / Google Cloud Agent Platform / Microsoft Foundry。Pro / Max / Team プランは対象外で通知も出ない
- フォールバック: サーバーのチェックがセッションに届かなくなると Claude Code 自身の classifier リクエストに戻り、課金も従来どおりになる。その時点で「このセッションは対象外」という通知が出て操作が保留される（Enter で続行・Esc で中止）
- 届かない原因: 経路上の LLM ゲートウェイ / プロキシが `safeguards` リクエストフィールドや `safeguard_results` を落とす、tool-use ID を書き換える、といった加工をしている場合。プラットフォーム・リージョン・資格情報が未展開の場合もある
- 切り戻し: `CLAUDE_CODE_AUTO_MODE_SERVER=0`（Anthropic API への直接接続では読まれない）。`/status` に **Auto mode server** 行が追加され `Enabled` / `Disabled` を確認できる。この環境変数は暫定で将来削除される可能性がある

⚠️ **`2.1.273`（9/15）は同じ対象に対して逆の既定を置いていた**。当時は Bedrock / Vertex / Foundry で当面ローカル classifier を既定とし、サーバー側へ回すには `=1` を設定する形だった。9/15 に `=1` を明示設定した組織は、本版以降その指定が既定と同じ意味になる。

⚠️ この変更は stable 固定の組織にまだ届いていない。npm の `dist-tags` は `{stable: 2.1.267, latest: 2.1.278, next: 2.1.278}` で、`stable` は 9/9 publish の `2.1.267` から11日連続の据え置き、未到達は `2.1.268`〜`2.1.278` の11版ぶんである。

- https://code.claude.com/docs/en/changelog
- https://code.claude.com/docs/en/auto-mode-classifier-billing

### 3. Teams のリテンションポリシーが10月に Copilot を外れる — 既存ポリシーで Copilot 会話を保持できていた前提が消える

**要点**: 10月以降、Teams のリテンションポリシーは Copilot の会話を暗黙に保持しなくなる。Copilot の保持期間は「Teams の設定を流用できる」前提から「専用ポリシーを別に作らないと素通し」へ変わる。

**詳細**: Roadmap **571306**「Microsoft Purview: Data Lifecycle Management-Legacy Teams retention policies covering Copilot will be treated as Teams-only」が 9/18 22:00Z に起票された。ステータスは `In development`、GA 期日は **October CY2026**、対象は Worldwide（Standard Multi-Tenant）の Web である。本文は、Teams をスコープにした既存のリテンションポリシーが現在 Copilot の対話にも適用されている場合があり、今後の変更でこれらが Teams 専用ポリシーへ変換されて Copilot ワークロードを暗黙に統制しなくなる、と書く。

- 分離後のロケーション: Microsoft Copilot experiences（M365 Copilot / Security Copilot / Copilot in Fabric / Copilot Studio）、Enterprise AI apps（Entra 登録 AI アプリ / ChatGPT Enterprise / Microsoft Foundry）、Other AI apps（ChatGPT / Google Gemini / Copilot 消費者版 / DeepSeek）
- 保持対象: ユーザーのプロンプトと応答。Copilot Studio は M365 Copilot と同じ扱いで、他の生成 AI アプリは収集ポリシーでコンテンツ取得を有効にした場合に入る
- 削除の所要時間: 1日で削除する設定でも、コンプライアンス上の多段処理のため eDiscovery から消えるまで最大16日かかる
- 退職者の扱い: アカウント削除後も Copilot のメッセージは非アクティブメールボックスに残り、リテンションポリシーの対象であり続ける

⚠️ 10月という期日に対して、一次ドキュメントは未更新である。`purview/retention-policies-copilot` の Note は**新規作成**のポリシーで別ロケーションを選ぶところまでしか書かず、既存ポリシーが変換される話は書いていない。Purview の What's New（`updated_at` 2026-09-16T17:34Z）September 2026 節にも本件はなく、**Roadmap 項目だけが一次**になっている。

- https://www.microsoft.com/microsoft-365/roadmap?id=571306
- https://learn.microsoft.com/en-us/purview/retention-policies-copilot

## カテゴリ別まとめ

### Claude / Anthropic

- Claude Code の `2.1.278`（9/19 01:48 UTC）が本日唯一の新版である（ハイライト2参照）。`2.1.277` 以前の内容は前日ぶんから変化がない
  - ⚠️ 本日時点で 9/19 の publish は `2.1.278` の1件のみで、UTC 09-19 はまだ終わっていない
- Anthropic が Accenture を初の「組込み評価者」に選んだ（9/18）。両社がそれぞれ今後5年で**最低10億ドル**をこの体制構築に投じる見込みで、第三者検証が社外から報告書を出す形から社内常駐へ変わる
  - 主導は Accenture の AI 専業部門 Faculty で、業務はモデルの評価とレッドチーミング、アライメント評価、セーフガードの検証である。さらに会社の運営の仕方を評価し、安全上の約束が守られているかを検証し、盲点を指摘し、インシデントを公表する役割まで含む
  - 従来の外部評価者との違いは access の水準にある。組込み評価者は従業員同等のアクセスで、訓練の途中でモデルが形になる過程を観察し、構築と展開を決める意思決定を追跡し、従業員と直接やり取りする
  - 非独占で、Anthropic は数週間内に追加の評価者を発表するとしている。METR ほかの非営利評価者とは、各団体自身の資金で組込み評価の一部を試行する協議が並行している。採用人数と開始時期は未公表である
  - ⚠️ 9/12 の Amodei 論考「We Must Pace the Frontier」で示した「評価者を社内に置く」という約束の実装にあたる。9/14 の Microsoft AI 行動規範草案、9/16 の OpenAI ミスアライメント6件公表、9/17 の Anthropic 指標公開と並ぶ8日間の5社目だが、**本件だけが契約と金額を伴う**
- ⚠️ Claude のモデル退役ページの Active は11件ではなく**13件**だった。01 の全行照合で確定したもので、前日までの記録は `claude-mythos-5`（2027-06-09 以降）と `claude-mythos-5-1`（2027-09-01 以降）の2件を落としていた。本サマリー 09-19 版の「Active は11件で据え置き」も同じ誤りを引き継いでいる
- Claude Platform API の release notes に新規はない。9/18 の Compliance API（Claude in Chrome のトランスクリプトを `product_surface` = `claude_in_chrome` で返す・Enterprise ベータ）が最上位のままである
- `claude.com/blog` は 9/17 以降の新規がなく、最上位は 9/17 の2本（Balyasny の Fable 5 評価事例／Projects 再設計）である。`support.claude.com` の Release Notes も 9/15 の Salesforce in Claude が最上位のままで、製品ブログが release notes に先行する形が続く
- `www.anthropic.com/research` と `alignment.anthropic.com` はいずれも新規投稿がない。research の最上位は 9/17 の生体分子モデリングで、alignment は8月の "Training a Misaligned Reward Seeker" のままである

### OpenAI / Codex / ChatGPT

- OpenAI が法務向けの **Astra for Law** を発表した（9/17・01 が本日はじめて検出）。GPT-6 Astra に法務分析と文書作成向けの指示・徹底的に調べる設定・法律事務所向けの統制を組み合わせた構成である
  - Legal Search Index: 米国の判例・制定法・規則・裁判所規則・行政決定を横断し、対象は 2億3,000万 URL 超で日次追加される。CourtListener を運営する非営利の Free Law Project と組み、公表済み米国先例判例の99.9%超を収める
  - ベンチマーク: 法務リサーチの正答率が **54%**（標準の Web 検索を使う GPT-6 Astra は 38.7%）だった
  - 提供: 選定事務所への Trusted Access（ChatGPT と Codex 経由）が先行し、API は後日 `gpt-6-astra-law` として提供予定である。日付も価格も示されていない
  - エコシステムプラグイン26件（Relativity・Clio 等）と法務向けコミュニティプラグイン47件が同時に用意され、Thomson Reuters・Harvey・Legora・iManage が参加している
  - ⚠️ 一次はオリジナル403で未読で、二次一致による構成である。本件は 09-18・09-19 のセッションでは検出できていなかった
- `learn.chatgpt.com` に 9/18 の2本が加わった
  - Codex CLI 0.155.1: 新規のローカル TUI セッションが推論サマリーを既定で無効にする。サマリー無しの設定を受け付けないプロバイダーで要求が拒否される問題への対処で、明示的な推論サマリー設定は従来どおり尊重される
  - ChatGPT for iOS 1.2026.251: ファイルピッカーから直接フォルダを作成でき、ライティングブロックにドラフト代替案とコピー操作が加わり、新規タスクがワークツリーモードと環境セットアップを記憶する。修正は音声通話の接続中断時の信頼性、iPad のプロジェクト / 環境 / Git 操作の配置、思考タイマーのリセットなど
  - ✅ `rust-v0.155.1` の本文が一次で確定した。前日は GitHub の個別タグ本文が2回とも読めず未確定だった項目で、併用一次が GitHub releases の欠落を埋めた2例目である
- Codex の tags に 0.156.0 系 alpha が4本増えた。9/19 に `rust-v0.156.0-alpha.6`〜`alpha.8` の3本、9/18 に `alpha.2`〜`alpha.5` の4本が刻まれており、安定版は `rust-v0.155.1`（9/18）のままである。0.156.0 系は 9/17 の `alpha.1` から3日で8本に達した
- OpenAI の一次料金ページは27日連続で据え置きである。GPT-6 Astra 短文脈 $10／$50（キャッシュ $1.00）・長文脈 $20／$75、GPT-5.6 Sol $4／$20（期間限定価格は少なくとも **2026年11月21日**まで）、Terra $2／$12、Luna $0.20／$1.20、`gpt-5.3-codex` $1.75／$14、`gpt-rosalind-research` $5／$25（課金開始 10/5）に改定告知は出ていない
  - ⚠️ 本日の抽出は主要モデル節だけを返し、09-19 に初めて記録したレガシーモデル行（`gpt-5.5` $5／$30 ほか）が出なかった。料金表から消えたのではなく抽出のばらつきである
- 退役ページに 9/11 より新しい告知はない。最上位は `gpt-5.4-cyber`（削除 10/1・移行先 `gpt-5.6-cyber`）のままで、撤回・延期・新規追加は検知されていない
- `developers.openai.com/api/docs/changelog` は 9/15 の API キー作成ガバナンス制御が最上位のままで、`community.openai.com` の Announcements RSS も 9/10 の Agents API 告知から9日間動いていない。`alignment.openai.com/misalignment-reports/` も6件のままである

### GitHub Copilot

- GitHub が Copilot code review のレビュー体験を一般提供へ更新した（9/18）。指摘の追跡と一括適用の手間が減る
  - 概要コメントがリアルタイムで更新され、各指摘に短いタイトルと重大度、インラインコメントへのリンクが付く。新規に入った問題には `new` ラベルが付き、複数コミットにまたがって進捗が保持される
  - 自動解決: 指摘が対応されたかどうかでコメントが自動解決し、返信で「開けておくべき」と示された場合はその返信を尊重する。以降のコード変更に応じて `Won't Fix` / `Incorrect` の解決理由が付く
  - コミットメッセージ: 提案をまとめて適用すると、選択した変更を元にコミットのタイトルと任意の説明が生成される。Copilot 以外のコメントを含むバッチでも生成される
  - ⚠️ 指摘の3分類について、01 は「未解決 / 前回レビュー以降に解決済み / 新規検出」、03 は「Open / Resolved / Previously missed」と書いており**中間の1分類が一致しない**（改善メモ参照）
  - https://github.blog/changelog/2026-09-18-copilot-code-review-an-improved-review-experience
- 週次リリース（9/14 ぶん・掲載は 9/18）で3段階のモデル選択が展開に入った。コスト・品質・応答時間を「効率 / バランス / インテリジェンス」から選ぶ形で、VS Code・CLI・アプリに順次届く
  - Business / Enterprise 側: VS Code Agents ウィンドウの利用統計が GA（日次アクティブユーザー・セッション数・メッセージ合計）、リポジトリのカスタムプロパティ値の提案がパブリックプレビュー、AI クレジット上限到達時の予算増加申請が GA
  - Copilot アプリ側: Sentry 統合が入り、クラッシュレポートから修正までを「Sentry キャンバス」で扱える
  - VS Code 1.138: ローカル Dev Containers でのエージェント実行（段階展開・Docker 必須）、非アクティブセッションの自動完了と削除（オプトイン・プレビュー）、Agents ウィンドウからの PR 作成
- Copilot CLI の pre-release `v1.0.87-0` が出た（9/18 21:29 UTC）。安定版は `v1.0.86`（9/17 22:57 UTC）のままである
  - 追加: 自動ルーティング層向けのユーザー管理スタートアップ既定、同一モード内での連続ステアリングプロンプトの統合、`worktreePathTemplate` によるワークツリー作成位置の指定
  - 改善: MCP の低速接続警告閾値をサーバー別に設定する `slowConnectionThresholdMs`、タイムラインでのサブエージェント経過時間表示、全モデルファミリーと低コストティアでのラバーダックエージェント有効化
  - 修正: 質問ダイアログの数字キー選択が10以上でも効く、Windows のサンドボックスプロキシと認証付きプロキシ、`/keep-alive` のスリープ阻止報告、大規模ローカルセッション再開の信頼性
  - ⚠️ 本 pre-release に破壊的変更の記載はなく、`v1.0.85` の3件（`copilot plugins list --json` のフラット配列化・`--kind` / `--scope` 削除・`plugins list` の対象縮小）は未解消のまま残る
- ⚠️ GitHub changelog の 9/18 付は **5件**で、前日記録の4件から1件増えている。増えた1件は上記の code review 改善であり、新規公開ではなく前日の抽出漏れである。9/19・9/20 付は0件である

### Copilot Studio / Power Platform

- Copilot Studio 標準ハーネスの既定オーケストレーションモデルが **GPT-5.5 Chat** になった。モデルを固定していないエージェントは、挙動と無効化時のフォールバック先が GPT-4.1 から入れ替わる
  - `authoring-select-agent-model` の `ms.date` が 2026-09-17 → 2026-09-18 へ動き、`Standard harness availability` 表は15行になった（9/18 記録は13モデル・既定 GPT-4.1）。`Tag/Category` 列（Deep / Auto / General）と `Model use categories` 表が新設された
  - GA: GPT-4.1 / GPT-5 Chat / Claude Sonnet 4.6 / Claude Opus 4.6（Deep）/ Claude Opus 4.7（Deep）。Preview は GPT-5 Reasoning（Deep）と GPT-5 Auto（ターンごとに動的ルーティング）
  - Experimental: 米国の早期アクセス環境のみで GPT-5.3 Chat / GPT-5.4 Reasoning / GPT-5.5 Reasoning / Grok 4.1 Fast、全リージョン cross-geo で Mistral Medium 3.5。Retired は GPT-4o / Claude Sonnet 4.5
  - ⚠️ 政府クラウドの表は同じ動きをしていない。`US Government availability` 表は GCC / GCC High / DoD の3列とも **GPT-4o が Default** のままで、商用13リージョンでは同じモデルが Retired である
  - ⚠️ この改訂は Copilot Studio What's New（July 2026 節が最新）にも Release Notes（August 25 バッチ）にも現れていない
  - https://learn.microsoft.com/en-us/microsoft-copilot-studio/authoring-select-agent-model
- Copilot Cowork が GCC / GCC High のロードマップに載った（Roadmap **571637**・GA November CY2026）。DoD は含まれず、対応面は Android / Desktop / iOS / Mac / Web の5つである。9/15 の Microsoft 365 G7 発表の延長線上にある
  - 商用で確定している前提のうち、政府クラウドでそのまま読めないものが4つある。ブラウザー操作は Allow browser access が既定無効で必要 Edge が 152.0.4191.53 以上、Web 検索は政府クラウドで既定オフ（商用は未構成なら使える）、既定モデルは GPT-4o のまま、Cowork 向け Purview DLP（570845・GA 10月）は Worldwide のみ対象で政府クラウドは対象外である
  - https://www.microsoft.com/microsoft-365/roadmap?id=571637
- Copilot Studio のガイダンスハブで `generative-orchestration` が標準ハーネスの語彙へ全面的に書き換わった（`ms.date` 2026-09-18）。プランナーの呼称が `Standard harness (planner)` になり、制御を3層に分ける節が入った
  - 決定論層: 支払い・レコード削除など不可逆な操作は AI 解釈を挟まないトピック / フローで実行し、ハーネスに上書きさせない
  - ハイブリッド層: AI が下書き・実行し、承認ステップや金額上限で差し込む
  - AI ハーネス層: 低リスクの Q&A や情報参照はプランナーに任せる
  - 決定境界を「確認なしで実行できる操作」「会話内でユーザー確認が要る操作」「オフラインの承認が要る操作」の3つに明示的に分けるよう求めている。⚠️ 本改訂はガイダンスハブ自身の What's New の September 2026 節に載っていない
- M365 Copilot Release Notes は **August 25, 2026** バッチのままで新規がない。隔週の期日 9/8（UTC）から12日、前バッチからは26日が過ぎている
- Copilot Studio の Roadmap 起票は22件で増減なく全件 `In development` のままである。⚠️ GA 期日 September CY2026 を持つ **14件**は残り10日で、うち3件（571194 / 571195 / 571196）はコスト可視化の3点セット（Preview Chat と History / Agent Evaluations / Monitor タブ）である
- Power Platform Blog の親ページは 9/3 の PPCC 2026 記事が先頭のままで、9/17 公開の「What's new in Power Platform: September 2026 feature update」が公開から3日たっても一覧に現れていない。Power Apps / Power Automate の子カテゴリでは 9/17 の月次記事が先頭である
- Copilot Studio Build の最新は **2026.6.3** のままで、`released-versions/copilotstudio` の `updated_at` が 81日動いていない。Copilot Agent Kit も CopilotAgentKit-September2026（9/8）が最新で新規はない

### Microsoft（その他）

- Partner Center が Check Inventory API の退役を再告知した（9/18）。パートナーは **9月25日**までに Check Inventory by Resource Type API へ移行する必要があり、9月の告知は13件から14件に増えた
  - 新 API は `resourceType` パラメーターを必須にしてリソース種別ごとに在庫を確認する。レスポンス契約は変わらない。⚠️ AI / Copilot とは無関係の在庫確認 API である
  - https://learn.microsoft.com/en-us/partner-center/announcements/2026-september
- Purview の What's New は 9/17 に取り上げた Entra Global Secure Access 連携の1件のままで増減がない。⚠️ **Purview 側の未掲載が3件から4件に増えた** — 9/8 起票の 570845、9/15 起票の 571397 / 571396 に加え、本日の 571306 も Purview の一次に現れていない
- Cowork ドキュメント19ページで `ms.date` が動いたページはゼロである。9/19 に検知した `cowork-local-browser`（必要 Edge 152.0.4191.53）と `cowork-plugin-development` も据え置きである
- ⚠️ Copilot Tuning は停止の発効（8/20）から31日たっても `copilot-tuning-overview` が停止も退役も書いていない。本文は「Access through Frontier is planned for April 2026」という既に過ぎた予定を現在形で残している
- Agent 365 Blog は「What's new in Agent 365 – July 2026」（8/6 公開）が最新のままで、沈黙が45日になる

### Google

- Gemini API changelog に 9/17 より新しいエントリはなく、最上位は `antigravity-preview-09-2026` のままである。旧 `antigravity-preview` の停止は **10/5** で、パラメータ命名が snake_case → PascalCase、ファイル編集が全文書き換え → 行範囲置換に変わる
  - ⚠️ 前日に記録した `gemini-omni-flash-preview` の廃止（9/30）が本日の抽出には現れず、代わりに `gemini-robotics-er-1.6-preview` の 8/31 停止が出た。エントリの取りこぼしが読むたびに入れ替わる型である
- Workspace 側に 9/18 の Weekly Recap が加わったが、既出記事のまとめで新規機能の告知はない（Drive の共有境界／Gmail 検索の AI Overviews 全世界展開／Gemini の外部ツール7件 MCP 接続／Apps Script のデータリージョン GA 等）
- `blog.google` は本日も差分判定に使えない。`curl` は 301 を返してゲートウェイを通過するが、WebFetch の応答に日付が出ないため更新有無を判定できない
- 既報: `gemini-3.8-flash` は入力 $0.75 / 出力 $3.75 が 2026-12-31 まで、Gemini 3.5 Pro GA は未ローンチが継続する

### Cursor / xAI / Devin / オープンウェイト

- Cursor changelog は 9/10 の Projects が最上位のままで新規がなく10日間動いていない。フォーラム Announcements も 9/2 の Grok Bot Android 版のままで18日間動いていない
  - ⚠️ Cursor は GPT-6 Astra の提供開始を告知しないまま17日目である（9/3 GA）。**11/12 の OpenAI による供給停止予定**と併せて読む必要がある
- Grok 4.7 は公開予定日 9/12 を過ぎて8日目も未公開である。2.1兆パラメータ等はいずれも Musk の X 投稿が出所の二次で、xAI 一次にはローンチページもモデル ID も価格もない。公式提供中の最新は Grok 4.6（8/12・context 50万トークン・$2/$6）である
  - ⚠️ Grok 4.5 は GitHub Copilot から 10/19 に廃止される。**4.7 が出ないまま 4.5 の退役だけが確定した**形になる
- Devin は一次・代替一次のいずれからも読めない状態が続く（`docs.devin.ai` / `cli.devin.ai` ともゲートウェイ拒否）
- HF の 8 org のいずれにも 9/19 に作成または更新されたリポジトリは1件もない。⚠️ `meta-models/utils`（safetensors 0件・README のみ）を除くと、8 org の実モデルは 9/11 以降9日間、新規も更新も1件もない
- `blog.modelcontextprotocol.io` は 8/22 の「The New MCP Roadmap」が最上位のままで29日間新規がない。⚠️ 仕様側は止まっているが、実装側の指示ファイル互換（Claude Code の AGENTS.md サポート、Copilot CLI のカスタムエージェントからの `AGENTS.md` / `CLAUDE.md` 読み取り）は動いている

### 企業構造 / GTM・規制

- 有料契約者4名が Anthropic / OpenAI / SpaceXAI / Google を相手に反トラスト集団訴訟を提起した（9/18・カリフォルニア州北部地区連邦地方裁判所）。訴状は、9/12 に Dario Amodei が開発ペースの減速を呼びかける論考を公開し同日 Sam Altman・Elon Musk・Demis Hassabis が同調したことを協調行為の中核に据える
  - 原告は ChatGPT / Claude / Grok / Gemini の有料加入者で、競争があれば得られたはずの改善が遅れるぶん**同じ料金で劣る製品**を買わされていると主張し、全国規模のクラスを想定する
  - ⚠️ 現時点で提起のみであり、認定も命令もない
  - https://www.cbsnews.com/news/ai-slowdown-lawsuit-openai-anthropic-google/
  - https://news.bloomberglaw.com/litigation/openai-anthropic-google-spacexai-hit-with-antitrust-lawsuit
- ⚠️ Harvey が OpenAI の法務エコシステムにプラグイン提供者として並んだ（9/17）。Harvey は Anthropic の frontier モデルを法務 SaaS に展開している事例として月次で追っている先であり、**ベンダー専属ではなく複数フロンティアの上に乗る形**が確認できた。Anthropic 側からの言及はない
- Google による Claude Opus 5 の全エンジニア開放（9/15・初出 09-16）に一次の追認は依然としてない。Anthropic のコンピュート契約 $517B・14.8GW（The Information・初出 09-16）も一次未読のままで、⚠️ $517B は確定支出ではなく上限枠である

### 市場データ

- IDC / MM総研 / NRC / Similarweb はいずれも新規公表がなく、引用可能値は 09-19 から変わっていない（IDC 国内 AI 支出 2025年 2兆3,725億円 → 2029年 6兆8,897億円・CAGR 36.0%／Gartner 世界 AI 支出 2026年 $2.59兆・+47%／MM総研 国内生成AI個人利用率 21.8%）
  - ⚠️ **Similarweb 8月分のシェアで二次情報が割れた**。09-09 に同社公式アカウントの投稿から確定させた ChatGPT 55.5%・Gemini 25.6%・Claude 9.3% に対し、本日の検索面には ChatGPT 53.9%・Gemini 27.9%・Claude 9.2% を8月分として示す集計が出ている。発信元の投稿が一次であるため既収録の値を採り、後者は併記しない
  - ⚠️ IDC はプレスリリースの別ホスト `my.idc.com` もゲートウェイ拒否であることが本日確認され、「2026年、日本の AI インフラ投資は8,000億円を超える」は4日連続で公表日に到達できていない

## 直近の注目予定

- **9/21**: Anthropic ウェルビーイング研究助成の応募締切 ／ 各リポジトリの週次復旧チェック（月曜）
- **9/22 前後**: M365 Copilot Release Notes の次バッチ（期日超過中）
- **9/23**: WebMCP Challenge の受賞発表 ／ Microsoft「Partnering for Success Together」第1回
- **9/24**: OpenAI の Videos API と Sora 2 系が退役（代替モデルの提示なし）
- **9/25**: Microsoft Partner Center の Check Inventory API が退役
- **9/28**: OpenAI の `gpt-3.5-turbo-instruct` / `babbage-002` / `davinci-002` / `gpt-3.5-turbo-1106` が停止 ／ Copilot のチャット3面統合・code review 既定の Balanced 化・チャットのデータ保持がアカウント存続期間へ ／ Anthropic × Adaptyv のタンパク質設計コンペ開始（〜10/31・毎週1題）
- **9/29**: OpenAI DevDay 本体（サンフランシスコ Fort Mason） ／ `claude-sonnet-4-5-20250929` の暫定退役日
- **9/30**: Gemini の旧 `gemini-omni-flash-preview` が廃止 ／ OpenAI の現行 OneGov 契約（$1/年）が失効 ／ **Copilot Studio の Roadmap 14件が GA 期日** ／ M365 E7 プロモ最終日・E5 / E3 の CSP 割引終了 ／ 2026 Wave 1 の対象期間終了
- **9 月中**: macOS 27 GA ／ Claude Projects 再設計が Pro / Max の Claude Code 利用者全体へ拡大 ／ Copilot Tuning の Public Preview 再開 ／ Release Plans の新規掲載停止 ／ Claude for Financial Advisors の一度限りの利用クレジットの期限
- **10/1**: **ChatGPT for Word の Word アクセスが既定オンへ** ／ OpenAI の `gpt-5.4-cyber` が API から削除 ／ OneGov トークン課金50%割引が開始 ／ Copilot Business・Enterprise の既存顧客が前払い必須に ／ Microsoft CSP ソフトウェア価格改定と M365 G7 の GA ／ Apple の EU 向け新ビジネス条件が発効
- **10/2**: GitHub Copilot が Gemini 3.5 Flash / Gemini 3.6 Flash / Kimi K2.7 Code / Claude Opus 4.7 を全体験から廃止
- **10/5**: Gemini の旧 `antigravity-preview` が停止（パラメータ命名と編集方式が変わる） ／ OpenAI `gpt-rosalind-research` の課金開始 ／ Anthropic 助成の full proposal 期限
- **10/13**: Office LTSC 2021・Project LTSC 2021・Visio LTSC 2021 のサポート終了
- **10/14**: OpenAI の `gpt-5.5` が ChatGPT / ChatGPT Work / Codex から退役（API は対象外）
- **10/15 以降**: `claude-haiku-4-5-20251001` の暫定退役日
- **10/16–11/11**: OpenAI DevDay Exchange 8都市（東京は 10/20）
- **10/19**: GitHub Copilot が Gemini 3.7 Flash / GPT-5.5 / GPT-5.4 / GPT-5.4 mini / GPT-5 mini / Grok 4.5 を全体験から廃止
- **10/22 / 10/23**: Apple の Volume Purchasing 開始 ／ iPhone Duo 発売（iOS 27.1） ／ OpenAI のレガシースナップショット退役
- **10/26 頃**: Microsoft AI の MAI モデル行動規範の公開協議が終了
- **10/27–29**: PPCC 2026
- **10/31**: OpenAI の既存 evals が読み取り専用に ／ Anthropic × Adaptyv コンペの最終週
- **10 月中**: **レガシー Teams リテンションポリシーが Teams 専用へ変換**（571306） ／ Cowork 向け Purview DLP の GA（570845） ／ Anthropic の IPO 観測（上場日は未確定）
- **11/2**: Copilot Business の従量課金が既定オン（$10/ユーザー/月の枠つき） ／ GitHub Actions の `pull_request_target` 既定無効化が公開リポジトリで強制開始
- **11/12**: OpenAI が Cursor へのモデル供給を停止する予定日（一次未読）
- **11/15**: Microsoft Release Planner 退役
- **11/21**: GPT-5.6 Sol の暫定値下げが有効とされる期限
- **11/24 以降**: `claude-opus-4-5-20251101` の暫定退役日
- **11/30**: OpenAI の Reusable prompts・Evals プラットフォーム・Agent Builder が停止
- **11 月中**: **Copilot Cowork の政府クラウド GA**（571637）
- **12/1**: OpenAI の GPT Image 系が停止（→ `gpt-image-2`）
- **12/2**: EU AI Act の生成コンテンツ標識義務の猶予終了
- **12/11**: OpenAI の旧スナップショット退役
- **12/31**: Gemini 3.8 Flash と 3.7 Flash の導入価格が終了 ／ GitHub Copilot の Fable 5.1 / Fable 5 に対する ZDR 暫定免除が終了
- **年内**: Anthropic の新データ保持方式 ／ Claude Docs / Claude Slides の Team・Free への展開 ／ Astra for Law の API 版 `gpt-6-astra-law`（日付未定）
- **2027-02-05 / 02-17 以降**: `claude-opus-4-6` / `claude-sonnet-4-6` の暫定退役日
- **2027-03-31**: Azure ポータルの Microsoft Sentinel 体験が退役
- **2027-04-16 / 05-28 / 06-09 / 06-30 / 07-24 / 09-01 以降**: `claude-opus-4-7` / `claude-opus-4-8` / `claude-fable-5`・`claude-mythos-5` / `claude-sonnet-5` / `claude-opus-5` / `claude-fable-5-1`・`claude-mythos-5-1` の暫定退役日

## 改善メモ

- 新規提案2件: 01 は B-077（Claude モデル退役ページの Active 行を件数ごと機械的に列挙する規定を B-047 に追加する）、02 は B-073（状態ファイルが追跡ページを完全 URL で記録していないため、サブツリー移設と記録の略記を区別できない）。03 は新規提案なし
- 継続提案: 01 が26件（最多 B-024 取りこぼし検出手順・46回目）、02 が42件（最多 B-011 Power Platform Blog の WebSearch 照合・60回目）、03 が5件（最多 B-004 取得方法欄の WebSearch 優先化・83回目）
- 障害の変化: 01 が `rust-v0.155.1` の本文を `learn.chatgpt.com` で一次確定した（GitHub の個別タグ本文欠落は未解消だが、併用一次で埋めた2例目）。`www-cdn.anthropic.com` はルートが 404 を返しゲートウェイ通過を確認したが、本文取得は PDF の実パスでしか確認できず未確認が続く
- ソース間の差分: Copilot code review の指摘3分類について、01 は「未解決 / 前回レビュー以降に解決済み / 新規検出」、03 は「Open / Resolved / Previously missed」と記録しており、**中間の1分類が一致しない**。本サマリーは両論併記とした
- 本サマリーの訂正: 09-19 版に書いた「Claude モデル退役ページの Active は11件で据え置き」は誤りで、正しくは **13件**である（01 の全行照合で確定。`claude-mythos-5` と `claude-mythos-5-1` の2件が落ちていた）
- ⚠️ 01 と 03 の GitHub changelog 取得に抽出のばらつきが続いている。03 は 9/18 付が4件→5件に増えた原因を「前日の抽出漏れ」と特定しており、同じ型が OpenAI 料金表（レガシーモデル行の消失）と Gemini API changelog（`gemini-omni-flash-preview` の消失）でも本日同時に起きている
