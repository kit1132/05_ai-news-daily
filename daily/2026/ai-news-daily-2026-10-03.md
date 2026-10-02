# AI News Daily Summary — 2026-10-03

退役日と統制の前提が動いた日である。OpenAI は API の7モデルに停止日を付け、`gpt-5.1` 系は 2027-04-01、`tts-1` 系は 2027-01-06 に止まる。Microsoft は Agent 365 で条件に応じてエージェントを自動でブロックするルールと、カスタム MCP サーバーの承認経路を入れた。Copilot in SharePoint では画像生成・Advanced Autofill・サイト分析が今月から Copilot Credits を消費する。

## 今日のハイライト

### 1. [廃止] OpenAI が API の7モデルに退役日を付けた — `gpt-5.1` 系は 2027-04-01、`tts-1` 系は 2027-01-06 に止まり、TTS の移行先は Realtime 系になる

**要点**: OpenAI が 10/1 付で退役告知を2件出した。`gpt-5.1` / `gpt-5.3-codex` / `gpt-5.4-nano` は 2027-04-01、TTS 4モデルは 2027-01-06 に停止する。TTS の移行先は専用 TTS ではなく `gpt-realtime-2.1-mini` で、音声合成を単体 API で組んだ構成は呼び出し方から見直しになる。

**詳細**:

- テキスト系（停止 2027-04-01）:
  - `gpt-5.3-codex` → `gpt-6-sol`
  - `gpt-5.1` → `gpt-6-sol`
  - `gpt-5.4-nano` → `gpt-6-luna`
- TTS 系（停止 2027-01-06）: `tts-1` / `tts-1-hd` / `gpt-4o-mini-tts-2025-03-20` / `gpt-4o-mini-tts-2025-12-15` の4つ。移行先はすべて `gpt-realtime-2.1-mini`
- 9/11 告知の `gpt-5.4-cyber` は 10/1 に停止日を迎えた
- 両ソースとも退役ページの更新を1〜2日遅れで捕捉した

- https://developers.openai.com/api/docs/deprecations

### 2. [新機能+仕様] Microsoft が Agent 365 にエージェントの自動統制ルールとカスタム MCP サーバーの承認経路を入れた — 統制が「一覧を見て手で止める」から「条件で自動適用する」に変わった

**要点**: 管理者は M365 管理センターで、条件に応じてエージェントを自動でブロックしたり公開要求を却下したりするルールを作れるようになった（プレビュー）。開発者が登録したカスタム MCP サーバーは管理者の承認を経ないと呼べない。ツール統制は MCP からプラグイン・スキル・コネクタへ広がり GA した。

**詳細**: 一次は Tech Community の Agent 365 Blog「What's new in Agent 365 - September 2026」（9/30）で、同ブログの更新は 8/6 以来である。登録エージェントは5月の提供開始から約 **5,000万**、数万組織に達した。

- Agent Management Rules（プレビュー）: 所有者の有無・タグ・Entra Agent ID・発行元・リスクシグナル・利用状況を条件に、ブロック・公開要求の却下・ポリシーテンプレートの適用を自動で実行する
- Tools management（GA）: MCP サーバーに加え、プラグイン・スキル・コネクタもテナント全体で許可・ブロックできる。Power Platform コネクタは対応中
- カスタム MCP サーバーの承認（プレビュー）: 開発者が Agent 365 CLI で登録し、管理者が発行元・エンドポイント・機能を確認して承認・却下する
- AI mode（プレビュー）: レジストリを自然言語で検索し、所有者のいないエージェントや非アクティブなエージェントを洗い出せる
- Azure API Management 連携: 9/30 から展開。APIM に載せたエージェント・ツール・モデル・MCP サーバーが自動検出される
- 支出ポリシー: グループごとに使えるモデルと推論の強さを割り当てられ、Cowork の Auto もこれに従う（展開中）。コスト管理の対象に Code と Copilot Managed Runtime が加わった

- https://techcommunity.microsoft.com/t5/agent-365-blog/what-s-new-in-agent-365-september-2026/ba-p/4560803

### 3. [料金+新機能] Microsoft が Copilot in SharePoint に PDF 操作・版の復元・メール送信・プラグイン呼び出しを入れた — 画像生成・Advanced Autofill・サイト分析は今月から Copilot Credits を消費する

**要点**: SharePoint の利用者は、Copilot に頼んで PDF を分割・結合し、ファイルを以前の版に戻し、生成したレポートをメールで送れるようになった。大半は M365 Copilot ライセンスに含まれるが、画像生成など3機能は今月展開の Copilot Credits を消費し、ライセンス内で収まる前提が崩れた。

**詳細**: 一次は SharePoint Blog「What's new in Copilot in SharePoint: October 2026」（10/1）。GA の展開は 9/30 に始まっている。

- ライセンスに含まれるもの:
  - PDF 操作: ページや節の単位で抽出・挿入・並べ替え・分割できる
  - 版の履歴: 変更点を要約し、指定した版に戻せる
  - メール送信: 「上司」「部下」のような呼び方から宛先を解決し、送信前に内容を確認できる
  - プラグイン: GitHub や CRM などの外部システムを読み書きできる。一括操作には人の承認が要る
  - ワークフロー: Teams にアダプティブカードで通知できる（Power Automate へのアクセスが必要）
- Copilot Credits が必要なもの: 画像の生成・編集、Advanced Autofill（大半は数分、混雑時は約1時間で終わる優先キュー）、サイト分析レポート

- https://techcommunity.microsoft.com/t5/microsoft-sharepoint-blog/what-s-new-in-copilot-in-sharepoint-october-2026/ba-p/4535423

## カテゴリ別まとめ

### Claude / Anthropic

- [動向] **Claude Frontier Academy** — Anthropic が 10/2、$100M を投じて2027年末までに 10,000人のエンタープライズ AI 展開人材を育てるプログラムを始めた。推薦制のエンジニアが数日間の対面研修と実技試験を経て Claude Resident Engineer になり、12週間のレジデンシーで自社の Claude プロジェクトを率いると Claude Frontier Deployed Engineer に認定される（初回認定は2027年初め）。
  - 初期参加: Accenture / Bain / Capgemini / Commonwealth Bank of Australia / Deloitte / McKinsey / Morgan Stanley / Novo Nordisk
  - 拠点と窓口: 最初はサンフランシスコ・ニューヨーク・ロンドン。窓口は Anthropic のアカウントチームか Partner Account Manager で、料金の記載は無い
  - https://www.anthropic.com/news/claude-frontier-academy
- [版更新] **Claude Code 2.1.288** — Anthropic が Claude Code `2.1.288` を npm の `next` に出した（10/2 18:30 UTC）。changelog は `2.1.287`（10/1）が最新のままで、変更内容は分からない。dist-tags は `{stable: 2.1.285, latest: 2.1.287, next: 2.1.288}` である。https://www.npmjs.com/package/@anthropic-ai/claude-code
- [据え置き] **API release notes・退役ページ・製品側の定点** — API release notes は 9/30 の Sonnet 4.5 退役告知が最上位のままで、`claude-haiku-4-5-20251001` は Active・「Not sooner than October 15, 2026」のまま退役告知が出ていない。Claude Haiku 5.5 は 9/22 の「数週間以内」の予告から出ていない。`claude.com/blog`・`/research`・`support.claude.com`・`status.claude.com` にも 10/2 付の新規は無い。

### OpenAI / Codex / ChatGPT

- **API 7モデルの退役告知**（ハイライト参照・1）
- [新機能] **Codex rust-v0.160.0** — OpenAI が Codex の安定版 `rust-v0.160.0`（10/1）を出し、Guardian review が会話履歴と引き継ぎコンテキストを扱えるようにし、agent command center のタスク履歴にページングを付けた。再接続後のキューメッセージ重複と Windows sandbox の PowerShell フォールバックも直した。pre-release は `0.162.0-alpha.7`（10/2）まで進んだ。https://github.com/openai/codex/releases
- [新機能] **ChatGPT ショッピングの Try on / Favorites** — OpenAI が ChatGPT のショッピングに、自分の写真で服を試着した画像を作る Try on と、商品を Library に保存する Favorites を全世界で出したと報じられた（10/1）。試着画像は ChatGPT Images 2.5 で作る。一次（`help.openai.com`）はオリジン403で未読である。https://dataconomy.com/2026/10/02/openai-chatgpt-virtual-try-on-product-favorites/
- [据え置き] **API changelog・Developer Community** — OpenAI の API changelog は 9/29 の3件、community Announcements は 9/30 の2件、`alignment.openai.com` は 9/25 の報告が最上位のままである。

### GitHub Copilot / GitHub

- [新機能] **Copilot の dynamic workflows** — GitHub が 10/1、Copilot CLI と Copilot app で、複数エージェントの並列実行・段階間の結果受け渡し・エージェントによる検証・人の確認待ちを1つの手順としてコードで組めるようにした（パブリックプレビュー・全 Copilot プランで追加料金なし）。app は設定不要で、CLI は `--experimental` または `/experimental on` で有効にする。https://github.blog/changelog/2026-10-01-dynamic-workflows-in-copilot-cli-and-the-copilot-app
- [廃止] **Copilot の4モデル廃止の発効告知** — GitHub が 10/2、Copilot から Gemini 3.5 Flash / Gemini 3.6 Flash / Kimi K2.7 Code / Claude Opus 4.7 を外したと告知した。移行先はそれぞれ Gemini 3.8 Flash / Gemini 3.8 Flash / Kimi K3 / Claude Opus 5.5 で、Enterprise 管理者が移行先モデルをポリシーで有効にしないと利用者の選択肢に出ない。https://github.blog/changelog/2026-10-02-selected-models-in-github-copilot-deprecated
- [版更新] **Copilot CLI v1.0.92 pre-release** — GitHub が Copilot CLI の pre-release を `v1.0.92-0`〜`v1.0.92-2`（10/1〜10/2）と刻み、アイドル切断後にリモート MCP サーバーへ再接続できるようにした。実行中のバックグラウンドエージェントへ送ったメッセージで進行中のターンを方向転換できる。安定版は `v1.0.91` のままである。https://github.com/github/copilot-cli/releases

### Microsoft 365 Copilot / Copilot Studio / Power Platform

- **Agent 365 の9月更新**（ハイライト参照・2）
- **Copilot in SharePoint の10月更新**（ハイライト参照・3）
- [新機能] **Agent Readiness が Launched** — メーカーは公開前に、ポリシー制限や評価不足でブロックされる機能を「Review」表示で確認できるようになった。Microsoft が Roadmap **568762** の状態を `Rolling out` から `Launched` に変えた（GA 期日 September CY2026）。Copilot Studio の起票25件のうち残る24件は `In development` のままである。https://www.microsoft.com/microsoft-365/roadmap?id=568762
- [据え置き] **Release Notes・What's New・Power Platform の定点** — M365 Copilot Release Notes の先頭は **September 23, 2026** のままで、Copilot Studio What's New は July 2026 節のまま GitHub Copilot ハーネスの GA（8/3）を61日反映していない。Power Platform のブログ・Release Wave・Released Versions（Copilot Studio 最新ビルド 2026.6.3 のまま94日）も動いておらず、Roadmap の 10/1 バッチ4件は Copilot と Copilot Studio に関わらない。
- [据え置き] **CSP の従量課金の既定オン延期** — 12/1 への延期と既定上限 月 4,000 クレジット/ユーザーは 10/2 に収録済みで、新しい事実は無い。industry は単価 $0.01/クレジット（二次）で換算すると1人月 $40 で、9月告知の $10 の4倍にあたると補っている。https://learn.microsoft.com/en-us/partner-center/announcements/2026-october

### Google

- [新機能] **Gemini 4 Argon** — Google DeepMind が Gemini 4 Argon を発表したと報じられた（9/30）。出力上限は 1M トークンで、導入価格は入力 $2・出力 $10（/1M トークン）、その後 $4・$20 に上がる。初期の利用者は Fairwind Program のサイバー防御組織に限られ、有料 API と Google AI Ultra への提供日は示されていない。Gemini API changelog には未掲載（最上位は 9/22 のまま）で、一次（`blog.google`）は未読である。https://techcrunch.com/2026/09/30/google-releases-gemini-4-argon-called-its-most-powerful-model-yet/
- [据え置き] **Gems から skills への移行日程** — Google の Workspace の skills 展開（Rapid Release 10/5〜12、Scheduled Release 10/19〜11月中旬）と Gems の 2027-03-01 廃止は 10/1 に収録した日程から変わっていない。Workspace Updates は 10/1 の3本が最上位で、10/2 付は無い。https://workspaceupdates.googleblog.com/2026/09/skills-gemini-app-workspace.html

### Cursor / xAI / Apple / オープンウェイト

- [廃止] **grok-voice-transcribe-1.0 の終了** — xAI が `grok-voice-transcribe-1.0` を 10/2 に終了し、リクエストを同価格の `grok-voice-transcribe-2.0` へ転送するようにした。一次（`docs.x.ai`）はゲートウェイ拒否で、WebSearch の本文相当で確認した。https://docs.x.ai/developers/release-notes
- [予定] **macOS の Full Disk Access の制御強化** — Apple が、macOS の Full Disk Access の付与に明示的なユーザー操作を必須にする追加の制御を入れると予告した（10/2）。理由に AI エージェントの能力と自律性の向上を挙げており、時期は示されていない。https://developer.apple.com/news/
- [据え置き] **Cursor・MCP・Hugging Face** — Cursor の changelog は 9/23、フォーラム Announcements は 9/21 の Grok 4.7 が最上位のままである。`blog.modelcontextprotocol.io` は 8/22 が最上位のままで、Hugging Face の登録8 org にも新規リポジトリは無い。Devin に日付つきの新規は検出していない。

### 規制・政策 / 市場

- [予定] **Anthropic の pre-IPO investor day** — Bloomberg によると、Anthropic が 10/14 にサンフランシスコ本社で機関投資家向けの pre-IPO investor day を開く（10/1 報道）。10/2 に収録した「11/9 の週にロードショー開始・11/26 前の上場」に、前段の日程が加わった。投資家の見積もる評価額は $1.8T〜2T で、会社の発表ではない。https://www.bloomberg.com/news/articles/2026-10-01/anthropic-is-said-to-plan-pre-ipo-investor-day-as-listing-nears
- [動向] **Dynatrace が Arize の買収を完了** — Dynatrace が AI オブザーバビリティの Arize を $9.15億で買収し、10/1 に完了したと発表した。Arize の CEO を含む全チームが Dynatrace に移り、OSS の Phoenix と企業向けの AX は引き続き提供される。https://www.dynatrace.com/news/blog/dynatrace-completes-acquisition-of-arize/
- [据え置き] **市場データ** — IDC Japan・MM総研・NRC・Similarweb はいずれも新規公表が無く、Similarweb の9月分トラッカーも未検知である。

## 直近の注目予定

- **10/5**: Gemini の `antigravity-preview-05-2026` が停止 ／ Workspace で skills の展開開始（Rapid Release） ／ GPT-Rosalind の課金開始 ／ Anthropic Wellbeing Research Grants の選考結果通知
- **10/7**: GHE.com が X25519 単独の TLS 接続を拒否
- **10/13**: Gemini アプリで skills の展開開始 ／ Office / Project / Visio LTSC 2021 のサポート終了 ／ 新しい Copilot の Partner Digital Airlift
- **10/14**: GitHub SSH の新規 RSA 鍵が 3072 ビット以上必須に ／ GPT-5.5 が ChatGPT / Codex から退役 ／ Anthropic の pre-IPO investor day（報道）
- **10/15 以降**: `claude-haiku-4-5-20251001` の暫定退役日（告知はまだ無い）
- **10月**: SharePoint の画像生成・Advanced Autofill・サイト分析が Copilot Credits の消費対象に ／ Copilot Studio エージェントがコスト管理の対象に ／ スキルカタログ GA（571880） ／ 自己学習 GA（570432） ／ Copilot UX components GA（SPFx 1.24） ／ Teams 通話委任の Preview（565216） ／ Word・Cowork の Legal plugins GA（571884） ／ Work IQ 拡張2件の Preview（570853・570854）
- **10/19**: GitHub Copilot が5モデルを廃止 ／ Workspace の skills 展開開始（Scheduled Release）
- **10/21**: GitHub Copilot の新機能既定ポリシーの設定期限（10/22 発効）
- **10/23**: OpenAI のレガシースナップショット12件が停止
- **10/27〜29**: PPCC 2026（ラスベガス）
- **10/29**: ChatGPT Pro 200 の現行枠の最終日（二次）
- **10/30**: ChatGPT Pro 200 の Work / Codex 利用枠が半減（二次）
- **10/31**: MCP サーバー認定の旧申請経路が終了 ／ OpenAI Evals が読み取り専用化
- **11月**: 永続的なエージェント ID GA（570430） ／ Maker guidelines GA（570967） ／ Teams 通話委任 GA（565216） ／ Purview 自動ラベル付け上限の引き上げ（571309） ／ Work IQ 拡張2件の GA
- **11/2**: GitHub Actions の `pull_request_target` 既定無効化が公開リポジトリで強制開始 ／ Partner Center の従量課金サンドボックス提供開始
- **11/4**: GitHub SSH `ssh-rsa` の1回目のブラウンアウト
- **11/9 の週**: Anthropic の上場マーケティング開始観測（二次、11/26 前の取引開始を狙う）
- **11/12**: OpenAI → Cursor のモデル供給停止予定（一次未読）
- **11/15**: Microsoft Release Planner 退役
- **11/17**: Gems が Gemini アプリの設定パネルへ移動
- **11/17〜20**: Microsoft Ignite
- **11/21**: OpenAI GPT-5.6 Sol の期間限定価格の下限
- **11/24 以降**: Claude Opus 4.5 の暫定退役日
- **11/30**: `claude-sonnet-4-5-20250929` が Claude API から退役 ／ OpenAI の `v1/prompts`・Evals・Agent Builder が停止
- **12/1**: CSP の Copilot Business 新規購入で従量課金が既定オン（既定上限 月 4,000 クレジット/ユーザー） ／ OpenAI `gpt-image-1-mini` / `gpt-image-1.5` / `chatgpt-image-latest` が停止
- **12/9**: GitHub SSH `ssh-rsa` の2回目のブラウンアウト
- **12/11**: OpenAI GPT-5 / o3 系スナップショットが停止
- **12/31**: 非営利向け M365 Copilot の併用プロモーション終了 ／ Gemini 3.8 Flash の導入価格が終了 ／ Pro 200 既存契約者の $2,500 クレジットが失効（二次）
- **2027-01-06**: OpenAI `tts-1` / `tts-1-hd` / `gpt-4o-mini-tts` 2版が停止
- **2027-03-01 以降**: Gems 廃止（Business / Enterprise）
- **2027-04-01**: OpenAI `gpt-5.1` / `gpt-5.3-codex` / `gpt-5.4-nano` が停止
- **2027-06-01 以降**: Gems 廃止（Education）

## 改善メモ

- 新規提案: 3ソースとも無し
- 継続提案: Master は2件を再確認（最多 B-035 npm dist-tags・48回目。`2.1.288` は `next` にだけ出て changelog に無い）／ Copilot は B-032（Agent 365 Blog が 8/6 以来の新規記事）・B-015（SharePoint Blog の10月 What's New）・B-037（94日）の回数を更新 ／ industry は4件を更新（最多 B-004・95回目）し、B-024・B-026・B-031 に取りこぼし実例を追記
- 障害の変化: industry が `news.crunchbase.com` を新規ゲートウェイ拒否として記録した（curl exit 56）。Master・Copilot は無し
- ソース間の差分・矛盾:
  - OpenAI の7モデル退役は Master と industry の両方がハイライトにしていた。記載は一致するため Master をベースに1件に統合した
  - CSP の従量課金延期（industry のハイライト1）は本サマリーが 10/2 に収録済みのため、ハイライトから外し [据え置き] に落とした。industry 側は $40/人月の換算（単価 $0.01 は二次）を補っており、それだけを残した
  - Gems の移行日程（industry のハイライト3）は本サマリーが 10/1 にハイライトにしているため、既報として [据え置き] にした
  - FTC の調査（Master は「本日はじめて載せる」と記載）は本サマリーが 10/2 に収録済みのため省いた
  - VS Code の Copilot 9月分は 10/2 に収録済み。Master は GA 項目（Codex 会話の ChatGPT ↔ VS Code 引き継ぎ・URL コンテキスト添付）を挙げているが、新しい発表ではないため省いた
  - Copilot の4モデル廃止は 10/2 に発効日として載せたが、GitHub の告知自体は 10/2 付で、Enterprise のポリシー有効化が要る点が新しいため [廃止] で残した（Master・industry と同じタグ）
- タグ: Copilot in SharePoint は分野側 [新機能] に対し、Copilot Credits の消費開始が前提を変える点を主として [料金+新機能] とした。Gemini 4 Argon は Master と同じ [新機能]（導入価格は本文に記載）
