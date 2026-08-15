# AI News Daily Summary — 2026-08-16

日曜は、待っていた値上げが本日発効し、選べるはずだったモデルが選べないと判明した日である。DeepSeek の新単価は 16:00 UTC（日本時間 8/17 1:00）に切り替わり、値上げ告知と同じ 8/13 に V4-Pro の重みが MIT で公開されていたことも今日はじめて分かった。Copilot Studio では、本サマリーが 7/25 以降くり返し「GA 最新」と書いてきた Claude Sonnet 5 が、一次のモデル可用性一覧では GitHub Copilot ハーネス限定・米国の早期アクセス環境限定だった。手元のツールでは Claude Code v2.1.233 が npm `latest` へ昇格したが、`stable` は9版遅れのままで、Windows のパス検証バイパス修正はそこに届いていない。

## 今日のハイライト

### 1. DeepSeek の新単価が本日 16:00 UTC に発効する — 同じ日に V4-Pro の重みが MIT で公開されていた

**要点**: DeepSeek が V4-Flash / V4-Pro の API 単価を最大11倍に引き上げ、本日 16:00 UTC に発効する。値上げ告知と同じ 8/13 に V4-Pro の重みが MIT で公開されており、前提が「安い API」から「高い API とセルフホストの二択」へ変わる。

**詳細**: 告知は 8/13、発効は **2026-08-16 16:00 UTC**（＝日本時間 8/17 1:00）。新料金は時間帯で二段になり、ピーク帯は UTC 01:00〜04:00 と 06:00〜10:00（日本時間 10:00〜13:00 と 15:00〜19:00）、それ以外のオフピークはピークの半額である。日本のオフィス時間はピーク帯とほぼ重なる。

- V4-Pro 出力: $0.87 → ピーク $3.96 / オフピーク $1.98（ピークで約4.6倍）
- V4-Pro 入力（キャッシュミス）: $0.435 → ピーク $1.32
- V4-Flash 出力: $0.28 → ピーク $1.32 / オフピーク $0.66
- V4-Flash 入力（キャッシュミス）: $0.14 → ピーク $0.44

上げ幅はモデル・トークン種別・時間帯の組み合わせで50%から1,100%超まで開く。DeepSeek は改定理由を「リソースをより合理的に配分するため」と説明している。

同じ 8/13 に **V4-Pro-0813 の重みが MIT ライセンスで公開**されていたことが、本日はじめて確認された。Hugging Face API の実測で `deepseek-ai/DeepSeek-V4-Pro-0813` は `private: false` / `gated: false`、safetensors 66シャード、`safetensors.total` 1,650,497,936,906（約1.65T・うち I8 が 1.62T）、作成 2026-08-13T03:05 UTC、ダウンロード 19,945 / likes 483 である。二次情報では総パラメータ 1.6T / アクティブ約49B、コンテキスト 1,048,576、出力上限 384,000、Terminal Bench 2.1 で 87.9、DeepSWE で 62.7。値上げと重み公開が同日である以上、セルフホストが今回の改定の受け皿として置かれていると読める。

⚠️ 一次3ホスト（`www.deepseek.com` / `api-docs.deepseek.com` / `platform.deepseek.com`）はいずれもゲートウェイ拒否で、価格の数値は二次報道の一致による。重み公開だけは Hugging Face API で一次確認した。⚠️ 本サマリーは 8/13 の重み公開を3日間検出できず、発効当日の本日に初検出した。

- https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro-0813
- https://qz.com/deepseek-api-price-increase-v4-peak-off-peak-081326
- https://www.scmp.com/tech/tech-trends/article/3363129/deepseek-signals-significant-price-hike-amid-surge-demand-low-cost-ai-models
- https://fortune.com/2026/08/13/deepseek-increases-prices-for-ai-services-by-multiple-times/

### 2. Copilot Studio の Claude Sonnet 5 は GitHub Copilot ハーネス限定だった — 標準ハーネスのエージェントでは選べない

**要点**: モデル可用性一覧を一次で読むと、Claude Sonnet 5 には GitHub Copilot ハーネス限定の脚注が付き、米国の早期アクセス環境にしか出ない。本サマリーが 7/25 以降「外部モデル選択の GA 最新」と書いてきた前提は誤りで、記録を訂正する。

**詳細**: ハイライト1と同じ日に公開された運用ガイダンスが「モデル可用性の権威ある情報源」と名指しした `authoring-select-agent-model` を一次取得して判明した。Copilot Studio の What's New 側にはハーネスの限定が書かれておらず、June 節の記載だけを引いていたために取りこぼしていた。⚠️ 本項は本日の変更ではなく、これまで取りこぼしていた制約の回収であり、変更日は特定できない。

同じ表から読める現在の提供状況は次のとおりである。

- 既定モデル: GPT-4.1 が全13リージョンで Default になっている。US Government（GCC / GCC High / DoD）だけは GPT-4o が Default のまま
- 退役済み: GPT-4o と Claude Sonnet 4.5 が公開リージョン全件で Retired になっている
- cross-geo が外れている組み合わせ: GPT-5 Chat は英国・米国・オーストラリア・欧州、GPT-5.5 Chat は欧州と米国のみに限られる。それ以外の地域は域外処理を伴う
- 実験モデルは米国の早期アクセス環境に集中している: GPT-5.3 Chat / GPT-5.4 Reasoning / GPT-5.5 Reasoning / Grok 4.1 Fast がこの扱いで、Mistral Medium 3.5 だけが全リージョンで Experimental

⚠️ Grok 4.1 Fast（Non-Reasoning）には、Microsoft の安全性・責任ある AI 評価で**他モデルより整合性が低い**と判定された旨と、有害コンテンツ生成のリスクが高く脱獄ベンチマークのスコアが低い旨が明記されている。Microsoft のコンテンツ安全システムが覆っていない種類の危害がありうるとも書かれており、本番利用は推奨されていない。

- https://learn.microsoft.com/en-us/microsoft-copilot-studio/authoring-select-agent-model

### 3. Claude Code v2.1.233 が npm latest へ昇格した — auto mode の承認回帰と Windows のパス検証バイパスは stable に届いていない

**要点**: Anthropic が v2.1.233 を `latest` へ昇格させ、Windows のパス検証バイパスと 2.1.232 の auto mode 回帰を修正した。npm の `stable` は v2.1.224 のままで、既定チャンネルに固定した組織には9版ぶんの修正が届いていない。

**詳細**: npm publish は 8/14 18:50 UTC、GitHub releases は 8/14 22:20 UTC。前回チェック時点では npm `next` にしか存在せず changelog にも未掲載だった版で、本日 `latest` へ昇格し、`code.claude.com/docs/en/changelog` / GitHub releases / npm `latest` の3ソースで最上位が一致した。

- セキュリティ: Windows の NT device path が UNC 検証を迂回する問題を修正した
- auto mode: 2.1.232 には通常の Bash コマンドでも手動承認を求め続ける回帰が入っており、auto mode が Pro / Max / Team の既定になった当日に修正版が出た。8/14 以降に「承認が減らない」と観測した場合、設定ではなくバージョンを先に疑うことになる
- タスク管理ツール: TaskCreate / TaskGet / TaskUpdate / TaskList と TodoWrite が新しいモデルでは既定で無効になり、戻すには `CLAUDE_CODE_ENABLE_TODO_TOOLS=1` が要る
- GitLab: `--worktree` と `claude agents` が MR の URL を受け付けるようになった（MR は `!N` 形式で表示される）
- 費用配賦: apps gateway に opt-in の `forward_user_identity` が加わり、サインイン中ユーザーの identity をヘッダで送るため、ゲートウェイ背後のプロキシがユーザー単位で費用を按分できる
- 環境変数: `CLAUDE_CODE_TOOL_MEMORY_LIMIT` で Linux の Bash ツール実行に memory cgroup を掛けられ、`CLAUDE_CODE_WEBFETCH_CACHE_TTL_MS` で WebFetch の URL キャッシュ TTL を設定できる
- 修正: MCP v2 接続が `subscriptions/listen` ストリームを開き続ける問題、権限プロンプトで Notification hooks が発火しない問題、環境シャットダウン時にクラウドセッションが lost 扱いになる問題、プラグインと MCP 併用時の同梱 skill エイリアスを直した

npm `dist-tags` の実測は **`{stable: 2.1.224, latest: 2.1.233, next: 2.1.233}`** である。前日は `{stable: 2.1.223, latest: 2.1.232, next: 2.1.233}` で、`stable` は1版しか進まず `latest` との差は9版のままになっている。この9版には本日の NT device path 修正のほか、auto mode の既定化と、PowerShell および Windows の権限バイパス修正3件が含まれる。「最新版で修正済み」と「手元で修正済み」は別物であり、changelog と GitHub releases だけを見ているとこの差は見えない。

- https://code.claude.com/docs/en/changelog
- https://github.com/anthropics/claude-code/releases/tag/v2.1.233
- https://registry.npmjs.org/@anthropic-ai/claude-code

## カテゴリ別まとめ

### Copilot Studio / Power Platform

- Microsoft が Copilot Studio ガイダンスハブに8月節を新設し、AI モデルのライフサイクル管理を扱う新規記事3本を公開した（`updated_at` は 2026-08-11T19:03Z）。「よいモデルが出たら選び直すだけ」ではなく評価ゲートを通す移行案件として計画せよ、という位置づけである。3本は入口の `plan-agent-model-lifecycle`（発見とインベントリ）、`manage-agent-model-upgrade`（判断と退役対応）、`manage-agent-model-migration`（評価・承認・展開・監視）で構成され、運用サイクルは発見 → インベントリ → 評価 → 承認 → ALM 経由の展開 → 監視 → 反復の7段になる
  - 既定モデルの自動切り替え: 既定モデルを使うエージェントは、既定が更新されるたび計画の有無にかかわらず別モデルへ移る。重要度・流量の高いエージェントは既定を追わず特定モデルを明示せよ、としている
  - 退役後の猶予は30日: エージェントの Settings > Model で「Continue using retired models」を有効にすると退役モデルを30日間使い続けられる。設定はエージェント個別で、期限までに移行を終える前提の一時措置である
  - 最頻の失敗は用途カテゴリの取り違え: 高頻度の FAQ エージェントを *general* から *deep* へ上げると、回答品質はわずかに上がる一方で遅延とクレジット消費が跳ね上がり、体験と費用の両方で純粋な後退になる
  - 外部モデルだけ管理者操作が2箇所要る: Power Platform 管理センターでの有効化に加え、Microsoft 365 管理センターでプロバイダーごとの許可が要る。プレビュー/実験モデルの設定とは独立しており、片方を開けても他方は開かない
  - インベントリの取り方: Power Platform 管理センターは Manage > Copilot Studio の Model 列と、Licensing > Copilot Studio > 環境 > Message consumption details の LLM Model 列の2経路がある。テナント横断で機械的に集めるには inventory API（`microsoft.copilotstudio/agents` を `properties.model` 付きで射影）を使う。⚠️ **`pac copilot list` はモデルを返さない**ため、退役対応の洗い出しには使えない
  - 評価側の制約: 評価結果の保持は89日（超えるぶんは CSV へ書き出す）、標準ハーネスのテストセットは100テストケースが上限、遅延とクレジット消費は評価が計測しないため別に測る必要がある。ロールバックは設定の切り戻しではなく検証済みソリューションの再展開になるため、展開前のゲートで止めるほうが安いとしている
- ガイダンスハブの7月節には、Copilot Agent Kit の新規記事5本（Agent Debugger / Agent Library / Agent Insights Hub / Power Shield / Agent Review Pipeline）と、*Copilot Studio Kit* から *Copilot Agent Kit* への改称の第1フェーズも記録されていた。本サマリーが Power CAT のリリース経由でしか追えていなかった情報がここに集約されている
- Copilot Studio の What's New は節構成が June 2026 のままで、7月節も8月節も追加されていない。June 節の10項目にも増減はない。⚠️ GitHub Copilot ハーネスは 8/3 に GA しているのに `(Production-ready preview)` の表記が残ったままで、未反映が13日連続になった
- Copilot Studio の Released Versions は **2026.6.3**（6/30 初出）のままで、6/30 以降6週間半にわたって新ビルドが出ていない。リージョン分布と UX 版 26.06.21-24 にも変化はない。次の定例は 8/18 で、ここでも更新がなければ7週間の空白になる
- Copilot Agent Kit（Power CAT）は 8/14 の August 2026 版（タグ `CopilotStudioAccelerator-August2026`）が最新のままで、本日の新規リリースはない。`releases.atom` 上では June 2026 版のエントリが 8/13 に更新されているが、既存リリースの編集であって新規ではない
- Power Platform の Release Wave（`power-automate` / `power-apps` の `planned-features`）は 8/15 と完全に同一で、緑チェックの追加・期日変更・行の増減はいずれも発生していない。期日超過は延べ6行（GA 列5件・Public preview 列1件）、8月期日は10件、9月期日は6件のままである。2026 Wave 1 の対象期間は9月末までで残り約1か月半になる
- Power Platform Blog の親ページは 8/13 の PPCC 2026 登録記事が先頭のままで、8/6 公開の月次合併号は依然として一覧に現れない（不完全レンダリングは継続）。Power Automate Blog / Power Apps Blog も同じ記事が先頭である。⚠️ PPCC 2026 の標準価格での登録は **8/18** までである
- Power Platform の非推奨一覧の先頭は Power Automate モバイルアプリの廃止（**8/31** 発効・残り15日）のままで、次回確認は 8/20 である
- Copilot Studio Blog（Tech Community）は 8/3 の記事、Microsoft Copilot Blog は 7/21 の記事が最新のままで、いずれも本日の新規はない

### Microsoft 365 Copilot / GitHub

- GitHub が Copilot CLI の pre-release v1.0.81-0 を出した（8/14 23:47 UTC）。内容は「モデル構成の更新」1点のみで、機能追加はない。安定版は v1.0.80（8/14 02:28 UTC）に据え置かれている
- `github.blog/changelog` は 8/14 の Grok 4.6 提供開始が最上位のままで、8/15 の追加はない（同一日の取りこぼしを避けるため「8/14 以降を全件」の形で確認した）
- M365 Copilot Release Notes は **August 11, 2026** バッチのままで、本日の新バッチはない。本文を取得して先頭の見出しと節構成7本（extensibility 2 / SharePoint 1 / Outlook 2 / Microsoft 365 Copilot 1 / PowerPoint 4 / Viva Insights 1 / Word 1）が 8/15 と一致することを確認した。次バッチは 8/25 前後の見込みである
- 拡張機能の What's New は「July 2026」節が最新のままで、8月節は立っていない（`ms.date` 7/15・`updated_at` 7/29）。Microsoft 365 Roadmap・Microsoft 365 Blog（本体）・M365 Developer Blog・Tech Community の M365 Copilot Blog も、いずれも本日の新規がない
- ⚠️ Tech Community の M365 Copilot Blog は、board RSS のエントリ並びが 8/13 → 8/12 → 8/5 → 8/7 → 7/31 → 8/4 → 7/24 で投稿日の降順になっておらず、乱れが3日連続で再現した
- ⚠️ Message Center の一次取得は9日連続でできていない（ゲートウェイ拒否）。WebSearch 照合でも 8/15 に検知した MC1454386（モバイルアプリからの Copilot Chat 到達の簡素化）より新しい索引は出ておらず、二次スニペットのみのため掲載内容と展開時期は引き続き採用していない
- 既報: Grok 4.6 の Copilot 追加（8/14・Business / Enterprise は既定オフ）、Gemini 3.7 Flash の追加（8/13・同じく管理者の有効化が必要）、Copilot CLI の Agent Host Protocol（8/13）
- 期限: Copilot 既定モデル有効化ポリシー発効（**8/26**）、GitHub Spark 退役（**8/31**）、モデル廃止（**9/1**）、MAI-Code-1-Flash 廃止（**9/10**）

### Anthropic / Claude

- Claude Code v2.1.233 が最新である（ハイライト3参照）。8/15 以降の新版はない
- Anthropic が JetBrains による Claude Fable 5 の評価・配備事例を公開している（8/13・既報）。08-15 に 03 側が本文を取得できず 01 側の値を採用した項目で、本日 03 側も本文取得に成功し、Python 合格率 **44.3%**（Opus 4.8 は 28.2%）・落としたタスク2件・手数が約22%減という数値が両ソースで一致した。CTO の Vladislav Tankov はモノレポを含む非公開リポジトリ上に大規模な評価セットを維持し、品質・タスクあたり費用・速度の3軸で社内リーダーボードを回していると説明している。配備先は複雑な推論を要する協働作業、IDE コンポーネント実装の長時間エージェント実行、自社製品に対するホワイトボックスの脆弱性検査、フレームワーク移行と言語間のコード変換である
- Anthropic が Claude Tag を「チャンネル全体の文脈で発言可否を判断する」形へ変えている（8/13・既報）。自社計測で判定が約30%改善したとしており、対象は Claude Teams と Enterprise で追加費用はなく、拡張した文脈は利用量・支出上限に算入しない
- Anthropic 自身が Claude Tag で Slack のセルフサービス分析を回している事例が 8/13 に公開されていた。中核は会話のたびに更新されるスキルファイルとして供給する「統制されたセマンティックレイヤー」で、精度は約95%、あるデータチャンネルでは明示的なメンションなしに75%超の質問へ回答し、応答は通常1〜2分だとしている
  - 接続: データウェアハウスへはスコープを絞ったサービスアカウントで接続し、統制済みの出力テーブルとキュレーション済みマートのみ参照する
  - 秘匿: 列レベルの PII 分類により、テーブルへアクセスできても機微な列はエージェントから見えない
  - 権限: チャンネルへの追加そのものを読み取り権限の付与として扱い、データチームが管理する
  - 監査: クエリにラベルを付けて費用の帰属と監査証跡を残す。計測は「統制レイヤーの利用率 対 場当たりの SQL」と「ドメイン別の訂正率」の2指標で行う
- Claude API release notes は 8/11 が最上位のままで、8/12〜8/15 の追加はない。`support.claude.com` の Release Notes も 8/6 の skill / plugin セキュリティスキャン beta が最上位のままで、10日連続で動きがない
- `www.anthropic.com` はオリジン403が継続している。日付入りの WebSearch を実行したが、新規の製品発表は返らなかった
- 期限: Claude Code の週次上限50%増は **8/19 23:59 PT** で終わる

### OpenAI

- OpenAI が macOS 版 ChatGPT に Computer History を追加した（8/13）。承認したアプリとサイトの操作が検索可能なタイムラインと記憶になり、ChatGPT と Codex が参照する。対象は ChatGPT Pro / Business / Enterprise で、提供対象外の地域は EEA・スイス・英国である。記録するのは macOS のアクセシビリティ機能が露出する操作イベント（クリック・タイピング・キーボードショートカット・アプリ切替）で、画面のスクリーンショットではない。イベントは OpenAI 側のサーバーで処理されて記憶に変換され、処理後は保持せず学習にも使わないと同社は説明している。生成された記憶は**ローカルに平文の Markdown ファイル**として置かれ、削除するまで残る。⚠️ OpenAI 自身が、アプリやサイトの悪意ある内容によるプロンプトインジェクションのリスクが上がると警告し、機微情報を含むアプリの除外を推奨している。位置づけとしては research preview だった Chronicle（画面キャプチャ方式）の作り直しにあたる
- ChatGPT の Linux デスクトップアプリが public preview で公開されていた（8/11・5日遅れの初検出）。対応は Ubuntu 24.04 / 26.04 LTS・Debian 13・Fedora 43 / 44 で、`.deb` と `.rpm` を x64 / ARM64 向けに配布する。ChatGPT・ChatGPT Work・Codex が動き、内蔵ブラウザと Chrome でのブラウザ操作は使えるが、他のデスクトップアプリの操作には未対応である。これで Codex が macOS / Windows / Linux の主要デスクトップ3系統で揃った
- OpenAI が ChatGPT Voice をアップロード済みファイルと Projects に対応させ、あわせて Record & Replay を EU・英国・スイスで利用可能にした（いずれも掲載日は未確定）
- Codex CLI の pre-release は **0.148.0-alpha.19**（8/15 02:21 UTC）が最新で、前回の alpha.16（8/14 17:18 UTC）から3版進んだ。安定版は 0.147.0（8/7 01:41 UTC）に据え置かれ、0.148.0 の安定版は未リリースである。⚠️ alpha 各版の個別リリースノートはページ側のエラーで表示されず、内容は3日連続で確認できていない
- `developers.openai.com/api/docs/changelog` は 8/13 の Ultrafast モードが最上位のままで追加はない。⚠️ 課金レートは依然として未確定である。`community.openai.com` の Announcements RSS も 8/10 の Daybreak 拡大告知が最新のままである
- 既報: GPT-5.4 / 5.4 mini の Codex 除外（**8/31**・移行先は `gpt-5.6-terra` / `gpt-5.6-luna`）、GPT-5.6 Luna 80%減・Terra 20%減（7/30）
- 到達性: `community.openai.com` と `developers.openai.com` は 200。`openai.com` / `help.openai.com` / `platform.openai.com` はオリジン403、`learn.chatgpt.com` はゲートウェイ拒否が継続している

### Google / DeepMind

- Google が FHE コンパイラ **HEIR** を Private Computing Toolkit の一部として公開した（8/15）。完全準同型暗号向けの MLIR ベースのコンパイラツールチェーンで、学習済みモデルを FHE 対応の形へ自動変換し、復号せずに暗号化された入力のまま推論を走らせる。想定用途はレコメンドや不正検知で、これまで暗号研究者の専門知識を要した FHE の導入障壁を下げる位置づけになる。対応スキームとバックエンドは OpenFHE と Lattigo が BGV / BFV / CKKS、tfhe-rs と Jaxite が CGGI で、ライセンスは Apache 2.0 である。⚠️ リポジトリには「これは Google の公式サポート製品ではない」と明記されており、提案に載せる場合は本番運用の前提として書かない
  - https://github.com/google/heir
- Gemini API の単価は据え置きで、導入価格の適用範囲も 08-15 から変化がない。3.7 Flash と 3.6 Flash の両方に入力 **$0.75** / 出力 **$3.75**（100万トークン）が掲載された状態が続き、有効期限は 2026-12-31、2027年1月1日以降は $1.50 / $7.50 へ戻る。3.5 Flash（$1.50 / $9.00）・3.5 Flash-Lite（$0.30 / $2.50）・3.1 Flash-Lite（$0.25 / $1.50）・3.1 Pro Preview（入力 $2.00〜$4.00 / 出力 $12.00〜$18.00）も変更はない
- Gemini API changelog は 8/13 の Gemini 3.7 Flash GA が最上位のままで、8/14・8/15 の追加はない。Gemini 3.5 Pro の GA は未ローンチが継続している（I/O 発表後に 6月 → 7月 → 7/17 と3回スリップした）
- ⚠️ 登録済みの Google 系5ソースはゲートウェイ拒否が続いており、到達できる Google 一次は未登録の `ai.google.dev` だけである。`blog.google` も拒否されたため、HEIR の公表日は二次確認による
- 退役カレンダー: Imagen 4.0 系3本の停止は **8/17** で残り1日である

### モデル・料金の動き

- DeepSeek の新単価が本日発効する（ハイライト1参照）
- Qwen3.8-27B（8/14 公開・既報）は本日時点でダウンロード **91,917** / likes 9,680 に達している。FP8 版 `Qwen/Qwen3.8-27B-FP8` は 123,157 ダウンロードである。ベンチ値はベンダー自己申告で第三者検証値ではなく、パラメータ数は一次モデルカードの「27B」と二次報道の「27.78B」が食い違うため一次を採っている
- 8/14〜8/15 に新規公開されたオープンウェイトモデルはない。`Qwen` / `moonshotai` / `deepseek-ai` / `meta-models` / `mistralai` / `zai-org` / `openai` / `google` の計8 org について Hugging Face の作成日降順一覧を実行し、8/13 の `deepseek-ai/DeepSeek-V4-Pro-0813` より新しいリポジトリが1件もないことを確認した

### MCP / 開発ツール

- MCP 公式ブログは新着がなく、RSS の最新は 7/28 の `The 2026-07-28 Specification` のまま19日連続で動きがない。Tier 1 SDK にも変化はない（TypeScript `@modelcontextprotocol/server` / `client` ともに 2.0.0、Python `mcp` 2.0.0、C# v2.0、Go は v2 未発行で `go-sdk` v1.7.0 が仕様対応）
- Devin が Automations にキューイング対応を追加していた（8/7・二次）。Automation ごとに同時実行数の上限とキューの深さを設定でき、events テーブルでキューのライフサイクル状態を、activity chart で実行状況を確認できる。あわせて GitLab トリガーと production automations API が入っている。⚠️ `docs.devin.ai` はゲートウェイ拒否が継続しており一次未確認である
- Cursor の changelog は 8/13 の Cloud Agents Builds が最上位のままで、フォーラムも 8/12 の Grok 4.6 関連2件が最新である
- ⚠️ xAI は一次に到達できない状態が継続している（`x.ai` / `docs.x.ai` がゲートウェイ拒否）。8/14〜8/15 の新規発表は二次でも確認できなかった
- 既報: Devin の Side Chats（8/12）、Devin Outposts（自環境実行・既定無効）、Grok 4.6（8/12）

### 国内・市場

- アジアクエストが AI エージェント向けアクセス基盤「GAIA Governed AI Access」の提供を開始した（8/14）。複数の AI エージェントと社内業務システムの間に入りデータアクセスを制御・記録・管理するクラウド型のプラットフォームで、権限パススルーによるデータ参照と全アクセスの自動ログ記録を特徴とする。狙いは「野良 AI エージェント」経由の情報漏洩リスクを下げることに置かれている。特定の AI モデル・製品に依存しない中立な基盤として設計され、接続規格は MCP 準拠、対応 AI は Claude・ChatGPT・Gemini・Copilot 等である。08-09 収録のソフトバンク AGENTIC STAR の LLM Gateway と同じく、統制点を利用者側から管理者側へ寄せる国内プロダクトが続いている。⚠️ `www.asia-quest.jp` の一次リリースはゲートウェイ拒否のため、内容は PR TIMES と二次報道の突き合わせによる
  - https://prtimes.jp/main/html/rd/p/000000214.000019319.html
- Partner Center の8月アナウンスは 8/14 付の14件目までで、本日の追記はない（`updated_at` も 8/14 のまま）。既報14件の内容にも変化はない
- Microsoft Purview の8月節は 8/15 に検知した Sensitivity labels の2件（自動ラベル付けポリシーのシミュレーションモード、ポリシー詳細パネルの Insights タブ）のままで、本日の追加はない。⚠️ 8月節に Copilot 固有の項目は依然として含まれていない
- SharePoint Blog（8/6 の月次記事）と Agent 365 Blog（8/6 の月次記事）は、いずれも本日の新規がない
- IDC / IDC Japan・MM総研・Similarweb・NRC はいずれも更新がない。直近で引用可能な国内の基準値は IDC の 2026年3月予測（国内 AI 市場支出額が 2025年 2兆3,725億円 → 2029年 6兆8,897億円・CAGR 36.0%）と、総務省 令和8年版情報通信白書（企業の生成AI業務利用 86.4%）のままである
- `developer.apple.com` は 200 で、8/12 の年齢レーティング更新以降に新規がない。AI 関連の最新は 8/5 のままで、iOS 27 / iPadOS 27 は developer beta 4（7/20・ビルド 23G71）が最新、GA は9月（予想 9/14 前後）の見込みである

## 直近の注目予定

- **8/16（本日）**: DeepSeek V4-Flash / V4-Pro の新単価が発効（16:00 UTC ＝ 日本時間 8/17 1:00・ハイライト1参照）
- **8/17**: Claude Console 旧 Workbench 退役と実験的プロンプトツール API 廃止 ／ Gemini API の Imagen 4.0 系3本停止 ／ Gemini in Classroom のモバイル開放 ／ MS-4005 と Power Platform Weekly の週次確認
- **8/18**: 業務用 Copilot の URL 移行開始（`copilot.cloud.microsoft`）とデスクトップ早期プレビュー ／ PPCC 2026 の標準価格での登録期限 ／ Copilot Studio Released Versions の次回定例 ／ Copilot Studio 課金ページの週次確認
- **8/19**: Claude Code の週次上限50%増が終了（23:59 PT）
- **8/20**: Gemini Enterprise Agent Platform の Grok 4.1 ファミリー停止（一次未確認） ／ Pixel 11 系の出荷開始 ／ 非推奨一覧と Release Wave の週次確認
- **8/22**: M365 Copilot アプリのチャット中心 UI が Deferred リングへ展開開始（MC1325422）
- **8/25 前後**: M365 Copilot Release Notes の次バッチ（隔週サイクルどおりなら）
- **8/26**: OpenAI Assistants API 廃止 / o3 退役 / GPT-4.5 完全廃止 ／ Copilot 既定モデル有効化ポリシー発効
- **8/27**: IT Nation Connect ANZ の Microsoft セッション
- **8/30**: 公式 DALL·E GPT の退役
- **8/31**: GitHub Spark の既存ユーザーアクセス終了 ／ `gemini-robotics-er-1.6-preview` 停止 ／ GPT-5.4・5.4 mini が Codex から除外 ／ Claude for Government の $1/機関プログラム終了 ／ Power Automate モバイルアプリ廃止 ／ CSP Copilot Partner Council コンテストの応募期限
- **9/1**: GitHub Copilot の全体験でモデル廃止 ／ OpenAI Daybreak で全アカウントにハードウェアセキュリティキー必須化 ／ MAICPP 契約の更新条項が自動発効
- **9/2〜9/3**: Windows 365 Frontline 名称での購入最終日（9/2）と Windows 365 Flex への改称（9/3）
- **9/10**: MAI-Code-1-Flash が全 Copilot 体験から廃止
- **9 月**: iOS 27 / macOS 27 GA ／ auto mode の既定化を Enterprise・API・各クラウドへ拡大予定 ／ 9月中旬に Copilot デスクトップアプリの広範な展開開始 ／ 9月末に 2026 Wave 1 の対象期間終了 ／ 9/30 に M365 E7 プロモーションの対象購入最終日と M365 E5・E3 の CSP 割引終了
- **10 月**: Anthropic の IPO 予定（$2T 超の評価額を目標と報道） ／ 10/1 に M365 E7 プロモーションの新規取引停止と CSP ソフトウェアの5%上乗せ発効 ／ 10/20〜22 に SMB Copilot Partner Council（NYC） ／ 10/25〜30 に PPCC 2026 本編とワークショップ
- **11/1**: パートナー特典の有効期限がオファー購入日基準へ移行
- **12/2**: EU AI Act の生成コンテンツ標識義務、8/2 以前に市場投入済みシステムへの猶予終了
- **12/31**: Gemini 3.6 Flash / 3.7 Flash の導入価格終了（$0.75 / $3.75 → $1.50 / $7.50） ／ M365 E3 プロモーション・Copilot in 30・Purview Suite 50%オフの提供終了
- **2027年6月末**: Frontier Partner バッジの廃止

## 改善メモ

- 本サマリー自身の記録に訂正が1件出た。Copilot Studio の外部モデル選択について 7/25 以降「Sonnet 5 / GPT-5.5 Chat が GA 最新」と書いてきたが、一次のモデル可用性一覧では Sonnet 5 が GitHub Copilot ハーネス限定・米国の早期アクセス環境限定である（ハイライト2）。What's New の節だけを追い、可用性一覧を読んでいなかったことが原因にあたる
- 検出遅れが2件ある。DeepSeek V4-Pro-0813 の MIT 重み公開（8/13）は発効当日の本日に3日遅れで初検出し、ChatGPT の Linux デスクトップアプリ（8/11）は5日遅れの初検出だった。DeepSeek は 01 側の `daily-sources.md` に1項目も登録されていない
- ソース間の食い違いは解消した。08-15 に記録した JetBrains 事例の不一致（01 は本文取得済み・03 は 404）は、03 側が一覧ページから href を確定させる手順で本文取得に成功し、定量値が両ソースで一致した。03 側は障害ではなく手順の問題と確定させている
- 取得できていないソースは次のとおり。Message Center は9日連続で一次取得できず、MC1454386 が未掲載のままである。Codex CLI の alpha 各版リリースノートはページ側エラーで3日連続未確認である。Copilot Studio の課金レート USD 単価は取得できない PDF にしかなく、Qiita / Zenn の記事にある具体値は一次に存在しないため採用していない
- 障害の新規登録が3件あった。`pnp.github.io`（PnP 週次アジェンダの一次）、`www.producthunt.com`（03 側の「最優先」登録ソース）、`www.asia-quest.jp`（GAIA の一次リリース）がいずれもゲートウェイ拒否を返した。02 側のゲートウェイ拒否ホストは7本になった
- 各ソースの改善提案は 01 が新規 B-036（DeepSeek のソース登録とオープンウェイト系ベンダー料金ページの監視）を追加して継続14件、02 が新規 B-034（ガイダンスハブ What's New の登録）と B-035（モデル可用性一覧の登録）を追加して継続16件、03 は新規なしで継続8件である。⚠️ 02 の継続提案は 08-15 の17件から16件へ減っているが、減った理由の記載がない
