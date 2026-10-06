# AI News Daily Summary — 2026-10-07

OpenAI は API の有料ティアを3段階に統合し、最上位に入る条件を累計 $500 に下げた。Anthropic は Claude を Google ドキュメント / スプレッドシート / スライドの中で直接編集できるようにし、サイバー用途の Cyber Verification Program を3段階に作り直した。Microsoft は Copilot Studio の標準ハーネスのエージェントを GitHub Copilot ハーネスへ移すアップグレードを preview で出し、What's New も64日ぶりに更新した。

## 今日のハイライト

### 1. [料金] OpenAI が API の利用ティアを5段階から3段階に統合した — 最上位 Grow の条件が累計 $1,000 から $500 に下がった

**要点**: OpenAI が API の有料ティアを Tier 1〜5 から Build / Launch / Grow の3つにまとめた（10/6）。累計 $500 の支払いで月 $200,000 枠の最上位に入れるため、「本番規模のレート上限には累計 $1,000 と待機日数が要る」という見積もりの前提が変わった。

**詳細**: 既存の有料組織は新ティアへ自動で移り、操作は不要である。

- Build: 累計クレジット購入 $5 以上・月額利用上限 $500
- Launch: 累計 $100 以上・月 $5,000
- Grow: 累計 $500 以上・月 $200,000。Luna の例で 30,000 RPM・1億8,000万 TPM（Build は 5,000 RPM・200万 TPM）。モデル別の RPM / TPM は Astra / Sol / Terra / Luna ごとに異なる
- 待機日数: 旧ティアにあった「初回支払いから7〜30日」の条件は、新ガイドの到達条件から消え、累計購入額だけが挙がっている
- 無料枠: 対象地域で月 $100 上限のまま

- https://community.openai.com/t/update-to-openai-api-rate-limits/1403852
- https://developers.openai.com/api/docs/changelog
- https://developers.openai.com/api/docs/guides/rate-limits

### 2. [新機能] Claude が Google ドキュメント / スプレッドシート / スライドの中で直接編集できるようになった — Google ファイルは「貼って読ませるもの」から「その場で書き換えるもの」になった

**要点**: Anthropic が Claude for Google Workspace アドオンと、Docs / Sheets / Slides のコネクタを公開ベータで出した（10/6）。対象は Pro / Max / Team / Enterprise の有料全プランで、Claude がファイルの中で選択範囲を読み、直接編集するか修正案を承認カードで出す。

**詳細**:

- アドオン: ファイル横のサイドバーで Claude を開く
- コネクタ: Claude のチャットからリンクを渡すか新規作成を頼むと、Google ファイルを作成・編集する
- できること: Docs は文の修正・見出しの書式・提案カード、Sheets は数式・ピボット・Python でのデータ整形、Slides はデッキのテーマに合わせたスライド作成と要素の重なり検出
- 編集の承認: 既定は「Ask before edits」（都度承認）で、「Accept all edits」で自動適用に切り替えられる
- 管理: Team / Enterprise はオーナーがコネクタを有効にする必要がある。Enterprise は Compliance API・顧客管理の暗号鍵・OpenTelemetry の監査エクスポートに対応する

- https://claude.com/resources/articles/claude-now-works-in-google-docs-sheets-and-slides

### 3. [新機能] Copilot Studio の標準ハーネスのエージェントを GitHub Copilot ハーネスへ移すアップグレードが preview で出た — 移行は「作り直し」から「コピーと移行レポート」になった

**要点**: Microsoft が新設ページで、Copilot Studio のホーム画面に「upgrade my ○○ agent」と指示すると標準ハーネスのエージェントを GitHub Copilot ハーネス側にコピーする手順を公開した（`ms.date` 10/5）。ナレッジソース・Power Fx・子エージェントは移らず、実行でもクレジットを消費する。

**詳細**: 新設ページ `upgrade-to-github-copilot-from-standard-harness`（`updated_at` 10/6 19:03Z・`9a7067b8`）で、過去のダイジェストに掲載歴は無い。

- 移行されるもの: 指示・ツール・推奨プロンプト。カスタムトピックはワークフローのスキルとして作り直せる
- 移行されないもの: ナレッジソース、Power Fx 式、子エージェント
- 結果: 新しいエージェントは名前に「(Upgraded)」が付いたカードで表示され、移行済み・要対応・スキップの3区分のレポートが出る。元のエージェントはそのまま残る
- 同じコミットで `switch-experiences` / `unified-authoring-conversion` / `agents-overview` / `memory-overview` なども再ビルドされた（`ms.date` は据え置き）

- https://learn.microsoft.com/en-us/microsoft-copilot-studio/upgrade-to-github-copilot-from-standard-harness

## カテゴリ別まとめ

### Claude / Anthropic

- **Google Docs / Sheets / Slides 対応**（ハイライト参照・2）
- [セキュリティ+新機能] **Cyber Verification Program の3段階化** — Anthropic が CVP と Project Glasswing を統合し、一般提供モデルでは遮断されるサイバー作業を審査済み組織に段階的に開放するようにした（10/6）。対象モデルは Opus 5.5 / Sonnet 5.5 / Mythos 5.1 と今後のモデルで、Mythos は Glasswing 参加組織だけの枠から申請で入れる階層に変わった。
  - Defense Access: SOC・インシデント対応・マルウェア解析・脆弱性の検証。企業や自治体の防御チーム、OSS メンテナー、脆弱性報告の実績がある個人も対象で、審査は数日
  - Red Team Access: 許可された対象へのペネトレーションテストとレッドチーミング。組織限定で審査は数週間。ランサムウェア展開など物理被害につながる操作は引き続き遮断する
  - Specialized Access: 航空・電力網・通信・銀行間送金などの安全系を試験する組織向けで、米国政府と共同で審査する。Glasswing の既存参加組織はここへ移る
  - 条件: 悪用監視のためのデータ保持が必須。今秋提供予定の Enterprise Frontier Safeguards（EFS）までは、ZDR で Fable 5.1 / Mythos 5.1 を使う組織に限り ZDR のまま使える
  - 評価と実績: CyScenarioBench で Red Team Access は遮断0件・34件成功（安全装置なしの 67.6% と同等）。Glasswing 参加組織は4〜7月に検証済み脆弱性を少なくとも12.9万件見つけ、うち3.3万件超が critical / high だった
  - https://www.anthropic.com/news/cyber-verification-program
  - https://claude.com/resources/articles/how-comcast-booz-allen-use-claude-mythos-to-secure-their-codebases
- [セキュリティ+新機能] **Claude Code 2.1.292** — Anthropic が Claude Code `2.1.292` を npm の `latest` に出し、PreToolUse フックの承認と auto mode がネットワーク（UNC）パスからのファイル読み取りで権限プロンプトを迂回していた問題を修正した（10/6 17:10 UTC）。
  - `claude plugin install --marketplace <source>`: マーケットプレイス追加とインストールを1コマンドで行う
  - Agent ツールの `effort` パラメーター: サブエージェントを指定した effort で動かせる
  - `CLAUDE_CODE_OVERLOADED_RETRY_BASE_DELAY_MS`: 529 の再試行の基準待ち時間を延ばせる
  - `HTTPS_PROXY` 設定時に `NO_PROXY` が無視される問題と、128字超の MCP ツール名で全リクエストが失敗する問題も直った
  - https://code.claude.com/docs/en/changelog
- [新機能] **Claude Code 2.1.290 / 2.1.291** — Anthropic が前日 `next` だった `2.1.290` の内容を changelog に載せた。`claude attach <name>` / `claude logs <name>` でセッション名の一部を ID の代わりに使えるようになり、`/claude-api managed-agents-onboard` で Managed Agents の構成を `ant apply` 用ファイルに起こせるようになった。`@` メンションや貼り付け画像のパスに Read の deny ルールが効かなかった問題、WebFetch が10万字超の本文を黙って落とす問題も直った。`2.1.291`（10/6 03:32 UTC）は回帰修正2件のみで、`stable` は `2.1.285` のまま。https://www.npmjs.com/package/@anthropic-ai/claude-code
- [新機能] **Claude Startups プログラムの拡大** — Anthropic が、設立5年以内または直近2年に資金調達したスタートアップに最大 $7,000 相当を出すようにした（10/6）。内訳は Claude Team の1年無料（Premium 5席・$6,000 相当）と API クレジット $1,000 で、提携ツール割引（合計最大 $45,000 相当）の Claude Startup Stack と Applied AI チームのオフィスアワーも加わった。https://claude.com/resources/articles/were-expanding-the-claude-startups-program-to-help-founders-build
- [動向] **Opus 5.5 のエラー率上昇** — Anthropic の API で、Claude Opus 5.5 へのリクエストのエラー率が 10/6 12:24〜12:43 UTC に上昇し、解消した。https://status.claude.com/incidents/ch27pb90bn85
- [据え置き] **API release notes・退役ページ** — Anthropic の API release notes は 10/1 の Models API `line` フィールド、モデル退役ページは 9/30 の Sonnet 4.5 が最新のままである。`claude-haiku-4-5-20251001` は Active・「Not sooner than October 15, 2026」のままで、`support.claude.com` のリリースノートも 9/28 が最上位である。

### OpenAI / Codex / ChatGPT

- **API 利用ティアの3段階化**（ハイライト参照・1）
- [新機能] **API の HIPAA 設定フロー** — OpenAI が API の Organization settings > General から標準の BAA に同意して HIPAA 対応を有効化できるようにした（10/5・1日遅れで捕捉）。対象は eligible な組織の管理者で、対象条件は changelog に書かれていない。従来は `baa@openai.com` へのメール申請で1〜2営業日かかるとする解説が多く、API の BAA は ChatGPT をカバーしない（二次）。https://developers.openai.com/api/docs/changelog / https://aptible.com/hipaa-compliant-ai-tools/openai-baa
- [料金] **Codex Auto-Review の無料化（28日間企画の2日目）** — OpenAI が Codex / ChatGPT Work の Auto-Review を ChatGPT にサインインした全利用者に無料で開放し、プランの利用枠を消費しないようにした（10/6）。主エージェントの操作を副エージェントが確認して高リスクな判断を止める機能で、設定 → Permissions → Auto-review で有効にする。https://community.openai.com/t/free-auto-review-day-2-of-28-days-of-quality-of-life-improvements-or-a-full-reset/1403525
- [仕様] **サブスクリプション推論の約50%高速化（同1日目）** — OpenAI が GPT-6 Astra と GPT-6.1 Sol のサブスクリプション経由の推論を約50%速くした（10/5）。Sign in with ChatGPT を使う OpenCode / Pi / Amp / Devin にも効く。前日の本サマリーは宣言の投稿だけを扱っており、1日目の中身はこれだった。https://community.openai.com/t/free-auto-review-day-2-of-28-days-of-quality-of-life-improvements-or-a-full-reset/1403525
- [版更新] **Codex pre-release** — OpenAI が Codex の pre-release を `0.162.0-alpha.16`（10/5 21:37）と `0.161.0-alpha.13.1`（10/6 05:27）まで進めた。安定版は `0.160.1` のまま。https://github.com/openai/codex/releases
- [据え置き] **changelog・退役ページ** — `learn.chatgpt.com` の changelog は 10/5 の Codex CLI 0.160.1、API 退役ページは 10/1 の2件が最上位のままである。

### Google

- [新機能] **`google/embeddinggemma-2` の公開** — Google の Hugging Face org に `google/embeddinggemma-2` が公開状態で現れた（`createdAt` 9/14・`lastModified` 10/6、非 gated、Apache-2.0、約7.4億パラメーター、feature-extraction）。非公開で作成して後日公開したとみられる。前日先頭だった `google/DiarizationLM-Gemma-4-E4B-v1` は 401 を返し一覧から消えた。https://huggingface.co/google/embeddinggemma-2
- [据え置き] **Gemini API changelog・無料枠の報道** — Google の Gemini API changelog に新しいテキストモデルは無く、10/6 付は画像生成モデルの GA で対象外である。Gemini アプリ無料枠の Flash-Lite 限定（10/9 発効の報道）は一次がまだ確認できていない。https://ai.google.dev/gemini-api/docs/changelog

### GitHub Copilot / GitHub

- [新機能] **Copilot CLI v1.0.92** — GitHub が Copilot CLI の安定版 `v1.0.92` を出した（10/5）。設定を操作する `copilot config` サブコマンドと環境切替、Git 操作時のサンドボックス内での認証情報マスク、MCP サーバー接続の安定化が入り、クォータ表示が現在の請求期間に合うようになった。pre-release `v1.0.93-2`（10/6）では、エンタープライズの `permissions.limitTo` でネットワーク要求の宛先ドメインを管理側で縛れるようになった。https://github.com/github/copilot-cli/releases
- [新機能] **シークレットスキャンの検出対象と AI Scan の導入状況** — GitHub がシークレットスキャンに Lovable・Pydantic（Logfire・AI Gateway）・Supabase のトークン検出を加えた（10/5）。10/6 には Enterprise Cloud のセキュリティ概要で、プルリクエスト向け AI Scan を有効にしたリポジトリ数を一覧・CSV で確認できるようにした。https://github.blog/changelog/2026-10-05-secret-scanning-adds-detectors-for-lovable-supabase-and-more / https://github.blog/changelog/2026-10-06-code-scanning-ai-scan-enablement-status-in-security-overview
- [据え置き] **Copilot changelog** — GitHub の Copilot ラベルの changelog は 10/2 の code review API 対応が最上位のままである。

### Microsoft 365 Copilot / Copilot Studio / Power Platform

- **標準ハーネスからのアップグレード**（ハイライト参照・3）
- [新機能] **Copilot Studio What's New の August / September 節** — Microsoft が What's New に2節を加え（`ms.date` 10/5）、7月節以来64日続いた告知面の空白が解消した。9月節の6項目のうち次の3つは初出である。
  - 抽出ノード: ワークフローで請求書・契約書・財務諸表などから名前付きの値と表を取り出す。PDF / Word / Excel / PowerPoint に対応し、GitHub Copilot ハーネス側の機能で UBB の対象になる
  - コンテンツ安全性: 評価のテスト方法に加わった。憎悪・性的・暴力・自傷の種別ごとに合否のしきい値を 0（最も厳格）〜7 で設定する
  - Dataverse ナレッジ: 1ソースにテーブルを15個まで追加でき、preview で複数行テキスト・ファイル列の非構造化検索が加わった。検索インデックスの作成には Dataverse の容量コストが追加でかかる
  - https://learn.microsoft.com/en-us/microsoft-copilot-studio/whats-new
- [仕様] **会話テストセットの上限** — Microsoft が Copilot Studio の評価ページ9本を同一コミットで改訂し、会話テストセットは1セット20件まで、1件あたり最大12メッセージ（6往復）と明記した。作成方法はクイック生成・ナレッジやトピックからの生成・テストチャットの変換の3つで、テスト結果は89日間保持される。https://learn.microsoft.com/en-us/microsoft-copilot-studio/analytics-agent-evaluation-multi-turn
- [観測] **差分を特定できない改訂** — Microsoft が Copilot Studio の `requirements-quotas` / `generate-document-output-prompt` / `govern-credit-consumption`、M365 の `user-subscription-license-usage-based-billing`、Power Platform の `important-changes-coming` を 10/5〜10/6 に改訂した。公開ミラーで旧版と比較できず差分は特定できていない。USL ページには「上限到達時に UBB へ切り替えるか Auto に戻るかを選ぶ」流れが coming soon と書かれ、非推奨一覧の `## ` 見出しは94本のままである。https://learn.microsoft.com/en-us/microsoft-365/copilot/user-subscription-license-usage-based-billing
- [据え置き] **Release Notes・Roadmap・Power Platform の定点** — M365 Copilot Release Notes の先頭は September 23, 2026 のままで、Roadmap の 10/5 起票4件は SharePoint / OneDrive / Dynamics 365 のみで対象外だった。Power Platform の親 RSS は 10/1 が先頭、Release Wave は 9/3 のまま、Copilot Studio の最新ビルドは 2026.6.3 のまま98日である。

### Cursor / その他エージェント

- [予定] **Reflection AI の Beam** — Reflection AI が初のオープンウェイトモデル Beam（総5,010億・アクティブ230億パラメーターの MoE）を発表した（10/5）。コーディングとエージェント向けで、中国系オープンモデルと同等の推論性能を3〜4分の1の計算量で出すと主張している（自社申告）。現時点はウェイトリストの限定提供で、重みは10月中に Apache 2.0 で公開する予定である。https://techcrunch.com/2026/10/05/reflection-debuts-beam-a-open-weight-ai-model-to-rival-chinese-models-at-lower-compute-cost/
- [据え置き] **Cursor・xAI・MCP・Hugging Face** — Cursor の changelog は 9/23、フォーラム Announcements は 9/21 が最上位のままで、xAI の新しい発表も見つからない。`blog.modelcontextprotocol.io` は 8/22 が最上位で、Google 以外の登録7 org に新規リポジトリは無い。

### 業界・市場

- [動向] **Atlassian と OpenAI の提携拡大** — Atlassian と OpenAI が、GPT-6 Astra と GPT-5.6 系を Rovo のエージェントと Atlassian 基盤に載せる提携拡大を発表した（10/6）。ChatGPT から Jira・Confluence・Bitbucket・Loom の内容を権限の範囲で検索・要約できるようにするなど4件の連携を含む。VentureBeat は利用額のコミットメントを伴うと報じたが金額は出ておらず、Rovo は Gemini も使うマルチモデルのままである。https://openai.com/index/atlassian-partnership/ / https://venturebeat.com/orchestration/atlassian-deepens-its-openai-partnership-with-a-spend-commitment-but-its-platform-stays-firmly-multi-model
- [据え置き] **市場データ** — IDC Japan・MM総研・NRC・Similarweb はいずれも新規公表が無く、Similarweb の9月分トラッカーも未検知のままである。

## 直近の注目予定

- **10/7**: GHE.com が X25519 単独の TLS 接続を拒否
- **10/9**: Gemini アプリの無料ユーザーが Flash-Lite のみ、AI Plus が Pro を失う（報道）
- **10/13**: Gemini アプリで skills の展開開始 ／ Office / Project / Visio LTSC 2021 のサポート終了 ／ 新しい Copilot の Partner Digital Airlift
- **10/14**: GitHub SSH の新規 RSA 鍵が 3072 ビット以上必須に ／ GPT-5.5 が ChatGPT / Codex から退役 ／ Anthropic の pre-IPO investor day（報道）
- **10/15 以降**: `claude-haiku-4-5-20251001` の暫定退役日（告知はまだ無い）
- **10月**: Copilot Chat の UBB モデル選択 GA（571400） ／ Copilot Studio エージェントがコスト管理の対象に ／ スキルカタログ GA（571880） ／ 自己学習 GA（570432） ／ Reflection AI Beam の重み公開（予定）
- **10/19**: GitHub Copilot が5モデルを廃止 ／ Workspace の skills 展開開始（Scheduled Release）
- **10/21**: GitHub Copilot の新機能既定ポリシーの設定期限（10/22 発効）
- **10/23**: OpenAI のレガシースナップショット12件が停止
- **10/27〜29**: PPCC 2026（ラスベガス）
- **10/30**: ChatGPT Pro 200 の Work / Codex 利用枠が半減（二次）
- **10/31**: MCP サーバー認定の旧申請経路が終了 ／ OpenAI Evals が読み取り専用化
- **11/1**: Codex の28日間「改善かリセット」の終了（二次）
- **11/2**: GitHub Actions の `pull_request_target` 既定無効化が公開リポジトリで強制開始
- **11/4**: GitHub SSH `ssh-rsa` の1回目のブラウンアウト
- **11/12**: OpenAI → Cursor のモデル供給停止予定（一次未読）
- **11/15**: Microsoft Release Planner 退役
- **11/17**: Gems が Gemini アプリの設定パネルへ移動
- **11/17〜20**: Microsoft Ignite
- **11/30**: `claude-sonnet-4-5-20250929` が Claude API から退役 ／ OpenAI の `v1/prompts`・Evals・Agent Builder が停止
- **12/1**: Copilot Business の従量課金が既定オン
- **12/31**: Gemini 3.8 Flash の導入価格が終了 ／ 非営利向け M365 Copilot の併用プロモーション終了
- **2027-01-06**: OpenAI `tts-1` / `tts-1-hd` / `gpt-4o-mini-tts` 2版が停止
- **2027-03-01 以降**: Gems 廃止（Business / Enterprise）
- **2027-04-01**: OpenAI `gpt-5.1` / `gpt-5.3-codex` / `gpt-5.4-nano` が停止

## 改善メモ

- 新規提案: 3ソースとも無し
- 継続提案: Master は B-035 npm dist-tags（52回目）・B-079 HF の ID 集合差分（6回目）・B-082 最上位エントリ基準の差分判定（13回目）を再確認 ／ Copilot は B-074（docset 全件突合・1,502ページ）・B-076（差分特定不可・4ページ）・B-037（98日）・B-063（`Microsoft365CopilotBlog` の board RSS が `<item>` ゼロ）を更新 ／ industry は2件を更新（最多 B-004・99回目）。B-031 に OpenAI changelog 10/5 分（HIPAA 設定フロー）の取りこぼしを追記
- 障害の変化: industry が `alphasignal.ai` / `siliconangle.com` を新規ゲートウェイ拒否として記録した。Master・Copilot は無し
- ソース間の差分・矛盾:
  - Cyber Verification Program は Master が [セキュリティ+新機能]、industry が [新機能] で割れた。一般モデルのセーフガードを審査済み組織に外す内容が主旨のため [セキュリティ+新機能] に揃えた
  - API ティアの3段階化は Master・industry とも [料金] でハイライトにしていた。Master は HIPAA 設定フローを同じハイライトの詳細に、industry は別ハイライトに置いていたため、1項目1リリースとして HIPAA を OpenAI カテゴリの別項目に切り出した
  - Claude Code は industry が 2.1.290〜2.1.292 を1項目にまとめ、Master は 2.1.292 と 2.1.290 / 2.1.291 を分けていた。1項目に2つのリリースを同居させないため Master の分け方を採った
  - Copilot Studio のハイライトは Copilot が What's New 9月節とアップグレード手順の2件を挙げていた。3件の枠のため、操作が当日から変わるアップグレード手順をハイライトに残し、What's New はカテゴリへ置いた
