# AI News Daily Summary — 2026-11-01

Anthropic は Claude Opus 4.8 の fast mode を 11/30 に削除する。Microsoft は Teams 会議の Copilot ポリシーを MeetingAI と TranscriptionWithMeetingAI の2つに分け、11月中旬から展開する。Claude Code `2.1.316` では、Team / Enterprise の管理設定が承認プロンプトなしで適用されるようになった。OpenAI は Daybreak Blue の作業データを 11/29 から学習に使うと参加者に伝えたと報じられている（二次）。

## 今日のハイライト

### 1. [廃止] Anthropic が Claude Opus 4.8 の fast mode を 11/30 に削除する — Opus 4.8 で fast mode を使う処理は、29日後にエラーを返すようになる

**要点**: Anthropic が 10/30 に Opus 4.8 の fast mode を非推奨にした。11/30 以降、`claude-opus-4-8` に `speed: "fast"` を付けたリクエストはエラーになり、通常速度の Opus 4.8 にも切り替わらない。速度を保つには Opus 5.5 へ移る必要がある。

**詳細**: 一次は Claude Platform のリリースノート（October 30 項）。Claude Code `2.1.316`（10/31）の changelog にも同じ告知が載った。

- 削除後の挙動: fast mode のリクエストはエラーを返し、標準の Opus 4.8 へのフォールバックは無い
- 移行先: `claude-opus-5-5`。リリースノートは Opus 5.5 の移行ガイド（Opus 4.8 からの移行節）を案内している
- 料金: fast mode の単価は Opus 5.5 が入力 $8・出力 $40、Opus 5 と Opus 4.8 が $10・$50（100万トークンあたり）。移すと単価は2割下がる
- 提供範囲: Google Cloud（Anthropic managed）と Microsoft Foundry で fast mode を使えるのは Opus 5.5 だけである
- 対象外: `claude-opus-4-8` 自体は Active のままで、暫定退役日は「2027-05-28 より前には退役しない」。モデル退役ページと API パラメーター廃止の表は更新されていない
- 同じ 11/30 に `claude-sonnet-4-5-20250929` も Claude API から退役する

- https://platform.claude.com/docs/en/release-notes/overview#october-30-2026
- https://platform.claude.com/docs/en/about-claude/pricing
- https://code.claude.com/docs/en/changelog

### 2. [破壊的変更] Teams 会議の Copilot ポリシーが MeetingAI と TranscriptionWithMeetingAI に分かれる — PowerShell で Copilot ポリシーを書き換える運用は、11月中旬以降に失敗する

**要点**: これまで1つの Copilot ポリシーが「会議で AI を使えるか」と「文字起こしを必須にするか」を決めていた。11月中旬から2つのポリシーに分かれ、新しい設定が有効になると Copilot ポリシーは直接更新できなくなる。既存の値は自動で移るが、スクリプトは書き直しが要る。

**詳細**: MC1532253（10/30・Feature update）による。Targeted Release は11月中旬〜12月上旬、全世界は11月下旬〜12月上旬に展開する。

- `MeetingAI`: 会議で Copilot・Facilitator・Intelligent Recap などを使えるかを決める。値は On / Off（開催者が変更可）/ Off（変更不可）
- `TranscriptionWithMeetingAI`: AI を有効にしたときに文字起こしを自動で始めるかを決める。値は On（開催者が変更可）/ On（変更不可）/ Off。従来の Transcription ポリシーは「文字起こしを許可するか」の役割で残る
- 組み合わせの規則: MeetingAI を強制オフにすると文字起こしもオフになり、そのあと文字起こしをオンに戻すと MeetingAI の強制オフは外れる
- 会議オプション: 「Allow Copilot and Facilitator」が「Who can manage AI」に置き換わり、「Who can use AI」「Start Transcription with AI」と Intelligent Recap の作成可否が加わる
- 移行: Microsoft が既存の値を新しい2つへ1回だけ写す。PowerShell や独自の自動化を使っていなければ管理者の作業は要らない

- https://mc.merill.net/message/MC1532253

### 3. [破壊的変更+新機能] Claude Code `2.1.316` で、Team / Enterprise の管理設定が承認プロンプトなしで適用され、gateway にグループ共有の月次予算が加わった — 管理設定は開発者の承認を経て入る前提から、取得した時点で効く前提に変わる

**要点**: Anthropic が 10/31 に Claude Code `2.1.316` を出した。Team / Enterprise ログインで Anthropic の API から取得した管理設定は承認なしで適用され、検証できない保存コピーは拒否される。Claude apps gateway ではチーム全体の支出も上限で止められるようになった。

**詳細**: 一次は Claude Code changelog（10/31）。npm は `{stable: 2.1.309, latest: 2.1.316, next: 2.1.316}` で、stable が `2.1.308` から1版進んだ。

- 管理設定・権限
  - `autoMode.allow` に `"$defaults"` を含めない管理リストに、`--settings` や `/permissions` 経由で組み込み例外が戻る不具合を直した
  - `--restricted` セッションが、作業ディレクトリ外のファイルを Read の allow ルールに当たるとアップロードしていた不具合を直した
- Claude apps gateway
  - `pooled_budget`: グループのメンバーが共有する月次予算を、個人の上限に重ねて設定できる（spend limits admin API）
  - `managed.policy_mode: layered`: 開発者に合致する全ポリシーを下位から順にマージして適用する（従来は最初の1件のみ）
  - Bedrock upstream の `guardrail.input_tagging`: prompt attacks フィルタに要る入力タグでプロンプトを包む
  - リクエストが名指すすべてのモデルを `availableModels` / `deniedModels` / `models` と照合し、ブロック対象には該当フィールド名つきの 400 を返す
- 環境変数: `CLAUDE_CODE_SUBAGENT_EFFORT`（サブエージェントの既定 effort。従来はセッションの値を継承）、`CLAUDE_CODE_DISABLE_ULTRATHINK`、`CLAUDE_CODE_DISABLE_LOOPED_CROSS_CERT_DROP`
- クラウドセッション: Enterprise メンバーが自分のクラウド環境のネットワークシークレットを追加・削除できる

- https://code.claude.com/docs/en/changelog
- https://registry.npmjs.org/@anthropic-ai/claude-code

## カテゴリ別まとめ

### Anthropic / Claude

- **Opus 4.8 の fast mode 削除**（ハイライト1参照）
- **Claude Code 2.1.316**（ハイライト3参照）
- [新機能] **Claude Enterprise の Chat と Cowork の統合画面** — Anthropic が 10/23 付の記事で、Chat と Cowork を1つにした画面を Claude Enterprise で一般提供にしたと発表した（industry が TLDR AI の週次スイープで8日遅れで検知）。会話はチャットで始まり、コードやファイルが要る作業はクラウドのセッションへ移る
  - 管理者: 役割ごとに使えるモデルを決め、組織・グループ・メンバーの3階層で支出上限をかけられる
  - Efficient mode: Sonnet と Haiku だけで動かすモードが加わった
  - Claude Code の ZDR・HIPAA 構成・顧客管理鍵の組織は現行構成のまま据え置かれる
  - https://claude.com/resources/articles/unified-claude-enterprise
- [仕様] **旧モデルへのテキスト透かしの拡大** — The Decoder（10/31）によると、Anthropic は API 顧客へのメールで、Claude Mythos 5・Opus 4.7・Opus 4.6・Sonnet 4.6 にも透かしを入れると伝えた。Opus 4.6 と Sonnet 4.6 では `temperature`・`top_p`・`top_k` を既定値から変えると透かしが入らない。EU AI Act の12月の期限に合わせた対応で、検出 API は限定プレビューのままである。ヘルプページはクラウド事業者経由の提供を対象に含めていない
  - https://the-decoder.com/anthropics-watermark-rollout-leaves-a-loophole-on-two-older-claude-models/
  - https://support.claude.com/en/articles/16266773-how-claude-marks-ai-generated-content
- [据え置き] **退役ページ・ニュース一覧** — モデル退役ページの Active は15件のままで、Deprecation history の最新も 9/30 の Sonnet 4.5 のままである。Claude Haiku 4.5 は退役下限日の17日後も Active にある。`www.anthropic.com/news` は 10/28、`/research` は 10/27、`claude.com/resources/articles` は 10/28、`support.claude.com` は 10/21 から動いていない
  - https://platform.claude.com/docs/en/about-claude/model-deprecations

### OpenAI / Codex

- [セキュリティ+仕様] **GPT-Rosalind-6 の system card 補遺** — OpenAI が 10/30 に、生命科学向け GPT-6 Rosalind の system card 補遺を Deployment Safety Hub に公開した。基盤は GPT-6 Astra と同じ重みで、追加の学習も事後学習もしていない。Preparedness の分類は生物・化学が High（Critical 未満）、サイバーは Astra の評価を引き継いで Critical である
  - 提供制限: 承認済みの科学者・研究機関・企業・政府パートナーに限る trusted access。承認企業は利用者を最小限に絞り、人のレビューを置く
  - 能力: MedChemBench v7 49.6%（GPT-Rosalind-5.5 は 28.9%）、LifeSciBench Gold 61.3%（同 44.0%）
  - 安全性: 過去のサイバー脱獄攻撃の成功率 14.3%（Astra 15.7%）
  - https://deploymentsafety.openai.com/gpt-rosalind-6
- [破壊的変更] **Daybreak Blue のセッションデータの学習利用（11/29〜・二次）** — The Decoder（10/31）によると、OpenAI は Trusted Access プログラムの参加者に、Daybreak Blue のサイバーセキュリティ作業データを 11/29 から学習に使うとメールで伝えた。これまでは「モデル改善」の設定をオフにしていれば学習から外れていた。反発を受けた2通目のメールで別の除外手段を約束したが、手順は書かれていない。OpenAI の一次ページでは確認できていない
  - https://the-decoder.com/openai-plans-to-train-models-on-daybreak-blue-cybersecurity-session-data-that-was-previously-off-limits/
- [動向] **OpenAI の調達は目標 $30B に対して $11B** — The Decoder（10/31）が WSJ の報道として、OpenAI の調達が $11B にとどまり、評価額も目標の $1.4兆に届かず $1.25兆だったと伝えた。OpenAI は残りを富裕層とファミリーオフィスから最大 $20B 集める計画で、IPO は来年初めを予定していると報じられた。WSJ の本文は確認できていない
  - https://the-decoder.com/openai-raises-just-11-billion-of-its-30-billion-target-as-big-investors-lose-their-ai-appetite/
- [据え置き] **API changelog・退役・Codex** — OpenAI の API changelog の最上位は 10/30 の `gpt-6-rosalind`、deprecations は 10/14 の GPT-4 系の告知のままである。community Announcements は 10/28、`learn.chatgpt.com` の changelog と Codex の安定版は 10/29 の `0.166.0`、`alignment.openai.com` の First posted は 10/20 から動いていない
  - https://developers.openai.com/api/docs/changelog

### Microsoft 365 Copilot / Teams

- **Teams 会議の Copilot ポリシーの分割**（ハイライト2参照）
- [予定] **Teams の会議メモリーファイルが2027年1月に延期** — Microsoft が MC1429018 を更新し、Intelligent Recap を有効にした会議で AI が要点をまとめた `.meeting` ファイルを作る機能の展開を延ばした。Targeted Release は11月上旬から2027年1月上旬へ、全世界は12月上旬から2027年1月中旬へ移り、既定で有効になる
  - ファイルの置き場所: テナント所有の SharePoint Embedded コンテナーで、利用者は直接開けない
  - 作られない会議: 暗号化を含む秘密度ラベルの会議、エンドツーエンド暗号化の会議、コピーや転送を制限した会議
  - https://mc.merill.net/message/MC1429018
- [予定] **Purview DLP の Microsoft 以外のアプリ対応が12月下旬に延期** — Microsoft が MC1449180 を更新し、Defender for Cloud Apps のコネクタ経由で Google Workspace・Box・Dropbox などに DLP と自動ラベル付けを掛ける機能の GA を、10月下旬から12月下旬に延ばした
  - https://mc.merill.net/message/MC1449180
- [据え置き] **Roadmap・Release Notes・ブログ** — Roadmap の 10/30 22:08Z バッチは新規5件で、総項目数は 2,229 になった。Copilot 関連の 578225（Frontier の対象を Teams・Outlook・OneDrive・SharePoint のパブリックプレビューへ広げる）は 10/28 の MC1529472 の範囲で、既存の利用者は登録し直さなくてよい。Release Notes は再ビルドされたが先頭は October 27 バッチの14項目のままで、Copilot ブログ・TC の各ブログ・Cowork の Learn 6本・Purview What's New にも新しい記事はない
  - https://www.microsoft.com/microsoft-365/roadmap?id=578225

### Copilot Studio / Power Platform

- [仕様] **Copilot Studio の課金レート表に推論モデルの計算例** — Microsoft が `requirements-messages-management` を 10/31 に改訂し（`ms.date` 10/30）、推論モデルの1メッセージが数百クレジットになる計算例を載せた。推論モデルは計画と回答でモデルを2回呼び、そのたびに指示・会話・検索結果のトークンに課金される
  - 続けて質問した場合: Claude Opus 4.7 のサポート用エージェントで、課金対象 14,100 トークン × 10 Credits / 1,000 トークン = **141 Copilot Credits**（機能ごとのレートは別）
  - 新しい会話で始めた場合: キャッシュから読めるのが 6,000 トークンだけだと **461 Copilot Credits**
  - 同じページの記載: 従量課金につないだ環境ではプリペイドのクレジットが尽きてもエージェントは止まらない。PPAC でエージェントに掛けた月の上限は、そのエージェントが呼ぶエージェントフローを止めない
  - https://learn.microsoft.com/en-us/microsoft-copilot-studio/requirements-messages-management
- [予定] **Power Apps の Copilot 機能の退役を Message Center で再告知** — Microsoft が MC1532421・MC1532426（10/31）で、12/11 以降はメーカーが Copilot による Power Fx 式の作成・編集と Power Apps Ideas を使えなくなり、Copilot がコントロール名を提案しなくなると告知した。昨日（10/31）のハイライト1と同じ内容で、オプトアウトはできず、既存の式とコントロール名は変わらない
  - https://mc.merill.net/message/MC1532421
  - https://mc.merill.net/message/MC1532426
- [据え置き] **What's New・課金・モデル表** — Copilot Studio What's New は `031b66d5`（`ms.date` 10/5）のままで、ハーネスの改名もまだ載っていない。課金5本・PPAC の容量管理・モデル表3本・ガイダンスハブ・非推奨一覧に改訂はなく、Released Versions は 2026.6.3 のまま123日たつ
  - https://learn.microsoft.com/en-us/microsoft-copilot-studio/whats-new

### GitHub Copilot / Google / その他の開発ツール

- [予定] **Antigravity のクラウド実行（未確認）** — TestingCatalog が 10/31 に、Google の Antigravity のビルドにローカル／クラウドの切り替え・Running Jobs 欄・Google Drive 添付が見つかったと報じた。同記事は Google が Jules を畳みつつあると書くが、公式の告知は見つかっていない
  - https://www.testingcatalog.com/cloud-execution-is-coming-to-antigravity-soon/
- [新機能] **Vercel CI のベータ** — TLDR AI（10/29）の要約によると、Vercel はコード変更の影響を受けるタスクだけを必要な計算資源で実行する CI を公開し、社内では push から CI 通過までの時間が2〜6倍短くなったとしている。一次の本文は未確認である
  - https://vercel.com/blog/introducing-vercel-ci
- [据え置き] **GitHub・Google・Cursor ほかの定点** — `github.blog/changelog` の Copilot 最上位は 10/28 の Copilot Fusion、Copilot CLI の安定版は `v1.0.105` のままである。Gemini API changelog は 10/30 の Computer Use GA が最上位で、deprecations の 11/17 停止予定も変わっていない。Cursor（10/20）、Devin（10/28）、Orca（`v1.4.245`）、TypeSafe AI（`jev-1.14.0`）、MCP blog（9/29）、Hugging Face の8 org、xAI のモデル一覧にも新規はない
  - https://github.blog/changelog/label/copilot/

### 業界・市場

- [動向] **Microsoft が約6万人に早期退職を提示** — The Decoder（10/31）によると、Microsoft の最高人事責任者 Amy Coleman が 10/26 付の社内メモで、社員の約4分の1にあたる約6万人に早期退職を提示した。対象は米国・カナダ・インド・英国の VP 以下で、Xbox・Windows・Copilot・Finance は全面的に対象になり、データセンター・営業・サイバーセキュリティ・量子は外れている。2026年の AI インフラ投資は約 $1,700億を見込む
  - https://the-decoder.com/microsoft-offers-a-quarter-of-its-workforce-voluntary-severance-while-shielding-ai-critical-teams/
- [据え置き] **買収協議・調査データ** — Amazon × Decart、Nvidia × Reflection AI の買収協議に続報はなく、IDC Japan・MM総研・NRC の新規公表も検知できなかった

## 直近の注目予定

- **11/1**: AI Builder の容量アドオンが提供終了（MC1526652） ／ Codex の28日間「改善かリセット」の終了（二次）
- **11/2**: xAI `grok-imagine-image-quality` が退役 ／ Meet の63言語音声翻訳が Scheduled Release へ展開開始
- **11/4**: Entra で一般ユーザーのブループリント作成が既定オン（MC1506733） ／ Kimi K3.1 Pro の重み公開の約束期限（二次）
- **11/5 ごろ**: Anthropic のゲスト研究者（生命科学）の応募受付が終了（締切日は明記なし）
- **11月**: GitHub の cloud sandbox の課金が開始（日付は明記なし） ／ Targeted release の割り当てが変更不可になり、統合 Release Preferences 画面が入る ／ Copilot アプリの新しい Home が全世界に出て、Autopilot が Frontier に出る
- **11/9**: Dataverse のみのテナントでストレージ検証が開始（MC1483529）
- **11/12**: Copilot Studio の GPT-4.1 / GPT-5 系が退役（MC1506318） ／ Anthropic Usage Policy 改定版が発効 ／ OpenAI → Cursor のモデル供給停止予定（一次未読）
- **11/15**: Dataverse for Teams 環境とアンマネージド開発者環境の新規作成が停止 ／ Copilot Studio のカスタム採点器ライブラリが GA（MC1531932）
- **11/16**: GitHub Copilot が Claude Opus 4.8・Opus 5・GPT-5.6 Terra を廃止 ／ Teams の旧 GitHub アプリが退役 ／ Cowork / Autopilot の Engage プラグインが GA（MC1530609）
- **11月中旬**: Teams 会議の MeetingAI / TranscriptionWithMeetingAI ポリシーの展開開始（MC1532253） ／ Office in Copilot の展開（MC1530611） ／ Agent Builder のプロンプトのスケジュール実行が開始（MC1302906） ／ Viva Insights の GitHub Copilot 指標が既定オン（MC1523085）
- **11/17**: Gems が Gemini アプリの設定パネルへ移動 ／ Gemini API の TTS・Live プレビュー5種が停止（最短日）
- **11/17〜20**: Microsoft Ignite
- **11/20**: Copilot Studio のコスト管理を M365 管理センターへ移す機能が GA（MC1530368）
- **11/24 以降**: `claude-opus-4-5-20251101` の暫定退役日（確定日ではない）
- **11/29**: OpenAI が Daybreak Blue のセッションデータの学習利用を開始（二次）
- **11/30**: Opus 4.8 の fast mode を削除 ／ `claude-sonnet-4-5-20250929` が Claude API から退役 ／ Power Apps のモデル駆動アプリの説明文の AI 生成・Plan Designer の共同編集・レコード単位の在席表示が退役 ／ OpenAI の Evals・`v1/prompts`・Agent Builder が停止 ／ Gemini 4 Argon の導入価格が終了 ／ Azure DevOps コネクタの旧接続が認証不可に（MC1508508） ／ App Builder と vibe.powerapps.com が退役
- **12/1**: M365 Copilot の前提サブスク不要オファー開始 ／ Copilot Business の従量課金が既定オン ／ Gemini 4 Argon の単価が $4/$20 に倍増 ／ Google スライドの複数スライド作成の上限引き上げ優待が終了しうる
- **12月上旬**: Copilot アプリのタスクバー固定にライセンス別の選択肢が入る（MC1530612）
- **12/11**: Power Apps の式の生成・Power Apps Ideas・Copilot によるコントロール名の変更が退役（MC1532421・MC1532426）
- **12/14**: claude.ai/design の単体サイトが閉鎖
- **12/15**: アンマネージド開発者環境が停止
- **12月下旬**: Purview DLP の Microsoft 以外のアプリ対応が GA（MC1449180・10月下旬から延期）
- **12/31**: Power Platform の環境間のコメントのインポート・エクスポートが終了 ／ Claude Security の無償クレジット（月 $25,000×2か月）の対象期間が終了 ／ Gemini 4 Carbon の導入価格の割引が終了
- **2027-01-06**: OpenAI `tts-1` / `tts-1-hd` / `gpt-4o-mini-tts` 2版が停止
- **2027年1月**: Targeted release が退役 ／ Copilot Studio の Teams アプリで編集ができなくなる（MC1511056） ／ Teams の会議メモリーファイルの生成が開始（MC1429018・延期）
- **2027-01-14**: OpenAI の GPT-4o・GPT-4o mini・GPT-4.1・GPT-4.1 mini が API から削除（→ `gpt-6-luna`）
- **2027-01-15**: アンマネージド開発者環境の削除開始 ／ Claude Code Review の Enterprise 向けクレジット請求期限
- **2027年1月中旬〜下旬**: 旧来の Teams 保持ポリシーが Copilot の対話に効かなくなる（MC1481313）
- **2027-03-01 以降**: Gems 廃止（Business / Enterprise）
- **2027年3月**: Purview の DSPM classic / DSPM for AI classic が退役（MC1481315）
- **2027年3月末**: Outlook の Copilot Prioritize の削除が完了（MC1519861） ／ SharePoint / OneDrive の `.agent` 形式エージェントが動かなくなる（MC1511052）
- **2027-04-01**: OpenAI `gpt-5.1` / `gpt-5.3-codex` / `gpt-5.4-nano` が停止

## 改善メモ

- 新規提案: industry が B-047（TLDR AI の週次スイープを `tldr.tech/ai/YYYY-MM-DD` の curl 取得に切り替える）を起票した。Master・Copilot は新規起票なし
- 継続提案: Copilot は継続2件（最多 B-080 Cowork の Learn URL 差し替え、6回目。B-081 ハーネス改名は Learn が本日も旧名のまま、4回目） ／ industry は継続5件（最多 B-040 セキュリティ開示の定点、13回） ／ Master は見送り候補 B-036 / B-037 / B-043 / B-078
- 障害の変化: industry が `www.indiatoday.in` のゲートウェイ拒否を新規に記録した。Master・Copilot は記録なし
- 欠損リカバリ: 前日（10/31）分は3ソース揃っており、対象なし
- ソース間の差分・矛盾:
  - Claude Code `2.1.316` のタグは、Master が [破壊的変更+新機能]（管理設定の承認なし適用を主旨）、industry が [新機能]（`pooled_budget` を主旨）とした。日次は管理設定の適用方法の変更を破壊的変更とみて Master のタグを採った
  - `2.1.315` について、industry は「欠番」、Master は「10/30 に npm に publish されたが changelog に項が無い」と書いている。日次は npm を確認した Master の記述を正とし、本文では触れていない
  - Opus 4.8 の fast mode 削除までの日数は、Master が「告知から31日」、industry が「29日以内」と起点が異なる。日次は本日（11/1）起点の29日で書いた
