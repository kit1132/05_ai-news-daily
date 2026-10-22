# AI News Daily Summary — 2026-10-23

Microsoft は Outlook の Copilot Prioritize を 10/26 から退役させ、10月中に Dataverse の Basic User ロールからカスタムコネクタ定義の読み取り権限を外す。PyPI に出た LiteLLM 1.107.0 には、Claude Code・Cursor・Copilot の認証情報まで盗む情報窃取プログラムが入っていた。

## 今日のハイライト

### 1. [廃止] Microsoft が Outlook の Copilot Prioritize を 10/26 から退役させる — 2027年3月末までに全クライアントから消える

**要点**: MC1519861 によると、Outlook でメールの優先度を Copilot が判定する Prioritize が 10/26 から順にロールバックされる。オプトインは不要で、退役後は使えない。Prioritize を前提にした受信トレイ整理の研修資料や社内手順は、ほかの手段に置き換える必要がある。

**詳細**:

- 対象: Prioritize を使える利用者。新しい Outlook を含む全 Outlook クライアントから UI が削除される
- 日程: 10/26 に開始し、2027年3月末までに完了する見込み
- 経緯: 10/21 公開、10/22 に v2 へ更新され、日程と本文が改められた（タグは Retirement）
- 管理者の対応は不要。Microsoft は利用者への周知、ヘルプデスクの準備、社内文書・研修資料からの記述削除を推奨している

- https://mc.merill.net/message/MC1519861

### 2. [破壊的変更] Dataverse の Basic User ロールからカスタムコネクタ定義の読み取り権限が外れる — 共有されていないコネクタは定義が見えなくなる

**要点**: MC1520706 によると、10月中に Power Platform の権限が変わり、Basic User ロールの利用者は、自分が所有するか明示的に共有されたカスタムコネクタの定義しか読めなくなる。環境内のコネクタ定義を一律に読めた前提で作ったメーカー向け手順は、カスタムセキュリティロールの追加が要る。

**詳細**:

- 対象: ソリューションに含まれるカスタムコネクタの定義
- 管理者の作業: Basic User のままコネクタ定義を読む必要がある環境を洗い出す。全コネクタを読ませたいときは、Connector テーブルに組織レベルの Read 権限を持つカスタムセキュリティロールを作って割り当てる
- 理由: 意図して共有していないコネクタの定義や構成を見せないためのセキュリティ強化としている
- 通知は 10/22 公開でタグは Admin impact。発効日は「October 2026」とだけあり、日付は書かれていない

- https://mc.merill.net/message/MC1520706

### 3. [セキュリティ] PyPI の LiteLLM 1.107.0 に情報窃取マルウェアが混入した — Claude Code・Cursor・Copilot の認証情報も盗まれる

**要点**: GIGAZINE によると、LLM ゲートウェイ LiteLLM の PyPI 版 1.107.0 に情報窃取プログラムが入っていた。`.pth` で Python 起動のたびに動くため、LiteLLM を使わない処理からも盗まれる。「入れただけなら安全」という前提が崩れ、環境の作り直しと鍵の総入れ替えが必要になった。

**詳細**:

- 公開期間: 10/21 20:39（JST）ごろに PyPI へ公開され、約2時間後に削除された。一部の Docker イメージにも混入した（版は非公表）
- 侵入経路: 攻撃者がエンジニア3人の GitHub 認証情報を得て、公開手順を偽リポジトリに向けた。GitHub 上のソースには不正ファイルが無い
- 盗まれるもの: ブラウザのパスワード・履歴、SSH 秘密鍵、クラウド認証情報、AI コーディングツール（Claude Code・Cursor・GitHub Copilot）の認証情報、LiteLLM で管理する API キー
- 持続化: `sitecustomize.py` が1時間ごとに GitHub 上の指示を読み、窃取の再実行と追加プログラムの取得を行う
- 対処: 先に不正ファイル（`cook.pth`・`cook.py`・`sitecustomize.py`）を消して環境を作り直し、パスワードと API キーを変える。消す前に Python を起動すると再び動くため、通常のアップグレードから始めてはいけない
- 一次: LiteLLM の GitHub advisory 一覧にはまだ載っておらず、SafeDep の分析と開発チームの発表を引いた二次報道で確認した

- https://gigazine.net/news/20261022-litellm-backdoor/

## カテゴリ別まとめ

### Claude / Anthropic

- [破壊的変更+新機能] **Claude Code `2.1.307` / `2.1.308` と stable の更新** — Anthropic が 10/21〜10/22 に Claude Code `2.1.307` / `2.1.308` を出し、npm の `stable` / `latest` / `next` がそろって `2.1.308` になった。10/20 の `2.1.305` で入った `allowedMcpServers` の緩和（`env` だけで `${VAR}` を使う stdio サーバーを絞らない）が、stable チャンネルに固定した組織にも届く。https://code.claude.com/docs/en/changelog
  - `/claude-api api-version`: Claude API を呼ぶコードを API バージョン `2026-10-21` へ書き換える
  - `claude_code.safety_event`: 権限ルール・auto mode・安全チェック・hook・サンドボックスがツール呼び出しを止めた、確認した、差し戻したときに、OpenTelemetry へ1件ずつ出す
  - セルフホストランナー: チェックアウト hook が既定30分で止まり、セッションの準備が失敗する。長い hook は `--checkout-hook-timeout-min` を上げるか `0` にする
  - その他: `@claude review stop` で PR の常時レビュー購読を止められる。`axScreenReader` はプロジェクトの設定に書いても無視される。HTTP MCP のツール呼び出しの二重送信を直した。`2.1.308` は不具合修正の1行だけ
- [新機能] **組織単位の web fetch 制御** — Anthropic が release notes の 10/20 の項に、管理者が Console の Capabilities ページで組織の web fetch を止めたり、許可・拒否ドメインを決めたりできると書き足した（本日初検出）。止めた場合、web fetch ツールを含む Messages API リクエストは 400 になる。https://platform.claude.com/docs/en/release-notes/overview
  - Managed Agents の `web_fetch`: 組織の一覧とエージェント側の `allowed_domains` / `blocked_domains` の両方を通った URL だけを取り、リダイレクト先も判定する
  - Managed Agents の `web_search`: 組織の「Allow web search」に 10/6 から、検索ドメイン制限に 10/14 から従っていた（今回はじめて明記された）
  - user profiles: 10/21 の項に `enforcement_status` / `enforcement_actions` が追記され、エンドユーザーを制限・BAN したかを読める
- [動向] **Agent Skills の AAIF への寄贈** — Anthropic が 10/22 に、Agent Skills の仕様・名称とロゴ・GitHub の organization・`agentskills.io` を Linux Foundation 傘下の Agentic AI Foundation（AAIF）に寄贈した。MCP に続く2つ目の寄贈で、`SKILL.md` の形式変更は書かれていない。ChatGPT・Cursor・GitHub Copilot・VS Code を含む70超の基盤が採用し、公開スキルは100万件である。https://www.anthropic.com/news/donating-agent-skills-to-the-agentic-ai-foundation
- [新機能] **サブエージェントを本体のループへ畳む判断基準** — Anthropic が 10/22 の記事で、役割ごとのサブエージェントを並べるより1つのループに文脈と道具を段階的に渡すほうが品質・費用・待ち時間で勝った例を挙げ、移行キット `anthropics/single-agent-loop-kit` を案内した。文脈の膨張で性能が落ちるとき、並列に捨てられる文脈で走らせたいとき、道具の指示が衝突するときはサブエージェントを残すとしている。https://claude.com/resources/articles/building-agents-when-to-fold-subagents-into-your-main-agent-loop
- [動向] **HCLTech の Claude Partner Network 参加** — Anthropic が 10/21 に、HCLTech（従業員23万人超）を Global Premier パートナーに迎えた。HCLTech は専任の Anthropic Business Unit と Center of Excellence を置き、HCLSoftware は HCL BigFix・HCL AppScan などに Claude を組み込む。https://claude.com/resources/articles/hcltech-joins-claude-partner-network
- [据え置き] **退役ページ・リリースノート・Claude Duet・Fable 5.5** — モデル退役ページの Active は15件のままで、Haiku 4.5 は退役下限日の8日後も Active、Deprecation history の最新も 9/30 の Sonnet 4.5 である。`support.claude.com` のリリースノートの最上位は 10/21 の Claude Duet（10-22 既報。industry が公式ページで確認した）になった。Fable 5.5 は一次に出ていない。https://platform.claude.com/docs/en/about-claude/model-deprecations

### OpenAI / Codex / ChatGPT

- [料金+新機能] **Decisions API（`v1/decisions`）の GA** — OpenAI が 10/22 に、型付きの判定（確率・選択・採点）を返す Decisions API を `gpt-6-luna` で一般提供にした。キャッシュなしの入力は **$0.10 / 100万トークン**で出力は課金せず、速さは Responses API の約10倍としている。https://developers.openai.com/api/docs/guides/decisions
  - ベータ（10/6）からの追加: プロンプトキャッシュ、質問ごとの画像と `input_json`、関数呼び出しを含む会話履歴、1リクエスト400問（ベータは200問）
  - 運用: 組織の利用状況レポート、Private Link、GPT-Live からの直接呼び出し
  - 比較: TypeSafe AI の Jev（`jev-1.13.0`）は入力 $0.042 / 100万トークン・出力無料で、入力単価は Jev が約4割である
- [新機能] **プロジェクト単位のサービスティア制限** — OpenAI が 10/21 に、Platform の設定でプロジェクトごとに使えるサービスティアを選べるようにし、組織の設定で全プロジェクトのティアを制限できるようにした。https://developers.openai.com/api/docs/changelog
- [廃止] **OpenAI のレガシー GPT 群と Gemini API の Deep Research プレビューが本日停止** — OpenAI の廃止ページでは停止日が 10/23 のまま変わっておらず、`gpt-3.5-turbo`・`gpt-4`・`gpt-4-turbo`・`gpt-4.1-nano`・`o1`・`o1-pro`・`o3-mini`・`o4-mini`・`gpt-image-1` と各ファインチューン版が止まる。Google の `deep-research-pro-preview-12-2025` も同日に止まり、移行先は `deep-research-preview-04-2026` である。https://developers.openai.com/api/docs/deprecations
- [動向] **ChatGPT の広告主が10万社超** — GIGAZINE によると、OpenAI が ChatGPT の広告主が10万社を超え、広告を26カ国（中南米の14カ国を追加）に広げたと明らかにした。広告の年換算売上は8月末時点で $1B だった。https://gigazine.net/news/20261022-chatgpt-ads/
- [版更新] **Codex CLI `0.164.0-alpha.12`** — OpenAI は Codex CLI の pre-release を `0.164.0-alpha.12`（10/22）まで進め、`0.163.0-alpha.11.1` / `.11.2` も出した。安定版は `0.163.0`（10/15）のままである。https://github.com/openai/codex/releases
- [据え置き] **退役一覧・Codex changelog・ミスアライメント報告** — OpenAI の退役一覧は 10/14 の GPT-4 系、`learn.chatgpt.com` の changelog は 10/14 の GPT-5.5 retirement in Codex、ミスアライメント報告の First posted は 10/20 が最新のままである。

### Microsoft 365 Copilot / Agent 365

- **Outlook の Copilot Prioritize の退役**（ハイライト1参照）
- [料金+新機能] **Copilot Code の Frontier 展開** — MC1519871 によると、自然言語でアプリを作る Copilot Code が 10月下旬から、M365 Copilot ライセンスと従量課金（Copilot Credits）の対象になっている Frontier 利用者へ展開される。スペンディングポリシーで「Allow new Agents and services as they become available」が有効だと、管理者が何もしなくても使えるようになる。https://mc.merill.net/message/MC1519871
  - 既定値: クラウドのコーディングセッションは Web と PC で有効。ローカルのセッションは既定で無効で、M365 管理センターの Code execution location を Cloud and local にすると使える
  - 公開と共有: 作ったアプリは Copilot Managed Runtime に公開して組織内で共有でき、データへのアクセスは利用者本人の権限に従う。管理者が有効にすれば GitHub にドラフトの pull request を開ける
  - 経緯: 9/25 に「数週間以内に Frontier で展開」と発表されていた。Tech Community ブログは 10/21 に「本日から展開を始める」と書いている
- [新機能] **Cowork のロール別プラグイン** — Microsoft が 10/21 に、Cowork の Customize ページに Roles & Industry 欄を加え、営業・サービス・教育・法務のプラグインを今日から追加できるようにした。Power Platform コネクタも今後数週間で Cowork に順次加わり、MCP のフェデレーテッドコネクタで外部システムのデータを本人の権限のまま扱える。使わせるプラグインとコネクタは管理者が決める。https://techcommunity.microsoft.com/t5/microsoft-copilot-blog/what-s-new-in-cowork-expanded-plugins-and-role-based-skills/ba-p/4566221
- [新機能] **Projects in Copilot** — MC1519856（10/21）によると、Cowork の利用者は関連するタスク・ファイル・指示を1つのプロジェクトにまとめられるようになった。Cowork タブでは 10/20 に全世界で展開済みで、Frontier の新しい Home には 10月下旬〜11月中旬に入る。ファイルは OneDrive に既存の権限・秘密度ラベル・保持ポリシーのまま保存される。https://mc.merill.net/message/MC1519856
- [新機能] **Insights Agent V2 のフィードバック分析** — MC1520901 によると、エージェントの所有者は Copilot Chat の Insights Agent V2（Frontier）で、自分のエージェントへの評価と自由記述のコメント、その傾向の要約を確かめられるようになった。共有は既定でオフで、管理者が M365 管理センターの Agents > Settings > Agent feedback sharing で対象を選ぶ。https://mc.merill.net/message/MC1520901
- [新機能] **Copilot Notebooks の画像・表ファイル参照** — MC1519842 / MC1519841（10/21）によると、Copilot Notebooks の利用者は JPG / PNG の画像と CSV / TSV のファイルを参照ソースに加えられるようになった。10月から全世界で提供済みで、管理者の対応は要らない。https://mc.merill.net/message/MC1519842
- [新機能] **宣言型エージェントのマニフェスト 1.9** — Microsoft が 10/22 に、開発者がマニフェスト 1.9 で Agent Skills 標準に沿ったスキルのディレクトリを `agent_skills` で参照し、`Fabric` 機能で Microsoft Fabric のデータを会話の中で照会・可視化できるようにした。ルートの `instructions` は省略できるようになった。https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/whats-new
- [新機能] **Purview DLP のネットワーク層への拡張** — Roadmap 522096 / 566528 が 10/21 に Launched になり、管理者は Entra Global Secure Access の Internet Access と連携して、生成 AI サービスを含む外部アプリへ送られるファイルとプロンプトを DLP ポリシーで検査・ブロックできるようになった。https://www.microsoft.com/microsoft-365/roadmap?id=566528
- [予定] **Planner の Cowork 統合** — Roadmap 567315（10/21 更新）によると、利用者は Cowork の中で Planner のプラン・バケット・目標・タスクを表示・作成・更新し、承認すれば進捗を Planner に書き戻せるようになる。GA は November CY2026 である。https://www.microsoft.com/microsoft-365/roadmap?id=567315
- [予定] **Sales Development Agent** — Roadmap 573700（10/21 起票）によると、見込み客の調査・選別・接触を自律で行う営業向けエージェントが、M365 Copilot に January CY2027 に GA で加わる。https://www.microsoft.com/microsoft-365/roadmap?id=573700
- [据え置き] **Release Notes / ブログ各種** — M365 Copilot Release Notes の先頭は October 06, 2026 のままで、Agent 365 Blog・SharePoint Blog・Copilot ブログに新しい記事は無い。Cowork What's New とモデル・統制・前提条件の各ページも改訂されていない。

### Copilot Studio / Power Platform

- **Basic User ロールのコネクタ定義読み取り権限の削除**（ハイライト2参照）
- [予定] **Power Apps 生成ページのカスタム API 呼び出しと監視** — Roadmap 576282 / 576284（10/21 起票）によると、メーカーは生成ページから Dataverse のカスタム API を呼んでサーバー側の業務ロジックを動かせるようになり、Application Insights エクスポートを設定すれば読み込み・エラー・Data API 操作がコードなしで送られる。GA はどちらも December CY2026 である。https://www.microsoft.com/microsoft-365/roadmap?id=576284
- [予定] **モデル駆動アプリのフォーム入力支援の拡大** — Roadmap 575296 / 575295（10/21 起票）によると、利用者は AI のフォーム入力支援を、参照・リッチテキスト・複数選択の列（November CY2026）と、値が入っている列（December CY2026）でも使えるようになる。https://www.microsoft.com/microsoft-365/roadmap?id=575296
- [動向] **Gartner と Forrester の Leader 評価** — Microsoft が 10/22 に、Gartner の AI-Augmented Low-Code Application Platforms（2026・8回連続）と Forrester Wave の AppGen And Low-Code Platforms（Q4 2026）の両方で Leader に選ばれたと発表した。https://www.microsoft.com/en-us/power-platform/blog/2026/10/22/microsoft-named-a-leader-in-two-evaluations-of-next-generation-app-development-platforms/
- [据え置き] **What's New / 非推奨一覧 / Released Versions** — Copilot Studio What's New は 10/22 に再ビルドされたが `ms.date` 10/5 のままで、Customer Conversation ハーネスはまだ載っていない。非推奨一覧は 10/22 に `21682266` へ改訂されたが新しい節は無く、Released Versions は 2026.6.3 のまま114日動いていない。

### GitHub Copilot / GitHub

- [破壊的変更] **Copilot CLI `v1.0.103` の `--remote` 廃止** — GitHub が 10/22 に Copilot CLI `v1.0.103` を出し、起動時の `--remote` / `--no-remote` フラグを廃止した。リリース本文は代わりのホスティング・接続フラグを「より分かりやすくした」とだけ書き、名前を挙げていない。https://github.com/github/copilot-cli/releases
  - ACP セッション: 保存したサンドボックス設定と `--sandbox` / `--no-sandbox` を、再開時も含めて守るようになった
  - 管理設定: 管理者がモデルの既定を必須にしている環境で、セッションの再開が拒否されなくなった
  - その他: Gemini のツール呼び出しで nullable と enum のフィールドが 400 になる不具合を直し、同じリポジトリの worktree 間でローカル MCP のツール一覧のキャッシュを共有する
- [新機能] **Copilot impact dashboard の同業比較** — GitHub が 10/22 に、Copilot impact dashboard に「Industry comparison」を加え、エージェント利用者の割合と PR マージ率の差を、同じ規模・業種の中央値（参加が増えれば上位10%）と並べられるようにした。参加は既定オフの opt-in で、オフにすると表示とデータ提供が両方止まる。https://github.blog/changelog/2026-10-22-industry-comparisons-in-the-copilot-impact-dashboard
  - 比較群: 従業員規模3区分（1–999 / 1,000–4,999 / 5,000+）と10業種。母数が足りないときは全業種に広げる
  - 対象外: Copilot Business のライセンス割り当てだけに使う Enterprise は参加できず、結果は API やエクスポートに出ない（industry の記載）

### Google

- [新機能] **Meet の音声翻訳を63言語に拡大** — Google が 10/22 に、Meet の音声翻訳を Gemini 3.5 Live Translate で63言語に広げ、話されている言語を自動で判定するようにした。会議全体で1組の言語を設定する方式から、参加者ごとにオンにする方式へ変わる。https://workspaceupdates.googleblog.com/
  - 管理者: Gemini for Meet の設定が有効なら既定でオンで、OU・グループ単位で切り替えられる
  - 上限: 基本の Workspace プランと Google AI Pro は1会議90分、AI Expanded Access・AI Ultra Access・Google AI Ultra は8時間
  - 展開: Rapid Release は 10/22 から1〜3日、Scheduled Release は 11/2 から最大15日。ライブ配信・録画・CSE の会議・電話参加は対象外
- [予定] **Agent Compute Engine** — Google Cloud が 10/22 に、エージェントのセッションごとに専用の microVM を割り当てる基盤を公表し、数カ月内のプレビューを目標にした。サンドボックスは認証情報を持たず、Agent Gateway が通信の途中で資格情報を差し込む。単価と起動・再開時間は公表されていない。https://cloud.google.com/blog/topics/ai-infrastructure/agent-compute-engine-deep-dive
- [据え置き] **Gemini API / Gemini アプリ** — Gemini API changelog と Gemini アプリのリリースノートは、どちらも 10/13 の Gemini 4 Argon が最上位のままで、`blog.google` の AI RSS にも新着は無い。

### その他エージェント / 開発ツール

- [新機能] **Recursive のローカル向けコーディングモデル Flint** — Recursive が 10/21 に、MoE（総40B / アクティブ2.5B）のコーディングモデル Flint の重みを Apache 2.0 で Hugging Face に公開した。Master が HF の API で `private: false`・`gated: false`・safetensors 15ファイルを確認している。最大コンテキストは512k で、M4 Pro の MacBook Pro で毎秒125トークン超（自社計測）とするが、ベンチマークのスコアは示していない。出典の TestingCatalog 記事はスポンサー記事である。https://huggingface.co/RecursiveSI/flint
- [新機能] **Devin Review の Bitbucket 対応** — Cognition が 10/21 に、Devin Review を Bitbucket に対応させ、レビュー指摘をセッションのチャットへ引用できる「Quote in chat」（Cmd+I）を加えた。https://docs.devin.ai/release-notes/overview
- [据え置き] **Cursor・xAI・Orca・TypeSafe・MCP・HF の定点** — Cursor の changelog は 10/16、フォーラムは 10/12 が最上位のままで、`docs.x.ai` は 10/14、Orca は `v1.4.237`（10/21）のままである。TypeSafe は `jev-latest` → `jev-1.13.0` のままで、MCP ブログ・Hugging Face の登録8 org・Apple Developer News にも新着は無い。

### 市場・企業 / セキュリティ

- **LiteLLM 1.107.0 の情報窃取マルウェア**（ハイライト3参照）
- [セキュリティ+動向] **米大手銀行の AI エージェント締め出し** — The Decoder が引く Axios によると、Morgan Stanley が顧客の認証情報で入る AI エージェントを全面的に遮断し、JPMorgan・Bank of America・Citi も同様の対応を取っている。対象は銀行の承認なしにブラウザ経由で口座へ入るエージェント（Computer Use や OpenClaw）で、銀行側はエージェントが利用者の指示で動いているかを見分けられない点を理由に挙げた。https://the-decoder.com/major-us-banks-are-locking-out-ai-agents-that-log-in-with-customer-credentials/
- [動向] **Gartner 調査で AI の大きな効果は13%** — Gartner が 10/22 に、技術責任者 2,002人への調査で「大きな、または変革的な効果」を得た企業は **13%** と公表した。58%の CIO が AI によるコスト削減を求められる一方、51%は技術基盤の運用費が AI で増えると見ている。調査対象の国は記事に書かれていない。https://the-decoder.com/only-13-percent-of-companies-see-real-returns-from-ai-gartner-survey-finds/
- [据え置き] **買収協議と国内市場データ** — Amazon × Decart、Nvidia × Reflection AI の買収協議に続報は無く、IDC Japan・MM総研・NRC の新規公表も無い。

## 直近の注目予定

- **10/23（本日）**: OpenAI のレガシー GPT スナップショットと Gemini API の `deep-research-pro-preview-12-2025` が停止
- **10月中**: Dataverse の Basic User ロールからカスタムコネクタ定義の読み取り権限が外れる（MC1520706）
- **10月後半**: claude.ai（米国）で Democracy Works の投票情報を表示 ／ Claude Fable 5.5（リークのみ・未確認）
- **10月下旬**: Copilot Code が Frontier で展開を始める（MC1519871）
- **10月下旬〜11月中旬**: Researcher の Critique / Council が退役（MC1515927、Act by 11/14） ／ Projects in Copilot が Frontier の新しい Home に展開（MC1519856）
- **10/26**: Outlook の Copilot Prioritize の退役が始まる（MC1519861） ／ Copilot Studio の Copilot Chat エージェント強化が GA（MC1518233） ／ Dataverse で .NET Framework 4.8 のプラグインパッケージが使える（MC1515315）
- **10/27〜29**: PPCC 2026（ラスベガス）
- **10/30**: ChatGPT Pro 200 の Work / Codex 利用枠が変更（二次・内容は割れている） ／ Gmail Live の Workspace への順次展開が完了（最大15日）
- **10/31**: MCP サーバー認定の旧申請経路が終了 ／ DeepSeek の Search・Fetch API の無料提供が終了
- **11/1**: CSP 価格表プレビューに Copilot の新オファーが載る ／ Codex の28日間「改善かリセット」の終了（二次）
- **11/2**: xAI `grok-imagine-image-quality` が退役 ／ Meet の63言語音声翻訳が Scheduled Release へ展開開始
- **11/4**: Entra で一般ユーザーのブループリント作成が既定オン（MC1506733）
- **11月上旬〜中旬**: GPT-6 Astra / Claude Fable 5.1 が Copilot Chat と Word / Excel / PowerPoint の UBB モデルとして展開（MC1519122）
- **11/12**: Copilot Studio の GPT-4.1 / GPT-5 系が退役（MC1506318） ／ Anthropic Usage Policy 改定版が発効 ／ OpenAI → Cursor のモデル供給停止予定（一次未読）
- **11月**: Planner の Cowork 統合が GA（Roadmap 567315）
- **11月中旬**: Copilot Analytics でエージェントデータのエクスポートが可能に（MC1288531）
- **11/15**: Dataverse for Teams 環境とアンマネージド開発者環境の新規作成が停止
- **11/16**: GitHub Copilot が Claude Opus 4.8・Opus 5・GPT-5.6 Terra を廃止 ／ Dataverse のプロンプト列が複数行テキスト出力に対応（MC1515841）
- **11/17**: Work IQ の業務アプリ統制がパブリックプレビュー（MC1518036） ／ Gems が Gemini アプリの設定パネルへ移動 ／ Gemini API の TTS・Live プレビュー5種が停止（最短日）
- **11/17〜20**: Microsoft Ignite
- **11/24 以降**: `claude-opus-4-5-20251101` の暫定退役日（確定日ではない）
- **11月下旬〜12月上旬**: Clipchamp の「Create a video」に管理者制御（MC1518034）
- **11/30**: Azure DevOps コネクタの旧接続が認証不可に（MC1508508） ／ App Builder と vibe.powerapps.com が退役 ／ `claude-sonnet-4-5-20250929` が Claude API から退役 ／ OpenAI の Evals・`v1/prompts`・Agent Builder が停止 ／ Gemini 4 Argon の導入価格が終了
- **12/1**: M365 Copilot の前提サブスク不要オファー開始、現行「(add-on)」オファーの CSP 販売終了 ／ Copilot Business の従量課金が既定オン ／ Gemini 4 Argon の単価が $4/$20 に倍増
- **12月上旬**: エクスプローラーの OneDrive Copilot 操作の一部が削除（MC1515940）
- **12月**: Power Apps 生成ページのカスタム API 呼び出しと Application Insights 連携が GA（Roadmap 576282 / 576284）
- **12/14**: claude.ai/design の単体サイトが閉鎖
- **12/15**: アンマネージド開発者環境が停止
- **12/31**: Claude Security の無償クレジット（月 $25,000×2か月）の対象期間が終了 ／ E7 + Copilot Studio 容量パックの Buy 5 Get 5 が終了
- **2027-01-06**: OpenAI `tts-1` / `tts-1-hd` / `gpt-4o-mini-tts` 2版が停止
- **2027年1月**: Copilot Studio の Teams アプリで編集ができなくなる（2月に削除。MC1511056） ／ GitHub Copilot ハーネスの Computer Use が GA 予定（576272） ／ Sales Development Agent が GA（Roadmap 573700）
- **2027-01-14**: OpenAI の GPT-4o・GPT-4o mini・GPT-4.1・GPT-4.1 mini が API から削除（→ `gpt-6-luna`）
- **2027-01-15**: アンマネージド開発者環境の削除開始 ／ Claude Code Review の Enterprise 向けクレジット請求期限
- **2027-03-01 以降**: Gems 廃止（Business / Enterprise）
- **2027年3月末**: Outlook の Copilot Prioritize の削除が完了（MC1519861） ／ SharePoint / OneDrive の `.agent` 形式エージェントが動かなくなる（MC1511052）
- **2027-04-01**: OpenAI `gpt-5.1` / `gpt-5.3-codex` / `gpt-5.4-nano` が停止

## 改善メモ

- 新規提案: Master が B-086（Claude Platform release notes を `daily-sources.md` に登録し、RSS で日付ごとの項目数を前回と突き合わせる。10/20・10/21 の項への後からの追記を本日まで検出できなかった）を起票した
- 継続提案: Master は B-036・B-037・B-043 を見送り候補に挙げた ／ Copilot は docset 全件突合を本日も未実施（追跡ページ約30本の `updated_at` 突合と toc.json で代替） ／ industry は継続5件（B-040 が10回目）で、B-007・B-023 を見送り候補に挙げた
- 障害の変化: 3ソースとも無し
- ソース間の差分・矛盾:
  - ハイライトは Master が Claude Code stable 更新・Decisions API・web fetch 制御、Copilot が Prioritize 退役・Basic User 権限・Copilot Code、industry が LiteLLM・Claude Code `2.1.307` を選んだ。本サマリーは選定基準1（期限・発効）の2件を先に採り、3件目は鍵の入れ替えが当日要る LiteLLM を採った。Copilot Code は既報（9/26）の続報としてカテゴリに置いた
  - Claude Code `2.1.307` は Master が `[破壊的変更+新機能]`、industry が `[新機能]` で割れた。チェックアウト hook の既定タイムアウトで既存のセッション準備が失敗しうるため `[破壊的変更+新機能]` を採った
  - Decisions API は industry が「単価は書かれていない」とし、Master は入力 $0.10 / 100万トークン・出力無課金と書いた。Master はガイドページを出典に挙げているため Master の記述を採った
  - ChatGPT Pro 200 の 10/30 の枠変更は、引き続き Master が「半減（二次）」、industry が「Plus 比10倍」と書いており、二次情報のまま割れている
