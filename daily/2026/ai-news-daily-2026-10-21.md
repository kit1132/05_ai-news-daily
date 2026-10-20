# AI News Daily Summary — 2026-10-21

GitHub は 10/19 に Copilot から6モデルを廃止し、9/22 に「対象外」とされた GPT-5 mini も消えていた。M365 Copilot の Researcher では、複数モデルで検証する Critique / Council が 11月中旬までに退役する。OpenAI は Responses API に12時間のプロンプトキャッシュを加え、書き込み単価が入力の2.5倍の段を新設した。

## 今日のハイライト

### 1. [廃止] GitHub Copilot が 10/19 に6モデルを廃止し、GPT-5 mini も含まれていた — 9/22 に「対象外」と訂正された GPT-5 mini が実際には消え、移行先も GPT-6 世代へ上がった

**要点**: GitHub が 10/19 付の完了告知で、Copilot Chat・インライン編集・Ask / Agent モード・コード補完から6モデルを廃止したと公表した。9/18 告知時点の5件に GPT-5 mini が加わっており、GPT-5 mini を既定や自動化に指定していた環境はすでに動かない。

**詳細**:

- 廃止6件と推奨移行先（すべて 2026-10-19）
  - Gemini 3.7 Flash → Gemini 3.8 Flash
  - GPT-5.5 / GPT-5.4 → GPT-6.1 Sol
  - GPT-5.4 mini / GPT-5 mini → GPT-6 Luna
  - Grok 4.5 → Grok 4.7
- 移行先は 9/18 告知時点（GPT-5.6 Sol / GPT-5.6 Luna / Grok 4.6）から一世代上がった
- Copilot Enterprise の管理者は、モデルポリシーで移行先モデルを有効にする必要がある場合がある。廃止モデルを削除する操作は要らない
- 同日、モデルポリシーを REST API で管理する Copilot model policy API が GA した（GitHub Copilot 節）

- https://github.blog/changelog/2026-10-19-github-copilot-models-deprecated-on-october-19-2026

### 2. [廃止] M365 Copilot の Researcher で Critique / Council が 10月下旬から11月中旬に退役する — Frontier で使えた「複数モデルで検証する」研究の流れが Researcher から消える

**要点**: MC1515927（10/19）によると、別モデルが下書きを検証する Critique と、複数モデルの回答を並べる Council が10月下旬から退役し、11月中旬に完了する。後継機能と時期は示されておらず、Researcher は単一モデルの流れに戻る。

**詳細**:

- 対象: Frontier プログラムに参加し、Researcher で Critique / Council を使える M365 Copilot ユーザー。Researcher と Analyst 自体は残る
- 対応期限（Act by）: **11/14**。管理者には、利用者への周知、社内ガイド・研修資料の更新、ヘルプデスクへの事前連絡が求められている
- 理由: プレビューが終わるためで、知見は将来の M365 Copilot に生かすとしている。両機能は 3/30 に Frontier で公開されていた

- https://mc.merill.net/message/MC1515927

### 3. [料金+新機能] OpenAI が Responses API に12時間のプロンプトキャッシュを追加した — 間隔の空く処理でもキャッシュ単価が効く代わりに、書き込みは入力単価の2.5倍になる

**要点**: OpenAI が 10/20 に、GPT-5.6 以降でキャッシュの最小保持時間を12時間にできるようにした。既定30分では切れていた定期実行やバッチでも読み出し単価が使えるが、書き込みは30分（1.25倍）の倍なので、再利用が少ないと割高になる。

**詳細**:

- 指定: `prompt_cache_options.ttl` に `"12h"`（既定 `"30m"`）。ブレークポイント単位では `prompt_cache_breakpoint.ttl` で上書きでき、未対応の値は 400 になる
- 単価: 書き込みは入力単価の **2.5倍**、読み出しは 0.1倍（GPT-6.1 Sol は 0.05倍）。30分で書いた範囲を12時間に延ばすと12時間の書き込み料金が改めて掛かる
- 旧モデル向けの `prompt_cache_retention`（`in_memory` / `24h`）とは別の設定で、キャッシュは組織内・処理リージョン内でだけ再利用される
- 料金ページ（`/api/docs/pricing`）には本日時点で12時間の記載がなく、倍率は changelog とガイドで確認した

- https://developers.openai.com/api/docs/changelog
- https://developers.openai.com/api/docs/guides/prompt-caching

## カテゴリ別まとめ

### Microsoft 365 Copilot / Cowork / Work IQ

- **Researcher の Critique / Council 退役**（ハイライト参照・2）
- [新機能] **Cowork 向けの Purview DLP** — Roadmap 570845 が 10/19 に Rolling out（GA October CY2026）へ変わり、管理者は M365 Copilot と同じ DLP ポリシーで Cowork を統制できるようになる。ラベル付きナレッジの利用禁止、機密情報を含むプロンプトの阻止、機密プロンプトの Bing 送信の阻止ができる。Purview What's new にはまだ載っていない。https://www.microsoft.com/microsoft-365/roadmap?id=570845
- [新機能] **PowerPoint のインタラクティブスライド** — 利用者は、リボンの Interactive Slide か Copilot のスキル選択から、操作できるスライド（ダッシュボード、タイムライン、比較）を Copilot に作らせられるようになった。Windows / Mac の Current Channel・Monthly Enterprise Channel と Web 版で展開中で、10月末に完了する見込みである。https://techcommunity.microsoft.com/t5/microsoft-copilot-blog/transform-your-storytelling-with-interactive-slides-in/ba-p/4564287
- [新機能] **Copilot のセッション共有と応答共有** — Roadmap 562353 が 10/19 に Launched（August CY2026）になり、利用者は Copilot の会話や応答を読み取り専用リンクで共有できる。管理者向けの統制は 9/21 に既報である。
- [仕様] **Work IQ の `retrieve` ツール** — Microsoft が 10/20 に、10/14 既報の `retrieve` ツールのパラメーター仕様を公開した。`strategy` は `copilot`（コネクタ・MCP まで検索）と `grounding`（SharePoint・OneDrive・Teams・Outlook のみ）から選び、`capabilities` で検索対象を絞れる。提供状況・料金は書かれていない。https://devblogs.microsoft.com/microsoft365dev/work-iq-retrieve-october-2026/
- [予定] **Work IQ の Roadmap 3件** — Microsoft が 10/19 に、Work IQ へ人の承認とポリシー統制を加える3件を起票した
  - Real Time Transcripts（570651）: アプリとエージェントが Teams 会議の書き起こしをリアルタイムで読める。GA は November CY2026
  - Human in the loop（570672）: エージェントとエージェントフローが続行前に人の承認を待てる。プレビュー November、GA January CY2027
  - Agent Policy Governance（570652）: 管理者がエージェントと機能をポリシーで一括統制できる。時期は 570672 と同じ
- [予定] **Copilot Analytics のエージェントデータのエクスポート** — MC1288531（10/20 更新）によると、Copilot ライセンス50以上の組織の対象ユーザーは、11月中旬から Agent Dashboard で最大6か月分の匿名化データをダウンロードできる。管理者は Viva の Feature Access Management で無効にできる。https://mc.merill.net/message/MC1288531
- [仕様] **Cowork のブラウザー利用設定の改称** — MC1515930（10/19）によると、管理者向け Copilot 設定の「Cowork」パネルが10月中旬に「Browser use in Microsoft Copilot」へ改称される。機能と既存の構成は変わらない。https://mc.merill.net/message/MC1515930
- [廃止] **OneDrive のエクスプローラー右クリックの Copilot 操作** — MC1515940（10/20）によると、エクスプローラーの右クリックメニューにある OneDrive の Copilot 操作の一部が12月上旬までに削除される。「Ask Copilot」とエクスプローラーのホームからは使い続けられ、管理者の対応は要らない。https://mc.merill.net/message/MC1515940
- [予定] **OneDrive iOS の PDF レビュー** — MC1470417（10/20 更新）によると、OneDrive iOS で PDF のテキストを選んで Copilot に説明・要約・翻訳させる予定だった機能は、提供が取りやめになった。https://mc.merill.net/message/MC1470417
- [据え置き] **Release Notes / ブログ各種** — M365 Copilot Release Notes の先頭は October 06, 2026 のままで、Copilot ブログ（10/8）と Tech Community の各 board、Cowork What's New、Partner Center 10月ページにも新しい記事・改訂は無い。

### Copilot Studio / Power Platform

- [予定] **Purview で保護された文書のアップロード** — Roadmap 571305（10/19 起票）によると、利用者は M365 チャネルに公開された Copilot Studio エージェントへ、MPIP ラベル付きファイルをアップロードできるようになる。ラベルの保護は処理の最後まで適用され、プレビューと GA はともに October CY2026 である。https://www.microsoft.com/microsoft-365/roadmap?id=571305
- [予定] **GitHub Copilot ハーネスの Computer Use** — Roadmap 576272（10/19 起票）によると、Copilot Studio のエージェントが GitHub Copilot ハーネスのネイティブ機能として Web サイトを操作できるようになる。プレビューは November CY2026、GA は January CY2027 である。https://www.microsoft.com/microsoft-365/roadmap?id=576272
- [予定] **Dataverse のプロンプト列の複数行出力** — MC1515841（10/20）によると、メーカーは 11/16 の GA からプロンプト列の出力を複数行テキストで保存できるようになる。新しく作る列だけが対象で、既存の列には追加されない。https://mc.merill.net/message/MC1515841
- [観測] **モデル表とハーネス概要の改訂** — Copilot Studio の `authoring-select-agent-model` と `harnesses-overview` が 10/19 付で改訂されたが、前版との差分は特定できていない。標準ハーネスの Default は GPT Chat Latest で、GA に Claude Sonnet 4.6・Opus 4.6 / 4.7 / 4.8 が並ぶ。https://learn.microsoft.com/en-us/microsoft-copilot-studio/authoring-select-agent-model
- [据え置き] **What's New / Released Versions / 非推奨一覧** — Copilot Studio What's New は `ms.date` 10/5 のまま、Released Versions は 2026.6.3 のまま112日動いておらず、非推奨一覧も 10/16 の `caf484d1` から改訂されていない。

### GitHub Copilot / GitHub

- **Copilot の6モデル廃止**（ハイライト参照・1）
- [新機能] **Copilot model policy API** — GitHub が 10/19 に Copilot model policy API を GA し、管理者は Enterprise・Enterprise チーム・エージェントアプリ・Organization の4階層で、モデルポリシーを REST API（GET / PATCH）から取得・更新できるようになった。Enterprise のポリシーから組織やチームへモデル管理を委任することもできる。https://github.blog/changelog/2026-10-19-copilot-model-policy-api-for-enterprise-orgs-and-teams
- [新機能] **GitHub package firewall** — GitHub が 10/20 に、Actions ランナーやコーディングエージェントが取得する npm パッケージを企業ポリシーで検査する機能をパブリックプレビューにした。対象は Enterprise Cloud で、公開直後のパッケージを止めるクールダウンと Advisory Database の照合ができる。プレビュー中は無料で、GA 後は従量課金になる。https://github.blog/changelog/2026-10-20-github-package-firewall-in-public-preview
- [新機能] **Copilot CLI `v1.0.101`** — GitHub が 10/20 に Copilot CLI `v1.0.101` を出し、Assisted Permissions の判断を誘導する `assistedApprovalInstructions` 設定と、動的ワークフローのサブエージェント向け構造化出力を加えた。モデルピッカーは管理者が管理するモデルを既定として示す。削除されたフラグはリリース本文に書かれていない。https://github.com/github/copilot-cli/releases

### Claude / Anthropic

- [新機能] **Claude Code `2.1.304` と stable の追いつき** — Anthropic が 10/19 19:47Z に Claude Code `2.1.304` を npm に出し、`stable` / `latest` / `next` がすべて `2.1.304` に揃った。前日まで11版遅れていた stable 固定の組織にも、2.1.293〜2.1.304 の変更がまとめて届く。https://code.claude.com/docs/en/changelog
  - Code Review: 組織の Owner が Quick / Standard（既定）/ Deep を選び、リポジトリごとに変えられる。GitHub 組織の全リポジトリを一括で対象にする設定も加わった
  - LLM ゲートウェイ: カスタム `ANTHROPIC_BASE_URL` の背後でもツール検索が既定オンになり、400 / 422 なら検索なしで再送する
  - `/auto-mode-setup`: プロジェクトと直近のセッションから auto mode に環境を教えるガイドを追加した
  - `claude --worktree`: HEAD が detached や別ブランチのとき、確認なしで worktree とブランチを消してコミットを失いうる不具合を直した
- [新機能] **Claude Enterprise の Inference hooks GA** — Anthropic が 10/20 に Inference hooks を正式提供にし、Enterprise の管理者は claude.ai・Cowork・Claude Code などのプロンプトを、推論前に自社サーバーの allow / deny 判定に通せるようになった。既定のタイムアウトは5秒で、シャドーモードとツール呼び出し前の判定がある。Bedrock・Google Cloud・API 利用の組織は対象外で、書き換えや墨消しはできない。https://platform.claude.com/docs/en/manage-claude/inference-hooks
- [動向] **Claude によるサソリ神経毒の結合タンパク質設計** — Anthropic が 10/20 に、社内の研究用モデルに神経毒5種へ結合する小型タンパク質を設計させ、実験に回した211件のうち17件の結合を確認したと公表した。約64時間ほぼ自律で318,484件を生成し、データセットを Hugging Face に公開した。中和効果は確かめていない。https://www.anthropic.com/research/claude-scorpion-toxin-binder-design
- [観測] **退役ページの Active 件数の訂正** — Master は、モデル退役ページの Active を `API model name` 単位で数え直して15件とし、前日の16件は数え誤りだったと記録した。Haiku 4.5 は退役下限日（10/15）の6日後も Active のままで、Deprecation history の最新は 9/30 の Sonnet 4.5 のままである。https://platform.claude.com/docs/en/about-claude/model-deprecations
- [据え置き] **`/news`・製品ブログ・Fable 5.5** — `www.anthropic.com/news` は 10/18 の Public Benefit Fund、製品ブログは 10/19 の source control 記事が最上位のままで、Fable 5.5 は一次に出ていない。

### OpenAI / Codex / ChatGPT

- **12時間プロンプトキャッシュ**（ハイライト参照・3）
- [動向] **GPT-6 のレガシー言語移行性能** — The Decoder によると、OpenAI は自社の MultiLangBench（20言語）で GPT-6 Astra のテスト合格率が 87.4% と、GPT-5.6 Terra の約38%から上がったと公表した。GPT-6.1 Sol の COBOL 移行の正答率は最大 97.9% としている。いずれも OpenAI 自身の測定である。https://the-decoder.com/openai-says-gpt-6-is-much-better-with-legacy-programming-languages-such-as-cobol-and-fortran/
- [版更新] **Codex CLI `0.164.0-alpha.7`** — OpenAI は Codex CLI の pre-release を `0.164.0-alpha.7`（10/20）まで進めた。安定版は `0.163.0`（10/15）のままである。https://github.com/openai/codex/tags
- [据え置き] **退役一覧・ミスアライメント報告・changelog** — OpenAI の退役一覧は 10/14 の GPT-4 系が最上位のままで、`alignment.openai.com` の First posted も 10/15 が最新のままである。community Announcements と `learn.chatgpt.com` の changelog にも新しい項目は無い。

### Google

- [新機能] **Sheets の Gemini で BigQuery 分析** — Google が 10/19 に、Google Sheets の Gemini で BigQuery のデータを自然言語で分析できるようにし、Classroom の教師用 Gemini Notebook に要約機能と信頼済みドメインの共有設定を加えた。https://workspaceupdates.googleblog.com/
- [据え置き] **Gemini API / Gemini アプリ** — Gemini API changelog と Gemini アプリのリリースノートは、どちらも 10/13 の Gemini 4 Argon が最上位のままで、deprecations の 10/22・10/23・11/17 の停止日にも変更は無い。https://ai.google.dev/gemini-api/docs/changelog

### その他エージェント / 開発ツール

- [新機能] **Devin Oncall GA** — Cognition が 10/19 に Devin Oncall を全組織へ GA し、Slack / Teams のチャンネルと PagerDuty のインシデントを見張って原因候補と次の対応を投稿できるようにした。Devin Review にはルールエディタと、未レビューの最新変更の表示が加わった。https://docs.devin.ai/release-notes/overview
- [新機能] **Orca `v1.4.232` / `v1.4.233`** — Stably AI が 10/20 に Orca を更新し、エージェントの権限モードを Manual / Auto / Yolo から選べるようにした。Auto では Claude と Codex の承認を自動で処理し、既定の変更は新規セッションだけに掛かる。ネイティブチャット（実験的）では OpenCode 2 を選べる。https://github.com/stablyai/orca/releases
- [新機能] **Cloudflare の抽出専用モデル Clairic** — Cloudflare が 10/19 に、文章や画像から識別子・日時・数量・価格を JSON と確信度つきで抜き出すモデルを Workers AI でプレビュー公開した。同社の例では LLM 単独より約69%速く、費用は約49%低い。料金は未発表で、重みは後日公開する予定である。https://gigazine.net/news/20261020-cloudflare-clairic/
- [新機能] **DeepSeek の推論エンジン DeepInfer** — DeepSeek が 10/20 に、V4.1-Flash を動かす vLLM ベースの推論フレームワークをオープンソース化した。https://the-decoder.com/deepseek-open-sources-the-inference-engine-that-powers-its-fastest-and-cheapest-ai-model/
- [据え置き] **Cursor・xAI・TypeSafe・MCP・HF の定点** — Cursor の changelog は 10/16、フォーラムは 10/12 が最上位のままで、`docs.x.ai` は 10/14、TypeSafe は `jev-latest` → `jev-1.13.0` のままである。MCP ブログ・Hugging Face の8 org・Apple Developer News にも新着は無い。

### 市場・企業 / セキュリティ

- [セキュリティ] **AI ペンテスト基盤 Cairn の悪用** — NorForge の研究者が、オープンソースの AI ペンテストツール Cairn を使った攻撃の実態を公表した。主な攻撃者は約1,100件の攻撃で約96件（約8.4%）を成功させ、トークン代は約 $5,000 だった。標的は米国・日本・豪州の EC や決済基盤で、Reuters は Deere・SharkNinja・Cummins を被害企業として報じた。https://gigazine.net/news/20261020-chinese-hacker-ai-agents-break-websites/
- [動向] **米国土安全保障省の DeepSeek 排除命令** — The Decoder と GIGAZINE によると、米国土安全保障省が 10/20 に連邦文民機関へ DeepSeek 技術の排除を命じた。対象範囲や期限の詳細は出ていない。https://the-decoder.com/us-bans-deepseek-technology-across-federal-civilian-agencies/
- [動向] **Salesforce の Braze 買収** — Salesforce が 10/20 に、顧客エンゲージメント基盤の Braze を企業価値約 $5.66B（1株 $47.50 の現金）で買収すると発表した。成立には規制当局と Braze 株主の承認が要る。https://www.sec.gov/Archives/edgar/data/0001108524/000119312526425881/d516983dex991.htm
- [据え置き] **買収協議と国内市場データ** — Amazon × Decart、Nvidia × Reflection AI の買収協議に続報は無く、IDC Japan・MM総研・NRC の新規公表も無い。

## 直近の注目予定

- **10/21 前後**: TypeSafe の `jev-latest` が `jev-1.14.0` へ移る
- **10/22**: Copilot Business / Enterprise の機能既定有効化が発効 ／ Gemini API の Veo 3.1 プレビュー3種と `gemini-omni-flash-preview` が停止（最短日）
- **10/23**: Gemini API の `deep-research-pro-preview-12-2025` が停止 ／ OpenAI のレガシー GPT スナップショットが停止
- **10月後半**: claude.ai（米国）で Democracy Works の投票情報を表示 ／ Claude Fable 5.5（リークのみ・未確認）
- **10月下旬〜11月中旬**: Researcher の Critique / Council が退役（MC1515927、Act by 11/14）
- **10/26**: Dataverse で .NET Framework 4.8 のプラグインパッケージが使える（MC1515315）
- **10/27〜29**: PPCC 2026（ラスベガス）
- **10/30**: ChatGPT Pro 200 の Work / Codex 利用枠が変更（二次） ／ Gmail Live の Workspace への順次展開が完了（最大15日）
- **10/31**: MCP サーバー認定の旧申請経路が終了 ／ DeepSeek の Search・Fetch API の無料提供が終了
- **11/1**: CSP 価格表プレビューに Copilot の新オファーが載る ／ Codex の28日間「改善かリセット」の終了（二次）
- **11/2**: xAI `grok-imagine-image-quality` が退役
- **11/4**: Entra で一般ユーザーのブループリント作成が既定オン（MC1506733）
- **11/12**: Copilot Studio の GPT-4.1 / GPT-5 系が退役（MC1506318） ／ Anthropic Usage Policy 改定版が発効 ／ OpenAI → Cursor のモデル供給停止予定（一次未読）
- **11月中旬**: Copilot Analytics でエージェントデータのエクスポートが可能に（MC1288531）
- **11/15**: Dataverse for Teams 環境とアンマネージド開発者環境の新規作成が停止
- **11/16**: GitHub Copilot が Claude Opus 4.8・Opus 5・GPT-5.6 Terra を廃止 ／ Dataverse のプロンプト列が複数行テキスト出力に対応（MC1515841）
- **11/17**: Gems が Gemini アプリの設定パネルへ移動 ／ Gemini API の TTS・Live プレビュー5種が停止（最短日）
- **11/17〜20**: Microsoft Ignite
- **11/24 以降**: `claude-opus-4-5-20251101` の暫定退役日（確定日ではない）
- **11/30**: Azure DevOps コネクタの旧接続が認証不可に（MC1508508） ／ App Builder と vibe.powerapps.com が退役 ／ `claude-sonnet-4-5-20250929` が Claude API から退役 ／ OpenAI の Evals・`v1/prompts`・Agent Builder が停止 ／ Gemini 4 Argon の導入価格が終了
- **12/1**: M365 Copilot の前提サブスク不要オファー開始、現行「(add-on)」オファーの CSP 販売終了 ／ Copilot Business の従量課金が既定オン ／ Gemini 4 Argon の単価が $4/$20 に倍増
- **12月上旬**: エクスプローラーの OneDrive Copilot 操作の一部が削除（MC1515940）
- **12/14**: claude.ai/design の単体サイトが閉鎖
- **12/15**: アンマネージド開発者環境が停止
- **2027-01-06**: OpenAI `tts-1` / `tts-1-hd` / `gpt-4o-mini-tts` 2版が停止
- **2027年1月**: Copilot Studio の Teams アプリで編集ができなくなる（2月に削除。MC1511056） ／ GitHub Copilot ハーネスの Computer Use が GA 予定（576272）
- **2027-01-14**: OpenAI の GPT-4o・GPT-4o mini・GPT-4.1・GPT-4.1 mini が API から削除（→ `gpt-6-luna`）
- **2027-01-15**: アンマネージド開発者環境の削除開始 ／ Claude Code Review の Enterprise 向けクレジット請求期限
- **2027-03-01 以降**: Gems 廃止（Business / Enterprise）
- **2027年3月末**: SharePoint / OneDrive の `.agent` 形式エージェントが動かなくなる（MC1511052）
- **2027-04-01**: OpenAI `gpt-5.1` / `gpt-5.3-codex` / `gpt-5.4-nano` が停止

## 改善メモ

- 新規提案: 3ソースとも無し
- 継続提案: Master は B-084（復旧8ソースの取得方法欄の差し戻し、3回目）を再確認した ／ Copilot は docset 全件突合を本日も未実施（追跡ページ約30本の `updated_at` 突合で代替） ／ industry は B-007・B-023 を見送り候補に挙げた
- 障害の変化: 3ソースとも無し
- ソース間の差分・矛盾:
  - Master は Copilot の6モデル廃止をハイライト1、industry は model policy API の項目に同居させていた。本サマリーは廃止をハイライト1、API をカテゴリに分けた（1項目に2つのリリースを同居させない）
  - 12時間キャッシュは Master が `[料金+新機能]`、industry が `[料金]` で割れた。新しい保持オプションの追加を含むため `[料金+新機能]` を採った
  - Inference hooks GA は industry がハイライト2、Master がカテゴリに置いた。価格・期限の変化がなく、本サマリーはカテゴリに置いた
  - Cowork の Purview DLP は Copilot がハイライト2にしたが、kit の利用ツールの挙動が当日から変わるものではないため、本サマリーはカテゴリに置いた
  - Claude Code `2.1.304` は industry が「changelog の日付は出ていない」とし、Master は npm の公開時刻（10/19 19:47Z）を記録していた。Master の記述を採った
  - Master は退役ページの Active を前日の16件から15件に訂正した（数え誤り。モデルの増減は無い）
