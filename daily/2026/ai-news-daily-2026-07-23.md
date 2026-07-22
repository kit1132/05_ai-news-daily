# AI News Daily Summary — 2026-07-23

> 本サマリーは 01_ai-news-Master・02_ai-news-Copilot・03_ai-news-industry の3ソース（7/23分）を統合して作成。

本日の中心はセキュリティとガバナンス。Pillar Security が **コーディングエージェント4製品に計7件のサンドボックス脱獄経路**を公開し、**Google は Gemini CLI/Antigravity を「修正しない」判断**を示した。テナント運用では **MC1422074（OpenAI GPT-5.6 のサブプロセッサー化）が明日 7/24 に自動有効化**され、ガバナンス方針を持つ組織は opt-out 判断の期限を迎える。開発ツールは **Claude Code v2.1.217** が同時サブエージェント上限・ネスト生成禁止・`--max-budget-usd` の破壊的変更を伴って前進。資本・政策面では **Databricks が評価額$188Bで$3B調達**、**AIラボの米連邦ロビイングが Q2 過去最高（Anthropic が Nvidia 超え）** と、フロンティア勢の資金・政策投下が続く。

## 今日のハイライト

### 1. Pillar Security「Week of Sandbox Escapes」— コーディングエージェント4製品に脱獄経路、Google は一部非対応 — 生成物→ホスト信頼境界が新たな要件に

**事実** — Pillar Security が 7/22、Cursor / OpenAI Codex CLI / Gemini CLI / Antigravity（3ベンダー4製品）で計7件の脆弱性を数カ月かけ再現・公開した。サンドボックス自体を破るのではなく、エージェントが生成したファイルをホスト上の信頼済みソフトが後処理する「信頼の問題」を突く新種。

**根拠** — Cursor は Claude hooks 設定ファイル経由でサンドボックス外実行（CVE-2026-48124、v3.0.0で修正）。Codex は「安全」許可リストが `git show` を読み取り専用と誤信（v0.95.0で修正・高額バウンティ）。**Google は Gemini CLI/Antigravity について修正しない判断**を示した。7/8 の JADEPUFFER に続くエージェント運用セキュリティの一次事例。

**影響** — 修正済み製品はアップグレードで対処できるが、Google 非対応の2製品は運用側での封じ込め（生成物のホスト信頼境界の設計、許可リスト検証、後処理ツールの隔離）が必須となる。「サンドボックスがあるから安全」という前提が崩れた。

**行動指針** — コーディングエージェント導入時は「生成物→ホスト信頼境界」を設計要件に組み込み、Cursor は v3.0.0・Codex は v0.95.0 以上へ更新。Gemini CLI/Antigravity 利用組織は非対応前提で許可リスト・後処理経路をレビューする。

- https://www.pillar.security/blog/the-week-of-sandbox-escapes
- https://www.bleepingcomputer.com/news/security/cursor-codex-gemini-cli-antigravity-hit-by-sandbox-escapes/

### 2. MC1422074 — OpenAI GPT-5.6 が M365 Copilot のサブプロセッサーに、7/24 自動有効化 — opt-out 期限は明日

**事実** — Microsoft は MC1422074 で、OpenAI モデル（GPT-5.6 含む）を M365 Copilot のサブプロセッサーとして利用可能にする。設定は既定で無効だが、管理者が opt-out しなければ **2026-07-24 に自動的に有効化**される。

**根拠** — データ処理のサブプロセッサー範囲に関わる変更で、M365 admin center でいつでも確認・変更可能。ガバナンス方針を持つテナントは処理者範囲の追加として審査対象となる。

**影響** — 明示的な承認プロセスを持つ組織では、無操作のまま 7/24 を迎えると意図しないサブプロセッサー拡大が既定で発生する。逆に活用したい組織は追加操作なしで有効化される。

**行動指針** — サブプロセッサー審査を要する組織は 7/24 までに M365 admin center で MC1422074 の設定を確認し、方針に応じて opt-out/維持を判断する。

- https://mc.merill.net/message/MC1422074

### 3. Claude Code v2.1.217 — 同時サブエージェント上限とネスト禁止、`--max-budget-usd` に破壊的変更 — エージェント制御と隔離の堅牢化

**事実** — Claude Code v2.1.217 が公開。①同時実行サブエージェント数に既定 20 の上限（`CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS` で調整）、②サブエージェントは既定でネストしたサブエージェントを生成しない（`CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH` で許可）、③**破壊的変更: `--max-budget-usd` がバックグラウンドのサブエージェントも停止対象に**（従来はフォアグラウンドのみ）。

**根拠** — 併せて、バックグラウンドセッションのワークスペース隔離がシンボリックリンクを正規化せずワークスペース外へ脱出し得た不具合、切り詰めた MCP ツール出力のメモリリーク、Claude Desktop で企業 mTLS/TLS 検証/OAuth スコープ/プロキシ設定が無視される不具合を修正。ログイン失効警告は 5 日前 → 3 日前に変更。プロンプト補完に絵文字ショートコード（`emojiCompletionEnabled` で無効化可）を追加。

**影響** — 大量サブエージェントを回すワークフローは既定上限に当たる可能性があり、`--max-budget-usd` を CI 等で使う運用はバックグラウンド停止の挙動変化で影響を受け得る。隔離の穴とメモリリーク修正は長時間セッションの安定性に効く。

**行動指針** — 20 超の並列を前提とするパイプラインは環境変数で上限を明示調整。`--max-budget-usd` を使う自動化は新挙動を前提に予算閾値を再確認。Desktop で企業プロキシ/mTLS 環境の利用者は更新を推奨。

- https://code.claude.com/docs/en/changelog
- https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md

## カテゴリ別まとめ

### Anthropic / Claude
- **Claude Code v2.1.217**（ハイライト参照）。
- **Claude for Teachers を提供開始**: 認証済みの米国 K-12 教員に上位ツール・教育向けスキル・州標準準拠のカリキュラム連携を無料提供（教育向けコネクタ・AI リテラシー研修も追加）。 https://www.anthropic.com/news/claude-for-teachers
- **Claude Developer Platform 更新**: Claude Sonnet 5 をコンテキスト 1M トークン・最大出力 128k で提供。Managed Agents にイベントデルタストリーミング/セッション単位オーバーライド/webhook 拡張、`agent-memory-2026-07-22` ベータヘッダーを追加。

### Microsoft 365 Copilot / Power Platform
- **宣言型エージェント manifest 1.8 公開**（拡張機能 What's New に「July 2026」節が新規追加）: `EmailActions`（メールのトリアージ・監督付き送信・削除・受信ルール・自動応答・フォルダー管理）、`MeetingActions`（会議スケジュール・時間調整投票・時間インサイト）、ワーカーエージェントの `file` プロパティ参照、埋め込みナレッジへの `embedded_resource_snapshot_id`。利用状況レポート API 3 種に `version` パラメーター追加。 https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/whats-new
- **MC1422074（OpenAI GPT-5.6 サブプロセッサー化・7/24 自動有効化）**（ハイライト参照）。
- **Power Platform ライセンス（7月版）補足**: Copilot Credits の購入は Pay-As-You-Go 優先に整理。**Copilot Studio エージェントの Work IQ API 利用は M365 Copilot ライセンスに含まれず Copilot Credits を消費**（コスト設計時の注意）。
- **Microsoft 一次情報は据え置き**: Copilot Studio What's New は June 節のまま、M365 Copilot Release Notes は「July 15, 2026」バッチが最新、Released Versions（CS）は Build 2026.6.3 が最新のまま（次の監視は 7/28〔火〕、Release Notes 次バッチは 7/29 前後見込み）。

### 開発ツール（Copilot CLI / Codex / Cursor）
- **GitHub Copilot CLI v1.0.74-1 pre-release**: 初回起動時に既定サンドボックスへのオプトインを促すスプラッシュを追加、**Gemini 3.6 Flash モデルのサポートを追加**。セッション多重化改善、`$` での対話シェルショートカット強化、MCP ウィザードの特殊文字保持修正、画像処理改善。 https://github.com/github/copilot-cli/releases
- **OpenAI Codex CLI 0.146.0-alpha 進行中**: 安定版は 0.145.0（7/21）据え置き。alpha ビルドに具体的変更記載はなく漸進段階。 https://github.com/openai/codex/releases

### 資本・市場
- **Databricks が評価額$188Bで$3B調達（Coatue 主導）**: 7/17 発表、2月の$134Bから約+40%・今年2度目のラウンド。用途は Unity AI Gateway / Genie / Lakebase（AIエージェント向けDB）の加速と戦略的買収。エンプラの「AIエージェント向けデータ基盤」への資本集中を示す定点。 https://www.databricks.com/company/newsroom/press-releases/databricks-raising-strategic-round-funding-188-billion-valuation

### 規制・政策
- **AIラボの米連邦ロビイングが Q2 2026 に過去最高**: Anthropic $1.97M（+26%）で **Nvidia を上回る**、OpenAI $1.2M（+18%）、2社計$3.17M（Q1比+23%）でともに四半期の自己記録更新。Anthropic は上半期累計$3.5M超で 2025 通年（$3.1M）を既に超過。注力は輸出規制・サイバーセキュリティ・著作権・クラウド・防衛調達・AI安全基準。ホワイトハウス自主フレームワーク合意は8月第1週観測。 https://www.cnbc.com/2026/07/21/openai-anthropic-ai-lobbying-spending-q2-2026.html

### ウォッチ
- **Gemini 3.5 Pro GA**: 7/23 時点でも公式発表（モデルカード/API/価格）は未確認。公開 API は gemini-3.5-flash / gemini-3.1-pro-preview のまま。7/16 Bloomberg 報道の「月単位遅延」から状況変化なし（8月ずれ込み観測継続）。

## 直近の注目予定

- **7/23（本日）**: OpenAI computer-use-preview シャットダウン / GPT-5.4 退役予定
- **7/24（金）**: OpenAI モデル サブプロセッサー（MC1422074）自動有効化（opt-out 期限）
- **7/28（火）**: Copilot Studio 版ページ 2026.7.x 反映見込み・Power Platform 定例更新
- **7/29 前後**: M365 Copilot Release Notes 次バッチ見込み
- **7/30**: M365 Copilot メモリ活用のエージェント提案 GA
- **7/31**: Devin classic 環境設定 read-only 参照終了
- **8/1**: covered frontier model 60 日 EO 期限
- **8月第1週**: ホワイトハウス フロンティアモデル自主フレームワーク合意観測
- **8/3**: 旧「Claude in Slack」退役
- **8/5**: Opus 4.1 Claude API 退役 / Cowork 倍増利用枠終了
- **8/9**: ChatGPT Atlas シャットダウン
- **8/26**: OpenAI Assistants API 廃止 / o3 退役 / GPT-4.5 完全廃止
- **8/31**: Sonnet 5 促進価格終了（→ $3/$15）
- **9 月**: iOS 27 / macOS 27 GA（AFM 3 本番）

## 改善メモ

- 3ソースとも新規提案・障害の変化なし（継続分は各リポの IMPROVEMENT-BACKLOG.md 参照）。
- 01: 本日は木曜のため週次復旧チェックは非対象（次回 07-27 月曜）。
- 03: 継続提案 1件（B-004 取得方法欄の WebSearch 優先化、24回目）。
- **クロスソース**: Gemini 3.5 Pro GA は 01（8月ずれ込み観測で本文非掲載）・03（最注目ウォッチ・変化なし）で一致。矛盾なし。Claude Code v2.1.217 は 01・02 で重複、情報量の多い記述を統合した。
