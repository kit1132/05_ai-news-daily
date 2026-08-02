# AI News Daily Summary — 2026-08-03

月曜は Anthropic の期限2本が主題になった。Sonnet 5 の導入価格は 8/31 で終わり、単価+50% に計上トークンの増加が上乗せされる。旧 Workbench は 8/17 に退役し、保存したプロンプトと評価は手動で退避しないと消える。あわせて DeepSeek-V4-Flash-0731 の重み公開が前日の両論併記から MIT 確定へ動き、Copilot は Web グラウンディングからサイト単位で最大1,000件を除外できるようになった。Microsoft の一次ソースはそれ以外ほぼ据え置きで、7月 GA 予定だった Power Platform の7機能は8月に入って3日が経っても未 GA のままである。

## 今日のハイライト

### 1. Claude Sonnet 5 の導入価格が 8/31 で終わる — 単価+50% に計上トークンの増加が上乗せされる

**要点**: 導入価格 $2/$10 が **8/31** で終わり、9/1 から標準 **$3/$15** へ移る。新トークナイザが同一入力で最大35%多く計上するため、9月分の試算前提は「単価+50%」から「実質はそれ以上」へ変わる。

**詳細**: 6/30 の Sonnet 5 投入時に告知された導入価格（入力$2／出力$10・100万トークンあたり）の期限が 8月31日にあたる。9/1 からの標準単価は入力$3／出力$15 で、レートだけで+50%。月間1,000万トークンの負荷は $20→$30、10億トークンなら $2,000→$3,000 になる。標準単価そのものは Sonnet 4.6 と同水準だが、Sonnet 5 は新しいトークナイザを採用しており、同じ入力で**最大35%多いトークン**が計上される場合がある。レートカード上は Sonnet 4.6 と横ばいに見えても、請求トークン数が増えるぶん実効コストはさらに上がる。⚠️ 35% の値は FinOps 系の二次情報が根拠で、一次の価格ページには記載がない。

- https://www.anthropic.com/news/claude-sonnet-5
- https://platform.claude.com/docs/en/about-claude/pricing
- https://finopsllm.com/research/sonnet-5-intro-pricing-deadline
- https://www.finout.io/blog/claude-sonnet-5-pricing-2026-the-hidden-costs-and-real-savings-behind-the-cost-neutral-launch

### 2. Claude Console の旧 Workbench が 8/17 に退役する — 保存プロンプトと評価は手動で退避しないと消える

**要点**: 旧 Workbench と実験的プロンプト API 3種が **8/17** に retire する。更新版は保存プロンプト・変数・評価を引き継がないため、前提は「移行すれば済む」から「期限内にエクスポートしないと失う」へ変わる。

**詳細**: 対象は `platform.claude.com/workbench` の旧版と、あわせて廃止される実験的プロンプトツール API 3種である。

- `/v1/experimental/generate_prompt`: プロンプト生成
- `/v1/experimental/improve_prompt`: プロンプト改善
- `/v1/experimental/templatize_prompt`: プロンプトのテンプレート化

更新版 Workbench は保存済みプロンプト・変数・評価（evals）に非対応で、8月17日以降は保存済みコンテンツへアクセスできなくなる。エクスポートは Workbench 上のバナーまたは Organizational Settings から実行する。プロンプトの生成・改善・テンプレート化を CI やスクリプトへ組み込んでいる場合は、データ退避に加えて API 側の代替実装も同じ期限までに要る。当リポジトリではこれまで日付一覧に1行載せていただけで、移行時に何が引き継がれないかを記録したのは本日が初めてである。

- https://platform.claude.com/docs/en/release-notes/overview
- https://support.claude.com/en/articles/8606378-how-do-i-use-the-workbench

### 3. DeepSeek-V4-Flash-0731 の重みが MIT で公開済みと確定した — 前日の「API 限定かもしれない」という留保が消えた

**要点**: DeepSeek が 7/31 に V4-Flash-0731 の重みを Hugging Face へ **MIT** で公開していたことが確定した。前日のサマリーで両論併記にしていた重み公開の可否が決まり、ローカル実行が検討対象に入る。

**詳細**: 08-02 時点では Industry 側が「MIT ライセンスでウェイト公開」、Master 側が「0731 は API 限定」とする二次情報を挙げて割れており、未確定として両論併記していた。本日 `deepseek-ai/DeepSeek-V4-Flash-0731` のモデルカードが一次 URL として検索結果に現れ、複数の二次情報が「7/31 に MIT で重み公開」で一致した。前日に傍証として挙げた第三者量子化 `unsloth/DeepSeek-V4-Flash-0731-GGUF` に加え、`Vontra/DeepSeek-V4-Flash-0731-MXFP4-MLX` と非量子化の `unsloth/DeepSeek-V4-Flash-0731` も確認できた。新しく分かった構造上の点として、配布チェックポイントには DSpark 投機的デコードモジュールが同梱されており、HF リポジトリが表示する 304B はこのドラフトモデルを含んだ値である（本体は 284B 総 / 13B アクティブ）。⚠️ `huggingface.co` はゲートウェイ拒否が続いておりモデルカード本体は読めておらず、数値は二次情報の一致による。

- https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-0731 （一次・未到達）
- https://benchlm.ai/blog/posts/deepseek-v4-flash-0731
- https://www.marktechpost.com/2026/07/31/deepseek-upgrades-deepseek-v4-flash-0731-with-major-agentic-and-coding-gains/

## カテゴリ別まとめ

### Anthropic / Claude

- Sonnet 5 の導入価格終了と旧 Workbench の退役（ハイライト参照）
- Anthropic は Claude Code を9日連続で更新していない — 最新は v2.1.220（7/25）のままである。Claude Platform の release notes も 7/24 エントリが最新で、7/25 以降10日間追加がない。一次 changelog の取得自体は本日も成功しているため、取得失敗ではなくリリースが出ていない状態にあたる。
  https://code.claude.com/docs/en/changelog
- Anthropic と Blackstone らの $1.5B 合弁 Ode が7月中旬に事業を開始していた（本日検知・当リポジトリ未追跡）— 5月に発表された JV が独立した AI 実装会社として立ち上がり、エンジニア100名で始動した。Blackstone がポートフォリオ企業への AI 導入で評価していたブティック企業 Fractional AI を買収して基盤とし、同社共同創業者の Chris Taylor が CEO、Eddie Siegel が CTO に就いた。「Claude ファースト」を原則としつつ顧客要件に応じて他社製品も使う方針で、対象は中堅の銀行・医療システム・製造業。出資には Goldman Sachs・General Atlantic・Apollo・GIC・Sequoia が並ぶ。
  https://www.technology.org/2026/07/16/ode-with-anthropic-blackstone-ai-implementation/

### OpenAI

- OpenAI が Astra の数学的成果に機械検証可能な証明書を添えて公開した（8/1・続報）— 8/2 収録の「未解決問題10件を解いた」に対し、本日新たに分かったのは検証手段と公開形態である。AI の数学的主張は「論文を人が査読するまで保留」から「Lean 4 証明書が通るかどうかで即判定できる」ものへ変わった。
  https://openai.com/index/ten-advances-in-mathematics/ （一次・未到達）
  - 公開形態: プレスリリースを出さず、249 ページの原稿と全結果に対応する Lean 4 証明書を GitHub へ Apache 2.0 で置いた
  - コスト: トークン消費は Sol の API 料金換算で約 **$2,000** 相当と説明されている
  - 主な結果: 非ソフィック群の初の明示的構成（Gromov が 1999 年に soficity を導入して以来の群論の中心問題）、Connes の剛性予想の反証、Ehrhart の体積予想の証明、高次元球充填密度の一般上界を 1978 年以来はじめて改善、2プレイヤー量子ゲームの並列反復定理、パーマネントの回路計算量の新しい下界、Erdős の問題集から3問
  - 位置づけ: Astra は既存の Sol / Terra / Luna と並ぶ新しいモデルクラスで、複数エージェントが数時間〜数日かけて協調する設計とされる。GPT-6 と名付けるか GPT-5 系にするかは未決定で、公開時期も未定。Altman はワシントンで政策当局者に実機デモを済ませている
  - ⚠️ 一次の `openai.com` はゲートウェイ拒否で本文に到達できておらず、上記は二次報道の一致による
- OpenAI は Codex CLI を3日間更新していない — 安定版は 0.146.0（7/29）、pre-release も 0.147.0-alpha.4（7/31 17:54 UTC）が最新のままである。
  https://github.com/openai/codex/releases

### Google / DeepMind・xAI

- Gemini 3.6 Flash / 3.5 Flash-Lite / 3.5 Flash Cyber の 7/21 公開が公式ブログで裏づけられた — 当リポジトリでは 7/21 以降「出典の信頼性が低く未確認」として保留してきたが、`blog.google` 配下の告知 URL が検索結果に現れ 9to5google の同日記事とも一致したため、確定扱いへ切り替えた。10日以上保留していた前提が解けたことになる。
  https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-6-flash-3-5-flash-lite-3-5-flash-cyber/
  - 価格: 入力 $1.50 / 出力 $7.50 per 1M。3.5 Flash の出力 $9.00 から **17% 減**で、出力トークン数自体も約17%減る
  - ベンチ: SWE-Bench Pro 58.7%（3.5 Flash 55.1%）、OSWorld Verified 83%（同 78.4%）。長文脈検索も改善した
  - 仕様: 知識カットオフが 2026-03 まで前進し、`temperature` / `top_p` / `top_k` は非推奨になった。1M コンテキストは維持される
- Gemini 3.5 Pro の GA は未達のままで、Vertex AI 限定 preview が続いている。公開 API の GA 済みフラッグシップは引き続き Gemini 3.1 Pro である。
- Google が AI Studio のモバイルアプリを中止した（7/31 発表）— iOS / Android で約 **80万件** の事前登録を集めていた単体アプリの提供を取りやめ、アプリ生成機能を Gemini アプリ（モバイル・デスクトップ）へ統合する。AI Studio の Web 版は「プロンプトから本番アプリまで」を担う面として投資を継続する。単体ツールを畳んで主力アシスタントへ集約する動きで、07-31 収録の「汎用チャットボットから組み合わせ可能な部品へ」とは逆向きの再統合にあたる。ツール単位で導入を積み上げる構成は、ベンダー側の統廃合で入り口が変わる。
  https://9to5google.com/2026/07/31/gemini-ai-studio-app/
- xAI の Grok 4.6 は 8/7 前後という目標時期から動いていない — Grok 4.5 と同じ 1.5T の V9 基盤を再利用し、SFT と RL の改善で伸ばす位置づけとされる。後続の 2.1T Grok 4.7 は数週間後になる。⚠️ SEO 系サイトが「8/7 に launched」と完了形で書き始めているが、本日は 8/3 であり公開の裏づけはない。
  https://aitoolsreview.co.uk/insights/grok-4-6-grok-4-7-release-date

### Microsoft / Copilot Studio / Power Platform

- 管理者が Copilot の Web グラウンディングから最大 **1,000ドメイン**を除外できるようになった — Web 参照を丸ごと許可するか無効化するかしかなかった前提が、参照先を名指しで絞る運用へ変わる。7/27 に MC1411435 の一部として1行だけ触れていたが、一次ページで仕様を確認したのは本日が初めてである。
  https://learn.microsoft.com/en-us/copilot/domain-exclusion
  - 対象と実行: Microsoft 365 Copilot と Copilot Chat の両方が対象で、`ConfigureTenantDomainExclusions.ps1`（`aka.ms/Copilot/DomainExclusionScript`）を Search 管理者または全体管理者の資格で実行する
  - CSV 仕様: `Domain` と `IncludeSubPages` の2列が必須で、1ファイルあたり最大1,000件、サブドメインは2階層まで
  - 運用上の注意: 既定では除外設定そのものが無いオプトイン方式で、更新は差分追加ではなく既存設定の置き換えになる。除外が効くのは Web ページ結果のみで、ニュース等の他バーティカルからは引き続き引用され得る
- Tech Community の月次記事「What's New in Microsoft 365 Copilot | July 2026」は公開済みだった — 8/2 時点で「未公開のまま7月終了」と記録していた判定が誤りで、月次記事の検知が board RSS の 403 で止まっていたことが判明した（記事ID 4538332）。掲載内容の大半は既報だが、次の2点は未掲載だった。⚠️ techcommunity は本文取得も 403 のため、下記は二次要約を根拠とする一次未確認である。
  https://techcommunity.microsoft.com/blog/microsoft365copilotblog/what%E2%80%99s-new-in-microsoft-365-copilot--july-2026/4538332
  - Copilot Chat のプロンプトから Word / Excel / PowerPoint エージェントを `@` メンションで直接呼び出せるようになり、Copilot アプリを離れずに文書・表・スライドを作成できる
  - Copilot の回答が簡潔化され、サイドバーの Copilot Chat で会話を続ける導線が目立つ位置へ移った
- Microsoft が Copilot を単一アプリへ統合すると表明した（7/29 決算コール・Nadella / 本日検知）— チャット・Cowork・エージェント型 Autopilot・コードを1つのアプリにまとめる構想で、消費者向けと商用の双方が対象になる。有料の AutoPilot エージェント階層の追加も計画されている。同時に、M365 Copilot の有料シートが **3,000万超**に達し、純増シート数が前四半期比で2倍以上になったことが開示された。
  https://techweez.com/2026/07/30/microsoft-unified-copilot-app-2026/
- Microsoft の一次ソースは本日いずれも据え置きだった — M365 Copilot Release Notes は「July 29, 2026」節が先頭のままで対象期間 7/15〜7/29 の全10項目に増減がなく（次バッチは隔週傾向なら8月中旬）、拡張機能 What's New も「July 2026」節の2項目のままで8月節が立っていない。Copilot Studio What's New は June 2026 節の10項目から動かず、基盤ビルドも 2026.6.3（6/30 初出）でリージョン分布が変わらない（次の火曜定例更新は 8/4）。M365 Blog 本体は 7/30 記事、M365 Roadmap の Latest announcements は 7/9 の GPT-5.6 が最新のままである。
  https://learn.microsoft.com/en-us/copilot/microsoft-365/release-notes
- 7月 GA 予定だった Power Platform の7機能は、8月に入って3日が経ってもいずれも GA が反映されていない — Release Wave の General availability 列に新しい緑チェックは付かず、直近の GA は 7/16 の3機能（PGP 暗号化・復号、時間/コスト削減の自動計測、チェッカーの管理者通知）から増えていない。Power Platform Blog も月次「What's New」の7月号を出さないまま8月に入り、最新は 6/11 の June Feature Update のままである。
  https://learn.microsoft.com/en-us/power-platform/release-plan/2026wave1/power-automate/planned-features
  - Power Automate（5件）: 削除したクラウドフローの復元、Process ライセンス容量の複数ワークフロー間での共有、統合 Power Apps によるフォーム UI、ワークキュー項目の CSV エクスポート、マシン・フロー稼働率のダッシュボード表示
  - Power Apps（2件）: code apps のコネクタ CLI 対応、FetchXML エディターでのオフラインプロファイル構成
- ガバナンス側は動きが小さい — Purview の What's new は7月節に Copilot 関連の新規項目が追加されておらず、Power Platform の非推奨一覧も先頭が Power Automate モバイルアプリの廃止（8/31 発効）のままである。Partner Center の8月アナウンスページ（`announcements/2026-august`）は本日も 404 で、8/1 に CSP 提供が始まった SMB 向け「Copilot in 30」（25ユーザー・30日）以降の変更は確認できていない。
  https://learn.microsoft.com/en-us/power-platform/important-changes-coming

### 開発ツール

- Microsoft が MCP の C# SDK を v2.0 として GA した（7/28）— 仕様 `2026-07-28` のステートレス既定・標準 HTTP ヘッダ・Multi Round-Trip Requests を実装しつつ、`2025-11-25` 以前とネゴシエートする相手との後方互換を保つ。廃止対象（roots / sampling / logging）は `[Obsolete]` 属性つきで残され、置き換え先が示される。Python / TypeScript / Go は beta 段階のままで、**Tier 1 のうち GA に到達したのは C# が最初**である。
  https://devblogs.microsoft.com/dotnet/announcing-v20-of-the-official-mcp-csharp-sdk/
- GitHub は Copilot CLI を2日間更新していない — pre-release v1.0.78-2（8/1 04:18 UTC）と安定版 v1.0.77（7/30）から動きがなく、`changelog.md`（main）側の最新見出しも 1.0.77 で releases ページと一致している。
  https://github.com/github/copilot-cli/releases
- Cursor と Cognition の Devin はいずれも日付を確定できる新規リリースを検出できなかった（7/30 以降）— Cursor は既報の iPad 対応と PR レビュー刷新（7/29）が最新で、Devin は Devin Outposts（7/21 alpha）が最新のままである。

### オープンウェイト / ローカル LLM

- Thinking Machines が Inkling-Small をオープンウェイトで公開した（7/30・当リポジトリ未追跡）— 276B 総 / **12B アクティブ**の MoE で、42層デコーダ・256 エキスパートのうち6個＋共有2個にルーティングする構成をとる。1M コンテキストと minimal〜xhigh の thinking effort を持つ。ベンチは上位版 Inkling（975B 総 / 41B アクティブ）を上回り、SWE-bench Verified 80.2%（Inkling 77.6%）、Terminal Bench 2.1 64.7%（同 63.8%）。重みは Hugging Face で配布され、Tinker で fine-tune、Tinker Playground でテキスト・画像・音声のチャットが試せる。
  https://thinkingmachines.ai/news/inkling-small/
- LG AI Research が韓国最大の 750B モデル K-EXAONE 2.0 を Apache 2.0 で公開した（7/31）— ハイブリッドアテンションの MoE 構成で、総パラメータ **750B**・1トークンあたりアクティブ約37B。24ベンチマークの平均が 70.1 で、K-EXAONE 1.0 の 63.3 から10%超改善した。長文脈検索と安全性の伸びが大きい。ライセンスに商用利用の追加条件がなく、Kimi K3 の独自ライセンス（07-28 収録）や中国製オープンウェイトとは調達上の位置づけが異なる。韓国政府のソブリンAI基盤モデル事業では LG AI Research / SK Telecom / Upstage の3陣営が第2段階に進んでおり、Naver Cloud と NC AI は2026年1月に脱落済みである。モデル出自の分散を求める官公需・防衛系の提案で代替経路になる。
  https://huggingface.co/LGAI-EXAONE/K-EXAONE-2.0-750B-A37B
  https://www.koreatimes.co.kr/business/tech-science/20260731/lg-unveils-750-bil-parameter-frontier-ai-model-k-exaone-20
- DeepSeek-V4-Flash-0731 の重み公開確定（ハイライト参照）

### 規制・政策

- 米政府のフロンティアモデル事前審査枠組みは 8/1 の期限を越えて未公表のままである — EO 14409（6/2 署名）が課した60日期限は 8/1 に満了したが、本日時点でも Federal Register 告示・NIST / CISA 公表・OSTP 声明のいずれも確認できていない。整備対象は「covered frontier model」の判定を行う機密ベンチマーク手続きと、公開前審査の任意枠組みの2点である。
  https://www.lw.com/en/insights/president-trump-signs-executive-order-establishing-ai-cybersecurity-and-frontier-model-framework
  https://vorplabs.com/ai-regulatory-updates/frontier-model-review-framework
  - 枠組みの中身: 政府が公開前に最大30日モデルへアクセスでき、審査は商務省 CAISI と NSA が担当する見込み。判定基準は機密のままで、開発者にも外部研究者にも閾値は開示されない
  - 関与状況: TRAINS の事前展開評価に参加する OpenAI・Anthropic・Google・Microsoft・xAI の5社が CVSS を模した jailbreak 深刻度スコアの共通化も進めている。Meta は不参加で、対象モデル判定は NSA 長官の単独権限という構図も 08-02 から変わらない
  - 影響: OpenAI の Astra がこの経路を通る第1号になる見込みで、枠組みの公表時期がフロンティアモデルの公開スケジュールに直結する
- EU AI Act 第50条について、本日は執行主体と対象範囲の細目が追補された（発効は 8/2・既報）— 執行は主として各国の市場監視当局が担い、透明性義務は ① 人との直接的なやり取り ② AI 生成コンテンツ ③ 感情認識・生体分類 ④ ディープフェイクと公共的関心事項に関する AI 生成テキスト、の4領域に掛かる。制裁は最大 1,500万ユーロまたは全世界年商 3% の高い方。8/2 より前に市場投入済みの生成 AI システムは 2026-12-02 まで標識要件への適合が猶予される。
  https://www.stibbe.com/publications-and-insights/the-ai-acts-transparency-obligations-rules-scope-and-timeline
- NVIDIA が Open Secure AI Alliance を発足させた（7/27・当リポジトリ未追跡）— 37 社が参加し、AI の脆弱性を検出・修正するオープンツール群と NOOA フレームワークをオープンソース化する。創設メンバーには Microsoft・Salesforce・Databricks・IBM・Hugging Face・Cisco・Palo Alto Networks・Cloudflare が並ぶ一方、**OpenAI・Google・Anthropic はいずれも不参加**である。発足は OpenAI の自律テストエージェントが Hugging Face を侵害したインシデントを受けたもので、7/30 公表の Anthropic のサイバー評価インシデントと同じ流れに位置する。
  https://thehackernews.com/2026/07/nvidia-forms-37-member-open-secure-ai.html

### 市場・エコシステム

- 生成AIのトラフィックシェアで ChatGPT が5割台へ下がったと複数媒体が報じている — 1年前の約76〜86%からの低下で、**数値は二次情報で割れている**。ChatGPT 53.9%／Gemini 27.9%／Claude 9.2%（7月報道・5月データ）とする系統と、ChatGPT 52.7% とする系統がある。下位は DeepSeek 4.1%・Grok 2.4%・Perplexity 1.3%・Microsoft Copilot 1.3%。総量では2025年6月〜2026年5月の月間平均訪問が 95億回（前年比+70%）、ユニーク訪問者が 6.55億人（+57%）で、訪問の伸びがユーザー数の伸びを上回る＝既存ユーザーの利用頻度が上がっている。Similarweb の一次ページは 403 で確認できず二次情報のみのため幅で記載する。シェア推移を引用する場合は計測期間（5月データ）を明記して使う。
  https://ppc.land/chatgpt-drops-to-52-7-as-claude-triples-its-ai-traffic-share/
- GitHub Trending はエージェント基盤とビジュアルビルダーが上位を占めている — OpenClaw が約9,000スターから **38.2万スター**超へ伸び、2026年で最も伸びた OSS になった。ほかに Langflow（14.6万）・Dify（13.6万）・Flowise（5.1万）のビジュアルビルダー群、MetaGPT / LobeHub / CrewAI / AutoGen のマルチエージェント協調系、400超の連携を持つ n8n が上位に入る。自律的な多段処理への問い合わせは直近1年で1,400%超増えた。自前構築の選択肢が増えたぶん、OSS 採用時のライセンス（n8n は fair-code）と運用主体の切り分けが提案の論点になる。
  https://ossinsight.io/trending/ai
- Product Hunt の上位は音声・スケジュール・リポジトリ常駐型に寄っている — 8月のローンチでは Bolcho AI（806票）と TimeOS 2.0（671票）が上位に立った。エージェント分野では音声・SMS でのアウトリーチと日程調整を担う Leaping AI、リポジトリ常駐のメモリをエージェントへ与える MemoryCustodian など、既存の業務動線に入り込む設計が続く。プライバシー重視のデスクトップ常駐型・業種特化のワークフロー自動化・統制されたデータアクセスの3方向にクラスタが分かれており、08-02 収録の「埋め込み先の争奪」の継続にあたる。個別ローンチ日の特定は困難のため幅表現とする。
  https://www.producthunt.com/categories/ai-agents

## 直近の注目予定

- **8/3（本日）**: 旧「Claude in Slack」退役 ／ Copilot Billing Preview app 廃止 ／ 週次復旧チェック実施日（実施済み・全ソース未復旧） ／ iOS 27 developer beta 5（予想）
- **8/4**: Copilot Studio Released Versions・Release Wave・非推奨一覧・拡張機能 What's New の定例更新 ／ Gemini Enterprise の global リージョンから Gemini 3.5 Flash を除外（一次未確認）
- **8/5**: Opus 4.1 の Claude API 退役 ／ Cowork 倍増利用枠終了
- **8/6**: ChatGPT Business の利用無償期間終了（以後は柔軟課金へ）
- **8/7 前後（推定）**: Grok 4.6（1.5T）
- **8/9**: ChatGPT Atlas シャットダウン
- **8/17**: Claude Console 旧 Workbench 退役 ＋ 実験的プロンプトツール API 廃止（ハイライト参照） ／ Gemini API 画像生成モデル停止（一次未確認）
- **8/18〜9/8**: Microsoft 365 Copilot Agent's Playbook ライブストリーム（各回 9AM PT）
- **8/19**: Claude Code 週次上限50%増の終了
- **8/20**: Gemini Enterprise Agent Platform の Grok 4.1 ファミリー停止（一次未確認）
- **8/26**: OpenAI Assistants API 廃止 ／ o3 退役 ／ GPT-4.5 完全廃止 ／ Copilot 既定モデル有効化ポリシー発効
- **8/31**: Sonnet 5 導入価格終了（→ $3/$15・ハイライト参照） ／ Power Automate モバイルアプリ廃止 ／ `gemini-robotics-er-1.6-preview` 停止（一次未確認）
- **8月上旬**: Partner Center 8月アナウンスの公開（本日時点で 404） ／ Power Platform Weekly の夏季休刊明け
- **8月中旬**: M365 Copilot Release Notes 次バッチ見込み（7/29 バッチから隔週）
- **8月見込み**: 7月 GA 予定から持ち越した Power Platform 7機能
- **9月**: iOS 27 / macOS 27 GA（AFM 3 本番）
- **11/12**: EU AI ギガファクトリー入札の応募締切
- **12/2**: EU AI Act の生成コンテンツ標識義務、8/2 以前に市場投入済みシステムへの猶予が終了

## 改善メモ

- B-021（Master・新規）: `curl` で 403 が返っても WebFetch は成功するホストがあるため、403 判定手順に WebFetch の成否確認を前置する
- B-022（Master・新規）: ChatGPT / Codex 公式 changelog `learn.chatgpt.com/docs/changelog` をソースに追加する
- B-021（Copilot・新規）: Tech Community 月次記事の公開検知が board RSS の 403 で止まり、月初の照合手順が未定義である。B-019（Release Notes）・B-020（M365 Blog 本体）と同じ「単一の取得経路が最新項目を落とす」類型にあたる
- Industry: 新規提案なし
- 継続提案: Master 6件（最多 B-013 8回目）、Copilot 12件（最多 B-011 15回目）、Industry 5件（最多 B-004 35回目）
- 障害: Master が週次復旧チェックを実施し、ゲートウェイ拒否16ホストと `www.anthropic.com` のオリジン403はいずれも未復旧と判定した。新規のゲートウェイ拒否は `learn.chatgpt.com` / `thinkingmachines.ai` / `cognition.com` / `devblogs.microsoft.com` / `blog.google` / `gemini.google` / `docs.cloud.google.com` / `the-decoder.com` の8ホスト。Industry は `techtimes.com` を WebFetch 広範403 の対象に追加した
- 前日からの持ち越し解消: 08-02 に両論併記した DeepSeek-V4-Flash-0731 の重み公開は、本日 Master 側が「MIT で公開済み」に確定させた（ハイライト参照）。一次の `huggingface.co` は未到達のままで、二次情報の一致による確定である
- ソース間の差分: EO 14409 について、Master は枠組みの中身（公開前最大30日アクセス・CAISI と NSA が担当・5社による jailbreak 深刻度スコアの共通化）を、Industry は 8/1 期限超過後も Federal Register / NIST / CISA / OSTP のいずれにも告示がない事実を持っていた。いずれも他方には無い情報のため両方を採用した
- ソース間の矛盾: 本日は確認されなかった
