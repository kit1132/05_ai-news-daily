# AI News Daily Summary — 2026-11-04

Power Platform のプロンプトで選べる Claude と Grok のモデルが 12/2 に外れ、GPT 系へ自動で移る。単体の Word / Excel / PowerPoint エージェントは11月中旬から撤去され、M365 Copilot のライセンスがない Copilot Chat 利用者には 11/9 から上限が広がる。開発ツールでは、Claude Code 2.1.317 でセッション内の `claude -p` が別セッション扱いになり、GitHub Copilot の PR 承認が必須レビュー数に数えられるようになった。

## 今日のハイライト

### 1. [廃止+破壊的変更] Power Platform のプロンプトから Anthropic と Grok のモデルが 12/2 に外れる — プロンプトで Claude を選べる前提が消え、全段が OpenAI の GPT 系に揃う

**要点**: Copilot Studio・Power Automate・Power Apps のプロンプトで使える Claude Sonnet 4.6・Claude Opus 4.6・Grok 4.1 Fast と旧 GPT 系が 12/2 に退役する。そのモデルを使うプロンプトは同じ段の GPT 系へ自動で移る。段ごとの料金は変わらないが、応答の書きぶりは変わりうる。

**詳細**: MC1536101（11/3 公開・Feature update）。移行は自動で、退役モデルを指定したままにしても止められない（Copilot）。

- Basic: GPT-4.1 mini → GPT-6 Luna
- Standard: GPT-4.1・GPT-5 chat・GPT-5.3 chat・Claude Sonnet 4.6・Grok 4.1 Fast reasoning → ChatGPT-latest
- Premium: GPT-5 reasoning・GPT-5.2 reasoning・Claude Opus 4.6 → GPT-6 Reasoning
- 求められる対応: 退役モデルを使うプロンプトと、それに頼るアプリ・フロー・エージェントを洗い出し、移行先で出力の形式と後続処理を試す。料金は段単位で据え置きだが、実際の消費は入出力のトークン数で変わる
- エージェント本体のモデル: MC1506318 が 11/3 に4版目へ更新され、GitHub Copilot ハーネスの移行先が2件変わった。GPT-5 Chat は GPT-5.6 Terra ではなく GPT-6 Luna へ、GPT 5.6 Sol は GPT-6 Sol ではなく GPT-6.1 Sol へ移る（11/12、残り8日）。Claude Opus / Sonnet の旧版の退役日は別に告知するとしている

- https://mc.merill.net/message/MC1536101
- https://mc.merill.net/message/MC1506318

### 2. [廃止] 単体の Word / Excel / PowerPoint エージェントが撤去される — エージェントを選んで呼ぶ操作が無くなり、Copilot Chat で頼む形だけになる

**要点**: M365 Copilot ライセンスの利用者は、11月中旬から順に、左レールとエージェント一覧で Word / Excel / PowerPoint エージェントを見つけられなくなり、ピン留めも @メンションもできなくなる。作成と編集は Chat で直接頼む。既存の会話の続きはできない。

**詳細**: MC1536062（11/3 公開・Feature update / User impact）。全世界で11月中旬に始まり、12月下旬に完了する見込み（Copilot）。

- 残るもの: 作ったファイルは OneDrive / SharePoint の元の場所に、既存の権限と保持設定のまま残る。過去の会話の履歴も見られる
- 求められる対応: 管理者の設定は不要。単体エージェントを案内している研修資料・ヘルプデスク手順を、Chat から始める手順に書き換える
- 同じ時期の関連: Office in Copilot（MC1530611・11/3 更新、11月中旬に展開）で、Copilot アプリの中で Word / Excel / PowerPoint のファイルを作成・編集・共同編集できるようになる

- https://mc.merill.net/message/MC1536062

### 3. [料金] ライセンスのない Copilot Chat 利用者に 11/9 から上限がかかる機能が増える — 無償の Chat で使える量が Microsoft の側で変わり、管理者は上限を見ることも変えることもできない

**要点**: 画像生成で先に入っていた公正利用の上限が、Copilot Chat の他の機能にも広がる。対象は商用テナントで M365 Copilot ライセンスを持たない利用者で、上限は時間帯でも変わる。無償の Chat を前提にした展開計画は、使える量が一定でないものとして見直す必要がある。

**詳細**: 同じ題名の通知が2本出ている。MC1536158 は「新しい上限は展開中」、MC1536163 は「11/9 から展開を始める」と書く（Copilot）。

- 上限の種類: 公正利用（1日の中でも変わる）と、機能ごとの上限。使えないときは製品の中で通知し、再開できる時期を示す。生成中の応答は止めない
- 管理者の側: 上限の確認も調整もできない。Microsoft はヘルプデスクへの周知と、セルフサービスのライセンス要求の扱いの確認を勧めている

- https://mc.merill.net/message/MC1536163
- https://mc.merill.net/message/MC1536158

## カテゴリ別まとめ

### Anthropic / Claude

- [破壊的変更+新機能] **Claude Code 2.1.317** — Anthropic が 11/3 に出した版で、セッションの中で動かす `claude -p` が親セッションの ID と transcript を共有しなくなった。self-hosted runner などで旧挙動に頼っていた場合は `CLAUDE_CODE_DISABLE_NESTED_SESSION_ID=1` で戻す。npm は `{stable: 2.1.311, latest: 2.1.317, next: 2.1.317}` で、stable は 2.1.309 から上がった（Master・industry）
  - 費用レポート: 管理者は Claude apps gateway の `GET /v1/organizations/analytics/cost` で、期間を指定して合計・開発者別・日別・IdP グループ別の支出を読める。`admin:` を設定した gateway は開発者ごとの IdP グループを毎日記録し、`admin.identity_retention_days` の期間だけ保持する
  - 組織向け: Desktop の Code タブが組織のリモート管理設定の読み込み状態を通知する。OTel に `anthropic.plan`・`anthropic.seat_type`・`anthropic.provider`・`anthropic.custom_base_url` が加わった
  - 安全側: web / shell ツールがアカウントのメールアドレスをネットワークへ送る前に確認を求める。Agent SDK の hook callback に `onFailure: "block"` が加わった
  - 挙動の変更: Read ツールの「前回から変更なし」スタブが廃止され、再読込で内容が返る。メインと違うモデルの subagent / teammate は、そのモデルに保存した effort（無ければ既定値）を使う
  - https://code.claude.com/docs/en/changelog
  - https://registry.npmjs.org/@anthropic-ai/claude-code
- [仕様] **Claude Code の既存ゲーム複製の拒否** — The Decoder（11/3）によると、Anthropic の Addy Osmani 氏は X で、Opus 5.5 向けのシステムプロンプトに入れた2文が既存ゲームの再現を止めていると説明した。名前を変えたり「オリジナル」と称したりしても対象になる。自作や同じジャンルのゲームは作れるが、オリジナル作品でも断られたという報告がある。発効日と正式なポリシーページは示されていない（industry）
  - https://the-decoder.com/anthropic-cracks-down-on-game-cloning-in-claude-code-after-wave-of-ai-built-knockoffs/
- [据え置き] **Platform・退役ページ・ニュース一覧** — Platform release notes の最上位は 11/2 の message threads のままで（TTFT 約35%短縮の報道は 11/3 既報の数値と同じ）、モデル退役ページの Active は15件、廃止履歴の最新は 9/30 のままである。Haiku 4.5 は退役下限日（10/15）を20日過ぎても Active にある。`www.anthropic.com/news`・`/research`（10/27）・`support.claude.com`（10/21）・Privacy Center（`dateModified` 10/30）も動いていない
  - https://platform.claude.com/docs/en/about-claude/model-deprecations

### セキュリティ

- [セキュリティ] **Postman デスクトップ版のプラグイン無断導入の報告** — GitHub の Postman リポジトリのイシューによると、Postman 12.33.4 が更新時に Codex 用プラグイン、Claude Code 用プラグイン（2.0.1）、Postman の API スキルを読ませる起動フック、リモート MCP 接続、Postman CLI を入れた。報告者は、インストーラーが自分のフックを自分で承認しようとしたと書いている。データの外部送信の証拠は示されておらず、Postman の公式回答はまだ無い（industry）
  - https://github.com/postmanlabs/postman-app-support/issues/14370
- [動向] **OpenAI のバグ報奨金の4倍引き上げ** — The Decoder（11/3）によると、OpenAI は ChatGPT・Codex などの重大な脆弱性に最大 $30,000、特に優れた報告に最大 $100,000 を払う。品質・継続参加（5段階）・期間限定キャンペーンの加算を合わせると最大約 $172,000 になり、直近30日の報告にも旧額との差額を払う（industry）
  - https://the-decoder.com/bug-hunters-can-now-earn-up-to-172000-from-openai-as-company-ramps-up-security/

### GitHub Copilot

- [新機能+仕様] **Copilot code review の承認 GA と Max レビュー** — GitHub が 10/28 に、Copilot code review の PR 承認を GA にした。有効にすると Copilot の承認がリポジトリの必須承認数に数えられ、「承認は人が出す」前提のブランチ保護の設計が組織の設定しだいで変わる。10/29 は個別に確認できず、本日 Publickey（11/3）経由で内容を確認した（industry）
  - 承認: 既定はオフ。Enterprise・Organization・リポジトリ単位で有効にでき、Copilot が承認してよいファイルパスを絞れる。新しいコミットの push で取り消される
  - Max: Lite・Balanced の上の3段目でパブリックプレビュー。提供元の異なる複数モデルのレビューエージェントを走らせ、集約エージェントが突き合わせる。AI クレジットの消費は Lite・Balanced より多い（倍率は非公表）
  - 管理と対象: 管理者はレビュー段階の上限を設定できる。対象は Copilot Pro・Pro+・Max・Business・Enterprise
  - https://github.blog/changelog/2026-10-28-copilot-code-review-merge-with-confidence-with-max-and-approvals
  - https://www.publickey1.jp/blog/26/githubcopilot_code_review_maxgithub_universe_2026.html
- [新機能] **JetBrains Air の Copilot 対応** — GitHub が 11/3、JetBrains のエージェント環境 Air のエージェント選択に Copilot を加え、JetBrains AI のクレジットではなく Copilot の契約で IDE 内のローカルタスクと Air Teams 経由のクラウドタスクを動かせるようにした。接続は Agent Client Protocol（ACP）である（Master）
  - クラウドタスク: 新しい VM 上の Docker コンテナで動き、通信はすべてプロキシを通る。タスク間で状態は引き継がない
  - 前提: Air Teams を有効にした JetBrains の組織アカウント、Copilot の契約、Air 管理者による Copilot の有効化。契約やクレジットはクラウド環境の起動時に確かめ、足りなければタスクが失敗する
  - ⚠️ 個人プランと組織プランのどちらで課金されるかはタスクごとに選べない。Air のガバナンス・分析機能に Copilot の利用は含まれない
  - https://github.blog/changelog/2026-11-03-github-copilot-is-now-available-in-jetbrains-air
- [予定] **GitHub のリポジトリ書き込み能力の180倍化** — Publickey（11/3）によると、GitHub はコンピュートとストレージを分け、ロックをリポジトリ単位からブランチ単位に変えて、来年初頭までに全ユーザーを新しい仕組みへ移す。5,000の AI エージェントでの試験では、1リポジトリあたり毎秒7,200回の push を処理できた。今年だけで CPU を400万コア、ストレージを160PB 増やした（industry）
  - https://www.publickey1.jp/blog/26/github180aigithub_universe_2026.html
- [版更新] **Copilot CLI `v1.0.106-3`〜`-6`** — GitHub が 11/2〜11/3 に pre-release を4版出した。安定版は `v1.0.105`（10/28）のままである（Master）
  - `/settings`: すべての設定とローカルのリソースを横断検索できる一画面にまとまった（`-6`）
  - JSON 出力: `copilot -p --output-format json` と `copilot workflow run` が端末制御文字を JSON 内でエスケープするようになった（パース後の値は同じ・`-3`）
  - 誤削除の防止: `/session delete` が `--force` など未知のオプションを使用法エラーで拒否するようになった。以前は確認なしで現在のセッションを消すことがあった（`-3`）
  - https://github.com/github/copilot-cli/releases

### OpenAI / Codex / ChatGPT

- [版更新] **Codex `0.167.0-alpha.4`** — OpenAI が Codex の pre-release を 11/3 に出した（リリース本文なし）。安定版は `0.166.0`（10/29）のままである
  - https://github.com/openai/codex/releases
- [据え置き] **API changelog・退役・安全性** — OpenAI の API changelog の最上位は 10/30 の gpt-6-rosalind、deprecations は 10/14 の GPT-4 系の告知のままである。Deployment Safety Hub（10/30）、community Announcements（10/28）、`learn.chatgpt.com` の changelog（10/29）、`alignment.openai.com`（First posted 10/20）も動いていない
  - https://developers.openai.com/api/docs/changelog

### Microsoft 365 Copilot

- **Word / Excel / PowerPoint エージェントの撤去**（ハイライト2参照）
- **Copilot Chat 利用者の上限拡大**（ハイライト3参照）
- [予定] **Excel と Cowork の会計機能** — Microsoft が MC1536053（11/3）で、経理担当者が Excel と Cowork で勘定の照合、仕訳の下書き、予実差異の分析、財務報告の作成をできるようにすると告知した。パブリックプレビューは Frontier の登録が必要で、11/13 の GA からは要らなくなる
  - 監査証跡: 会計機能を呼ぶときに選ぶと、Copilot が何をなぜ変えたかがチャット履歴に残る。Excel では使え、Cowork は予定
  - 統制: ERP や基幹システムへの転記はユーザーの承認なしには行わない。他社の会計コネクタは別のライセンスや管理者の有効化が要ることがある
  - https://mc.merill.net/message/MC1536053
- [新機能] **Cowork の Planner プラグイン** — Cowork What's New に「November 2026」節ができ、Planner プラグインが載った。M365 Copilot ライセンスの利用者は、管理者が組織に提供すると、Cowork から割り当てタスクの確認・状況報告の作成・目標のタスク分解ができる。Planner への変更は承認を経て反映される
  - https://learn.microsoft.com/en-us/copilot/cowork/whats-new
  - https://support.microsoft.com/planner/planner-plugin-overview
- [予定] **Chat から別のモードへの切り替え提案** — Microsoft が MC1536065（Roadmap 577841）で、Copilot アプリの Chat がプロンプトに合う別のモード（Cowork など）を提案するカードを出すと告知した。切り替えるとプロンプトと Chat の文脈がそのまま渡り、提案はそのモードを使えるユーザーにだけ出る。11月中旬に始まり、11月下旬に完了する見込み
  - https://mc.merill.net/message/MC1536065
- [仕様] **リリース設定の例外の上限が 10,000 人に** — Microsoft が MC1536057 で、テナント全体と違うリリース設定（Standard / Deferred）を割り当てる例外の対象を、管理者が100人から10,000人まで広げられるようにすると告知した。個別の割り当てとグループのメンバーを合わせて数え、入れ子のグループは引き続き使えない。展開は10月下旬から11月中旬である
- [予定] **展開時期の後ろ倒し3件** — Microsoft が次の3件の通知で展開時期を後ろへずらした
  - Notebooks の Power BI 参照（MC1474458）: GA は11月末に始まり12月中旬に完了する見込み（前は10月下旬開始・11月中旬完了）
  - 低評価フィードバックのカテゴリ選択（MC1530595）: 11月中旬に延期（前は10月下旬）。選んだカテゴリと自由記述は新たに保存されるデータになる
  - PowerPoint の営業向けスキル（MC1521609・MC1529476 ほか）: 完了が11月下旬に延びた
  - https://mc.merill.net/message/MC1474458
- [予定] **Roadmap 11/3 バッチ** — 11/3 00:14Z のバッチに10件が入り、総項目数は 2,238 になった。Copilot 関連の新規は 573170（米国政府クラウド向けの Copilot Search・コネクタ・エージェントの利用状況レポート、12月）だけである。同じ時刻に 569612（Purview の Copilot メモリーの保持）が `Launched` になった
  - https://www.microsoft.com/releasecommunications/api/v2/m365/rss
- [据え置き] **Release Notes・ブログ各種** — Release Notes の先頭は October 27, 2026 のままで、Copilot ブログ（10/29）・TC の M365 Copilot Blog（10/30）・Agent 365 Blog（9/30）・SharePoint Blog（10/29）に新しい記事はない。Purview・拡張機能 What's New・Partner Center の11月分も前日のままである

### Copilot Studio / Power Platform

- **プロンプトの Anthropic / Grok モデルの退役**（ハイライト1参照）
- [観測] **GitHub Copilot ハーネスのモデル表と課金ページの改訂** — `authoring-agent-model-availability` が 11/3 07:03Z に `dc0fae59`（`ms.date` 11/2）へ改訂され、表は MC1506318 の4版目と一致した。前版との差分は特定できていない。FedRAMP の顧客と、地域をまたぐデータ移動を制限している米国外の環境では、GPT-5 Chat を当面使える。`billing-licensing` と課金レート表は 11/3 19:07Z に再ビルドされたが、消費レートと 125% のエンフォースメントは変わっていない。どのページもハーネスの旧名「GitHub Copilot」のままである
  - https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-experience/authoring-agent-model-availability
  - https://learn.microsoft.com/en-us/microsoft-copilot-studio/requirements-messages-management
- [据え置き] **What's New・その他の Learn・ブログ** — Copilot Studio What's New は `031b66d5`（`ms.date` 10/5）のままで、非推奨一覧（`2cc84953`）、PPAC の容量管理、標準ハーネスのモデル表、ガイダンスハブに改訂はない。Released Versions は 2026.6.3 のまま126日たつ。Power Platform ブログ・Copilot Studio ブログ・TC の Copilot Studio Blog に新しい記事はなく、Qiita / Zenn にも一次の範囲を出る記事はない
  - https://learn.microsoft.com/en-us/microsoft-copilot-studio/whats-new

### Google / その他の開発ツール

- [観測] **Gemini API の一次ページに2日続けて届かない** — Google が `ai.google.dev/gemini-api/docs/changelog`（`.md.txt` も）を `aistudio.google.com/docs/changelog` へ 301 で移しており、転送先はこの実行環境からゲートウェイ拒否だった。WebSearch でも 10/30 より新しい項目は見つからず、11/17 の停止と 12/1 の Argon 値上げは本日も未確認である。二次は、Gemini API の docs を AI Studio に組み込んだ（first preview）と報じている（Master・industry）
  - https://alphasignal.ai/news/google-builds-gemini-api-docs-directly-into-ai-studio
- [新機能] **Apple の Siri AI Developer Preview** — Apple が 11/3、iOS / iPadOS / macOS / watchOS / visionOS 27.3 beta で Siri AI の Developer Preview を始め、どの開発者でも App Intents で自分のアプリを Siri AI につなげられるようにした。一般ユーザーへの提供は数か月後、App Store への提出受付は春で、利用条件は後日示す
  - skills: 複数のアクションを1つの体験にまとめる方法を Siri AI に教えられる
  - Spotlight: 既存のスキーマに合わないエンティティも、Spotlight の意味インデックスから Siri AI が呼び出せる
  - https://developer.apple.com/news/
- [新機能] **Devin の MCP 認証とセキュリティ所見の取り込み** — Cognition が 10/30 と 11/2 にリリースノートを2本出し、セッションマシンに固定した MCP サーバーに header script（呼び出しごとに短命トークンのヘッダを出すコマンド）を設定できるようにした。セッション中に 401 を返したサーバーは `resource_metadata` から OAuth を始める
  - セキュリティ連携: SonarQube・Linear・Vanta から所見を取り込め、コードスキャンの1回あたりのリポジトリ上限は 500 から 1,000 に上がった
  - 個人プラグイン: インストールや編集が実行中のセッションにそのまま反映される
  - https://docs.devin.ai/release-notes/overview
- [新機能] **Orca `v1.4.247`** — Stably AI が 11/3 にデスクトップ版を出し、Chat UI を Experimental から外した。エージェントごとに Chat と CLI を選べ、利用上限がリセットされたときにチャットを自動で続ける設定（任意）が加わった。Claude Code / Codex 連携の変更と非互換の記載は無い
  - 電話アプリ: ブランチのコミットの閲覧、差分ファイル間の移動、PR のレビューコメントの閲覧と追加ができる
  - プラグイン: カスタムエディタ、ステータスバー項目、パネルを作れ、エージェントのプロンプトやワークスペース操作とつなげられる
  - https://github.com/stablyai/orca/releases
- [据え置き] **Cursor・xAI ほかの定点** — Cursor の changelog（10/20）とフォーラム（10/12）、xAI（11/2）、TypeSafe AI（`jev-1.14.0`）、MCP blog（9/29）、Hugging Face の8 org に新規はない。The Keyword は 11/2 の10月まとめのままで、Workspace Updates の 11/3 は AI と関係ない。Gemini アプリの release notes は 2026.10.13、Obsidian は 11/2 の 1.15 のままである

### 業界・市場

- [動向] **企業の LLM API 支出で Anthropic のシェアが55%** — Menlo Ventures が 11/3 の年次報告「2026: The State of Enterprise AI」で、企業の LLM API 支出に占める比率を Anthropic 55%（前年40%）・OpenAI 31%（同27%）・Google 9%（同21%）と推計した。企業の AI 支出は 2026年9月時点で $176.8B と推計し、1年前の $33B から5.4倍になった（industry）
  - 調査方法: 米国企業の AI 意思決定者 約400人（担当する AI 支出の合計 $4B 超）への調査と、ボトムアップの市場推計の組み合わせ
  - ⚠️ 留意点: Menlo Ventures は Anthropic の出資者で、報告でもそれを開示している。`menlovc.com` などの一次に届かず、数値は WebSearch の抜粋による。前年版は支出総額を $37B としており、今回の「1年前 $33B」とは集計範囲が異なる可能性がある
  - https://www.globenewswire.com/news-release/2026/11/03/3394279/0/en/menlo-ventures-2026-state-of-enterprise-ai-report-enterprise-ai-spending-hits-177b-up-5-4x-in-one-year-as-agents-take-over.html
- [据え置き] **買収協議・決算・調査データ** — Amazon × Decart、Nvidia × Reflection AI の買収協議に続報はなく、Anthropic の S-1/A の本文と Grok Bot の利用枠の公式説明も出ていない。IDC Japan・MM総研・NRC の新しい公表も無かった

## 直近の注目予定

- **11/4**: Entra で一般ユーザーのブループリント作成が既定オン（MC1506733） ／ Kimi K3.1 Pro の重み公開の約束期限（二次）
- **11/4〜5**: Apple Intelligence の開発者向けラボ（Siri AI の質疑。11/4 9〜10時 PT、11/5 18〜19時 PT）
- **11/5 ごろ**: Anthropic のゲスト研究者（生命科学）の応募受付が終了（締切日は明記なし）
- **11/5**: PnP の Community call
- **11月**: GitHub の cloud sandbox の課金が開始（日付は明記なし） ／ Targeted release の割り当てが変更不可になり、統合 Release Preferences 画面が入る
- **11/9**: GitHub が公開リポジトリの `pull_request_target` を試験ブロック（16:00〜18:00 UTC） ／ ライセンスのない Copilot Chat 利用者の上限拡大が開始（MC1536163） ／ Dataverse のみのテナントでストレージ検証が開始（MC1483529）
- **11/12**: Copilot Studio の GPT-4.1 / GPT-5 系と、GitHub Copilot ハーネスの GPT-5 Chat・GPT 5.6 Sol / Luna が退役（MC1506318） ／ Anthropic Usage Policy 改定版が発効 ／ OpenAI → Cursor のモデル供給停止予定（一次未読）
- **11/13**: Excel と Cowork の会計機能が GA（MC1536053）
- **11/15**: Dataverse for Teams 環境とアンマネージド開発者環境の新規作成が停止 ／ Copilot Studio のカスタム採点器ライブラリが GA（MC1531932）
- **11/16**: GitHub Copilot が Claude Opus 4.8・Opus 5・GPT-5.6 Terra を廃止 ／ Teams の旧 GitHub アプリが退役 ／ `pull_request_target` の2回目の試験ブロック ／ Cowork / Autopilot の Engage プラグインが GA（MC1530609）
- **11月中旬**: 単体の Word / Excel / PowerPoint エージェントの撤去が開始（MC1536062、12月下旬に完了） ／ Office in Copilot の展開（MC1530611） ／ Chat からのモード切り替え提案（MC1536065） ／ Teams 会議の MeetingAI / TranscriptionWithMeetingAI ポリシー（MC1532253） ／ 低評価フィードバックのカテゴリ選択（MC1530595） ／ Agent Builder のプロンプトのスケジュール実行（MC1302906） ／ Viva Insights の GitHub Copilot 指標が既定オン（MC1523085）
- **11/17**: Gems が Gemini アプリの設定パネルへ移動 ／ Gemini API の TTS・Live プレビュー5種が停止（最短日。2日続けて一次未確認）
- **11/17〜20**: Microsoft Ignite
- **11/20**: Copilot Studio のコスト管理を M365 管理センターへ移す機能が GA（MC1530368）
- **11/24 以降**: `claude-opus-4-5-20251101` の暫定退役日（確定日ではない）
- **11月下旬**: Copilot アプリの Home の Projects / Workspaces が Deferred release に出る（MC1535647） ／ PowerPoint の営業向けスキルの展開完了
- **11/29**: OpenAI が Daybreak Blue のセッションデータの学習利用を開始（二次）
- **11月末**: Word の Top of Doc 要約の廃止が完了（MC1454113） ／ Notebooks の Power BI 参照の GA が開始（MC1474458）
- **11/30**: Power Automate の Describe it to design it が退役 ／ Opus 4.8 の fast mode を削除 ／ `claude-sonnet-4-5-20250929` が Claude API から退役 ／ Power Apps のモデル駆動アプリの説明文の AI 生成などが退役 ／ OpenAI の Evals・`v1/prompts`・Agent Builder が停止 ／ Gemini 4 Argon の導入価格が終了 ／ Azure DevOps コネクタの旧接続が認証不可に（MC1508508） ／ App Builder と vibe.powerapps.com が退役
- **12/1**: M365 Copilot の前提サブスク不要オファー開始 ／ Copilot Business の従量課金が既定オン ／ Gemini 4 Argon の単価が $4/$20 に倍増 ／ Google スライドの複数スライド作成の上限引き上げ優待が終了しうる
- **12/2**: Power Platform のプロンプトから Anthropic・Grok・旧 GPT 系のモデルが退役し自動移行（MC1536101） ／ GitHub が公開リポジトリの `pull_request_target` を既定でブロック
- **12月上旬**: Copilot アプリのタスクバー固定にライセンス別の選択肢が入る（MC1530612）
- **12月中（日付未公表）**: ChatGPT と Codex の利用枠が Plus・Pro・Business で1つの予算に統合（二次）
- **12/11**: Power Apps の式の生成・Power Apps Ideas・Copilot によるコントロール名の変更が退役（MC1532421・MC1532426）
- **12/14**: claude.ai/design の単体サイトが閉鎖
- **12/15**: アンマネージド開発者環境が停止
- **12月下旬**: Purview DLP の Microsoft 以外のアプリ対応が GA（MC1449180） ／ 単体 Word / Excel / PowerPoint エージェントの撤去が完了（MC1536062）
- **12/31**: Power Platform の環境間のコメントのインポート・エクスポートが終了 ／ Claude Security の無償クレジット（月 $25,000×2か月）の対象期間が終了 ／ Gemini 4 Carbon の導入価格の割引が終了
- **2027-01-06**: OpenAI `tts-1` / `tts-1-hd` / `gpt-4o-mini-tts` 2版が停止
- **2027年1月**: Targeted release が退役 ／ Copilot Studio の Teams アプリで編集ができなくなる（MC1511056） ／ Teams の会議メモリーファイルの生成が開始（MC1429018）
- **2027年初頭**: GitHub のリポジトリ書き込み基盤の全ユーザー移行が完了
- **2027-01-14**: OpenAI の GPT-4o・GPT-4o mini・GPT-4.1・GPT-4.1 mini が API から削除（→ `gpt-6-luna`）
- **2027-01-15**: アンマネージド開発者環境の削除開始 ／ Claude Code Review の Enterprise 向けクレジット請求期限
- **2027年1月中旬〜下旬**: 旧来の Teams 保持ポリシーが Copilot の対話に効かなくなる（MC1481313）
- **2027-02-01**: Microsoft が `usage_ai-training` トークンへの対応を開始
- **2027-03-01 以降**: Gems 廃止（Business / Enterprise）
- **2027年3月**: Purview の DSPM classic / DSPM for AI classic が退役（MC1481315）
- **2027年3月末**: Outlook の Copilot Prioritize の削除が完了（MC1519861） ／ SharePoint / OneDrive の `.agent` 形式エージェントが動かなくなる（MC1511052）
- **2027年春**: Siri AI 対応アプリの App Store 提出受付が開始
- **2027-04-01**: OpenAI `gpt-5.1` / `gpt-5.3-codex` / `gpt-5.4-nano` が停止

## 改善メモ

- 新規提案: Master が B-088（Gemini API Changelog の URL を `aistudio.google.com` へ差し替える）を起票した。Copilot と industry は新規起票なし
- 継続提案: Master は継続6件（最多 B-036 DeepSeek 登録、12回目。見送り候補 B-036 / B-037 / B-043 / B-078） ／ Copilot は継続4件（最多 B-080 Cowork の Learn URL 差し替え、9回目。B-081 ハーネス改名は7回目） ／ industry は継続7件（最多 B-040 セキュリティ開示の定点、14回。見送り候補 B-036）
- 障害の変化: Master が `aistudio.google.com` のゲートウェイ拒否を新規に記録した（industry は前日に記録済み）。industry が `menlovc.com`（Menlo Ventures）のゲートウェイ拒否を新規に記録した
- 欠損リカバリ: 前日（11/3）分は3ソース揃っており、対象なし
- ソース間の差分・矛盾:
  - 前日に記録した Gemini API changelog の食い違い（Master は 10/30 が最上位のまま、industry は 301 で届かず）は、本日 Master も 301 と到達不能を記録したことで解消した。Master の B-088 と industry の B-048（11/3 起票）は同じ URL 差し替えの提案で、両リポで別 ID になっている
  - Claude Code 2.1.317 のタグが、Master は `[破壊的変更+新機能]`、industry は `[新機能]` で割れた。`claude -p` のセッション共有の変更は旧挙動に頼る構成を壊すため、本サマリーは Master のタグを採った
  - GitHub Copilot の JetBrains Air 対応を、Master はハイライトに置き、industry は採録見送りにした（担当範囲の違いで、事実の矛盾ではない）
