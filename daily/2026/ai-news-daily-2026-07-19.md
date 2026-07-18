# AI News Daily Summary — 2026-07-19

> 本サマリーは 01_ai-news-Master・02_ai-news-Copilot・03_ai-news-industry の3ソース（7/19分）を統合して作成。

日曜。前日の静けさから一転、週末の主役は**中国 Moonshot「Kimi K3」**。7/17 WAIC で公開された 2.8兆パラメータのオープンウェイト・フロンティア級モデルが「第二の DeepSeek ショック」として半導体売り（TSMC 約-7%・ソフトバンク約-9%）を誘発し、「低価格×オープン×主権AI」を国際枠組みごと押し出す中国の構図が鮮明に。Anthropic 側では**Fable 5 の無償枠が本日 7/19 23:59 PT で終了**（3度目の延長を経て以降は前払いクレジット従量課金）、**Claude Code v2.1.214** がディレクトリ権限バイパスや Windows PowerShell 権限昇格などのセキュリティ修正を伴い着地（Master／Copilot 一致）。最注目の **Gemini 3.5 Pro GA は目標日 7/17 を2日超過も公式発表なし**。WAIC は 7/20 最終日、Microsoft は「Project Perception」でマルチモデル・ルーティングのAIセキュリティに参入。

## 今日のハイライト

### 1. Moonshot「Kimi K3」— 2.8兆パラメータのオープンウェイトが「第二の DeepSeek ショック」、半導体売りを誘発 — 中国勢がフロンティア級×低価格×オープンを同時提示

**事実**: 7/17（金）WAIC 会場で Moonshot AI が「Kimi K3」を公開。2.8兆パラメータ・1Mトークン文脈のオープンウェイト多モーダル推論モデルで、総合性能は Claude Fable 5・GPT-5.6 Sol に次ぐ2番手、コーディング/エージェントでは Opus 4.8・GPT-5.5 を上回ると自称。API は入力$3／出力$15（100万トークン、キャッシュ入力$0.30＝9割引）とフロンティア級の約1/3。オープンウェイトは 7/27 公開予定。

**根拠**: Automation Bench 30.8・SpreadsheetBench 2 34.8・BrowseComp 91.2 で首位を主張。発表直後に「第二の DeepSeek ショック」として半導体売りが波及し、金曜に TSMC 約-7%・ソフトバンク約-9%。

**影響**: 中国勢が「フロンティア級に肉薄×低価格×オープンウェイト」を同時に提示した決定版事例。WAIC での習近平「オープンソースAI」旗振り・WAICO ブロック（後述）と符合し、主権AI／コストの議論に直結する。ただし推論トークンも出力課金のため、実タスクではトークン消費が Fable 系より嵩むとの実測報告あり。

**行動指針**: 提案資料のコスト／主権AI論点の一次材料として押さえる。7/27 のオープンウェイト公開後にベンチの第三者検証とトークン消費実測を確認し、自称性能を鵜呑みにしない。

- https://fortune.com/2026/07/17/china-moonshot-kimi-k3-markets-china-ai/
- https://www.cnbc.com/2026/07/17/moonshot-ai-kimi-k3-model-openai-anthropic-china.html
- https://openrouter.ai/moonshotai/kimi-k3

### 2. Anthropic Fable 5 — サブスク無償枠が本日 7/19 23:59 PT で終了、以降は前払いクレジット従量課金 — Fable 5 常用のコスト再見積もりが必須に

**事実**: 6/22→7/12→7/19 と3度延長された Fable 5 の無償枠（Pro/Max/Team・対象 Enterprise で週次上限の最大50%まで追加費用なしで利用可）と、Claude Code の週次上限50%ブースト特典が本日 23:59 PT で終了。7/20 以降は前払いクレジット（$10／$50）での従量課金が標準運用となり、通常の使用上限が復帰する。

**根拠**: 従量課金は入力$10／出力$50（100万トークン）。「compute が整い次第サブスク復帰」との方針は不変。並行して Opus 5 とみられるモデルが Cursor に一時出現（7/12）とのリークがあり、無償枠終了と次期フラッグシップ投入のタイミングが注視される。

**影響**: Fable 5 を常用してきたワークフローは本日以降コスト構造が変わる。無償枠に依存した検証・生成タスクは実費が発生する。

**行動指針**: 本日中に Fable 5 常用タスクの月次コストを再見積もりし、必要に応じて Opus 4.8 等への振り分け方針を決める。前払いクレジット（$10／$50）の要否を判断する。

- https://www.bleepingcomputer.com/news/artificial-intelligence/claude-fable-5-stays-free-for-paid-users-until-july-19-as-anthropic-buys-more-time/
- https://dataconomy.com/2026/07/13/claude-fable-5-free-access-extended-july-19/
- https://www.anthropic.com/news

### 3. Claude Code v2.1.214 — ディレクトリ権限バイパス等のセキュリティ修正、新ツール `EndConversation` 追加 — 権限系の穴を塞ぐメンテナンスリリース

**事実**: 7/18 に Claude Code v2.1.214 が着地。機能追加より「セキュリティと権限システムの修正」に主眼を置き、ネストしたディレクトリの権限ルール・バイパス、Windows PowerShell の権限昇格、ファイルディスクリプタのリダイレクトや超長コマンド（>10,000文字）を含む Bash 権限チェックを是正。

**根拠**: 新機能は濫用対応の `EndConversation` ツール、長時間ツール実行中の定期進捗ハートビート、メモリファイル frontmatter への ISO `modified` タイムスタンプ、OpenTelemetry 拡張など。Docker/Podman デーモンのリダイレクトフラグは権限確認プロンプトの対象に。Master／Copilot 両ソースが一致して報告。

**影響**: 前日 7/18 に報告された plan モードの権限バイパス脆弱性系と同じ「権限系の穴を塞ぐ」流れ。CLI をローカル運用する開発者はセキュリティ修正の適用が推奨される。

**行動指針**: Claude Code 利用者は v2.1.214 へ更新する。Windows/PowerShell 環境や CI で Bash 権限に依存する構成は特に優先。changelog で自環境に関わる修正項目を確認する。

- https://code.claude.com/docs/en/changelog

## カテゴリ別まとめ

### Anthropic / Claude
- **Fable 5 無償枠終了（本日 7/19）**（ハイライト参照）
- **Claude Code v2.1.214 セキュリティ修正**（ハイライト参照）
- **Claude「Reflect」ダッシュボード（ベータ）**: Claude 利用状況とAI習慣を可視化・追跡するアナリティクス機能を導入。メモリ機構は日次サマリーからカテゴリ別の個別エントリへ移行（メモリ有効の Free/Pro/Max 対象）。
- **Opus 4.1 API 提供終了は 8/5**、ユーザー移行が必要。Anthropic はヘルスケア連携を継続し、Enterprise/API 向けにセルフサービスの HIPAA 設定を提供。

### Google / DeepMind
- **Gemini 3.5 Pro GA**: 目標日 7/17 を2日超過した 7/19 時点でも公式発表（モデルカード／価格ページ／`gemini-3.5-pro` API リスティング）は未確認。公開APIは gemini-3.5-flash / gemini-3.1-pro-preview のままで Vertex AI の限定エンタープライズプレビュー止まり。噂ベースの想定は 2Mトークン文脈・Deep Think 層・API $3/$18 前後（未確認）。延期の穴埋めに Gemini 3.6 Flash 先行投入との観測も。予測市場は 7/31（約81%）と 8/7（約73%）で割れる。
  - https://coursiv.io/blog/gemini-3-5-pro
  - https://www.techtimes.com/articles/320736/20260716/rebuilt-gemini-35-pro-misses-third-deadline-google-eyes-stopgap-release.htm

### Microsoft / GitHub
- **「Project Perception」**: Microsoft/OpenAI/Anthropic の複数モデルを束ね、コード・クラウド・エンドポイント横断で脆弱性を検知→影響説明→修正案提示するAIセキュリティ製品を今月中投入予定（7/17 報道）。各処理を最適モデルへ割り振るオーケストレーション層でコストを抑え、Anthropic の Mythos（高単価）に「安さ」で対抗。MS の自社 MAI 置換（7/7）と同じ階層ルーティング路線の延長。
  - https://www.techrepublic.com/article/news-microsoft-project-perception-ai-security-tool/
  - https://windowsnews.ai/article/microsofts-project-perception-aims-to-make-ai-vulnerability-fixing-cheap-enough-to-run-nonstop.439207
- **Microsoft 一次情報源は静穏**: M365 Copilot は 7/15 リリースバッチ据え置き、Copilot Studio は Build 2026.6.3（11リージョン）据え置き。次回更新見込みは 7/21（火）。

### OpenAI / 開発ツール
- **OpenAI Codex CLI Stable 0.144.6（7/18）**: GPT-5.6 Sol/Terra/Luna 向けのバンドル指示更新で文脈長を **272,000トークン**に訂正。機能追加ではなくモデルメタデータの修正。Alpha は 0.145.0-alpha.23（7/17）へ。
  - https://github.com/openai/codex/releases
- **その他ツール**: GitHub Copilot CLI は v1.0.71 stable 据え置き、Cursor はコミュニティ報告で 3.12.x 更新、Devin は 8/31 まで Claude Sonnet 5 を統合。

### 規制・政策 / 市場
- **WAIC 2026（7/17-20 上海、7/20 最終日）**: 習近平が基調で各国に「オープンソースAIの歴史的好機」を掴むよう呼びかけ、特定国の技術独占を牽制。29カ国署名の「世界AI協力機構（WAICO、本部上海）」の高官級会合には国連グテーレス事務総長も同席し、グローバルサウス軸の対抗ブロックの体裁が固まった。Kimi K3 のオープンウェイト路線と符合。
  - https://www.aljazeera.com/news/2026/7/17/chinas-xi-jinping-launches-new-ai-alliance-what-is-it
- **半導体市場**: Kimi K3 ショックで金曜に TSMC 約-7%・ソフトバンク約-9%（ハイライト参照）。

## 直近の注目予定

- **7/19（本日）**: Fable 5 無償枠終了 / Claude Code 週次上限ブースト特典終了（23:59 PT）
- **7/20**: WAIC 2026 最終日
- **7/21**: Copilot Studio 次回更新見込み（要監視）
- **7/23**: OpenAI computer-use-preview 提供終了
- **7/27**: Kimi K3 オープンウェイト公開予定
- **7/31**: Devin classic read-only 設定リファレンス期限
- **8/1**: 対象フロンティアモデルの大統領令60日期限
- **8/3**: 旧「Claude in Slack」提供終了
- **8/5**: Opus 4.1 Claude API 提供終了 / Cowork 倍増利用ボーナス失効
- **8/9**: ChatGPT Atlas 提供終了
- **8/26**: OpenAI Assistants API 廃止 / o3 退役 / GPT-4.5 完全提供終了
- **8/31**: Sonnet 5 プロモ価格終了（→ $3/$15）/ Devin の Sonnet 5 統合終了
- **9月**: iOS 27 / macOS 27 GA（AFM 3 production）

## 改善メモ

- 3ソースとも新規提案・障害の変化なし。継続項目: industry 側 B-004「WebSearch 優先化」20回目（詳細は IMPROVEMENT-BACKLOG.md）。
- Master 側は日曜のため週次リカバリチェックを免除、次回検証は 7/20（月）に開発者・コミュニティプラットフォーム RSS フィードで実施予定。
- Kimi K3 のベンチマーク値・性能順位は Moonshot 自称ベース。第三者検証（7/27 オープンウェイト公開後）まで確定情報として扱わない。
- Gemini 3.5 Pro の仕様・価格・GA日は全て報道／噂ベース。公式 launch post 確認後に更新する。
