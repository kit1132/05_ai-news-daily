# AI News Daily Summary — 2026-07-15

> 本サマリーは 01_ai-news-Master・02_ai-news-Copilot・03_ai-news-industry の3ソース（7/15分）を統合して作成。

水曜。**本日発の新モデル・提供条件変更はなし**。動きは開発ツールとエンタープライズ運用に集中。**Claude Code が v2.1.208 で今週最大のアップデート**（7/14、スクリーンリーダーモード・企業ランチャー対応・大幅な性能改善）を出し、直後に v2.1.209 で不具合修正。Microsoft は **新 M365 Copilot アプリ UI が本日 7/15 に標準リリースでデフォルト化**（opt-out トグル削除で旧UIに戻せなくなる・MC1325422）。前日開幕の **VB Transform 2026 は Day 1 の実キーノート成果**（Amazon の「信頼できるエージェント」設計フレーム、Intuit のオーケストレータ分離）が出そろい、競争軸が「モデル選定」から「本番運用の設計・体制」へ移ったことを一次事例で裏づけた。インフラ面では **Reflection AI × Nebius $1B コンピュート契約**・**Nous Research $1.5B 評価額調達協議** と、効率シフトの裏で計算基盤・OSSエージェントへの資本投下が継続。

## 今日のハイライト

### 1. VB Transform 2026 Day 1 実キーノート — エージェント設計は「分離（decoupled）」が本番要件、オーケストレータをモデルから切り離す

**事実**: 7/14 開幕の **VB Transform 2026（Menlo Park）Day 1** で、Amazon（AGI autonomy 研究ラボ）が「信頼できるエージェント」の設計フレームを提示 — **consistency / robustness / predictability / safety の4軸**。モデルを安全に「調教」する前提を捨て、**サンドボックス環境でエージェントが変更を提案 → 人間がレビュー後に実行する decoupled（分離）設計**を、金融など高リスク領域の要件として示した。Intuit（VP of AI, Nhung Ho）は「大きなエージェントが多くをこなす多エージェント構成」から、workflow / skill / tool を基底まで分解し、**オーケストレータをモデルプロバイダから切り離す**再構築を証言。

**根拠**: 前日（7/13）掲載の VentureBeat Research「評価ギャップ」調査（企業リーダー573名）が研究的背骨で、本日は本番運用企業（Amazon / Intuit）の実キーノートがそれを裏づける一次事例となった。

**影響**: エージェント案件の提案枠組みが、モデル比較から「オーケストレーション＋ガードレール設計」に完全に移る。特に「エージェントが提案し人間が実行する分離設計」は、高リスク業種（金融・医療・公共）向け提案の設計原則としてそのまま流用できる。オーケストレータをモデルプロバイダに固定しない設計は、前日の中国製モデル台頭・マルチモデル調達トレンドとも整合する。

**行動指針**: 高リスク業種のエージェント提案では Amazon の4軸（consistency / robustness / predictability / safety）を評価チェックリストの骨子に、「提案→人間レビュー→実行」の分離アーキテクチャを既定設計に据える。オーケストレーション層をモデル非依存に設計し、モデル差し替え可能性を提案要件に明記する。

- https://venturebeat.com/orchestration/amazon-will-present-its-framework-for-engineering-trustworthy-ai-agents-at-vb-transform-2026
- https://venturebeat.com/orchestration/intuit-will-show-off-how-it-rebuilt-its-ai-infrastructure-to-support-fast-and-complex-tasks-at-vb-transform-2026

### 2. 新 Microsoft 365 Copilot アプリ UI が本日デフォルト化 — opt-out トグル削除で旧UIに戻せなくなる（MC1325422）

**事実**: **本日 7/15、標準リリースで新 M365 Copilot アプリ UI がデフォルト化**され、**「New Copilot」opt-out トグルが削除**される（[MC1325422](https://mc.merill.net/message/MC1325422)）。新デザインは chat-centered・**Tasks タブ**（長時間実行タスク／スケジュールチャット／エージェント活動の統合ビュー）・**Work IQ トグル**（業務データ＋Web グラウンディングの統合、既定オン）・ピン留めナビ。6/22 から WW 展開・トグルで切替可能だったが、本日以降は旧UIに戻せない。**UX/URL 統合でありライセンス変更なし**（既存 M365 Copilot アドオン保有者は再割当不要）。

**根拠**: Microsoft の Message Center 一次通知（MC1325422）と公式ブログ（5/28 New Design 発表）。日付確定の破壊的 UX 変更。

**影響**: 社内で M365 Copilot を展開している組織は、本日から全ユーザーの UI が強制的に切り替わる。Work IQ が既定オンのため、業務データ＋Web グラウンディングのガバナンス確認（データ境界・コンプライアンス）が急務。ヘルプデスク問い合わせ増・ユーザー教育の準備が必要。

**行動指針**: M365 Copilot 導入顧客に本日の UI 強制切替と「旧UIに戻せない」点を即時周知。Work IQ 既定オンのデータグラウンディング範囲を確認し、Tasks タブ／エージェント活動ビューの社内利用ガイドを更新。ライセンス変更なしのため再割当は不要と案内する。

- https://mc.merill.net/message/MC1325422
- https://www.microsoft.com/en-us/microsoft-365/blog/2026/05/28/introducing-a-new-design-for-microsoft-365-copilot/

### 3. Claude Code v2.1.208 が今週最大の更新 — アクセシビリティ・企業ランチャー対応・大幅な性能改善

**事実**: **Claude Code v2.1.208（7/14）** が今週最大の更新。新機能: **スクリーンリーダーモード**（`claude --ax-screen-reader` / `CLAUDE_AX_SCREEN_READER=1` / `"axScreenReader": true`、プレーンテキスト描画のアクセシビリティ対応）、**`vimInsertModeRemaps`**（`jj`→Esc 等の2キー挿入モードリマップ）、**`CLAUDE_CODE_PROCESS_WRAPPER`**（自己起動プロセスを企業ランチャー経由で実行）、フルスクリーン複数選択メニューのマウスクリック対応。性能面は**ツール呼び出し CPU オーバーヘッドを高ツール数で約7倍高速化**、**トランスクリプトサイズ最大79倍削減**、複数のメモリリーク解消、自動更新後の context window 誤表示（200k リセット）修正、大規模 markdown テーブルの描画停止修正など多数。直後の **v2.1.209** は `agents` バックグラウンドセッションで `/model` 等ダイアログがブロックされる過剰ガードを是正。

**根拠**: Claude Code 公式 Changelog（github raw CHANGELOG で一次確認）。Master・Copilot の両ソースが独立に確認。

**影響**: (1) スクリーンリーダーモードでアクセシビリティ要件のある組織への導入障壁が下がる。(2) `CLAUDE_CODE_PROCESS_WRAPPER` は**企業のプロセス起動ポリシー（ランチャー経由の統制）に適合**でき、エンタープライズ導入の要件を満たしやすくなる。(3) 高ツール数（MCP 多用）環境での CPU 7倍高速化・トランスクリプト縮小は、大規模エージェント運用の実コストに直結。

**行動指針**: Claude Code のエンタープライズ導入提案に `CLAUDE_CODE_PROCESS_WRAPPER`（ランチャー統制）とスクリーンリーダーモードを「企業要件対応」の根拠として追加。MCP を多用する顧客には性能改善（7倍高速化・79倍縮小）を v2.1.208 以降への更新推奨材料にする。

- https://code.claude.com/docs/en/changelog

## カテゴリ別まとめ

### 開発ツール（Claude Code / Copilot CLI / Codex CLI / Cursor / Devin）
- **Claude Code v2.1.208 / v2.1.209（7/14）**（ハイライト参照）。
- **GitHub Copilot CLI pre-release v1.0.71-1（7/14）** — **GitHub MCP ツールセット設定が `settings.json` で永続化**、`plugins marketplace` サブコマンド（マーケットプレイス管理）新設、サイドバーのセッションが再起動をまたいで永続化、`/move` が未コミット変更を新規 worktree へ持ち越し。安定版 v1.0.70（7/10、GPT-5.6 対応・`/refine`）は据え置き。 https://github.com/github/copilot-cli/releases
- **OpenAI Codex CLI 0.144.4（7/14）** — ユーザー向け変更なしのパッチ。alpha は **0.145.0-alpha.11（7/14）** まで進行。安定版 0.144.2（Guardian 自動レビューのリグレッション是正）/ 0.144.3（バージョンのみ）は既報。 https://github.com/openai/codex/releases
- **Cursor 3.11（7/10、Side Chats）／ Devin（7/3 更新）いずれも据え置き**。

### Microsoft / Copilot / Power Platform
- **新 M365 Copilot アプリ UI デフォルト化（本日 7/15・MC1325422）**（ハイライト参照）。
- **一次情報の動きなし（Learn MCP で一次確認）** — M365 Copilot Release Notes は **July 01 バッチが最新**（次バッチは隔週傾向で 7/15 前後見込みだが本日時点未公開・off-cycle もなし）。Copilot Studio What's New は June 2026 のまま。月次「What's New in Power Platform: July 2026」・Tech Community「What's New in M365 Copilot 7月」・2026 Release Wave 2 計画ページはいずれも未公開（wave2 URL は 403 継続）。
- **ガバナンス（継続確認）**: Copilot Studio は **2026年7月以降、新規エージェントに Microsoft Entra Agent ID が必須化**（自動 ID 作成の opt-out 不可、環境レベル除外設定は廃止）。 https://learn.microsoft.com/microsoft-copilot-studio/admin-use-entra-agent-identities
- **週次ソース**: Released Versions〔火曜更新〕は **Build 2026.6.3 据え置き**（次ビルド 2026.7.x 反映は次回火曜 **7/21** が要監視）。

### エンタープライズAI・エージェント運用
- **VB Transform 2026 Day 1 実キーノート**（ハイライト参照）。会期は本日 7/15 まで。

### AIインフラ・ディール
- **Reflection AI × Nebius が $1B コンピュート契約（7/14）** — Nvidia 最新チップへのアクセスを確保。Reflection は評価額 ~$8B、Nvidia / Sequoia / Lightspeed 等から累計 ~$2.6B 調達済み。効率シフトの裏で計算基盤への資本投下が継続。 https://www.crescendo.ai/news/latest-vc-investment-deals-in-ai-startups
- **Nous Research（Hermes）が $1.5B 評価額で調達協議（7/13 TechCrunch）** — 最低 $75M・Robot Ventures 主導、USV 等参加。OSSエージェント Hermes は GitHub 21.4万スター・4万フォーク、$20/月からデスクトップ/VPS/クラウドで稼働。プロプライエタリ勢に対し OSSエージェントが評価額 $1B 超で台頭。 https://techcrunch.com/2026/07/13/hermes-agent-maker-nous-research-in-talks-for-new-funding-at-1-5b-valuation/

### Anthropic / Claude
- **Claude Code 以外は据え置き** — Fable 5（1M context / 128k output / $10・$50、refusal 分類器あり）仕様据え置き。Cowork のモバイル/web 展開（7/7 発表・Max 先行）、Enterprise 向け admin analytics / model entitlements / spend alerts は既報の継続。公式 news の新規なし（anthropic.com/news は WebFetch 403 継続、WebSearch 運用）。

### OpenAI / ChatGPT
- **新モデル・新機能なし** — 7/9 の GPT-5.6 GA（Sol/Terra/Luna）・ChatGPT Work・GPT-Live-1（音声）以降据え置き。7/12〜13 の GPT-5.6 Sol 利用制限一時緩和は既報。

### Google / DeepMind
- **Gemini 3.5 Pro** は限定 preview 継続。**7/17 GA 候補日**の第三者報道は据え置き（公式モデルカード・料金・2M context いずれも未確定、公開 API に未掲載）。一部報道は Vertex AI エンタープライズ枠を 7/15 前後に展開と観測するが公式確認なし。ベースモデル破棄・完全再構築（数学推論・SVG生成・画質を GPT-5.6/Fable 5 対抗へ）、Deep Think 層を予告。

### SpaceXAI / Grok
- Grok 4.5（7/8、$2/$6、Cursor 共同訓練）以降の新規進展なし。EU 提供は7月中旬めど（EU AI Act の systemic risk 分類による遅延、確定日なし）。

### Apple / プラットフォーム
- iOS 27 / macOS 27 初回 Public Beta（7/13、刷新版 Siri）以降の新規なし。GA は9月路線変更なし。

## 直近の注目予定

- **7/15（本日）**: 新 M365 Copilot アプリ UI デフォルト化（opt-out トグル削除・MC1325422）/ VB Transform 2026 最終日（Menlo Park）/ Claude Science（AI for Science）応募締切
- **7/17**: Claude Corps 第1期応募締切 / Gemini 3.5 Pro GA 候補日（未確定）
- **7月中旬**: Grok 4.5 EU 提供予定 / ChatGPT Work が Plus・Business へ拡大
- **7月中（隔週）**: M365 Copilot Release Notes 次バッチ見込み（本日時点未公開・要監視）
- **7/21**: Copilot Studio 版ページ次更新（火曜・2026.7.x 反映見込み）/ Copilot Cowork GA 告知イベント
- **7/23**: OpenAI computer-use-preview シャットダウン
- **7/30**: M365 Copilot メモリ活用のエージェント提案 GA 予定（Copilot Studio Release Wave）
- **7/31**: Devin classic 環境設定の read-only 参照終了
- **7月中旬〜下旬**: 2026 Release Wave 2 計画ページ公開見込み
- **8/1**: covered frontier model 大統領令60日期限
- **8/3**: 旧「Claude in Slack」退役
- **8/5**: Opus 4.1 Claude API 退役 / Cowork 倍増利用枠の終了
- **8/26**: OpenAI Assistants API 廃止 / o3 退役 / GPT-4.5 完全廃止
- **8/31**: Sonnet 5 促進価格終了（$2/$10 → $3/$15）
- **9 月**: iOS 27 / macOS 27 GA（AFM 3 本番）

## 改善メモ

- **ソース間整合**: Claude Code v2.1.208/209 は Master（詳細）と Copilot（要点）の両方が独立に確認、内容矛盾なし。VB Transform Day 1 キーノートは industry が一次、Master/Copilot は言及なし（役割分担どおり）。3ソース間の内容矛盾は検出されず。
- **障害の変化**: `developers.openai.com/codex/changelog` が 403 再発（07-08 復旧確認済みの exception ソース。Master が2回試行とも 403、Codex CLI 情報は GitHub releases で完全代替済み・欠落なし）。ほか x.ai/*・cursor.com/changelog・anthropic.com/news・wave2 planned-features は 403 継続（各ソースとも WebSearch で補完）。
- **前日欠損リカバリ**: 対象なし（7/14 分サマリーは3ソース完全統合で欠損記録なし）。
