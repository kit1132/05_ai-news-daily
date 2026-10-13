# AI News Daily Summary — 2026-10-14

OpenAI が GPT-4o・GPT-4.1 系4モデルを 2027-01-14 に API から削除すると告知した。Cursor は xAI と組んだ新プランで他社モデルを API 定価の別課金にし、Google は Gemini 4 Argon を GA にして GitHub Copilot にも入れた。GPT-5.5 は本日 ChatGPT / Codex から退役する。

## 今日のハイライト

### 1. [廃止] OpenAI が GPT-4o・GPT-4o mini・GPT-4.1・GPT-4.1 mini を 2027-01-14 に API から削除する — 安価な据え置き先として組んだ4モデルが3カ月後に一斉に止まる

**要点**: OpenAI が 10/14 付で、GPT-4 系4モデル5スナップショットを 2027-01-14 に API から削除すると告知した。推奨移行先はすべて `gpt-6-luna`。GPT-4o mini や GPT-4.1 を「安くて動き続ける既定」として使ってきたシステムは、残り92日で移行が必要になった。

**詳細**: 一次は OpenAI の廃止ページの「2026-10-14: GPT-4 series model deprecations」節である。

- 対象: `gpt-4o-2024-08-06`・`gpt-4o-2024-11-20`、`gpt-4o-mini-2024-07-18`、`gpt-4.1-2025-04-14`・`gpt-4.1-mini-2025-04-14`
- これらをベースにしたファインチューニング済みモデルも同じ日に止まる。`gpt-4.1-nano`・`chatgpt-4o-latest`・音声／検索系の派生は本節に記載が無い
- 移行先の GPT-6 Luna は入力 $0.10・出力 $0.50（100万トークン、9/22 公開時の記録）
- OpenAI は 10/1 にも `gpt-5.1`・`gpt-5.3-codex`・`gpt-5.4-nano`（2027-04-01 停止）と TTS 4モデル（2027-01-06 停止）の廃止を告知している

- https://developers.openai.com/api/docs/deprecations

### 2. [料金+破壊的変更] xAI と Cursor が「The X Subscription」を始め、新プランでは Claude・GPT 等の他社モデルが API 定価の別課金になった — Cursor の月額に他社モデル枠が含まれる前提が崩れた

**要点**: Cursor が 10/12 に Grok・Cursor・X Premium を1本にまとめた新プランを告知した。Grok の利用枠は従来比2倍以上に増える一方、Premium 以上で使う他社モデルはトップアップで API 定価の別課金になる。「Cursor Pro の月額で Claude が使える」前提が新プランでは成り立たない。

**詳細**: 一次は `forum.cursor.com` の Announcements（10/12 22:51 UTC）である。

- 利用枠: Grok モデルの枠は Grok アプリ・X・Cursor の共通プールで毎週リセットされる。コーディング利用量は同等の Cursor プランの2倍以上
- 他社モデル: Premium 以上で引き続き使えるが、API 定価でトップアップから課金される。支出上限は設定できる
- Teams: Premium / Super / Ultra は個人と同じ席単価で、旧 Teams プランより安くコーディング利用量は3倍とされる。SSO・管理機能・SOC 2 は付く
- 既存契約: 既存契約者には数日かけて切替ボタンが出る。切り替えるまでは含まれている他社モデル枠をそのまま使える。旧 Cursor Ultra は新規受付を停止した
- 価格は一次に載っていない。二次（TechCrunch 10/13 ほか）は Free $0 / Plus $8 / Premium $30 / Super $100 / Ultra $200 の5段階と報じている
- 既報の「OpenAI が 11/12 に Cursor へのモデル供給を停止する」は、本日も単一の投稿が出所のままで一次は確認できない

- https://forum.cursor.com/t/introducing-the-x-subscription/174450
- https://techcrunch.com/2026/10/13/spacexsi-bundles-x-premium-grok-and-cursor-into-one-subscription/

### 3. [料金+新機能] Google が Gemini 4 Argon を GA にし、同日に GitHub Copilot にも入った — 限定公開の最上位モデルが一般の API と Copilot で使えるようになり、単価は 12/1 に倍になる

**要点**: Google が 10/13 に `gemini-4-argon` を Gemini API で GA にした。9/30 の発表時は審査を通った防御側組織に限られていた。導入価格 $2/$10 は 11/30 までで、12/1 から $4/$20 に倍増する。GitHub も同日に Copilot へ追加し、Business / Enterprise は既定有効化ポリシーのままなら自動で選択肢に出る。

**詳細**: 一次は Gemini API の changelog・料金ページ・モデルページ（10/13）と GitHub changelog（10/13 18:39 UTC）である。

- 単価（100万トークン）: Standard は入力 $2.00・出力 $10.00・キャッシュ $0.10（11/30 まで）→ $4.00・$20.00・$0.20（12/1 から）。Batch・Flex は半額、Priority は $3.60/$18.00 → $7.20/$36.00。20万トークン超の割増は無い
- 提供条件: 無料枠と Google AI Pro プランでは使えない。明示キャッシュは非対応で暗黙キャッシュのみ
- 仕様: コンテキスト 1,048,576 トークン。出力は既定 65,536、long decode で最大 1,048,576。thinking は low / medium / high。computer use は Preview、Live API・画像／音声生成は非対応
- GitHub Copilot: Pro+ / Max / Business / Enterprise で GA（段階展開）。VS Code・Visual Studio・Copilot CLI・coding agent・JetBrains・Xcode・Eclipse のモデルピッカーが対象で、利用量課金はプロバイダー定価。premium request の倍率は書かれていない
- Gemini アプリ・Antigravity・Vertex AI での提供は二次報道のみで、一次は未確認

- https://ai.google.dev/gemini-api/docs/changelog
- https://ai.google.dev/gemini-api/docs/pricing
- https://ai.google.dev/gemini-api/docs/models/gemini-4-argon
- https://github.blog/changelog/2026-10-13-gemini-4-argon-in-github-copilot

## カテゴリ別まとめ

### OpenAI / Codex / ChatGPT

- **GPT-4 系4モデルの API 削除**（ハイライト参照・1）
- [廃止] **GPT-5.5 の ChatGPT / Codex からの退役（発効当日）** — OpenAI は本日 10/14 に GPT-5.5 を ChatGPT・ChatGPT Work・Codex から退役させる。API は対象外である。一次ドキュメントは本日時点でも「退役予定」の未来形のままで、日付の変更は無い。https://learn.chatgpt.com/docs/models
- [据え置き] **Codex CLI と OpenAI の changelog** — OpenAI は Codex CLI の安定版を `0.162.1`（10/9）のまま据え置き、pre-release だけを `0.163.0-alpha.10`（10/13）まで進めた。API changelog と `learn.chatgpt.com` の RSS は 10/8 の GPT-6.1 Sol Ultrafast、Announcements は 10/9 の dots 更新が最上位のままである。https://learn.chatgpt.com/docs/changelog

### Claude / Anthropic

- [セキュリティ+料金] **蒸留攻撃への対策と課金** — Anthropic が 10/12 に、他社モデルを作るための出力抜き取り（蒸留）への対策をまとめ、安全策で応答前に止めたリクエストも 9/24 から課金していると明かした。誤検知率は0.1%未満とされる。https://www.anthropic.com/research/distillation-defenses
  - 分類器: Sonnet 5.5、Opus 5 / 5.5、Fable 5 / 5.1 で2段の分類器が稼働し、推論の翻訳やタグ書き出しといった新しい回避手口も検知する
  - Preserved thinking: 8/31 以降に作成された API アカウントは Fable 5.1 / Opus 5.5 の過去コンテキストを編集できない。一部の開発者は統合の更新が必要になる
  - アカウント措置: 数万アカウントを停止し、多くはキャンペーン開始から2時間以内に止めた。蒸留側が得るデータは約90〜99%減ったとしている
- [セキュリティ] **小型モデルの自己複製の検証** — Anthropic の Frontier Red Team が、小型オープンウェイトモデルが安価な IoT 機器へ自己複製できるかを検証し、「数ヶ月先」に現実になりうると公表した（10/12）。端から端まで成功したのは GLM-5.2 だけで、5試行中4回で8/8ノードに到達した（侵入経路は認証なし ADB に単純化した上限値）。対策として ISP のフロー監視、ハニーポット、IoT の安全な既定設定を挙げた。https://www.anthropic.com/research/self-replicating-ai
- [動向] **Uber CISO の寄稿** — Anthropic が `claude.com` に Uber の CISO による AI 向け内部不正対策プログラムの寄稿を載せた（10/13）。https://claude.com/resources/articles/uber-s-ciso-on-building-an-insider-threat-program-for-ai
- [観測] **platform.claude.com の利用レポート障害が解決** — Anthropic は 10/7 に始まった Usage・Rate limits ページと Admin API 利用レポートの障害を 10/13 18:00 UTC に解決済みとした。API リクエスト自体には影響していない。https://status.claude.com/incidents/978mjkgw6mh7
- [据え置き] **Claude Code・Platform の定点** — Anthropic は Claude Code を `2.1.296` のまま据え置いた（npm は `{stable: 2.1.287, latest: 2.1.296}`・10/9 以降 publish なし）。Platform release notes は 10/9、`anthropic.com/news` は 10/8 が最上位のままである。https://code.claude.com/docs/en/changelog
- [据え置き] **Claude Haiku 4.5 は退役下限日の前日でも Active** — Anthropic の廃止ページに `claude-haiku-4-5-20251001` の退役告知は出ていない（Not sooner than 10/15）。https://platform.claude.com/docs/en/about-claude/model-deprecations

### GitHub Copilot / GitHub

- **Gemini 4 Argon の Copilot 追加**（ハイライト参照・3）
- [破壊的変更+セキュリティ] **Anthropic API キーの push を既定でブロック** — GitHub が 10/13 に、secret scanning の push protection で `anthropic_service_api_key` と `anthropic_user_api_key` を既定のブロック対象に加えた。secret scanning が有効なリポジトリでは無料の公開リポジトリも含め、Anthropic のキーを含むコミットの push が止まる。Salesforce をパートナーに加え Cloudsmith のキーも検出対象にしたが、この2種は既定ブロックではない。https://github.blog/changelog/2026-10-13-secret-scanning-blocks-anthropic-keys-by-default-adds-salesforce
- [破壊的変更+新機能] **管理設定の `sandbox` キーで旧クライアントが停止** — GitHub が 10/13 に、管理設定に `sandbox` キーを入れた組織では古い版の Copilot クライアントが更新するまで使えないようにした。他の統制系キーにも順次最小版を付けるとしている。https://github.blog/changelog/2026-10-13-enterprise-managed-settings-enforcement-updates
  - `forceRemoteSettingsRefresh`: `true` にすると CLI・VS Code・Copilot app が起動時に最新ポリシーを取得し、確認できなければ起動しない（fail closed）。既定は従来どおりキャッシュを使う
- [新機能] **Copilot テレメトリの利用者識別** — 管理者が `telemetry.capture.identity` で、Copilot の OpenTelemetry に GitHub ログイン・OS アカウント・ホスト名を付けられるようになった（10/12）。`prompts` / `responses` / `toolArguments` / `toolOutput` / `policyDetail` も個別に有効化でき、いずれも既定は無効。対象は Copilot CLI・Copilot app・Agent Host を使う VS Code で、管理設定の値はローカル設定より優先される。https://github.blog/changelog/2026-10-12-client-telemetry-user-attribution-and-configurable-capture
- [新機能] **Copilot CLI `v1.0.97`** — GitHub が Copilot CLI `v1.0.97` を安定版で出し、カスタムエージェント単位で宣言型フックを書けるようにした（10/13）。対応端末ではインライン画像を既定で表示し、`/usage` がトークン課金セッションの AI Credits を表示する。Autopilot は preToolUse フックの「ask」を拒否として扱う。https://github.com/github/copilot-cli/releases
- [新機能] **AI Scan の指標を security overview に表示** — 組織・エンタープライズ管理者が、AI Scan の検出件数・解消件数・修正率・リポジトリ別内訳をパブリックプレビューで見られるようになった（10/13）。GitHub Code Security または Advanced Security の契約が必要で、Enterprise Server は対象外である。https://github.blog/changelog/2026-10-13-code-scanning-ai-scan-metrics-in-security-overview

### Microsoft 365 Copilot / Work IQ

- [新機能] **Work IQ MCP の `retrieve` ツール** — 開発者が、Work IQ MCP の `retrieve` ツールで M365 のデータと接続ソースを横断検索できるようになった（パブリックプレビュー・Learn 10/13 新設）。Copilot Retrieval API から移行すると、課金は M365 Copilot ライセンスまたは従量課金から Copilot Credits に変わる。https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/work-iq/mcp/migrate-retrieval-api
  - 対象ソース: 1回の要求でメール・会議・Teams・人物・OneDrive / SharePoint・Graph コネクタを指定できる（Retrieval API は1要求1ソース）
  - 前提: 委任認証と `WorkIQAgent.Ask` スコープ、Work IQ API を含む支出ポリシーへの割り当てが要る。既存のライセンスや従量課金設定からは自動構成されない
  - Retrieval API: 廃止の告知は無い。固定の REST スキーマや KQL に依存するアプリは残すか並行運用するよう書かれ、Work IQ のツールは2026年11月に REST でも使える予定
- [新機能] **Copilot メモリが業務データから推論** — Copilot が M365 のコンテンツから得た推論を応答の文脈に使うようになり、10月下旬までに全世界へ展開される（MC1492154・10/8 付・二次ミラーの要約で確認）。管理者による統制は Graph の `enhancedPersonalizationSetting` で、既定はオンである。Learn は Purview の保持ポリシーと保持ラベルがメモリに適用されず、操作が監査ログに残らないと明記している。Roadmap 551195 は GA を November CY2026 のまま載せており、時期が一致していない。https://learn.microsoft.com/en-us/microsoft-365/copilot/copilot-personalization-memory
- [新機能] **Sales Development Agent の Salesforce 連携（574105）** — Sales Development Agent が Microsoft の Salesforce MCP サーバー経由で Salesforce と連携し、リードの参照・見込み客レコードの管理・営業活動の記録ができるようになる。状態は Rolling out、GA は October CY2026 である。https://www.microsoft.com/microsoft-365/roadmap?id=574105
- [予定] **Work IQ のエージェント操作2件** — Microsoft が Roadmap（10/12 バッチ）に、エージェントからのファイル書き込みと Office 文書編集を載せた。
  - Upload（570850）: エージェントが M365 の保存先へファイルをアップロードできるようになる。Preview・GA とも October CY2026
  - Updating documents in Office（570871）: エージェントが組織の文脈で Office 文書を作成・編集できるようになる。Preview は November CY2026、GA は January CY2027
- [据え置き] **Release Notes / ブログ各種** — M365 Copilot Release Notes の先頭は October 06, 2026 のままで、Copilot ブログ・Tech Community・Agent 365 Blog にも新規記事は出ていない。https://learn.microsoft.com/en-us/copilot/microsoft-365/release-notes

### Copilot Studio / Power Platform

- [予定] **モデル駆動型アプリの Work IQ 対応（571888）** — 利用者が、Copilot Studio の Work IQ ツールや Work IQ MCP から自然言語でモデル駆動型アプリのレコードを一覧・参照・作成・更新・削除できるようになる。作成・更新は利用者の明示確認後に送信される。GA は November CY2026 である。https://www.microsoft.com/microsoft-365/roadmap?id=571888
- [仕様] **外部モデルの許可ページに OpenAI** — PPAC の `allow-llm-generative-responses` が 10/13 に改訂され、管理者が許可する外部モデルの提供元に Anthropic・Mistral・xAI と並んで OpenAI が載った。M365 管理センターと PPAC の2段の手順や、Anthropic の EU Data Boundary 対象外・xAI の米国テナント限定は変わっていない。旧版の本文が取れず差分は特定できていない。https://learn.microsoft.com/en-us/power-platform/admin/allow-llm-generative-responses
- [新機能] **Power Pages の SPA テンプレート** — 開発者が、GitHub Copilot CLI と Claude Code 向けの Power Pages プラグインの `/create-site` から、311 市民サービスポータルと仕入先請求ポータルの React テンプレートでサイトを作れるようになった（10/13）。https://www.microsoft.com/en-us/power-platform/blog/power-pages/create-power-pages-sites-in-minutes-with-spa-templates/
- [観測] **Learn の改訂19ページ** — Microsoft が 10/12 20:00Z 以降に Learn の19ページを改訂したが、上記以外で新しい事実は確認できていない。`authoring-instructions` に引用の形式を変えないよう求める Important があるが、新設かどうかは比較できていない
- [据え置き] **What's New / Released Versions / 非推奨一覧** — Copilot Studio What's New と非推奨一覧は `ms.date` 10/5 のまま、Released Versions は 2026.6.3 のまま105日動いていない。https://learn.microsoft.com/en-us/power-platform/released-versions/copilotstudio

### Cursor / Google / その他モデル

- **The X Subscription**（ハイライト参照・2）
- [新機能] **Cursor の Origin App Marketplace** — Cursor が Origin App Marketplace を公開し、利用者が20件超の外部連携を追加できるようにした（10/13）。開発者は Origin API で作ったアプリを公開申請できる。対象はデプロイ（Cloudflare・Vercel など）、CI とレビュー（Buildkite・CodeRabbit など）、セキュリティと監視（Semgrep・Sentry など）で、対象プランと価格は書かれていない。https://cursor.com/changelog/origin-app-marketplace
- [新機能] **Meta の Muse Wonder** — Meta が 10/12 に初のフロンティアモデル Muse Wonder を Meta Model API と Muse Code で提供したと複数の報道が伝えた。単価は入力 $4・出力 $20・キャッシュ入力 $0.20（100万トークン）、コンテキストは100万トークン。上位版 Muse Wonder Full は従量 API が無く、Muse Code の月 $50 以上のプランでだけ使える。性能値は自社測定で、Meta の一次ページは未確認（二次のみ）。https://forkast.news/meta-ships-muse-wonder-its-first-frontier-model-and-leaves-the-research-blog-empty/
- [据え置き] **Workspace・MCP・HF・Apple の定点** — Workspace Updates の Atom は本日も取得できず、10/12 以降の Gemini 関連の告知は確認できていない。MCP ブログは 8/22 が最上位のまま、Hugging Face の登録8 org の新規は関心領域外（画像生成・音声系）、Apple Developer News にも 10/6 以降の告知は無い

### 市場・その他

- [据え置き] **買収協議・市場データ** — Amazon × Decart と Nvidia × Reflection AI の買収協議に 10/10〜11 の報道以降の続報は無い。IDC Japan・MM総研・NRC・Similarweb・Business Insider Japan も新規公表が無く、Similarweb の9月分と Business Insider Japan の10月版料金早見表は引き続き未検知である。https://www.thestar.com.my/tech/tech-news/2026/10/11/nvidia-in-talks-to-invest-further-in-reflection-ai-or-buy-it-ft-reports

## 直近の注目予定

- **10月**: Copilot メモリの業務データ対応の展開完了（MC1492154・10月下旬） ／ Sales Development Agent の Salesforce 連携 GA（574105） ／ Work IQ Upload（570850） ／ Copilot Chat の UBB モデル選択（571400） ／ 共有プラグインレジストリ Preview（570669） ／ フェデレーテッドコネクタの書き込み対応 GA（570964）
- **10/14**: GPT-5.5 が ChatGPT / ChatGPT Work / Codex から退役 ／ GitHub SSH の新規 RSA 鍵が 3072 ビット以上必須に ／ Anthropic の pre-IPO investor day（報道）
- **10/15 以降**: `claude-haiku-4-5-20251001` の暫定退役日（告知はまだ無い）
- **10/19**: GitHub Copilot が5モデルを廃止（`gpt-5.5`・Gemini 3.7 Flash を含む）
- **10/22**: Copilot Business / Enterprise の機能既定有効化が発効 ／ Gemini API の Veo 3.1 プレビュー3種と `gemini-omni-flash-preview` が停止（最短日）
- **10/23**: Gemini API の `deep-research-pro-preview-12-2025` が停止 ／ OpenAI のレガシー GPT スナップショットが停止
- **10月下旬〜11月上旬**: Copilot オンボーディング（Frontier）の展開（MC1486291）
- **10/27〜29**: PPCC 2026（ラスベガス）
- **10/30**: ChatGPT Pro 200 の Work / Codex 利用枠が変更（二次）
- **10/31**: MCP サーバー認定の旧申請経路が終了
- **11/1**: Codex の28日間「改善かリセット」の終了（二次）
- **11月**: Work IQ のツールが REST に対応 ／ モデル駆動型アプリの Business Apps in Work IQ GA（571888） ／ Business Applications in Work IQ が既存環境で既定オン ／ Work IQ の Office 文書編集 Preview（570871）
- **11/12**: Anthropic Usage Policy 改定版が発効 ／ OpenAI → Cursor のモデル供給停止予定（一次未読）
- **11/16**: Sales Development Agent が Copilot Credits の消費を開始
- **11/17**: Gems が Gemini アプリの設定パネルへ移動
- **11/17〜20**: Microsoft Ignite
- **11/30**: `claude-sonnet-4-5-20250929` が Claude API から退役 ／ OpenAI の Evals・`v1/prompts`・Agent Builder が停止 ／ Gemini 4 Argon の導入価格が終了
- **12/1**: Gemini 4 Argon の単価が $4/$20 に倍増 ／ Copilot Business の従量課金が既定オン
- **12/14**: claude.ai/design の単体サイトが閉鎖
- **2027-01-06**: OpenAI `tts-1` / `tts-1-hd` / `gpt-4o-mini-tts` 2版が停止
- **2027-01-14**: OpenAI の GPT-4o・GPT-4o mini・GPT-4.1・GPT-4.1 mini が API から削除
- **2027-03-01 以降**: Gems 廃止（Business / Enterprise）
- **2027-04-01**: OpenAI `gpt-5.1` / `gpt-5.3-codex` / `gpt-5.4-nano` が停止

## 改善メモ

- 新規提案: 3ソースとも無し
- 継続提案: Master は B-082 最上位エントリ基準の差分判定（20回目）に `anthropic.com/research` の 10/12 付2本を1日遅れで検出した事例を追記 ／ Copilot は B-074（docset 全件突合・1,632ページ）・B-070・B-037（105日）・B-079 を更新 ／ industry は3件を更新（最多 B-004・106回目）し、B-024 に GPT-4 系廃止告知の当日捕捉を記録
- 障害の変化: industry が `usecarly.com`・`www.technology.org`・`tech.yahoo.com` をゲートウェイ拒否として新規登録した（WebSearch で代替）。Master・Copilot は変化なし
- ソース間の差分・矛盾:
  - GPT-5.5 退役後の Codex の移行先を、Master は `gpt-5.6-sol` と書き、前日の本サマリーと industry が参照した `learn.chatgpt.com/docs/models` の現行記載は `gpt-6-sol` / `gpt-6-luna` である。本日の項目では移行先を書かなかった
  - 10/30 の ChatGPT Pro 200 の枠変更は、Master が「Work / Codex 利用枠が半減」、industry が「Plus 比10倍」と書き、二次どうしの割れが続いている。予定欄は「変更（二次）」のままにした
  - Gemini 4 Argon の価格は、Master が「一次のモデルページに無く二次のみ」、industry が「一次の料金ページで確認」としている。本サマリーは industry の一次（pricing ページ）を採った
  - Copilot メモリの業務データ対応は、MC1492154（10月下旬完了）と Roadmap 551195（GA November CY2026）で時期が割れている（Copilot 側の記録どおり）
