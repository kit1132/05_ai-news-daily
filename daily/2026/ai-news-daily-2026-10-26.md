# AI News Daily Summary — 2026-10-26

The Information の報道によると、OpenAI は Anthropic の大口顧客に定価から30〜90%の値引きを出して乗り換えさせている。Google は Gemini アプリからノートブックを作成・削除できる Gemini Notebook の接続アプリを既定オンで出した。Stably AI は Orca `v1.4.240` で、承認が要る Codex の MCP ツール呼び出しを承認カードで止めるようにした。週末明けのため、Microsoft の一次情報に新しい発表は無い。

## 今日のハイライト

### 1. [料金+動向] OpenAI が Anthropic の大口顧客を最大9割引で奪っていると報じられた — API の定価は企業調達の基準にならなくなった

**要点**: The Information によると、OpenAI は Replit・DataCamp などの大口顧客に定価から30〜90%の値引きを出し、Anthropic から乗り換えさせている。Rippling ではコーディング用途の OpenAI の比率が16%から52%に上がった。エンタープライズ契約の実勢価格は、公開単価の比較では見積もれなくなった。

**詳細**: The Decoder（10/25）が The Information の報道として伝えた。The Information の本文は読めておらず、OpenAI・Anthropic のコメントもない。

- Rippling: CEO の Parker Conrad 氏によると、コーディング用途の比率は OpenAI が16%→52%、Anthropic が57%→18%に入れ替わった
- Replit: 年$1億超の契約に30%超の値引きを提示されて乗り換えた。CEO の Amjad Masad 氏は TechCrunch Disrupt で、既定モデルを ChatGPT に切り替えたが Anthropic モデルも引き続き使えると話した
- DataCamp: CEO の Jonathan Cornelissen 氏によると、OpenAI の価格でコストが80〜90%下がった
- 米地銀（資産$70億超）: ChatGPT の席数を500人に倍増させても追加料金はなく、1人あたり通常$20以上のところを$7未満で払っている
- 背景: 値引きには利益を削って取る分と、Sol・Luna 系列の値下げ（モデルと基盤の効率化）による分がある。The Information は 9/28 にも、Anthropic は契約トークンを使い切ると約15%の割引を打ち切るが、OpenAI は翌月末まで猶予すると報じていた

- https://the-decoder.com/openai-offers-discounts-up-to-90-percent-to-poach-anthropics-biggest-customers/
- https://techcrunch.com/2026/10/20/replit-is-no-longer-working-with-anthropic-ceo-says/

### 2. [新機能] Google が Gemini Notebook を Gemini アプリの接続アプリとして既定オンで出した — Gemini と Gemini Notebook の両方が有効な組織では、チャットからノートブックの作成・削除までできる

**要点**: Google が 10/23 に、Gemini アプリのチャットから `@Gemini Notebook` でノートブックとソースを作成・編集・削除できるようにした。管理者側は既定でオンで、Gemini と Gemini Notebook の両方を許可した OU では、設定を変えなくてもチャットからノートブックを書き換えられる状態になる。

**詳細**:

- できる操作: ノートブックの作成・編集・削除、ソースの追加・更新・削除、一覧、ノートブックの内容を使った回答。`@` を付けなくても Gemini が必要と判断すれば呼び出す
- 対象: すべての Workspace 顧客、Workspace Individual、個人アカウント。Rapid / Scheduled Release とも提供済み
- 管理: 接続アプリは既定でオン。Gemini と Gemini Notebook のアクセス設定の両方がオンのグループ・OU だけで使える
- 利用者側: 既定オン（欧州経済領域は既定オフ）。Gemini アプリの「設定 > 接続アプリ」で切り替える

- https://workspaceupdates.googleblog.com/2026/10/take-actions-on-your-notebooks-from-Gemini-Notebook-directly-in-the-Gemini-app.html

### 3. [新機能] Stably AI が Orca `v1.4.240` で、承認が要る Codex の MCP ツール呼び出しを承認カードで止めるようにした — Codex の MCP 操作を Orca の画面上で許可・拒否できる

**要点**: Stably AI が 10/25 に Orca `v1.4.240` を出し、Codex の MCP ツールで承認が必要なものに承認カードを出すようにした。完了した Codex サブエージェントが「Working」のまま残る表示も直り、並列実行中のエージェントの状態を画面どおりに読めるようになった。

**詳細**:

- エージェント連携
  - Codex: 承認が要る MCP ツールに承認カードを出す。完了したサブエージェントを Working と表示しない。`/side` の会話中もメインタスクを表示し続ける
  - Claude: Orca の外で進んだターンもチャットに出し、再接続後に保持していたメッセージを戻す。クラッシュから復旧したとき、送信済みのメッセージを未配信と誤表示しない
- ワークフロー: `orca ports` で worktree の開発サーバーのポートを調べられる。開発用 worktree の古い依存インストールとビルド出力を回収でき、クイックコマンドを40件より多く保存できる
- リモート: 遅い接続でウェイクの応答が欠けても切断しない。SSH 端末はサインインを待ち、新しい分割はペアリング済みサーバー上に作る
- 取り消し: 端末のファイルリンクをクリックしたワークスペースで開く変更は元に戻した

- https://github.com/stablyai/orca/releases

## カテゴリ別まとめ

### Claude / Anthropic

- [新機能] **サブエージェント統合の手引きと移行キット** — Anthropic が 10/22 に、複数のサブエージェントに仕事を分ける構成を、必要なときにスキルとツールを読み込む1本のループにまとめる手引きを公開し、Claude Code 用の移行キット `single-agent-loop-kit`（Apache-2.0）を GitHub に置いた。Opus 4.5 以降は1本のループで複雑な計画をこなせ、分割すると遅くなるうえ引き継ぎで文脈が抜けるとしている
  - 実測と目安: ある顧客の比較で単一ループはマルチエージェント構成の約2倍速かった。ツール定義が30〜50個を超えるとツールの選び方が崩れ、推奨構成はシステムプロンプト1本・薄いデータツール4〜5個・出力のガードレール
  - Claude Code: 新しいモデル向けのシステムプロンプトを80%超削り、スキルとツールを必要なときだけ読み込む方式に移した
  - サブエージェントを残す条件: 1本では文脈が膨らんで性能が測れるほど落ちるとき、使い捨ての文脈で並列に走らせるとき、ツール選択や指示の矛盾で迷うとき
  - キット: スキルとして入れるとサブエージェントごとに「統合・合併・ツールとして呼ぶ・残す」を提案し、変更のたびに評価を回す。保守せず issue・PR も受け付けない参照実装で、一部の手順は実モデルで未検証
  - https://claude.com/resources/articles/building-agents-when-to-fold-subagents-into-your-main-agent-loop
  - https://github.com/anthropics/single-agent-loop-kit
- [動向] **Elvis Presley の権利者が Anthropic を提訴** — Authentic Brands Group 系の権利者が 10/23 に、Claude が Presley の楽曲274曲を無断で学習し、歌詞を丸ごと出力できると訴えた。1曲$15万、計約$4,100万の法定損害賠償を求めており、Anthropic はコメントしていない。原告の名義（ABE EPE LLC／ABG EPE IP LLC）と事件番号は報道ごとに異なる
  - https://www.nme.com/news/music/elvis-presley-rightsholders-sue-anthropic-copyright-infringement-274-songs-3974178
- [据え置き] **Claude Code・Platform・ニュース一覧の定点** — Claude Code の changelog の最上位は `2.1.310` のままで、npm も `{stable: 2.1.308, latest: 2.1.310, next: 2.1.310}` から動いていない。Platform release notes の項目数とモデル退役ページ（Active 15件・Deprecation history 最新 9/30）も前回と同じで、`/news`（10/22）・`/research`（10/23）・`claude.com/resources/articles`（10/23 Claude Duet）・`support.claude.com`（10/21）の最上位も変わっていない

### GitHub Copilot / Microsoft 365 Copilot

- [仕様] **Copilot 構成の見直しページ** — （`optimize-copilot-configuration-settings`・`ms.date` 10/22）管理者は、展開時に確認すべき Copilot の設定を11領域の一覧で参照できるようになった。ページ自身は「すべてを有効にする推奨ではない」と明記している
  - 11領域: Frontier、従量課金、Microsoft 365 Apps の更新チャネル、Web 検索、タスクバーへのピン留め、Teams 会議の文字起こし、Copilot Analytics、フィードバックとログ、サブプロセッサとしての AI プロバイダー、Copilot コネクタ、エージェントのアクセスと展開
  - 関連の改訂: 管理センターの設定ページ（`configure-copilot-admin-center`・`ms.date` 10/23）が4区分の表に書き直されたが、新しい設定項目は無い
  - https://learn.microsoft.com/en-us/microsoft-365/copilot/optimize-copilot-configuration-settings
- [据え置き] **Copilot CLI・Release Notes・ブログ各種** — GitHub changelog の Copilot ラベルは 10/23 の `totals_by_client` が最上位のままで、Copilot CLI も Latest `v1.0.103`・pre-release `v1.0.104-3` から動いていない。M365 Copilot Release Notes の先頭は October 06, 2026 のままで隔週の更新見込みを過ぎて20日になり、Roadmap と Message Center も 10/23 23:10Z から動いていない。Copilot ブログ・TC 各ブログ・Cowork・拡張機能・Purview の What's New にも改訂はない

### Copilot Studio / Power Platform

- [仕様] **Customer Conversation ハーネスの接続エージェント** — （`ms.date` 10/23）開発者が Foundry のエージェントを接続エージェントとして加えるには、Foundry 側で Activity プロトコルのエンドポイントを有効にしておく必要があると一次で明文化された。新規作成した Foundry エージェントが既定で公開するのは Responses と A2A だけで、Activity が無いと実行時に 400 エラーで失敗する
  - 有効化の方法: Foundry エージェントを M365 / Teams に発行するか、REST API・Python SDK で構成する
  - 制約: 接続エージェントからは、プライマリエージェントのツール・トピック・イベント・サブエージェント・変数を参照できない
  - https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-experience/add-agent-connected-customer-conversation
- [据え置き] **What's New / モデル表 / 課金 / 非推奨一覧 / Released Versions** — Copilot Studio What's New は `ms.date` 10/5 のままで、Customer Conversation ハーネスはまだ載っていない。モデル表3本・課金6本・PPAC の容量管理2本・非推奨一覧・ガイダンスハブにも改訂はなく、Released Versions は 2026.6.3 のまま117日動いていない。Copilot Studio・Power Platform の各ブログにも新しい記事はない

### OpenAI / Codex / ChatGPT

- [据え置き] **Codex CLI・API・ChatGPT の定点** — Codex CLI の安定版は `0.164.0`（10/23）、pre-release は `0.165.0-alpha.1` のままである。changelog RSS（191件・最上位 10/23）、API changelog（10/22 Decisions API GA）、deprecations（最上位 10/14 の GPT-4 系）、community Announcements、`alignment.openai.com` にも新規はなく、ChatGPT release notes の最上位も 10/20 の Locked chats のまま
- [据え置き] **料金・廃止ページ** — Anthropic・OpenAI・Google・xAI の料金と廃止ページに変化はなく、Claude Haiku 4.5 は退役下限日の11日後も Active である。Gemini の deprecations は 10/22 更新のまま、xAI の単価も 10-25 と同じだった
  - https://developers.openai.com/api/docs/deprecations

### Google

- **Gemini Notebook の接続アプリ化**（ハイライト2参照）
- [予定] **AI Studio の Managed Agents ハブ** — TestingCatalog が 10/25 に、Google が AI Studio に Managed Agents のハブを準備していると報じた。未発表で、提供日は示されていない
  - https://www.testingcatalog.com/google-ai-studio-prepares-new-managed-agents-hub/
- [据え置き] **Gemini API / Gemini アプリ / The Keyword** — Gemini API changelog の最上位は 10/13 の Gemini 4 Argon GA、アプリの release notes も 2026.10.13 のままで、The Keyword の AI RSS も 10/21 から動いていない

### その他モデル / 開発ツール

- **Orca `v1.4.240`**（ハイライト3参照）
- [据え置き] **TypeSafe・Cursor・xAI・Devin・MCP・HF・Obsidian・Apple の定点** — TypeSafe AI は `/blog/` が8件のままで、`jev-latest` / `jev-preview` とも `jev-1.14.0` を指している。Cursor の changelog（10/16）とフォーラム（10/12）、xAI release notes、Devin（October 21）、MCP blog（8/22）はいずれも前回から動いていない。HF の `moonshotai` の最新は 6/13 の `Kimi-K3` で、Kimi K3.1 Pro の重み（11/4 までに公開予定）はまだ無い。Obsidian は 10/22 の 1.15.0 / 1.14.5、Apple Developer News も AI 関連の新規はない

### 市場・企業

- [据え置き] **買収協議と調査公表** — Amazon × Decart、Nvidia × Reflection AI の買収協議に続報はなく、IDC Japan・MM総研・NRC の新規公表も検知されなかった

## 直近の注目予定

- **10月中**: Dataverse の Basic User ロールからカスタムコネクタ定義の読み取り権限が外れる（MC1520706）
- **10月下旬**: Copilot Code が Frontier で展開を始める（MC1519871）
- **10月下旬〜11月中旬**: Researcher の Critique / Council が退役（MC1515927、Act by 11/14）
- **10/26（本日）**: Copilot Business / Enterprise の新機能の既定ポリシーの適用が完了 ／ Outlook の Copilot Prioritize の退役が始まる（MC1519861） ／ Copilot Studio の Copilot Chat エージェント強化が GA（MC1518233）
- **10/27〜29**: PPCC 2026（ラスベガス）。10/28 に Dataverse / Work IQ / Agent 365 の Innovation Session
- **10/30**: Copilot Connectors ページが Allowed agent types の設定に従う（MC1454973） ／ ChatGPT Pro 200 の Work / Codex 利用枠が変更（二次・内容は割れている） ／ Gmail Live の Workspace への順次展開が完了（最大15日）
- **10/31**: MCP サーバー認定の旧申請経路が終了 ／ DeepSeek の Search・Fetch API の無料提供が終了 ／ OpenAI の既存 Evals が読み取り専用に
- **11/1**: AI Builder の容量アドオンの販売が終了（Partner Center） ／ Codex の28日間「改善かリセット」の終了（二次）
- **11/2**: xAI `grok-imagine-image-quality` が退役 ／ Meet の63言語音声翻訳が Scheduled Release へ展開開始
- **11/4**: Entra で一般ユーザーのブループリント作成が既定オン（MC1506733） ／ Kimi K3.1 Pro の重み公開の約束期限（二次）
- **11/5 ごろ**: Anthropic のゲスト研究者（生命科学）の応募受付が終了（締切日は明記なし）
- **11/12**: Copilot Studio の GPT-4.1 / GPT-5 系が退役（MC1506318） ／ Anthropic Usage Policy 改定版が発効 ／ OpenAI → Cursor のモデル供給停止予定（一次未読）
- **11月**: Power Pages の AI コーディング用プラグインと生成ページの追加モデルが GA（Roadmap 577900 / 576285） ／ Power Pages の ID プロバイダー統制がプレビュー（Roadmap 578062）
- **11月中旬**: Viva Insights の GitHub Copilot 指標が既定オン（MC1523085、12月中旬に完了） ／ 会議メモの保存先が開催者の OneDrive に（MC1523076） ／ Copilot Analytics でエージェントデータのエクスポートが可能に（MC1288531）
- **11月中旬〜下旬**: Teams モバイルの検索に Copilot（MC1523087）
- **11/15**: Dataverse for Teams 環境とアンマネージド開発者環境の新規作成が停止
- **11/16**: GitHub Copilot が Claude Opus 4.8・Opus 5・GPT-5.6 Terra を廃止 ／ Teams の旧 GitHub アプリが退役
- **11/17**: Work IQ の業務アプリ統制がパブリックプレビュー（MC1518036） ／ Gems が Gemini アプリの設定パネルへ移動 ／ Gemini API の TTS・Live プレビュー5種が停止（最短日）
- **11/17〜20**: Microsoft Ignite
- **11/24 以降**: `claude-opus-4-5-20251101` の暫定退役日（確定日ではない）
- **11/30**: `claude-sonnet-4-5-20250929` が Claude API から退役 ／ OpenAI の Evals・`v1/prompts`・Agent Builder が停止 ／ Gemini 4 Argon の導入価格が終了 ／ Azure DevOps コネクタの旧接続が認証不可に（MC1508508） ／ App Builder と vibe.powerapps.com が退役
- **12/1**: M365 Copilot の前提サブスク不要オファー開始 ／ Copilot Business の従量課金が既定オン ／ Gemini 4 Argon の単価が $4/$20 に倍増
- **12月**: 生成ページへの Power Platform コネクタのデータ取り込みが GA（Roadmap 576283）
- **12/14**: claude.ai/design の単体サイトが閉鎖
- **12/15**: アンマネージド開発者環境が停止
- **12/31**: Claude Security の無償クレジット（月 $25,000×2か月）の対象期間が終了
- **2027-01-06**: OpenAI `tts-1` / `tts-1-hd` / `gpt-4o-mini-tts` 2版が停止
- **2027年1月**: Power Pages の ID プロバイダー統制が GA（Roadmap 578062） ／ Copilot Studio の Teams アプリで編集ができなくなる（MC1511056）
- **2027-01-14**: OpenAI の GPT-4o・GPT-4o mini・GPT-4.1・GPT-4.1 mini が API から削除（→ `gpt-6-luna`）
- **2027-01-15**: アンマネージド開発者環境の削除開始 ／ Claude Code Review の Enterprise 向けクレジット請求期限
- **2027-03-01 以降**: Gems 廃止（Business / Enterprise）
- **2027年3月末**: Outlook の Copilot Prioritize の削除が完了（MC1519861） ／ SharePoint / OneDrive の `.agent` 形式エージェントが動かなくなる（MC1511052）
- **2027-04-01**: OpenAI `gpt-5.1` / `gpt-5.3-codex` / `gpt-5.4-nano` が停止

## 改善メモ

- 新規提案: 3ソースとも無し
- 障害の変化: industry が Apollo（`www.apollo.com`）をゲートウェイ拒否として新規記録した。Master は月曜の週次復旧チェックで、`feeds.feedburner.com/GoogleAppsUpdates` を「curl 000」からゲートウェイ拒否（exit 56）へ記録し直した（復旧 0件）
- 継続提案: Master は B-036・B-037・B-043 を見送り候補に挙げた ／ industry は継続5件（最多 B-040 セキュリティ開示の定点、10回）、見送り候補 B-007・B-023 ／ Copilot は月曜の定例で docset 全件突合（目次2本・638ページ、10/16 以降の改訂233本の大半は一括再ビルド）を実施した
- ソース間の差分・矛盾:
  - Orca `v1.4.240`（Master）と Gemini Notebook（Master）、OpenAI の値引き報道と Anthropic のサブエージェント手引き（industry）がそれぞれハイライト候補だった。選定基準の2・3に当たる3件をハイライトに採り、手引きはガイダンスで当日の挙動変化を伴わないためカテゴリに置いた
  - ChatGPT Pro 200 の 10/30 の枠変更は、引き続き Master が「半減（二次）」、industry が「Plus 比10倍」と書いており、二次情報のまま割れている
