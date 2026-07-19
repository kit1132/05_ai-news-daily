# AI News Daily Summary — 2026-07-20

> 本サマリーは 01_ai-news-Master・02_ai-news-Copilot・03_ai-news-industry の3ソース（7/20分）を統合して作成。

週末明けの静かな月曜。開発ツール側の新規は **Claude Code v2.1.215**（`/verify`・`/code-review` の自動実行を廃止）のみで、Microsoft 一次情報源は全て据え置き（明日 7/21 火が Copilot Studio 版ページ更新の要監視日）。一方でインフラ・規制・資金の動きが厚く、**EU が Google に Android と検索データの競合AI開放を命令**、**NVIDIA×Noetra が経産省 FRONTia の「国家AIファクトリー」（140MW・Rubin GPU 2.75万基・5年で最大約1兆円）**を発表、**Fireworks AI が $15億 Series D（評価額$175億）**。Anthropic 側では **Fable 5 の無償枠が本日 7/20 以降は前払いクレジット従量課金へ移行**し、Enterprise Admin API のユーザー管理が beta 提供開始。**Gemini 3.5 Pro GA は3度目の目標日も逸失**で未ローンチ継続。

## 今日のハイライト

### 1. EU、Google に Android と検索データの競合AI開放を命令 — 第三者AIアシスタントが「Hey Google」同等の音声起動・アプリ横断を獲得 — モバイルAIエージェントの前提が動く

**事実**: 欧州委員会が拘束力ある2措置を採択し、競合AIサービスに「Gemini と同等の Android 機能アクセス」を開放するよう Google に命令（7/16）。第三者AIアシスタントを「Hey Google」同様に音声起動でき、配車予約・返信提案・訪問地情報提供などアプリ横断タスクを実行可能にする必要がある。

**根拠**: 検索データ共有は2027年1月、Android の AI 機能開放は2027年7月からユーザーに到達見込み。EU 成人の6割が Android を利用しており、Anthropic / OpenAI のスマホ上エージェント展開の余地が制度面で広がる。

**影響**: プラットフォーム規制の変化として、モバイルAIアシスタント選定の前提が動く。Google の垂直統合（Gemini×Android×検索）が崩れ、フロンティア勢がモバイルの一等地に音声・横断アクセスで参入する道が開く。実装は2027年と先だが、製品ロードマップの前提に織り込むべき構造変化。

**行動指針**: モバイル/エンドユーザー向けAIアシスタント戦略の中期前提として押さえる。2027年の実装タイミング（検索データ 1月・Android AI 7月）を監視し、Anthropic/OpenAI 側の対応発表を追う。

- https://www.semafor.com/article/07/17/2026/eu-orders-google-to-open-android-ai-system-to-rivals
- https://www.macrumors.com/2026/07/16/eu-google-ai-apps-android-access/

### 2. NVIDIA×Noetra、世界初の国家AIインフラ — 140MW・Rubin GPU 2.75万基（経産省 FRONTia、5年で最大約1兆円） — 主権AI／国産オプションの根拠が具体化

**事実**: NVIDIA と国策AI企業 Noetra が、140MW・NVIDIA Rubin GPU 27,500基＋Vera CPU 13,750基の「国家AIファクトリー」を構築（Vera Rubin NVL72・Spectrum-X 接続）。経産省「FRONTia プロジェクト」の計算基盤として、ロボティクス/デジタルツイン/産業自動化向けのオープン多モーダル基盤モデルを学習し、学習済み重みは国内開発者へ広く共有する。

**根拠**: 6/30 に NEDO 公募採択、FY2026-2030 で初年度3,873億円・5年で最大約1兆円。建設は2027年4月着工・稼働2028年6月予定。SoftBank/Sony/NEC/Honda が中核、44社超が参画。7/1 始動の Noetra の計算基盤詳細が判明した形。

**影響**: 「フロンティア級のオープン多モーダル基盤モデルを国産インフラで学習し重みを国内共有」という主権AIの具体像。EU-Google 命令（ハイライト1）や WAIC のオープンソースAI旗振りと同じく、コストと主権の議論を国家インフラ単位で押し上げる。国内開発者にとっては将来の学習済み重み受領先が一つ増える。

**行動指針**: 主権AI／国産モデル選択肢を検討する提案の一次材料として保管。2028年稼働に向けたモデル/重み公開条件を継続監視する。

- https://www.tomshardware.com/pc-components/gpus/nvidia-and-japans-noetra-consortium-to-build-140mw-rubin-ai-factory-with-27500-gpus
- https://blogs.nvidia.co.jp/blog/japan-government-industrial-leaders-and-nvidia-launch-the-worlds-first-national-ai-infrastructure/

### 3. Claude Code v2.1.215 — `/verify`・`/code-review` の自動実行を廃止、明示呼び出しへ — 既定ワークフローが変わる、要設定見直し

**事実**: 7/19 に Claude Code v2.1.215 が着地。ワークフロー影響の大きい変更として、これまで Claude が自動起動していた verify / code-review スキルが自動実行されなくなり、今後は `/verify`・`/code-review` で明示的に呼び出す方式に変更。あわせて `dir/**` 単一セグメント allow ルールが配下ツリー全体の書き込みを誤承認する不具合を修正（前日 2.1.214 のネスト allow ルール修正に続く権限強化）。

**根拠**: Bash パーミッションチェックを複雑なコマンド構文でフェイルセキュアに、OpenTelemetry ログにメッセージ単位の相関属性を追加。Windows PowerShell 5.1 ブロック環境での `/background` エラー、シェルモード中のパス入りコマンド実行不具合、`/ultrareview` の PR URL 拒否問題も修正。Master／Copilot 両ソースが一致して報告。

**影響**: 自動でかかっていた検証・レビューが走らなくなるため、これらに依存していたユーザーは品質ゲートが素通りする恐れがある。権限系の誤承認修正は前日からの連続で、ローカル運用者はセキュリティ面でも更新価値が高い。

**行動指針**: Claude Code 利用者は v2.1.215 へ更新し、verify/code-review を CI やコミット前フローに明示的に組み込む運用へ切り替える。`dir/**` 系 allow ルールを使っている構成は権限範囲を再確認する。

- https://code.claude.com/docs/en/changelog
- https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md

## カテゴリ別まとめ

### Anthropic / Claude
- **Claude Code v2.1.215**（ハイライト参照）
- **Fable 5 が前払いクレジット運用へ移行**: 7/19 23:59 PT で無償提供と週次上限ブースト特典が終了。7/20 以降は前払いクレジット（$10/$50）利用に変更され、通常の使用上限が復帰する。モデル仕様は変更なし。「compute が整い次第サブスク復帰」方針は不変。Fable 5 常用ワークフローは本日以降コスト構造が変わるため、月次コストの再見積もりが必要。
  - https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5
- **Claude Enterprise Admin API のユーザー管理が beta 提供開始**: Enterprise 組織のメンバーを API から管理可能に（一覧検索・ロール変更・削除・招待管理・グループ管理）。グループ／カスタムロール系リクエストに `anthropic-beta: ce-user-management-2026-07-13` ヘッダーが必要。
  - https://platform.claude.com/docs/en/manage-claude/admin-api
- **Anthropic Reflect ダッシュボード（ベータ）**は 7/19 既報。**Opus 4.1 の Claude API 提供終了は 8/5**。

### Google / DeepMind
- **Gemini 3.5 Pro GA — 未ローンチ継続**: I/O 2026 発表後、3度目の目標日を逸失。Vertex AI 限定 preview のみで、GA は Gemini 3.5 Flash のみ。月末〜8月上旬の実ローンチを監視中。
  - https://www.cometapi.com/gemini-3-5-pro-release-date-rumored-specifications-all-we-know-in-2026-updated-july-2026/

### Microsoft / GitHub（一次情報源は据え置き）
- **Copilot Studio - What's New**: June 2026 セクションのまま（7月セクション未公開）。
- **M365 Copilot Release Notes**: 「July 15」バッチが最新のまま。次バッチは隔週傾向で 7/29 前後見込み。
- **Power Platform Released Versions**: Copilot Studio Build **2026.6.3（6/30初出）が最新のまま**、リージョン分布も無変化。版ページは毎週火曜更新のため、**次回 7/21 が 2026.7.x 反映の要監視日**。
  - https://learn.microsoft.com/en-us/power-platform/released-versions/copilotstudio

### OpenAI / 開発ツール
- **OpenAI 初のハードウェア「Codex Micro」**: コーディングエージェント Codex 操作用の $230 キーボードを発表（Work Louder 共同設計、7/15）。13スイッチ、状態表示の発光「Agent Keys」、推論量調整ダイヤル、ワークフロー起動用ジョイスティック、Bluetooth/USB-C。「複数のAIコーディングエージェントの艦隊管理」を物理UI化する試みで、Apple との営業秘密訴訟のさなかでの初ハード投入。限定生産・今月中出荷。
  - https://techcrunch.com/2026/07/15/amid-hardware-legal-battle-openai-releases-a-230-keyboard-for-codex/
- **OpenAI Codex CLI**: alpha は 0.145.0-alpha.24（7/18）、安定版は 0.144.6 据え置き。GitHub Copilot CLI（v1.0.71）、Cursor（3.11）ともに新規リリースなし。

### 規制・政策
- **EU、Google に Android/検索データ開放を命令**（ハイライト参照）

### 資金・資本
- **Fireworks AI が $1.5B Series D（評価額$17.5B）**: Nvidia 出資の Fireworks AI が $15.05億 Series D、評価額$175億（主導 Atreides / Index / TCV）。ARR $10億超（前年比5倍）・日次40兆トークン処理、うち95%超が顧客の独自データに特化させたオープンモデル。「汎用クローズドモデルを特化＋低コスト＋高速で置換」路線が$100億超評価を獲得。あわせて 8090 Labs が $135M Series A（Salesforce Ventures 主導）を調達。
  - https://www.cnbc.com/2026/07/16/fireworks-nvidia-cloud-ai-startup-value.html
- **DeepSeek、中国本土IPOを準備**: 年末〜2027年初に申請予定、プレマネー評価額 最低4,800億元（約$710億）の新ラウンドも協議（Bloomberg 7/14）。Anthropic（10月観測）・OpenAI（2027）と米中フロンティアのIPO競争が並走。
  - https://www.bloomberg.com/news/articles/2026-07-14/deepseek-mulls-new-funding-weeks-after-7-billion-round-ft-says

### 主権AI・国産基盤
- **NVIDIA×Noetra 国家AIファクトリー（FRONTia）**（ハイライト参照）

## 直近の注目予定

- **7/21（火）**: Copilot Studio 版ページ次更新 — 2026.7.x 反映見込みの要監視日
- **7/23**: OpenAI computer-use-preview 提供終了
- **7/27**: Kimi K3 オープンウェイト公開予定
- **7/29前後**: M365 Copilot Release Notes 次バッチ見込み
- **7/30**: M365 Copilot メモリ活用のエージェント提案 GA 予定
- **7/31**: Devin classic 環境設定 read-only 参照終了
- **8/1**: 対象フロンティアモデルの大統領令60日期限
- **8/3**: 旧「Claude in Slack」提供終了
- **8/5**: Opus 4.1 Claude API 提供終了
- **8/9**: ChatGPT Atlas 提供終了
- **8/26**: OpenAI Assistants API 廃止
- **8/31**: Sonnet 5 プロモ価格終了
- **9月**: iOS 27 / macOS 27 GA
- **2027年1月/7月**: EU-Google — 検索データ共有（1月）／Android AI 機能開放（7月）
- **2027年4月/2028年6月**: FRONTia 国家AIファクトリー 着工（2027/4）／稼働（2028/6）

## 改善メモ

- 3ソースとも新規提案・障害の変化なし。継続項目: Copilot 側 B-005「Qiita RSS の WebSearch 化」6回目、industry 側 B-004「WebSearch 優先化」21回目（詳細は各リポの IMPROVEMENT-BACKLOG.md）。
- Gemini 3.5 Pro の仕様・価格・GA日は全て報道／噂ベース。公式 launch post 確認後に更新する。
- Fireworks AI / DeepSeek / FRONTia の評価額・投資額は各報道ベース。一次発表（S-1・公募資料等）での確定は追って確認する。
- Microsoft 一次情報源は 7/19 から据え置き。次回検証は 7/21（火）の Copilot Studio 版ページ更新で実施予定。
