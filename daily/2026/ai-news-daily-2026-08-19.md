# AI News Daily Summary — 2026-08-19

水曜は、昨日始まった Copilot アプリ統合の「消える側」が見えた日である。URL とアイコンの移行として記録していた 8/18 の変更には、Group Chat をスレッドごと恒久削除する機能廃止が3件付いていた。手元のツールでは Claude Code v2.1.234 が changelog に載り、上限リセット時の自動継続と Windows パス偽装の修正が同時に入っている。Claude Code の週次上限50%増は本日 23:59 PT で切れ、Copilot Tuning の停止は明日 8/20 に来る。OpenAI は DevDay を8都市へ分割し、東京を 10/20 に置いた。応募は 9/17 締切である。

## 今日のハイライト

### 1. 消費者向け Copilot の3機能が 8/18 に廃止された — Group Chat はスレッドごと恒久削除され、退避手段の案内が無い

**要点**: Copilot アプリ統合にあわせ Group Chat・Podcasts・Deep Research（消費者向け）が 8/18 に廃止された。前提が「統合は URL とアイコンの変更」から「消費者側の成果物が消える」へ変わる。Group Chat は復元できない。

**詳細**: Microsoft は消費者向け Copilot と商用 Copilot を1つの「Microsoft Copilot」アプリへ束ねる移行を 8/18 に開始した。Partner Center の 8/14 付告知（一次）が扱うのはアカウント判別の視覚指標・アプリ名とアイコンの簡素化・Web URL の `m365.cloud.microsoft` から `copilot.cloud.microsoft` への移行の3点で、セキュリティ・コンプライアンス・ガバナンスの制御に変更はないとされる。同じ 8/18 を期日とする機能廃止は告知の外側にあり、二次報道でのみ具体化している。

- Group Chat: スレッドと内部の画像が**恒久削除**される。退避手段の案内は無い
- Podcasts: 消費者向け Copilot アプリで廃止された。ライブラリの音声ファイルは個別ダウンロードでのみ退避できる
- Deep Research: 消費者向けで廃止された。保存済みレポートは 8/18 以降も残るが新規作成はできない。後継の Researcher は Microsoft 365 Premium の加入者のみが使える

Windows / Mac デスクトップ版の早期プレビューも 8/18 開始で、広範展開は9月中旬から始まる。プレビュー中はタスクバーの Ask Copilot が一時無効化され、Notebooks・Connectors・Vision が一時的に使えなくなる（Windows Insider リリースノート・version 152.0.4191.25）。

⚠️ **廃止対象は消費者向け Copilot であって M365 Copilot ではない**が、統合後は同一アプリの中で両者が同居するため、社内の利用者が個人アカウント側で作った Podcasts / Deep Research の成果物は退避の対象になる。

⚠️ 本サマリーは 08-17・08-18 に URL 移行だけを記録し、削除を伴う側を2日続けて落としていた。同じ 8/18 に効く変更が一次告知（Partner Center）と二次報道に分かれて載っており、一次だけを読むと削除の存在に気づけない。

- https://learn.microsoft.com/partner-center/announcements/2026-august#microsoft-copilot-app-update
- https://learn.microsoft.com/windows-insider/release-notes/apps/copilot-on-windows
- https://www.thurrott.com/a-i/microsoft-copilot-a-i/339475/microsoft-is-retiring-copilot-deep-research-and-podcasts
- https://www.techrepublic.com/article/news-microsoft-copilot-app-merger/

### 2. Claude Code v2.1.234 が上限リセット時の自動継続と Windows パス偽装の修正を入れた — 上限で人が張り付く前提が消える

**要点**: Anthropic が **v2.1.234** を公開し、利用上限で止まったセッションをリセット時刻に自動再開する挙動を既定で入れた。上限に当たったら人が戻って再開する前提が、放置して待てる前提へ変わる。NT 名前空間パスの拒否も5経路へ広がった。

**詳細**: v2.1.234 は npm publish が 8/17 18:19 UTC で、本日 `code.claude.com/docs/en/changelog` と `raw.githubusercontent.com` の CHANGELOG.md の2ソースに掲載を確認した。08-18 時点では npm の `next` にしか無く、本サマリーは「リリース済みとして扱わない」と記録していた版にあたる。自動継続は `/config` の「Continue automatically at usage limit」でオフにできる。

統制系の修正は前版 v2.1.233 の続きにあたる。

- NT 名前空間パス（`\??\`）の拒否範囲を、リモートファイル読み取り・セッション復元・CLAUDE.md の include・ワークフロースクリプト・ファイルアップロードの5経路へ広げた。事前承認で通るファイルアクセス経路を NTLM 資格情報の漏洩ベクタから塞ぐ位置づけである
- MCP 診断が解決済みシークレットを表示していた問題を修正した。スコープ衝突の警告は `${VAR}` の形のまま出し、接続失敗の詳細はサーバー origin のみを出す
- `strictKnownMarketplaces` がホスト不一致の SCP 形式 git ソースを受理していた問題を修正し、チャネルサーバーへ中継される権限プレビューを尊重するようにした

機能面の追加は次のとおりである。

- `CLAUDE_CODE_PROJECT_DIR_NAME`: セッションごとに設定ディレクトリを分けるホストが、プロジェクト別トランスクリプトディレクトリに短い名前を付けられる
- `DirectoryAdded`: `/add-dir` の後に発火するフックを設定できる
- `selection:clear`: アプリ内テキスト選択を解除するキーバインドを割り当てられる（agents ビューでも動く）
- GitLab の MR バッジがフッターとステータスラインに出る（GitLab リモート＋認証済み `glab` CLI が条件。draft / pending / green を表示）
- Remote Control 側は、スマホや claude.ai/code での effort 指定がターミナル・Desktop / VS Code ホストのセッションへ反映される。長時間セッションで auto mode がサンドボックス済みコマンドのネットワーク到達性を繰り返し再確認する問題も直った

⚠️ npm `dist-tags` は `{stable: 2.1.226, latest: 2.1.234, next: 2.1.235}`（本日実測）。`next` の **v2.1.235** は 8/18 18:24 UTC に publish 済みだが changelog にも GitHub releases にも載っておらず、changelog 未掲載版が配布経路へ先行する形の3例目になる。`stable` は 8/7 の 2.1.224 から2版進んだものの `latest` とは8版の差が残り、上記の NT 名前空間パス修正は stable 固定環境にまだ届いていない。

⚠️ **Claude Code の週次上限50%増は本日 8/19 23:59 PT で終了する**。延長の告知は本日時点で無い。5時間枠の 5/6 恒久倍化は影響を受けない。

- https://code.claude.com/docs/en/changelog
- https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md
- https://registry.npmjs.org/@anthropic-ai/claude-code

### 3. OpenAI が DevDay を8都市へ分割し、東京を 10/20 に置いた — 配信で追う前提から 9/17 までに応募する前提へ変わる

**要点**: OpenAI が DevDay Exchange として10月から8都市で開発者イベントを開き、**東京開催を 10/20** に設定した。定員は限定で、応募は **9/17** 締切である。配信で本編を追う前提から、期限内に現地枠へ応募する前提へ変わる。

**詳細**: 公式フォーラムの Announcements カテゴリ（8/18 17:59 UTC 投稿）で告知された一次情報である。開催日程は次のとおり。

- 10/16 Bengaluru ／ **10/20 Tokyo** ／ 10/22 Seoul
- 10/26 Berlin ／ 10/28 Paris ／ 11/3 London
- 11/6 São Paulo ／ 11/11 Mexico City

内容は「ビルドノートの交換・実プロジェクトの共有・OpenAI のツールを作っているチームとの面会」と説明されており、従来の単一開催・基調講演型とは組み立てが違う。応募窓口は `events.openai.com` である。

- https://community.openai.com/t/openai-devday-is-going-global/1391106

## カテゴリ別まとめ

### Anthropic / Claude

- Claude Code の最新公開版が **v2.1.234** になった（ハイライト2参照）。v2.1.230 は欠番のままである
- Claude Code の週次上限50%増が本日 23:59 PT で終了する（ハイライト2参照）
- Anthropic が自社の CI/CD 障害対応を Claude Tag に一次対応させている事例を 8/18 に公開した。検知 → トリアージ → 解決 → 検証の4段で回し、**最初の分析レポートまで中央値14分**、最速の根本原因特定は4分、テスト欠落の調査では検証開始から3分で44件を解消したとしている。直近のインシデントで最初の状況報告は「いずれも Claude が書いた」と記載されている
  - トリアージでは複数の executor エージェントが並行して Grafana・ログストア・GitHub を当たり、解決は feature flag 経由の段階デプロイと PR 形式の修正提案で行う。検証後はポストモーテムと週次サマリーまで生成する
  - 構成は Grafana・ログ・PagerDuty・GitHub・Kubernetes の MCP コネクタと Claude Code Remote で、導入は「数日ではなく数時間」とされる。前提として Claude Team または Claude Enterprise の契約が要る
  - ⚠️ 削減額・工数の絶対値と、比較対象になる従来の初報時間は記事に無い。背景として同社のエンジニアは2021〜2025年比で四半期あたり8倍のコードを出しているとする
  - https://claude.com/blog/ai-ci-cd-on-call
- Anthropic が Claude Science のプロダクトガイドを 8/18 に公開した。ライフサイエンス向けの AI ワークベンチで、**ローカルの daemon がデータと計算を手元に置いたまま**、重い処理だけを GPU・SLURM クラスタ・クラウドアカウントへ投げる構成をとる。Chat / Cowork / Claude Code / Microsoft 365 との連携、データベースコネクタ、ライフサイエンス向けスキルを備え、導入は Foundation → Pilot → Scale の3段で示される。導入先として Novo Nordisk・Garvan Institute・Benchling を挙げる。新製品の発表ではなくガイドの公開で、製品自体は beta が継続する
  - 記事が引く調査値は、バイオ医薬・医療機器の経営層の 78% が AI による大きな変化を見込み、科学者の 91% がさらなる AI 活用を望む一方、79% が信頼性を最大の障壁に挙げ、日常業務に完全に組み込めているのは 14% にとどまるというもの。⚠️ 価格は未公表で、調査の出典・標本数は記事に明示されていない
  - https://claude.com/blog/the-claude-science-product-guide
- Claude API のリリースノートは **8/11** の Compliance API ローカルセッション対応が最上位のままで、8/12〜8/18 の追加はない。`support.claude.com` の Release Notes も 8/6 の skill / plugin セキュリティスキャン beta が最上位のままで、13日連続で動きがない
- `www.anthropic.com` はオリジン403が続いており、01 は規定の検索5本＋日付入り1本を全て実行したうえで 8/18 付けの新規製品発表を検出していない
- 研究助成は新規なし（AI for Science 希少疾患グラントは 8/2 締切済み、Claude Science は 7/15 締切済み、Fellows 11月コホートは 7/26 締切済み）
- 既報: 下院民主党22名の監督書簡（回答期限 **8/24**）、August 2026 Risk Report（8/14）、8/16 の約36分の認証障害、ABC Legal の Managed Agents 導入事例（8/17）

### Copilot Studio / Power Platform

- Copilot Tuning の停止期限は明日 **8/20** だが、Learn の一次ページは注記なしで Optimization テンプレートを現行機能として載せ続けている。本日 `copilot-tuning-overview` を再取得しても停止も退役も書かれていなかった。⚠️ 一次が期限を告げないまま当日を迎える状態で、一次だけを読むと退役予定の機能で着手してしまう
  - 「サポートされるシナリオ」節に Optimization エージェントの項が残り、テンプレート選択表でも「制約付きの割り当て・計画問題を解く」用途として現行扱いのまま載っている
  - 冒頭の Important ノートは「Frontier 経由の提供は 2026年4月予定」という4か月半前の記述で止まっている
  - 告知内容（既報）: 8/20 までに完了していない進行中のモデル調整実行は破棄され、Optimization テンプレートは退役する。既存エージェントとファインチューニング済みモデルを使うエージェントは動作を継続し、自動移行はない。再開は Public Preview が 2026年9月・GA が 2026年12月である
  - ⚠️ `mc.merill.net` は **12日連続**でゲートウェイ拒否を返し、MC1454393 の本文は検索インデックスのスニペットでしか読めない。MC を扱う二次ブログ2本も本日あらためて同じ拒否を返した
  - ⚠️ 8/17・8/18 に出典として書いた `learn.microsoft.com/en-us/microsoft-365-copilot/copilot-tuning-overview` は `.../microsoft-365/copilot/copilot-tuning-overview` へ **HTTP 301** で恒久リダイレクトしている。ページ本体は生きているため取得障害ではなく、出典 URL の陳腐化である
  - https://learn.microsoft.com/en-us/microsoft-365/copilot/copilot-tuning-overview
- Release Wave の「ガバナンス・管理」ページを本日はじめて一次取得したところ、掲載12行のうち掲載歴があるものが1行も無かった。これまで `power-automate` と `power-apps` の2ページだけを毎日照合しており、Copilot Studio と管理者統制を扱う3ページ目が丸ごと監視外にあった（02 が **B-038** として起票）
  - Usage ページ（PPAC）: Public preview が 2026-02-13〔緑チェック済み〕で、**GA 期日は今月**である。Copilot Studio のエージェントセッション数を、Power Apps のアクティブユーザー数・Power Automate のフロー実行数と同じ画面で追える
  - エージェントセキュリティの管理者制御強化: Public preview が 2026-05-31〔緑チェック済み〕で、GA 期日は9月である
  - 既定環境からのアプリ移動: Public preview が 2026-01-30〔緑チェック済み〕で、GA 期日は9月である
  - 運用状態の異常検知とソースコード統合の GitHub 対応は、どちらも Public preview の期日が8月で緑チェックがまだ付いていない
  - 期日超過は4行ある（Agentic Center of Enablement〔Preview・Jul〕、Copilot Studio の秘密度ラベル表示〔GA・Jun〕、コネクタの秘密度ラベル表示〔GA・Jun〕、環境へのゲストアクセス許可/拒否〔GA・May〕）
  - ⚠️ 本ページの `updated_at` は 2026-07-23T15:20Z で、毎日照合している2ページ（8/12 更新）より3週間古い。緑チェックの状態を2ページ分の照合結果で代表させることはできない
  - https://learn.microsoft.com/en-us/power-platform/release-plan/2026wave1/power-platform-governance-administration/planned-features
- PPAC の Usage ページ（Preview）では、管理者が Power Apps / Power Automate / Copilot Studio の利用状況を1画面で追えるようになった。表示は直近28日の集計で、アダプション推移・製品別の使用量・高価値リソース上位3件が並ぶ。Copilot Studio の表はエージェントセッション数で、対象は Copilot Studio（フル）で作られたエージェントに限られる。閲覧には Power Platform 管理者ロールが要り、リージョンごとに順次展開中である。⚠️ 2025-12-25〜2026-01-03 の Power Automate / Copilot Studio のデータは不正確な場合があると既知の問題に明記されている。Copilot ハブ側のエージェントセッション数と食い違うのは本ページが28日のルックバック窓を使うためで、指標は将来統一予定とされる
  - https://learn.microsoft.com/en-us/power-platform/admin/usage
- Copilot Studio の What's New は節構成が June 2026 のままで、7月節も8月節も公開されていない。June 節の10項目にも増減はない。⚠️ 新エージェント体験（GitHub Copilot ハーネス）の項が `(Production-ready preview)` のままで、8/3 の GA から**16日連続**で反映されていない
- Copilot Studio の Released Versions に新ビルドは出ておらず、Build は **2026.6.3**（6/30 初出）のままで空白が7週間と1日に達した。リージョン分布（11 / 5 / 3 の3段）も UX 版 26.06.21-24 も据え置きである
- Release Wave の `power-automate` / `power-apps` は 8/18 と完全に同一で、緑チェックの追加・期日変更・行の増減はいずれも発生していない。期日超過は延べ6行（GA 列5件・Public preview 列1件）、8月期日は10件、9月期日は6件のままである。2026 Wave 1 の対象期間は9月末までで残り約1か月半になる
- 非推奨一覧に新規項目は追加されておらず、先頭は Power Automate モバイルアプリの廃止（**2026-08-31** 発効・残り12日）のままである。⚠️ ページの `updated_at` が 7/27 から 2026-08-14 へ動いていたが、項目の増減が伴わないため差分は特定できていない。Fluent UI (v8) コントロールの非推奨が本ページに載っていない状態も続く
- Power Platform Blog / Power Automate Blog / Power Apps Blog は3ページとも先頭が 8/13 の PPCC 2026 登録記事のままで、本日の新規はない。8/6 公開の月次合併号が一覧に現れない不完全レンダリングも継続している

### Microsoft 365 Copilot / パートナー

- 消費者向け Copilot の3機能が 8/18 に廃止された（ハイライト1参照）
- M365 Copilot Release Notes は **August 11, 2026** が最新セクションのままで、本日の新バッチはない。対象期間 7/28〜8/11・全12項目・節構成7本（extensibility 2 / SharePoint 1 / Outlook 2 / Microsoft 365 Copilot 1 / PowerPoint 4 / Viva Insights 1 / Word 1）が 8/18 と一致した。次バッチは隔週傾向どおりなら 8/25 前後の見込みである
- M365 Roadmap の Latest announcements の先頭が **7/24 の「Available today: Anthropic's Claude Opus 5 in Microsoft 365 Copilot」**だったことを本日確認した。⚠️ 02 は 8/2 以降6回にわたり「7/9 の GPT-5.6 が最新のまま」と記録しており、先頭項目を落とし続けていた（**B-039** 起票）。当該記事自体は Microsoft Copilot Blog 経由で 2026-07-25 の digest に掲載済みのためニュースの取りこぼしは無いが、「Roadmap に新規なし」という毎日の判定が誤りだった
- 二次の「セッション共有の GA」は採用しない。チャットセッションと個別応答を読み取り専用リンクで共有する機能が「8月に GA」とする二次記事があるが、August 11 バッチにも過去バッチにも該当項目が無く一次で裏が取れていない
- Partner Center の8月アナウンスは 8/14 付の14件目までで、**4日連続**で追記がない（`updated_at` 2026-08-14T16:04Z）。既報の内容（MAICPP 契約更新条項の 9/1 自動発効、Frontier Partner バッジの 2027年6月末廃止、7/31 付の3スペシャライゼーション統合、7/30 発効の資格差し替え、CSP ソフトウェアの5%上乗せ〔10/1〕、M365 E7 プロモーションの 10/1 新規取引停止）にも変化はない
- Microsoft Purview の8月節は Sensitivity labels の2件のままで、Copilot 固有の項目は含まれていない（`updated_at` 2026-08-14T07:32Z）
- Tech Community の各ブログはいずれも本日の新規がない（M365 Copilot Blog 8/13、Copilot Studio Blog 8/3、SharePoint Blog 8/6、Agent 365 Blog 8/6、M365 Developer Blog 8/13、Microsoft Copilot Blog 7/21、M365 Blog 本体 7/30）。⚠️ board RSS の並び順の乱れは**6日連続**で再現している

### GitHub Copilot / 開発ツール

- GitHub が Copilot CLI の pre-release **v1.0.81-1** を 8/18 18:30 UTC に公開した。Gemini 3.7 Flash に対応し、エージェント別の使用量メトリクスが JSON 出力に加わった
  - `/sandbox` で `Ctrl+E` を押すと `settings.json` をエディタで開ける。スケジュールマネージャーでは `x` キーから `/every` と `/after` のプロンプトを削除できる
  - 修正は、ACP クライアントで allow-all を無効化する際の権限処理、ツール呼び出し失敗時のラベル重複、プラグイン提供のエージェント / スキル / MCP サーバーが非対話実行で削除される問題、`$` 入力で対話シェルが再度開く問題、foot / alacritty など複数ターミナルの表示である
  - 安定版は **v1.0.80**（8/14 02:28 UTC）で据え置かれており、8/15〜8/18 の安定版リリースはない
  - https://github.com/github/copilot-cli/releases/tag/v1.0.81-1
- `github.blog/changelog/label/copilot/` は 8/14 の Grok 4.6 提供開始が最上位のままで、8/15〜8/18 の追加はない
- Copilot Autofix が co-author として入ったコミット由来の脆弱性を、別の AI エージェントが5日で悪用した事例が報じられた。対象は `snowflakedb/snowflake-connector-net` の GitHub Actions ワークフローで、**6/18 に PR #1218 が merge** され、**6/23 に Wiz の Red Agent** が公開リポジトリの定期スキャン中に検出している。攻撃は認証不要で、細工した題名の Issue を立てるだけで Actions ランナー上の任意コマンド実行に至る。Wiz は取得したトークンで `snowflakecomputing.atlassian.net` へ認証し、エンジニアリング・セキュリティコンプライアンス・バグバウンティの各プロジェクトを読み取れる状態を確認した。Snowflake は HackerOne 経由の報告を受けて 6/23 に修正している
  - ⚠️ Copilot の関与について当事者の見解が割れている。Wiz 側は当該コミットが既存のサニタイズ済み入力パターンを削除して `run:` ブロックでのシェル変数展開に置き換えたとし、GitHub 側は社内レビューの結果として脆弱性につながった変更は人間が書いたもので Copilot の関与もレビューも無いと否認している
  - どちらの主張を採っても、AI が関与しうるコード変更経路に静的解析と人間のレビューを残すという運用上の結論は変わらない。同型の入口（Issue 題名を `run:` に展開する Actions ワークフロー）は既知の古典的パターンであり、書き手が誰かを問わず検出できる
  - https://www.wiz.io/blog/red-agent-snowflake-copilot-cicd-bug
  - https://www.theregister.com/security/2026/08/17/an-ai-broke-snowflakes-code-then-another-ai-agent-exploited-it/5288666
- Cursor の changelog は 8/17 の Origin Code Hosting が最上位のままで、8/18 の追加はない（RSS 実測 200 / item 50件）。フォーラムの Announcements も同じ Origin（8/17 17:42 UTC）が最新である
- Devin は 8/14 の Devin Coach が最新のままで、8/15〜8/18 の新規項目は二次でも確認できなかった。⚠️ `docs.devin.ai` はゲートウェイ拒否が続き一次未確認である
- 期限: Copilot 既定モデル有効化ポリシー発効（**8/26**）、GitHub Spark 退役（**8/31**）、モデル廃止（**9/1**）、MAI-Code-1-Flash 廃止（**9/10**）

### OpenAI

- OpenAI が DevDay Exchange を8都市で開催すると 8/18 に告知した（ハイライト3参照）。応募期限は **9/17** である
- OpenAI が13〜17歳向けの ChatGPT for Teens を 8/18 に展開し、**年齢推定で18歳未満と判定したアカウントも自動で**同じ体験へ入れるようにした。制限が強まるのは性的・ロマンチックなロールプレイ、露骨な暴力、自傷、摂食障害、危険行為で、長時間利用には休憩を促すリマインダーが挟まる。学習側には Study Mode への誘導・宿題の丸投げを抑える挙動・クイズと学習ビジュアル・学習時間の設定が入った。保護者はアカウントを連携すると Quiet Hours などの設定を管理でき、急性の苦痛を検知した高リスク時に通知を受け取る
  - ⚠️ **年齢推定は全利用者に掛かる仕組み**であり、法人契約の利用者が誤判定を受けた場合の扱いは告知の範囲では確認できていない
  - ⚠️ 01 は `openai.com/index/building-more-helpful-chatgpt-experiences-for-everyone/` が HTTP 403 で一次未到達のため二次一致で採り、03 は `openai.com/index/chatgpt-for-teens/` を出典に挙げている。掲載日 8/18 と内容は両者で一致する
  - https://www.axios.com/2026/08/18/openai-chatgpt-for-teens
  - https://techcrunch.com/2026/08/18/openai-launches-a-safer-chatgpt-for-teens-years-after-teens-started-using-it/
- ChatGPT Work と Codex 向けの教育プラグイン3本を確認した。いずれも自分のコース教材・接続済みツール・機関が承認したアプリを対象に動き、提供経路は ChatGPT Edu と ChatGPT for Teachers の学区展開である。⚠️ `learn.chatgpt.com` はゲートウェイ拒否のため WebSearch 経由で、掲載日は確定できていない
  - College Student: 学習中の教材からスタディガイド・練習クイズ・フラッシュカード・対話的な解説を作る
  - College Educator: シラバス・教材・評価課題・LMS 向けコンテンツを含む学習リソースを作る
  - K–12 Educator: 授業計画・教室用リソース・学習者別の教材調整・対話的なビジュアルを作る
- Codex CLI の pre-release は **0.148.0-alpha.22**（8/18 13:30 UTC）が最新で、8/17 に alpha.21 も出ている。安定版は 0.147.0（8/7 01:41 UTC）据え置きで**12日間**更新がない。⚠️ リリース本文は各版とも空で、変更内容は GitHub releases からは読めない
- `developers.openai.com/api/docs/changelog` は 8/13 の Ultrafast モードが最上位のままである。⚠️ 課金レートは依然として未確定である
- 到達性は前日から変わらない。`community.openai.com`（RSS）と `developers.openai.com/api/docs/changelog` は 200 で、`openai.com` / `help.openai.com` / `platform.openai.com` はオリジン403、`learn.chatgpt.com` はゲートウェイ拒否が継続している
- 既報: GPT-5.4 / 5.4 mini の **8/31** Codex 除外（代替は `gpt-5.6-terra` / `gpt-5.6-luna`）、ChatGPT Voice のアップロード済みファイルと Projects 対応、Computer History（8/13）、Linux デスクトップアプリ public preview（8/11）

### Google / DeepMind

- Gemini API の changelog は 8/13 の Gemini 3.7 Flash GA が最上位のままで、8/14〜8/18 の追加はない
- Imagen 4.0 系3本の停止日が一次で確定した。`ai.google.dev/gemini-api/docs/deprecations` は `imagen-4.0-generate-001` / `imagen-4.0-ultra-generate-001` / `imagen-4.0-fast-generate-001` の停止日を **2026-08-17** と記載し、推奨代替を `gemini-3.1-flash-image` としている。⚠️ ページの最終更新は 2026-08-13 UTC で、停止が実施済みかどうかの記載はない
- Gemini API の単価は据え置きで、Google は**17日連続**で一次料金ページを更新していない。3.7 Flash と 3.6 Flash はいずれも入力 $0.75 / 出力 $3.75 の導入価格が 2026年12月31日まで続き、2027年1月1日以降は $1.50 / $7.50 になる。3.5 Flash（$1.50 / $9.00）・3.5 Flash-Lite（$0.30 / $2.50）も変更はない
- Gemini 3.5 Pro は未 GA が継続している（I/O 発表後 6月 → 7月 → 7/17 と3回スリップ）
- ⚠️ `ai.google.dev/gemini-api/docs/changelog` が 01 の `daily-sources.md` に未登録のままで、登録済み Google 系5ソースはゲートウェイ拒否が続く。登録ソースだけを回すと Google のモデル発表は一次で1件も取れない

### モデル・料金 / オープンウェイト

- 8/14〜8/18 に新規公開されたオープンウェイトモデルはない。`Qwen` / `moonshotai` / `deepseek-ai` / `meta-models` / `mistralai` / `zai-org` / `openai` / `google` の計8 org で作成日降順一覧を実行し、8/13 の `Qwen/Qwen3.8-27B-FP8` と `deepseek-ai/DeepSeek-V4-Pro-0813` より新しいリポジトリが1件も無いことを確認した
  - 実測（8/19）: `Qwen/Qwen3.8-27B` は DL **665,513** / likes 11,067（前日 415,039 / 10,643）、FP8 版は DL 741,011 / likes 557。`deepseek-ai/DeepSeek-V4-Pro-0813` は DL 30,985 / likes 597。`meta-models/Muse-Glimmer-30B` は DL 384,097 / likes 1,675
- 撤回済みの Sonnet 5 値上げが料金アグリゲータで流通している。複数の価格比較サイトが本日時点でも「導入価格は 8月31日まで、以後 $3 / $15 へ戻る」と記載しているが、Anthropic は 8/10 のリリースノートで 9/1 の引き上げを実施しないと明記済みで、これらの記載は誤りである。⚠️ 提案書の単価はアグリゲータではなく `platform.claude.com` の Pricing ページから引く
  - https://platform.claude.com/docs/en/release-notes/api
- DeepSeek の一次料金表には本日も到達できない。`api-docs.deepseek.com` のゲートウェイ拒否が継続しており、8/17 に発効した値上げの課金区分別倍率は依然として二次報道の突き合わせにとどまる
- xAI は一次に到達できない状態が続いている。`x.ai` / `docs.x.ai` に加え、本日新たに `grok.com` もゲートウェイ拒否と判定した（`curl` exit 56）。8/18 の新規発表は二次でも確認できず、既報は Grok 4.6（8/12・入力 $2 / キャッシュ $0.50 / 出力 $6、Fast は $4 / $1 / $12）である
- 既報: DeepSeek Harness v0.1.0-rc.7（8/17・MIT・developer preview）、Meta の Muse Code / Muse Spark 1.2（8/5）、Qwen3.8-Max（8/8）、Kimi K3

### MCP

- MCP ブログに新着はなく、RSS 最新は 7/28 の `The 2026-07-28 Specification` のままで**22日連続**で動きがない
- 仕様 `2026-07-28` の内容は、ステートレス化（`initialize`/`initialized` ハンドシェイクと `Mcp-Session-Id` を廃止）、Multi Round-Trip Requests、`Mcp-Method`/`Mcp-Name` ヘッダによるルーティング、`ttlMs`/`cacheScope` による一覧キャッシュ、RFC 9207 issuer 検証必須化と DCR → CIMD 移行である
- Tier 1 SDK は変化がない（TypeScript `@modelcontextprotocol/server` / `client` ともに 2.0.0 ／ Python `mcp` 2.0.0 ／ C# v2.0 ／ Go は v2 未発行で `go-sdk` v1.7.0 が仕様対応）
- 実装側では Claude Code v2.1.234 が MCP 診断のシークレット漏れを修正した（ハイライト2参照）

### 企業・市場・国内

- Anthropic の年換算売上が **$65B** を超えたと 8/17〜8/18 に報じられた（出所は Bloomberg で、同社の公式発表ではない）。7月末時点のラン レートで、2025年末の約 $9B から7倍超にあたる。4月に $30B、5月に $47B を通過したとされ、投資家は年末に $100B〜$120B を見込むと伝えられている。IPO は秋にも実施の見通しで、想定評価額は $2T 超とされる（6月の SpaceX の $1.77T を超えれば史上最大の IPO になる）
- Groq が $350M を調達し、評価額はピークの半分になった（8/17 発表）。Series A として $350M を調達し評価額は **$3.5B** で、昨年9月のピーク $6.9B から半減した水準にあたる。減価の起点は Nvidia とのライセンス契約と、創業 CEO の Jonathan Ross を含む人材の引き抜きである。リードは投資会社 Disruptive で Nvidia も参加予定とされる。6月に $650M を調達した直後で、2カ月弱で計 $1B を集めたことになる。事業は AI チップの自社設計から neocloud へ軸を移している
  - https://techcrunch.com/2026/08/17/groq-raises-350m-to-fuel-its-pivot-from-ai-chips-to-neocloud/
- Baidu の Q2 で GPU クラウドが前年同期比 **283%増**となった（8/18 発表）。AI クラウドインフラの売上は RMB 73億（+50%）で、うち GPU クラウドは +283% と前四半期の +184% から加速した。AI 中核事業全体は RMB 125億（+25%）である。一方で全社売上は RMB 313億で前年同期比 4%減、オンライン広告は RMB 131億で 19%減となった。⚠️ AI の伸びが広告の減少を補いきれておらず、「AI へ転換した中国大手は増収」という単純化は成り立たない
  - https://infotechlead.com/cloud/baidu-q2-2026-ai-business-revenue-jumps-25-to-rmb-12-5-billion-as-gpu-cloud-surges-283-97831
- OpenAI の公開 S-1 は本日時点でも EDGAR に出ていない。6/8 に SEC へ機密扱いの草案を提出済みで、公開版の目論見書は8月中旬〜下旬の掲載が見込まれるとされる。上場時期は9月または2026年 Q4 が目標で、2027年へずれる可能性も報じられている。⚠️ 流通している評価額（直近ラウンドの $852B・上場時に狙うとされる $1T 超）と財務値（月間売上 約 $2B）はいずれも公開文書に基づかないため、提案資料に確定値として引かない
- AI 店長が人間の従業員の契約終了を判断した事例が報じられた。Andon Labs がサンフランシスコで運営する実験店舗 Andon Market で、AI 店長 Luna が23シフト中17回の遅刻を理由に判断している。⚠️ 自律的な判断ではなく、Luna は自身の勤怠ポリシーを数カ月見失っており、人間の監督者から就業規則を確認するよう促されてはじめて解雇を提案した。⚠️ 稼働モデルの記述が割れており、二次報道は Claude Sonnet 4.6 とする一方 Andon Labs 自身の投稿は Claude Opus 4.8 としている（後者を採る）。エージェントに人事判断の権限を渡すときは、ポリシーの保持と定期的な再読み込みを構成側で担保する必要がある
  - https://time.com/article/2026/08/14/claude-fired-worker-ai-job-disruption/
- Apple が EU 向けのビジネス条件変更2本を 8/18 に公開した。Core Technology Fee を廃止してデジタル取引の5%を課す Core Technology Commission に置き換え、Initial Acquisition Fee と Store Services Fee を廃止する。あわせて Apple Developer Program License Agreement に Attachment 14 が追加された。発効は **2026-10-01** である。⚠️ AI 関連の内容ではない
- 国内の市場データ定点は新規リリースがない。引用可能な基準値は IDC の2026年3月予測（国内 AI 市場支出額 2025年 2兆3,725億円 → 2029年 6兆8,897億円・CAGR 36.0%）、総務省 令和8年版情報通信白書（企業の生成AI業務利用 86.4%）、MM総研の個人利用率 21.8%（2025年8月時点・利用者数1,597万人）のままである
- 既報: Manus が Meta から分離（8/12 買収解消）、Decart AI 買収交渉の報道（8/13・成立していない）、下院民主党22名の監督書簡（回答期限 **8/24**）

## 直近の注目予定

- **8/19（本日）**: Claude Code の週次上限50%増が終了（23:59 PT）
- **8/20**: **Copilot Tuning の停止期限（未完了の調整実行は破棄・カテゴリ参照）** ／ Gemini Enterprise Agent Platform の Grok 4.1 ファミリー停止（一次未確認） ／ Pixel 11 系の出荷開始 ／ Copilot Studio Release Wave の週次確認
- **8/22**: M365 Copilot アプリのチャット中心 UI が Deferred リングへ展開開始（MC1325422）
- **8/23**: PnP・Power CAT・拡張機能 What's New・モデル可用性一覧の週次確認
- **8/23–24**: Manus が Meta 買収後（2025-12-29 以降）のユーザーデータを削除（8/23 08:00 SGT 開始・復元は 8/25 から）
- **8/24**: **Anthropic / OpenAI が下院民主党の監督書簡へ回答する期限** ／ MS-4005・Power Platform Weekly の週次確認 ／ 01 の週次復旧チェック
- **8/25 前後**: M365 Copilot Release Notes の次バッチ（隔週サイクルどおりなら） ／ 8/25 に Copilot Studio 課金ドキュメントの週次確認
- **8/26**: OpenAI Assistants API 廃止 / o3 退役 / GPT-4.5 完全廃止 ／ Copilot 既定モデル有効化ポリシー発効
- **8/27**: IT Nation Connect ANZ の Microsoft セッション
- **8/30**: 公式 DALL·E GPT の退役
- **8/31**: GitHub Spark の既存ユーザーアクセス終了 ／ `gemini-robotics-er-1.6-preview` 停止 ／ GPT-5.4・5.4 mini が Codex から除外 ／ Claude for Government の $1/機関プログラム終了 ／ Power Automate モバイルアプリ廃止 ／ CSP Copilot Partner Council コンテストの応募期限
- **8月下旬**: Planner Agent チャットの基本プラン展開開始（MC1443514） ／ スペシャライゼーション監査の Partner Center からの取り下げ対応
- **8月中**: Release Wave の8月期日10件と持ち越し6行 ／ PPAC Usage ページの GA ／ Word の Legal Agent GA〔二次のみ〕 ／ Copilot in 30 の顧客向け評価ツール
- **9/1**: GitHub Copilot の全体験でモデル廃止 ／ OpenAI Daybreak で全アカウントにハードウェアセキュリティキー必須化 ／ MAICPP 契約の更新条項が自動発効
- **9/2〜9/3**: Windows 365 Frontline 名称での購入最終日（9/2）と Windows 365 Flex への改称（9/3）
- **9/10**: MAI-Code-1-Flash が全 Copilot 体験から廃止
- **9/17**: **OpenAI DevDay Exchange の応募締切**
- **9 月**: Copilot Tuning の新体験が Public Preview ／ ガバナンス Release Wave の9月期日2件（既定環境からのアプリ移動 GA、エージェントセキュリティの管理者制御強化 GA） ／ iOS 27 / macOS 27 GA ／ 9月中旬に Copilot デスクトップアプリの広範な展開開始 ／ 9月末に 2026 Wave 1 の対象期間終了 ／ 9/30 に M365 E7 プロモーションの対象購入最終日と M365 E5・E3 の CSP 割引終了 ／ OpenAI の IPO 観測
- **10/1**: Apple の EU 向け新ビジネス条件が発効（Core Technology Commission へ移行） ／ M365 E7 プロモーションの新規取引停止 ／ CSP ソフトウェアの5%上乗せ発効
- **10/16–11/11**: OpenAI DevDay Exchange 8都市（**東京は 10/20**）
- **10 月**: Anthropic の IPO 予定（$2T 超の評価額を目標と報道） ／ 10/20〜22 に SMB Copilot Partner Council（NYC） ／ 10/25〜30 に PPCC 2026 本編とワークショップ
- **11/1**: パートナー特典の有効期限がオファー購入日基準へ移行
- **12/2**: EU AI Act の生成コンテンツ標識義務、8/2 以前に市場投入済みシステムへの猶予終了
- **12 月**: Copilot Tuning の新体験が GA ／ 12/31 に Gemini 3.6 Flash / 3.7 Flash の導入価格終了（$0.75 / $3.75 → $1.50 / $7.50）と M365 E3 プロモーション・Copilot in 30・Purview Suite 50%オフの提供終了
- **2027年6月末**: Frontier Partner バッジの廃止
- **2027年7月**: 退役資格の有効期限（2026-07-30 発効分）

## 改善メモ

- 本サマリー自身の見落としが1件確定した。8/18 の Copilot アプリ統合について、08-17・08-18 は URL 移行とデスクトップ早期プレビューだけを記録し、同じ日に効く機能廃止3件（うち Group Chat は恒久削除）を落としていた。一次告知（Partner Center）と二次報道で扱う範囲が分かれる型で、03 が B-008 / B-024 の根拠に追加している
- 監視漏れの新規起票が2件ある。02 が B-038（Release Wave の「ガバナンス・管理」ページが未登録で、Copilot Studio の統制機能12行が監視外）と B-039（M365 Roadmap の Latest announcements を要約取得しており、先頭項目を6回連続で落としていた）を起票した。どちらも「見ているつもりで見ていなかった」型で、B-039 は毎日の「新規なし」判定そのものが誤りだったことになる
- ソース間で扱いが割れた項目が1件ある。Imagen 4.0 系3本の 8/17 停止について、01 は deprecations ページで停止日 2026-08-17 を一次確認したうえで「実施済みかは未記載」と留保し、03 は料金ページの退役一覧で「Imagen 4（8/17 停止）」を確定として扱っている。参照ページが違うだけで矛盾ではないが、どのページを退役の一次とするかの定義は前日から未解決のまま持ち越している
- 当事者の見解が割れた項目が2件ある。Snowflake の脆弱性について Wiz は Copilot Autofix が co-author のコミットによるとし、GitHub は人間が書いたもので Copilot の関与は無いと否認している。Andon Market の AI 店長 Luna の稼働モデルは、二次が Claude Sonnet 4.6・Andon Labs 自身の投稿が Claude Opus 4.8 で割れており、後者を採る
- 一次に到達できないまま採用した項目がある。Copilot Tuning は `mc.merill.net` の**12日連続**ゲートウェイ拒否で MC1454393 の本文が読めず、停止前日の本日も根拠は検索インデックスのスニペットにとどまる。ChatGPT for Teens は 01 側が `openai.com` のオリジン403で一次未到達のため二次一致で採った。教育プラグイン3本は `learn.chatgpt.com` のゲートウェイ拒否で掲載日を確定できていない
- 出典 URL の陳腐化が1件ある。8/17・8/18 に出典として書いた `learn.microsoft.com/en-us/microsoft-365-copilot/copilot-tuning-overview` は `.../microsoft-365/copilot/copilot-tuning-overview` へ HTTP 301 で恒久リダイレクトしている。取得障害ではないため、次回以降は新 URL を書く
- 障害の変化は2件ある。01 が `status.anthropic.com` をゲートウェイ拒否からオリジン403へ再分類し（`curl` が exit 56 ではなく HTTP 403 を返したため、許可ドメイン追加では解決しない）、`grok.com` を新規にゲートウェイ拒否として記録した。xAI は `x.ai` / `docs.x.ai` と合わせて一次3ホストが全て到達不可になっている
- 各ソースの改善提案は 01 が新規なしで継続19件、02 が新規2件（B-038 / B-039）で継続19件、03 が新規なしで継続10件である
