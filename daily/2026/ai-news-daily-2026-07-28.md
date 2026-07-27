# AI News Daily Summary — 2026-07-28

> 本サマリーは 01_ai-news-Master・02_ai-news-Copilot・03_ai-news-industry の3ソース（7/28分）を統合して作成。

火曜の主題は3つ。Kimi K3 のオープンウェイトが実際に公開され（前日サマリーの「7/28 0:00 JST 公開」は誤りで、実際は 7/27 朝 JST）、Nvidia が SK Group と $500B 超で合意して争点が GPU から HBM へ移り、Microsoft は Power Automate モバイルアプリの 8/31 廃止を掲載した。

## 今日のハイライト

### 1. Kimi K3 のオープンウェイトが公開 — ライセンスは緩いが、自前ホストの下限が高い

**要点**: **2.8兆パラメータ**のウェイトが Hugging Face で公開。史上最大のオープンウェイトで商用利用も可能だが、動かすには最低8基の H100 クラスが要る。

**詳細**: 公開は **7/27 8:30 JST 頃**（Moonshot の予告は 7/27 15:00 UTC＝7/28 0:00 JST だったため約15時間の前倒し。industry 側は「7/27 00:00 UTC に予定どおり公開」と記載しており評価が割れる。改善メモ参照）。`moonshotai/Kimi-K3` に safetensors シャード・LICENSE・モデルカードが揃い、技術レポートも同時公開された。構成は 896 エキスパート中16個を選択する MoE で、総 2.8T に対しアクティブ 104B、コンテキストは 1,048,576 トークン、ネイティブ画像入力あり。新規要素は Kimi Delta Attention と Attention Residuals で、Moonshot は K2 比でスケーリング効率が約2.5倍と主張。量子化は SFT 段階以降の quantization-aware training で重み MXFP4 / 活性化 MXFP8、共同創業者は AMA で「配布ウェイトの MXFP4 はホスト API と完全に同一」と明言している。配布サイズは **約594GB**（MXFP4）とする報道と、4bit で約1.4TB とする試算に割れたまま。ベンチは Artificial Analysis 初日計測で GDPval-AA v2 が 1668 Elo（K2.6 は1190）、AutomationBench-AA が 53% で首位、自社ベンチは GPQA Diamond 93.5%・BrowseComp 91.2。一方 7/25 に指摘された51%のハルシネーション率は今回の公開でも解消していない。推論基盤は vLLM と SGLang が day-0 対応（SGLang は CUDA / AMD 版 Docker イメージを公開）、Together AI と Modal が day-0 ホスティングを提供。

**意味**: 中国 API へデータを送らずに最大級のオープンモデルを使う選択肢が初めて現実になったが、検証の入口が重い。ワークステーションや単一 GPU サーバでは成立せず、触るなら Together AI / Modal のホスト経由か、既存 GPU クラスタに SGLang の Docker を載せる経路になる。llama.cpp / Ollama / LM Studio 系は新アーキテクチャ対応待ちで、DeepSeek V4 の前例では mainline 対応まで数週間かかった。官公需・規制産業の案件では 7/22 に OSTP が名指しした蒸留疑惑と制裁リスクが残り、出自の説明責任が先に来る。

- https://huggingface.co/moonshotai/Kimi-K3
- https://vllm.ai/blog/2026-07-22-kimi-k3-preview
- https://docs.sglang.io/cookbook/autoregressive/Moonshotai/Kimi-K3
- https://www.unite.ai/moonshot-opens-kimi-k3-weights-under-a-revenue-tiered-license/
- https://northflank.com/blog/what-is-kimi-k3-self-hosting

### 2. Nvidia × SK Group が $500B 超で合意 — 争点が GPU から HBM の確保へ移った

**要点**: 7/24-25、Nvidia と韓国 SK Group が **$500B超** のAIインフラ協業で基本合意。前日報道の OpenAI 向け保証と合わせ、週末の2件で $750B 規模になる。

**詳細**: 柱は3つで、①SK テレコムが Vera Rubin プラットフォームで **2GW** のAIデータセンターを建設し第1期を2027年稼働、②Nvidia と SK hynix が次世代広帯域メモリ HBM4 を長期共同開発して Nvidia 向け供給を固定、③スケーリングの実質的ボトルネックであるメモリ供給不足への対処。発表はサンフランシスコのAIサミットで、現時点は法的拘束力のない LOI 段階にとどまる。同じ週末には Nvidia が OpenAI のデータセンター賃借に約 **$250B** の保証を検討中と WSJ が報じている（7/27 分収録済）。

**意味**: 顧客に2027年以降の計算資源コストを説明する場面では、GPU 単価と電力に加えて「メモリ供給が確約されているか」が調達リードタイムを左右する変数になる。ただし NAVER 案件（7/25）と同様に非拘束の LOI なので、稼働時期を前提にした試算は割り引いて置くのが妥当。

- https://nvidianews.nvidia.com/news/sk-group-and-nvidia-expand-strategic-partnership-across-ai-factories-and-next-generation-memory
- https://www.cnbc.com/2026/07/25/nvidia-locks-down-memory-from-sk-hynix-as-part-of-500-billion-ai-deal.html

### 3. Power Automate モバイルアプリが 8/31 に廃止 — 承認と通知の受け皿を Teams へ寄せる作業が発生する

**要点**: Microsoft が Power Automate モバイルアプリ（iOS / Android）を **2026-08-31** に非推奨とすると公式の非推奨一覧に掲載した。既存フローの実行そのものには影響しない。

**詳細**: 廃止後はアプリが App Store と Google Play から削除され、更新とサポートが停止する。実害は2点で、①「Send me a mobile notification」アクションの通知先が消滅する（アクション自体は designer に残るため、フローを直さない限り通知が届かないことに気づけない）、②ホーム画面ウィジェット（run a flow）が機能しなくなる。代替として **Teams Approvals**、Power Automate ポータル（モバイルブラウザー可）、Power Apps mobile が案内されているが、Microsoft 自身が制約も明記しており、ホーム画面ウィジェットに直接の等価物はなく（Power App のピン留めが部分的回避策）、失敗時のプッシュ通知はメーカーが「Run after = has failed」で Teams / メール通知アクションを自前で足す必要がある。管理者側は Teams アプリ権限ポリシーで Approvals アプリがブロックされていないかの確認が要る。なお本項目は learn.microsoft.com の en-us / ja-jp 両方と Learn 検索インデックスに存在する一方、`MicrosoftDocs/power-platform` の GitHub main には未反映（`ms.date` は 05/22/2026 のまま）で、公開が先行している状態。

**意味**: 研修や PoC で「モバイルアプリで承認する」構成を案内していた場合、8月末までに Teams Approvals ベースへ差し替える必要がある。特にモバイル通知アクションを使っているフローは棚卸し対象で、通知先の付け替えが漏れると失敗に気づけない運用になる。

- https://learn.microsoft.com/en-us/power-platform/important-changes-coming
- https://learn.microsoft.com/en-us/power-automate/teams/native-approvals-in-teams

## カテゴリ別まとめ

### Microsoft / Copilot / Power Platform

- Agent 365 の新規購入に前提ライセンスが必須化（6/1 発効・Partner Center に 7/1 掲載）— 認められるのは **M365 E5** / A5 / Business Premium、Microsoft Defender Suite と Microsoft Purview Suite の組み合わせ、その Edu 版、Defender and Purview Suite FLW のいずれか。前提を持たない顧客は一部機能を利用できない可能性がある。M365 E7 は E5・Agent 365・M365 Copilot・Entra Suite を内包するため E7 の商談には影響しない。Agent 365 を含む提案では前提ライセンスの充足確認が見積もりの前段に入り、E5 未満の顧客には E7 との比較が実質的な選択肢になる。 https://learn.microsoft.com/en-us/partner-center/announcements/2026-july
- Partner Center の未回収分3件 — SMB 向けトライアル「**Copilot in 30**」（300名未満の組織向け・25ユーザー/30日の M365 Copilot Business トライアル、CSP 提供は 8/1 開始、7/14 掲載）、M365 Copilot スペシャライゼーションの要件刷新（MS-102 要件を撤廃し AB-100 / AB-620 を追加、7/9 掲載）、M365 Copilot 非営利オファーのパートナーマージン改定（7/1 遡及適用・8月価格表に反映、7/27 掲載）。 https://learn.microsoft.com/en-us/partner-center/announcements/2026-july
- Microsoft 365 Copilot の7月更新まとめ — Copilot Cowork が全世界 GA（タスクを定義すると下書きではなく完成した成果物を返す）、Copilot Notebooks がノートから Word / Excel / PowerPoint を直接生成しメールを参照追加可能、Outlook の Copilot Chat が単一スレッドから受信箱・カレンダー全体へ拡大（有償アドオンなしで利用可）。搭載モデルは GPT-5.6 と Claude Sonnet 5 の2本立て。定着化支援の提案では、アドオンなしで届く範囲が広がった点が導入ステップの組み替えに効く。 https://www.aguidetocloud.com/blog/microsoft-365-copilot-july-2026-updates/
- デスクトップフローの統合 Power Apps が **7/31 GA** 予定 — メーカーが canvas アプリを有人デスクトップフローのフォーム UI として使える。デスクトップフローからアプリへ context / state を渡して事前入力でき、ボタン操作から特定のサブフローを呼べる。 https://learn.microsoft.com/en-us/power-platform/release-plan/2026wave1/power-automate/build-better-forms-integrated-power-apps
- Microsoft 一次のドキュメント系は据え置きが継続 — Copilot Studio What's New は June 2026 節が最新で7月節は未公開（外部モデル選択の GA 表記は Claude Sonnet 5 / GPT-5.5 Chat どまりで Opus 5 は Learn 側に未追加）、M365 Copilot Release Notes は `July 15, 2026` バッチが最新（全文9,845行を Learn MCP で取得し 7/22・7/29 バッチの不在を確認、隔週傾向から次は 7/29 前後）、Released Versions は Copilot Studio Build **2026.6.3**（6/30 初出）のままで火曜更新日の本日も 2026.7.x は反映されず7月中のビルドが1本もない状態が4週続く、M365 Roadmap の Latest announcements も 7/9 が最新。 https://learn.microsoft.com/en-us/power-platform/released-versions/copilotstudio
- 拡張性まわりも新規なし — 拡張機能 What's New の「July 2026」節に追加項目なし（宣言型エージェント manifest 1.8 と Copilot 利用状況レポート API 3種の `version` パラメーターが同節の内容）、Copilot Agent Kit は「June 2026」（7/9 更新）が最新、7月分の「What's New in Power Platform」も未公開で最新は 6/11 の June Feature Update。 https://learn.microsoft.com/en-us/microsoft-365-copilot/extensibility/whats-new
- Message Center は 7/22 以降の新規 MC を検知できず（mc.merill.net が 403 のため WebSearch で照合）。MC1436831（M365 Admin agent の GA・7/22）と MC1422074（OpenAI モデルのサブプロセッサー化・7/24 発効）はいずれも既報。 https://mc.merill.net/
- 日本語コミュニティ（Qiita / Zenn）は本日、厳選掲載に値する新規記事なし。Copilot Studio の週次まとめ系・「2026年7月版」系は既知トピックのキュレーションにとどまる。 https://qiita.com/tags/copilotstudio

### コーディングエージェント / 開発ツール

- Devin Outposts が alpha 公開（7/21・初報）— Devin Cloud のセッションを自社が管理するマシン上で実行できる。Outpost は「名前付きキュー」で、**エージェントループ（推論・プランニング）は Devin のクラウドに残り**、コマンド実行・ファイル編集・リポジトリアクセスだけが自分のマシンで行われる。対応先はラボの GPU ボックス、プライベートネットワーク内の VM、社内サービス隣の Kubernetes クラスタ、机上の Mac mini など。手順は Devin Cloud 側で Outpost を作成 → Devin CLI で自マシンに worker を追加 → セッション開始時にランタイム環境として選択。Modal・E2B・Daytona の統合が用意され、Modal 経由なら学習・推論と同じ GPU 基盤上で障害再現やプロファイリングをさせて終了後ゼロにスケールダウンできる。社内リソースに触れる作業をコードを外に出さずエージェントへ渡せる一方、完全なオンプレ化ではないので、評価ではこの境界線がセキュリティ要件を満たすかが判断軸になる。 https://devin.ai/blog/introducing-devin-outposts / https://modal.com/blog/devin-outposts-run-devin-in-modal-sandoxes
- Devin の7月アップデート（Outposts 以外）— ①デスクトップ全体の E2E テスト: computer use で Linux 上の任意のデスクトップアプリをテストでき、Devin が自分の PR の QA を申請して承認するとアプリを起動しクリック操作を行い、編集済みの操作録画をレビュー用に送ってくる。②v3 API が beta を脱して主 API に昇格し、旧 API の全機能に加えロールベースアクセス制御・セッション帰属・automations の CRUD・消費量トラッキングを提供。③Slack / Linear 連携の高速化。`docs.devin.ai` が実行環境から到達不可のため①②は二次情報ベースで、個別の適用日は未確定。 https://docs.devin.ai/release-notes/2026
- Claude Code と Codex が同じ週に「乗り換えコストを下げる」更新 — Claude Code は Opus 5 を既定の Opus モデルに切り替え、動的ワークフローとネストしたサブエージェントを拡張、MCP・サンドボックス・モデルピッカーを改善。Codex は `/import` で Cursor と Claude Code の設定・MCPサーバー・プラグイン・セッション・コマンド・プロジェクト単位のメモリを移行できるようにし、Amazon Bedrock ログイン（既定モデルは GPT-5.6 Sol）、音声入力、realtime V3 会話に対応。設定資産の持ち出しが標準機能になると、エージェント CLI のロックインは想定より弱くなる。 https://releasebot.io/updates/openai/codex
- Codex CLI の pre-release が再開 — `0.146.0-alpha.12`（7/27 08:25 UTC）と `0.146.0-alpha.13`（7/27 16:03 UTC）が公開され、7/25 の alpha.10.1 で止まっていた刻みが動き出した。安定版は **0.145.0**（7/21）据え置きで、公開リリースノートに具体的な変更内容の記載はない。 https://github.com/openai/codex/releases
- 主要 CLI はバージョン据え置き — Claude Code **v2.1.220**（7/25）、GitHub Copilot CLI v1.0.75（7/24・Opus 5 対応）。Claude Platform の release notes も最新エントリが 7/24（Opus 5 と破壊的変更2件）のままで 7/25〜28 の追加はない。 https://code.claude.com/docs/en/changelog

### AI モデル

- Kimi K3 のオープンウェイト公開（ハイライト参照）
- **Gemini 3.5 Pro** は未 GA が継続 — I/O 2026（5/19）発表 → 6月 GA 目標 → 7/17 目標説をいずれも逸失し、7/22 時点でも Vertex AI の限定エンタープライズ preview どまり。公開日・価格・スペックのいずれも確定していない。報道ベースでは 2M トークンコンテキストとされるが未確認で、公開 API で GA 済みなのは gemini-3.5-flash / gemini-3.1-pro-preview のみ。 https://theairankings.com/google/gemini-3-5-pro/
- **Grok 4.6** は予告の「約2週間」を過ぎても未リリース — Musk が 7/18 に 2T パラメータ機として公表した際の予告は「約2週間後に 4.6、その2週後に 4.7」で、その期限が今週到来したが公開はない。pre-training は 7/20 週に完了済みで、SpaceX の工学データ（ITAR 対象を除く）による追加学習が計画されている。コミュニティの見立ては8月下旬〜9月中旬。xAI は Kimi K3 に匹敵しつつ Grok 4.5 の速度・トークン効率を維持する点を勝負どころとしている。 https://www.nextbigfuture.com/2026/07/spacexai-will-release-grok-4-6-in-2-weeks-and-grok-4-7-in-4-weeks.html

### 市場データ・調査

- VentureBeat のコンテキストレイヤ調査（6月実施・n=101）— 過去6カ月で **57%** の企業が「自信をもって間違えた」エージェント回答の原因を業務コンテキストの欠落・不整合に特定し、31%は複数回経験。にもかかわらず統制されたコンテキストレイヤを本番稼働させているのは25%だけ。エージェントが業務文脈を得る既定手段は文書に対する検索（RAG）が38%で最多だが、選定基準は取り込みやすさと運用の簡単さが上位で検索精度はその下。提案で「モデルを替える前に、参照する業務データの正規化と権限設計が先」と言い切れる定量根拠になる。 https://venturebeat.com/data/57-of-enterprises-have-watched-ai-agents-be-confidently-wrong-the-fix-is-an-agentic-context-layer-but-who-has-one
- 同じ調査群のオーケストレーション面 — **71%** が「導入済みエージェントのうち自律的に多段作業を完了できるのは1/4以下」と回答し、真のエージェントが過半を占めるとしたのは10%のみ。7/13 掲載の評価ギャップ（社内評価をパスしたのに顧客対応で失敗した企業が半数）と合わせ、「エージェント導入済み」という自己申告と実態の乖離を数字で示せる。 https://venturebeat.com/technology/venturebeat-research-where-enterprise-ai-agent-governance-hasnt-caught-up

### エンタープライズ・導入支援

- OpenAI が中小企業向けプログラムを開始（7/21・catch-up）— オンライン研修、米国内での対面「AIアカデミー」、導入ガイド、Shopify / Intuit との連携の4本立てで、基盤は ChatGPT Work と GPT-5.6。同時に ChatGPT Work と Codex の合計利用者が **1,000万** を超えたと公表した。大企業向けの実装体制競争（Microsoft Frontier / Anthropic Ode / OpenAI Presence）とは別に、研修とテンプレートで裾野を取りにいく動きが並走している。 https://openai.com/index/introducing-chatgpt-small-business-program/

### 規制・地政学

- 7/24 のオープンウェイト書簡（Nvidia / Microsoft / OpenAI ほか）を ITmedia が 7/27 に国内報道 — Anthropic は署名しておらず、同社従業員が X で「CUDA と Windows のオープンソース化が楽しみだ」と皮肉った経緯も伝えている。クローズド専業ほど規制強化で利する構図が、当事者の発言レベルでも見えている。 https://www.itmedia.co.jp/aiplus/article/2607/27/2000000222/
- Kimi K3 のライセンス解釈が二次情報間で割れている（ハイライト・改善メモ参照）

### インフラ投資・決算

- Nvidia × SK Group の $500B 超合意（ハイライト参照）
- 7/29-30 に Microsoft・Meta・Apple・Amazon が決算発表 — 焦点は通年 capex ガイダンスで、7/22 の Alphabet（$180–190B → **$195–205B** へ上方修正）に続く動きが出るかを確認する。 https://www.zaikei.co.jp/article/20260725/862802.html
- Anthropic の公開 S-1 / S-1A は EDGAR 上で引き続き未掲載。6/1 の極秘申請から状況変化なく、ティッカー・価格レンジ・取引所も未発表。

## 直近の注目予定

- **7/29 前後**: M365 Copilot Release Notes の次バッチ（Opus 5 の記載有無を確認）
- **7/29-30**: Microsoft・Meta・Apple・Amazon の決算発表（通年 capex ガイダンスが焦点）
- **7/30 前後**: M365 Copilot 拡張機能 What's New の次月次、Copilot Agent Kit / MS-4005 の週次確認、M365 Copilot メモリ活用のエージェント提案 GA 予定
- **7/31**: デスクトップフローの統合 Power Apps が GA 予定 / Devin classic 環境設定 read-only 参照終了
- **8/1**: covered frontier model 60日 EO 期限 / SMB 向け「Copilot in 30」トライアルが CSP で提供開始
- **8/3**: 旧「Claude in Slack」退役
- **8/5**: Claude Opus 4.1 の Claude API 退役 / Cowork 倍増利用枠終了
- **8月第1週**: Power Platform Weekly の夏季休刊明け
- **8/9**: ChatGPT Atlas シャットダウン
- **8/17**: Claude Console 旧 Workbench 退役 ＋ 実験的プロンプトツール API 廃止
- **8/26**: OpenAI Assistants API 廃止 / o3 退役 / GPT-4.5 完全廃止
- **8/31**: Sonnet 5 促進価格終了（→ $3/$15）/ Power Automate モバイルアプリ廃止（ハイライト参照）
- **8月下旬〜9月中旬（推定）**: Grok 4.6（予告の2週間期限は経過）
- **9/15**: Cloudflare の新規ドメインで Training / Agent がデフォルト拒否に
- **9月**: iOS 27 / macOS 27 GA（AFM 3 本番）
- **2026年秋**: SharePoint Copilot Apps の GA と SharePoint ストア配布

## 改善メモ

- **前版の訂正: Kimi K3 の公開時刻**: 07-27 版は Hugging Face メタデータ `releaseDate: 2026-07-27T15:00:00.000Z` を根拠に「7/28 0:00 JST 公開」としたが、実際には 7/27 朝（JST）に公開された。予告メタデータは公開時刻の確定根拠にならない。
- **不一致: Kimi K3 の公開が前倒しか予定どおりか**: Master は「7/26 約19:30 EDT ＝ 7/27 8:30 JST 頃に約15時間前倒しで公開」、industry は「7/27 00:00 UTC ＝ 7/27 9:00 JST に予定どおり公開」。実時刻の差は30分程度で実質一致するが、「予告 7/27 15:00 UTC に対して前倒しだったか」の評価が正反対。本文は Master の前倒し説を採り、industry の記載を併記した。
- **不一致: Kimi K3 のライセンス条件**: Master は「商用条件付きの MIT ライク。Moonshot 自身の API と競合する用途は別途交渉が必要という解釈が優勢」、industry は「1億MAU超または月商$20M超の事業者にのみモデル名表示を義務づけるだけで、国内の一般的な事業会社には実質フリー」。競合用途の制限有無という重要な点で食い違うため、実案件で使う前にライセンス原文の確認が必要。
- **不一致: Kimi K3 の配布サイズ**: 両ソースとも「MXFP4 約594GB」説と「4bit 約1.4TB」説の併存を認めており、公式値は未確定のまま（07-27 から進展なし）。
- **不一致: Kimi K3 の実行要件**: Master は「Moonshot 推奨は64アクセラレータ以上のスーパーノード」、industry は「MXFP4 でも最低8基の H100 クラス、フル精度なら8ノード×8基」。下限と推奨で整合しうるが、提案で引用する際は前提を明記すること。
- **一次情報の公開先が割れている（Copilot）**: Power Automate モバイルアプリの廃止は learn.microsoft.com（en-us / ja-jp）と Learn 検索インデックスに存在する一方、`MicrosoftDocs/power-platform` の GitHub main には未反映（`ms.date` は 05/22/2026）。Learn 側が先行公開される事例として記録。
- **台帳番号の衝突（再発）**: Master の B-013（403 の2分類記録）と Copilot の B-013（Partner Center 月次アナウンスの追加）は別台帳の同番号。07-27 の B-012 衝突に続く2例目で、横断参照時は必ずソース名を添えること。
- Master: 新規提案 B-015（Hugging Face をオープンウェイト系の一次ソースとして `daily-sources.md` に追加）。継続提案2件（最多は B-013、2回目）。
- Copilot: 新規提案 B-013（Partner Center 月次アナウンスを週次ソースに追加）、B-014（Learn MCP 単独検知時の裏取り手順を `fetch-flow.md` に明文化）。継続提案6件（最多は B-011 Power Platform Blog のトピック記事照合、9回目）。
- industry: 新規提案 B-005（二次情報で数値が食い違う場合の記載ルールを `fetch-flow.md` に追加）。継続提案1件（B-004 取得方法の WebSearch 優先化、29回目）。
- **障害の変化: Master**: `huggingface.co` / `www.kimi.com` / `docs.devin.ai` / `devin.ai` / `www.tomshardware.com` の5ホストを新たにゲートウェイ拒否（CONNECT 403）と判定。WebFetch は一律「HTTP 403 Forbidden」としか返さず2分類を区別できないため、curl による判定を経て確定した（B-013 に追記）。
- **障害の変化: Copilot**: `learn.microsoft.com` の WebFetch 直取得が 403 になり、MS-4005 コレクション API（`/api/lists/`）も取得不可。Learn MCP で回避できるが MS-4005 のみ代替がなく、本日は週次確認をスキップした。`mc.merill.net` も 403。
- **障害の変化: industry**: WebFetch の 403 が Hugging Face のモデルカードなど一次情報ページにも拡大し、実質全滅に近い状態。Kimi K3 のライセンス・配布サイズの数値が二次情報間で割れたまま確定できない直接の原因になっている。
- 前日（07-27）分の欠損リカバリは対象なし（3ソース統合で生成済み）。
