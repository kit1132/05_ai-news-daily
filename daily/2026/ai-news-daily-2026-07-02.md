# AI News Daily Summary — 2026-07-02

> 本サマリーは 01_ai-news-Master・02_ai-news-Copilot・03_ai-news-industry の3ソース（7/2分）を統合して作成。

## 今日のハイライト

### 1. Fable 5 / Mythos 5 の輸出規制が解除 — 7/1 に Fable 5 がグローバル復帰、約3週間のサーガ決着

**事実** 米商務省（Lutnick長官署名）が 6/30 に Fable 5 / Mythos 5 への輸出規制を解除。Anthropic は 7/1（15:31 ET）に Fable 5 を Claude Platform / Claude.ai / Claude Code / Claude Cowork で**全世界再展開**した。Mythos 5（同一基盤・安全制約が緩い版）は 6/26 承認の米組織（Annex A）に加え、今回さらに再展開。6/12 の BIS 指令による全世界停止から約3週間ぶりの復旧。

**根拠** 発端は Amazon 研究者が 6/12 に報告した Fable 5 のジェイルブレイク（脆弱性発見・悪用コード生成）。米政府・Amazon との精査の結果、Anthropic は「Fable 5 の safeguard にとって境界事例」「Mythos 級の固有サイバー能力は露出せず」と結論し、安全分類器を再訓練。当該手法を**99%超のケースでブロック**する。副作用としてコード/デバッグ系 benign リクエストの誤検知（フラグ）が増える、安全側に振ったトレードオフで、ブロック時は要求を自動で **Opus 4.8 にフォールバック**する設計。

**影響** フロンティア3モデルの「7月待ち」構図のうち Anthropic 分が決着。ただし**利用条件は要注意**——7/7 までは Pro/Max/Team/一部Enterprise で週次利用上限の最大50%まで「込み」で利用可、7/7 以降は従量課金（usage credits）へ移行。**標準Enterpriseシートは猶予枠なし・初日からクレジット課金**（未有効だと利用不可）。API直販レートは入力 $10 / 出力 $50（per 1M）で、Fable 5 は Opus 4.8 より利用枠の消費が速い。

**行動指針** Fable 5 依存ワークフローは復旧を前提に再開できるが、7/7 の従量課金移行前に usage credits の有効化とコスト試算（Opus 4.8 比で枠消費が速い点を織り込む）を済ませる。Enterprise 標準シートは初日からクレジット必須のため事前準備を優先。次の節目は 7/8 施行の政府発行ID・生体情報検証ポリシー（復旧後の本人確認運用に影響しうる）。

- https://www.anthropic.com/news/redeploying-fable-5
- https://www.coindesk.com/tech/2026/07/01/anthropic-restores-ai-models-fable-mythos-after-the-u-s-lifts-export-controls
- https://www.nbcnews.com/business/business-news/commerce-department-gives-green-light-anthropic-bring-back-fable-5-rcna352501
- https://venturebeat.com/technology/anthropic-is-bringing-back-claude-fable-5-globally-after-us-lifts-export-control-order-where-can-enterprises-access-it
- https://www.digitalapplied.com/blog/claude-fable-5-usage-credits-july-7-pricing-guide-2026

### 2. Anthropic が業界横断「ジェイルブレイク深刻度フレームワーク」を提唱 — 停止・復帰劇を制度化

**事実** Anthropic が Project Glasswing を拡張し、ジェイルブレイクの深刻度を客観評価する**4軸の業界共通フレームワーク**を提案。①既存ツール比の能力ゲイン ②攻撃タスク横断での広がり ③兵器化の容易さ ④手法の既知度/発見容易性。Amazon / Microsoft / Google ら Glasswing パートナーと策定中。

**根拠** 現状ジェイルブレイクの深刻度を表す業界標準がなく、開発者は優先対応の、政府は介入タイミングの判断基準を欠く。CVSS（脆弱性スコアリング）に相当する共通尺度を目指す。最重篤クラス（重要インフラへの実害）には深刻度確定と同時に緩和を展開し、投稿チャネルを24時間監視する専任チームを新設。

**影響** 今回の Fable 5 輸出規制騒動（発見→停止→再審査→復帰）の再発防止を業界横断で制度化する狙い。政府承認制（managed-release）の定着を示す動きで、フロンティアモデルの「安全な出荷」プロセスが標準化へ向かう。

**行動指針** AI ガバナンス/セキュリティ担当は 4 軸フレームワークを社内のモデル評価・インシデント対応基準にマッピングしておく。標準化の進展（他社の採用・政府の参照）を継続監視する。

- https://www.anthropic.com/news/expanding-project-glasswing

### 3. Copilot Studio 基盤 Build 2026.6.3 着地 — Power Platform API 拡張と破壊的変更

**事実** Copilot Studio 基盤に新ビルド **2026.6.3**（6/30 初出）が Preview(US)/仏/瑞/韓/独/加/印/北欧/南米へ展開開始。前日は「2026.6.2 が最新・新ビルドなし」だったが更新。

**根拠** 新機能としてエージェントの作成/更新/一覧/取得/削除＋コンポーネント取得用の **Power Platform API 新エンドポイント**、per-agent 経時メトリクス（健全性を「エラー率」で表示）、**GPT-5 Mini fine-tuned モデルのデフォルト有効化**、GCC/High でのエージェントインベントリ既定有効化。**破壊的変更**として Skill エージェントが未サポートの参照ファイル形式をブロック（従来受理していた形式を拒否）。

**影響** セキュリティ強化も伴う——エージェントユーザー未設定のエージェントが Graph 等の制限リソースのトークンを取得できないよう防止、コンポーネント取得の認可エラーが HTTP 500 → **403 Forbidden** に変更、Agent365 監査ログが同意プロバイダーチェック不要に（テナント単位オプトアウト可）。API を叩く既存自動化・参照ファイル運用に影響しうる。

**行動指針** Copilot Studio エージェントを運用する組織は、Skill エージェントの参照ファイル形式が新仕様でブロックされないか確認。Power Platform API 連携は 403 応答への変更とトークン取得防止の挙動を織り込んでテストする。

- https://learn.microsoft.com/en-us/power-platform/released-versions/copilotstudio/2026.6.3

## カテゴリ別まとめ

### Anthropic / Claude
- Fable 5 / Mythos 5 輸出規制解除・7/1 グローバル復帰（ハイライト参照）
- ジェイルブレイク深刻度フレームワーク提唱（ハイライト参照）
- Claude Code は新バージョンなし。最新は v2.1.197（6/30、デフォルトを Sonnet 5 に変更）。v2.1.196（6/29）で組織デフォルトモデル設定・`claude mcp list`/`get` の自己承認 MCP 起動修正・`/code-review` トークン25%削減 https://code.claude.com/docs/en/changelog

### OpenAI / Codex
- Codex CLI 0.142.5（7/1）※新規: Responses WebSocket のリクエストペイロード全文がトレースログに書き込まれる問題を修正（保守）。0.143.0-alpha.32（7/1）開発中。実質最新機能は 0.142.2（6/25、MCP ツール検索既定化）のまま https://github.com/openai/codex/releases
- GPT-5.6（Sol/Terra/Luna）据え置き。政府承認の約20組織への限定プレビュー（API＋Codex）継続で個人利用は不可。広域リリースは「7月第2週」観測（7/10-17レンジ）。Cerebras で7月最大750 tok/s 提供予定 https://cryptobriefing.com/openai-releases-gpt-56-models-to-20-partners-public-launch-expected-by-july-2026/

### Google / DeepMind
- Gemini 3.5 Pro は7月延期継続。Vertex AI 限定エンタープライズプレビュー（2M context・Deep Think、Ultra $250/月限定）にとどまり GA 未達・具体日未発表。延期理由はコーディング/トークン効率/長タスク性能の refine。政府のセキュリティ規制線を越えていない唯一のフロンティアモデルとして「制約なく出荷可能」な立ち位置は維持 https://tech-insider.org/au/gemini-3-5-pro-delayed-july-2026/

### Microsoft / GitHub
- Copilot Studio 基盤 Build 2026.6.3（ハイライト参照）
- GitHub Copilot CLI 安定版 v1.0.67（6/30）※新規: **Claude Sonnet 5 サポート追加**、サンドボックス無効化の即時反映、サブエージェントが親のツール制限を継承、MCP OAuth の Microsoft Entra テナントドメイン不具合修正、hook タイムアウト時もツール呼び出しを継続。GitHub Copilot 本体（IDE/CLI）でも Claude Sonnet 5 が Pro/Pro+/Max/Business/Enterprise 向けに順次提供（Zero Data Retention 対応） https://github.com/github/copilot-cli/releases
- Microsoft 一次情報は動きなし（Copilot Studio What's New は June セクションのまま、M365 Copilot Release Notes / Power Platform Blog も新着なし）

### Cursor / 開発ツール
- Cursor for iOS 公開ベータ（6/29、全有料プラン、常時稼働エージェント・Remote Control・ライブ通知・モバイルレビュー）。Cursor 3.9（6/30）で Team Marketplace に MCP/Organizations を追加。**Composer 2.5 実行 75% オフは 7/5 まで** https://cursor.com/changelog
- Devin: 6/12 に削除した Fable 5 を、7/1 の全世界復帰を受けて Devin Fusion ユーザー向けに再展開予定 https://devin.ai/blog/claude-fable-5-available-in-devin/

### xAI / Grok（動きなし）
- 旗艦 Grok 5（噂 6T MoE、Colossus 2 訓練）は 7/2 時点未出荷。直近は Grok Voice（6/4）、Grok V9-Medium（1.5T コーディング、Cursor データ訓練、6月訓練完了）

### 市場・資金調達
- AI大型ラウンド継続。直近の Crunchbase 週次集計で Baseten（AI推論基盤）$1.5B Series F、Nexthop AI（AIネットワーキング）$500M Series B、Yann LeCun 共同創業の Advanced Machine Intelligence（世界モデル）$1.03B シード（欧州スタートアップ史上最大のシード）。Q1 2026 はグローバル VC $300B・AI が8割超という記録的水準が継続 https://news.crunchbase.com/venture/biggest-funding-rounds-ai-marketing-robotics-baseten/

## 直近の注目予定

- **7/5**: Cursor Composer 2.5 割引終了
- **7/7**: Fable 5 の週次上限「込み」枠終了 → 従量課金（usage credits）へ移行
- **7/8**: Anthropic 政府発行ID・生体情報検証ポリシー施行（Fable 5 復旧後の本人確認運用に影響しうる）
- **7月第2週**: GPT-5.6 一般提供目標（7/10-17レンジ観測）
- **7月**: GPT-5.6 Cerebras 提供開始 / Gemini 3.5 Pro GA
- **7/15**: Claude Science（AI for Science）応募締切（最大50件・各最大 $30,000 クレジット + Modal $2,000 compute、9/1–12/1 実施）
- **7/17**: Claude Corps 第1期応募締切
- **8/1**: covered frontier model フレームワーク 60日 EO 期限
- **8/3**: 旧「Claude in Slack」アプリ退役
- **8/5**: Opus 4.1 Claude API 退役
- **8/26**: OpenAI Assistants API 廃止 / o3 退役 / GPT-4.5 完全廃止
- **8/31**: Sonnet 5 促進価格終了（$2/$10 → $3/$15）
- **9月**: iOS 27 / macOS 27 GA（AFM 3 本番）

## 改善メモ

- Fable 5 復帰の料金条件がソース間で相互補完的。02 は「7/7まで週次上限最大50%込み・以降 usage credits」、03 は「7/7以降従量課金＋API直販レート 入力$10/出力$50・標準Enterpriseは猶予枠なし」と、02＝消費者/Team目線、03＝Enterprise/API目線で粒度が異なる。両者を統合して料金表として記録した
- 03 ソースは RSS/WebFetch 全ソース403継続のため WebSearch で収集（継続課題）。各ソースの新規提案・障害変化は本日なし
