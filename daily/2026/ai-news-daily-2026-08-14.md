# AI News Daily Summary — 2026-08-14

金曜は、本日そのものが期限になった日である。Claude Code は Pro / Max / Team の既定モードを auto mode へ切り替え、承認の主体を人から分類器へ移した。ChatGPT Enterprise / Edu は個人が認可した同期コネクタを本日無効化し、同期済みデータの削除を始める。2日後の 8/16 には DeepSeek がピーク帯の出力単価を4.7倍に上げる。価格側では Google が Gemini 3.7 Flash を半額の導入価格で GA し、期限を 12/31 に置いた。Microsoft 側は Power Automate の Release Wave に緑チェックが4件付き、「まだ来ていない」と扱っていた4機能が7月中にリリース済みだったと判明している。

## 今日のハイライト

### 1. Claude Code の既定が本日 auto mode へ切り替わった — 承認の主体が人から分類器に移る

**要点**: 本日 8/14 から Pro / Max / Team の新規セッションが auto mode で始まる。前提が「危険な操作は人が都度承認する」から「分類器が既定で審査し、拒否ルールを書いていなければ止まらない」へ変わる。

**詳細**: auto mode は別モデルの分類器がシェルコマンドと操作を実行前に審査し、要求を超えた権限昇格・未知のインフラへの接続・読み込んだ敵対的コンテンツに誘導された挙動を止める。1,053人の対照試験では、仕込んだ危険コマンドの検出率が人手 **13.6%** に対し **89%** だった。分類器のトークン費用は Pro / Max / Team の利用上限には算入されない。既定モードを変更していない利用者には当日にアプリ内通知が出て、別の既定を設定済みの場合は切り替えるかどうかを一度だけ聞かれる。統制の書き場所は次の2層になる。

- managed settings: `defaultMode` で既定モードを固定し、`disableAutoMode` で auto mode 自体を封じる
- `autoMode` の細目: `environment` / `allow` / `soft_deny` / `hard_deny`。⚠️ `allow` を書く際に `"$defaults"` を配列へ含めないと組み込みルールが消える

既定化の範囲は当面この3プランで、Claude Enterprise・Claude API・AWS 上の Claude Platform・Amazon Bedrock・Google Cloud Agent Platform・Microsoft Foundry はオプトインのまま、1カ月以内に既定へ移す計画が示されている。⚠️ 08-09 収録の AI Now Institute の PoC「Friendly Fire」は、素の auto mode 構成のまま第三者ライブラリのセキュリティレビューを依頼するとホスト上でのコード実行に至ることを示していた。本日の既定化はその構成が3プランの全利用者へ既定として広がることを意味するため、統制はプロンプトではなく拒否ルールとサンドボックス設定の側で書く必要がある。

- https://claude.com/blog/auto-mode-default-in-claude-code
- https://claude.com/blog/auto-mode-in-production
- https://code.claude.com/docs/en/permission-modes

### 2. ChatGPT Enterprise / Edu の個人同期が本日停止し、同期済みデータの削除が始まる

**要点**: 個人が自分で認可した同期コネクタが本日無効化され、紐づく同期済みデータの削除が始まる。前提が「利用者が各自でファイル連携する」から「管理者が同期を設計しないと社内知識が消える」へ変わる。

**詳細**: 対象は ChatGPT Enterprise / Edu の connected apps である。8月10日から個人が新規に認可する同期接続を作れなくなり、**8月14日**に既存の個人同期接続が無効化されて同期済みデータの削除が始まる。管理者が管理する同期（admin-managed sync）は影響を受けない。管理者側に求められる対応は次のとおり。

- Google Drive: プラグインを有効化する。同期済みナレッジが必要な場合は **domain-wide delegation** で管理者管理の同期を構成する
- SharePoint: プラグインを有効化し、同期済みナレッジが必要な場合は管理者同期を構成する
- GitHub: 同期を伴わない GitHub プラグインを有効化する

連携の設計責任が利用者から管理者へ移り、対応を取らなかったワークスペースでは同期済みナレッジが失われる。⚠️ 一次の `help.openai.com` はオリジン403（`curl` HTTP 403）で本文に到達できず、リリースノートを引く二次スニペットの突き合わせで構成した。本サマリーも 08-13 まで本件を扱っておらず、実施当日での捕捉になっている。

- https://help.openai.com/en/articles/10128477-chatgpt-enterprise-edu-release-notes
- https://releasebot.io/updates/openai

### 3. DeepSeek の値上げが 8/16 実施で確定した — ピーク帯の出力は4.7倍になる

**要点**: DeepSeek が V4-Flash / V4-Pro を 8/16 16:00 UTC に値上げし、ピーク／オフピークの二段課金を新設する。前提が「出力 $0.28 の定額で最安」から「時間帯で単価が変わり、日本の日中がピーク側に入る」へ変わる。

**詳細**: 実施は 8月16日 16:00 UTC（日本時間 8月17日 1:00）で、上げ幅はモデル・トークン種別・時間帯により50%から最大1,100%超に及ぶ。オフピークはピークの半額に設定される。

- ピーク帯: **01:00〜04:00 と 06:00〜10:00**（UTC）。日本時間では 10:00〜13:00 と 15:00〜19:00 にあたる
- V4-Flash 出力: 現行 $0.28（定額）→ ピーク $1.32 / オフピーク $0.66
- V4-Flash 入力（キャッシュミス）: $0.14 → ピーク $0.44
- V4-Pro 出力: $0.87 → ピーク $3.96 / オフピーク $1.98
- V4-Pro 入力（キャッシュミス）: $0.435 → ピーク $1.32

DeepSeek は改定理由を「リソースをより合理的に配分するため」と説明し、二段課金で処理を混雑の少ない時間帯へ移すことを狙うとしている。08-09 収録の予告（北京時間の平日 9〜12時・14〜18時で単価2倍）と比べると、時間帯の区切りは一致したが倍率は大きく上回った。日本のオフィス時間はピーク帯とほぼ重なるため、国内から日中に叩く構成では実効単価が最も高い側に入る。⚠️ 一次料金表の `api-docs.deepseek.com` はゲートウェイ拒否で到達できず、二次報道の突き合わせで構成した。「最大1,100%」がどの課金区分に掛かるかは本日時点で確定できていない。

- https://qz.com/deepseek-api-price-increase-v4-peak-off-peak-081326
- https://dataconomy.com/2026/08/06/deepseek-significant-api-price-increase-2026/

## カテゴリ別まとめ

### Anthropic / Claude

- Anthropic が Claude Code の既定を auto mode へ切り替えた（ハイライト1参照）
- Anthropic が Claude Code **v2.1.229**（8/12）と **v2.1.231**（8/13）を公開した。v2.1.229 は30項目超の大型で、統制に効く変更が3件ある。⚠️ v2.1.230 は欠番である
  - `/commit-push-pr`: `--force` / `--amend` / `--no-verify` 等の危険フラグを含む git / gh コマンドを自動承認しないようにした
  - サンドボックス: ネットワークドメイン一覧の IPv6 リテラルを角括弧表記（`[::1]:443`）へ統一し、曖昧な綴りを fail-closed で弾いて `/doctor` に出す
  - セルフホストランナー: Windows の起動に `--base-dir` の明示を必須化し、`managed-mcp.json` 配備時の起動直後終了と Git Credential Manager でのハングを修正した
  - 本日の既定化に直結する修正として、`CLAUDE_CODE_ATTRIBUTION_HEADER` で帰属ヘッダーを無効化している利用者の全ツールコールが auto mode で失敗する不具合が解消した
  - ほかに Remote Control の `claude remote-control --continue`、ゲートウェイ経由の SSE keepalive ping、プラグインマーケットプレースの `command` ソース、VSCode 拡張のセッショングループが入った。v2.1.231 は Slack のような事前登録 OAuth クライアントを使う MCP サーバーでのサインイン失敗の修正1件のみ
- Anthropic が Chrome 拡張のサイドパネルを Claude Cowork のセッションへ統合した（8/12）。従来は孤立していたサイドパネルの会話が履歴に保存され、skills とコネクタがブラウザ内でも動くようになった。API を持たない社内ダッシュボードやベンダーポータルへブラウザ経由で到達させる使い方が想定されている。提供は Max / Team が即日、Pro は数週間かけて展開し、**Enterprise は既定オフ**で有効化と承認済みドメインの限定を管理者が握る。⚠️ Chrome 専用のままで、他の Chromium 系ブラウザとモバイルでは動かない
- Anthropic が Claude Tag（Slack 連携）の発言判断をチャンネル全体の文脈へ広げた（8/13）。従来はメッセージ単位を軽量分類器で評価していたが、チャンネルの文脈・メモリ・ユーザー設定の指示を使うようになり、発言すべきか黙るべきかの判定精度が**約 30% 改善**した。対象は Claude Teams / Enterprise で追加費用はなく、広げた文脈は使用量上限にも spend cap にもカウントしない
- Anthropic が Compliance API の対象を Claude Cowork と Claude Code へ広げた（8/11・既報）。セッション本文（プロンプト・応答・ツール呼び出し・アーティファクト）とメタデータを単一 API で引ける。⚠️ ベータのため Claude Code on web と Claude Platform は対象外で、Bedrock / Vertex AI / Microsoft Foundry 経由の配備も未対応
- Claude API release notes は 8/11 が最上位のままで、8/12〜8/13 の追加はない。Claude Release Notes（`support.claude.com`）も 8/6 の skill / plugin セキュリティスキャン beta から8日連続で動きがない
- 報道ベースの企業動向が3件あった。⚠️ いずれも Anthropic の公式発表ではない
  - Decart AI の買収交渉に入ったと報じられた（8/13・Bloomberg）。金額は約 **$6B** で、成立すれば同社最大の買収になる。Decart はチップ効率を上げる最適化スタック（DOS）とリアルタイム映像生成・world model を持つ。交渉は継続中で成立していない
  - 10月の IPO で $2T 超の評価額を目標としていると報じられた（8/13）。株主側は $3T まで見ているとされる
  - Q2 に初の四半期営業黒字 $559M（売上 $10.9B）を投資家へ示したと報じられた。ただし同社はデータセンター投資で次四半期以降は再び赤字になりうると明言している

### OpenAI

- OpenAI が ChatGPT Enterprise / Edu の個人同期を停止した（ハイライト2参照）
- OpenAI が Ultrafast モードを限定プレビューで公開した（8/13）。GPT-5.6 Sol を**最大 14 倍速・750 tokens/sec** で動かす新しい API サービス階層で、推論基盤は Cerebras の Wafer-Scale Engine である。知能は Standard の GPT-5.6 Sol と同一とされ、GDP-Val では5.6倍の高速化を品質低下なしで達成したと説明されている。比較値は Claude Opus 4.8 の Fast mode の約5倍、Claude Fable 5 の約11倍。⚠️ 課金レートは一次（オリジン403）で確認できておらず、本日時点では未確定として扱う
- Codex CLI の pre-release は 0.148.0-alpha.12（8/13 06:43 UTC）が最新で、安定版は 0.147.0（8/7）に据え置かれている。⚠️ alpha.12 の個別リリースノートはページ側のエラーで表示されず、内容は未確認である
- ChatGPT Voice がアップロード済みファイルと ChatGPT Projects に対応した。デスクトップアプリの内蔵ブラウザはアドレスバーから履歴の再訪と Google 検索ができるようになった。⚠️ いずれも掲載日は確定できていない
- 既報: GPT-5.4 / 5.4 mini の Codex 除外（8/31・移行先は `gpt-5.6-terra` / `gpt-5.6-luna`）、GPT-5.6-Cyber と Daybreak Blue / Red（8/10）、ChatGPT 広告テストの5ヶ国展開（8/11）

### Google / DeepMind

- Google が `gemini-3.7-flash` を GA した（8/13）。コーディングとエージェント向けの workhorse モデルという位置づけで、デバッグと課題解決の精度、少ないプロンプトで動く Web レイアウト生成、実業務ワークフローでの推論精度が上がったとされる
  - 導入価格は入力 **$0.75** / 出力 **$3.75**（100万トークン）で、**2026-12-31** まで有効。以後は $1.50 / $7.50 へ倍増するため、この単価で組んだ試算は年末で引き直しになる
  - 3.6 Flash の GA は 7/21 で、3週間で後継が GA した。一方 Gemini 3.5 Pro の GA は依然として未ローンチで、I/O（5/19）発表後に3回スリップしたまま動いていない
  - 提供面は Gemini アプリの Spark（AI Pro / Ultra 契約が必要）、Google Antigravity、AI Studio、Android Studio、Gemini Enterprise Agent Platform に及ぶ
- GitHub が Gemini 3.7 Flash を Copilot に追加した（8/13）。対象は Pro / Pro+ / Max / Business / Enterprise で、VS Code・Visual Studio・JetBrains IDE・Xcode・Eclipse・Copilot CLI・クラウドエージェントのモデルピッカーから選べる。⚠️ Business / Enterprise は管理者が Gemini 3.7 Flash Preview のポリシーを有効化しないと選択肢に出ない
- Gemini API の既存単価は据え置きで、Imagen 4.0 系3本の停止は **8/17** で期限まで3日となった。`gemini-robotics-er-1.6-preview` の 8/31 停止予定も変わっていない
- 8/12 の Made by Google 2026 はクラウド側の新モデル発表がなく、端末内処理（Tensor G6 / Gemini Nano 4 / Gemini Intelligence）が中心だった

### Microsoft / GitHub

- GitHub が Agent Plugins 1.0 を VS Code / Copilot CLI / Copilot SDK / Copilot アプリで GA した（8/12）。クライアントごとに manifest を書き分ける前提が消え、拡張の配布単位がベンダー横断で1つになる。仕様は 8/6 公開のベンダー中立標準で、Core Maintainer は Amazon / Anysphere / Microsoft / OpenAI / Vercel の5社に Google が加わった構成である
  - プラグインはアーカイブではなくディレクトリとして定義される: ルートの `plugin.json`、各サブディレクトリが `SKILL.md` を1つ持つ `skills/`、MCP サーバー構成の `mcp.json`、`com.github.copilot/` のような逆ドメイン名のクライアント固有ディレクトリ
  - GA は全 Copilot プランで、プラグインのガバナンス機能は Business / Enterprise が対象
  - ⚠️ v1.0.0 には権限モデル・サンドボックス・署名検証・シークレット機構のいずれも無く、すべて future work とされている。⚠️ Anthropic は Core Maintainer にもローンチクライアントにも入っておらず、Claude Code は独自のマーケットプレース機構を続けている
- Copilot Notebooks が Markdown・プレーンテキスト・リッチテキストのファイルを参照ソースとして受け付けるようになった（8/13・記事ID 4545652）。README・Wiki・ログ・書き起こしを Office 形式へ変換する前処理が不要になる。管理者の設定は不要で、既存の権限はそのまま効く。⚠️ 展開時期の記述が食い違っており、本記事は3形式まとめて「8/13 の週から」とするのに対し、二次経由で索引に出る MC1423103 は「TXT と RTF は7月に展開済み、Markdown は8月」と書いている
- 事業者が M365 Copilot Chat の中から LegalZoom の法務サービスを呼び出せるようになった（8/12・記事ID 4546016）。LLC 設立の手順案内、弁護士への接続、契約条項の評価に対応し、配布は Microsoft Marketplace 経由である。Copilot のやり取りは基盤モデルの学習に使われない
- M365 Copilot Release Notes は August 11, 2026 バッチのままで本日の新バッチはなく、次バッチは隔週傾向どおりなら 8/25 前後の見込みである。Microsoft 365 Roadmap と Microsoft 365 Blog（本体）にも新規はない
- M365 Developer Blog が Teams 上のエージェントの振る舞いを扱う記事を出した（8/13）。会話を埋めないための API 利用パターンとして、`addReaction()` / `deleteReaction()` による受領応答、`reply()` によるスレッド返信、`quote()` と `send()` による引用返信を挙げている。⚠️ 設計パターンの解説で、提供段階の発表は含まれていない
- Microsoft 365 管理センターのマルチテナントエージェント管理が public preview で提供開始された。顧客テナント・子会社テナントを横断してエージェントを1画面で管理できる
- Copilot CLI は v1.0.79（8/10）が最新のままで、4日間動きがない
- 既報: MAI-Code-1-Flash の 9/10 廃止（移行先の MAI-Code-1.1-Flash は Business / Enterprise で既定オフ）、JetBrains 版の Copilot memory と Ollama 連携（8/11）

### Copilot Studio / Power Platform

- Power Automate の計画機能4件に緑チェックが付き、すでにリリース済みだったと判明した。`planned-features` が6日ぶりに更新され（`ms.date` 8/4 → **8/11**）、期日超過は延べ12行から6行へ半減した。⚠️ 4件とも Power Automate Blog にも月次記事にも Release Notes にも告知がなく、Release Wave の緑チェックだけが一次シグナルだった
  - ローカル AI モデルへの接続（デスクトップフロー）: Public preview 2026-06-30
  - 現行 Python バージョンでのスクリプト実行 / PowerPoint 操作の自動化: Public preview 2026-07-31
  - ワークキュー項目の CSV エクスポート: GA 2026-07-31
  - 期日の後ろ倒しも4件あり、マシン・フロー稼働率ダッシュボードが GA Jul → Sep、デスクトップフローの直接スケジュール実行とフローチャート表示が Public preview Jul → Aug、カスタムダッシュボードタイルが Public preview Aug → Sep になった
- Power Platform 管理センターの Licensing > Copilot Studio > Manage Agents で、エージェント単位の月次消費上限を設定できることを確認した。125% のエンフォースメントが働く前に個別に頭を打たせる経路であり、テナント全体の容量が1つのプールである以上、暴走した1エージェントを他から隔離する手段はここにしかない。消費レート自体は 8/11 の一次確認から変化していない
- Copilot Studio の What's New は節構成が June 2026 のままで、7月節も8月節も追加されていない。⚠️ GitHub Copilot ハーネスは 8/3 に GA しているのに `(Production-ready preview)` の表記が残り、未反映が11日連続になった。Released Versions も **2026.6.3**（6/30 初出）のままで、6週間半にわたって新ビルドが出ていない
- Power Platform Community Conference 2026 の登録記事が Power Automate / Power Apps 両方の子カテゴリページに出た（8/13）。会期は **10/27〜29**・MGM Grand ラスベガスで、前日ワークショップが 10/25〜26、翌日が 10/30 である。基調講演は Charles Lamanna と Ryan Cunningham。⚠️ 標準価格での登録は 8/18 までで、チーム申込には最大20%の割引がある

### ガバナンス・ライセンス

- CSP ソフトウェアサブスクリプションへの5%上乗せが 2026-10-01 から適用される（Partner Center の8月アナウンスに 8/12 付で追記）。対象は年間契約かつ月次請求の SQL Server / Windows Server / CAL / System Center 等で、既存分は 10/1 以降の更新時に発効する。年次請求と月単位サブスクリプションは対象外である。⚠️ 本アナウンスは以前の通知に誤った発効日が含まれていたことの訂正で、M365 Copilot / Copilot Studio のライセンスは対象に含まれない
- Copilot Success Planner の提供開始日が本日 8/14 にあたる。⚠️ 配信先の skilling-hub 側で提供開始を一次確認できていない
- Microsoft Purview の `whats-new` は7月節に Copilot 関連の新規追加がなく、8月節は未作成である。SharePoint Blog と Agent 365 Blog も 8/6 の月次記事が最新のままである

### Cursor / xAI / その他開発ツール

- Cursor が Cloud Agents に Builds を導入した（8/13）。リポジトリ・ツール・依存関係をあらかじめ焼いたマシンスナップショットからエージェントを起動する仕組みで、内部計測では環境の起動時間が**10 分の1**、first token までが3分の1になったとしている
  - clone・install・依存解決を事前に済ませるため、エージェントは準備済みの状態から始まる
  - 設定が壊れても直前の成功 Build から起動し続けるので、デバッグ中に環境が使えなくなることがない
  - 新規環境は自動で Builds を使い、既存環境は Builds タブの「Enable Builds」から切り替える
- xAI は 8/13 も一次に到達できていない。二次では Grok 4.6 と同時にコーディングエージェント Grok Build が Cursor 上で使える旨と、Grok 4.7 が数週間内という観測が出ているが、⚠️ いずれも一次未確認として扱う
- Devin は 8/7 の Automations Queueing Support 以降に新規がない

### MCP / オープンウェイト

- MCP 公式ブログは新着がなく、RSS 最新は 7/28 の `The 2026-07-28 Specification` のまま17日連続で動きがない。Tier 1 SDK にも変化はない
- ⚠️ Agent Plugins 1.0 は MCP を置き換えるものではなく、MCP サーバー構成（`mcp.json`）を skills と一緒に梱包する層であり、両者は競合しない
- 8/12〜8/13 に公開された注目のオープンウェイトモデルはない。HF の作成日降順100件を走査したが、この期間の新顔は第三者による量子化・改変版に集中していた。Qwen3.8-27B は未公開が継続している

### 市場データ・その他

- IDC / MM総研 / Similarweb は本日時点で新規の調査・プレスリリースがない。国内 AI 市場支出額の最新予測は2026年3月発行の 2兆3,725億円（2025年）→ 6兆8,897億円（2029年・CAGR 36.0%）のままである
- `developer.apple.com` は 8/12 の年齢レーティング更新以降に新規がなく、AI 関連の最新は 8/5 のままである。iOS 27 / iPadOS 27 は developer beta 4（7/20）が最新で、GA は9月見込みである

## 直近の注目予定

- **8/14**（本日）: Claude Code の既定が auto mode へ（Pro / Max / Team） ／ ChatGPT Enterprise / Edu の個人同期停止と同期データ削除開始 ／ Copilot Success Planner 提供開始
- **8/16**: DeepSeek の値上げ実施（16:00 UTC＝日本時間 8/17 1:00） ／ Alibaba が表明した Qwen3.8 重み公開の週の終わり ／ Power CAT・PnP の週次確認
- **8/17**: Claude Console 旧 Workbench 退役と実験的プロンプトツール API 廃止 ／ Gemini API の Imagen 4.0 系3本停止 ／ Gemini in Classroom のモバイル開放
- **8/18**: PPCC 2026 の標準価格での登録期限 ／ Copilot Studio Released Versions の次回定例
- **8/19**: Claude Code 週次上限50%増の終了（23:59 PT）
- **8/20**: Gemini Enterprise Agent Platform の Grok 4.1 ファミリー停止（一次未確認） ／ Pixel 11 系の出荷開始
- **8/22**: M365 Copilot アプリのチャット中心 UI が Deferred リングへ展開開始
- **8/25 前後**: M365 Copilot Release Notes の次バッチ（隔週サイクルどおりなら）
- **8/26**: OpenAI Assistants API 廃止 / o3 退役 / GPT-4.5 完全廃止 ／ Copilot 既定モデル有効化ポリシー発効
- **8/30**: 公式 DALL·E GPT の退役
- **8/31**: GitHub Spark の既存ユーザーアクセス終了 ／ `gemini-robotics-er-1.6-preview` 停止 ／ GPT-5.4・5.4 mini が Codex（ChatGPT サインイン）から除外 ／ Claude for Government の $1/機関プログラム終了 ／ Power Automate モバイルアプリ廃止 ／ CSP Copilot Partner Council コンテスト応募期限
- **9/1**: GitHub Copilot の全体験でモデル廃止 ／ OpenAI Daybreak 全アカウントでハードウェアセキュリティキー必須化
- **9/2〜9/3**: Windows 365 Frontline 名称での購入最終日（9/2）→ Flex へ改称（9/3）
- **9/10**: MAI-Code-1-Flash が全 Copilot 体験から廃止
- **9月**: iOS 27 / macOS 27 GA ／ auto mode の既定化を Enterprise・API・各クラウドへ拡大予定 ／ 2026 Wave 1 の対象期間終了（9月末）
- **10/1**: CSP ソフトウェアの5%上乗せ発効 ／ M365 E7 プロモーションの新規取引停止
- **10月**: Anthropic の IPO 予定（$2T 超の評価額を目標と報道） ／ PPCC 2026 本編とワークショップ（10/25〜30）
- **12/2**: EU AI Act の生成コンテンツ標識義務、8/2 以前に市場投入済みシステムへの猶予終了
- **12/31**: Gemini 3.7 Flash の導入価格終了（$0.75/$3.75 → $1.50/$7.50）

## 改善メモ

- ソース間の食い違い: Copilot Notebooks の展開時期が Tech Community 記事（3形式まとめて 8/13 の週）と MC1423103（TXT / RTF は7月、Markdown は8月）で一致していない。⚠️ MC1423103 は 02 側に一度も掲載がなく、TXT / RTF の7月展開を取りこぼしていた。Message Center の一次取得がゲートウェイ拒否で7日連続できていないことが背景にある
- 未登録ソース2件が本日のハイライト・主要項目の唯一の一次経路になっている。⚠️ `claude.com/blog`（01 側 B-017・回数12）と Gemini API changelog（`ai.google.dev`・01 側 B-034 で新規起票）。前者は本日の Anthropic 側3件、後者は Gemini 3.7 Flash の一次にあたる
- 一次未達のまま二次で構成した項目が3件ある: DeepSeek の新単価（`api-docs.deepseek.com` ゲートウェイ拒否）、ChatGPT Enterprise / Edu の個人同期停止（`help.openai.com` オリジン403を実測で再確認）、Ultrafast モードの課金レート（未確定として保留）
- 障害の変化: 二次ソース `www.globenewswire.com` / `www.cerebras.ai` / `qz.com` / `blog.google` / `www.edenai.co` を新規のゲートウェイ拒否として記録した。Copilot Credits Guide の PDF は 403 から `EGRESS_BLOCKED` へ分類変更し、ファイル名も `Microsoft-Copilot-Credits-Guide-August-2026.pdf` へ変わっていた
- 各ソースの継続提案: 01 が14件（最多 B-013・18回目）、02 が17件（最多 B-011・26回目）＋新規 B-033（board RSS を先頭N件で打ち切ると新着を落とす）、03 が4件（最多 B-004・46回目）
