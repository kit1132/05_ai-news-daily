# AI News Daily Summary — 2026-06-04

> 本サマリーは 01_ai-news-Master・02_ai-news-Copilot・03_ai-news-industry の3ソース（6/4分）を統合して作成。6/5のスケジュール実行時に6/4分として生成。

## 今日のハイライト

### 1. GitHub Copilot、6/1からトークン課金に完全移行 — Pro+ユーザーが2日で枯渇報告

**事実**: GitHub Copilotの全プランがAI Credits制（1 Credit = $0.01）に移行した。月額料金にCreditsが含まれ、超過分は追加課金。コード補完・Next Edit Suggestionsは引き続き無制限だが、Chat・Agent機能はCredit消費対象。Pro+（$39/月）ユーザーが2時間で月間クレジットの8%を消費し、2日以内に枯渇する見込みとの報告が出ている。GitHub Discussionに400超のコメントと900超のdownvoteが集中。

**根拠**: Claude 4.8使用で1セッション1,180クレジット（月間の16%）消費という具体的な数字が報告されている。フロンティアモデルのトークン単価が高いため、Agent的な使い方（複数ファイル横断の編集・リファクタリング）では想定以上に消費が膨らむ構造。同日のUber事例（後述）でもClaude Code・Cursorの月額$500〜$2,000/人が報告されており、「AIコーディングツールのコスト予測不能性」が業界共通の課題として顕在化した。

**影響**: 月額固定で使い放題だった開発者の体験が根本的に変わる。特にAgent機能のヘビーユーザーは月半ばでCreditsが枯渇し、作業が止まるリスクがある。OpenRouter・RooCode・LM Studio等のオープンソース代替への移行検討が加速しており、GitHub Copilotのロックインが初めて揺らいでいる。

**行動指針**: まず自分のCredit消費ペースを1週間トラッキングし、月間予算内に収まるか検証する。収まらない場合の選択肢は、モデルを低コストに切り替える（Claude 4.8→Sonnet 4.5等）、Agent機能の利用頻度を絞る、または代替ツール（Cursor・Claude Code直接利用）のコスト比較を行う。組織の管理者はユーザーレベル予算設定（GA済）を即座に有効化する。

- https://github.blog/changelog/2026-06-01-updates-to-github-copilot-billing-and-plans/
- https://docs.github.com/en/copilot/reference/copilot-billing/models-and-pricing

### 2. トランプ大統領、AI大統領令に署名 — フロンティアモデルの30日事前政府アクセス

**事実**: 6/2署名。AI企業に対し、フロンティアモデルのリリース30日前に政府へ早期アクセスを提供するよう任意ベースで要請する大統領令。政府機関がサイバーセキュリティ・国家安全保障リスクのベンチマーク評価を実施する枠組みを構築する。当初草案の90日から30日に短縮された。

**根拠**: これまでトランプ政権はBiden時代のAI規制を撤回し規制緩和路線を維持してきたが、今回は「監視強化」方向へのシフト。ただし義務的規制やライセンス制ではなく、あくまで「任意ベース」であり、罰則規定はない。EU AI Actのような法的拘束力のある規制とは性質が異なる。

**影響**: Anthropic・OpenAI・Google等のフロンティアラボは、リリーススケジュールに30日のバッファを組み込む必要が出てくる可能性がある。ただし「任意」のため、実効性は各社の協力姿勢次第。Anthropicは既にProject Glasswing（政府向けClaude Mythosアクセス）を拡大中であり、この枠組みと整合的に動ける立場にある。

**行動指針**: 開発者・事業者への直接的影響は現時点では限定的。ただしフロンティアモデルのリリースタイミングが今後30日程度遅延する可能性があることを念頭に置く。経過観察。

- https://www.whitehouse.gov/presidential-actions/2026/06/promoting-advanced-artificial-intelligence-innovation-and-security/
- https://www.cnbc.com/2026/06/02/trump-executive-order-ai.html

### 3. Uber、AI開発ツール予算を4ヶ月で消化 — 月額$1,500キャップ導入

**事実**: UberがClaude Code・Cursorの社内展開で、エンジニア1人あたり月$500〜$2,000のAPI費用が発生。2026年度のAI予算を4月時点（開始4ヶ月）で使い切った。エンジニアの95%がAIツールを月次利用し、コミットコードの70%がAI起源。対策として月額$1,500/人のキャップを導入。COO Andrew Macdonaldは「ツール投資と消費者向けイノベーションの因果関係はまだ見えない」と発言。

**根拠**: コミットコードの70%がAI起源という数字は、AIコーディングツールが「あると便利」から「インフラ」に移行した証拠。一方でCOO発言が示す通り、コスト増がアウトプット向上に直結しているかは未検証。GitHub Copilotの課金移行（ハイライト1）と合わせると、「AIツール利用量の急増 → コスト予測不能 → 予算超過 → 利用制限」のサイクルがテック大企業レベルで起きている。

**影響**: Uberの事例は他の大企業にとって先行指標になる。AIコーディングツールの予算策定において「席数 × 月額固定費」ではなく「実使用量ベースの変動費」として計画する必要がある。

**行動指針**: 自社でAIコーディングツールの月間コストを人別・チーム別で可視化していない場合は即座に始める。可視化済の場合は「コスト上限設定」と「ROI測定の仕組み（コード品質・速度・バグ率との相関）」を導入する。ツール側の予算管理機能（GitHub Copilotのユーザーレベル予算、Claude Codeの6/15クレジットプール分離）を活用する。

- https://fortune.com/2026/05/26/uber-coo-ai-spending-tokens-claude-code/
- https://www.bloomberg.com/news/articles/2026-06-02/uber-caps-usage-of-ai-tools-like-claude-code-to-cut-costs

---

## カテゴリ別まとめ

### Microsoft Build 2026（続報）

- **Microsoft Scout** — 常時バックグラウンド稼働の「Autopilot」パーソナルエージェント。会議自動スケジュール・準備資料生成・ワークフローリスク検知。Private Preview（[Microsoft Blog](https://www.microsoft.com/en-us/microsoft-365/blog/2026/06/02/introducing-microsoft-scout-your-always-on-personal-agent/)）
- **Work IQ APIs** — M365の数百APIを10個のMCPツールに集約。トークン消費80%削減・処理速度2倍。6/16 GA予定（[Microsoft Blog](https://www.microsoft.com/en-us/microsoft-365/blog/2026/06/02/announcing-the-new-work-iq-apis/)）
- **MXC（Microsoft Execution Containers）** — AIエージェント向けOSレベルサンドボックス。Process Isolation / Session Isolationの2段階。OpenAI・NVIDIA・Manus・GitHub Copilot CLIが採用パートナー（[Windows Developer Blog](https://blogs.windows.com/windowsdeveloper/2026/06/02/windows-platform-security-for-ai-agents/) / [VentureBeat](https://venturebeat.com/security/microsoft-launches-mxc-an-os-level-sandbox-for-ai-agents-with-openai-and-nvidia-already-on-board)）
- **GPT-5.5 Microsoft FoundryでGA** — $5/M入力・$30/M出力。Foundryカタログ11,000+モデル（[Azure Blog](https://azure.microsoft.com/en-us/blog/openais-gpt-5-5-in-microsoft-foundry-frontier-intelligence-on-an-enterprise-ready-platform/)）
- **Frontier Tuning** — Copilot Studio向けファインチューニング機能。Private Preview（[Microsoft Copilot Blog](https://www.microsoft.com/en-us/microsoft-copilot/blog/copilot-studio/frontier-tuning-teaching-ai-to-work-the-way-you-do/)）

### M365 / Copilot Studio

- **M365価格改定（7/1発効）** — Business Standard $12.50→$14.00（+12%）、E3 $36→$39（+8%）、E5 +5%。Copilot Chat強化・Defender for Office P1・Intune Suiteをバンドル追加（[Microsoft Licensing](https://www.microsoft.com/en-us/licensing/news/2026-m365-packaging-pricing-updates)）
- **Copilot Studioエージェント評価テストケース** — expected responseの手動追加・ファイルインポート対応。複数採点方式（[Release Notes](https://learn.microsoft.com/microsoft-365/copilot/release-notes#june-2,-2026)）
- **Copilot Studio for Teams終了予告** — 6月末以降クラシックchatbot作成不可、Webアプリへリダイレクト
- **Planner Agent GA** — M365 Copilot内でタスク・プラン管理。6月中旬〜下旬GA予定
- **Defender XDR AgentsInfoテーブル（Preview）** — エージェント統合スキーマ。旧AIAgentsInfoは7/1廃止

### Anthropic / Claude

- **Anthropic S-1提出（6/1）** — SEC にForm S-1ドラフトを機密提出。評価額$965B、ARR $47B。株数・価格帯・時期は未定（[Anthropic](https://www.anthropic.com/news/confidential-draft-s1-sec)）
- **Claude Partner Network Services Track + Partner Hub（6/3）** — パートナーを3階層化（Select/Preferred/Global Premier）。40,000社応募・10,000名超がCertification取得（[Anthropic](https://www.anthropic.com/news/services-track-partner-hub)）
- **課金分離予告（6/15施行）** — Agent SDK・Claude Code GitHub Actions等を別クレジットプールに移行。Pro $20/月、Max 5x $100/月（[DevToolPicks](https://devtoolpicks.com/blog/anthropic-splits-claude-subscriptions-agent-sdk-credit-june-2026)）
- **Project Glasswing拡大** — Claude Mythos Previewを約150新組織に拡大。15カ国以上の重要インフラ向け（[TechCrunch](https://techcrunch.com/2026/06/02/anthropic-scales-claude-mythos-to-critical-infrastructure-in-15-countries/)）

### Claude Code

- **v2.1.161（6/2 stable）** — OTel `OTEL_RESOURCE_ATTRIBUTES`ラベル化、`claude agents`ファンアウトdone/total表示、並列ツール呼出し独立化、バックグラウンドセッション再接続修正、MCP `/mcp` unused connectors折りたたみ、Windows WSL画像ペースト対応（[Changelog](https://code.claude.com/docs/en/changelog)）

### OpenAI

- **Codex Annotations / Sites / 6業界別プラグイン** — ドキュメントのピンポイント編集、作業内容のWebサイト化、営業・データ分析・投資銀行等向け62アプリ+110スキル。非開発者ユーザーが5M WAUの20%（[9to5Mac](https://9to5mac.com/2026/06/02/openai-putting-codex-inside-chatgpt-app-everywhere-releasing-6-business-plugins/) / [VentureBeat](https://venturebeat.com/orchestration/openais-codex-update-lets-agents-build-interactive-enterprise-workspaces-via-sites-and-role-specific-plugins)）
- **Realtime 2 / Realtime Translate / Realtime Whisper** — 設定可能なreasoningを持つspeech-to-speechモデル、ストリーミング音声翻訳・STT（[OpenAI API Changelog](https://developers.openai.com/api/docs/changelog)）
- **Rosalind Biodefense Initiative** — GPT-Rosalindを活用したパンデミック対策・生物兵器検知プログラム（[OpenAI News](https://openai.com/news/)）
- **Codex CLI v0.137.0-alpha.4** — Windows管理者向け`codex sandbox setup --elevated` alpha、App-server統合（[GitHub Releases](https://github.com/openai/codex/releases)）
- **ChatGPTセキュリティ機能** — Active sessions（アカウントセッション一覧・不審セッション管理）、Trusted Contact（安全信号検出時の信頼連絡先通知）（[Release Notes](https://help.openai.com/en/articles/6825453-chatgpt-release-notes)）

### Cognition / Devin

- **Devin Desktop正式ローンチ（6/2）** — 旧WindsurfをDevin Desktopにリブランド。Agent Command Center（Kanban一元管理）、Spaces（エージェント間コンテキスト共有）、ACP対応でCodex・Claude Agent・OpenCode統合、Devin Local（旧Cascade、Rust書き直しでトークン効率+30%）。クラシック環境セットアップは6/30廃止（[Cognition Blog](https://cognition.ai/blog/introducing-devin-desktop) / [Devin Blog](https://devin.ai/blog/windsurf-is-now-devin-desktop)）

### Cursor

- **Teams利用制限増加** — Standard席の含有利用量増加、Premium席新設（7/1以降の更新から適用）
- **Build in Parallel** — プランの独立部分を非同期サブエージェントで同時並列実行
- **Canvas共有・PR分割アクション** — リンクでCanvas共有、マルチタスク時のPR論理分割提案（[Changelog](https://cursor.com/changelog)）

### Mistral

- **Le Chat → Vibe リブランド + Work Mode商用展開** — Google Workspace・Outlook・Slack・GitHub統合のAIエージェントプロダクトに転換。新料金: Free / Pro $14.99 / Team $24.99/user / Student $5.99（[WinBuzzer](https://winbuzzer.com/2026/06/01/mistral-rebrands-le-chat-as-vibe-for-work-and-coding-xcxwbn/) / [AI Daily Post](https://aidailypost.com/news/mistral-ai-rebrands-lechat-vibe-positioning-it-full-ai-work-agent)）

### Google

- **Google Workspace更新** — Gemini appのchat/canvas/生成メディアをDrive経由共有、Device Bound Session Credentials GA（Chrome on Windows）、Workspace Studioリスト反復ループ追加、Drive「Organize My Files」GA（[Google Workspace Blog](https://workspaceupdates.googleblog.com/)）
- **xAI Grok Imagine API Quality Mode** — 画像生成・編集の写実度・テキストレンダリング強化（[x.ai](https://x.ai/news)）

### Computex 2026（続報）

- **Perplexity AI ハイブリッド推論** — ローカルLLMが「トラフィックコップ」として機密データをオンデバイス処理、高負荷タスクはクラウドにルーティング。7月提供開始（[VentureBeat](https://venturebeat.com/technology/perplexity-ai-unveils-hybrid-local-cloud-inference-system-at-computex-2026)）
- **Vector Core Compute** — Vista Equity + Cambium設立の推論特化クラウド。Intel Xeon 6 + SambaNova SN40 RDU + NVIDIA Blackwell GPU混在。SambaNova向け$3.5B投資（[DataCenter Dynamics](https://www.datacenterdynamics.com/en/news/vista-equity-partners-launches-vector-core-computer-an-inference-agentic-neocloud-with-sambanova-and-intel-compute/)）

### 市場データ

- **Similarweb AIトラッカー 4月** — Webトラフィックシェア: ChatGPT 54.7%（前月56.72%）、Gemini 27.4%（25.46%）、Claude 8.2%（6.02%）、DeepSeek 4.1%、Grok 2.8%。Claudeが+2.2pt上昇（[Similarweb](https://x.com/Similarweb/status/2008805674893939041)）

---

## 直近の注目予定

- **6/8**: Cursor Bugbot従量課金化 / Gemini 3.5 Flash Enterprise app既定有効化
- **6/15**: Anthropic Programmatic Credit Pool施行 / Claude API側でSonnet 4・Opus 4退役
- **6/16**: Microsoft Work IQ API GA
- **6/18**: Gemini CLI・Gemini Code Assist IDE拡張サービス終了（Antigravity CLI移行）
- **6/27**: GPT-4.5がChatGPTから退役
- **6/30**: Copilot Studio for TeamsでクラシックChatbot作成不可 / Devinクラシック環境セットアップ廃止
- **7/1**: Anthropic Claude Partner Network初回階層昇格レビュー / M365価格改定発効 / Defender XDR旧AIAgentsInfoテーブル廃止
- **8月**: GitHub CopilotでProject Polaris既定モデル化
- **8/26**: OpenAI Assistants API廃止 / o3退役
- **Q4 2026**: Azure Agent Mesh GA目標

---

## 改善メモ

- 01_ai-news-Master: WebFetch `code.claude.com/docs/en/changelog` のみ成功、他はWebSearchプライマリ運用継続
- 02_ai-news-Copilot: WebFetch 403継続（Microsoft Learn、GitHub Blog等）。Microsoft Learn MCP・WebSearch併用で対応
- 03_ai-news-industry: 全RSSフィード 403継続。WebSearchフォールバックで対応
- 02_ai-news-Copilot・03_ai-news-industryの6/4ダイジェストが復旧（前回6/3 daily時点では5/29以降停止中と記録）
- Trump AI大統領令: 6/2署名だが01_ai-news-Master・02_ai-news-Copilotでは未掲載。03_ai-news-industryのみが報道を拾っており、ソース横断の網羅性に差異あり
