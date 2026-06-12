# AI News Daily - 2026-04-22

## 今日のハイライト

### 1. GitHub Copilot 個人プランの実質縮小 — Opusモデル除外・新規登録停止・使用量制限強化

- **事実**: 4/20付でGitHub Copilotの個人向けプランに3つの大きな変更が入った。Pro / Pro+ / Studentの新規サインアップ一時停止、使用量制限の厳格化（Pro+はProの5倍以上の枠）、そしてOpusモデルのPro除外（Opus 4.7はPro+のみ、Opus 4.5/4.6はPro+からも削除）。
- **根拠**: エージェント型ワークフローの長時間・並列セッション急増がプラン設計の想定を大幅に超えた、とGitHub自身が説明している。加えて4/24にはデータ学習ポリシー変更（Free/Pro/Pro+のインタラクションデータをモデル学習に使用、デフォルトON）が発効する。つまり「使える範囲は狭まるが、データは取られる」という非対称な変更が同時進行している。
- **影響**: Proプランで高性能モデルを前提にしていた開発者は、実質的にPro+への課金か別ツールへの移行を迫られる。一方Claude Code（ARR $2.5B）やCursor等の競合は制限が異なるため、ツール選択の再評価タイミングになる。
- **行動指針**: (1) 4/24までにSettings > Copilot > Featuresでデータ学習のオプトアウトを確認。(2) 現在のモデル使用状況をVS Code/CLIの残量表示で把握し、Pro+への移行コストと代替ツール（Claude Code、Cursor）のコストを比較する。Business/Enterpriseユーザーはデータ学習対象外のため作業不要。
- https://github.blog/changelog/2026-04-20-changes-to-github-copilot-plans-for-individuals/

### 2. Moonshot AI Kimi K2.6 — オープンウェイト1Tモデルがクローズド最上位と肩を並べる

- **事実**: 4/20公開。1TパラメータMoEアーキテクチャ、128Kコンテキスト。複数ベンチマークでClaude Opus 4.6・GPT-5.4を上回るスコアを記録。最大300サブエージェント・4,000ステップの長時間自律コーディングに対応。オープンウェイトで誰でもダウンロード可能。
- **根拠**: Artificial Analysis Intelligence Indexで#4（Anthropic・Google・OpenAIに次ぐ）にランクイン。中国発オープンモデルとしてDeepSeek v4に先行。ベンチマーク上位のモデルがオープンウェイトで手に入る状況は、API依存のコスト構造を根本から変える可能性がある。
- **影響**: セルフホスト可能な1Tモデルが最上位クローズドモデルと同等性能を出すなら、推論コストの自社コントロールやデータプライバシーの完全確保が現実的になる。ただし1T MoEの推論にはGPUクラスタが必要で、個人や中小規模では恩恵が限定的。
- **行動指針**: GPU予算のある組織はKimi K2.6のベンチマーク再現と自社タスクでの検証を検討する価値がある。個人開発者はAPI経由での提供状況を待つか、量子化版の登場を経過観察。
- https://siliconangle.com/2026/04/20/moonshot-ai-releases-kimi-k2-6-model-1t-parameters-attention-optimizations/
- https://www.marktechpost.com/2026/04/20/moonshot-ai-releases-kimi-k2-6-with-long-horizon-coding-agent-swarm-scaling-to-300-sub-agents-and-4000-coordinated-steps/

### 3. Anthropic ARR $30B突破 — 4ヶ月で3倍、企業顧客が成長の主軸

- **事実**: 4月初旬にARRが$30Bに到達。2025年末$9Bから約4ヶ月で3倍超。企業顧客が売上の約80%を占め、年間$1M以上支出の顧客が2ヶ月で500→1,000社に倍増。Claude CodeのARRは$2.5B。Fortune 10の8社が顧客。
- **根拠**: 2月のSeries G $30B調達（評価額$380B）後も加速が続いており、売上規模でOpenAIを逆転したとの報道もある。Google/Broadcomとの3.5GW TPU契約はインフラ投資の本気度を示す。
- **影響**: Anthropicの事業継続性リスクは大幅に低下した。Claude/Claude Codeを業務基盤に据える判断の合理性は高まっている。一方、急成長期の価格改定やポリシー変更の可能性は常にある。
- **行動指針**: Claude前提の業務設計は継続で問題ない。ただし前回（4/16）のハイライトで述べた通り、半期に一度は代替モデルへの切り替えドライランを実施し、ベンダーロックインを管理する。
- https://www.pymnts.com/artificial-intelligence-2/2026/anthropic-hits-30-billion-run-rate-as-enterprise-demand-accelerates/
- https://techcrunch.com/2026/04/14/anthropics-rise-is-giving-some-openai-investors-second-thoughts/

---

## カテゴリ別まとめ

### Microsoft 365 / Copilot

- **M365 Community Conference 2026 開幕（4/21-23, Orlando）**: Day 1でCopilot・Teams・SharePointのAI統合ロードマップ発表。マルチエージェント連携デモ。Agent 365の統合デモ。本日Day 2はセキュリティキーノート（Purview・Defender・Entra・Security Copilot統合）
  - https://techcommunity.microsoft.com/blog/microsoft_365blog/your-guide-to-the-microsoft-365-community-conference/4505384
- **Security Copilot × M365 E5 バンドル展開開始（4/20）**: 400 SCU/1,000ユーザー（上限10,000 SCU/月/テナント）。データ共有がデフォルトONのため管理者確認推奨
  - https://mc.merill.net/message/MC1261596
- **M365 E7 Frontier Suite**がトランザクション可能に（E5 + Entra Suite + Copilot + Agent 365、$99/user/月で5/1 GA）
- **M365 Copilot 4月ロールアウト**: 会議ビデオハイライトリール生成、AI in SharePoint（Public Preview）、Excel × Work IQ、Copilot Search管理者制御
  - https://www.flotek.io/blog/microsoft-365-copilot-updates-april-2026

### Copilot Studio

- **MC1282727: クラシックエージェント作成の廃止延期** — 当初4/1予定が実装上の問題で延期。新廃止日は別途通知
  - https://mwpro.co.uk/blog/2026/04/17/microsoft-copilot-studio-update-classic-agent-creation-experience-in-teams-mc1282727/
- **MC1282306: 変更管理モダナイズ** — Frontier/Standard/Deferredリリースオーディエンス制、MCP Server AI変更管理が展開中（4月下旬完了見込み）
  - https://mc.merill.net/message/MC1282306

### Anthropic / Claude

- **Claude Haiku 3 正式廃止（4/19実施済み）**: APIリクエストがエラーを返すように。猶予期間なし。移行先はClaude Haiku 4.5（コスト約4倍、API破壊的変更あり）
  - https://platform.claude.com/docs/en/about-claude/model-deprecations

### OpenAI

- **GPT-Rosalind（ライフサイエンス特化モデル）発表（4/17）**: 生物学・創薬向け専門推論。BixBenchで0.751 Pass@1（GPT-5.4: 0.732超）。Amgen・Moderna等と提携。汎用→専門特化モデルへのシフトを象徴
  - https://openai.com/index/introducing-gpt-rosalind/
  - https://venturebeat.com/technology/openai-debuts-gpt-rosalind-a-new-limited-access-model-for-life-sciences-and-broader-codex-plugin-on-github

### GitHub Copilot

- **CLI v1.0.33（4/20）**: `--resume`/`--continue`で`--remote`フラグ自動継承、`auto`モデル選択、週次使用量75%/90%到達時に警告表示、ドキュメント添付機能
  - https://github.blog/changelog/2026-04-20-changes-to-github-copilot-plans-for-individuals/
- **データ学習ポリシー変更 4/24発効（残り2日）**: Free/Pro/Pro+のインタラクションデータがモデル学習対象に。opt-outはSettings > Copilotから
  - https://github.blog/changelog/month/04-2026/

### Google

- **Gemini in Chrome、日本含むAPAC 7カ国に展開（4/20-21）**: Chromeサイドパネルから複数タブ要約、Gmail/Photos/Calendar/Maps連携。日本はデスクトップのみ（iOS未対応）
  - https://techcrunch.com/2026/04/20/google-rolls-out-gemini-in-chrome-in-seven-new-countries/
  - https://gigazine.net/news/20260421-chrome-ai-japan/

### 開発者ツール・プラットフォーム

- **Cloudflare Agents Week（4/13-17）**: 5日間で10製品リリース。Email Service（AIエージェントがメール送受信）、Artifacts（Gitコンパチ版管理ストレージ）等
  - https://blog.cloudflare.com/agents-week-in-review/
  - https://blog.cloudflare.com/email-for-agents/
- **Fathom 3.0（4/15）**: ボットフリーAI議事録、ChatGPT/Claude MCP連携、Product Hunt #1
  - https://techcrunch.com/2026/04/15/fathom-adds-a-bot-less-meeting-mode-in-a-bid-to-take-on-granola/

### スタートアップ・資金調達

- **Recursive Superintelligence**: 創業4ヶ月で$500M調達（評価額$4B）。GVリード、NVIDIA参加。元Salesforce CSO Richard Socher創業。自己改善AIシステムを目指す
  - https://the-decoder.com/self-improving-ai-startup-recursive-superintelligence-pulls-in-500-million-just-four-months-after-founding/

### 規制・政策

- **公正取引委員会: 生成AI実態調査報告書 ver.2.0（4/16）**: AI検索サービスによる報道記事無許可利用問題を含む包括調査。Google・LINEヤフー等を念頭に優越的地位の濫用の観点から調査
  - https://www.jftc.go.jp/houdou/pressrelease/2026/apr/260416_generativeai.html

### 市場データ

- **IDC: AI Compute牽引で半導体ファウンドリ市場$360B（前年比+17%）**。AI累積経済効果2031年$22.5T予測
  - https://www.biztechreports.com/news-archive/2026/4/8/ai-compute-boom-propels-foundry-20-market-to-usd-360-billion-up-17-in-2026-idc-april-13-2026
- **MIT Technology Review「10 Things That Matter in AI Right Now」初公開（4/21）**: AIコンパニオン、メカニスティック・インタープリタビリティ、生成コーディング等を選出
  - https://www.technologyreview.com/2026/04/14/1135298/coming-soon-10-things-that-matter-in-ai-right-now/
- **Deezer: 楽曲アップロードの44%がAI生成（日量75,000曲）**: 2025年1月の日量10,000曲から7.5倍に急増。ただしストリーミング再生の1-3%に留まり、大半は不正再生として収益化停止
  - https://techcrunch.com/2026/04/20/deezer-says-44-of-songs-uploaded-to-its-platform-daily-are-ai-generated/

---

## 直近の注目予定

| 日付 | イベント |
|------|---------|
| 4/23（明日） | M365 Conference Day 3 — Jamie Teevan「The Future of Work」キーノート |
| 4/24 | GitHub Copilot データ学習ポリシー変更発効（Free/Pro/Pro+ 対象） |
| 4月下旬 | MC1263276: サードパーティモデルプロバイダーのユーザー割当展開開始 |
| 4月下旬 | MC1282306: 変更管理モダナイズ展開完了見込み |
| 5/1 | Agent 365 GA（$15/user/月）、M365 E7 Frontier Suite GA（$99/user/月） |
| 5/1 | Power Apps MCP Server 移行期限 |
| 5/4 | Power Apps Agent Feed GA |
| 5/20 | GitHub Copilot プラン変更に対する返金申請期限 |

---

## 改善メモ

- [Copilot Studio What's New] 取得失敗（403、13日連続）→ WebSearchで成功
- [M365 Copilot Release Notes] 取得失敗（403）→ WebSearchで成功
- [Power Platform Released Versions] 取得失敗（403）→ WebSearchで成功
- [Copilot Studio Release Wave] 取得失敗（403）→ WebSearchで成功
- [changepilot.cloud / flotek.io] 取得失敗（403）→ WebSearchで成功
- 全RSSフィード（Google News RSS / GIGAZINE / The Decoder / VentureBeat / Publickey / hnrss.org / Product Hunt / GitHub Trending RSS）が引き続き403。WebSearchフォールバックで取得
- learn.microsoft.com系の403が13日連続。daily-sources.mdの取得方法を「WebSearch」プライマリに改定することを強く推奨（両ソースから同一提案が継続中）
