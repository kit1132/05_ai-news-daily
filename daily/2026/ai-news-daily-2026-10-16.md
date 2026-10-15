# AI News Daily Summary — 2026-10-16

GitHub Copilot が 11/16 に Claude Opus 4.8・Opus 5・GPT-5.6 Terra を廃止すると告知した。Power Platform では Azure DevOps コネクタの旧接続が 11/30 までに認証できなくなり、Word Online (Business) コネクタの返す URL も 10/14 から認証必須になった。GitHub は code scanning の agentic autofix を GA にし、無料の Generate Fix を有料の作業に置き換えた。

## 今日のハイライト

### 1. [廃止] GitHub Copilot が 11/16 に Claude Opus 4.8・Opus 5・GPT-5.6 Terra を廃止する — Opus 系は 5.5 一本に寄せる前提になった

**要点**: GitHub が 10/15 に、Copilot の全体験から3モデルを **11/16** に外すと告知した。Opus 系で残るのは Claude Opus 5.5 だけになる。モデルを名指しで固定したワークフローや連携は、1カ月以内に差し替えないと止まる。

**詳細**: 10/19 の `gpt-5.5`・`gpt-5.4` 系廃止（既報）とは別の告知で、2回目の整理になる。

- 移行先: Claude Opus 4.8 と Opus 5 は Claude Opus 5.5 へ、GPT-5.6 Terra は GPT-6.1 Sol か GPT-6 Luna へ移る
- 例外: Opus 4.8 は年額プランの個人契約者には残る
- 管理者: Business / Enterprise では移行先が自動で有効になる。ただし管理者がグローバル既定をオフにしているか、モデルを無効化している場合はモデルポリシーで有効化が要る。廃止モデルの削除操作は不要

- https://github.blog/changelog/2026-10-15-upcoming-deprecation-of-selected-github-copilot-models-in-mid-november

### 2. [破壊的変更] 2024年9月より前に作った Azure DevOps コネクタの接続が 11/30 までに認証できなくなる — フロー・アプリ・エージェントが止まる

**要点**: MC1508508 によると、Azure DevOps コネクタの古い接続が使う旧方式のアプリ登録が削除される。削除は既に始まっていて **11/30** に完了する。2024/9/1 より前に作った接続は、作り直さない限り認証に失敗する。

**詳細**: 10/15 公開。対象サービスは Power Platform と Microsoft Copilot (Power Platform) で、通知は対象の接続がある環境にだけ届く。

- 対応: 新しい Azure DevOps 接続を作って同意を済ませ、古い接続を参照するフロー・キャンバスアプリ・エージェントを切り替える。参照がなくなったら古い接続を削除する

- https://mc.merill.net/message/MC1508508

### 3. [料金+新機能] GitHub が code scanning アラートの agentic autofix を GA にした — 無料の修正案生成が、Copilot が検証まで回して draft PR を出す有料の作業に変わった

**要点**: GitHub が 10/15 に、code scanning のアラートを Copilot に割り当てると、修正を書き、CodeQL を再実行して解消を確かめてから draft PR を出す機能を GA にした。有効にすると無料の「Generate Fix」が「Assign to Copilot」に置き換わり、AI Credits と Actions 分数を消費する。

**詳細**: 対象は GitHub Enterprise Cloud（データレジデンシー版を含む）の GitHub Code Security / GitHub Advanced Security 利用者。単価の記載は無い。

- 使い方: 既定ブランチのアラートを1件ずつ割り当てるか、一覧かセキュリティキャンペーンから最大25件を1本の PR にまとめる。REST API では `assignees` に `["copilot-swe-agent[bot]"]` を指定する
- 課金: enterprise の請求画面「AI usage」の「Advanced Security」に計上され、SKU 単位の予算を設定できる
- 有効化: enterprise 管理者が Advanced Security ポリシーの「Agentic autofix」を有効化し、org / リポジトリ管理者が Code Security 設定で有効化したうえで、Copilot の請求方法を設定する

- https://github.blog/changelog/2026-10-15-agentic-autofix-for-code-scanning-alerts-general-availability

## カテゴリ別まとめ

### Claude / Anthropic

- [新機能] **Opus 5.5 の fast mode** — Anthropic が 10/15 に、Opus 5.5 の fast mode をリサーチプレビューから外し、アクセス申請とベータヘッダーなしで全利用ティアが使えるようにした。リクエストに `speed: "fast"` を付けると出力トークン毎秒が最大2.5倍になり、単価は入力 $8・出力 $40（/1M トークン）である。Claude API（Managed Agents 含む）限定で、Bedrock・Claude Platform on AWS・Google Cloud・Foundry・Batch API・Priority Tier では使えない。Opus 5 / Opus 4.8 は $10/$50 のリサーチプレビューのまま。https://platform.claude.com/docs/en/build-with-claude/fast-mode
- [新機能] **Claude Code `2.1.301`** — Anthropic が 10/15 に出した版で、`CLAUDE_CODE_RETRY_WATCHDOG_MAX_USAGE_LIMIT_WAIT_MS` を設定すると、利用上限のリセットが遠いときに待たず終了するようになった。npm では `next` が `2.1.301`、`latest` は `2.1.300`、`stable` は `2.1.292` のままである。https://code.claude.com/docs/en/changelog
  - `fable` エイリアス: 最新モデルが組織で使えないときは1つ前の Fable に切り替える
  - モデル切り替え: 小さいコンテキストのモデルへ移ると、長い会話は前のモデルで要約してから移る
  - OpenTelemetry: `tool_decision` イベントに `classifier_verdict`・`permission_mode` が付いた
- [新機能] **Compliance API のユーザー指示取得（ベータ）** — Anthropic が Claude Enterprise 向けに、メンバーが claude.ai の「Instructions for Claude」と Cowork の「Global instructions」に書いた文面を `GET /v1/compliance/organizations/{org_uuid}/user_preferences` で取得できるようにした。既存の Compliance Access Key に `read:compliance_user_data` スコープが要る。10/14 には Managed Agents の scheduled deployments が Claude Platform on AWS でも使えるようになった。https://platform.claude.com/docs/en/release-notes/api
- [動向] **METR に社員並みの社内アクセス** — Anthropic が 10/15 に、METR のチーム6人へ社内ツールとシステムへのアクセスを与え、METR が承認なしにリスク評価を公表できる体制にした。顧客データ・弁護士秘匿特権・モデルアーキテクチャの情報は除く。SecureBio は8月の Risk Report の化学・生物兵器章を審査中で、Accenture・Faculty とは評価・red teaming の提携を詰めている。https://www.anthropic.com/news/an-update-on-independent-evaluators
  - Tier 1: 範囲を絞った調査で、公表に Anthropic の承認が要る（SecureBio）
  - Tier 2: 承認なしで公表でき、定められた分類だけ削除を求められる
  - Tier 3: 社員並みのアクセスに Tier 2 の公表権を足したもの（METR）
- [セキュリティ] **米中間選挙向けの誤用分類器** — Anthropic が 10/14 に、偽の SNS アカウントや政治ニュースサイトの作成のように、無害に見える作業に分けた多段の選挙関連の誤用を見つける分類器を Claude に追加した。10月後半からは米国の claude.ai 利用者に Democracy Works の公式投票情報を出す。9/21〜27 の米国会話25万件のうち、選挙の規約違反は約0.002%だった。https://www.anthropic.com/news/2026-us-midterms
- [据え置き] **Claude Haiku 4.5 は退役下限日の翌日も Active** — Anthropic の廃止ページは `claude-haiku-4-5-20251001` を「Not sooner than October 15, 2026」の Active のまま表示し、廃止履歴にも追加は無い。https://platform.claude.com/docs/en/about-claude/model-deprecations

### GitHub Copilot / GitHub

- **Copilot の3モデル廃止**（ハイライト参照・1）
- **agentic autofix GA**（ハイライト参照・3）
- [新機能] **HydraFusion の更新と HydraFusion Max** — GitHub が 10/14 に、複数モデルを束ねて1つの回答を返す research preview の HydraFusion を更新し、推論を深くした Max を加えた。モデルは Claude Opus 5.5・GPT-6 Astra・GPT-6.1 Sol・GPT-6 Luna から選ばれ、組織のモデルポリシーに従う。VS Code・Copilot アプリ・Copilot CLI で、Pro / Pro+ / Business / Enterprise の preview 機能を有効にすると使える。premium request の倍率は記載が無い。https://github.blog/changelog/2026-10-14-hydrafusion-updates-and-new-max-option
  - 推論の深さ: 段階ごとに決める（下書きは medium、レビューは high）
  - Cascade: 最初の結果を判定する段を挟み、必要なときだけ修正を依頼する
  - Critique: 要約よりワークスペースを調べるツールに頼り、批評役のモデルを並列に走らせる
- [新機能] **AI Scan for pull requests GA** — GitHub が 10/15 に、CodeQL が未対応の言語（PHP・Shell・Terraform・Dockerfile・JSP・Blazor）の PR 差分から脆弱性を探す機能を正式提供した。指摘は助言扱いでマージはブロックしない。公開リポジトリは無料、private / internal は Code Security か GHAS が要り、Copilot ライセンスは不要で、Code Security AI Credits で課金される。https://github.blog/changelog/2026-10-15-ai-scan-for-pull-requests-generally-available
- [新機能] **Copilot CLI `v1.0.98`** — GitHub が Copilot CLI の安定版 `v1.0.98`（10/14）を出し、Gemini 4 Argon と `/ask` の展開（Ctrl+E）・全文コピー（Ctrl+Y）を安定版に入れた。pre-release `v1.0.99-0` / `v1.0.99-1`（10/15）では、`/sandbox` をセッション単位で有効にでき、`-p` やパイプ入力向けに `--trust-folder` が加わった。https://github.com/github/copilot-cli/releases

### Microsoft 365 Copilot

- [新機能] **法務向けプラグインの GA** — Microsoft が 10/15 に、M365 Copilot の利用者が法務向けスキル20種超を Word と Cowork で使えるようにした。Roadmap 571884（GA 期日 October CY2026）が予定どおり出荷された形で、Frontier 公開以降1,800人超が約10万件の編集を生成し約7割が採用されたという。https://techcommunity.microsoft.com/t5/microsoft-copilot-blog/introducing-microsoft-copilot-for-legal/ba-p/4564246
  - Legal for Cowork: 契約の起案・赤入れ・定義語チェック・義務と期限の抽出などを、M365 Copilot の商用ライセンスで使える
  - パートナー製プラグイン: Bloomberg Law・iManage Work・NetDocuments・Docusign・Harvey・Relativity など約30社が、プラグインレジストリで同日提供を始めた
- [新機能] **メモリの引用表示** — Roadmap 574111 によると、Copilot Chat の利用者は、応答の「Sources」の Personalization タブで、応答に使われたカスタム指示・保存済みメモリ・過去のチャットを確認し、その場で削除できるようになった。メモリが有効なときだけ表示される。
- [予定] **Copilot ダッシュボードのデータエクスポート** — MC1173208 によると、全社データを閲覧できるダッシュボード利用者が、過去6か月分の利用状況をユーザー×週の単位でエクスポートできるようになる。パブリックプレビューは10月下旬までに展開を終え、GA は11月中旬〜末である。既定オンで、ユーザーはハッシュ化 ID で表され、Copilot ライセンス50以上が要る。https://mc.merill.net/message/MC1173208
- [新機能] **Viva Engage のコミュニティエージェント** — MC1155311 によると、コミュニティ管理者が、コミュニティ外の SharePoint サイトや公開 Web サイトをエージェントの回答根拠に追加できるようになった。Copilot ライセンスを持つメンバーは @メンションで呼べる（既定オン）。https://mc.merill.net/message/MC1155311
- [仕様] **拡張機能 What's New に「October 2026」節** — Microsoft が 10/15 に節を追加し、管理者が Cost Management API で支出ポリシーの作成・割り当て・閾値アラートと利用者ごとの消費の診断を行えると明記した。`getMicrosoft365CopilotUsageUserDetailByDate` は指定日の利用者単位の利用状況を返す。https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/whats-new
- [予定] **Teams の Facilitator が1か月延期** — MC1409304 によると、会議中の質問に Web 検索で答える機能は、Targeted Release が12月上旬、GA が12月中旬〜1月中旬に延びた。
- [据え置き] **Release Notes / ブログ** — M365 Copilot Release Notes の先頭は October 06, 2026 のままで、M365 / Copilot ブログ・Agent 365 Blog・M365 Developer Blog にも新規記事は出ていない。

### Copilot Studio / Power Platform

- **Azure DevOps コネクタの旧接続**（ハイライト参照・2）
- [破壊的変更] **Word Online (Business) コネクタの URL が認証必須に（10/14）** — MC1508992 によると、コネクタは 10/14 から一時的な事前認証済みダウンロード URL を使わなくなった。`CreateWordFileWithContent` が返す URL を認証なしのリンクとして渡していたフローは壊れている可能性がある。代わりに SharePoint / OneDrive の「ファイル コンテンツの取得」で中身を渡すか、テナントのポリシーに沿った共有リンクを作る。`GetSchema`・`GetFile`・`ConvertFile` は影響しない。https://mc.merill.net/message/MC1508992
- [セキュリティ+新機能] **エージェントアカウント（Frontier）** — Copilot Studio の作成者が、エージェントに Entra アカウント・メールボックス・Teams プレゼンスを持たせられるようになった（10/15 ブログ・Learn 改訂）。共有メモリは「権限のない利用者への応答にも秘密度ラベルに関係なく含まれうる」と一次に明記され、利用者はオプトアウトできず、管理者もメモリだけを止められない。https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-experience/authoring-agent-account
  - 前提: 環境のリリースサイクルが Early で、作成者に M365 E5＋Agent 365 アドオンか M365 E7 が要る。公開時にエージェント1体につき Microsoft 365 Frontier for AI Teammates ライセンスを1つ消費する
  - 有効化: M365 管理センターでエージェントテンプレートを有効にし、PPAC の Copilot > Settings で環境ごとに「Agent accounts」をオンにする
  - 制限: テナント外の人には応答せず、メールは宛先250人以下のスレッドだけに応答する。保護ラベル付き文書は読めない
- [新機能] **GitHub Copilot ハーネスのトリガーと自律エージェントの共有（preview）** — 作成者が、メール受信・SharePoint の項目作成・スケジュールなどのトリガーでエージェントを自動実行し、「Can use」リンクで他の利用者に自分の資格情報で動かさせられるようになった（Learn 10/15 改訂）。各利用者の実行分はホスト環境に合算して課金される。https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-experience/authoring-share-agent
- [予定] **Copilot Studio ブログの予告と Power Pages の暗号化 ID トークン** — Microsoft が 10/15 のブログで、作成者への改善案提示とエージェント用のブラウザー付きクラウド PC を予告したが、日付は出していない。Power Pages の OpenID Connect は暗号化 ID トークンに対応する予定で、GA は December CY2026 である（Roadmap 576395）。
- [据え置き] **What's New / Released Versions / 非推奨一覧 / 課金レート表** — Copilot Studio What's New は `ms.date` 10/5 のまま、Released Versions は 2026.6.3 のまま107日動いておらず、非推奨一覧と課金レート表の単価も変わっていない。

### OpenAI / Google / その他エージェント

- [新機能] **TypeSafe AI `jev-1.14.0`** — TypeSafe AI が 10/14 に Jev の新版を `jev-preview` で出し、`jev-latest` は1週間後に移るとした。多言語対応の伸びが最も大きく、料金は入力 $0.042 / 100万トークン・出力無料のまま。実験機能として画像入力、`box` 型、上限を 64k から 262k に広げる長文コンテキストが加わった。https://typesafe.ai/blog/jev-1-14
- [観測] **Orca `v1.4.225` のリリースが GitHub から消えた** — Stably AI の GitHub から前日掲載の `v1.4.225` のリリースとタグが消え、Latest が `v1.4.224`（10/10）に戻った。一方 `onorca.dev/changelog` には `1.4.225`（10/14）と `1.4.226`（10/15）が載っている。https://github.com/stablyai/orca/releases
- [据え置き] **Codex・OpenAI・Cursor・Google・MCP の定点** — OpenAI は Codex CLI 安定版を `0.162.1` のまま据え置き、pre-release `0.163.0-alpha.10.2` を足した。`learn.chatgpt.com` は 10/14 の GPT-5.5 退役、Cursor の changelog は 10/13、Gemini API changelog は 10/13、`blog.modelcontextprotocol.io` は 8/22 が最上位のままである。

### オープンウェイト

- [新機能] **Meta Muse Spark Open** — Meta が 10/15 に、総パラメータ 816B（アクティブ 42B）・1M コンテキストのマルチモーダルモデルの重みを Hugging Face で公開した。512GB の Mac Studio 2台で動くという。利用は無料だが「Built with Muse Spark Open」の表記が要り、年商 $20M 超の事業者が API として提供するには別契約が要る。https://techcrunch.com/2026/10/15/meta-launches-an-open-weight-model-that-runs-on-macs/
- [新機能] **Nvidia Nemotron 3.5 Super VL** — Nvidia が 10/15 に、エージェント常時稼働向けの 120B（アクティブ 12B）MoE 視覚言語モデルの重み・データセット・学習レシピを公開し、NIM でも提供した。24GB に収まる 2bit 量子化の Bolt 74B-A9B も同時に出し、llama.cpp・Ollama・vLLM などで動く。https://the-decoder.com/nvidias-nemotron-3-5-super-vl-is-an-open-model-built-to-run-enterprise-ai-agents-nonstop/

### 市場・企業

- [動向] **Anthropic の Q3 売上 $16.8B と IPO 日程** — Bloomberg・FT・CNBC が 10/14〜15 に、Anthropic が投資家に Q3 売上 $16.8B（前期比約45%増、前期は147%増）と2四半期連続の調整後黒字を示したと報じた。正式なマーケティングは早ければ11/9の週、取引開始は感謝祭（11/26）前が有力とされる。上場時評価額は $1.8兆〜$2兆と $1.5兆未満で見方が割れている。いずれも関係者情報で公式発表ではない。https://www.cnbc.com/2026/10/15/anthropics-third-quarter-revenue-hits-16point8-billion-ipo.html
- [動向] **Bank of America が AI 発見の脆弱性修正に約4,000人** — Bank of America の Moynihan CEO が CNBC に、Mythos などの AI モデルが見つけた脆弱性の修正に外部委託1,000人と社員3,000人を第2四半期から充てていると明かした。Q3 はマネロン対策とあわせて「数億ドル」を支出した。https://the-decoder.com/bank-of-america-puts-4000-people-on-fixing-vulnerabilities-uncovered-by-anthropics-mythos-and-other-ai-models/
- [据え置き] **買収協議・国内市場データ** — Amazon × Decart と Nvidia × Reflection AI の買収協議に 10/10〜11 以降の続報は無く、IDC Japan・MM総研・NRC・Business Insider Japan（10月版）も新規公表が無い。

## 直近の注目予定

- **10月中旬**: App Builder / vibe.powerapps.com で新規作成が停止し、移行機能が提供される（MC1505609）
- **10月下旬**: Copilot ダッシュボードのデータエクスポートのパブリックプレビュー展開が完了（MC1173208） ／ claude.ai（米国）で Democracy Works の投票情報を表示
- **10/15 以降**: `claude-haiku-4-5-20251001` の暫定退役日（告知はまだ無い）
- **10/19**: GitHub Copilot が `gpt-5.5`・`gpt-5.4` 系・Gemini 3.7 Flash などを廃止
- **10/21 前後**: TypeSafe の `jev-latest` が `jev-1.14.0` へ移る
- **10/22**: Copilot Business / Enterprise の機能既定有効化が発効 ／ Gemini API の Veo 3.1 プレビュー3種と `gemini-omni-flash-preview` が停止（最短日）
- **10/23**: Gemini API の `deep-research-pro-preview-12-2025` が停止 ／ OpenAI のレガシー GPT スナップショットが停止
- **10/27〜29**: PPCC 2026（ラスベガス）
- **10/30**: ChatGPT Pro 200 の Work / Codex 利用枠が変更（二次）
- **10/31**: MCP サーバー認定の旧申請経路が終了
- **11/1**: Codex の28日間「改善かリセット」の終了（二次）
- **11/4**: Entra で一般ユーザーのブループリント作成が既定オン ／ `AgentIdentity.CreateAsManager` の自動付与が停止
- **11/9 の週**: Anthropic の IPO マーケティング開始の見込み（二次）
- **11/12**: Copilot Studio の GPT-4.1 / GPT-5 系が退役 ／ Anthropic Usage Policy 改定版が発効 ／ OpenAI → Cursor のモデル供給停止予定（一次未読）
- **11/16**: GitHub Copilot が Claude Opus 4.8・Opus 5・GPT-5.6 Terra を廃止 ／ Sales Development Agent が Copilot Credits の消費を開始
- **11/17**: Gems が Gemini アプリの設定パネルへ移動
- **11/17〜20**: Microsoft Ignite
- **11月中旬〜末**: Copilot ダッシュボードのデータエクスポートが GA
- **11/24**: `claude-opus-4-5-20251101` の退役下限日（告知なし）
- **11/26 まで**: Anthropic の取引開始の見込み（感謝祭前・二次）
- **11月下旬**: Agent 365 の可観測性データがライセンス不要に（MC1506727）
- **11/30**: Azure DevOps コネクタの旧接続が認証不可に（MC1508508） ／ App Builder エージェントと vibe.powerapps.com が退役 ／ `claude-sonnet-4-5-20250929` が Claude API から退役 ／ OpenAI の Evals・`v1/prompts`・Agent Builder が停止 ／ Gemini 4 Argon の導入価格が終了
- **12/1**: Gemini 4 Argon の単価が $4/$20 に倍増 ／ Copilot Business の従量課金が既定オン
- **12月上旬**: Teams の Facilitator が Targeted Release（GA は12月中旬〜1月中旬）
- **12/14**: claude.ai/design の単体サイトが閉鎖
- **2027-01-06**: OpenAI `tts-1` / `tts-1-hd` / `gpt-4o-mini-tts` 2版が停止
- **2027-01-14**: OpenAI の GPT-4o・GPT-4o mini・GPT-4.1・GPT-4.1 mini が API から削除
- **2027-03-01 以降**: Gems 廃止（Business / Enterprise）
- **2027-04-01**: OpenAI `gpt-5.1` / `gpt-5.3-codex` / `gpt-5.4-nano` が停止
- **2027-10-15**: Purview の `Search-UnifiedAuditLog` コマンドレットが退役

## 改善メモ

- 新規提案: 3ソースとも無し
- 継続提案: Master は B-082 最上位エントリ基準の差分判定（22回目。前日未掲載だった 10/14 の Anthropic 2本を検出） ／ Copilot は B-074（docset 全件突合・本日 643ページ）・B-037（Released Versions 107日）を更新 ／ industry は3件を更新（最多 B-004・108回目）し、B-031 に Claude リリースノートの同日2エントリ取りこぼし、B-043 に Haiku 4.5 下限日翌日の確認を記録
- 障害の変化: industry で `the-decoder.com`（RSS）と `www.publickey1.jp`（Atom）が WebFetch で復旧し、`hnrss.org`・`techcrunch.com` の台帳上の復旧も記録された。Master と Copilot は変化なし
- ソース間の差分・矛盾:
  - Claude Code `2.1.301` を、Master（04:10 頃実行）は「npm の `next` に出たが changelog 最上位は `2.1.300`」として [観測] にし、industry（05:10 頃実行）は changelog の新機能つきで [新機能] にした。本サマリーは industry の changelog 内容を採り [新機能] にした
  - Compliance API のユーザー指示取得は、Master が release notes 上の日付を **October 19, 2026**（取得時点より先の日付）と記録し、industry は 10/15 としている。本サマリーは日付を書かずに載せた
  - agentic autofix と HydraFusion は Master と industry の両方に載っていた。本サマリーは agentic autofix をハイライト3、HydraFusion をカテゴリに置いた（選定基準1の廃止2件を先に採った）
  - 10/30 の ChatGPT Pro 200 の枠変更は、Master が「半減」、industry が「Plus 比10倍」で二次どうしの割れが続いている
