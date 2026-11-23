# AI News Daily Summary — 2026-11-24

Anthropic が Claude Opus 4.5 の API 退役日を 2027-01-22 に決め、暫定の下限日が確定した期日に変わった。Power Platform 管理センター（PPAC）のデータエクスポートは 12/1 からインベントリを出力しなくなる。Anthropic は保持必須の最上位モデルをプロンプトを残さずに使える Enterprise Frontier Safeguards（EFS）をベータで公開し、Copilot の Fable 5 系の ZDR 例外が 12/31 に終わったあとの道筋が具体的になった。

## 今日のハイライト

### 1. [廃止] Anthropic が Claude Opus 4.5 の API 退役日を 2027-01-22 に決めた — 「11/24 以降のいつか」という下限日が、残り59日の確定した期日に変わった

**要点**: Anthropic が 11/23、`claude-opus-4-5-20251101` と日付なしの `claude-opus-4-5` を 2027-01-22 に Claude API から退役させると告知した。暫定の下限日は確定した停止日に変わり、Opus 4.5 を名指しで呼ぶコードは59日以内に `claude-opus-5-5` へ移す必要がある。

**詳細**: リリースノートと退役一覧の「Deprecation history」節（2026-11-23）に載った。告知から退役までの60日は、Anthropic が明記する最低通知期間と同じである（Master・industry）。
- 推奨移行先: `claude-opus-5-5`。手順は Opus 5.5 移行ガイドの「Migrating from Claude Opus 4.5 or earlier」節にある
- Status 表: `claude-opus-4-5-20251101` が Active から Deprecated に移り、Active は17件から16件になった
- 他プラットフォーム: Bedrock / Vertex AI などの退役日は Model deprecations ページで別に示すとしている
- 次の下限日: Opus 4.6 が「Not sooner than February 5, 2027」、Sonnet 4.6 が「Not sooner than February 17, 2027」（どちらも確定日ではない）

出典:
- https://platform.claude.com/docs/en/about-claude/model-deprecations
- https://platform.claude.com/docs/en/release-notes/overview#claude-opus-4-5-deprecation

### 2. [廃止+破壊的変更] PPAC のデータエクスポートが非推奨になり、12/1 からインベントリを出力しなくなる — データレイクの在庫集計は、残り7日で Inventory API へ移さないと更新が止まる

**要点**: Microsoft が PPAC のデータエクスポート（プレビュー）を非推奨にし、段階的に退役させる。第1段として 12/1 以降はインベントリのデータが出力されない。使用状況と環境のエクスポートは当面続くが、データレイクのインベントリを前提にした集計は Power Platform inventory API へ切り替える必要がある。

**詳細**: Power Platform の非推奨一覧（`important-changes-coming`）が 11/23 19:03Z に改訂され（`a406dde7`・`ms.date` 11/23）、先頭に節「Deprecation of data export (preview)」が加わった。見出しは106本から107本になった（Copilot）。
- 影響: 12/1 以降、インベントリは出力されない。出力済みのデータはデータレイクに残る
- 対象外: 使用状況（usage）と環境（environment）のエクスポートは今と同じく動く。これらも後日、事前告知のうえで退役する
- 移行先: Power Platform inventory API。Learn は移行前の比較ページとフィールド対応表を案内している
- Message Center の告知は 11/24 時点で見つかっていない（WebSearch でも該当なし）

出典:
- https://learn.microsoft.com/en-us/power-platform/important-changes-coming
- https://learn.microsoft.com/en-us/power-platform/admin/self-service-analytics

### 3. [新機能+仕様] Anthropic が Enterprise Frontier Safeguards（EFS）をベータで公開した — 30日保持が必須だった Fable / Mythos 系を、プロンプトを Anthropic に残さずに使える契約形態ができた

**要点**: Anthropic が 11/23、保持必須の Covered Models（Fable 5.x / Mythos 5.x など）を ZDR 相当で使える EFS をベータで出した。プロンプトと応答は暗号化して顧客のクラウドの bucket に置く。GitHub Copilot が 12/31 の ZDR 例外終了後に求める EFS の中身が、これで具体的になった。

**詳細**: リリースノートと製品ブログ（11/23）に載った。対象顧客の条件は公開されておらず、対象の顧客に案内が届く形である（Master・industry）。
- 提供先: Claude Platform、Claude Platform on AWS、Claude Models on Google Cloud（Anthropic managed）。製品ブログは Amazon Bedrock も挙げ、Microsoft Foundry は「近日」としている
- 料金: Anthropic は EFS に課金せず、モデルの挙動・API 料金・レート制限も変わらない。bucket の読み書きと転送はクラウド事業者が通常どおり請求する
- 保存: Sealed Safety Data（プロンプト・応答・推論の暗号化した写し）を自社の S3 / GCS に送る。自社チームも中身を読めず、Anthropic の人によるレビューは常にオフである
- 適用範囲: Claude Platform では workspace 単位で、その workspace の全モデルへのリクエストに掛かる。code execution のコンテナ、Files API、Batch API の結果、Managed Agents のセッションは対象外。Anthropic 管理のストレージを使う workspace も対象外
- Webhook: organization webhooks（beta）に `external_storage.failed` と `external_storage.recovered` が加わり、顧客の bucket が日次の検査に落ちたとき・戻ったときに届く
- 導入経路: Accenture / Deloitte / KPMG / PwC 経由でも導入できる

出典:
- https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/overview
- https://claude.com/resources/articles/zero-data-retention-with-enterprise-frontier-safeguards
- https://platform.claude.com/docs/en/release-notes/overview#enterprise-frontier-safeguards

## カテゴリ別まとめ

### Anthropic / Claude

- **Claude Opus 4.5 の退役日の確定**（ハイライト1参照）
- **Enterprise Frontier Safeguards のベータ公開**（ハイライト3参照）
- [版更新] **Claude Code `2.1.331`** — Anthropic が npm の `next` タグを `2.1.331`（11/23）に進めた。changelog は `2.1.330`（11/20）のままで変更内容はまだ公開されておらず、`stable` は `2.1.323`、`latest` は `2.1.330` のままである（Master）
  - https://registry.npmjs.org/@anthropic-ai/claude-code
- [据え置き] **Anthropic のその他の一次** — `support.claude.com` の release notes（11/20 Claude Mobile）、`/news`（11/20）、`/research`（11/17）は動いていない。`claude.com/resources/articles` の新着は EFS の記事1本だけで、Claude Code の changelog には課金付き分類フォールバックの削除もまだ書かれていない（Master・industry）

### OpenAI / Codex / ChatGPT

- [新機能] **ChatGPT のチャット向け GPT-6.2** — OpenAI が 11/23、チャットタブ向けに調整した GPT-6.2（GPT-6.2 Sol の1版）を Plus / Pro / Business / Enterprise に順次展開し始めた。Work と Codex のモデルは変わらず、Enterprise は管理者の設定に従う。旧モデルの扱いと Free への提供は書かれていない（Master）
  - 社内評価（GPT-6 比）: 画像理解 47.4% → 71.7%、難しい指示への追従 62.5% → 78.1%、BrowseComp（最高設定）54.4% → 64.5%
  - https://help.openai.com/en/articles/6825453-chatgpt-release-notes
- [版更新] **Codex `0.172.0-alpha.2.1`** — OpenAI が pre-release（11/23）を出したが、本文は「Release」だけで変更点の記載は無い。安定版は `0.171.0` のままである（Master）
  - https://github.com/openai/codex/releases
- [据え置き] **OpenAI のその他の一次** — API changelog（11/19）、deprecations（11/18）、`openai.com/news`（11/22）、community Announcements（11/20）、`learn.chatgpt.com` changelog（11/20）、Deployment Safety Hub（11/17）、misalignment reports（First posted 最新 11/18）は動いていない。料金ページの GPT-5.6 Sol の期間限定価格は「until November 30, 2026」のままである（Master・industry）

### GitHub Copilot / GitHub

- [据え置き] **Copilot CLI と GitHub changelog** — Copilot CLI は安定版 `v1.0.114`・pre-release `v1.0.115-7` のままで、`github.blog/changelog` の Copilot ラベルも 11/18 から動いていない。11/23 の changelog 2件（Slack の secret scanning の誤検知削減、コードカバレッジのアップロード形式の警告）は Copilot と関係しない（Master・industry）
  - https://github.com/github/copilot-cli/releases

### Copilot Studio / Power Platform

- **PPAC データエクスポートの非推奨**（ハイライト2参照）
- [新機能] **Copilot Agent Kit 11月版** — Power CAT が 11/23 に `CopilotAgentKit-November2026` を公開し、PowerShield を Request Center に改めた。メーカーは Copilot Credits の追加やテナントの余剰クレジットの利用を申請でき、管理者の承認がそのまま Power Platform に反映される。非互換の記載は無い（Copilot）
  - Agent Inventory: 統計の「Missing owner」が「Web search enabled」に置き換わった
  - Conversation Analyzer: Conversations タブで会話 ID から会話を探して分析・デバッグできるようになった
  - Agent Value Summary: グラフとカードから、絞り込み済みのエージェント一覧（CSV 出力可）へ掘り下げられるようになった
  - Agent Debugger: 推論ステップが 0 秒と表示される不具合を直し、Latency タブにオーケストレーターの推論時間を出すようになった
  - Microsoft Copilot ハーネス: ハーネス名を「GitHub Copilot」から「Microsoft Copilot」へ改め、標準エージェントの移行可否・移行後の比較・ハーネス適合の助言を加えた。Work IQ の表記を GA に直した
  - https://github.com/microsoft/Power-CAT-Copilot-Studio-Kit/releases
- [据え置き] **Copilot Studio と Power Platform の一次** — Copilot Studio What's New（`1e58d09d`）、ハーネスと課金のページ、レート表、PPAC 容量管理、ガイダンスハブ、モデル表、メモリのページは前日から変わっていない。Released Versions も 2026.6.3 のままで、Copilot・Power Platform・TC Copilot Studio の各ブログに新しい記事は無い（Copilot）
  - https://learn.microsoft.com/en-us/microsoft-copilot-studio/whats-new

### Microsoft 365 Copilot

- [観測] **Roadmap の総項目数がさらに3件減少** — Release Communications の API と RSS は 2,389 項目を返し、前日の 2,392 から3件減った。最終 `modified` は 11/21 02:55Z のままで新しいバッチは無く、Copilot Studio タグは33件で増減はない。Message Center も 11/20 23:37Z（MC1562279）の後に新しい通知が出ていない（Copilot）
  - https://www.microsoft.com/releasecommunications/api/v1/m365
- [据え置き] **Release Notes・Purview・Cowork・Partner Center** — M365 Copilot Release Notes（先頭 November 17）、Purview・拡張機能・Cowork の What's New、Cowork のモデル・管理者統制、Partner Center 11月ページは前日のまま変化がない。M365 Developer Blog と TC の Copilot / Agent 365 / SharePoint の各 board にも新しい記事は無い（Copilot）
  - https://learn.microsoft.com/en-us/microsoft-365/copilot/release-notes

### Google

- [新機能] **Google Chat のアプリ向けの表と見出し** — Google が 11/23、Google Chat のアプリとエージェントが表と見出しつきのメッセージを送れるようにした。開発者は Chat API で Markdown を使って書き、人が使う作成欄では使えない（Master）
  - https://workspaceupdates.googleblog.com/2026/11/make-messages-in-google-chat-from-apps-and-agents-easier-to-read-with-tables-and-headings.html
- [観測] **Gemini API changelog に届かない** — Gemini API changelog は転送先 `aistudio.google.com` に届かないままで、WebSearch でも 10/27 より新しい項目を確かめられない。Gemini アプリ（11/19）は動いていない（Master・B-088）

### 開発ツール・エージェント

- [新機能] **Z.ai GLM-5.4** — Z.ai が、GLM-5 をもとに27〜54層を2回通すループ型トランスフォーマー GLM-5.4（7,500億パラメーター・画像入力対応）を GLM Coding Plan・ZCode・Z.ai Chat で使えるようにした。API と重みの公開は後日で、料金とベンチマークは出ていない。Hugging Face の `zai-org` にも新しいリポジトリは無い（Master・industry）
  - 速度: 閑散時に毎秒最大200トークン、負荷時は70〜80トークン（The Decoder・11/23）
  - https://the-decoder.com/z-ai-follows-openai-into-loop-transformer-territory-with-its-new-750b-flagship-model/
- [新機能] **Orca `v1.4.271` / `v1.4.272`** — Stably AI が 11/22〜23 に2版を出し、Bots で Qwen Code が使えるようになり、使用制限に当たったあとも作業を続けるのが既定になった（Master）
  - `v1.4.271`: Bots を複数のペアリング済みコンピュータのグループに入れられ、複数の GitHub アカウントを連携できる。再起動や使用制限のあと Bots が途中で止まる既知の問題を記載した
  - `v1.4.272`: 中断した会話の再開を改善し、`/btw` / `/side` で下書きをサイドチャットにできる（対応エージェントのみ）。1Password などの拡張を SSH ワークスペースでも使える
  - https://github.com/stablyai/orca/releases
- [据え置き] **Cursor・Devin・xAI・TypeSafe AI・MCP・Obsidian** — Cursor の changelog（11/6）とフォーラム（10/12）、Devin（11/20）、xAI（11/19・grok-4.7）、TypeSafe AI（9件）、MCP blog（11/11）、Obsidian（1.15.1）は動いていない。Hugging Face の8 org にも新しいリポジトリは無い（Master・industry）

### 市場・企業

- [動向] **Amazon × Decart が決着** — Bloomberg・Calcalist（11/23）によると、Amazon は Decart の Optimization Stack の技術を取得し、共同創業者3人と研究者・技術者を迎える契約を結んだ。金額は報道ベースで約 $75億、Decart の AI モデルは対象外で、Trainium・Inferentia の性能向上に使う。5年間の業績目標に連動し、規制当局の承認が条件である（industry）
  - https://www.geekwire.com/2026/amazon-is-buying-decarts-ai-chip-software-for-a-reported-7-5b-and-bringing-its-founders-aboard/
- [動向] **Nvidia が Jensen Huang を CEO に戻した** — The Decoder（11/23）によると、Nvidia の取締役会は全会一致で Huang を社長兼 CEO・取締役に即日復帰させ、株価は30%超上がった。11/12 の辞任後は CFO の Colette Kress が経営していた。独立委員会の調査は続き、Nvidia は輸出管理の監督委員会を作る（industry）
  - https://the-decoder.com/nvidia-tried-life-without-jensen-huang-and-it-lasted-about-two-weeks/
- [動向] **Anthropic が xAI の計算資源を月約 $31億で借りている** — The Decoder（11/23）が伝えた NYT の報道によると、Anthropic は xAI の最大の計算資源顧客で、Google も月約 $8億を払っている。どちらの契約も90日前の通知で解約でき、xAI は Grok Imagine の60人のチームを解散する（industry）
  - https://the-decoder.com/anthropics-appetite-for-compute-is-pushing-xai-toward-a-rent-over-build-strategy/
- [動向] **Sierra がシリーズFで $17.5億を調達** — Sierra が 11/23、Greenoaks と Lightspeed が主導するシリーズF（評価額 $300億）を発表した。5月のシリーズE（約 $158億）から半年で評価額が約2倍になり、ARR は 10/30 に $4億を超えた。`sierra.ai` には届かず、数値は報道の突き合わせで確認した（industry）
  - https://www.cmswire.com/contact-center/sierra-hits-30b-valuation-on-175b-series-f/
- [動向] **CrowdStrike が Zscaler を約 $439億で買収** — CrowdStrike が 11/23 の SEC 提出書類（8-K）で、Zscaler を全額株式交換（Zscaler 1株に CrowdStrike 1.135株）で買うと発表した。完了時期と規制審査の条件は確認できていない（industry）
  - https://www.sec.gov/Archives/edgar/data/0001535527/000153552726000035/crwd-20261123xex991.htm
- [据え置き] **Nvidia × Inception、Nvidia × Reflection AI** — 2件の買収協議に続報はない。MM総研・IDC Japan の新しい公表も見つからなかった（industry）

## 直近の注目予定

- **11月下旬**: Copilot ライセンスの無い利用者の検索画面が新しくなる（MC1562275）。Copilot Code のローカル Sandbox が既定でオンになる（MC1519871）
- **11月中**: GitHub の cloud sandbox の課金が始まる（日付は明記なし）
- **11/29**: OpenAI が Daybreak Blue のセッションデータの学習利用を始める（二次）
- **11/30**: `claude-sonnet-4-5-20250929` が退役し、Opus 4.8 の fast mode が削除される。OpenAI の `/v1/prompts`・Evals・Agent Builder が停止する。Power Automate デザイナーの Copilot と Copilot Studio の Mistral Medium 3.5 が退役する。GPT-5.6 Sol の期間限定価格と Gemini 4 Argon・Carbon の導入価格が終わる
- **12/1**: PPAC のデータエクスポートがインベントリを出力しなくなる。OpenAI `gpt-image-1-mini` / `gpt-image-1.5` / `chatgpt-image-latest` が停止する。Gemini 4 Argon・Carbon の単価が $4/$20 に倍増する。Copilot Studio のワークフローの Code ノードが GA になる
- **12/2**: GitHub が公開リポジトリの `pull_request_target` を既定でブロックする。Power Platform のプロンプトから Anthropic・Grok・旧 GPT 系が退役する（MC1536101）
- **12/3**: Agent ノードからのファイル生成が GA になる（MC1561859）
- **12月上旬**: Teams のチャネル単位の Copilot がパブリックプレビューに入る（MC1562277）
- **12/8**: GitHub が活動の無いリポジトリの Dependabot アラートを停止し、ARM32 ジョブのサポートを終える。Dataverse のエージェントユーザーが GA、M365 Copilot in Power BI が既定でオンになる
- **12/9**: EU / EFTA / UK で Claude モデルが既定で有効になる（MC1546438）
- **12/11**: OpenAI `gpt-5` 系 / `o3` / `o3-pro` が停止する。ChatGPT の Advanced / Standard 音声モードが退役する（二次）
- **12/14**: Copilot から Claude Fable 5 / Haiku 4.5 / Gemini 3.8 Flash / Gemini 4 Argon / Grok 4.6 / Kimi K3 が廃止される。claude.ai/design の単体サイトが閉鎖する
- **12/15**: アンマネージドの開発者環境の削除が始まる（MC1515303）
- **12月中旬**: Copilot デスクトップアプリと Edge の同期が展開される（MC1562269）。Chat と Office のモデルの従量課金が GA になる（MC1557754）
- **12月中**: ChatGPT と Codex の利用枠が Plus・Pro・Business で1つの予算に統合される（二次）
- **12/17**: Copilot Studio のワークフローのサービスプリンシパル認証が GA になる（MC1557509）
- **12/18**: Copilot から MAI-Code-1.1-Flash が廃止される
- **12/31**: Copilot の Fable 5 系の ZDR 例外が終わる（以後は EFS が必要）。Claude Security の無償クレジットの対象期間が終わる
- **2027-01-01**: Anthropic の新しい開示期限（高・重大度30日）が、この日以降の報告に適用される
- **2027-01-03**: Copilot デスクトップアプリのアプリ内ブラウズの既定オンに備える期限（MC1560922）
- **2027-01-06**: OpenAI `tts-1` / `tts-1-hd` / `gpt-4o-mini-tts` が停止し、セルフサービスの fine-tuning ジョブ作成が制限される
- **2027-01-11**: OpenAI の EU データレジデンシーで GPT-5.2 / 5.4 / 5.4 mini の `fast` / `priority` 処理が停止する
- **2027-01-14**: OpenAI `gpt-4o` / `gpt-4o-mini` / `gpt-4.1` / `gpt-4.1-mini` が停止する
- **2027-01-15**: アンマネージドの開発者環境が完全に削除される。Claude Code Review の Enterprise 向けクレジットの請求期限
- **2027-01-20**: OpenAI `gpt-realtime` / `gpt-audio` 系が停止する
- **2027-01-22**: `claude-opus-4-5-20251101` / `claude-opus-4-5` が Claude API から退役する
- **2027-01-30**: ChatGPT Classic（旧デスクトップアプリ）が終了する（二次）
- **2027-02-01**: OpenAI `gpt-5.5-cyber-preview` が停止する
- **2027年2月**: VS Code の Copilot から Local harness が削除される
- **2027-02-10**: OpenAI `gpt-image-2` が停止する。Claude Meetings の成果物の無料期間が終わる
- **2027-02-15**: Copilot Studio の Claude Opus 4.8・Opus 5・Sonnet 4.6・Sonnet 5 が退役する
- **2027-03-01**: GPT-6.2 Astra・Sol の Ultrafast が Standard の3倍から6倍になる

## 改善メモ

- Master: 新規提案・障害の変化なし。継続提案の最多は B-088（Gemini API changelog の URL 差し替え、21回目）。B-086（Claude Platform release notes の登録）に、Opus 4.5 退役告知と EFS を RSS で検出した実例を追記した
- Copilot: 新規提案・障害の変化なし。継続提案 5件（最多: B-080 Cowork の Learn URL の移設、26回目）
- industry: `sierra.ai` がゲートウェイ拒否（新規）。継続提案 7件（最多: B-048 Gemini 一次 URL、22回目）
- ソース間の差: GLM-5.4 を Master は `[予定]`（API と重みは後日）、industry は `[新機能]`（GLM Coding Plan で今日から使える）とした。本サマリーは今日使える提供面があるため `[新機能]` を採った
- ソース間の差: Copilot は Released Versions を `[版更新]` としたが、2026.6.3 のまま新しいビルドが無いため本サマリーは据え置きに寄せた
- 前日の注目予定にあった「11/24 以降: Opus 4.5 の暫定退役日」は、確定日 2027-01-22 に置き換えた
