# AI News Daily Summary — 2026-07-09

> 本サマリーは 01_ai-news-Master・02_ai-news-Copilot・03_ai-news-industry の3ソース（7/9分）を統合して作成。
> ※ 当初 01_ai-news-Master の当日分が未取得のため 2 ソースで作成したが、翌 7/10 に 01 の 7/9 分が取得可能となったため3ソースで再生成（欠損リカバリ、改善メモ参照）。

木曜。**主役はフロンティアモデルとコスト戦略**。最重要は **GPT-5.6 の広域公開が本日 7/9 始動** — 米商務省 CAISI が事前レビュー制限を解除し、OpenAI が Sol/Terra/Luna をグローバル公開。予測市場が追い続けた「7/9」がそのまま着地した。あわせて **Microsoft が Excel/Outlook の AI 推論を自社 MAI モデルへ置換開始**し、Suleyman が「Anthropic 支出の全廃」を明言 — 階層ルーティングによるコスト最適化が標準化しつつある。開発ツールは **Claude Code が v2.1.204** に進み、ヘッドレス/クラウド実行のフック不具合を修正。

## 今日のハイライト

### 1. GPT-5.6 広域公開が本日 7/9 始動 — 政府レビュー解除、Sol/Terra/Luna をグローバル展開 — 「モデル公開日＝政府レビュー通過日」の構図が定着

**事実** 6/26 の約20組織限定プレビューを経て、米商務省 Center for AI Standards and Innovation（CAISI）が追加試験のうえ広域展開を承認。OpenAI は 7/8 に告知し、**本日 7/9 に Sol/Terra/Luna をグローバル公開・プレビュー拡大**する。ChatGPT/Codex/API への順次搭載を予定。標準料金は据え置き（100万トークンあたり Sol 入力$5/出力$30、Terra $2.5/$15、Luna $1/$6）。Terra は GPT-5.5 相当性能で約半額。あわせて **Sol Fast（Cerebras 最大 750 tok/s・Terminal-Bench 2.1 で SOTA）の価格 $12.5/$75** が判明（通常 Sol とは別のプレミアム高速枠）。GPT-5.6 公開に合わせ **GPT-Live System Card 公開・ChatGPT Voice を GPT-Live-1（有料）/ GPT-Live-1 mini（無料）へ切替**（同時発話・割り込み対応）、Realtime の **gpt-realtime-2.1 / 2.1-mini**（p95 レイテンシ 25%+ 改善）も更新。

**根拠** 6/2 大統領令のAIサイバーセキュリティ枠組み（公開30日前の任意事前レビュー）に基づく限定プレビューが実質のゲートだった。CNBC/Axios（7/8）が制限解除を報道し、Engadget（7/8）が 7/9 公開を確認。6/26 開始から約2週間で予測市場の本命「7/9」に着地した。

**影響** 先端モデルのリリース時期を政府の任意事前レビューが実質左右する構図が定着（Gemini 3.5 Pro・Anthropic Fable/Mythos 5 も同枠組み下）。Terra の「GPT-5.5 相当で約半額」は、定型タスクの推論コストを一段押し下げる。

**行動指針** 導入計画は「モデル公開日＝政府レビュー通過日」を前提に据える。既存の GPT-5.5 利用は Terra への切替でコスト最適化を検討。ChatGPT/Codex への搭載時期は順次のため、業務組込みは API 経由での先行検証を推奨。

- https://openai.com/index/previewing-gpt-5-6-sol/
- https://www.cnbc.com/2026/07/08/openai-expanding-gpt-5point6-ai-model-release-ending-government-limits.html
- https://www.axios.com/2026/07/08/openai-gpt-trump-ban-lifted
- https://www.engadget.com/2210308/openai-rolls-out-gpt5-6-july-9/

### 2. Microsoft、Excel/Outlook の AI を自社 MAI モデルへ置換開始 — 「Anthropic 支出の全廃」を明言 — 階層ルーティングがコスト最適化の標準アーキテクチャに

**事実** Microsoft が Excel・Outlook で従来 OpenAI/Anthropic に依存していた推論を、Build 2026 発表の自社 MAI モデル群（7モデル・推論〜画像/音声、主力 **MAI-Thinking-1**）へ置換開始（Bloomberg、7/7）。サーバー側更新でユーザーには不可視（トグルなし）。AI責任者 Mustafa Suleyman は **「Anthropic への支出をいずれ完全になくす」** と明言。GitHub Copilot・Teams へも展開予定で、定型・高頻度タスクは MAI、フロンティア級のみ OpenAI/Anthropic へルーティングする。

**根拠** Bloomberg（7/7）が週数万プロンプト規模の MAI 移行を報道。主眼はコスト削減で、「効率重視（tokenmaxxing 脱却）」トレンドの最も象徴的な事例。最大級の顧客であった Microsoft の内製シフトという点で影響が大きい。

**影響** "フロンティアモデル＝一部の高難度タスク、日常業務＝安価な自社/軽量モデル" の階層ルーティングが、コスト最適化の標準アーキテクチャになりつつある。M365 Copilot の裏側モデルが不可視で置換されるため、既存利用のコスト・品質の期待値が変動しうる。

**行動指針** M365 Copilot 定着化支援の提案では、裏側のモデル置換を前提にコスト・品質の期待値を再設定する。自社の AI 構成でも「高難度＝フロンティア／日常＝軽量モデル」の階層ルーティングをコスト設計の基本形として検討する。

- https://www.bloomberg.com/news/articles/2026-07-07/microsoft-replaces-openai-anthropic-with-own-ai-in-some-apps

### 3. Claude Code v2.1.203〜205 — ヘッドレス/クラウド実行のフック不具合を修正、auto mode の安全策を強化 — スケジュール実行・リモートワーカー運用に直結

**事実** Claude Code が [7/8 記録の v2.1.202](./ai-news-daily-2026-07-08.md) から連日更新し **v2.1.205（7/8）** まで進行（github raw CHANGELOG 一次確認。※当初 02/03 ソースでは v2.1.204 までの記録だったが、01_ai-news-Master で v2.1.205 を一次確認し補正）。**v2.1.205** は auto mode がセッション transcript 改ざんをブロック／解決できない変数への `rm -rf` を実行前に確認、`/doctor` をセットアップ総合診断に格上げ（`/checkup` はエイリアス）、agent view 刷新（色付き state 語 + headline 表示・PR 自動リンク）、auto-update のピークメモリ約 400MB 削減。**v2.1.204** は、ヘッドレスセッションで SessionStart フックのイベントがストリーミングされず、リモートワーカーがフック実行中に idle 判定で回収される不具合を修正。**v2.1.203** はバックグラウンドセッション中断前の再認証を促す**ログイン期限切れ警告**、フッターの権限モード表示（グレーの ⏸ バッジ）、追加作業ディレクトリの MCP roots/list 反映、macOS バックグラウンドエージェントの誤低メモリ検出による 15〜20 秒停止・デーモンのトークン失効時無応答・`claude agents` 復帰時のサブエージェント作業消失を修正、コンテキスト使用量インジケータ最適化でメモリ/CPU 退行を解消。

**根拠** anthropics/claude-code の raw CHANGELOG が一次ソース。v2.1.204 の SessionStart フック修正は、まさにクラウド/スケジュール実行（Routines 等）でフックを使う運用に直結する内容。v2.1.205 の transcript 改ざんブロックはバックグラウンド/自律運用の安全策強化。

**影響** ヘッドレス/リモート実行でフックが idle 誤判定で中断される問題が解消され、CI・スケジュール実行の安定性が向上。バックグラウンド運用のメモリ/CPU 退行や再認証まわりの不具合も解消された。

**行動指針** クラウド/スケジュール実行で SessionStart フックを使うチームは v2.1.204 以降へ即更新。バックグラウンドエージェントを常用する環境は v2.1.205 の transcript 改ざんブロック・`rm -rf` 事前確認など安全策強化の恩恵が大きいため v2.1.205 への更新を推奨。

- https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md

## カテゴリ別まとめ

### OpenAI / フロンティアモデル
- **GPT-5.6 広域公開が本日始動**（ハイライト参照）。料金据え置き（Sol $5/$30・Terra $2.5/$15・Luna $1/$6）、ChatGPT/Codex/API へ順次搭載

### Google / DeepMind
- **Gemini 3.5 Pro、GA 目標が 7/17 に具体化（TechTimes、7/8）**: 5/19 I/O 発表・当初6月GA目標から遅延し、7月第2週も限定プレビューのまま。DeepMind が 7/17 を GA 目標とする報道。ただしモデルカード・API ドキュメント・確定価格による公式確認はなお未発表で日付保証はない。GPT-5.6 の本日公開と合わせ、7月中旬に主要フロンティア2モデルが出揃う公算。 https://www.techtimes.com/articles/319877/20260708/gemini-35-pro-targets-july-17-deepseeks-july-24-deadline-hits-developers-now.htm

### Microsoft / MAI・コスト戦略
- **Excel/Outlook の AI を自社 MAI へ置換開始**（ハイライト参照）。GitHub Copilot・Teams へも展開予定

### 開発ツール
- **Claude Code v2.1.205（＋v2.1.204/203）**（ハイライト参照）
- **OpenAI Codex CLI 安定版 0.143.0（7/8）**: Remote plugins をデフォルト有効化、macOS/Windows のシステムプロキシ対応（0.142.5〔7/1〕から更新）。 https://github.com/openai/codex/releases
- **GitHub Copilot VS Code 6月まとめ公開（7/8）**: VS Code 側（v1.123–v1.127）で**エージェント用ブラウザツール GA**（ページ操作/スクショ/Web 検証）・並列セッション・1M コンテキスト対応・クレジット可視化強化。CLI は pre-release を集約した**安定版 v1.0.69**（プラグイン管理ダッシュボード、セッション再起動なしの拡張リロード）に昇格。 https://github.blog/changelog/2026-07-08-github-copilot-in-visual-studio-code-june-2026-releases/
- **GitHub Copilot デスクトップアプリが全プランで提供開始（7/7）**: macOS/Windows/Linux のデスクトップからエージェント駆動開発を開始できるアプリが全 Copilot プランで利用可能に。 https://github.blog/changelog/2026-07-07-github-copilot-app-available-to-all/
- **Cursor / Devin**: 新規なし。Cursor は 3.9（Customize ページ・6/22）／iOS 公開ベータ（6/29）、Devin は Security Swarm（7/1）が最新のまま（cursor.com/changelog は本日も 403）

### Microsoft / Copilot Studio（一次情報の動きなし）
- **Copilot Studio 公式ブログ「Building reliable voice agents: A practical guide」（6/25・回収）**: 音声エージェントをプロトタイプから本番までスケールさせ負荷下でも安定させる設計を扱う実装ガイド。製品リリースではないが、リアルタイム音声エージェント（4月 Preview）を検証する実務者向け内容。 https://www.microsoft.com/en-us/microsoft-copilot/blog/copilot-studio/
- **Released Versions**: 最新は Build 2026.6.3（6/30初出）のまま。版ページ（火曜更新）に次ビルド 2026.7.x は依然未反映。リージョン展開も変化なし（11リージョンが 2026.6.3／UK・Asia・Japan・Europe・UAE が 2026.6.2／US 本体・Australia・GCC が 2026.6.1）。次回火曜 7/14 が要監視
- **What's New**: June 2026 セクションのまま7月項目なし。**M365 Copilot Release Notes**: July 01 バッチが最新、off-cycle バッチなしを一次確認。次バッチは隔週傾向で 7/14〜7/15 前後見込み
- **Power Platform Blog / Message Center / Roadmap**: 「What's New in Power Platform: July 2026」は未公開（最新は 6/11 の June Feature Update）。7/9 の新規 MC 番号・大型発表は未検出（固有MC番号の網羅は手動確認推奨）

## 直近の注目予定

- **7/9（本日）** GPT-5.6 広域公開始動（Sol/Terra/Luna グローバル展開）
- **7/13** Claude Code の週次上限+50%プロモ（5月開始）の期限（延長なき場合）
- **7/14** 破壊的変更: Visio → Power Automate エクスポート廃止発効（Current Channel は 6/30 適用済み）／M365 Copilot Release Notes 次バッチ見込み／Copilot Studio 版ページ次更新（2026.7.x 反映見込み）
- **7/14–15** VB Transform 2026 開催
- **7/17** Gemini 3.5 Pro GA 目標日（未確定）／Claude Corps 第1期応募締切
- **7/15** Claude Science（AI for Science）応募締切
- **7/16・7/23** GitHub Models ブラウンアウト（7/30 全面廃止に向けた移行予行）
- **7/21** Copilot Cowork GA 告知イベント
- **7/23** OpenAI computer-use-preview シャットダウン
- **7/30** GitHub Models 全面廃止 → Azure AI Foundry 移行必須
- **7/31** Devin classic 環境設定の read-only 参照終了
- **8/1** covered frontier model 60 日 EO 期限（GPT-5.6/Gemini 3.5 Pro の広域リリース条件を規定）
- **8/3** 旧「Claude in Slack」退役
- **8/5** Opus 4.1 Claude API 退役
- **8/26** OpenAI Assistants API 廃止／o3 退役／GPT-4.5 完全廃止
- **8/31** Sonnet 5 促進価格終了（$2/$10 → $3/$15）
- **9月** iOS 27 / macOS 27 GA（AFM 3 本番）

## 改善メモ

- **【欠損リカバリ実施】01_ai-news-Master の 7/9 分**: 当初欠損だった `digests/2026/07/ai-news-2026-07-09.md` が翌 7/10 に取得可能となったため、本サマリーを3ソースで再生成・上書き（Sol Fast $12.5/$75・GPT-Live Voice・gpt-realtime-2.1 を追記、Claude Code の版を v2.1.204→v2.1.205 に補正）。前夜（7/8 夜）の Master 側ルーチンは翌朝までに復旧したとみられる。
- **ソース間の版差を検出・補正**: Claude Code の最新版について 02/03 ソースは v2.1.204 まで、01 ソースは v2.1.205（いずれも 7/8）を記録。01 の一次確認（github raw CHANGELOG）に合わせ v2.1.205 に統一した。
- **RSS/WebFetch 全ソース403継続**（02/03）: WebSearch で収集。取得方法の WebSearch 優先化提案（B-004）が10回目の継続。github.blog も 403 継続。
- ソース間で GPT-5.6 の 7/9 公開・Microsoft 一次情報の静穏が整合。上記の版差以外に矛盾は検出されず。
