# AI News Daily Summary - 2026-04-15

## 今日のハイライト

### 1. Copilot Chat 本日仕様変更発効 — Word/Excel/PPT/OneNoteでの無料アクセスが終了

**事実**: 本日4/15から、M365 Copilotライセンスを持たないユーザーのCopilot ChatがWord/Excel/PowerPoint/OneNoteで利用不可になる（2,000席以上の組織）。2,000席未満の組織は「standard access」に移行し日中のパフォーマンス制限が適用される。ラベルも「Copilot Chat (Basic)」「M365 Copilot (Premium)」に分離。Outlook内のCopilot Chat（受信トレイ・カレンダー連携）は引き続き利用可能。

**根拠**: 4/13のサマリーで予告した変更が本日発効。Microsoftの「無料Copilot Chat縮小→有料M365 Copilot移行促進」戦略の最大マイルストーン。2,000席以上の大企業が先行対象となるのは、エンタープライズ契約でのアップセルが主目的。一方、4/20にはSecurity CopilotがM365 E5に無料同梱開始（1,000ユーザーあたり400 SCU/月）と、有料ライセンスの価値を高める施策も並行して展開されている。

**影響**: 2,000席以上の組織でM365 Copilotライセンス未購入の場合、本日以降Word/Excel/PowerPointのCopilotボタン・サイドパネルが消える。Office内でCopilotを日常的に使っていた場合、業務フローが中断する。

**行動指針**: 対象組織の場合、ブラウザ版Copilot Chatへの切り替え手順をチームに周知する。ライセンス購入判断は実影響を見てからで構わない。2,000席未満の組織は「パフォーマンス低下」が許容範囲かを観察し、問題が出たら検討に入る。

- https://office-watch.com/2026/microsoft-removes-copilot-chat-word-excel-powerpoint-april-2026/
- https://techcommunity.microsoft.com/discussions/microsoft365copilot/removal-of-copilot-chat-availability-in-m365-apps/4502990

### 2. Claude Code 5日間で4リリース — Prompt Caching 1h TTL・/recap・Managed Agents基盤が揃う

**事実**: 4/10〜14にClaude Code v2.1.101→v2.1.108の4リリース。主要な追加: (1) v2.1.108でPrompt Caching 1h TTL（`ENABLE_PROMPT_CACHING_1H`環境変数）、`/recap`コマンド（セッション復帰時のコンテキスト再構築）、Skill toolでビルトインスラッシュコマンド実行、メモリフットプリント削減。(2) v2.1.105でWorktreeパス切替、PreCompactフックのブロック対応、プラグインバックグラウンドモニター、WebFetchのCSS/JS除去。(3) v2.1.101で`/team-onboarding`、OS CA証明書ストアのデフォルト信頼、コマンドインジェクション脆弱性修正。同時に、Claude Managed Agents（自律エージェント実行基盤、$0.08/session-hour + API料金）がパブリックベータ開始、ant CLI（Claude API公式CLIクライアント）もリリース。

**根拠**: Prompt Caching 1h TTLは、Claude Codeの長時間セッションでのAPI費用を大幅に削減する可能性がある（通常5分のキャッシュが1時間に延長）。`/recap`はコンテキストウィンドウのコンパクション後にセッション文脈を復元する機能で、長時間作業の実用性を直接向上させる。Managed Agentsは24/7稼働で約$58/月（ランタイムのみ）と、人間の常駐監視なしに自律タスクを実行する基盤を提供する。

**影響**: Claude Codeを日常利用しているなら、Prompt Caching 1h TTLによるコスト削減と`/recap`による作業継続性の改善は体感できるレベル。Managed Agentsは「バックグラウンドで自律的に動くエージェント」の公式基盤であり、定期タスクの自動化・CI/CDパイプラインへのAI組み込みが現実的になった。

**行動指針**: `ENABLE_PROMPT_CACHING_1H`を環境変数にセットして長時間セッションのコスト変化を計測する。`/recap`はコンパクション後に試して復元精度を確認する。Managed Agentsは現時点ではベータのため、本番投入前にサンドボックスで挙動を検証する段階。

- https://code.claude.com/docs/en/changelog
- https://platform.claude.com/docs/en/managed-agents/overview
- https://github.com/anthropics/anthropic-cli

### 3. Stanford HAI AI Index 2026公開 — AI経済価値の集中と透明性急落が鮮明に

**事実**: 4/13に423ページのレポートが公開。主要ファインディング: (1) 米国プライベートAI投資額$285.9B（中国の23倍）、(2) フロンティアモデルの90%超が産業界発、(3) PhD級科学・数学ベンチマークで人間水準超過、(4) Foundation Model Transparency Index平均58→40に急落（高性能モデルほど情報開示が少ない）、(5) AI楽観派59%（前年52%）だが不安感も52%に微増。PwC AI Performance Study 2026も同時期公開で「AI経済価値の74%が上位20%企業に集中」「差別化要因は効率化ではなく成長・事業変革へのAI活用」と報告。

**根拠**: 透明性スコアの急落（58→40）は、規模拡大とオープンネスがトレードオフに入ったことを意味する。PwCデータと合わせると「AIの恩恵は一部の先行企業に集中し、かつそれらのモデルはブラックボックス化が進行している」という構造が明確。IDC Directions 2026の「AI累積経済効果2031年に$22.5T」予測も、この偏在構造を前提にしたもの。

**影響**: コンサル提案で「AIを導入すべき理由」を語る際、PwCの「上位20%が成果の74%」は強力な根拠になる。ただし、導入しても「効率化」止まりでは差がつかず、「事業変革」レベルの活用でないと上位20%には入れない、という文脈で使う必要がある。

**行動指針**: Stanford HAI（無料DL可）とPwC AI Performance Study 2026の主要図表をNotionに保存する。提案資料への引用は「導入するかどうか」ではなく「どう活用するか（効率化vs事業変革）」の文脈で使うと刺さる。経過観察: IDC予測の2029年インフレクションポイント（訓練→推論シフト、エージェント大規模展開）は中期計画の時間軸設定に有用。

- https://hai.stanford.edu/ai-index/2026-ai-index-report
- https://www.pwc.com/gx/en/news-room/press-releases/2026/pwc-2026-ai-performance-study.html
- https://www.financialcontent.com/article/accwirecq-2026-4-9-idc-highlights-new-ai-research-at-directions-2026-on-economic-impact-agentic-buyers-and-the-rise-of-ai-agents

---

## カテゴリ別まとめ

### Anthropic / Claude

- **Project Glasswing / Mythos 波紋拡大**: 米財務省がMythos Previewへのアクセスを要請中（4/14 Bloomberg）。FRB議長パウエル・財務長官ベッセントがメガバンクCEOを緊急招集しAI起因のサイバーリスクについて警告（4/10）。Goldman SachsはMythosの利用を開始。FreeBSD 17年物RCE（CVE-2026-4747）等の重大脆弱性を完全自律で発見。$100Mクレジット + $4Mオープンソースセキュリティ寄付を投入
  - https://www.bloomberg.com/news/articles/2026-04-14/us-treasury-seeking-access-to-anthropic-s-mythos-to-find-flaws
  - https://www.anthropic.com/glasswing
  - https://red.anthropic.com/2026/mythos-preview/

- **MCP 97Mインストール突破（2026年3月）**: 実験的プロトコルからAIエージェント基盤インフラへの移行が完了。全主要AIプロバイダーがMCP互換ツールを出荷
  - https://thenewstack.io/ai-coding-tool-stack/

### OpenAI

- **GPT-5.4 APIリリース**: GPT-5.3-codexのコーディング能力を統合した初のメインラインモデル。Codexでは100万トークンコンテキスト（実験的）。GPT-5.2比で事実誤り33%減。GPT-5.4 pro（高計算量版）も同時提供。GPT-5.3 Instant MiniがChatGPTフォールバックモデルに追加
  - https://openai.com/index/introducing-gpt-5-4/
  - https://platform.openai.com/docs/changelog

- **GPT-5.5 "Spud" リリース間近**: 事前学習完了（3/24）。Polymarket: 4月中リリース78%。GPT-5.4比40%+向上ならGPT-6命名の可能性
  - https://lumichats.com/blog/gpt-5-5-spud-openai-release-date-features-april-2026-complete-guide

- **ChatGPT新機能群**: ショッピング改善（チャット内商品閲覧・比較）、Libraryファイル管理、Outlook連携拡張（共有メールボックス）、Codex Pro tier（$100/月）、omni-moderation-latest
  - https://help.openai.com/en/articles/6825453-chatgpt-release-notes

- **広告事業で2026年$2.5B、2030年$100B予測**: Sora終了（アプリ4/26、API 9/24）と並行して収益多角化を加速
  - https://www.usnews.com/news/business/articles/2026-04-13/as-ai-use-increases-at-work-many-employees-still-choose-not-to-use-it-gallup-poll

### Google

- **Gemini Robotics-ER 1.6（4/14）**: ロボティクス向け推論モデル新版。空間推論・マルチビュー理解強化、産業用計器読取り能力新規追加（Boston Dynamics協業）。Gemini API / AI Studioで提供。ER 1.5は4/30廃止
  - https://deepmind.google/blog/gemini-robotics-er-1-6/

- **gemini-embedding-2-preview**: Google初のマルチモーダル埋め込みモデル。テキスト・画像・動画・音声・PDFを統一埋め込み空間にマッピング
  - https://ai.google.dev/gemini-api/docs/changelog

- **Gemini Deep Research Agent API**: Interactions API経由で開発者に提供開始。HLE・DeepSearchQAでSOTA
  - https://blog.google/technology/developers/deep-research-agent-gemini-api/

- **Gemma 4（4/2リリース）**: 2B/4B/26B MoE/31B Denseの4構成。256Kコンテキスト、ネイティブ画像・音声、140言語超。Apache 2.0
  - https://blog.google/innovation-and-ai/technology/developers-tools/gemma-4/

### Meta

- **Llama 4 Scout & Maverick（4/5）**: 初のMoE + ネイティブマルチモーダル。Scout: 10Mトークンコンテキスト（業界最大）。Maverick: GPT-4o・Gemini 2.0 Flash超え。Apache 2.0
  - https://ai.meta.com/blog/llama-4-multimodal-intelligence/

- **Muse Spark（4/8）**: Meta Superintelligence Labs初の公開モデル。クローズドモデル（コード・ウェイト非公開）
  - https://www.bloomberg.com/news/articles/2026-04-08/meta-debuts-first-ai-model-from-prized-superintelligence-group

### Microsoft / Copilot / Power Platform

- **Security Copilot M365 E5同梱（4/20〜ロールアウト）**: 1,000ユーザーあたり400 SCU/月、最大10,000 SCU/月。追加費用なし
  - https://mc.merill.net/message/MC1261596

- **Power Platform April Feature Update GA群**: Monitor アラートGA、インベントリGA、ライセンスキャパシティレポートGA、Dataverse削除レコード復元GA（4月末）
  - https://www.microsoft.com/en-us/power-platform/blog/2026/04/09/whats-new-in-power-platform-april-2026-feature-update/

- **Copilot Analytics メトリクス強化**: Edge/OneNote/Outlook/Word/Excel/PowerPointの新メトリクス追加（4月末〜5月展開）
  - https://mc.merill.net/message/MC1266023

- **Microsoft Foundry Local GA**: ローカルAI推論SDK（~20MB）が正式リリース。クラウド不要・トークン課金なし。JS/Python/C#/Rust対応。OpenAI互換APIでクラウド↔ローカル切替可
  - https://devblogs.microsoft.com/foundry/foundry-local-ga/

### 開発ツール

- **Cursor 3.1（4/13）**: Agents Windowバグ修正。Tiled Layoutペイン分割、Voice Input改善、フレームドロップ87%削減
  - https://cursor.com/changelog/3-1

- **Devin — 知識管理・統合強化**: ナレッジノート管理、プレイブック管理、Slack/Linear統合改善、親子セッション階層化
  - https://docs.devin.ai/release-notes/overview

- **MiniMax M2.7オープンソース化**: SWE-Pro 56.22%（GPT-5.3-Codex並）。Opus 4.6比で入力50倍・出力60倍安価、推論速度3倍
  - https://www.minimax.io/news/minimax-m27-en

### エンタープライズ・ビジネス

- **Visa Intelligent Commerce Connect**: AIエージェントがユーザー代理で商品検索・選択・決済を実行するインフラ。主要エージェントプロトコル（Trusted Agent Protocol / MPP / ACP / UCP）対応
  - https://usa.visa.com/about-visa/newsroom/press-releases.releaseId.22276.html

- **GitHub Copilotデータ訓練ポリシー 4/24発効（リマインダー）**: Free/Pro/Pro+のインタラクションデータがデフォルトで訓練利用。オプトアウトはSettings > Copilot > Features
  - https://github.blog/news-insights/company-news/updates-to-github-copilot-interaction-data-usage-policy/

### 市場データ

- **Gallup調査**: 米国労働者の約30%がAI頻繁利用、約50%は未使用。非利用者の46%が「今のやり方を変えたくない」
  - https://www.gallup.com/workplace/704225/rising-adoption-spurs-workforce-changes.aspx

- **IDC Directions 2026**: AI累積経済効果2031年に$22.5T。2029年にインフレクションポイント（訓練→推論シフト、エージェント大規模展開）
  - https://www.financialcontent.com/article/accwirecq-2026-4-9-idc-highlights-new-ai-research-at-directions-2026-on-economic-impact-agentic-buyers-and-the-rise-of-ai-agents

---

## 直近の注目予定

| 日付 | イベント |
|------|---------|
| 4/15（本日） | Copilot Chat仕様変更発効 / Power Platform & Copilot Studioイベント（9AM PDT） |
| 4/19 | Claude Haiku 3 非推奨化 |
| 4/20 | Security Copilot M365 E5同梱ロールアウト開始（〜6/30） |
| 4/21-23 | Microsoft 365 Community Conference（Orlando） |
| 4/24 | GitHub Copilot データ訓練ポリシー変更発効 |
| 4/26 | Sora アプリ終了 |
| 4/30 | Gemini Robotics-ER 1.5廃止 / Claude 1Mコンテキストベータ終了 |

---

## 改善メモ

- 01_ai-news-Master: 多数ソースでWebFetchが403を返す状況が継続。WebSearchへのフォールバックが実質プライマリ化。daily-sources.mdの取得方法順序見直しを推奨
- 02_ai-news-Copilot: Copilot Studio What's New / M365 Release Notes / mc.merill.net / Power Platform Released Versions等が403継続。全てWebSearch経由で取得
- 03_ai-news-industry: 全RSSフィード403が継続。daily-sources.mdの取得方法を`WebSearch`優先に変更することを強く推奨
- Stanford HAI AI Index 2026が4/13に公開済。03_ai-news-industryの.last-check-state.mdを更新推奨
