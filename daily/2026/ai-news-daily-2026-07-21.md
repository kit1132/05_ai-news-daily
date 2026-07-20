# AI News Daily Summary — 2026-07-21

> 本サマリーは 01_ai-news-Master・02_ai-news-Copilot・03_ai-news-industry の3ソース（7/21分）を統合して作成。

静かな火曜。開発ツールの新規は **GitHub Copilot CLI v1.0.72（7/20）安定版**（`agentStop` フックの無限ループ是正・サンドボックス内 Git/GitHub 認証）のみで、Microsoft 一次情報源は全て据え置き（**要監視だった 7/21 火の版ページ更新でも 2026.7.x は未反映**、次の監視日は 7/28）。モデル面では **Alibaba「Qwen3.8-Max」プレビュー（2.4兆パラメータ、Fable 5 に次ぐ2番手を自称）**が Kimi K3 の数日後に登場し中国オープン勢の連続攻勢が続く。**Gemini 3.5 Pro の遅延は Bloomberg の一次報道に格上げ**（「数カ月遅れ」・Alphabet 株下落）、**ソフトバンクが GPT-5.5-Cyber 基盤の「Patching as a Service」を3,000社へ本格提供**。Anthropic 側では **Claude Mythos Preview が本日 7/21 で退役**（widely-released の Fable 5・Opus 4.8 等には影響なし）。

## 今日のハイライト

### 1. Alibaba「Qwen3.8-Max」プレビュー — 2.4兆パラメータの多モーダル、Kimi K3 の数日後に投入 — 中国オープン勢の週単位攻勢が続く

**事実**: Alibaba が 2.4兆パラメータのマルチモーダルモデル「Qwen3.8-Max」のプレビューを公開（同チーム初の1兆超マルチモーダル）。「Fable 5 に次ぐ2番手」を自称するが独立ベンチは未公表。オープンウェイト公開は「近く」とするのみで日付・ライセンス未定、現状は Token Plan サブスクのホスト版プレビューのみ（7/19）。

**根拠**: 7/16 の Moonshot「Kimi K3」（2.8兆・オープンウェイト、Frontend Code Arena 首位）に続く投入で、中国勢の「大規模×オープン×低価格」攻勢が週単位で連続している。現状のプレビューはホスト版のみでオープンウェイト実体・独立ベンチはいずれも未確認。

**影響**: エンタープライズのモデル選定で、中国製オープンモデルを比較対象に入れる圧力が一段と強まる。Fable 5 を基準に据える提案でも、コスト・主権・オープン性の観点で対抗選択肢の層が厚くなる。

**行動指針**: モデル選定の比較材料として「Qwen3.8-Max（ホスト版プレビュー）／Kimi K3（オープンウェイト）」を並べて把握しておく。独立ベンチ・オープンウェイト公開日・ライセンスが確定するまでは提案の前提には織り込まず、監視対象に置く。

- https://www.marktechpost.com/2026/07/19/alibaba-previews-qwen3-8-max-a-2-4-trillion-parameter-multimodal-model-days-after-moonshots-kimi-k3-open-weight-launch/
- https://dataconomy.com/2026/07/20/qwen3-8-24t-parameters-alibaba-ai-model-launch/

### 2. Gemini 3.5 Pro の遅延を Bloomberg が一次報道 — 「数カ月遅れ」・コーディング未達、Alphabet 株下落 — 遅延は日単位でなく月単位に確定

**事実**: これまで噂・リーク扱いだった Gemini 3.5 Pro の遅延が、Bloomberg（7/16）で「数カ月遅れ」の一次報道に格上げ。6月公開予定だったが、6月末に訓練データを更新してコーディング能力の改善を試みるも結果が振るわず社内目標に未達。現・元従業員10名の証言として「Anthropic / OpenAI が Gemini を上回るモデルを出す中で優位を失うリスク」への懸念を伝える。報道を受け Alphabet 株は下落（CNBC）。

**根拠**: I/O 2026（5/19）発表・当初6月 GA 目標から3度目標日を逸失（6月 → 7/17 → 未定）した状態が続く。モデルカード・API・料金・2M context のいずれも未発表で、公開 API の GA 済みは Gemini 3.5 Flash のみ、Vertex AI 限定 preview が継続。穴埋めに上位版 Flash をテスト中との観測もある。

**影響**: 「公式未確認の遅延」から「一次報道された月単位の遅延」へ状況が進んだ。Gemini 3.5 Pro を前提にした比較・提案は、当面 Flash 系または Vertex 限定 preview で代替する前提に切り替える必要がある。フロンティア競争で Google が一時的に後手に回る構図が定着。

**行動指針**: Gemini 3.5 Pro を織り込んだロードマップは GA 未定を前提に見直す。GA・価格・ベンチは引き続き公式 launch post を待って更新。予測市場は月末〜8月上旬を最有力とするため、その時期を重点監視する。

- https://www.bloomberg.com/news/articles/2026-07-16/google-gemini-launch-delayed-as-tech-falls-short-of-internal-goals
- https://www.cnbc.com/2026/07/16/alphabet-stock-gemini-3-5-pro-ai.html
- https://9to5google.com/2026/07/16/gemini-3-5-pro-delays/

### 3. GitHub Copilot CLI v1.0.72（7/20）安定版 — `agentStop` 無限ループ是正・サンドボックス内 Git 認証 — エージェント運用系が前進

**事実**: GitHub Copilot CLI の安定版 v1.0.72 が確定（7/20、pre-release v1.0.72-1 を経て）。常にブロックする `agentStop` フックの無限ループを是正（8回連続ブロックでターン終了）、follow-up メッセージでのマルチターンサブエージェントを常時有効化、`/add-dir` ディレクトリのセッション横断可視化を追加。サンドボックス内での Git / GitHub 認証をオプション提供し、ワークツリー作成の堅牢性も向上。Master／Copilot 両ソースが一致して報告。

**根拠**: セキュリティ面では OS サンドボックスの macOS keychain アクセスを既定オフ（分離強化）。UX では `/plugins` ヘルプコマンド（スキル・MCP サーバ管理）、`copilot plugins install --skill` でのスキル導入、`$` プロンプトショートカット（対話シェル、`/settings shellShortcut on` が必要）、`/model --session`（当該セッションのみモデル・reasoning effort・context window を調整）を追加。

**影響**: エージェントの停止制御（`agentStop` 無限ループ）とサンドボックス実行下のリポジトリ操作が実務的に改善。CLI ベースでエージェントを常用するチームには運用安定性の向上として更新価値が高い。

**行動指針**: Copilot CLI 利用者は v1.0.72 へ更新。サンドボックス内での Git/GitHub 認証や `/model --session` を運用フローに取り込む。macOS keychain アクセスが既定オフになった点は既存の権限前提を再確認する。

- https://github.com/github/copilot-cli/releases
- https://github.com/github/copilot-cli/blob/main/changelog.md

## カテゴリ別まとめ

### Anthropic / Claude
- **Claude Mythos Preview が本日 7/21 で退役**: `claude-mythos-preview` が予定どおりリタイア（以降リクエストは失敗）。移行先は Project Glasswing の `claude-mythos-5`（Fable 5 と同等能力・safety 分類器なし・限定提供）。仕様は 1M context / 128k output / $10・$50 で据え置き。widely-released 側の Fable 5・Opus 4.8 等には影響なし。
  - https://platform.claude.com/docs/en/about-claude/model-deprecations
- **Claude Code は v2.1.215（7/19）が最新**（`/verify`・`/code-review` の自動実行廃止・明示呼び出しへ）で新規リリースなし。**Opus 4.1 の Claude API 提供終了は 8/5**。Anthropic Reflect ダッシュボード（ベータ）は 7/19 既報。

### モデル・中国勢
- **Alibaba「Qwen3.8-Max」プレビュー**（ハイライト参照）
- 直近の中国オープン勢: 7/16 Moonshot「Kimi K3」（2.8兆・オープンウェイト、Frontend Code Arena 首位）に Qwen3.8-Max が続く連続投入。

### Google / DeepMind
- **Gemini 3.5 Pro — Bloomberg が「数カ月遅れ」を一次報道**（ハイライト参照）。GA 済みは Gemini 3.5 Flash のみ、Pro は Vertex AI 限定 preview が継続。

### OpenAI / 開発ツール
- **GitHub Copilot CLI v1.0.72**（ハイライト参照）
- **OpenAI Codex CLI**: alpha が 0.145.0-alpha.25（7/20）まで進行。安定版は 0.144.6（7/18）据え置きで新機能追加なし。Cursor は 3.11（7/11）＋ Slack 版強化（7/17）から新規リリースなし。
  - https://github.com/openai/codex/releases

### Microsoft / GitHub（一次情報源は据え置き）
- **Power Platform Released Versions**: Copilot Studio Build **2026.6.3（6/30初出）が最新のまま**、リージョン分布も無変化。**版ページは毎週火曜更新だが、要監視だった 7/21 の更新機会でも予告の 2026.7.x は未反映**。次の要監視日は 7/28（火）。
  - https://learn.microsoft.com/en-us/power-platform/released-versions/copilotstudio
- **Copilot Studio - What's New**: June 2026 セクションのまま（7月セクション未公開）。
  - https://learn.microsoft.com/en-us/microsoft-copilot-studio/whats-new
- **M365 Copilot Release Notes**: 「July 15」バッチが最新のまま（本日新バッチなし。次バッチは隔週傾向で 7/29 前後見込み）。
  - https://learn.microsoft.com/en-us/copilot/microsoft-365/release-notes
- **Power Platform 重要な変更（週次）**: 新規非推奨項目なし。直近は Visio→Power Automate エクスポート廃止（7/14 発効・MC1323265）が最新のまま。

### 国内エンプラ・AIセキュリティ
- **ソフトバンク「Patching as a Service」を3,000社へ本格提供**: ソフトバンクと SB OAI Japan が OpenAI のセキュリティ特化モデル「GPT-5.5-Cyber」を基盤とする「Patching as a Service」を重要インフラ企業3,000社へ本格提供開始（7/14）。脆弱性診断→修復方針策定→パッチ適用提案を一気通貫で支援し、発表時点で金融・交通・製造など137社が導入意向。7/16 に約1,000名規模の「エンタープライズAIサイバー防衛室」を設置。国内重要インフラ向けの大規模 AI セキュリティ商用事例。
  - https://www.softbank.jp/en/corp/news/press/sbkk/2026/20260714_02/
  - https://www.sbbit.jp/article/cont1/186115

## 直近の注目予定

- **7/23**: OpenAI computer-use-preview 提供終了
- **7/28（火）**: Copilot Studio 版ページ次更新 — 2026.7.x 反映見込みの要監視日（7/21 でも未着のためスライド）
- **7/29前後**: M365 Copilot Release Notes 次バッチ見込み
- **7/30**: M365 Copilot メモリ活用のエージェント提案 GA 予定
- **7/31**: Devin classic 環境設定 read-only 参照終了
- **8/1**: 対象フロンティアモデルの大統領令60日期限
- **8/3**: 旧「Claude in Slack」提供終了
- **8/5**: Opus 4.1 Claude API 提供終了 / Cowork 倍増利用枠終了
- **8/9**: ChatGPT Atlas 提供終了
- **8/26**: OpenAI Assistants API 廃止 / o3 退役 / GPT-4.5 完全廃止
- **8/31**: Sonnet 5 プロモ価格終了（→ $3/$15）
- **9月**: iOS 27 / macOS 27 GA（AFM 3 本番）

## 改善メモ

- 3ソースとも新規提案・障害の変化なし。継続項目: Copilot 側 B-005「Qiita RSS の WebSearch 化」6回目、industry 側 B-004「WebSearch 優先化」22回目（詳細は各リポの IMPROVEMENT-BACKLOG.md）。Master 側は火曜のため週次復旧チェックは非対象（次回 07-27 月曜）。
- Qwen3.8-Max は独立ベンチ未公表・オープンウェイト公開日／ライセンス未定（現状ホスト版プレビューのみ）。実体確認後に更新する。
- Gemini 3.5 Pro 遅延は Bloomberg 一次報道に格上げ（月単位で確定）。GA日・価格・ベンチ・2M context は引き続き公式発表待ち。
- ソフトバンク PaaS の導入社数・体制規模は各報道／プレスベース。
- Microsoft 一次情報源は 7/21（火）の更新機会でも 2026.7.x 未反映。次回検証は 7/28（火）の Copilot Studio 版ページ更新で実施予定。
