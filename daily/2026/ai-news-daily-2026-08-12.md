# AI News Daily Summary — 2026-08-12

水曜は「消えた期限」と「増えた期限」が同時に出た日である。Anthropic は 8/31 に終わるはずだった Sonnet 5 の導入価格をそのまま恒久価格にし、9/1 の値上げを取り消した。代わりに GitHub が MAI-Code-1-Flash に 9/10 の退役日を付け、同じ日に定価73%減の後継を出している。Anthropic はさらに、生成物への不可視ウォーターマークを全世界へ適用し、Compliance API の取得範囲を利用者の端末で動く Claude Code / Cowork にまで広げた。Microsoft 側は Agent 365 の月次記事が出所で、レジストリの他社エージェント同期・マルチテナント管理・Copilot Credit のコスト管理が一度に動いている。

## 今日のハイライト

### 1. Sonnet 5 の $2/$10 が恒久価格になった — 9/1 値上げ前提の費用試算は引き直しになる

**要点**: Anthropic が Sonnet 5 の導入価格 $2/$10 を恒久価格へ切り替え、9/1 に予定していた $3/$15 への値上げを取り消した。入出力とも50%上がる前提で組んだ費用試算は、据え置き前提へ引き直すことになる。

**詳細**: 公式 pricing ページに「launch 時に 2026年8月31日までの導入価格として告知した $2/$10 は now the standard price であり、2026年9月1日に予定していた $3/$15 への引き上げは実施しない」という注記が入った。API release notes 側の掲載日は **8/10**、Claude 公式アカウントの告知は 8/11 である。現行の単価は次のとおり。

- 通常: 入力 **$2 / MTok**、出力 $10 / MTok
- Batch API（50%割引）: 入力 $1 / MTok、出力 $5 / MTok
- プロンプトキャッシュ: 5分書き込み $2.50、1時間書き込み $4、キャッシュヒット $0.20

比較対象の Sonnet 4.6 / 4.5 は $3/$15 のまま据え置かれているため、Sonnet 5 が旧世代より安い状態が恒久化したことになる。⚠️ 本サマリーは 08-11 まで「8/31 に促進価格終了 → $3/$15」を直近の注目予定に載せてきたが、この期限は消滅した。本日分から記載を外している。

- https://platform.claude.com/docs/en/about-claude/pricing
- https://platform.claude.com/docs/en/release-notes/api
- https://www.techmeme.com/260810/p42

### 2. Claude の生成物に不可視ウォーターマークが入る — 出力の来歴が既定で残る前提に変わる

**要点**: Anthropic が Claude の生成テキストへ不可視の機械可読マークを埋め込み、画像等のファイルに C2PA 署名を付ける運用を公表した。API・Claude Code・Cowork が対象で、オプトアウトの記載はなく全世界に適用される。

**詳細**: EU AI Act 第50条（8/2 発効）の透明性義務に対応する措置で、Anthropic は EU の Code of Practice に署名している。適用範囲は次のとおり。

- 対象プロダクト: Claude Platform（API）／ Claude ／ Claude Code ／ Claude Cowork ／ Claude Tag、および AWS・Google Cloud・Microsoft Foundry 経由の各版
- 対象モデル: **2026年8月2日以降**にローンチする新モデルは launch 時点で対応する。それ以前の既存モデルへの後付けは作業中で時期は未提示である
- テキスト: 生成文そのものに知覚できない信号を織り込む。通常の閲覧では見えず、コピー&ペーストしても残るが、大幅な書き換えでは劣化する
- ファイル: `.svg` / `.png` / `.jpg` に C2PA 準拠の署名付き来歴メタデータを付与する。プラットフォームごとに対応の程度は異なる

Anthropic は限界も明記している。マークが検出されても「Claude が処理した可能性」しか示さず著者性を確定せず、逆にマークが無くても AI 生成でない証明にはならない（編集・翻訳・メタデータ除去・旧モデル生成のいずれもあり得る）。利用者と第三者が透かしを検出・検証するための技術文書は「今後公開」とされ、本日時点で未公開である。Article 50 の違反には最大 **€15M** または全世界年間売上の3%の制裁が定められている。

- https://support.claude.com/en/articles/16266773-how-claude-marks-ai-generated-content
- https://techcrunch.com/2026/08/11/anthropic-says-it-will-watermark-text-generated-by-its-ai-models/
- https://the-decoder.com/anthropic-watermarks-all-claude-outputs-globally-with-marks-that-may-persist-through-some-editing/

### 3. Copilot の MAI-Code-1-Flash が 9/10 に退役する — モデル名を固定した設定は書き換えが要る

**要点**: GitHub が MAI-Code-1-Flash の 9/10 退役と、後継 MAI-Code-1.1-Flash の提供開始を同日に告知した。後継は定価が73%安い一方、モデル名を直接指定した設定やワークフローは期日までに書き換えが要る。

**詳細**: 8/11 の Changelog 2本での告知である。**MAI-Code-1-Flash は 9月10日**に全 Copilot 体験から外れ、それまでにワークフローと連携先を新モデルへ更新するよう案内されている。後継の MAI-Code-1.1-Flash は前版に画像理解（native vision）が加わり、コード品質・指示追従・ツール利用が改善した。価格は前版比 **73% 低いリスト価格**で、年額 Copilot 契約者には 0.25× の premium request 倍率が適用され、それ以外は従量課金となる。

- 提供対象: Free / Student は自動モデル選択経由、Pro / Pro+ / Max / Business / Enterprise は手動・自動の両方で選べる
- ⚠️ Business / Enterprise は既定でオフのため、管理者が Copilot 設定でモデルポリシーを有効化するまで選択肢に出ない
- 対応面: Copilot CLI、クラウドエージェント、GitHub Copilot アプリ、GitHub 上の Copilot Chat、VS Code、Visual Studio、GitHub Mobile、JetBrains IDE、Eclipse、Xcode

- https://github.blog/changelog/2026-08-11-upcoming-deprecation-of-mai-code-1-flash/
- https://github.blog/changelog/2026-08-11-mai-code-1-1-flash-available-in-github-copilot/

## カテゴリ別まとめ

### Anthropic / Claude

- **Compliance API がローカルセッションを返すようになった（8/11・beta）**: Anthropic が Enterprise 向けに、利用者の端末で動く Cowork と Claude Code のセッション文字起こしを取得できるようにした。「ローカル実行なら組織側に残らない」という前提が崩れる
  - エンドポイントは3本で、組織全体のセッション一覧（`/v1/compliance/apps/sessions/local`）、1セッションのメタデータ（`.../{session_id}`）、文字起こし本体（`.../{session_id}/messages`）である
  - 取得できるのはプロンプトと応答、ツール呼び出し（web・MCP）の中身、skills と artifacts の中身、検証済みユーザー資格情報・組織ID・セッションID・タイムスタンプになる
  - 除外は Claude Code on the web、Claude Platform 経由の Claude Code、Bedrock / Vertex AI / Microsoft Foundry 上のセッションの3系統である
  - 既存の Compliance Access Key と `read:compliance_user_data` スコープでそのまま使え、追加の統合作業は要らない。8/3 に入った Cowork のリモートセッション対応に、ローカル実行側が加わった形になる
  - https://claude.com/blog/compliance-api-cowork-and-claude-code
- **Claude Code v2.1.227 がリリースされた（8/10 22:56 UTC）**: バグ修正と表示改善が中心で、破壊的変更は含まれていない
  - GitHub ホストランナー上で `allowed_non_write_users` を付けた `claude-code-action` の下で、Bash コマンドが全て失敗する不具合を修正した
  - 期限切れログイントークンでセッションを開始すると契約ティアを見ずに feature flag が評価され、Max プラン利用者へ Fable 用クレジットの有効化を誤って促す不具合を修正した
  - `/tui` が最初のメッセージより前まで巻き戻した会話を復元する問題も直り、スラッシュコマンドメニューは選択行のみ青字・一致文字は太字に変わった
- **既定権限モードの auto mode 切り替えは 8/14 に予定どおり実施される**（8/7 告知・既報）。対象は Pro / Max / Team で、管理は managed settings の `defaultMode` / `disableAutoMode`、分類器設定は `autoMode` の `environment` / `allow` / `soft_deny` / `hard_deny` である。⚠️ `"$defaults"` を配列に入れないと組み込みルールが消える。v2.1.227 に切り替えへ向けた挙動変更は入っていない
- Claude の利用枠に残る期限は1つになった。週次上限50%増は **8/19**（23:59 PT）までで、対象は Pro / Max / Team / シート課金 Enterprise である
- `support.claude.com` の Release Notes は 8/6 の skill / plugin セキュリティスキャン beta が最上位のままで、8/7〜8/11 の追加はない。⚠️ ウォーターマークの記事は同じホストにありながら Release Notes 一覧から辿れず、日付入りの検索で初めて検出できた
- 既報の破壊的変更2件（7/24）は継続している。Opus 5 で `thinking:{"type":"disabled"}` × effort `xhigh`/`max` は 400 を返し、Opus 4.7 の fast mode は廃止済みである

### GitHub Copilot

- **利用状況レポートにモデル別のトークン内訳が追加された（8/11）**: GitHub が入力・出力・キャッシュ読み込み・キャッシュ書き込みの各トークン数を、消費した AI クレジットと並べてモデルごとに出せるようにした。従来は課金額の合計しか見えずトークンの裏づけを追えなかったため、単価の議論を推計ではなく実測で回せるようになる。取得は課金設定の AI usage ページからレポートをダウンロードする形で、対象は Business / Enterprise の管理者と個人契約の全ユーザーである
  - https://github.blog/changelog/2026-08-11-per-model-token-breakdown-in-the-usage-report/
- MAI-Code-1.1-Flash の提供開始と MAI-Code-1-Flash の 9/10 退役（ハイライト参照）
- **Copilot CLI は v1.0.79（8/10 16:19 UTC）が最新のまま**で、8/11・8/12 の新版・pre-release は出ていない。同版の破壊的変更2件（`allowDevToolCaches` → `allowDevToolAccess`、`sandbox.gitAuth`/`ghAuth` → `sandbox.auth.git`/`auth.gh`）は既報のとおり対応が要る
- 既報の期限3件は動いていない。GitHub Spark の既存ユーザーアクセス終了が 8/31、既定モデル有効化ポリシーの発効が 8/26、全体験でのモデル廃止が 9/1 である

### Microsoft 365 / Agent 365

- **Agent 365 の Registry Sync が GA になった**: 管理者が Amazon Bedrock・Google Cloud Gemini・Anthropic Claude・Databricks Genie・Salesforce Agentforce のエージェントを Agent 365 レジストリへ同期できるようになった。テナント内のエージェント台帳が「Microsoft 製の一覧」から「全社の一覧」へ変わる
  - 同期は接続済みプラットフォームからエージェントとメタデータを日次または週次で取り込み、基盤側 API が対応する範囲では Agent 365 の画面からエージェント単位のガバナンス操作を直接実行できる
  - リスク可視化にセキュリティパートナー3社（**Cyera・Darktrace・Zenity**）のシグナルを統合し、紐づけは Microsoft Entra Agent ID を identity anchor として行う。リスクは High / Medium / Low に分類される
  - ⚠️ パートナー連携は任意で、管理者が有効化するまでパートナーへのデータ流入は発生しない
  - https://techcommunity.microsoft.com/blog/agent-365-blog/whats-new-in-agent-365-%E2%80%93-july-2026/4543654
- **マルチテナントのエージェント管理が Public Preview に入った（8/10）**: 管理者が統制下の複数テナントのエージェントを M365 管理センターの単一画面から棚卸し・追加・インストール／ブロックできるようになり、サインアウトも別管理者アカウントの維持も不要になった。対象は CSP ディストリビューター・CSP 間接リセラー・CSP 直接請求パートナーと SI / GSI で、既存のテナント間管理関係と GDAP のスコープ内に限られる。テナント固有のリスクとアクティビティのインサイトには Agent 365 ライセンスが必要になる
  - 同じ 8/10 に **Microsoft Entra Tenant Governance が GA** し、企業側がテナント間関係を構成する経路も揃った。GA 版は Related Tenants、Governance Relationships、Tenant Configuration Management、Secure Tenant Creation の4機能で構成される
  - https://learn.microsoft.com/en-us/partner-center/announcements/2026-august
  - https://techcommunity.microsoft.com/blog/microsoft-entra-blog/microsoft-entra-tenant-governance-is-now-generally-available/4543638
- **Copilot Credit の従量支出に M365 管理センターのコスト管理が付いた**: 管理者が従量課金型サービスのクレジット消費を監視・制御できるようになり、初期の対象は Cowork と Work IQ である。支出アラートの信頼性向上、ユーザー単位のオーバレージ処理の強化、各管理センター間での前払い容量の見え方の整理が入った。⚠️ 1人が複数ポリシーに属する場合はユーザー単位の上限が最も高いものが適用され、次いでポリシー上限の大きいもの、さらに作成日が新しいものの順で決まる
  - あわせて **Agent 365 ダッシュボードが GA** し、アクティブユーザー・リテンション推移・利用の多いエージェント・エンゲージメントの観点でドリルダウンできるようになった
- **CSP Copilot Partner Council コンテストが始まった（8/10）**: パートナーが M365 Copilot の顧客導入事例を応募し、20社が SMB Copilot Partner Council の席とニューヨークでの費用負担イベント（10/20〜22）への参加権を得る。⚠️ 応募期限は **8/31** で、応募には M365 Copilot を25席以上導入した証跡が必要になる。当選通知は 9/7〜9/11 である
- M365 Copilot Release Notes は July 29, 2026 バッチが先頭のままで、8/11 から変化がない。次バッチは隔週傾向どおりなら8月中旬見込みである。M365 Roadmap の Latest announcements も 7/9 のままで、Coming soon の Researcher と Frontier 枠4件にも変化はない
- Message Center の一次取得はゲートウェイ拒否で5日連続できていない。検索索引には Planner Agent チャットの基本プラン展開（MC1443514・8月下旬開始〜9月下旬完了）、Word の Legal Agent の8月中旬 GA、エンドユーザー資格情報で動く自律エージェントのトリガー（8月中旬）が出たが、⚠️ いずれも二次スニペットのみで一次未確認のため内容は採用していない

### Copilot Studio / Power Platform

- Copilot Studio の What's New は節構成が June 2026 のままで、7月節も8月節も追加されていない。⚠️ GitHub Copilot ハーネスは 8/3 に GA しているのに `(Production-ready preview)` の表記が残ったままで、未反映が9日連続になった
- Released Versions は **2026.6.3**（6/30 初出）が最新のままで、8/11 の定例更新日を過ぎても新ビルドは出ていない。ページの `ms.date` は 6/30、`updated_at` は 7/1 で据え置きである。次の定例は 8/18 で、更新がなければ空振り5回目になる
- 課金レート表（`requirements-messages-management`）は `updated_at` 2026-08-03T14:59Z のまま記載に変化がない。生成 AI ツールの階層別レート（10応答あたり basic 1 / standard 15 / premium 100 クレジット）、推論モデルの二重課金、枯渇時の2系統は 8/11 の記載どおりである。同ページにはエージェント単位で月次の消費上限を設定できる旨も記載されており、エンフォースメント前に打ち止めできる経路にあたる
- Power Platform の Release Wave（全体版）は緑チェックの追加・期日の変更・行の削除がいずれも発生せず、**4日連続で完全に同一**だった。期日超過は延べ12行のまま変わらず、8月に期日がある7件もすべて未達である。2026 Wave 1 の対象期間は9月までで残り約1か月半になる
- Copilot Studio の Release Wave ページは本日も M365 Roadmap への HTTP 301 恒久リダイレクトを返した。Power Platform Blog は 8/6 の July/August 合併号が最新のままで、親ページと子カテゴリページの不完全レンダリングも続いている

### OpenAI / Codex

- Codex CLI の pre-release が 0.148.0-alpha.8 まで進んだ（8/11 18:41 UTC）。8/11 だけで alpha.7 と alpha.8 の2本が刻まれた一方、**安定版は 0.147.0（8/7）で据え置き**のままである
- `developers.openai.com/changelog` は 8/7 の Daybreak エントリが最上位のままで、8/8〜8/11 の追加はない。Announcements RSS も 8/10 の Daybreak 告知が最新である
- ChatGPT & Codex changelog は2件を検索経由で確認したが、⚠️ `learn.chatgpt.com` がゲートウェイ拒否のため**掲載日を確定できていない**。内容は ChatGPT Enterprise / Education で1万字超のペーストが自動で添付ファイルに変換される件と、Sign in with ChatGPT のベータ提供先（Airtable / GitLab / HubSpot / Notion / Supabase / Vercel）である
- 既報: GPT-5.6-Cyber と Daybreak Blue / Red の公開（8/10）、Astra の開発一部停止（8/7）。期限は o3 と Assistants API が 8/26 退役、公式 DALL·E GPT が 8/30 退役、GPT-5.4 / 5.4 mini が 8/31 に Codex（ChatGPT サインイン）から除外である

### Google / DeepMind

- **Made by Google が 8/13 07:00 JST（8/12 18:00 ET）にニューヨークで開催される**。ダイジェスト生成時点では未開催で、Pixel 11 系4機種と Pixel Watch 5 の発表が見込まれている。AI 面では Gemini が端末横断の中心に据えられる見通しだが、⚠️ 具体的な発表内容は現時点で全て未確認である
- Gemini 3.5 Pro の未ローンチが続いている。I/O（5/19）発表後に6月 → 7月 → 7/17 と3回スリップしており、本日の Made by Google で言及されても trusted tester / Gemini Advanced / API preview 限定なら GA には当たらない
- **Google が Google Ads と Google Analytics へエージェント機能を投入した（8/10）**: 自然言語プロンプトから生データで成果レポートを作る AI ダッシュボードと、その数字の理由を説明するリアルタイム要約が加わった。Ads 側の agentic expert はキーワードや広告クリエイティブの提案に加えて**実装まで代行し**、Analytics にはホーム画面の AI Overviews と競合ベンチマーキングが入る。マーケティング業務のエージェント化が「提案」から「実行」へ踏み込んだ事例にあたる
  - https://blog.google/products/ads-commerce/google-ads-analytics-ai-updates/
- Gemini API の changelog は 7/30 の Gemini Robotics ER 2 public preview が最上位のままで、単価も10日連続で据え置きである（3.6 Flash $1.50／$7.50 と 3.5 Flash $1.50／$9.00 の出力単価の逆転も継続）。退役は **Imagen 4 系3本が 8/17 停止**で期限まで5日、`gemini-robotics-er-1.6-preview` は 8/31 停止である
- Gemini in Classroom の全年齢開放は 8/10 に web で始まっており、モバイルは 8/17 になる

### 資本・インフラ

- **Anthropic が Riot Platforms と $9.1B のデータセンター契約を結んだ（8/11）**: Bitcoin マイナーから AI データセンター容量の販売に転じた先との20年リースで、テキサス州 Rockdale キャンパスの **191MW** を 2048年6月まで確保する。5年の延長オプションが2回あり、行使すると総額は最大 $16.1B になる。容量は段階投入で、2027年12月までに 96MW、2028年6月に全量が立ち上がる予定である。Riot は初期工事の資金として Morgan Stanley 経由で $573M のつなぎ融資枠を用意した
- **Anthropic・Macquarie Asset Management・GIC が Theseus Infrastructure を設立した（8/10）**: データセンターを大規模に開発・運営し、長期契約で Anthropic へ賃貸する専用プラットフォームにあたる。各案件のエクイティの大半は Macquarie の運用ファンドと GIC が拠出して保有し、Anthropic はアンカーテナントとして入る。Anthropic は送電網の増強費用を全額負担し、自社需要に起因する家庭向け電気料金の上昇分も負担すると表明した。米国内データセンターへの $50B 投資計画を自社バランスシートの外へ出す構図になる。⚠️ 容量と投資総額はいずれも非開示で、一次プレスリリースはゲートウェイ拒否のため二次報道の突き合わせによる
  - https://www.datacenterdynamics.com/en/news/gic-and-macquarie-form-theseus-infrastructure-to-serve-anthropics-data-center-needs/

### モデル / オープンウェイト

- **Qwen3.8-Max / Qwen3.8-27B の重みは 8/12 時点でも公開されていない**。HF API で両リポジトリを叩くと存在しないリポジトリと同じ 401 が返り、Qwen org の公開モデルは 6/26 が最新のままである。Alibaba は「8/10 の週」に HF と ModelScope へ出すと表明しており、期限は **8/16** までまだ残っている。Max クラスの重み公開は初で、ライセンスは未開示のままである
- Meta の `meta-models/Muse-Glimmer-30B`（Apache 2.0・8/10 告知）はサードパーティ量子化が積み上がり続けている。trending 上位は `moonshotai/Kimi-K3`、`MiniMaxAI/MiniMax-H3`、`deepseek-ai/DeepSeek-V4-Flash-0731` で変化はない
- DeepSeek が 8/6 に告知した API の「大幅値上げ」は、幅・新単価・対象の課金区分・実施日のいずれも未公表のままである。現行 V4-Flash は入力$0.14／出力$0.28（100万トークン）で据え置きが続き、北京時間の平日ピーク時間帯の単価2倍も未発動である

### 開発ツール / MCP

- Cursor は changelog・フォーラムとも更新がない。changelog は 8/3 の Google Workspace Plugins、Announcements フォーラムは 7/28 の Cursor Start が最上位のままである。✅ 08-10・08-11 と2日続いた `cursor.com` の WebFetch 503 は本日再現せず、間欠障害だったと確定した
- Devin が Outposts を公開した（自分の環境で Devin のワークロードを実行する機能で、既定では無効・有効化には Cognition の担当者への連絡が要る）。⚠️ `docs.devin.ai` がゲートウェイ拒否のため公開日を確定できていない
- Grok 4.6 の一次確認は依然できていない。二次サイトは「8/7 ローンチ・1.5T パラメータ・V9 基盤据え置き」と書き、2.1T の Grok 4.7 が数週間後に続くとするが、`x.ai` / `docs.x.ai` / `openrouter.ai` がいずれもゲートウェイ拒否で裏取り経路がない
- MCP のブログ新着はなく、RSS 最新は 7/28 の `The 2026-07-28 Specification` のままで**15日連続**動きがない。Tier 1 SDK も変化なし（TypeScript / Python 2.0.0、C# v2.0、Go は v2 未発行で `go-sdk` v1.7.0 が仕様対応）

### 規制・政策

- EU AI Act 第50条の透明性義務が、フロンティアラボの製品仕様を実際に動かした（ハイライト2参照）。8/2 の発効から9日で Anthropic が全世界一律のマーキングを表明しており、EU 域外の利用者にも仕様変更として降りてくる形になった
- 既報: 英 AISI のインシデント報告（8/4）、Anthropic の cybersecurity evals インシデント（7/30 公表・141,006 ラン精査）、ホワイトハウスの任意フロンティア安全性試験枠組み（8/4）

### 市場データ

- 定点の調査ソースはいずれも新規公表がない。IDC / IDC Japan の最新は2026年3月発行の Worldwide AI and Generative AI Spending Guide 2026V1（国内 AI 市場支出額は2025年 2兆3,725億円 → 2029年 6兆8,897億円・CAGR 36.0%）、MM総研の生成AI 個人利用状況調査は2025年8月時点（個人利用率 21.8%・利用者 1,597万人）のままである。Similarweb の生成AIトラフィックシェアも 08-03 収録分から動いていない。提案書への引用は計測時点の明記を継続する

## 直近の注目予定

- **8/13**: Made by Google のキーノート（8/12 18:00 ET）
- **8/14**: Claude Code の既定権限モードが auto mode へ（Pro / Max / Team）／ Copilot Success Planner の提供開始 ／ DOE Genesis 寄与プログラムの第1次応募締切
- **8/16**: Alibaba が表明した Qwen3.8-Max / 27B 重み公開の週の終わり ／ Power CAT（Copilot Agent Kit）・PnP の週次確認
- **8/17**: Claude Console 旧 Workbench 退役 ＋ 実験的プロンプトツール API 廃止 ／ Gemini API の Imagen 4.0 系3本停止 ／ Gemini in Classroom のモバイル開放 ／ MS-4005 の週次確認
- **8/18**: Copilot Studio Released Versions の次の定例更新日（更新がなければ空振り5回目）
- **8/18〜9/8**: M365 Copilot Agent's Playbook ライブストリーム（各回 9AM PT）
- **8/19**: Claude Code 週次上限50%増の終了（23:59 PT）
- **8/20**: ChatGPT Business Premium シートのクレジット販促の受付終了 ／ Gemini Enterprise Agent Platform の Grok 4.1 ファミリー停止（一次未確認）
- **8/22**: M365 Copilot アプリのチャット中心 UI が Deferred リングへ展開開始
- **8/26**: OpenAI Assistants API 廃止 / o3 退役 / GPT-4.5 完全廃止 ／ Copilot 既定モデル有効化ポリシー発効
- **8/30**: 公式 DALL·E GPT の退役
- **8/31**: GitHub Spark の既存ユーザーアクセス終了 ／ `gemini-robotics-er-1.6-preview` 停止 ／ GPT-5.4・5.4 mini が Codex から除外 ／ Claude for Government の $1/機関プログラム終了 ／ Power Automate モバイルアプリの廃止 ／ CSP Copilot Partner Council コンテストの応募期限
- **9/1**: GitHub Copilot の全体験でモデル廃止 ／ OpenAI Daybreak 全アカウントでハードウェアセキュリティキー必須化
- **9/2**: Windows 365 Frontline 名称での購入最終日 ／ **9/3**: Windows 365 Flex へ改称
- **9/10**: GitHub Copilot の MAI-Code-1-Flash 退役
- **9/30**: M365 E7 プロモーションの対象購入最終日 ／ M365 E5 / E3 の CSP 割引終了 ／ **10/1**: E7 プロモーションの新規取引停止
- **10/1**: OpenAI 対 Apple の営業秘密訴訟の審尋
- **10/20〜22**: SMB Copilot Partner Council イベント（ニューヨーク・当選20社）
- **10/27〜29**: Power Platform Community Conference 2026（MGM Grand ラスベガス）
- **11/1**: パートナー特典の有効期限がオファー購入日基準へ移行
- **12/2**: EU AI Act の生成コンテンツ標識義務、8/2 以前に市場投入済みシステムへの猶予終了
- **12/31**: M365 E3 プロモーション ／ Copilot in 30 ／ Purview Suite 50%オフの提供終了
- **8月中旬**: M365 Copilot Release Notes の次バッチ見込み ／ OpenAI の公開 S-1 掲載見込み
- **9月**: iOS 27 / macOS 27 GA ／ auto mode の既定化を Enterprise・API・各クラウドへ拡大予定
- **時期未定**: ドメイン除外の再提供 ／ Cowork 1 の提供開始 ／ Copilot Studio What's New への7月・8月節の追加とハーネス GA の反映 ／ Fluent UI (v8) コントロールの廃止日 ／ Bedrock Agents Classic の提供終了日

## 改善メモ

- 本サマリーの訂正: 08-11 まで「8/31 に Sonnet 5 の促進価格が終了し $3/$15 へ戻る」と注目予定に載せてきたが、この値上げは実施されないことが確定した。本日分から当該期限を削除している
- ソース定義の穴（Copilot）: 新規提案 B-032（Agent 365 ブログを `daily-sources.md` へ登録）を出した。本日のハイライト級3件（Registry Sync GA・マルチテナント管理 Preview・Copilot Credit のコスト管理）はすべて 8/6 公開の同一記事が出典で、**6日間取りこぼしていた**ことになる。継続提案は16件で、最多は B-011（Power Platform Blog のトピック記事照合・24回目）である
- Master: 新規提案 B-031（一覧ページが日付降順であることを前提にしない判定）を出した。`claude.com/blog` が特集順で最上部10件が2ヶ月前の記事だった件が発端である。継続提案は10件で、最多は B-013（403の2分類記録・16回目）である
- industry: 新規提案 B-025（`support.claude.com` を日次ソースに追加）を出した。継続提案は6件で、最多は B-004（取得方法欄の WebSearch 優先化・44回目）である
- ⚠️ 提案番号の重複が続いている。本日の Master B-031 は Copilot が 08-11 に採番した B-031 と、industry B-025 は Master の B-025 と番号が重なる。台帳がソースごとに独立しているためで、横断参照の際は必ずソース名を添える必要がある
- 取りこぼしの検知（Master）: Claude API release notes に 8/10・8/11 の2エントリが入っていた（前回記録は「8/7 が最上位」）。ウォーターマークの記事も Release Notes 一覧から辿れず、日付入り検索で初めて検出できた。一覧ページ経由の巡回だけでは当日分を落とす事例が2件重なっている
- 障害の変化（Master）: `cursor.com` の WebFetch 503 が 08-10・08-11 の2日連続から復旧し、間欠障害だったと確定した
- 障害の変化（industry）: `www.publickey1.jp`（最優先の登録ソース）・`www.macquarie.com`・`www.datacenterdynamics.com` の3ドメインをゲートウェイ拒否として新規記録した。Theseus Infrastructure は一次プレスに到達できず二次報道の突き合わせで書いている
- 障害の変化（Copilot）: 変化なし（`mc.merill.net` / `qiita.com` / `zenn.dev` / `www.ppweekly.com` のゲートウェイ拒否は継続中）。Message Center の一次取得は5日連続でできていない
