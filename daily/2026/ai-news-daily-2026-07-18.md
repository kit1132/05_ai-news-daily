# AI News Daily Summary — 2026-07-18

> 本サマリーは 01_ai-news-Master・02_ai-news-Copilot・03_ai-news-industry の3ソース（7/18分）を統合して作成。

土曜。大型ローンチのない静かな一日。**WAIC Day2 で「WAICO」29カ国が正式署名**し主権AIブロックが発足、**Claude Code v2.1.212** が `/fork` の挙動変更・セッション上限新設・セキュリティ修正を含む実務更新。**Gemini 3.5 Pro は目標日 7/17 を過ぎても GA なし**、予測市場は 7/30 を最有力（約52%）としつつ未リリースの可能性も約23%。

## 今日のハイライト

### 1. WAIC Day2：主権AIブロック「WAICO」29カ国が正式署名 — 中国AI産業は2025年に1兆元超

**事実**: WAIC 2026（7/16-20・上海）Day2 で、29カ国が「世界AI協力機構（WAICO）」創設協定に正式署名。習近平が同大会初の基調講演に登壇し、西側AIガバナンス体制への対抗ブロックが発足した。中国 NDRC は「AI関連産業が2025年に1兆元（約$147B）超、2026年は30%超成長見込み」と公表。7/18 には学術会議 WAICA が開幕（282投稿中57採択・採択率約20%・10カ国超）。展示は108チップ・261基盤モデル・208身体性端末。

**根拠**: 産業規模（1兆元・30%成長）と展示規模が定量的に示されている。前日の MiniMax M3（100万トークン文脈）・Huawei Atlas 950（最大8,192枚接続）発表と併せ、中国勢の「低価格×大規模」路線が製品・スペック付きで具体化している。フロンティア3社CEOの「公開前外部審査」提唱（7/16）と対になる動きで、AIガバナンスの二極化が同一週に可視化された。

**影響**: AIガバナンスが「西側主導の一枠組み」から「米中二極」へ移行する転換点。モデル調達・データ規制・輸出管理の前提が変わりうる。前日のフロンティア3社CEO提唱と併せ、今後の調達要件に「どちらの規制枠組みに準拠するか」が加わる可能性がある。

**行動指針**: 公共・規制業種の案件では「AIガバナンスの二極化」を前提変数として認識する。ただし WAICO は署名段階で実効的な基準の内容は未定。具体的な制度設計の進展を継続監視し、確定情報が出るまで調達判断には反映しない。会期中（〜7/20）の追加発表を引き続きウォッチ。

- https://www.techtimes.com/articles/320812/20260717/china-launches-rival-ai-governance-bloc-waic-2026-opens-300-product-debuts.htm
- https://en.people.cn/n3/2026/0708/c90000-20475542.html

### 2. Claude Code v2.1.212 — `/fork` の挙動変更・セッション上限新設・セキュリティ修正

**事実**: Claude Code v2.1.212（7/17）がリリース。主な変更は3点。(1) `/fork` が会話を新規バックグラウンドセッションへコピーする方式に変更（現行作業を維持、セッション内サブエージェント起動は `/subtask` へ置き換え）。(2) WebSearch のセッション全体上限（既定200・`CLAUDE_CODE_MAX_WEB_SEARCHES_PER_SESSION`）とサブエージェント生成のセッション上限（既定200・`CLAUDE_CODE_MAX_SUBAGENTS_PER_SESSION`）を新設。2分超の MCP ツール呼び出しは自動でバックグラウンド移行。(3) plan モードがファイル変更 Bash を権限プロンプトなしで自動実行する不具合と worktree 作成時の symlink 脆弱性を修正。

**根拠**: `/fork` は v2.1.211 まで「現セッション内でサブエージェントを起動」だったが、v2.1.212 で「会話を別セッションにコピー」に変わった。既存ワークフローで `/fork` を多用しているユーザーは挙動が変わる。セッション上限は長時間自律実行での暴走ループ・コスト暴走を防ぐ安全策。plan モードの権限バイパスは深刻度の高い不具合。

**影響**: `/fork` を「並行作業の分岐」として使っていた場合は `/subtask` への移行が必要。セッション上限（200回）は通常利用では到達しないが、自動化パイプラインや長時間エージェントタスクでは制約になりうる（環境変数で調整可能）。

**行動指針**: `/fork` を使っている場合は `/subtask` への置き換えを確認する。自動化パイプラインでは `CLAUDE_CODE_MAX_WEB_SEARCHES_PER_SESSION` と `CLAUDE_CODE_MAX_SUBAGENTS_PER_SESSION` の既定値200が十分かを検証。plan モードのセキュリティ修正があるため v2.1.212 への更新を推奨。

- https://code.claude.com/docs/en/changelog
- https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md

### 3. Gemini 3.5 Pro — 目標日7/17を過ぎてもGA未発表、予測市場は7/30を最有力視

**事実**: リーク報道の GA 目標日 7/17 を経過したが、Google はモデルカード・API・料金・2Mトークン context のいずれも未発表。公開 API は gemini-3.5-flash / gemini-3.1-pro-preview のまま、Vertex AI 限定 preview が継続。予測市場は 7/30 を最有力（約52%）、7/31 までにリリースなしの可能性も約23%。

**根拠**: 報道ベースの想定スペック（2Mトークン文脈・Deep Think 推論層・$15/$60）はすべて未確認。WAIC 開催期間と重なっており発表タイミングの調整が入っている可能性もあるが、公式は沈黙。

**影響**: Gemini 3.5 Pro を前提とした技術検証やベンダー選定は引き続きスケジュールが立たない。Claude Sonnet 5 / GPT-5.5 との比較評価を計画している場合、Gemini 側の遅延を織り込む必要がある。

**行動指針**: 7/30 前後を次の確認ポイントとしつつ、未リリースの可能性（23%）も想定して代替シナリオを用意する。GA 確定まで報道ベースのスペック値を前提に判断しない。経過観察。

- https://www.techtimes.com/articles/320308/20260713/gemini-35-pro-targets-july-17-after-full-rebuild-every-spec-remains-unconfirmed.htm
- https://startupfortune.com/google-delays-gemini-35-pro-launch-to-july-17-after-scrapping-its-base-model/

## カテゴリ別まとめ

### コーディングエージェント / 開発ツール
- **Claude Code v2.1.212**（ハイライト参照）
- **GitHub Copilot CLI v1.0.72-1（7/17・pre-release）** — プラグイン変更操作を `--plugin` / `--mcp` / `--skill` フラグでサポート、スキル削除に対応。plan 承認メニューのモデル間統一、ディレクトリ可視性のエージェント文脈保持を追加。安定版は v1.0.71（7/16）据え置き。 https://github.com/github/copilot-cli/releases
- **OpenAI Codex CLI** — 安定版 0.144.5 据え置き。alpha は 0.145.0-alpha.22（7/17）まで進行（リリースノート詳細なし）。 https://github.com/openai/codex/releases
- **据え置き**: Cursor 3.11（7/10）/ Devin SWE-1.7（7/8）は新版なし。

### モデル・プラットフォーム
- **Gemini 3.5 Pro GA 未発表**（ハイライト参照）
- **OpenAI GPT-Live-1（catch-up・7/8投入）** — 全二重（full-duplex）音声モデル。聞きながら同時に話せるアーキテクチャで、Web検索や深い推論はバックエンドの GPT-5.5 に委譲。Go/Plus/Pro は GPT-Live-1、Free は GPT-Live-1 mini が既定。API は近日提供予告。 https://openai.com/index/introducing-gpt-live/ / https://techcrunch.com/2026/07/08/openai-releases-new-voice-models-for-more-natural-live-conversations/

### AI業界・資本
- **WAIC Day2: WAICO 29カ国正式署名**（ハイライト参照）
- **Anthropic IPO（継続・小幅更新）** — 7/15 開始の投資家プレ面談が進行中。公開 S-1 が8〜9月、プライシングが10〜11月との観測が加わった。主幹事 Goldman/Morgan Stanley/JPMorgan、$965B評価。 https://www.cnbc.com/2026/07/15/anthropic-ipo-banks-investor-meetings.html / https://www.startuphub.ai/ai-news/ipo-watch/2026/anthropic-ipo-roadshow-begins-2026-07-16

### Microsoft / Copilot Studio
- **新規動向なし。** Copilot Studio What's New は June セクションのまま、Release Notes は 7/15 バッチが最新、Released Versions は 2026.6.3 据え置き。**次回火曜 7/21 が 2026.7.x 反映の要監視日**。 https://learn.microsoft.com/en-us/power-platform/released-versions/copilotstudio

## 直近の注目予定

- **7/19（明日）**: Fable 5 無償提供終了（→ 7/20 から前払いクレジット $10/$50）/ Claude Code 週次上限 +50% 終了
- **7/20**: WAIC 2026 閉幕
- **7/21**: Copilot Studio Released Versions 次更新（2026.7.x 反映見込み）
- **7/23**: OpenAI computer-use-preview シャットダウン
- **7/30 前後**: Gemini 3.5 Pro GA 最有力日（予測市場約52%）
- **7/31**: Devin classic 環境設定 read-only 参照終了
- **8/1**: covered frontier model 大統領令60日期限
- **8/3**: 旧「Claude in Slack」退役
- **8/5**: Opus 4.1 Claude API 退役 / Cowork 倍増利用枠終了
- **8/9**: ChatGPT Atlas シャットダウン
- **8/26**: OpenAI Assistants API 廃止 / o3 退役 / GPT-4.5 完全廃止
- **8/31**: Sonnet 5 促進価格終了（→ $3/$15）
- **9月**: iOS 27 / macOS 27 GA（AFM 3 本番）

## 改善メモ

### Master
- 障害の変化: `developers.openai.com/changelog` と `community.openai.com/c/announcements/6.rss` が本日 403（07-15 の codex/changelog 再障害が OpenAI 開発ドメイン全体へ拡大）。WebSearch フォールバックで代替でき情報欠落なし。次回月曜 07-20 の復旧チェック対象

### Copilot
- 新規提案・障害の変化なし（継続分は IMPROVEMENT-BACKLOG.md 参照）
- 継続提案 5件（最多: B-005 Qiita RSS→WebSearch 前提化、5回目）
- 次の節目: 7/21（CS 版ページ次更新 2026.7.x 見込み）、7/29 前後（Release Notes 次バッチ見込み）、7/30（メモリ活用エージェント提案 GA）、8/5（Claude Opus 4.1 API 提供終了）

### Industry
- 新規提案・障害の変化なし（継続: B-004 WebSearch優先化 19回目。詳細は IMPROVEMENT-BACKLOG.md 参照）

### ソース間整合
- 3ソース間で内容矛盾は検出されず。Claude Code v2.1.212 は Master・Copilot で一致。Gemini 3.5 Pro の状況は Master・Industry で一致。Copilot CLI は Master が v1.0.72-1（pre-release）を検出、Copilot は v1.0.71（安定版）据え置きと報告 — 観測対象の差異（pre-release vs 安定版）で矛盾ではない。
