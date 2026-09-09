# AI News Daily Summary — 2026-09-10

期限と価格の前提が同時に動いた日である。Apple が iOS 27 の配信日を 9/14 に確定し、SiriKit の退役で iOS アプリ側の対応要件が変わった。OpenAI の一次料金ページからは、コンテキスト長で単価が2階層に分かれる構造が確定し、単一単価の試算が長文脈でほぼ倍ずれることが判明している。GitHub は Code Quality の指摘を最大25件まとめて Copilot に委任できる機能を GA にした。Microsoft 側は5日間止まっていた Roadmap の起票が再開し、Cowork を Purview DLP で統制する項目が起票された。

## 今日のハイライト

### 1. Apple が iOS 27 の配信日を 9/14 に確定した — Siri の入口が SiriKit から App Intents へ一本化される

**要点**: Apple が **9/14** の iOS 27 配信と新世代 Siri を告知した。SiriKit は iOS 27 で退役するため、iOS アプリの前提は「音声で操作できるか」から「アシスタントから呼べるアクションを宣言しているか」へ変わる。

**詳細**: 9/9 の特別イベント "Surprise and shine" での告知で、基調講演は Tim Cook を継いだ John Ternus が担当した。

- 配信条件: iOS 27 / iPadOS 27 は 9/14（月）に無償配信され、Siri は**英語のベータ**として出荷される。EU ではローンチ時点で提供されない
- 開発者側: SiriKit ベースのままのアプリはビルドは通るが、新しい Siri からの音声トラフィックも Spotlight のインデックスも受け取らなくなるとされる。App Intents 2.0 側にはストリーミング応答・複数ターン・View Annotations・App Schemas が入る
- 対応機種: iOS 27 は iPhone 11 / SE（第2世代）まで動くが、Apple Intelligence と Siri の一部は **iPhone 15 Pro 以降**を要する
- ハードウェア: iPhone 18 Pro が $1,199、Pro Max が $1,299、折りたたみの iPhone Ultra が加わった。予約は 9/12、発売は 9/18

⚠️ **一次未読**。`apple.com` はオリジン403で、`developer.apple.com/news/` はイベント当日にもかかわらず 9/1 の Rosetta 告知が最上位のままである。上記は複数の二次一致で採った。「新しい Siri は Google Gemini で動く」という記述は二次のみに現れ、モデル供給元の内訳は一次で確認できていない。

- https://developer.apple.com/news/ （9/1 が最上位・イベント未反映）
- https://9to5mac.com/2026/09/09/apple-confirms-ios-27-release-date-september-14/
- https://www.macrumors.com/2026/09/09/apple-announces-ios-27-release-date/

### 2. OpenAI の単価がコンテキスト長で2階層に分かれていた — 単一単価の試算は長文脈でほぼ倍ずれる

**要点**: 一次料金ページの直接確認で、`gpt-5.6-luna` などの単価が**短文脈と長文脈で別建て**だと確定した。あわせて CFO が Luna はオープンウェイトのクラウド実行より安いと述べており、「単一単価で見積もる」前提と「安く回すならオープンウェイト」の前提が同時に崩れた。

**詳細**: 発言は 9/8〜9/9 に San Francisco で開かれた Goldman Sachs の Communacopia + Technology Conference でのもの。

- 単価の一次確定: `gpt-5.6-luna` は Standard ティアで短文脈が入力 **$0.20** / 出力 $1.20、長文脈が入力 $0.40 / 出力 $1.80（100万トークンあたり）だった。GPT-6 Astra は $10.00 / $50.00、GPT-5.6 Sol は $4.00 / $20.00 で、long context の境界は 272K トークンである
  - ⚠️ この2階層構造は登録ソースのどこにも載っていない。単一の数値で試算していると長文脈運用でほぼ倍ずれる
- 値下げの効き: Luna の80%値下げ（7/30・$1/$6 → $0.20/$1.20）で利用が約10倍に増えたとされ、Friar は GLM-5.3 のクラウド実行と比べて自社が安いと述べた
- 課金モデル: OpenAI は利用量ではなく**ビジネス上の成果に基づく課金**を試しており、チップ設計・ライフサイエンス・金融の業種別展開を進めている
- Jalapeño チップ: Broadcom との共同開発で 9ヶ月未満で tape-out に到達し、初期サンプルは一般的な AI GPU に対して約50%のコスト削減を示した。年内の初期展開を目標としている

⚠️ カンファレンス発言であり一次未読（`openai.com` はオリジン403）。価格だけは公式料金ページで裏を取ったが、GLM-5.3 との比較・10倍・50%削減はいずれも OpenAI 自身の主張で第三者検証はない。

- https://developers.openai.com/api/docs/pricing
- https://www.investing.com/news/economy-news/openai-offers-ai-for-chip-design-touts-cost-advantage-over-opensource-cfo-says-4892636
- https://venturebeat.com/technology/ai-price-wars-openai-cuts-gpt-5-6-luna-prices-by-80-as-model-competition-shifts-toward-cost

### 3. GitHub Code Quality の一括 agentic autofix が GA になった — 指摘対応が1件ずつから25件単位へ変わる

**要点**: 開発者が Code Quality の指摘を**最大25件**まとめて Copilot に委任し、ブランチ上で自己検証させて PR を出させられるようになった。個別の Generate fix は Assign to Copilot に置き換わり、9/1 に減った AI クレジットを1操作で大きく消費しうる形になる。

**詳細**: 9/9 付で一般提供が始まった。1ページ上の standard findings を最大25件選択して一括で割り当てると、Copilot がブランチ上で修正し、自分の変更を検証してからレビュー用の PR を開く。

- 対象: **GitHub Team** と GitHub Enterprise Cloud（データレジデンシー版を含む）。専用ポリシーは新設されず、既存の Code Quality のエンタープライズポリシーをそのまま継承するため追加の管理操作は要らない
- 費用: 割り当てごとに AI クレジットを消費する。9/1 発効の込みクレジット減額（Business が $30 → **$19**・Enterprise が $70 → $39）と直結し、一括委任は消費量が読みにくい
- 同日の関連: シークレット混入 PR のマージを止めるルールセット `Require secret scanning alerts are resolved` が public preview で入った。push protection がプッシュ段階で止めるのに対し、こちらは PR 段階で「head コミットのスキャン完了」と「当該 PR が持ち込んだシークレットの未解決アラートがゼロ」の2条件を課す

- https://github.blog/changelog/2026-09-09-remediate-code-quality-findings-with-agentic-autofix
- https://github.blog/changelog/2026-09-09-block-pull-requests-with-exposed-secrets-from-merging

## カテゴリ別まとめ

### Anthropic / Claude

- **Claude Code の changelog が `2.1.266` まで進んだ**（9/8）。`2.1.266` は LLM ゲートウェイ／プロキシ設定の回帰修正1点で、`CLAUDE_CODE_USE_GATEWAY` を設定すると Cloud ゲートウェイのサインインを不当に強制し、API キーや `apiKeyHelper` と併用する構成が全リクエスト失敗していた問題を解消している。設定変更は不要である
  - `2.1.265`（9/8 19:05 UTC）の内訳は4系統で、テレメトリに `user.email` と `user.groups` が加わり、`--plugin-dir` で複数のプラグインフォルダを指定できるようになり、ツール結果に **1GB の上限**が入り、サブエージェント再開時のプロンプトキャッシュ再利用と `/model opusplan[1m]` の拒否が修正された
- **npm の `dist-tags` は `{stable: 2.1.236, latest: 2.1.266, next: 2.1.267}`** である。`2.1.267` は 9/9 18:25 UTC に `next` へ publish されたが changelog にも CHANGELOG.md にも記載がなく内容は未確定で、`stable` と `latest` の差は**30版**に開いた。stable 固定の組織に未到達の権限・ポリシー系は `2.1.251`・`2.1.260`・`2.1.261`・`2.1.263` の4件である
- **Claude Code の週次上限50%増の終了が 9/13 に迫っている**。9/14 からは標準週次上限が恒久的に +25% となり、現行比では **17%減**になる（既報・カウントダウンとして再掲）
- **Claude Platform API の release notes は 9/3 が最上位のまま**で、9/4〜9/9 の追加はない。`support.claude.com` の Release Notes も 9/1 の Fable 5.1 / Mythos 5.1 が最上位のままで、`claude.com/blog` にも 9/8 以降の新規記事はない
- ⚠️ Anthropic の**8月 Risk Report は26日連続で一次未読**である（初出 08-17）。`www.anthropic.com` のゲートウェイ拒否が解消しない限り読めない
  - https://code.claude.com/docs/en/changelog

### OpenAI / Codex

- 単価の2階層構造と成果連動課金はハイライト2参照。
- **Prompt Cache Diagnostics が Responses API で GA になった**（9/8）。**GPT-5.6 以降**の対応モデルで、直前のレスポンスとキャッシュ再利用を比較し、プロンプトキャッシュのミスが起きた理由を分類してトラブルシューティング指針を返す。ヒット率の監視は Prompt Caching Dashboard 側が担う
- **Codex CLI は pre-release が2日で8版出た一方、安定版は `0.153.4`（9/4）のまま5日間据え置きである**
  - ⚠️ `alpha.6.1`（9/9 11:51 UTC）が `alpha.11`（9/9 09:14 UTC）より新しく、**版番号の大小と公開日時が一致しない**。既存の alpha へ後からパッチを当てる運用に見えるので、最新の版番号を最新リリースと読み替えないこと
- **退役一覧と料金ページはいずれも据え置きである**。`deprecations` は 8/26 の文字起こし4モデル（停止 2027-02-26）が最新のままで13日連続、料金ページは17日連続で単価に変更がない。⚠️ `gpt-5.4-cyber` は7日連続で単価欄が空のままで、同じ節の `gpt-5.6-cyber` / `gpt-5.5-cyber` には $12.50 / $75 が入っている
- ⚠️ `learn.chatgpt.com` はゲートウェイ拒否が継続しており、ChatGPT アプリ側と Codex アプリ／プラグインの更新は本日も確認できていない
  - https://developers.openai.com/api/docs/deprecations

### Google

- **Gemini API changelog は 9/3 の Lyria 3.5 public preview が最上位のまま**で、7日間新規がない。料金改定の告知もなく、`gemini-omni-flash-preview` の廃止は **9/30**（後継 `gemini-omni-1.1-flash`）、Gemini 3.7 Flash の導入価格が 12/31 までという記載も不変である
- 到達できる Google 一次が `ai.google.dev` だけという状態は変わらない。登録済み5ソースはゲートウェイ拒否が継続している
  - https://ai.google.dev/gemini-api/docs/changelog

### Microsoft 365 Copilot / Cowork

- **Purview DLP が Cowork へ広がる**（Roadmap **570845**・Preview 9月 / GA 10月）: データセキュリティ管理者が、M365 Copilot と Cowork を1本の DLP ポリシーで統制できるようになる。Cowork の統制点がテナント一括のトグルしか無かった前提が、内容の粒度へ移る
  - ラベル付きナレッジソースを Cowork に使わせない
  - 対応する機微情報の種類を含むプロンプトをブロックする
  - 機微なプロンプトが Bing の Web 検索へ送られるのを制限する
  - ⚠️ `purview/whats-new` は 2026-08-28 のままで本項目も 570445 も掲載されていない
- **Cowork のアプリ生成（App skill）に Message Center の告知が見つかった**（**MC1469329**）: 管理者は、Cowork への展開が 9/8 開始・**9/14 完了見込み**で、Copilot Studio 版が「次の数週間」で**対象メーカーに既定オン**で降りてくると告知された。Frontier 限定という前日までの理解と食い違う
  - ⚠️ MC の本文は読めない（`mc.merill.net` が34日連続でゲートウェイ拒否）ため、要旨は WebSearch の索引スニペットのみで一次未確認である
  - 同系の App Builder は `support.microsoft.com` の復旧により一次解説を取得できた。**Frontier プログラム**への参加と Microsoft Copilot ライセンスが必須で、英語・米国のみ、**GPT-5** で動作し利用者はオプトアウトできない
  - ⚠️ 共有は生成リンク方式で、**リンクを持つ全員がアプリとその全データを開ける**。アプリを削除すると全受領者のアクセスが即時に切れる
- **Roadmap の起票が5日ぶりに再開した**: 9/8 22:57Z に8件が起票され、総項目数は 1,757 → **1,766** へ動いた。Copilot 関連は3件である
  - Agent 365 Dashboard の価値可視化（570847・Preview 9月 / GA 10月）: 事業部門のリーダーが、Viva Insights の Agent 365 Dashboard でエージェントが生んだ推定支援時間と寄与した業務の種類を見られるようになる
  - Teams の会議共有ファイル（570427・GA 10月）: 利用者が会議に付けたファイルとリンクが参加者へ自動共有され、Facilitator エージェントを含む会議中の AI がグラウンディングに使う
  - Teams チャネルのバックアップ（570668・GA 12月）: 管理者が、チーム・チャネルとその配下データを直近の正常な状態へ復旧できるようになる。保持期間は30日間である
- **Release Notes は August 25, 2026 が先頭のまま**で、隔週の期日 9/8（UTC）から2日過ぎており周期が崩れている。Cowork 配下のドキュメントは 9/9 に再ビルドされたが、New features 4件・モデルピッカー8件・組み込みスキル表14件に増減はない
  - ⚠️ `cowork-admin-governance` は同じ再ビルドを受けながらモデル記述が古いままで、8/27 にピッカーから消えた Sonnet+Opus Advisor を現行として書き、GPT 5.6 系と GPT-6 Astra を欠いている
  - https://www.microsoft.com/en-us/microsoft-365/roadmap
  - https://support.microsoft.com/en-us/topic/build-apps-with-microsoft-365-copilot-a50c7eb7-ed36-45b5-baa4-b24e70f3b550

### Copilot Studio / Power Platform

- **What's New は July 2026 節が最新のまま**で、8月節・9月節とも作成されていない。June 節の GitHub Copilot ハーネスは `(Production-ready preview)` の表記が残り、GA（8/3）から38日連続の未反映である
- **Released Versions は 2026.6.3 のまま71日動いていない**。⚠️ 本文が明記する「毎週火曜更新」の定例日（UTC 9/8）を過ぎても新ビルドが出ておらず、GA の検知経路が Release Wave の緑チェックへ一段と寄っている
- **非推奨一覧に新規項目はない**。週次確認の定例日として本文まで突合したが見出しは94本のままで、9/9 に発効した PVA ヘルプチャットボット削除の節にも変更はない。Release Wave のリネーム後5ページも 9/3 から7日連続の据え置きである
- **ASPX がレポートツールから実行支援へ変わった**（9/8・Partner Center）: CSP 各層と SSP / GSI・SI のパートナーが、Copilot の商談シグナルを受け取ってそこから直接行動できるようになる。FY27 の優先領域は無償から有償への転換、**Microsoft 365 E7** のターゲティング、Cowork の利用状況、Frontier アカウント、エンドポイントを80超から4本へ減らす **API v1.5** の5つである
  - https://learn.microsoft.com/en-us/microsoft-copilot-studio/whats-new

### GitHub / 開発ツール

- Code Quality の一括 autofix とシークレット混入 PR のマージ禁止はハイライト3参照。
- **Copilot for JetBrains にエンタープライズ管理サンドボックスが入った**（9/8・public preview）: 管理者が、サンドボックスの有効／無効・ファイルシステムとネットワークのアクセス制御・プロキシ設定・開発者ツールへのアクセス・macOS Keychain へのアクセスを中央で設定できるようになる。管理設定は利用者設定を上書きし、該当項目は IDE 上でロックされて「組織管理」と表示される。表示には `Editor Preview` フラグの有効化か管理設定の配布が要る
- **Copilot CLI の pre-release `v1.0.84-3` が 9/9 に出た**。`/copy` がタスク完了メッセージを含められるようになり、OAuth 認証を使う MCP サーバーへの接続の信頼性が向上した。安定版は `v1.0.83`（9/4）のまま5日間動いていない
- **9/8〜9/9 の GitHub changelog は計7件である**。上記のほか、GitHub Advanced Security のトライアル提供範囲拡大、GitHub Enterprise Server 3.22 の GA、新カスタマーポータル `help.github.com` の開設、Dependabot のレジストリ自動アクセス（既報）が出ている
- **本日 9/10 に MAI-Code-1-Flash が全 Copilot 体験から廃止された**。以降は 9/28 のチャット3面統合・code review 既定 Balanced 化・データ保持変更、10/1 の既存顧客前払い必須、10/2 の4モデル廃止が続く
  - https://github.blog/changelog/2026-09-08-enterprise-managed-sandbox-in-copilot-for-jetbrains

### Cursor / xAI / Devin

- **Cursor は changelog もフォーラム Announcements も 9/2 が最上位のまま**で、8日間動いていない。⚠️ GPT-6 Astra の提供開始を告知しないまま7日目で、Copilot は 9/4 に GA、Codex CLI は `0.153.1` 以降で対応済みである
- **Grok 4.7 の公開見込み 9/12 が2日後に迫るが、xAI 側の一次は何も出ていない**。ローンチページ・モデル ID・価格・モデルカード・コンテキスト長・ベンチマークのいずれも未公開で、出所は 9/2 の Musk の X 投稿のみである。公式提供中の最新は Grok 4.6（8/12・context 50万トークン・$2/$6）である
- Devin は `docs.devin.ai` / `cli.devin.ai` ともゲートウェイ拒否で、一次・代替一次のいずれからも読めない状態が続いている

### MCP / オープンウェイト

- `blog.modelcontextprotocol.io` は RSS で読めるが、8/22 の "The New MCP Roadmap" が最上位のまま**19日間**新規がない。WebMCP Challenge は提出締切 9/4 を過ぎ、次は 9/23 の受賞発表（賞金総額 $35,000）である
- **登録8 org のいずれにも新規公開はない**。`Qwen` / `moonshotai` / `deepseek-ai` / `meta-models` / `mistralai` / `zai-org` / `openai` / `google` を作成日降順と `lastModified` 降順の両方で確認した。⚠️ HF の `downloads` は前日と同値で、30日ローリングの反映ラグとみられるため増減の解釈はしない

### 資本・市場・新規プロダクト

- **Anthropic の IPO 開始が10月中旬へ後退した**: マーケティング開始が10月中旬以降、S-1 の公開が9月下旬へずれ、上場は11月の米中間選挙の数日前に置く想定と報じられた。先行して **$15B のリボルビング与信枠**の確定を進めており、$2兆規模の上場が年内前半という前提は崩れている
  - ⚠️ 一次の開示ではなく関係者取材にもとづく報道段階の情報で、日程はいずれも確定していない
- **Meta が個人向けエージェント Muse を提供開始した**（9/8・米国）: 利用者は iOS / Android / Web と WhatsApp から呼び出し、メール送信・旅行予約・フォーム入力・購買を代行させられる。実行基盤は利用者専用のクラウド VM で、同じ VM 上の Sentinel が承認しない限り外部通信が出ない設計である
  - 料金は無料・Power（月 **$20**）・Maximum（月 $100）の3段で、有料ティアが買うのは機能ではなく利用量である。⚠️ 有料2段の上限トークン数は未公表で、公開値は無料枠の週1億トークンのみである
- **エージェント統制系スタートアップに5カ月で $435M が入った**: 2026年4月から9月にかけて、エンタープライズ AI エージェントのセキュリティ・ガバナンス分野の12件に総額が集まり、うち9件は用途を社内での安全な実行に絞ったラウンドだった。⚠️ 集計主体と対象範囲の定義が示されておらず、単独の数値として提案資料に引用するには根拠が弱い
- **市場データの定点ソースに新規公表はない**: IDC・Gartner・MM総研・NRC・Similarweb のいずれも本日の更新がなく、引用可能な最新値は据え置きである。Similarweb は8月分（ChatGPT **55.5%**・Gemini 25.6%・Claude 9.3%）が最新で、次回は10月上旬の9月分投稿を待つ
  - ⚠️ 検索面に古い発表が2件浮上した。Anthropic の Bengaluru 事務所開設は 2026-02-16、Gartner の「2026年末までにエンタープライズアプリの40%がタスク特化型エージェントを搭載」は 2025-08-26 公表で、いずれも1年落ちの数値である
  - https://www.cnbc.com/2026/09/05/anthropic-ipo-launch-shifts-toward-mid-october-reuters.html
  - https://techcrunch.com/2026/09/08/meta-debuts-its-muse-ai-agent-will-consumers-trust-it/

### エンタープライズ / 政府調達

- **国防総省の AI 契約4件の契約書が FOIA で公開された**: The Intercept が情報公開訴訟で400ページ超を入手したと 9/8 に報じた。対象は 2025年7月に各社 **最大$200M** で結ばれた Anthropic・Google・OpenAI・xAI との契約で、国防総省が OpenAI に対し拒否率を最小化した専用版の提供を求めていた記載が含まれる。既報の Anthropic と国防総省の決裂も、争点が機密ネットワーク上での無制限展開への同意にあったことが契約文書から確認された
  - ⚠️ 一次の契約文書には到達しておらず、内容は報道による
  - https://theintercept.com/2026/09/08/military-ai-weapons-contracts-openai-anthropic-google/

### Apple / クラウド

- iOS 27 と新 Siri はハイライト1参照。
- ⚠️ `developer.apple.com/news/` はイベント当日にもかかわらず 9/1 の Rosetta 告知が最上位のままで、**イベント内容の一次確定は翌日以降に持ち越しである**。AI 関連の Apple Developer News の最新も 6/11 の ImageCreator クラス廃止告知のまま3ヶ月動いていない

## 直近の注目予定

- **9/10**: MAI-Code-1-Flash が全 Copilot 体験から廃止（本日発効）
- **9/12**: iPhone 18 Pro / Pro Max / iPhone Ultra の予約開始 ／ Grok 4.7 の公開予定（Musk の X 投稿のみが出所）
- **9/13**: **Claude Code の週次上限50%増が終了**
- **9/14**: **iOS 27 / iPadOS 27 の配信**（Siri は英語ベータ・EU 提供なし）／ Claude Code の標準週次上限が恒久的に +25%（現行比では17%減）／ Cowork の App skill 展開完了見込み
- **9/17**: OpenAI DevDay Exchange の応募締切 ／ Anthropic Startup Grant Program の配分年度締切（二次のみ）
- **9/18**: iPhone 18 Pro / Pro Max と AirPods 5 の発売
- **9/21**: Anthropic ウェルビーイング研究助成の応募締切
- **9/23**: WebMCP Challenge の受賞発表
- **9/24**: OpenAI の Videos API と Sora 2 系が退役（代替モデルの提示なし）
- **9/28**: Copilot のチャット3面統合 ／ code review の既定 effort が Lite → Balanced ／ チャットのデータ保持がアカウント存続期間へ ／ OpenAI の `gpt-3.5-turbo-instruct` / `babbage-002` / `davinci-002` / `gpt-3.5-turbo-1106` が停止
- **9/29 以降**: `claude-sonnet-4-5-20250929` の暫定退役日（確定日ではない）
- **9/30**: Gemini の旧 `gemini-omni-flash-preview` エンドポイント廃止 ／ M365 E7 プロモ最終日 ／ E5・E3 の CSP 割引終了 ／ 2026 Wave 1 の対象期間終了
- **9 月**: Purview DLP for Cowork のプレビュー ／ Copilot Studio 版アプリ生成体験の提供（既定オン）／ Agent 365 Dashboard の価値インサイトのプレビュー ／ Copilot Tuning の Public Preview 再開 ／ macOS 27 GA ／ Claudeforce のオープンベータ（二次情報）
- **10/1**: Copilot Business・Enterprise の既存顧客が前払い必須に ／ CSP software 価格改定 ／ Apple の EU 向け新ビジネス条件が発効 ／ Ask Gemini in Chat のプロモーション上限が終了
- **10/2**: GitHub Copilot が Gemini 3.5 Flash / Gemini 3.6 Flash / Kimi K2.7 Code / Claude Opus 4.7 を全体験から廃止
- **10/5**: Anthropic ウェルビーイング研究助成の full proposal 提出期限（採択者）
- **10/15 以降**: `claude-haiku-4-5-20251001` の暫定退役日（確定日ではない）
- **10/16–11/11**: OpenAI DevDay Exchange 8都市（東京は 10/20）
- **10/23**: OpenAI のレガシースナップショット退役（`gpt-3.5-turbo-0125` / `gpt-4-0613` / `o1-2024-12-17` 等）
- **10/27–29**: PPCC 2026（ラスベガス MGM Grand）
- **10/31**: OpenAI の既存 evals が読み取り専用になる
- **10 月**: Purview DLP for Cowork の GA ／ Agent 365 価値インサイトの GA ／ Teams 会議共有ファイルの GA ／ Anthropic の IPO マーケティング開始見込み（中旬・報道）
- **11/15**: Release Planner 退役
- **11/21**: GPT-5.6 Sol の暫定値下げが有効とされる期限
- **11/24 以降**: `claude-opus-4-5-20251101` の暫定退役日（確定日ではない）
- **11/30**: OpenAI の Reusable prompts・Evals プラットフォーム・Agent Builder が停止
- **12/1**: OpenAI の GPT Image 系が停止（→ `gpt-image-2`）
- **12/2**: EU AI Act の生成コンテンツ標識義務、8/2 以前に市場投入済みシステムへの猶予終了
- **12/11**: OpenAI の旧スナップショット退役（`gpt-5-2025-08-07` / `o3-2025-04-16` 等）
- **12 月**: Teams チャネルバックアップの GA
- **12/31**: Gemini 3.8 Flash と 3.7 Flash の導入価格が終了 ／ GitHub Copilot の Fable 5.1 / Fable 5 に対する ZDR 暫定免除が終了
- **年内**: Anthropic の新データ保持方式（顧客自身のクラウドでの30日保持）／ OpenAI の Jalapeño チップの初期展開
- **2027-01-06**: OpenAI で大半のユーザーの新規ファインチューニングジョブ作成が終了
- **2027-01-20**: OpenAI の audio / realtime 系退役
- **2027-02-05 以降 / 02-17 以降**: `claude-opus-4-6` / `claude-sonnet-4-6` の暫定退役日（確定日ではない）
- **2027-02-26**: OpenAI の文字起こし4モデル退役（`whisper-1` / `gpt-4o-transcribe` 等）
- **2027-03-01 / 2028-10-01**: SharePoint クラシック体験の退役
- **2027-04-16 以降**: `claude-opus-4-7` 以降の暫定退役日が順次（確定日ではない。`claude-opus-4-7` は Copilot では 10/2 に消える）
- **2027-06-30**: Claude for Teachers の学区登録期限
- **2027年末**: Anthropic が借りる Nscale West Virginia データセンター（460MW）の稼働開始見込み
- **2028-03**: OpenAI が「automated AI researcher」の実現目標とする時期
- **2028-06**: 米国 K-12 教職員向け ChatGPT for Teachers の無料提供期限

## 改善メモ

- 新規提案 1件: 01 B-065（OpenAI の料金ページを Platform Changelog 項の副 URL として追加）。02 は B-062 を回数2へ更新、03 は新規なし。いずれも詳細は各リポの台帳
- 継続提案は 01 が15件（提案中は計46件・最多 B-013 41回目）、02 が36件（最多 B-011 52回目）、03 が4件（最多 B-004 73回目）である
- 障害の変化: 02 で `support.microsoft.com` が復旧し（2026-08-15 からのゲートウェイ拒否が解消）、App Builder の一次解説を全文取得できた。03 は `about.fb.com` をゲートウェイ拒否として新規記録し、`cloud.google.com/blog` の WebFetch に成功して到達可能な一次ホストが7件に増えた
- ソース間の重複: GitHub の 9/9 分3件（Code Quality の autofix GA・シークレット混入 PR のマージ禁止・GHES 3.22 GA）は 03 のみが捕捉し、01 は Copilot ラベル URL を一次にしているため「9/5 以降の新規は JetBrains の1本だけ」と記録している。ラベル外の changelog 項目が 01 の視野から落ちる構造である
- ソース間の重複: Anthropic の IPO 時期は 01 が「10月・$2T 超」を既報として扱う一方、03 は本日ハイライトで初捕捉（5日遅れ）としており、同一報道に対する扱いが両リポでずれている
