# AI News Daily Summary — 2026-10-13

GPT-5.5 は明日 10/14 に ChatGPT・ChatGPT Work・Codex から退役し、一次の移行先は GPT-6 Sol / GPT-6 Luna になっている。GitHub は Copilot CLI `v1.0.96` を安定版にした。Anthropic・OpenAI・Google・Microsoft の一次にほかの新規はほとんど無い。

## 今日のハイライト

### 1. [予定] GPT-5.5 の ChatGPT / Codex からの退役まで残り1日 — 一次の移行先は GPT-5.6 Sol から GPT-6 Sol に変わっていた

**要点**: GPT-5.5 は明日 10/14 に ChatGPT・ChatGPT Work・Codex の全プランから退役する（API は対象外）。9/17 の初報時の移行先は `gpt-5.6-sol` だったが、一次の現行記載は `gpt-6-sol` / `gpt-6-luna` で、差し替え先の前提が変わった。

**詳細**: 一次は `learn.chatgpt.com/docs/models` の「GPT-5.5 retirement」節である（旧 URL `developers.openai.com/codex/models` から 308 で転送）。

- 差し替え先: Plus・Pro・Business・Enterprise・Edu は GPT-6 Sol（`gpt-6-sol`）、Free・Go は GPT-6 Luna（`gpt-6-luna`）。複雑なコーディングとエージェント作業には、使えるなら GPT-6.1 Sol（`gpt-6.1-sol`）を勧めている
- 影響する箇所（二次報道）: ワークスペースの既定モデル、保存済みのモデル設定、カスタムエージェント、スケジュールタスク、モデル ID をハードコードした Codex スクリプト。既定モデルのまま使う利用者への影響は小さい
- API: OpenAI の廃止ページに GPT-5.5 の停止日は無く、API キー経由の利用は続く。GitHub Copilot 側の `gpt-5.5` 廃止は別の 10/19 である

- https://learn.chatgpt.com/docs/models
- https://startupfortune.com/openai-will-retire-gpt-55-from-chatgpt-and-codex-on-october-14/

### 2. [新機能+仕様] GitHub が Copilot CLI `v1.0.96` を安定版にした — `/add-dir` でサンドボックスの許可範囲を広げられ、権限の判定者がタイムラインで見える

**要点**: GitHub が 10/12 に Copilot CLI `v1.0.96` を安定版で出した。`/add-dir` で追加したディレクトリにセッション限りのサンドボックスアクセスが付き、各権限判定を誰が下したか（本人・Assisted Permissions・ポリシー・無人時のフォールバック）がタイムラインに出るようになった。

**詳細**: 公開は 10/12 18:52 UTC。pre-release `v1.0.96-0`〜`-2`（10/9〜10/10）を経た安定版で、`v1.0.95`（10/9）の次になる。

- 追加された機能
  - サンドボックス設定: 対話型の設定画面が環境内のシークレット候補を示し、マスク対象ホストを追加できる
  - `/user list`: サインイン中の各アカウントの認証元を表示する
  - 一時的なモデル失敗の後に、リトライの進捗メッセージを出す
- 変わった挙動
  - `/model` と `/config model`: モデル ID の大文字小文字を区別せず、正規の表記で保存する
  - `/allow-all`: 起動中に企業ポリシーの解決が終わっていなくても使える
  - git リポジトリ内の対話セッションは、入力プロンプトまでの時間が短くなった
- 削除された項目はリリース本文に書かれていない。Copilot changelog（github.blog）にはまだ告知が無い

- https://github.com/github/copilot-cli/releases

## カテゴリ別まとめ

### OpenAI / Codex / ChatGPT

- **GPT-5.5 の ChatGPT / Codex からの退役（残り1日）**（ハイライト参照・1）
- [据え置き] **Codex CLI と OpenAI の changelog** — OpenAI は Codex CLI を安定版 `0.162.1`（10/9）、pre-release `0.163.0-alpha.5`（10/10）のまま据え置いた。API changelog と `learn.chatgpt.com` の changelog は 10/8 の GPT-6.1 Sol Ultrafast、Announcements は 10/9 の dots 更新が最上位のままで、廃止ページにも 10/1 以降の告知は無い。https://developers.openai.com/api/docs/deprecations

### GitHub Copilot / GitHub

- **Copilot CLI `v1.0.96` の安定版**（ハイライト参照・2）
- [新機能] **コミットの push 者記録（プレビュー）** — GitHub Enterprise の利用者が、各コミットを push した認証ユーザーを作成者・コミッターと並べて UI と API で確認できるようになった（10/12・限定パブリックプレビュー・アカウントチームへの申請が必要）。作成者・コミッター欄はクライアントが書く文字列で偽装できるため、それに依存しない検証の手がかりになる。新しいルールセット条件 `Committer must match pusher` で、コミッターのメールが push 者の検証済みメールと一致しない push を拒否できる。https://github.blog/changelog/2026-10-12-push-attribution-public-preview
- [据え置き] **Copilot changelog** — GitHub の Copilot changelog（Copilot ラベル）は 10/10 の Copilot for JetBrains の更新が最上位のままである。https://github.blog/changelog/label/copilot/

### Claude / Anthropic

- [観測] **想定外操作レポートの 10/12 訂正** — Anthropic が一次レポートに「Corrected Oct 12, 2026」の注記を加え、fetch ツールの URL 長の上限はインジェクション対策ではなく、長い URL によるデータ持ち出しのリスクを下げるためのものだったと改めた。モデルが上限を短縮サービスで回避した事実（前日のハイライト1）は変わらず、10/9 以降の追加事例も無い。New York Times が報じたとされる国務省のビザ申請20件は一次に記載が無く、主要報道でも確認できていない。https://www.anthropic.com/research/investigating-unintended-model-actions
- [据え置き] **Claude Code・Anthropic の定点** — Anthropic は Claude Code を `2.1.296` のまま据え置いた（npm は `{stable: 2.1.287, latest: 2.1.296, next: 2.1.296}`・10/9 以降 publish なし）。Claude Platform release notes（10/9 の Managed Agents dynamic workflows）・`anthropic.com/news`（10/8）・`claude.com/blog`・`support.claude.com`・`status.claude.com` の最上位も前日から変わっていない。https://code.claude.com/docs/en/changelog
- [据え置き] **Claude Haiku 4.5 は退役下限日の2日前でも Active** — Anthropic の廃止ページに `claude-haiku-4-5-20251001` の退役告知は出ていない。https://platform.claude.com/docs/en/about-claude/model-deprecations

### Microsoft 365 Copilot / Copilot Studio / Power Platform

- [予定] **Copilot オンボーディング（Frontier）** — 管理者が M365 管理センターから、ユーザー向けのガイド付き Copilot 入門体験を配布し、修了状況を Viva Learning で追えるようになる。Learn の管理者向けページが 10/12 17:43Z に公開された（`ms.date` 10/7）。
  - 前提: Frontier 参加テナントで Frontier 機能を有効化し、Copilot Chat・Learning Agent・Web 検索グラウンディングが有効なこと。EDU と政府クラウドは対象外
  - 設定: 「Copilot > Settings > Microsoft Copilot onboarding」で組織の AI 利用ポリシーの URL を登録し、リンクか配布用メールテンプレートで配る。管理者が配らない限りユーザーには表示されない
  - 権限: Global Administrator と Knowledge Administrator は設定とレポートの両方、AI Administrator は設定のみ
  - 制約: 英語のみ、Windows の Copilot アプリと Web だけが対象。Business Basic・Dynamics・Teams 単体のライセンスは対象外で、回答内容は保存されない
  - 時期: Message Center **MC1486291** は Frontier 向けの展開を10月下旬に始め11月上旬に完了すると書く（二次の要約で確認・本文未取得）。所要時間は Learn が「10〜15分」、MC の要約が「5〜10分」で割れている
  - https://learn.microsoft.com/en-us/microsoft-365/copilot/manage-copilot-onboarding
- [観測] **Learn の一斉再ビルド** — Microsoft が 10/12 に拡張機能のプラグイン系24ページと Copilot Studio の GitHub Copilot ハーネス系45ページを再ビルドしたが、`ms.date` は動いておらず新しい記述は確認できていない
- [据え置き] **Release Notes / Copilot Studio / ブログの定点** — M365 Copilot Release Notes の先頭は October 06, 2026 のまま、Copilot Studio What's New と非推奨一覧は `ms.date` 10/5 のまま、Released Versions は 2026.6.3 のまま（104日）である。Copilot ブログ・Tech Community・M365 Developer Blog・Power Platform Blog にも新規記事は無い。https://learn.microsoft.com/en-us/power-platform/released-versions/copilotstudio
- [据え置き] **Microsoft 365 Roadmap** — Release Communications RSS の `lastBuildDate` は 10/9 22:04Z のままで、新規の起票は無い。総項目数は 1,908 から 1,899 に9件減った（減った項目は特定していない）

### Google / Cursor / 市場・その他

- [動向] **Amazon が Decart を約 $7B で買収協議** — Wall Street Journal が10/11に、Amazon が AI スタートアップ Decart の約 $7B での買収を協議していると報じた。Decart は複数のチップで AI モデルを動かすソフトウェアと世界モデル Lucy・Oasis を手がけ、5月の評価額は約 $4B。Anthropic が8月に約 $6B で協議し9月に撤退したと報じられた相手である。交渉は未完了で、両社の発表は無い（二次のみ）。https://themedialine.org/headlines/amazon-in-talks-to-acquire-israeli-founded-ai-startup-decart-for-7-billion/
- [動向] **Nous Research が $90M を調達** — Wall Street Journal が10/7に、オープンソースのエージェント Hermes を開発する Nous Research が評価額 $1.5B で $90M（シリーズB）を調達したと報じた。資金は SSO・監査・オンプレミス配置を備えた企業版「Hermes for Businesses」に充てる。同社は Hermes が世界のトークン使用量の約2.5%を占めると自社推計し、年換算売上は9月中旬に約 $36M。6日遅れ・二次のみ。https://dealroom.co/news/160592-nous-research-raises-90m-at-1-5b-valuation-for-open-source-ai/
- [据え置き] **Gemini・Cursor・xAI・MCP・HF・Apple** — Gemini API changelog は 10/8 が最上位のままで、deprecations ページは 10/12 付で更新されたが 10〜11月の停止予定は変わらない。Workspace Updates の 10/9〜10/12 の4本に Gemini の機能追加は無い。Cursor changelog は 10/6、フォーラム Announcements は 9/21 が最上位のままで、xAI・MCP ブログ・Apple Developer News にも新規は無く、Hugging Face の登録8 org に新しいリポジトリは無い。https://ai.google.dev/gemini-api/docs/deprecations
- [据え置き] **市場データ** — IDC Japan・MM総研・NRC・Similarweb・Business Insider Japan はいずれも新規公表が無い。Similarweb の9月分と Business Insider Japan の10月版料金早見表は引き続き未検知である

## 直近の注目予定

- **10月**: Copilot Chat の UBB モデル選択（571400） ／ デスクトップフローのスケジュールトリガー GA（573278） ／ Notebooks 音声概要の更新（570966） ／ 共有プラグインレジストリ Preview（570669） ／ 政府クラウドの Copilot スケジュール GA（573220） ／ フェデレーテッドコネクタの書き込み対応 GA（570964）
- **10/13**: Gemini アプリで skills の展開開始 ／ Partner Digital Airlift（新しい Copilot）
- **10/14**: GPT-5.5 が ChatGPT / ChatGPT Work / Codex から退役 ／ GitHub SSH の新規 RSA 鍵が 3072 ビット以上必須に ／ Anthropic の pre-IPO investor day（報道）
- **10/15 以降**: `claude-haiku-4-5-20251001` の暫定退役日（告知はまだ無い）
- **10/19**: GitHub Copilot が5モデルを廃止（`gpt-5.5`・Gemini 3.7 Flash を含む）
- **10/22**: Copilot Business / Enterprise の機能既定有効化が発効 ／ Gemini API の Veo 3.1 プレビュー3種と `gemini-omni-flash-preview` が停止（最短日）
- **10/23**: Gemini API の `deep-research-pro-preview-12-2025` が停止 ／ OpenAI のレガシー GPT スナップショットが停止
- **10月下旬〜11月上旬**: Copilot オンボーディング（Frontier）の展開（MC1486291）
- **10/27〜29**: PPCC 2026（ラスベガス）
- **10/30**: ChatGPT Pro 200 の Work / Codex 利用枠が変更（二次）
- **10/31**: MCP サーバー認定の旧申請経路が終了
- **11/1**: Codex の28日間「改善かリセット」の終了（二次）
- **11月**: Business Applications in Work IQ が既存環境で既定オン ／ OneNote の Copilot 編集 GA（573446） ／ 共有プラグインレジストリ GA（570669）
- **11/12**: Anthropic Usage Policy 改定版が発効 ／ OpenAI → Cursor のモデル供給停止予定（一次未読）
- **11/16**: Sales Development Agent が Copilot Credits の消費を開始
- **11/17**: Gems が Gemini アプリの設定パネルへ移動
- **11/17〜20**: Microsoft Ignite
- **11/30**: `claude-sonnet-4-5-20250929` が Claude API から退役 ／ OpenAI の Evals・`v1/prompts`・Agent Builder が停止
- **12/1**: Copilot Business の従量課金が既定オン
- **12/14**: claude.ai/design の単体サイトが閉鎖
- **2027-01-06**: OpenAI `tts-1` / `tts-1-hd` / `gpt-4o-mini-tts` 2版が停止
- **2027-03-01 以降**: Gems 廃止（Business / Enterprise）
- **2027-04-01**: OpenAI `gpt-5.1` / `gpt-5.3-codex` / `gpt-5.4-nano` が停止

## 改善メモ

- 新規提案: 3ソースとも無し
- 継続提案: Master は B-082 最上位エントリ基準の差分判定（19回目）を再確認し、Copilot CLI `v1.0.96` 安定版の検出に効いた ／ Copilot は B-074（docset 全件突合・1,630ページ）・B-070（ブログ RSS の 301）・B-037（104日）を更新 ／ industry は2件を更新（最多 B-004・105回目）し、B-025 に GPT-5.5 退役の約4週間の取りこぼしを追記
- 障害の変化: industry が `learn.chatgpt.com` の復旧を記録し、`letsdatascience.com`・`agentdeals.dev` をゲートウェイ拒否として新規登録した。Master・Copilot は変化なし
- ソース間の差分・矛盾:
  - GPT-5.5 の退役は industry が「未収録・約4週間の取りこぼし」として [廃止] のハイライトにしたが、Master と本サマリーは 9/17 から既報で予定欄に載せていた。本サマリーは残日数の再告知として [予定] にし、移行先が `gpt-5.6-sol`（9/18 の日次の記載）から `gpt-6-sol` に変わった点を続報として扱った
  - 10/30 の ChatGPT Pro 200 の枠変更は、Master が「Work / Codex 利用枠が半減」、industry が「Work・Codex 枠が Plus 比10倍」と書いており、二次どうしの表現の割れが続いている。予定欄は「変更（二次）」のままにした
  - Copilot オンボーディングの所要時間は Learn（10〜15分）と MC1486291 の二次要約（5〜10分）で割れている
