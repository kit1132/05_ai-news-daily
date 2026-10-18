# AI News Daily Summary — 2026-10-19

GitHub Copilot から GPT-5.5・GPT-5.4 系など6モデルが今日外れる。xAI は `grok-voice-3.0` を出して 2.0 を deprecated にし、Google は Gmail Live を Gemini 有効の Workspace で既定オンにした。Anthropic は株式の5%を公益ファンドに拠出すると発表した。

## 今日のハイライト

### 1. [廃止] GitHub Copilot から GPT-5.5・GPT-5.4 系など6モデルが今日 10/19 に外れる — 固定でこれらを選んでいたチャット・エージェント・組織ポリシーは移行先へ切り替わる

**要点**: GitHub が 9/18 に告知した Copilot の6モデル廃止が今日発効する。GPT-5.5 / GPT-5.4 は GPT-5.6 Sol、GPT-5.4 mini / GPT-5 mini は GPT-5.6 Luna へ移る。モデル指定のある手順書や組織のモデルポリシーは今日から古くなる。

**詳細**:

- 対象と移行先
  - Gemini 3.7 Flash: Gemini 3.8 Flash
  - GPT-5.5 / GPT-5.4: GPT-5.6 Sol
  - GPT-5.4 mini / GPT-5 mini: GPT-5.6 Luna
  - Grok 4.5: Grok 4.6
- Business / Enterprise: 既定のモデル有効化がオンなら、移行先が自動で有効になる
- 実施を示す changelog は確認時点で未掲載で、OpenAI API 側の `gpt-5.5` 等の廃止告知は出ていない

- https://github.blog/changelog/2026-09-18-upcoming-deprecation-of-selected-github-copilot-models-in-mid-october

### 2. [廃止+新機能] xAI が `grok-voice-3.0` を出し、`grok-voice-2.0` を deprecated にした — `grok-voice-latest` はすでに 3.0 を指しており、版を固定していない音声アプリは 10/14 から挙動が変わっている

**要点**: xAI が 10/14 に Speech to Speech の新版 `grok-voice-3.0` を同価格・同 API で出し、`grok-voice-2.0` を deprecated にした。エイリアス利用者は何もしなくても新版に切り替わっており、終了日はまだ示されていない。

**詳細**:

- `grok-voice-3.0`: Speech to Speech 対応。価格と API 仕様は 2.0 と同じ
- `grok-voice-2.0`: deprecated。移行先は `grok-voice-3.0` か `grok-voice-latest`
- 先行の退役: `grok-voice-transcribe-1.0` は 10/2 に終了し、`grok-voice-transcribe-2.0` へ同価格で自動転送されている
- 一次の `docs.x.ai` が週次復旧チェックで初めて読めたため、5日遅れの検出になった

- https://docs.x.ai/developers/release-notes

### 3. [新機能] Google が Gmail Live と AI Inbox を有償 Workspace に展開し始めた — Gmail Live は Gemini を有効にした組織で既定オンになる

**要点**: Google が 10/15 に、受信トレイを音声で問い合わせる Gmail Live（モバイル）と、メールから ToDo と要約を抜き出す AI Inbox を有償 Workspace へ展開し始めた。Gmail Live は既定オンなので、止めたい管理者は既存のスマート機能の設定で対処する必要がある。

**詳細**:

- Gmail Live: 低遅延で受信トレイを音声検索し、出典メールのカードつきで合成音声が答える。既存のスマート機能・パーソナライズの管理設定に従う
- 対象: Business / Enterprise の各エディション、Frontline Plus、Nonprofits、Gemini Business / Enterprise などのアドオン、個人の Google AI Plus / Pro / Ultra
- 制約: 米国・EN-US のみ。Rapid / Scheduled Release とも 10/15 から最大15日で順次表示
- AI Inbox: 対応すべき ToDo・成果物・期限を抜き出し、優先度の高い業務連絡を要約する

- https://workspaceupdates.googleblog.com/

## カテゴリ別まとめ

### Claude / Anthropic

- [観測] **Claude Fable 5.5 のリーク** — TestingCatalog が 10/17 に「Anthropic が来週 Claude Fable 5.5 を出す」と報じたが、根拠はリーク投稿だけで Anthropic は何も認めていない。Azure カタログに「Generally available」と載ったとするスクリーンショットは翌日 LiteLLM から消え、価格 $10 / $50 は Fable 5.1 の値の流用とみられる。コードネームは `claude-onigiri-eap` など6件が出ているが、どれが Fable 5.5 かは分かっていない。https://www.testingcatalog.com/anthropic-several-models-coming-fable-5-5-reaches-partners/
- [動向] **Anthropic の社内雇用調査の追加数値** — The Decoder が 10/18 に、10/16 公表の「Employment at Anthropic」を報じ、前日までに触れていない数値を挙げた。エンジニア1人あたりのコミットは半年前の約5倍で、社員の75%が「2030年までに仕事の75%を AI がこなす」と見込む（米国の一般就業者は28%）。対話セッション時間の約80%は人の入力待ちで、本文は単一企業のデータで一般化は難しいと明記している。https://the-decoder.com/anthropic-has-nearly-stopped-hiring-junior-staff-because-ai-agents-now-work-six-times-as-many-hours/
- [据え置き] **Claude Code / Platform / Haiku 4.5** — Claude Code は changelog 最上位が `2.1.302` のままで、npm も `{stable: 2.1.292, latest: 2.1.302, next: 2.1.302}` から動いていない。Platform release notes は 10/15 が最上位で、廃止ページは `claude-haiku-4-5-20251001` を退役下限日の4日後も Active と表示している。https://platform.claude.com/docs/en/about-claude/model-deprecations

### GitHub Copilot / GitHub

- **Copilot 6モデルの廃止**（ハイライト参照・1）
- [据え置き] **Copilot CLI** — GitHub は Copilot CLI の安定版を `v1.0.98`（10/14）、pre-release を `v1.0.100-1`（10/16）のまま据え置いた。`github.blog` の Copilot ラベルも 10/16 の Slack / Teams 対応が最上位のままである。https://github.com/github/copilot-cli/releases

### OpenAI / Codex / ChatGPT

- [据え置き] **Codex CLI と OpenAI の各 changelog** — OpenAI は Codex CLI の安定版を `0.163.0`（10/15）、pre-release を `0.164.0-alpha.3`（10/17）のまま据え置いた。API changelog は 10/16、community Announcements と `learn.chatgpt.com` の changelog は 10/15 が最上位のままである。https://github.com/openai/codex/releases

### Google / xAI

- **`grok-voice-3.0`**（ハイライト参照・2）
- **Gmail Live と AI Inbox**（ハイライト参照・3）
- [据え置き] **Gemini API / Gemini アプリ** — Gemini API changelog は 10/13 の Gemini 4 Argon GA が最上位のままである。今日はじめて読めた Gemini アプリのリリースノート（`gemini.google/release-notes/`）も、最上位は 10/13 の Gemini 4 Argon で既報の範囲に収まる。https://gemini.google/release-notes/

### Microsoft 365 Copilot

- [予定] **Interpreter の逐次通訳モード** — MC1239927（10/16 更新）によると、M365 Copilot ライセンス保有者が Teams 会議で使う予定だった逐次通訳モードは、7/13 に展開が止まったまま再開日が示されていない。10/16 の更新は終了日の変更だけで、GA は「準備ができたら Message Center で知らせる」のままである。https://mc.merill.net/message/MC1239927
- [据え置き] **Release Notes / ブログ / Message Center** — M365 Copilot Release Notes の先頭は October 06, 2026 のままで、Copilot・Copilot Studio・Tech Community・M365 Developer の各ブログにも新規記事は出ていない。Roadmap と Message Center も 10/16 から更新されていない。

### Copilot Studio / Power Platform

- [新機能] **人事サポートの参照アーキテクチャ** — Microsoft は Architecture Center に、Copilot Studio のオーケストレーターが人事の問い合わせを専門エージェントへ振り分ける構成例を追加した（`ms.date` 10/13・ガイダンスハブ What's New の October 2026 節）。https://learn.microsoft.com/en-us/power-platform/architecture/reference-architectures/modernize-hr-support
  - 専門エージェント: 個人情報、休暇、マネージャー操作、学習、人事ポリシーの5領域を分担する
  - 接続: HCM・学習基盤へはカスタムコネクタと Power Automate フロー、ポリシー回答は ITSM のナレッジ記事を Graph コネクタで索引化する
  - 運用: 会話と性能のデータは Dataverse と Application Insights に置き、環境間の移送は Power Platform のパイプラインで行う
- [据え置き] **What's New / Released Versions / 非推奨一覧** — Copilot Studio What's New は `ms.date` 10/5 のまま、Released Versions は 2026.6.3 のまま110日動いておらず、非推奨一覧も 10/16 の `caf484d1` から改訂されていない。

### その他エージェント / 開発ツール

- [新機能] **Devin の Git 連携拡大** — Cognition が 10/16 に、GitLab のマージリクエストで `/devin review` と `/devin <prompt>` を使えるようにし、Devin Review が Bitbucket Cloud の PR のマージ可否を表示するようにした。https://docs.devin.ai/release-notes/overview
  - PR の一覧と検索: GitHub / GitLab / Azure DevOps / Gerrit / Perforce Swarm で、状態・作成者・ブランチ・タイトルで絞り込める
  - Git ツール: GitHub で issue・ラベル・担当者・ブランチ保護を扱う組み込みツールを足し、リポジトリ情報とブランチ保護は他の4サービスでも使える
  - Bitbucket Data Center: 接続時にプロジェクトごとの webhook を自動で張る
- [据え置き] **Cursor・Orca・TypeSafe・MCP・HF の定点** — Cursor の changelog は 10/16、フォーラム Announcements は 10/12 が最上位のままで、Orca は `v1.4.229`、TypeSafe は `jev-latest` → `jev-1.13.0` のままである。`blog.modelcontextprotocol.io` は 8/22 が最上位で、Hugging Face の8 org にも新しい ID は無い。

### 市場・企業

- [動向] **Anthropic Public Benefit Fund** — Anthropic が 10/18 に、株主の承認を条件として、全額出資の LLC に発行済み株式の **5%** を拠出すると発表した。創業者の誓約と社員の株式寄付マッチとあわせ、株式の約20%が公益に向けられる。https://www.anthropic.com/news/public-benefit-fund
  - 追加拠出: 基準値から企業価値が50%上がるごとに、取締役会の判断で **2%** ずつ足す（基準値は未公表）
  - 形態: 501(c)(3) ではない LLC で、保有株をロビー活動や政治献金に使わないと明記した
  - 用途: 非営利団体への大口寄付、特定の層への直接分配、労働市場への影響対策。ガバナンスは今後数か月で公表する
- [動向] **Anthropic の AI 安全法案草案（報道）** — Politico によると、Anthropic が 10/16 までにフロンティア AI の安全法案の草案を議会関係者に非公式に示した。政府がモデルの公開・利用を止められるのは、生物兵器・サイバー攻撃・制御からの逸脱で $1B 超の損害か50人超の死傷の危険がある場合に限られ、差し止めの申し立ては商務省だけが D.C. の連邦裁判所に行える。提出する議員がいるかは分かっていない。https://www.pymnts.com/cpi-posts/anthropic-proposes-ai-safety-bill-giving-us-government-power-to-block-high-risk-models/
- [動向] **Disney が Character.AI 社員66人に採用を提示** — 裁判所提出書類によると、Disney は破産手続き中の Character.AI のフルタイム約86人のうち66人に職を提示し、3年で約 $180M を本人に支払う。Disney は $20M で技術の非独占ライセンスを得るストーキングホース入札者で、アプリ・ブランド・利用者データは対象外であり、競売は11月下旬〜12月上旬の見込みである。https://ppc.land/disney-budgets-180m-for-character-ai-staff-20m-for-the-bankrupt-company/
- [据え置き] **Business Insider Japan 10月版と国内市場データ** — Business Insider Japan が 10/18 に10月版の生成AI主要8サービス料金早見表を公開したが、内容は既報の改定の整理にとどまる。買収協議（Amazon × Decart、Nvidia × Reflection AI）にも続報は無く、IDC Japan・MM総研・NRC の新規公表も無い。https://www.businessinsider.jp/article/2610-how-much-did-major-generative-ai-service-fees/

## 直近の注目予定

- **10/15 以降**: `claude-haiku-4-5-20251001` の暫定退役日（告知はまだ無い）
- **10/19**: GitHub Copilot が GPT-5.5・GPT-5.4 系・GPT-5 mini・Gemini 3.7 Flash・Grok 4.5 を廃止
- **10/21 前後**: TypeSafe の `jev-latest` が `jev-1.14.0` へ移る
- **10/22**: Copilot Business / Enterprise の機能既定有効化が発効 ／ Gemini API の Veo 3.1 プレビュー3種と `gemini-omni-flash-preview` が停止（最短日）
- **10/23**: Gemini API の `deep-research-pro-preview-12-2025` が停止 ／ OpenAI のレガシー GPT スナップショットが停止
- **10月後半**: claude.ai（米国）で Democracy Works の投票情報を表示 ／ Claude Fable 5.5（リークのみ・未確認）
- **10月下旬**: Copilot ダッシュボードのデータエクスポートのパブリックプレビュー展開が完了（MC1173208）
- **10/27〜29**: PPCC 2026（ラスベガス）
- **10/30**: ChatGPT Pro 200 の Work / Codex 利用枠が変更（二次） ／ Gmail Live の Workspace への順次展開が完了（最大15日）
- **10月末**: Planner Agent チャットの GA 完了（MC1443514）
- **10/31**: MCP サーバー認定の旧申請経路が終了 ／ DeepSeek の Search・Fetch API の無料提供が終了
- **11/1**: Codex の28日間「改善かリセット」の終了（二次）
- **11/4**: Entra で一般ユーザーのブループリント作成が既定オン ／ `AgentIdentity.CreateAsManager` の自動付与が停止
- **11月上旬**: Copilot Notebooks の成果物提案が GA 完了（MC1411727）
- **11/12**: Copilot Studio の GPT-4.1 / GPT-5 系が退役 ／ Anthropic Usage Policy 改定版が発効 ／ OpenAI → Cursor のモデル供給停止予定（一次未読）
- **11/15**: Dataverse for Teams 環境とアンマネージド開発者環境の新規作成が停止
- **11月中旬**: SharePoint / OneDrive のエージェント作成が Agent Builder に切り替わる（MC1511052）
- **11/16**: GitHub Copilot が Claude Opus 4.8・Opus 5・GPT-5.6 Terra を廃止 ／ Sales Development Agent が Copilot Credits の消費を開始
- **11/17**: Gems が Gemini アプリの設定パネルへ移動
- **11/17〜20**: Microsoft Ignite
- **11月**: Copilot コネクタ利用状況レポートが GA（MC1404326）
- **11/24**: `claude-opus-4-5-20251101` の退役下限日（告知なし）
- **11月下旬〜12月上旬**: Character.AI の資産競売
- **11月下旬**: Agent 365 の可観測性データがライセンス不要に（MC1506727）
- **11/30**: Azure DevOps コネクタの旧接続が認証不可に（MC1508508） ／ App Builder エージェントと vibe.powerapps.com が退役 ／ `claude-sonnet-4-5-20250929` が Claude API から退役 ／ OpenAI の Evals・`v1/prompts`・Agent Builder が停止 ／ Gemini 4 Argon の導入価格が終了
- **12/1**: Gemini 4 Argon の単価が $4/$20 に倍増 ／ Copilot Business の従量課金が既定オン
- **12/14**: claude.ai/design の単体サイトが閉鎖
- **12/15**: アンマネージド開発者環境が停止
- **2027-01-06**: OpenAI `tts-1` / `tts-1-hd` / `gpt-4o-mini-tts` 2版が停止
- **2027年1月上旬**: Copilot Studio の Teams アプリで編集ができなくなる（MC1511056）
- **2027-01-14**: OpenAI の GPT-4o・GPT-4o mini・GPT-4.1・GPT-4.1 mini が API から削除
- **2027-01-15**: アンマネージド開発者環境の削除開始 ／ Claude Code Review の Enterprise 向けクレジット請求期限
- **2027年2月上旬**: Copilot Studio の Teams アプリが Teams から削除される（MC1511056）
- **2027-03-01 以降**: Gems 廃止（Business / Enterprise）
- **2027年3月末**: SharePoint / OneDrive の `.agent` 形式エージェントが動かなくなる（MC1511052）
- **2027-04-01**: OpenAI `gpt-5.1` / `gpt-5.3-codex` / `gpt-5.4-nano` が停止
- **2027-10-15**: Purview の `Search-UnifiedAuditLog` コマンドレットが退役
- **2027-10-30**: アップグレードしていない Dataverse for Teams 環境が廃止

## 改善メモ

- 新規提案: Master が B-084（週次復旧チェックで本文取得を確認した8ソースの取得方法欄を一次へ戻す）を起票した。Copilot と industry は無し
- 継続提案: Master は B-082（25回目）と B-083 Gemini アプリ release notes の URL 差し替え（3回目） ／ Copilot は B-037（Released Versions 110日）と B-063 を更新し、docset 全件突合は本日未実施 ／ industry は B-004（111回目）を更新
- 障害の変化: Master でゲートウェイ拒否17ホストのうち15ホストが通過し、`docs.x.ai` / `docs.devin.ai` / `www.testingcatalog.com` / `gemini.google` ほかを復旧とした。`claude.dev` / `www.geekwire.com` は拒否が継続し、`x.ai` はオリジン403に変わった。Copilot と industry は変化なし
- ソース間の差分・矛盾:
  - Copilot の 10/19 廃止は、Master が5モデル、industry が GPT-5 mini を含む6モデルとしていた。一次（github.blog の 9/18 告知）を本日読み、6モデルが正しいことを確認した
  - industry は Anthropic の社内雇用調査をハイライト1にしたが、本サマリーは 10/18 にカテゴリで既報のため、追加数値だけをカテゴリに置いた
  - Anthropic Public Benefit Fund は industry がハイライト2、Master がカテゴリだった。期限も操作の変化も無いため、本サマリーはカテゴリに置いた
  - 10/30 の ChatGPT Pro 200 の枠変更は、Master が「半減」、industry が「Plus 比10倍」で二次どうしの割れが続いている
