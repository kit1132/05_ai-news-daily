# AI News Daily Summary — 2026-07-14

> 本サマリーは 01_ai-news-Master・02_ai-news-Copilot・03_ai-news-industry の3ソース（7/14分）を統合して作成。

火曜。**本日発の大型モデルローンチはなし**。実イベントは **VB Transform 2026 開幕（7/14-15・Menlo Park）** と **GPT-5.6 の ChatGPT Team 全面提供が本日着地**（API 7/7→Plus 7/10→Team 7/14）、前日には **iOS 27 初回 Public Beta が公開**（7/13、刷新版 Siri が一般ベータへ）。開発ツールは **Codex CLI が 0.144.2/0.144.3 を連続リリース**（Guardian 自動レビューのリグレッション巻き戻し）した以外は据え置き。提供条件面では **OpenAI が GPT-5.6 Sol の需要急増で利用枠を一時緩和**、**Claude Code の週次上限+50%促進が 7/13 終了**、Microsoft 側は **Visio → Power Automate エクスポート廃止が本日発効**。加えてコンサル提案に直結する既報の市場データ2件——**中国製モデルの米エンタープライズ・トークンシェア最大46%** と **Claude Cowork の9割超が非コーディング**——を本日のハイライトとして捕捉した。

## 今日のハイライト

### 1. 中国製モデルが米エンタープライズ・トークンの30〜46%を占有 — 「効率重視」トレンドの定量的決定版（CNBC）

**事実**: CNBC 調査（7/7）によると、OpenRouter 上の米エンタープライズ・トークン量で **中国発モデルのシェアが 2/8 以降毎週30%以上、年央には週次で最大46%に到達**。直近12カ月平均11%、2025年上期はわずか4.5%からの急伸。主因は価格で、オープンソース中国モデルは Anthropic/OpenAI 主力比 **60〜90%安**（DeepSeek V4 Flash $0.14/百万入力 対 GPT-5.5 $5.00）。Z.ai の GLM 5.2 は投入初週で日次トークン量約27倍・顧客数約80倍。7/8 には米議員が企業での中国モデル利用を問題視し調査に着手。

**根拠**: OpenRouter 実測トークン量という定量ベース。「安価な中国/OSSモデルへのルーティング」が現場で急速に進んでいる実態を、逸話ではなく週次シェアの推移として示した。

**影響**: (1) モデル選定提案の論点が「性能」から「コスト最適化 vs データ主権・調達リスク・規制動向」のトレードオフに移る。(2) 議会調査の着手により、企業での中国モデル利用は今後コンプライアンス・調達ポリシーの検討事項になる。(3) 主力モデルの価格圧力が強まり、Anthropic/OpenAI の価格戦略（促進価格終了・利用枠調整）とも連動する。

**行動指針**: モデル選定提案では「米エンタープライズ・トークンの最大46%が中国製（2026年央）」を引用し、コスト最適化ルーティングとデータ主権・調達リスクを一枚で対比する。中国モデル採用を検討する顧客には議会調査動向をリスク項目として明記する。

- https://www.cnbc.com/2026/07/07/chinese-ai-models-costs-us-openai-anthropic.html
- https://www.cnbc.com/2026/07/08/chinese-ai-models-probe-us-lawmakers.html

### 2. Claude Cowork 利用の9割超は「非コーディング」— エージェントの実需はバックオフィス（Anthropic 利用実態調査）

**事実**: Anthropic の利用実態調査（7/7 公開）は 60万超の組織・120万セッション（5月末2週間）を分析。**ソフトウェア開発はわずか8.7%**、最大は **業務プロセス運用33.4%**（散在情報のレポート集約、オンボーディング・チェックリスト作成、スプレッドシート照合＝財務/人事/総務系）、次いで **コンテンツ制作16.4%**（下書き/スライド/提案書）。DevOps 7%、リサーチ6.4%、データ分析5.8%。**9割超が非コーディング**。

**根拠**: 60万組織・120万セッションという大規模な一次データ。「AIエージェント＝開発者ツール」という支配的ナラティブを実利用分布で否定した。

**影響**: エージェント導入提案のターゲット部門を、開発組織ではなく財務/人事/総務/マーケの定型業務（レポート集約・照合・下書き）に置くべき根拠になる。ROI 試算の組み立て方も「開発生産性」から「ホワイトカラーの定型作業削減」へ変わる。

**行動指針**: エージェント導入提案では対象部門を定型ホワイトバックオフィス業務に設定し、「Cowork 実利用の9割超が非コーディング・最大用途は業務プロセス運用33.4%」を引用する。ROI は開発工数削減ではなく定型作業の削減時間で見積もる。

- https://claude.com/blog/how-people-are-using-claude-cowork
- https://the-decoder.com/claude-coworks-biggest-use-case-is-the-mundane-office-work-nobody-wants-to-own-anthropic-says/

### 3. VB Transform 2026 開幕 — 「パイロットの時代は終わり」、本番投入エンタープライズ・エージェントが主題

**事実**: VentureBeat の旗艦カンファレンス **VB Transform 2026 が本日 7/14〜15、Menlo Park で開催**。登壇は Visa / Target / Mastercard / Instacart / Brex / LangChain など、agentic AI を本番運用する事業会社のエンジニア・アーキテクトが中心。主題はオーケストレーション、LLM 可観測性・評価（LLMOps）、RAG インフラ、推論プラットフォーム最適化、エージェントのセキュリティ・ID。Amazon の AGI 自律研究ラボが「信頼できるエージェント」の設計フレーム（一貫性・堅牢性・予測可能性・安全性）、Intuit が高速・複雑タスク向け AI インフラ再構築事例を提示予定。

**根拠**: 前日（7/13）掲載の VentureBeat Research「評価ギャップ」調査（企業リーダー573名・6月実施）が会議の研究的背骨。競争軸が「モデル選定」から「本番運用のオーケストレーション・評価・ガードレール設計」へ移ったことを、登壇企業の顔ぶれとセッション構成が象徴する。

**影響**: エージェント案件の提案枠組みが、モデル比較から「可観測性／評価／ID・セキュリティ」の運用設計へ移行する。会議のセッション構成をそのまま導入チェックリストの骨子に流用できる。

**行動指針**: エージェント導入提案では会議のトラック構成（オーケストレーション／LLMOps・評価／RAG／セキュリティ・ID）を導入チェックリストの骨子として使い、前日の573名調査の数値（評価をパスしたエージェントの顧客対応失敗を半数が経験、66%が人間レビューなし本番投入を許可/計画）を提案根拠に添える。実キーノートの成果は明日以降に反映。

- https://venturebeat.com/vbtransform2026

## カテゴリ別まとめ

### OpenAI / ChatGPT
- **GPT-5.6（Sol/Terra/Luna）の ChatGPT Team 全面提供が本日 7/14 完了** — Enterprise API 7/7 → Plus 7/10 → Team 7/14 の段階展開が着地。全プランで Sol が既定に。Plus/Pro/Business/Enterprise は Sol を medium 以上 effort で、Pro/Enterprise は Sol Pro も選択可。API 価格据え置き（Sol $5/$30、Terra $2.5/$15、Luna $1/$6）、Enterprise 文脈長 1.5M トークン。**社内標準モデルの棚卸し・effort 設定（コスト対品質）見直しのタイミング**。 https://openai.com/index/gpt-5-6/
- **GPT-5.6 Sol の利用枠を一時緩和（7/12〜13）** — ローンチ48時間で Sol 需要がトラフィックを倍増させたため、OpenAI（Tibo Sottiaux）が対応。**Plus/Pro/Business で5時間利用上限を一時撤廃**、Sol の1タスクあたり消費クォータを削減（推論効率化で約+10%の利用余地）、banked reset を50万ユーザーへ展開（Work/Codex 全ユーザーは 7/14 の 7M マイルストーンで1回付与）。thinking-budget 引き下げ（nerf）疑惑は否定。**組織導入時のクォータ設計に直結する運用変更**。 https://www.explainx.ai/blog/chatgpt-codex-5-hour-limit-removed-weekly-reset-july-2026

### Apple / プラットフォーム
- **iOS 27（macOS 27 等含む）初回 Public Beta が 7/13 公開** — 目玉は刷新版 **Siri AI**（専用アプリ・ウェイトリスト制、Apple Intelligence 対応は iPhone 15 Pro 以降に限定）。ほか AI 写真編集（画像拡張）、Safari のタブ自動整理、Image Playground 強化、Shortcuts のアクセシビリティ改善など。対応機種は iPhone 11 以降（AI 機能は 15 Pro+ ゲート）。GA は9月予定。**Apple Intelligence Extensions / Claude 統合の続報を追う上で、Siri 刷新が一般手元に降りた点が節目**。 https://www.macrumors.com/2026/07/12/ios-27-public-beta-release-date-timing/

### 開発ツール（Codex CLI / Claude Code / Cursor / Copilot CLI）
- **OpenAI Codex CLI 0.144.2 / 0.144.3（7/13）** — 本日唯一の版更新。**0.144.2 は Guardian 自動レビューのリグレッションを是正**し、プロンプト変更を巻き戻して従来のポリシー・リクエスト形式・ツール挙動を復元。0.144.3 はマージ変更なしのバージョンのみリリース。alpha は **0.145.0-alpha.7（7/13）** まで進行。 https://github.com/openai/codex/releases
- **Claude Code / Cursor / Copilot CLI いずれも据え置き** — Claude Code v2.1.207（7/11、Bedrock/Vertex/Foundry で Auto mode 既定有効化・既定モデル Opus 4.8 化）、Cursor 3.11（7/10、Side Chats）、Copilot CLI 安定版 v1.0.70（7/9・GPT-5.6 対応・`--sandbox`/`--no-sandbox`・`/refine`）／pre-release v1.0.71-0 から新版なし。

### Anthropic / Claude
- **Claude Code の週次利用上限+50%促進が 7/13 で終了** — 5/13 開始の Pro/Max/Team/seat 型 Enterprise 向け50%増枠が期限到来、7/14 以降は標準上限に戻る。**Fable 5 有償プランでの無償提供終了（7/12、既報）と併せ、7月中旬は Claude 側の利用枠が絞られる方向**。 https://pasqualepillitteri.it/en/news/2494/claude-code-weekly-limits-50-percent-anti-codex-anthropic-2026
- **Cowork 利用実態調査**（ハイライト参照）。Fable 5 は仕様据え置き（1M context / 128k output / $10・$50）、公式 news の新規なし。

### Microsoft / Copilot / Power Platform
- **破壊的変更が本日 7/14 発効: Visio デスクトップの Power Automate エクスポート廃止**（Learn 一次＋MC1323265）— Visio から BPMN 図をクラウドフローとしてエクスポートする統合を廃止。**Monthly Enterprise / Semi-Annual Enterprise チャネルで本日発効**（Current Channel は 6/30 適用済み）。既存の BPMN 図・エクスポート済みフローは影響なし、移行先は Power Automate 上での直接フロー作成。 https://learn.microsoft.com/en-us/power-platform/important-changes-coming
- **Copilot Studio 版ページ〔火曜更新〕は Build 2026.6.3 据え置き**（Learn MCP 一次確認）。予告の次ビルド 2026.7.x は未反映だが、**2026.6.3 のリージョン展開は前週より拡大（11リージョン、Japan は 2026.6.2 に前進）**。次ビルド反映は次回火曜 **7/21 が要監視**。
- **一次情報の動きなし**: What's New は June 2026 のまま、M365 Copilot Release Notes は July 01 バッチが最新（off-cycle なし・次バッチは 7/15 前後見込み）。月次「What's New in Power Platform: July 2026」・2026 Release Wave 2 計画ページはともに未公開（7月中旬〜下旬公開見込み）。

### Google / DeepMind
- **Gemini 3.5 Pro** は限定 preview 継続。第三者報道は **7/17 GA 目標**で一致するが、Google 公式のモデルカード・API ドキュメント・確定価格は未発表（2M トークン文脈・Deep Think 層を予告）。7/13 時点で公開 API にモデル未掲載。

### 標準・エコシステム
- **エージェント接続標準の分裂（MCP vs ARD）** — Google/Microsoft/Salesforce/Snowflake/ServiceNow/Nvidia/Databricks/GitHub 等が、Anthropic の MCP に対抗する開放標準 **Agentic Resource Discovery（ARD、6/17 公開）** を推進。`ai-catalog.json` マニフェストでエージェントがツール/他エージェントを自動探索。7/7 の MCP Enterprise-Managed Authorization に続き、アプリ横断エージェントの「接続・権限・発見」レイヤーが競争の主戦場に。**導入提案では当面 MCP/ARD 両にらみの設計が無難**。 https://developers.googleblog.com/announcing-the-agentic-resource-discovery-specification/

### SpaceXAI / Grok
- Grok 4.5（7/8、$2/$6、Cursor 共同訓練）以降の新規進展なし。EU 提供は7月中旬めど（EU AI Act の systemic risk 分類による遅延、確定日なし）。

## 直近の注目予定

- **7/14（本日）**: VB Transform 2026 開幕（〜7/15・Menlo Park）/ GPT-5.6 の ChatGPT Team 全面提供着地 / 破壊的変更: Visio → Power Automate エクスポート廃止発効（Monthly Enterprise / Semi-Annual チャネル）
- **7/15**: 新 M365 Copilot アプリ UI（MC1325422）の opt-out トグル終了・以降デフォルト化 / M365 Copilot Release Notes 次バッチ見込み / Claude Science（AI for Science）応募締切
- **7/17**: Claude Corps 第1期応募締切 / Gemini 3.5 Pro GA 候補日（未確定）
- **7月中旬**: Grok 4.5 EU 提供予定 / ChatGPT Work が Plus・Business へ拡大
- **7/21**: Copilot Studio 版ページ次更新（火曜・2026.7.x 反映見込み）/ Copilot Cowork GA 告知イベント
- **7月中旬〜下旬**: 2026 Release Wave 2 計画ページ公開見込み
- **7/23**: OpenAI computer-use-preview シャットダウン
- **7/31**: Devin classic 環境設定の read-only 参照終了
- **8/1**: covered frontier model 大統領令60日期限
- **8/3**: 旧「Claude in Slack」退役
- **8/5**: Opus 4.1 Claude API 退役 / Cowork 倍増利用枠の終了
- **8/26**: OpenAI Assistants API 廃止 / o3 退役 / GPT-4.5 完全廃止
- **8/31**: Sonnet 5 促進価格終了（$2/$10 → $3/$15）
- **9 月**: iOS 27 / macOS 27 GA（AFM 3 本番）

## 改善メモ

- **既報市場データの遅延捕捉**: 中国製モデルのトークンシェア（CNBC 7/7）と Claude Cowork 利用実態（Anthropic 7/7）は、いずれも7/7発の一次データだが 03 のダイジェスト未収録だったものを本日捕捉。提案根拠として価値が高いため日次ハイライトに昇格した。
- **障害の変化なし**: RSS/WebFetch は x.ai/*・cursor.com/changelog・anthropic.com/news・wave2 planned-features 等で 403 継続（各ソースとも WebSearch・二次ソースで補完）。取得方法の WebSearch 優先化提案（03 の B-004、15回目）が継続中。
- **ソース間整合**: iOS 27 Public Beta（Master: 7/13 公開 / industry: GA 9月）、GPT-5.6 Team 展開、Visio エクスポート廃止、Claude Code 促進終了の各件で3ソース間の内容矛盾は検出されず。
</content>
</invoke>
