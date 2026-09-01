# AI News Daily Summary — 2026-09-02

9月1日は3ベンダーが同じ日に「既存の実装と規程を書き直させる変更」を出した日である。Anthropic は Fable 5.1 / Mythos 5.1 を GA させ、キャッシュ読み単価を4分の1にする一方で破壊的変更を3件同梱した。GitHub は Copilot code review の PR 承認をプレビュー公開し、必須承認数にカウントされることを一次で明記した。Claude Code 2.1.257 は auto モードの自動承認範囲を絞ったが、`stable` タグは 2.1.236 のままで差が21版に開いている。Power Platform ではキャンバスアプリの共同編集エージェントが GA した。加えて 02 は、8月の月次まとめが Release Notes に一度も現れない機能を7件含んでいたことを突き止め、「一次の網羅を Release Notes 単独で代表させる」検証手順そのものの誤りを確定させた。

## 今日のハイライト

### 1. Claude Fable 5.1 が GA した — キャッシュ読みが4分の1になり、履歴を書き換える実装は 400 で落ちる

**要点**: Anthropic が 9/1 に Fable 5.1 を全顧客へ出した。基本単価 $10/$50 は据え置きでキャッシュ読みだけ **$1 → $0.25/MTok**。同時に破壊的変更が3件入り、前提が「Fable は最上位で高い」から「反復が多いほど安いが実装は要修正」へ変わる。

**詳細**: モデル ID は `claude-fable-5-1`（Mythos 5.1 は `claude-mythos-5-1` で Project Glasswing 参加者限定）。context 100万トークン・最大出力 12.8万トークン・adaptive thinking 常時オンは Fable 5 と同じで、5分キャッシュ書き込み $12.50 / 1時間 $20 / Batch $5・$25 も据え置き。キャッシュ読みの倍率だけが他モデルの 0.1倍に対し **0.025倍**の例外になった。

破壊的変更は3件ある。

- `tool_choice` の `any` と `tool`: 400 `invalid_request_error` を返す。`auto`（既定）と `none` は変更なし。スキーマを強制したい場合は strict tool use か structured outputs へ移す
- thinking ブロックのモデル束縛: Fable 5.1 は旧モデルの thinking ブロックを読めるが逆は読めず、読めないブロックは API が黙って落とす（`thinking-binding-controls-2026-08-01` ヘッダを付けると `input_transformations` に報告される）
- 過去ターンの編集: `system` プロンプト・`tools` 配列・過去メッセージのいずれかを書き換えると、以後の thinking ブロックが無効になり 400 を返す。⚠️ **2026-08-31 以降に作成されたアカウントでは強制適用**され、それ以前のアカウントは `prefix_mismatch_behavior` を明示したときだけ作動する

コード変更なしで挙動が変わる点も6件挙がっている。並列ツール呼び出しが減って1ターン1呼び出しになりやすい／ツール実行中の進捗テキストが減る／`low` effort で検索を呼ばず記憶から答えがち／散文が密になる／チャットでの装飾が減る／小さな修正でもファイル全体を書き直しがち。Anthropic 自身が「回答品質は落ちないがトークン・往復・実時間のコストが増える」と明記している。

- ⚠️ **ゼロデータ保持では使えない。** 両モデルは30日データ保持が最低要件で、zero retention 契約下では提供されない。規制業種向けの提案ではこの1点でモデル指定の可否が決まる
- ⚠️ 二次が報じる「標準的な負荷で約25%減・エージェント色の強い負荷で最大45%減」は**一次には無い推計**である。一次が保証しているのはキャッシュ読み単価だけで、削減幅はキャッシュ読みの比率次第になる
- 提供先は Claude API・Amazon Bedrock・Claude Platform on AWS・Google Cloud・Microsoft Foundry で、いずれも 9/1 の同日提供。⚠️ Bedrock と Google Cloud は退役スケジュールを独自に持つ
- ベンチマーク（二次報道）: Terminal-Bench-Science 0.1 が Fable 5 の 24.7% に対し 52.6%、Terminal-Bench 4.0 が 42.0% に対し 55.8%。Mythos 5.1 の Terminal-Bench 4.0 は 60.9%

- https://platform.claude.com/docs/en/release-notes/api
- https://platform.claude.com/docs/en/models/fable-5-1/whats-new-fable-5-1
- https://platform.claude.com/docs/en/about-claude/pricing

### 2. Copilot code review が PR を承認できるようになった — 承認がリポジトリの必須承認数にカウントされる

**要点**: GitHub が 9/1 に PR 承認をパブリックプレビューで公開した。Copilot の承認は**必須承認数にカウントされる**と一次が明記しており、前提が「AI レビューは必須承認を満たせない」から「設定次第で満たせる」へ変わる。レビュー規程は書き直しが要る。

**詳細**: 一次 changelog は「有効にすると、Copilot はリポジトリの required-approvals ルールにカウントされる承認を提出できる」と書き、既定でレビューに付く「承認アセスメント」だけでは要件を満たさないという区別も同時に置いている。既定は**無効**で、有効化は3階層で制御する。

- Enterprise: 配下の組織が承認を有効化できるかどうかを決める
- Organization: 組織全体で有効化・リポジトリへ委譲・特定リポジトリのみ対象・全体で無効、の4通りから選ぶ
- Repository: 承認のオン／オフに加え、Copilot が承認してよいファイルパスを限定できる

新しいコミットが push されると Copilot の承認は人間のレビュアーと同様に自動で解除され、更新後のコードに対して再レビューを依頼できる。対象プランは Copilot Pro・Pro+・Max・Business・Enterprise である。

- ⚠️ **GitHub Docs 側の記述は旧仕様のまま**で、「Copilot は Comment レビューしか残さず、必須承認や CODEOWNERS の要件を満たせない」という説明が本日時点でも検索に出る。社内規程をドキュメント経由で確認すると誤った結論になる
- ⚠️ 01 は「`github.blog/changelog` の Copilot ラベルに 9/1 の新規エントリは無く 8/31 の2本が最上位」と報告しており、03 の本項と食い違う。本サマリーは一次 URL を提示している 03 側を採った（改善メモ参照）

- https://github.blog/changelog/2026-09-01-copilot-code-review-can-now-approve-pull-requests/

### 3. Claude Code 2.1.257 で auto モードの自動承認が絞られた — stable 固定の組織には権限修正が21版ぶん届いていない

**要点**: auto モードに Containment Escape ルールが入り、クラウドメタデータからの資格情報取得は自動承認されなくなった。一方 `stable` は 2.1.236 のままで、前提が「stable に居れば安全側」から「権限修正が5日以上届かない側」へ変わる。

**詳細**: 9/1 公開の 2.1.257 で権限境界の変更が複数入った。

- クラウドメタデータからの資格情報取得・egress 回避・テナント跨ぎのアクセスは、環境が想定内と示さない限り auto モードでも自動承認されない
- 作業ディレクトリ外の初回ファイル読み込み前に一度だけ確認が入り、`permissions.blockReadsOutsideWorkingDirectories` で読み取り自体を禁止できる
- `--add-dir` / `additionalDirectories` は UNC 共有や `/net/<host>` 自動マウントを触る前に拒否する（Windows ではドライブレターを割り当てて使う）
- Bash の権限チェックは、解析できない不正な形式のコマンドについて常に承認を要求するようになった。プラグインが symlink 経由でファイルを読めた不具合も修正された
- Cowork と claude.ai のクラウドセッションでは、自分のものではない artifact の読み込みに auto モードでも必ず確認が入る
- `defaultMode: "bypassPermissions"` はプロジェクト設定（`.claude/settings.json` / `settings.local.json`）では無視されるようになった

モデル面では Fable 5.1 が既定の Fable モデルになった。⚠️ ただしゲートウェイ経由のセッションでは `fable` / `best` が当面 Fable 5 に解決されるため、使うには `/model` で明示的に選ぶ。設定系では `timeFormat` と `timeZone`、サブエージェントのモデル指定を全階層へ強制する `CLAUDE_CODE_SUBAGENT_MODEL_FORCE`、当該セッションのみ変更する `/effort` の `s` が加わった。

⚠️ **`stable` タグは 2.1.236 のまま据え置き**で、`latest`（2.1.257）との差が21版に開いた（`registry.npmjs.org` の `dist-tags` 実測）。8/28 の 2.1.251 に入った権限境界の修正群（symlink 差し替えによる作業ディレクトリ外の読み書き・marketplace プラグインのディレクトリ外参照・symlink 経由の Grep / Glob での deny 無視）は、stable 固定の組織へ5日経っても届いていない。`next` は 2.1.257 で `latest` に再合流した。`2.1.253`〜`2.1.256` は npm の `time` にも changelog にも無い欠番で、取りこぼしではない。

- https://code.claude.com/docs/en/changelog
- https://registry.npmjs.org/@anthropic-ai/claude-code

## カテゴリ別まとめ

### Anthropic / Claude

- **Fable 5.1 / Mythos 5.1 の仕様・料金・破壊的変更**（ハイライト参照）
- **会話途中で挙動を変えるベータが3件入った**: Anthropic が Fable 5.1 と同日に、プロンプトキャッシュを壊さずに状態を変えるためのベータヘッダーを公開した
  - `mid-conversation-output-config-2026-07-01`: 会話途中のシステムメッセージへ `output_config.effort` を入れ、1ステップ単位で効力を上下できる（Opus 5 でも使える）
  - `mid-conversation-system-clear-at-2026-08-21`: `clear_at: "next_user_message"` で1ターンだけ有効なシステムメッセージを置ける
  - `thinking-display-updates-2026-08-18`: `thinking.display: "updates"` でツール呼び出しの合間の進捗をテキストブロックとして受け取れる
- **モデル退役ページに `claude-fable-5-1` が Active で追加された。** 暫定退役日は 2027-09-01 以降で、Active は10件から11件へ増えた。⚠️ 「not sooner than」であって確定日ではない。新規の退役告知は無く、直近告知は 2026-06-05 の Opus 4.1（8/5 退役済み）のまま
- **Fable 5.1 と Mythos 5.1 の生成テキストには統計的透かしが入る。** コード実行ツールが作った画像・動画を Files API 経由で取得すると C2PA Content Credentials が付く。リクエスト側の変更は不要で、トークンや隠し文字も増えない
- **`support.claude.com` の Release Notes が7日ぶりに動いた。** 9/1 の Fable 5.1 / Mythos 5.1 リリースが最上位に入り、その前は 8/25 の memory 更新のままだった
- **`claude.com/blog` は 8/28 の2本が最新のままで5日間追加がない。** ⚠️ Fable 5.1 の発表記事は `www.anthropic.com/news` 側にあるとみられるが、同ホストはゲートウェイ拒否で一次未読である。仕様・料金・破壊的変更は `platform.claude.com` の2ページで一次確定できているため、未読なのは発表文の言い回しだけにとどまる
- ⚠️ **8月 Risk Report は17日連続で一次未読**（初出 08-17）。二次の内容に変化はない
- ⚠️ 検索結果に出た「Anthropic が AI 学習とサイバーセキュリティ評価の一部を停止した」という記事群は、7/30 公開の評価インシデント（8/1 に既報）の焼き直しであり新規の出来事ではない
- 既報: 週次上限50%増の 9/13 終了と 9/14 からの恒久 +25%（現行比17%減）、Claudeforce（オープンベータは9月中）、Model Hardware Standard 研究プレビュー、ウェルビーイング研究助成 $5M、Claude for Teachers、インフォスティーラーによる Claude セッション乗っ取り（8/30 連絡開始）

### GitHub Copilot / 開発ツール

- **Copilot code review の PR 承認**（ハイライト参照）
- **Claude Code 2.1.257 の権限・モデル変更**（ハイライト参照）
- **複数組織にシートを持つ利用者のモデルアクセスが、請求元組織の設定だけで決まるようになった**（8/31 適用済み・GitHub Team プラン）。従来は所属するどれかの組織が有効にしていれば使えたため、今日から使えるモデルが減る利用者が出る。請求元は Copilot features ページの「Usage billed to」で確認でき、アクセスが enterprise またはその配下組織だけから来ている利用者は影響を受けない。⚠️ 告知に**対象モデルの記載がない**ため、影響の有無は各自が請求元組織の model policy を見て確かめるほかない。9/1 に完了した global model policy の全 enterprise 適用と合わせると、モデル選択の決定権が個人・所属組織から請求元組織へ寄る流れが2日続けて発効したことになる
  - https://github.blog/changelog/2026-08-31-copilot-model-access-update-for-github-team-plans
- **GitHub が VS Code 版 Copilot の8月分（v1.132〜v1.135）をまとめて公開した**（8/31）。エージェント運用とチャット周りに寄った内容である
  - エージェント: チャットの左右並列比較、`/btw` での脇道会話、プロンプトタイムラインでの履歴移動、Agent Plugins 1.0 準拠のポータブルプラグイン導入、GitHub サインイン無しでの Agents ウィンドウ起動（実験的）、Anthropic 契約と Copilot 契約のモデル切り替え
  - チャット / レビュー: 会話全体のテキスト検索（大文字小文字・正規表現つき）、入力中プロンプトの sticky scroll 固定、Markdown 差分のハイブリッドエディタ表示、応答フッターのホバーでのモデル別トークン使用量表示
  - 内蔵ブラウザ / ディクテーション: Web ページ要素へのコメント、HTML 変更時の自動リロード、HTML の既定エディタ化、オンデバイスモデルでの多言語書き起こしとプロジェクト用語に合わせた整形
  - ⚠️ **IDE 側の変更はこのまとめエントリにしか載らない**。各リポジトリ releases にも Copilot ラベルの個別エントリにも出ない
- **Copilot CLI に pre-release `v1.0.83-1` が出た**（9/1 17:19）。Sessions サイドバーの並び替え（Recent / Created / Name）が再起動をまたいで保持され、enterprise 管理者がサインインを承認済み organization に固定でき、大きなリポジトリでのファイルパス補完が速くなった。`--resume` / `--worktree` 下での `--add-dir` / `--plugin-dir` の相対パス解決も修正された。安定版は `v1.0.82`（8/29）のままである
- **OpenAI が Codex CLI の安定版 `0.152.0` を出した**（9/1 01:58 UTC・前安定版 `0.151.0` は 8/29）。Vim モードで `/` と `?` による下書き内検索が使え、レート上限バナーから使用量確認・クレジット管理・プラン変更へ直接進めるようになった。MCP サーバー名に `:` `@` `/` `.` を使えるようになり、MCP ツールごとに `output_token_limit` を設定でき、app-server クライアントが `thread/shellCommand` のタイムアウトを1時間超まで指定できる。⚠️ **プランニングツールは既定で無効になった**（`tools.update_plan.enabled = true` で有効化）
  - ⚠️ pre-release 3版（`0.152.0-alpha.7.2` / `0.153.0-alpha.1` / `0.153.0-alpha.2`）は本文が展開されず変更内容が未確定である。空になるのは pre-release 側だけで、安定版タグページからは取得できている
- **Cursor が Fable 5.1 の提供を開始した**（9/1）。CursorBench 3.2 の max effort で **73.4%** を記録したと告知しており、同社はこれを「CursorBench 3.2 で走らせた中で最も高い」と表現している。⚠️ Privacy Mode 有効の利用者は Cursor Dashboard で当該モデルの Data Retention Policy に同意しないと使えない。⚠️ モデル提供開始の告知がフォーラム側にしか出ない構造は本日も再現し、`cursor.com/changelog` の RSS には記載がない。プラン別の提供範囲と Cursor 上の単価も告知本文には無い
- 期限: **9/10** MAI-Code-1-Flash 廃止、**9/28** チャット3面統合／code review 既定 Balanced 化／チャットのデータ保持がアカウント存続期間へ、**10/1** 既存顧客の前払い必須化

### Microsoft 365 Copilot / Copilot Studio / Power Platform

- **8月の月次まとめが Release Notes に無い機能を7件含んでいた。** Tech Community の「What's New in Microsoft Copilot」8月号が 8/31 17:51Z に公開され、ユーザー機能12分類＋IT管理者1分類で31機能を扱っている。Release Notes 全文（12,891行・2023年3月以降の全バッチ）を機能名で検索したところ、次の機能が1回も現れなかった
  - チャットセッションと個別応答の読み取り専用リンク共有（`Share chat` / `Share response`）、同じプロンプトの再生成（`Try again`）
  - Excel の変更履歴スキルとチャット履歴、PowerPoint の Strict brand adherence とノート記述による slide 単位の指示
  - SharePoint の個人スキル（Public Preview 8月・全世界展開12月）、Cowork の effort 5段選択と `/cost` スキルの残枠表示
  - Power BI レポート／セマンティックモデルへのグラウンディングは Release Notes では 1/27・4/7・5/5 の3バッチにしか現れないが、月次記事は「6月に Public Preview・8月に全世界展開」と書く
  - ⚠️ **02 は 8/19〜9/1 の6セッションで、二次記事が挙げるセッション共有と Power BI グラウンディングを「Release Notes の全バッチに存在しない」を根拠に不採用としていた。**本記事により、二次が誤っていたのではなく突合先を Release Notes 1本に置いていたことが誤りだったと確定した（B-054 起票）
- **キャンバスアプリの共同編集エージェントが GA した**（9/1）。メーカーが手持ちのコーディングエージェントを MCP 経由でキャンバスアプリの共同編集者にでき、作成の入口が Studio の GUI からエージェント対話へ広がる。プラグインが渡すツールはアプリと画面の作成・変更、利用できるコントロール／コネクタ／データソースの検査、データソーススキーマの解釈、Power Fx 数式の記述と更新、変更の検証と稼働中セッションへの同期である。記事は **coauthoring であって autopilot ではない**と明記し、メーカー側が監督を保持する前提を置く。⚠️ 対応するコーディングエージェントの具体名・前提ライセンス・制限は記事本文に記載がない。2026年5月に Preview 掲載済みで、今回が GA への移行にあたる
  - https://www.microsoft.com/en-us/power-platform/blog/power-apps/turbocharge-your-canvas-development-with-the-canvas-authoring-agent-plugin-now-generally-available/
- **M365 Copilot Release Notes は August 25, 2026 バッチが最新のままである。** 10節・全19項目に増減はなく `updated_at` も 2026-08-25T20:41Z で動いていない。隔週傾向どおりなら次バッチは 9/8 前後になる
- **月次記事が挙げる9月ロールアウト分は3件が一次で確定している**: Copilot Notebooks の Android マルチモーダルキャプチャ、Planner タスクの作成と照会、Copilot ダッシュボードと Agent 365 ダッシュボードからの行単位・非識別化データのエクスポート（管理者向け）
- **Roadmap に 570155 が起票された**（8/31 23:13Z・`In development`・GA 2026年9月・Worldwide）。SharePoint のサイトスキルの編集・バージョン管理・公開・復元・サイト間複製に対応し、組織がスキルを統制して再利用できるようにする。月次記事の「SharePoint の個人スキル」（ユーザー所有・OneDrive に Markdown で保存）とは層が異なる
  - ⚠️ Copilot Studio 製品の15件は全件 `In development` のままで状態変化がない。**566997**（メーカー資格情報の使用ブロック）は GA 期日「August CY2026」を満たせないまま9月に入り、**562221**（MCP 準拠ツールのワークフロー利用）は GA 期日 2026年6月から超過4か月目である
  - RSS の `lastBuildDate` は 8/28 21:59Z から 8/31 23:13Z へ動いて4日間の据え置きが解消した。⚠️ ただし総項目数は 1,769 → 1,766 と3件減っており、総数差分を新規件数として読むと本日の新規1件も検出できない
- **Copilot Studio What's New は July 2026 節が最新のままで、8月節・9月節とも未作成である。** ⚠️ June 節の GitHub Copilot ハーネスは `(Production-ready preview)` のままで、GA（8/3）から30日連続の未反映が続く
- **Released Versions の Copilot Studio Build は 2026.6.3 のままで空白が64日に達した。** 9/1 の定例更新日（火曜）にも新ビルドが出ず、定例日の空振りは10回連続である
- **Release Wave 3ページは 8/28 から6日連続まったく再ビルドされていない**（`updated_at` 2026-08-27T17:04Z・`git_commit_id` b92ae441）。冒頭 Important の移行注記は3ページとも入ったままで、9月に入っても Release Plans 側に掲載停止の実装は現れていない
- **Copilot Tuning は停止発効（8/20）から13日たっても一次に停止も退役も書かれていない。** `copilot-tuning-overview` の `updated_at` は 2026-08-18T17:48Z で動かず、Optimization エージェントを現行機能として掲載したままである
- **Partner Center の9月ページが開設された**（`updated_at` 2026-09-01T16:42Z）。8/31 時点で 404 だったページが 200 を返し、掲載は Microsoft Marketplace の Purchase order mapping 1件のみである。顧客が Marketplace 購入を自社の発注書・調達プロセスへ割り付けられるようにするもので、⚠️ Copilot 固有のライセンス変更ではない。MAICPP 契約の更新条項は 9/1 に自動発効済みで、Solutions Partner バッジの名称が3つの商用ソリューション領域（AI Business Solutions・Cloud & AI Platforms・Security）に揃えられた
- **SharePoint ページ作成者が、柔軟セクションを標準セクション並みに予測しやすく扱えるようになった**（9/1・記事ID 4548566）。列レイアウトガイドが標準セクションと同じ列構造を可視化し、Web パーツ追加時に列幅へ自動整合する。グリッド表示はコマンドバーのトグルでページ単位に常時表示でき、標準セクションから柔軟セクションへの変換は非破壊で列構成と重なり順を保持する。Copilot 固有の機能ではない
- **コネクタ／プラグインの追加が業種横断で続いている**: 金融は Mercury / Xero、法務は iManage Work / Harvey / Relativity / Everlaw、専門サービスは Statista / ZoomInfo / IDC、ヘルスケアは Scite / Consensus、技術系は Adobe Journey Optimizer / GoDaddy / Asana
- 既報: SharePoint クラシック体験の退役はフェーズ1が **2027-03-01**、フェーズ2が **2028-10-01** で変更なし

### Google

- **Gemini の Flash 系3モデルに agentic video understanding が入った**（9/1）。従来は動画を先頭から一定レートで走査していたが、新方式ではモデルが内部のエージェントループでツールを呼び、必要な区間だけをフレーム・音声・書き起こしのいずれかで読み込む。読む速度とチャンネルもモデルが決める。対象は Gemini 3.7 Flash・3.6 Flash・3.5 Flash-Lite で、効果は 3.7 Flash で**トークン最大88%減**・精度最大7%向上とされ、別の二次はコスト最大66%減と報じている。変わるのは単価ではなく同じ動画の処理に要するトークン数である
  - ⚠️ 一次の `blog.google` はゲートウェイ拒否のため、削減率と対象モデルは二次スニペットの突き合わせによる。API changelog 側に「長尺コンテンツで静的処理比 最大88%少ないトークン」の記載があり、この1点は一次で裏が取れている
  - https://ai.google.dev/gemini-api/docs/changelog
- **Gemini API 料金ページは最終更新日だけ 9/1 UTC へ進み、単価は据え置きだった。** 3.7 Flash / 3.6 Flash は入力 $0.75・出力 $3.75（12/31 まで。2027/1/1 から $1.50／$7.50）、3.5 Flash $1.50／$9.00、3.5 Flash-Lite $0.30／$2.50 で、更新は agentic video understanding の追記によるものとみられる
- **Gemini API changelog は 8/27 の Gemini Omni Flash GA が最上位のままである**（8/28〜9/1 の追加なし）。⚠️ 01 は本日の巡回でも「5日間追加なし」としており、03 が確認した agentic video understanding の記載と食い違う可能性がある（改善メモ参照）
- **9/1 付けの Google の AI 発表は検出できなかった。** ⚠️ 9/2 から Build with Gemini イベントが Chicago / New York / San Francisco / Sunnyvale / Seattle で順次開催されるとされるが、一次は `blog.google` / `cloud.google.com` 側にあり到達できていない
- 既報: 旧 `gemini-omni-flash-preview` は 9/30 廃止、Gemini 3.5 Pro GA は未ローンチが継続

### OpenAI / Codex / ChatGPT

- **Codex CLI 0.152.0**（開発ツール節を参照）
- **OpenAI の退役ページに新規期限はなかった。** 既存9件を前日の記録と全件突き合わせ、撤回・延期・追加のいずれも無いことを確認した。次の期限は **9/24** の Videos API と `sora-2` / `sora-2-pro` / Sora 2 スナップショットで残り22日であり、移行先が用意されていない点は変わらない。その後は 9/28 の旧 GPT-3.5 系4モデル、10/23 の旧 GPT スナップショット群と `o1` / `o1-pro` / `o3-mini` と続く
- **GPT-5.6 の単価は9日連続で据え置きである。** 100万トークンあたり Sol は入力 $4・キャッシュ $0.40・キャッシュ書込 $5.00・出力 $20（長文脈側 $8／$0.80／$10／$30）、Terra は $2／$0.20／$2.50／$12（長文脈側 $4／$0.40／$5／$18）、Luna は $0.20／$0.02／$0.25／$1.20（長文脈側 $0.40／$0.04／$0.50／$1.80）である。Sol の期間限定価格が「少なくとも 2026年11月21日まで」という記載も動いていない
- **`developers.openai.com/api/docs/changelog` は 8/29 の mTLS / X.509 GA が最上位のままである**（8/30〜9/1 の追加なし）
- **`community.openai.com` の Announcements RSS は 8/25 の WebMCP 2本が最上位のままで8日間動きがない。** WebMCP Challenge は提出締切 9/4・受賞発表 9/23・賞金総額 $35,000 である
- ⚠️ **`learn.chatgpt.com` は9月分の新規エントリを返さなかった。** ゲートウェイ拒否が継続しているため `site:` 付き WebSearch で確認したが、返るのは 8/24〜8/28 週までだった。検索インデックスのラグの範囲内とみて取りこぼしとは区別している
- 到達性: `developers.openai.com` は 200、`openai.com` はオリジン403、`learn.chatgpt.com` はゲートウェイ拒否が継続している

### オープンウェイト / MCP / xAI

- **HF の 8 org いずれにも 9/1 の新規公開は無かった。** `createdAt` 降順と `lastModified` 降順の両方で確認した。各 org の最新作成は `Qwen3.8-Flash-Next-FP8` 8/24、`DeepSeek-V4-Flash-Vision-Exp` 8/31、`GLM-5.3-Flash-BF16` 8/25、`timesfm-3.0-pytorch` 8/24、`Muse-Glimmer-30B-ExecuTorch-PTE` 8/10、`Shieldstral-1.0-3B` 7/16、`Kimi-K3` 6/13、`privacy-filter` 4/17 である
  - ⚠️ **2ヶ月半前に公開された `GLM-5.2` 系2件が 9/1 に更新された点は、新規公開の検出手順では拾えない。** `createdAt` は 6/16 のままなので `createdAt` 降順の巡回には一切現れない
  - `downloads` 実測（9/1 19:15 UTC）: `Qwen3.8-27B-FP8` 5,528,743、`DeepSeek-V4-Flash-0731` 4,650,353、`GLM-5.3-Flash` 441,348。追跡リポジトリは全て公開状態に変化なく、`DeepSeek-V4-Flash-Vision-Exp` は公開2日目で初めて `downloads` に値が付いた
- **`blog.modelcontextprotocol.io` は 8/22 の「The New MCP Roadmap」が最上位のままで11日間新規がない。** ⚠️ WebMCP は MCP 公式ブログ側に一切言及がなく、OpenAI 発の別系統として扱う。A2A の AAIF 参加は未確定のままで、一次3ホストはゲートウェイ拒否が継続している
- **Grok 5 も Grok 4.7 も未リリースが継続している。** ⚠️ 二次は「9/2 までに 4.7 が出るとするロードマップ signal がある」と書くが、日付・仕様とも公式の裏づけが無い観測である。一次3ホスト（`x.ai` / `docs.x.ai` / `grok.com`）は到達不可のままで、8/30 とされる Grok Build の更新も一次未読で据え置いている
- **Devin は `docs.devin.ai` のゲートウェイ拒否が続き一次に到達できない。** ⚠️ 二次が挙げる CLI の org / agent / session 管理改善、`/recap`・`/rename`・`devin doctor` の追加、Gmail / Google Calendar / Gamma / Supabase の MCP サーバー追加は、いずれも公開日を特定できず既報との切り分けができないため新着扱いしない

### 企業動向・規制 / 市場データ

- **米国防総省が GenAI.mil へ ChatGPT Mil と Grok for Government を追加した。** 従来は Google Cloud の Gemini for Government 1本だったため、単一ベンダーの試験導入から複数モデルのマーケットプレイスへ移ったことになる。対象は軍人・文民あわせて300万人超で、うち170万人超が既にオンボード済みとされる。ChatGPT Mil はチャット・ファイル・プロジェクト・カスタム GPT を含み、調達資料の作成とレビュー、方針文書の要約、内部レポートとコンプライアンスチェックリストの生成に使うとされる。ChatGPT Mil と Grok for Government はいずれも **Impact Level 5** の CUI 認定を取得しており、対象は非機密の業務である
  - ⚠️ **Anthropic は本発表に含まれていない。** 8/27 に連邦地裁が国防総省による Anthropic の指定を違法と判断した件と地続きで、政府調達では「フロンティア3社が横並びで載る」前提が成り立たない実例になった。二次記事のいずれもこの関係には触れていない
  - ⚠️ 発表日は 01 が 9/1、03 が 8/31 としており食い違う（改善メモ参照）。一次は `www.defense.gov` / `openai.com` 側にあるとみられるが未読で、人数・認定レベル・機能一覧は二次一致で採った
  - https://defensescoop.com/2026/08/31/grok-chatgpt-added-to-genai-mil/
- **市場データ定点はいずれも更新がなかった。** IDC・MM総研・NRC・Similarweb のすべてで新規公表を検知できていない。参照可能な最新値は IDC の国内AI市場予測（2025年 2兆3,725億円 → 2029年 6兆8,897億円・CAGR 36.0%）と MM総研の個人利用経験率 21.8%（2025年8月時点・利用者数1,597万人）で、いずれも既収録から不変である
- 既報: 100社超のサイバー防衛公開書簡（8/27）、Anthropic × Nscale 約 $45B・6年（West Virginia 約 460MW・2027年末稼働）、年換算 run-rate $650億（7月末）、SpaceX による Cursor 買収完了（8/14・$60B）

### Apple / クラウド

- **`developer.apple.com` は 8/27 の税・価格更新告知が最上位のままで5日間追加がない。** AI 関連の最新は 6/11 の ImageCreator クラス廃止告知（iOS 27 / iPadOS 27 / macOS 27 / visionOS 27 以降で動作しない）で、8/5 の App Store creative assets 以降に新規はない
- **AWS Bedrock は Fable 5.1 を初日から扱う**（`anthropic.claude-fable-5-1`）。Claude Platform on AWS・Google Cloud・Microsoft Foundry も 9/1 提供開始である
- 既報: Apple 特別イベント（**9/9 10:00 PT**）、Sign in with Apple 新ドメイン（`private.icloud.com`）、EU 向けビジネス条件変更2本（発効 **2026-10-01**）

## 直近の注目予定

- **9/3**: Copilot 非推奨一覧の週次確認
- **9/4**: WebMCP Challenge の提出締切 ／ Copilot 拡張機能 What's New・モデル可用性一覧の週次確認
- **9/6**: PnP・Power CAT の週次確認
- **9/7**: 週次復旧チェック（月曜）／ ppweekly・MS-4005・課金レート表の週次確認
- **9/8 前後**: M365 Copilot Release Notes の次バッチ
- **9/9**: Apple 特別イベント（10:00 PT）／ GLM-5.3-Flash の Z.ai 経由50%割引が終了
- **9/10**: MAI-Code-1-Flash が全 Copilot 体験から廃止
- **9/13**: Claude Code の週次上限50%増が終了
- **9/14**: Claude Code の標準週次上限が恒久的に +25%（現行比では17%減）
- **9/17**: OpenAI DevDay Exchange の応募締切
- **9/21**: Anthropic ウェルビーイング研究助成の応募締切
- **9/23**: WebMCP Challenge の受賞発表
- **9/24**: OpenAI の Videos API と Sora 2 動画生成モデルが退役（代替モデルの提示なし）
- **9/28**: Copilot のチャット3面統合 ／ code review の既定 effort が Lite → Balanced ／ チャットのデータ保持がアカウント存続期間へ ／ OpenAI の旧 GPT-3.5 系4モデル退役
- **9/29 以降**: `claude-sonnet-4-5-20250929` の暫定退役日（確定日ではない）
- **9/30**: Gemini の旧 `gemini-omni-flash-preview` エンドポイント廃止
- **9 月**: iOS 27 / macOS 27 GA ／ Claudeforce のオープンベータ（二次情報）／ Copilot Studio の Roadmap 項目9件が GA 期日 ／ Release Plans on Learn への新規掲載停止 ／ Copilot Tuning の再開 Public Preview ／ App Store の Social Media 年齢レーティング回答が必須化 ／ OpenAI の IPO 観測
- **10/1**: Copilot Business・Enterprise の既存顧客が前払い必須に ／ Apple の EU 向け新ビジネス条件が発効 ／ Ask Gemini in Chat のプロモーション上限が終了
- **10/5**: Anthropic ウェルビーイング研究助成の full proposal 提出期限（採択者）
- **10/15 以降**: `claude-haiku-4-5-20251001` の暫定退役日（確定日ではない）
- **10/16–11/11**: OpenAI DevDay Exchange 8都市（**東京は 10/20**）
- **10/23**: OpenAI のレガシースナップショット退役（`gpt-3.5-turbo` / `gpt-4-0613` / `gpt-4-turbo` とファインチューン版、`o1` / `o1-pro` / `o3-mini`）
- **10 月**: Anthropic の IPO 予定（$2T 超の評価額を目標と報道）／ 韓国 App Store のコンテンツ記述子2件が All → 12+
- **11/15**: Release Planner の退役
- **11/21**: GPT-5.6 Sol の暫定値下げが有効とされる期限
- **11/24 以降**: `claude-opus-4-5-20251101` の暫定退役日（確定日ではない）
- **11/30**: OpenAI の Reusable prompts・Evals プラットフォーム・Agent Builder が停止
- **12/1**: OpenAI の GPT Image 系が停止（`gpt-image-1-mini` / `gpt-image-1.5` / `chatgpt-image-latest` → `gpt-image-2`）
- **12/2**: EU AI Act の生成コンテンツ標識義務、8/2 以前に市場投入済みシステムへの猶予終了
- **12/11**: OpenAI の旧スナップショット退役（`gpt-5-2025-08-07` / `o3-2025-04-16` 等）
- **12/31**: Gemini 3.7 Flash の導入価格終了（$0.75/$3.75 → $1.50/$7.50）
- **年内**: Anthropic の新データ保持方式（顧客自身のクラウドでの30日保持）投入予定 ／ OpenAI の Jalapeño チップの初期展開
- **2027-01-06**: OpenAI で大半のユーザーの新規ファインチューニングジョブ作成が終了
- **2027-01-20**: OpenAI の audio / realtime 系退役（`gpt-realtime` / `gpt-audio` / `gpt-4o-audio` と mini 系）
- **2027-02-26**: OpenAI の文字起こし4モデル退役（`whisper-1` / `gpt-4o-transcribe` / `gpt-4o-mini-transcribe` / `gpt-4o-transcribe-diarize`）
- **2027-03-01**: SharePoint クラシック体験の退役フェーズ1
- **2027-06-30**: Claude for Teachers の学区登録期限
- **2027-09-01 以降**: `claude-fable-5-1` の暫定退役日（確定日ではない。09-02 追加）
- **2027年末**: Anthropic が借りる Nscale West Virginia データセンター（460MW）の稼働開始見込み
- **2028-06**: 米国 K-12 教職員向け ChatGPT for Teachers の無料提供期限
- **2028-10-01**: SharePoint クラシック体験の退役フェーズ2

## 改善メモ

- 3ソースの当日分（01 Master / 02 Copilot / 03 industry）はいずれも取得できた。前日 09-01 分にも欠損記録はなく、欠損リカバリの対象はない
- ⚠️ **`github.blog/changelog` の 9/1 分について 01 と 03 が食い違う** — 01 は「Copilot ラベルに 9/1 の新規エントリは無く、8/31 の2本が最上位」と報告するが、03 は 9/1 付の Copilot code review PR 承認エントリを一次 WebFetch で本文まで確認し URL も提示している。**本サマリーは一次 URL のある 03 側を採った**が、01 側の巡回でラベル絞り込みの取りこぼしが起きている可能性があるため、次回以降も突合が必要になる
- ⚠️ **Gemini API changelog の扱いも 01 と 03 で分かれた** — 01 は「8/27 の Omni Flash GA が最上位のまま、8/28〜9/1 の追加なし（5日間）」とし、03 は同じ changelog で agentic video understanding の提供開始を確認したとしている。03 は「長尺コンテンツで静的処理比 最大88%少ないトークン」の文言まで一次で裏を取っており、01 側が更新を拾えていないとみて 03 を採った
- ⚠️ **GenAI.mil への ChatGPT Mil / Grok 追加の日付が 01 は 9/1、03 は 8/31 で食い違う** — 03 は自リポジトリの捕捉が「2日遅れ」と明記しており 8/31 発表を前提としている。一次（`www.defense.gov` / `openai.com`）はいずれも未読のため、本サマリーは日付を断定せず両論を残した
- **Fable 5.1 のコスト削減幅は一次の保証範囲外である** — 01 は「典型的な負荷で 25% 安い」を一次に無い推計と明記し、03 は二次報道として「標準25%減・エージェント色の強い負荷で最大45%減」を採録した。一次が保証するのはキャッシュ読み単価 $1→$0.25 だけであり、削減幅はキャッシュ読みの比率次第になる
- **新規の改善提案は2件** — B-056（01: モデルドキュメントの URL をモデル固有ページからモデル非依存の一覧＋現行モデルの `whats-new` へ差し替え）、B-054（02: 二次報告の裏取りを Release Notes 単独で行うと実際にロールアウト済みの機能を落とす）。03 は新規提案なし
- **継続提案は3ソース計73件**（01: 32件・最多は B-013 の35回目、02: 29件・最多は B-011 の44回目、03: 12件・最多は B-004 の65回目）。⚠️ 前日サマリーは 02 を40件と記録していたが本日は29件で、増減の内訳は本日のダイジェストからは追えない。前々日の28件を含めて 28 → 40 → 29 と振れており、計数基準が安定していない可能性がある
- **B-054 の番号が 01 と 02 で重複している** — 01 の B-054 は「DeepSeek 公式 news をソース登録」（09-01 起票）、02 の B-054 は「Release Notes 単独での裏取りの誤り」（本日起票）で、別々の台帳の別提案である。横断で参照する際に取り違えやすい
- **取得障害の変化は無い。** 3ソースとも新規の障害・復旧は発生していない。01 は本日試行した全ホストで本文取得に成功しており、03 の `the-decoder.com` / `venturebeat.com` / `blog.google` はいずれも既知のゲートウェイ拒否で最終確認日のみ更新した
- ⚠️ **長期化している一次未読・接続障害**: 8月 Risk Report が17日連続（01）、`www.anthropic.com` の拒否継続で Fable 5.1 の発表記事が未読（01）、`mc.merill.net` の `EGRESS_BLOCKED` が26日連続（02）、Copilot Tuning 一次の未更新が13日連続（02）、Copilot Studio What's New への GA 未反映が30日連続（02）、Released Versions の空白が64日（02）。いずれも解消の見込みが立っていない
- **未解決の要 kit 対応（08-07 確定・継続）**: 08-06 追加の許可ドメイン13件は新規起動セッションでも全件未到達。① 保存先環境とスケジュールタスク実行環境の同一性確認 ② `.google` TLD 3件の個別指定確認 ③ 次回追加対象に `api-docs.deepseek.com` / `www.deepseek.com`（B-054）ほかを含める
