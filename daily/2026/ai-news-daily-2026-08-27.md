# AI News Daily Summary — 2026-08-27

木曜は、エージェントに渡す権限と鍵の前提が3方向から動いた日である。Claude Code は第三者ゲートウェイ用の API キーを Anthropic 宛テレメトリに載せていた欠陥を v2.1.246 で修正したが、npm の `stable` は14日間 2.1.231 のままで修正が届いていない。Claude in Chrome は全有料プランで GA になり、ブラウザ操作が都度承認から分類器による事前検証へ移った。Cowork はモデル一覧が入れ替わって effort 5段が付き、モデル選択が従量課金の操作になった。監査側では Compliance API のセッション取得が beta を抜け、Admin API が7言語 SDK に載った。OpenAI は WebMCP を公開し、A2A は Linux Foundation 傘下で MCP と同じ屋根の下に入った。

## 今日のハイライト

### 1. Claude Code v2.1.246 が第三者ゲートウェイの API キー送信を修正した — 「鍵は自ホストにしか出ない」前提が「出ていた」に変わる

**要点**: Claude Code が `ANTHROPIC_BASE_URL` 用に設定した認証情報を Anthropic 宛のテレメトリにも載せていた欠陥を、8/25 公開の v2.1.246 で修正した。ゲートウェイ経由の組織は鍵をローテートするかを今日判断することになる。

**詳細**: v2.1.246 は60項目超の大型リリースで、修正の記述は「テレメトリとメトリクスのリクエストが第三者ゲートウェイ用の API キーを持って Anthropic へ送られていた／認証情報は自身のホストにしか送られなくなった」である。同版には権限系の修正が3件同居する。

- `/permissions` に **Auto mode タブ**が加わり、自動承認を決めている分類器ルールを一覧・編集できるようになった。何が承認なしで通るかを組織側で棚卸しできる
- `Bash(git * main)` のようにサブコマンドの手前にワイルドカードを置いた allow ルールは、サブコマンドより前に挿入されたオプションにも一致するため、起動時に警告が出るようになった
- 末尾に `&&` / `||` が残った不正な Bash コマンドは、常に承認を要求するようになった

⚠️ npm の `dist-tags` は本日 `{stable: 2.1.231, latest: 2.1.246, next: 2.1.247}` で、**`stable` は 8/13 publish の 2.1.231 から14日間動かず**、`latest` との差は15版に開いた。上記の認証情報修正も権限系の修正も、stable チャネルに固定している組織にはまだ届いていない。

- https://code.claude.com/docs/en/changelog
- https://registry.npmjs.org/@anthropic-ai/claude-code

### 2. Claude in Chrome が全有料プランで GA になった — ブラウザ操作の判断が「使えるか」から「どのドメインを許すか」へ移る

**要点**: Anthropic が Claude in Chrome を beta から GA へ移し、全有料プランで提供した。1操作ごとの承認が分類器による事前検証に置き換わったため、検討事項は導入可否ではなく許可ドメインの線引きになる。

**詳細**: 2025年8月のリサーチプレビューから約1年での GA で、Chrome Web Store から導入する。ログイン済みセッションのままページ閲覧・テキスト入力・リンククリックとページ遷移・フォーム入力と送信を行い、Claude Code と同じ考え方の自動承認モードで一連の操作を続けられる。Enterprise では管理者が Organization Settings で可否を制御し、承認済みドメインに限定できる。他の Chromium 系ブラウザとモバイルは対象外である。

プロンプトインジェクション対策は3層で、攻撃ライブラリを拡張したモデル学習、ツール結果を走査するプローブ、実行直前の操作が当初の依頼と整合するかを照合する分類器を組み合わせる。攻撃成功率は対策前で **Opus 4.5 の 17.6%** から Opus 5 の 3.8% へ下がり、プローブと分類器を併用すると Sonnet 5 / Opus 5 で 0%、Fable 5 で 0.3% だったとしている。

⚠️ 数値はいずれも Anthropic 自身のレッドチーム評価であり、第三者検証ではない。承認済みドメインの限定をかけずに配布すると、社内 SaaS の画面をエージェントが自律操作できる状態になる。

- https://claude.com/blog/claude-in-chrome-generally-available

### 3. Cowork のモデル一覧が入れ替わり effort 5段が付いた — モデル選択が品質の選択から従量課金の選択に変わる

**要点**: Cowork のモデル一覧が 8/25 に入れ替わり、Claude Opus 4.8 と Sonnet+Opus Advisor が消えて Opus 5 と GPT 5.6 系が入った。あわせて effort 5段が付き、モデル選択が消費量の選択になった。

**詳細**: 一次は `cowork-models`（`updated_at` 2026-08-25T02:52Z）で、現在のモデルピッカーは Auto（既定）／GPT 5.5 (Frontier)〔Azure AI Foundry ホスト〕／GPT 5.6 Sol〔難易度の高い作業向け〕／GPT 5.6 Terra〔一般的なタスク向け〕／Opus 5〔複雑・高リスクな作業向け〕／Claude Sonnet 5／Claude Fable 5 (Preview) の7つである。7/30 に同ページで確認した Opus 4.8 と Advisor は現在の表から消えている。effort は Light / Medium（既定）/ High / Extra High / Max の5段で入力ボックスに置かれ、ページは「高い effort ほど時間がかかり、上限の消費が速くなる」と明記する。Cowork は 6/16 の GA で使用量ベース課金に移り、管理者が M365 admin center でユーザー単位・グループ単位の上限を設定できるため、effort は課金に直結する操作にあたる。

⚠️ 本件は Cowork What's New にも M365 Copilot Release Notes にも記載がない（Release Notes の全バッチを grep して `5.6 Sol` / `Terra` / `Opus 5` / `Extra High` はいずれも0件）。⚠️ **一次どうしが食い違っている。**`cowork-admin-governance`（`updated_at` 2026-08-18T17:48Z）は、消えたはずの Sonnet+Opus Advisor を現行として残したままである。Work IQ ボタン（B-044）に続き2件目の一次間矛盾になった。

- https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-models
- https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-admin-governance

## カテゴリ別まとめ

### Anthropic / Claude

- Claude Code v2.1.246 の認証情報修正と stable の据え置きはハイライト1を参照
- v2.1.246 は認証情報・権限系以外の変更も広い。設定の反映と応答の扱いが変わった
  - `/cd` の移動先のプロジェクト設定・hooks・`.mcp.json`・skills・agents が、`--resume` を待たずその場で有効になった
  - `maxTurns` で止まったサブエージェントは、「完了」ではなく **partial** として結果を返すようになった
  - 非対話セッション（`-p` / SDK / クラウド）が、ストリーム途中で切れた応答を自動継続するようになった
  - ターン完了時刻が所要時間の行に表示される（`done 6:05 PM` の形式）
- v2.1.246 は描画とメモリの重い不具合も直した。base64 のような超長1行を含む diff でトランスクリプトが極端に遅くなる問題、フルスクリーンと Ctrl+O の表示でメッセージ行ごとに会話全体のツール参照を保持していたメモリ増加、巨大ファイル上書き後に Write ツールが "Out of memory" を出す問題、45秒でバックグラウンドセッションが失敗する不具合が対象である。自分で作った `.claude/worktrees/` 配下の git worktree が古いバックグラウンドセッション記録に紐づいて掃除される問題も解消した
- ⚠️ `next` の **v2.1.247 は 8/26 18:02 UTC に publish 済み**だが changelog には無く、npm 先行の形のためリリース済みとして扱わない。8/26 に記録した「v2.1.244 は欠番」は本日も変わらず、`time` にも記録が無い
- **Compliance API のセッション取得が beta を抜けた。** Anthropic が 8/26 付けの Platform release notes で公開し、端末上で動く Cowork と Claude Code のセッションを組織が取得できる状態を GA にした。08-11 のベータ提供から2週間強での GA にあたる（https://platform.claude.com/docs/en/release-notes/overview ）
  - GA の範囲: 組織横断の一覧・個別セッションのメタデータ・トランスクリプトの3系統
  - beta で追加された範囲: Claude Science セッション（`product_surface` が `claude_science`）と、Excel / PowerPoint / Word / Outlook 上の Claude for Microsoft 365 セッション（`office_agents` で始まる値）。対象は Claude Enterprise 組織である
  - 必要な資格情報は既存の Compliance Access Key と `read:compliance_user_data` スコープで、追加の申請はいらない
  - 「端末上のセッションは追えない」を前提に置いていた社内展開の設計は組み直せる。M365 の Office アプリ内エージェントまで同じ鍵で追えるため、Copilot との併存環境でログ収集の窓口を1つにまとめられる
- **Admin API が `ant` CLI と7言語 SDK から使えるようになった。** Anthropic が Python / TypeScript / C# / Go / Java / PHP / Ruby の各 SDK に `client.beta.organization` として載せた。組織情報・メンバー・招待・ワークスペース・API キー・レート制限・サービスアカウント・workload identity federation・顧客管理暗号鍵をカバーする。⚠️ 使用量とコストのレポート、Claude Enterprise のユーザー管理・分析エンドポイントは **curl 専用のまま**である
- Anthropic が `claude.com/blog` に 8/26 付けで Warp のエージェント自己改善事例を追加した（後述の「市場データ・導入事例」参照）。`support.claude.com` の Release Notes は 8/25 の memory 更新が最上位のままで 8/26 の追加はない
- モデル退役ページに新規の告知はない。直近の告知は 2026-06-05 の Opus 4.1（8/5 退役済み）で、現行モデルはすべて Active である。暫定退役日で最も近いのは `claude-sonnet-4-5-20250929` の 9/29 以降、次いで `claude-haiku-4-5-20251001` の 10/15 以降、`claude-opus-4-5-20251101` の 11/24 以降だが、⚠️ いずれも「not sooner than」で確定日ではない
- 既報の期限: Claude Code の週次上限50%増は **8/31** のままで、延長告知は検出できていない。⚠️ 一次は `x.com`（ゲートウェイ拒否）の公式アカウント投稿のため、期限そのものは二次一致で確認している

### Microsoft 365 Copilot / Cowork

- Cowork のモデル入れ替えと effort 5段はハイライト3を参照
- **Cowork が7月から event-driven tasks に対応していたことを本日はじめて確認した。** 自動化の起点が定時実行だけでなく、条件に合うメールの受信と Teams のメンション受信にも広がっていた。ユーザーが監視したい条件をメッセージで説明すると Cowork が自動化案を提示し、ユーザーが確認して確定する方式で、作成した自動化は既存のスケジュールプロンプトと同じ **Automations** ページに並ぶ。⚠️ 一次の Cowork What's New は `daily-sources.md` 未登録で、7月の公開から本日まで検知できていなかった（https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/whats-new ）
- ⚠️ **08-26 の本サマリーが書いた「Cowork の画像生成が Imagen 2 から ChatGPT Images 2.0 に変わった」は誤りである。** Cowork What's New の「June 2026 (general availability)」節は GA 時点から ChatGPT Images 2.0 と明記しており、変わったのは `cowork-models` の記述のほうで、同ページは現在いずれの画像モデルにも触れていない
- **Copilot Notebooks に Power BI レポートを参照として追加できるようになる。** Microsoft が Roadmap 569928 を 8/25 に起票し、ファイルと並べてレポートのデータをノートブックへ持ち込む形にした。状態は `In development` で、Preview が 2026年8月・GA が **2026年9月**である。8/26 に GA が確認された Outlook メール（564910）と Teams 会議（560706）に続く3件目の知識ソース拡張にあたる（https://www.microsoft.com/microsoft-365/roadmap?id=569928 ）
- M365 Copilot Release Notes の August 25 バッチは全19項目のままで、節構成・項目とも 8/26 から増減していない。`## ` 見出しの並びも August 25 → August 11 → July 29 → July 15 → July 01 → June 16 → June 2 で変化がない
- Roadmap 全体の Release Communications RSS は本日 **1,787項目**（前日比 +2）で、増分は 569928 と 569929（Planner の Connected Plans・対象外）である。広報枠の先頭は 7/24 の Opus 5 提供開始のままで、Frontier 枠4件にも変化はない
- ⚠️ **Copilot Tuning は停止発効から7日たっても一次が無記載である。**`copilot-tuning-overview` は `ms.date` 2026-06-03 / `updated_at` 2026-08-18T17:48Z で 8/26 から動いておらず、Optimization エージェントを「サポートされるシナリオ」節とテンプレート選択表の両方に現行機能として載せたままである。冒頭の Important も「Frontier 経由の提供は 2026年4月予定」で止まっている（B-024 回数 20）
- ⚠️ 二次の空振りが8例目になった。英語圏の「8月の新機能8件」系が挙げる Excel の `@theme-design` スキルは、Release Notes の全バッチを grep して0件だった。同記事群が8月の新規として挙げる Copilot Notebooks のマインドマップは July 01 バッチ、クラシック Outlook の会議準備は August 11 バッチの既報である
- Purview の What's new に Copilot 固有の新規項目は追加されていない。8月節は Sensitivity labels の2件、7月節は6分類・計16項目で 8/26 から差分ゼロである。⚠️ 8/23 に Roadmap 側で検知した 569612（Copilot メモリの Purview 保持・GA 2026年9月）は本日も Purview 側に現れていない（B-016 回数 28）

### Copilot Studio / Power Platform

- ⚠️ **今月が GA 期日の資格情報ガバナンスが残り4日で未達である。** Roadmap 566997（メーカー資格情報の使用ブロック）は本日も `In development` で、GA 期日「August CY2026」まで4日しかない。PPAC の Usage ページも GA 期日が今月なのに緑チェックが付かないまま同じ残り日数になった。⚠️ 562221（ワークフローでの MCP 準拠ツール利用）は GA 期日 2026年6月のまま `In development` で、超過が2か月を超えた（https://www.microsoft.com/microsoft-365/roadmap?id=566997 ）
- **Power Automate モバイルアプリの廃止が 8/31 に発効する（残り4日）。** Power Platform の非推奨一覧の先頭項目で、週次確認でも新規追加はなく `## ` 見出しは90本のままである（https://learn.microsoft.com/en-us/power-platform/important-changes-coming ）
  - アプリが App Store と Google Play から削除され、更新とサポートが終了する
  - 「Send me a mobile notification」アクションは残るが、モバイルアプリ宛の通知に届き先が無くなるためフロー側の変更が要る
  - iOS / Android のホーム画面ウィジェット（run a flow）が動作しなくなる
  - 既存のクラウドフロー（自動・スケジュール・インスタント）は影響を受けない。承認は Teams の Approvals アプリ、フロー管理はモバイルブラウザーの Power Automate ポータル、インスタントフローの実行は Power Apps mobile が代替になる
- Copilot Studio の What's New は July 2026 節が最新のままで、8月節は作成されていない。`updated_at` は 2026-08-20T19:04Z で動いておらず、⚠️ June 節の GitHub Copilot ハーネスは本日も `(Production-ready preview)` の表記で、GA（8/3）から **24日連続**の未反映になった（B-023 回数 23）
- Release Wave の3ページ（`power-automate` / `power-apps` / ガバナンス・管理）は 8/26 と完全に同一で、緑チェックの追加・期日変更・行の増減はいずれも発生していない。期日超過は延べ6行、8月期日10件、9月期日6件で据え置きである。⚠️ 3ページのいずれにも Release Wave 廃止・移行の注記は本日も一文も入っていない
- Released Versions の Copilot Studio Build は 2026.6.3（6/30 初出）のままで、空白が8週間を超えた。リージョン分布（11 / 5 / 3 の3段）と UX 版 26.06.21-24 にも変化はなく、次回の定例更新日は 9/1 である（B-037 回数 10）
- **CSP の growth margins が 2026-10-01 から始まる。** Direct Bill パートナーとディストリビューターが、対象の Microsoft 365 成長取引で基本マージンに上乗せする partner-earned economics を得られるようになる。顧客向けの値引きではなく、現時点では **Sandbox のみ**で本番未提供である（https://learn.microsoft.com/en-us/partner-center/pricing/growth-margins ）
  - 計算は基本マージンと growth margin を ERP から並列に減算する（ERP $100・基本20%・growth 15% → パートナー価格 $65）。顧客向けプロモーションはその後に乗算で適用される
  - 対象外の主な理由は、ルックバック期間（既定3年）内の同製品保有、最低シート数未達、シート拡張倍率の未達、既存サブスクリプションへのシート追加、EA→CSP のチャネルシフト、Specialized Offer の優先適用である
  - 期中のシート拡張は新規サブスクリプションに載せた分だけが対象で、更新時は既存分を含む全シートが対象になる。更新時に再判定され、要件を満たさなければ基本マージンへ戻る
- パートナーがコンプライアンス研修を **Partner Skilling hub** から受けるようになった（Partner Center 8/26 付）。Partner University と従来のコンプライアンスギャラリーの両方を置き換える単一の入口で、Microsoft Partner Agreement に関わる14本のオンデマンド研修が掲載されている
- 据え置き: Microsoft Copilot Blog は 7/21、Copilot Studio Blog は 8/3、Tech Community の M365 Copilot Blog は 8/13、M365 Developer Blog は 8/13、Agent 365 Blog は 8/6、Power Platform Blog の月次は 8/6 の合併号で、いずれも新規がない。⚠️ M365 Blog 本体は RSS・HTML 一覧ともオリジン 403 が再発し、本日は WebSearch のみでの照合になった

### GitHub Copilot / 開発ツール

- **GitHub Copilot app の Customize タブが GA になった。** GitHub が 8/25 に一般提供を開始し、MCP サーバー・プラグイン・スキル・キャンバスという拡張手段の入口を1画面に集約した。MCP サーバーはカテゴリ別のおすすめとトレンド表示から絞り込める。例示されている使い方は Azure DevOps 連携で、課題のトリアージ・バックログの優先度付け・フォローアップの割り当てを行い、調査や実装、レビュー準備を Copilot へ引き渡すというものである。⚠️ **対象プランと利用上限**は告知に記載がない（https://github.blog/changelog/2026-08-25-github-copilot-app-customize-tab-is-generally-available/ ）
- **Copilot CLI に pre-release が2版入った。** 安定版は v1.0.80（8/14）のまま **13日間据え置き**で、8/19 以降の版はすべて pre-release 側にとどまる
  - `v1.0.81-12`（8/26 18:21）: Windows で Microsoft Entra ID 保護のリモート MCP サーバーに OS 認証ブローカー（WAM）経由でサインインでき、「多くの場合プロンプトなし」で通るようになった。他プラットフォーム・device code フロー・ブローカーライブラリの無い環境は従来のブラウザ認証のままである。テレメトリ置換中に同一セッションを繰り返し再開するとクラッシュする問題も修正した
  - `v1.0.81-11`（8/26 01:32）: エンタープライズポリシーでブロックされた MCP サーバーが、`/mcp` で「ブロック済み」と表示されるようになった
  - ⚠️ `v1.0.81-10` は releases 一覧に存在しない（-9 の次が -11）。連番の飛びを取りこぼしと誤判定しないこと
- `github.blog/changelog` の Copilot ラベルは 8/25 の Customize タブ GA が最上位で、8/21 の Slack / Microsoft Teams 連携2本がそれに続く。8/26 の追加は「GitHub App からエンタープライズ課金データへアクセス可能に」の1件のみで AI 関連ではない
- Cursor の changelog は 8/19 の Cloud Agents / Harness 更新が最上位のままで **8日間**動きがなく、フォーラムの Announcements も 8/17 の Origin Code Hosting のまま10日間止まっている
- **Cognition が Devin Coach を 8/14 に投入していたことを本日確定した。** セッションの入力ボックスに書きながら改善案を出し、送信前にプロンプトを直させる機能である。同時期に Devin Review が base ブランチとの diff が変わらない PR（stacked PR の restack 等）の再レビューを省くようになり、Devin のセッションが自身の投稿した Slack スレッドを購読して返信をセッションへ戻すようになった。⚠️ `docs.devin.ai` はゲートウェイ拒否が継続しており、いずれも二次一致で一次未読である
- xAI / Grok に新規発表を検出できていない。**Grok 5 は未リリースが継続**し、8/12 の Grok 4.6（context 50万トークン・reasoning effort 4段）から進展がない。一次3ホスト（`x.ai` / `docs.x.ai` / `grok.com`）は到達不可が続く
- 期限: GitHub Spark の既存ユーザーアクセス終了（**8/31**）、モデル廃止（**9/1**）、MAI-Code-1-Flash の廃止（**9/10**）

### OpenAI

- **OpenAI が実験的オープン標準 WebMCP を公開した。** ChatGPT Work と Codex の内蔵ブラウザが対応し、エージェントにスクリーンショットとクリックで操作させる前提から、サイトが同一セッション上でツールを直接提供する前提へ移した。ウェブアプリが人向けの UI と並べてエージェント向けのツール（ChatGPT 上では **Site tools**）をページ上で公開し、エージェントは利用者のログイン済みセッションのまま同じ生きたページを操作する。Chrome 開発者向けガイドと ChatGPT Learn のドキュメントが同時公開され、協力企業は Google Chrome / Cloudflare / Shopify / Vercel / Render / Netlify である（https://community.openai.com/t/build-agent-ready-websites-with-chatgpt/1392588 ）
  - 併走する **WebMCP Challenge** が 8/25 11:00 PT に始まった。10日間のハッカソンで賞金総額 $35,000 に Codex Micros・ChatGPT Pro・パートナークレジットが付く
  - 提出締切は **9/4**、受賞発表は 9/23 で、10チームが各 $3,000 とパートナークレジット約 $18,480 を受け取る
  - 参加要件はコード全体の OSS 公開・3分の動画・説明文の提出である
- **ChatGPT の Scheduled tasks がイベント起動に対応した**（8/26）。Gmail の新着メッセージ（送信者・件名でのフィルタ可）、Slack のチャンネル新着メッセージ（監視するチャンネルごとに `@ChatGPT` の追加が必要）、認可した github.com リポジトリの pull request 活動をトリガーにタスクを開始できる
  - 対象は Plus / Pro / Business / Enterprise / Edu である。⚠️ **Free はイベント起動を使えず**、アクティブなタスクは3件まで、繰り返しタスクも1日1回までに制限される
  - 有料層限定だったスケジューリングのハブ画面が、Free でも使えるようになった
  - 作成したタスクを共有し、受け取った側が自分のアカウントを接続してカスタマイズすることもできる
- ChatGPT / Codex の 8/24〜8/28 週にはほかに2件が載っている。デスクトップアプリの **Apple Messages 連携**（Mac 上の Messages でチャット検索・要約・返信作成・送信）と、Site の共同編集（ワークスペースの有効メンバーを編集者として招待し公開まで行える）である
- **8/26 に停止した Assistants API と o3 の区分更新は一次にまだ反映されていない。** ChatGPT 側は90日のサンセット期間を経て web とモバイルのモデルピッカーから o3 が消え、API 側は `/v1/assistants` `/v1/threads` `/v1/threads/runs` が対象で代替は Responses API と Conversations API の組み合わせになる。⚠️ 一次の退役ページは本項を「Upcoming deprecations」の区分に置いたままで、実行済みへの区分変更が入っていない。API の o3（`o3-2025-04-16` / `o3-pro-2025-06-10`）は対象外で停止は 12/11 である（https://developers.openai.com/api/docs/deprecations ）
- OpenAI の残る退役期限8件に変更はない。一次ページの全件を突き合わせ、撤回・延期・新規追加のいずれも無いことを確認した。内訳は 9/24（Videos API と Sora 2 系）、9/28（旧 GPT スナップショット4種）、10/23（旧モデル12種とファインチューン版5種）、11/30（Evals / Agent Builder / `v1/prompts`）、12/1（GPT Image 系）、12/11（GPT-5 と o3 のスナップショット）、2027/1/6（ファインチューニングの新規ジョブ作成終了）、2027/1/20（旧 audio / realtime / transcription 系）である
- **GPT-5.6 の単価は3日連続で据え置きである。** 1M トークンあたり Sol は入力 $4・キャッシュ $0.40・キャッシュ書込 $5.00・出力 $20（長文脈側 $8／$0.80／$10／$30）、Terra は $2／$0.20／$2.50／$12、Luna は $0.20／$0.02／$0.25／$1.20 で、Sol の期間限定価格が「少なくとも 2026年11月21日まで」の記載も不変である。Batch と Flex は標準比おおむね50%引きが続く（https://developers.openai.com/api/docs/pricing ）
- `developers.openai.com/api/docs/changelog` は 8/21 の2件が最上位のままで、8/22 以降の追加が6日間ない
- **Codex CLI に pre-release が4版追加された**（`0.150.0-alpha.10` 8/25 20:36 ／ `.11` 8/25 21:30 ／ `.12` 8/26 10:06 ／ `.13` 8/26 11:18）。⚠️ 4版とも本文が空で変更内容は未確定である。代替経路のタグ間比較は数十コミット規模で GitHub 側が生成しきれないため適用していない。安定版は `rust-v0.149.1`（8/24）据え置きである
- **OpenAI が ZDR を保ったまま悪用検知する方式を予告した。** 8/19 公表の Private Safety Processing で、ゼロデータ保持の対象顧客に対し、複数の関連するやり取りをまたいだ悪用パターンを検出しつつプロンプトと応答を同社の担当者が閲覧しない構成をとる。保管の選択肢として、顧客が管理するインフラに置く方式に加え、顧客が管理する鍵で暗号化した OpenAI ホスト型を開発中とする。⚠️ 現時点では preview の位置づけで一般提供時期は示されていない。「ZDR を選ぶと悪用監視が単一リクエスト単位に限られる」という提案上の前提が動く可能性がある（https://openai.com/index/offering-zero-data-retention-for-frontier-models/ ）
- 期限: 公式 DALL·E GPT の退役（**8/30**）、GPT-5.4 / 5.4 mini が Codex（ChatGPT サインイン）から除外（**8/31**・移行先は `gpt-5.6-terra` と `gpt-5.6-luna`）

### Google

- **Google が Gemini 3.5 Transcribe と Transcribe Live を GA にした**（8/26）。Gemini の音声理解を土台にした専用の音声認識モデル2種で、いずれも一般提供である
  - `gemini-3.5-transcribe`: 非ストリーミングの高精度・低レイテンシで、**85言語以上**に対応する。発話単位の言語検出、話者ダイアライゼーション、単語単位のタイムスタンプ、最大1,000語のカスタム語彙バイアスを持つ
  - `gemini-3.5-transcribe-live`: Live API 上の WebSocket による双方向ストリーミングで、暫定と確定の文字起こしイベント、smart transcription モード、複数の VAD 戦略に対応する
  - ⚠️ 料金は changelog に記載がない
- **Ask Gemini in Chat のロールアウトが 8/26 に始まった**（既報の予定どおり）。Gmail / Drive / Calendar を横断した検索、会話を離れずの画像生成・下書き作成、会話のキャッチアップを Google Chat 上で行える。**10/1 まで上限のプロモーション枠**が付き、機能が見えるまで最大15日かかる
- Gemini API の料金ページは最終更新日だけが 8/13 から 8/26 UTC へ動き、単価は全モデルで据え置きだった。3.7 Flash / 3.6 Flash は入力 $0.75・出力 $3.75（**12/31 まで**、以降は約2倍へ戻る）、3.5 Flash $1.50／$9.00、3.5 Flash-Lite $0.30／$2.50、3.1 Pro $2.00／$12.00（20万トークン以下）、2.5 Pro $1.25／$10.00 で変化がない（https://ai.google.dev/gemini-api/docs/pricing ）
- 既報: `gemini-robotics-er-1.6-preview` の停止は 8/31、**Gemini 3.5 Pro の GA は未ローンチが継続**で、モデル ID・価格・日付のいずれも公表されていない。HF の `google` org も 8/19 の TIPS v1 6本が最新のままである

### オープンウェイト / ローカル LLM

- **8/26 にオープンウェイトの主要モデルが2本同時に公開された。** どちらも 08-26 のセッションでは検出できておらず、本日が初検出にあたる
  - `Qwen/Qwen3.8-Flash-Next`（Alibaba）: Qwen4 のアーキテクチャを先行公開する実験モデルで、総パラメータ 125B に対しトークンあたり **6B のみ活性化**する MoE である。N-gram 埋め込みを 51B 持ち、ビジョンエンコーダ付きの因果言語モデルで、ネイティブ context は 262,144 トークン（100万まで拡張可）。HF 実測は BF16 で約180GB / 144ファイル、ライセンスは `other`（Apache でも MIT でもない）。FP8 版も同時公開された
  - `zai-org/GLM-5.3-Flash`（Z.ai）: GLM-5 系で初のネイティブマルチモーダルモデルで、**MIT ライセンス**である。総 320B / 活性 18B の MoE、context は100万トークンで、HF 実測は FP8 主体で約321GB / 72ファイル。API 料金は入力 $0.15 / 出力 $0.50（100万トークンあたり）で、**9/9 まで50%割引**が付く。公開前は匿名エイリアス `Ox Alpha` として運用されていた
  - ⚠️ どちらも HF のリポジトリ作成日が公開日より前である（Qwen は 8/24 作成 / 8/26 公開、GLM は 8/25 作成 / 8/26 公開）。`createdAt` 降順の一覧だけを見ていると、org が活発な日には公開当日のモデルが上位に出ない
- 実測（8/27・カッコ内は前日比）: `Qwen/Qwen3.8-27B-FP8` が DL **3,797,538**（+433,638）／ likes 702、`Qwen/Qwen3.8-27B` が DL 3,298,569（+353,154）／ likes 12,865 で伸びが突出する。`DeepSeek-V4-Flash-0731` は DL 3,857,140（+328,767）、`DeepSeek-V4-Pro-0813` は DL 85,230（+10,523）である。新規2本は公開直後で `Qwen3.8-Flash-Next` が DL 2,551 / likes 3,500、`GLM-5.3-Flash` が DL 0 / likes 682 にとどまる
- `moonshotai` / `mistralai` / `meta-models` / `openai` の4 org に新規はない

### 標準化・エージェント統制

- **A2A が Linux Foundation 傘下の Agentic AI Foundation へ移管された。** Google 由来の A2A が Anthropic 由来の MCP と同じ中立組織の管理下に入り、エージェント間連携の標準が単一ベンダー保有から共通基盤へ変わった。8/17 の Axios 報道を皮切りに 8/19〜20 にかけて公表されたもので、本サマリーでは 08-26 に「未確定」としていた項目が本日確定した（https://www.forbes.com/sites/janakirammsv/2026/08/19/agent2agent-joins-the-agentic-ai-foundation-alongside-mcp/ ）
  - 役割の分担: MCP はエージェントとツールの縦方向（データベース・API・ファイルシステムへの到達）、A2A はエージェント同士の横方向（依頼と結果の受け渡し）を標準化する
  - A2A の仕組みは、各エージェントが能力と到達方法を記述した agent card を公開し、他のエージェントがそれを読んで人の仲介なしに作業を引き渡すというものである
  - 経緯は Google が 2025年4月に公開し **2026年3月に v1.0** へ到達、採用組織は150超に及ぶ
  - AAIF は発足1年足らずで加盟が49社から250社超へ増え、Platinum には AWS・Anthropic・Block・Bloomberg・Cloudflare・Google・Microsoft・OpenAI が並ぶ
  - マルチエージェント構成の設計で A2A を採る際に「Google 独自プロトコルへの依存」という論点が消える。⚠️ 一次の `www.linuxfoundation.org` はゲートウェイ拒否で本文に到達できず、公表日が 8/17・8/19・8/20 の3系統に割れているため単日で引用しないこと

### 市場データ・導入事例

- **Warp が自己改善エージェントの二重スキル構成を公開した。** Warp が Claude Platform 上で組んだ枠組みを 8/26 に公表した。内側の base skill が業務固有の指示（コードレビュー等）を持ち、外側の improver skill が定期実行の観測役として人間のフィードバックを分析し base skill への更新案を出す2層構成である。Skills API と Files API でスキルファイルを書き換えるため、エージェントの改善が会話ではなくファイルの版として残る。同社は仕様策定・レビュー・トリアージの各エージェントへ同じループを広げ、数百名の貢献者がいる OSS リポジトリで数千件のレビューに適用している。規模は Warp 内の Claude Code セッションが累計 **1,000万件**・週次40万件超、Warp Agent の会話が累計4,000万件、月間の開発者が80万人である。⚠️ **精度の改善幅・コスト削減率**はいずれも記事に無いため、定量根拠ではなく実装例として使う（https://claude.com/blog/how-warp-builds-self-improving-agents-on-claude ）
- **山形銀行が neoAI Chat の全社利用を 2026年8月から始めた。** Lightblue の法人向け AI エージェント基盤を第21次長期経営計画の DX 戦略に位置づけたもので、当面の用途は行内規程と業務マニュアルの参照にあたる情報検索である。営業店の担当者が融資関連の手続きを確認する際に、規程とマニュアルを即時参照できる形をとる。地銀での全行展開として、あいち銀行・岩手銀行に続く同基盤の採用例になる。⚠️ **利用者数・工数削減率・ROI** はいずれも公表に含まれない（https://neoai.jp/news/article/3rKls-QZ ）
- **AI 電力インフラへ資金が向かった。** 8/26 の資金調達で、AI データセンターを電力網の柔軟な参加者にする Emerald AI が **$150M**（Series A・評価額 $1.05B、Energize Capital と DCVC が共同リード、超過応募）、自動運転トラックの Gatik が $200M を調達した。同日の上位10件の開示合計は $546M 超である。汎用ソフトウェアの層ではなく AI を電力や物流という物理側へつなぐ技術へ投資が寄る構図で、08-18 収録の Nvidia による OpenAI オハイオDC の融資保証（最大 $105B）や 08-25 収録の Alibaba の $10.2B 増資と同じ方向にある。⚠️ 一次の各社発表には到達できず二次報道による
- ⚠️ **Nvidia の FY27 Q2 確報は本日も取得できていない。** 発表は米国時間 8/26 の市場終了後（JST 8/27 早朝）だが、本日時点で検索インデックスに反映されていない。取得可能な範囲では会社ガイダンスが $91.0B（±2%）、コンセンサスが売上 $92.07B・EPS $2.09（前年同期比 約+97%）、Q3 ガイダンスのコンセンサスが $103.8B である。一次の `nvidianews.nvidia.com` / `investor.nvidia.com` / `www.sec.gov` がいずれもゲートウェイ拒否で、IR 開示にも 8-K にも到達経路がない。確報は 8/28 に再取得する
- ⚠️ **Similarweb の7月版は当月の内訳が二次で割れている。** 確定的に引けるのは比較値のほうで、12カ月前が ChatGPT 77.5%・Gemini 9.4%・DeepSeek 4.2%・Grok 3.1%・Copilot 2.0%・Claude 1.9%、6カ月前（2026年1月）が ChatGPT 63.8%・Gemini 22.8%・Grok 4.1%・DeepSeek 3.3%・Claude 2.2% である。7月当月の ChatGPT シェアは **52.7% と 54.8%** の2系統が流通し、片方は同じ 52.7% を5月の値としている。既収録値（2026年5月時点で ChatGPT 53.9%・Gemini 27.9%・Claude 9.2%）とも整合しないため当月値は提案に引かない。方向としては ChatGPT が1年で約77%から50%台前半へ低下し、Gemini が4分の1超、Claude がカテゴリ最速の伸びという構図で一致している
- 市場データ定点は IDC・MM総研・NRC のいずれも新規公表を検知できていない。参照可能な最新値は国内AI市場予測（2025年 2兆3,725億円 → 2029年 6兆8,897億円・CAGR 36.0%）、個人利用経験率 21.8%（2025年8月時点／ChatGPT 65.7%・Gemini 40.0%・Copilot 26.2%）で据え置きである

### 企業・市場

- ⚠️ **08-26 に「桁が3桁違う」として除外した Anthropic の $30兆超は、売上見通しではなく TAM だった。** 本日の検索では「Anthropic が IPO を前に、AI 技術の総アドレス可能市場が $30兆を超えると投資家候補へ伝える見込み」という形で一致する。売上側の確立報道は変わらず7月末の年換算 run-rate **$650億**、投資家の2026年着地見込み $1,000〜1,200億である。⚠️ TAM は自己申告の市場規模推計であり実績値ではない
- ⚠️ 8月の Risk Report（186ページ・RSP v3.4・対象期間 2/24〜7/15）で misalignment リスク評価を「very low」から「low」へ引き上げた件は、`www.anthropic.com` と `www-cdn.anthropic.com` がいずれもオリジン403のため**一次未読のまま**である（初出 08-17・二次一致）
- 既報: SpaceX による Cursor 買収完了（8/14・$60B）、Bain & Company の Global Premier partner 参加（8/25）、OpenAI が9月にも $1T 超で株式売出しとの報道、Manus が Meta から分離（8/12）

### Apple / クラウド

- **Apple が 9/9 10:00 PT の特別イベントを告知した**（8/26）。apple.com / Apple TV / YouTube Live で配信され、iOS 27 / macOS 27 の GA は例年どおりこのイベント後になる見込みである
- 既報: 8/24 の Sign in with Apple 新ドメイン（`private.icloud.com`）は、アカウントシステムとメール検証ロジックの更新が必要である点が変わらない。8/18 の EU 向けビジネス条件変更2本（Core Technology Fee 廃止 → Core Technology Commission 5%／DPLA に Attachment 14）は発効が **2026-10-01** である
- AWS Bedrock への Anthropic モデル追加は 7/24 の Claude Opus 5 が最新のままで、8月の新規提供開始を検出できていない

## 直近の注目予定

- **8/28**: Nvidia FY27 Q2 確報の再取得 ／ OpenAI 退役ページの区分更新の確認
- **8/29 前後**: 拡張機能 What's New・モデル可用性一覧の週次確認
- **8/30**: 公式 DALL·E GPT の退役 ／ PnP・Power CAT の週次確認
- **8/31**: Claude Code の週次上限50%増が終了 ／ GitHub Spark の既存ユーザーアクセス終了 ／ `gemini-robotics-er-1.6-preview` 停止 ／ GPT-5.4・5.4 mini が Codex から除外 ／ Claude for Government の $1/機関プログラム終了 ／ **Power Automate モバイルアプリの廃止** ／ CSP Copilot Partner Council コンテストの応募期限
- **8月末（残り4日）**: Copilot Studio 566997 と PPAC Usage ページの GA 期日 ／ Release Wave の8月期日10件と持ち越し6行 ／ Word の Legal Agent GA〔二次のみ〕 ／ Anthropic が IPO を公開申請する可能性
- **9/1**: GitHub Copilot の全体験でモデル廃止 ／ MAICPP 契約の更新条項が自動発効 ／ OpenAI Daybreak でハードウェアセキュリティキー必須化 ／ Released Versions の次回定例日
- **9/2・9/3**: Windows 365 Frontline 名称での購入最終日 ／ Windows 365 Flex へ改称
- **9/4**: WebMCP Challenge の提出締切
- **9/9**: Apple 特別イベント（10:00 PT）／ GLM-5.3-Flash の 50%割引が終了
- **9/10**: MAI-Code-1-Flash が全 Copilot 体験から廃止
- **9/17**: OpenAI DevDay Exchange の応募締切
- **9/23**: WebMCP Challenge の受賞発表
- **9/24**: OpenAI の Videos API と Sora 2 動画生成モデルが退役（代替モデルの提示なし）
- **9/28**: 旧 GPT スナップショット4種が退役（`gpt-3.5-turbo-instruct` / `babbage-002` / `davinci-002` / `gpt-3.5-turbo-1106`・代替は `gpt-5.6-terra`）
- **9/29 以降**: `claude-sonnet-4-5-20250929` の暫定退役日（確定日ではない）
- **9月**: AI at Work roadmap への掲載開始と Release Plans on Learn の新規掲載停止 ／ Outlook と Teams のチャット中心 UI と Work IQ コントロールが既定で有効化 ／ Copilot Tuning の新体験が Public Preview ／ Copilot メモリの Purview 保持（569612）／ Federated Copilot Connectors（569212）／ Power BI レポートの Notebooks 参照（569928）／ iOS 27 / macOS 27 GA ／ ChatGPT Ads Manager のセルフサービス提供
- **9月中旬 / 9月末 / 9/30**: Copilot デスクトップアプリの広範な展開開始 ／ 2026 Wave 1 の対象期間終了 ／ M365 E7 プロモーションの対象購入最終日・M365 E5 / E3 の CSP 割引終了
- **10/1**: Apple の EU 向け新ビジネス条件が発効 ／ CSP ソフトウェアの5%上乗せ発効 ／ **CSP growth margins の本番提供開始** ／ M365 E7 プロモーションの新規取引停止 ／ Ask Gemini in Chat のプロモーション上限が終了
- **10/15 以降**: `claude-haiku-4-5-20251001` の暫定退役日（確定日ではない）
- **10/16–11/11**: OpenAI DevDay Exchange 8都市（**東京は 10/20**）／ **10/20〜22**: SMB Copilot Partner Council イベント（NYC）／ **10/25〜30**: PPCC 2026
- **10/23**: OpenAI のレガシースナップショット12種とファインチューン版5種が退役
- **10月**: Anthropic の IPO 予定（$2T 超の評価額を目標と報道）
- **11/1**: パートナー特典の有効期限がオファー購入日基準へ移行
- **11/15**: Release Planner の退役と AI at Work roadmap への移行完了
- **11/21**: GPT-5.6 Sol の暫定値下げが有効とされる期限
- **11/24 以降**: `claude-opus-4-5-20251101` の暫定退役日（確定日ではない）
- **11/30**: OpenAI Evals プラットフォーム・Agent Builder・`v1/prompts` が退役
- **12/1**: OpenAI の GPT Image 系が退役
- **12/2**: EU AI Act の生成コンテンツ標識義務の猶予終了
- **12/11**: `gpt-5-2025-08-07` 系と `o3-2025-04-16` / `o3-pro-2025-06-10` が退役
- **12/31**: Gemini 3.7 Flash の導入価格終了（$0.75/$3.75 → $1.50/$7.50）／ Copilot in 30・M365 E3 プロモーション・Purview Suite 50%オフの提供終了
- **12月**: Copilot Tuning の新体験が GA
- **2027/1/6**: OpenAI のファインチューニング新規ジョブ作成が全面終了
- **2027/1/20**: OpenAI の旧 audio / realtime / transcription 系が退役
- **2027年6月末**: Frontier Partner バッジの廃止

## 改善メモ

- **本サマリーの 08-26 分に誤りがあった**: 「Cowork の画像生成が Imagen 2 から ChatGPT Images 2.0 に変わった」と書いたが、Cowork What's New の GA 節は当初から ChatGPT Images 2.0 と明記している。変わったのは `cowork-models` 側の記述で、同ページは現在いずれの画像モデルにも触れていない。Release Notes だけを根拠に「変更」と判定した点が原因である
- **Copilot 一次どうしの矛盾が2件目になった**: `cowork-models` が Sonnet+Opus Advisor を削除した一方、`cowork-admin-governance` は現行として残している。8/26 に記録した Work IQ ボタン（B-044）と同じ形の食い違いで、いずれも第3の一次で決着させる手段がない
- **A2A / AAIF は 08-26 の「未確定」から確定へ移った**: industry が二次2系統（Forbes・Axios）で確認した。⚠️ 公表日が 8/17・8/19・8/20 の3系統に割れており、一次の `www.linuxfoundation.org` はゲートウェイ拒否のため単日での引用はできない
- **Copilot B-048 起票**: Cowork の一次ページ群（`cowork-models` / `cowork/whats-new` / `cowork-admin-governance`）が `daily-sources.md` 未登録で、8/25 のモデル入れ替えと7月の event-driven tasks を検知できなかった
- **Master B-046 / B-047 起票**: HF のオープンウェイト検出で `createdAt` 降順だけでなく `lastModified` 降順も併用する提案（本日の Qwen / GLM 2本が作成日と公開日のズレで漏れかけた）と、`platform.claude.com` のモデル退役ページを `daily-sources.md` に登録する提案である
- **一次未読のまま採用した項目**: Anthropic の8月 Risk Report（`www.anthropic.com` オリジン403）、Anthropic の TAM $30兆超（同）、Devin Coach（`docs.devin.ai` 拒否）、A2A の AAIF 移管（`www.linuxfoundation.org` 拒否）、Warp / 山形銀行 / Emerald AI の各事例
- **未確定として保留した項目**: Nvidia FY27 Q2 の確報値（IR 経路が全滅）、Similarweb 7月当月のシェア（二次で2系統に割れる）、Codex CLI `0.150.0-alpha.10`〜`.13` の変更内容（本文が空）、Claude Code v2.1.247（npm 先行・changelog 未掲載）
- **障害の変化**: Master が `qwen.ai` を新規のゲートウェイ拒否として登録した。industry は企業の一次財務開示に到達する経路が全滅し、`nvidianews.nvidia.com`・`investor.nvidia.com`・`www.sec.gov`・`www.kiplinger.com` の4ドメインと、`www.linuxfoundation.org`・`www.techzine.eu`・`ppc.land`・`www.similarweb.com` の4ドメインを新規登録した（`www.similarweb.com` は「高優先」の登録ソース）。Copilot は M365 Blog 本体のオリジン 403 が再発し、B-020 が要求する二重確認が本日は成立していない
- 継続提案は Master 26件（最多: B-013 403の2分類記録・30回目）、Copilot 36件（最多: B-011 Power Platform Blog のトピック記事照合・38回目）、industry 5件（最多: B-004 取得方法欄の WebSearch 優先化・59回目）
