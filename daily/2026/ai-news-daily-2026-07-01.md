# AI News Daily Summary — 2026-07-01

> 本サマリーは 01_ai-news-Master・02_ai-news-Copilot・03_ai-news-industry の3ソース（7/1分）を統合して作成。

## 今日のハイライト

### 1. Claude Sonnet 5 GA（6/30）— 安価なエージェント実行手段として投入

**事実** Anthropic が Claude Sonnet 5 を一般提供開始。Free/Pro のデフォルトモデルに昇格し、Max/Team/Enterprise でも利用可能。Claude Code も v2.1.197（6/30）でデフォルトを Sonnet 5（ネイティブ1Mコンテキスト）に切り替えた（利用には更新が必要）。

**根拠** 導入価格は $2/$10 per 1M（8/31まで、以後 $3/$15）で、Opus 4.8 想定 $10/$50 に対し大幅ディスカウント。agentic coding ベンチは 63.2%（Opus 4.8 69.2% / Sonnet 4.6 58.1%）。安全性評価も Sonnet 4.6 比で望ましくない挙動が低下。新トークナイザ採用により同一入力でもトークン数が約1.0〜1.35倍になる場合あり。

**影響** Fable 5/Mythos 5 が輸出規制で停止する中、可用な主力モデルとして既定を引き上げた形。ブラウザ・ターミナル等のツール使用と自律実行を低コストで回せる。VentureBeat/TechCrunch は「エージェントを安く回す手段」「IPO 前の競争激化」と位置づけ。

**行動指針** Claude Code 利用者は v2.1.197 へ更新。コスト試算は新トークナイザ（最大1.35倍）を織り込み、8/31 の価格改定（$3/$15）も予算に反映する。

- https://www.anthropic.com/news/claude-sonnet-5
- https://venturebeat.com/technology/anthropic-launches-claude-sonnet-5-at-a-steep-discount-to-its-top-model-as-the-company-races-toward-a-blockbuster-ipo
- https://techcrunch.com/2026/06/30/anthropic-launches-claude-sonnet-5-as-a-cheaper-way-to-run-agents/

### 2. Fable 5 / Mythos 5 世界停止が継続 — Fable 5 復旧は Pentagon/NSA 署名待ち

**事実** 7/1 時点で Fable 5 は一般利用者（消費者/API/Claude Code/海外サブスク）向けに停止継続。Mythos 5 は米重要インフラ・防衛を担う一部組織（Annex A）限定で再展開済み。

**根拠** 6/9 公開 → 6/12 BIS 指令で全世界停止（発端は他社による Mythos jailbreak 主張）→ 6/26 Lutnick 書面で Mythos 限定復旧、という経緯。予測市場（Kalshi）は7月中の Fable 5 復旧を約57%と見込むが、Pentagon・NSA の最終署名が未了で不透明。Axios の「今週中」観測も週末を経て全面復旧の発表なし。

**影響** 復旧条件（無制限か本人確認付きか）は未公表。Fable 5 復旧時に ID 検証が必要となる可能性を Claude アプリ文字列が示唆。次の節目は 7/8 の政府発行ID・生体情報検証ポリシー施行。

**行動指針** Fable 5 依存のワークフローは引き続き代替（Sonnet 5 等）で運用。7/8 ポリシー施行と本人確認要件の発表を注視する。

- https://news.kalshi.com/p/fable-5-odds-anthropic-access-restored-july-57-percent
- https://www.anthropic.com/news/fable-mythos-access
- https://www.axios.com/2026/06/27/anthropic-fable-5-return-soon

### 3. Microsoft 365 商用価格改定が本日 7/1 発効 — 恒久バンドル新設

**事実** M365 Copilot for Business（スタンドアロン）が $18→$21 に値上げ。プロモは 6/30 で終了。あわせて新・恒久バンドル「Microsoft 365 Business Standard with Copilot $23.50」「Business Premium with Copilot $32」を設定。

**根拠** Enterprise/Business/Frontline 横断の値上げで、6/30 が現行レートのロックイン期限（経過済み）。Teams・Copilot のスタンドアロン SKU は対象外。

**影響** Copilot を含む M365 商用契約のコスト構造が本日から変化。バンドル恒久化により単体 Copilot 追加とバンドル移行のコスト比較が必要になる。

**行動指針** 契約更新を控える組織はバンドル（Standard/Premium with Copilot）と単体加算の総額を比較。スタンドアロン Copilot 利用は $21 の新レートを前提に再見積もり。

- https://www.uscloud.com/blog/microsoft-365-price-increase-july-1-2026-what-enterprise-buyers-need-to-know-part-1/
- https://www.microsoft.com/en-us/microsoft-365-copilot/pricing

## カテゴリ別まとめ

### Anthropic / Claude
- Claude Sonnet 5 GA・Claude Code 既定モデル化（ハイライト参照）
- Fable 5 / Mythos 5 輸出規制停止の継続（ハイライト参照）
- Claude Code v2.1.196（6/29）: 組織既定モデル設定（管理コンソール「Org default」「Role default」）、可読なデフォルトセッション名、チャット内ファイル添付のクリック展開。セキュリティ修正として `claude mcp list`/`get` が自己承認 MCP サーバを起動しないよう変更。`/code-review` のトークン使用25%削減、stream watchdog（5分無応答で中断・再試行）を全プロバイダーで既定ON https://code.claude.com/docs/en/changelog

### OpenAI
- Codex CLI 0.142.4（6/29）は保守リリース（変更なし）、0.143.0-alpha.31 開発中。実質最新機能は 0.142.2（6/25、MCP ツール検索既定化） https://github.com/openai/codex/releases
- GPT-5.6 Sol 限定プレビュー継続（約20組織）。7月に Cerebras 上で最大 750 tokens/sec 提供開始、一般提供は「7月第2週」目標。Terminal-Bench 2.1 で新 SOTA 主張、Sol Ultra が規制ベンチで High 分類超え https://openai.com/index/previewing-gpt-5-6-sol/

### Google / DeepMind
- Gemini 3.5 Pro は7月延期が確定的な流れ。「6月内公開」予測期限を通過し、依然 Vertex AI 限定 Enterprise preview のみ。トークン効率の問題対応と Gemini 3.5 Flash の知見反映が延期理由。2M context / Deep Think。政府規制をクリアした「制約なく出荷可能」な位置付けは維持 https://cryptobriefing.com/google-delays-gemini-35-pro-launch-to-july-2026/

### Microsoft / GitHub
- M365 商用価格改定が本日発効（ハイライト参照）
- GitHub Copilot CLI 安定版 v1.0.66（6/30）: Claude Opus 4.8 Fast モデル追加、非点滅ブロックカーソル、MCP HTTP ヘッダ対応、PR 自動化改善、タイムラインの compact highlight reel 化、macOS デスクトップ通知 https://github.com/github/copilot-cli/releases
- GitHub Desktop 3.6（6/26）: Copilot がコミットメッセージ生成（`copilot-instructions.md`/`AGENTS.md` 反映）とマージコンフリクトの AI 解消を担当、Git worktree 対応、モデルピッカー＋BYOK。GitHub Copilot for Jira が GA https://github.blog/changelog/2026-06-26-github-desktop-3-6-worktrees-and-deeper-copilot-integration/

### Copilot Studio / Power Platform（動きなし）
- Copilot Studio 新ビルドなし（最新 2026.6.2、6/22）。UK/Asia/Japan/Europe が 2026.6.1 へ地域展開
- Power Platform Blog は 6/11「June 2026 Feature Update」以降の新着なし https://learn.microsoft.com/en-us/power-platform/released-versions/copilotstudio

### Cursor / 開発ツール
- Cursor 新規なし。Cursor for iOS 公開ベータ（6/29、全有料プラン、always-on エージェント起動）が直近
- Devin Cascade（Windsurf 旧ローカルエージェント）が本日 7/1 EOL。CI/自動化が明示的に Cascade を呼ぶ箇所は Devin Local（Rust 再実装、6/2 より既定、並列サブセッション・ACP ネイティブ対応）へ要再設定 https://docs.devin.ai/release-notes/overview

### 市場・IPO
- STARTRADER が Anthropic と OpenAI のプレ IPO CFD 取引を開始（6/29）。未上場 AI 企業への投機需要が個人向け商品として表面化

## 直近の注目予定

- **7/1**: M365 商用価格改定発効（経過）/ Devin Cascade EOL（経過）
- **7月第2週**: GPT-5.6 一般提供目標
- **7月**: Fable 5 US 復旧（Pentagon/NSA 署名待ち）/ GPT-5.6 Cerebras 提供開始 / Gemini 3.5 Pro GA
- **7/8**: Anthropic 政府発行ID・生体情報検証ポリシー施行
- **7/17**: Claude Corps 第1期応募締切
- **8/1**: covered frontier model フレームワーク 60日 EO 期限
- **8/3**: 旧「Claude in Slack」アプリ退役
- **8/5**: Opus 4.1 Claude API 退役
- **8/26**: OpenAI Assistants API 廃止 / o3 退役 / GPT-4.5 完全廃止
- **8/31**: Sonnet 5 促進価格終了（→ $3/$15）
- **9月**: iOS 27 / macOS 27 GA（AFM 3 本番）

## 改善メモ

- Fable 5 停止の経過日数がソース間で不一致（01: 20日目 / 02: ~Day 22 / 03: 17日経過）。6/12 停止起点なら 7/1 は19〜20日目に相当。日数表記は起点（6/12 BIS 指令 vs 6/9 公開）の取り方で差が出るため、今後は「6/12 起点」に統一して表記することを推奨
- 継続提案 3件（B-005 Qiita / B-006 Zenn / B-007 M365 Dev Blog の RSS→WebSearch 降格、02 ソース）。各ソースの新規提案・障害変化は本日なし
