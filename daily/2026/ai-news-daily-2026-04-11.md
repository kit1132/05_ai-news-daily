# AI News Daily Summary - 2026-04-11

## 今日のハイライト

### 1. Anthropic Mythos/Project Glasswing — 財務長官・FRB議長が大手銀行CEOを緊急招集

**事実**: 4/10、米財務長官Bessentと連邦準備制度理事会議長Powellが、JPMorgan・Goldman Sachs・BofA・Citi・Morgan Stanley・Wells Fargoの6大銀行CEOを招集し、AnthropicのMythosモデルに関する緊急警告を実施。Mythosは主要OS・ブラウザで「数千件の高深刻度脆弱性を自律発見」する能力を持ち、Anthropicは24時間の内部審議を経て限定公開を決定した。Project GlasswingにはAWS・Apple・Broadcom・Cisco・CrowdStrike・Google・JPMorgan・Linux Foundation・Microsoft・NVIDIA・Palo Alto Networksが参加。Anthropicは最大$100Mの利用クレジットと$4Mのオープンソースセキュリティ団体向け寄付を拠出。

**根拠**: FRB議長と財務長官が直接、特定AIモデルについて大手銀行CEOを緊急招集した事例はこれが初。通常の金融システミックリスク通知とは別枠の対応規模。前日までの報道では「17年前のFreeBSD RCE（CVE-2026-4747）を発見」という具体的成果も確認済み。11社に及ぶハイパースケーラー・セキュリティ企業の連名参加は、単独ベンダー対応では吸収しきれない規模の脆弱性発見を示唆する。

**影響**: 「AIの自律脆弱性発見」が防御側と攻撃側の双方で実用フェーズに入ったことの公式シグナル。金融機関はまずパッチ適用前倒しの連鎖対応が求められ、次いで自社SOCでの同種能力の獲得が論点化する。一般ユーザーの直接的な行動はないが、今後数週間で主要OS・ブラウザの緊急パッチが集中する可能性が高い。

**行動指針**: 自社でOS/ブラウザを管理しているならパッチ適用キャパシティを2週間前倒しで確保する。それ以外は経過観察でよいが、Glasswing参加11社（AWS/Apple/Google/Microsoft等）のセキュリティアドバイザリを来週1週間は優先度を上げて確認する。Anthropic Mythosそのものは現時点で触れる手段がないため、自分で試そうとする時間は不要。

- https://www.bloomberg.com/news/articles/2026-04-10/anthropic-model-scare-sparks-urgent-bessent-powell-warning-to-bank-ceos
- https://www.cnbc.com/2026/04/10/powell-bessent-us-bank-ceos-anthropic-mythos-ai-cyber.html

### 2. Claude Code v2.1.101 連続リリース + CoreWeave契約 + 自社チップ検討 — Anthropicが「ARR $30B」側から見えるインフラ固め

**事実**: Claude Code v2.1.98の翌日にv2.1.101がリリース（4/10）。`/team-onboarding`（チーム向けランプアップガイド自動生成）、`/ultraplan`とリモートセッション機能（クラウド環境自動作成）、OS CA証明書ストアのデフォルト信頼（企業TLSプロキシ対応）、POSIX `which` 経由のコマンドインジェクション脆弱性修正を含む。同日、CoreWeaveがAnthropicと複数年GPU契約を発表し株価は13%急騰、Anthropicの年間ランレート売上は$30Bを突破（2025年末$9Bから3倍超）。さらにReutersは、AnthropicがMeta/OpenAIに追随する形で独自AIチップ設計を初期段階で検討中と報道（開発費最大$500M規模、専任チーム未編成）。

**根拠**: v2.1.98→v2.1.101まで4日で4バージョン刻みは異例のペースで、4日連続でセキュリティ修正（Bash toolパーミッションバイパス、POSIX whichインジェクション）が続いている。CoreWeave契約で上位10社中9社のAIモデルプロバイダがCoreWeave基盤を利用する構図となり、NVIDIA依存からの脱却圧力とインフラ枠取り競争の両方を示す。$30B ARRは2025年末の3倍超で、エンタープライズClaude採用とClaude Codeの急成長が明確に牽引。

**影響**: Claude Codeを業務利用しているユーザーにとって、セキュリティ修正未適用のまま放置するリスクが日毎に増している。エンタープライズTLSプロキシ環境での接続問題は追加設定なしで解消される可能性が高い。インフラ側ではAnthropicの供給制約が緩和される方向のシグナルで、中期的には料金・レート制限の追加引き締め圧力が下がる。

**行動指針**: Claude Codeは **即時v2.1.101以降にアップデート**（セキュリティ修正7件相当）。`CLAUDE_CODE_CERT_STORE=bundled` で従来挙動に戻せる点は企業TLSプロキシ問題があった場合のみ覚えておく。`/team-onboarding`はチーム導入時に有用だが、個人利用では当面不要。自社チップ検討は報道段階のため経過観察で十分、Anthropic長期契約への影響が出るのは早くて2027年。

- https://code.claude.com/docs/en/changelog
- https://www.coreweave.com/news/coreweave-announces-multi-year-agreement-with-anthropic
- https://www.cnbc.com/2026/04/10/coreweave-anthropic-claude-ai-deal.html
- https://www.benzinga.com/markets/tech/26/04/51748158/anthropic-eyes-custom-ai-chips-amid-global-shortage-as-claude-demand-surges-past-30-billion-run-rate

### 3. M365 Copilot Researcher Critique Mode — OpenAI生成＋Anthropic検証の二段階構成

**事実**: Microsoft 365 Copilot ResearcherエージェントにCritique Modeが追加。OpenAI GPTが下書きを生成し、Anthropic Claudeが正確性・網羅性・引用品質をレビューして最終化する二段階構成で、Microsoftの「マルチモデル戦略」の第一弾。同時にResearcher Council（複数モデルの並列実行で合意・対立を可視化）も追加、PowerPoint/PDF/インフォグラフィック/音声概要の新出力フォーマットが4月中旬〜下旬に展開予定。

**根拠**: これまでMicrosoftはCopilotの裏側モデルを非公開または不明瞭にしてきた経緯があるが、今回は「OpenAI GPTで生成→Anthropic Claudeでレビュー」と明示的にクロスモデル構成を打ち出している。4/10の GitHub Copilot CLI Rubber Duck（Sonnet単体とOpus単体の性能差の74.7%を埋める）と同じ思想で、単一モデルの限界をクロスモデルレビューで埋める設計が企業AIツールの主流になりつつある。

**影響**: Copilot Researcherで生成した調査レポートの信頼性が単一モデル構成より一段上がる一方、処理時間と課金は増える可能性がある。Microsoft側の「マルチモデル」宣言はOpenAI単独依存からの明確な距離取りでもあり、Copilotの料金・モデル選択肢に今後影響する。

**行動指針**: M365 Copilot Researcherを業務で使っている場合、Critique Modeをデフォルトに設定し、数回の出力で従来モードとの品質・速度差を比較する。クロスモデルレビューの設計思想は自前でも再現可能（1stプロンプトでClaudeに書かせ、2ndプロンプトでGPT-5に検証させる等）なので、Researcher Council相当の使い方を試すのはローコストで価値が高い。一方で新出力フォーマット（音声概要等）は慌てて触る必要はなく、自分の業務で必要になったときで十分。

- https://dataconomy.com/2026/04/02/microsoft-upgrades-365-copilot-researcher-with-new-critique-mode/
- https://www.geekwire.com/2026/microsoft-365-copilot-and-the-end-of-the-single-model-era-in-enterprise-ai/

---

## カテゴリ別まとめ

### Anthropic / Claude

- **Mythos/Project Glasswing 金融業界緊急会合（4/10）**: 米財務長官Bessent・FRB議長Powellが6大銀行CEOを招集し緊急警告。Mythosは主要OS・ブラウザで数千件の高深刻度脆弱性を自律発見。最大$100Mクレジット＋$4Mオープンソース寄付。AWS/Apple/Google/Microsoft/NVIDIA等11社参加
  - https://www.bloomberg.com/news/articles/2026-04-10/anthropic-model-scare-sparks-urgent-bessent-powell-warning-to-bank-ceos
  - https://www.cnbc.com/2026/04/10/powell-bessent-us-bank-ceos-anthropic-mythos-ai-cyber.html

- **Claude Code v2.1.101（4/10）**: v2.1.98の翌日にマイナーアップデート。`/team-onboarding`、`/ultraplan`とリモートセッション機能、OS CA証明書ストアのデフォルト信頼、POSIX `which` コマンドインジェクション脆弱性修正、長時間セッションメモリリーク修正、`--resume`コンテキスト喪失修正
  - https://code.claude.com/docs/en/changelog

- **Claude Code v2.1.99〜v2.1.100 補足**: `/powerup`（機能解説レッスン）、`.husky`保護ディレクトリ追加、LSP拡張（clientInfo自己識別）、レート制限ダイアログ無限ループ修正。v2.1.98以降、起動時に空ファイル17個以上生成される既知バグが一部環境で継続報告中
  - https://github.com/anthropics/claude-code/releases

- **CoreWeave × Anthropic 複数年GPU契約（4/10）**: Nvidia GPUキャパシティ提供。CoreWeave株13%急騰、上位10社中9社のAIプロバイダがCoreWeave基盤を利用する構図に。Anthropic ARRは$30B突破（2025年末$9Bの3倍超）
  - https://www.coreweave.com/news/coreweave-announces-multi-year-agreement-with-anthropic
  - https://www.bloomberg.com/news/articles/2026-04-10/anthropic-agrees-to-rent-coreweave-ai-capacity-to-power-claude
  - https://www.cnbc.com/2026/04/10/coreweave-anthropic-claude-ai-deal.html

- **Anthropic 独自AIチップ検討（4/10報道）**: Reutersスクープ。初期段階、専任チーム未編成。Google TPU/Amazon Trainium利用継続、4月初旬にGoogle/Broadcomと3.5GW TPU長期契約済み（2027年稼働）。開発費最大$500M規模
  - https://www.cnbc.com/2026/04/10/anthropic-weighs-building-its-own-ai-chips-reuters.html
  - https://techbriefly.com/2026/04/10/anthropic-explores-custom-ai-chip-design-to-power-claude-models/

### Microsoft / Copilot

- **M365 Copilot Notebooks Overview Page（MC1275564、4/10）**: Notebook内の全参照資料を横断要約しワンクリック更新。3カラムレイアウト刷新（参照資料／Copilot Pages／Copilot chat）。参照可能資料をWord/PPT/Excel/OneNote/PDF/Copilot Pagesに拡大
  - https://mwpro.co.uk/blog/2026/04/10/microsoft-365-copilot-updated-copilot-notebooks-overview-page-experience-mc1275564/
  - https://techcommunity.microsoft.com/blog/microsoft365copilotblog/meet-the-updated-copilot-notebooks-experience-your-home-for-understanding-work-p/4501383

- **M365 Copilot Researcher Critique Mode + Researcher Council**: OpenAI GPTで生成→Anthropic Claudeで検証の二段階構成。複数モデル並列実行で合意・対立を可視化。PowerPoint/PDF/インフォグラフィック/音声概要の新出力フォーマットを4月中旬〜下旬展開
  - https://dataconomy.com/2026/04/02/microsoft-upgrades-365-copilot-researcher-with-new-critique-mode/
  - https://www.geekwire.com/2026/microsoft-365-copilot-and-the-end-of-the-single-model-era-in-enterprise-ai/

- **Security Copilot M365 E5組み込み（MC1261596、4/20〜6/30段階展開）**: E5顧客は追加コストなしで1,000ライセンスあたり毎月400 SCU（最大10,000 SCU）自動付与。Defender/Entra/Intune/Purview統合のAI脅威分析・インシデント要約。テナントはアクティベーション7日前と当日に通知、ゼロクリックで有効化
  - https://mc.merill.net/message/MC1261596
  - https://www.microsoft.com/en-us/security/security-copilot-in-microsoft-365-e5

- **Power Automate Process License Capacity共有 4/21 GA**: 最大25個のクラウドフロー間でキャパシティをプール可能に。Windows 365コネクタもPower Platform/Azure Logic Apps向けPublic Preview（4/2）、Cloud PC管理自動化
  - https://learn.microsoft.com/en-us/power-platform/release-plan/2026wave1/power-automate/
  - https://4sysops.com/archives/windows-365-connector-for-power-platform-and-logic-apps-automate-cloud-pc-management/

- **M365 Community Conference 4/21-23（Orlando）全キーノート判明**: 5基調講演＋Ask Microsoft Anything 1本＋200+セッション。Ryan Cunningham基調講演で「M365 Copilot / Copilot Studio / Power Apps / Agent 365」統合ストーリー。クロージングは「From Momentum to Movement」（4/23 15:15-16:15）
  - https://techcommunity.microsoft.com/blog/microsoft_365blog/announcing-the-2026-microsoft-365-community-conference-keynotes/4494714

### OpenAI

- **ChatGPT $100/月 Proプラン新設（4/9-10）**: 既存$20 Plusと$200 Proの中間。Codex利用上限はPlusの5倍、Instant/Thinkingモデルは$200プラン同等。AnthropicのClaude Max $100プランへの対抗策。OpenAIはCodex利用量が前月比70%超成長と明かす
  - https://techcrunch.com/2026/04/09/chatgpt-pro-plan-100-month-codex/
  - https://www.cnbc.com/2026/04/09/openai-chatgpt-pro-subscription-anthropic-claude-code.html

- **広告収入2030年$100B計画（Axios報道4/9）**: 2026年 $2.5B → 2027年 $11B → 2028年 $25B → 2029年 $53B → 2030年 $100B。前提は2030年までにWAU 27.5億人到達。Smartly経由のChatGPT広告パイロットは既に年率$100M水準
  - https://www.axios.com/2026/04/09/openai-100-billion-in-ad-revenue
  - https://thetechportal.com/2026/04/09/openai-projects-100bn-in-ad-revenue-by-2030-around-2-5bn-in-2026-report

### Google

- **Workspace Guest Accounts ロールアウト完了（4/10）**: 非Workspaceユーザーとの安全なChatコラボ。Scheduled Releaseドメインへの展開完了。Business Starter〜Enterprise Plus全プラン対象
  - https://workspaceupdates.googleblog.com/

- **Workspace 個人購入 AI Expanded Access アドオン（4/7〜）**: エンドユーザーがアプリ内プロンプトから直接自費購入可能。Geminiアプリ/NotebookLMの上限拡張、Google VidsのVeo 3/Avatar作成など。米加のBusiness版から開始
  - https://workspaceupdates.googleblog.com/2026/04/enabling-user-initiated-purchases.html

- **Gemini Temporary Chat + Labs新機能**: 履歴・Apps Activity・モデル訓練に残らないプライベートチャット。Labsでvisual layout / dynamic viewの2実験機能追加
  - https://gemini.google/release-notes/

- **Intel × Google Cloud 複数年AI契約（4/9）**: 複数世代のXeon CPUをグローバルデータセンター導入、AIワークロードの前処理・オーケストレーション・推論担当。IntelのIPUをGoogleがカスタマイズしネットワーク/セキュリティ/ストレージ処理。GPU偏重論に「CPU+IPU」で対抗
  - https://newsroom.intel.com/data-center/intel-google-deepen-collaboration-to-advance-ai-infrastructure
  - https://techcrunch.com/2026/04/09/google-and-intel-deepen-ai-infrastructure-partnership/

### モデル・動画生成

- **Alibaba HappyHorse-1.0 出自公表（4/10）**: ATH Future Life Lab（元Kuaishou/Kling AI技術責任者Zhang Di氏率いる）が開発。匿名でArtificial Analysisのtext-to-video / image-to-videoベンチマークでByteDance Seedance 2.0等を抜き首位獲得済み。15Bパラメータ単一ストリーム統合Transformerで音声+動画1パス同時生成。API提供4/30予定、重み含む完全オープンソース化も予告
  - https://www.bloomberg.com/news/articles/2026-04-10/stealth-alibaba-video-ai-model-tops-global-ranking-on-debut
  - https://www.cnbc.com/2026/04/10/alibaba-happyhorse-ai-video-model-benchmark-reveal.html

### エンタープライズAI / 開発者ツール

- **Perplexity「Computer for Enterprise」発表**: Ask 2026開発者カンファレンスで発表。Snowflake / Datadog / Salesforce / SharePoint / HubSpotコネクタ追加（既存100+連携に追加）。Slack内で`@computer`直接呼び出し可。法務契約レビュー・財務監査・セールスコール準備・サポートチケットトリアージのテンプレート同梱。SSO/SAML・SCIM・監査ログ・SOC 2 Type II取得。週末に100社超がエンタープライズ版要請
  - https://venturebeat.com/technology/perplexity-takes-its-computer-ai-agent-into-the-enterprise-taking-aim-at
  - https://www.pymnts.com/news/artificial-intelligence/2026/perplexity-computer-enterprise-completed-3-years-work-4-weeks/

- **GitHub Copilot SDK パブリックプレビュー（4/2）**: Copilotのエージェント機能を自社アプリ・ワークフローに埋込。Node.js / Python / Go / .NET対応、OpenTelemetry分散トレース、読み取り専用ツール識別の権限フレームワーク、OpenAI / Microsoft Foundry / Anthropic BYOK対応。Copilot Free / 非Copilotサブスクユーザーにも開放
  - https://github.blog/changelog/2026-04-02-copilot-sdk-in-public-preview/
  - https://www.publickey1.jp/blog/26/github_copilot_cliaigithub_copilot_sdk.html

---

## 直近の注目予定

| 日付 | イベント |
|------|---------|
| 4/13 | Stanford HAI AI Index 2026 詳細解説イベント |
| 4/15 | Copilot Chat仕様変更発効 / Power Platform & Copilot Studio アップデートイベント（9AM PDT） |
| 4/17 | Anthropic OpenClaw 移行クレジット期限 |
| 4/19 | Claude Haiku 3 非推奨（リタイア） |
| 4/20 | Security Copilot for M365 E5 段階展開開始（〜6/30） |
| 4/21 | Power Automate Process License共有 GA |
| 4/21-23 | M365 Community Conference（Orlando） |
| 4/23 | Google Drive限定アクセス自動移行開始 |
| 4/30 | Alibaba HappyHorse-1.0 API提供開始予定 |
| 4/30 | 1Mコンテキストベータ終了（Sonnet 4.5 / Sonnet 4向け） |
| 5/1 | M365 E7 Frontier Suite GA / Agent 365 GA |

---

## 改善メモ

### Master
- [Claude Code Changelog] WebFetch成功（4/11）— 安定して唯一WebFetchが動くソース
- [Anthropic Blog] WebFetch 403 → WebSearch成功（4/11）
- [OpenAI News RSS] WebFetch 403 → WebSearch成功（4/11）
- [Cursor Changelog] WebFetch 403 → WebSearch成功（4/11）— 4/8のBugbot以降、新エントリなし
- [Devin Release Notes] WebFetch 403 → WebSearch成功（4/11）— 4/3以降、新エントリなし
- [Google Workspace] WebSearch成功（4/11）
- 4日連続でClaude Code以外のほぼ全ソースが403。WebSearchがプライマリ手段として完全に定着。`daily-sources.md` の取得方法欄を「WebSearch → WebFetch（稀に成功時）」の順に入れ替える改訂を検討推奨
- [Anthropic Mythos/Project Glasswing] 今週最大のニュース。監視対象として `.anthropic.com/glasswing` を daily-sources.md に追加を推奨
- [CoreWeave] AIインフラ契約の重要性が増しており、CoreWeave投資家向けリリースページをソースに追加検討（https://investors.coreweave.com/news/）

### Copilot
- [Copilot Studio What's New] WebFetch 403継続（9日連続）。WebSearch経由で取得
- [M365 Copilot Release Notes] WebFetch 403継続。WebSearch経由で取得
- [mc.merill.net] WebFetch 403継続。WebSearch経由で取得（mwpro.co.uk も同様に403）
- learn.microsoft.com 配下全般で403が継続しており、ほぼ全ソースでWebSearchがプライマリ手段になっている。`daily-sources.md` 側に「現状WebSearchをプライマリとして扱う」旨の注記追加を推奨
- Anthropic関連ニュースの速報性向上のため、`ai-tools-sources.md`（未作成）の整備を推奨。現状 `ai-tools.md`（interests）のみでソース一覧が散在

### Industry
- 全RSSフィード（Google News / GIGAZINE / The Decoder / VentureBeat AI / Publickey Atom / hnrss.org / Product Hunt / GitHub Trending）の403が5日以上連続。`daily-sources.md` の各ソース「取得方法」欄の先頭を `WebSearch` に変更することを**強く推奨**（5回目の提案）
  - 失敗URL: 全RSSエンドポイント
  - ステータスコード: 403
  - 成功した方法: WebSearch フリーワード
  - 日時: 2026-04-11
- JST 2026-04-11 時点で main ブランチの先端は 2026-04-10 ダイジェスト。前回ワークフローで発生した detached HEAD 状態は、4/10コミット（`49f5f49`）が正常に push 済みであることを確認。日次自動化の冒頭に `git checkout main && git pull --ff-only origin main` を明示的に入れるルール化を推奨
- Stanford HAI AI Index 2026 は4/13に詳細解説イベント予定。13日以降のダイジェストで重点反映
