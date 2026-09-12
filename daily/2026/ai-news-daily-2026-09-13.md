# AI News Daily Summary — 2026-09-13

モデルを「誰から、いつまで借りられるか」が3件同時に動いた日である。Claude Code の週次上限の増枠は本日で終わり、OpenAI は `gpt-5.4-cyber` を20日通知で退役させ、Cursor へのモデル供給そのものを 11/12 で打ち切ると通告した。Microsoft 側では Grok が Copilot に載ったが、その経路には Product Terms も著作権補償も適用されない。GreyNoise は AI エージェント群が48カ国395組織を侵害した実例を外形観測から公表している。

## 今日のハイライト

### 1. Claude Code の週次上限50%増が本日で終了する — 明日からの恒久 +25% は現行比では17%減

**要点**: Claude Code の週次上限50%増が本日 9/13 で終わり、9/14 から標準週次上限が恒久的に **+25%** になる。+25% は増枠前の基準に対する値なので、+50% で回してきた実効枠は明日から17%縮む。

**詳細**: 対象は Pro / Max / Team とシート課金 Enterprise である。増枠は 7/19 期限から 8/19 へ、さらに本日へと延長を重ねてきたもので、恒久化されるのは増枠後の水準ではなく増枠前の基準に +25% を乗せた水準になる。週次でセッションを詰めている使い方では、明日以降に上限到達が早まる形になる。⚠️ この期限は 09-01 以降の各サマリーで予定として記録してきたもので、本日が発効日にあたる。

- https://www.anthropic.com/news

### 2. OpenAI が `gpt-5.4-cyber` を20日通知で退役させる — GA モデルに6か月の猶予があるという前提が崩れた

**要点**: OpenAI が 9/11 に `gpt-5.4-cyber` の退役を告知し、停止を **10/1** に置いた。通知期間は20日で、同じページが定める「GA モデルは最低6か月」を大きく下回り、退役予告に6か月の猶予を見込んだ移行計画が成り立たなくなる。

**詳細**: 一次 `developers.openai.com/api/docs/deprecations` に 2026-09-11 付の新規エントリを確認した。対象は `gpt-5.4-cyber` 単体で、移行先は `gpt-5.6-cyber` である。同ページの方針欄は「安全性またはコンプライアンス上の懸念により早期の退役が必要な場合を除き、一般提供モデルには最低6か月の通知期間を設ける」と定め、例外条項は「早期に退役させる場合は合理的に可能な限りの通知を行う」となっている。⚠️ **告知本文に短縮の理由は書かれていない**ため、例外条項の適用なのか運用上の判断なのかは一次から判別できない。

本件は 09-04 以降「単価欄が空のまま」と記録し続けてきた状態を説明する。同じ Cyber 節の `gpt-5.6-cyber` / `gpt-5.5-cyber` は入力 $12.50 ／出力 $75（1Mトークン）で据え置かれており、空欄は掲載漏れではなく退役準備だったことになる。廃止ページの最新告知日も 8/26 から 9/11 へ16日ぶりに進んだ。

- https://developers.openai.com/api/docs/deprecations
- https://developers.openai.com/api/docs/pricing

### 3. OpenAI が Cursor へのモデル供給を 11/12 で打ち切る — ツールの傘下が可用性を左右するようになった

**要点**: OpenAI が契約の change-of-control 条項を発動し、Cursor への自社モデル提供を **2026-11-12** で停止する。どのベンダーのモデルを使うかだけでなく、そのツールが誰の傘下にあるかが可用性リスクになる前提へ変わった。

**詳細**: SpaceX による Anysphere（Cursor 開発元）の $60B 買収完了（8/14）を受け、OpenAI が **8/28** に条項を発動した。遮断予定日の 11/12 は契約上の最大通知期間にあたり、OpenAI は開発者がモデルを使える期間を最大化するためだと説明している。理由として挙げているのは Musk 傘下の企業が過去に契約と利用規約に違反した経緯で、SpaceX が自社技術を規約の範囲で使う確証が持てないとしている。

- Cursor 側の反応: 共同創業者の Michael Truell は X で、OpenAI モデルは Cursor のユーザートラフィックの約5%にとどまり OpenAI と協議中だと述べた
- Anthropic 側の反応: 共同創業者の Tom Brown が Cursor 向け Claude の計算資源を増やすと表明しており、供給停止が競合の取り込み機会として働いている
- ⚠️ **一次未読**（`openai.com/index/our-decision-on-cursor-following-its-acquisition-by-spacex/` は HTTP 403）。出来事は 8/28〜8/29 で、本サマリーは本日が初検出にあたる

- https://www.cnbc.com/2026/08/29/openai-cursor-spacex-model-access.html
- https://www.digitaltrends.com/computing/stung-by-openai-pulling-gpt-models-from-cursor-anthropic-offers-a-timely-lifeline-with-higher-claude-limits/

## カテゴリ別まとめ

### Anthropic / Claude

- **週次上限の切り替え**: （ハイライト1参照）
- **Claude Code `2.1.269`**: Anthropic が前日は版番号しか分からなかった版の changelog を公開し、権限とサンドボックスまわりを中心に変更した
  - 権限ルール: `!` で始まる deny / ask ルールが、それを書いた設定ソースの中だけに適用されるようになった。単独の `!` 否定は無視される
  - 書き込み経路: `Edit()` の deny ルールと書き込みパス検査が Bash の `tee` の出力先にも掛かり、`Bash(tee:*)` の allow だけでは作業ディレクトリ外へ書けなくなった
  - プラグイン展開: 展開したアーカイブが他のローカルユーザーから読める問題、world-writable ビットを引き継ぐ問題、再展開時に古いファイルが残る問題が直った
  - 新コマンド: `claude plugin eval` がプラグインの eval スイートを実行して JSON と HTML のレポートで採点する。`/output-style [name]` は Remote Control とクラウド / headless セッションでも使える
  - 環境変数3種が加わった: `CLAUDE_CODE_WORKFLOW_MAX_CONCURRENT_AGENTS`（1〜256）／ `OTEL_METRICS_INCLUDE_REPOSITORY` ／ `CLAUDE_CODE_GATEWAY_MODEL_DISCOVERY_TIMEOUT_MS`（既定3秒）
  - prompt cache: 出力トークン上限で切れて自動再開した次のターンでの部分無効化と、中断後の resume でキャッシュ再利用が落ちる問題が直った
  - https://code.claude.com/docs/en/changelog
- **Claude Code `2.1.270`**: Anthropic が 9/12 に公開し、修正1件だけを入れた。セッションを長時間動かしたあとに Bash の読み取り専用 git コマンドが予期せず権限を求める **`2.1.269` の回帰**を解消している
  - ⚠️ 01 は本版を「changelog に無く内容未確定」と記録し、03 は上記の内容を確定させた。前日の `2.1.269` と同型の食い違いで、改善メモに記録する
  - npm の `dist-tags` は `{stable: 2.1.236, latest: 2.1.269, next: 2.1.270}` で、**stable と latest の差は33版**に開いた（前日32版）。`stable` 固定の組織には権限ルール・`tee` 書き込み検査・プラグイン展開権限の3件がまだ届いていない
- **Anthropic の公表面は3経路とも静止している**: `www.anthropic.com` の `/news`・`/research` と `claude.com/blog` は 9/11・9/12 とも新規がなく、いずれも本文取得には成功しているので到達性の問題ではない。`/news` の最新は 9/10 の脅威インテリジェンスレポート、`/research` は 9/10 の危険能力測定、`claude.com/blog` は 9/10 の2本である
- **Platform API / アプリのリリースノート**: Anthropic の Platform API release notes は 9/10 の Managed Agents 権限ポリシー `auto` が最上位のままで、`support.claude.com` 側も 9/10 の Smart reports（ベータ・Enterprise 対象）から動いていない。単価・上限の改定告知も出ていない
- **モデル退役ページ**: Anthropic の Active は11件で据え置き、暫定退役日にも変更がない。表の外の Note で `claude-mythos-preview` が deprecated 扱いである点も変わらない
- ⚠️ **8月 Risk Report は28日連続で一次未読である**（初出 08-17）。`/research` の一覧10件にも現れず、WebSearch でも一次 URL を特定できていない

### OpenAI / ChatGPT / Codex

- **`gpt-5.4-cyber` の退役**: （ハイライト2参照）
- **Cursor への供給停止**: （ハイライト3参照）
- **ChatGPT デスクトップの Pets と Appshots が Windows へ広がった**（9/11・Windows 26.908）。他アプリで作業したまま浮かぶ Pets のコントロールから即席のチャットを送れ、`@` で参照先、`$` でスキルを指定する。Appshots は Alt を2回押すと最前面のアプリのウィンドウを ChatGPT に渡す仕組みで、ショートカットと送り先は変更できる
- **`gpt-rosalind-research` が trusted-access program 経由で GA になっていた**（9/8）。対象は承認済み参加者が行う社内のライフサイエンス研究に限られ、料金は入力 $5 ／キャッシュ入力 $0.50 ／出力 $25（1Mトークン）、**課金開始は 2026-10-05** である
  - ⚠️ この項目は 9/8 の changelog にありながら 09-08〜09-12 のどのセッションでも記録されていなかった（同一日の3件目が落ちた形）
- **一次料金ページは20日連続で据え置きとなった**。GPT-6 Astra は短文脈 $10 ／$50・長文脈 $20 ／$75、GPT-5.6 Sol は短文脈 $4 ／$20 で期間限定価格が「少なくとも **2026年11月21日**まで」の記載のまま、Terra は $2 ／$12、Luna は $0.20 ／$1.20 である。Batch・Flex が標準の50%、Fast mode が標準の2倍という構造にも変化はない
- **changelog と Announcements はいずれも 9/10 が最上位のままである**。`developers.openai.com/api/docs/changelog` は Agents API パブリックベータ / GPT-Live 1 GA / プロジェクト API キーの有効期限の3本、`community.openai.com` の Announcements RSS は Agents API 告知が先頭で、9/11・9/12 の追加はない
- **Codex CLI は pre-release `rust-v0.155.0-alpha.3.10`（9/11）が最新で、9/12 の新規リリースはない**。⚠️ 安定版は接頭辞で分かれ、rust 側は `rust-v0.154.0`（9/9）、python 側は `python-v0.154.0`（9/10）である。releases ページ最上位の非 pre-release だけを見て「最新の安定版」と読まないこと
- ⚠️ `learn.chatgpt.com` はゲートウェイ拒否が継続しており、本日も `site:` 付き WebSearch で内容を確認した。9/5 以降は 9/8 の ChatGPT for iOS 1.2026.244、9/9 の Codex CLI 0.154.0、9/10 の Python SDK 0.154.0、9/11 の Pets / Appshots が確認できる

### Microsoft / GitHub Copilot

- **Copilot に Grok が載ったが、その経路には Microsoft の契約保護が適用されない**（9/12 15:00Z 告知）。管理者が有効化を判断する対象はモデルの良し悪しではなく契約条件の切り替えになる
  - 提供範囲: Microsoft Frontier Program 経由で **Word / Excel / PowerPoint** から開始する。⚠️ プレビュー期間中、EU・EFTA・英国の Frontier 顧客は対象外である
  - 適用されないもの: Product Terms、Data Processing Addendum、データ所在地コミットメント、監査およびコンプライアンス要件、SLA、Customer Copyright Commitment。代わりに xAI Enterprise Terms of Service と xAI DPA が適用される
  - 有効化: M365 管理センター > Copilot > Settings > View all > AI providers for other large language models で SpaceXAI を選び、法的条件に同意してユーザー／グループを指定する。グローバル管理者ロールが必要で反映に数時間かかり、無効化は同じ画面で No users を選ぶ
  - Copilot Studio 側は Power Platform 管理センターの「Allow external large language models (LLMs) for generative responses」で別途許可する
  - ⚠️ **一次は M365 アプリ経路について書いていない**。`connect-to-ai-models` は対象を「Copilot Studio in Microsoft 365」としか書かず、告知が挙げる Word / Excel / PowerPoint に同じ契約除外が掛かるかは明示されていない
  - https://techcommunity.microsoft.com/t5/microsoft-copilot-blog/expanding-model-choice-in-copilot-with-grok/ba-p/4555749
  - https://learn.microsoft.com/en-us/microsoft-365/copilot/connect-to-ai-models
- **Copilot code review が指摘を自動解決し、シェル実行で検証するようになった**（9/11）。指摘に対応するコミットを push すると再レビュー時に Copilot 自身が該当スレッドを解決するため、手動でのスレッド解決が要らなくなる
  - 検証の強化: ファイアウォール下で SDK の完全なシェルツールを使い、ビルド・テスト実行・スクリプトによる検証ができるようになった
  - Lite の合議化: 単一エージェントのレビューから複数エージェントの見解を統合する ensemble 方式へ変わり、高深刻度の指摘の対応数が **47%** 増、中が31%増、低が11%増で、コストは約8%減とされる
  - 提案を適用するときのコミットメッセージも、自動入力の定型文から内容に即した文面へ変わった
  - ⚠️ 提供段階と対象プランは告知本文に明記がない
  - https://github.blog/changelog/2026-09-11-auto-resolution-and-analysis-updates-in-copilot-code-review/
- **VS Code Agents の利用指標が Copilot 利用状況メトリクスに入り GA になった**（9/11）。管理者がエージェント利用を既存 API で測れるようになる
  - 集計レポートに `daily_active_vscode_agent_users` と `totals_by_vscode_agent`、ユーザー単位レポートに `used_vscode_agent` と `totals_by_vscode_agent` が加わる
  - 対象は Enterprise オーナー・支払い管理者・Organization オーナーと View Copilot Metrics 権限を持つカスタムロールで、利用状況メトリクスのポリシー有効化が前提になる
  - 計上されるのは**専用の VS Code Agents ウィンドウだけ**で、エディタ内の Agent Mode とは別枠である。追加フィールドは任意扱いのため既存の連携は壊れない
  - https://github.blog/changelog/2026-09-11-add-vs-code-agents-to-copilot-usage-metrics/
- **GitHub changelog の 9/11 分は当日 0件から2件へ増えていた**。09-12 の確認では 9/11・9/12 をいずれも0件と記録したが、本日同じ一覧を読むと 9/11 付が上記2件掲載されている。9/10 分も6件から7件に増えており、降順ページの当日追記を翌日読み直す必要があることが5例目として確認された
- **Copilot CLI は pre-release `v1.0.84-5`（9/11）が最新で、セマンティック JSONL でのセッションとメモリのインポートに対応した**。安定版は `v1.0.83`（9/4）のまま8日間据え置きである
- **Microsoft Partner Center の9月ページは 9/10 から更新がない**。掲載9件のままで、月次の AI Cloud Partner Program update は例月の第2週を過ぎても未掲載である（2日連続）。CSP ソフトウェア価格改定の **10/1 発効**に変更の告知は出ていない

### Copilot Studio / Power Platform

- **Copilot Agent Kit の9月リリースが 9/8 に出ていた**（週次確認の期日が本日のため初検知）。Agent Inventory が **GitHub Copilot ハーネス**に対応し、8/3 GA 以降そのハーネスで作ったエージェントを棚卸しできなかった状態が解消する
  - Agent Inventory V2: Code App アーキテクチャで作り直され、収集メタデータに MCP List・接続されたエージェント・Agent Owner ID が加わった
  - Agent Review Tool: バージョン履歴が入り、エージェントのバージョン間で評価結果を比較できるようになった
  - Agent Debugger: セッションセレクター、トランスクリプトの高度なフィルター、実行が最も遅いステップの特定を備えた UI に刷新された
  - Agent Change Tracker と Advanced Testing: 変更活動の監査履歴アナリティクスが加わり、Adaptive Card 応答の検証で Contains 演算子を使えるようになった。修正は20件
  - ⚠️ リリース周期（ほぼ月次）と確認頻度（週次）のずれが上限値どおり出て、9/8 公開から検知まで5日かかった
  - https://github.com/microsoft/Power-CAT-Copilot-Studio-Kit/releases/tag/CopilotAgentKit-September2026
- ⚠️ **Work IQ ボタンの食い違いが「訂正」ではなく「片方の消滅」で終わった**。`learn.microsoft.com/en-us/copilot/which-copilot-for-your-organization` が本日 HTTP 404（転送先なし）を返し、旧パスの 301 転送先は Work IQ を「Microsoft Graph と並ぶグラウンディング元」としてのみ扱ってボタンの意味を書いていない。「オフのとき Web 結果も出る」という記述は一次から消え、Release Notes の August 25 バッチの記述だけが残った
- **M365 Copilot Release Notes に新バッチは追加されていない**。先頭は **August 25, 2026**・H2 は83本のままで、隔週の期日 9/8（UTC）から5日、前バッチからは19日が経過した
- **Copilot Studio の What's New も新規節がない**。**July 2026** 節が最新で8月節・9月節とも未作成のままである。⚠️ June 節の GitHub Copilot ハーネスは `(Production-ready preview)` 表記のままで、GA（8/3）から41日連続の未反映になる。同じハーネスを Power CAT 側は本日のリリースで棚卸し対象に入れており、製品ドキュメントだけが GA に追いついていない
- **Roadmap の新規起票は本リポジトリ対象で1件だった**。**570277**（Word の Copilot edit mode が Office 365 GCC で提供・GA 2026年10月）で、政府機関の顧客が文書内で Copilot を共同作成者として使えるようになる
  - ⚠️ Copilot Studio と Power Platform 系の新規起票はゼロで、広報枠は 7/24 の Opus 5 記事のまま51日動いていない。Fable 5.1（9/2）・GPT-6 Astra（9/4）・Grok（9/12）の3件が「Available today」型でありながら未掲載である
- **Released Versions は74日更新がない**。Copilot Studio Build の最新は **2026.6.3**（UX 26.06.21-24）で、日本・欧州・英国・アジア・UAE は 2026.6.2、米国・オーストラリア・GCC は 2026.6.1 に留まる。ページ本文が「毎週火曜に更新」と書きながら 9/8 の定例日も空振りし、次回は 9/15 になる
- **Release Wave のリネーム後5ページは10日連続で据え置きである**。`updated_at` 2026-09-03T14:35Z・緑チェックの増減もなく、登録 URL は本日も 301 で `aka.ms/MCStoM365Roadmap` へ転送されてゲートウェイ拒否になる
- ⚠️ **Copilot Tuning は停止発効（8/20）から24日たっても一次が停止も退役も書いていない**。`copilot-tuning-overview` は「Access through Frontier is planned for April 2026」という既に過ぎた予定を現在形で残している
- ⚠️ **Purview 側は Cowork 向け DLP（570845・Preview 9月 / GA 10月）を未掲載のままである**。`purview/whats-new` は 8/28 から9月節が未作成で、`purview/ai-copilot-cowork` も 6/25 から動かず 9/11 の Cowork 一式再ビルドの対象外だった

### セキュリティ

- **AI エージェント群が PaperCut を突き、48カ国395組織を侵害した**。GreyNoise が 9/11 に公表し、前日の Anthropic レポートが自社ログで示した「人間は標的選定だけ」の構図が別ベンダーの外部観測でも裏づけられた
  - 攻撃は **8月31日**開始で、PaperCut NG/MF の CVE-2026-81578 と CVE-2026-82078 を悪用した。被害は判明分で440インスタンス・395組織に及ぶ
  - 構成は OpenAI Codex のハーネスと DeepSeek モデルの組み合わせに市販の攻撃ツールを載せたもので、オーケストレーションに AionUI、永続メモリに Hindsight、標的リスト生成に Netlas のスキャン基盤が使われた
  - 到達段階は資格情報の窃取が280組織、OS またはドメインの機密取得が147組織、管理者権限の奪取が12組織。業種別では教育が204件と突出するが、GreyNoise は PaperCut の顧客構成の反映と見ている
  - ⚠️ **キャンペーン開始から26秒で11組織が侵害された**と観測されており、人手による初動対応が追随できない速度域に入っている。一次の `greynoise.io` はゲートウェイ拒否のため数値は二次の突き合わせによる
  - https://www.helpnetsecurity.com/2026/09/11/ai-agents-papercut-ng-mf-attack-campaign/
  - https://www.bleepingcomputer.com/news/security/ai-powered-attack-exploited-papercut-flaws-to-hack-395-organizations/

### Google

- **Gemini API changelog は10日間動きがない**。9/3 の Lyria 3.5 public preview が最上位のままで、9/2 の `gemini-3.8-flash` GA・9/1 の agentic video understanding から追加がなく、料金改定の告知も出ていない
- 到達できる Google 一次が `ai.google.dev` だけという状態は変わらず、登録済み5ソースはゲートウェイ拒否が継続している。HF の `google` org も `gnm-v3`（9/1 作成）が最新のままである
- 既報: `gemini-3.8-flash` の導入価格 $0.75 ／$3.75 は **2026-12-31** まで、旧 `gemini-omni-flash-preview` は 9/30 廃止（後継 `gemini-omni-1.1-flash`）、Gemini 3.5 Pro GA は未ローンチが継続

### Cursor / xAI / Devin

- **OpenAI からの供給停止**: （ハイライト3参照）
- **Grok 4.7 は公開予定日 9/12 を過ぎても出ていない**。Musk は 9/11 に「あと数日必要」と述べ、理由として強化学習で応答長を過度に減点した結果として解ける難問でもモデルが早々に諦めること、自己検証がまだ厳密でないことを挙げた。新しい日程は示されていない
  - ⚠️ xAI 一次にはモデル ID・価格・コンテキスト長・ベンチマーク表のいずれも無く、出所は引き続き Musk の X 投稿だけである。公式提供中の最新は **Grok 4.6**（8/12・context 50万トークン・$2 ／$6）のままになる
- **Cursor changelog は 9/10 の Projects が最上位のままで、フォーラム Announcements は 9/2 から11日間動いていない**。⚠️ Cursor は GPT-6 Astra の提供開始を告知しないまま10日目で、これは changelog とフォーラムの両方を確認したうえでの不在である
- Devin は `docs.devin.ai` / `cli.devin.ai` ともゲートウェイ拒否で、一次・代替一次のいずれからも読めない状態が続いている

### MCP / オープンウェイト / 市場データ

- **Sakana AI が Fugu Max と Fugu Ultra v2 を公開した**（9/11）。いずれも単体モデルではなく、タスクを他モデルへ振り分けて結果を統合するオーケストレーターで、OpenAI 互換の単一 API の裏でモデルプールを選択する
  - Fugu Max: 入力 $2 ／出力 $6（1Mトークン）。NVIDIA Nemotron 系を含む open-weight・特化モデルへプールを広げ、解ける範囲で最も安いモデルへ振る
  - Fugu Ultra v2: 入力 $5 ／出力 $30、キャッシュ読み取り $0.5、Web 検索 $10 ／1,000回。272Kトークン超の文脈では入力 $10 ／出力 $45 へ上がる
  - ⚠️ 一次の `sakana.ai` は未試行で単価は二次の突き合わせによる。**Copilot CLI の Project HydraFusion**（09-12 収録）と同じ方向の製品化が独立に2社から出た形になる
  - https://openrouter.ai/sakana/fugu-ultra-v2
- **オープンウェイトは 8 org のいずれにも新規公開も更新もない**。`Qwen` / `moonshotai` / `deepseek-ai` / `meta-models` / `mistralai` / `zai-org` / `openai` / `google` を作成日降順と更新日降順の両方で確認し、9/12 に更新されたリポジトリは1件もなかった
  - 各 org の最新作成は `DeepSeek-V4.1-Flash` 9/10 ／ `gnm-v3` 9/1 ／ `Qwen-Drive-1.0-4B` 8/27 ／ `GLM-5.3-Flash-BF16` 8/25 である
- **MCP 公式ブログは22日間新規がない**。`blog.modelcontextprotocol.io` の RSS は 200 を返すが 8/22 の The New MCP Roadmap が最上位のままで、WebMCP Challenge は受賞発表 9/23・賞金総額 $35,000 の予定である
- **市場データの定点ソースに新規公表はない**。IDC・MM総研・NRC・Similarweb のいずれにも本日の公表を検知できず、Similarweb は8月分（ChatGPT 55.5%・Gemini 25.6%・Claude 9.3%）が最新で次回は10月上旬になる
- **Apple Developer News も 9/9 の2本から動いていない**。⚠️ AI 固有のエントリは 6/11 の ImageCreator クラス廃止告知のままで3か月動いておらず、「新しい Siri は Google Gemini で動く」と SiriKit 退役・App Intents 2.0 の内訳は引き続き二次のみで確定として扱わない

### 企業構造 / GTM 動向

- **モデル供給契約が競争上の手段として使われた**。OpenAI による Cursor への供給停止は、供給元1社に依存する構成のリスクを具体化した事例で、Anthropic が計算資源の増強で受け皿に回る構図も同時に出ている（ハイライト3参照）
- 既報（一次未読含む）: OpenAI が拘束力ある連邦 AI 安全規制を求めた件（9/9・12月の議会閉会前の立法を要求）、Sam Altman が最先端 AI の開発減速の選択肢を社内に示したとの報道（9/11・Bloomberg 1本）、OpenAI と GSA の27か月 OneGov 契約、Anthropic の秋 IPO 観測（**上場日は未確定**）、SpaceX による Cursor 買収完了（8/14・$60B）

## 直近の注目予定

- **9/13（本日）**: **Claude Code の週次上限50%増が終了**
- **9/14**: **Claude Code の標準週次上限が恒久的に +25%**（Pro / Max / Team / シート課金 Enterprise。現行比では17%減）／ iOS 27 / iPadOS 27 の配信（二次情報）／ 週次復旧チェック（月曜）
- **9/15**: Power Platform Released Versions の定例日（火曜）
- **9/16**: PnP Power Platform コミュニティコール
- **9/17**: OpenAI DevDay Exchange の応募締切 ／ Anthropic Startup Grant Program の配分年度締切（二次のみ・一次に記載なし）
- **9/18**: 新 iPhone と AirPods 5 の発売
- **9/20**: Power CAT・PnP・拡張機能 What's New の週次確認
- **9/21**: Anthropic ウェルビーイング研究助成の応募締切 ／ ppweekly・MS-4005・課金レート表の週次確認
- **9/22 前後**: M365 Copilot Release Notes の次バッチ（隔週周期。9/8 の期日は空振り）
- **9/23**: WebMCP Challenge の受賞発表 ／ Partnering for Success Together 初回セッション
- **9/24**: **OpenAI の Videos API と Sora 2 系が退役**（代替モデルの提示なし）
- **9/28**: Copilot のチャット3面統合 ／ code review の既定 effort が Lite → Balanced ／ チャットのデータ保持がアカウント存続期間へ ／ **OpenAI の `gpt-3.5-turbo-instruct` / `babbage-002` / `davinci-002` / `gpt-3.5-turbo-1106` が停止**
- **9/29 以降**: `claude-sonnet-4-5-20250929` の暫定退役日（確定日ではない）
- **9/30**: Gemini の旧 `gemini-omni-flash-preview` エンドポイント廃止 ／ OpenAI の現行 OneGov 契約（$1/年）が失効 ／ M365 E7 プロモ最終日 ／ E5・E3 の CSP 割引終了 ／ 2026 Wave 1 の対象期間終了
- **9月**: macOS 27 GA ／ Claudeforce のオープンベータ（二次情報）／ Purview DLP for Cowork の Preview ／ Copilot Tuning の Public Preview 再開 ／ Copilot デスクトップアプリの広範展開
- **10/1**: **OpenAI の `gpt-5.4-cyber` が API から削除される**（移行先 `gpt-5.6-cyber`） ／ OpenAI の OneGov トークン課金50%割引が開始 ／ Copilot Business・Enterprise の既存顧客が前払い必須に ／ CSP ソフトウェア価格改定が発効 ／ Apple の EU 向け新ビジネス条件が発効
- **10/2**: **GitHub Copilot が Gemini 3.5 Flash / Gemini 3.6 Flash / Kimi K2.7 Code / Claude Opus 4.7 を全体験から廃止**
- **10/5**: **GPT-Rosalind の課金が開始** ／ Anthropic ウェルビーイング研究助成の full proposal 提出期限（採択者）
- **10/15 以降**: `claude-haiku-4-5-20251001` の暫定退役日（確定日ではない）
- **10/16–11/11**: OpenAI DevDay Exchange 8都市（東京は 10/20）
- **10/23**: OpenAI のレガシースナップショット退役（`gpt-3.5-turbo-0125` / `gpt-4-0613` / `o1-2024-12-17` / `o4-mini-2025-04-16`）
- **10/27–29**: Power Platform Community Conference 2026
- **10/31**: OpenAI の既存 evals が読み取り専用になる
- **10月下旬まで**: METR による Anthropic のインシデント独立調査の初回8週間（9/9 起点）
- **10月**: Anthropic の IPO 観測（上場日は未確定）／ Roadmap 12件の GA / Preview 期日 ／ 韓国 App Store のコンテンツ記述子2件が All → 12+
- **11/12**: **OpenAI が Cursor へのモデル供給を停止する予定日**（契約上の最大通知期間・一次未読）
- **11/15**: Release Planner の退役。Release Wave の緑チェックに依存する GA 検知経路がこの日までに失われる
- **11/21**: GPT-5.6 Sol の暫定値下げが有効とされる期限
- **11/24 以降**: `claude-opus-4-5-20251101` の暫定退役日（確定日ではない）
- **11/30**: OpenAI の Reusable prompts・Evals プラットフォーム・Agent Builder が停止
- **12/1**: OpenAI の GPT Image 系が停止（→ `gpt-image-2`）
- **12/2**: EU AI Act の生成コンテンツ標識義務、8/2 以前に市場投入済みシステムへの猶予終了
- **12/11**: OpenAI の旧スナップショット退役（`gpt-5-2025-08-07` / `o3-2025-04-16` / `o3-pro-2025-06-10` 等）
- **12/31**: **Gemini 3.8 Flash と 3.7 Flash の導入価格が終了**（$0.75 ／$3.75 → $1.50 ／$7.50）／ **GitHub Copilot の ZDR 暫定免除が終了**（Fable 5.1 / Fable 5）
- **年内**: Anthropic の新データ保持方式（顧客自身のクラウドでの30日保持）投入予定 ／ OpenAI の Jalapeño チップの初期展開
- **2027-01-06**: OpenAI で大半のユーザーの新規ファインチューニングジョブ作成が終了
- **2027-01-20**: OpenAI の audio / realtime 系退役（`gpt-realtime` / `gpt-audio` / `gpt-4o-audio` と mini 系）
- **2027-02-26**: OpenAI の文字起こし4モデル退役（`whisper-1` ほか）
- **2027-03-01 / 2028-10-01**: SharePoint クラシックの退役
- **2027-04**: **Apple の最小 SDK 要件が iOS 27 世代へ上がる**
- **2027-06-30**: Claude for Teachers の学区登録期限
- **2027年末**: Anthropic が借りる Nscale West Virginia データセンター（460MW）の稼働開始見込み
- **2028-03**: OpenAI が「automated AI researcher」の実現目標とする時期

## 改善メモ

- ソース間の食い違い: Claude Code `2.1.270` について、01 は「changelog に無く内容未確定」、03 は「回帰修正1件（読み取り専用 git コマンドの権限要求）」と記録した。前日 `2.1.269` で起きた食い違いと同型で、2日連続になる。01 の巡回（当日 04:10 頃）が 03（同 05:10 頃）より早いことが原因として説明できるかは、次回 changelog の掲載時刻を確認して判定する
- 新規提案: 01 が B-069（登録ツールに対する他社モデル供給の停止・契約解除を検出する検索軸を常設）、02 が B-065（モデル追加告知の提供面と契約条件を定める一次ページの対象面が一致しない問題）を起票した。03 は新規提案なし
- 継続提案は 01 が19件（最多 B-013 403の2分類・43回目）、02 が41件（最多 B-011 Power Platform Blog のトピック記事照合・52回目）、03 が4件（最多 B-004 取得方法欄の WebSearch 化・76回目）
- ⚠️ 02 の継続提案は前日の「32件・B-011 は53回目」から「41件・52回目」へ変わり、件数と回数の増減方向が逆になった。台帳の集計方法が日によって違う可能性があり、件数サマリを推移として読めない
- 障害の変化: 03 が `www.greynoise.io` を新規のゲートウェイ拒否として台帳に追加した。02 は `learn.microsoft.com/en-us/copilot/which-copilot-for-your-organization` が転送先を示さない HTTP 404 になったことを記録している（取得障害ではなくソース側の変更のため台帳の障害欄には未記載）
- 降順ページの当日追記による取りこぼしが本日も出た。GitHub changelog の 9/11 分は 09-12 時点で0件、本日読み直すと2件で、9/10 分も6件から7件に増えている。01 の同型の既知課題と合わせて5例目になる
