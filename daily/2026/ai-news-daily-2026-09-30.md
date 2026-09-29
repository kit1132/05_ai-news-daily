# AI News Daily Summary — 2026-09-30

OpenAI DevDay（9/29）の翌朝である。OpenAI は GPT-6.1 Sol を GPT-6 Sol と同じ入出力単価で出し、GitHub Copilot も同日に GA した。一方で ChatGPT Pro 200 の利用枠を 10/30 から半減し、$500 の Pro 500 を新設したと報じられた。Claude Code `2.1.285` は管理設定 `allowedProviders` を加え、第三者プロバイダの `claude -p` を auto mode で起動するようにした。Microsoft 側では Copilot Studio に Hooks（preview）と推定クレジット表示の一次ページが出た。

## 今日のハイライト

### 1. [料金] ChatGPT Pro 200 の利用枠が 10/30 に半減し、$500 の Pro 500 が新設された — $200 で足りていた1人あたり費用の試算が崩れる

**要点**: OpenAI が DevDay で、Pro 200 の Work・Codex 枠を 10/30 から半減すると発表したと報じられた。同じ使い方を続けるなら $500 の Pro 500 が前提になり、「Pro は月 $200」という試算は引き直しになる。

**詳細**: 報道ベースである（`openai.com` はオリジン403で一次未確認）。

- Pro 200 の変更（10/30 から）:
  - Work・Codex の利用枠: Plus 比 **20倍 → 10倍**
  - GPT-6 Pro のチャット: 週200件 → 100件
  - 既存契約者は 10/29 まで現行枠のままで、年末に失効する $2,500 の一回限りのクレジットが付く
- Pro 500（月額 $500）: 利用枠は Plus 比 25倍。GPT-6 Astra の高速版 Astra Ultrafast（Codex で最大毎秒300トークン・標準の最大8倍）と常駐エージェント dots を含む。Ultrafast を使える個人プランは Pro 500 だけで、法人は Enterprise で提供される
- 01 Master は「9/30 に Pro 200 の新規受付再開」も二次情報として挙げている

- https://www.engadget.com/2272106/openai-adds-dollar500-pro-subscription-nerfs-its-existing-dollar200-tier/
- https://thenextweb.com/news/openai-devday-pro-200-usage-cut-pro-500-plan
- https://www.androidheadlines.com/2026/09/openai-launches-500-pro-plan-reduces-200-tier.html

### 2. [料金+新機能] OpenAI が GPT-6.1 Sol を公開し、GitHub Copilot でも同日 GA した — 入出力は据え置きのまま、キャッシュ単価が半減しキャッシュ書き込みに課金が付いた

**要点**: OpenAI が `gpt-6.1-sol` を $2 / $10 で公開した。Astra に迫る性能を Astra 標準価格の1/5で出すとしている。キャッシュ読み取りは半額になったが、書き込みは新たに課金される。Copilot では Pro+ 以上で今日から選べ、Sol 系の単価表は 6.1 基準に差し替わる。

**詳細**:

- 料金（1M トークンあたり・272K トークン以下）: 入力 $2 ／ キャッシュ読み取り **$0.10**（GPT-6 Sol は $0.20）／ キャッシュ書き込み $2.50（新設）／ 出力 $10。272K 超は $4 / $0.20 / $15。Fast モードは2倍、Batch / Flex は50%引き
- 仕様: コンテキスト 1.05M（入力最大 922K）／ 最大出力 128K ／ 知識カットオフ 2026-04-30。Chat Completions / Responses / Batch に対応し、ツール呼び出しには Responses API が要る。Realtime・Fine-tuning・Assistants は非対応
- 同日の API 変更:
  - Ultrafast: `service_tier: "ultrafast"` で GPT-6 Astra を高速実行する。単価は $60 / $6 / $300 で標準（$10 / $1 / $50）の6倍。EU データ保管には対応しない
  - Agents API: OpenAI がホストするブラウザで computer use を実行できるようになった。サイトへのアクセス承認とサインインは開発者側のアプリで処理する
- 提供先: Codex と ChatGPT Work にも同日入った。GitHub Copilot は Pro+ / Max / Business / Enterprise で段階展開し、既定で有効になる。Pro は対象外で、課金はプロバイダ定価の従量課金

- https://developers.openai.com/api/docs/changelog
- https://developers.openai.com/api/docs/pricing
- https://developers.openai.com/api/docs/models/gpt-6.1-sol
- https://github.blog/changelog/2026-09-29-gpt-6-1-sol-in-github-copilot

### 3. [破壊的変更+新機能] Claude Code 2.1.285 で第三者プロバイダの `claude -p` も auto mode で起動するようになった — 権限モード未設定のヘッドレス実行は確認なしで動く

**要点**: Anthropic が 9/29 の `2.1.285` で、Bedrock などの第三者プロバイダやテレメトリ無効の環境でも、権限モード未設定の `claude -p` と Python Agent SDK を auto mode で起動するようにした。前版の対話セッションに続き、自動化の既定も auto になった。管理設定 `allowedProviders` で接続先も絞れる。

**詳細**:

- 既定・挙動の変更:
  - `claude -p` / Python Agent SDK: 第三者プロバイダかテレメトリ無効で、権限モードが未設定なら auto mode で起動する。`--permission-mode` は引き続き優先される
  - バックグラウンドの Bash / PowerShell: 時間制限で停止するようになった（既定30分・最大2時間）
  - sandbox: プロジェクト設定では、管理者が必須にした sandbox を広げたり止めたりできなくなった
  - カスタム `ANTHROPIC_BASE_URL`: 1M コンテキスト対応モデルでは 1M を使う。200K で止まるゲートウェイでは `/autocompact 200k` が要る
- 追加:
  - `allowedProviders`: 端末が使える API プロバイダ（Anthropic API・カスタムエンドポイント・Bedrock・Mantle・Vertex AI・Foundry・Claude Platform on AWS・Cloud gateway）を管理設定で限定する
  - `CLAUDE_CODE_DISABLE_WEB_FETCH`: WebFetch ツールを環境変数で無効にする
  - `claude --desktop` / `claude plugin configure`: デスクトップアプリで開く、プラグインの未設定項目を表示・保存する
- 修正: `ANTHROPIC_AUTH_TOKEN` で認証したセッションが組織ポリシーを読み込まなかった問題、PowerShell ツールの権限検査がパーサ起動失敗時に deny / ask ルールを飛ばしていた問題
- npm は 9/29 17:32 UTC 時点で `{stable: 2.1.277, latest: 2.1.284, next: 2.1.285}` で、`2.1.285` はまだ next タグにある

- https://code.claude.com/docs/en/changelog
- https://www.npmjs.com/package/@anthropic-ai/claude-code

## カテゴリ別まとめ

### Claude / Anthropic

- **Claude Code 2.1.285**（ハイライト参照・3）
- [セキュリティ] **9/29 のエラー率上昇とサインイン障害** — Anthropic の claude.ai / Claude Code / Cowork / API で、9/29 14:00〜14:59 UTC（JST 23:00〜23:59）にエラー率が上がった。一次対処の後も別の問題で SSO と Sign in with Apple のサインインが通らず、新規チャットやファイルアップロードも止まった。16:27 UTC に解決済みになったが、この時間帯のメッセージの一部は保存されていない可能性がある。https://status.claude.com/history.rss
- [動向] **NVIDIA との企業向けエージェント統制** — Anthropic が NVIDIA と組み、企業向けエージェントの統制を強化すると発表した（9/28）。
  - Claude Managed Agents: 認証情報を別の vault に置いてエージェントから見えなくし、監査証跡と数時間規模のセッション、顧客管理インフラでの実行に対応する
  - NVIDIA OpenShell: 明示的に許可した操作以外を止めるオープンソースの実行環境（Apache 2.0）
  - 導入企業として Notion / Rakuten / Asana が挙がっている
  - https://claude.com/blog/giving-companies-more-control-over-their-ai-agents-with-nvidia
- [動向] **Asana の人とエージェントの混成チーム** — Anthropic が 9/29、Asana が Claude で混成チームを作った事例を公開した。エージェントの長期メモリに書き込めるのは管理者と編集者だけにしている。https://claude.com/blog/agents-you-can-coach-how-asana-builds-human-agent-teams-with-claude
- [据え置き] **Platform release notes と Sonnet 4.5 の退役** — Anthropic の release notes は 9/28 の Sonnet 5.5 が最上位のままで、`claude-sonnet-4-5-20250929` は暫定退役日（9/29）を過ぎても退役告知が出ていない。モデル退役ページは Active 15件のままである。https://platform.claude.com/docs/en/about-claude/model-deprecations
- [据え置き] **控訴裁判決後の対応** — Anthropic が DC 巡回区控訴裁判所の 9/25 判決（既報）に対し再審理や最高裁への申立てを出したという情報は、まだ無い。

### OpenAI / Codex / ChatGPT

- **ChatGPT Pro 200 の枠半減と Pro 500**（ハイライト参照・1）
- **GPT-6.1 Sol・Ultrafast・Agents API の computer use**（ハイライト参照・2）
- [新機能] **ChatGPT の dots と Space** — OpenAI が DevDay で、ChatGPT に常時稼働のエージェントと共有ワークスペースを加えたと報じられた（二次のみ）。
  - dots: GPT-6 Astra で動き、専用のクラウド PC とブラウザで24時間作業する。Slack / Teams から操作でき、当日から Pro / Business Premium で1プラン1つ使える。EEA・スイス・英国の Pro は当面対象外
  - ChatGPT Space / Pages: チームと ChatGPT と dot が同じ文書・スライド・タスクで作業する。Pro / Business / Enterprise のデスクトップと Web で使える
  - Plugin extensions: 開発者がサイドバーの置き場や会話横の対話型パネルを持つプラグインを作れる
  - https://9to5google.com/2026/09/29/openai-dots-agent/
  - https://www.axios.com/2026/09/29/openai-dev-day-2026-dots-space-sol
- [新機能] **Codex のクラウド環境と Codex Security Cloud** — OpenAI が DevDay で、チームで設定と権限を共有できる再利用型クラウド環境を Codex に加えた。Codex Security Cloud は GitHub リポジトリをオンデマンドか定期でスキャンし、新規コミットも継続確認して検証済みの修正案を用意する。GitHub・GitLab 向けのコードレビュー機能も加わった。https://techcrunch.com/2026/09/29/openai-gives-codex-reusable-cloud-environments-that-work-across-devices/
- [予定] **Decisions API** — OpenAI が、Luna に固定の選択肢から1つを150msで選ばせる Decisions API を limited preview で発表したと報じられた（二次のみ）。https://decrypt.co/379584/openai-ai-agents-computers-devday-2026-everything-announced
- [新機能] **Codex rust-v0.159.0** — OpenAI が Codex の安定版 `rust-v0.159.0`（9/29 08:05 UTC）で、応答中でも新しい入力で割り込める `instant_interrupt` を opt-in で加えた。自動 follow-up 提案（`tui.prompt_suggestions`）と同梱の plugin-creator skill は削除され、`.aws` は既定で保護されるようになった。pre-release は `rust-v0.161.0-alpha.2` まで進んだ。https://github.com/openai/codex/releases/tag/rust-v0.159.0
- [廃止] **レガシー4モデルの停止確定** — OpenAI の廃止ページで、`gpt-3.5-turbo-instruct` / `babbage-002` / `davinci-002` / `gpt-3.5-turbo-1106` が「過去の廃止」に移った。前日は停止日 9/28 の経過後も予定節に残っていたが、停止の実施が一次で確認できた。https://developers.openai.com/api/docs/deprecations
- [据え置き] **最上位モデルの訓練停止** — OpenAI は DevDay 時点でも訓練停止（9/25）の解除を発表しておらず、`alignment.openai.com` は報告9本・notices 3本のままである。https://www.nbcnews.com/tech/tech-news/openai-pauses-training-latest-models-agents-searched-us-government-sit-rcna600098
- [据え置き] **退役ページと Developer Community** — OpenAI の退役ページの最新告知は 9/11 の `gpt-5.4-cyber`（10/1 削除）、Developer Community Announcements は 9/22 が最上位のままである。

### GitHub Copilot / GitHub

- [破壊的変更+新機能] **Copilot CLI v1.0.89** — GitHub が Copilot CLI の安定版 `v1.0.89`（9/28）で `.claude/rules` のルールファイルを custom instructions として読むようにし、Fast プロファイルを廃止した。Claude Code 向けに書いたルールが Copilot CLI の挙動も変え、保存済みの Fast 設定は Balance で動く。
  - モデルピッカー: GPT-6 Sol / GPT-6 Luna を追加し、`claude-opus-5.5` に対応した
  - プラグイン: 無効として記録済みのものは読み込まれなくなるので、`copilot plugin enable` で戻す
  - 修正: MCP ツールのスキーマで `anyOf` の横に `type` か `properties` があると Gemini モデルが毎回 400 になっていた問題
  - pre-release `v1.0.90-3` で `--mcp-github-auth` が加わり、GitHub 認証を渡す MCP サーバーを承認済みの接続元に限定できる（`v1.0.90-4` まで進行）
  - https://github.com/github/copilot-cli/releases/tag/v1.0.89
- [新機能] **外部カスタムプロパティ** — GitHub が 9/29、CMDB や開発者ポータルの値を読み取り専用のカスタムプロパティとしてリポジトリに同期する API をパブリックプレビューで公開した。最初の連携先は Port.io で、同日に Dependabot の実行ランナーをリポジトリ単位で指定する設定も加わった。https://github.blog/changelog/2026-09-29-bring-business-context-with-external-custom-properties

### Microsoft 365 Copilot / Copilot Studio / Power Platform

- [新機能] **Copilot Studio の Hooks（preview）** — メーカーが、GitHub Copilot ハーネスのセッション開始・プロンプト送信・ツール実行前後・エラーの各イベントでワークフローを必ず走らせられるようになった（Learn `ms.date` 2026-09-29）。エージェント任せだったガードレールを決定的に掛けられるが、フックが失敗・タイムアウトするとエージェントは何もなかったものとして続行する。
  - イベント: Start / User prompt submitted / Error / Pre tool use / Post tool use / After tool failure の6種
  - 遮断できるのは Pre tool use だけ: `permissionDecision` に `deny` を返す。他は `additionalContext` や `modifiedParameters` などで値を差し替えられるが止められない
  - 設定場所: エージェントのコマンドバーの More options > Hooks。動くのは保存・公開後で、紐づけるワークフローも公開済みである必要がある
  - https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-experience/hooks-overview
- [新機能] **Copilot Studio の推定クレジット表示** — メーカーは、テスト中の会話（Preview）と評価の実行（Evaluate）で推定消費クレジットをほぼリアルタイムで確認できるようになった（Learn `ms.date` 2026-09-28）。確定値は Monitor に数時間遅れで出て、`Total estimated credits used` が課金の基準値になる。対応する Roadmap 571194〜571196 は、GA 期日当日の今日も `In development` のままである。https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-experience/billing-credit-understand-display
- [仕様] **Work IQ（preview）** — Learn `add-work-iq`（`ms.date` 2026-09-28）は、Work IQ を GitHub Copilot ハーネス上で動き Copilot Credits で課金されるツールとして説明している。管理者が M365 管理センターで有効にしない限り読み取り専用で動き、管理者は Work IQ 用に別の支出ポリシーを作る必要がある。従来のワークロード別ツールは後方互換の旧来体験で、Work IQ の改称ではないと明記する。https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-experience/add-work-iq
- [予定] **Copilot Studio の9月 GA 期日** — Roadmap の Copilot Studio 起票22件は全件 `In development` のままで、GA 期日が September CY2026 の **14件**は本日が期日である。
- [予定] **Word・Cowork の Legal plugins** — Microsoft が Roadmap **571884** で、法務向けの要約・起案・レビュー・赤入れのスキルを持つプラグインが Word と Cowork で GA すると起票した（GA 期日 October CY2026）。4月から Frontier で出ていた Word の Legal Agent について、GA 時期が一次で示されたのは初めてである。9/28 の Roadmap バッチ（7件）のうち対象はこの項と下の2件である。
- [予定] **OneDrive の Prompt Gallery** — Microsoft が Roadmap **571308** で、OneDrive の Copilot に Create / Analyze / Find / Collaborate 分類のプロンプト集が入ると起票した（Preview・GA とも October CY2026）。
- [予定] **Purview の自動ラベル付け上限** — Microsoft が Roadmap **571309** で、SharePoint と OneDrive の自動ラベル付け上限をテナントあたり1日 **10万 → 50万**ファイルへ引き上げると起票した（GA 期日 November CY2026・GCC / GCC High / DoD 対象）。
- [動向] **Frontier Accelerate for Marketplace** — Microsoft が Partner Center の9月アナウンスに、適格パートナーの Marketplace 出品を支援するプログラムの提供開始を加えた（9/28）。Premium 版では最大 **30,000 USD** の Azure スポンサーシップが付く。https://learn.microsoft.com/en-us/partner-center/announcements/2026-september
- [観測] **Learn の改訂差分が特定できないページ** — Copilot Studio の `authoring-agent-status`（Review problems パネル）と M365 の `copilot-flex-routing`（EU / EFTA）の `ms.date` が 2026-09-29 へ動いたが、改訂差分は特定できていない。Flex routing の本文は、ピーク時の推論先が米国・カナダ・オーストラリアであることを書く。
- [据え置き] **Release Notes・What's New・Power Platform の定点** — M365 Copilot Release Notes の先頭は **September 23, 2026** のままで、Copilot Studio What's New は July 2026 節のまま GitHub Copilot ハーネスの GA（8/3）を58日反映していない。Power Platform のブログ・Release Wave・Released Versions（Copilot Studio 最新ビルド 2026.6.3）も動いていない。https://learn.microsoft.com/en-us/copilot/microsoft-365/release-notes

### Google

- [新機能] **Google Vids の AI ナレーション** — Google が Google Vids の AI ナレーションを Gemini 3.8 Flash Lite TTS に上げた（9/29）。http://workspaceupdates.googleblog.com/2026/09/create-more-natural-expressive-ai-voiceovers-in-Google-Vids-with-upgraded-Gemini-3.8-Flash-Lite-TTS.html
- [据え置き] **Gemini API changelog** — Google の Gemini API changelog は 9/22 の 3.8 Flash TTS GA が最上位のままで、新規の料金改定・廃止告知も Gemini 4 の公式発表も無い。https://ai.google.dev/gemini-api/docs/changelog

### Cursor / Devin / xAI / オープンウェイト

- [据え置き] **Cursor の新モデル告知** — Cursor の changelog は 9/23、フォーラム Announcements は 9/21 の Grok 4.7 が最上位のままである。Opus 5.5・GPT-6 Sol / Luna・Sonnet 5.5 の提供開始は8日目も告知されておらず、GPT-6.1 Sol の告知も無い。
- [観測] **xAI・Devin の一次** — xAI と Devin に 9/28〜29 付の新規は検出していない。
- [据え置き] **MCP・Hugging Face・Apple** — `blog.modelcontextprotocol.io` は 8/22、`developer.apple.com/news/` は 9/18 が最上位のままである。Hugging Face の登録8 org にも 9/28 以降の新規リポジトリは無い。

### 市場・企業

- [据え置き] **市場データ** — IDC Japan・MM総研・NRC・Similarweb はいずれも新規公表が無い。MM総研の2026年版個人利用率調査もまだ見つかっていない。

## 直近の注目予定

- **9/30（本日）**: Copilot in SharePoint の GA 展開開始 ／ Copilot Studio の Roadmap 14件が GA 期日 ／ Gemini の `gemini-omni-flash-preview` が停止 ／ OpenAI の現行 OneGov 契約が失効 ／ CSP の M365 E5 / E7 / Copilot プロモーション終了 ／ Copilot Dev Camp Summit ／ Clinical Applications スペシャライゼーションの受付開始
- **10/1**: CSP 成長マージンの一般提供 ／ Microsoft CSP ソフトウェア価格改定が発効 ／ OpenAI の `gpt-5.4-cyber` が停止（移行先 `gpt-5.6-cyber`） ／ Copilot 既存顧客の前払い必須化 ／ ChatGPT for Word の Word アクセスが既定オンへ
- **10/2**: GitHub Copilot が4モデルを廃止 ／ Gemini の `gemini-2.5-flash-image` が停止
- **10/5**: Gemini の `antigravity-preview-05-2026` が停止 ／ GPT-Rosalind の課金開始
- **10/13**: Office / Project / Visio LTSC 2021 のサポート終了 ／ 新しい Copilot の Partner Digital Airlift
- **10/14**: GitHub SSH の新規 RSA 鍵が 3072 ビット以上必須に ／ GPT-5.5 が ChatGPT / Codex から退役
- **10/15 以降**: `claude-haiku-4-5-20251001` の暫定退役日
- **10月**: Copilot Studio エージェントがコスト管理の対象に ／ Word・Cowork の Legal plugins GA（571884） ／ OneDrive の Prompt Gallery（571308） ／ PowerPoint の Copilot 非同期通知（Mac）GA
- **10/19**: GitHub Copilot が5モデルを廃止
- **10/21**: GitHub Copilot の新機能既定ポリシーの設定期限（10/22 発効）
- **10/23**: OpenAI のレガシースナップショット12件が停止
- **10/27〜29**: PPCC 2026（ラスベガス）
- **10/29**: ChatGPT Pro 200 の現行枠の最終日（二次）
- **10/30**: ChatGPT Pro 200 の Work / Codex 利用枠が半減（二次）
- **10/31**: MCP サーバー認定の旧申請経路が終了 ／ OpenAI Evals が読み取り専用化
- **11月**: Copilot Studio の Maker guidelines（570967）GA ／ Purview 自動ラベル付け上限の引き上げ（571309）
- **11/2**: GitHub Actions の `pull_request_target` 既定無効化が公開リポジトリで強制開始 ／ M365 Copilot Business の従量課金が既定オン
- **11/4**: GitHub SSH `ssh-rsa` の1回目のブラウンアウト
- **11/12**: OpenAI → Cursor のモデル供給停止予定（一次未読）
- **11/15**: Microsoft Release Planner 退役
- **11/17〜20**: Microsoft Ignite
- **11/21**: OpenAI GPT-5.6 Sol の期間限定価格の下限
- **11/30**: OpenAI の `v1/prompts`・Evals・Agent Builder が停止
- **12/1**: OpenAI `gpt-image-1-mini` / `gpt-image-1.5` / `chatgpt-image-latest` が停止
- **12/9**: GitHub SSH `ssh-rsa` の2回目のブラウンアウト
- **12/11**: OpenAI GPT-5 / o3 系スナップショットが停止
- **12/31**: 非営利向け M365 Copilot の併用プロモーション終了 ／ Gemini 3.8 Flash の導入価格が終了 ／ Pro 200 既存契約者の $2,500 クレジットが失効（二次）

## 改善メモ

- 新規提案: 3ソースとも無し
- 継続提案: Master は2件を再確認（最多 B-035 npm dist-tags・45回目）／ Copilot は B-012・B-061（9/28 の Roadmap バッチを1日遅れで検知）・B-074・B-076（Flex routing・Review problems パネルの改訂差分を特定できず）の回数を更新 ／ industry は B-004（92回目）ほか
- 障害の変化: industry で The Next Web（`thenextweb.com`）のゲートウェイ拒否が新規発生（WebSearch で代替）。Master・Copilot は無し
- ソース間の差分・矛盾:
  - Claude Code `2.1.285` について、Master（04:10 頃生成）は「npm の next に出たが changelog に項目が無く中身不明」、industry（05:10 頃生成）は `allowedProviders` などの追加を報じた。本サマリー生成時に changelog を確認すると 9/29 付で掲載されていたため、Master の生成時点では未掲載だったと判断し、changelog の記載でハイライト3を書いた。`claude -p` の auto mode 既定化は両ソースとも拾っていない
  - OpenAI の旧4モデル停止は、前日サマリーの「予定節に残ったまま」という観測を industry の本日確認（過去の廃止へ移動）で更新した
  - タグ: Master の Anthropic 障害（動向）は手順の「可用性障害の事後」に当たるためセキュリティとした。industry の DevDay の dots（動向）は当日から使えるため新機能、訓練停止の続報なし（セキュリティ）は新しい事実が無いため据え置きとした。Copilot の推定クレジット表示（料金）は単価・課金方式の変更ではないため新機能、Pro 200 の変更は Master の料金+予定・industry の料金のうち料金を採った。Copilot の Release Communications RSS（動向）は 571884 の項へ寄せた
- 手順の不整合（前日から継続）: `scripts/check-update-tags.py` は「ハイライト参照」を含む行だけを検査対象外にするため、本日は `（ハイライト参照・N）` の形で参照行を置いた（手順の `（ハイライトN参照）` は検査の除外語「ハイライト参照」に一致しない）
