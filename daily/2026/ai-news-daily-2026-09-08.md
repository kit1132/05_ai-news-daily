# AI News Daily Summary — 2026-09-08

Microsoft 一次は2日連続で新規発表がゼロだった。Roadmap・Release Notes・Copilot Studio What's New・各公式ブログとも据え置きで、02 は「次バッチは 9/8」と書いた項目の判定を実行時刻の都合で明日へ回している。その中で 01 が OpenAI の社内エージェント稼働の実測（人間1労働日あたり 3.1）を前日セッションでは拾えず本日初検出した。03 は Claude Managed Agents の課金を一次料金ページで確定し、Gemini Notebook の日次回数上限廃止を6日遅れで捕捉した。9/9 は PVA ヘルプチャットボット削除と Apple 特別イベントが同日に来る。

## 今日のハイライト

### 1. OpenAI がエージェント稼働量を自社実測で公開した — 「効果がある」から「人間労働の3倍動いている」へ

**要点**: OpenAI が社内のエージェント稼働を初めて数値で公表し、8月中旬時点で人間の1労働日あたり 3.1 エージェント労働日に達したとした。判断材料がベンダーの定性的な主張から、当事者が但し書きつきで出した実測比率へ変わった。

**詳細**: 公開は 9/6 で、記事は `openai.com/index/research-acceleration-view-inside-openai/`。示された数値は次のとおり。

- エージェント稼働は8時間労働日換算で人間労働の **3.1倍**（8月中旬時点）。2026年6月以前は合計稼働が人間労働を下回っていた
- 研究者1人あたりの推論支出は中央値で **1日 $600 超**、上位の利用者は **1日 $7,000 超**
- 「automated research intern」（人間の指示のもとで定義済みの研究タスクを遂行する系）を9月までに実現する目標を達成したとする
- 次の目標は **2028年3月**までの「automated AI researcher」

⚠️ **OpenAI 自身が 3.1 を生産性3.1倍と読まないよう明記している。** 稼働時間は並列に走り、冗長・失敗・人間による強い誘導を含むためとされる。あわせて 8/7 に Astra の critical サイバー能力の予備証拠が出たことで、Astra はより高セキュリティな研究環境での実行を要求されるようになったと記されている（Preparedness Framework の Critical 到達そのものは 09-04 に既報）。

⚠️ **一次未読。** `openai.com` はオリジン403で、01 の WebFetch も HTTP 403 を返した。数値は複数の二次媒体の一致で採っている。⚠️ **前日 09-07 のセッションは未検出**で、本日が初検出である。

- https://openai.com/index/research-acceleration-view-inside-openai/
- https://simonwillison.net/2026/Sep/6/research-acceleration-the-view-inside-openai/

### 2. Claude Managed Agents の課金体系が一次で確定した — 常駐エージェントの月額を試算できる前提に変わった

**要点**: Anthropic の一次料金ページで Managed Agents の課金が確定した。トークンに加えセッション実行時間 **$0.08/時** が別建てで課金される。常駐型エージェントのコストを見積もれる段階に入った。

**詳細**: 課金は2軸で、トークンと実行時間が独立して積み上がる。

- トークン: Messages API と同一単価。プロンプトキャッシュの倍率（5分書込 1.25倍・1時間書込 2倍・キャッシュ読み 0.1倍）もそのまま適用される
- セッション実行時間: **$0.08 / session-hour**。`running` の間だけミリ秒単位で計上し、`idle`・`rescheduling`・`terminated` は課金対象外
- `inference_geo: "us"` を指定した場合はトークン側に 1.1倍が掛かる
- セッション実行時間は code execution のコンテナ時間課金を置き換える。Managed Agents 利用時にコンテナ時間が二重課金されることはない

一次ページの試算例は、Opus 5 で1時間・入力5万トークン・出力1.5万トークンなら **$0.705**（入力 $0.25・出力 $0.375・実行時間 $0.08）。うち入力4万トークンがキャッシュ読みなら $0.525 に下がる。

⚠️ Managed Agents はベータのままで、全エンドポイントに `managed-agents-2026-04-01` ベータヘッダが要る。⚠️ **ステートフル設計のため ZDR と HIPAA BAA の対象外**であり、ゼロデータ保持や BAA を要件にする案件には現状のまま提案できない。⚠️ 掲載開始日はページ内に日付表記が無く、03 は 09-03 にも同ページを取得しているが当該節を記録していなかった。**本日はじめて確認した事実**として収録する。

- https://platform.claude.com/docs/en/about-claude/pricing
- https://platform.claude.com/docs/en/managed-agents/overview

## カテゴリ別まとめ

### Anthropic / Claude

- Claude Managed Agents の課金が一次で確定した（ハイライト参照）
- **Anthropic は 9/7 に Claude Code の新版を publish しなかった。** 最新は `2.1.263`（9/6 02:07 UTC）のままで、9/5 に続き2日目の非公開日である
- npm `dist-tags` は `{stable: 2.1.236, latest: 2.1.263, next: 2.1.263}`（09-08 実測）。`next` == `latest` の合流が継続している
  - ⚠️ **`stable` は `latest` と27版差で据え置き。** stable 固定組織に未到達の権限系修正は3件＝`2.1.251`（symlink 追跡）／`2.1.260`（括弧を含む権限ルールの破棄と `rm -rf` の確認プロンプト）／`2.1.263`（内容未確定）
  - 欠番は `2.1.244` / `2.1.249` / `2.1.253`〜`2.1.256` / `2.1.262` の計7件で据え置き
- Claude Code changelog の最上位8版は 2.1.263（9/6）→ 2.1.261（9/4）→ 2.1.260（9/3）→ 2.1.259（9/2）→ 2.1.258（9/1）→ 2.1.257（9/1）→ 2.1.252（8/31）→ 2.1.251（8/28）で、日付列に飛びはない
- **Claude Platform API release notes** は 9/3 の `ant` CLI 1.30.0（`ant apply`）が最上位のままで、9/4〜9/7 の追加はない
- **モデル退役ページ**: 新規の退役告知はない。Active は11件で据え置き、直近告知は 2026-06-05 の Opus 4.1（8/5 退役済み）のままである
  - 表の外の Note ブロックで `claude-mythos-preview` が deprecated 扱いのままである（移行先 `claude-mythos-5`）
  - 日付は Anthropic 運営（Claude API / Claude Platform on AWS / Microsoft Foundry）にのみ適用され、Amazon Bedrock と Google Cloud は独自スケジュールを持つ
- `claude.com/blog` は 9/2 の commerce agents 2本が最上位のままで、9/3 以降の新規はない（6日間）。`support.claude.com` Release Notes も 9/1 の Fable 5.1 / Mythos 5.1 が最上位である
- ⚠️ Anthropic の8月 Risk Report は **23日連続**で一次未読である（初出 08-17）
- 03 が `platform.claude.com/docs/en/about-claude/pricing` から全モデル単価を一次取得した。Fable 5.1 / Mythos 5.1 は入力 $10／出力 $50 でキャッシュ読みのみ **$0.25**（基本入力の 0.025倍）、Opus 5 は $5／$25、Sonnet 5 は $2／$10、Haiku 4.5 は $1／$5。Sonnet 5 の $2／$10 が標準価格として確定し 9/1 の $3／$15 への引き上げが行われない旨も同ページの注記で再確認できた（08-18 収録済み）
  - ⚠️ `daily-sources.md` は Anthropic の料金ソースを `www.anthropic.com/pricing` と定義し「オリジン403のため WebSearch 継続」としているが、`platform.claude.com` 側は到達可能である（03 の B-034）

### OpenAI

- OpenAI が社内エージェント稼働の実測を公開した（ハイライト参照）
- **API 単価は15日連続で据え置かれた。** GPT-6 Astra は短文脈で入力 $10／出力 $50、長文脈で $20／$75、Fast mode は短文脈 $20／$100。GPT-5.6 Sol は $4／$20、GPT-5.6 Terra は $2／$12 で、Sol の期間限定価格は「少なくとも 2026年11月21日まで」のままである
  - ⚠️ `gpt-5.4-cyber` の単価欄は5日連続で空のままである
- **廃止期限は11日連続で動いていない。** 最新の告知日は 2026-08-26（転写系4件）のまま。⚠️ 今月2件が到来する — 9/24 に Videos API と `sora-2` / `sora-2-pro` 系（代替の記載なし）、9/28 に `gpt-3.5-turbo-instruct` / `babbage-002` / `davinci-002`（代替 `gpt-5.6-terra`）。⚠️ **GPT-6 Astra 登場に伴う退役告知は依然として無い**
- `developers.openai.com/api/docs/changelog` は 9/3 の2本が最上位のままで、9/4〜9/7 の追加はない
- **OpenAI は Codex CLI の pre-release を3版出した**（安定版は `0.153.4`（9/4 23:25 UTC）のまま）。⚠️ 本文はいずれも `Release <タグ名>` の1行だけで内容は確定できない
  - `0.154.0-alpha.4`: 9/5 00:59 UTC ／ `0.154.0-alpha.5`: 9/7 15:59 UTC ／ `0.154.0-alpha.6`: 9/7 18:03 UTC
  - ⚠️ **`alpha.4` と `alpha.5` は releases ページの上位8件に現れなかった。** 同ページは安定版6件を pre-release 群より上にまとめて出しており日付降順ではない。`github.com/openai/codex/tags` で突き合わせて存在を確定した（01 の B-063）。前日 09-07 の「9/5・9/6 のリリースなし」は、この形の取りこぼしにあたる
- `community.openai.com` Announcements RSS は 9/3 の GPT-6-Astra 告知が最上位のままで、5日間動きがない
- **GPT-6 Astra の Plus 層への展開は「順次」とされる状態が続いている。** 一次側（community 告知）の記述は 9/3 から更新されておらず、Plus での利用可否は日付で確定できない
- 到達性: `developers.openai.com`（changelog・deprecations・blog とも）と `community.openai.com` RSS は 200。`openai.com` は HTTP 403、`learn.chatgpt.com` はゲートウェイ拒否

### Google / DeepMind

- **Gemini Notebook が日次回数の上限を廃止した** — Google が9月2日から利用上限を固定の日次回数から消費量ベースへ切り替え、全課金ティアへ展開している。枠は入力と出力の重さで決まり **5時間ごとに回復**する。上限に当たると代替の出力形式を提案し、Video Overview と Slide Deck は後回し生成を予約できる
  - ⚠️ 一次の `blog.google` と `support.google.com` はゲートウェイ拒否。⚠️ **本サマリーとしては6日遅れの捕捉**である
  - https://blog.google/innovation-and-ai/products/gemini-notebook/new-flexible-usage-limits/
- Gemini API changelog は 9/3 の Lyria 3.5 public preview が最上位のままで、9/4〜9/7 の追加はない（4日間）
  - ⚠️ Lyria 3.5 は音楽生成なので `interests/ai-tools.md` の除外基準に該当し、内容は追わない
- 旧 `gemini-omni-flash-preview` エンドポイントの廃止日 **9/30**（本日から22日後）に変更はない
- 01 が `gemini.google/release-notes/` を代替一次として試したがゲートウェイ拒否だった。登録済みの `support.google.com/gemini/answer/13594961` も拒否継続で、**到達できる Google 一次は `ai.google.dev` のみ**という状態は変わらない
- HF の `google` org は `timesfm-3.0-pytorch`（作成 8/24）が最新のままである
- 既報: 9/2 GA の `gemini-3.8-flash` は入力 $0.75 / 出力 $3.75 が 2026-12-31 まで、2027-01-01 から $1.50 / $7.50。**Gemini 3.5 Pro GA は未ローンチ継続**

### Microsoft / GitHub Copilot

- ⚠️ **Microsoft の一次情報に本日の新規発表はない（2日連続）。** Roadmap の新規起票はゼロ、Release Notes・Copilot Studio What's New・各公式ブログとも据え置きである
- ⚠️ **Roadmap の検知は構造的に2日遅れている** — RSS の公開は UTC 22:50〜23:13 に集中するが、02 のセッションは UTC 21:10（JST 06:10）に走る。直近21件の Feature ID を突合すると、検知遅延は例外なく2日だった。巡回手順を厳密にしても解消しない（02 の B-061）。このため「次の要監視 9/8」と書いた Release Notes 次バッチと Released Versions 定例は、本日のセッションでは判定できない
- `github.blog/changelog` の Copilot ラベルは 9/4 の2本が最上位のままで、9/5〜9/7 の新規はない（3日間）
- Copilot CLI は 9/5〜9/7 のリリースなし。pre-release の最新は `v1.0.84-1`（9/4 23:20 UTC・GPT-6 Astra 対応）、安定版は `v1.0.83`（9/4 15:38 UTC）
- **M365 Copilot Release Notes**: August 25, 2026 バッチが最新。`updated_at` は 2026-09-03T19:39Z から動いていない
- **Tech Community（M365 Copilot Blog）**: 全20エントリを突合して新規はない。最新は 9/4 の GPT-6 Astra 提供開始記事で既報である
- **Cowork**: What's New は August 2026 節が最新で `updated_at` 2026-08-28T05:15Z から動かず、9月節は作成されていない
- **拡張機能 What's New**: `updated_at` が 2026-07-29T20:23Z のままで、更新停止は **41日**（次回確認は 9/11）
- **Purview**: `whats-new` の `updated_at` は 2026-08-28T07:31Z。⚠️ 569612（Copilot メモリの Purview 保持・GA 2026年9月）は本日も Purview 側に未掲載である
- **Agent 365 Blog**: 最新は 8/6 の7月号で、**33日間**新規がない
- `learn.microsoft.com` 配下10 URL は `curl` で全て HTTP 200。9/7 の復旧が2日連続で維持されている

### Copilot Studio / Power Platform

- ⚠️ **PVA ヘルプチャットボット削除は明日発効で、本日が利用者周知の最終日である** — Power Automate メーカーポータル左下の PVA ヘルプチャットボットが **9/9** に全ページから消える。一次は `power-platform/important-changes-coming` の先頭節で「Effective September 9, 2026」と明記している
  - 9/9 以降: 左下のチャットボットが消える、メーカーはそこから Power Automate について質問できなくなる、右上の Help (?) メニューは残る
  - クラウドフロー・デスクトップフロー・コネクタなど Power Automate の機能そのものには影響しない。管理者側の作業は不要で、必要なのは利用者への周知と内部ドキュメントの更新だけである
  - ページは `updated_at` 2026-09-04T19:03Z から動かず、新規の非推奨項目はゼロだった
  - ⚠️ 09-05・09-06 にハイライトし 09-07 に外した項目で、続報は無い。不可逆な期限のためカテゴリと注目予定に残す
  - https://learn.microsoft.com/en-us/power-platform/important-changes-coming
- **Copilot Studio What's New**: 最新は July 2026 節のまま。June 節の GitHub Copilot ハーネスは `(Production-ready preview)` の表記が残り、GA（8/3）から **36日連続**の未反映である
- **モデル一覧**: `authoring-select-agent-model` は本文に `Fable` も `Astra` も現れない。提供開始を当日に掴める経路は Tech Community の `Available today:` 記事だけという状態が続く
- **Released Versions**: 全リージョンで **2026.6.3** のまま、ページの `updated_at` も 2026-07-01T15:55Z から **69日間**動いていない。本日は「毎週火曜更新」の定例日だが、UTC ではまだ 9/7 のため判定は明日へ回す
- **Copilot Tuning**: 停止発効（8/20）から **19日**たっても一次は停止も退役も無記載である
- **Release Wave**: 製品別の `planned-features` 4本が HTTP 404 のまま6日目。登録 URL の Copilot Studio 向けは本日も 301 で `aka.ms` へ転送される
- **Roadmap 広報枠**: Latest announcements の先頭は **7/24** の Claude Opus 5 のままで、**46日**追加がない
- **Partner Center**: 9月ページは掲載4件・`updated_at` 2026-09-04T22:04Z のまま。⚠️ **Partnering for Success Together** の初回は明日 **9/9** である
- `Microsoft Copilot Studio:` で始まる Roadmap 項目は19件で全件 `In development`。**566997** は GA 期日「August CY2026」を超過し、**562221** は 2026年6月から超過4か月目に入った

### Cursor / 開発ツール

- ⚠️ **Cursor は GPT-6 Astra の提供開始を告知しないまま5日目**（9/3 GA）。Copilot は 9/4 に GA、Codex CLI は `0.153.1`〜`0.153.4` で対応済みである。changelog とフォーラム Announcements の両方を確認したうえでの不在なので追跡を続ける
- Cursor changelog は 9/2 の Self-hosted machines が最上位のままである。フォーラム Announcements も 9/2 の Grok Bot Android 版が最上位である
- **Grok 4.7 は二次情報のまま動きがない。** 公開見込み 9/12、パラメータ 2.1兆とされる。⚠️ xAI はローンチページ・API モデル ID・価格・モデルカードのいずれも未公開で、一次3ホストはゲートウェイ拒否が継続している。公式提供中の最新は **Grok 4.6**（8/12・context 50万トークン・$2/$6）
- Devin は一次・代替一次のいずれからも読めない（`docs.devin.ai` / `cli.devin.ai` ともゲートウェイ拒否）

### MCP / エージェント標準

- `blog.modelcontextprotocol.io` は 200。8/22 の「The New MCP Roadmap」が最上位のままで新規は **17日間**ない
- WebMCP Challenge は提出締切 9/4 を経過。受賞発表 9/23・賞金総額 $35,000。⚠️ WebMCP は MCP 公式ブログ側に言及がなく OpenAI 発の別系統として扱う
- A2A の AAIF 参加は未確定のまま。一次3ホストはゲートウェイ拒否が継続している

### オープンウェイト / ローカル LLM

- 追跡8 org のいずれにも 9/7 の新規公開はない
  - 各 org の最新作成: `Qwen-Drive-1.0-4B` 8/27 ／ `DeepSeek-V4-Flash-Vision-Exp` 8/31 ／ `GLM-5.3-Flash-BF16` 8/25 ／ `timesfm-3.0-pytorch` 8/24 ／ `Muse-Glimmer-30B-ExecuTorch-PTE` 8/10 ／ `Shieldstral-1.0-3B` 7/16 ／ `Kimi-K3` 6/13 ／ `privacy-filter` 4/17
- HF `downloads` の実測（2026-09-07 19:08 UTC・追跡8リポジトリは全て `private: false` / `gated: false`）
  - `Qwen/Qwen3.8-27B-FP8` 6,785,214 ／ `Qwen/Qwen3.8-Flash-Next` 474,693 ／ `DeepSeek-V4-Flash-0731` 4,469,466 ／ `DeepSeek-V4-Pro-0813` 159,392 ／ `DeepSeek-V4-Flash-Vision-Exp` 251,611 ／ `GLM-5.3-Flash` 784,005 ／ `GLM-5.3` 442,064 ／ `moonshotai/Kimi-K3` 2,408,747
  - ⚠️ `DeepSeek-V4-Flash-0731` と `moonshotai/Kimi-K3` は前回記録から減った。30日ローリングのため減少は異常ではない

### 資本・M&A・市場データ

- **Fluidstack が $1.5B を調達し評価額 $18B に乗せた** — Jane Street Capital 主導。累計調達は $2.6B 超。⚠️ 7月の $750M 調達時は評価額 $7.5B で、2カ月弱で2.4倍に切り上がった。Anthropic の米国計算基盤 $50B 投資で NY・テキサスの建設先に選ばれている。⚠️ 一次未到達。**3〜5日遅れの捕捉**である
- **HiddenLayer が $100M を調達した** — Series B（累計 $155M 超）。資金使途に **Agent Harness Security**（実行中のコーディングエージェントそのものを保護する）が挙げられる。⚠️ 一次未到達
- **NEC が「BluStellar Intelligent Managed Service」を発表した** — フロンティアAI 由来の脆弱性を扱うマネージドサービスで、**9月末から提供開始**、3年間で 300億円の売上収益を目標とする。⚠️ 一次の `jpn.nec.com` はゲートウェイ拒否。**6日遅れの捕捉**である
- Similarweb の8月分は二次ごとに数値が割れている。「ChatGPT 55.5%・Gemini 25.6%」と「ChatGPT 68%・Gemini 18.2%」が並存し、水準を提案資料に引ける状態ではない。`www.similarweb.com` はゲートウェイ拒否が継続している
- 定点の IDC Japan・Gartner・MM総研・NRC に本日の新規公表はない。⚠️ IDC の国内 AI インフラ記事が日付なしで浮上したが 2026年5月公表で新規ではない

### Apple / クラウド

- `developer.apple.com` は 200。9/1 の Rosetta 告知が最上位のままで、9/2 以降の新規はない
- ⚠️ Apple の AI 関連の最新は 6/11 の ImageCreator クラス廃止告知のままである
- 既報: 8/26 の特別イベント告知（**9/9 10:00 PT**）、8/24 Sign in with Apple 新ドメイン（`private.icloud.com`）、8/18 EU 向けビジネス条件変更（発効 2026-10-01）
- `azure.microsoft.com` はゲートウェイ拒否のままである

## 直近の注目予定

- **9/9**: Apple 特別イベント（10:00 PT）／ Power Automate の PVA ヘルプチャットボット削除が発効 ／ Partnering for Success Together 初回 ／ GLM-5.3-Flash の Z.ai 経由50%割引が終了
- **9/9〜9/10**: M365 Copilot Release Notes の次バッチと Copilot Studio Released Versions 定例の判定（UTC 公開のため 02 の本日セッションでは未確定）
- **9/10**: MAI-Code-1-Flash が全 Copilot 体験から廃止
- **9/11**: 拡張機能 What's New とモデル可用性一覧の週次確認
- **9/12**: Grok 4.7 の公開予定（Musk の X 投稿のみが出所・公式の裏づけなし）
- **9/13**: **Claude Code の週次上限50%増が終了** ／ Power CAT・PnP の週次確認
- **9/14**: **Claude Code の標準週次上限が恒久的に +25%**（Pro / Max / Team / シート課金 Enterprise。現行比では17%減）／ ppweekly・MS-4005・課金レート表の週次確認
- **9/17**: OpenAI DevDay Exchange の応募締切 ／ Anthropic Startup Grant Program の配分年度締切（**二次のみ・一次に記載なし**）
- **9/21**: Anthropic ウェルビーイング研究助成の応募締切
- **9/23**: WebMCP Challenge の受賞発表
- **9/24**: OpenAI の Videos API と Sora 2 系が退役（代替モデルの提示なし）
- **9/28**: Copilot のチャット3面統合 ／ code review の既定 effort が Lite → Balanced ／ チャットのデータ保持がアカウント存続期間へ ／ OpenAI の `gpt-3.5-turbo-instruct` / `babbage-002` / `davinci-002` / `gpt-3.5-turbo-1106` が停止（代替 `gpt-5.6-terra`）
- **9/29 以降**: `claude-sonnet-4-5-20250929` の暫定退役日（確定日ではない）
- **9/30**: Gemini の旧 `gemini-omni-flash-preview` エンドポイント廃止 ／ M365 E7 プロモーション最終日 ／ E5・E3 の CSP 割引終了 ／ 2026 Wave 1 の対象期間終了 ／ NEC BluStellar の提供開始
- **9 月**: iOS 27 / macOS 27 GA ／ Claudeforce のオープンベータ（二次情報）／ Release Plans on Learn の新規掲載停止 ／ Copilot Tuning の Public Preview 再開 ／ Copilot デスクトップアプリの広範展開（中旬）／ Eligibility Dashboard の展開完了（中旬）／ Copilot Studio の Roadmap 項目が GA 期日 ／ App Store の Social Media 年齢レーティング回答が必須化
- **10/1**: Copilot Business・Enterprise の既存顧客が前払い必須に ／ Apple の EU 向け新ビジネス条件が発効 ／ CSP software の価格改定 ／ Ask Gemini in Chat のプロモーション上限が終了
- **10/2**: **GitHub Copilot が Gemini 3.5 Flash / Gemini 3.6 Flash / Kimi K2.7 Code / Claude Opus 4.7 を全体験から廃止**
- **10/5**: Anthropic ウェルビーイング研究助成の full proposal 提出期限（採択者）
- **10/15 以降**: `claude-haiku-4-5-20251001` の暫定退役日（確定日ではない）
- **10/16–11/11**: OpenAI DevDay Exchange 8都市（東京は 10/20）
- **10/23**: OpenAI のレガシースナップショット退役
- **10/31**: OpenAI の既存 evals が読み取り専用になる
- **10 月**: Anthropic の IPO 予定（$2T 超の評価額を目標と報道）
- **秋**: Anthropic の Enterprise Frontier Safeguards が段階的に提供開始（二次情報）
- **11/15**: Microsoft の Release Planner が退役し、Learn 上の Release Plans がアーカイブされる
- **11/21**: GPT-5.6 Sol の暫定値下げが有効とされる期限
- **11/24 以降**: `claude-opus-4-5-20251101` の暫定退役日（確定日ではない）
- **11/30**: OpenAI の Reusable prompts・Evals プラットフォーム・Agent Builder が停止
- **12/1**: OpenAI の GPT Image 系が停止（`gpt-image-1-mini` / `gpt-image-1.5` / `chatgpt-image-latest` → `gpt-image-2`）
- **12/2**: EU AI Act の生成コンテンツ標識義務、8/2 以前に市場投入済みシステムへの猶予終了
- **12/11**: OpenAI の旧スナップショット退役
- **12/31**: Gemini 3.8 Flash と 3.7 Flash の導入価格が終了 ／ GitHub Copilot の Fable 5.1 / Fable 5 に対する ZDR 暫定免除が終了
- **年内**: Anthropic の新データ保持方式投入予定 ／ OpenAI の Jalapeño チップの初期展開
- **2027-01-06**: OpenAI で大半のユーザーの新規ファインチューニングジョブ作成が終了
- **2027-01-20**: OpenAI の audio / realtime 系退役
- **2027-02-05 以降 / 02-17 以降**: `claude-opus-4-6` / `claude-sonnet-4-6` の暫定退役日（確定日ではない）
- **2027-02-26**: OpenAI の文字起こし4モデル退役
- **2027-03-01 / 2028-10-01**: SharePoint クラシックページ退役のフェーズ1・フェーズ2
- **2027-04-16 / 05-28 / 06-09 / 06-30 / 07-24 / 09-01 以降**: `claude-opus-4-7` / `claude-opus-4-8` / `claude-fable-5` / `claude-sonnet-5` / `claude-opus-5` / `claude-fable-5-1` の暫定退役日（確定日ではない。⚠️ `claude-opus-4-7` は Copilot では 10/2 に消える）
- **2027-06-30**: Claude for Teachers の学区登録期限
- **2027年末**: Anthropic が借りる Nscale West Virginia データセンター（460MW）の稼働開始見込み
- **2027年上半期**: Nvidia による Hugging Face 買収のクローズ見込み
- **2028-03**: OpenAI が「automated AI researcher」の実現目標とする時期（ハイライト参照）
- **2028-06**: 米国 K-12 教職員向け ChatGPT for Teachers の無料提供期限

## 改善メモ

- 3ソースの当日分（01 Master / 02 Copilot / 03 industry）はいずれも取得できた。前日 09-07 分にも欠損記録はなく、欠損リカバリの対象はない
- ⚠️ **07:00 JST の自動実行がまた生成に至らなかった。** 09-06 は 21:56 JST の後追い、09-07 は手動依頼、本日 09-08 は 07:00 時点の成果物が GitHub / Pages / Vercel のいずれにも無く、本サマリーは後刻の手動復旧である。入口の「今日のまとめ」は既定タブのため、自動実行が空振りするとサイト全体が「掲載されない」ように見える
- 入力3リポは公開リポの `raw.githubusercontent.com` から読み取り専用で取得した（書き込みは行っていない）。09-07 時点で GitHub MCP スコープが `kit1132/05_ai-news-daily` のみという状態が5日連続と記録されており、**自動実行側でこの回避が働かないと以後も当日分が空振りする**
- ⚠️ **PVA ヘルプチャットボット削除はハイライトに戻さなかった** — 続報が無く、09-07 に外した判断を維持する。ただし発効は **9/9（明日）** で本日が周知の最終日のため、カテゴリ別まとめと注目予定の両方に残した
- 新規提案は 01 の B-063（Codex CLI の版検出を `tags` 併用にする）、02 の B-061（Roadmap 検知遅延は実行時刻に起因する）、03 の B-034（Anthropic の料金定点を `platform.claude.com` へ差し替える）。番号の衝突は本日は起きていない
- 継続提案の計数: 01 が「再確認16件・提案中計44件」（最多 B-013・40回目）、02 が29件（最多 B-011・50回目）、03 が16件（最多 B-004・71回目）
- 到達性の変化: 01 が新規ホスト5件をゲートウェイ拒否として記録（`gemini.google` / `www.unite.ai` / `www.datastudios.org` / `kingy.ai` / `aiweekly.co`）。03 は `www.idc.com` と `support.google.com` を新規拒否として起票し、うち **`www.idc.com` は定点ソース**である。02 の `learn.microsoft.com` 復旧は2日連続で維持。復旧は0件
- ⚠️ **長期化している一次未読・接続障害**: Anthropic の8月 Risk Report が23日連続で一次未読（01）、`mc.merill.net` の拒否が32日連続（02）、Copilot Studio What's New への GA 未反映が36日連続（02）、Released Versions の空白が69日（02）、拡張機能 What's New の停止が41日（02）、Roadmap 広報枠の空白が46日（02）、MCP ブログの空白が17日（01）、`learn.chatgpt.com` / xAI 一次3ホスト / Google 系 / Devin 一次。いずれも解消の見込みが立っていない
