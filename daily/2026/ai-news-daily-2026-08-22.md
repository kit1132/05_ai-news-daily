# AI News Daily Summary — 2026-08-22

土曜は、書いたコードと操作する場所の両方に手が入った日である。Anthropic Python SDK が v1.0 で `temperature` を落とし、サンプリング指定で出力を揃えていた実装は移行なしでは上がらなくなった。操作面では Slack が Slack Code を公開し、GitHub Copilot も Slack と Teams に入って、エージェントの操作がターミナルから共有チャンネルへ出た。Microsoft 側は9月に簡素化 Copilot UI を Outlook と Teams へ既定で入れる MC が2本見つかっている。Claude Security は Mythos 5 に載り替わり、Enterprise なら追加契約なしで今日から使える。Claude Code は v2.1.238 が `latest` に昇格し、`headersHelper` の実行にフォルダの信頼承認が要るようになった。

## 今日のハイライト

### 1. Anthropic Python SDK が v1.0 になり `temperature` が消えた — サンプリング指定で出力を揃えていたコードは書き直しになる

**要点**: Anthropic が 8/20 に Python SDK **v1.0** を公開し、Messages の `temperature` / `top_p` / `top_k` と旧 Text Completions API を削除した。出力制御の前提が「サンプリング指定」から `effort` 一本へ確定した。

**詳細**: 削除・変更されたのは長期の非推奨面と HTTP 層で、いずれも移行作業を伴う。

- HTTP 層: `httpx` から `httpx2`（API 互換のメンテナンス継続フォーク）へ移った。カスタムの `http_client` / `Timeout` / transport は `httpx2` 側のオブジェクトで組み直す。`DefaultHttpxClient` ヘルパーは変更がない。`httpx` にパッチを当てるトレーシング・モック系ライブラリを使う場合は起動時に `httpx2.alias_httpx()` を呼ぶ
- 削除: 旧 Text Completions API、Messages メソッドの `temperature` / `top_p` / `top_k`、tool runner のクライアント側 `compaction_control`
- 必要 Python: **3.10 以上**へ引き上げられた
- 非同期クライアント: `.with_raw_response` の結果に `await response.parse()` が必要になった
- `AnthropicBedrock`: AWS リージョン未設定時に `us-east-1` へ既定で落ちる挙動をやめ、エラーを送出するようになった

サンプリング系パラメータの削除は、モデル側の制御が `effort` へ一本化された流れの帰結にあたる。07-24 収録の Claude Opus 5 で「`effort` が主要な制御手段」と明記され、`thinking: disabled` が effort `xhigh` / `max` で 400 を返す破壊的変更が入っていた。SDK 側はその前提を v1.0 で確定させた形になる。移行の全差分は公式の migration guide に before / after 付きで載っている。

- https://platform.claude.com/docs/en/release-notes/api
- https://platform.claude.com/docs/en/cli-sdks-libraries/sdks/python
- https://github.com/anthropics/anthropic-sdk-python/blob/main/MIGRATION.md

### 2. 簡素化された Copilot UI が9月に Outlook と Teams へ既定で入る — 影響範囲が Copilot アプリ利用者から両アプリの全利用者へ広がる

**要点**: 未掲載の MC 2本が索引に現れ、チャット中心の Copilot UI を **2026年9月**に Outlook と Teams へ既定投入することが分かった。管理者・ユーザーの操作は不要で、UI 変更の対象が「Copilot アプリを開く人」から両アプリの全利用者へ広がる。

**詳細**: 本日 8/22 は、M365 Copilot アプリのチャット中心 UI（MC1325422）が Deferred リリースリングへ全世界展開を始める日にあたる。その確認の過程で、同じ設計を他アプリへ広げる MC 2本が索引に現れた。

- **MC1458470**（Outlook）: 全画面 Copilot は Copilot アプリの更新をほぼそのまま反映し、サイドペインは Outlook 内の文脈的なやり取りに最適化した新デザインになる
- **MC1458472**（Teams）: ナビゲーションの簡素化、チャットレイアウトの更新、エージェントの発見と操作の改善、Work IQ コントロールの導入が入り、全画面表示に新しい Tasks ビューが加わる
- 適用方法: どちらもサービス更新の一部として既定で有効になり、ユーザー・管理者の操作を必要としない

MC1325422 本体の経緯は、6/22 に全世界展開を開始し、7/15 までオプトアウトのトグルを置いたうえで以後は新体験を既定にする、というものだった。本日はその Deferred リング分の展開にあたる。

⚠️ **本件は一次を読めていない。** `mc.merill.net` は15日連続で `EGRESS_BLOCKED`、MC を扱う二次ブログの `m365admin.handsontek.net` / `mwpro.co.uk` も同じ拒否で、本日新たに索引に出た `pupuweb.com` も拒否を返した。読めたのは検索インデックスのスニペットだけで、確定しているのは MC 番号と要旨に留まる。

- https://mc.merill.net/message/MC1325422 （取得不可・検索インデックス経由）
- https://www.microsoft.com/en-us/microsoft-365/blog/2026/05/28/introducing-a-new-design-for-microsoft-365-copilot/

### 3. Slack Code が公開され GitHub Copilot も Slack / Teams に入った — エージェントの操作面が個人のターミナルからチャンネルへ移る

**要点**: Slack が 8/20〜8/21 に **Slack Code** を公開し、GitHub も 8/21 に Copilot の Slack / Microsoft Teams 連携を public preview で出した。エージェント操作の場が個人のターミナルから共有チャンネルへ移り、「誰がどのエージェントに何をさせたか」がレビュー対象になる。

**詳細**: Slack Code は、任意の会話でコーディングエージェントをメンションすると専用の code チャンネルが立ち、会話 / plan / コード差分 / ライブプレビューのタブでチャンネル全員が経過を追える仕組みである。ローンチパートナーは **Claude Code・GitHub Copilot・Devin・Vercel Agent・ChatGPT** で、Slack 側は全サブスクリプションで追加費用なし（各エージェントのアクセス権は別途必要）。

GitHub 側の2件は対象プランと課金が異なる。

- Slack 版: `@GitHub` にコードや GitHub 上の活動を質問でき、issue のトリアージ・障害調査・隔離クラウドサンドボックスでの実装と検証・PR 作成までを任せられる。対象は Copilot Business / Enterprise で、消費は既存の Copilot エンタイトルメントから引かれる
- Teams 版: チャンネル / スレッド / DM で `@GitHub` をメンションすると cloud agent セッションが立ち、参加者全員が質問・文脈追加・計画の操舵を行える。ただし変更をトリガーできるのはリポジトリへ write 権限を持つ参加者だけである。課金は cloud agent セッションとサンドボックスが別々の AI クレジットを消費する
- 共通の統制: issue / PR は Copilot アプリの identity に帰属し、リポジトリ管理者はエージェント作成 PR のマージ前に追加承認を必須化できる

⚠️ 課金の当たり方が2製品で違う点が見積もりの分岐になる。Slack 版は既存エンタイトルメント内に収まるが、Teams 版はサンドボックス利用が従量消費になるため席数だけでは費用が読めない。

- https://slack.com/blog/news/slack-code-channels-for-agents
- https://github.blog/changelog/2026-08-21-the-new-github-copilot-experience-in-slack/
- https://github.blog/changelog/2026-08-21-shared-agentic-work-with-github-copilot-in-microsoft-teams/

## カテゴリ別まとめ

### Anthropic / Claude

- **Claude Security が Mythos 5 で公開ベータに入った**: Anthropic が 8/21 に、Claude Security の脆弱性スキャンを Claude Mythos 5 で動かすと発表した。全 Claude Enterprise 顧客が使え、**追加のサブスクリプション契約は不要**で、消費は通常のトークン課金として扱われる。有効化は管理者が admin console で行い、アクセスは Claude.ai のサイドバーまたは `claude.ai/security` から可能である
  - 動作: コードベースのスキャン → 敵対的な検証パスによる裏取り → 修正パッチの提案（人間レビュー前提）。定期スキャン・却下理由の記録・CSV / Markdown エクスポートを備える
  - 経緯: 2026-04-30 に public beta へ入った時点では Opus 4.7 で動いており、今回が cyber 特化モデルへの入れ替えにあたる。Team / Max 向けの提供は「開発中」とされ日付は示されていない
  - 見積もり: 料金はライセンス固定ではなくスキャンしたコード量に比例するため、シート数ではなく対象コード量から立てる必要がある
  - ⚠️ Mythos 5 はセーフガードを外した版が審査済みの防御側・重要インフラ事業者に限定されてきた経緯があり、今回開放されたのはセーフガードが掛かった Claude Security 経由の利用である
- **同日の Anthropic 告知は4本立てだった**: Claude Security への Mythos 5 投入に加え、セキュリティベンダーが自社製品へ Mythos 5 を統合する経路（利用者が触れるのはパッチやアラートのみ・提供時期の明示なし）、オープンソース向けに $35M 分の Claude クレジットを配る **Defender Advantage Fund**（0xDAF・初回交付先は数週間内に公表）、Cyber Verification Program を広い dual-use 能力へ拡大する計画が同時に出た
- **browser use tool の仕様が判明した**（ハイライトは 8/21 分を参照）: 8/19 公開の `browser_toolset_20260801` は、自社アプリが持つブラウザを Claude に運転させるクライアント側ツールセットで、実行はすべて自環境で行う。member tool は31本あり、`read_page`（アクセシビリティツリーと要素参照）・`find`・`get_page_text` の読み取り系、`form_input` / `file_upload`（既定で無効）、タブ管理4本、`read_console` / `read_network` / `javascript_exec` の診断系、従来の座標系操作が揃う。computer use との違いは要素参照（`ref_2` 等）でレイアウト変化に耐える点にある
  - ⚠️ **browser use tool は Claude API 限定**で、Bedrock / Google Cloud / Microsoft Foundry では使えない（computer use の GA 版はこれらで beta 提供）。対応モデルは Fable 5 / Mythos 5 / Opus 5 / Sonnet 5 / Opus 4.8
  - computer use の GA 側は、beta ヘッダ不要に加えて1ターンに複数アクションを返すバッチ実行、`zoom` の既定有効化、`configs` による member 単位設定が入った。`display_width_px` の指定は不要になり、既存の `computer_20251124` 連携はそのまま動く
  - ⚠️ ドキュメントは、認証情報を持たない隔離コンテナで動かし、ネットワーク層でドメイン許可リストを敷き、`javascript_exec` と `file_upload` は必要になるまで無効のままにすることを求めている
- **Anthropic が The AI-Native SDLC playbook を公開した**（8/21）: 従来の6段階（Plan / Design / Build / Test / Deploy / Maintain）を AI ネイティブなループへ組み替える運用ガイドで、文書の受け渡しをバージョン管理下の markdown 成果物（`intent.md` / `spec.md` / `plan.md`）に置き換える点が中心にある。具体値としてエンジニア1人が Claude セッションを2〜3本並行で走らせること、eval スイートを実タスク20〜50件から始めること、`CLAUDE.md` を1ページ以内に保つことを挙げる。⚠️ 調査データや定量値はなく、Anthropic 自身の実践に基づく設計テンプレートとして扱う
  - 7/21 公開の「How Anthropic secures its AI-native software development lifecycle」と対になる。あちらの実測値はマージされるコードの約80%を Claude が執筆、四半期あたり出荷量が 2021〜2025 年比8倍、実質的なレビューコメントが付く PR の割合が 16% → 54%、Claude が発見・修正した OSS の high-severity 脆弱性が500件超
- **Anthropic の IPO 規模が SpaceX の記録に並ぶか上回る見込みと Bloomberg が報じた**（8/21）: 今月末にも公開申請する可能性があり、引受行に Citigroup を追加する見通しとされる。比較対象の SpaceX は6月に5億5,556万株を1株 $135 で売り出して **$75B** を調達し（オーバーアロットメント行使後 $86.2B）、評価額は約 $1.77T だった。⚠️ 公式発表ではない
- `support.claude.com` の Release Notes は 8/6 の skill / plugin セキュリティスキャン beta が最上位のままで、16日連続で動きがない。同期間に `platform.claude.com` は3日分のエントリを出しており、更新頻度の差が再現している
- 既報: Claude Code の週次上限50%増は **8/31 まで延長済み**（Pro / Max / Team とシート課金のレガシー Enterprise）、下院民主党22名の監督書簡（回答期限 8/24）、データ保持ポリシー変更計画の Bloomberg 報道（8/20・一次の `privacy.claude.com` は 7/9 更新のまま）、Claude Sonnet 5 の 9/1 値上げ撤回（入力 $2 / 出力 $10 を標準価格として維持）

### Claude Code / 開発ツール

- **Claude Code v2.1.238 が `latest` へ昇格した**（8/20 18:01 UTC）: 前日は npm の `next` にしか出ていなかった版が changelog に掲載された。50項目超の大型リリースで、実務に効くのは次の4点である
  - `headersHelper`: プラグインマーケットプレイスとカタログエントリで、短命トークン等の HTTP ヘッダをコマンドで都度発行できる。カタログエントリ側はインストール / 更新時のみ実行され、コマンドを表示したうえで `[y/N]` を問う
  - **信頼ダイアログが前提条件になった**: プロジェクトの `.mcp.json` やエージェントファイル由来のインライン MCP サーバー・`headersHelper` は、そのフォルダの trust ダイアログを承認済みでなければ動かない（`claude -p` でも同様）。実行時に継承した認証情報の環境変数は渡されない
  - `claude self-hosted-runner` に `--defer-shutdown-max-min` と `--proxy-authorization-command` / `--proxy-authorization-file` が加わった。SIGTERM 後も接続中セッションを指定分まで維持でき、接続ごとに `Proxy-Authorization` を要求する egress プロキシに対応する
  - 長時間セッションのメモリ増加を修正した。サブエージェントのツール結果が表示ウィンドウを外れた時点で解放される。`keybindingFlavor` に `"readline"` を指定すると Ctrl+W が Bash と同じく直前の空白まで削除する
  - v2.1.237 では LLM ゲートウェイ / カスタム base URL 利用時のプロンプトキャッシュが直り、結果を先に出して前置きと実況を省く出力スタイル「Concise」が `/config` に追加された
- **npm の `dist-tags` は `{stable: 2.1.228, latest: 2.1.238, next: 2.1.239}`**（8/22 実測）: `next` の v2.1.239 は 8/21 17:18 UTC publish で changelog 未掲載である（npm 先行の6例目）。`stable` は 2.1.228 で据え置きのため、`latest` との差は10版に拡大した
- **Copilot CLI の pre-release v1.0.81-7 が出た**（8/21 18:39 UTC）: セッション復帰と管理ポリシーの厳格化が入った
  - 起動時に、CLI が落ちたまま残っていたセッションの復元を提案するようになった
  - `forceRemoteSettingsRefresh` が fail-closed になった。設定時はキャッシュ済みの管理ポリシーを一切使わず、取得に失敗した起動は制限的な undetermined-policy 姿勢で動く。既定外の MCP サーバーがブロックされ、bypass-permissions モードが有効化できず、ポリシー対象のプラグイン導入 / 更新が止まる
  - 企業の管理ポリシーでサンドボックス化されたセッションが、その事実をタイムライン上に表示するようになった。`copilot app` と Ctrl+Space による音声ディクテーション切り替えも加わった
  - ⚠️ v1.0.81-2 / -3 / -4 の本文は3日連続で空のままで、`changelog.md` にも v1.0.81 系のエントリがない。安定版は v1.0.80（8/14）据え置きで8日間更新がない
- **Codex CLI の安定版 0.149.0 が出た**（8/20 21:04 UTC）: 8/18 の 0.148.0 以来の安定版更新で、内容が判明した初めての版でもある。`codex agents`（タスクの検索・開始・オープン・リネーム・停止を行う対話ダッシュボード）、`/cd` / `/pwd` / `/cwd` による作業ディレクトリ操作、`codex queue` によるローカル / リモートセッションへのメッセージ送信が加わった。`codex doctor` は endpoint protection・ネットワーク / プロキシ障害・デスクトップアプリ状態・更新到達性を診断するようになり、resume / fork したスレッドは元の permission profile を復元する。opt-in で MCP 2026-07-28 プロトコルにも対応した
  - pre-release は 8/20〜8/21 に5版刻まれたが、⚠️ いずれも本文は1行のみである
- **GitHub Code Quality の有効化変更が監査ログに載るようになった**（8/20）: `repo.code_quality_enabled` / `repo.code_quality_disabled` / `repo.code_quality_updated` の3イベントが追加され、対象リポジトリ・変更者・時刻を記録して監査ログ API から照会できる。Code Quality の課金は有効なリポジトリのアクティブコミッター数で数えるため、有効化の履歴がそのまま費用の説明材料になる。対象は GitHub Enterprise Cloud（data residency 版を含む）と GitHub Team
- **Code scanning に「Mitigated」の却下理由が追加された**（8/20）: 脆弱性はコードに残るが WAF やネットワークポリシー等の外部統制でリスクを抑えている場合に選べる却下理由で、「Won't fix」と区別して記録できる。⚠️ 対象プランの限定は告知に記載がなく、API・監査ログへの影響も明示されていない
- Cursor の changelog は 8/19 の Cloud Agents / Harness 更新が最上位のままで、8/20〜8/21 の追加がない。フォーラム Announcements も 8/17 の Origin Code Hosting が最上位のままである
- Devin は 8/15 の release notes が最新のままで、8/16〜8/21 の新規項目を二次でも確認できない。Slack Code のローンチパートナーには入っている（ハイライト3参照）

### Microsoft 365 Copilot / Copilot Studio

- 簡素化 Copilot UI の Outlook / Teams 展開はハイライト2を参照。
- **エンドユーザーが自分の資格情報で Jira / Confluence を接続できるようになる**: Roadmap に Feature ID **568788**（Self-serve sync connectors・`In development`・Desktop / Web）が 2026-08-20 に起票された。Preview 期日は 2026年8月、GA 期日は 2026年9月である。利用者自身の資格情報と権限で同期し、その人が既にアクセスできる内容だけを取り込む。同期した内容は Copilot Chat と Microsoft Search から引ける。管理者側には段階展開・表示の管理・コネクタの無効化がテナントレベルで残る。⚠️ 一次は Roadmap 項目だけで、Learn のページはまだ存在しない
- **Roadmap にチャット応答のインライン編集が2件起票された**: どちらも Desktop / Mobile・GA 期日は 2026年9月である。`569428` Writing Blocks は下書き・メモ・メールなどを Chat を使いながらインラインで編集・反復でき、`569429` Code Blocks はコード・グラフ・図をチャット内でインラインにプレビューできる（従来はコードキャンバスで左右に並べる形だった）
- **政府クラウドの MCP ウィジェットが `Rolling out` へ変わった**: `564608`（MCP ベースのエージェントがチャット内に対話的 UI ウィジェットを出せる機能）が 8/18 に `In development` から進んだ。対象は GCC / GCC High / DoD で、GA 期日は今月である
- **Copilot Studio の What's New は July 2026 節から増減していない**: 8月節も未作成である（Entra Agent ID の必須化 / ワークフロー・MCP サーバーのツール追加〔Preview〕/ MCP サーバーの Microsoft 認証申請〔Preview〕/ リアルタイムエージェントの digital messaging 対応 / 環境レベルのエージェントテレメトリ〔Preview〕/ 添付ファイルと生成ファイル〔Preview〕の6項目）
  - ⚠️ June 節の GitHub Copilot ハーネスは本日も `(Production-ready preview)` のままで、GA（8/3）から**19日連続**の未反映である。ページ本体は 8/20 に編集されているため、「更新を待てば直る」という説明は成り立たない
- **Copilot Agent Kit の August 2026 Update 1 を5日遅れで検知した**: Power CAT がタグ `CopilotStudioAccelerator-August2026.1` を 8/17 に公開していた。内容は Agent Review Tool のセットアップ不具合の修正で、セットアップウィザードから Agent Review インストーラーを開き、4つのチェックが Ready になってからツールを起動する手順に改められている
- Release Notes の最新セクションは「August 11, 2026」のままで、節構成7本・全12項目も 8/21 と一致する。次バッチは隔週傾向どおりなら 8/25 前後の見込みである
- Copilot Studio の Released Versions は Build **2026.6.3**（6/30 初出）のままで、空白が7週間と4日に達した。次の定例更新日は 8/25 である
- 拡張機能 What's New は July 2026 節のままで8月節が未作成、掲載2件（宣言型エージェント manifest 1.8、Copilot 利用状況レポート API 3種の `version` パラメーター）にも変化がない。モデル可用性一覧も 8/16 から変わらず、GPT-4o と Claude Sonnet 4.5 は全公開リージョンで Retired、既定は GPT-4.1、Claude Sonnet 5 は GitHub Copilot ハーネス限定で米国のみ提供である
- ⚠️ M365 Copilot Blog の board RSS は本日も投稿日の降順になっておらず、順序の乱れが9日連続で再現した。Tech Community の M365 Copilot Blog は 8/13、Microsoft 365 Blog 本体は 7/30、Copilot Studio Blog は 8/3 が最新のままである
- 期限: Copilot の既定モデル有効化ポリシー発効（**8/26**）、GitHub Spark 退役（**8/31**）、モデル廃止（**9/1**）、MAI-Code-1-Flash 廃止（**9/10**）

### Power Platform / ガバナンス

- **Release Wave の期日超過が延べ6行に達した**: GA 列は統合 Power Apps によるフォーム UI〔Jul〕/ code apps のコネクタ CLI 対応〔Jul〕/ FetchXML エディターでのオフラインプロファイル構成〔Jul〕/ カスタムブランドアプリのプッシュ通知〔Jun〕/ デスクトップ版 Power Automate の以前のプロンプト参照〔May〕の5件、Public preview 列は code apps のコネクタ CLI 対応〔Jun〕の1件である。8月に期日がある行は10件、9月は6件で、2026 Wave 1 の対象期間（4月〜9月）は残り約1か月となった
- ⚠️ **PPAC の Usage ページは GA 期日が今月なのに緑チェックが付いていない**: Public preview は 2026-02-13 で緑チェック済みだが、残り9日で GA 側に動きがない。Copilot Studio 側でも今月が GA 期日の `566997`（メーカー資格情報の使用ブロック）に緑の動きがない
- Copilot Studio の Roadmap を全件列挙したところ13件で、`modified` の最新は 8/19 起票の `569607`（評価体験の改善）のまま、状態変化も期日変更もなかった。`power-automate` / `power-apps` / `power-platform-governance-administration` の3ページも 8/21 と完全に同一である
- Power Platform Blog の親ページ先頭は 8/13 の PPCC 2026 登録記事のままで、8/6 公開の月次合併号は依然として一覧に現れない
- **Partner Center 8月アナウンスが 15件に増えた**: 6日間止まっていた月内追記が再開し、8/20 付で Dragon Copilot Physician apps and agents が加わった。パートナーが専用の Marketplace オファー種別で医療 AI アプリとエージェントを公開し、Dragon Copilot の体験内に直接埋め込める。提供地域は米国のみである
- ⚠️ **Microsoft Purview の7月節に未掲載の追記が見つかった**: ページの `updated_at` は 2026-08-21T07:32Z へ動いた一方、8月節は Sensitivity labels の2件から変わっていなかった。差分は7月節側にあり、これまで「7月節は3項目」と記録してきたのに対し本日は6分類・計16項目だった
  - Exchange Online の DLP ポリシーが、タイムアウトやスロットリングによる分類失敗を検知できるようになった〔Preview〕。管理者は `DocumentScanFailures` 条件で失敗の種類ごとに保護動作を変えられる
  - Priority cleanup ポリシーは、コンテンツを完全削除する前に3者の承認（Priority Cleanup 管理者・保持マネージャー・eDiscovery 管理者）を必須とするようになった
  - Purview のロールグループ割り当てに有効期限を設定し、権限を自動失効させられるようになった。期間は1日〜2年である
  - 自動ラベル付けの運用ドキュメントが6件更新され、シミュレーションが完全な dry run ではないことなどが明文化された

### OpenAI

- **OpenAI が ChatGPT に Apple Messages プラグインを追加した**（8/20〜8/21）: Apple silicon Mac の ChatGPT デスクトップアプリで iMessage / SMS / RCS の会話を読み・検索し、メッセージの作成と送信ができる。**全プラン対象**で、ChatGPT Work と Codex でも使える。⚠️ Intel Mac は対象外である
- **ChatGPT Sites / Codex / Work に 8/21 付けの更新が入った**: Sites は Plus / Pro のオーナーが既存サイトのホスト URL を再デプロイなしで変更でき、旧アドレスは新 URL へリダイレクトする。Codex は会話の読み取り専用スナップショットをリンクで共有できるようになった（ツール呼び出しとシェルの入出力は含まれない）。デスクトップと iOS の間でピン留めチャットが同期し、GitLab 連携が全プランで beta 提供に入った
- **API changelog に 8/20 の2件が加わった**: Prompt Caching ダッシュボード（キャッシュヒット率の推移、write あたりの read 数、cache-read / cache-write / uncached のトークン内訳をモデル別・サービスティア別に絞って見られる）と、`gpt-image-2` 系の透過背景対応（preview）である。⚠️ 8/13 の Ultrafast モードの課金レートは依然未確定である
- **OpenAI の公開 S-1 は本日も EDGAR に出ていない**: 6/8 に SEC へ機密扱いの草案を提出して以降、公開版は掲載されていない。ロードショー開始の15日以上前に登録届出書の公開が要るという SEC 規則からの逆算で8月下旬〜9月上旬の公開が見込まれているが、確定日程ではない。⚠️ 流通している評価額 $852B と財務値（月間売上 約$2B・売上1ドルあたり約1.22ドルの損失）はいずれも公開文書に基づかない
- `community.openai.com` の Announcements RSS は 8/18 の DevDay Exchange 告知が最上位のままである（応募締切 9/17・東京は 10/20）

### Google

- **Google が Ask Gemini in Chat を発表した**: Workspace Intelligence を基盤に、Google Chat 上で Gmail / Drive / カレンダーを横断検索し、会話から離れずに画像生成や更新文の作成ができる。ロールアウト開始は **8/26** で、機能が見えるまで最大15日かかる
  - ⚠️ プロモーション枠の高上限は **10/1 まで**である。それ以降は通常の上限に戻るため、試用の結論はこの期間内に出す必要がある
  - あわせて Sheets canvas（自然言語でスプレッドシートをインタラクティブアプリに変える機能）と、Gemini レポートダッシュボードでの Google Chat 利用状況メトリクスが公開された
  - ⚠️ 一次の `workspaceupdates.googleblog.com` はゲートウェイ拒否継続のため、WebSearch のスニペット経由で確定した
- Gemini API changelog は 8/13 の Gemini 3.7 Flash GA が最上位のままで、8/14〜8/21 の追加がない。**Gemini 3.5 Pro GA は未ローンチ継続**である（6月 → 7月 → 7/17 と3回スリップ）
- Hugging Face の `google` org は 8/19 の TIPS v1 6本が最新で、8/20〜8/21 の追加はない

### モデル・料金 / オープンウェイト

- **8/21〜8/22 に新規公開されたオープンウェイト LLM はない**: `Qwen` / `moonshotai` / `deepseek-ai` / `meta-models` / `mistralai` / `zai-org` / `openai` / `google` の計8 org で作成日降順一覧を実行し、8/13 の `Qwen/Qwen3.8-27B-FP8` と `deepseek-ai/DeepSeek-V4-Pro-0813` より新しいものが1件もないことを確認した
- 実測（8/22）: `Qwen/Qwen3.8-27B` は DL **1,726,651** / likes 11,912（前日 1,373,584）。`DeepSeek-V4-Pro-0813` は DL 49,601 / likes 702（前日 43,287）で、`DeepSeek-V4-Flash-0731` の DL 2,833,064 に対し **約57分の1**とダウンロードは Flash 側に偏り続けている
- Gemini API の単価は 8/21 分から変更がない。3.7 Flash と 3.6 Flash はともに入力 $0.75 / 出力 $3.75 の導入価格が継続し、**2027/1/1 以降は $1.50 / $7.50** になる。2.5 Pro（$1.25 / $10.00・200k 超は $2.50 / $15.00）以下の各モデルも据え置きである
- ⚠️ **DeepSeek の区分別の新単価は本日も一次で確定できていない**: `api-docs.deepseek.com` がゲートウェイ拒否のままで、8/16 16:00 UTC 発効の値上げについて確定単価を確認できない状態が6日続く。二次では V4-Pro の出力が peak $3.96 / off-peak $1.98 と報じられているが、提案資料に確定値として書かない
- GitHub Copilot のモデル構成に追加はなく、8/14 の Grok 4.6 追加以降エントリが出ていない。**MAI-Code-1-Flash の 9/10 退役は予定どおり有効**である。xAI 側も 8/19 の Grok 4.6 の Amazon Bedrock GA 以降、新規発表がない

### MCP

- MCP のブログ新着はない。RSS 最新は 7/28 の `The 2026-07-28 Specification` のままで**25日連続**で動きがない
- 実装側では Codex CLI が opt-in で MCP 2026-07-28 プロトコルに対応した。Copilot CLI 側は `forceRemoteSettingsRefresh` の fail-closed 化により、ポリシー未確定時に既定外 MCP サーバーをブロックする姿勢へ倒れる。Claude Code はプロジェクト由来のインライン MCP サーバーに trust ダイアログの承認を要求するようになった

### 企業・市場・国内

- **AWS の $1B フォワードデプロイ組織を53日遅れで捕捉した**: Amazon が **6/30** の AWS Summit Washington DC で発表していた。$1B を投じて AWS Forward Deployed Engineering 組織を立ち上げ、数千人の FDE を顧客チーム内に常駐させてエージェント型 AI システムを共同構築する。統括は frontier AI engineering and services 担当 VP の Francessca Vasquez である
  - 同日にパートナー向けの Partner-Led FDE も告知されており、コンサルティングパートナー内に AWS 認定のエンジニアチームを置き、ドメインオントロジー・評価フレームワーク・エージェント運用ツール群からなる再利用可能な harness をパートナー側の資産として残す
  - 07-17 収録の Anthropic「Ode」・Microsoft Frontier Company（7/2・$2.5B）と並び、競争軸が「モデル性能」から「導入を成功させる常駐体制」へ移る流れの3社目にあたる
  - ⚠️ **8/20〜8/21 に複数の二次媒体が一斉に記事化したため当日ニュースとして浮上したが、発表日は 6/30 である**
- **monday.com がプラットフォームをエージェント前提へ作り替えた**: 8/20 公開の Anthropic 事例記事で、250,000社超が使う作業管理プラットフォームを AI エージェントと人間が協働する構成へ組み替えたと説明した。内訳は Claude を使ったカスタムエージェント（monday Agents）、外部で作った Claude エージェントを持ち込む Bring Your Own Agent、Agents Store の既製エージェント、顧客環境でタスクを実行するコーディング連携の4つである。2026年5月のエージェント基盤ローンチ以降のエージェント対話は500万件に達した。⚠️ ROI・工数削減・コスト削減の定量値は記事になく、示されているのは導入社数と対話量だけである
- Slack がコーディングエージェントの共通配信面になる動きが出た（ハイライト3参照）。Anthropic・GitHub・Cognition・Vercel・OpenAI が同一プロダクトのローンチパートナーとして並んだ
- 国内の市場データに新規リリースはない。引用可能な基準値は IDC の2026年3月予測（国内 AI 市場支出額 2025年 2兆3,725億円 → 2029年 6兆8,897億円・CAGR 36.0%）と総務省 令和8年版情報通信白書（企業の生成AI業務利用 86.4%）のままで、MM総研の個人利用率も 2025年8月時点の 21.8%（1,597万人）から更新がない
- Qiita / Zenn で厳選掲載に値する新規記事は検出できなかった。⚠️ Copilot Credit の USD 単価とキャパシティパック価格を具体的に書く記事があるが、いずれも一次（Learn）に存在しない数値のため採用しない
- 既報: 下院民主党22名の監督書簡（回答期限 8/24）、OpenAI の CRO に Dali Rajic 就任報道（8/17）、OpenAI 9月にも $1T 超で株式売出し報道、Manus が Meta から分離（8/12）
- Apple は 8/18 の EU 向けビジネス条件変更2本が最上位のままで、AI 関連の最新は 8/5 の「Get ready for new creative assets on the App Store」である

## 直近の注目予定

- **8/22（本日）**: M365 Copilot アプリのチャット中心 UI（MC1325422）が Deferred リングへ展開
- **8/23**: PnP 週次 / Power CAT の定例確認 ／ Manus が Meta 買収後（2025-12-29 以降）のユーザーデータを削除開始（08:00 SGT・復元は 8/25 から）
- **8/24**: ChatGPT Ads が欧州31市場で開始 ／ Anthropic / OpenAI が下院民主党の監督書簡へ回答する期限 ／ MS-4005 / ppweekly の週次確認
- **8/25**: M365 Copilot Release Notes の次バッチ見込み ／ Copilot Studio Released Versions の定例更新日
- **8/26**: OpenAI Assistants API 廃止 / o3 退役 / GPT-4.5 完全廃止 ／ Copilot 既定モデル有効化ポリシー発効 ／ Ask Gemini in Chat のロールアウト開始
- **8/27**: 非推奨一覧の週次確認 ／ IT Nation Connect ANZ の Microsoft セッション
- **8/30**: 公式 DALL·E GPT の退役
- **8/31**: Claude Code の週次上限50%増が終了 ／ GitHub Spark の既存ユーザーアクセス終了 ／ `gemini-robotics-er-1.6-preview` 停止 ／ GPT-5.4・5.4 mini が Codex（ChatGPT サインイン）から除外 ／ Claude for Government の $1/機関プログラム終了 ／ Power Automate モバイルアプリの廃止
- **8月中**: PPAC Usage ページの GA 期日 ／ Roadmap `566997`（メーカー資格情報のブロック）と `564608`（政府クラウドの MCP ウィジェット）の GA 期日 ／ Anthropic が IPO を公開申請する可能性
- **9/1**: GitHub Copilot の全体験でモデル廃止 ／ OpenAI Daybreak 全アカウントでハードウェアセキュリティキー必須化 ／ MAICPP 契約更新条項の自動発効
- **9月**: 簡素化 Copilot 体験の Outlook / Teams 展開 ／ Self-serve sync connectors の GA ／ Writing Blocks・Code Blocks の GA ／ iOS 27 / macOS 27 GA ／ OpenAI の IPO 観測
- **9/10**: MAI-Code-1-Flash が全 Copilot 体験から廃止
- **9/17**: OpenAI DevDay Exchange の応募締切
- **10/1**: Apple の EU 向け新ビジネス条件が発効（Core Technology Commission へ移行）／ Ask Gemini in Chat のプロモーション上限が終了
- **10/16–11/11**: OpenAI DevDay Exchange 8都市（東京は **10/20**）
- **10月**: Anthropic の IPO 予定（$2T 超の評価額を目標と報道）
- **12/2**: EU AI Act の生成コンテンツ標識義務、8/2 以前に市場投入済みシステムへの猶予終了
- **12/31**: Gemini 3.7 Flash の導入価格終了（$0.75 / $3.75 → $1.50 / $7.50）

## 改善メモ

- **Master B-041 起票**: 一覧ページから個別記事へ進むとき、slug を推測せず一覧取得時に URL も同時に取得することを `fetch-flow.md` に規定した
- **Master B-024 追記（回数18）**: 同一日付ブロックの取りこぼしが同一 URL で3日連続・毎回別項目という形で再発した（8/19 の API リリースから 8/20 は Admin API のみ、8/21 は Files API / Agent Skills、本日 browser use / computer use を検出）。件数を先に問う手順を追加した
- **Copilot B-042 起票**: Purview の What's new を当月節だけで突合しており、過去月の節への追記を検知できていなかった。直近2か月分を全項目突合する運用へ変更する提案である
- **industry B-005 に新類型を追記**: 二次媒体の再掲載日が発表日として流通する類型を追加した（AWS の $1B FDE 組織を 8/21 付の複数記事が新規のように扱ったが、発表は 6/30）
- **industry B-008 の根拠を更新**: AWS FDE の53日遅れが取りこぼしの最長記録を更新した（従来は42日・GhostApproval）
- **ソース間の粒度差**: Claude Security の Mythos 5 移行は Master と industry の双方がハイライトに採ったが、有効化経路の記述が分かれた（Master は Claude.ai サイドバー / `claude.ai/security`、industry は管理者による admin console）。矛盾ではなく参照した一次の粒度差とみて両方を併記した
- **到達性の変化**: `pupuweb.com`（Message Center を扱う二次ブログ）と `www.ciodive.com` が新たにゲートウェイ拒否となった。`code.claude.com` は前日の不通から復旧した。Copilot 側のゲートウェイ拒否ホストは11本目に達している
- 継続提案は Master 21件（最多: B-013 403の2分類記録・25回目）、Copilot 24件（最多: B-011 Power Platform Blog のトピック記事照合・33回目）、industry 3件（最多: B-004 取得方法欄の WebSearch 優先化・54回目）
</content>
</invoke>
