# AI News Daily - 2026-04-23

## 今日のハイライト

### 1. SpaceX、Cursorを$60Bで買収するオプション契約を締結 — AIコーディングツール市場の勢力図が変わる

- **事実**: SpaceX（xAI親会社）がAIコーディングスタートアップCursorと、年内に$60Bで買収するか$10Bのパートナーシップ料を支払う二択構造の契約を締結した。SpaceXは6月に$2T評価額でのIPOを計画中のため即時買収は見送り。
- **根拠**: Cursor単体の買収額として$60Bは、AIコーディングツール市場における過去最大級の評価。xAIにとってはOpenAI Codex・Anthropic Claude Codeへの直接対抗策となる。SpaceXのIPO後に$60Bの現金を動かせる体力があるかが焦点になる。
- **影響**: AIコーディングツール市場がOpenAI（Codex）・Anthropic（Claude Code）・xAI/Cursor・GitHub Copilotの四つ巴に収斂しつつある。各ツールのデータポリシー・価格・モデル性能の差異が、開発者のツール選択に直結する構造がより鮮明になった。
- **行動指針**: 現時点で開発者が取るべきアクションはない。ただし、CursorユーザーはxAI傘下入り後のデータポリシー変更リスクを念頭に置き、設定のエクスポートや代替ツールの検証環境を維持しておく。買収が成立するかはIPO後の判断次第で、経過観察。
- https://techcrunch.com/2026/04/21/spacex-is-working-with-cursor-and-has-an-option-to-buy-the-startup-for-60-billion/
- https://www.cnbc.com/2026/04/21/spacex-says-it-can-buy-cursor-later-this-year-for-60-billion-or-pay-10-billion-for-our-work-together.html

### 2. GitHub Copilot データ学習ポリシー変更 — 明日（4/24）発効、opt-outは今日中に

- **事実**: Free/Pro/Pro+ユーザーのインタラクションデータ（入出力・コードスニペット・コンテキスト）をモデル学習に使用する変更が4/24に発効する。デフォルトON。プライベートリポジトリのコードもCopilot使用中は対象。GitHub Community Discussionでは232ダウンvoteと強い反発が出ている。
- **根拠**: 前日（4/22）のハイライトで報じたプラン縮小（Opusモデル除外・新規登録停止）に加え、データ収集がデフォルトONで重なる。「使える範囲は狭まるが、データは取られる」という非対称な構造は変わっていない。Business/Enterprise/Student/Teacherは対象外。
- **影響**: 個人開発者がプライベートリポジトリでCopilotを使う場合、コードがモデル学習に流れる可能性がある。企業の副業開発者や機密性の高い個人プロジェクトを持つ層には看過できない変更。
- **行動指針**: 今日中に `/settings/copilot/features` → Privacy でオプトアウトを確認・実行する。過去にopt-out済みなら設定は維持される。Business/Enterpriseユーザーは対象外のため作業不要。
- https://github.blog/news-insights/company-news/updates-to-github-copilot-interaction-data-usage-policy/
- https://the-decoder.com/github-will-use-copilot-interaction-data-to-train-ai-models-starting-april-2026/

### 3. Anthropic Claude Code — Pro プラン除外テストを即日撤回、料金改定の布石

- **事実**: 4/21にAnthropicが$20 Proプランからclaude Codeを除外し、最低Max 5x（$100/月）を必要とするテストを実施。数時間後に撤回。成長責任者Amol Avasareは「新規prosumerサインアップの約2%を対象にしたテスト」と説明し、テスト対象外の98%にとってランディングページの変更が混乱を招いたミスだったと認めた。
- **根拠**: 背景にあるのはエージェント型利用の急増。「現行プランはこの使い方を想定していない」とAvasare自身が言及しており、今後の料金体系改定はほぼ確実に起こる。AnthropicのARR $30B（4ヶ月で3倍）の成長を支えつつ、エージェント利用のコスト構造を持続可能にする必要がある。
- **影響**: 今回は撤回されたが、Claude Codeの$20プランでの提供は長期的に維持されない可能性が高い。現在のProプランでClaude Codeをヘビーに使っているユーザーは、将来の価格変更に備える必要がある。
- **行動指針**: 現時点ではProプランでClaude Codeを引き続き利用可能。ただし、(1) 月額コストが上がった場合の代替ツール（GitHub Copilot CLI、Cursor）との比較基準を持っておく、(2) Claude Code固有の設定やワークフロー（CLAUDE.md等）が他ツールに移植しやすい形かを確認しておく。
- https://www.theregister.com/2026/04/22/anthropic_removes_claude_code_pro/

---

## カテゴリ別まとめ

### Microsoft 365 / Copilot

- **M365 Community Conference Day 2-3**: Day 2はVasu Jakkal & Rohan Kumarによるセキュリティキーノート。Purview・Defender・Entra・Security Copilotの統合によるAIセキュリティの多層防御を実演。Day 3（本日）はJaime Teevan「The Future of Work」キーノート
  - https://techcommunity.microsoft.com/blog/microsoft_365blog/your-guide-to-the-microsoft-365-community-conference/4505384
- **MC1266023: Copilot Analytics 包括的メトリクス追加**: Edge・OneNote・Outlook・Word・Excel・PowerPointでのCopilot利用メトリクスを追加。4月下旬〜5月下旬展開
  - https://mc.merill.net/message/MC1266023
- **MC1279072: プリペイド Copilot Credits**: M365 Copilot Chatでプリペイドクレジットを PAYG なしで利用可能に。4/20開始〜5月上旬完了
  - https://mc.merill.net/message/MC1279072
- **MC1263276: サードパーティモデルプロバイダー割当**: 管理者がAnthropic・xAI等のモデルをユーザー/グループに割当可能に。4月下旬展開中
  - https://mc.merill.net/message/MC1263276
- **Microsoft「Frontier Transformation」パートナー認定拡充**: Frontier Badge → Frontier Partner Specializationに進化。Frontier Engineer Badge新設
  - https://blogs.microsoft.com/blog/2026/04/21/accelerating-frontier-transformation-with-microsoft-partners/

### Anthropic / Claude

- **Claude Cowork Live Artifacts**: リアルタイム更新のダッシュボード・トラッカーをCowork内で構築可能に。接続アプリから最新データを自動取得。BIツール不要の軽量ダッシュボード
  - https://x.com/claudeai/status/2046328619249684989
  - https://yourstory.com/ai-story/claude-cowork-live-dashboards-ai-bi-disruption
- **Claude Code 新機能**: Ultraplan（クラウド上でプラン作成→Webエディタでレビュー）、Monitorツール（バックグラウンドイベントのストリーミング）、`/resume`が40MB+セッションで最大67%高速化
  - https://code.claude.com/docs/en/changelog

### OpenAI

- **ChatGPT Images 2.0**: gpt-image-2モデル搭載。Thinking機能（画像モデル初の推論）、2K解像度・最大8枚同時生成、多言語テキスト描画の精度向上、Web検索連携。Image Arenaで全カテゴリ1位（+242pt差）
  - https://openai.com/index/introducing-chatgpt-images-2-0/
  - https://gigazine.net/news/20260422-chatgpt-images-2-0/

### GitHub Copilot

- **データ学習ポリシー変更（4/24発効）**: ハイライト参照
- **Cursor Bugbot Learned Rules**: PRフィードバック（開発者リアクション・人間レビューアーコメント）から学習するルールを追加。バグ検出精度向上とfalse positive低減
  - https://cursor.com/changelog

### 国内AI動向

- **NII「LLM-jp-4」オープンソース公開**: 8Bと32B-A3B（MoE）の2モデル。約12兆トークンの日本語中心コーパスで学習。日本語MT-Benchで32B-A3Bが7.82（GPT-4o: 7.29を上回る）。2,600名超の産学コミュニティで開発
  - https://www.nii.ac.jp/news/release/2026/0403.html
  - https://gihyo.jp/article/2026/04/llm-jp-4
- **ICT総研: 国内生成AI個人利用率54.7%**: 初の過半数超え（前回29.0%から+25.7pt）。ChatGPT 36.2%、Gemini 25.0%、Microsoft Copilot 13.3%
  - https://ictr.co.jp/report/20260220.html/

### その他

- **Snap: 従業員16%（約1,000名）削減**: AIの新規コードの65%以上を生成。年間$500M以上のコスト削減。株価は11%上昇。AI効率化による大規模レイオフの事例
  - https://techcrunch.com/2026/04/15/snap-is-cutting-1000-jobs-16-of-its-workforce/
- **Power Pages エージェントコードプラグイン拡張**: サーバーサイドロジック対応の3つの新スキルを追加
  - https://www.microsoft.com/en-us/power-platform/blog/2026/04/09/whats-new-in-power-platform-april-2026-feature-update/

---

## 直近の注目予定

| 日付 | イベント |
|------|---------|
| **4/24（明日）** | GitHub Copilot データ学習ポリシー変更発効（Free/Pro/Pro+ 対象） |
| 4月下旬 | MC1263276: サードパーティモデルプロバイダーのユーザー割当展開 |
| 4月下旬 | MC1266023: Copilot Analytics 包括的メトリクス展開 |
| 5/1 | Agent 365 GA（$15/user/月）、M365 E7 Frontier Suite GA（$99/user/月） |
| 5/1 | Power Apps MCP Server 移行期限 |
| 5/4 | Power Apps Agent Feed GA |
| 5/20 | GitHub Copilot プラン変更に対する返金申請期限 |

---

## 改善メモ

- [Copilot Studio What's New] 取得失敗（403、14日連続）→ WebSearchで成功
- [M365 Copilot Release Notes] 取得失敗（403）→ WebSearchで成功
- [Power Platform Released Versions] 取得失敗（403）→ WebSearchで成功
- [mc.merill.net] 取得失敗（403）→ WebSearchで成功
- 全RSSフィード（Google News RSS / GIGAZINE / The Decoder / VentureBeat / Publickey / hnrss.org / Product Hunt / GitHub Trending RSS）が引き続き403。WebSearchフォールバックで取得
- learn.microsoft.com系の403が14日連続。daily-sources.mdの取得方法を「WebSearch」プライマリに改定することを強く推奨（両ソースから同一提案が継続中）
- NII LLM-jp-4（4/3公開）・Snap レイオフ（4/15発表）は公開日から遅延した報告。デイリーチェック時の検索クエリに幅を持たせることを検討
