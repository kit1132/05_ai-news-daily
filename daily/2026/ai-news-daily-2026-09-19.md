# AI News Daily Summary — 2026-09-19

退役期日が1本増え、手元の道具が2日で3回入れ替わった日である。GitHub は Copilot の6モデルを 10/19 に廃止すると告知し、Claude Code は `2.1.275`〜`2.1.277` を連続で出して、途中の1版がプロキシ構成の全リクエストを落とした。最新版は CLAUDE.md の無いリポジトリで AGENTS.md を読む。Microsoft 側では Cowork のローカルブラウザーに必要な Edge が告知なく 150 系から 152 系へ上がり、8/29 に配った前提条件が古くなっている。

## 今日のハイライト

### 1. GitHub Copilot が6モデルを 10/19 に廃止する — 10/2 の4モデル廃止に続く2波目で、GPT-5.5 / 5.4 系が丸ごと消える

**要点**: GitHub が 9/18 に Copilot の6モデル廃止を告知し、廃止日を **10/19** とした。10/2 の4モデル廃止から17日後に2波目が来るため、「Copilot のモデル欄に並んでいるものを選ぶ」前提が、期日ごとに移行先を確かめる前提へ変わる。

**詳細**: 廃止対象と GitHub が示した代替は、Gemini 3.7 Flash → Gemini 3.8 Flash、GPT-5.5 → GPT-5.6 Sol、GPT-5.4 → GPT-5.6 Sol、GPT-5.4 mini → GPT-5.6 Luna、GPT-5 mini → GPT-5.6 Luna、Grok 4.5 → Grok 4.6 の6件である。対象面は Copilot Chat・インライン編集・ask / agent モード・コード補完で、Copilot の全体験に及ぶ。

Enterprise と Business では、管理者がグローバル既定または個別モデルを無効化していない限り、代替モデルが既定で自動的に有効になる。廃止後にユーザー側で旧モデルを削除する操作は要らない。

⚠️ **OpenAI API 側には対応する廃止告知が無い。** `gpt-5.5` $5／$30、`gpt-5.4` $2.50／$15、`gpt-5.4-mini` $0.75／$4.50 はいずれも本日時点の OpenAI 料金表に残っており、消えるのは Copilot 経由の提供だけである。ただし `gpt-5.5` 自体は **10/14** に ChatGPT / ChatGPT Work / Codex から退役する（API は対象外）ので、同じモデルに面ごとの期日が3本立っている状態になる。

- https://github.blog/changelog/2026-09-18-upcoming-deprecation-of-selected-github-copilot-models-in-mid-october
- https://developers.openai.com/api/docs/pricing

### 2. Claude Code が2日で3版を出し、うち1版がプロキシ構成を全断させた — 即日更新は「回帰を踏まないか確かめる」作業になった

**要点**: Claude Code が 9/17〜9/18 に `2.1.275`〜`2.1.277` を出し、`2.1.275` は `ANTHROPIC_BASE_URL` でプロキシやゲートウェイを挟む構成の全リクエストを 400 で落とす回帰を含んでいた。翌日の `2.1.276` はこの1件だけを修正している。

**詳細**: 回帰時のエラーは `400 … Input tag 'advisor_20260301'` で、`2.1.276` のリリース本文はこの修正のみを挙げる。`2.1.275` 自体も大きく、`Changed` 行が9件ある。

- 組織環境: Team / Enterprise の Code タブから開く組織環境が読み取り専用の要約になり、管理設定のラベル「Web」が「Cloud sessions」へ変わった
- プラグイン取得: npm 由来のプラグインを `npm pack --ignore-scripts` と整合性検証で取得するようになった
- 確認の省略: スケジュール実行と Run now のアーティファクト再公開が確認を求めなくなった（公開アーティファクト・初回公開・削除は従来どおり確認する）
- 追加側: claude.ai アカウントで有効なスキル / プラグインのターミナル同期（`syncClaudeAiSkills` / `syncClaudeAiPlugins` で無効化可）、`/plugin install <plugin> --marketplace <source>`、送信キー ctrl+enter

`2.1.277`（9/18 16:22 UTC）は **AGENTS.md サポート**を追加した。**CLAUDE.md が無いリポジトリでのみ**プロジェクト指示として読み、切り替えは `/config` の「Project instructions」で行う。Bedrock / Vertex / Foundry は未対応である。他エージェント向けに置いた AGENTS.md が Claude Code には無関係、という前提はここで崩れる。

同版の `Changed` 5件のうち2件はプロンプトインジェクション対策で、サブエージェントの結果がサブエージェント出力であることを示すヘッダ付き・インデント付きで主エージェントへ届き、結果内のテキストがセッション自身の指示として通らなくなった。あわせて TaskOutput ツールが廃止され、背景タスクの出力は Read で読む方式へ変わった（`taskOutputMaxChars` と `TASK_MAX_OUTPUT_LENGTH` は無効）。Anthropic API 上では Fable が `/model` に常時表示される。

⚠️ npm の `stable` は `2.1.267` のまま10日連続で据え置きで、`2.1.268`〜`2.1.277` の**10版ぶん**が stable 固定の組織に届いていない。`latest` / `next` は `2.1.277`。

- https://code.claude.com/docs/en/changelog
- https://registry.npmjs.org/@anthropic-ai/claude-code

### 3. Cowork のローカルブラウザーに必要な Edge が 150 系から 152 系へ上がった — 8/29 に配った前提条件が告知なく置き換わっていた

**要点**: 必要 Edge バージョンが **150.0.4078.83** から **152.0.4191.53** へ引き上げられた。8/29 に前者を掲載して以来この数値に触れておらず、150 系・151 系のまま配ったテナントは文書上の最低要件を下回る。

**詳細**: `cowork/cowork-local-browser` の `ms.date` が 2026-08-27 → **2026-09-16**、`updated_at` が 2026-08-28T05:15Z → 2026-09-16T17:36Z へ動いた。表記も「Edge 150 Stable 2 以上」から「recommended minimum Edge version 152.0.4191.53 or higher」へ変わっている。グループ単位の制御に必要な Edge 152（8/24 の週リリース）の記述は据え置きなので、要件バージョンと制御バージョンが 152 に揃った形になる。管理者側の前提は変わらず、`Copilot > Settings > View All > Cowork settings` の Allow browser access は既定で無効のままである。

改訂では利用者から見た失敗時の挙動が4節ぶん増えた。

- 対応面: Cowork on the web（Edge）のみ対応で、他ブラウザーとモバイルは対象外。デスクトップアプリは「ブラウザー作業は Web 版で動く」と返す
- Edge が無い場合: ブラウザーを使わない工程は最後まで実行し、どの工程に Edge が要るかを会話で名指しして `Get Microsoft Edge` のリンクを出す
- 組織がブロックするサイト: Purview DLP・条件付きアクセス・Web フィルタリング・ブラウザー管理ポリシーをそのまま継承し、止まった場合はブロックされた工程と手作業の代替手順を提示する
- 中断したタスク: タブを閉じる・スリープ・切断では失敗させずに一時停止し、同じ会話で「continue」「resume」等を送ると Edge の可用性を確かめて再開するか確認を求める

⚠️ 本文は対応面を `m365.cloud.microsoft` と書いており、8/18 に業務用 Copilot の既定入口が `copilot.cloud.microsoft` へ移った件とは表記が揃っていない。

- https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-local-browser

## カテゴリ別まとめ

### Claude / Anthropic

- Claude Code が `2.1.275` / `2.1.276` / `2.1.277` の3版を出した（ハイライト2参照）。`2.1.277` は `CLAUDE_GATEWAY_PROXY_IS_EGRESS_BOUNDARY=1` と Claude apps gateway upstream の任意 `headers:` マップも追加し、非対話セッションの `/ultrareview` がベースブランチも共通履歴も無いリポジトリでは拒否するようになった
- Anthropic が自社の AI R&D 自動化率を数値で公開した（9/17）。Claude が Anthropic の AI R&D 作業の **26%を主導**し、90%が「AI が協働する」水準以上にあるとする。9/12 の Amodei 論考「We Must Pace the Frontier」を運用指標へ落としたもので、第三者評価者を社内に常駐させる構想も示した
  - AI-Led R&D Automation Index: AI の関与度を AL0（関与なし）から AL5（完全自律）の6段階で採点し、社内の AI R&D 作業を全件分類する
  - エージェントの監督: 監視されている行動の割合・行動から確認までの時間・遮断／フラグされた割合の3つを出す。プラットフォーム上で約30,000 のエージェントが動き、判断が遮断されるのは **0.002%**（約47,000件に1件）
  - 計算資源の配分: 安全性研究への配分は全体で6%、AI 主導の R&D 内に限ると12%
- Anthropic が Claude による生体分子モデリングの高速化を報告した（9/17）。ツール30本超を4週弱で平均約4倍（出力が完全一致する範囲でも約2倍）にし、1標的あたりのコストが **$10,000 から約 $150 へ**下がったとする
  - FlashPairformer カーネルは triangle attention で 2.7〜2.9倍、triangle multiplication で 1.7〜3.2倍を出す。8-GPU B300 ノード1台で7万トークン超の構造を予測した
  - Adaptyv Bio と組んだタンパク質設計コンペを併せて告知した。Claude クレジット最大 **$100万**・Modal の計算クレジット $25万・5,000超の設計のウェットラボ検証つきで、**9/28 から 10/31 まで毎週1題**出る
- Balyasny Asset Management の Claude Fable 5 評価事例が `claude.com/blog` に載った（9/17）。運用資産 約380億ドル・投資プロフェッショナル 約2,000人の組織が数千件の実務タスクで検証し、Fable が 89.4%、旧本番モデルが 86.1% だったとする
  - ⚠️ 能力が上がってもモデルの権限は自動で広げないという原則を明示し、データ境界・最小権限・ツール単位の許可を先に敷いたうえで重要な出力に人間の確認を挟むとしている
  - マージャーアービトラージ分析が3〜5日から1日未満（エージェント実行 約30分）へ、中央銀行分析が約2日から約30分へ短縮したとする
- Claude Platform API の release notes は 9/18 の Compliance API エントリが最上位のままで新規がない。ローカルセッションエンドポイントが Claude in Chrome のトランスクリプト（`product_surface` = `claude_in_chrome`）も返す Enterprise ベータである
- `support.claude.com` の Release Notes は 9/15 の Salesforce in Claude が最上位のままで、Cowork 統合も Projects 再設計も未反映が続く。製品ブログが release notes に先行する形が変わっていない
- モデル退役ページに新規告知はなく、直近告知は 2026-06-05 の Opus 4.1 のままで Active は11件で据え置きである。`alignment.anthropic.com` も9月の新規投稿が無い

### OpenAI / Codex / ChatGPT

- Codex CLI `0.155.0` の内容が `learn.chatgpt.com` の統合 changelog で一次確定した。実験的な `/voice` 会話（ライブ文字起こしとマイク操作つき）、TUI のライブ推論要約と完了時刻表示、agents overview でのタスク非表示・アーカイブ・削除、対応 Mac のローカル TUI セッションにおける MCP リクエストの Touch ID 確認、デーモン更新スケジュールの設定化と保存スレッドの復旧が入る
  - ⚠️ 前日ダイジェストが二次から引いた列（`codex agents` ダッシュボード / MCP 2026-07-28 対応 / `/cd` `/pwd` `/cwd` / `codex queue` / Vim 編集拡張 / `codex doctor` 改善 / SDK からの effort 上書き）は、この一次の記載と一致しない。前日「一次未読のため確定として扱わない」としていた判断が結果として正しかった
  - 安定版 `rust-v0.155.1` が 9/18 19:04 UTC に出たが本文は読めない。tags 列では **0.156.0 系の alpha が既に3本**刻まれている
- ⚠️ `learn.chatgpt.com` の 9/14 に、前日まで把握していなかった退役告知がもう1件あった。研究プレビューの **GPT-5.3-Codex-Spark が廃止**され、ChatGPT デスクトップアプリ・Codex CLI・IDE 拡張から削除された
- OpenAI の API 単価は26日連続で据え置きとなった。GPT-6 Astra 短文脈 $10／$50（キャッシュ $1.00）、GPT-5.6 Sol $4／$20（期間限定価格は「少なくとも 2026年11月21日まで」）、Terra $2／$12、Luna $0.20／$1.20、`gpt-5.6-cyber` $12.50／$75、`gpt-5.3-codex` $1.75／$14
  - ファイル検索はツール呼び出し $2.50／1kコール・保管 $0.10／GB日（1GB 無償）、Hosted Shell / Code Interpreter はセッション単位で 1GB $0.03 〜 64GB $1.92
  - データレジデンシーの10%上乗せは、2026年3月5日以降にリリースされたモデルが対象と明記されている
- OpenAI の廃止一覧は全件抽出に戻り、**09-18 の3件への縮小は削除ではなく抽出のばらつきだったと確定した**。新規告知は 2026-09-11（`gpt-5.4-cyber` → `gpt-5.6-cyber`）のままで、撤回・延期・追加はない
- `developers.openai.com/api/docs/changelog` は 9/15 の API キー作成ガバナンス制御が最上位のまま、`community.openai.com` の Announcements RSS は 9/10 の Agents API 告知のまま8日間動きがない。`alignment.openai.com/misalignment-reports/` も6件のままである

### Google

- Google が Workspace 側で 9/17 に3本、9/18 に1本を出した。いずれも Gemini API changelog には載らない種類の更新である
  - Notebooks in Gemini: 集中作業用の専用ワークスペースを学校・組織向けに提供開始した
  - Expert Intelligence in Gemini Notebook: 9/17 公開
  - Workspace Studio: カスタムスターター／ステップ・サードパーティ連携・webhook でワークフローを自動化できるようになった
  - 9/18 は Gemini Notebook の新学期向け機能と学習ツール
- Gemini API changelog は 9/17 の `antigravity-preview-09-2026` が最上位のままで新規がない。⚠️ 旧 `antigravity-preview` の停止は **10/5** で、パラメータ命名が snake_case → PascalCase、ファイル編集が全文書き換え → 行範囲置換に変わる破壊的変更を伴う
  - 新しい組み込みツールは `write_to_file` / `replace_file_content` / `view_file` / `list_dir` / `find_by_name` / `grep_search` の6種である
  - 影響範囲は実行環境で分かれる。リモートサンドボックスでテキスト出力だけを読む構成ならエージェント文字列の差し替えで済み、ローカル実行は呼び出し側の書き換えが要る
- 既報: `gemini-3.8-flash` の入力 $0.75 / 出力 $3.75 は **2026-12-31 まで**、旧 `gemini-omni-flash-preview` は **9/30 廃止**、Gemini 3.5 Pro GA は未ローンチ継続

### Microsoft 365 Copilot / Cowork

- Cowork のローカルブラウザー要件が Edge 152 系へ上がった（ハイライト3参照）
- Cowork プラグインが Claude Code / Cursor のプラグインを CLI で取り込めることが分かった。`atk import openplugin` が既存プラグインを M365 マニフェストへ変換し、`SKILL.md` は**無変換でそのまま通る**。取り込みが約5分、ゼロから作る場合が約30分と書かれている
  - ⚠️ 本日の変更ではなく**初検知**であり、この経路がいつ提供開始されたかは一次から確定できない
  - 変換される成果物: `.claude-plugin/plugin.json`（または `.cursor-plugin/plugin.json` / `.plugin/plugin.json`）が `manifest.json` へ、`skills/*/SKILL.md` が `agentSkills[]` へ書式そのままコピー、`.mcp.json` が `agentConnectors[]` へ
  - 変換されないもの: `commands/`（スラッシュコマンド）・`agents/`（サブエージェント）・`hooks/`（イベントハンドラ）はいずれも未対応
  - 必須の追加入力は `--privacy-url` と `--terms-url`。コネクタの `authorization.referenceId` はプレースホルダーで入るため、実際の OAuth クライアント登録 ID へ差し替える必要がある
  - スキルの読み込みは3層で、frontmatter が常時（約100トークン）、`SKILL.md` 本体が発火時（5,000トークン未満推奨）、`references/` が要求時（上限なし）。カスタムプラグインはモバイルの Cowork では動かない
- Cowork の What's New は September 2026 節の New features 4件から増減がなく、⚠️ 上記2本のドキュメント更新は**いずれもこの What's New に現れない**
- M365 Copilot Release Notes は新バッチが追加されていない。先頭見出しは August 25, 2026 のままで、隔週の期日 9/8（UTC）から11日、前バッチからは25日が過ぎている
- Web グラウンディング統制のページは 9/9 に復活した Domain Exclusion（上限1,000ドメイン・既定無効）の記述を本日も反映していない。Copilot Tuning のページも停止発効（8/20）から30日たって停止も退役も書いていない

### Copilot Studio / Power Platform

- Copilot Studio の Roadmap 22件のうち**14件が GA 期日 September CY2026** を持ち、全件 `In development` のまま残り11日になった。9/12 時点の9件から増えている
  - 9月期日には、9/15 起票のコスト可視化3件（Monitor タブ・エージェント評価・プレビューチャット／履歴）、ツール呼び出しへの人手承認要求（570434）、SharePoint リストのナレッジソース化（566859）、Dataverse 連携（568929）、SQL Server 対応（568930）が含まれる
  - 期日超過も2件あり、566997（maker 提供資格情報のブロック）が「August CY2026」から19日、562221（エージェントワークフローでの MCP 準拠ツール利用）が「June CY2026」から3か月半を過ぎている
  - ⚠️ **GA を当日に判定できる経路は3本ともふさがっている。** What's New は July 2026 節が最新で8月節すら未作成、Release Wave の緑チェックは 9/3 で据え置き（**11/15** に Release Planner ごと退役）、Roadmap のステータス欄は22件が一度も `Rolling out` へ動いていない
- Roadmap に 9/17 23:00Z の新規起票が5件あったが、Copilot Studio / Power Platform の対象はゼロだった。内訳は Outlook 1件・M365 管理センター 1件・Teams 1件・Dynamics 365 Field Service 2件で、GA 期日はいずれも October CY2026 である
- Copilot Studio のモデル可用性表はハーネス別の2本とも据え置きで、9/18 に初検知したハーネス側11モデル・標準側13モデルの構成に変化はない。課金・課金レート表・ガイダンスハブ（相対 href 171件）も動いていない
- Power Platform の Released Versions は Copilot Studio Build **2026.6.3** のままで、⚠️ 「毎週火曜更新」と書く定例日（UTC 9/15）にも新ビルドが出ず80日が過ぎた
- Power Platform Blog の親ページは 9/3 の PPCC 記事が先頭のままで、9/17 公開の9月月次記事が2日たっても現れない。子カテゴリ（Power Automate / Power Apps）側では先頭に出ている
- Purview の What's New は 9/8 起票の **570845**（DLP for Microsoft Cowork・Preview 9月 / GA 10月）を本日も掲載していない。Agent 365 の What's New も 8/6 公開分から44日新規がない

### GitHub / 開発ツール

- GitHub Copilot の6モデルが 10/19 に廃止される（ハイライト1参照）
- Copilot CLI の安定版 `v1.0.86` が 9/17 22:57 UTC に出た。カスタムエージェントが `include-custom-instructions: true` でリポジトリの指示ファイル（`AGENTS.md` / `copilot-instructions.md` / `CLAUDE.md`）を読めるようになった
  - 再開時に marketplace のプラグインとスキルが保持され、`/sandbox` のポリシー表示がローカルネットワークアクセスを設定どおり出し、autopilot がタスク完了受理後に停止する
  - ⚠️ `v1.0.85` の破壊的変更3件（`copilot plugins list --json` のフラット配列化・`--kind` / `--scope` 削除・`plugins list` の対象縮小）は `v1.0.86` でも解消されていない
- GitHub が 9/14 週の Copilot リリースをまとめて 9/18 に公開した。コードレビューが対応済みコメントを次回レビューで自動解決し、提案を適用する際にコミットメッセージ案を出すようになった（GA）
  - VS Code Agents の利用状況メトリクスが GA になり、日次アクティブユーザー・セッション数・ユーザーメッセージ総数をエディタ側と分けた専用画面で見られる
  - GitHub Copilot アプリに Sentry 連携のキャンバスが加わり、VS Code 1.138 ではローカルの Dev Container 上でエージェントを動かせるようになった（Docker が必要・段階展開）
  - ⚠️ 9/16 に GA した予算増額申請は、**マネージドユーザーを使うエンタープライズでは利用できない**
- GitHub が 9/17 に Copilot の計測系を2件更新した。Copilot impact dashboard が機能単位のエンゲージメントを表示し、エージェント型 CLI のカスタマイズが利用状況メトリクス API の対象に入った
- GitHub が 9/18 に統制系の変更を2件出した。コードカバレッジの ruleset 条件を REST API から管理できるようになり、npm には公開前の検証段階だけで使える stage-only トークンが加わった
- Cursor の changelog は 9/10 の Projects が最上位のままで9日間、フォーラム Announcements は 9/2 のまま17日間動きがない。⚠️ **Cursor は GPT-6 Astra の提供開始を告知しないまま16日目**に入った（9/3 GA・11/12 に OpenAI 側が供給停止予定）
- Grok 4.7 は公開予定日 9/12 を過ぎて7日目も未公開で、xAI 一次にはローンチページ・モデル ID・価格・コンテキスト長のいずれも無い。公式提供中の最新は Grok 4.6（8/12・context 50万トークン・$2/$6）である
  - ⚠️ 2.1兆パラメータ・SpaceX 社内データの利用・9/11 の「あと数日必要」表明は**いずれも Musk の X 投稿が出所の二次**にとどまる

### セキュリティ

- Hacktron が OpenAI 社内 monorepo への侵入チェーンを 9/18 に開示した。フォーラムの画像デコーダ脆弱性と SSO 設定不備を繋いで従業員アカウントを奪い、連携済みの Codex から社内 monorepo に実証用 PR を出している。実施は 2026年7月25日で、発見から到達まで **72時間未満**だった
  - 侵入口: `community.openai.com`（Discourse）のアップロード処理が HEIC / HEIF を ImageMagick 経由で脆弱な libheif に渡しており、細工した画像でヒープオーバーフロー → RCE → フォーラムの管理権限（**CVE-2026-32882**）
  - 横展開: OpenAI 側の SSO 設定不備により、ChatGPT と Codex のアカウント乗っ取りに繋がった
  - 到達点: 従業員の連携済み Codex アカウントから社内 monorepo へ無害な PR を作成し、社内コードや機微情報は読まずに検証を止めたとしている
  - 対応: OpenAI は初報から約14時間で修正を確認し、指摘に **$6,500** を支払った。フォーラム自体はバウンティ対象外である
  - ⚠️ 一次（`hacktron.ai`）はゲートウェイ拒否で本文に到達できず、複数の二次の一致で構成されている
  - https://idtechwire.com/researchers-chain-forum-exploit-and-sso-weakness-to-access-openai-employee-accounts/

### MCP / オープンウェイト

- MCP 公式ブログは 8/22 の「The New MCP Roadmap」が最上位のまま28日間新規がない。⚠️ **仕様側が止まる一方で実装側が AGENTS.md へ寄りはじめており**、Claude Code `2.1.277` と Copilot CLI `v1.0.86` が同じ日に指示ファイルの相互運用へ動いた
- WebMCP Challenge は提出締切を経過し、**受賞発表は 9/23**（賞金総額 $35,000）である
- 8 org のうち `meta-models` にだけ新規リポジトリがあり、9/11 以降7日間続いた全 org の空白が途切れた。⚠️ **ただし重みは無い。** `meta-models/utils` のファイルは `.gitattributes` / `README` / `README.md` の3点のみで safetensors は0件、タグはプレースホルダのまま、ライセンス未設定・`gated: manual` である
  - 他7 org の最新作成は `DeepSeek-V4.1-Flash` 9/10 ／ `gnm-v3` 9/1 ／ `Qwen-Drive-1.0-4B` 8/27 ／ `GLM-5.3-Flash-BF16` 8/25 ／ `Shieldstral-1.0-3B` 7/16 ／ `Kimi-K3` 6/13 ／ `privacy-filter` 4/17 で据え置きである

### 市場データ / 企業構造・規制

- Anthropic のペース測定指標の公表を、各紙が「AI が自らの後継を作りつつある」という文脈で扱った（9/18 報道）。Claude が自社 AI R&D の26%を主導するという数値が根拠として引かれている
- ⚠️ 開発ペースの減速論は 9/12 の Amodei 論考 → 9/14 の Microsoft AI 行動規範草案 → 9/16 の OpenAI ミスアライメント6件公表 → 9/17 の Anthropic 指標公開と**5日間で4社ぶんが並んだ**。ただし Amodei の論考本文と Microsoft の草案 PDF 本体はいずれも一次未読である（ホストがゲートウェイ拒否）
- 国内外の調査機関に新規公表はなく、引用可能値は 09-18 から不変である。Similarweb 8月分は ChatGPT 55.5%・Gemini 25.6%・Claude 9.3%・DeepSeek 3.4%・Grok 2.4%・Copilot 1.6%・Perplexity 0.9%、IDC の国内 AI 支出は2025年 2兆3,725億円 → 2029年 6兆8,897億円（CAGR 36.0%）である
- AI データ保護と電力需給の2社が資金調達を公表した。MIND が 9/18 に Series B で **$72M**（Crosspoint Capital Partners 主導・累計 $112M）、Emerald AI が Series A で **$150M**（データセンターの需要応答で系統容量 100GW の解放を狙う）である。⚠️ いずれも一次プレスリリース未到達で二次のみのため、金額以上の条件は採録していない
- Apple の Developer News は 9/18 の iPhone Duo 向け開発リソースが最上位で AI 関連ではない。⚠️ AI 関連の独立エントリは 6/11 の ImageCreator クラス廃止告知のまま3ヶ月動いていない
- 既報（一次未読を含む）: Google による Claude Opus 5 の全エンジニア開放（9/15）、Anthropic のコンピュート契約 $517B・14.8GW（⚠️ 確定支出ではなく**上限枠**でオプション・LOI を含む）、Altman の年内 IPO 否定（9/12）、OpenAI → Cursor のモデル供給停止（遮断予定 11/12）、Anthropic の秋 IPO 観測（上場日は未確定）

## 直近の注目予定

- **9/21**: Anthropic ウェルビーイング研究助成の応募締切 ／ 各リポジトリの週次復旧チェック（月曜）
- **9/23**: WebMCP Challenge の受賞発表 ／ Microsoft「Partnering for Success Together」第1回
- **9/24**: OpenAI の Videos API と Sora 2 系が退役（代替モデルの提示なし）
- **9/28**: OpenAI の `gpt-3.5-turbo-instruct` / `babbage-002` / `davinci-002` / `gpt-3.5-turbo-1106` が停止 ／ Copilot のチャット3面統合・code review 既定の Balanced 化・チャットのデータ保持がアカウント存続期間へ ／ Anthropic × Adaptyv のタンパク質設計コンペ開始（〜10/31・毎週1題）
- **9/29**: OpenAI DevDay 本体（サンフランシスコ Fort Mason・基調講演はライブ配信）
- **9/30**: Gemini の旧 `gemini-omni-flash-preview` が廃止（後継 `gemini-omni-1.1-flash`） ／ OpenAI の現行 OneGov 契約（$1/年）が失効 ／ **Copilot Studio の Roadmap 14件が GA 期日** ／ M365 E7 プロモ最終日・E5 / E3 の CSP 割引終了 ／ 2026 Wave 1 の対象期間終了
- **9 月中**: macOS 27 GA ／ Claude Projects 再設計が Pro / Max の Claude Code 利用者全体へ拡大 ／ Copilot Tuning の Public Preview 再開 ／ Release Plans の新規掲載停止
- **10/1**: OpenAI の `gpt-5.4-cyber` が API から削除（移行先 `gpt-5.6-cyber`） ／ OpenAI の OneGov トークン課金50%割引が開始 ／ Copilot Business・Enterprise の既存顧客が前払い必須に ／ Microsoft CSP ソフトウェア価格改定と M365 G7 の GA ／ Apple の EU 向け新ビジネス条件が発効
- **10/2**: GitHub Copilot が Gemini 3.5 Flash / Gemini 3.6 Flash / Kimi K2.7 Code / Claude Opus 4.7 を全体験から廃止
- **10/5**: Gemini の旧 `antigravity-preview` が停止（移行先 `antigravity-preview-09-2026`・パラメータ命名と編集方式が変わる） ／ OpenAI `gpt-rosalind-research` の課金開始 ／ Anthropic ウェルビーイング助成の full proposal 期限
- **10/13**: Office LTSC 2021・Project LTSC 2021・Visio LTSC 2021 のサポート終了
- **10/14**: OpenAI の `gpt-5.5` が ChatGPT / ChatGPT Work / Codex から退役（移行先 `gpt-5.6-sol`・API は対象外）
- **10/16–11/11**: OpenAI DevDay Exchange 8都市（東京は 10/20）
- **10/19**: **GitHub Copilot が6モデルを廃止**（Gemini 3.7 Flash / GPT-5.5 / GPT-5.4 / GPT-5.4 mini / GPT-5 mini / Grok 4.5）
- **10/22 / 10/23**: Apple のサブスクリプション Volume Purchasing 開始 ／ iPhone Duo 発売（iOS 27.1）
- **10/23**: OpenAI のレガシースナップショット退役（`gpt-3.5-turbo-0125` / `gpt-4-0613` / `o1-2024-12-17` / `o4-mini-2025-04-16` 等12件）
- **10/26 頃**: Microsoft AI の MAI モデル行動規範に対する公開協議の6週間が終了
- **10/27〜29**: Power Platform Community Conference 2026
- **10/31**: OpenAI の既存 evals が読み取り専用になる ／ Anthropic × Adaptyv コンペの最終週
- **10 月**: Anthropic の IPO 観測（上場日は未確定） ／ METR による Anthropic のインシデント独立調査の初回8週間が下旬まで
- **11/2**: GitHub Actions の `pull_request_target` 既定無効化が公開リポジトリで強制開始 ／ M365 Copilot Business の従量課金が既定オン（$10/ユーザー/月の枠つき）
- **11/12**: OpenAI が Cursor へのモデル供給を停止する予定日（一次未読）
- **11/15**: Microsoft Release Planner 退役
- **11/21**: OpenAI GPT-5.6 Sol の暫定値下げが有効とされる期限
- **11/30**: OpenAI の Reusable prompts・Evals プラットフォーム・Agent Builder が停止
- **12/1**: OpenAI の GPT Image 系が停止（→ `gpt-image-2`）
- **12/2**: EU AI Act の生成コンテンツ標識義務、8/2 以前に市場投入済みシステムへの猶予終了
- **12/11**: OpenAI の旧スナップショット退役（`gpt-5-2025-08-07` / `o3-2025-04-16` 等）
- **12/31**: Gemini 3.8 Flash と 3.7 Flash の導入価格が終了（$0.75/$3.75 → $1.50/$7.50） ／ GitHub Copilot の Fable 5.1 / Fable 5 に対する ZDR 暫定免除が終了
- **年内**: Anthropic の新データ保持方式 ／ Claude Docs / Claude Slides の Team・Free への展開 ／ Claude Projects 再設計の Team / Enterprise 展開 ／ Microsoft AI の MAI モデル行動規範の改訂版公開
- **Q4 CY2026**: Graph PowerShell v3.0.0 リリース（Windows PowerShell 5.x のサポートなし）
- **2027-01-20 / 02-26**: OpenAI の audio / realtime 系退役 ／ 文字起こし4モデル退役
- **2027-03-01 / 03-31 / 2028-10-01**: SharePoint クラシック退役 ／ Azure ポータルの Microsoft Sentinel 体験が退役 ／ SharePoint クラシック第2波
- **2027-04**: Apple の最小 SDK 要件が iOS 27 世代へ上がる
- **2028-03**: OpenAI が「automated AI researcher」の実現目標とする時期

## 改善メモ

- 新規提案3件: 01 は B-076（`www.anthropic.com/research` の一覧取得に href の同時取得を義務づける）、02 は B-072（最低バージョン・上限値・エンドポイントといった前提条件の数値を状態ファイルに記録し、無告知の要件変更を検知する）、03 は B-040（AI 開発ツールのセキュリティ開示を定点ソースに追加）
- 継続提案: 01 が19件（最多 B-024 取りこぼし検出手順・45回目）、02 が48件（最多 B-011 Power Platform Blog の WebSearch 照合・59回目）、03 が6件（最多 B-004 取得方法欄の WebSearch 優先化・82回目）
- 障害の変化: 03 が `docs.cloud.google.com`（Gemini Enterprise リリースノート）と `www.hacktron.ai` のゲートウェイ拒否を新規記録した。01 は `github.com/openai/codex` の個別タグ本文欠落が再発した一方、`0.155.0` の本文を `learn.chatgpt.com` で一次確定でき、併用一次が GitHub releases の欠落を埋めた初の事例となった
- 障害の変化: 01 で `devblogs.microsoft.com/commandline` の日付食い違いが解消し、Intelligent Terminal 0.2.2572 は 9/14 付と確定した（09-17 の「8/31 付」が誤読）
- ソース間の差分: Claude Code の3版について、01 は `Changed` 9件と AGENTS.md のゲートウェイ設定を、03 は TaskOutput ツールの廃止と送信キー ctrl+enter を拾っており、**同じ changelog から抽出した項目が一致しなかった**。本サマリーは両者を統合した
- ソース間の差分: GitHub Copilot のモデル廃止は 10/2（4モデル・既報）と 10/19（6モデル・本日 03 が初検知）の2波があり、01 の注目スケジュールには 10/19 が入っていない。**01 側の `github.blog/changelog` 取得が Copilot ラベルの 9/18 分を拾えていない可能性がある**
