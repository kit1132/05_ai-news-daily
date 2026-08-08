# AI News Daily Summary — 2026-08-09

日曜は「統制点をどこに置くか」が主題になった。Anthropic は 8/14 に Claude Code の既定を auto mode へ切り替える。都度承認は危険なコマンドの 13.6% しか止められないという対照試験が根拠で、統制点が承認プロンプトから分類器と managed settings へ移る。逆向きの材料として、素の auto mode 構成そのものを狙う AI Now Institute の PoC が7月から公開されており、両方を並べて読む必要がある。ソフトバンクが AGENTIC STAR に LLM Gateway を標準搭載したのも同じ方向で、統制が利用者側から管理者側へ寄っている。Power Platform 側では Release Wave の期日超過を Public preview 列でも数え直した結果、延べ12行が期日を過ぎたままだと判明した。ChatGPT Atlas は本日停止する。

## 今日のハイライト

### 1. auto mode が 8/14 に Claude Code の既定になる — 承認プロンプトを統制点にした運用は5日後に崩れる

**要点**: Anthropic が 8/14 に Pro / Max / Team の Claude Code 既定を auto mode へ切り替える。前提は「都度承認で止める」から「人は 13.6% しか止められないので分類器で止める」へ変わった。

**詳細**: 8/7 に `claude.com/blog` で告知された。auto mode は各ツール呼び出しを分類器に通し、取り返しがつかない・破壊的・環境外を狙う操作だけを止めて、それ以外の承認プロンプトを省く。既定化の対象は新規セッションで、自分で既定を設定している場合は一度だけ切り替え確認が出る。組織が管理設定で固定した既定は変更されない。切り替えは CLI の Shift+Tab かデスクトップアプリのモードドロップダウンで随時できる。分類器が消費する追加トークンは Pro / Max / Team には課金しない扱いへ変わった。

Anthropic が根拠として出した数値は4系統ある。

- 1,053人の有料テスターによる対照試験: 危険なコマンドを人手のレビューは **13.6%** しか止められず、auto mode は同じ集合の 89% を止めた。人間が承認してしまい auto mode が捕まえたものが800件、逆に人間だけが捕まえたものは6件
- 人の捕捉率の劣化: セッションが長いほど落ち、プロンプト50件以降は約5%まで下がる。Claude Code 利用者は承認プロンプトの **97%** を承認している
- 実運用の分析（5〜6月）: 意図しない重大な害を含むセッションの割合が、都度承認は auto mode の2倍。本番相当の深刻度では 6.3% 対 2.4%
- 外部評価: Apollo Research の敵対的レッドチーミングで見逃し率が堅牢化前 12% → 後 7%、Trajectory Labs のプロンプトインジェクション評価（720回）で auto mode の Claude は成功率 0%（競合の自動レビューモードは 5.83%）

統制を残す側の設計も告知と同時に整理されている。

- 組織既定は managed settings の `defaultMode` で固定し、全面禁止は `disableAutoMode` で指定する
- 分類器の設定は `autoMode` ブロックで、`environment`（信頼するリポジトリ・バケット・ドメイン）と `allow` / `soft_deny` / `hard_deny` の4リストを持ち、いずれも自然文で書く。⚠️ `"$defaults"` を配列に入れ忘れると組み込みルールが丸ごと消える（force push・`curl | bash`・本番デプロイ・auto mode 迂回の各ソフトブロックと、データ持ち出しのハードブロック）
- 分類器は `.claude/settings.json` と `.claude/settings.local.json` の `autoMode` を読まない。チェックインされたリポジトリ側から許可ルールを注入されるのを防ぐためで、組織向けの信頼設定は managed settings 側に置く必要がある
- `permissions.deny` は分類器より前に評価され分類器でも上書きできない。押し戻したい操作だけ人の承認へ戻すには `permissions.ask` に `Bash(git push *)` などを入れる
- v2.1.211 以降は作業中リポジトリの任意ブランチへの push と PR 作成が既定で通る。`production` / `release` / `gh-pages` のようにデプロイ先と読めるブランチは分類器が個別に判断し、force push や秘密情報の混入は引き続き止まる
- `autoMode.classifyAllShell` を `true` にすると、`Bash(npm test)` のような狭い許可ルールも auto mode 中は停止して全シェルコマンドが分類器を通る（v2.1.193 以降）
- `claude auto-mode defaults` / `config` / `critique` / `reset` の4サブコマンドで、組み込みルール・実効設定・自作ルールの講評・ユーザー設定の初期化を扱える（`reset` は v2.1.212 以降）

Enterprise・Claude API・Claude Platform on AWS・Amazon Bedrock・Google Cloud Agent Platform・Microsoft Foundry では当面オプトインのままで、Anthropic は1ヶ月以内にこれらも既定化する予定としている。

⚠️ **逆向きの材料が1件ある。** AI Now Institute が 7/8 に公開した PoC「Friendly Fire」は、素の auto mode（Codex は auto-review）構成そのものを対象とする。第三者ライブラリのドキュメントとソースへプロンプトインジェクションを仕込んでおき、利用者が「このライブラリのセキュリティを見て」と頼むと、エージェントが囮のソースを読んで「このバイナリは安全」と判断し実行してホスト上でコード実行に至る。Hooks・プラグイン・MCP サーバー・設定ファイルをいずれも必要としない。対象は Claude Sonnet 4.6 / Sonnet 5 / Opus 4.8 と GPT-5.5 である。

- https://claude.com/blog/auto-mode-default-in-claude-code
- https://code.claude.com/docs/en/auto-mode-config
- https://ainowinstitute.org/publications/friendly-fire-exploit-brief
- https://the-decoder.com/anthropic-sets-claude-code-to-auto-mode-by-default-to-protect-developers-from-bad-approvals/
- https://www.developer-tech.com/news/developers-face-rce-via-claude-code-auto-mode-exploit/

### 2. 2026 Wave 1 は延べ12行が期日超過だった — 計画ページの日付は達成見込みとして読めない

**要点**: 照合を Public preview 列まで広げたところ、GA 列の7件に加えて6件が期日を過ぎたまま止まっていた。Wave 1 の日付は達成見込みではなく、遅延を前提に読む数字へ変わった。

**詳細**: これまでの日次照合は GA 列の緑チェックと月表記だけを数えており、Public preview 列の期日超過を数えていなかった。本日 Power Automate / Power Apps の `planned-features` を全行照合したところ、Public preview 列に月表記のまま緑チェックが付いていない行が6件あった。GA 列の7件と重複するのは code apps のコネクタ CLI 対応の1件だけで、**延べ12行**が期日を過ぎている。2026 Wave 1 の対象期間は4月から9月までで、残りは約2か月である。ページ自体は 8/7 20:59 UTC 更新のままで、本日の再取得では緑チェックの新規追加も期日変更も行削除も発生していない。

- Public preview 列が期日超過の6件
  - デスクトップフローの直接スケジュール実行: Jul 2026
  - デスクトップフローのフローチャート表示: Jul 2026
  - デスクトップフローでの現行 Python バージョン実行: Jul 2026
  - デスクトップフローでの PowerPoint 操作: Jul 2026
  - デスクトップフローからローカル AI モデルへの接続: Jun 2026（2か月超過）
  - code apps のコネクタ CLI 対応: Jun 2026（GA 列の Jul 2026 とも超過）
- GA 列が期日超過の7件（8/8 から増減なし）
  - 1か月超過が5件: 統合 Power Apps によるフォーム UI / マシン・フロー稼働率のダッシュボード表示 / ワークキュー項目の CSV エクスポート / code apps のコネクタ CLI 対応 / FetchXML エディターでのオフラインプロファイル構成
  - 2か月超過: カスタムブランドアプリのプッシュ通知（Jun 2026）
  - 3か月超過: デスクトップ版 Power Automate の以前のプロンプト参照（May 2026）

- https://learn.microsoft.com/en-us/power-platform/release-plan/2026wave1/power-automate/planned-features
- https://learn.microsoft.com/en-us/power-platform/release-plan/2026wave1/power-apps/planned-features

### 3. Claude Code v2.1.225 が headless のトークン破壊を直した — 無人実行を「落ちたら再起動」前提で組まなくてよくなる

**要点**: Anthropic が 8/8 に v2.1.225 / v2.1.226 を出した。一過性の401が長期 OAuth トークンを短命トークンで上書きし headless が壊れる不具合が直り、CI の無人実行を再起動前提で組まなくてよくなった。

**詳細**: 8/7 の 2.1.224 の翌日に2本が続いた。v2.1.226 は「バグ修正と信頼性の改善」のみで、実体は v2.1.225 にある。修正は無人・遠隔で動かす経路に集中している。

- 一過性の401が、保存済みログインの短命トークンで長期の `CLAUDE_CODE_OAUTH_TOKEN` を置き換え、再起動するまで headless セッションが壊れ続けていた
- macOS の MCP OAuth サーバーが、キーチェーン読み取りのタイムアウト後に「一度も認証していない」かのように401を連発することがあった
- auto mode が、自身の権限チェックに対する安全フィルタの拒否を連続ブロック数に数えていた。操作が拒否される点は変わらないが、モデルには再試行せず先へ進むよう伝わる
- セッション間メッセージが headless セッションと起動中に、通知も期限もないまま滞留していた
- `claude self-hosted-runner` が `--base-dir` を作成・書き込みできないとき、登録だけ済ませて全セッションを失敗させていた。起動時に明示エラーで終了するようになった
- Claude Code on the web のセッションが停止扱いで誤報告され、再接続のたびに膨らむイベントを再送していた。巨大な会話を compact した後の Remote Control セッション再開で会話履歴が壊れる問題も直った

機能追加は3点ある。

- ゲートウェイの支出上限が使用量警告に反映され、上限額・リセット時刻・運用者のメッセージが表示される（ゲートウェイ側も 2.1.225 が要る）
- `claude agents` が信頼していないディレクトリで `claude` と同じワークスペース信頼プロンプトを出すようになった
- `SendMessage` が他マシンの Remote Control セッションを名前で指定して会話を開始できるようになった（`ListAgents` に `name [ref]` 形式で並ぶ）。確認済みの Remote Control 宛先が同名のローカルセッションへ差し替わることもなくなった

Remote Control では Claude アプリから添付した写真が、ディスク経由の別ツール呼び出しではなく直接モデルに渡される。VSCode の Focus view が最新の TODO リスト・保留中の質問の文脈・確定した回答を畳んでしまう不具合も直った。`code.claude.com` と `raw.githubusercontent.com` の2ソースで最上位が一致している。

- https://code.claude.com/docs/en/changelog
- https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md

## カテゴリ別まとめ

### Anthropic / Claude

- **auto mode の 8/14 既定化**（ハイライト1参照）。⚠️ `claude.com/blog` が 01 Master の登録ソースでないため検出遅れが3日連続で起きている。03 industry 側は `claude.com` の WebFetch が復旧したことで、テスター1,053人・捕捉率 13.6% / 89%・分類器トークンの非課金を本日はじめて一次で確定した
- **Claude Code v2.1.225 / v2.1.226**（ハイライト3参照）
- `platform.claude.com` の API release notes は **8/7 の Managed Agents 4件**が最上位のままで、8/8・8/9 の追加はない
- `support.claude.com` の Claude Release Notes も 8/6 の skill / plugin セキュリティスキャン beta が最上位のままで動きがない
- `www.anthropic.com` はオリジン403が継続している。WebSearch 5本を実行したが、8/8・8/9 付けの新規企業発表・インシデント公表・助成プログラムは検出できなかった。AI for Science の希少疾患グラント（Claude API クレジット最大 $50,000・6ヶ月）は **8/2 に応募締切済み**である
- 既報: self-hosted environments の public beta（8/6）、Inference hooks の Enterprise beta（8/5）、Claude Opus 4.1 の退役完了（8/5）、Claude Code 週次上限50%増は **8/19** まで、Sonnet 5 促進価格 $2/$10 は **8/31** 終了

### GitHub Copilot

- **Copilot code review の effort level が GA になった（8/7）**: 組織管理者が、レビュー深度の既定を organization settings → Copilot → Copilot code review で決められるようになった。public preview の Low / Medium は Lite / Balanced へ改名され、既存の設定は自動移行された。レビュー深度が「常に同じ」から「変更の性質で選ぶ」前提に変わる。
  - Lite: 定型的で単純な変更に絞った指摘を返す
  - Balanced: 複雑・機微・大規模な変更に対して深い分析を行う
  - 個別設定を持たないリポジトリは組織既定を継承する。レビュー依頼時に利用者がその場で選ぶこともでき、その選択はそのレビュー1回にだけ効いてリポジトリ・組織の既定を上書きしない。どちらの effort level で実行されたかはタイムラインイベントと PR 概要コメントの両方に表示される
  - ⚠️ 対象プランがソース間で食い違う。01 Master は Copilot Pro / Pro+ / Max / Business / Enterprise の全プラン、03 industry は Copilot Enterprise 対象と書いている。一次 changelog を読み直すまでは全プラン前提で提案を書かないこと
  - https://github.blog/changelog/2026-08-07-copilot-code-review-effort-levels-are-generally-available/
- **impact dashboard に ROI 節が追加された（8/7）**: 管理者が、Copilot の投資対効果を自社の給与前提で試算できるようになった。Enterprise / Organization の両階層で提供され、導入段階の異なる2群（chat と補完が中心の passive / Phase 1 層と、エージェント中心の Phase 2 / Phase 3 層）を並べたカードで表示する。効果の語り方が「利用率とアンケート」から「1人あたり月額コストと PR 数」へ寄る。
  - Cost/dev/month: AI クレジットの実消費に基づく、開発者1人あたりの Copilot 月額費用
  - % Payroll/month: その費用を開発者の人件費に対する比率で表したもの
  - Pull requests/month: 開発者1人あたりの月間 PR 数
  - ⚠️ GitHub 自身が「費用は AI クレジット消費からの推計、給与セレクタは実際の給与データではなくモデリング入力」と明記している。提案書へ引用するなら方向性の指標として扱い、金額の断定には使わない
  - 導入コホートの人数集計が、28日レポート期間中に一度でも活動した全ユーザーを数えるよう修正された（従来は最終日に活動したユーザーのみ）。ダッシュボードのみの変更で API と NDJSON エクスポートは変わらない
  - 閲覧には Enterprise owner・billing manager・organization owner か「View Copilot Metrics」権限が要り、Copilot 利用状況メトリクスのポリシー有効化が前提になる
  - https://github.blog/changelog/2026-08-07-copilot-impact-dashboard-adds-a-return-on-investment-section/
- **週次リリースまとめ（8/3 週分）が 8/7 に公開された**: Copilot App / CLI / VS Code の3面で更新が入っている。
  - Copilot App: どのモデルがリクエストを処理したかがクレジットとキャッシュの指標つきで表示され、共有セッションへ直接飛べるようになった。`/side` で並行検討を分岐でき、Impeccable スキルがモバイル UI のデザインレビューに拡張された
  - Copilot CLI: サイドバーで複数セッションを管理できる（`n` 新規・`x` 閉じる・矢印で移動）。実験的な `/worktree` が会話ごとに独立した作業領域を作り、`/rewind` が Git なしでも動くようになった（後続の編集は保持したまま変更ファイルを戻す）
  - VS Code 1.132: ブラウザ統合で Web ページの要素単位に指摘を書けるようになり、端末内モデルによる多言語ディクテーション（言語自動判定）が入った。`/btw` でエージェントの本題を中断せず脇の質問ができ、ハイブリッドエディタで Markdown の差分をガター表示付きで見られる
- **Copilot CLI は pre-release 1.0.79-9（8/7 23:39）が最新で、安定版 1.0.78（8/3）は据え置きである**。実質的な変更は 1.0.79-8（8/7 21:29）に集まっている。
  - Enterprise の allow-auto-only ポリシーに対応し、allow-all 全体は禁じたまま `/allow-all auto` だけを許可できる。Enterprise 管理のサンドボックスポリシーがプロキシ URL を強制し、資格情報は利用者が持つ形になった
  - サンドボックス設定ダイアログに Auth タブが新設され、設定キーが `sandbox.gitAuth` / `sandbox.ghAuth` から **`sandbox.auth.git` / `sandbox.auth.gh`** へ移動した
  - `worktreeBaseRef` が追加され、`/worktree` の起点を HEAD にするかリモート既定ブランチにするかを選べる（既定は HEAD）
  - 大規模モノレポの検索が ripgrep から tgrep（トライグラム索引付き grep）に切り替わった。モデルピッカーに Recent / Recommended / New の区分が入り Shift+Tab で切り替わる
  - ワークスペース内で PATH に載る `.venv/bin` や `node_modules/.bin` などがサンドボックス下で読み取り専用になる不具合が直った。1.0.79-9 は `/sandbox` 設定ダイアログに設定の保存先を表示する改善のみである
- 既報: 利用状況メトリクス API のエージェントアプリ活動追加（8/7・`totals_by_3rd_party_agent` 配列を新設）、Code Quality が Copilot を自動レビュアー登録しなくなった変更（8/7）、Kimi K3 の Copilot 追加（8/6）、GitHub Spark 退役（**8/31**）、既定モデル有効化ポリシー発効（**8/26**）、モデル廃止（**9/1**）

### OpenAI / Codex / ChatGPT

- **ChatGPT Atlas が本日 8/9 に停止する**: 08-07 のハイライトに載せた期限が到来した。ブックマークは自動移行されず、開いているタブと閲覧履歴も引き継がれない可能性があるため、HTML でのエクスポートが案内されている。ChatGPT の会話履歴はアカウント側に保存されており本件の影響を受けない。停止の理由として、投入から8カ月の間 macOS を出られず、予告されていた Windows / iOS / Android 版が公開ベータすら出なかった点が挙げられている。受け皿は ChatGPT デスクトップアプリ・Chrome 連携・ChatGPT Work・Codex で、移行期間は約30日とされる。
  - https://help.openai.com/en/articles/20001371-evolving-atlas-into-chatgpt-for-browser-based-agentic-work
- **ChatGPT デスクトップアプリの内蔵ブラウザが強化された**: 利用者が、アドレスバーから履歴の再訪と Google 検索を行えるようになった。あわせて、コンポーザーに1万字を超える内容を貼ると本文に挿入せず自動で添付ファイル化する挙動が入っている。⚠️ `learn.chatgpt.com` はゲートウェイ拒否が継続しており、内容は `site:` 付き WebSearch 経由である
- **Codex CLI は安定版 0.147.0（8/7 01:41 UTC）が据え置きで、pre-release が 0.148.0-alpha.5（8/8 02:26 UTC）まで進んだ**。8/8 中に alpha.4（00:43）と alpha.5（02:26）の2本が刻まれており、0.148.0 の安定版はまだ出ていない
- `developers.openai.com/changelog` は 8/5 の Fast mode long-context 対応が最上位のままで、8/6〜8/9 の追加はない。`community.openai.com` の Announcements RSS も 7/30 の GPT-5.6 値下げ告知が最新のままで10日間動きがない
- 既報: ChatGPT の Free / Go 無制限化と Think ボタン（8/6）、GPT-5.6 Luna 80%減・Terra 20%減（7/30）、GPT-5.4 / 5.4 mini が **8/31** に Codex（ChatGPT サインイン）から除外、公式 DALL·E GPT は **8/30** 退役

### Microsoft 365 Copilot / Copilot Studio

- **Copilot Studio の What's New はハーネス GA を6日連続で反映していない**: Microsoft は本日も7月節・8月節を追加しておらず、最新は June 2026 節（10項目）のままである。⚠️ 新エージェント体験（GitHub Copilot ハーネス）の表記は `(Production-ready preview)` のままで、8/3 の GA から6日連続で未反映が続いている（B-023）。
  - https://learn.microsoft.com/en-us/microsoft-copilot-studio/whats-new
- **Copilot Studio のビルドは 2026.6.3（6/30 初出）のままで、7月ビルドがゼロのまま8月に入った**。リージョン分布も無変化で、ページの `ms.date` は 6/30、`updated_at` は 7/1 のままである。週次更新日（火曜）を3回またいでおり、**次回 8/11** でも更新がなければ4回目になる
  - https://learn.microsoft.com/en-us/power-platform/released-versions/copilotstudio
- **課金ドキュメント3本に変化はない**: `harnesses-overview` / `billing-credit-overview` / `billing-licensing` を再取得し、いずれも `updated_at` が 8/3 14:59 UTC のままで記載も変わっていないことを確認した。ハーネス比較表（3ハーネスの用途・回復動作・ファイル操作・スキルとメモリ・公開先・課金）と、GitHub Copilot ハーネスが構築開始時点から課金される点も従来どおりである
- **M365 Copilot Release Notes の最新バッチは July 29, 2026（対象期間 7/15〜7/29・全10項目）のままである**。`## ` 見出しの並び（July 29 → July 15 → July 01 → June 16 → June 2）と `### ` 節見出し5本の構成も 8/8 と一致する。次バッチは隔週傾向どおりなら8月中旬見込みになる
  - ⚠️ 英語圏の二次要約が8月の新着として挙げる3件（メール添付ファイルの一覧表示・応答内へのリッチ画像表示・Copilot Chat での SharePoint リスト指定）は、いずれも July 29 バッチに収録済みで新規ではない。一次の先頭バッチを直接読んで突合した結果である
  - https://learn.microsoft.com/en-us/copilot/microsoft-365/release-notes
- 拡張機能 What's New の最新は July 2026 節（宣言型エージェント manifest 1.8、利用状況レポート API 3種の `version` パラメーター）のままで、8月節は未作成である（`ms.date` 7/15、`updated_at` 7/29）
- `purview/whats-new` は7月節が最新のままで、Copilot 関連の新規追加はない。Copilot Agent Kit も releases.atom 上の最新が「Copilot Agent Kit June 2026」（7/9 更新）のままである
- ブログ系はいずれも据え置きである。Microsoft Copilot Blog は 7/21、Copilot Studio Blog は 8/3 の新ハーネス記事、Tech Community M365 Copilot Blog は 8/5 の ICYMI、SharePoint Blog は 8/6 の月次8月号、M365 Developer Blog は 8/6 の Work IQ Developer Tools、M365 Blog 本体は 7/30 の記事が最新である。M365 Roadmap の Latest announcements も 7/9 の GPT-5.6 から動いていない

### Power Platform / ライセンス

- **Release Wave 2026 Wave 1 の延べ12行が期日超過だった**（ハイライト2参照）
- **Partner Center の8月アナウンスに請求書の遅延が追加された（8/7 付・7件目）**: Microsoft が、CSP ディストリビューターと直接請求パートナーの約 **7%** で請求書の生成が遅れていることを告知した。影響は請求書と調整ファイルが Partner Center に出てくるタイミングだけで、金額は正確でありパートナー側の対応は不要とされている。ページの `updated_at` は 8/6 22:02 UTC から 8/7 22:02 UTC へ動いた。公開から4日連続の月内追記で、8月分の掲載は3→4→5→6→7件と増えている
  - https://learn.microsoft.com/en-us/partner-center/announcements/2026-august
- **Copilot Credits の単価は Learn 側に掲載されていない**: 本日あらためて確認した。`billing-licensing` は PAYG メーター・前払いプラン（CCCU）・プリペイドパックの3経路と「未使用分は翌月に繰り越さない」旨を書くのみで、金額は月次改訂の Licensing Guide（PDF）に委ねている。同 PDF は配信元 CDN が 403 のため一次未確認で、**二次に出回る単価は載せない**方針を継続する
  - https://learn.microsoft.com/en-us/microsoft-copilot-studio/billing-licensing
- Power Platform の月次記事は 8/6 公開の「What's new in Power Platform: July/August 2026 feature update」が最新のままで、本日の新規記事はない。親ページと子カテゴリ（Power Automate 4/8・Power Apps 5/13）の WebFetch が不完全レンダリングを返す状態も継続している

### Google

- **Gemini in Google Docs で本文の隣に画像・図表・インフォグラフィックを作成・編集できるようになった**。生成時に文書の文脈を参照する。⚠️ `workspaceupdates.googleblog.com` がゲートウェイ拒否のため、公開日を一次で確定できていない
- **Google Meet の議事メモが、画面共有の開始時に警告を出すようになった**。発表を始めると Gemini が発表内容のスクリーンショットをメモに取り込む可能性がある旨が通知される
- **Gemini API の単価は7日連続で据え置きだった**: `ai.google.dev` の料金ページを再取得し、08-08 収録分から変更がないことを確認した。3.6 Flash（$1.50／$7.50）と 3.5 Flash（$1.50／$9.00）の出力単価の逆転、3.1 Flash-Lite（$0.25／$1.50）が 3.5 Flash-Lite（$0.30／$2.50）より安い関係のいずれも継続している。3.1 Pro Preview はプロンプト長に応じ入力 $2.00〜$4.00／出力 $12.00〜$18.00 である
  - https://ai.google.dev/gemini-api/docs/pricing
- Gemini API changelog は 7/30 が最新のままで8月の追加はない
- 既報: Gemini in Classroom の全年齢開放は web が **8/10**・モバイルが **8/17**、Made by Google は **8/12** 開催予定、Gemini 3.5 Pro は未 GA が継続（8/12 のリーク報道はあるが Google 未発表）、Imagen 4.0 系3本が **8/17** 停止

### AI セキュリティ

- **DEF CON 34 で自律エージェントが CTF 上位5%に入った**: 8/6〜9 にラスベガスで開催中の DEF CON 34 で、自律エージェントが競技の標準装備として扱われる段階に入ったことが示された。運営側が「自律エージェントが参加する前提」で競技設計を組み替え始めた点が変化にあたる。
  - UC Santa Barbara と UC Berkeley の研究者が作った自律システム **SageCTF** は、DEF CON CTF のオンライン予選で8つのフラグを取り、採点対象686チームの上位5%に入った。AI 支援なし（または最小限）と自己申告したチームはすべて下回っている。1問あたり平均5時間の自律探索を要した
  - AI Village は今年 **HalCTF**（Hostile Autonomous Layer CTF）を新設し、参加者が自律エージェントを OCI コンテナとして構築・投入してサンドボックス化された標的を攻略する形式にした。モデル推論は集中サービス経由に統一され、GPU 予算の差で勝敗がつかないようにしている
  - 08-08 収録の Black Hat（8/5〜6）のコーディングエージェント脆弱性3件と同じ週の出来事で、攻撃側の道具としての成熟と防御対象としての脆弱性が同時に提示された形になる
  - https://aivillage.org/blog/halctf/
  - https://www.techtimes.com/articles/323346/20260806/def-con-34-opens-today-ai-agents-graduate-novelty-standard-hacking-weapon.htm

### 資本 / インフラ

- **AMD が Taalas を買収する（8/6 合意）**: モデルの重みをシリコンへ直接焼き込む方式のスタートアップを取り込み、推論単価の下げ方に専用チップを加える。前提が「推論単価は GPU の世代交代とソフト最適化で下がる」から「モデルを固定できるなら専用チップで桁が変わる」へ広がる。
  - Taalas は2023年設立のトロント拠点で、汎用アクセラレータではなく特定モデル向けに設計したチップを作る。デモチップ HC1 は Llama 3.1-8B で **1ユーザーあたり毎秒16,960トークン**を記録し、報道は競合 GPU 比で最大48倍としている
  - 自社ツールで設計から完成シリコンまで約2カ月で回せるとも説明しており、モデルの更新周期に対して製造周期が追いつくかがこの方式の成否を分ける
  - 買収金額は非開示で、クロージングは規制当局の承認を条件に **2026年 Q4** の見込みである。AMD は Taalas の技術を自社アクセラレータのロードマップへ取り込み、Instinct GPU・EPYC・Helios ラックスケール・ROCm と並ぶシステムレベル製品を作るとしている
  - 07-31 収録の Anthropic × AMD 最大2GW 提携、08-07 収録の Anthropic 自社チップ設計チーム（トークンあたり推論コスト約50%削減が目標）と同じ方向の動きにあたる。⚠️ 一次リリース（`newsroom.amd.com`）はゲートウェイ拒否で本文に到達できず、数値は二次報道の突き合わせで構成されている
  - https://www.cnbc.com/2026/08/06/amd-buys-taalas-startup-that-hardwires-ai-models-into-its-silicon.html
  - https://www.theregister.com/systems/2026/08/06/amd-acquires-ai-chip-startup-taalas-to-boost-inference-performance-by-etching-models-into-silicon/5284344

### モデル / 料金

- **DeepSeek のピーク時間課金は時間帯が既に公表済みだった**: 08-08 に「ピーク時間帯の単価倍増案は未実施」として収録した案の中身が、V4 系列の投入時に公表されていたことを確認した。対象は**北京時間の平日 9〜12時と 14〜18時**で、この時間帯は v4-pro / v4-flash 両モデルの入力・出力単価がいずれも2倍になる。V4 Pro の出力は100万トークンあたり通常6元がピーク時12元（約$1.77）である。ただし 8/2 時点で割増は発動しておらず公式料金ページは時間帯なしの単一レートのままで、8/6 に予告された「大幅値上げ」の幅と実施日は依然として未開示にある。⚠️ `api-docs.deepseek.com` はゲートウェイ拒否で一次の料金表に到達できず、時間帯と倍率は二次報道の突き合わせによる
  - https://www.scmp.com/tech/big-tech/article/3358868/after-triggering-price-war-deepseek-reverses-course-surcharge-peak-hour-api-use
- **Grok 4.6 は一次確認が依然できていない**: 二次サイトは「8/7 ローンチ・1.5T パラメータ・V9 基盤据え置きで SFT と RL に投資」と完了形で書くが、同じ記事群が「アクセスは X と SuperGrok の購読者から順次」「開発者 API と独立ベンチマークは数日遅れ」と未確定形でも書いており、xAI 自身の告知は確認できない。`x.ai` / `docs.x.ai` / `openrouter.ai` がいずれもゲートウェイ拒否のため、モデル ID・価格・コンテキスト長のいずれも裏が取れていない。2.1T の新基盤による Grok 4.7 が8月末〜9月初と報じられている点も同様に未確認である
- **8/8〜8/9 に作成された注目のオープンウェイトモデルはない**。Hugging Face の作成日降順100件を走査したが、該当期間で likes 5 超または DL 100 超のものは1件もなかった（最大でも likes 1 / DL 0 の個人リポジトリ）。モデルリリースの追跡サイトでも、フロンティア級の最新は 8/5 の Meta Muse Spark 1.2 のままである

### 開発ツール / その他

- **Cursor は changelog・Announcements フォーラムとも動きがない**。changelog RSS の最上位は 8/3 の Google Workspace Plugins、Announcements の最上位は 7/28 の Cursor Start のままで、RSS 2本とも取得に成功している
- **Devin は 8/5 の更新が最新のままで、8/6 以降の追加はない**。`docs.devin.ai` はゲートウェイ拒否が継続しており、内容は WebSearch 経由である
- **MCP は公式ブログの新着がなく、RSS 最新は 7/28 の `The 2026-07-28 Specification` のままで12日連続の据え置きになっている**。Tier 1 SDK のバージョン（TypeScript / Python `2.0.0`、C# `v2.0`、Go は `go-sdk` `v1.7.0`）にも変化はなく、8/8 の Codex CLI alpha 2本に MCP 関連の追加記載はない
- **Apple は AI 関連の新規がない**。`developer.apple.com` は 200 で取得でき、最新は 8/5「Get ready for new creative assets on the App Store」のままである。iOS 27 / iPadOS 27 developer beta 4（7/20・ビルド 23G71）が最新で、GA は9月見込みになる

### 国内

- **ソフトバンクが AGENTIC STAR に LLM Gateway を標準搭載する**: 8/7 発表。法人向け AI 活用プラットフォーム「AGENTIC STAR」の SaaS 版に、複数の LLM を統合管理する LLM Gateway 機能を8月上旬から標準搭載し、既存顧客へは順次提供する。位置づけは、エンジニアが業務で使う AI コーディングツールと、顧客が契約して使う LLM サービスとの間に挟まるゲートウェイにあたる。狙いは、開発者に AI コーディングツールを使わせたまま、企業側のセキュリティポリシーと情報保護要件を統制下に置くことにある。ハイライト1の auto mode 既定化・Copilot 側のモデルポリシー統制と同じく、統制点がエージェントの利用者側から管理者側へ移る流れの国内版にあたる
  - https://ai.watch.impress.co.jp/docs/news/2131486.html
  - https://robotstart.info/article/2026/08/07/382247.html

## 直近の注目予定

- **8/9**: ChatGPT Atlas シャットダウン（本日）／ DEF CON 34 最終日
- **8/10**: Gemini in Classroom が全年齢の生徒へ開放（web）／ Power Platform Weekly の休刊明け確認、PnP 週次アジェンダ
- **8/11**: Copilot Studio Released Versions の定例更新日（4回目）／ 拡張機能 What's New・非推奨一覧・MS-4005 の週次確認
- **8/12**: Made by Google ／ Gemini 3.5 Pro ローンチの噂（Google 未発表）
- **8/14**: Claude Code の既定権限モードが auto mode へ（Pro / Max / Team・ハイライト参照）／ Copilot Success Planner のマイクロスキリング提供開始
- **8/17**: Claude Console 旧 Workbench 退役 ＋ 実験的プロンプトツール API 廃止 ／ Gemini API の Imagen 4.0 系3本停止 ／ Gemini in Classroom のモバイル開放
- **8/18〜9/8**: M365 Copilot Agent's Playbook ライブストリーム（各回 9AM PT）
- **8/19**: Claude Code 週次上限50%増の終了
- **8/20**: Gemini Enterprise Agent Platform の Grok 4.1 ファミリー停止（一次未確認）
- **8/22**: M365 Copilot アプリのチャット中心 UI が Deferred リングへ展開開始
- **8/26**: OpenAI Assistants API 廃止 / o3 退役 / GPT-4.5 完全廃止 ／ Copilot 既定モデル有効化ポリシー発効
- **8月中旬**: M365 Copilot Release Notes の次バッチ見込み ／ Copilot in 30 の顧客向け評価ツール追加
- **8/30**: 公式 DALL·E GPT の退役
- **8/31**: GitHub Spark の既存ユーザーアクセス終了 ／ Sonnet 5 促進価格終了（→ $3/$15）／ `gemini-robotics-er-1.6-preview` 停止 ／ GPT-5.4・5.4 mini が Codex から除外 ／ Power Automate モバイルアプリの廃止
- **9/1**: GitHub Copilot の全体験でモデル廃止
- **9/2**: Windows 365 Frontline 名称での購入最終日（9/3 に Flex へ改称）
- **9月**: iOS 27 / macOS 27 GA ／ App Store の Social Media 年齢レーティング回答が必須化 ／ auto mode 既定化を Enterprise・API・各クラウドへ拡大予定
- **9/30**: M365 E7 プロモーションの対象購入最終日（10/1 新規取引停止）／ M365 E5・E3 の CSP 割引終了
- **2026 Q4**: AMD による Taalas 買収のクロージング見込み（規制当局の承認が条件）
- **10/27〜29**: Power Platform Community Conference 2026（MGM Grand ラスベガス）
- **11/1**: パートナー特典の有効期限がオファー購入日基準へ移行
- **12/2**: EU AI Act の生成コンテンツ標識義務、猶予終了
- **12/31**: M365 E3 プロモーション、Copilot in 30、Purview Suite 50%オフの提供終了
- **時期未定**: ドメイン除外の再提供 ／ Cowork 1 の提供開始 ／ Copilot Studio What's New への7月・8月節の追加とハーネス GA の反映 ／ Fluent UI (v8) コントロールの廃止日

## 改善メモ

- 3ソースとも当日分を取得できた（01 Master / 02 Copilot / 03 industry）。欠損リカバリの対象はない
- **検出遅れが3日連続**: `claude.com/blog` が 01 Master の登録ソースでないため、8/7 告知の auto mode 既定化を本日まで拾えていなかった（Master B-017）。03 industry 側は `claude.com` の WebFetch 復旧により本日一次で確定できており、同じ告知を一方が一次・一方が未登録で扱う状態になっている
- **32日遅れの捕捉**: AI Now Institute の PoC「Friendly Fire」（7/8 公開）を 03 industry が本日はじめて収録した。素の auto mode 構成そのものを対象とする材料で、8/14 の既定化と正面から関わる
- **照合漏れの是正**: 02 Copilot の Release Wave 照合が GA 列だけを数えていたため、Public preview 列の期日超過6件を取りこぼしていた（ハイライト2参照）
- **ソース間の矛盾（1件）**: Copilot code review の effort level GA の対象プランが、01 Master は「Pro / Pro+ / Max / Business / Enterprise の全プラン」、03 industry は「Copilot Enterprise 対象」と食い違う。一次 changelog の再読で確定するまで両論併記とした
- 障害の変化: `newsroom.amd.com` / `ainowinstitute.org` / `api-docs.deepseek.com` の3ドメインがゲートウェイ拒否で新規登録（industry）。`www.ppweekly.com` を 403 から `EGRESS_BLOCKED` へ分類変更（Copilot）。`claude.com` の WebFetch は復旧（industry・2026-07-30 以降オリジン403として扱ってきたドメイン）
- 継続提案は Master 7件（最多 B-013 403の2分類・13回目）、Copilot 17件（最多 B-011 Power Platform Blog のトピック記事照合・21回目）、industry 5件（最多 B-004 取得方法の WebSearch 優先化・41回目）。3ソースとも新規提案はない
- ソース間の重なり: auto mode 既定化は Master と industry で重複し、Master の設定リファレンス（`$defaults`・`classifyAllShell`・サブコマンド）と industry の逆向き材料（Friendly Fire）を合わせた。Claude Code v2.1.225 / 226 も両方にあり、変更点の網羅は Master 側を基にした。Copilot の ROI 節は Master が指標の日本語説明を、industry が画面上の英語表記を持っており、後者を採って前者で補った
