# AI News Daily Summary — 2026-10-30

Microsoft は Power Automate の「Describe it to design it」を 11/30 に退役させ、説明文からフローを作る入口を AI アシスタントのプラグインへ移す。OpenAI は ChatGPT Pro / Business の契約者に、API 組織をつなぐと毎月最大 $500 の API クレジットを付け始めた。Microsoft は Copilot Studio のコスト管理を、環境ごとに M365 管理センターの Cost Management へ移せるようにする（11/20 までに GA）。Anthropic は Usage and Cost Analytics API を beta で出し、Mistral は Large 4 の重みを公開した。

## 今日のハイライト

### 1. [廃止] Power Automate の「Describe it to design it」が 11/30 に退役する — 説明文からフローを作る入口が、Power Automate の画面から AI アシスタントのプラグインへ移る

**要点**: 11/30 以降、メーカーは Describe it to design it で新しいクラウドフローを作れなくなる。既存のフローは消えない。説明文から作りたい場合は、組織が承認した AI アシスタント（GitHub Copilot など）の Power Automate プラグインを使うよう Microsoft は案内している。

**詳細**: Power Platform の非推奨一覧（`important-changes-coming`）が 10/29 19:04Z に `5a32b903`（`ms.date` 10/28）へ改訂され、この節が先頭に加わった。前回の `21682266`（`ms.date` 10/6）には無かった。

- 対象: すべての顧客。ビジュアルデザイナーでの作成・編集とテンプレートからの作成は引き続き使える
- 求められる対応: メーカーに周知し、Describe it to design it を勧めている社内ガイドを書き換える
- 退役まで31日。研修資料で Power Automate の Copilot によるフロー作成を扱っている場合は、手順の差し替えが要る

- https://learn.microsoft.com/en-us/power-platform/important-changes-coming

### 2. [料金] OpenAI が ChatGPT Pro / Business の契約者に、月最大 $500 の API クレジットを付け始めた — 「ChatGPT の席と API の従量は別々に払う」前提が、席の契約に API の月次枠が付く前提に変わる

**要点**: OpenAI が 10/28 に、ChatGPT Pro と Business の契約者が自分の API 組織をリンクすると、毎月最大 $500 の API クレジットを受け取れるようにした。枠は月ごとに失効し、繰り越せない。小規模な API 検証は既存の ChatGPT 契約の範囲で賄えるようになった。

**詳細**: 一次は OpenAI API changelog（10/28）・解説ガイド・公式フォーラム。

- 付与額（月額・上限 $500）
  - Pro: $100 プランは $100、$200 プランは $200、$500 プランは $500
  - Business: Standard 席1つにつき $20、Premium 席1つにつき $100 をワークスペースでプール（上限 $500/月、年払いは年 $6,000）
- 使える範囲: Responses API・Agents API（OpenAI ホストのサンドボックス料金を含む）・Decisions API・Realtime API・Images API と、組み込みツールの利用料・保存料。**API キー経由の Codex は対象外**で、ChatGPT やサインイン版 Codex の利用枠も増えない
- 条件: 有効な有料契約で開始から7日以上。ChatGPT 契約と API 組織の両方を本人が所有し、同じメールアドレスであること。Enterprise・Plus・Go・Free は対象外。初回は残り日数で按分する
- 手順: `chatgpt.com/settings/billing` で請求し、ChatGPT または Codex の「OpenAI Developers」プラグインで API キーを作る
- Anthropic は 10/7 に Max / Team へ月次 API クレジットを付けており、席に API 枠を付ける形が2社に揃った

- https://developers.openai.com/api/docs/changelog
- https://developers.openai.com/api/docs/guides/chatgpt-api-credits
- https://community.openai.com/t/claim-up-to-500-in-api-credits-using-your-chatgpt-pro-or-business-subscription

### 3. [予定] Copilot Studio のコスト管理を、M365 管理センターの Cost Management へ環境ごとに移せるようになる — 移した環境の新しい利用状況は PPAC に出なくなる

**要点**: MC1530368 によると、管理者は 11/20 までに、Copilot Studio の環境やエージェントに M365 管理センターのスペンディングポリシーを掛けられるようになる。移行は任意で環境ごとに選ぶ。移した環境の新しい利用データは M365 管理センターにだけ出て、PPAC の利用レポートには出なくなる。

**詳細**: Message Center（10/29 公開・Power Platform・New feature）による。GA は 2026-11-20 まで。

- 適用単位: 環境単位またはエージェント単位でポリシーを掛けられ、対応する全環境にまとめて掛けることもできる
- 既定の扱い: 既存の環境は自動では移らない。移さない環境は PPAC の既存のコスト統制をそのまま使う
- 移行後: M365 管理センターのスペンディングポリシーが有効なコスト統制になる。移行前の利用データは PPAC に残り、コスト以外の Copilot Studio の管理は PPAC のまま
- 表示通貨: Cost Management とエージェントレジストリは、費用を組織の現地通貨で表示する
- 対象の管理者: AI 管理者・グローバル管理者、Power Platform 管理者、課金・コスト管理者。影響範囲には Agent Builder と Copilot Credits も含まれる

- https://mc.merill.net/message/MC1530368

## カテゴリ別まとめ

### Copilot Studio / Power Platform

- **Power Automate の Describe it to design it の退役**（ハイライト1参照）
- **Copilot Studio のコスト管理の M365 管理センター移行**（ハイライト3参照）
- [新機能] **エージェントのメーカー間共有** — メーカーが、Roadmap 569475 により、Microsoft Copilot ハーネス（旧 GitHub Copilot ハーネス）のエージェントを、他のメーカーに Agent Viewer（分析・評価の閲覧のみ）または Editor（閲覧・編集・構成・共有・公開）の権限で共有できるようになった。10/28 23:04Z の更新で status が `Launched`（GA October CY2026）になり、セキュリティロールは自動で割り当てられる
  - https://www.microsoft.com/microsoft-365/roadmap?id=569475
- [動向] **PPCC 2026 の一次まとめ** — Microsoft が Power Platform ブログ（10/29）で PPCC 2026 の利用指標を公表し、前日に二次ソースのみで掲載した基調講演の内容を一次で裏づけた
  - 利用規模: 月間アクティブなメーカーが200万人超、アプリは400万本超。参加者は9,000人超
  - 伸び率（前年比）: Power Apps の日次アクティブユーザーが 20% 増え、Power Apps の AI 利用は2倍超、フローの実行数は 20% 増。Copilot Studio のアプリ利用は3倍超
  - 事例: Asurion は請求書の取り込みに Copilot Studio のエージェントを組み込み、人手を介さない処理の割合が 20% 未満から 70% 超に上がった
  - 前日の二次記事にあった「月間アクティブユーザー8,000万人」は一次の記事に出てこない
  - https://www.microsoft.com/en-us/power-platform/blog/2026/10/29/built-by-makers-five-years-of-power-platform-community-conference/
- [仕様] **Microsoft Copilot ハーネスの費用管理ページ** — Microsoft が `manage-usage-github-copilot-harness` を 10/29 01:03Z に `5691cde5`（`ms.date` 10/28）へ改訂したが、URL・題名・本文はまだ「GitHub Copilot harness」のままである。機能別の課金表と、環境割当・テナントプールからの引き当て・エージェント単位の上限の手順は既報と同じ構成である
  - https://learn.microsoft.com/en-us/power-platform/admin/manage-usage-github-copilot-harness
- [版更新] **Copilot Agent Kit の October 2026 ホットフィックス** — Microsoft が 10/26 のホットフィックスで、管理者に Agent Review Workflow を別のマネージドソリューションとして同時に入れ直すよう求めた。Agent Review Tool は GCC / GCC High / DoD でサポートされなくなり、Agent Inventory に共有の Editor / Viewer 数が加わった。Usage 機能は一時的に無効になった
  - https://github.com/microsoft/Power-CAT-Copilot-Studio-Kit/releases
- [動向] **ハーネスのファイル入出力の検証** — Qiita の投稿者（10/29）が、GitHub Copilot ハーネスのエージェントで作ったファイルを SharePoint に保存できた一方、SharePoint から読み込んだ Excel は文字化けしたと報告した。ワークフローからファイルを渡せたのはインラインエージェントだけで、見積依頼の読み取りには 16.51 クレジットかかった（ファイルの取得だけなら 0.13）
  - https://qiita.com/Takashi_Masumori/items/0ef4f38910f10829b51f
- [据え置き] **Copilot Studio の定点** — Copilot Studio What's New は `031b66d5`（`ms.date` 10/5）のままで、ハーネスの改名はまだ載っていない。課金レート表・課金5本・PPAC の容量管理・モデル表3本・ガイダンスハブにも改訂は無く、Released Versions は 2026.6.3 のまま121日動いていない
  - https://learn.microsoft.com/en-us/microsoft-copilot-studio/whats-new

### Microsoft 365 Copilot

- [新機能] **Copilot の財務向けスキルとプラグイン** — Microsoft が 10/29 に、財務部門の利用者が Excel と Cowork で25種類を超える財務向けスキルとパートナー製プラグインを使えるようにした。提供状況は機能ごとに違う
  - Capital Markets / Finance プラグイン（Cowork）: GA。投資ケース・類似企業比較・LBO モデル、決算レビュー資料などを扱う
  - 会計機能（Excel と Cowork）: Frontier。勘定照合・仕訳の作成・予算対比の業績報告を扱い、Copilot が何をなぜ変えたかの監査証跡を任意で Excel に残せる
  - Fabric IQ: Cowork で GA。Power BI のレポートとセマンティックモデルを参照できる
  - Dynamics 365 ERP プラグインとパートナー製プラグイン（QuickBooks・Moody's・FactSet・S&P Global など）: プラグインレジストリで展開を始めた。提供元側の別ライセンスや管理者の有効化が要る場合がある
  - Cowork What's New の10月節にも、10/29 15:34Z の改訂（`bd8f49bb`）で Accounting（Frontier Public）・Finance・Capital Markets のプラグインが加わった
  - https://www.microsoft.com/en-us/copilot/blog/2026/10/29/microsoft-copilot-for-finance-purpose-built-for-the-way-finance-teams-work/
- [予定] **PowerPoint の営業向け Copilot スキル4本** — PowerPoint の Copilot 利用者は、MC1529476 / 1529477 / 1529480 / 1529481 によると、11月上旬までに、提案書への回答・パイプラインのレビュー・顧客レビュー資料・経営層向けの売上サマリーを作るシナリオ別スキルを使えるようになる。Windows・Mac・Web が対象で、管理者の対応は要らない
  - https://mc.merill.net/message/MC1529481
- [据え置き] **Frontier の拡大と Copilot Code** — MC1529472（10/28）は、11月から Frontier の対象が Teams・新しい Outlook for Windows・OneDrive・SharePoint のプレビューに広がると告知したが、10/27 掲載の TC 記事と同じ内容である。MC1519871（Copilot Code の Frontier 展開）は 10/28 に本文が更新されたが、要件は変わっていない
  - https://mc.merill.net/message/MC1529472
- [据え置き] **Release Notes・ブログ・Learn の定点** — Release Notes は October 27, 2026 バッチ（`82b8ece5`）のままで、TC の各ブログと M365 Developer Blog にも新しい記事は無い。Partner Center 10月ページは 10/29 に3件が追記されたが、Copilot に関係する CSP の販促と AB-650 は既報である
  - https://learn.microsoft.com/en-us/partner-center/announcements/2026-october

### Claude / Anthropic

- [新機能] **Usage and Cost Analytics API（beta）** — Anthropic が 10/29 に、Claude Console と Claude Enterprise の組織のトークン利用量とコストを、モデル・ワークスペース・API キー・利用者で絞り込み・集計できる API を beta で出した。従来の Usage and Cost API と Enterprise Analytics API の利用・コスト系4エンドポイントは legacy になったが、引き続きサポートされ、退役日は示されていない
  - 新 API: beta ヘッダー `analytics-usage-cost-2026-08-24`、エンドポイントは `/v1/organizations/analytics/usage` と `/v1/organizations/analytics/cost`
  - legacy: Usage and Cost API と、`usage_report` / `cost_report` / `user_usage_report` / `user_cost_report`。移行ガイドが2本用意された
  - https://platform.claude.com/docs/en/release-notes/overview
- [仕様] **Claude API のリクエスト上限が 128MB に** — Anthropic が 10/28 に、第一者の Claude API の Messages API と Token Counting API の最大リクエストサイズを **32MB から 128MB** に上げた
  - https://platform.claude.com/docs/en/release-notes/overview
- [動向] **AI for Science の拡大** — Anthropic が 10/28 に、研究者へ無料の Claude クレジットを出す AI for Science を、財団・研究機関・研究プロジェクトの計20組織との提携に広げた。Sloan Foundation・Simons Foundation・米 NSF・Wellcome Sanger Institute・EMBL などが入り、クレジットの金額・応募方法・期限は書かれていない
  - https://www.anthropic.com/news/ai-for-science-expands-foundations-research-institutions
- [動向] **専門家はエージェントの意見を自分の判断と思い込む** — Anthropic が因果推論の専門家50人で実験し、コイントスで決めたエージェントの立場に4つの分析判断の86%で同調した（偶然なら50%）と報告した。52%は最終提言を「エージェントより自分のもの」と感じていた。一方、重大な手法上の誤りは AI なしで55%（11件中6件）、AI ありで6%（50件中3件）に減った
  - https://the-decoder.com/experts-adopt-ai-agents-random-opinions-and-think-theyre-their-own-anthropic-study-finds/
- [据え置き] **Claude Code とモデル退役の定点** — Claude Code の changelog の最上位は `2.1.312` のままで、npm は `{stable: 2.1.308, latest: 2.1.312, next: 2.1.312}` である。モデル退役ページの Active は15件のままで、Claude Haiku 4.5 は退役下限日の15日後も Active、Deprecation history の最新は 9/30 の Sonnet 4.5 のまま。`claude.com/resources/articles` と `support.claude.com` にも新着は無い
  - https://platform.claude.com/docs/en/about-claude/model-deprecations

### OpenAI / Codex / ChatGPT

- **ChatGPT Pro / Business の API クレジット**（ハイライト2参照）
- [料金] **ChatGPT Pro の Work・Codex 枠を倍に、Pro 200 の削減は撤回（二次）** — The Decoder（10/29）によると、OpenAI は Pro 100・Pro 500 の Work・Codex 枠を2倍にし、Pro 200 は予定していた 10/30 の削減を利用者の反発を受けて撤回した。Plus は変わらず、既存契約者にも自動で適用される。典拠のヘルプ記事「About ChatGPT Pro tiers」はオリジン403で本文に届かず、倍率は一次で確認できていない
  - https://the-decoder.com/openai-doubles-usage-limits-on-pro-plans-as-competition-with-anthropic-heats-up/
- [新機能] **ChatGPT の iCloud Mail / Calendar プラグイン** — OpenAI が 10/27 に、iCloud の利用者が Mail と Calendar を ChatGPT につなげるようにした。全プランの Web・デスクトップ・iOS が対象である（release notes は WebSearch 経由で確認）
  - https://help.openai.com/en/articles/6825453-chatgpt-release-notes
- [据え置き] **Codex・OpenAI の定点** — Codex の安定版は `0.165.0`（10/27）のままで、pre-release は `0.166.0-alpha.6`（10/29）まで進んだ。`learn.chatgpt.com` の changelog、deprecations（`2026-10-14: GPT-4 series model deprecations`）、`alignment.openai.com` の First posted（10/20）は動いていない
  - https://github.com/openai/codex/releases

### GitHub Copilot

- [新機能] **プラグイン統制の GA** — GitHub が 10/28 に、VS Code・Copilot CLI・Copilot app でリポジトリ既定のプラグインと企業管理のプラグイン統制を GA にした。企業は承認済みマーケットプレイスの指定・必須プラグイン（利用者は無効化不可）・個別ブロックを設定でき、管理設定がリポジトリと個人の選択に優先する。企業統制は GitHub Enterprise Cloud で Copilot Business / Enterprise のライセンスを持つ利用者が対象である
  - https://github.blog/changelog/2026-10-28-repository-plugin-defaults-and-enterprise-plugin-controls-generally-available
- [据え置き] **Copilot changelog と CLI の定点** — `github.blog/changelog/label/copilot/` の最上位は 10/28 の Copilot Fusion のままで、10/29 のエントリは無い。Copilot CLI の安定版も `v1.0.105`（10/28）のまま

### Google

- [予定] **Gemini 4 Carbon の一次発表** — Google が 10/28 に、Gemini 4 Argon を土台にした Gemini 4 Carbon を The Keyword で発表し、同じ週からサイバー防御担当者の一部に提供し始めた。Fairwind Program の信頼パートナーへ段階的に広げ、開発者・企業・一般向けの時期は示していない。前日に二次で掲載した内容を一次で裏づけた
  - 価格: 導入価格は入力 $2 / 出力 $10（100万トークンあたり。Argon と同額）、キャッシュ入力は95%引き。導入期間の後は $4 / $20
  - Google の公表値: Artificial Analysis Intelligence Index v5.0 で59点、SEC-bench Pro 88.2%、Gray Swan の間接プロンプトインジェクションの攻撃成功率 0.0%（Argon は 0.7%）
  - Gemini API の changelog（最上位 10/27）にはまだ載っていない
  - https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-carbon/
- [新機能] **Gemini API CLI（beta）** — Google が 10/27 に、AI コーディングエージェント・スクリプト・CI から Interactions API を呼ぶ依存ゼロのコマンドラインクライアント `gemini-api` を beta で出した。テキストやメディアの生成、ファイル解析、Gemini managed agents の実行ができる
  - https://ai.google.dev/gemini-api/docs/changelog
- [新機能] **Gemini アプリでのファイル作成・編集** — Google が 10/29 に、Workspace の利用者が Gemini アプリのチャット内でスライド・スプレッドシート・ドキュメント・Markdown・コードなどを作り、プレビューして編集できるようにした。PDF は Web とモバイル、他の形式は Web のみで、管理者向けの設定は無い
  - https://workspaceupdates.googleblog.com/2026/10/create-preview-and-edit-files-directly-in-the-Gemini-app.html
- [据え置き] **Gemini の定点** — Gemini アプリの release notes は 2026.10.13、The Keyword の AI RSS は 10/26 のままで、Gemini API の deprecations は 11/17 の停止予定から動いていない

### オープンウェイト / その他エージェント

- [新機能] **Mistral Large 4 の重み公開** — Mistral が 10/29 に、総パラメータ約1T・アクティブ約52B の MoE モデル Mistral Large 4（通称 Le Chonk）の重みを Hugging Face で公開した（`private: false` / `gated: false`）。Microsoft Foundry でも提供され、NVFP4 量子化版も同時に出た
  - モデル: 1M コンテキスト、テキストと画像の入力、`low` / `medium` / `high` の推論強度。API では `mistral-large-4`
  - ライセンス: Mistral Ecosystem Open-Weight License（MIT の改変版）。商用利用はできるが、Model-as-a-Service 事業には別ライセンスが要る
  - API 価格: 入力 $0.70 / 出力 $2.10（100万トークンあたり・二次。プレビュー時は $1.36 / $4.18）。`mistral.ai` は本環境から到達できず一次未読
  - 性能（二次）: Artificial Analysis の Coding Agent Index は48（Opus 5.5 の Claude Code は62）、Terminal-Bench 4.0 は41%
  - https://huggingface.co/mistralai/Mistral-Large-4-1T-A52B
  - https://the-decoder.com/paris-based-mistral-releases-le-chonk-a-strong-coding-model-that-still-trails-china-overall/
- [新機能] **Devin の 10/28 更新** — Cognition が 10/28 に、Azure DevOps の PR へのフィードバック（コメント・CI・マージコンフリクト）を GitHub と同じく PR を持つセッションへ届けるようにした。Progress タブはタスクのライブ一覧になり、@ メニューからユーザー単位のスキルを呼べるようになった
  - https://docs.devin.ai/release-notes/overview
- [新機能] **Orca `v1.4.244`** — Stably AI が 10/29 に Orca `v1.4.244` を出し、多数のエージェントを走らせる Codex チャットの履歴の膨らみを抑え、SSH・ペアサーバー上のファイルをローカルと同じく開けるようにした。worktree の場所に書いた `~` はホームフォルダーを指すようになり、SSH ワークスペースの削除にはホストのファイルを残す「Remove from Orca」が加わった
  - https://github.com/stablyai/orca/releases
- [据え置き] **Cursor / xAI / TypeSafe / MCP の定点** — Cursor の changelog（10/20）とフォーラム（10/12）、xAI release notes は動いていない。TypeSafe AI は `jev-1.14.0` のまま、MCP blog は 8/22 のまま、Hugging Face の他7 org にも新規リポジトリは無い

### セキュリティ

- [セキュリティ] **中国のラボの蒸留の標的が GPT-6 Astra に移った** — The Decoder（10/29）が The Information の報道を伝え、DeepSeek と Moonshot AI が Kimi K3.1 Pro などの最新モデルで OpenAI の GPT-6 Astra の出力に大きく頼ったと報じた。Anthropic は 10/12 付の一次記事で、2段階の分類器により蒸留側が得られるデータを90〜99%減らし（誤検知0.1%未満）、Sonnet 5.5 の推論を発行した組織にだけ見せる設定に変えたと説明している
  - https://the-decoder.com/openais-astra-becomes-the-main-target-for-chinese-ai-labs-after-anthropic-tightens-its-defenses/
  - https://www.anthropic.com/news/distillation-defenses

### 市場・企業

- [動向] **Alphabet の Q3 で Google Cloud 売上が前年比 103%増** — Alphabet が 10/28 に発表した Q3 決算で、Google Cloud の売上は $30.7B だった（報道）。全社売上は $127.6B（+25%）で予想に届かず、フリーキャッシュフローは −$9.1B。Gemini アプリは10億人、Gemini API は毎分約320億トークン（前四半期比+40%）を処理している。決算資料の一次には届かなかった
  - https://www.cnbc.com/2026/10/28/alphabet-googl-earnings-q3-2026.html
- [動向] **米司法省が Nvidia の Hugging Face 買収を調査** — The Decoder（10/29）が Reuters（10/28・関係者2人）を伝え、米司法省が総額 $12.93B の買収（2027年上期に完了予定）で Nvidia が AI 配布の要所を握るかを調べていると報じた。SchedMD・Run:ai の買収、Groq とのライセンス、チップとネットワーク機器の抱き合わせも審査対象とされ、仏競争当局も CUDA 依存を調べている
  - https://the-decoder.com/us-antitrust-regulators-are-scrutinizing-nvidias-hugging-face-deal-and-sales-practices/
- [据え置き] **買収協議・調査の定点** — Amazon × Decart、Nvidia × Reflection AI の買収協議に続報は無い。IDC Japan・MM総研・NRC の新規公表も検知されていない

## 直近の注目予定

- **10月下旬**: Copilot Code が Frontier で展開を始める（MC1519871）
- **10月下旬〜11月中旬**: Researcher の Critique / Council が退役（MC1515927、Act by 11/14）
- **10/27〜2027/6/30**: M365 E3 の30%割引オファー（CSP・新規300ライセンス以上）
- **10/30**: Copilot Connectors ページが Allowed agent types の設定に従う（MC1454973） ／ AB-650 認定が開始 ／ Gmail Live の Workspace への順次展開が完了（最大15日）
- **10/31**: MCP サーバー認定の旧申請経路が終了 ／ DeepSeek の Search・Fetch API の無料提供が終了 ／ OpenAI の既存 Evals が読み取り専用に
- **11/1**: AI Builder の容量アドオンが提供終了し、新規・更新のライセンスに AI Builder クレジットが付かなくなる（MC1526652） ／ Codex の28日間「改善かリセット」の終了（二次）
- **11/2**: xAI `grok-imagine-image-quality` が退役 ／ Meet の63言語音声翻訳が Scheduled Release へ展開開始
- **11/4**: Entra で一般ユーザーのブループリント作成が既定オン（MC1506733） ／ Kimi K3.1 Pro の重み公開の約束期限（二次）
- **11/5 ごろ**: Anthropic のゲスト研究者（生命科学）の応募受付が終了（締切日は明記なし）
- **11月上旬**: PowerPoint の営業向け Copilot スキル4本の展開が完了（MC1529476 ほか）
- **11月**: GitHub の cloud sandbox の課金が開始（日付は明記なし） ／ Targeted release の割り当てが変更不可になり、統合 Release Preferences 画面が入る ／ Frontier の対象が Outlook / OneDrive / SharePoint / Teams のプレビューに拡大（MC1529472） ／ Power Pages の AI コーディング用プラグインと生成ページの追加モデルが GA（Roadmap 577900 / 576285） ／ Copilot アプリの Chat のモード切替提案が GA（Roadmap 577841）
- **11月上旬〜下旬**: Audio Overview の拡張機能が展開（MC1492959）
- **11/9**: Dataverse のみのテナントでストレージ検証が開始（MC1483529。12/14 に展開完了）
- **11/12**: Copilot Studio の GPT-4.1 / GPT-5 系が退役（MC1506318） ／ Anthropic Usage Policy 改定版が発効 ／ OpenAI → Cursor のモデル供給停止予定（一次未読）
- **11月中旬**: Viva Insights の GitHub Copilot 指標が既定オン（MC1523085） ／ 会議メモの保存先が開催者の OneDrive に（MC1523076） ／ Interpreter の逐次通訳モードの GA 展開が開始（MC1239927） ／ クラシック Outlook の Copilot の入口が移る（MC1441784） ／ Anthropic の上場（早ければ・報道）
- **11/15**: Dataverse for Teams 環境とアンマネージド開発者環境の新規作成が停止
- **11/16**: GitHub Copilot が Claude Opus 4.8・Opus 5・GPT-5.6 Terra を廃止 ／ Teams の旧 GitHub アプリが退役
- **11/17**: Work IQ の業務アプリ統制がパブリックプレビュー（MC1518036） ／ Gems が Gemini アプリの設定パネルへ移動 ／ Gemini API の TTS・Live プレビュー5種が停止（最短日）
- **11/17〜20**: Microsoft Ignite
- **11/20**: Copilot Studio のコスト管理を M365 管理センターへ移す機能が GA（MC1530368）
- **11/24 以降**: `claude-opus-4-5-20251101` の暫定退役日（確定日ではない）
- **11月下旬**: Copilot Dashboard の Viva Pulse アンケートの GA 展開が開始（MC1446805。12月中旬に完了）
- **11/30**: Power Automate の Describe it to design it が退役 ／ `claude-sonnet-4-5-20250929` が Claude API から退役 ／ OpenAI の Evals・`v1/prompts`・Agent Builder が停止 ／ Gemini 4 Argon の導入価格が終了 ／ Azure DevOps コネクタの旧接続が認証不可に（MC1508508） ／ App Builder と vibe.powerapps.com が退役 ／ MS-102 認定が退役
- **11月末**: Copilot メモリの業務データ対応の展開が完了（MC1492154）
- **12/1**: M365 Copilot の前提サブスク不要オファー開始 ／ Copilot Business の従量課金が既定オン ／ Gemini 4 Argon の単価が $4/$20 に倍増
- **12月初旬**: Microsoft の自主退職制度の申し出期限（12/31 付で退職）
- **12/14**: claude.ai/design の単体サイトが閉鎖
- **12/15**: アンマネージド開発者環境が停止
- **12/31**: Claude Security の無償クレジット（月 $25,000×2か月）の対象期間が終了 ／ Gemini 4 Carbon の導入価格の割引が終了
- **2027-01-06**: OpenAI `tts-1` / `tts-1-hd` / `gpt-4o-mini-tts` 2版が停止
- **2027年1月**: Targeted release が退役 ／ Power Pages の ID プロバイダー統制が GA（Roadmap 578062） ／ Copilot Studio の Teams アプリで編集ができなくなる（MC1511056） ／ Microsoft Copilot ハーネスの Computer Use が GA（Roadmap 576272）
- **2027-01-14**: OpenAI の GPT-4o・GPT-4o mini・GPT-4.1・GPT-4.1 mini が API から削除（→ `gpt-6-luna`）
- **2027-01-15**: アンマネージド開発者環境の削除開始 ／ Claude Code Review の Enterprise 向けクレジット請求期限
- **2027年1月中旬〜下旬**: 旧来の Teams 保持ポリシーが Copilot の対話に効かなくなる（MC1481313） ／ Purview の DSPM classic / DSPM for AI classic が退役（MC1481315）
- **2027-03-01 以降**: Gems 廃止（Business / Enterprise）
- **2027年3月**: Power Automate の UI 自動化の AI 修復が GA（Roadmap 577869）
- **2027年3月末**: Outlook の Copilot Prioritize の削除が完了（MC1519861） ／ SharePoint / OneDrive の `.agent` 形式エージェントが動かなくなる（MC1511052）
- **2027-04-01**: OpenAI `gpt-5.1` / `gpt-5.3-codex` / `gpt-5.4-nano` が停止
- **2027年4月末**: Copilot Chat の従量課金のメッセージ消費レポートの GA 展開が開始（MC1069563）

## 改善メモ

- 新規提案: 3ソースとも新規起票なし
- 継続提案: Copilot は継続2件（最多 B-080 Cowork の Learn URL 差し替え、4回目。B-081 ハーネス改名は Learn の費用管理ページが 10/28 改訂後も旧名のまま、2回目） ／ industry は継続5件（最多 B-040 セキュリティ開示の定点、13回）で、Anthropic の蒸留対策の一次記事（10/12）を18日遅れで二次経由で検知したと記録した。見送り候補 B-023 ／ Master は記録なし
- 障害の変化: industry が `s206.q4cdn.com`（Alphabet の決算資料）のゲートウェイ拒否を新規に記録した。Master・Copilot は記録なし
- ソース間の差分・矛盾:
  - ChatGPT Pro 200 の 10/30 の枠変更は、Master が注目スケジュールに「半減（二次）」を残したまま、industry が The Decoder（10/29）を典拠に「削減は撤回」と書いた。どちらも一次未確認のため、日次は撤回の報道を [料金]（二次）で収録し、注目予定から 10/30 の半減を外した
  - Anthropic の Usage and Cost Analytics API と 128MB 上限は、Master が1項目 [新機能+仕様]、industry が2項目（[新機能] / [仕様]）に分けた。日次は「1項目に2つのリリースを同居させない」に従い2項目に分けた
  - ChatGPT の API クレジットの付与条件は、Master が「フォーラムの公式回答以外の補足を含む」とし、industry が解説ガイド（一次）で7日以上の契約・同一メールなどの条件を確認している。日次は industry の条件を採った
  - Mistral Large 4 の提供面は、Master が Hugging Face のみ、industry（The Decoder）が Hugging Face と Microsoft Foundry と書いた。日次は両方を記載した
