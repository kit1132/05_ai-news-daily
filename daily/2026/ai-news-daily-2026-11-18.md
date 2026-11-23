# AI News Daily Summary — 2026-11-18

Ignite 初日に GitHub が VS Code の Copilot の Local harness を2027年2月に削除すると告げ、MAI-Code-1.1-Flash を 12/18 に外す。OpenAI は GPT-6.2 Astra / Sol を出し、Astra の単価を2割下げたが、既存のパラメータの一部は使えなくなる。Cowork の利用可否は支出ポリシーだけで決まるようになった。

## 今日のハイライト

### 1. [廃止+予定] VS Code の Copilot が Local harness を2027年2月に削除し、MAI-Code-1.1-Flash は 12/18 に消える — 旧ハーネスに戻す例外設定も一緒に消え、移行を先送りする手段がなくなった

**要点**: GitHub が 11/16、VS Code の Copilot エージェントを動かす旧来の Local harness を VS Code 1.146 で非推奨にし、2027年2月に削除すると告げた。管理者が旧ハーネスを既定に戻す例外設定 `vscode.temporaryDefaultToLocalHarness` も同時に廃止される。11/17 には MAI-Code-1.1-Flash を 12/18 に全 Copilot から外すと告知した。

**詳細**: github.blog の changelog で一次確認した（Master）。
- Local harness: エディタ内のエージェントセッションでモデル・コンテキスト・ツールをつなぐ旧実装。後継の Copilot harness（Copilot SDK ベース）は VS Code 1.143 から新規セッションの既定で、移行期間の3か月は組織ポリシーが許す範囲で旧実装が残る
- 利用者: 新しいセッションの Session Target で「Copilot」を選ぶ。カスタマイズはすべて自動変換されるわけではない
- 管理者: 例外設定を残しても旧ハーネスは保てない。権限制御とサンドボックス設定が Copilot harness で効くかが2月までの確認点になる
- MAI-Code-1.1-Flash: 後継は同日発表の最新 MAI Code Flash。Enterprise では後継モデルのポリシーを有効にする必要がある
- 発効済み（11/16）: Claude Opus 4.8 / Opus 5 / GPT-5.6 Terra が Copilot の大半の画面から外れた（既報の予定どおり）。Opus 4.8 は年額プランの個人契約者に残り、Opus 5 は拒否時のフォールバック先としては使われる

出典:
- https://github.blog/changelog/2026-11-16-vs-code-retires-the-local-harness-in-february-2027
- https://github.blog/changelog/2026-11-17-upcoming-deprecation-of-mai-code-1-1-flash-in-december
- https://github.blog/changelog/2026-11-16-github-copilot-models-deprecated-on-november-16-2026

### 2. [破壊的変更+料金] OpenAI が GPT-6.2 Astra / Sol を出し、Astra の単価を2割下げた — 上位モデルの基準単価は $8/$40 に変わったが、`temperature` などを送る既存コードはそのままでは動かない

**要点**: OpenAI が 11/17 に `gpt-6.2-astra` と `gpt-6.2-sol` を API で公開し、ChatGPT Work と Codex（Plus / Pro / Enterprise / Edu）にも載せた。Astra は GPT-6 Astra の $10/$50 から $8/$40 に下がった。一方で移行ガイドは `temperature` / `top_p` / logprobs 系を外すよう求め、ツール呼び出しは Responses API でしか使えない。

**詳細**: developers.openai.com の changelog・料金ページ・移行ガイドで一次確認した（Master・industry）。単価は100万トークンあたり。
- 単価（Standard）: Astra は入力 $8・キャッシュ $0.40（GPT-6 Astra は $1.00）・出力 $40、Sol は $2 / $0.10 / $10 で GPT-6.1 Sol と同額。入力 **272K トークン超**は Astra $16 / $60、Sol $4 / $15。Batch・Flex は半額
- API の移行点:
  - パラメータ: Chat Completions は `temperature`・`top_p`・`logprobs`・`top_logprobs` を外す。Responses は `temperature`・`top_p`・`top_logprobs` を外し、`include` から `message.output_text.logprobs` を除く
  - ツール呼び出し: Chat Completions では使えない（モデル自体は Chat Completions に対応）
  - キャッシュ: GPT-5.5 以前から移るときは `prompt_cache_retention` を `prompt_cache_options.ttl: "30m"` に置き換える。推論の深さ `none` / `minimal` は `low` に上げるよう勧めている
- 同日の API 追加: Responses API の background completion window（2時間・8時間）が公開ベータになり、Standard 比で30%・40%安い。対象は 6.2 の2モデルと `gpt-6.1-terra`・`gpt-6-luna`
- Ultrafast: API では 2027-02-28 まで Standard の3倍、2027-03-01 から6倍。ChatGPT・Codex では Pro $500 で両モデル、Pro $200 は今回はじめて Sol だけで使える
- system card: Preparedness の分類は両モデルともサイバーが **Critical**、生物・化学が High。自己改善は Astra だけ High で、OpenAI が外部に出したモデルで初めて（Unite.ai）。ExploitBench Internal Port は Astra 53.5%（GPT-6 Astra 31.5%）

出典:
- https://developers.openai.com/api/docs/changelog
- https://developers.openai.com/api/docs/guides/latest-model
- https://developers.openai.com/api/docs/pricing
- https://community.openai.com/t/gpt-6-2-astra-and-sol-are-now-available/1417531
- https://deploymentsafety.openai.com/gpt-6-2-astra-sol

### 3. [破壊的変更] Cowork の利用可否は支出ポリシーだけで決まるようになった — プレビュー期にエージェント一覧で作った許可リストは、もう誰も止めていない

**要点**: M365 管理センターの「Agents > All Agents > Cowork」でユーザーを許可・ブロックする方式が、アクセス制御としては廃止になった。設定画面は残るが効かない。Cowork を使えるのは、Cowork を選んだ支出ポリシーの範囲に入るユーザーだけになる。

**詳細**: `cowork-admin-governance`（11/17 改訂・`76ffc707`）で一次確認した（Copilot）。11/16 の実装ガイダンスで「ポリシーの範囲で絞る」と書かれた件が、管理者統制のページで旧方式の無効化として明文化された。
- 移行手順: 旧許可リストのユーザーを Entra ID のセキュリティグループにまとめ、Copilot > Cost Management > Configuration で支出ポリシーを作り、スコープにそのグループ、サービスに Cowork を選ぶ
- アクセスを外すとき: Cowork を含む支出ポリシーのすべてからユーザーを外す。クレジット上限を低くしてもアクセスは止まらない
- モデル統制との関係: Anthropic モデルファミリーをオフにしても Cowork のアクセスは変わらず、Auto は残りのモデルから選ぶ

出典:
- https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-admin-governance

## カテゴリ別まとめ

### Anthropic / Claude

- [破壊的変更+セキュリティ] **Claude Code `2.1.326`** — Anthropic が Claude Code `2.1.326` を changelog に載せ、npm の `latest` にした。組織ポリシーを読み込む前のターミナル / VS Code セッションは、モードの指定がなければ Manual ではなく auto mode で始まる。HIPAA 構成（Claude Code + Cowork）の組織も auto が既定になり、`disableAutoMode` で止められる。設定もポリシーも取れなければ Manual に落ちる（Master・industry）
  - サンドボックス: macOS / Linux / WSL でホーム配下の機密フォルダに書けなくなり（`sandbox.filesystem.allowWrite` で許可）、`.credentials.json` などの認証ファイルへの書き込みを拒否する
  - フック: `"decision": "block"` が効く場面が増え、常に block を返すフックは呼び出しを止め始めることがある。bypass permissions でも一部の呼び出しは承認を求める
  - 管理設定: `autoMode.environment` に `"$defaults"` を入れないと、Claude Desktop と Agent SDK でも組み込みの項目がすべて置き換わる。`OTEL_RESOURCE_INCLUDE_HOST`（既定オフ）も加わった。全体は Added 11・Fixed 233・Changed 62・Removed 2 件
  - npm: `stable` は `2.1.311` のまま
  - https://code.claude.com/docs/en/changelog
- [新機能] **Linked billing（ベータ）** — Anthropic が Claude Platform で Linked billing をベータで出した（11/17）。顧客が自分の Claude 組織をアプリにつなぐと、アプリ開発者は `/v1/messages` などのリクエストごとに `billing_policy` で支払う側を選べる。顧客は Console でアプリの支出上限の設定と連携の解除ができる。対象は API 利用を Anthropic に直接支払う組織で、ベータヘッダーは `user-profiles-billing-2026-10-01`（Master・industry）
  - https://platform.claude.com/docs/en/release-notes/overview#linked-billing
  - https://claude.com/resources/articles/linked-billing-on-claude-platform
- [仕様] **旧モデル出力の透かし** — Master も release notes で、Opus 4.6 / Opus 4.5 / Sonnet 4.5 / Haiku 4.5 の生成テキストに対応プラットフォームで透かしが入るという 11/16 付の記載を確認した。前日に industry 経由で収録した件で、前日の両ソースの食い違いは解消した（Master）
  - https://platform.claude.com/docs/en/release-notes/overview#text-watermark-claude-opus-4-6-and-4-5-models
- [据え置き] **Anthropic のその他の一次** — モデル退役一覧（Active 17件）と廃止履歴（9/30）は動いておらず、Opus 4.5 の下限日 11/24 の確定告知もない。`/news`（11/10）、`/research`（11/16）、`support.claude.com`（11/12）、Privacy Center（11/9）も変わらない（Master・industry）
  - https://platform.claude.com/docs/en/about-claude/model-deprecations

### OpenAI / Codex / ChatGPT

- **GPT-6.2 Astra / Sol**（ハイライト2参照）
- [動向] **オレゴン州による OpenAI 提訴** — Rayfield 司法長官が 11/17 にマルトノマ郡の巡回裁判所へ OpenAI を訴え、$20.35億を求めた。ChatGPT は依存と迎合的な回答を促すよう作られ、子どもを自傷や摂食障害へ向かわせうるのに安全だと偽ったとして、不公正取引慣行法違反・過失・不当利得・公的不法妨害を主張している。前日のカリフォルニア州の提訴（エージェントの暴走）とは別件で、OpenAI は反論の声明を出した（industry）
  - https://www.doj.state.or.us/media-home/news-media-releases/ag-rayfield-files-2b-lawsuit-against-open-ai-launches-keeping-kids-safe-initiative/
- [動向] **Daybreak の NATO・欧州政府への開放** — The Decoder（11/17）によると、OpenAI がセキュリティ向けの Daybreak を NATO とドイツ・フランス・ポーランドなどの政府に開放した。EU の ENISA は既に EU のソフトウェアの実際の脆弱性を見つけている（industry）
  - https://the-decoder.com/openai-opens-its-cybersecurity-tool-daybreak-to-nato-and-european-governments/
- [動向] **医療事務のエージェント自動化** — The Decoder（11/17）によると、CVS Health と Cigna が OpenAI の GPT-6 Astra / Luna に既存の診療所ソフトや保険会社のポータルを操作させ、事務作業の自動化を始めた。Luna は保険の事前承認を1件約8.5セントで処理する（industry）
  - https://the-decoder.com/ai-agents-are-starting-to-fill-out-medical-forms-and-file-insurance-requests-in-place-of-human-staff/
- [観測] **GPT-5.6 Sol の期間限定価格の終了日** — OpenAI の一次どうしで記載が割れている。changelog は「少なくとも11/21まで」、料金ページは「11/30まで」としている（industry）
  - https://developers.openai.com/api/docs/pricing
- [版更新] **Codex CLI `0.171.0-alpha.12`** — OpenAI の Codex CLI の pre-release が 11/17 に `0.171.0-alpha.12` まで進み、`0.170.0-alpha.4.1` も出た。安定版は `0.169.0`（11/13）のまま（Master）
  - https://github.com/openai/codex/releases
- [据え置き] **OpenAI のその他の一次** — deprecations の最新告知は 11/10 の GPT Image 2 のままで、Upcoming 表の直近停止も 12/1 と 12/11 から変わらない。misalignment reports（First posted 11/12）も動いていない（Master・industry）

### GitHub Copilot / GitHub

- **Local harness の削除と MAI-Code-1.1-Flash の廃止**（ハイライト1参照）
- [料金+新機能] **MAI Code 2 / MAI Code 2 Flash** — Microsoft の新しいコーディングモデル2つを、GitHub が Copilot で一般提供した（11/17）。VS Code・CLI・cloud agent・JetBrains・Xcode など全画面で使え、従量課金に計上される。Business / Enterprise では新モデルを自動で有効にする設定のままだと使える状態になり、止めるにはモデルポリシーで個別に無効にする（Master・industry）
  - MAI Code 2: 入力 $0.50・キャッシュ $0.025・出力 $2.50（100万トークン）。2027-05-17 から $1.00 / $0.05 / $5.00 に倍増する。Pro 以上が対象
  - MAI Code 2 Flash: 入力 $0.05・キャッシュ $0.005・出力 $0.25。2027-05-17 から入力 $0.10・キャッシュ $0.01。Free / Student を含む全プランが対象
  - Microsoft は MAI Code 2 が GPT-6.1 Sol のコーディング性能の98%を40%の価格で出すと説明した（二次。40%は導入価格での比較）
  - https://github.blog/changelog/2026-11-17-mai-code-2-and-mai-code-2-flash-in-github-copilot
  - https://docs.github.com/en/copilot/reference/copilot-billing/models-and-pricing
- [新機能] **Copilot の管理・監査機能** — GitHub が Ignite に合わせて企業向けの制御を足した（11/16–11/17）（Master・industry）
  - `strictPluginOnlyCustomization`: Enterprise 管理者が、ユーザー・プロジェクト由来の単独のスキル・カスタムエージェント・フック・MCP サーバーを止め、プラグインと管理設定経由だけを許せる
  - Copilot CLI `v1.0.113`: 管理設定 `features.browserUse` で組み込みのブラウザ操作を止められ、実行中のセッションにも効く。Microsoft Entra サインインも public preview になった
  - Microsoft Agent 365 連携: Copilot の各クライアントのエージェント操作を監査データとして Agent 365 へ流せる
  - https://github.blog/changelog/2026-11-16-control-where-github-copilot-customizations-come-from
  - https://github.blog/changelog/2026-11-17-github-copilot-cli-adds-microsoft-entra-sign-in-as-a-preview
  - https://github.blog/changelog/2026-11-17-monitor-github-copilot-activity-through-microsoft-agent-365
- [新機能] **Copilot アプリ・code review・Evals・Fusion** — GitHub が Ignite 版をまとめて出した（11/17）（Master・industry）
  - Copilot アプリ: GitHub Enterprise Server が GA（アプリ 1.2.0 以降）、Azure DevOps リポジトリとブラウザ操作は public preview。GHES と Azure DevOps ではクラウドセッションを使えない
  - code review: PR ごとに深さを変える Adaptive とシークレット検出が加わり、リポジトリの Insights に集計ページができた
  - Copilot Evals: プロンプト・モデル・スキルの組み合わせを自分で評価する機能が public preview になった
  - Copilot Fusion: Standard に MAI-Code-2、Max に Claude Sonnet 5.5、High に GPT-6.1 Terra が加わった
  - https://github.blog/changelog/2026-11-17-github-copilot-app-microsoft-ignite-releases
  - https://github.blog/changelog/2026-11-17-copilot-code-review-adaptive-effort-secret-detection-and-more
  - https://github.blog/changelog/2026-11-17-github-copilot-fusion-updates-more-availability-benchmarks-and-models
- [新機能] **VS Code 1.146 の Copilot（11/9 週のまとめ）** — GitHub が、エージェントにモデル比較を走らせる機能（実験）、注意が要るセッションを先に並べる Inbox モード（実験）、チャットの別ウィンドウ化（preview）を入れたとまとめた（Master）
  - https://github.blog/changelog/2026-11-16-github-copilot-weekly-releases-november-9
- [セキュリティ] **Windows 11 のコーディングエージェント遠隔測定** — GIGAZINE（11/17）によると、開発者の Shu Sheng Li 氏が、Windows 11 の診断データに Claude Code や Codex など AI コーディングエージェントの使用状況が含まれていると報告した。収集項目と止め方、Microsoft の説明は確認できていない（industry）
  - https://gigazine.net/news/20261117-windows-coding-agent-telemetry/

### Microsoft 365 Copilot

- **Cowork のアクセス制御の一本化**（ハイライト3参照）
- [廃止+新機能] **Cowork のモデル表** — Microsoft が Cowork のモデル選択から GPT 5.5 を外し、Microsoft がホストする GPT 6.1 Sol を後継にした。Claude Fable 5.2 は一部の顧客向けに Fable 5.1 を置き換え、Fable 5.2 だけゼロデータ保持の対象外になる。Opus 5.5 には Fast オプションが付き、選択肢は Auto＋8モデルになった。GPT 6.1 Sol は OpenAI をサブプロセッサーとして無効にしたテナントでも使える（Copilot）
  - https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-models
- [新機能] **Home と Office in Copilot の GA** — Microsoft が Ignite で、Chat と Cowork を1つの入力欄にまとめた Home の全世界展開を始め、Word / Excel / PowerPoint をアプリ内で直接編集できる Office in Copilot を GA にした（11/17）。作ったファイルは OneDrive に保存され、秘密度ラベルなどの統制を引き継ぎ、追加課金はない。Copilot Managed Runtime も GA になった（Copilot）
  - Frontier: 自分の Entra Agent ID と管理者を持つ常駐エージェント Autopilot、Copilot Code（GA は12月予定）、Workspaces
  - Today: 朝の Today Brief は Copilot ライセンスに含まれ、日中の Today Feed は Copilot Credits を消費する（Frontier のプライベートプレビュー）
  - https://www.microsoft.com/en-us/copilot/blog/2026/11/17/copilot-at-microsoft-ignite-expanding-whats-possible-with-intelligence-built-for-work/
  - https://news.microsoft.com/events/ignite/2026/book-of-news/
- [新機能] **Dynamics 365 と Salesforce のプラグイン** — Microsoft が Dynamics 365 Sales と ERP apps のプラグインを GA にし、利用者が Copilot と Cowork から CRM・ERP の作業をできるようにした。Salesforce in Copilot（38以上の営業スキル）はプレビューで、Salesforce の既存権限の範囲で MCP 経由で操作する（Copilot）
  - https://news.microsoft.com/events/ignite/2026/book-of-news/
- [新機能] **Work IQ の人・組織コンテキスト** — 利用者が、自社の人事・組織データと用語定義に基づく組織の質問への回答を Copilot から得られるようになる。計算を伴う分析と Cowork の Workforce Intelligence プラグインは Frontier で、展開は12月まで続く。Work IQ の取得・メモリ・コンテンツ作成は GA になった（Copilot）
  - https://techcommunity.microsoft.com/t5/microsoft-copilot-blog/copilot-that-understands-your-organization-introducing-people/ba-p/4573356
- [新機能] **Teams のデジタルチームメイト** — 開発者が Teams のエージェントに自分の Entra アカウントを持たせ（Agentic Users）、同僚のように @メンションさせられるようになった。操作は Agent 365 で個々のツール呼び出しまで確認できる。スレッド返信・HTML ウィジェット・Socket mode などはパブリックプレビュー（Copilot）
  - https://devblogs.microsoft.com/microsoft365dev/new-capabilities-for-building-digital-teammates-in-microsoft-teams/
- [予定] **PowerPoint のプラグインと Learning Agent** — Microsoft が、PowerPoint の Copilot から許可済みプラグインのスキルとコネクタを使える機能を11月下旬に GA で展開すると告知した（MC1556104）。Learning Agent は Teams のチャット・メール・会議の文字起こしから個人向けの学習プロンプトを出す機能を、12月中旬から下旬に GA にする（MC1556094）（Copilot）
  - https://mc.merill.net/message/MC1556104
  - https://mc.merill.net/message/MC1556094
- [仕様] **リリース設定の統合** — 管理者は Standard / Deferred / Frontier の設定を、M365 管理センターの Release preferences の1画面で管理するようになる（MC1556082・11月末まで）。既存の設定は引き継がれ、Targeted Release は表示されるが変更も新規登録もできない（Copilot）
  - https://mc.merill.net/message/MC1556082
- [据え置き] **M365 Copilot のその他の一次** — Release Notes（先頭 November 4, 2026）は改訂されておらず、拡張機能 What's New は改訂されたが節の項目は変わっていない。SharePoint Blog（先頭 11/4）と Agent 365 Blog（先頭 11/10）に新しい記事はない（Copilot）
  - https://learn.microsoft.com/en-us/microsoft-365/copilot/release-notes

### Copilot Studio / Power Platform / ガバナンス

- [新機能] **Copilot Studio の Fable 5.2 GA** — Microsoft が Copilot Studio の Microsoft Copilot ハーネスのモデル表に Claude Fable 5.2 を GA として載せた（11/17）。11/11 に告知だけだった件が表に入った。Fable 5.1 は残っている（Copilot）
  - https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-experience/authoring-agent-model-availability
- [仕様] **Copilot Studio のハーネスは3種類** — Microsoft が `harnesses-overview` を、Microsoft Copilot・Customer Conversation・標準の3ハーネスの比較表に書き換えた（11/17）。課金ページも同時に改訂されたが、レート表の値の変化は見当たらない（Copilot）
  - https://learn.microsoft.com/en-us/microsoft-copilot-studio/harnesses-overview
- [新機能] **モデル移行の評価手順** — 作成者が Copilot Agent Kit のモデル評価機能（プレビュー）でモデルを比べ、回帰を見つけてから本番の移行を判断できるようになった。ガイダンスハブの November 節に記事が加わった（Copilot）
  - https://learn.microsoft.com/en-us/microsoft-copilot-studio/guidance/whats-new
- [料金] **Agent 365 の利用状況の無償化** — 管理者が Agent 365 ライセンスなしで、Microsoft 製と Microsoft 基盤で作ったエージェントの利用状況を管理センターで見られるようになった（GA）。Viva Insights のエージェント分析も Agent 365 ライセンスが不要になる。他社製エージェントの詳細と Defender・Purview の統制には引き続き Agent 365 か ME7 が要る（Copilot）
  - https://news.microsoft.com/events/ignite/2026/book-of-news/
- [新機能] **Agent 365 のコスト管理と統制** — 管理者が Cowork・Code・Copilot Studio・Managed Runtime・Autopilot・Work IQ API の従量課金を Agent 365 Cost Management でまとめて管理できるようになった（プレビュー）。プラグインとスキルのユーザー・グループ単位の割り当ては GA、放置エージェントを洗い出すアクションセンターは12月にプライベートプレビューの予定（Copilot）
  - https://news.microsoft.com/events/ignite/2026/book-of-news/
- [予定] **Purview の Copilot 向け DLP の強化** — Microsoft が、ラベルのないファイルでも機微情報を含めば Copilot の参照を止める DLP と、添付・リンク先を含むプロンプトの保護をプレビューで発表した。Windows 上のローカルエージェントへの DLP は Roadmap 577862（March CY2027）に載った（Copilot）
  - https://news.microsoft.com/events/ignite/2026/book-of-news/
- [予定] **Roadmap の Ignite 関連の起票** — Microsoft が Roadmap に Cowork でのモデル駆動型アプリ作成（579979・January CY2027）、Copilot Code（571887・December CY2026）などを起票し、API の総項目数は 2,310 から 2,363 になった。Copilot Studio のエージェントノード 562222 は `Launched` になった（Copilot）
  - https://www.microsoft.com/releasecommunications/api/v1/m365
- [据え置き] **Copilot Studio と Power Platform のその他の一次** — Copilot Studio What's New、課金3本、PPAC の容量管理、非推奨一覧、Partner Center 11月ページは前日のまま。Copilot ブログ・Power Platform Blog・Copilot Studio Blog に Ignite の記事はまだない（Copilot）
  - https://learn.microsoft.com/en-us/microsoft-copilot-studio/whats-new
- [動向] **Qiita の実務記事** — 日本の実務者が、Copilot Studio のエージェントを Teams に展開しても表示されないときに管理者が確認する3か所を整理した（11/17）（Copilot）
  - https://qiita.com/Sidejob/items/593cbb84207ec2e65838

### Google

- [新機能] **Tasks in Gemini の無料化** — Google が Gemini アプリの Tasks（複数手順の作業や定期ルーチンを代行する機能）を米国・インド・カナダ・オーストラリア・日本・韓国で無料にし、Hydrogen 4 で動かすと発表した（11/17）。米国では予算上限つきの Google Pay 購入代行と、メッセージアプリからのタスク指示も始まった（Master）
  - https://gemini.google/release-notes/
  - https://blog.google/innovation-and-ai/products/gemini-app/tasks-in-gemini-free-new-features/
- [新機能] **Gemini アプリのスキル共有** — 利用者が Gemini アプリのスキルを閲覧 / 編集の権限つきで他人に共有でき、Drive・Gemini Notebook・Google フォトのファイルを添付できるようになった（11/16）（Master）
  - http://workspaceupdates.googleblog.com/2026/11/share-skills-add-files-from-Drive-Notebook-Photos-to-skills-Gemini-app.html
- [観測] **Gemini API の Live / TTS preview 停止** — 11/17 に停止予定だった preview が止まったかは、Gemini API changelog の転送先 `aistudio.google.com` に届かず、WebSearch でも 10/27 より新しい項目が出ないため一次で確かめられない（Master・industry）
  - https://ai.google.dev/gemini-api/docs/deprecations

### Cursor / Devin / その他エージェント

- [新機能] **Devin の 11/16 リリース** — Cognition が Devin のセキュリティ設定にプラグイン・スキャン対象パス・除外 glob・脅威モデルのルール指定を加え、指摘一覧の CSV 書き出しを足した。Phonebook は各メンバーの Devin・Slack・Teams・git・Jira・Linear の ID をつなぐ（Master）
  - https://docs.devin.ai/release-notes/overview
- [据え置き] **その他の開発ツール** — Cursor の changelog（11/6）とフォーラム（10/12）、xAI（`grok-4.7`）、Orca（`v1.4.261`）、TypeSafe AI（`jev-1.14.0`）、MCP blog（11/11）、Hugging Face の8 org、Obsidian（1.15.1）は動いていない。Apple Developer News の 11/16 の記事は AI と関係がない（Master・industry）

### 市場・企業・導入事例

- [新機能] **NTTデータの COBOL 刷新サービス** — NTTデータが 11/17、生成 AI で既存のプログラムと設計書から業務仕様を復元し、COBOL の基幹システムを Java で設計し直す「クリーンモダナイゼーション」を始めた。開発工期は人手比で約4割短く、刷新後の保守工数は約5割減ると同社は試算する。販売目標は2027〜2029年度の累計500億円（industry）
  - https://www.nttdata.com/global/ja/news/release/2026/111700/
- [動向] **Isomorphic Labs の $50億調達** — The Decoder（11/17）によると、Alphabet 傘下の Isomorphic Labs が6か月前の $21億に続いて $50億を調達し、創薬パイプラインを臨床試験へ進める資金に充てる。承認された薬はまだない（industry）
  - https://the-decoder.com/isomorphic-labs-raises-5-billion-in-its-second-mega-round-within-six-months/
- [据え置き] **未決の案件と国内調査** — Anthropic の IPO は米国時間 11/18 の価格決定待ちで、仮条件（$70〜78）の変更は報じられていない。Amazon × Decart、Nvidia × Reflection AI の買収協議に続報はなく、IDC Japan・MM総研・NRC の新しい公表もなかった（industry）

## 直近の注目予定

- **11/18（本日・米国時間）**: Anthropic の IPO 価格決定（11/19 Nasdaq 取引開始の見込み・報道） ／ MODS の Workforce Insights エンドポイント退役（MC1542066） ／ Microsoft Ignite（〜11/20）
- **11/19**: Claude Enterprise で Claude Data が既定でオン
- **11/20**: Conductor のクラウド版が終了（二次） ／ Copilot Studio のコスト管理を M365 管理センターへ移す機能が GA（MC1530368）
- **11/21〜30**: GPT-5.6 Sol の期間限定価格が終了（一次どうしで日付が割れる）
- **11/24 以降**: `claude-opus-4-5-20251101` の暫定退役日（確定日ではない）
- **11月下旬**: PowerPoint の Copilot のプラグインが GA の展開に入る（MC1556104）
- **11/29**: OpenAI が Daybreak Blue のセッションデータの学習利用を開始（二次）
- **11月中**: GitHub の cloud sandbox の課金開始（日付明記なし）
- **11月末**: M365 管理センターのリリース設定の統合が完了（MC1556082）
- **11/30**: `claude-sonnet-4-5-20250929` 退役 ／ Opus 4.8 の fast mode 削除 ／ OpenAI の Evals・`v1/prompts`・Agent Builder 停止 ／ Gemini 4 Argon の導入価格終了 ／ Power Platform のアプリ説明の AI 生成・Power Automate デザイナーの Copilot などが終了（MC1540258）、Describe it to design it と vibe.powerapps.com が退役
- **12/1**: OpenAI `gpt-image-1-mini` / `gpt-image-1.5` / `chatgpt-image-latest` 停止 ／ Gemini 4 Argon の単価が $4/$20 に倍増 ／ Google スライドの複数スライド作成の上限引き上げ優待が終了しうる
- **12/2**: GitHub が公開リポジトリの `pull_request_target` を既定でブロック ／ Power Platform のプロンプトから Anthropic・Grok・旧 GPT 系モデルが退役（MC1536101）
- **12月**: Copilot Code が GA ／ Agent 365 のアクションセンターがプライベートプレビュー
- **12月上旬**: Dataverse のストレージ検証の確定日程を告知（MC1483529）
- **12/8**: GitHub が非活動リポジトリの Dependabot アラートを停止、ホステッドランナーの ARM32 終了 ／ M365 Copilot in Power BI が既定でオン（MC1546429）
- **12/9**: EU / EFTA で Claude モデルが既定で有効に（MC1546438）
- **12/11**: OpenAI `gpt-5` / `gpt-5-mini` / `gpt-5-nano` / `gpt-5-pro` / `o3` / `o3-pro` 停止 ／ Power Apps の式の生成・Power Apps Ideas などが退役（MC1532421・MC1532426）
- **12/14**: Copilot から Claude Fable 5 / Haiku 4.5 / Gemini 3.8 Flash / Gemini 4 Argon / Grok 4.6 / Kimi K3 を廃止 ／ claude.ai/design の単体サイトが閉鎖
- **12月中旬**: Copilot Pages と Notebooks の OneDrive 保存の展開完了（MC1449182） ／ Learning Agent の GA 展開（MC1556094）
- **12/18**: Copilot から MAI-Code-1.1-Flash を廃止（→ 最新の MAI Code Flash）
- **12月中（日付未公表）**: ChatGPT と Codex の利用枠が Plus・Pro・Business で統合（二次）
- **12/31**: Claude Security の無償クレジット期間終了 ／ Copilot の Fable 5 系の ZDR 例外終了 ／ MCP File Uploads 拡張の安定版目標 ／ Power Platform 版のスケジュール済みプロンプト退役（MC1550533） ／ Copilot Studio の会話内での接続設定が GA（MC1548034）
- **2027-01-01**: Anthropic の新しい開示期限（高・重大度30日）を適用 ／ Commercial Cloud の現地通貨価格を5通貨で改定（日本円は対象外）
- **2027年1月以降**: Dataverse のみのテナントでストレージ検証開始（MC1483529）
- **2027-01-06**: OpenAI `tts-1` / `tts-1-hd` / `gpt-4o-mini-tts` 2版が停止
- **2027-01-14**: OpenAI `gpt-4o` 2版 / `gpt-4o-mini` / `gpt-4.1` / `gpt-4.1-mini` が停止
- **2027-01-15**: Claude Code Review の Enterprise 向けクレジット請求期限
- **2027年1月中旬**: Power BI の単体の Copilot が退役（MC1546429）
- **2027-01-20**: OpenAI `gpt-realtime` / `gpt-audio` / `gpt-4o-realtime` 系などが停止
- **2027-01-30**: ChatGPT Classic（旧デスクトップアプリ）終了（二次）
- **2027年1月末**: UBB の入口が既定で表示され、旧設定が退役（MC1546354）
- **2027-02-01**: OpenAI `gpt-5.5-cyber-preview` が停止
- **2027年2月**: VS Code の Copilot から Local harness を削除（`vscode.temporaryDefaultToLocalHarness` も廃止）
- **2027-02-10**: Claude Meetings の成果物の無料期間終了 ／ OpenAI `gpt-image-2` 停止
- **2027-03-01**: GPT-6.2 Astra / Sol の API の Ultrafast が Standard の3倍から6倍に
- **2027-03-01 以降**: Gems 廃止（Business / Enterprise）
- **2027-03-08**: Fable 5.2 ローンチ特典のリセットが失効
- **2027-03-30**: MCP 仕様 `2027-03-30` 版のリリース予定
- **2027 春**: Siri AI 対応アプリの App Store 提出受付が開始
- **2027-04-01**: OpenAI `gpt-5.1` / `gpt-5.3-codex` / `gpt-5.4-nano` 停止 ／ SharePoint の tempauth URL 退役（MC1551122・MC1492958）
- **2027-05-17**: GitHub Copilot の MAI Code 2 / MAI Code 2 Flash の導入価格が終わり、単価が倍に
- **2027-11-12**: Purview Data Governance のサポート終了

## 改善メモ

- Master: 新規提案・障害の変化なし。継続提案8件（最多 B-088 Gemini API changelog の URL 差し替え、15回目）
- Copilot: 新規提案・障害の変化なし。継続提案5件（最多 B-080 Cowork の Learn URL の移設、20回目）
- industry: 新規提案・障害の変化なし。継続提案7件（最多 B-040 セキュリティ開示の定点、17回目）
- ソース間の差異: 前日に食い違った Anthropic Platform の release notes の透かし（11/16 付）は、本日 Master も確認して解消した
- ソース間の差異: Claude Code `2.1.326` の日付を industry は 11/16 とし、Master は日付を書かず changelog 掲載と npm `latest` 化を本日の新規としている。本サマリーは日付を付けずに統合した
- ソース間の差異: GPT-5.6 Sol の期間限定価格の終了日は、OpenAI の changelog（11/21以降）と料金ページ（11/30）で一次どうしが食い違う（industry）
- 前日（11/17）分に欠損ソースはなく、欠損リカバリは不要
