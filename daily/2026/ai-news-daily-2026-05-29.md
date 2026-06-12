# AI News Daily Summary — 2026-05-29（木）

> 対象ダイジェスト: 3ソース（Master / Copilot / Industry）の `ai-news-2026-05-29.md`
> ※当日（5/30）の digest が未生成のため、5/29 分を使用

---

## 今日のハイライト

### 1. Claude Opus 4.8 リリース — コーディング・エージェント性能で単独首位を確立

**事実**: Anthropic が 5/28 に Claude Opus 4.8 をリリース。同日 Claude Code v2.1.154/153 も連動リリースされ、Dynamic Workflows（数百エージェントの並列オーケストレーション）、`/effort xhigh` デフォルト化、Lean system prompt デフォルト化などが追加された。

**根拠**: SWE-Bench Pro 69.2%（Opus 4.7 64.3%、GPT-5.5 58.6%で +10.6pt リード）、OSWorld-Verified 83.4%（GPT-5.5 78.7%）、USAMO 2026 96.7%（Opus 4.7 69.3% から +27.4pt）。Super-Agent ベンチで全ケースを end-to-end 完走したのは Opus 4.8 のみ。価格は据置（$5/$25 per M tokens）で、Fast Mode は 3 倍値下げ（$10/$50）。Claude Code v2.1.154 では auto-mode 分類器のデータ持出検知強化、カスタム API ゲートウェイのトークン漏洩バグ修正など、セキュリティ面も大幅に改善。

**影響**: コーディング・コンピュータ操作・数学推論の 3 領域で GPT-5.5 に対して明確な差をつけた。Claude Code ユーザーにとっては、Fast Mode 値下げにより実効コストが大幅に下がる。Dynamic Workflows は「数百ファイル規模のリファクタリングや移行」を並列処理できるため、大規模コードベースでの作業効率が質的に変わる。一方、Mythos クラスは「数週間以内に一般展開予定」と発表されており、Opus 4.8 はその前段の位置づけ。

**行動指針**: Claude Code ユーザーは v2.1.154 へ即時アップデートし、`/workflows` と `/effort xhigh` を試す。API 利用者は Fast Mode（$10/$50）でのバッチ処理コスト削減を検討する。`CLAUDE_CODE_OPUS_4_6_FAST_MODE_OVERRIDE` は 6/1 に廃止されるため、利用中なら移行が必要。

ソース: [Anthropic](https://www.anthropic.com/news/claude-opus-4-8) / [TechCrunch](https://techcrunch.com/2026/05/28/anthropic-releases-opus-4-8-with-new-dynamic-workflow-tool/) / [VentureBeat](https://venturebeat.com/technology/anthropics-claude-opus-4-8-is-here-with-3x-cheaper-fast-mode-and-near-mythos-level-alignment) / [Claude Code Changelog](https://code.claude.com/docs/en/changelog)

---

### 2. AIコーディング市場に資金集中 — Anthropic $9,000億・Cognition $260億の評価額が示す構造

**事実**: Anthropic が $300 億の調達を完了し、評価額 $9,000 億超（プレマネー）で OpenAI の $8,520 億を初めて逆転した。同時期に Cognition（Devin）も Series D で $10 億を調達し、評価額 $260 億に到達（8 ヶ月前の $102 億から 2.5 倍）。Ramp AI Index 4 月データでは、エンタープライズ AI 採用率で Anthropic 34.4% が OpenAI 32.3% を上回った。

**根拠**: Anthropic の Q2 売上は $109 億で Q1 の $48 億から倍増し、2025 年通年売上を 1 四半期で超過。Claude Code が同社史上最速成長プロダクト。Cognition は ARR $4.92 億、企業利用が年初から 10 倍成長で Mercedes-Benz・NASA・Goldman Sachs が顧客。両社とも「AIコーディングエージェント」が成長ドライバーであり、市場の資金がこの領域に集中していることを示す。

**影響**: Anthropic が評価額で OpenAI を逆転したことは象徴的だが、ユーザーの判断基準は変わらない。重要なのは、コーディングエージェント市場が急拡大しており、Claude Code・Devin・Cursor・Copilot CLI の選択肢が増え続けていること。各ツールの実効性能とエコシステム連携が選択の決め手になる。

**行動指針**: 経過観察。ツール選択は評価額ではなく自分のワークフローとの適合度で判断する。VentureBeat が指摘する「3 つの脅威（インフラコスト・規制・オープンソース競合）」も念頭に、特定ベンダーへの依存度を意識しておく。

ソース: [Bloomberg](https://www.bloomberg.com/news/articles/2026-05-22/anthropic-to-close-over-30-billion-round-as-soon-as-next-week) / [TechCrunch](https://techcrunch.com/2026/05/27/ai-coding-startup-cognition-raises-1b-at-25b-pre-money-valuation/) / [VentureBeat](https://venturebeat.com/technology/anthropic-finally-beat-openai-in-business-ai-adoption-but-3-big-threats-could-erase-its-lead)

---

## カテゴリ別まとめ

### Anthropic / Claude

- **Claude Opus 4.8 リリース（5/28）**: SWE-Bench Pro 69.2%、OSWorld-Verified 83.4%、USAMO 96.7%。価格据置、Fast Mode 3 倍値下げ。Dynamic Workflows・Effort コントロールパネル同時導入 — [Anthropic](https://www.anthropic.com/news/claude-opus-4-8) / [TechCrunch](https://techcrunch.com/2026/05/28/anthropic-releases-opus-4-8-with-new-dynamic-workflow-tool/)
- **Mythos クラス「数週間以内」に一般展開予定**: Opus 4.8 で先行投入したセーフガードを Mythos 用に磨き込み中 — [The Register](https://www.theregister.com/security/2026/05/25/anthropic-to-release-mythos-class-models-to-the-public/5245596)
- **$300 億調達完了、評価額 $9,000 億超**: OpenAI の $8,520 億を初めて逆転。Q2 売上 $109 億 — [Bloomberg](https://www.bloomberg.com/news/articles/2026-05-22/anthropic-to-close-over-30-billion-round-as-soon-as-next-week)
- **エンタープライズ採用率で OpenAI 逆転**: Ramp AI Index 4 月、Anthropic 34.4% vs OpenAI 32.3% — [VentureBeat](https://venturebeat.com/technology/anthropic-finally-beat-openai-in-business-ai-adoption-but-3-big-threats-could-erase-its-lead)

### Claude Code

- **v2.1.154（5/28）**: Opus 4.8 で `/effort xhigh` デフォルト、Dynamic Workflows（`/workflows`）、Lean system prompt デフォルト化、Fast Mode 値下げ、auto-mode データ持出検知強化、`HOME` 末尾スラッシュ脆弱性修正 — [Changelog](https://code.claude.com/docs/en/changelog)
- **v2.1.153（5/28）**: `skipLfs` で LFS スキップ、`claude agents` でスラッシュコマンド autocomplete、`claude doctor` に直近 update 結果表示、カスタム API ゲートウェイのトークン送信リグレッション修正 — [Changelog](https://code.claude.com/docs/en/changelog)
- **廃止予告**: `CLAUDE_CODE_OPUS_4_6_FAST_MODE_OVERRIDE`（6/1 削除予定）

### Microsoft / Copilot

- **Copilot Studio に Mistral Medium 3.5 追加（5/28, パブリックプレビュー）**: EU 組織向けリージョン内データ処理対応。二段階オプトインで利用開始 — [Microsoft Blog](https://www.microsoft.com/en-us/microsoft-copilot/blog/copilot-studio/mistral-joins-copilot-studios-growing-lineup-of-model-providers/)
- **Copilot Studio に GPT-5.5 Reasoning (Deep) プレビュー追加**: 深い分析的推論向け実験モデル — [Microsoft Learn](https://learn.microsoft.com/en-us/microsoft-copilot-studio/whats-new)
- **Copilot Studio Question Themes Analysis GA（5/29）**: ユーザー質問をテーマ別グループ化、応答品質・回答率を可視化 — [Microsoft Learn](https://learn.microsoft.com/en-us/microsoft-copilot-studio/analytics-themes)
- **M365 Copilot Notebooks 5 月更新（5/26）**: 会議トランスクリプト・メール・Web 調査をコンテキスト取り込み。OneNote iPhone で音声→構造化ページ変換 — [Tech Community](https://techcommunity.microsoft.com/blog/microsoft365copilotblog/what%E2%80%99s-new-in-notebooks--may-2026/4519838)
- **Computer-Using Agents GA（5/13）**: OpenAI CUA + Claude Sonnet 4.5 搭載、A2A 通信も GA — [Tech Community](https://techcommunity.microsoft.com/blog/copilot-studio-blog/computer-using-agents-in-microsoft-copilot-studio-are-now-generally-available/4519427)

### GitHub Copilot

- **組織ごとのモデルルール（5/26, パブリックプレビュー）**: Enterprise 向けに組織単位でモデル可用性を制御 — [GitHub Blog](https://github.blog/changelog/2026-05-26-target-copilot-models-to-organizations-with-model-rules/)
- **Individual プラン: 新規サインアップ一時停止**: Opus モデルは Pro+ 限定に。利用制限を VS Code / CLI に表示 — [GitHub Blog](https://github.blog/news-insights/company-news/changes-to-github-copilot-individual-plans/)
- **Copilot CLI v1.0.55-6/-7（5/27）**: `/autopilot` コマンド追加、ネイティブバイナリのクラッシュハンドリング修正 — [GitHub Releases](https://github.com/github/copilot-cli/releases)

### OpenAI

- **Codex で自己改善する税務エージェント（5/27）**: Thrive Holdings 共同開発。7,000 件処理・最大 97% 精度・調製時間 1/3 削減 — [OpenAI](https://openai.com/index/building-self-improving-tax-agents-with-codex/)
- **Deployment Company 設立**: $40 億超の資本で TPG 主導、AI コンサルティング Tomoro 買収（約 150 名即戦力） — [OpenAI](https://openai.com/index/openai-launches-the-deployment-company/)
- **Microsoft-OpenAI 非独占契約へ移行（4/27）**: Azure 独占解除、AGI 条項撤廃、収益シェア構造変更 — [OpenAI](https://openai.com/index/next-phase-of-microsoft-partnership/)

### Google / Gemini

- **Workspace 3 件 5/28 Rapid Release**: Meet の Ask Gemini 位置変更、Gemini 会話スナップショット共有、Connected Sheets 異常検知 — [Workspace Updates](https://workspaceupdates.googleblog.com/2026/)
- **Gemini 3.5 Flash GA（5/19）**: Intelligence Index 55、Claude Opus 4.7 の 1/3 価格。3.5 Pro は 6 月予定 — [The Decoder](https://the-decoder.com/anthropics-900-billion-valuation-would-make-it-more-valuable-than-openai-for-the-first-time/)
- **Managed Agent API（5/21）**: API 一発で Linux 環境付きエージェント起動 — [Publickey](https://www.publickey1.jp/blog/26/apigooglelinuxaimarkdownmanaged_agent_api.html)

### Cursor / Devin

- **Cognition（Devin）Series D: $10 億調達、$260 億評価額（5/27）**: ARR $4.92 億、企業利用年初比 10 倍。Mercedes-Benz・NASA 等が顧客 — [TechCrunch](https://techcrunch.com/2026/05/27/ai-coding-startup-cognition-raises-1b-at-25b-pre-money-valuation/)
- **Devin v3 API 正式化**: RBAC・セッションアトリビューション対応。マージコンフリクト自動検出追加 — [Devin Docs](https://docs.devin.ai/release-notes/2026)
- **Cursor Composer 2.5（5/18）**: Kimi K2.5 ベース、SWE-Bench Multilingual で Opus 4.7 同等・コスト約 1/10 — [Cursor Blog](https://cursor.com/blog/composer-2-5)

### 地政学・規制

- **中国、DeepSeek 等の AI 人材に海外渡航制限（5/26）**: 民間 AI 企業の創業者・研究者・幹部に政府承認を義務付け。AI 人材を「国家安全保障資産」として扱う方針 — [Bloomberg](https://www.bloomberg.com/news/articles/2026-05-26/china-expands-travel-curbs-to-top-ai-talent-at-private-firms)

### 市場データ

- **Similarweb AI Tracker**: ChatGPT 56.72%（1 年前 86.7%）、Gemini 25.46%（同 5.7%）、Claude 6.02%。Gemini が 1 年で 4.5 倍成長 — [Similarweb](https://www.similarweb.com/blog/marketing/geo/gen-ai-stats/)
- **Apple iOS 27 でサードパーティ AI 選択導入へ**: Gemini・Claude をテスト中、WWDC 2026 でプレビュー予定 — [Business Standard](https://www.business-standard.com/amp/technology/tech-news/apple-intelligence-ios-27-open-siri-ai-features-third-party-models-126050600980_1.html)

---

## 直近の注目予定

- **2026-05-31**: Copilot Studio CLI GA
- **2026-06-01**: GitHub Copilot 従量課金開始、GPT-4.1 廃止、`CLAUDE_CODE_OPUS_4_6_FAST_MODE_OVERRIDE` 削除
- **2026-06-15**: Anthropic Agent SDK / claude -p 別枠クレジット移行
- **2026-06 中**: Gemini 3.5 Pro 提供開始予定
- **2026-06-30**: Microsoft 社内 Claude Code 利用終了期限
- **数週間以内**: Anthropic Mythos クラス一般展開

---

## 改善メモ

- Industry ソース（03）は前回チェック（5/22）から 7 日分をまとめて取得しているため、4/27〜5/26 の既報ニュースが含まれる。本日分のサマリーでは日付を明記して新旧を区別した
- 当日（5/30）の digest が未生成のため、5/29 分の 3 ソースを使用
- WebFetch 403 継続中ソース: Anthropic・OpenAI・Cursor・Devin・mc.merill.net・Tech Community。全ソース WebSearch プライマリ運用で対応済み
- Claude Code Changelog の WebFetch は安定して機能。GitHub Copilot CLI releases ページも同様
