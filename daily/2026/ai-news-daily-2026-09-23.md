# AI News Daily Summary — 2026-09-23

フロンティアモデルの単価が同じ日に2社そろって落ちた日である。Anthropic は Claude Opus 5.5 を Opus 5 比2割安で出して Claude Code の既定 Opus にし、OpenAI は GPT-6 Sol / Luna を 5.6 系の半額で API・Codex へ入れた。どちらも発表の第一声が性能ではなく価格で、手元では Claude Code `2.1.280` が既定モデルと symlink 経由の書き込み承認を同時に変えている。Microsoft 側では M365 Copilot の推論を国内で実行する計画が Roadmap に起票された。

## 今日のハイライト

### 1. [料金+破壊的変更] Claude Opus 5.5 が $4/$20 で出て既定の Opus になった — 「Opus は高いので Sonnet で回す」前提が崩れた

**要点**: Anthropic が Claude Opus 5.5 を $4/$20 で公開し、既定の Opus に据えた。Fable 5.1（$10/$50）相当の仕事が6割安く回るようになり、費用で上位モデルを見送っていた用途の試算が引き直しの対象になる。

**詳細**: `claude-opus-5-5` はコンテキスト 1M・最大出力 128k・adaptive thinking 常時オンで、キャッシュ読み取りは $0.50 → $0.20 の6割減、キャッシュ書き込みは $6.25 → $5 である。Anthropic は「Opus 5 比で典型的なワークロードのコストが 40% 減」「出力生成が 30% 以上高速」「同じ high effort の結果を出力トークン 20〜25% 少なく達成」としている。ベンチマークは Terminal-Bench 4.0 が 66.4%（Opus 5 は 52.3%）、CursorBench 4.0 が 57.8%（同 46.6%）、FrontierCode v1.1 が 54.4%（同 48.0%・GPT-6 Astra の 53.3% を上回り「約5分の1のコスト」と併記）、OSWorld 2.0 が 81.8% partial（同 74.0%）、AutomationBench が 40.0%（同 26.9%）、GDPval-AA v2.1 が Elo 1846（同 1708）。

- 位置づけ: Claude 5.5 ファミリーの第1弾で、Sonnet 5.5 と Haiku 5.5 が数週間内に続くと明記されている
- プラン側: Pro / Max / Team / シート課金の Enterprise で5時間の利用上限が引き上げられ、サブスク利用者にはレート制限のリセットが1回、任意のタイミングで使える形で付与される
- Fast mode: Claude Code と Claude Platform で最大 2.5 倍速・$8/$40。Bedrock・AWS・Google Cloud・Microsoft Foundry では提供されない
- セーフガード: 生体系の分類器が追加され、サイバー系タスクの大半は Opus 4.8 へ再ルーティングされる。阻害される業務は Life Sciences Verification Program へ申請する
- 提供面: Claude API（`claude-opus-5-5`）／ Amazon Bedrock（`anthropic.claude-opus-5-5`）／ Claude Platform on AWS ／ Google Cloud ／ Microsoft Foundry。同日 GitHub Copilot にも入った（Pro+ / Max / Business / Enterprise・**Pro は対象外**）
- 退役日: 暫定退役日は 2027-09-22 以降として退役表に載り、Active は13件から14件に増えた

⚠️ **Opus 5 で動くコードに影響する API の破壊的変更が4件ある。**

- thinking を無効化できない: `thinking: {"type": "disabled"}` と `{"type": "enabled", "budget_tokens": N}` はいずれも 400 を返す。フィールドを省くか `{"type": "adaptive"}` を送り、深さは effort で制御する
- 強制ツール利用が使えない: `tool_choice` の `any` と `tool` が 400 を返す（token counting エンドポイントでも同じ）。`auto` ＋ strict tool use か structured outputs へ移す
- thinking ブロックがモデルと会話に紐づく: Opus / Sonnet / Haiku 系のブロックは読むが Fable 系・Mythos 系は読まない。2026-08-31 00:00 UTC 以降に作成されたアカウントでは、system・tools・先行メッセージの変更後に再送すると既定で 400 になる
- computer use: Claude API と Google Cloud では `computer_toolset_20260801` のみ受け付け、旧 `computer_20251124` は 400。Amazon Bedrock では旧ツールが引き続き動く

⚠️ あわせて既定の effort が `high` から `medium` へ下がり、同じ effort 設定でも Opus 5 よりターンあたりの thinking が増える（特に `xhigh` と `max`）。設定を持ち越さず sweep を引き直し、`max_tokens` に余裕を取る必要がある。ツール呼び出しの合間のテキストが `text` ブロックではなく progress-update の `thinking` ブロックで返るため、既定の `display: "omitted"` ではエラーなく無言になる点も挙動が変わる。

⚠️ `support.claude.com` の Release Notes は「Fable 5.1 の水準の仕事を 40% 安く」とだけ書き、消費者向けアプリでどのプランに出るかを示していない。

- https://www.anthropic.com/news/claude-opus-5-5
- https://platform.claude.com/docs/en/release-notes/api
- https://claude.com/blog/what-a-task-costs-on-opus-5-5
- https://github.blog/changelog/2026-09-22-claude-opus-5-5-is-now-available-in-github-copilot/

### 2. [料金+新機能] OpenAI が GPT-6 Sol と Luna を 5.6 系の半額で出した — 29日続いた料金据え置きが終わった

**要点**: OpenAI が GPT-6 Sol（$2/$10）と Luna（$0.1/$0.5）を API・Codex・ChatGPT Work へ投入し、5.6 系から単価を半減させた。29日続いた料金据え置きが終わり、5.6 系で引いた見積もりは当日で過大になる。

**詳細**: `gpt-6-sol` は「複雑なコーディングとエージェント的ワークフロー向け」で入力 $2 / 出力 $10（272K 入力までの標準価格でキャッシュ入力 $0.20、長文コンテキストは $4 / $0.40 / $15）、知識カットオフ 2026-04-20。`gpt-6-luna` は「集中した大量処理向けの最も効率的なモデル」で入力 $0.1 / 出力 $0.5（キャッシュ $0.01、長文は $0.20 / $0.02 / $0.75）、知識カットオフ 2026-05-18。いずれもコンテキスト 1.05M・最大出力 128K で、Responses API と Chat Completions API がテキストと画像の入力を受け付ける。OpenAI は「GPT-6 Astra の成果をより速く安価なモデルへ持ち込んだもの」と説明し、値下げの理由をキャッシュと推論の改善としている。

- ChatGPT 側の提供範囲: Plus / Pro / Business / Enterprise / Edu が当日から利用できる。Free と Go はデスクトップアプリで **Luna のみ**試せる
- ⚠️ ChatGPT 本体の Chat では使えない。提供面は **Work と Codex に限られる**と changelog が明記している
- Enterprise では管理者がワークスペースごとに有効化する。Codex CLI では `codex --model gpt-6-sol` / `codex --model gpt-6-luna` で指定する
- GitHub Copilot にも同日入った。Sol は Pro+ / Max / Business / Enterprise、**Luna は Pro を含む全 SKU** が対象で、SKU の範囲は Opus 5.5 と揃っていない
- Plus / Pro / Business のアカウントに「banked reset」が追加されたとフォーラム告知が述べている

⚠️ **Sol / Luna の名称は 5.6 系と重複する。** 既存の設定やコスト表で世代を取り違えると単価が2倍ずれる。

⚠️ 退役告知は出ていない。`developers.openai.com/api/docs/deprecations` の最上位は 9/11 の `gpt-5.4-cyber`（削除 10/1・移行先 `gpt-5.6-cyber`）のままで、GPT-5.6 系の API 側の期限は本日時点で示されていない。GPT-5.5 の 10/14 退役（ChatGPT / ChatGPT Work / Codex・API は対象外）は据え置きである。

- https://developers.openai.com/api/docs/changelog
- https://developers.openai.com/api/docs/pricing
- https://learn.chatgpt.com/docs/changelog
- https://github.blog/changelog/2026-09-22-openais-gpt-6-sol-and-gpt-6-luna-now-available/

### 3. [破壊的変更] Claude Code 2.1.280 が symlink の書き込みを着地先で判定するようになった — auto モードの許可範囲が今日から変わる

**要点**: Claude Code `2.1.280` が、書き込み許可の判定を見かけのパスから着地先へ移した。ツリー外へ着地する symlink 経由の書き込みは auto モードも承認しなくなり、既定モデルも Pro / Team Standard で Opus へ変わる。

**詳細**: 権限まわりの修正が3件入った。① symlink を経由する書き込みがツリー内の見かけのパスで判定されていたため、実際にはツリー外へ着地する書き込みを自動承認できていた。承認プロンプトは着地先を表示し、これらの経路では承認されない。② セーフティチェックが審査を拒んだ操作を auto モードが無限に再試行していた問題を、1回で拒否し「再試行しても無意味」と示す形に変えた。③ セーフティチェックが無回答だったときの再試行にバックオフを入れ、10連続でターンを止めるようにした。

- キーバインド: ダイアログ中の `n` が閉じる・`y` が確定する動作を廃し、Enter と Esc に統一した。従来の挙動は `keybindings.json` で `confirm:yes` / `confirm:no` に割り当てて戻す
- 差し戻し: `ctrl+l` / `cmd+k` のフルスクリーンでのトランスクリプト消去（2.1.260 で追加）は撤回され、画面の再描画に戻った
- MCP: `CLAUDE_CODE_MAX_MCP_DESCRIPTION_LENGTH` でツール説明とサーバー指示の 2,048 文字上限を変更できる
- フック: `PermissionRequest` フックでの agent 型フックは拒否されるようになった（許可・拒否の判断に使えないため。command / http フックへ誘導される）
- プラグイン: GitHub リポジトリ／git URL からプラグインを更新した後も `installed_plugins.json` がインストール時のコミットを保持し続ける問題が修正された。9/18 の `2.1.277` のピン留め記録の修正と同系統だが、いずれも security 扱いの記載はない
- Enterprise: Claude Code on the web の Routines のオン／オフ設定が Admin settings → Capabilities → Remote sessions 配下へ移った

⚠️ **npm の `stable` は `2.1.267` のまま14日連続で据え置かれている。** 未到達は `2.1.268`〜`2.1.280` の13版ぶんで前日の11版から増えた。stable 固定の組織には Opus 5.5 の既定化も上記の権限修正も届いていない。

- https://code.claude.com/docs/en/changelog
- https://registry.npmjs.org/@anthropic-ai/claude-code

## カテゴリ別まとめ

### Claude / Anthropic

- [料金+破壊的変更] **Opus 5.5 の公開**（ハイライト1参照）。`2.1.280` の権限変更はハイライト3を参照
- [版更新] **publish 間隔**: Claude Code `2.1.280` は 9/22 15:44:39 UTC に publish され、`2.1.278`（9/19 01:48:59 UTC）から3日ぶりだった。UTC 09-20・09-21 は publish 0件である。`dist-tags` は `{stable: 2.1.267, latest: 2.1.280, next: 2.1.280}` だった
- [新機能] **メッセージ内ツール定義の beta**: 開発者が、`inline-tools-2026-09-15` ヘッダーを付けると会話途中の system メッセージの `tool_addition` ブロックでツールの完全な定義を運べるようになった。`tools` を編集せずに追加・スキーマ変更・サーバーツールの版上げができ、プロンプトキャッシュを壊さない。`mcp-client-2026-09-15` を併用すると定義に MCP toolset を置け、応答の `mcp_tool_listing` ブロックがサーバーごとの取得済みツール一覧を記録する
- [動向] **1タスクの費用の分解**: `claude.com/blog` に 9/22 の `What a task costs on Opus 5.5` が出て、入出力2割・キャッシュ読み取り6割の値下げを前提に費用の決まり方を整理している
  - ターン数: 40ターンから25ターンに減ると入力処理が 2.8M から 1.75M トークンへ落ち、費用は約4割減る
  - キャッシュヒット率: 2.8M 入力（うち9割キャッシュ）・出力 60K のセッションで入力側は約 $1.62、キャッシュ無しなら $11.20 になる
  - effort の使い分け: low は rename のような機械作業、medium が通常の既定、high は複雑なデバッグで thinking 約 20K トークン（約 $0.40）を上乗せする。「モデルを変える前に effort を上げる」を推奨し、再試行1回を防げれば $0.40 は回収できるとする。high effort で同じ問題に2回当たってから Fable 5.1（$10/$50）へ移るのが切替の目安である
  - https://claude.com/blog/what-a-task-costs-on-opus-5-5
- [据え置き] **退役ページの中身**: 暫定退役日は全14件で、`claude-opus-5-5` の追加以外に変化はない。直近は `claude-sonnet-4-5-20250929` の 9/29、`claude-haiku-4-5-20251001` の 10/15、`claude-opus-4-5-20251101` の 11/24 で、⚠️ いずれも「Not sooner than」の下限であり確定した停止日ではない。Anthropic は公開モデルの退役に最低60日前の通知を約束しており、確定日はその通知で現れる。表外の Note で `claude-mythos-preview` が Deprecated（退役日 To be announced・移行先 `claude-mythos-5`）のまま残る
  - https://platform.claude.com/docs/en/about-claude/model-deprecations
- [動向] **研究側の新規1件**: `anthropic.com/research` の一覧が10件から12件に増え、9/17 の `Scenarios for our Economic Future`（`/institute/econ-scenarios`）を本日はじめて検出した。出来事は6日前だが3ソースいずれにも掲載歴がない
- [据え置き] **alignment 側は沈黙が続く**: `alignment.anthropic.com` は10日目も本文取得に成功したが9月の新規投稿は0件で、最上位は8月の "Training a Misaligned Reward Seeker" のままである
- [据え置き] 既報: 9/18 Accenture 組込み評価（両社が今後5年でそれぞれ最低10億ドルを投じる見込み）、9/17 生体分子モデリング高速化（1標的 $10,000 → 約 $150・Adaptyv Bio コンペ 9/28〜10/31）、9/16 Cowork と chat の統合、9/15 Salesforce in Claude（37スキル）

### OpenAI / Codex / ChatGPT

- [料金+新機能] **GPT-6 Sol / Luna の公開**（ハイライト2参照）。`developers.openai.com/api/docs/changelog` は 9/15 から7日ぶりに動き、`learn.chatgpt.com` は 9/18 から4日ぶりに動いた
- [版更新] **Codex の安定版が4日ぶりに動いた**: 安定版が `rust-v0.156.0`（9/22）へ上がり、`rust-v0.155.1`（9/18 20:03 UTC）から止まっていた状態が解消した。`0.156.0` 系は `alpha.18`（9/22）まで刻まれてから安定版が出ている
  - ⚠️ 同日に `0.157.0` 系の pre-release が `alpha.3` から `alpha.9` まで7本出た（前日の `alpha.1` から24時間で8本）。開発の山は releases ページの上位だけでは追えない
  - ⚠️ `github.com/openai/codex` の個別タグ本文は本日も取得できなかった（releases ページ上でリリース本文の読み込みエラーが継続）
- [観測] **料金ページの抽出が本日は全節そろった**: 09-20・09-22 に落ちていたレガシー節（`gpt-5.2` / `gpt-5.1` / GPT-4 系・o 系・3.5 系）とファインチューニング全10行が復帰した。据え置き分は GPT-6 Astra $10/$50（キャッシュ $1.00）、GPT-5.6 Sol $4/$20、Terra $2/$12、Luna $0.20/$1.20、`gpt-5.6-cyber` / `gpt-5.5-cyber` 各 $12.50/$75、`gpt-5.3-codex` $1.75/$14、`gpt-rosalind-research` $5/$25、`chat-latest` $5/$30、`gpt-5-search-api` $1.25/$10 である。Batch・Flex は標準の50%、Fast mode は2倍。⚠️ `gpt-5.4-cyber` の行は 09-14 の消滅から不掲載が続く（停止まで8日）
- [観測] **廃止ページの件数が日ごとに揺れる**: 本日の抽出は Upcoming 10件（対象27モデル）・Past 28件で、前日の Upcoming 15件から減った。告知の内容に撤回・延期・新規追加はない。⚠️ 告知単位の数え方が日ごとに揺れるため、件数の一致は差分判定の根拠にしない
- [動向] **公式フォーラムが12日ぶりに動いた**: `community.openai.com` の Announcements RSS が 9/22 18:16 UTC に更新された。GPT-6 Sol / Luna の告知で、benchmark のチャートは載るが数値は本文に書かれていない
- [据え置き] **事案レポートは12日間動きなし**: `alignment.openai.com/misalignment-reports/` は事案レポート6件・notices 3件で据え置きである。notices は 9/11 RubyGems / 9/5 DSEwiki / 8/26 Hugging Face
- [観測] ⚠️ `openai.com` / `help.openai.com` のオリジン403は継続しており、本日も一次には到達できていない
- [据え置き] 既報: Sponsored Agents の限定アルファ（9/16・Free と Go にのみ広告表示）、Astra for Law（9/17）、GPT-6 Astra GA（9/3）、OpenAI DevDay 本体 9/29（Fort Mason・基調講演は無料ライブ配信）

### GitHub Copilot

- [新機能] **1日で3モデルが追加された**: GitHub が 9/22 付で Claude Opus 5.5・GPT-6 Sol・GPT-6 Luna の提供を告知した（ハイライト1・2参照）。課金はいずれも provider list pricing の従量課金で、プレミアムリクエスト倍率の記載はない
  - SKU の範囲は3モデルで揃っていない。Opus 5.5 と GPT-6 Sol は Pro+ 以上、GPT-6 Luna のみ Pro を含む
  - 新モデルは既定で有効になり、Business / Enterprise の管理者が全体の既定を切るか個別に無効化しない限り選択できる。ロールアウトは段階的である
  - Opus 5.5 の対応サーフェスは10面（VS Code / Visual Studio / Copilot CLI / コーディングエージェント / Copilot アプリ / github.com / モバイル / JetBrains / Xcode / Eclipse）で、初期検証では Opus 5 と同等の解決率をより少ないステップとトークンで達成したとされる。⚠️ 既定モデルの置き換えかどうかは書かれていない
- [廃止] **Copilot ラベル以外にも退役告知が2件出た**: 9/21 はプルリクエスト一覧ページ刷新の GA と GitHub Enterprise の資格情報インベントリのエクスポート追加、9/22 はモデル追加3件に加えて SSH のセキュリティ改善（旧方式の退役告知）と全プラットフォーム版 CodeQL バンドルの廃止告知が出ている
- [据え置き] **CLI の安定版は据え置きで pre-release が2本**: 安定版は `v1.0.87`（9/21 15:31 UTC）のままである
  - `v1.0.88-2`（9/22 14:33 UTC）: 下端に固定されるダイアログでテキスト選択が効くようになった（ログインのデバイスコードを含む）
  - `v1.0.88-1`（9/22 00:31 UTC）: managed-settings の更新失敗時に `/allow-all` を保持し、存在しないパスへのセッション承認を正確に記憶する。サンドボックスのネットワーク拒否がプロキシトンネル失敗由来のとき回避方法を表示する
- [セキュリティ] **Plugin4Shell は開示6日目でも CVE 未採番**: 4社とも security advisory は未公開で、実攻撃の記録も出ていない。Microsoft は GitHub Copilot の修正を依然として出しておらず、Copilot CLI のリリースノートにプラグイン関連の修正は記載がない。Anthropic の Claude Code `2.1.179`、OpenAI の Codex `0.146.0` で修正済み、Google は Gemini CLI を retire 済みとして修正しないという構図も不変である。⚠️ 一次の `www.air.security` は本日もゲートウェイ拒否で、追跡経路が二次のみの状態が続く
- [動向] 期限: 9/28 にチャット3面統合・code review の既定 effort が Lite → Balanced・チャットのデータ保持がアカウント存続期間へ、10/1 に既存顧客の前払い必須、10/2 に4モデル廃止、10/19 に5モデル廃止、12/31 に Fable 5.1 / Fable 5 の ZDR 暫定免除終了が並ぶ

### Copilot Studio / Power Platform

- [破壊的変更] **標準ハーネスの入門が「新エクスペリエンスをオフにする」から始まる形に書き換わった**: `microsoft-copilot-studio/fundamentals-get-started`（`ms.date` 2026-09-22・`updated_at` 2026-09-22T19:03Z）が本日改訂され、見出しが「Quickstart: Create and deploy an agent with the standard harness」になった。手順2が New experience トグルをオフにし Submit を選んでフィードバックパネルを閉じる操作で、研修や手順書が前提にしてきた「サインインしたら標準ハーネスの画面」は一次の上で成立しなくなる
  - `harnesses-overview`: 「Choose a harness」から Harnesses in Copilot Studio へ改題された。ハーネスを「設計したエージェントと推論を担うモデルのあいだに立つランタイム」と定義し、いつモデルを呼ぶか・何を送るか・返ってきたものをどう解釈しツールを呼ぶかを決める層だと説明する
  - `agents-experience/overview`: 「Agents powered by the GitHub Copilot Harness overview」として自然言語でエージェントを記述する方式に (preview) が付いた。標準ハーネスとの相互移行は不可で、GitHub Copilot ハーネスではオーケストレーション挙動を設定できず、構築・テスト・評価のいずれも Copilot Credits を消費する
  - 3ハーネスの位置づけ（GitHub Copilot ハーネス＝複数ステップの業務処理、標準ハーネス＝ルールベースのエージェントとエージェントフロー、Copilot チャットハーネス＝M365 Copilot Chat の拡張）と課金の記述は 8/5 掲載時から不変である。標準ハーネスへ戻る経路はトグルのオフ以外に2つある（`switch-experiences` の「Other ways to build」からの作成と、Agents / Workflows 一覧から開く方法）
  - ⚠️ この3本の改訂は Copilot Studio What's New（July 2026 節が最新）にも Release Notes（August 25 バッチ）にも現れていない
  - https://learn.microsoft.com/en-us/microsoft-copilot-studio/harnesses-overview
- [据え置き] **統制ブログに新機能の告知はない**: 製品チームが、エージェント統制を「観測し続ける → 度合いに応じて対応する → 適切なところは自動化する」の3段で運用モデル化する考え方を示した（Tech Community・9/22・本 board では1週間ぶりの新規）。⚠️ 主眼は10月の PPCC 2026 セッション告知で、製品面の言及は Agent 365 を横断管理レイヤーとして使うことと Agents Map による可視化の2点にとどまる
  - https://techcommunity.microsoft.com/t5/copilot-studio-blog/governance-is-becoming-agentic-too-how-enterprises-can-operate/ba-p/4556820
- [据え置き] **What's New は8月節・9月節とも未作成**: 掲載は July 2026 節が最新のままである（`ms.date` 2026-08-18・`updated_at` 2026-09-17T19:04Z で6日連続据え置き）。⚠️ 8/3 に GA した GitHub Copilot ハーネスは June 節で `(Production-ready preview)` と書かれたままで、GA から51日連続の未反映になる
- [据え置き] **モデル表とガイダンスハブは据え置き**: 標準ハーネスの `authoring-select-agent-model` は Default が全13リージョンで GPT-5.5 Chat のままである。ガイダンスハブは169ページを全件取得して `ms.date` を突合し、動いたページはゼロだった
- [据え置き] **Released Versions が84日動いていない**: Copilot Studio Build は 2026.6.3 のままで、`released-versions/copilotstudio` の `updated_at` は 2026-07-01T15:55Z から動かない。「毎週火曜更新」と書かれた定例日（UTC 9/22）にも新ビルドは出ていない
- [据え置き] **月次記事が親ページの一覧に出ない**: 9/17 公開の「What's new in Power Platform: September 2026 feature update」は、公開から6日たっても親ページの一覧に現れない。親ページの先頭は 9/3 の PPCC 記事のままで、子カテゴリ（Power Automate / Power Apps）では正しく先頭に並ぶ
- [据え置き] **Release Wave と非推奨一覧は据え置き**: `planned-features` 側5ページは `updated_at` 2026-09-03T14:35Z、非推奨一覧も `updated_at` 2026-09-04T19:03Z・見出し94本のままで、新規の非推奨項目はゼロだった

### Microsoft（その他）

- [予定] **M365 Copilot の推論を国内で実行する計画が起票された**: Roadmap 571886（Microsoft Copilot (Microsoft 365): Local inferencing）が 9/21 23:04Z のバッチで起票され、3ソースいずれにも掲載歴がなかった。対応する Copilot のやり取りについて推論そのものを該当地域内で実行する機能で、前提が「データの保存先を国内に寄せる」から「推論の実行場所まで問える」へ動く
  - 提供開始地域: オーストラリア / インド / アラブ首長国連邦 / 英国 / 米国の5か国
  - 状態: `In development`・GA 期日 December CY2026（Preview 期日の記載なし）
  - 対象範囲: 「supported Copilot interactions」とあり、どのやり取りが対象かは一次に内訳がない
  - 既存の枠組みとの関係: これまでの Advanced Data Residency / Multi-Geo は保存時（at rest）のコミットメントで、推論の実行場所は対象外だった
  - ⚠️ 9/21 に掲載した SpaceXAI サブプロセッサは「在国内処理（in-country processing）のコミットメントから除外される」と明記されている。モデルごとに在地推論の可否が割れるため、地域要件のあるテナントではモデル可用性の表とは別軸で在地推論の対象かを確認する必要が出る
  - https://www.microsoft.com/microsoft-365/roadmap?id=571886
- [仕様] **情報バリアを有効にしたテナントでは Cowork プラグインを配布できない**: `cowork/cowork-plugin-development` の `ms.date` が 2026-09-17 → 2026-09-21 へ動き、Microsoft Purview 情報バリア（IB）が plugin / skill の管理・共有に未対応であることが明記された。IB が有効なテナントでは埋め込みナレッジのファイルアップロードがテナントレベルでブロックされ、該当するプラグインとスキルを公開できない。⚠️ 9/19 時点の本文にあったのか 9/21 の改訂で入ったのかは一次から確定できない
  - ISV コンテンツの非索引化: Microsoft は ISV コンテンツを含む永続的な索引・ナレッジグラフ（Microsoft Graph を含む）・データベースを作成・維持せず、リアルタイム応答のための一時処理もセッションを超えて保持しない。ISV が書面で要求した場合は10営業日以内に削除し書面で証明する
  - MCP 注釈による確認要求: `readOnlyHint` が `false` か `destructiveHint` が `true` のツールは実行前にユーザー確認が入る。⚠️ 注釈の無いツールは破壊的として扱われるため、全ツールに安全性注釈を付ける必要がある
  - https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-plugin-development
- [動向] **Roadmap が5日ぶりに動いた**: Release Communications RSS の `lastBuildDate` が 2026-09-18T22:00:04Z → 2026-09-21T23:04:49Z へ動き、7件が起票された。内訳は Copilot 在地推論（571886）、Teams 会議への粒度の細かい条件付きアクセス（571879・GA November CY2026）、Viva Insights のリーダー向け Power BI レポート公開（570446・GA October CY2026）、Dynamics 365 Customer Service の品質評価4件である
  - ⚠️ 総項目数は 1,773 で前日の 1,768 から5件増だった。新規バッチが7件なのに増分が5件で一致せず、総項目数の増減では新規の有無を判定できない
  - Copilot Studio の起票は22件で増減なく全件 `In development` である。GA 期日 September CY2026 は14件で残り7日になった。期日超過は 566997（August CY2026・23日）と 562221（June CY2026・3か月半）である
- [動向] **Partner Center が2件増えて16件になった**: パートナーが、9/30 から Dragon Copilot の医療向け導入実績を示す Clinical Applications スペシャライゼーションを取得できるようになる（co-sell・紹介の対象資格、資金提供機会、Azure バルククレジット、GTM 資材が開く）。対象は医療分野の実績または Dragon Copilot に関心のある CSP 各層とソフトウェア開発企業である
  - Microsoft Ignite のセッションカタログが公開された（会期 11/17〜20・現地とオンラインの併催）。本サマリーで Ignite に触れるのは初めてで、11月の節目として追跡対象に加える
  - 直近の期限は Check Inventory API の退役 9/25（2日後）で、代替 API は `resourceType` を必須にする一方レスポンス契約は変えない
  - https://learn.microsoft.com/en-us/partner-center/announcements/2026-september
- [据え置き] **Release Notes は9月分が1回も出ていない**: 本文の先頭見出しは August 25, 2026・H2 は83本・`updated_at` 2026-09-03T19:39Z で据え置きである。隔週の期日 9/8（UTC）から15日、前バッチからは29日になる。差分判定はメタデータではなく本文の最終収録日で行っている
- [動向] **Cowork ドキュメントの一括再ビルド**: `cowork/` 配下9ページが 9/21 22:35Z に同一コミットで再ビルドされ、`ms.date` が 9/21 へ動いたのは `cowork-faq` と `cowork-plugin-development` の2本だった。Cowork What's New の September 2026 節の New features 4件に増減はない
- [据え置き] **統制面の据え置き3件**: Purview の `whats-new` は September 2026 節が Entra Global Secure Access 連携の1件のままで、571306（レガシー Teams リテンションの Teams 専用化）の記載がない。`manage-public-web-access` は 9/9 に復活した Domain Exclusion（上限1,000ドメイン・既定無効）を本文に入れていない。Agent 365 board RSS は全13エントリに増減なく、最新が 8/6 公開の「What's new in Agent 365 – July 2026」で48日間新規がない
- [動向] **Copilot Tuning の停止が文書に反映されない**: 停止発効（8/20）から34日たっても `copilot-tuning-overview` は停止も退役も書いておらず、「Access through Frontier is planned for April 2026」という既に過ぎた予定を現在形で残している
- [据え置き] **組織プロンプトに続報なし**: 9/22 に掲載した `organizational-prompts`（テナント上限1,000件・採用率の 7/14/28日表示）は `ms.date` 2026-09-21 で据え置きである。⚠️ Roadmap 569425（委任公開・GA 期日 September CY2026）の記述は本日も本文に無く、期日まで残り7日になった

### Google

- [破壊的変更] **Gemini 2.5 系へのアクセスが既存利用者に限定された**: Google が、過去に実際に使った利用者に限って Gemini 2.5 系の API アクセスを続ける方針を Gemini API changelog の 9/18 付エントリで示した。新規の利用者は API から呼べず、既存利用者には「追って通知があるまで」提供が続く。新規プロジェクトの移行先は 3.5 Flash-Lite または 3.8 Flash と案内されている
  - ⚠️ モデル ID は明示されていない。「2.5 models」とだけ書かれており、対象の粒度は一次から確定できない
  - ⚠️ 前日の記録では 9/17 の `antigravity-preview-09-2026`（組み込みツール引数の PascalCase 化・ファイル編集の行範囲置換化という破壊的変更を含む）を最上位としていた。同じページの上位に1日後のエントリが後から現れた形である
- [観測] **廃止ページの抽出が復帰した**: 68モデルを列挙し、09-22 の抽出に現れなかった `gemini-omni-flash-preview` の 9/30 停止（代替 `gemini-omni-1.1-flash`）が本日は列挙に戻った。`antigravity-preview-05-2026` の 10/5 停止、`gemini-2.5-flash-image` の 10/2 停止も再確認している。⚠️ 2日続けて抽出内容が入れ替わっており、一度記録した期限を台帳側で保持する運用が実際に効いた形になった
- [動向] **Workspace 側の AI 連携は1本**: Workday for Google Sheets が 9/21 から利用できるようになった。Workday Adaptive Planning を Google Sheets / Slides に接続し、自然言語の要約・異常検知・可視化・アドホックレポートを Sheets 内で行える。Workspace 全エディションと Workspace Individual、個人アカウントが対象で、Workday Adaptive Planning のライセンスが要る。Rapid / Scheduled の両リリース系統が対象だが、Workday 側と Workspace 側の両方で管理者の有効化が必要である
  - 同日の「Google Sheets の手動計算設定」は AI 連携ではないため対象外とした
- [据え置き] **HF の `google` org に動きなし**: `gnm-v3`（作成 9/1 / 更新 9/2）が最新のままで新規作成も更新もない。`blog.google` は 301（ゲートウェイ通過）で、⚠️ 応答に日付が出ないため差分判定には使えない
- [据え置き] 既報: 9/16 Gemini in Workspace の外部コネクター7件（MCP 経由・既定 ON）、`gemini-3.8-flash` は入力 $0.75 / 出力 $3.75 が 2026-12-31 まで、Gemini 3.5 Pro GA は未ローンチ継続

### Cursor / xAI / Devin

- [料金] **Grok 4.7 の API 仕様が二次で埋まったが、2ソースで単価が割れている**: 一次3ホスト（`x.ai` / `docs.x.ai` / `grok.com`）はゲートウェイ拒否が続き、公開翌日の WebSearch で仕様相当が返るようになった。⚠️ **本項は二次のみで確定として扱わない**
  - Master 側の記録: 200K 入力未満で $2.20 / $0.55 / $6.60（入力 / キャッシュ入力 / 出力・100万トークンあたり）、超過で $4.40 / $1.10 / $13.20、コンテキスト長 500,000 トークン
  - industry 側の記録: グローバルエンドポイントで $2 / $6（キャッシュ入力 $0.55）、200K 超で $4.40 / $13.20、Fast 版は出力2倍速で $4 / $12、US リージョンエンドポイントはグローバル比1.1倍
  - 差は US リージョンの1.1倍係数を掛けた値かどうかで説明が付く（$2×1.1＝$2.20・$6×1.1＝$6.60）。⚠️ どちらの記録がどのエンドポイントを指すかは二次からは確定できない
  - `Grok 4.7 Fast` は Cursor と Grok Build 限定で公開 API には無いと Master 側が記録する一方、industry 側は $4/$12 の表示単価を記録しており、提供範囲の記述も揃っていない
  - ⚠️ 公開当日は同じ検索が「未リリース」を返していた。インデックスが1日遅れで追いついた形である
- [据え置き] **Cursor は2日連続で新規なし**: changelog は 9/10 の Projects が最上位のまま13日間（RSS 200）、フォーラム Announcements も 9/21 の2本が最上位のままである
- [動向] ⚠️ **Cursor は Opus 5.5 の提供開始を告知していない。** Grok 4.7 は公開当日に告知しており、同じ経路が Anthropic のモデルには働いていない。GPT-6 Astra（9/3 GA）の告知も20日目まで出ておらず、11/12 の OpenAI による供給停止予定と併せて読む必要がある
- [観測] **Devin は一次・代替一次のいずれからも読めない**: `docs.devin.ai` / `cli.devin.ai` ともゲートウェイ拒否が継続する
- [据え置き] 既報: OpenAI → Cursor のモデル供給停止（遮断予定 11/12・一次未読）、SpaceX による Cursor 買収完了（8/14・$60B）

### MCP / オープンウェイト

- [据え置き] **MCP 仕様側は32日間止まっている**: `blog.modelcontextprotocol.io`（RSS `index.xml`）は 200 だが、8/22 の「The New MCP Roadmap」が最上位のままである。その前は 7/28 の 2026-07-28 仕様、7/27 の Ruby SDK 1.0 である
  - ⚠️ 仕様が止まる一方で実装側は運用設定を増やし続けている。Claude Code `2.1.280` は MCP ツール説明の 2,048 文字上限を環境変数で変更できるようにし、Claude API は `mcp-client-2026-09-15` で MCP toolset をメッセージ内定義に載せられるようにした
  - WebMCP Challenge の受賞発表は本日 9/23 で賞金総額 $35,000 である。結果は未確認である
- [据え置き] **8 org のいずれにも 9/22 の作成・更新はゼロ**: `Qwen` / `moonshotai` / `deepseek-ai` / `meta-models` / `mistralai` / `zai-org` / `openai` / `google` を `createdAt` 降順と `lastModified` 降順の両方で確認した。各 org の最新作成は `Qwen-Image-2.1-PE-I2I` 9/20 ／ `DeepSeek-V4.1-Flash` 9/10 ／ `gnm-v3` 9/1 ／ `GLM-5.3-Flash-BF16` 8/25 ／ `Muse-Glimmer-30B-ExecuTorch-PTE` 8/10 ／ `Shieldstral-1.0-3B` 7/16 ／ `Kimi-K3` 6/13 ／ `privacy-filter` 4/17 である
  - ⚠️ Qwen を除く7 org のテキスト系モデルは 9/11 以降12日間、新規作成も更新も1件もない。前々日に記録した `meta-models/utils`（作成 9/17）は `limit=8` でも現れず、公開一覧から外れたとみられる
- [観測] **HF の `downloads` 実測値**（2026-09-22 19:10 UTC 取得・増減の解釈はしない）: `Qwen3.8-27B-FP8` 6,473,584 ／ `Qwen3.8-Flash-Next` 787,525 ／ `moonshotai/Kimi-K3` 1,900,376 ／ `deepseek-ai/DeepSeek-V4.1-Flash` 542,014 ／ `zai-org/GLM-5.3-Flash` 3,547,021 ／ `meta-models/Muse-Glimmer-30B-GGUF` 496,331 ／ `openai/gpt-oss-20b` 6,714,095 ／ `google/timesfm-3.0-pytorch` 1,151,294
- [観測] A2A（Agent2Agent）の AAIF 参加は未確定のままで、一次3ホストはゲートウェイ拒否が継続する

### Apple / 市場データ / 企業構造

- [据え置き] **Apple の AI 関連は3ヶ月以上動いていない**: `developer.apple.com/news/` の最上位は 9/18 の iPhone Duo 向け開発リソースで AI 関連の記載がなく、AI 関連の独立エントリは 6/11 の ImageCreator クラス廃止告知のままである。⚠️「新しい Siri は Google Gemini で動く」「SiriKit 退役・App Intents 2.0 の内訳」は引き続き二次のみで確定として扱わない。既報の期日は iPhone Duo 10/23 発売（iOS 27.1）、EU 向けビジネス条件の 10/1 発効、最小 SDK 要件の 2027年4月引き上げである
- [料金] **2社が同じ日に値下げを一次メッセージにした**: Opus 5.5 は Opus 5 比で入出力2割・キャッシュ読み取り6割の値下げ、GPT-6 Sol / Luna は 5.6 系比で5割の値下げである。性能の比較ではなく単価が発表の主題になっている
  - Anthropic は Opus 5.5 の発表で GPT-5.6 Sol を名指しで比較し、「Terminal-Bench 4.0 では Astra に匹敵する結果を約4割のコストで出し、CursorBench では GPT-5.6 Sol を11ポイント上回って約3分の1のコストで済む」としている。⚠️ GPT-6 Sol は同日の公開なので比較対象に入っていない
- [動向] **上場観測と Opus 5.5 公開が同じ文脈で語られている**: 09-22 に記録した後ろ倒し（調達最大 $1,000億・評価額 約 $2兆）について、理由として挙げられていた「GPT-6 Astra に対抗する新モデルの投入」が本日の公開で具体化した形になる。年換算売上は7月末 $650億超で、投資家筋は2026年末に $1,100億超と見込む。May 2026 の Series H-1 は評価額 約 $9,650億である。⚠️ 上場の時期・価格・評価額はいずれも一次未確認で、Anthropic の一次告知は 2026-06-01 の Form S-1 機密提出に留まる。本日のニュース面にも上場への言及はない
- [据え置き] **市場データ4ソースは新規公表なし**: Similarweb・IDC・MM総研・NRC のいずれも引用可能な値が 09-20 から動いていない。Similarweb 8月分（ChatGPT 55.5%・Gemini 25.6%・Claude 9.3%）、IDC 国内 AI 支出（2029年 6兆8,897億円・CAGR 36.0%）、Gartner 世界 AI 支出（2026年 $2.59兆・+47%）、MM総研 国内生成AI個人利用率 21.8% はいずれも据え置きで、Similarweb 9月分の公表は未検知である
- [観測] 既報（一次未読含む）: Google による Claude Opus 5 の全エンジニア開放（9/15・一次の追認なし）、Anthropic のコンピュート契約 $517B・14.8GW（⚠️ 確定支出ではなく11ヶ月で結んだ契約の上限枠）、Microsoft AI の MAI モデル行動規範草案（9/14・協議は10/26頃まで）

## 直近の注目予定

- **9/23（本日）**: WebMCP Challenge の受賞発表
- **9/24**: OpenAI の Videos API と `sora-2` 系5件が退役
- **9/25**: Microsoft Partner Center の Check Inventory API が退役
- **9/28**: Copilot のチャット3面統合 ／ code review の既定 effort が Lite → Balanced ／ チャットのデータ保持がアカウント存続期間へ ／ OpenAI の `gpt-3.5-turbo-instruct` / `babbage-002` / `davinci-002` / `gpt-3.5-turbo-1106` が停止 ／ Anthropic × Adaptyv のタンパク質設計コンペ開始（〜10/31）
- **9/29**: OpenAI DevDay 本体（サンフランシスコ Fort Mason・基調講演は無料ライブ配信）
- **9/29 以降**: `claude-sonnet-4-5-20250929` の暫定退役日（確定日ではない）
- **9/30**: Gemini の `gemini-omni-flash-preview` が停止 ／ OpenAI の現行 OneGov 契約（$1/年）が失効 ／ Copilot Studio の Roadmap 14件が GA 期日（組織プロンプトの委任公開 569425 も同期日） ／ Clinical Applications スペシャライゼーションの受付開始 ／ M365 E7 プロモ最終日 ／ E5・E3 の CSP 割引終了 ／ 2026 Wave 1 の対象期間終了
- **9 月末**: Claude for Financial Advisors の一度限りの利用クレジットの期限
- **9 月**: macOS 27 GA ／ Claude Projects 再設計が Pro / Max の Claude Code 利用者全体へ拡大
- **10/1**: OpenAI の `gpt-5.4-cyber` が API から削除 ／ OneGov トークン課金50%割引が開始 ／ Copilot Business・Enterprise の既存顧客が前払い必須に ／ Microsoft CSP ソフトウェア価格改定が発効 ／ Microsoft 365 G7 の GA ／ ChatGPT for Word の Word アクセスが既定オンへ ／ Apple の EU 向け新ビジネス条件が発効
- **10/2**: GitHub Copilot が Gemini 3.5 Flash / Gemini 3.6 Flash / Kimi K2.7 Code / Claude Opus 4.7 を全体験から廃止 ／ Gemini の `gemini-2.5-flash-image` が停止
- **10/5**: Gemini の `antigravity-preview-05-2026` が停止 ／ GPT-Rosalind の課金開始 ／ Anthropic 助成の full proposal 期限
- **10/13**: Office LTSC 2021・Project LTSC 2021・Visio LTSC 2021 のサポート終了
- **10/14**: OpenAI の `gpt-5.5` が ChatGPT / ChatGPT Work / Codex から退役（API は対象外）
- **10/15 以降**: `claude-haiku-4-5-20251001` の暫定退役日（確定日ではない）
- **10/16–11/11**: OpenAI DevDay Exchange 8都市（東京は 10/20）
- **10/19**: GitHub Copilot が Gemini 3.7 Flash / GPT-5.5 / GPT-5.4 / GPT-5.4 mini / Grok 4.5 を全体験から廃止（5モデル。移行先は 3.8 Flash / 5.6 Sol / 5.6 Sol / 5.6 Luna / Grok 4.6。⚠️ `GPT-5 mini` は対象外）
- **10/22 / 10/23**: Apple の Volume Purchasing 開始 ／ iPhone Duo 発売（iOS 27.1）
- **10/23**: OpenAI のレガシースナップショット12件が退役
- **10/26 頃**: Microsoft AI の MAI モデル行動規範の公開協議が終了
- **10/27〜29**: PPCC 2026
- **10/31**: OpenAI の既存 evals が読み取り専用に ／ Anthropic × Adaptyv コンペの最終週
- **10 月下旬まで**: METR による Anthropic のインシデント独立調査の初回8週間（9/9 起点）
- **10 月中**: レガシー Teams リテンションポリシーが Teams 専用へ変換（571306） ／ Cowork 向け Purview DLP の GA（570845） ／ Viva Insights のリーダー向けレポート公開（570446）
- **11/2**: GitHub Actions の `pull_request_target` 既定無効化が公開リポジトリで強制開始 ／ M365 Copilot Business の従量課金が既定オン（$10/ユーザー/月の枠つき）
- **11/12**: OpenAI が Cursor へのモデル供給を停止する予定日（一次未読）
- **11/15**: Microsoft Release Planner 退役
- **11/17〜20**: Microsoft Ignite（現地・オンライン併催）
- **11/21**: GPT-5.6 Sol の暫定値下げが有効とされる期限
- **11/24 以降**: `claude-opus-4-5-20251101` の暫定退役日（確定日ではない）
- **11 月中**: Copilot Cowork の政府クラウド GA（571637） ／ Teams 会議の粒度の細かい条件付きアクセス（571879）
- **11/30**: OpenAI の Reusable prompts・Evals プラットフォーム・Agent Builder が停止
- **12/1**: OpenAI の GPT Image 系が停止（→ `gpt-image-2`）
- **12/2**: EU AI Act の生成コンテンツ標識義務の猶予終了
- **12/11**: OpenAI の GPT-5 / o3 系スナップショットが停止
- **12/31**: Gemini 3.8 Flash と 3.7 Flash の導入価格が終了 ／ GitHub Copilot の Fable 5.1 / Fable 5 に対する ZDR 暫定免除が終了
- **12 月中**: M365 Copilot の在地推論 GA（571886・豪／印／UAE／英／米）
- **数週間内**: Claude Sonnet 5.5 と Claude Haiku 5.5 のリリース（Anthropic の Opus 5.5 発表で明言・日付未提示）
- **年内**: Anthropic の新データ保持方式 ／ Claude Docs / Claude Slides の Team・Free への展開 ／ Astra for Law の API 版 `gpt-6-astra-law` ／ ChatGPT Ads の Sponsored Agents の限定アルファ拡大 ／ Grok 4.7 と Opus 5.5 の Copilot ロールアウト完了（ともに段階展開・完了日未提示） ／ Microsoft AI の MAI モデル行動規範の改訂版公開予定
- **Q4 CY2026**: Graph PowerShell v3.0.0 リリース（Windows PowerShell 5.x のサポートなし）
- **2027-01-06 / 01-20 / 02-26**: OpenAI の新規ファインチューニングジョブ作成終了 ／ audio・realtime 系退役 ／ 文字起こし4モデル退役
- **2027-02-05 以降 〜 2027-09-22 以降**: Claude 各モデルの暫定退役日（`claude-opus-4-6` 2/5 → `claude-sonnet-4-6` 2/17 → `claude-opus-4-7` 4/16 → `claude-opus-4-8` 5/28 → `claude-fable-5`・`claude-mythos-5` 6/9 → `claude-sonnet-5` 6/30 → `claude-opus-5` 7/24 → `claude-fable-5-1`・`claude-mythos-5-1` 9/1 → `claude-opus-5-5` 9/22。⚠️ `claude-opus-4-7` は Copilot では 10/2 に消える）
- **2027-03-01 / 03-31 / 2028-10-01**: SharePoint クラシック退役 ／ Azure ポータルの Microsoft Sentinel 体験が退役 ／ SharePoint クラシック退役（第2段階）
- **2027-04**: Apple の最小 SDK 要件が iOS 27 世代へ上がる
- **2027-06-30**: Claude for Teachers の学区登録期限
- **2027年末 / 2028-03**: Anthropic が借りる Nscale West Virginia データセンター（460MW）の稼働開始見込み ／ OpenAI が「automated AI researcher」の実現目標とする時期

## 改善メモ

- 新規提案: B-082（Master・同一ページの上位に過去日付のエントリが後から現れる形を取りこぼし対策へ追加）、B-076（Copilot・掲載歴のあるページの再改訂で前回の根拠節が記録されず改訂差分を特定できない）、B-043（industry・Anthropic のモデル廃止ページを定点ソースに追加）
- 継続提案は Master 29件（最多 B-024・49回目）／ Copilot 38件（最多 B-011・63回目）／ industry 8件（最多 B-004・86回目）
- ソース間の矛盾3件:
  - 10/19 の GitHub Copilot 廃止モデル数が Master 5件・industry 6件で割れている。Master は 9/18 付の告知本文から `GPT-5 mini` を対象外と確定しており、本サマリーは 09-22 の訂正どおり**5件**を採る。industry 側は 6件のまま据え置かれている
  - Grok 4.7 の表示単価が Master $2.20/$6.60・industry $2/$6 で割れている（US リージョン1.1倍の適用有無で説明が付く）。両方とも二次で、一次3ホストはゲートウェイ拒否が継続する
  - Anthropic の上場時期が Master「10月観測」・industry「11月へ後ろ倒し」で割れている。いずれも二次で、一次は 2026-06-01 の S-1 機密提出のみである
- 障害の変化: 3ソースとも新規発生・復旧ともなし。`mc.merill.net` は47日連続、`www.air.security` / `x.ai` 系3ホスト / Devin 系2ホスト / `qiita.com` / `zenn.dev` / `the-decoder.com` / `venturebeat.com` 等のゲートウェイ拒否は継続する
