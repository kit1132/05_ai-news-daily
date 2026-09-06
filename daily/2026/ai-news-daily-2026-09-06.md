# AI News Daily Summary — 2026-09-06

9月4日に出た告知が、本日3ソースで同時に確定した日である。Microsoft は半期リリースウェーブそのものを廃止し、2026 Wave 2 の告知を出さないまま Release Planner を 11/15 に閉じると Partner Center で明記した。GPT-6 Astra は GitHub Copilot で既定有効のまま GA し、同日 Microsoft Copilot の Cowork と Copilot Studio にも入ったが、Learn 側のモデル一覧はどちらも Astra の行を持たない。前日「npm にあるが changelog 未記載」だった Claude Code 2.1.261 は内容が確定し、`/skill-doctor` と組織ポリシーの可視化が入っていた。OpenAI 側では料金ページの注記から地域処理アップリフト 10%・EU での Fast mode 不可・長文脈境界 272K の3点が読み取れ、09-05 の単価表だけの読みが埋まった。Anthropic は Claude によるフェルマーの最終定理の Lean 4 形式化を Apache-2.0 で公開している。

## 今日のハイライト

### 1. Microsoft が Release Wave を廃止した — 半期単位で導入計画を組む前提が消え、Release Planner は 11/15 に閉じる

**要点**: Microsoft が Dynamics 365 / Power Platform / Dataverse の半期リリースウェーブを廃止する。2026 Wave 2 の告知は行われず Release Planner も **11/15** に退役するため、前提が「Wave 単位で計画を追う」から「AI at Work roadmap を随時見る」へ変わる。

**詳細**: 一次は Partner Center の9月分 announcements で、`updated_at` が **2026-09-04T22:04Z** へ動き、掲載が3件 → 4件に増えた。追加分が「Business Applications roadmap content moving」節である。確定している変更は4点。

- 告知の取りやめ: 「there won't be a September 2026 Release Wave 2 announcement」と明記され、Wave 2 の計画一覧は公開されない。半期ごとの wave 1 / wave 2 という公表単位そのものを廃止し、計画が固まった時点で随時公開する方式へ移る
- 退役の期日: Release Planner は 2026年11月15日に retire し、Microsoft Learn 上の Release Plans はアーカイブされる
- 移行先: 2026年9月以降の新規ロードマップ項目は AI at Work roadmap（`aka.ms/AIatWorkRoadmap`）へ直接公開され、Microsoft 365・Copilot・エージェント・Business Applications が1か所に統合される
- 移行対象の線引き: public preview または GA の期日が **2026年6月1日以降**の既存項目が、9月以降に新ロードマップへ移る見込みとされる

影響範囲はロードマップ告知に限ると一次が明記しており、製品のリリーススケジュール・展開プロセス・Message Center 通知・製品ドキュメントは変更されない。代替経路として Microsoft Release Communications MCP サーバーが無償・サインイン不要で案内され、roadmap ビューのフィルター・CSV エクスポート・RSS 購読も使える。⚠️ **02 は Power Automate / Power Apps の GA 移行を Release Wave の緑チェックの差分で判定してきたため、判定基盤が 11/15 で止まる。**⚠️ Microsoft 本体の告知は Dynamics 365 ブログの **8/25** 付で、本サマリーの定点3ソースが捕捉したのは12日遅れの本日が初めてである。

- https://learn.microsoft.com/en-us/partner-center/announcements/2026-september
- https://www.microsoft.com/en-us/dynamics-365/blog/business-leader/2026/08/25/one-always-on-roadmap-dynamics-365-power-platform-and-dataverse-join-the-ai-at-work-roadmap/
- https://mc.merill.net/message/MC1461529

### 2. GPT-6 Astra が Copilot 3面に初日から入った — GitHub 側は既定有効かつ従量課金で、premium request 換算の試算が崩れる

**要点**: GitHub が 9/4 に `gpt-6-astra` を Copilot で GA にし、Microsoft も同日 Cowork と Copilot Studio へ載せた。GitHub 側は**既定で有効**かつプロバイダー定価の従量課金なので、管理者が切らない限り Sol 比2.5倍の単価が自動で入る。

**詳細**: GitHub 側の対象プランは Copilot **Pro+ / Max / Business / Enterprise** で、⚠️ Pro は対象外である（09-04 収録の Gemini 3.8 Flash は Pro を含んでいた）。提供面は VS Code / Visual Studio / Copilot CLI / coding agent / Copilot アプリ / github.com / GitHub Mobile（iOS・Android）/ JetBrains IDEs / Xcode / Eclipse の10面で、モデルピッカーから選べる。ロールアウトは段階的である。

- 既定の向き: 一次は「管理者がグローバル既定を切っているか、このモデルを明示的に無効化していない限り、新モデルは自動的に有効になる」と記載する。Business / Enterprise は Copilot 設定のモデルポリシーで制御する
- 課金: provider list pricing の従量課金で、一次告知に premium request の倍率は書かれていない。09-05 収録の OpenAI 一次料金の値が効くと読むと、短文脈で入力 $10／出力 $50、長文脈で $20／$75 になる
- 期間限定価格の有無: Astra には introductory pricing の記載がない。09-04 収録の Gemini 3.8 Flash が 2026-12-31 までの導入価格だったのと対照的である
- ⚠️ Fable 5.1 の GA（9/1）との差: あちらは Business・Enterprise で既定無効で、Anthropic の安全性分類器のためのデータ保持要件の承諾が前提だった。Astra 側は記事にデータ保持要件の記載がなく、既定有効で入る

Microsoft 側は Tech Community の M365 Copilot Blog に **9/4 20:28Z** 付「Available today: OpenAI GPT-6 Astra in Microsoft Copilot」が出た。提供範囲は Cowork と Copilot Studio の2面で、9/2 の Claude Fable 5.1 と同じ形である。展開は当日から順次で、提供可否は地域と組織により異なり、管理者は Microsoft 365 管理センターから制御する。モデル仕様は Learn の Foundry ドキュメントに `gpt-6-astra`（バージョン 2026-09-03）として載っており、コンテキストは 1,050,000 トークン（入力 922,000 / 出力 128,000）、学習データは2026年4月までである。`temperature` と `top_p` は使えず、Tier 5 と Tier 6 は既定でクォータが要る。⚠️ **Copilot Studio のモデル一覧にも Cowork のモデル一覧にも Astra の行は無い。**クライアント側の追随は同日中に済んでおり、Copilot CLI の pre-release `v1.0.84-1`（9/4 23:20 UTC）と Codex CLI 安定版 `0.153.4`（9/4 23:25 UTC）が Astra 対応を入れている。

- https://github.blog/changelog/2026-09-04-gpt-6-astra-is-generally-available-in-github-copilot
- https://techcommunity.microsoft.com/blog/microsoft365copilotblog/available-today-openai-gpt-6-astra-in-microsoft-copilot/4552808
- https://learn.microsoft.com/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure#gpt-6
- https://developers.openai.com/api/docs/models/gpt-6-astra

### 3. Claude Code 2.1.261 の内容が確定した — 前日「changelog 未記載」だった版に /skill-doctor と組織ポリシーの可視化が入っていた

**要点**: 09-05 時点で npm にだけ存在し内容不明だった **2.1.261**（9/4 17:49 UTC publish）が changelog に載った。未使用スキルを洗い出す `/skill-doctor` と、組織ポリシーの読み込み失敗の理由を `/status` に出す行が入っている。

**詳細**: 追加は4件である。

- `/skill-doctor`: 読み込み済みで使われていないスキルと、そのコンテキスト消費量を洗い出す。剪定の判断材料になる
- `bashOutputMaxChars` / `taskOutputMaxChars`: インライン出力の上限を最大 **128K 文字**まで引き上げる
- `--append-subagent-system-prompt-file`: コマンドライン長の制限を超える大きなサブエージェント用プロンプトをファイルで渡す
- `/status` と `claude doctor` の「Organization policy」行: プロキシ等でポリシー読み込みに失敗した理由が表示される。管理下設定の修正も2件入り、フィーチャーフラグが誤ったバージョンへ適用される問題と、信頼済みプロキシ配下でのゲートウェイのクライアント IP 取り扱いが対象である

修正は60件超で、高速入力・キーリピート時の文字順序の乱れ、`/net` オートマウント上で `/add-dir` が誤って「解決できない」と返す問題、AWS 認証情報が無応答のときに Bedrock セットアップウィザードが固まる問題、セッション再開でフック出力のコンテキストが失われる問題、TLS 検査プロキシ配下の Windows での失敗が含まれる。⚠️ **スケジュール／クラウド実行環境の不具合修正は4版連続**である（2.1.258 の `user messages must have non-empty content`、2.1.259 のコネクタツール権限承認後の無応答、2.1.260 のクラウド上 Claude in Chrome の `Not connected`、2.1.261 の管理下設定がプラグインを強制有効にするとクラウドセッションが同期済みプラグインを捨てる問題）。⚠️ npm の `dist-tags` は 09-06 実測で `{stable: 2.1.236, latest: 2.1.261, next: 2.1.261}` で、前日に一度解けた `next` == `latest` の合流が再び戻った。`stable` は 2.1.236 のままで `latest` と **25版差**（前日24版差から拡大）であり、8/28 の 2.1.251 の symlink 権限境界修正群も 9/3 の 2.1.260 の Bash 権限チェック脆弱性修正も、stable 固定の組織へは依然として届いていない。

- https://code.claude.com/docs/en/changelog
- https://registry.npmjs.org/@anthropic-ai/claude-code

## カテゴリ別まとめ

### Anthropic / Claude

- Anthropic が Claude Code **2.1.261** を公開した（ハイライト3参照）
- Anthropic が Claude によるフェルマーの最終定理の Lean 4 形式化を公開した（9/4）。機械検証済みの完全な証明で、成果物は `github.com/anthropics/fermats-last-theorem` に Apache License 2.0 で置かれている
  - 規模: モジュール **60,475 個**、定理 29,511 個、定義モジュール 1,450 個で、コミュニティライブラリ Mathlib の約5倍にあたる
  - 依存と公理: Lean 4.33.1（2026年のカーネル健全性修正を含む）と Mathlib v4.33.0（`lakefile.lean` でコミット固定）。公理は `propext` / `Classical.choice` / `Quot.sound` の3つだけで、`axiom` / `sorry` / `native_decide` / `unsafe` / `partial def` を含まない
  - 検証: `lake build` の Lean カーネル検証に加え、Mathlib のみで状態を再チェックする comparator（15時間）と、Rust 実装の独立カーネル nanoda v0.4.13 による 1,052,234 宣言の検証を通している
  - 再現条件: Linux / macOS のみ（Windows はパス長超過で不可）、ディスク約 287GB、メモリ最大 230GB、96並列で約5.5時間
  - 帰属: `ATTRIBUTION.md` が106ファイルの上流出典を明記し、Imperial College London の FLT プロジェクト（Kevin Buzzard 主導）・flt-regular・Mathlib を挙げている。リポジトリはメンテナンス対象外で貢献を受け付けない研究成果物である
  - ⚠️ 「Claude が11日間ほぼ自律で作業した」「約60億出力トークンを消費した」「Prove2Me 上で組み立てた」は二次情報である。README は Prove2Me に言及せず使用モデル名も書いていない。発表本文と論文 PDF はゲートウェイ拒否で読めず、一次で確定できたのは成果物の仕様だけである
- Claude Platform API release notes は 9/3 の `ant` CLI 1.30.0 が最上位のままで、9/4・9/5 の追加はない。`support.claude.com` の Release Notes も 9/1 の Fable 5.1 / Mythos 5.1 が最上位で変わらない
- `claude.com/blog` は 9/2 の commerce agents 2本が最上位のままである。01 は一覧の全 href 15件を日付条件なしで取得して確認しており、B-060 で規定した取得形が動いている
- Claude Code の changelog 最上位6版は 2.1.261（9/4）→ 2.1.260（9/3）→ 2.1.259（9/2）→ 2.1.257（9/1）→ 2.1.252（8/31）→ 2.1.251（8/28）で日付列に飛びはなく、欠番 `2.1.244` / `2.1.249` / `2.1.253`〜`2.1.256` の計6件も据え置きである
- ⚠️ Anthropic の8月 Risk Report は **21日連続で一次未読**である（初出 08-17）
- 既報: 週次上限50%増の 9/13 終了と 9/14 からの恒久 +25%（現行比17%減）、Model Hardware Standard の研究プレビュー（8/27）、Enterprise Frontier Safeguards（9/1・今秋から段階提供）、Fable 5.1 / Mythos 5.1 の GA（9/1）、commerce agents blueprint（9/2）、Claudeforce（オープンベータは9月中）

### GitHub Copilot / 開発ツール

- GitHub が GPT-6 Astra を Copilot で GA にした（ハイライト2参照）
- GitHub が 8/31 週の Copilot weekly releases まとめを 9/4 に公開した。管理者側の変更が3件ある
  - Agent Merge: public preview に入り、レビュー指摘・失敗したチェック・マージコンフリクトを解消してプルリクエストをマージ可能な状態まで運ぶ。CI を監視し、必要なレビュアーを追跡し、条件が満たされるまで待つとされる
  - enterprise-managed settings: 任意のモデルを既定として指定できるようになった。09-03 収録の `managed.json` の `model` キーの拡張にあたる
  - 個人ユーザー予算: 有効期限を設定できるようになった
  - IDE 側は VS Code 1.136 でマルチルートワークスペースが実験的機能となり、Copilot と Claude のエージェントセッションが全フォルダーに及ぶ。チャットセッションの階層化とチャット背景のカスタマイズも実験的に入り、JetBrains 向け Copilot ハーネスは GA になった。Copilot アプリ / CLI ではコンテンツ除外がエージェントワークフロー全体に効くようになった
- GitHub が Copilot CLI の pre-release を2版出した。`v1.0.84-0`（9/4 21:15 UTC）はマネージドサンドボックスセッションの無効化・PowerShell の書き込み・複数 GitHub アカウント対応・Windows 上の git 操作を修正し、`v1.0.84-1`（9/4 23:20 UTC）が GPT-6 Astra に対応した。安定版は 9/4 15:38 UTC の `v1.0.83` のままである
- OpenAI が Codex CLI の安定版 `0.153.4` を 9/4 23:25 UTC に公開した。Astra をバンドルモデルピッカーへ表示するよう修正し、非同期の clarification 質問に関するガイダンスをツールが利用可能なときだけ適用するよう変更している
- `github.blog/changelog` の Copilot ラベル最上位10件は 9/4 の2本 → 9/3 の3本 → 9/2 の2本 → 9/1 の3本で、9/5 の新規はない
- `devblogs.microsoft.com/commandline` の AI 関連は 8/10 の Intelligent Terminal 0.2 が最新のままである（B-042・回数12）

### Microsoft 365 Copilot / Copilot Studio / Power Platform

- Microsoft が Release Wave を廃止した（ハイライト1参照）
- Microsoft が GPT-6 Astra を Cowork と Copilot Studio へ載せた（ハイライト2参照）
- Copilot Studio のモデル可用性一覧（`authoring-select-agent-model`）の `updated_at` が 2026-08-03T14:59Z → **2026-09-05T01:02Z** へ1か月ぶりに動いたが、Claude Fable 5.1（9/2 告知）も GPT-6 Astra（9/4 告知）も行が追加されていない。表の内容（GPT-4o と Claude Sonnet 4.5 が `Retired`、既定は GPT-4.1、Claude Sonnet 5 は GitHub Copilot ハーネス限定、Mistral Medium 3.5 のみ全リージョンで Experimental）は 8/16 の一次取得時から変わっていない
- Cowork のモデル一覧（`cowork-models`）の `updated_at` は 2026-09-02T17:33Z へ動いたが、ピッカーの7モデル（Auto / GPT 5.5 (Frontier) / GPT 5.6 Sol / GPT 5.6 Terra / Opus 5 / Claude Sonnet 5 / Claude Fable 5 (Preview)）は据え置きで、告知された「Fable 5.1」の表記にも一致しない
  - ⚠️ **公開済みページに編集者向けの未公開指示が残っている。**「State which populations the GPT 5.5 (Frontier) model is available to before publishing.」と、Note「Confirm the GPT 5.5 (Frontier) availability statement and the definition of the "(Frontier)" qualifier before this page is published.」の2箇所である。ページ自身が可用性記述を未確定と書いているため、この一覧を提供状況の権威として使う前提は成立しない（02 が B-059 を起票）
- M365 Copilot の Release Notes は August 25, 2026 バッチが最新のままで、10節・全19項目に増減はない。⚠️ ただし `updated_at` が 2026-08-25T20:41Z → **2026-09-03T19:39Z** へ動いており（`ms.date` も 2026-09-03）、見出しの並びだけを見ていた 9/4・9/5 のセッションはこの再ビルドを記録していない。次バッチは隔週傾向なら 9/8 前後である
- ⚠️ AI at Work roadmap の Latest announcements は 7/24 の Opus 5 告知が先頭のままで、9月も1件も追加されていない。Fable 5.1（9/2）と GPT-6 Astra（9/4）は同じ「Available today」型でありながら広報枠に載らず、未掲載は1件から2件に増えた
- ⚠️ Release Communications RSS の総項目数が 1,782 → **1,774** と8件減り、`lastBuildDate` は 9/3 22:50Z → 9/4 22:03Z へ動いた。9/3 22:50Z より新しい起票はゼロだが、どちらの指標でも「新規ゼロ」を正しく判定できない
- 定点の停滞が続いている。Copilot Studio の What's New は July 2026 節が最新のままで、June 節の GitHub Copilot ハーネスは GA（8/3）から **34日連続**で `(Production-ready preview)` と書かれている。Released Versions は Copilot Studio Build 2026.6.3（6/30 初出）のままで空白が **68日**に達し、次の定例日は 9/8 である。Copilot Tuning の一次は停止発効（8/20）から17日たっても停止も退役も書いていない
- 拡張機能 What's New は July 2026 節のままで、`updated_at` 2026-07-29T20:23Z から39日間止まっている（週次確認の次回は 9/11）。Purview / ガイダンスハブ / Cowork What's New の3ソースも `updated_at` に変化がなく、8/23 に Roadmap で検知した 569612（Copilot メモリの Purview 保持・GA 2026年9月）は Purview 側に未掲載のままである
- 非推奨一覧は `updated_at` 2026-09-04T19:03Z のままで 9/5 から変化はない。9/9 発効の PVA ヘルプチャットボット削除は掲載済みで、発効まで3日である
- Partner Center の9月ページは掲載が3件 → 4件へ増えた。既存3件（9/1 Marketplace の購買オーダー紐づけ、9/2 CSP flex spend plan サンドボックス、9/3 Partnering for Success Together）に変化はない。⚠️ 9/9 開催の Partnering for Success Together は初回セッションで、Copilot 固有の内容かは告知から判別できない
- Microsoft Copilot Blog の登録 RSS が内容ごと復旧した。`lastBuildDate` が 2026-07-21T23:56Z → **2026-09-02T17:23Z** へ動き、HTML 一覧の先頭にある 9/2 の記事が `<item>` に含まれるようになった。⚠️ 9/3 は 403・9/5 は 200 でも中身が45日古いという経緯があるため、RSS 単独運用へ戻す根拠にはしない
- ブログ系に新規はない。Copilot Studio Blog は 9/3 のハーネス選択白書、M365 Blog 本体は 9/3 の PPCC 2026 記事（非イベント記事は 7/30）、M365 Developer Blog は 9/2、SharePoint Blog は 9/3、Agent 365 Blog は 8/6、Power Platform Blog は 9/3 の PPCC 記事がそれぞれ最新である
- PnP コミュニティは 8/31 週の Weekly Agenda と 9/3 開催のコミュニティコールを WebSearch の索引で確認した。8/30 の確認時は 8/10 週が最新だったため3週分進んだことになる。デモは Ian Tweedie「Sometimes a Little Code Saves a Hundred-Step Flow」/ Katrina Frolinka「Custom Copilot Agent for Document Generation in SharePoint」/ Elio Struyf「Supporting WebMCP within an SPFx extension」である
- Copilot Agent Kit（Power CAT）は 8/17 の `CopilotStudioAccelerator-August2026.1` が最新のままで、課金系ドキュメント3本も `updated_at` が動いていない

### OpenAI / Codex / ChatGPT

- OpenAI が料金ページの注記に地域課金と長文脈の条件を明示した。⚠️ 09-05 収録では単価表だけを読んでいたため取りこぼしていた3点である
  - 地域処理アップリフト: データレジデンシー対象ワークスペースでは、**2026年3月5日以降**にリリースされたモデルに 10% が掛かる
  - EU の制限: EU データレジデンシーでは GPT-6 Astra の Fast mode が使えず、Standard を使うよう案内されている
  - 長文脈の境界: long context 単価が適用されるのは `gpt-6-astra` / `gpt-5.6` 系 / `gpt-5.5` / `gpt-5.4` で、境界は **272Kトークン**と注記されている（09-05 の「次アクション」に挙げた適用境界がこれで埋まった）
  - https://developers.openai.com/api/docs/pricing
- OpenAI の単価は13日連続で据え置きである。Sol は入力 $4／出力 $20、Astra は短文脈で $10／$50 で、Sol の期間限定価格は「少なくとも 2026年11月21日まで」の記載が続く
- ⚠️ Cyber 節の `gpt-5.4-cyber` は単価欄がすべて空のままで、09-04・09-05 に続き**3日連続で充足していない**。`gpt-5.6-cyber` は入力 $12.50／キャッシュ入力 $1.25／キャッシュ書込 $15.625／出力 $75.00 で不変、`gpt-5.5-cyber` はキャッシュ書込のみ空欄である
- `developers.openai.com/api/docs/changelog` は 9/3 の2本（GPT-6 Astra リリース／Responses API の3制御）が最上位のままで、9/4・9/5 の追加はない。`community.openai.com` の Announcements RSS も 9/3 の告知が最上位である
- 退役ページに新規告知はなく、GPT-6 Astra の登場に伴う退役告知も出ていない。⚠️ 今月中に 9/24 の Videos API / Sora 2 系と 9/28 の旧 GPT-3.5 系4モデルの2件が到来する。⚠️ 11/30 の Evals 廃止の代替として一次が挙げるのは外部OSS の Promptfoo で、Agent Builder の代替は Agents SDK である
- ⚠️ `learn.chatgpt.com` はゲートウェイ拒否が継続している（`curl` HTTP コード 000）。`site:` 付き WebSearch で拾えたのは「GPT-6 Astra が 8/31〜9/4 に Codex と ChatGPT Work へ入った」「8/24〜28 に ChatGPT デスクトップアプリが Edge / Brave / Opera / Vivaldi に対応した」「スケジュールタスクを Gmail / Slack / GitHub のイベントで起動できる」の3点で、個々の公開日は未確定である

### Google

- Gemini API changelog は 9/3 の Lyria 3.5 public preview が最上位のままで、9/4・9/5 の追加はない。料金改定の告知も出ていない。⚠️ Lyria 3.5 は音楽生成なので `interests/ai-tools.md` の除外基準に該当する
- HF の `google` org は `timesfm-3.0-pytorch`（作成 8/24）が最新のままで、新規作成も `lastModified` の更新もない
- 登録済み Google 系5ソースはゲートウェイ拒否が継続しており、`ai.google.dev` だけが到達できる Google 一次である
- 既報: 9/2 GA の `gemini-3.8-flash` は入力 $0.75 / 出力 $3.75 が 2026-12-31 まで、9/1 の agentic video understanding、旧 `gemini-omni-flash-preview` は 9/30 廃止、Gemini 3.5 Pro GA は未ローンチ継続

### オープンウェイト / MCP / Cursor / xAI / Devin

- HF の8 org のいずれにも 9/5 の新規公開はない。`createdAt` 降順と `lastModified` 降順の両方で確認しており、`lastModified` の最新は `zai-org` の GLM-5.3 系4リポジトリ（9/4 06:38〜06:45 UTC）だが作成日は全て 8/25 のままなのでカード更新である
- ⚠️ 二次の集計サイトが「Meta が 9/2 に Muse Spark 1.3 を出荷した」と書いているが、HF の `meta-models` org に該当は無い（最新作成は 8/10 の `Muse-Glimmer-30B-ExecuTorch-PTE`）。Meta の一次3ホストはゲートウェイ拒否のため確認できず、01 は採用していない
- HF `downloads` の実測（2026-09-05 19:09 UTC 取得・追跡8リポジトリは全て `private: false` / `gated: false`）は `Qwen3.8-27B-FP8` 6,461,901 ／ `Qwen3.8-Flash-Next` 401,327 ／ `DeepSeek-V4-Flash-0731` 4,565,650 ／ `DeepSeek-V4-Pro-0813` 152,234 ／ `DeepSeek-V4-Flash-Vision-Exp` 184,542 ／ `GLM-5.3-Flash` 727,610 ／ `GLM-5.3` 370,417 ／ `Kimi-K3` 2,552,594 である。⚠️ `Kimi-K3` だけが前回記録から減っているが、`downloads` は30日ローリングなので減少は異常ではない（B-050・回数8）
- `blog.modelcontextprotocol.io` は 8/22 の「The New MCP Roadmap」が最上位のままで、15日間新規がない
- Cursor changelog は 9/2 の Self-hosted machines が最上位のままで、フォーラム Announcements も 9/2 の Grok Bot Android 版が最上位である
- ⚠️ **Grok 4.7 は二次情報のまま動いていない。**予告は 9/2 の Musk の X 投稿が出所で、公開見込みは 9/11〜9/12、パラメータ 2.1兆（Grok 4.6 の1.5兆から40%増）とされる。xAI はローンチページ・API モデル ID・価格・モデルカード・コンテキスト長・ベンチマーク表のいずれも公開しておらず、一次3ホストはゲートウェイ拒否である。公式提供中の最新は Grok 4.6 のまま（8/12・context 50万トークン・$2/$6）
- Devin は一次・代替一次のいずれからも読めない状態が続いている。二次が挙げる更新（`devin doctor` のサブエージェント frontmatter 検査、cleanup スキャン、`/scan`・`/recap`・`/rename` 等）は前回チェックと内容が変わらず公開日も特定できないため、01 は新着扱いしていない

### 資本 / 市場データ / 料金

- データセンター新興 Crusoe が $3B 超を調達し、評価額 約 **$30B** のラウンドを確定させたと Bloomberg が 9/3 に報じた。Atreides Management と Valor Equity Partners が共同主導し Mubadala Capital が参加した。2025年10月の Series E（$1.375B・評価額 $10B 超）から約3倍で、07-04 収録時点では「調達交渉中」だった案件が成立したことになる。あわせて Jane Street 向けに GPU と AI インフラを供給する5年 $13B のクラウド契約を締結したとされる。⚠️ 数値はすべて関係者取材にもとづく二次情報である
- AI 半導体まわりの新興 Gimlet Labs が評価額 $3B で $300M を調達したと複数の二次媒体が 9/4 に報じた。⚠️ 一次発表を確認できていないため、03 は金額と評価額を提案に引かない扱いとしている
- Gartner の AI 支出予測2件を本日はじめて捕捉した。⚠️ いずれも本日の新規公表ではないため、引用時は公表日を添える必要がある
  - 世界の AI 支出 2026年 **$2.59兆**・前年比 +47%（5月19日公表）。AI-optimized IaaS・AI 最適化サーバー・AI ネットワークファブリック・AI 処理半導体を含む「AI インフラ」が最大セグメントで、全体の45%超を占めるとする
  - 世界の AI-optimized IaaS 支出 2026年 **$42B**・前年比 +96%（8月10日公表）
  - 既収録の「AI モデル・プラットフォームへの世界エンドユーザー支出 2026年 $64B・前年比 +63.4%」（7月20日公表）と合わせ、インフラ層・IaaS 層・モデル層の3階層で引用できる数字がそろった
- ⚠️ Similarweb の生成AI ウェブトラフィックシェアは二次情報が割れている。ChatGPT 53.9%／Gemini 27.9%／Claude 9.2% を「8月版」とする媒体がある一方、別の媒体は ChatGPT 52.7% を挙げ、対象月も「8月版」と「2026年5月時点」が混在している。一次はゲートウェイ拒否のため、03 は既収録の「ChatGPT 約53%・Gemini 約27〜28%・Claude 約9%（2026年5月時点）」を引用可能な範囲としている
- IDC / IDC Japan・MM総研・NRC に9月の新規公表はない。IDC Japan の最新は3月公表の国内 AI 市場支出予測（2025年 2兆3,725億円 → 2029年 6兆8,897億円・CAGR 36.0%）である
- Google が18歳以上の大学生へ Google AI Plus（月額725円相当・ストレージ400GB・動画生成付き）を無償提供している。⚠️ 09-05 収録では書いていなかったが、**申込期限は 2026年12月31日**である

### Apple

- `developer.apple.com` は 9/1 の「Upcoming changes to Rosetta support for Intel-based macOS apps」が最上位のままで、9/2 以降の新規はない。⚠️ AI 関連の最新は 6/11 の ImageCreator クラス廃止告知のままである
- 既報: 8/26 の特別イベント告知（9/9 10:00 PT）、8/18 の EU 向けビジネス条件変更（発効 2026-10-01）

## 直近の注目予定

- **9/7**: 週次復旧チェック（月曜）／ ppweekly・MS-4005・課金レート表の週次確認
- **9/8**: M365 Copilot Release Notes の次バッチ（隔週傾向）／ Copilot Studio Released Versions の定例更新日
- **9/9**: Apple 特別イベント（10:00 PT）／ Power Automate の PVA ヘルプチャットボット削除が発効 ／ Partnering for Success Together 初回 ／ GLM-5.3-Flash の Z.ai 経由50%割引が終了
- **9/10**: MAI-Code-1-Flash が全 Copilot 体験から廃止
- **9/11**: 拡張機能 What's New とモデル可用性一覧の週次確認
- **9/12**: Grok 4.7 の公開予定（Musk の X 投稿のみが出所・公式の裏づけなし）
- **9/13**: Claude Code の週次上限50%増が終了 ／ Power CAT・PnP の週次確認
- **9/14**: Claude Code の標準週次上限が恒久的に +25%（Pro / Max / Team / シート課金 Enterprise。現行比では17%減）
- **9/17**: OpenAI DevDay Exchange の応募締切
- **9/21**: Anthropic ウェルビーイング研究助成の応募締切
- **9/23**: WebMCP Challenge の受賞発表
- **9/24**: OpenAI の Videos API と Sora 2 系が退役（代替モデルの提示なし）
- **9/28**: Copilot のチャット3面統合 ／ code review の既定 effort が Lite → Balanced ／ チャットのデータ保持がアカウント存続期間へ ／ OpenAI の `gpt-3.5-turbo-instruct` / `babbage-002` / `davinci-002` / `gpt-3.5-turbo-1106` が停止
- **9/29 以降**: `claude-sonnet-4-5-20250929` の暫定退役日（確定日ではない）
- **9/30**: Gemini の旧 `gemini-omni-flash-preview` エンドポイント廃止 ／ M365 E7 プロモーション最終日 ／ E5・E3 の CSP 割引終了 ／ 2026 Wave 1 の対象期間終了
- **9 月**: iOS 27 / macOS 27 GA ／ Claudeforce のオープンベータ（二次情報）／ Release Plans on Learn の新規掲載停止 ／ Copilot Tuning の Public Preview 再開 ／ Copilot デスクトップアプリの広範展開（中旬）／ App Store の Social Media 年齢レーティング回答が必須化 ／ OpenAI の IPO 観測
- **10/1**: Copilot Business・Enterprise の既存顧客が前払い必須に ／ Apple の EU 向け新ビジネス条件が発効 ／ CSP software の価格改定 ／ Ask Gemini in Chat のプロモーション上限が終了
- **10/2**: GitHub Copilot が Gemini 3.5 Flash / Gemini 3.6 Flash / Kimi K2.7 Code / Claude Opus 4.7 を全体験から廃止
- **10/5**: Anthropic ウェルビーイング研究助成の full proposal 提出期限（採択者）
- **10/15 以降**: `claude-haiku-4-5-20251001` の暫定退役日（確定日ではない）
- **10/16–11/11**: OpenAI DevDay Exchange 8都市（東京は 10/20）
- **10/23**: OpenAI のレガシースナップショット退役（`gpt-3.5-turbo-0125` / `gpt-4-0613` / `o1-2024-12-17` / `o4-mini-2025-04-16` とファインチューン版）
- **10/31**: OpenAI の既存 evals が読み取り専用になる
- **10 月**: Anthropic の IPO 予定（$2T 超の評価額を目標と報道）／ 韓国 App Store のコンテンツ記述子2件が All → 12+
- **秋**: Anthropic の Enterprise Frontier Safeguards が段階的に提供開始（二次情報）
- **11/15**: Microsoft の Release Planner が退役（ハイライト1参照）
- **11/21**: GPT-5.6 Sol の暫定値下げが有効とされる期限
- **11/24 以降**: `claude-opus-4-5-20251101` の暫定退役日（確定日ではない）
- **11/30**: OpenAI の Reusable prompts・Evals プラットフォーム・Agent Builder が停止
- **12/1**: OpenAI の GPT Image 系が停止（`gpt-image-1-mini` / `gpt-image-1.5` / `chatgpt-image-latest` → `gpt-image-2`）
- **12/2**: EU AI Act の生成コンテンツ標識義務、8/2 以前に市場投入済みシステムへの猶予終了
- **12/11**: OpenAI の旧スナップショット退役（`gpt-5-2025-08-07` / `o3-2025-04-16` / `o3-pro-2025-06-10` 等）
- **12/31**: Gemini 3.8 Flash と 3.7 Flash の導入価格が終了（$0.75/$3.75 → $1.50/$7.50）／ GitHub Copilot の Fable 5.1 / Fable 5 に対する ZDR 暫定免除が終了 ／ Google AI Plus 学生無償提供の申込期限
- **年内**: Anthropic の新データ保持方式（顧客自身のクラウドでの30日保持）投入予定 ／ OpenAI の Jalapeño チップの初期展開
- **2027-01-06**: OpenAI で大半のユーザーの新規ファインチューニングジョブ作成が終了
- **2027-01-20**: OpenAI の audio / realtime 系退役（`gpt-realtime` / `gpt-audio` / `gpt-4o-audio` と mini 系）
- **2027-02-05 以降 / 02-17 以降**: `claude-opus-4-6` / `claude-sonnet-4-6` の暫定退役日（確定日ではない）
- **2027-02-26**: OpenAI の文字起こし4モデル退役（`whisper-1` / `gpt-4o-transcribe` / `gpt-4o-mini-transcribe` / `gpt-4o-transcribe-diarize`）
- **2027-03-01 / 2028-10-01**: SharePoint クラシックページ退役のフェーズ1・フェーズ2
- **2027-04-16 / 05-28 / 06-09 / 06-30 / 07-24 / 09-01 以降**: `claude-opus-4-7` / `claude-opus-4-8` / `claude-fable-5` / `claude-sonnet-5` / `claude-opus-5` / `claude-fable-5-1` の暫定退役日（確定日ではない。⚠️ `claude-opus-4-7` は Copilot では 10/2 に消える）
- **2027-06-30**: Claude for Teachers の学区登録期限
- **2027年末**: Anthropic が借りる Nscale West Virginia データセンター（460MW）の稼働開始見込み
- **2028-06**: 米国 K-12 教職員向け ChatGPT for Teachers の無料提供期限

## 改善メモ

- 3ソースの当日分（01 Master / 02 Copilot / 03 industry）はいずれも取得できた。前日 09-05 分にも欠損記録はなく、欠損リカバリの対象はない
- **Release Wave 廃止は12日遅れの検知である** — 03 は Microsoft 本体の告知が Dynamics 365 ブログの 8/25 付・Message Center が MC1461529 だと記録しており、定点ソース（Partner Center の9月ページ）に載った 9/4 まで捕捉できていない。02 は 8/25 側に触れず「移行対象の線引きが一次で示されたのは本日が初めて」とだけ書く。**検知経路の差がそのまま遅延日数の差になっている**
- ⚠️ **GPT-6 Astra の Copilot 提供で 01 と 03 の粒度が割れた** — 03 は「Pro は対象外」を明示し 09-04 収録の Gemini 3.8 Flash（Pro を含む）との差を指摘するが、01 は対象プランを列挙するだけで Pro の不在に触れていない。どちらも同じ github.blog の changelog を出典としており、**記述の欠落であって矛盾ではない**
- ⚠️ **Astra の提供状況が Microsoft 側の一次内で食い違っている** — 02 は Tech Community 記事が Cowork と Copilot Studio への提供を「Available today」と書く一方、Learn のモデル可用性一覧にも Cowork のモデル一覧にも Astra の行が無いと記録する。X 上の Charles Lamanna の投稿も「初日から提供」としており、**Learn 側の一覧だけが追随していない**
- ⚠️ **Cowork のモデル一覧に編集者向けの未公開指示が残っている** — 「State which populations the GPT 5.5 (Frontier) model is available to before publishing.」等の2箇所で、公開済みページが自身の可用性記述を未確定と書いている。02 はこれを根拠に、モデルの提供開始判定を Learn のモデル一覧から Tech Community の `Available today:` 記事へ移す提案（B-059）を起票した
- **新規の改善提案は3件** — B-061（01: Anthropic の research 公表を `github.com/anthropics/<リポジトリ>` から一次確定する経路を `fetch-flow.md` に規定）、B-059（02: 上記のモデル提供開始判定の移管）、B-032（03: Microsoft のロードマップ告知の定点を Release Plans / Release Planner から AI at Work roadmap へ差し替える）
  - ⚠️ **B-032 の番号は 01 の台帳では別提案**（HF の org を `createdAt` 降順で確認する運用）に割り当てられている。09-05 に記録した B-058 の衝突に続き2日連続で、**台帳がリポジトリごとに独立しているため番号だけでは提案を特定できない**
- ⚠️ **継続提案の計数が5日連続で安定しない** — 本日は 01 が18件（最多 B-013・39回目）、02 が33件（最多 B-011・48回目）、03 が14件（最多 B-004・69回目）で計 **65件**。前日は 01: 17件 / 02: 46件 / 03: 13件の計76件で、02 が −13 と大きく振れている。01 と 03 は +1 ずつで整合しており、**振れているのは 02 の計数だけ**である
- **到達性の変化** — 02 で Microsoft Copilot Blog の RSS（`copilot-studio/feed/`）が内容ごと復旧し、`lastBuildDate` が45日ぶりに前進して 9/2 の記事を含むようになった。一方 02 は `azure.microsoft.com` をゲートウェイ拒否として新規登録し（Astra の Azure ブログ一次が読めず Learn の Foundry ドキュメントで代替）、01 は `siliconangle.com` を新規のゲートウェイ拒否として記録した。03 は障害の変化なしである
- ⚠️ **長期化している一次未読・接続障害**: Anthropic の8月 Risk Report が21日連続で一次未読（01）、`mc.merill.net` の拒否が30日連続（02）、Copilot Studio What's New への GA 未反映が34日連続（02）、Released Versions の空白が68日（02）、Copilot Tuning 一次の未更新が17日（02）、拡張機能 What's New の停止が39日（02）、`aka.ms` の拒否（02）、`pnp.github.io`（02）、`www.ppweekly.com`（02）、`learn.chatgpt.com` / xAI 一次3ホスト / Google 系5ソース / Devin 一次（01）、`www.similarweb.com` / `www.anthropic.com` ほか6ホスト（03）。いずれも解消の見込みが立っていない
- **本サマリーの生成環境について（4日連続）** — 本日の実行でも GitHub MCP のリポジトリスコープが `kit1132/05_ai-news-daily` のみに設定されており、入力3リポを MCP 経由で読めなかった。公開リポの `raw.githubusercontent.com` から読み取り専用で取得して生成した（入力3リポへの書き込みは行っていない）。⚠️ **4日連続で同じ回避を要している**ため、取得経路を raw に固定するか実行環境のスコープへ入力3リポを追加するかを決める必要がある
  - ⚠️ 03 は Claude Code のスケジュール／クラウド実行環境の不具合修正が4版連続（2.1.258〜2.1.261）だと記録し、「本ダイジェストの生成環境そのものが該当する系統」と指摘している。本サマリーの実行環境も同じ系統である
- **未解決の要 kit 対応（08-07 確定・継続）**: 08-06 追加の許可ドメイン13件は新規起動セッションでも全件未到達。① 保存先環境とスケジュールタスク実行環境の同一性確認 ② `.google` TLD 3件の個別指定確認 ③ 次回追加対象に `api-docs.deepseek.com` / `www.deepseek.com` ほかを含める
