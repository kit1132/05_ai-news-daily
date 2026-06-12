# AI News Daily Summary - 2026-04-06

## 今日のハイライト

### 1. Copilot Cowork が Frontier プログラムで公開 — Microsoft×Anthropic $30B提携が具体化し、Claudeが M365 の自律エージェント基盤に

**事実**: Microsoft 365 Copilot 内で長時間・複数ステップの業務を自律実行する「Copilot Cowork」が Frontier プログラムで利用可能になった（3/30〜）。基盤にはAnthropic Claudeのエージェント技術を採用。Microsoft と Anthropic の $30B 提携に基づき、Claude が OpenAI モデルと並んでサブプロセッサとして機能する。

**根拠**: ユーザーが目的を記述するとCoworkが計画を生成し、メール・会議・メッセージ・ファイル・データを横断して作業を遂行する。カレンダー管理、デイリーブリーフィング、月次予算レビュー等のスキルが組み込み済み。Microsoftが自社のCopilotエコシステムに、OpenAI以外のモデルプロバイダーを正式に組み込んだ初の大型事例。

**影響**: M365 Copilot ライセンス保有企業にとって、エージェント型自動化の実用レベルが一段上がった。同時に、MicrosoftがOpenAI一社依存から脱却しマルチモデル戦略を明確化したことで、今後のCopilot機能がどのモデルで動くかはユーザーから見えにくくなる。Anthropic側にとっては、M365の数億ユーザーベースへの間接的なリーチを獲得した意味が大きい。

**行動指針**: M365 Copilotライセンス保有組織は、Frontier プレビュープログラムへの参加可否を確認する。未導入の場合は経過観察でよいが、Copilot Coworkの自律実行範囲（メール・ファイル・データ横断）に対するガバナンスポリシーの検討は先行して始めておくべき。

- https://www.microsoft.com/en-us/microsoft-365/blog/2026/03/30/copilot-cowork-now-available-in-frontier/

### 2. OpenAI、エージェント基盤を一気に拡張 — Responses API にシェルツール・コンテナ環境、Codex CLI は 1,000+ TPS の GPT-5.3-Codex-Spark 搭載

**事実**: OpenAI の Responses API にシェルツール（Debian 12ベースの完全ターミナル）、エージェント実行ループ、ホステッドコンテナワークスペース、コンテキスト圧縮（compaction）、再利用可能なエージェントスキルが追加された。Codex CLI は Windows Sandbox 対応と、GPT-5.3-Codex-Spark モデルによる 1,000+ TPS の高速推論を実現。

**根拠**: シェルツールは従来の Code Interpreter と異なり Python/Node.js/Java/Go 等が利用可能な完全ターミナル環境。サブエージェントはパスベースアドレス（`/root/agent_a`）で構造化メッセージングに対応し、マルチエージェント構成が公式にサポートされた。1,000+ TPS は現行の主要モデルの出力速度を大幅に上回り、対話的なコーディングエージェントのレスポンスが体感レベルで変わる水準。

**影響**: OpenAI のエージェント構築基盤が、Claude Code やDevin 等の専用ツールに近い機能セットを API レベルで提供し始めた。開発者は OpenAI API 上で「コードを書いて実行して検証する」一連のループを完結できるようになり、サードパーティツールへの依存度が下がる可能性がある。

**行動指針**: OpenAI API でエージェントを構築中、または検討中の場合、Responses API のシェルツールとコンテナワークスペースを評価対象に追加する。Claude Code / Devin 等を既に使っている場合は、機能重複と価格差を比較した上で切替判断。Codex CLI の GPT-5.3-Codex-Spark は速度重視のユースケース（対話的コード生成、CI/CD連携）で試す価値がある。

- https://www.infoq.com/news/2026/03/openai-responses-api-agents/
- https://daily1bite.com/en/blog/ai-tools/openai-codex-cli-april-2026-update

### 3. Google Gemma 4 + Microsoft MAI + Gemini 3.1 Flash Live — モデル競争が全方位で加速し、選択肢の質が底上げされた週

**事実**: Google が Gemma 4 ファミリー（E2B/E4B/26B MoE/31B Dense）を Apache 2.0 で公開（4/2）。Microsoft は自社開発 MAI シリーズ3種（音声認識・音声生成・画像生成）を Foundry 経由でリリース（4/2）。Google はさらに Gemini 3.1 Flash Live をリリースし、リアルタイム音声会話の品質を大幅向上（90言語以上対応、会話コンテキスト保持2倍、環境音識別強化）。

**根拠**: Gemma 4 は Gemini 3 ベースでネイティブ動画・画像処理とエージェント最適化が特徴。E2B/E4B はエッジデバイス向けで音声入力にも対応。MAI-Transcribe は既存 Azure 比 2.5 倍速・$0.36/時間。Gemini 3.1 Flash Live はリアルタイム音声の実用性を引き上げ、音響認識（ピッチ・テンポ変化検知）にも対応した。1週間で Google 2件・Microsoft 1件の主要モデルリリースが重なった。

**影響**: オープンモデル（Gemma 4）、クラウドAPI（MAI・Gemini Flash Live）の両面で選択肢の質が上がった。エッジ/オンプレ展開には Gemma 4、Azure 環境の音声処理コスト削減には MAI-Transcribe、リアルタイム音声対話には Gemini Flash Live と、ユースケース別に最適解が分かれる。

**行動指針**: エッジ/オンプレ LLM を検討中なら Gemma 4 の E2B/E4B を評価対象に追加。Azure で音声認識を使っているなら MAI-Transcribe（$0.36/時間）と現行コストを比較。リアルタイム音声対話を組み込みたい場合は Gemini 3.1 Flash Live の API を検証。いずれも即日利用可能。

- https://blog.google/innovation-and-ai/technology/developers-tools/gemma-4/
- https://venturebeat.com/technology/microsoft-launches-3-new-ai-models-in-direct-shot-at-openai-and-google
- https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-1-flash-live/

---

## カテゴリ別まとめ

### 資金調達・M&A

- **OpenAI、$122B 資金調達を完了（3/31）**: 評価額 $852B。SoftBank・a16z 共同リード。年間売上 $25B 突破、2026年後半の IPO も視野に
  - https://openai.com/index/accelerating-the-next-phase-ai/
  - https://techcrunch.com/2026/03/31/openai-not-yet-public-raises-3b-from-retail-investors-in-monster-122b-fund-raise/

- **Anthropic、AI 創薬 Coefficient Bio を約$400M で買収**: 設立8ヶ月・従業員10人未満。Genentech 出身の創業者がタンパク質設計の専門知識を持ちヘルスケア部門に合流
  - https://techcrunch.com/2026/04/03/anthropic-buys-biotech-startup-coefficient-bio-in-400m-deal-reports/

### OpenAI

- **Responses API にエージェント機能を大幅拡張**: シェルツール（Debian 12 完全ターミナル）、エージェント実行ループ、ホステッドコンテナ、コンテキスト圧縮、再利用可能スキル。サブエージェントのパスベースアドレス対応
  - https://www.infoq.com/news/2026/03/openai-responses-api-agents/

- **Codex CLI アップデート — Windows Sandbox 対応、GPT-5.3-Codex-Spark**: 1,000+ TPS の高速推論。ファーストクラスプラグイン、マルチエージェントワークフロー改善
  - https://daily1bite.com/en/blog/ai-tools/openai-codex-cli-april-2026-update

- **ChatGPT モバイル UI 刷新**: サイドバー簡素化、位置情報共有によるローカル対応、10代向けペアレンタルコントロール追加
  - https://help.openai.com/en/articles/6825453-chatgpt-release-notes

### Google

- **Gemma 4 ファミリーリリース（4/2）**: Gemini 3 ベース、Apache 2.0。E2B/E4B（エッジ）・26B MoE・31B Dense。動画・画像ネイティブ対応、エージェント最適化
  - https://blog.google/innovation-and-ai/technology/developers-tools/gemma-4/

- **Gemini 3.1 Flash Live リリース**: リアルタイム音声会話の大幅向上。会話コンテキスト保持2倍、音響認識（ピッチ・テンポ変化検知）、90言語以上対応
  - https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-1-flash-live/

- **Gemini にチャット履歴インポート機能**: ChatGPT・Claude からの履歴を直接インポート可能に
  - https://blog.mean.ceo/google-gemini-latest-model-news-april-2026/

- **Google Vids — Lyria 3 によるカスタム音楽生成対応**: 動画のトーンに合わせた AI 楽曲を自動生成。2D/3D カートゥーンアバターも追加
  - https://workspaceupdates.googleblog.com/2026/

### Microsoft 365 Copilot / Copilot Studio

- **Copilot Cowork が Frontier プログラムで公開（3/30〜）**: Anthropic Claude ベースの自律エージェント。メール・会議・ファイル横断で業務を自動遂行
  - https://www.microsoft.com/en-us/microsoft-365/blog/2026/03/30/copilot-cowork-now-available-in-frontier/

- **Copilot Chat モデルセレクターに GPT-5.2 追加**: Quick Response（即時回答）と Think Deeper（深い推論）の2モード提供
  - https://support.microsoft.com/en-us/topic/latest-updates-for-microsoft-365-copilot-a5685141-8081-458c-80d6-42493aad51ed

- **M365 Copilot モバイルアプリ刷新（4月下旬〜パブリックプレビュー）**: チャットファースト設計にリデザイン。GA は8月下旬完了予定
  - https://m365admin.handsontek.net/microsoft-365-copilot-new-chat-first-design-copilot-mobile-app/

- **Copilot Analytics に新メトリクス追加（4月下旬〜）**: Edge/OneNote/Outlook/Word/Excel/PowerPoint の利用状況が Dashboard に追加
  - https://m365admin.handsontek.net/microsoft-365-copilot-comprehensive-copilot-metrics-copilot-analytics/

- **Copilot Chat 仕様変更（4/15）まであと9日**: Word/Excel/PowerPoint/OneNote での Copilot Chat が M365 Copilot 有料ライセンス専用に
  - https://blogs.imperial.ac.uk/office365/2026/03/20/copilot-chat-changes-april-2026/

- **Viva Glint に AI 生成ハイライト（4月〜）**: 調査レポートに AI サマリ・インサイトを自動追加
  - https://mc.merill.net/message/MC1247887

- **Microsoft MAI シリーズ3種公開（4/2）**: MAI-Transcribe-1（音声認識・25言語・$0.36/時間）、MAI-Voice-1（音声生成・$22/100万文字）、MAI-Image-2（画像生成）
  - https://venturebeat.com/technology/microsoft-launches-3-new-ai-models-in-direct-shot-at-openai-and-google

### Claude Code / Anthropic

- **Claude Code 継続アップデート**: MCP 結果の大容量永続化、スキル・コマンドのインラインシェル実行無効化、マルチラインディープリンク対応、プラグインの bin ディレクトリ同梱対応、大容量ファイル書き込み高速化
  - https://releasebot.io/updates/anthropic/claude-code

- **Claude Code ソースコード誤公開**: 約1,900ファイル・51.2万行が流出。リリースパッケージングの人的ミス。顧客データ・認証情報の漏洩はなし
  - https://www.bloomberg.com/news/articles/2026-04-01/anthropic-executive-blames-claude-code-leak-on-process-errors

- **サードパーティツールでの Claude Pro/Max サブスク利用停止（4/4）**: API 課金または従量課金アドオンへの移行が必要。4/17 までの一回限りクレジット付与、事前購入で最大30%割引
  - https://www.indexbox.io/blog/anthropic-changes-claude-code-subscription-for-third-party-tools-in-2026/
  - https://thetechportal.com/2026/04/05/anthropic-removes-openclaw-from-claude-plans-adds-extra-charges-for-use

### プラットフォーム・ツール動向

- **Salesforce、Slack に30の新 AI 機能を追加**: Slackbot が MCP クライアントとしてエージェント化。一部社員は1日90分の時間節約を報告
  - https://techcrunch.com/2026/03/31/salesforce-announces-an-ai-heavy-makeover-for-slack-with-30-new-features/

- **GitHub Copilot、Free/Pro ユーザーのデータをモデル訓練に使用へ（4/24発効）**: Business/Enterprise は対象外。オプトアウト済み設定は維持
  - https://github.blog/news-insights/company-news/updates-to-github-copilot-interaction-data-usage-policy/

- **Apple、ARM Mac 向け Nvidia/AMD eGPU ドライバーを正式承認**: TinyGPU ドライバー。SIP 無効化不要、Thunderbolt/USB4 経由。コンピュート専用（ディスプレイ出力非対応）
  - https://appleinsider.com/articles/26/04/04/amd-or-nvidia-egpus-can-work-on-apple-silicon-macs-but-not-for-graphic-acceleration

### 開発ツール・エージェント

- **JetBrains Central — AI コーディングエージェント管理プラットフォーム**: エージェント駆動型開発の制御プレーン。Q2 2026 に早期アクセス開始予定
  - https://www.infoworld.com/article/4149535/new-jetbrains-platform-manages-ai-coding-agents.html

- **Codenotary AgentMon — AI エージェント監視ツール**: エージェントの行動・ファイルアクセス・データパターンを横断的にモニタリング
  - https://devops.com/devins-latest-update-brings-major-enterprise-features-and-developer-improvements/

### 市場データ・調査

- **AI データセンター建設計画の半数が延期・取消見込み**: 2026年稼働予定の実際の建設中は3分の1未満。チップ・変圧器・バッテリー不足が主因
  - https://gigazine.net/news/20260404-ai-data-center-delayed-canceled/

- **IDC: エージェンティック AI 支出、2029年に$1.3T**: AI 関連 IT 支出は年平均31.9%成長、2029年には IT 支出全体の26%超
  - https://my.idc.com/getdoc.jsp?containerId=prUS53765225

---

## 直近の注目予定

- **4/13**: Stanford HAI AI Index 2026年版 公開
- **4/15**: Copilot Chat 仕様変更（Basic/Premium 二層化）
- **4/15**: Power Platform & Copilot Studio アップデートイベント（マルチエージェントオーケストレーション GA 等）
- **4/17**: Anthropic OpenClaw 移行クレジット期限
- **4/20**: Teams Pre-Day（Orlando）
- **4/20〜**: Security Copilot M365 E5 自動有効化開始
- **4/21-23**: Microsoft 365 Community Conference（Orlando）
- **4/24**: GitHub Copilot Free/Pro データ学習利用開始
- **4/30**: Claude 1M コンテキストベータ終了（Sonnet 4.5/4）
- **5/1**: M365 E7 Frontier Suite GA / Agent 365 GA

---

## 改善メモ

### 01_ai-news-Master
- 全12ソース中11ソースで WebFetch 403。WebSearch フォールバックで取得成功
- 403発生率が非常に高い状態が継続。daily-sources.md の取得方法を WebSearch 優先に変更することを強く推奨

### 02_ai-news-Copilot
- learn.microsoft.com 配下で WebFetch 403 継続（4日連続）。daily-sources.md の「Cloudflare未使用のため WebFetch が安定する傾向」記載と乖離 → 取得方法を WebSearch に更新推奨
- mc.merill.net / releasebot.io: WebFetch 403 → WebSearch 経由で取得成功

### 03_ai-news-industry
- 全 RSS ソースが 403 を返却（Google News RSS・GIGAZINE・The Decoder・VentureBeat・Publickey・Hacker News・Product Hunt・GitHub Trending）
- WebSearch フォールバックが安定して機能。WebSearch 主体の取得フローを推奨

### 共通
- 3ソース横断で WebFetch の 403 率が極めて高い状態が数日間継続。WebFetch → WebSearch のフォールバック順序を全ソースで逆転させる（WebSearch をプライマリ化する）ことを検討すべき段階
