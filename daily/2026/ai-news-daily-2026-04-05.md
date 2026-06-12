# AI News Daily Summary - 2026-04-05

## 今日のハイライト

### 1. Anthropic、サードパーティハーネス経由のClaude利用を遮断 — サブスク依存の開発者は即座にコスト構造の見直しが必要

**事実**: AnthropicはClaude Pro/Maxプランのサブスクリプション枠を、OpenClaw等のサードパーティ自律エージェントフレームワーク経由で利用することを4/4正午（PT）付で禁止した。今後は「extra usage」の従量課金が必要になる。

**根拠**: 推定135,000以上のOpenClawインスタンスが稼働中で、影響を受けるユーザーの中には最大50倍のコスト増となるケースもある。Boris Cherny（Claude Code責任者）は「サブスクリプションはサードパーティツールの利用パターンを想定して設計されていない」と説明。移行措置として月額相当の1回限りクレジット（4/17まで有効）と、事前購入で最大30%割引を提供。

**影響**: OpenClawやAider等のサードパーティハーネスで月額定額のClaude APIを前提にワークフローを組んでいた開発者は、即座にコスト構造が変わる。Claude Code（公式CLI）経由の利用は影響なし。OpenClaw作者が2月にOpenAIに入社済みという背景もあり、ツール自体の継続性リスクも併存する。

**行動指針**: サードパーティハーネスでClaudeを使っている場合、4/17までにextra usageの従量課金コストを試算し、公式Claude Codeへの移行またはAPI直接利用への切り替えを判断する。公式ツールのみ使用している場合は影響なし。

- https://thenextweb.com/news/anthropic-openclaw-claude-subscription-ban-cost
- https://www.news9live.com/technology/artificial-intelligence/claude-users-hit-by-surprise-cost-hike-as-anthropic-cuts-off-openclaw-access-2951813

### 2. GitHub Copilot、4/24からFree/Proユーザーのデータをモデル学習に使用 — オプトアウト確認は今週中に

**事実**: GitHub Copilot Free・Pro・Pro+ユーザーのインタラクションデータ（入出力・コードスニペット・カーソル周辺コンテキスト・リポジトリ構造等）が4/24からAIモデル学習に使用される。Business/Enterpriseプランは対象外。

**根拠**: 以前にオプトアウト設定済みのユーザーは引き継がれるが、新規ユーザーはデフォルトオプトイン。開発者コミュニティからは「ダークパターン」との批判が出ている。Business/Enterpriseとの差別化により、個人開発者と組織利用者の間でデータ保護レベルに明確な格差が生じる。

**影響**: 個人でCopilot Free/Proを使っている場合、自分のコードと操作データがモデル学習に使われることになる。プロプライエタリなコードや機密性の高いプロジェクトでの利用は再検討が必要。

**行動指針**: Copilot Free/Proユーザーは4/24までにGitHub Settings → Copilot → データ利用設定でオプトアウトを確認する。組織利用の場合はBusiness/Enterpriseプランへのアップグレードを検討。Cursor等の代替ツールとのデータポリシー比較も判断材料になる。

- https://github.blog/news-insights/company-news/updates-to-github-copilot-interaction-data-usage-policy/
- https://www.infoq.com/news/2026/04/github-copilot-training-data/

### 3. Security CopilotがM365 E5に標準バンドル（4/20〜段階展開） — E5テナント管理者は自動有効化に備えた準備を

**事実**: Microsoft Security CopilotがM365 E5/E7テナントに自動有効化（ゼロクリックアクティベーション）される。4/20〜6/30にかけて段階展開。1,000ライセンスあたり月400 SCU（最大10,000 SCU/月）を無償提供。

**根拠**: Entra・Intune・Purview・Defenderおよびスタンドアロンポータルのチャット・プロンプトブック・エージェントシナリオが対象範囲。E5ライセンスを既に持つ組織にとっては追加コストなしでセキュリティAIが利用可能になる。

**影響**: E5テナントでは管理者が何もしなくても自動有効化される。セキュリティポリシーやデータアクセス権限の設定を事前に確認しないと、意図しないデータ参照が発生する可能性がある。

**行動指針**: M365 E5テナント管理者は4/20までにSecurity Copilotのデータアクセス範囲とアクセス制御ポリシーを確認する。E5未満のプランでは対象外のため、経過観察。

- https://mc.merill.net/message/MC1261596

---

## カテゴリ別まとめ

### Claude Code / Anthropic

- **Claude Code v2.1.92リリース（4/4）**: Bedrock対話型セットアップウィザード追加、`/cost`にモデル別・キャッシュヒット別内訳表示、Write toolの差分計算が大規模ファイルで60%高速化、`/tag`と`/vim`コマンド削除（vimモードは`/config`から切替）、複数バグ修正
  - https://code.claude.com/docs/en/changelog

- **マルチエージェントハーネス設計を公開（4/4）**: 長時間自律アプリケーション開発向け3エージェント構成（Planner/Generator/Evaluator）。1回のランで5〜15イテレーション、最大4時間の自律セッション。単独20分/$9 → フルハーネス6時間/$200
  - https://www.anthropic.com/engineering/harness-design-long-running-apps

- **Claude API 1Mコンテキストベータ終了予定（4/30）**: Sonnet 4.5/4の1Mトークンベータが4/30終了。以降は標準200k超のリクエストがエラーに。Sonnet 4.6/Opus 4.6への移行が必要
  - https://releasebot.io/updates/anthropic

- **日本向けClaude料金に消費税10%適用開始（4/1〜）**: 全プラン対象
  - https://support.claude.com/en/articles/14051822-notice-regarding-consumption-tax-jct-for-japanese-customers

### Microsoft 365 Copilot / Copilot Studio

- **Copilot Chat仕様変更（4/15）まであと10日**: Word/Excel/PowerPoint/OneNoteでのCopilot Chatアクセスが有料ライセンス（M365 Copilot Premium）専用に。Copilot Chatユーザーは「Basic」ラベルに変更
  - https://blogs.imperial.ac.uk/office365/2026/03/20/copilot-chat-changes-april-2026/

- **Copilot Chat、Outlook共有/委任メールボックスで利用可能に（4月初旬〜5月初旬）**
  - https://mc.merill.net/message/MC1246031

- **Researcherに新出力形式追加（4月中旬〜下旬）**: PowerPoint/PDF/インフォグラフィック/音声概要の4形式
  - https://learn.microsoft.com/en-us/copilot/microsoft-365/release-notes

- **Copilot NotebooksにパブリックWebリンク参照機能（4月下旬）**
  - https://learn.microsoft.com/en-us/copilot/microsoft-365/release-notes

- **Power Platform & Copilot Studioアップデートイベント: 4/15 9:00 AM PDT**: マルチエージェントオーケストレーションGA等の発表予告

- **Planner Agentパブリックプレビュー展開中（〜4月下旬）**
  - https://mc.merill.net/message/MC1256306

- **PowerPoint Agent Mode展開継続中（〜4月末）**
  - https://mc.merill.net/message/MC1243550

- **Purview Insider Risk Managementに従量課金モデル（生成AIアプリ向け）**
  - https://mc.merill.net/message/MC1242784

### OpenAI

- 4/4-5時点で新規アップデートなし。直近の主要変更（既報）: GPT-4o完全廃止（4/3）、ChatGPT Voice CarPlay対応（4/3）、Codex従量課金制。GPT-5.5（コードネーム"Spud"）開発完了報道は継続中

### Google

- **Gmail「Help me schedule」がグループ会議対応**: 複数ゲストとの会議調整をGmail作成画面から直接実行可能に
  - https://workspaceupdates.googleblog.com/

- **Google Meet CarPlay対応**: 車のダッシュボードから直接Google Meetにアクセス可能

- **Ask Gemini in Meet多言語対応拡大**: 日本語を含む7言語を追加

- **Google Vidsアバターカスタマイズ**: Nano Banana 2によるブランド合致のAIアバター作成

### Devin

- **エンタープライズ機能強化（4/3）**: フルデスクトップテスト（Computer Use活用、Linux上のE2Eテスト＋録画レビュー）、Enterprise-Scoped Secrets、ACU Visibility Control、MCP Registry Enforcement、Build Pinning
  - https://docs.devin.ai/release-notes/overview

### Cursor

- 4/4-5時点で新規アップデートなし。Cursor 3.0（4/2リリース）が最新

### 企業動向・リストラ

- **Oracle、2〜3万人規模のレイオフ**: 全従業員の約18%。FY2026 CapEx $50B（前年比+40%）をAIインフラに集中投下。FCFは2024年の$11.8Bから2026年に-$23Bへ転落見通し
  - https://www.cnbc.com/2026/03/31/oracle-layoffs-ai-spending.html

- **Block（Square/Cash App）、4,000人解雇**: 全従業員の約40%を削減。DorseyがAIによる中間管理職代替を提唱。現場からは「AI生成コードの95%は修正が必要」との声
  - https://www.coindesk.com/tech/2026/04/01/jack-dorsey-says-ai-should-replace-corporate-hierarchy-after-block-cuts-4-000-jobs

### 市場データ・調査

- **IDC: エージェンティックAI支出、2029年に$1.3T（IT支出全体の26%超）**: 年平均31.9%成長
  - https://my.idc.com/getdoc.jsp?containerId=prUS53765225

- **IDC Japan: 国内AIシステム市場、2029年に4兆1,873億円**: 2024年は前年比56.5%増の1兆3,412億円。生成AI市場は2028年に8,028億円（CAGR 84.4%）
  - https://my.idc.com/getdoc.jsp?containerId=prJPJ53362125

- **Stanford HAI AI Index 2026年版、4/13公開予定**
  - https://hai.stanford.edu/ai-index

---

## 直近の注目予定

- **4/13**: Stanford HAI AI Index 2026年版 公開
- **4/15**: Copilot Chat仕様変更（Basic/Premium二層化）
- **4/15**: Power Platform & Copilot Studioアップデートイベント
- **4/17**: Anthropic OpenClaw移行クレジット期限
- **4/20〜**: Security Copilot M365 E5自動有効化開始
- **4/21-23**: Microsoft 365 Community Conference（Orlando）
- **4/24**: GitHub Copilot Free/Proデータ学習利用開始
- **4/30**: Claude 1Mコンテキストベータ終了（Sonnet 4.5/4）
- **5/1**: M365 E7 Frontier Suite GA / Agent 365 GA

---

## 改善メモ

### 01_ai-news-Master
- [Anthropic Blog] 403 → WebSearchで取得成功
- [Claude Release Notes] 403 → WebSearchで取得成功
- [OpenAI RSS/Platform Changelog/ChatGPT Release Notes] すべて403 → WebSearchで取得成功
- [Google Workspace RSS / Gemini App / The Keyword RSS / Research RSS] すべて403 → WebSearchで取得成功
- [Cursor Changelog / Devin Release Notes] 403 → WebSearchで取得成功
- 多数のソースで403が発生。WebFetchの制限が一時的か恒常的か要観察

### 02_ai-news-Copilot
- [Copilot Studio What's New / M365 Copilot Release Notes / Power Platform Released Versions] WebFetch 403 → WebSearch経由で取得成功
- [Tech Community M365 Copilot Blog / mc.merill.net / releasebot.io] WebFetch 403 → WebSearch経由で取得成功
- learn.microsoft.com配下も403を返すようになっている（3日連続）

### 03_ai-news-industry
- [TechCrunch AI] RSS 403継続。WebSearchで4月上旬記事のインデックスが遅い
- [The Verge AI] WebFetch/WebSearch共に直接記事取得困難が継続
- [テクノエッジ / ITmedia AI＋] 4月個別記事取得困難が継続
- [MM総研] 新規プレスリリースなし
