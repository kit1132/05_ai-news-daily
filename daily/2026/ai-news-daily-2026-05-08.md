# AI News Daily - 2026-05-08

## 今日のハイライト

### 1. Anthropic × SpaceX Colossus 1 契約 — 300MW・22万GPU確保とレート上限倍増の一体発表

- **事実**: AnthropicがSpaceXのColossus 1データセンタの全コンピュート容量（300MW超・220,000+ NVIDIA GPU）を確保。同時にClaude Code の5時間レート上限を全有料プランで2倍に引き上げ、Pro/Maxではピーク時間スロットルを完全撤廃。API側もTier 1で入力トークン/分+1500%、出力トークン/分+900%と大幅増。
- **根拠**: 従来のAnthropicの弱点は「モデル性能は高いが利用上限がきつい」だった。SpaceX契約でコンピュート基盤を一気に拡張し、その余力を即座にレート上限引き上げへ変換した。Elon Muskが過去にAnthropicを批判していた経緯を商業合理性が上回った点も、AI業界の計算資源争奪の熾烈さを示す。
- **影響**: Claude Codeのヘビーユーザーは5時間あたりの作業量が倍増するが、週次上限は据え置きのため週の前半で使い切るリスクがある。API開発者はTier 1で十分な処理量が得られるケースが増え、上位ティア課金の必要性を再評価できる。
- **行動指針**: Claude Code利用者は週次上限を意識した配分計画を立てる。API開発者はTier 1の新上限で自社ワークロードが収まるか検証し、不要な上位ティア課金があれば見直す。
- https://www.anthropic.com/news/higher-limits-spacex
- https://www.cnbc.com/2026/05/06/anthropic-spacex-data-center-capacity.html

### 2. Claude Managed Agents に Dreaming・Outcomes・Multi-Agent Orchestration — エージェントが「自己改善ループ」を持つ段階へ

- **事実**: Code with Claude SF（5/6）で3機能を発表。Dreaming（リサーチプレビュー）は過去セッションをスケジュール走査してパターン抽出・メモリ最適化。Outcomes（公開ベータ）は成功基準をルーブリックで記述し別コンテキストのgraderが独立評価。Multi-Agent Orchestration（公開ベータ）はリードエージェントが最大20エージェント・同時25スレッドにタスクを分配。
- **根拠**: Dreamingは単一セッションでは見えない長期的な改善パターンを抽出する仕組みで、エージェントが「使えば使うほど賢くなる」フライホイールを形成する。Outcomesはエージェント自身の推論バイアスからgraderを分離する設計で、自己評価の甘さという根本課題に対処している。
- **影響**: エージェントを業務に組み込んでいるチームにとって、Dreamingは「暗黙知の蓄積」を自動化する。Outcomesは品質保証の仕組みをエージェント内に内蔵するため、人間によるレビュー工数を段階的に削減できる可能性がある。
- **行動指針**: Managed Agentsを利用中のチームはOutcomes（公開ベータ）を優先的に試す。成功基準をルーブリック化する作業自体が、エージェントへの指示品質を上げる副次効果がある。Dreamingはリサーチプレビュー段階のため、本番適用は経過観察。
- https://claude.com/blog/new-in-claude-managed-agents
- https://platform.claude.com/docs/en/managed-agents/dreams

### 3. GPT-5.5 InstantがChatGPTの新デフォルトに — ハルシネーション52.5%減・出力30%短縮

- **事実**: OpenAIがGPT-5.3 Instantを置き換えるGPT-5.5 Instantを全ユーザーに順次展開。高リスク領域（医療・法律・金融）でハルシネーション52.5%減、事実誤認会話37.3%減。出力は語数・行数ともに約30%削減。API価格は$5/M入力・$30/M出力。
- **根拠**: ハルシネーション削減率の公表は、OpenAIが「精度」を差別化軸として明確に打ち出した転換点。出力の30%短縮はトークン消費削減に直結するため、API利用者にはコスト面でもメリットがある。GPT-5.3 Instantは3ヶ月後に廃止予定。
- **影響**: ChatGPT無料ユーザーも恩恵を受ける。API利用者はGPT-5.3からの移行を3ヶ月以内に完了する必要がある。出力長の短縮は、長文生成を前提としたプロンプト設計の見直しが必要になる場合がある。
- **行動指針**: API利用者はGPT-5.5 Instantの出力傾向を早期にテストし、既存プロンプトとの互換性を確認する。GPT-5.3依存のワークフローがあれば移行計画を立てる。3ヶ月の猶予があるため急ぐ必要はないが、着手は早い方がよい。
- https://openai.com/index/gpt-5-5-instant/
- https://techcrunch.com/2026/05/05/openai-releases-gpt-5-5-instant-a-new-default-model-for-chatgpt/

---

## カテゴリ別まとめ

### Anthropic / Claude

- Anthropic × SpaceX Colossus 1 コンピュート契約（ハイライト参照）
- Claude Code / API レート上限倍増（ハイライト参照）
- Claude Managed Agents: Dreaming / Outcomes / Multi-Agent Orchestration（ハイライト参照）
- **Claude Code v2.1.132**: `CLAUDE_CODE_SESSION_ID`環境変数追加、MCP サーバーのメモリリーク修正（10GB+ RSS問題）、JetBrains/Cursor/VS Codeスクロール修正など多数のバグフィックス
  - https://code.claude.com/docs/en/changelog
- **Anthropicがコンシューマ向けに方針シフト**（Bloomberg報道）: 健康・旅行・レシピなど個人向けクエリへの最適化を開始。ChatGPTのコンシューマ優位を切り崩す動き
  - https://www.bloomberg.com/news/articles/2026-05-07/anthropic-is-making-claude-chatbot-more-appealing-to-consumers
- **Jack Clark（共同創設者）**: 2028年末までにAIが自律的に後継モデルを構築する確率60%超と発言。SWE-Bench成功率が2023年2%→2026年93.9%
  - https://www.axios.com/2026/05/07/anthropic-jack-clark-ai-intelligence-explosion

### OpenAI / ChatGPT

- GPT-5.5 Instant（ハイライト参照）
- **Realtime API Beta廃止**（5/7実施）: `gpt-realtime`系へ移行未済の本番環境は要点検。DALL-E-3スナップショットは5/12廃止予定
  - https://developers.openai.com/api/docs/deprecations
- **ChatGPT Futures: Class of 2026**: 高校生・大学生・若手研究者に$10,000助成金+フロンティアモデルアクセスを提供
  - https://openai.com/index/introducing-chatgpt-futures-class-of-2026/

### Google

- **Gemini in Google Docs にCustom Instructions展開中**: ドキュメントごとに恒常ルール（トーン・フォーマット等）を設定可能。最大1,000件、管理者制御なし（個人設定）
  - https://workspaceupdates.googleblog.com/2026/05/set-custom-instructions-for-gemini-in-Google-Docs.html
- **Workspace Intelligence / AI Control Center**: 5/6からRapid Releaseへ正式展開。生成AI・エージェントアクセスのガバナンスを集約
  - https://workspaceupdates.googleblog.com/

### 開発ツール

- **GitHub Copilot CLI — Rubber Duck（クロスモデル批評エージェント）**: メインエージェントの計画・実装を異なるモデルファミリーのcriticがレビュー。Claude Sonnet 4.6 + GPT-5.4でSWE-bench解決率がSonnet-Opus差の74.7%を埋めた
  - https://github.blog/ai-and-ml/github-copilot/github-copilot-cli-combines-model-families-for-a-second-opinion/
- **Cursor v3.3**: エージェントのコンテキスト使用量内訳表示（ルール・スキル・MCP・サブエージェント別）
  - https://cursor.com/changelog
- **Devin v3 API正式リリース**: ロールベースアクセス制御、Devin Manages Devins（委任・管理）、インラインファイルプレビュー
  - https://docs.devin.ai/release-notes/overview
- **GitHub Secret Scanning in MCP がGA**: MCP対応AIコーディングエージェントでコミット前にシークレット漏洩を検出
  - https://github.blog/changelog/label/copilot/

### Microsoft 365 / Copilot

- **Copilot Studio**: Agent Evaluations GA、Content Moderation Settings GA、Prompt ToolにClaude Opus 4.6/Sonnet 4.5追加
  - https://learn.microsoft.com/en-us/microsoft-copilot-studio/whats-new
- **M365 Roadmap**: Legal Agent in Word（契約書レビュー特化）、Work IQ API（A2A/MCP/REST）、Agent 365 Registry Sync
  - https://www.microsoft.com/en-us/microsoft-365/roadmap
- **Copilot Notebooks**: OneNote iOS で音声・画像・テキストを同時キャプチャしCopilot Pageに変換
  - https://learn.microsoft.com/en-us/microsoft-365/copilot/release-notes
- **Request for Information アクション**: エージェントフロー中に人間の入力を要求し、応答まで一時停止するHuman-in-the-Loop機能
  - https://learn.microsoft.com/en-us/power-platform/release-plan/2026wave1/microsoft-copilot-studio/planned-features

### AI投資・企業動向

- **DeepSeek、初の資金調達で評価額$45B**: 中国国家半導体ファンド主導、Tencent・Alibabaも参加協議。$3-4B調達想定。数週間で評価額が$20B→$45Bに倍増
  - https://techcrunch.com/2026/05/06/deepseek-could-hit-45b-valuation-from-its-first-investment-round/
- **DeepL、従業員25%（約250名）を削減**: AI-native組織への再編。同時にリアルタイム音声翻訳強化（Mixhaloチーム買収）
  - https://sifted.eu/articles/deepl-cuts-250-jobs

### セキュリティ

- **MCPのSTDIOトランスポートに設計レベルの脆弱性**: 20万台以上のサーバーが影響（CVE-2026-30623）。設定ファイルからの任意OSコマンド実行が可能。Anthropicは「想定された動作」として修正を拒否
  - https://venturebeat.com/security/mcp-stdio-flaw-200000-ai-agent-servers-exposed-ox-security-audit
- **Cursor 2.5+ RCE脆弱性パッチ**: 悪意あるGitリポジトリ経由のRCE。未アップデートのチームは要確認
  - https://cursor.com/changelog

### インフラ

- **Cloudflare「Infire」推論エンジン公開**: Rust製、Kimi K2.5で従来比3倍高速化。「Unweight」技術でモデル重みを15-22%圧縮（精度劣化なし）
  - https://blog.cloudflare.com/cloudflares-most-efficient-ai-inference-engine/

### 地政学・規制

- **米中AI公式対話を検討**: 5/14-15の北京首脳会談で議題に。自律兵器・オープンソース技術悪用が論点。大きなブレイクスルーの見込みは低い
  - https://www.benzinga.com/markets/tech/26/05/52361259/trump-administration-eyes-first-official-ai-dialogue-with-china-at-beijing-summit-with-xi-jinping-report

### 市場データ

- **SimilarwebAIトラッカー**: ChatGPTトラフィックシェア64.5%（1年前86.7%）、Gemini 21.5%（1年前5.7%で約4倍）、Grokが3%超でDeepSeekに接近
  - https://x.com/Similarweb/status/2008805674893939041

### GitHub Trending（5月第1週）

- Karpathy/skills (106.8K★) — Claude Code用CLAUDE.mdファイル集
- mattpocock/skills (55.3K★) — 実務エンジニア向けClaude Code Skills
- Warp (52.9K★) — ターミナル発エージェント型開発環境
- NousResearch/Hermes-agent (130K★) — 成長型AIエージェント

---

## 直近の注目予定

- **5/11**: Power Platform バックアップ保持期間変更（28日→7日）
- **5/12**: DALL-E-3 スナップショット廃止
- **5/14-15**: 米中北京首脳会談（AI対話の可能性）
- **5/15**: Copilot Studio SharePoint リスト知識ソース Public Preview
- **5/19**: Code with Claude London
- **5/30**: Claude Sonnet 4.5 Copilot Studio 退役（自動移行）
- **6/1**: GitHub Copilot 利用量ベース課金切替
- **6/10**: Code with Claude Tokyo

---

## 改善メモ

- [Master] Anthropic Blog/News が WebFetch で7週連続403。CDN/API経由の代替アクセス（`claude.com/blog/<slug>`のAMP版やRSS復旧確認用URL）を`daily-sources.md`に追記する価値あり
- [Master] Code with Claude SF の発表が数日かけて段階的に公式化。次回London/Tokyoはキーノート当日+翌日+翌々日の3日間ウォッチを定型化推奨
- [Copilot] Copilot Studio What's New・M365 Copilot Release Notes・mc.merill.net 等が WebFetch 403継続。WebSearchで代替
- [Industry] 全RSSフィード（Google News RSS、GIGAZINE、The Decoder、VentureBeat等）が403継続。WebSearchフォールバックで対応
- [Industry] 前回チェック（5/4）から4日空いたため5/5-5/8を一括収録。GPT-5.5 Instant（5/5）等は日付を明記
