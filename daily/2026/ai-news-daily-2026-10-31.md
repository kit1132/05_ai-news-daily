# AI News Daily Summary — 2026-10-31

Microsoft は Power Apps の Copilot による式の生成とコントロール名の変更を 12/11 に、モデル駆動アプリの説明文の AI 生成を 11/30 に退役させる。Anthropic は Claude Code `2.1.314` で、作業ディレクトリ外への書き込みを全モードで拒否する設定を入れた。Cursor の拡張機能マーケットプレイスには Claude Code を装う悪性拡張が約11時間載っていた。昨日ハイライトにした Power Automate の「Describe it to design it」の退役節は、非推奨一覧から消えた。

## 今日のハイライト

### 1. [廃止] Power Apps の Copilot 機能3つと共同編集表示2つが 11/30・12/11 に退役する — メーカー画面の中の Copilot 支援が、Power Apps からも外れる

**要点**: 12/11 以降、メーカーはキャンバスアプリで Copilot に Power Fx 式を生成させることも、コントロール名を一括で付け直させることもできなくなる。モデル駆動アプリの説明文の AI 生成は 11/30 に終わる。「Copilot に式を書かせる」前提の研修手順は差し替えが要る。

**詳細**: Power Platform の非推奨一覧（`important-changes-coming`）が 10/30 19:04Z に `0219930b`（`ms.date` 10/28）へ改訂され、先頭に6節が加わった（`## ` 見出しは 98 → 103）。

- 式の生成と Power Apps Ideas（12/11）: Ideas、Create a formula、コードコメントからの式の生成が使えなくなる。Explain this formula / Explain this selection は残り、既存の式には影響しない
- Rename controls with Copilot（12/11）: Copilot がコントロール名を提案しなくなる。Tree view で手で変える
- モデル駆動アプリの説明文の AI 生成（11/30）: Publish ダイアログと設定パネルから Create descriptions using AI が消える。代わりに「model app-builder スキル」が案内されている
- Plan Designer の共同編集（11/30・MC1530697）: 同じプランを同時に編集できなくなり、未保存の変更が上書きされうる
- モデル駆動アプリのレコード単位の在席表示（11/30・MC1532182）: 誰が同じレコードを開いているかが見えなくなる
- 環境間のコメントのインポート・エクスポート（12/31）: 環境内のコメント機能は残る

- https://learn.microsoft.com/en-us/power-platform/important-changes-coming
- https://mc.merill.net/message/MC1532182

### 2. [破壊的変更+新機能] Claude Code `2.1.314` で作業ディレクトリ外への書き込みを全モードで拒否できるようになり、`FORCE_HYPERLINK=false` の意味が反転した — 書き込み範囲は permission mode と deny ルールで組む前提から、1キーで全モード共通に固定できる前提に変わる

**要点**: Anthropic が 10/30 に出した Claude Code `2.1.314` で、`permissions.blockWritesOutsideWorkingDirectories` を入れると Write / Edit / NotebookEdit が permission mode に関係なく作業ディレクトリ外を拒否する。auto mode を許す運用でも書き込み範囲を設定で固定できる。

**詳細**: 一次は Claude Code changelog（10/30）。`2.1.313` は publish されていない。npm は `{stable: 2.1.308, latest: 2.1.314, next: 2.1.314}`。

- 権限・管理設定
  - Claude apps gateway: upstream に `groups`（IdP グループで振り分け。フェイルオーバー時も適用）、Bedrock upstream に `guardrail_trace`（発火した guardrail フィルタを本文なしで記録）が加わった
  - 管理者が effort に上限を掛けた組織で "Invalid effort level" が毎ターン出る不具合を直し、effort を下げて再試行するようにした
  - リモート管理設定だけに置いた `forceRemoteSettingsRefresh` が保存コピーの期限切れ後に効かず、ポリシー無しで起動できた不具合を直した
- 挙動の変更
  - `FORCE_HYPERLINK=false`（`no` / `off` も）がハイパーリンクを有効ではなく無効にする
  - `claude -p` は起動失敗時に終了コード0・無出力で終わっていたが、エラーを出して1で終わる
  - VS Code と Claude Desktop の Code タブで、20万トークン超の会話を放置すると要約する（idle compaction）。Bedrock・Vertex・Foundry・LLM ゲートウェイでも1時間キャッシュ有効時に動く

- https://code.claude.com/docs/en/changelog
- https://registry.npmjs.org/@anthropic-ai/claude-code

### 3. [セキュリティ] Cursor の拡張機能マーケットプレイスに Claude Code の偽拡張が約11時間載っていた — マーケットプレイスの拡張は「公式名なら安全」とは言えなくなった

**要点**: The Decoder（10/30）によると、Claude Code を装った悪性拡張が Cursor のマーケットプレイスに 10/29 の約11時間公開され、最大5,000人に影響した可能性がある。Anthropic は開発に関与していない。Cursor で Claude Code 拡張を入れた端末は入手元の確認が要る。

**詳細**: 典拠は Cursor の説明を引く The Decoder（10/30）。拡張機能名と発見者は記事に書かれていない。

- 収集を試みた情報: ホスト名・ユーザー名・OS・グローバル IP アドレス
- 遠隔操作: 攻撃者は遠隔操作の設定を試みたが、管理者権限が要るため多くの端末では成立しなかったとみられる
- Cursor の対応: 拡張を削除してマーケットプレイス全体を一時停止し、マルウェアを無効化して他の拡張に影響がないことを確かめてから再開した

- https://the-decoder.com/malicious-claude-code-extension-in-cursors-marketplace-attempted-remote-access-and-data-theft/

## カテゴリ別まとめ

### Copilot Studio / Power Platform

- **Power Apps の Copilot 機能と共同編集表示の退役**（ハイライト1参照）
- [観測] **Describe it to design it の退役節が消えた** — 昨日（10/30）の本サマリーがハイライト1に載せた Power Automate の「Describe it to design it」（11/30 退役）の節が、10/30 19:04Z の改訂（`0219930b`）で非推奨一覧から消えた。撤回の告知も Message Center の通知も二次報道も見当たらず、退役が取り消されたのか別ページへ移ったのかは確認できていない
  - https://learn.microsoft.com/en-us/power-platform/important-changes-coming
- [新機能] **Copilot Studio の評価機能の一括 GA** — Microsoft が 10/29〜30 の Message Center 7件で、評価機能が 10/15 に GA したと告知した。管理者は Evaluation Viewer ロールで、エージェントの編集権限を渡さずに評価結果だけを見せられる
  - 採点器: タスク完了（MC1530742）とツール精度（MC1530748）を判定し、エージェントとシナリオに合わせたカスタム採点器の自動生成（MC1531924）もできる
  - 自動化フローの評価（MC1531903）: エージェントと同じ方法でフローの品質を評価できる
  - 評価の警告（MC1532071）: 未評価のエージェントや、前回評価の後にモデルが変わったエージェントに Review パネルが警告を出す。公開は止めない
  - カスタム採点器のライブラリ（MC1531932）は 11/15 に GA する
  - https://mc.merill.net/message/MC1532073
- [予定] **M365 管理センターでの Copilot Studio のコスト管理（Roadmap 577834・10/29 起票）** — Microsoft が、昨日の MC1530368 を Roadmap にも載せた。最初に対応するのは環境とエージェント単位のポリシーで、ユーザー・グループ単位は後の段階になる。Cowork と Copilot Studio のエージェントの費用データは Cost Management とエージェントレジストリに出る
  - https://www.microsoft.com/microsoft-365/roadmap?id=577834
- [据え置き] **Copilot Studio の What's New・課金・モデル表** — Copilot Studio What's New は `031b66d5`（`ms.date` 10/5）のままで、ハーネスの改名もまだ載っていない。課金レート表・課金5本・PPAC の容量管理・モデル表3本・ガイダンスハブにも改訂はなく、Released Versions は 2026.6.3 のまま122日たつ
  - https://learn.microsoft.com/en-us/microsoft-copilot-studio/whats-new

### Microsoft 365 Copilot / ライセンス

- [新機能+予定] **Copilot Notebooks から Copilot Workspaces への移行** — Microsoft が Tech Community の「What's New in Microsoft Copilot | October 2026」（10/30）で、既存の Notebooks を Workspaces に移し、チームのメンバー・文脈・作業ファイルを1か所にまとめる形に変えると示した。Frontier には10月に出ている
  - Workspaces: 複数人が同じ文書を同時に編集でき、ライブカーソルが出る（Frontier・10月）
  - Office ファイルの作成と編集: ワークスペース内で Word / Excel / PowerPoint を作って直接編集できる（Frontier・10月、全世界は1月）
  - 音声概要: トピック別エピソード、秘密度ラベルの継承、Outlook と Teams の参照に対応した（全世界は11月）
  - 同じ記事のその他: Copilot アプリの Home に Chat と Cowork がまとまる（全世界11月）。Autopilot は11月に Frontier へ出る。スキルは11月に Copilot Chat でも作れる
  - https://techcommunity.microsoft.com/t5/microsoft-copilot-blog/what-s-new-in-microsoft-copilot-october-2026/ba-p/4568528
- [仕様] **10月の What's New の管理者向け項目** — Microsoft が同じ記事で、Purview のデータライフサイクル管理から Copilot のメモリーに保持ポリシーを掛けられるようにしたと示した。Purview DLP の Cowork 対応はパブリックプレビューになり、PowerPoint の Copilot には Sonnet 5.5 が入った
  - https://techcommunity.microsoft.com/t5/microsoft-copilot-blog/what-s-new-in-microsoft-copilot-october-2026/ba-p/4568528
- [新機能] **Copilot Chat のメモリーの出典表示（MC1530959・Roadmap 574111）** — Copilot Chat の利用者は、回答に使われたカスタム指示・保存したメモリー・過去のチャットを Sources の Personalization タブで確かめ、その場で見直し・削除できるようになる。Premium ライセンスが必要で、10月下旬に展開する
  - https://mc.merill.net/message/MC1530959
- [予定] **Office in Copilot（MC1530611）** — 利用者は、11月中旬から Copilot アプリの中で Word / Excel / PowerPoint のファイルを作成・編集・共同編集できるようになる。管理者の操作は不要で、既存の Copilot のポリシーと Entra ID で統制する
  - https://mc.merill.net/message/MC1530611
- [予定] **Copilot アプリのタスクバー固定の設定（MC1530612）** — 管理者は、12月上旬から有償の M365 Copilot ライセンスを持つ利用者だけに Copilot アプリをタスクバーへ固定できるようになる。保存すると M365 管理センターが Entra にライセンスベースのグループを作る
  - https://mc.merill.net/message/MC1530612
- [予定] **Cowork と Autopilot の Engage プラグイン（MC1530609）** — Microsoft が 11/16 の GA を予定している。既定はオフで、管理者が組織全体か対象のユーザー・グループに有効化する
  - https://mc.merill.net/message/MC1530609
- [予定] **Agent Builder のプロンプトのスケジュール実行の延期（MC1302906 更新）** — Microsoft が展開の開始を10月末から11月中旬に、完了を11月末から12月中旬に延ばした
  - https://mc.merill.net/message/MC1302906
- [予定] **Purview の DSPM classic の退役延期（MC1481315 更新）** — Microsoft が DSPM classic と DSPM for AI classic の退役を、2027年1月下旬から3月中旬開始・3月下旬完了に延ばした
  - https://mc.merill.net/message/MC1481315
- [観測] **Web 検索の統制ページの改訂** — `manage-public-web-access` が 10/29 23:24Z に `78eced4f` へ改訂され、Web 検索の説明が Researcher・Analyst・Cowork にも当てはまるという注記が入った。9/9 に復活したドメイン除外の記述は今回も本文にない
  - https://learn.microsoft.com/en-us/microsoft-365/copilot/manage-public-web-access
- [据え置き] **Release Notes と Microsoft のブログ各種** — Release Notes は October 27, 2026 バッチのままである。Copilot ブログ・Power Platform ブログ・TC の Copilot Studio Blog・Agent 365 Blog・M365 Developer Blog に新しい記事はない
  - https://learn.microsoft.com/en-us/microsoft-365/copilot/release-notes

### Anthropic / Claude

- **Claude Code `2.1.314`**（ハイライト2参照）
- **Cursor のマーケットプレイスの Claude Code 偽拡張**（ハイライト3参照）
- [据え置き] **Anthropic の一次各種** — Platform release notes の最上位は 10/29 の Usage and Cost Analytics API のままで、モデル退役ページの Active は15件、Deprecation history の最新も 9/30 のままである。Claude Haiku 4.5 は退役下限日の16日後も Active のまま残る。`/news`（10/28）・`/research`（10/27）・`claude.com/resources/articles`（10/28）・support の release notes（10/21）も動いていない
  - https://platform.claude.com/docs/en/about-claude/model-deprecations

### OpenAI / ChatGPT / Codex

- [新機能] **GPT-6 Rosalind** — OpenAI が 10/30 に、生物学の推論と科学ツールの利用に特化した `gpt-6-rosalind` を API に出した。使えるのは trusted-access プログラムで Rosalind Research の承認を受けた組織の、内部研究目的の認可ユーザーに限られる。料金ページの単価は 27.2万トークン以下で入力 $15・キャッシュ $1.50・出力 $75、超えると $30・$3・$112.50（100万トークンあたり）で、データレジデンシーは10%増し。system card は Deployment Safety Hub に無い
  - https://developers.openai.com/api/docs/changelog
  - https://developers.openai.com/api/docs/pricing
- [セキュリティ+仕様] **GPT-6 Luna の 10/29 更新** — OpenAI が 10/29 に ChatGPT の GPT-6 Luna を更新し、応答を簡潔にして迎合的な言い回しを減らした。system card の補遺では、Preparedness の分類はサイバー・生物化学とも High のままで、セーフガードも 10/7 版と同じである
  - 退行: 事実誤りの率は6指標すべてで 10/7 版より上がった（GPT-5.6 Luna よりは低い）。HealthBench Hard は 27.2 → 22.8
  - 改善: 重度の生物系プロンプトの安全応答率は 0.945 → 0.976、プロンプトインジェクション堅牢性は 99.91%
  - https://deploymentsafety.openai.com/gpt-6-luna-october-28-2026-addendum
- [動向] **Model Spec の5価値への再編** — OpenAI が 10/29 付の Model Spec 更新で、行動指針をユーザーの意図への忠実さ・害の低減・誠実さと透明性・人間の主体性の尊重・ケアの5つに組み直した。The Decoder（10/30）によると、エージェントには監視・修正・停止を妨げないことと、自己保存などの独自目標を追わないことを求めている
  - https://the-decoder.com/openai-sets-new-behavioral-guidelines-for-ai-models-that-have-already-proven-hard-to-control/
- [新機能] **Codex CLI `0.166.0`** — OpenAI が 10/29 に Codex CLI `0.166.0` を安定版にし、GPT-6.1 Terra を同梱・Vertex AI・Amazon Bedrock のモデルカタログに加えた。`codex queue --resume`、`codex doctor --network-only`、トランスクリプトのキーボード選択と検索も入り、破壊的変更の記載は無い
  - https://github.com/openai/codex/releases
- [新機能] **ChatGPT の Dots テキスト送信（beta）** — OpenAI が、米国の一部 ChatGPT Pro 利用者が常駐エージェント Dots にテキストメッセージで指示し、進捗を受け取れる限定 beta を始めた。release notes の日付は 10/28 だが、WebSearch の断片と二次記事でしか確認できていない
  - https://help.openai.com/en/articles/6825453-chatgpt-release-notes
- [据え置き] **OpenAI の定点** — deprecations（`2026-10-14: GPT-4 series model deprecations`）、community Announcements（10/28 の API クレジット）、`alignment.openai.com` の First posted（10/20）は動いていない

### Google / Gemini

- [新機能] **Gemini API の Computer Use が GA** — Google が 10/30 に、Gemini API の Computer Use ツールを Interactions API と GenerateContent API の両方で一般提供にした。対応モデルは `gemini-4-argon`・`gemini-3.8-flash`（推奨）・`gemini-3.5-flash-lite`・`gemini-3-flash-preview` で、ブラウザ・Android・デスクトップを操作できる。changelog と Computer Use のページに料金は載っていない
  - https://ai.google.dev/gemini-api/docs/changelog
  - https://ai.google.dev/gemini-api/docs/computer-use
- [新機能] **Google スライドの全体編集** — Google が 10/30 に、Gemini in Google スライドの1つのプロンプトで複数スライドやプレゼン全体を編集できるようにした。スタイルの統一、Drive のファイルを使った内容更新、スライドの結合・展開ができる。英語のみで、Business / Enterprise の Standard・Plus と Google AI Pro / Ultra が対象。複数スライド作成の上限を引き上げる優待は少なくとも 12/1 まで続く
  - https://workspaceupdates.googleblog.com/2026/10/edit-entire-presentations-with-gemini-in-Google-Slides.html
- [新機能] **Gemini アプリでのドキュメント・表の作成と編集** — GIGAZINE（10/30）によると、Google は Gemini のチャット内で Google ドキュメント・スプレッドシート・スライドを作成・編集できるようにした。Web 版は PDF とテキストファイルも扱い、スマホ版は PDF の作成と編集に対応する。日本でも使えるが、対象プランは記事に書かれていない
  - https://gigazine.net/news/20261030-gemini-document-spreadsheet-edit/
- [据え置き] **Google の定点** — Gemini アプリの release notes は 2026.10.13、The Keyword の AI RSS は 10/26 のままである。Gemini API の deprecations は 11/17 の停止予定のまま変わっていない

### Cursor / Orca / その他の開発ツール

- [破壊的変更+新機能] **Orca `v1.4.245`** — Stably AI が 10/30 に出した Orca `v1.4.245` で、プラグインが既定で有効になり、Mac の computer use が既定でバックグラウンド操作になった。インストール時にレビュー画面が開き、コードを実行するプラグインは同意を求めるが、承認したプラグインはコンピューター全体にアクセスできる
  - Codex: macOS / Linux で貼り付け推定を切り、別クライアントから送ったプロンプトが送信されるようにした。Orca 管理アカウントの履歴を `~/.codex` に見せる設定（既定オン）が加わった
  - Mac の computer use: 従来の前面操作は `--restore-window` で求める
  - 既定の変更: 新しいターミナルは新しいホストで動き、同時実行ターミナル数の上限は各マシンのシステム上限に合わせる
  - `v1.4.244` へ戻すと Source Control の AI 操作のモデル・effort 設定が消え、再更新でも戻らない
  - https://github.com/stablyai/orca/releases
- [据え置き] **Cursor・Devin・xAI・TypeSafe AI** — Cursor の changelog（10/20 Agent SDK）とフォーラム（10/12）、Devin（10/28）は動いていない。xAI の release notes は「October」の4項に日付が付いたが、項目は既報のままである。TypeSafe AI の `jev-latest` / `jev-preview` は `jev-1.14.0` のまま

### MCP / オープンウェイト

- [仕様] **MCP Ruby SDK が Tier 1 に** — MCP プロジェクトが、公式 Ruby SDK を SDK 階層制度の Tier 1 に上げた。2026-07-28 仕様リビジョンを完全にサポートし、採点対象の2リビジョンで適合テストを100%通過している。記事の日付は 9/29 で、RSS の最上位より上に加わったのを本日初めて検出した
  - https://blog.modelcontextprotocol.io/posts/ruby-sdk-tier-1/
- [据え置き] **Hugging Face の登録8 org** — Hugging Face の8 org に新規リポジトリは無く、Obsidian も 10/22 のまま動いていない

### セキュリティ

- [セキュリティ] **GLM 5.3 による Firefox の攻撃チェーンの自律作成** — The Decoder（10/30）によると、Epoch AI の研究者が、オープンウェイトの GLM 5.3 で修正前のコードから脆弱性を探す「パッチギャップ」攻撃を検証した。9/17〜10/26 公開の Firefox 6版を対象に、閲覧したページから PC のローカルファイルを外へ送る攻撃を組み、成功1件あたりの API 費用は約 $1,000、最速は12時間だった。Chrome では約 $100,000 をかけても同等の攻撃は作れず、Mozilla は 10/27 の Firefox 159.0 で修正した
  - https://the-decoder.com/open-weight-model-glm-5-3-built-full-firefox-exploit-chains-with-zero-human-input-in-under-48-hours/

### 市場・業界動向

- [動向] **Microsoft の Azure 売上が前年比48%増** — Microsoft が 10/28 に発表した FY27 Q1（7〜9月）決算で、Azure は **$33.2B** だった。全社売上は $92.3B（+19%）、Microsoft Cloud は $63.9B（+30%）、商用 RPO は $677B（+73%）、設備投資は $39.4B（前年 $19.4B）。セグメントは「Agents and Infra」に組み替えられ、Copilot の席数は開示されていない
  - https://www.microsoft.com/en-us/investor/earnings/FY-2027-Q1/press-release-webcast
- [動向] **AWS の売上が前年比39%増** — Amazon が 10/29 に発表した Q3 決算で、AWS は **$46.0B**、営業利益は $17.8B（+55%）だった。全社売上は $201.9B（+12%）。Bedrock は Fortune 500 企業の支出が前年比約7倍、トークン量が約17倍に増えたと説明している
  - https://ir.aboutamazon.com/news-release/news-release-details/2026/Amazon-com-Announces-Third-Quarter-Results/default.aspx
- [動向] **Google 検索の売上比率が初めて50%割れ** — GIGAZINE（10/30）が Company Atlas のデータを基に、Q3 の検索売上 $63.4B が Alphabet の総売上 $128B の49.7%（Q2 は52.8%）だったと伝えた。Google Cloud は24.1%を占める
  - https://gigazine.net/news/20261030-google-search-alphabet-revenue/
- [据え置き] **買収協議と国内調査** — Amazon × Decart、Nvidia × Reflection AI の買収協議に続報はなく、IDC Japan・MM総研・NRC の新規公表も検知されていない

## 直近の注目予定

- **10/31**: MCP サーバー認定の旧申請経路が終了 ／ DeepSeek の Search・Fetch API の無料提供が終了 ／ OpenAI の既存 Evals が読み取り専用に
- **10月下旬〜11月中旬**: Researcher の Critique / Council が退役（MC1515927、Act by 11/14）
- **11/1**: AI Builder の容量アドオンが提供終了し、新規・更新のライセンスに AI Builder クレジットが付かなくなる（MC1526652） ／ Codex の28日間「改善かリセット」の終了（二次）
- **11/2**: xAI `grok-imagine-image-quality` が退役 ／ Meet の63言語音声翻訳が Scheduled Release へ展開開始
- **11/4**: Entra で一般ユーザーのブループリント作成が既定オン（MC1506733） ／ Kimi K3.1 Pro の重み公開の約束期限（二次）
- **11/5 ごろ**: Anthropic のゲスト研究者（生命科学）の応募受付が終了（締切日は明記なし）
- **11月**: GitHub の cloud sandbox の課金が開始（日付は明記なし） ／ Targeted release の割り当てが変更不可になり、統合 Release Preferences 画面が入る ／ Copilot アプリの新しい Home が全世界に出て、Autopilot が Frontier に出る
- **11/9**: Dataverse のみのテナントでストレージ検証が開始（MC1483529）
- **11/12**: Copilot Studio の GPT-4.1 / GPT-5 系が退役（MC1506318） ／ Anthropic Usage Policy 改定版が発効 ／ OpenAI → Cursor のモデル供給停止予定（一次未読）
- **11/15**: Dataverse for Teams 環境とアンマネージド開発者環境の新規作成が停止 ／ Copilot Studio のカスタム採点器ライブラリが GA（MC1531932）
- **11/16**: GitHub Copilot が Claude Opus 4.8・Opus 5・GPT-5.6 Terra を廃止 ／ Teams の旧 GitHub アプリが退役 ／ Cowork / Autopilot の Engage プラグインが GA（MC1530609）
- **11月中旬**: Office in Copilot の展開（MC1530611） ／ Agent Builder のプロンプトのスケジュール実行が開始（MC1302906・10月末から延期） ／ Viva Insights の GitHub Copilot 指標が既定オン（MC1523085）
- **11/17**: Gems が Gemini アプリの設定パネルへ移動 ／ Gemini API の TTS・Live プレビュー5種が停止（最短日）
- **11/17〜20**: Microsoft Ignite
- **11/20**: Copilot Studio のコスト管理を M365 管理センターへ移す機能が GA（MC1530368）
- **11/24 以降**: `claude-opus-4-5-20251101` の暫定退役日（確定日ではない）
- **11/30**: Power Apps のモデル駆動アプリの説明文の AI 生成・Plan Designer の共同編集・レコード単位の在席表示が退役 ／ `claude-sonnet-4-5-20250929` が Claude API から退役 ／ OpenAI の Evals・`v1/prompts`・Agent Builder が停止 ／ Gemini 4 Argon の導入価格が終了 ／ Azure DevOps コネクタの旧接続が認証不可に（MC1508508） ／ App Builder と vibe.powerapps.com が退役 ／ Power Automate の Describe it to design it の退役は非推奨一覧から消えた（撤回かは未確認）
- **12/1**: M365 Copilot の前提サブスク不要オファー開始 ／ Copilot Business の従量課金が既定オン ／ Gemini 4 Argon の単価が $4/$20 に倍増 ／ Google スライドの複数スライド作成の上限引き上げ優待が終了しうる
- **12月上旬**: Copilot アプリのタスクバー固定にライセンス別の選択肢が入る（MC1530612）
- **12/11**: Power Apps の式の生成・Power Apps Ideas・Copilot によるコントロール名の変更が退役
- **12/14**: claude.ai/design の単体サイトが閉鎖
- **12/15**: アンマネージド開発者環境が停止
- **12/31**: Power Platform の環境間のコメントのインポート・エクスポートが終了 ／ Claude Security の無償クレジット（月 $25,000×2か月）の対象期間が終了 ／ Gemini 4 Carbon の導入価格の割引が終了
- **2027-01-06**: OpenAI `tts-1` / `tts-1-hd` / `gpt-4o-mini-tts` 2版が停止
- **2027年1月**: Targeted release が退役 ／ Copilot Studio の Teams アプリで編集ができなくなる（MC1511056）
- **2027-01-14**: OpenAI の GPT-4o・GPT-4o mini・GPT-4.1・GPT-4.1 mini が API から削除（→ `gpt-6-luna`）
- **2027-01-15**: アンマネージド開発者環境の削除開始 ／ Claude Code Review の Enterprise 向けクレジット請求期限
- **2027年1月中旬〜下旬**: 旧来の Teams 保持ポリシーが Copilot の対話に効かなくなる（MC1481313）
- **2027-03-01 以降**: Gems 廃止（Business / Enterprise）
- **2027年3月**: Purview の DSPM classic / DSPM for AI classic が退役（MC1481315・1月から延期）
- **2027年3月末**: Outlook の Copilot Prioritize の削除が完了（MC1519861） ／ SharePoint / OneDrive の `.agent` 形式エージェントが動かなくなる（MC1511052）
- **2027-04-01**: OpenAI `gpt-5.1` / `gpt-5.3-codex` / `gpt-5.4-nano` が停止

## 改善メモ

- 新規提案: 3ソースとも新規起票なし
- 継続提案: Copilot は継続2件（最多 B-080 Cowork の Learn URL 差し替え、5回目。B-081 ハーネス改名は Learn が本日も旧名のまま、3回目） ／ industry は継続5件（最多 B-040 セキュリティ開示の定点、13回）。B-007 は Microsoft・Amazon の決算を IR 一次で取れた実例で6回目。見送り候補 B-023 ／ Master は記録なし
- 障害の変化: industry が `www.bbc.co.uk` のゲートウェイ拒否を新規に記録した。Master・Copilot は記録なし
- 訂正: 昨日（10/30）の本サマリーがハイライト1に載せた Power Automate の Describe it to design it の退役は、非推奨一覧から節が消えた。撤回の一次は無いため昨日分は書き換えず、本日の [観測] 項目と注目予定の注記で扱った
- ソース間の差分・矛盾:
  - GPT-6 Rosalind の価格は、Master が「価格とモデルページは未掲載」、industry が料金ページの単価（入力 $15・出力 $75 など）を記載した。日次は industry の一次（料金ページ）を採り、タグは [新機能] にした（Master は [セキュリティ+新機能]）
  - Claude Code `2.1.314` のタグは、Master が [破壊的変更+新機能]、industry が [新機能] とした。日次は `FORCE_HYPERLINK=false` の意味の反転と `claude -p` の終了コード変更を破壊的変更とみて Master のタグを採った
  - Gemini API の Computer Use GA は、industry だけが対応モデル4種と操作対象を書いている。日次は両方を統合した
