# AI News Daily Summary — 2026-06-25

> 本サマリーは 01_ai-news-Master・02_ai-news-Copilot・03_ai-news-industry の3ソース（6/25分）を統合して作成。木曜・主要ラボの新規フロンティアモデル発表は引き続きなし。中心は (1) Fable 5 / Mythos 5 停止14日目で「ホワイトハウス×Anthropic 共同リスクフレームワーク起草」と「議会の回答期限が明日6/26」という2つの節目、(2) リーク最有力日とされた GPT-5.6（6/25）の空振り、(3) Anthropic の Slack 常駐・共有AIチームメイト「Claude Tag」。

## 今日のハイライト

### 1. Fable 5 / Mythos 5 停止14日目 — ホワイトハウス×Anthropic が「共同リスクフレームワーク」起草、議会の回答期限が明日6/26に迫る

**事実**: 6/12 17:21 ET の米輸出規制指令による Fable 5 / Mythos 5 の世界一斉停止は、**6/25 時点で14日目（停止から13日経過）も未復旧**（全顧客で両モデルを無効化し Opus 4.8 へ自動ルーティング継続、他 Claude モデルは影響なし）。前日のトランプ大統領の事実上の容認発言から一夜明けても、**商務省は正式な解除命令を発出していない**。解決交渉は前進しており、**ホワイトハウスと Anthropic が「共同リスクフレームワーク」を起草中**（Politico 報道）— jailbreak の深刻度（safeguard をどこまで突破したか／露出した能力／実被害）を採点する共通基準を策定し、将来のフロンティアモデル事案で政府がいつ介入すべきかの判断指針とする狙い。一度は「Fable de-deploy 要求」で決裂したが、約1週間の対面協議で枠組み構築へ転換し、**政権側は「完全に jailbreak 不可能なモデルは存在しない」と譲歩**したとされる。Anthropic 幹部は「数日のうちに再開できる」と楽観を示すが、確定復旧日はなお無い。

**根拠**: 共同フレームワーク起草・政権側の譲歩は Politico / Globe and Mail 等の報道（01_Master・02_Copilot、一次は WebSearch スニペット経由で確度は中程度）。**明日6/26 が一つの節目** — Sam Liccardo ら超党派4議員が 6/18 付で Lutnick 商務長官に公開書簡を送り、輸出管理措置の法的根拠（14 C.F.R. §744.22(b) の "is informed" letter、ERA 2018 権限）・技術評価・復旧/ライセンス基準の文書回答を 6/26 までに要求している。予測市場の織り込みはソース間で幅があり、Polymarket「6/26 までに US 再開」**41%**、「〜7/1 復旧」は Kalshi 58% / Polymarket 67%（01_Master）、別ソースは「7/1 まで57%・7/10 まで67%・7/17 まで75%」（02_Copilot）。停止の技術的背景は既報のとおり、Amazon の研究者が「防御的コードレビュー」を装って Fable 5 のサイバーセキュリティ分類器を回避した多段手法だが、表面化したのは他の公開モデルでも検出可能な既知の軽微な脆弱性で、Anthropic は「狭いジェイルブレイクを商用モデル全面回収の理由とすべきでない」と反論を継続。

**影響**: 政治シグナル（容認・フレームワーク起草）が前進する一方、商務省の正式解除命令という確証は未達で、「目前」と「未確定」が併存する状態が続く。共同リスクフレームワークが成立すれば、フロンティアモデル障害時の政府介入ルールの先例となり、業界全体のデプロイ可否プロセスに波及しうる。Fable 5 / Mythos 5 を本番前提にしていた組織にとって、復旧時期は依然「未定（ただし上振れ材料あり）」。

**行動指針**: Fable 5 / Mythos 5 を本番に組み込む組織は復旧を「目前の可能性ありだが未確定」と扱い、Opus 4.8 等へのフォールバック前提の運用を継続。明日6/26 の議会回答（Lutnick → Liccardo ら）と、商務省の正式解除命令／anthropic.com/news での明示確認を最優先の確証とし、トランプ発言や暗号メディア速報を確定根拠として扱わない。共同リスクフレームワークの内容が公開されれば調達・ガバナンス方針へ反映を検討。

- https://www.koreajoongangdaily.com/business/anthropic-confident-of-reenabling-mythos-fable-5-access-in-coming-days-executive/12727522
- https://www.anthropic.com/news/fable-mythos-access

### 2. GPT-5.6 — リーク最有力日6/25が公式発表なしで空振り、7月ローンチ説が再浮上

**事実**: 昨日まで複数リークで「**6/25 に GPT-5.6 Pro**」が最有力視されていたが、**6/25 時点で openai.com に発表・system card・API モデルページ・ベンチマークはいずれも未掲載**。リーク最有力日が空振りに終わった。一部トラッカーで予測オッズが大幅低下し（83% 圏から大きく後退）、**7 月ローンチ説が再浮上**している。予測窓（6/22–28）は 6/28 まで残るが、短期の織り込みは後退した。

**根拠**: openai.com の発表ページ・API モデル一覧・system card のいずれにも 6/25 時点で記載なし（01_Master が直接確認）。リーク内容（未確認）は不変で、reasoning effort budget 768→960、Playwright 統合による web 自動化（テスト/スクレイピング）、ツール統合強化など。

**影響**: 「リーク日付」を前提に検証・移行計画を組んでいた場合は前提が崩れる。実物・system card・API 文字列が出るまで GPT-5.6 を計画の確定要素に含めない運用が妥当。なお **GPT-4.5 は 6/27 に ChatGPT から退役**（30 日 sunset、予定どおり）が確定スケジュールとして残る。

**行動指針**: GPT-5.6 の採用検討組織は、公式 system card / API モデルページ / ベンチマークの公開を待って評価を開始し、リーク日付では動かない。並行して 6/27 の GPT-4.5 退役に向けた移行（後継モデルへの切替）を予定どおり進める。

- https://openai.com/

### 3. Anthropic「Claude Tag」— Slack 常駐の共有AIチームメイトをベータ提供、個人ツールからチーム業務基盤へ

**事実**: Anthropic が **Slack 常駐の共有AIチームメイト「Claude Tag」をベータ提供開始**（06-23）。チャンネルに `@Claude` を入れてタスクを委任でき、**チーム全員が同一の Claude インスタンスを共有**（他人が始めた作業を誰でも引き継げる）。プロアクティブにスレッドへ介入してフォローアップする「アンビエントモード」を搭載し、**Claude Opus 4.8** で動作、Team / Enterprise プラン向け。Anthropic 社内ではプロダクトチームのコードの **約65%** を内製版 Claude Tag が生成しているという。既存の「Claude in Slack」連携は **08-03 に廃止**、6/23 から30日のオプトイン移行期間に入る。

**根拠**: TechCrunch / Fortune の報道（03_industry）。個人チャットボットからチーム協働基盤へ、という AI エージェントの位置づけの転換点として整理されている。社内コード65%生成はベンダー（Anthropic）自己申告。

**影響**: AI エージェントが「個人の補助ツール」から「チームの共有業務基盤」へ移る流れを象徴。共有インスタンス・アンビエント介入というモデルは、ナレッジ共有や引き継ぎの設計、権限・監査・コストガバナンスを前提にした導入が必要になる。

**行動指針**: Slack を主軸にする Team / Enterprise 組織は、Claude Tag の共有インスタンス運用（誰でも引き継げる前提）と「Claude in Slack」からの08-03廃止に向けた移行計画を確認。アンビエントモードの介入範囲・データアクセス権限・コスト配分を事前にポリシー化してからベータ評価に入ること。

- https://techcrunch.com/2026/06/23/anthropics-claude-tag-is-learning-your-company-one-slack-message-at-a-time/
- https://fortune.com/2026/06/23/anthropic-claude-tag-virtual-employee-tool-slack/

## カテゴリ別まとめ

### Anthropic / Claude・規制
- Fable 5 / Mythos 5 停止14日目・ホワイトハウス×Anthropic 共同リスクフレームワーク起草・議会回答期限6/26・予測市場はソース間で幅あり（ハイライト1参照）
- **Anthropic × Micron 提携（6/24）**: Micron が Q3 決算を前に、メモリ/ストレージ供給で Anthropic との新 AI インフラ提携を発表。Anthropic の計算基盤拡大（Amazon 5GW 等）の流れに連なる infra ニュース
- 人材移籍（Noam Shazeer → OpenAI / John Jumper → Anthropic）は追加続報なし。Anthropic サイエンスイベント **6/30** が次の節目

### Claude / 開発ツール（Claude Tag・Claude Code・Cursor）
- Anthropic「Claude Tag」（Slack 常駐の共有AIチームメイト）ベータ開始（ハイライト3参照）
- **Claude Code v2.1.190（6/24 stable・最新）**: changelog は「Bug fixes and reliability improvements」のみ。v2.1.187 以降は個別エントリ化されない小規模な安定性・信頼性修正が中心
- **v2.1.187（6/23 stable・前出）**: `sandbox.credentials` 設定追加（sandbox コマンドから認証ファイル・秘密環境変数の読み取りをブロック）、組織設定のモデル制限を model picker / `--model` / `/model` / `ANTHROPIC_MODEL` に反映、fullscreen の select メニューでマウスクリック対応。主な修正: `--resume` の「No conversation found」失敗、`--json-schema` / workflow `agent({schema})` の `StructuredOutput` 無限再呼び出し防止、リモート MCP ツール呼び出しの無限ハング → 5分でタイムアウト中断（`CLAUDE_CODE_MCP_TOOL_IDLE_TIMEOUT` で調整）、ペースト時の CJK 文字化け修正等。https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
- **Cursor 3.9（6/22）**: 新 Customize ページで plugins / skills / MCPs / subagents / rules / commands / hooks を user / team / workspace の各レベルで一元管理。v3.8（6/18, Automations 強化）に続くアップデート。Devin は新規リリースなし

### OpenAI
- GPT-5.6 リーク最有力日6/25が空振り・7月説再浮上（ハイライト2参照）
- **ChatGPT Enterprise: クレジット分析・支出上限（6/18・補足）**: 「Global Admin Console」で ChatGPT / Codex のクレジット消費をユーザー/プロダクト/モデル別に可視化、Cost API で外部取り込み可。ワークスペース既定・グループ別・個人オーバーライドの上限を設定可。Cloudflare AI Gateway 支出上限（6/24）と同じ「エージェント常時稼働で AI 請求が膨張する問題」への統制策。https://openai.com/index/chatgpt-enterprise-spend-controls/
- **ChatGPT for Excel / Google Sheets が Enterprise・Edu・K-12 向けにグローバル GA**: スプレッドシートに ChatGPT サイドバーを統合、承認済みファイル/システム/データソースに基づく表計算作業が可能（Skills/apps 対応）。https://help.openai.com/en/articles/10128477-chatgpt-enterprise-edu-release-notes

### Google / DeepMind
- **Gemini 3.5 Pro は依然 GA 待ち**: 6/25 時点も Vertex AI 限定プレビューのみ（2M context / Deep Think）で消費者向け Gemini アプリ / AI Studio 未提供。Pichai「来月中に届ける」の月内期限まで残り約5日、予測市場の「6/30 までの GA」確率は約50〜55%で月内ずれ込みの可能性も残る。https://www.techtimes.com/articles/317919/20260606/google-gemini-35-pro-nears-june-launch-2-million-token-context-deep-think-reasoning.htm

### Microsoft / GitHub
- **Microsoft は新規一次情報なし（静穏継続）**: Copilot Studio What's New（最新 May 2026、6月月次未公開）、Power Platform ブログ（最新 6/11「June 2026 Feature Update」）、M365 Copilot リリースノート（最新 6/16 バッチ）、Tech Community「What's New in M365 Copilot」（6月号未公開）いずれも変更なし
- GitHub Copilot / Cursor / Devin も 6/24 以降の新規リリースなし

### AI 業界トレンド（提案根拠用）
- **市場シェア（Similarweb・2026年4月）**: ChatGPT 54.7%、Gemini 27.4%、Claude 8.2%、DeepSeek 4.1%、Grok 2.8%（変化なし）

## 直近の注目予定

- **6/26**: 議会（Liccardo ら）への Lutnick 回答期限 / Polymarket「Fable 5 US 復旧」予測対象日（41%）
- **6/22–28**: GPT-5.6 ローンチ予測窓（6/25 空振り、オッズ後退）
- **6/27**: GPT-4.5 が ChatGPT から退役
- **6/30**: Anthropic サイエンスイベント / GPT-5.2・GPT-5.3-Codex 新規 API リクエスト不可化 / Devin クラシック環境セットアップ廃止 / Copilot Studio for Teams クラシック作成終了 / 感度ラベル表示 GA / Security Copilot E5 展開完了 / M365 価格ロックイン期限 / Gemini 3.5 Pro GA 予測窓（約50〜55%）
- **〜7/1（予測・未確定）**: Fable 5 / Mythos 5 の US 顧客向けアクセス復旧（Kalshi 58% / Polymarket 67%、02_Copilot は57%）
- **7/1**: M365 価格改定発効（E3 $36→$39、E5 $57→$61、Copilot Business $18→$21）/ Cursor 新価格 / Anthropic Claude Partner Network 初回階層昇格レビュー / Devin Cascade 完全廃止
- **7/8**: Anthropic 政府ID検証ポリシー発効（Fable 5 の米国先行復旧経路の最有力候補・02_Copilot）
- **7/10**: Fable 5 復旧予測の中間マイルストーン（Kalshi 74%）
- **7/17**: Claude Corps 第1期応募締切
- **8/1**: フロンティアモデル枠組みに関する大統領令の60日期限（Anthropic が目指す交渉経路・02_Copilot）
- **8/3**: 「Claude in Slack」連携が廃止（Claude Tag へ移行）
- **8/5**: Claude Opus 4.1 が Claude API から退役
- **8/26**: OpenAI Assistants API 廃止 / o3 退役

## 改善メモ

- **Fable 5 の停止日数カウントがソース間で不一致**: 01_Master は「14日目」、02_Copilot は「13日目」。6/12 停止を起点に inclusive（停止日を1日目）で14日目、elapsed（経過日数）で13日。本サマリーは「14日目（停止から13日経過）」と両表記で明記。日数は起算方法の差であり実態の矛盾ではない。
- **予測市場の数値がソース間で食い違い**: 「〜7/1 復旧」を 01_Master は Kalshi 58% / Polymarket 67%、02_Copilot は57%と記載。市場・時点の差と見られ、両論併記とした。確証は商務省の正式解除命令を最優先とする方針を継続。
- **GPT-5.6 はリーク日付で動かさない**: 6/25 のリーク最有力日が空振り。日付系のリークは複数回外れており（予測窓 6/22–28 はまだ残るが）、公式 system card / API 文字列の公開を確証とする運用を継続。
- **WebFetch / RSS 403 が全ソースで継続**: 入力3リポとも anthropic.com / theglobeandmail.com / github.blog / cursor.com / 各種 RSS（Google News / GIGAZINE / The Decoder / VentureBeat / Publickey / hnrss / Product Hunt / GitHub Trending / llm-stats 等）が 403。各ソースとも WebSearch ＋ raw.githubusercontent.com / 大手メディアでフォールバック。03_industry が `daily-sources.md` の取得方法欄を「WebSearch 優先」へ更新する推奨を複数日継続で強く要対応と記録。
- **データ鮮度（03_industry）**: WebSearch が過去の大型ニュース（OpenAI/Astral=3月、Harness=2025年12月）を「June 2026」クエリでも上位に返すことがあり、本日も2件を日付検証で除外。金額・買収系は必ず一次ソースで公表日を確認する運用を継続。リリースノート系（OpenAI/Anthropic/Google の help・changelog）の取りこぼし対策として、エンタープライズ向け管理機能のリリースノートを定点ソースに追加検討。
- **入力3リポ側で起動時のローカル main 乖離が連日再発**: 01_Master・03_industry がともに「開始時にローカル main が 06-05 で停滞し origin/main と乖離（merge-base 空／多数コミット）」を報告（06-15 以降ほぼ連続、01_Master は6/23・6/24に続き3回連続）。各リポで SessionStart hook に `git fetch && git reset --hard origin/<branch>` 相当を導入する恒久対策を強く推奨。
- **本サマリーの入力取得方法に関する注記**: 本セッションでは GitHub MCP・ローカル git とも入力3リポ（01/02/03）へのアクセスが scope 制限・git proxy 403 で不可だったため、`raw.githubusercontent.com` 経由（curl）で当日ダイジェストを取得した。3ソースとも当日分を取得できており欠損なし。
