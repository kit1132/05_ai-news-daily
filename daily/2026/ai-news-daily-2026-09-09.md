# AI News Daily Summary — 2026-09-09

3ソースとも据え置き報告が主だった前2日から動いた日である。Anthropic が Claude Platform のコスト最適化ガイドを公開し、Claude Code に測定用スラッシュコマンド3種が用意された。Microsoft は3日ぶりに一次へ新規が載り、Cowork のドキュメント一式が 9/8 17:37Z に一斉再ビルドされて September 2026 節と App skill が現れている。資本側は Cognition の $2B（$48B 評価）と Mistral の €3B（€21B 超）が同日に確定し、どちらも本リポジトリが記録した交渉観測を上回った。数学では Navier–Stokes と Euler の有限時間爆発を主張する2陣営が Lean 形式化を同時期に公開している。本日は PVA ヘルプチャットボットの削除が発効し、Apple 特別イベントが日本時間 9/10 02:00 に開かれる。

## 今日のハイライト

### 1. Anthropic がコスト最適化の手順を一次で公開した — 削減の的が「トークンを減らす」から「旧世代向け指示を外す」へ

**要点**: Anthropic が 9/8 にコスト最適化ガイドを公開し、プロンプトのアンチパターン除去だけでコスト14.6%減・精度5.3%向上という自社ベンチマークを示した。削れる余地はトークン量ではなく旧世代モデル向け指示の残骸と effort の過剰指定にある。

**詳細**: 記事は `claude.com/blog/reducing-cost-and-improving-performance-with-claude-platform` で、`claude.com/blog` の最上位が 9/2 の commerce agents から6日ぶりに入れ替わった。削減手段は3系統に整理されている。

- プロンプトキャッシュ: 安定した接頭辞を先頭に置き、使用頻度の低いツール定義を後ろへ回して、Console でヒット率を監視する
- アンチパターンの除去: 「verify twice」のような検証儀式、不要な網羅性ブースター、手順の強制、scratchpad の足場、古い few-shot 例を外す
- effort の較正: `effort` パラメータを段階的に振ってタスクごとの最適点を測る

Claude Code 側には測定用のスラッシュコマンド3種が用意された。`/claude-api prompt-audit` がアンチパターンを検出し、`/claude-api cost-optimize` がトークン支出をプロファイルして削減レバーを試し、`/claude-api hillclimb` がモデル・effort・プロンプトの組み合わせを反復探索する。数値は、カスタマーサポートのベンチマークで prompt-audit 単独がコスト **14.6%減**・精度 5.3%向上、Fable 5.1 の low effort が Fable 5 の high effort に匹敵してコストは1/3、公開ベンチマーク4本での最適化後の削減幅が 52〜73% である。⚠️ いずれも Anthropic 自身のベンチマークで、第三者の再現報告はない。

- https://claude.com/blog/reducing-cost-and-improving-performance-with-claude-platform

### 2. Cognition が $2B を $48B 評価で調達した — 交渉段階の報道値は前提に置けないと3回連続で確定した

**要点**: Cognition が Series E を $2B 超・評価額 **$48B** で成立させた。本リポジトリが 09-04 に記録した交渉観測は $1B・$47B で調達額が倍にずれており、同社の交渉報道は3回とも確定値を下回っていた。

**詳細**: 9月8日公表。新規の Andreessen Horowitz と Accel が主導し、既存の Founders Fund・General Catalyst・Avenir が参加した。シンジケートには Benchmark・Bessemer・Kleiner Perkins・Greylock・Lightspeed・Altimeter・Bond Capital・Meritech が並ぶ。5月の $26B から4カ月弱で1.8倍で、年換算売上は前回調達時の $492M から約 $900M へ約83%増えている。Dealroom は2026年末までに $1.5B 超を目標とする社内見通しを伝えた。顧客として NVIDIA・GE Aerospace・Citi・Mercedes-Benz・Modal を挙げ、2025年の Windsurf 買収が ARR を倍以上に押し上げたとしている。⚠️ 本リポジトリは同社の調達交渉を 08-13（$40B）・08-24（$40B）・09-04（$47B・$1B）と3回「未成立」で記録しており、成立時の確定値は3回とも観測値を上回った。⚠️ 一次のプレスリリース本文には未到達で、数値は二次複数件の突き合わせによる。

- https://www.bloomberg.com/news/articles/2026-09-08/ai-startup-cognition-raises-2-billion-at-a-48-billion-value
- https://www.unite.ai/cognition-raises-over-2b-series-e-at-48b-valuation-to-scale-devin-agents/
- https://app.dealroom.co/news/note/cognition-reportedly-reaches-900m-annualised-revenue-targets-1-5b-by-end-2026

### 3. PVA ヘルプチャットボットの削除が本日発効した — 質問導線が Help (?) メニューに一本化された

**要点**: Power Automate メーカーポータル左下のヘルプチャットボットが本日 **9/9** から全ページで消え、質問導線は右上の Help (?) メニューに一本化される。フロー・コネクタへの影響はなく管理者作業も不要で、残るのは利用者周知と社内文書の更新だけである。

**詳細**: 一次 `important-changes-coming` の先頭節が「Effective September 9, 2026, Microsoft is removing the Power Virtual Agents (PVA) help chatbot in the Power Automate maker portal from all pages」と明記する。Microsoft の説明は「旧来のサポート体験で内容が古くほとんど保守されていない」ため。Help (?) メニューはヘルプ参照とサポート要求の作成を含めて残り、クラウドフロー・デスクトップフロー・コネクタなど機能そのものは変わらない。同ページは `updated_at` 2026-09-04T19:03Z から動かず `## ` 見出しも 94本で、新規の非推奨項目はゼロだった。

- https://learn.microsoft.com/en-us/power-platform/important-changes-coming

## カテゴリ別まとめ

### Anthropic / Claude

- **コスト最適化ガイド**: Anthropic が Claude Platform の削減手順を公開した（ハイライト1参照）。
- **Claude Code のバージョン**: Anthropic は 9/8 19:05 UTC に `2.1.265` を npm へ publish したが、changelog には載せていない。`dist-tags` は `{stable: 2.1.236, latest: 2.1.263, next: 2.1.265}` で、09-08 まで一致していた `next` と `latest` の合流が解けた。内容は changelog・`raw` の CHANGELOG.md のどちらにも無く確定できない
  - 欠番は `2.1.244` / `2.1.249` / `2.1.253`〜`2.1.256` / `2.1.262` / `2.1.264` の計8件になった
  - ⚠️ `stable` は `latest` と27版差で据え置き、権限系修正3件（`2.1.251` の symlink 追跡・`2.1.260` の括弧を含む権限ルールの破棄と `rm -rf` の確認プロンプト・`2.1.263` の内容未確定分）が stable 固定組織に届いていない
- **Claude Code changelog**: 最上位は 9/6 の `2.1.263` のままで、9/7・9/8 付けのエントリは追加されていない。記載は `Bug fixes and reliability improvements` の1行だけである
- **フェルマーの最終定理の形式化**: Anthropic が9月4〜5日に公表した Lean 形式化を、03 が本日初捕捉した（5日遅れ）。Claude が11日間ほぼ自律で走り、1,300万行の Lean コード・証明した定理 30,300件（最終証明に使われたのが 29,500件）・出力トークン約 **60億**を要した。基盤は Columbia University の Tianyi Peng らによる協調プラットフォーム Prove2Me で、⚠️ 学術成果よりも長時間エージェント運用の実測値が一次で出た点を記録する
  - https://www.anthropic.com/research/formalizing-fermats-last-theorem
- **Platform API release notes**: 9/3 の `ant` CLI 1.30.0（`ant apply`）が最上位のままで、9/4〜9/8 の追加はない。`support.claude.com` の Release Notes も 9/1 の Fable 5.1 / Mythos 5.1 が最上位で変わっていない
- **モデル退役**: Anthropic は本日も新規の退役告知を出しておらず、Active は11件のままである。直近告知は 2026-06-05 の Opus 4.1（8/5 退役済み）で、表外の Note にある `claude-mythos-preview` の deprecated 扱い（移行先 `claude-mythos-5`）も据え置き
- ⚠️ 8月 Risk Report は24日連続で一次未読である（初出 08-17）

### OpenAI

- **Navier–Stokes と Euler の Lean 形式化**: OpenAI が Clay 数学研究所の alternatives (C)(D) にあたる形式化を Apache-2.0 で公開し、Alpöge–Buckmaster も smooth forcing つきの3本を同時期に公開した。AI の数学的主張を確かめる手段が論文公開待ちから機械検証の再実行へ移っている
  - OpenAI 側（`github.com/openai/NavierStokesAndEuler`）: 任意の正の粘性について ℝ³ と周期トーラスの両方で大域的な滑らかな解が存在しないことを形式化した。Lean は 4.34.0-rc2 で、独立検証は DeepMind の Formal Conjectures を参照ステートメントに使い独立カーネル `nanoda_bin` で照合する
  - Alpöge–Buckmaster 側（`github.com/tristanbuckmaster/fluid_lean`）: IPM・2次元 Boussinesq・3次元非圧縮 Euler の3本を形式化した。Lean は 4.32.2、`Challenge.lean` 以外に `sorry` は無い。README は Lean コードをすべて Claude が書いたと記している
  - ⚠️ 経緯に係争がある。着手の先後について OpenAI と Buckmaster 側の説明が食い違っており、本サマリーでは判定しない。⚠️ 二次が繰り返した「OpenAI は証明を公開していない」は不正確で、未公開なのは人間可読の論文2本である
  - https://github.com/openai/NavierStokesAndEuler / https://github.com/tristanbuckmaster/fluid_lean
- **ChatGPT Work の文体学習**: 利用者が Gmail / Google Drive / Slack / SharePoint を接続すると、ChatGPT Work が言い回し・締めの挨拶・大文字化の癖・敬体の度合いを推定して新規メッセージに反映するようになった（9/8）。設定は Personalization → Writing style で、Web とモバイルの ChatGPT Work メッセージが対象である。⚠️ 接続先が業務メールとファイル共有そのものである点は組織導入で確認が要る。⚠️ 一次未読で複数の二次の一致による
- **GPT Image 2.5**: OpenAI が 9/8 に Sunburst と Flare を Image API / Responses API へ投入した。品質設定に `xhigh` と `max` が加わり、トークン単価は GPT Image 2 と同じである。⚠️ 画像生成は除外基準に該当するため内容は追わないが、12/1 に停止する GPT Image 系の移行先が `gpt-image-2` である点に変更はない
- **Codex CLI**: OpenAI が pre-release `0.154.0-alpha.7` を 9/8 17:44 UTC に出した。安定版は `0.153.4`（9/4）のままである。⚠️ 個別タグページが読み込みに失敗し本文を確定できていない
- **料金・廃止期限**: OpenAI の一次料金ページは16日連続で据え置きで、GPT-6 Astra の短文脈 $10／$50・長文脈 $20／$75、GPT-5.6 Sol の期間限定価格「少なくとも 2026年11月21日まで」に変更はない。廃止期限も12日連続で不変で、⚠️ `gpt-5.4-cyber` の単価欄が6日連続で空のままである
  - https://developers.openai.com/api/docs/pricing / https://developers.openai.com/api/docs/deprecations
- **その他の一次**: `community.openai.com` Announcements RSS は 9/3 の GPT-6-Astra 告知が最上位で6日間動いていない。GPT-6 Astra の Plus 層への展開も一次の記述が 9/3 から更新されていない
- 到達性: `developers.openai.com` と `github.com` は 200、`openai.com` は本日も HTTP 403（オリジン403）、`learn.chatgpt.com` はゲートウェイ拒否である

### Google / DeepMind

- **Gemini API changelog**: 9/3 の Lyria 3.5 public preview が最上位のままで、9/4〜9/8 の追加はない（5日間）。料金改定の告知もなく、`gemini-omni-flash-preview` の 9/30 廃止（後継 `gemini-omni-1.1-flash`）は据え置きである
- **到達性**: Google 系で到達できる一次は `ai.google.dev` のみという状態が続いている。登録済み5ソースと 09-08 に試した `gemini.google` はいずれもゲートウェイ拒否である
- 既報: 9/2 GA の `gemini-3.8-flash` は入力 $0.75 / 出力 $3.75 が 2026-12-31 まで、2027-01-01 から $1.50 / $7.50 になる。Gemini 3.5 Pro の GA は未ローンチが継続している

### Microsoft 365 Copilot / Cowork

- **Cowork の App skill (Frontier)**: 利用者が説明を書くだけで対話型アプリを生成・公開できるようになった。Cowork What's New に September 2026 節が新設され（`updated_at` 2026-08-28T05:15Z → **2026-09-08T17:37Z**）、組み込みスキル表は14件になった
  - 生成: 解決したい課題を書くと Cowork が App skill を呼び、M365 のドキュメント・スプレッドシート・会議・メッセージを参照する。対応コネクタにデータスキーマを生成し、データソース接続済みの状態で組むこともできる
  - 公開と共有: 編集中は自動保存され、公開すると共有リンクが発行される。⚠️ リンクを持つ組織内の M365 Copilot 利用者は、アプリとその全データを開ける
  - 提供条件: Frontier プレビュー限定で、Microsoft Product Terms のプレビュー条項が適用される
  - ⚠️ 本機能は Roadmap にも Release Notes にも存在せず、Release Communications RSS 全1,757項目と Release Notes 全文で `App skill` は0件だった。Frontier 限定機能を掴む一次は Cowork What's New と `use-cowork` の2本しかない
  - https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/whats-new
- **モデル一覧の追いつき**: `cowork-models` に Claude Fable 5.1（告知から6日）と GPT 6 Astra（4日）の行が入り、8日間続いた一次どうしの食い違いが解消した。判定順序は「Available today 記事が先、Learn の一覧は数日後の追認」で確定する
  - ⚠️ Fable 5.1 の行には Fable 5 にあった「既定オフ・管理者が有効化」の注記と `(Preview)` 表記がどちらも無い
  - ⚠️ `cowork-admin-governance` は同じ再ビルドを受けながらモデル一覧を「Claude Fable, Opus and Sonnet variants, the Sonnet+Opus Advisor pairing, GPT 5.5」のままにしている。食い違いはモデル一覧側だけが直った形である
- **スキルの品質評価**: 利用者がスキルを作成・更新・検証すると、Cowork が依頼なしで自動評価し平文の品質レポートを返すようになっている。評価の深さは到達範囲（個人 / チーム / 組織 / ストア）とリスクで4段階に変わり、点数は4軸25点ずつの100点満点である。⚠️ トラスト&セーフティのゲートは点数から独立しており、高得点でも通過にはならない。⚠️ 本ページは本日の一斉再ビルド対象のため、記述自体が本日の新規かは判定できない
- **モバイルアプリのプラグイン**: 利用者が Web / デスクトップに限られていたプラグインの探索と構成を、モバイルアプリでも行えるようになった。添付メニュー（+）> Skills から開く
- **Release Notes**: 先頭の `## ` 見出しは August 25, 2026 のままで H2 は83本である。⚠️ 隔週の周期では 9/8（UTC）が次バッチの期日にあたり公開時刻帯も過ぎたが、新バッチは出ていない
- **拡張機能 What's New / Copilot Tuning**: 宣言型エージェント側の一次は `updated_at` 2026-07-29T20:23Z のままで42日間更新がない。`copilot-tuning-overview` も 2026-08-18T17:48Z から動かず、停止発効（8/20）から20日たっても停止も退役も無記載である
- **Tech Community / Agent 365 Blog**: M365 Copilot Blog の board RSS 全20エントリに新規はなく、最新は 9/4 の GPT-6 Astra 記事である。Agent 365 Blog は 8/6 の7月号のままで34日間新規がない

### Copilot Studio / Power Platform

- **非推奨一覧**: PVA ヘルプチャットボットの削除が本日発効した（ハイライト3参照）。
- **Copilot Studio What's New**: 最新は July 2026 節のままで、8月節・9月節とも作成されていない。June 節の GitHub Copilot ハーネスは `(Production-ready preview)` 表記が残り、GA（8/3）から37日連続の未反映である
- **Roadmap 項目**: タイトルが `Microsoft Copilot Studio:` で始まる項目は19件で、全件が `In development` のまま増減がない。**566997** は GA 期日「August CY2026」を超過し、**562221** は2026年6月から超過4か月目に入った
- **Roadmap の新規起票**: Release Communications RSS 全1,757項目を `pubDate` でパースしたが、9/3 22:50Z より新しい起票は無く 9/4〜9/8 の5バッチが空振りだった。⚠️ 総項目数は 1,769 → 1,757 と12件減り `lastBuildDate` も 9/4 から5日連続動かないため、どちらの指標でも新規ゼロを判定できない
  - ⚠️ 検知遅延の構造も再現した。02 の実行時刻は UTC 21:02 で Roadmap の公開時刻帯（UTC 22:50〜23:13）より1時間50分早く、9/8 UTC 分の起票があっても翌日以降にしか見えない
- **Release Wave**: リネーム後の5ページはいずれも HTTP 200・`updated_at` 2026-09-03T14:35Z・`git_commit_id` 06b3b6ba で、6日連続の据え置きだった。⚠️ 9/8 の「製品別4本が 404」は旧パス（`microsoft-` 接頭辞付き）を叩いた結果で、新パスは 200 である
- **Released Versions**: Copilot Studio 版は全リージョンで 2026.6.3（UX は 26.06.21-24）のままで、ページの `updated_at` も 2026-07-01T15:55Z から70日間動いていない。⚠️ 明記された「毎週火曜更新」の定例日（UTC 9/8）にも新ビルドは出ていない
- **Power Platform Blog / Purview**: 親ページの先頭は 9/3 の PPCC 記事のままで、子カテゴリも Power Automate 8/13・Power Apps 9/1 の既報である。`purview/whats-new` は 2026-08-28T07:31Z のままで、569612（Copilot メモリの Purview 保持・GA 2026年9月）は本日も Purview 側に未掲載である
- **Partner Center**: 9月アナウンスページは掲載4件・`updated_at` 2026-09-04T22:04Z のままで追記がない。9/3 告知の月次パートナースキリングセッション「Partnering for Success Together」は本日 9/9 に開かれる

### GitHub / 開発ツール

- **Copilot CLI に Vim モード**: GitHub が pre-release `v1.0.84-2` を 9/8 13:50 UTC に出し、Vim モードを全ユーザーへ開放した。`/vim` か `editorMode` を `vim` に設定すると composer がモーダル編集になる。安定版は `v1.0.83`（9/4）のままである
  - Windows のサンドボックスポリシーが対話的シェルコマンド中のブロックされたアクセスを記録し、承認するとその制限下で再実行するようになった
  - 修正は tmux / screen 上のキー挙動、MCP サーバのクライアント識別子の一貫性、MCP 承認プロンプトのキャンセル、拡張機能再起動後のフック復帰などである
- **Dependabot の GitHub Packages 自動認証**: 利用者が PAT なしで `*.pkg.github.com` / `ghcr.io` のプライベートレジストリへ到達できるようになった（9/8）。Dependabot が `packages: read` 権限の `GITHUB_TOKEN` を使うため `dependabot.yml` の変更は不要で、認証目的の PAT ベース設定は削除できる。パッケージ側で「Manage Actions access」にリポジトリを Read 権限で追加する作業が要る。⚠️ 6月23日の初回リリース後に npm のパッケージ解決と競合して一時無効化され、自動認証をフォールバックに限定して再有効化された経緯がある
  - https://github.blog/changelog/2026-09-08-automatic-dependabot-access-to-github-hosted-registries/
- **github.blog の Copilot ラベル**: 9/4 の2本が最上位のままで、9/5〜9/8 の新規はない（4日間）

### Cursor / xAI / Devin

- **Cursor**: changelog は 9/2 の Self-hosted machines、フォーラム Announcements は 9/2 の Grok Bot Android 版が最上位のままで、どちらも1週間動いていない。⚠️ Cursor は GPT-6 Astra の提供開始を告知しないまま6日目で、Copilot は 9/4 に GA、Codex CLI は `0.153.1`〜`0.153.4` で対応済みである
- **Grok 4.7**: xAI は公開見込み **9/12**・パラメータ 2.1兆という二次情報から動いていない。出所は 9/2 の Musk の X 投稿である。⚠️ ローンチページ・API モデル ID・価格・モデルカード・コンテキスト長・ベンチマーク表のいずれも未公開で、公式提供中の最新は Grok 4.6（8/12・context 50万トークン・$2/$6）である
- **Devin**: 一次・代替一次のいずれからも読めない状態が継続している（`docs.devin.ai` / `cli.devin.ai` ともゲートウェイ拒否）

### MCP / エージェント標準

- **MCP 公式ブログ**: 8/22 の「The New MCP Roadmap」が最上位のままで新規はない（18日間）。RSS `index.xml` は 200 で取得できている
- **WebMCP Challenge**: 提出締切 9/4 を経過し、受賞発表は 9/23、賞金総額は $35,000 である。⚠️ MCP 公式ブログ側に言及がなく OpenAI 発の別系統として扱う
- **A2A**: AAIF 参加は未確定のままで、一次3ホストはゲートウェイ拒否が継続している

### オープンウェイト / ローカル LLM

- **新規公開ゼロ**: 8 org のいずれにも 9/8 の新規公開はない。`Qwen` / `moonshotai` / `deepseek-ai` / `meta-models` / `mistralai` / `zai-org` / `openai` / `google` を `createdAt` 降順と `lastModified` 降順の両方で確認した
  - 各 org の最新作成: `Qwen-Drive-1.0-4B` 8/27 ／ `DeepSeek-V4-Flash-Vision-Exp` 8/31 ／ `GLM-5.3-Flash-BF16` 8/25 ／ `timesfm-3.0-pytorch` 8/24 ／ `Muse-Glimmer-30B-ExecuTorch-PTE` 8/10 ／ `Shieldstral-1.0-3B` 7/16 ／ `Kimi-K3` 6/13
  - ⚠️ `mistralai` の `lastModified` 降順の先頭に `Mistral-Small-4-119B-2603-NVFP4`（更新 9/7）が現れたが、作成日は 7/16 より古くカード更新にとどまる
- **PyTorch Foundation に中国勢3社**: Alibaba Cloud と Cambricon が Platinum 会員として理事会と技術諮問評議会に各1議席を得て、Ant Group が Gold 会員で加わった（9/8・上海の KubeCon + PyTorch Conference China 2026）。⚠️ 提案への直接の影響は薄いが、オープンソース AI スタックの意思決定構造の変化として記録する
  - https://pytorch.org/blog/alibaba-cloud-ant-group-cambricon-and-huawei-come-together-in-shanghai-to-advance-the-open-source-ai-stack-at-pytorch-conference-china/

### 資本・M&A・市場データ

- **Cognition が $2B・$48B で成立**（ハイライト2参照）。
- **Mistral が €3B を Samsung 主導で調達した — 欧州テック史上最大の株式調達となった。** 9月8日公表の Series D で、ポストマネー評価額は **€21B 超**（1年前は €11.7B）である。Samsung Electronics が主導し、EQT 運用の Scaleup Europe Fund と既存の PSG Equity が共同主導に入った
  - 新規投資家は Advent、BlackRock の運用ファンド、ルクセンブルク大公国である
  - 既存投資家として a16z、ASML、General Catalyst、Lightspeed、NVIDIA、Salesforce Ventures が参加した
  - 資金使途はデータセンターの自社保有と外部計算資源の追加借用で、年内に ARR $1B 超に届く見通しとしている
  - https://techcrunch.com/2026/09/08/mistral-raises-e3b-as-sovereign-ai-becomes-big-business/
- **Anthropic が Decart の買収交渉を打ち切った**（9/8 報道）。評価額は約 **$60億**とされ、デューデリジェンスで判明した非公開の事項が判断に影響したと伝えられている。Decart は world models と学習コストを下げるハードウェア効率化ソフトウェアを手がける。⚠️ 一次未読で、Anthropic・Decart のどちらも公式声明を確認できていない。⚠️ 報道は本件を IPO 準備と結びつけているが、IPO 自体が観測（10月・$2T 超）にとどまるため因果は確定していない
- **Similarweb 8月分シェアが発信元投稿で確定した。** ChatGPT **55.5%**・Gemini 25.6%・Claude 9.3%・DeepSeek 3.4%・Grok 2.4%・Copilot 1.6%・Perplexity 0.9% である。12カ月前は ChatGPT 73.3%・Gemini 12.9%・Claude 1.9% で、⚠️ Claude は1年でおよそ5倍と伸び幅が Gemini（12.9% → 25.6%）を上回る。⚠️ 09-08 に割れていた「ChatGPT 68%」系の数値は同社が2026年1月に出した First Global AI Tracker の値が日付表記なしで流通したもので、投稿単位で公表月を確認してから引く
  - https://x.com/Similarweb/status/2096878021378466096
- **Accenture と Google Cloud が FDE 1,000名の専任部門を設けた。** Accenture Gemini Enterprise Business Group を Accenture の一部門として運営し、Google Cloud が forward deployed engineer に訓練を提供して Gemini Enterprise 上の個別 AI アプリ開発を担わせる。母体となる Google Cloud 有資格者は約5万人である。定量成果として YouTube の NFL Sunday Ticket 事例で平均通話処理時間 **37%削減**・顧客感情 11%改善が示された。⚠️ 「Google Cloud が導入実行の人手不足で追う側にいる」という文脈で報じられている点は割り引いて読む
  - https://newsroom.accenture.com/news/2026/accenture-and-google-cloud-deepen-partnership-with-formation-of-new-accenture-gemini-enterprise-business-group
- **Forus が $150M を $3B 評価で調達した。** Bain Capital Ventures 主導の Series C で 9月8日公表である。⚠️ 関心領域からやや外れるため数値の裏取りは行っていない
- **定点の市場データに新規公表はない。** IDC・Gartner・MM総研・NRC のいずれにも本日の新規公表を検知できず、引用可能な最新値は IDC 国内 AI 市場支出額 2025年 2兆3,725億円 → 2029年 6兆8,897億円・CAGR 36.0%、Gartner 世界 AI 支出 2026年 $2.59兆・+47% のままである。⚠️ IDC は検索面に日付なしの旧記事が3日連続で浮上しており、「2029年に4兆1873億円」は別系列の予測で既収録の支出額系列とは対象が異なる
- 既報: Anthropic のリボルビング枠 $150億拡大観測（9/3）、Anthropic × Lambda 約 $350億、直近クラウド契約は計 $1,750億とされる、SpaceX による Cursor 買収完了（8/14・$60B）

### Apple / クラウド

- **Apple 特別イベントが本日 9/9 10:00 PT（日本時間 9/10 02:00）に開かれる。** 告知は 8/26 の "Surprise and shine" である
- **Apple Developer News**: 9/1 の「Upcoming changes to Rosetta support for Intel-based macOS apps」が最上位のままで、9/2 以降の新規はない。macOS 26.4 以降は Intel 専用アプリ起動時にシステム通知が出て、macOS 27 が Rosetta を載せる最後のリリースになる。⚠️ AI 関連の最新は 6/11 の ImageCreator クラス廃止告知のままで3ヶ月動いていない
- `azure.microsoft.com` はゲートウェイ拒否が継続している（09-05 初出・本日未試行）

## 直近の注目予定

- **9/9**: Apple 特別イベント（10:00 PT）／ GLM-5.3-Flash の Z.ai 経由50%割引が終了 ／ PVA ヘルプチャットボット削除が発効 ／ パートナースキリングセッション初回
- **9/10**: MAI-Code-1-Flash が全 Copilot 体験から廃止
- **9/11**: 拡張機能 What's New / Copilot Studio モデル可用性一覧（週次確認）
- **9/12**: Grok 4.7 の公開予定（Musk の X 投稿のみが出所・公式の裏づけなし）
- **9/13**: Claude Code の週次上限50%増が終了 ／ Power CAT リリース / PnP コミュニティコール（週次確認）
- **9/14**: Claude Code の標準週次上限が恒久的に +25%（現行比では17%減）／ 週次復旧チェック（月曜）／ ppweekly / MS-4005 / 課金レート表（週次確認）
- **9/17**: OpenAI DevDay Exchange の応募締切 ／ Anthropic Startup Grant Program の配分年度締切（二次のみ）
- **9/21**: Anthropic ウェルビーイング研究助成の応募締切
- **9/23**: WebMCP Challenge の受賞発表
- **9/24**: OpenAI の Videos API と Sora 2 系が退役（代替モデルの提示なし）
- **9/28**: Copilot のチャット3面統合 ／ code review の既定 effort が Lite → Balanced ／ チャットのデータ保持がアカウント存続期間へ ／ OpenAI の `gpt-3.5-turbo-instruct` / `babbage-002` / `davinci-002` / `gpt-3.5-turbo-1106` が停止
- **9/29 以降**: `claude-sonnet-4-5-20250929` の暫定退役日（確定日ではない）
- **9/30**: Gemini の旧 `gemini-omni-flash-preview` エンドポイント廃止 ／ M365 E7 プロモ最終日 ／ E5・E3 の CSP 割引終了 ／ 2026 Wave 1 の対象期間終了
- **9 月**: iOS 27 / macOS 27 GA ／ Claudeforce のオープンベータ（二次情報）／ Release Plans の新規掲載停止 ／ Copilot Tuning の Public Preview 再開 ／ Copilot デスクトップアプリの広範展開（中旬）／ OpenAI の IPO 観測
- **10/1**: Copilot Business・Enterprise の既存顧客が前払い必須に ／ Apple の EU 向け新ビジネス条件が発効 ／ CSP software 価格改定 ／ Ask Gemini in Chat のプロモーション上限が終了
- **10/2**: GitHub Copilot が Gemini 3.5 Flash / Gemini 3.6 Flash / Kimi K2.7 Code / Claude Opus 4.7 を全体験から廃止
- **10/5**: Anthropic ウェルビーイング研究助成の full proposal 提出期限（採択者）
- **10/15 以降**: `claude-haiku-4-5-20251001` の暫定退役日（確定日ではない）
- **10/16–11/11**: OpenAI DevDay Exchange 8都市（東京は 10/20）
- **10/23**: OpenAI のレガシースナップショット退役（`gpt-3.5-turbo-0125` / `gpt-4-0613` / `o1-2024-12-17` / `o4-mini-2025-04-16`）
- **10/27〜29**: PPCC 2026（ラスベガス MGM Grand）
- **10/31**: OpenAI の既存 evals が読み取り専用になる
- **10 月**: Anthropic の IPO 予定（$2T 超の評価額を目標と報道）／ 韓国 App Store のコンテンツ記述子2件が All → 12+
- **秋**: Anthropic の Enterprise Frontier Safeguards が段階的に提供開始（二次情報）
- **11/15**: Release Planner 退役
- **11/21**: GPT-5.6 Sol の暫定値下げが有効とされる期限
- **11/24 以降**: `claude-opus-4-5-20251101` の暫定退役日（確定日ではない）
- **11/30**: OpenAI の Reusable prompts・Evals プラットフォーム・Agent Builder が停止
- **12/1**: OpenAI の GPT Image 系が停止（`gpt-image-1-mini` / `gpt-image-1.5` / `chatgpt-image-latest` → `gpt-image-2`）
- **12/2**: EU AI Act の生成コンテンツ標識義務、8/2 以前に市場投入済みシステムへの猶予終了
- **12/11**: OpenAI の旧スナップショット退役（`gpt-5-2025-08-07` / `o3-2025-04-16` / `o3-pro-2025-06-10` 等）
- **12/31**: Gemini 3.8 Flash と 3.7 Flash の導入価格が終了 ／ GitHub Copilot の Fable 5.1 / Fable 5 に対する ZDR 暫定免除が終了
- **年内**: Anthropic の新データ保持方式（顧客自身のクラウドでの30日保持）投入予定 ／ OpenAI の Jalapeño チップの初期展開
- **2027-01-06**: OpenAI で大半のユーザーの新規ファインチューニングジョブ作成が終了
- **2027-01-20**: OpenAI の audio / realtime 系退役（`gpt-realtime` / `gpt-audio` / `gpt-4o-audio` と mini 系）
- **2027-02-26**: OpenAI の文字起こし4モデル退役（`whisper-1` / `gpt-4o-transcribe` 等）
- **2027-03-01 / 2028-10-01**: SharePoint クラシック体験の退役
- **2027-06-30**: Claude for Teachers の学区登録期限
- **2027年末**: Anthropic が借りる Nscale West Virginia データセンター（460MW）の稼働開始見込み
- **2028-03**: OpenAI が「automated AI researcher」の実現目標とする時期

## 改善メモ

- 新規提案 3件: 01 B-064（成果物リポジトリからの一次確定を他ベンダー・著者個人まで拡張）／ 02 B-062（Frontier 限定機能は Learn の What's New と機能ページだけが一次）／ 03 B-035（Similarweb 月次トラッカーの取得先を発信元 SNS 投稿へ定義し直す）。いずれも詳細は各リポの台帳
- 継続提案は 01 が18件（提案中は計45件・最多 B-013 41回目）、02 が25件（最多 B-011 50回目）、03 が4件（最多 B-004 72回目）である
- 障害の変化: 01 が `terrytao.wordpress.com` / `www.nature.com` を、03 が `www.hpcwire.com` / `newsroom.accenture.com` / `officechai.com` / `www-cdn.anthropic.com` / `x.com` をゲートウェイ拒否として新規記録した。復旧は3ソースとも0件
- ソース間の重複: Anthropic のフェルマー形式化を 03 が5日遅れで初捕捉した一方、01 は 9/4 に既報として扱っている。同一の Anthropic research 記事に対する捕捉日が両リポで5日ずれている
