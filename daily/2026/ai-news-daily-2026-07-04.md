# AI News Daily Summary — 2026-07-04

> 本サマリーは 01_ai-news-Master・02_ai-news-Copilot・03_ai-news-industry の3ソース（7/4分）を統合して作成。

## 今日のハイライト

### 1. Claude Code v2.1.200 — デフォルト権限モードが「Manual」に、自動継続を廃止（安全側の既定変更）

**事実**: Claude Code v2.1.200（7/3）で、デフォルト権限モードが `default` → **Manual** に改称・変更された（CLI / `--help` / VS Code / JetBrains 共通、`--permission-mode manual` / `"defaultMode": "manual"` を受理）。加えて **`AskUserQuestion` ダイアログが既定で自動継続しなくなった**（アイドルタイムアウトは `/config` でオプトイン）。v2.1.199/200 では背景セッション・サブエージェントの安定性も集中修正（sleep/wake 後の無言停止、レート制限で打ち切られたサブエージェントの空結果、ストリーミング API エラー時の部分出力破棄など）。

**根拠**: 01・02 の両ソースが一致して報告。02 は起動クラッシュ修正（`.claude.json` の非配列 disabledMcpServers/enabledMcpServers）やスタック実行スラッシュスキルの先頭5個ロード（従来1個）も明記。

**影響**: エージェントが承認を待たず勝手に進む挙動が絞られ、承認が明示操作に寄る。CI や無人ルーチンで `AskUserQuestion` の自動継続に依存していたフローは停止しうる。

**行動指針**: 無人・自動化フローを持つチームは `/config` でアイドルタイムアウトを明示オプトインするか、`--permission-mode` を運用に合わせて明示指定する。安定版へ更新推奨。

- https://code.claude.com/docs/en/changelog
- https://github.com/anthropics/claude-code/releases

### 2. Cursor に致命的 RCE 脆弱性「DuneSlide」— 3.0 未満は要更新（CVSS 9.8×2）

**事実**: Cato AI Labs が Cursor の2つの重大脆弱性を公開（**CVE-2026-50548 / CVE-2026-50549**、いずれも CVSS 3.1 = 9.8）。**間接プロンプトインジェクション → サンドボックスエスケープ → 開発マシン上での RCE** に至る。攻撃ベクトルは MCP 接続先や Web 検索結果に埋め込まれた指示（ユーザーが入力しない）。**Cursor 3.0（4/2）で修正済み、3.0 未満の全バージョンが影響**。実運用での悪用は未確認（研究開示）。

**根拠**: 02 が詳細を報告。50548 は `run_terminal_cmd` が非既定 `working_directory` を使う際の未検証書込みでサンドボックスヘルパーを上書き、以降のコマンドサンドボックス化を無効化。50549 は symlink 解決の失敗後にプロジェクト内パスを信頼するフォールバックを悪用。

**影響**: MCP や Web 検索を有効化した Cursor 利用組織で、外部コンテンツ経由の遠隔コード実行リスク。攻撃にユーザー操作を要さない点が深刻。

**行動指針**: 組織内 Cursor を **3.0 以上へ即時更新**。3.0 未満の利用状況を棚卸しし、更新完了まで信頼できない MCP エンドポイント・外部検索連携を制限する。

- https://thehackernews.com/2026/07/critical-cursor-flaws-could-let-prompt.html

### 3. Anthropic の売上ラン・レートが $30B 超で OpenAI を逆転（訓練コスト効率が収益優位に）

**事実**: Anthropic の売上ラン・レートが **$30B 超**に達し、OpenAI を上回る状況が報告された。Q1 で **80倍成長**を記録し、Claude（Sonnet 5 / Claude Code など）の需要加速が要因。モデル訓練コストが OpenAI の約 **1/4** という効率優位が収益面の逆転に直結しているとの分析。

**根拠**: 03（industry）が報告。関連して VC も動き、Anthropic 投資の含み益（約 $14B 相当）を背景に Menlo Ventures が自社最大 $3B ファンドを組成。

**影響**: フロンティアモデル市場の収益リーダーシップが流動化。訓練効率がそのまま価格・利益率の競争力になりつつあり、投資マネーは「インフラ・フロンティアモデル・AIネイティブアプリ」へ再配分が進む。

**行動指針**: モデル選定でコスト効率と需要トレンドを継続監視。ベンダーロックインを避けつつ、Claude 系の価格・キャパシティ動向（後述の Fable 5 従量課金移行等）を織り込んで調達計画を立てる。

- 出典: 03_ai-news-industry ダイジェスト（原文に個別出典URLの記載なし。改善メモ参照）

## カテゴリ別まとめ

### Anthropic / Claude
- Claude Code v2.1.200 — デフォルト Manual・自動継続廃止・安定性修正（ハイライト参照）
- **Fable 5 従量課金へ移行**: 7/7 まで週次利用上限50%、以降は使用クレジット（**入力 $10 / 出力 $50 per M tokens**）。クレジット未有効化テナントは 7/7 以降アクセス不可。キャパシティ確保後にサブスク標準へ復帰予定 — https://www.anthropic.com/news/redeploying-fable-5
- **Claude Enterprise に管理者向け強化** — リッチな利用分析、モデル単位の entitlement 制御、spend アラート — https://www.anthropic.com/news
- **隠しコード（steganography マーカー）を削除**（修正7/1）— base URL 環境変数を検査し中国系AIラボ等のホスト名一致を検出する仕組みを撤去。より強力な代替策への移行が理由 — https://www.theregister.com/ai-and-ml/2026/07/01/anthropic-is-removing-its-covert-code-for-catching-chinese-competitors/5265366
- **Anthropic × Samsung、カスタムAIチップで予備協議**（The Information、7/2）— 2nm ファウンドリを狙う。AWS Trainium / Google TPU / Nvidia GPU は中核継続、カスタムチップは「追加レイヤー」 — https://techcrunch.com/2026/07/02/anthropic-is-discussing-a-new-custom-chip-with-samsung/

### OpenAI / Codex
- **GPT-5.6 Sol / Terra / Luna** は約20組織の限定プレビュー継続（一般提供「数週間内」、ChatGPT 未提供、個人利用未対応）。**Sol は7月に Cerebras 上で最大 750 tok/s のレーン**（$20B の Cerebras 推論契約に付随）。価格 Sol $5/$30・Terra $2.5/$15・Luna $1/$6 per Mtok — https://openai.com/index/previewing-gpt-5-6-sol/
- Codex CLI: 安定版 0.142.5（7/1、WebSocketトレースログ書込み修正）/ 0.143.0-alpha.35（7/3、リリースノート未掲載）。実質最新機能は 0.142.2（6/25） — https://github.com/openai/codex/releases

### Google / DeepMind
- Gemini 3.5 Pro は7月延期継続、Vertex AI 限定 Enterprise preview のみで GA 日未定（2M context / Deep Think、Ultra $250/月）
- Noam Shazeer（Transformer 論文著者・Gemini 共同リード）が OpenAI へ移籍と報道

### Microsoft / GitHub Copilot
- **Copilot CLI が GitHub Actions で PAT 不要に** — 組込み `GITHUB_TOKEN` で動作、PAT 作成・保管の運用/セキュリティリスクを低減 — https://github.blog/changelog/2026-07-02-copilot-cli-no-longer-needs-a-personal-access-token-in-github-actions/
- **Copilot エージェントセッションのストリーミングが Public Preview**（EMU エンタープライズ）。CLI v1.0.68 は kimi-k2.7-code 対応
- Copilot Studio は一次情報静穏（What's New は6月分のまま、次ビルド 2026.6.3 系は 7/7 予定）。M365 Copilot Vision の7月ロールアウト、**Copilot Cowork GA 発表イベントは 7/21**

### Cursor / 開発ツール
- **Cursor for iOS が public beta**（iOS 26.0+、有料全プラン）— クラウド always-on エージェント起動、PC エージェントのリモート操作、音声入力・スラッシュコマンド、モバイルからの通知/PRマージ。Plugin Canvases（共有設定テンプレート）も追加 — https://cursor.com/blog/ios-mobile-app
- DuneSlide RCE 脆弱性（ハイライト参照）。Composer 2.5 実行 75%オフは 7/5 まで

### セキュリティ
- Cursor DuneSlide（CVE-2026-50548/50549、CVSS 9.8）— 3.0+ へ更新（ハイライト参照）
- **Devin Security Swarm 提供開始** — Cognition がエンタープライズ向けに展開。map-reduce 並列エージェントで脆弱性探索 → 隔離サンドボックスで再現・悪用性確認 → 自動パッチ生成 → PR 作成 — https://www.prnewswire.com/news-releases/cognition-launches-devin-security-swarm-to-tackle-the-vulnerability-backlog-302814800.html

### 業界・インフラ投資
- **Crusoe Energy** がデータセンター事業で約 $3B 調達交渉、評価額が昨年10月の約 $10B から約3倍の **$30B** に上昇。契約済み AI インフラ容量 約4.9GW、パイプライン 40GW超
- **Menlo Ventures が自社最大 $3B ファンド**組成（インフラ・フロンティアモデル・AIネイティブアプリ）
- **Anthropic 売上ラン・レート $30B 超で OpenAI 逆転**（ハイライト参照）
- **Linux Foundation** が AI エージェントの認証・統治フレームワーク立ち上げを表明

## 直近の注目予定

- **7/5**: Cursor Composer 2.5 割引（75%オフ）終了
- **7/7**: Fable 5 週次50%上限撤廃 → 従量課金（$10/$50 per M tokens）移行 / Copilot Studio 次ビルド予定
- **7/8**: Anthropic 政府発行ID・生体検証ポリシー施行
- **7/14**: Visio → Power Automate エクスポート廃止（Current Channel は6/30適用済み）
- **7/15**: Claude Science（AI for Science）応募締切
- **7/17**: Claude Corps 第1期応募締切
- **7/21**: Copilot Cowork GA 発表イベント
- **7/31**: Devin classic 環境設定の read-only 参照終了
- **8/1**: covered frontier model 60日 EO 期限
- **8/3**: 旧「Claude in Slack」退役
- **8/5**: Opus 4.1 Claude API 退役
- **8/26**: OpenAI Assistants API 廃止 / o3 退役 / GPT-4.5 完全廃止
- **8/31**: Sonnet 5 促進価格終了（$2/$10 → $3/$15）
- **9月**: iOS 27 / macOS 27 GA（AFM 3 本番） / Gemini 3.5 Pro GA（有力）

## 改善メモ

- **03_ai-news-industry のダイジェスト原文に個別出典URLが含まれていない**（Crusoe / Menlo Ventures / Anthropic 売上等）。統合時の出典追跡性が低いため、当該ソース側で 出典URL を各項目に付与する運用改善を提案。
- 02 の指摘: **7/3 ダイジェストが Claude Code / GitHub Copilot を「no new releases」と誤記録**していた（実際は 7/2 に両者更新あり）。当日は 01・02 で補正済み。
- 02 の障害メモ: TechCommunity 板 RSS（Copilot Studio Blog / M365 Copilot Blog）と devblogs.microsoft.com RSS が 7/2 復旧後も **断続的に 403（7/4）**。WebSearch フォールバックで当日新規なしを確認済み。
- ソース間の重複（Claude Code v2.1.200、Fable 5、GPT-5.6、Gemini 3.5 Pro）は情報量の多い記述をベースに統合。矛盾は検出されず。
