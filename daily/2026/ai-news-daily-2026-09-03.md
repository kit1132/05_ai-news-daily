# AI News Daily Summary — 2026-09-03

9月2日は、モデルの選択肢が広がった一方で「何が GA したかを確かめる経路」が1本失われた日である。Anthropic の Fable 5.1 は GitHub Copilot・Copilot Cowork・Copilot Studio の3面へ同日到達したが、いずれも既定オフでデータ保持の承諾が前提になる。Google は Gemini 3.8 Flash を単価据え置きで GA し、Flash 系の最上位が20日で入れ替わった。Microsoft 側では Power Platform の Release Wave 製品別ページ4本が 404 で消え、11/15 の Release Planner 退役を待たずに緑チェックによる GA 判定ができなくなった。統制面では GitHub が企業側で既定モデルを固定できるようにし、Copilot Studio にはツール実行前の人間承認を必須化する Roadmap 項目が起票された。安全性側では OpenAI が Astra のサイバー能力について Preparedness Framework の Critical 超えを公表している。

## 今日のハイライト

### 1. Fable 5.1 が Copilot 3面で開放された — 既定オフかつデータ保持が前提になる

**要点**: GitHub Copilot と Microsoft Copilot の3面で Fable 5.1 が開放された。Business / Enterprise は既定オフかつデータ保持が要件で、ZDR 前提の組織は年内の暫定免除しかない。

**詳細**: GitHub 側は 9/1 公開で GA。対象は Copilot Pro+ / Max / Business / Enterprise（Free と Pro は対象外）で、VS Code / Visual Studio / Copilot CLI / coding agent / Copilot アプリ / github.com / GitHub Mobile（iOS・Android）/ JetBrains / Xcode / Eclipse に同時提供された。課金は premium request の倍率ではなく provider list pricing の従量である。Microsoft 側は 9/2 15:16Z の Tech Community 記事で「Available today」として告知され、提供面は Copilot Cowork と Copilot Studio の2つに限られる。7/24 の Claude Opus 5・7/9 の GPT-5.6 が「in Microsoft 365 Copilot」だったのに対し、本記事は改称後の「Microsoft Copilot」表記で書かれている。

データ保持の扱いが他の Claude モデルと異なる。

- GitHub は「Fable 5.1 ポリシーを有効化することがデータ保持要件の承諾にあたる」と明記しており、既定では Anthropic の安全性分類器のためにデータ保持が必要になる
- zero data retention を続けられるのは適格な enterprise 顧客のみで、**暦年末までの暫定免除**にとどまる。以後の継続には **Enterprise Frontier Safeguards** の導入が要る
- 09-02 に記録した「Fable 5.1 は zero retention 契約下では提供されない」という Claude Platform 側の記載と整合しており、Copilot 経由でも同じ制約が掛かることが確定した

⚠️ **Copilot Studio の `authoring-select-agent-model` に Fable 5.1 の行は無い。** 同ページの `updated_at` は 2026-08-03T14:59Z で1か月動いておらず、公開表は GPT-4.1 が既定・Claude Sonnet 5 が GitHub Copilot ハーネス限定・GPT-4o と Claude Sonnet 4.5 が `Retired` のままである。「可用性表に載っていない＝使えない」という読み方は成立しなくなった。展開は対象ユーザーへ順次で、提供可否は地域と組織で異なる。Copilot CLI 側も 9/2 の pre-release `v1.0.83-2` で `claude-fable-5.1` に対応した。

- https://github.blog/changelog/2026-09-01-claude-fable-5-1-generally-available-in-github-copilot
- https://techcommunity.microsoft.com/t5/microsoft-365-copilot-blog/available-today-anthropic-claude-fable-5-1-in-microsoft-copilot/ba-p/4551974
- https://learn.microsoft.com/en-us/microsoft-copilot-studio/authoring-select-agent-model

### 2. Gemini 3.8 Flash が GA した — 単価据え置きでコーディング性能だけが上がった

**要点**: Google が Gemini 3.8 Flash を GA した。単価据え置きで Terminal-Bench 2.1 が 81.6%→90.8% に上がった。「Flash は安いが力不足」を前提にしたモデル振り分けは引き直しが要る。

**詳細**: 9/2 公開。モデル ID は `gemini-3.8-flash` で、コンテキスト100万トークン・最大出力6.4万トークン。thinking level を low / medium / high で調整でき、既定は medium である。提供面は Gemini API・Google AI Studio・Antigravity・Android Studio・Gemini Enterprise。一次 changelog は「long-horizon なソフトウェアエンジニアリング、自律エージェント、複雑な企業ワークフロー向けの最も知的な Flash」と位置づけ、8/13 GA の 3.7 Flash 側の説明は「日常のコーディング、エージェント的なツール利用、信頼できる複数ステップ実行」へ書き換わった。Flash 系の最上位が20日で入れ替わったことになる。

単価は 3.7 Flash と同額で、期限もそのまま引き継がれる。

- 標準: 入力 **$0.75** / 出力 **$3.75**（100万トークンあたり・2026-12-31 まで）。2027-01-01 から $1.50 / $7.50 へ倍増する
- Batch / Flex: $0.375 / $1.875、Priority: $1.35 / $6.75
- ⚠️ 単価と期限は changelog に載らず料金ページ側にしかない。12/31 の倍増期限は**新モデルにもそのまま掛かる**

⚠️ ベンチマーク値は二次のみである。Terminal-Bench 2.1 の 90.8%（3.7 Flash は 81.6%）と DeepSWE v1.1 の長期コーディング優位は二次報道の突き合わせで、一次の `blog.google` / `deepmind.google` はゲートウェイ拒否で本文に到達できていない。料金ページ・changelog・モデル解説ページの3点は WebFetch で一次確定している（最終更新はいずれも 9/2 UTC）。前日 9/1 には agentic video understanding が 3.7 Flash / 3.6 Flash / 3.5 Flash-Lite 向けに入っており、changelog の日付列は 9/2 → 9/1 → 8/27 → 8/26 → 8/13 と連続していて欠落は起きていない。

- https://ai.google.dev/gemini-api/docs/changelog
- https://ai.google.dev/gemini-api/docs/pricing
- https://ai.google.dev/gemini-api/docs/latest-model

### 3. Release Wave の製品別ページ4本が 404 で消えた — GA 判定の主経路が 11/15 を待たず失われた

**要点**: Release Wave の製品別ページ4本が 404 で消えた。Power Automate と Power Apps の GA 判定を緑チェックの差分で行ってきた前提が崩れ、Roadmap の `status` へ移すしかなくなった。

**詳細**: `power-platform/release-plan/2026wave1/` 配下で、`microsoft-power-automate` / `microsoft-power-apps` / `microsoft-power-pages` / `microsoft-dataverse` の各 `planned-features` が一斉に HTTP 404 を返している。前日 9/2 の時点では登録3ページとも 200 で、`updated_at` 2026-08-27T17:04Z・`git_commit_id` `b92ae441` だった。301 も 308 も返らず転送先が示されない。`microsoft-power-automate/` のようにサブツリーの親ごと 404 になっており、消えたのは planned-features 単体ではない。親の `2026wave1/` 自体は 200 のままである。8/25 の移行告知は「9月に新規掲載停止・11/15 に Release Planner 退役」までしか示していなかったため、消滅は告知より先行して起きたことになる。

- **残存は1ページのみ**: `power-platform-governance-administration/planned-features` だけが 200 を返し、掲載12行に増減はない（`git_commit_id` は `b92ae441` のままで 8/28 から7日連続の再ビルドなし）
- ⚠️ **その残存ページの冒頭 Important は本日も「Existing release plans will remain available for historical reference until further notice」と書いており**、同じサブツリーの4ページが消えている事実と矛盾する
- ガバナンス面の未達3件は追跡できる: PPAC の Usage ページ（Public preview 2026-02-13・GA 期日 Aug 2026・緑チェック未付与のまま9月へ超過）、Agentic Center of Enablement（Public preview Sep 2026）、運用状態の異常検知（同 Sep 2026）
- Copilot Studio 版は従来どおり `aka.ms/MCStoM365Roadmap` へ 301 で、`aka.ms` はゲートウェイ拒否のため到達できない

8月期日で緑チェックの付かなかった行がどう決着したかを追う手段が無くなったため、当面は Roadmap 項目の `status` が唯一の判定経路になる。

- https://learn.microsoft.com/en-us/power-platform/release-plan/2026wave1/power-platform-governance-administration/planned-features
- https://aka.ms/ReleasePlannerMigrationBlog

## カテゴリ別まとめ

### Anthropic / Claude

- **Claude Code 2.1.258**: Anthropic が 2.1.255 の回帰で起きていた macOS 12（Monterey）の起動失敗を修正した（9/1 22:25 UTC publish）。権限承認の再送に起因して remote / scheduled セッションが `user messages must have non-empty content` で落ちる不具合も直っている。スケジュール実行を使っている環境は 2.1.258 まで上げないと失敗が残る
  - https://code.claude.com/docs/en/changelog
- **npm `dist-tags`**: `stable` が **2.1.236** のまま据え置かれ、`latest`（2.1.258）との差が22版に開いた（9/2 実測）。8/28 の 2.1.251 に入った symlink 経由の権限境界修正は、stable 固定の組織へ6日経っても届いていない
- **commerce agents blueprint**: Anthropic が小売・マーケットプレイス・EC 事業者向けに、Claude 上でショッピングエージェントを組む実装一式を公開した（9/2）。コードは `github.com/anthropics/commerce-agents` にあり、Claude API / Amazon Bedrock / Microsoft Foundry / Google Cloud Vertex AI へデプロイできる
  - Shopping Agent: 商品検索・複数商品の要求処理・パーソナライズ・カスタマーサービス連携・カート操作を担う
  - Merchant Agent: 売上分析・在庫追跡・価格推奨・マーケティング施策のドラフトを担う
  - 実装は Messages API / Agent SDK / Claude Managed Agents（ベータ）から選べ、セットアップ用の Claude Code プラグインとデモが付く
  - 連名で挙がる企業は Shopify / Priceline / Visa / Mastercard / Accenture / Intuit / Klaviyo / Wix / Zomato / Fetch / Square / Warp である
  - ⚠️ 「カートが最大35%大きく、購入完了率が60%高い」という数値は**測定条件と対象社数の記載がない**ため、引用時は出典元の表現ごと引く必要がある
  - https://claude.com/blog/claude-for-commerce-agents
- **モデル退役ページ**: 新規の退役告知はなく、直近告知は 2026-06-05 の Opus 4.1（8/5 退役済み）のままである。Active は11件で、暫定退役日は `claude-sonnet-4-5-20250929` 9/29 以降を先頭に `claude-fable-5-1` 2027-09-01 以降まで並ぶ。⚠️ いずれも「not sooner than」であって確定日ではない
- ⚠️ **`claude-mythos-preview` が deprecated 扱いになっている**（移行先は `claude-mythos-5`）。同ページの注記にしか現れず、表側の Active 一覧には出ないため見落としやすい
- **Release Notes 2本は 9/1 のまま**: `platform.claude.com` と `support.claude.com` はいずれも Fable 5.1 / Mythos 5.1 が最上位で、9/2 の追加がない。mid-conversation ベータ3件（`output_config.effort` / `clear_at: "next_user_message"` / `thinking.display: "updates"`）にも追加や GA 移行の告知はない
- 既報: 週次上限50%増の **9/13** 終了と 9/14 からの恒久 +25%（現行比では17%減）、Claudeforce（オープンベータは9月中）、Claude for Teachers（登録期限 2027-06-30）、ウェルビーイング研究助成 $5M（締切 9/21）

### GitHub Copilot / 開発ツール

- **Copilot code review の PR 承認**（ハイライト参照）— 9/1 公開のパブリックプレビューで、既報である。承認は必須承認数にカウントされ、既定はオフ。enterprise / organization / repository の3階層で制御し、repository 層では Copilot が承認できるファイルパスを限定できる。新規コミットの push で承認は自動的に取り消される
- **企業側で既定モデルを固定できるようになった**（9/2・GA）。GitHub は enterprise-managed settings で任意のモデルを新規会話の既定に設定できるようにした。管理者は `managed.json` の `model` キーに設定して `overridable` と印を付け、`team-mappings.json` にチーム別の設定を書けばチーム単位の既定も配れる。設定のないユーザーは企業既定を継承する。対象は Copilot Business / Enterprise で、GitHub Copilot アプリ・Copilot CLI・VS Code に効く。ハイライト1の Fable 5.1 ポリシーと組み合わせると、**モデルの可否と既定を企業側で一括統制できる**構成が揃った
  - https://github.blog/changelog/2026-09-02-enterprise-managed-settings-support-any-default-model
- **個別ユーザー予算に任意の有効期限を設定できるようになった**（9/1・Copilot Business / Enterprise）。期限が来ると予算は自動で削除され、ユーザーは次に適用される予算レベルへ戻る
  - 選べるのは「期限なし（既定・従来どおり）」「次の請求サイクル開始時に失効」「指定日（UTC）に失効」の3つである
  - 期限はいつでも変更・解除でき、Budgets REST API の `expires_at` でも設定できる
  - 従来は一時的な予算上乗せを手作業で消す必要があり、GitHub は「企業規模では反復的な後始末が発生していた」と説明している
- **Copilot CLI に pre-release が2版入った**。`v1.0.83-2`（9/2 06:35 UTC）は `claude-fable-5.1` に対応し、カスタムエージェントがフォールバック順つきで複数モデルを列挙できるようにした。Linux サンドボックスは slirp4netns 利用時に egress を設定済みプロキシへ限定する。⚠️ `v1.0.83-3`（9/2 15:14 UTC）は**本文が展開されず変更内容を確定できない**。安定版は `v1.0.82`（8/29 23:39 UTC）のままで 8/30〜9/2 の安定版リリースはない
- **Codex CLI の安定版 `0.152.1` が出た**（9/1 22:33 UTC）。内容は Guardian の承認レビューがモデルメタデータ由来の Node REPL ポリシーを尊重するようにした1件のバグ修正である。⚠️ pre-release 3版（`0.153.0-alpha.4` / `alpha.5` / `alpha.6`）はいずれも本文が `Release <タグ名>` の1行だけで変更内容が未確定である
- **Cursor は 8/27 の「Start from scratch, without a repo」が最上位のまま**で、8/28〜9/2 の changelog 追加がない（RSS 200 / item 50件）。フォーラム Announcements も 9/1 の Fable 5.1 提供開始告知が最上位のままである
- ⚠️ **Devin は `docs.devin.ai` のゲートウェイ拒否が継続**しており一次に到達できない。二次が挙げる CLI の org / agent / session 管理改善、`/recap`・`/rename`・Alt+P、Gmail / Google Calendar / Gamma / Supabase の MCP 追加は、前回チェックと内容が変わらず公開日も特定できないため新着扱いしない
- 期限: **9/10** MAI-Code-1-Flash 廃止、**9/28** チャット3面統合／code review 既定の Balanced 化／チャットのデータ保持がアカウント存続期間へ、**10/1** 既存顧客の前払い必須化

### Microsoft 365 Copilot / Copilot Studio / Power Platform

- **Release Wave 製品別ページの 404 消滅**（ハイライト参照）
- **Fable 5.1 が Cowork と Copilot Studio へ**（ハイライト参照）
- **ツール呼び出しに人間の承認を必須化できるようになる**（Roadmap **570434**・`In development`・GA 2026年9月）。Copilot Studio のメーカーが、特定のツールについて実行前の人間承認を必須にできるようになる。トグルはエージェント単位かつツール単位で、対象ツールの呼び出しは停止し、エージェントが何をしようとしているかを説明する承認要求が表示される。承認者は「承認」「このセッションでは承認」「拒否」を選べる
  - ⚠️ 記事は「エージェントの指示とは独立した確定的なガードレール（deterministic guardrail）」と明記する。想定はメール送信・チケットのクローズ・決済処理といった高リスク操作である
  - 承認要求はエージェントを配置したチャネル内にインラインで出る（Microsoft Teams と Microsoft 365 Copilot を含む）
  - 同じ 9/1 のバッチで **570435**（Copilot Studio エージェントの応答を M365 Copilot 側の体験に寄せる。書式・思考連鎖の圧縮表示・ストリーミング・再開／再試行・音声入力・クリック可能な引用・ツール実行トレース。GA 2026年9月）も新規起票された
  - https://www.microsoft.com/releasecommunications/api/v2/m365/rss
- **ハーネス選択の白書が公開された**（Tech Community・9/2 15:30Z）。Copilot Studio 製品チームが、標準ハーネスと GitHub Copilot ハーネスのどちらを選ぶかを論じる白書を出した。記事はハーネスを「モデルとエージェント構成の間にある動作レイヤー」と定義し、モデルが推論能力を担い**ハーネスがそれを装備して方向づける**と説明する。使い分けは、標準ハーネスが境界の定まった業務プロセスを一貫して確実に実行する用途、GitHub Copilot ハーネスが長時間・調整の多い・推論負荷の高い作業をより大きな規模で扱う用途である。⚠️ 本文の詳細は添付 PDF 側にあり、記事本体には差分・トレードオフの一覧が含まれない
  - https://techcommunity.microsoft.com/t5/copilot-studio-blog/white-paper-choosing-between-the-github-copilot-and-standard/ba-p/4552385
- **M365 Roadmap に 9/1 22:59Z 付の新規12件が入った**（RSS 総項目数 1,766 → 1,778）。総数差分は新規件数と一致しないため、判定は `pubDate` の全件パースで行われている
  - 569424 Excel canvas: Copilot がブックのデータから主要な可視化・指標・示唆をまとめた対話的なビューを生成する。データが変わると自動更新され、対話でキャンバスを変更できる（GA 2026年9月）
  - 569477 Purview DLP: 管理者が Exchange Online の分類・テキスト抽出の失敗種別ごと（タイムアウト／スロットリング／その他のスキャンエラー）に DLP ポリシーを作れるようになる（Public preview 提供中・GA 2026年9月）
  - 政府クラウド向けが3件入った: 570431 Organizational Data Service の GCC High 対応、570428 Viva Insights と Copilot Analytics の GCC High 展開（いずれも GA 2026年9月）、569214 Teams の Copilot Chat の GCC / GCC High / DoD 展開（GA 2026年10月）
  - その他は 569720 / 570444 / 568784 / 567885 で、Copilot 固有の変更は含まない
- **Copilot Studio の Roadmap は15件 → 17件になり、全件が `In development` のままである**。9月が GA 期日の項目は **11件**（562222 / 566859 / 566873 / 566998 / 568762 / 568929 / 568930 / 569607 / 569930 / 570434 / 570435）ある。⚠️ **566997**（メーカー資格情報の使用ブロック）は GA 期日「August CY2026」を満たせないまま9月に入り、**562221**（ワークフローでの MCP 準拠ツール）は GA 期日 2026年6月から超過4か月目である
- **M365 Copilot Release Notes は August 25, 2026 バッチが最新のまま**で、10節・全19項目に増減がない（`updated_at` 2026-08-25T20:41Z）。隔週傾向どおりなら次バッチは 9/8 前後になる
- **Copilot Studio What's New は July 2026 節が最新のまま**で、8月節・9月節とも作成されていない（`updated_at` 2026-08-20T19:04Z）。⚠️ June 節の GitHub Copilot ハーネスは `(Production-ready preview)` の表記のままで、GA（8/3）から**31日連続の未反映**である
- **Released Versions の Copilot Studio Build は 2026.6.3 のまま**で、空白が **65日**に達した。ページ本文は「This page is updated each week on Tuesday.」と書いたまま 9/1 の定例日にも新ビルドが出ていない。次の定例日は 9/8 である
- ⚠️ **Copilot Tuning は停止発効（8/20）から14日たっても一次に停止も退役も書かれていない**。`copilot-tuning-overview` の `updated_at` は 2026-08-18T17:48Z で動かず、Optimization エージェントを現行機能として掲載したままである。MC1454393 の本文は `mc.merill.net` が27日連続でゲートウェイ拒否のため一次で読めない
- **AI at Work Roadmap の Latest announcements は 7/24 の Claude Opus 5 記事が先頭のまま**で、8月に続き9月も新規追加がない。⚠️ ページ表題は既に「AI at Work Roadmap」で、Release Plans の移行先として告知された面はここである
- **SPFx Dev Skills の検証記事が公開された**（M365 Developer Blog・9/2 10:14Z）。SharePoint Framework チームと Developer Relations が、スキル公開前に「エージェントが何を知っていて何を外すか」を測った経緯を出した。SPFx 1.21.1 → 1.22.2 の更新（gulp から Heft への移行を含む）をスキルなしで5回試行したところ、**5回とも成果物はビルドも実行も通った**一方で、依存関係の最新性は50件中34件、構成の正確性は85件中38件しか満たさなかった。実行が通ることと更新が正しいことは別だという測り方そのものが主題である
  - https://devblogs.microsoft.com/microsoft365dev/behind-spfx-dev-skills-testing-what-agents-know-and-fixing-what-they-miss/
- **Power Platform の非推奨一覧に新規項目はない**（週次確認）。`## ` 見出しは90本のままで 8/31 から増減がなく、`updated_at` 2026-08-14T01:04Z も動いていない。先頭は 8/31 に発効済みの Power Automate モバイルアプリ廃止で、発効日を過ぎても本文の書き換えは入っていない
- **Power Apps / Power Automate / Power Platform の各ブログに新規記事はない**。先頭はそれぞれ 9/1 のキャンバス共同編集エージェント GA（9/2 に既報）、8/13 の PPCC 2026 告知、8/25 の「One always-on roadmap」である
- **モデル可用性の GCC 系は本日も GPT-4o の1行だけ**で、公開側の退役が米国政府クラウド（GCC / GCC High / DoD）の表に反映されていない
- **Purview / ガイダンスハブ / Cowork の3本は `updated_at` に変化がない**（それぞれ 2026-08-28T07:31Z / 2026-08-28T19:03Z / 2026-08-28T05:15Z）

### Google

- **Gemini 3.8 Flash の GA**（ハイライト参照）
- **agentic video understanding が Flash 系3モデルに入った**（9/1）。Google は Gemini 3.7 Flash / 3.6 Flash / 3.5 Flash-Lite で、Interactions と GenerateContent の両 API から動画タイムラインを動的に辿れるようにした。長尺コンテンツのトークンを最大88%削減するとされる
- **HF の `google` org は `timesfm-3.0-pytorch`（作成 8/24）が最新のまま**である。`lastModified` が 9/2 15:44 UTC に動いたのはカード更新であり、新規公開ではない
- 既報: 旧 `gemini-omni-flash-preview` は **9/30** 廃止、**Gemini 3.5 Pro の GA は未ローンチが継続**している

### OpenAI / Codex / ChatGPT

- **API のエラーコードが分離された**（9/2）。OpenAI が急激なトラフィック増加と一時的なモデル過負荷を呼び分け側で区別できるようにした。前者は `429` に `slow_down`、後者は `503` に `server_is_overloaded` が返るため、リトライ戦略をコード別に分けられる
- **退役ページに新規告知はない**が、⚠️ **本サマリーの注目予定が持っていなかった期限を2件確認した** — **9/28** に `gpt-3.5-turbo-instruct` / `babbage-002` / `davinci-002` / `gpt-3.5-turbo-1106` が停止（移行先 `gpt-5.6-terra`）、**10/31** に既存の evals が読み取り専用になる。次の期限は 9/24 の Videos API と Sora 2 系（移行先の提示なし）で残り21日である
  - https://developers.openai.com/api/docs/deprecations
- **GPT-5.6 の単価は10日連続で据え置きである**。100万トークンあたり Sol が入力 $4／キャッシュ $0.40／キャッシュ書込 $5.00／出力 $20（長文脈 $8／$0.80／$10／$30）、Terra が $2／$0.20／$2.50／$12、Luna が $0.20／$0.02／$0.25／$1.20 で、Sol の期間限定価格は「少なくとも 2026年11月21日まで」の記載が続く
- **ChatGPT Ads のセルフサービス購入が3地域へ広がった**。OpenAI がこれまで米国限定だった Ads Manager をインド・欧州・中東北アフリカへ開放し、広告事業は開始200日未満で年換算売上 **$10億** に到達したとされる。インド向けは **9/4 開始**で日次最低予算 ₹725（約 $7.60）、ローンチ時点で50ブランドが参加し WPP・Omnicom と提携する。⚠️ 発表日と一次到達性の扱いが 01 と 03 で分かれている（改善メモ参照）
- **ChatGPT for Healthcare に Epic 連携と Healthcare Public Data プラグインが入ったとされる**（9/1）。米国の適格な ChatGPT for Clinicians ユーザーが対象で、ClinicalTrials.gov / CMS Coverage / RxNorm / DailyMed / PubMed など9つの公開情報源を読み取り専用で検索できる（患者チャートには触れない）。Epic 連携は個人アカウントでは使えない。⚠️ 一次未読である
- ⚠️ **`learn.chatgpt.com` のゲートウェイ拒否が継続**しており、`site:` 付き WebSearch でも9月分の新規エントリは返らなかった。検索で拾えた Codex / ChatGPT の機能追加（Site URL の再デプロイなし変更・Apple silicon Mac での Apple Messages・読み取り専用の Codex スレッド共有・ピン留めチャットの同期）はいずれも 8/20 公開の既報であり新着ではない
- **`community.openai.com` の Announcements RSS は 8/25 の WebMCP 2本が最上位のまま**で9日間動きがない

### セキュリティ / フロンティアモデルの統制

- **OpenAI が Astra の Preparedness「Critical」到達を公表した**（9/1）。自社 Preparedness Framework のサイバー領域で初めて Critical を超えたとしており、Critical の定義は「多数の堅牢な実システムに対し人手なしでゼロデイを発見して実用的なエクスプロイトを作れること」または「高レベルの目標指示だけで堅牢な標的への攻撃を端から端まで組み立てて実行できること」である
  - 評価では ExploitBench が満点で、直近に公開された脆弱性を扱う別テストではゼロデイ2件を自力で発見した
  - 堅牢化したブラウザで、HTML ファイルを開かせるだけでサンドボックスを脱出しホスト上でコマンドを実行する連鎖を構築した
  - 堅牢化した OS でも複数の脆弱性をつなぎ、非特権ユーザーから root への権限昇格の連鎖を作った
  - ⚠️ **この結果は Daybreak Blue アクセス時のもの**で、既定の本番構成ではない。一般公開版は実システム向けエクスプロイト作成を拒否する制限が掛かり、高度なサイバー能力はサイバーセキュリティ連合 Daybreak の参加組織に限定される
- **Google は Gemini 3.8 Flash Cyber を一般 API に出さなかった**。同じ週の公開だが、消費者向けツールにも載せず、政府機関・重要インフラ事業者・ソフトウェアメンテナを対象とする新設の Fairwind Program 経由でのみ提供する。Chrome Security チームの評価では、はるかに大きな商用最上位モデル比で 2.6倍の正しいパッチを生成したとされる。最上位のサイバー能力は API 調達の対象から外れたことになる
- **CrowdStrike が SafeMind を発表した**（9/1・Fal.Con）。攻撃側の Red Tempest と防御側の Blue Solano の2モデル構成で、NVIDIA Nemotron を基盤に Falcon センサーのテレメトリと15年分の侵害対応データで学習させている。今後6〜12カ月で Falcon プラットフォーム全体へ展開する計画である
- ⚠️ **本節は一次本文にいずれも到達できていない**（`openai.com` はオリジン403、`deepmind.google` / `www.marktechpost.com` は本日新規のゲートウェイ拒否）。内容は複数の二次スニペットの突き合わせによる。Astra は 08-02 収録の「次期モデルファミリー」の続報で、EO 14409 の公開前レビュー枠組みを通る最初のモデルになる見込みという論点と地続きである
  - https://www.cnbc.com/2026/09/01/open-ai-astra-cyber-model.html
  - https://www.securityweek.com/openais-astra-becomes-first-model-to-cross-critical-cybersecurity-threshold/
  - https://www.crowdstrike.com/en-us/press-releases/crowdstrike-launches-frontier-models-for-cybersecurity-with-nvidia/

### オープンウェイト / MCP / xAI

- **HF の 8 org いずれにも 9/2 の新規公開はない**。`Qwen` / `moonshotai` / `deepseek-ai` / `meta-models` / `mistralai` / `zai-org` / `openai` / `google` を `createdAt` 降順と `lastModified` 降順の両方で確認した。各 org の最新作成は `Qwen3.8-Flash-Next-FP8` 8/24、`DeepSeek-V4-Flash-Vision-Exp` 8/31、`GLM-5.3-Flash-BF16` 8/25、`timesfm-3.0-pytorch` 8/24 などである
  - ⚠️ **追跡8リポジトリの `downloads` が前日の記録と全件同値**で、日次バッチの反映がない（9/2 19:09 UTC 取得）。likes は8件中8件が増えており API 応答自体は新しい
- **`blog.modelcontextprotocol.io` は 8/22 の「The New MCP Roadmap」が最上位のまま**で、新規エントリが12日間ない。⚠️ OpenAI 発の WebMCP は MCP 公式ブログ側に一切言及がなく、別系統として扱う状態が続いている
- **Musk が Grok 4.7 を予告した**（9/2）。パラメータ数は **2.1兆**（Grok 4.6 の1.5兆から40%増）、公開は 9/11〜9/12 頃で、ロケット・衛星・製造に関する SpaceX のデータを取り込んだと述べたとされる。提供は Grok 4.6 より遅くなる代わりにトークン効率が上がるという
  - ⚠️ **出所は X の投稿のみで、xAI の公式ブログ・モデルカード・プレスリリースはいずれも存在しない。** 一次3ホスト（`x.ai` / `docs.x.ai` / `grok.com`）と `x.com` はゲートウェイ拒否で到達できず、日付・仕様とも公式の裏づけがない観測として扱う
  - 現時点で公式に提供されている最新は **Grok 4.6**（8/12・context 50万トークン・$2/$6）のままである

### 企業動向 / 規制 / 市場データ

- **米商務長官 Howard Lutnick が Anthropic への評価を転換したとされる**（9/2・ノースカロライナ州 Chapel Hill の G20 Innovation Ministerial）。「we trust Anthropic」「back on the right side」と述べたとされ、国家安全保障と AI セーフガードをめぐる数ヶ月の対立を経ての転換と報じられている。同イベントでは共同創業者 Tom Brown が登壇し Lutnick のインタビューを受けた
  - ⚠️ **一次未読**である。`www.axios.com` はゲートウェイ拒否で到達できず、Axios / Forbes / Yahoo の二次一致で採った
  - ⚠️ 8/27 の連邦地裁による国防総省の指定違法判断（D.C. で訴訟継続中）や 9/1 の GenAI.mil への ChatGPT Mil / Grok 追加（Anthropic は非参加）との関係に、二次記事はいずれも触れていない
- **Microsoft が CSP の従量課金型オファーの検証枠を開けた**（9/2 付 Partner Center 告知）。9/1 からサンドボックス環境に flex spend plan（ストレージ／データベースのテスト製品）が提供され、CSP パートナーが従量課金型オファーの構造を検証できるようになった。対象は CSP 全セグメント（直接請求・間接リセラー・ディストリビューター）と SSP、および GSI / SI である
  - 構造は「単一契約で複数の対象製品をカバーする」「全額前払いではなく月次請求」「コミット期間全体をカバーする」「自動更新」の4点で支えられる
  - Microsoft は同じ構造を今後の複数の従量課金製品にも使うとしている
  - ⚠️ **Copilot 固有のライセンス変更ではない。** 本番オファーではなく、トライアル・プロモーション・インセンティブは対象外である。AI 支出の調達設計を「年間前払い」前提で組んでいる場合、選択肢が増える方向に前提が動く
  - https://learn.microsoft.com/en-us/partner-center/announcements/2026-september
- **市場データの定点はいずれも更新がなかった**。IDC / IDC Japan・MM総研・Similarweb・NRC のすべてで新規公表を検知できていない。参照可能な最新値は IDC の国内AI市場予測（2025年 2兆3,725億円 → 2029年 6兆8,897億円・CAGR 36.0%）と MM総研の個人利用経験率 21.8%（2025年8月時点）で、いずれも既収録から不変である
- 既報: Anthropic の IPO 観測（10月・$2T 超の評価額を目標と報道）、Anthropic × Nscale 約 $45B・6年、年換算 run-rate $650億（7月末）、SpaceX による Cursor 買収完了（8/14・$60B）

### Apple / クラウド

- **Apple が Intel 版 macOS アプリ向けの Rosetta サポート終了を予告した**（9/1）。macOS 26.4 以降は Intel 専用アプリの起動時にシステム通知が出るようになり、**macOS 27 が Rosetta を載せる最後のリリース**になる。以後 Intel 専用アプリは Apple silicon 上で動かないため、ユニバーサルバイナリ化が要る
- ⚠️ **Apple Developer News の AI 関連は 6/11 の ImageCreator クラス廃止告知が最新のまま**で、8/5 の App Store creative assets 以降に新規がない
- **AWS Bedrock は Fable 5.1 を初日から扱う**（`anthropic.claude-fable-5-1`）。⚠️ Bedrock と Google Cloud は退役スケジュールを独自に持つため、`platform.claude.com` の日付はそのまま適用されない
- 既報: 特別イベント（**9/9 10:00 PT**）、8/27 の税・価格改定、8/24 の Sign in with Apple 新ドメイン（`private.icloud.com`）、8/18 の EU 向けビジネス条件変更（発効 2026-10-01）

## 直近の注目予定

- **9/4**: WebMCP Challenge の提出締切 ／ ChatGPT Ads のインド向けセルフサービス開始（二次情報）／ Copilot 拡張機能 What's New・モデル可用性一覧の週次確認
- **9/6**: PnP コミュニティコール・Power CAT の週次確認
- **9/7**: 週次復旧チェック（月曜）／ ppweekly・MS-4005・課金レート表の週次確認
- **9/8**: M365 Copilot Release Notes の次バッチ（隔週傾向）／ Power Platform Released Versions の定例更新日
- **9/9**: Apple 特別イベント（10:00 PT）／ GLM-5.3-Flash の Z.ai 経由50%割引が終了
- **9/10**: MAI-Code-1-Flash が全 Copilot 体験から廃止
- **9/11–9/12**: Grok 4.7 の公開見込み（Musk の X 投稿のみが出所・公式の裏づけなし）
- **9/13**: Claude Code の週次上限50%増が終了
- **9/14**: Claude Code の標準週次上限が恒久的に +25%（現行比では17%減）
- **9/17**: OpenAI DevDay Exchange の応募締切
- **9/21**: Anthropic ウェルビーイング研究助成の応募締切
- **9/23**: WebMCP Challenge の受賞発表
- **9/24**: OpenAI の Videos API と Sora 2 系が退役（代替モデルの提示なし）
- **9/28**: Copilot のチャット3面統合 ／ code review の既定 effort が Lite → Balanced ／ チャットのデータ保持がアカウント存続期間へ ／ OpenAI の `gpt-3.5-turbo-instruct` / `babbage-002` / `davinci-002` / `gpt-3.5-turbo-1106` が停止
- **9/29 以降**: `claude-sonnet-4-5-20250929` の暫定退役日（確定日ではない）
- **9/30**: Gemini の旧 `gemini-omni-flash-preview` エンドポイント廃止
- **9 月**: iOS 27 / macOS 27 GA ／ Claudeforce のオープンベータ（二次情報）／ Copilot Studio の Roadmap 11件が GA 期日 ／ Release Plans on Learn への新規掲載停止 ／ Copilot Tuning の再開 Public Preview ／ App Store の Social Media 年齢レーティング回答が必須化 ／ OpenAI の IPO 観測
- **10/1**: Copilot Business・Enterprise の既存顧客が前払い必須に ／ Apple の EU 向け新ビジネス条件が発効 ／ Ask Gemini in Chat のプロモーション上限が終了
- **10/5**: Anthropic ウェルビーイング研究助成の full proposal 提出期限（採択者）
- **10/15 以降**: `claude-haiku-4-5-20251001` の暫定退役日（確定日ではない）
- **10/16–11/11**: OpenAI DevDay Exchange 8都市（**東京は 10/20**）
- **10/23**: OpenAI のレガシースナップショット退役（`gpt-3.5-turbo-0125` / `gpt-4-0613` / `o1-2024-12-17` / `o4-mini-2025-04-16` とファインチューン版）
- **10/31**: OpenAI の既存 evals が読み取り専用になる（09-03 追加）
- **10 月**: Anthropic の IPO 予定（$2T 超の評価額を目標と報道）／ 韓国 App Store のコンテンツ記述子2件が All → 12+
- **11/15**: Release Planner の退役（⚠️ 製品別ページの消滅は 9/3 に先行して発生した）
- **11/21**: GPT-5.6 Sol の暫定値下げが有効とされる期限
- **11/24 以降**: `claude-opus-4-5-20251101` の暫定退役日（確定日ではない）
- **11/30**: OpenAI の Reusable prompts・Evals プラットフォーム・Agent Builder が停止
- **12/1**: OpenAI の GPT Image 系が停止（`gpt-image-1-mini` / `gpt-image-1.5` / `chatgpt-image-latest` → `gpt-image-2`）
- **12/2**: EU AI Act の生成コンテンツ標識義務、8/2 以前に市場投入済みシステムへの猶予終了
- **12/11**: OpenAI の旧スナップショット退役（`gpt-5-2025-08-07` / `o3-2025-04-16` / `o3-pro-2025-06-10` 等）
- **12/31**: Gemini 3.8 Flash と 3.7 Flash の導入価格が終了（$0.75/$3.75 → $1.50/$7.50）／ GitHub Copilot の Fable 5.1 / Fable 5 に対する ZDR 暫定免除が終了
- **年内**: Anthropic の新データ保持方式（顧客自身のクラウドでの30日保持）投入予定 ／ OpenAI の Jalapeño チップの初期展開
- **2027-01-06**: OpenAI で大半のユーザーの新規ファインチューニングジョブ作成が終了
- **2027-01-20**: OpenAI の audio / realtime 系退役（`gpt-realtime` / `gpt-audio` / `gpt-4o-audio` と mini 系）
- **2027-02-05 以降 / 02-17 以降**: `claude-opus-4-6` / `claude-sonnet-4-6` の暫定退役日（確定日ではない）
- **2027-02-26**: OpenAI の文字起こし4モデル退役（`whisper-1` / `gpt-4o-transcribe` / `gpt-4o-mini-transcribe` / `gpt-4o-transcribe-diarize`）
- **2027-03-01**: SharePoint クラシック体験の退役フェーズ1
- **2027-04-16 以降 / 05-28 以降 / 06-09 以降 / 06-30 以降 / 07-24 以降 / 09-01 以降**: `claude-opus-4-7` / `claude-opus-4-8` / `claude-fable-5` / `claude-sonnet-5` / `claude-opus-5` / `claude-fable-5-1` の暫定退役日（確定日ではない）
- **2027-06-30**: Claude for Teachers の学区登録期限
- **2027年末**: Anthropic が借りる Nscale West Virginia データセンター（460MW）の稼働開始見込み
- **2028-06**: 米国 K-12 教職員向け ChatGPT for Teachers の無料提供期限
- **2028-10-01**: SharePoint クラシック体験の退役フェーズ2

## 改善メモ

- 3ソースの当日分（01 Master / 02 Copilot / 03 industry）はいずれも取得できた。前日 09-02 分にも欠損記録はなく、欠損リカバリの対象はない
- **前日サマリーが記録した 01 と 03 の食い違い2件は本日解消した** — `github.blog/changelog` の Copilot code review PR 承認（9/1）と Gemini API changelog の agentic video understanding（9/1）は、本日いずれも 01 側が一次 URL つきで収録している。09-02 に「01 側でラベル絞り込みの取りこぼしが起きている可能性」と書いた懸念は、少なくとも本日分では再現していない
- ⚠️ **ChatGPT Ads の地域拡大について 01 と 03 で発表日と一次到達性が分かれた** — 01 は「一次未読（`openai.com` はオリジン403）で複数媒体の二次一致で採った」とし、インド開始を **9/4** の予定として扱う。03 は「8月31日に開放した」と断定し `openai.com/index/expanding-access-to-ai-with-chatgpt-ads/` を出典に挙げて「2日遅れの捕捉」と書く。⚠️ 同じホストを 01 が403、03 が出典として提示しており**到達性の記録自体が矛盾する**。本サマリーは事実（3地域への開放・年換算 $10億）を採り、発表日は断定せず 9/4 のインド開始のみ予定に残した
- ⚠️ **継続提案の計数が3ソースとも前日と合わない** — 本日は 01 が24件（最多 B-013・36回目）、02 が28件（最多 B-011・45回目）、03 が12件（最多 B-004・66回目）で計 **64件**。前日は 01: 32件 / 02: 29件 / 03: 12件の計73件だったため、01 だけで8件減っている。02 は 09-01 に28件 → 09-02 に29件 → 本日28件と振れており、09-02 に記録した「計数基準が安定していない可能性」は 01 側にも及ぶ
- **新規の改善提案は2件** — B-057（01: Gemini API Changelog 項に料金ページ `ai.google.dev/gemini-api/docs/pricing` を副 URL として追加）、B-055（02: 登録ソースが 404・転送先なしで消えたときの手順が未定義。取得障害として記録せず、消滅範囲の確定と判定経路の移設で閉じる規定を `fetch-flow.md` に追加）。03 は新規提案なし
- **B-055 はハイライト3の直接の帰結である** — Release Wave 製品別ページの消滅は「取得できなかった」のではなく「ソースが無くなった」事象で、既存の取得障害フローでは扱えない。02 が同日中に起票している
- ⚠️ **取得障害が2件増えた（03 起票）** — `deepmind.google`（Gemini 3.8 Flash モデルカード）と `www.marktechpost.com`（3.8 Flash Cyber の詳報）を新規のゲートウェイ拒否として台帳に追加した。03 は「ハイライト1・2の一次／詳報がいずれもこの2ホストにあたり、**同一主題の一次と二次が同時に落ちる型の再発**」と記録している。01 も同じ主題で `blog.google` / `deepmind.google` に到達できておらず、Gemini 系の一次確認は料金ページと changelog の2本に依存している
- ⚠️ **長期化している一次未読・接続障害**: `mc.merill.net` の拒否が27日連続（02）、Copilot Tuning 一次の未更新が14日連続（02）、Copilot Studio What's New への GA 未反映が31日連続（02）、Released Versions の空白が65日（02）、`learn.chatgpt.com` の拒否（01）、`docs.devin.ai` の拒否（01）、xAI 一次3ホストの拒否（01）、`www.axios.com` の拒否（01）。いずれも解消の見込みが立っていない
- **本サマリーの生成環境について** — 本日の実行では GitHub MCP のリポジトリスコープが `kit1132/05_ai-news-daily` のみに設定されており、入力3リポを MCP 経由で読めなかった。公開リポの `raw.githubusercontent.com` から読み取り専用で取得して生成した（入力3リポへの書き込みは行っていない）。⚠️ スコープ設定が今後も同じなら、取得経路を raw に固定するか実行環境のスコープへ入力3リポを追加するかを決める必要がある
- **未解決の要 kit 対応（08-07 確定・継続）**: 08-06 追加の許可ドメイン13件は新規起動セッションでも全件未到達。① 保存先環境とスケジュールタスク実行環境の同一性確認 ② `.google` TLD 3件の個別指定確認 ③ 次回追加対象に `api-docs.deepseek.com` / `www.deepseek.com` ほかを含める
