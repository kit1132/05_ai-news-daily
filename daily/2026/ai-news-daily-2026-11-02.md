# AI News Daily Summary — 2026-11-02

週末明けで一次ソースの大半は動いていない。The Decoder の報道では、OpenAI が12月から ChatGPT と Codex の利用枠を1つの予算にまとめる（二次）。Microsoft は、MCP サーバーやアクション付きのエージェントを誰がアップロードできるかを管理者が絞れる設定を出していた。何も設定しなければ 10/25 から全ユーザーに許可されている。

## 今日のハイライト

### 1. [料金+予定] OpenAI が12月から ChatGPT と Codex の利用枠を1つの予算にまとめる — 「チャットは Codex と別枠」の前提が崩れる

**要点**: The Decoder（11/1）によると、OpenAI はサポートページで、12月から Plus・Pro・Business の ChatGPT と Codex が1つのトークン予算を共有すると明記した。重いモデルやタスクほど早く減るため、Codex を多用するとチャットに使える枠も減る。

**詳細**: 典拠は The Decoder と、記事が引く OpenAI のサポートページ。`help.openai.com` は本日もオリジン403で、一次の本文は確認できていない（industry）。

- 対象外: Instant モデルとのチャットは予算に数えない
- 上限到達時: 設定画面で残量とリセット時刻を確認でき、リセットを待つ・上位プランへ移る・追加クレジットを買う、のいずれかを選ぶ
- 背景: ChatGPT の Chat と Work を1つの画面に統合する計画の一部。10/29 報道の Pro 100・Pro 500 の Work・Codex 枠倍増はこの統合への備えとみられている
- 未公表: 開始日、プラン別の予算額

- https://the-decoder.com/openais-upcoming-chat-and-work-merger-in-chatgpt-signals-the-end-of-all-you-can-prompt-pricing/

### 2. [新機能] MCP サーバーやアクション付きのエージェントを誰がアップロードできるか、M365 の管理者が絞れるようになった — 何も設定しなければ 10/25 から全ユーザーに許可されている

**要点**: これまでユーザーは MCP サーバー付きのエージェントを自由にアップロードでき、管理者に止める手段は無かった。M365 管理センターで、全ユーザー・特定のユーザーやグループ・誰にも許可しない、の3つから選べるようになった。設定していないテナントは全ユーザー可のままである。

**詳細**: MC1472007（9/14 公開・Major change）。展開は 9/25 に始まり、10月末に完了する予定。Copilot が月曜の docset 全件突合で、Learn の設定一覧（`ms.date` 10/31）と新設の手順ページ（`ms.date` 10/29）から検知した。MC の公開時は mc.merill.net がゲートウェイ拒否で、これまで載っていなかった。

- 設定の場所: M365 管理センター > Copilot > Settings > All settings > Advanced package uploads。変更には AI 管理者ロールが要る
- 対象: アクション付きの宣言型エージェントと、MCP サーバーを含むパッケージ。指示だけの宣言型エージェントは今後もアップロードできる
- 対象外: Microsoft 製・サードパーティ製のエージェントと、設定ができる前にアップロードされた高度なパッケージ
- 対象の面: Microsoft 365 Copilot、Cowork、Agents Toolkit（ATK）

- https://mc.merill.net/message/MC1472007
- https://learn.microsoft.com/en-us/microsoft-365/copilot/configure-copilot-advanced-package-uploads

## カテゴリ別まとめ

### OpenAI / Codex / ChatGPT

- **ChatGPT と Codex の利用枠の統合**（ハイライト1参照）
- [仕様] **ChatGPT 有料アカウントのカード・端末上限** — The Decoder（11/1）によると、OpenAI は1枚のカードや1台の端末に紐づけられる有料サブスクリプションの数に上限を設けた。対象は Go・Plus・Pro 100・Pro 200・Pro 500 で、Free・Business・Enterprise・Edu は数えない。上限に達すると「Device limit reached」が出てその端末で使えなくなり、ログアウトしても枠は空かない。上限の数とヘルプ記事の本文は未確認である
  - https://the-decoder.com/openai-is-steering-chatgpt-users-toward-more-paid-usage/
- [版更新] **Codex `0.167.0-alpha.2`** — OpenAI が Codex の pre-release を 11/1 に出した。安定版は `0.166.0`（10/29）のままである
  - https://github.com/openai/codex/releases
- [据え置き] **API changelog・退役・安全性** — OpenAI の API changelog の最上位は 10/30 の `gpt-6-rosalind`、deprecations は 10/14 の GPT-4 系の告知のままである。Deployment Safety Hub は 10/30 の GPT-Rosalind-6 補遺、community Announcements は 10/28、`learn.chatgpt.com` の changelog は 10/29、`alignment.openai.com` の First posted は 10/20 から動いていない
  - https://developers.openai.com/api/docs/changelog

### Anthropic / Claude

- [観測] **Privacy Center の Covered Models 記事の更新** — Anthropic が「Data retention practices for covered models」を 10/30 17:08 UTC に更新した（HTML の `dateModified`）。Master は前回の本文を保存していなかったため、どこが変わったかは特定できていない
  - 現在の記載: 対象は Mythos 級モデルと同等能力の将来モデル。ZDR の組織でも Covered Models の入出力は全提供面で30日保持される
  - 保持の設定先: Claude Platform（ワークスペース単位）、Claude Platform on AWS、Amazon Bedrock、Google Cloud Agent Platform、Azure Foundry（サブスクリプション単位）
  - 参照先の Covered Models 記事（`support.claude.com` 15425695）は 9/1 更新のままで、Enterprise Frontier Safeguards は「2026年秋から段階的に提供」の記載のまま
  - https://privacy.claude.com/en/articles/15425996-data-retention-practices-for-covered-models
- [据え置き] **Claude Code・Platform・退役ページ** — Claude Code の changelog の最上位は `2.1.316`（10/31）のままで、npm も `{stable: 2.1.309, latest: 2.1.316, next: 2.1.316}` から動いていない。Platform release notes の最上位は 10/30（Opus 4.8 fast mode の廃止告知）、モデル退役ページの Active は15件のままである。Claude Haiku 4.5 は退役下限日（10/15）を過ぎても Active にある
  - https://code.claude.com/docs/en/changelog
  - https://platform.claude.com/docs/en/about-claude/model-deprecations
- [据え置き] **ニュース一覧** — `www.anthropic.com/news` は 10/28、`/research` は 10/27、`claude.com/resources/articles` は 10/28、`support.claude.com` は 10/21 から動いていない

### Microsoft 365 Copilot / ライセンス

- **高度なパッケージのアップロード制御**（ハイライト2参照）
- [仕様] **E3 / E5 / E7 の比較ページ** — Microsoft が、Copilot 導入前のデータ整備に関わる機能を E3・E5・E7 で比べる Learn ページを新設した（`ms.date` 10/28）。E7 は E5 に Copilot・Entra Suite・Agent 365 を加えたもので、E3・E5 では Copilot はアドオンのままである
  - SharePoint Advanced Management: E3・E5 は Copilot アドオン購入時のみ、E7 は同梱の Copilot ライセンスで使える
  - Security Copilot: E3 には含まれず、E5・E7 では対象の顧客に含まれる
  - Agent 365: E7 にだけ含まれる
  - https://learn.microsoft.com/en-us/microsoft-365/copilot/compare-copilot-e3-e5-e7
- [仕様] **Mistral の接続ページ** — Microsoft が Learn に、Copilot Studio で使える Mistral のモデルは現時点で Mistral Medium 3.5（パブリックプレビュー）だけだと書いた（`ms.date` 10/28）。管理者が M365 管理センターの「AI providers operating as independent processors」で Mistral を許可し、対象を選ぶ必要がある。Mistral で処理するデータには Microsoft の Product Terms・DPA・データ所在地の約束が適用されない
  - https://learn.microsoft.com/en-us/microsoft-365/copilot/connect-mistral-ai-models
- [据え置き] **Roadmap・Message Center・Release Notes・ブログ** — Roadmap の RSS は 10/30 22:08Z のバッチのままで、総項目数は 2,229 である。Message Center は 10/31 04:46Z から更新がなく、Release Notes の先頭は October 27 バッチのまま。Copilot ブログ・TC の各ブログ・M365 Developer Blog・SharePoint Blog・Cowork の Learn 6本・Purview にも新しい記事はない。Partner Center の `2026-november` はまだ 404 を返す
  - https://www.microsoft.com/releasecommunications/api/v2/m365/rss

### Copilot Studio / Power Platform

- [据え置き] **What's New・課金・モデル表・非推奨一覧** — Copilot Studio What's New は `031b66d5`（`ms.date` 10/5）のままで、ハーネスの改名もまだ反映されていない。課金レート表・課金とハーネスの6本・PPAC の容量管理・モデル表3本・ガイダンスハブ・非推奨一覧に改訂はなく、Released Versions は 2026.6.3 のまま124日たつ
  - https://learn.microsoft.com/en-us/microsoft-copilot-studio/whats-new
- [観測] **Learn docset の週次突合** — Copilot が目次3本（Copilot Studio 478・M365 Copilot 138・Cowork 26）の641ページを突合し、すべて 200 を返した。10/26 以降の改訂約150本の大半は一括の再ビルドで、掲載歴のないページで中身が増えていたのはハイライト2と上の E3/E5/E7・Mistral の3本だった。M365 Copilot の目次は163リンクから138リンクに減ったが、前回の一覧が無いため消えたリンクは特定できない
  - https://learn.microsoft.com/en-us/microsoft-365/copilot/toc.json

### GitHub Copilot

- [版更新] **Copilot CLI `v1.0.106-1` / `-2`** — GitHub が Copilot CLI の pre-release を 10/31 と 11/1 に出した。`-2` は修正5件（`--screen-reader` の接頭辞、`/resume` の二重表示、応答しない HTTP MCP サーバーの起動待ち、symlink の `mcp-config.json` の保持、`/skills` の同期）で、フラグの削除や非互換の記載は無い。安定版は `v1.0.105`（10/28）のままである
  - https://github.com/github/copilot-cli/releases
- [据え置き] **github.blog changelog・Windows Command Line** — `github.blog/changelog/label/copilot/` の最上位は 10/28 の Copilot Fusion のままで、Windows Command Line ブログも PowerToys 0.102（10/21）から動いていない

### Google / その他の開発ツール

- [予定] **Antigravity のボイスモード付きエージェント（未確認）** — TestingCatalog が 11/1 に、Google が Antigravity に音声モードを持つ新しい AI エージェントを用意していると報じた。10/31 のクラウド実行に続く準備段階の観測で、公式の告知は無い
  - https://www.testingcatalog.com/rss/
- [予定] **Gemini 4 Carbon の新チェックポイント** — TestingCatalog が 11/1 に、Gemini 4 Carbon の新しいチェックポイントが Arena で試験されていると報じた。未発表モデルの試験で、提供日は分からない
- [据え置き] **Google・Cursor ほかの定点** — Gemini API changelog の最上位は 10/30 の Computer Use GA のままで、Workspace Updates・Gemini アプリ・The Keyword も動いていない。Cursor（10/20）、Devin（10/28）、Orca（`v1.4.245`）、xAI、TypeSafe AI（`jev-1.14.0`）、MCP blog（9/29）、Hugging Face の8 org、Obsidian、Apple Developer News にも新規はない

### 業界・市場

- [据え置き] **買収協議・調査データ** — Amazon × Decart、Nvidia × Reflection AI の買収協議に続報はなく、週末のため IDC Japan・MM総研・NRC の新規公表も無かった

## 直近の注目予定

- **11/2**: xAI `grok-imagine-image-quality` が退役 ／ Meet の63言語音声翻訳が Scheduled Release へ展開開始
- **11/4**: Entra で一般ユーザーのブループリント作成が既定オン（MC1506733） ／ Kimi K3.1 Pro の重み公開の約束期限（二次）
- **11/5 ごろ**: Anthropic のゲスト研究者（生命科学）の応募受付が終了（締切日は明記なし）
- **11月**: GitHub の cloud sandbox の課金が開始（日付は明記なし） ／ Targeted release の割り当てが変更不可になり、統合 Release Preferences 画面が入る ／ Copilot アプリの新しい Home が全世界に出て、Autopilot が Frontier に出る
- **11/9**: Dataverse のみのテナントでストレージ検証が開始（MC1483529）
- **11/12**: Copilot Studio の GPT-4.1 / GPT-5 系が退役（MC1506318） ／ Anthropic Usage Policy 改定版が発効 ／ OpenAI → Cursor のモデル供給停止予定（一次未読）
- **11/15**: Dataverse for Teams 環境とアンマネージド開発者環境の新規作成が停止 ／ Copilot Studio のカスタム採点器ライブラリが GA（MC1531932）
- **11/16**: GitHub Copilot が Claude Opus 4.8・Opus 5・GPT-5.6 Terra を廃止 ／ Teams の旧 GitHub アプリが退役 ／ Cowork / Autopilot の Engage プラグインが GA（MC1530609）
- **11月中旬**: Teams 会議の MeetingAI / TranscriptionWithMeetingAI ポリシーの展開開始（MC1532253） ／ Office in Copilot の展開（MC1530611） ／ Agent Builder のプロンプトのスケジュール実行が開始（MC1302906） ／ Viva Insights の GitHub Copilot 指標が既定オン（MC1523085）
- **11/17**: Gems が Gemini アプリの設定パネルへ移動 ／ Gemini API の TTS・Live プレビュー5種が停止（最短日）
- **11/17〜20**: Microsoft Ignite
- **11/20**: Copilot Studio のコスト管理を M365 管理センターへ移す機能が GA（MC1530368）
- **11/24 以降**: `claude-opus-4-5-20251101` の暫定退役日（確定日ではない）
- **11/29**: OpenAI が Daybreak Blue のセッションデータの学習利用を開始（二次）
- **11/30**: Opus 4.8 の fast mode を削除 ／ `claude-sonnet-4-5-20250929` が Claude API から退役 ／ Power Apps のモデル駆動アプリの説明文の AI 生成・Plan Designer の共同編集・レコード単位の在席表示が退役 ／ OpenAI の Evals・`v1/prompts`・Agent Builder が停止 ／ Gemini 4 Argon の導入価格が終了 ／ Azure DevOps コネクタの旧接続が認証不可に（MC1508508） ／ App Builder と vibe.powerapps.com が退役
- **12/1**: M365 Copilot の前提サブスク不要オファー開始 ／ Copilot Business の従量課金が既定オン ／ Gemini 4 Argon の単価が $4/$20 に倍増 ／ Google スライドの複数スライド作成の上限引き上げ優待が終了しうる
- **12月上旬**: Copilot アプリのタスクバー固定にライセンス別の選択肢が入る（MC1530612）
- **12月中（日付未公表）**: ChatGPT と Codex の利用枠が Plus・Pro・Business で1つの予算に統合（二次）
- **12/11**: Power Apps の式の生成・Power Apps Ideas・Copilot によるコントロール名の変更が退役（MC1532421・MC1532426）
- **12/14**: claude.ai/design の単体サイトが閉鎖
- **12/15**: アンマネージド開発者環境が停止
- **12月下旬**: Purview DLP の Microsoft 以外のアプリ対応が GA（MC1449180）
- **12/31**: Power Platform の環境間のコメントのインポート・エクスポートが終了 ／ Claude Security の無償クレジット（月 $25,000×2か月）の対象期間が終了 ／ Gemini 4 Carbon の導入価格の割引が終了
- **2027-01-06**: OpenAI `tts-1` / `tts-1-hd` / `gpt-4o-mini-tts` 2版が停止
- **2027年1月**: Targeted release が退役 ／ Copilot Studio の Teams アプリで編集ができなくなる（MC1511056） ／ Teams の会議メモリーファイルの生成が開始（MC1429018）
- **2027-01-14**: OpenAI の GPT-4o・GPT-4o mini・GPT-4.1・GPT-4.1 mini が API から削除（→ `gpt-6-luna`）
- **2027-01-15**: アンマネージド開発者環境の削除開始 ／ Claude Code Review の Enterprise 向けクレジット請求期限
- **2027年1月中旬〜下旬**: 旧来の Teams 保持ポリシーが Copilot の対話に効かなくなる（MC1481313）
- **2027-03-01 以降**: Gems 廃止（Business / Enterprise）
- **2027年3月**: Purview の DSPM classic / DSPM for AI classic が退役（MC1481315）
- **2027年3月末**: Outlook の Copilot Prioritize の削除が完了（MC1519861） ／ SharePoint / OneDrive の `.agent` 形式エージェントが動かなくなる（MC1511052）
- **2027-04-01**: OpenAI `gpt-5.1` / `gpt-5.3-codex` / `gpt-5.4-nano` が停止

## 改善メモ

- 新規提案: Master が B-087（Privacy Center の更新日を HTML の `dateModified` で取り、本文の段落数とハッシュを状態ファイルに残して差分を取る）を、Copilot が B-082（週次突合の目次リンク一覧を保存し、次回の増減を特定できるようにする）を起票した。industry は新規起票なし
- 継続提案: Master は継続5件（最多 B-036 DeepSeek 登録、12回目。見送り候補 B-036 / B-037 / B-043 / B-078） ／ Copilot は継続2件（最多 B-080 Cowork の Learn URL 差し替え、7回目。B-081 ハーネス改名は Learn が本日も旧名のまま、5回目） ／ industry は継続6件（最多 B-040 セキュリティ開示の定点、13回。見送り候補 B-036）
- 障害の変化: 3ソースとも記録なし。Master は月曜の週次復旧チェックを実施し、復旧・分類の変化は無かった。Copilot は Copilot Studio Kit の releases.atom が `curl` で 403 だったが、週次確認は 10/30 に実施済みのため WebFetch は試していない
- 欠損リカバリ: 前日（11/1）分は3ソース揃っており、対象なし
- ソース間の差分・矛盾: industry の継続提案は前日の5件から6件になった。ほかに矛盾する記述は無い
