# AI News Daily Summary — 2026-08-17

月曜は、締切を近い順に並べ替える日である。Copilot Tuning は 8/20 に止まり、そこまでに終わらない調整実行は破棄される。Manus は Meta 買収の解消にともない、買収後に作られたユーザーデータを 8/23–24 に消す。値上げの側では DeepSeek の新単価が日本時間の本日 1:00 に発効し、倍率が最大なのは出力ではなくキャッシュヒット入力の12倍だった。手元のツールは静かで、Claude Code v2.1.233・Copilot CLI v1.0.81-0 のいずれも週末に新版が出ていない。そのかわり12日前に出ていた Meta の Muse Code を本日はじめて検出した——学習データの提供に同意すると入力単価が 1/12 になる。

## 今日のハイライト

### 1. Copilot Tuning が 8/20 で止まり Copilot Studio へ移る — 期限までに終わらない調整実行は破棄される

**要点**: Agent Builder のテンプレートによる Copilot Tuning が **2026-08-20** に停止し、Copilot Studio のスキル基盤へ移る。前提が「いつでも調整をやり直せる」から「8/20 までに完了しない実行は破棄される」へ変わる。

**詳細**: 出所は Message Center の MC1454393（8/14 付）である。二次2件が一致して伝えている内容は次のとおり。

- 停止の範囲と期限: Agent Builder の一部の調整可能テンプレートで tuning が一時停止し、8/20 までに完了していない進行中のモデル調整実行は破棄される
- 移行先: Copilot Studio のスキルベースのアーキテクチャへ移る。Skills は Markdown で書く再利用可能な指示書で、6月の新エージェント体験で既に提供されている仕組みにあたる
- Optimization テンプレートは退役する。既存エージェントは動き続け、ファインチューニング済みモデルを使っているエージェントもそのモデルのまま動作する
- 再開の時期は Public Preview が **2026年9月**、GA が **2026年12月**である
- 自動移行はない。管理者は 8/20 までに進行中の調整を終わらせる必要があり、既存の学習済みモデルの再利用方法は追って案内される

⚠️ 一次が読めない状態が構造的に続いている。Message Center アーカイブ（`mc.merill.net`）は10日連続でゲートウェイ拒否で、本日は MC を扱う二次ブログ2本も同じ拒否を返した。本文を読めたのは検索インデックスのスニペットだけである。

⚠️ Learn 側は停止も退役も書いていない。本日 `copilot-tuning-overview` / `copilot-tuning-faq` / `copilot-tuning-optimization-template` の3本を一次取得したが、停止・退役の注記はどこにもなく、3本とも「Frontier 経由の提供は 2026年4月予定」という古い注記を載せたままだった。Learn の掲載を提供中の根拠にすると読み違える類型にあたる。

- https://m365admin.handsontek.net/microsoft-365-copilot-updates-copilot-tuning-transition-microsoft-copilot-studio/
- https://mwpro.co.uk/blog/2026/08/14/mc1454393-microsoft-365-copilot-pauses-current-tuning-and-moves-to-microsoft-copilot-studio/
- https://learn.microsoft.com/en-us/microsoft-365/copilot/copilot-tuning-overview

### 2. Manus が Meta から分離し、買収後に作られたユーザーデータを 8/23–24 に削除する — 猶予は6日

**要点**: 中国当局の命令で Meta による $2B の Manus 買収が解消し、Manus が独立運営に戻った。**2025-12-29 以降に生成されたユーザーデータは 8/23–24 に消える**。復元は 8/25 からで、取り返しのつかない期限が6日後にある。

**詳細**: Meta が買収を完了したのは 2025-12-29 である。中国の NDRC が 2026年4月に、技術輸出と外国投資に関する規制違反を理由として撤回命令を出し、**2026-08-12 に買収が正式に解消**した。3月には共同創業者の CEO Xiao Hong と chief scientist Ji Yichao が北京に召喚され、審査期間中は出国を禁じられていたと FT / Reuters が報じている。

データ削除は分離手続きと一部法域の規制対応として行われ、対象は Meta 買収完了（2025-12-29）以降に生成された分にあたる。削除の実施は **8/23 08:00（シンガポール時間）から 8/24 にかけて**で、ユーザーはそれ以前にバックアップを取り、8/25 以降に復元できる。告知は Manus アプリ内とメールで行われる。

⚠️ 本件はこれまで一度も本サマリーに載っていない。分離の報道は 8/11〜8/15 に複数出ていた。

- https://qz.com/manus-independent-meta-acquisition-china-unwind-081126
- https://www.scmp.com/news/us/article/3363704/facebook-parent-meta-unwind-us2-billion-manus-ai-deal-after-beijing-block
- https://www.trendingtopics.eu/manus-becomes-independent-again-following-2b-meta-deal-and-deletes-user-data/

### 3. Meta のターミナル型コーディングエージェント Muse Code を12日遅れで検出した — 学習データの提供と引き換えに入力単価が1桁下がる

**要点**: Meta が 8/5 に **Muse Code** をベータ公開していた。Claude Code / Codex と同じターミナル常駐型で、学習データの提供に同意すると入力単価が 1/12 になる。「フロンティア級エージェントは高い」という前提が支払い方法の選択次第で崩れる。

**詳細**: 発表は 2026-08-05、Meta Superintelligence Labs から出た初のコーディング専用プロダクトで、状態はベータである。モデルは同時公開の Muse Spark 1.2 にあたる。

- インストールは `curl -fsSL https://dev.meta.ai/install.sh | bash` の1行で、認証は `muse login` のデバイスコード方式である。バイナリは静的リンクで Node.js / Python / Homebrew に依存しない
- 対応 OS は macOS と Linux（x86_64 / arm64）で、ネイティブ Windows はインストーラが明示的に失敗するため WSL2 経由になる
- 1つのジョブが並列サブエージェントに分岐し、各サブエージェントが自分の git worktree を持つ。バックグラウンドエージェントはセッション中ずっと常駐する
- モデル呼び出し・ツール実行・承認・編集を実行前にローカルの event log へ追記する設計で、Meta はこれを replay-exact / restart-safe と表現している。クラッシュしても完了済みステップを失わずに再開できる
- 組み込み skill として `/plan`・`/grill`・`/goal` を持つ

料金は Meta Model API の2ティア制で、同じモデルに2つの ID が割り当てられている。

- 標準ティア: 入力 **$1.25 / 出力 $4.25**（per 1M tokens）、キャッシュ入力 $0.15。プロンプトと生成物は学習に使わない。レート制限はチームあたり 3,000 RPM / 400万トークン毎分
- Contributor ティア: 入力 **$0.10 / 出力 $0.20**、キャッシュ入力 $0.002。プロンプトと生成物が将来の Meta モデルの学習に使われる。レート制限は 60 RPM
- 差は入力で約12倍、出力で約21倍にあたる。長コンテキストの割増料金はない

ベンチマークは Muse Spark 1.2 を Muse Code の中で計測した値が公表されているが、Terminal-Bench 2.1 の 82.9% は 8/6 時点で公式 verified leaderboard に載っていない。初代 Muse Spark の SWE-Bench Verified は 77.4 で、Claude Opus 4.6 の 80.8 / Gemini 3.1 Pro の 80.6 に届いていなかった。

⚠️ 一次3ホスト（`research.meta.ai` / `dev.meta.ai` / `ai.meta.com`）はいずれもゲートウェイ拒否で、上記の数値・仕様は複数の二次情報の一致による。検出が12日遅れた原因はソース定義側にあり、Meta の項目が1つも登録されていなかった。

- https://techcrunch.com/2026/08/05/meta-launches-muse-code-an-ai-agent-for-large-code-bases/
- https://venturebeat.com/orchestration/meta-enters-the-ai-coding-wars-with-muse-spark-1-2-and-muse-code-with-persistent-async-background-agents
- https://www.marktechpost.com/2026/08/05/meta-superintelligence-labs-releases-muse-code/

## カテゴリ別まとめ

### Copilot Studio / Power Platform

- Copilot Tuning が 8/20 で停止する（ハイライト1参照）
- Copilot Studio の What's New は節構成が June 2026 のままで、7月節も8月節も追加されていない。June 節の10項目にも増減はない。⚠️ GitHub Copilot ハーネスは 8/3 に GA しているのに `(Production-ready preview)` の表記が残ったままで、未反映が**14日連続**になった
- ガイダンスハブの What's New は 8/16 に検知した `plan-agent-model-lifecycle`（AI モデルのライフサイクル管理）1本のままで、本日の追加はない。ページの構成にも変化はない
- Copilot Studio の Released Versions は **2026.6.3**（6/30 初出）のままで、新ビルドが出ない状態が6週間半続いている。リージョン分布と UX 版 26.06.21-24 にも変化はない。ページ本文は「毎週火曜更新」と書いているが実態と食い違ったままで、次の定例は 8/18 である
- Copilot Agent Kit（Power CAT）は 8/14 の August 2026 版（タグ `CopilotStudioAccelerator-August2026`）が最新のままで、本日の新規リリースはない
- Power Platform の Release Wave（`power-automate` / `power-apps`）は 8/16 と完全に同一で、緑チェックの追加・期日変更・行の増減はいずれも発生していない。期日超過は延べ6行（GA 列5件・Public preview 列1件）、8月期日は10件、9月期日は6件のままである。2026 Wave 1 の対象期間は9月末までで残り約1か月半になる
- Power Platform Blog の親ページは 8/13 の PPCC 2026 登録記事が先頭のままで、8/6 公開の月次合併号は依然として一覧に現れない（不完全レンダリングが継続）。Power Automate Blog / Power Apps Blog も同じ記事が先頭である。⚠️ PPCC 2026 の標準価格での登録は **8/18** までである
- Power Platform 系のスペシャライゼーションが 7/31 付で Agentic Business Solutions へ統合されていた。Low Code Application Development と Intelligent Automation の2つが1つになり、既存の登録パートナーは記念日を維持したまま新スペシャライゼーションへ移された。**Power Platform の提案を担う組織では要求される資格の顔ぶれが変わる**
  - 実績要件: 「Power Automate の本番フローと5名以上が使う Power Apps を持つ新規顧客2社」または「Copilot Studio の新規展開2件で各 TTM $10,000 以上」のいずれか
  - 資格要件: Power Platform Functional Consultant / Intelligent App Builder / AI Agent Builder のいずれか5名に加え、Power Platform Developer 系2名と Agentic AI Business Solutions Architect 2名
  - 出品要件: Microsoft Marketplace へのコンサルティングサービス出品1件
  - https://learn.microsoft.com/partner-center/announcements/2026-august
- Microsoft Purview の8月節は Sensitivity labels の2件（自動ラベル付けポリシーのシミュレーションモード／ポリシー詳細パネルの Insights タブ）のままで、`updated_at` も 2026-08-14 から動いていない。⚠️ 8月節に Copilot 固有の項目は依然として一件も含まれていない

### Microsoft 365 Copilot / GitHub

- Microsoft Copilot アプリの統合が **8/18** に始まり、Web URL が `m365.cloud.microsoft` から `copilot.cloud.microsoft` へ移る。旧 URL からは自動リダイレクトするが、組織内で新 URL がブロックされている場合は開けないため、事前に許可リストを確認する必要がある。Microsoft がパートナーに求めているのは、既存のネットワーク・プロキシ・ファイアウォール・アクセスポリシーでの遮断確認、`*.cloud.microsoft` の許可リストへの追加、接続検証の3点である。あわせて職場アカウントを示す緑のシールドなどの視覚指標が入り、Windows / Mac 版デスクトップの早期プレビューが 8/18 に始まる（広範な展開は9月中旬から）。⚠️ Windows Insider 向けリリースノート（8/14・version 152.0.4191.25）は、プレビュー期間中にタスクバーの Ask Copilot を一時的に無効化し、**Notebooks・Connectors・Vision が一時的に使えなくなる**と告知している
  - https://learn.microsoft.com/partner-center/announcements/2026-august#microsoft-copilot-app-update
  - https://learn.microsoft.com/windows-insider/release-notes/apps/copilot-on-windows
- Microsoft がマルチテナントのエージェント管理をパブリックプレビューで提供している（8/10 告知）。Microsoft 365 管理センターに、管理下の複数テナントを横断してエージェントを閲覧・管理する画面が入った。できるのは統合されたエージェント在庫の閲覧、エージェントの追加、対象テナントへの一括インストールと遮断、テナント別のリスクと稼働の確認、サインアウトなしでのテナント切り替えである。⚠️ リスクと稼働の確認には Agent 365 ライセンスが要る。CSP パートナーが GDAP 経由で顧客テナントを管理する構成を主眼に置いており、操作は各テナントでの委任ロールの範囲に限定される
  - https://learn.microsoft.com/microsoft-365/admin/manage/agent-365-overview
- M365 Copilot Release Notes は **August 11, 2026** バッチのままで、本日の新バッチはない。本文を取得して先頭の見出しと節構成7本（extensibility 2 / SharePoint 1 / Outlook 2 / Microsoft 365 Copilot 1 / PowerPoint 4 / Viva Insights 1 / Word 1）が 8/16 と一致することを確認した。次バッチは 8/25 前後の見込みである
- 英語圏の二次記事が「8月から展開」として挙げる PowerPoint のブランドキットは、Release Notes 上では July 15 バッチと July 01 バッチの既存項目に対応する。August 11 バッチには一件も入っておらず、「8月の大型アップデート」系の空振りは4例目になった
- Copilot CLI は pre-release の v1.0.81-0（8/14 23:47 UTC）が最新のままで、8/15・8/16 の新規リリースはない。安定版は v1.0.80（8/14 02:28 UTC）に据え置かれている。`github.blog/changelog` も 8/14 の Grok 4.6 提供開始が最上位のままである
- Microsoft 365 Roadmap・Microsoft 365 Blog（本体）・M365 Developer Blog・SharePoint Blog・Agent 365 Blog は、いずれも本日の新規がない。⚠️ Tech Community の M365 Copilot Blog は board RSS のエントリ並びが 8/13 → 8/12 → 8/5 → 8/7 → 7/31 → 8/4 → 7/24 で投稿日の降順になっておらず、乱れが**4日連続**で再現した
- Partner Center の8月アナウンスは 8/14 付の14件目までで、本日の追記はない（2日連続）
- 既報: Grok 4.6 の Copilot 追加（8/14・Enterprise / Business は既定オフ）、Gemini 3.7 Flash の追加（8/13）、MAI-Code-1.1-Flash の提供開始（8/11）
- 期限: 既定モデル有効化ポリシー発効（**8/26**）、GitHub Spark 退役（**8/31**）、モデル廃止（**9/1**）、MAI-Code-1-Flash 廃止（**9/10**）

### Anthropic / Claude

- Anthropic が 8/14 に186ページの August 2026 Risk Report を公開していた。Responsible Scaling Policy v3.4 に基づく2本目の全社報告で、対象期間は 2026-02-24 から 2026-07-15 である。misalignment（高stakes環境での破滅的被害）の評価は2月の初回報告の very low から **low** へ上がったが、Anthropic 自身は「報告書内の論証は依然として very low を支持している可能性が高い」と書いており、引き上げの理由を能力の向上ではなく**不確実性の増大**だと説明している。7/30 に公表したサイバー評価インシデント（3組織への意図しない侵入）が根拠に挙がっている
  - Model 2: 社内のエンジニアリングベンチマークで公開モデルの Claude Mythos 5 を上回る未公開モデルの存在を開示した。報告書は「現時点で外部公開の予定はない」と明言している。公開モデル＝同社の到達点という読み方はできなくなる
  - 運用面の欠落: human feedback ベンダー経由のトラフィックが、2025年5月から2026年4月までの約 **133,000,000 件**のやりとり（契約者約 50,000 人）にわたってブロック用の生物学分類器を通らずに流れていた。是正済みで悪用の証拠も顧客影響もないとしたうえで、「同種の欠落が他に無いという確信は下がった」と書いている
  - これを受けて非新規（non-novel）兵器 uplift の評価は「low だが従前の見積もりよりは高い」に変わった
  - ⚠️ 一次（`www.anthropic.com/aug-2026-risk-report` と PDF）はどちらもオリジン403で本文未確認であり、数値は複数の二次報道の一致による。本サマリーは 08-15・08-16 に検出できず、3日遅れの初検出になった
  - https://www.axios.com/2026/08/14/anthropic-model-2-ai-risk
  - https://thenextweb.com/news/anthropic-risk-report-bio-classifiers-human-feedback-gap
- Anthropic が Fable 5 の生物学セーフガードを再調整し、誤検知を約85%減らしていた（8/7 公表・10日遅れの捕捉）。対象は生物学の保護対象コンテンツを含むと判定した要求を能力の低いモデルへ自動的に回す「フォールバック」で、自社テストで製品全体のフォールバックが約85%減った。作業は分類器の constitution の書き直し、社内外の専門家からの意見収集、改訂ルールに沿う学習データの再生成と再学習である。⚠️ 専門的な生物学研究を開放したわけではなく、ウイルス学・毒性学・分子設計を含むデュアルユース要求は引き続き Claude Opus 5 へフォールバックする。変わるのは臨床業務や検査値の解釈といった日常の健康・教育用途での拒否率にあたる
  - https://www.anthropic.com/news/improving-fable-5-s-biology-safeguards
- Claude Code は **v2.1.233**（8/14 22:20 UTC）が最新のままで、8/15・8/16 の新版はない。npm `dist-tags` は前日から1つも動かず、実測は `{stable: 2.1.224, latest: 2.1.233, next: 2.1.233}` で 08-16 と完全に同じである。`next` の先行も止まっており、`stable` と `latest` の差は**9版のまま**で、v2.1.233 に入った Windows の NT device path 脆弱性修正は stable 固定環境に届いていない
- Claude API release notes は 8/11 が最上位のままで、8/12 以降の追加はない。`support.claude.com` の Release Notes も 8/6 の skill / plugin セキュリティスキャン beta が最上位のままで、**11日連続**で動きがない。`claude.com/blog` も 8/14 の記事が最新である
- Claude Code の週次上限50%増は **8/19 23:59 PT** で終了する。対象は Pro / Max / Team / シート課金の Enterprise で、2026-05-13 の開始以降3回延長された末の期限にあたる。5時間枠の上限が 5/6 に恒久的に倍化した分は影響を受けない
- 既報: Chrome 拡張サイドパネルの Cowork 化（8/12）、Claude Tag のチャンネル文脈対応（8/13）、JetBrains の Fable 5 評価事例（8/13）、Decart AI 買収交渉の報道（8/13・成立していない）

### OpenAI

- OpenAI が ChatGPT デスクトップアプリを更新し、コードレビューと画像編集の導線を作り替えた。⚠️ 一次 `learn.chatgpt.com` がゲートウェイ拒否のため掲載日は未確定で、WebSearch 経由の検出にとどまる
  - Review: 複数リポジトリの diff を1画面で確認できる。マルチフォルダプロジェクトの全リポジトリと各リポジトリの変更行数が並ぶ
  - 画像: 生成画像を拡大ビューアで開き Focused view と Canvas view を切り替えられる。画像をまたいでコメントを付け、対象を選んで会話から離れずに編集を投げられる
  - 内蔵ブラウザ: アドレスバーから閲覧履歴の再訪と Google 検索ができ、履歴は Settings で管理する。ChatGPT に履歴を検索させることもできる
  - Activity view: サイドバーに加わり、最近やりとりしたチャットと対応が要るものを一覧できる
- Codex の Guardian auto-review が prompting regression から旧ポリシーへ差し戻された。リクエスト形式とツール挙動も従前のものに戻り、cyber 能力を持つモデルに対して自動レビューの既定値がより安全側に変更された。⚠️ 掲載日は未確定である
- Codex CLI の pre-release が **0.148.0-alpha.20**（8/16 00:21 UTC）に進んだ。前回の alpha.19（8/15 02:21 UTC）から1版で、安定版は 0.147.0（8/7 01:41 UTC）に据え置かれている。⚠️ alpha 各版の個別リリースノートはページ側のエラーで表示されず、内容は**4日連続**で確認できていない
- ChatGPT の Linux デスクトップアプリは 8/11 のプレビュー公開以降に続報がない。`.deb` / `.rpm` の対象は Ubuntu 24.04 / 26.04 LTS・Debian 13・Fedora 43 / 44 の x64 / ARM64 で、インストーラが OpenAI のリポジトリを追加するため以後の更新は apt 等で配られる。デスクトップアプリは Claude Code・Claude Cowork・Cursor から指示・設定・スキル・プラグイン・直近の作業を取り込め、Settings > Import で自動同期も設定できる
- `developers.openai.com/api/docs/changelog` は 8/13 の Ultrafast モードが最上位のままで追加はない。⚠️ 課金レートは依然として未確定である。`community.openai.com` の Announcements RSS も 8/10 の Daybreak 拡大告知が最新のままである
- 既報: Computer History（8/13）、GPT-5.4 / 5.4 mini の Codex 除外（**8/31**・移行先は `gpt-5.6-terra` / `gpt-5.6-luna`）
- 到達性: `community.openai.com` と `developers.openai.com` は 200。`openai.com` / `help.openai.com` / `platform.openai.com` はオリジン403、`learn.chatgpt.com` はゲートウェイ拒否が継続している

### Google / DeepMind

- Gemini API changelog は 8/13 の Gemini 3.7 Flash GA が最上位のままで、8/14〜8/16 の追加はない。Gemini 3.5 Pro の GA は未ローンチが継続しており、I/O 発表後に 6月 → 7月 → 7/17 と3回スリップしている
- Gemini API の単価は据え置きで、3.7 Flash と 3.6 Flash の両方に入力 **$0.75** / 出力 **$3.75**（100万トークン）の導入価格が掲載された状態が続いている。有効期限は 2026-12-31 で、2027年1月1日以降は $1.50 / $7.50 へ戻る。バッチはいずれも標準の半額で、3.5 Flash（$1.50 / $9.00）と 3.5 Flash-Lite（$0.30 / $2.50）も変更はない
  - https://ai.google.dev/gemini-api/docs/pricing
- 退役カレンダーでは Imagen 4.0 系3本の停止日が**本日 8/17** にあたる。Gemini 2.0 Flash / 2.0 Flash-Lite（6/1）と Veo 3 / Veo 2（6/30）は停止済みである
- ⚠️ 登録済みの Google 系5ソースは本日の週次チェックでも全件ゲートウェイ拒否で、到達できる Google 一次は未登録の `ai.google.dev` だけである。登録ソースだけを回すと Google のモデル発表は一次で1件も取れない

### モデル・料金 / オープンウェイト

- DeepSeek の新 API 料金が日本時間 8/17 01:00（＝8/16 16:00 UTC）に発効した。08-16 収録の「上げ幅50%〜最大1,100%超」の内訳が課金区分ごとに判明し、**倍率が最大なのは出力ではなく V4-Pro のキャッシュヒット入力**だった。キャッシュ活用を前提に安さを見積もっていた試算ほど大きく狂う
  - キャッシュヒット入力: オフピーク6倍・ピーク **12倍**（100万トークンあたり 0.025元 → 0.30元）
  - キャッシュミス入力: オフピーク1.5倍・ピーク3倍
  - 出力: オフピーク2.25倍・ピーク4.5倍。絶対額は V4-Flash が定額 $0.28 からピーク $1.32 / オフピーク $0.66 へ、V4-Pro が $0.87 からピーク $3.96 / オフピーク $1.98 へ移る
  - ピーク帯は UTC 01:00〜04:00 と 06:00〜10:00（日本時間 10:00〜13:00 と 15:00〜19:00）で、日本のオフィス時間とほぼ重なる。⚠️ `api-docs.deepseek.com` は本日もゲートウェイ拒否で、発効後の一次料金表による確認はできていない
  - https://qz.com/deepseek-api-price-increase-v4-peak-off-peak-081326
- **DeepSeek V4-Pro-0813 のベンチが参照ハーネスで33ポイント落ちる。** DeepSeek が Terminal-Bench 2.1 で 87.9% と申告した V4-Pro-0813 を Vals が同ベンチの参照ハーネス Terminus 2 で測ると **54.68%** だった。DeepSeek 側の数値は自社の「DeepSeek Harness minimal mode」で測ったもので、このハーネスは未公開である。ハーネス差でスコアが動くこと自体は正常で、Kimi K3 は 7.4ポイント、Claude Fable 5 は 7.5ポイント、Claude Opus 4.8 は 13.1ポイント、GLM-5.2 は 13.2ポイント落ちる。33ポイントはこの範囲から外れた外れ値で、しかも参照ハーネス下では自社の安価な V4-Flash（67.04%）を12ポイント下回る。提案でベンチ値を引くならハーネス名の明記が要る
  - https://www.techtimes.com/articles/324241/20260813/deepseek-v4-pro-0813-goes-ga-benchmark-claims-await-independent-proof.htm
- Z.ai が GLM-5.3 のウェイト公開だけを約2週間延期し、理由に自社モデルの攻撃的サイバー能力を挙げた。8/14 に API では提供開始しており、オープンウェイトと広範な API 開放は安全性評価とハードニングの完了後に段階的に行うとしている。**主要なオープンウェイト系ラボが、自社モデルの攻撃的サイバー能力を理由に公開延期を明言した初の事例**にあたる。構成は GLM-5.2 と同じ 743B のベース（1トークンあたり活性は約40B）で、性能差は post-training だけから出ているとしている
  - 自己申告ベンチ: DeepSWE 1.1 66.9%・Terminal-Bench 3.0 28.3%・CyberGym 84.5%・ExploitBench 54.4%・Humanity's Last Exam（ツールあり）62.5%
  - 能力の裏づけ: GLM-5.2 以降のモデルが 269件のオープンソースプロジェクトで **2,436件の脆弱性**を特定し、うち 1,097件が Critical / High だったとしている。対象はシステムカーネル・ブラウザエンジン・ネットワークプロトコル・OS に及ぶ
  - ⚠️ ベンチ値はいずれもベンダー自己申告で第三者検証値ではない。`huggingface.co/zai-org/GLM-5.3` は HTTP 401 を返し、ウェイトが未公開であることと矛盾しない
  - https://www.axios.com/2026/08/14/china-open-source-ai-glm-53
- 8/16 に新規公開されたオープンウェイトモデルはない。`Qwen` / `moonshotai` / `deepseek-ai` / `meta-models` / `mistralai` / `zai-org` / `openai` / `google` の計8 org について Hugging Face の作成日降順一覧を実行し、8/13 の `deepseek-ai/DeepSeek-V4-Pro-0813` より新しいリポジトリが1件もないことを確認した
- `deepseek-ai/DeepSeek-V4-Pro-0813` は本日時点でダウンロード **21,873** / likes 526（前日は 19,945 / 483）である。Qwen3.8-27B は 267,725 / 10,194、FP8 版は 352,971 / 470 になっている

### MCP / 開発ツール

- MCP 公式ブログは新着がなく、RSS の最新は 7/28 の `The 2026-07-28 Specification` のまま**20日連続**で動きがない。Tier 1 SDK にも変化はない（TypeScript `@modelcontextprotocol/server` / `client` ともに 2.0.0、Python `mcp` 2.0.0、C# v2.0、Go は v2 未発行で `go-sdk` v1.7.0 が仕様対応）
- Devin が Web アプリと自動化まわりを更新していた（二次・⚠️ 掲載日未確定・`docs.devin.ai` はゲートウェイ拒否継続で一次未確認）
  - Automations が Slack のダイレクトメッセージ上でも動くようになり、DM を有効にするかの設定が付いた
  - SCIM のユーザー / グループプロビジョニングが Enterprise 向けに GA した
  - ネストした `AGENTS.md`・小文字の `agents.md`・対応するドットディレクトリ内のルールが検出対象になり、置かれたディレクトリにスコープされる
  - 完了した `ask_user_question` が `/steps` のエントリとして残り、そこへ revert / fork できる
- Cursor の changelog は 8/13 の Cloud Agents Builds が最上位のままで追加はない。フォーラムも 8/12 の Grok 4.6 関連2件が最新である
- ⚠️ xAI は一次に到達できない状態が継続している（`x.ai` / `docs.x.ai` がゲートウェイ拒否）。8/16 の新規発表は二次でも確認できなかった

### 企業・市場・国内

- Databricks が $5B を調達し評価額 **$190B** に達した（8/13・半年で $134B から）。Coatue Management がリードし、Blackstone・MGX・T. Rowe Price 系のほか Sixth Street Growth・BOND・Clearlake Capital・Point72・Premji Invest・TPG が新規に参加した。同社は売上ランレートが $7B 超、第2四半期の前年同期比成長が80%超としている。資金の投入先として名指しされたのは Lakebase（エージェント向けデータベース）・Genie（業務データを参照する AI アシスタント）・**Unity AI Gateway**（モデル利用の管理と費用統制）の3製品で、いずれもエージェント運用の土台にあたる
  - https://www.cnbc.com/2026/08/13/databricks-funding-round-190-billion-valuation.html
- CSP のソフトウェア月額請求に **10/1** から5%の資本コスト上乗せが入る。対象は年間契約かつ月次請求の CSP ソフトウェアサブスクリプション（SQL Server・Windows Server・CAL・System Center 等）で、年次一括請求と月々契約には変更がない。既存の年間契約・月次請求は 10/1 以降の更新時から適用される。⚠️ Microsoft は「以前の通知に誤った発効日が含まれていた」と明記して訂正しており、旧通知の日付で顧客に説明していれば言い直しが要る
- 業務用 Copilot の URL 移行にともなうエンドユーザー向け一次解説がある `support.microsoft.com` は、本日もゲートウェイ拒否で読めない
- MS-4005 の週次確認では、API が 200 を返し「Craft effective prompts for Microsoft 365 Copilot - Video Series」の全9モジュールに 7/23 の初回確認時から構成・タイトルとも変化がないことを確認した
- IDC / IDC Japan・MM総研・Similarweb・NRC はいずれも更新がない。直近で引用可能な国内の基準値は IDC の 2026年3月予測（国内 AI 市場支出額が 2025年 2兆3,725億円 → 2029年 6兆8,897億円・CAGR 36.0%）と、総務省 令和8年版情報通信白書（企業の生成AI業務利用 86.4%）のままである
- `developer.apple.com` は 200 で、8/12 の年齢レーティング更新以降に新規がない。AI 関連の最新は 8/5 のままで、iOS 27 / iPadOS 27 は developer beta 4（7/20・ビルド 23G71）が最新、GA は9月（予想 9/14 前後）の見込みである

## 直近の注目予定

- **8/17（本日）**: DeepSeek API の新料金が発効済み（JST 01:00・カテゴリ参照） ／ Claude Console 旧 Workbench 退役と実験的プロンプトツール API 廃止 ／ Gemini API の Imagen 4.0 系3本停止 ／ Gemini in Classroom のモバイル開放
- **8/18**: 業務用 Copilot の URL 移行開始（`copilot.cloud.microsoft`）とデスクトップ早期プレビュー ／ PPCC 2026 の標準価格での登録期限 ／ Copilot Studio Released Versions の次回定例
- **8/19**: Claude Code の週次上限50%増が終了（23:59 PT）
- **8/20**: **Copilot Tuning の停止期限（未完了の調整実行は破棄・ハイライト1参照）** ／ Gemini Enterprise Agent Platform の Grok 4.1 ファミリー停止（一次未確認） ／ Pixel 11 系の出荷開始 ／ 非推奨一覧と Release Wave の週次確認
- **8/22**: M365 Copilot アプリのチャット中心 UI が Deferred リングへ展開開始（MC1325422）
- **8/23–24**: **Manus が Meta 買収後（2025-12-29 以降）のユーザーデータを削除**（8/23 08:00 SGT 開始・復元は 8/25 から・ハイライト2参照）
- **8/25 前後**: M365 Copilot Release Notes の次バッチ（隔週サイクルどおりなら）
- **8/26**: OpenAI Assistants API 廃止 / o3 退役 / GPT-4.5 完全廃止 ／ Copilot 既定モデル有効化ポリシー発効
- **8/27**: IT Nation Connect ANZ の Microsoft セッション
- **8/30**: 公式 DALL·E GPT の退役
- **8/31**: GitHub Spark の既存ユーザーアクセス終了 ／ `gemini-robotics-er-1.6-preview` 停止 ／ GPT-5.4・5.4 mini が Codex から除外 ／ Claude for Government の $1/機関プログラム終了 ／ Power Automate モバイルアプリ廃止 ／ CSP Copilot Partner Council コンテストの応募期限
- **9/1**: GitHub Copilot の全体験でモデル廃止 ／ OpenAI Daybreak で全アカウントにハードウェアセキュリティキー必須化 ／ MAICPP 契約の更新条項が自動発効
- **9/2〜9/3**: Windows 365 Frontline 名称での購入最終日（9/2）と Windows 365 Flex への改称（9/3）
- **9/10**: MAI-Code-1-Flash が全 Copilot 体験から廃止
- **9 月**: Copilot Tuning の新体験が Public Preview ／ iOS 27 / macOS 27 GA ／ auto mode の既定化を Enterprise・API・各クラウドへ拡大予定 ／ 9月中旬に Copilot デスクトップアプリの広範な展開開始 ／ 9月末に 2026 Wave 1 の対象期間終了 ／ 9/30 に M365 E7 プロモーションの対象購入最終日と M365 E5・E3 の CSP 割引終了
- **10 月**: Anthropic の IPO 予定（$2T 超の評価額を目標と報道） ／ 10/1 に M365 E7 プロモーションの新規取引停止と CSP ソフトウェアの5%上乗せ発効 ／ 10/20〜22 に SMB Copilot Partner Council（NYC） ／ 10/25〜30 に PPCC 2026 本編とワークショップ
- **11/1**: パートナー特典の有効期限がオファー購入日基準へ移行
- **12/2**: EU AI Act の生成コンテンツ標識義務、8/2 以前に市場投入済みシステムへの猶予終了
- **12 月**: Copilot Tuning の新体験が GA ／ 12/31 に Gemini 3.6 Flash / 3.7 Flash の導入価格終了（$0.75 / $3.75 → $1.50 / $7.50）と M365 E3 プロモーション・Copilot in 30・Purview Suite 50%オフの提供終了
- **2027年6月末**: Frontier Partner バッジの廃止

## 改善メモ

- 検出遅れが3件重なった。Meta Muse Code（8/5）は**12日遅れ**、Anthropic の Risk Report（8/14）は3日遅れ、Fable 5 の生物学セーフガード再調整（8/7）は10日遅れの初検出である。原因の性質は2通りに分かれる
  - ソース未登録: Meta の一次3ホストは `daily-sources.md` に1項目も登録されていなかった（B-037 で起票）。Google 系も登録5ソースが全件ゲートウェイ拒否で、到達できる一次は未登録の `ai.google.dev` だけという同型の状態にある
  - 規定手順の未実行: Anthropic 項は検索キーワードを5本に増やす手当てが済んでいたのに、08-15・08-16 はいずれも日付入りの製品発表クエリ1本しか実行しておらず、**規定された5本のうち4本が実行されていない**。手当てが済んでいても実行されなければ検出されない
- ソース間で食い違いはなかった。DeepSeek の値上げについて 01 が「最大11倍」、03 が「キャッシュヒット入力ピーク12倍・上げ幅最大1,100%超」と書いているが、これは 08-16 時点の概数と本日判明した課金区分別の内訳の差であり、矛盾ではない
- 一次に到達できないまま採用した項目が2件ある。ハイライト1（Copilot Tuning）は Message Center アーカイブと MC 系二次ブログ2本がいずれもゲートウェイ拒否で、検索インデックスのスニペットだけが根拠にあたる。ハイライト3（Muse Code）は Meta 一次3ホストが同様で、数値・仕様は二次の一致による。⚠️ どちらも一次未確認のまま期限や単価を扱っているため、提案に引く際は出典の性質を明示する
- 取得できていないソースは次のとおり。Message Center は**10日連続**で一次取得できない。Codex CLI の alpha 各版リリースノートはページ側エラーで4日連続未確認である。Power Platform Weekly は本日の週次確認がゲートウェイ拒否でスキップとなり、#270（6/29）以降の夏季休刊が明けたかを確かめる手段が依然としてない。Copilot Credit の単価は一次（Learn）に存在しないため、Qiita / Zenn の具体値は採用していない
- 障害の新規登録が5件あった。01 が Meta 一次3ホストと `www-cdn.anthropic.com`、02 が `m365admin.handsontek.net` / `mwpro.co.uk`、03 が `www.ghacks.net` / `digiday.com` / `www.vals.ai` をいずれも記録している。02 側のゲートウェイ拒否ホストは9本になった。01 の週次復旧チェック（月曜）では対象8ホストが**1件も復旧していない**（2週連続）
- 各ソースの改善提案は 01 が新規 B-037（Meta のソース登録）で継続15件、02 が新規 B-036（Message Center の代替経路定義）で継続18件、03 が新規 B-026（Partner Center 月次 announcements の定点化）で継続9件である。⚠️ 02 の継続提案は 08-16 の16件から18件へ増えているが、新規は B-036 の1件だけで、残る1件の由来が記載されていない
