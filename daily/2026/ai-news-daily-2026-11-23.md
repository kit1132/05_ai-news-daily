# AI News Daily Summary — 2026-11-23

Dragos の調査で、安価な推論プロバイダー経由で数百件の AWS キーが盗まれ、OpenRouter は125エンドポイントのデータ保持ゼロ（ZDR）承認を取り消した。Copilot Studio のエージェントのメモリは GA 展開に入り、記憶は28日使われないと消える。ChatGPT Space が Plus に広がって Library を置き換え、共有したページは無料ユーザーには開けない。

## 今日のハイライト

### 1. [セキュリティ] 安価な AI 推論プロバイダー経由で AWS キーが盗まれた — ルーターの「データ保持ゼロ」表示は、送信先が守っている前提にできなくなった

**要点**: Dragos が偽の認証情報を仕込んだ約200万件のリクエストで調べると、少なくとも3社の推論プロバイダーが侵害され、数百件の AWS キーが抜かれた。OpenRouter は3社を外し、125エンドポイントの ZDR 承認を取り消した。ZDR 表示だけでは送信先を信用できない。

**詳細**: The Decoder（11/22）が Dragos の調査（2026年7〜11月）を報じた。Dragos の一次ブログと Ars Technica（11/20）はゲートウェイ拒否で読めていない（industry）。
- 鍵の窃取: プロバイダーが拒否したリクエストに含まれていた鍵も盗まれた。数時間以内に鍵を試し、S3 を探って居座ろうとした攻撃者がおり、1人は AI の攻撃ツール ARTEX を使った
- 盗み見: マーケットプレイスの再販業者が、モデルを最安値で出品してログを有効にし、利用者のリクエストを読んでいた。抜いたパスワードで SSH ログインを試みた例もある
- ZDR の不履行: 中国の AI 研究所が、米国のプロバイダーを通したものも含め半数を超えるリクエストの秘密のテスト URL にアクセスした。米大手でも、1回送っただけのテスト URL を2カ月以上クロールした例があった
- 名前が出た事業者: Novita・Phala・Together・AtlasCloud・StreamLake。どこが侵害されたかは記事に書かれていない。OpenRouter は MiniMax のモデルへのリクエストを第三者が読んだ可能性があると利用者に警告した
- Dragos の推奨: リクエストの経路を自分で管理し、カナリアトークンを仕込み、認証情報を仲介業者へ送らない

出典:
- https://the-decoder.com/security-researchers-show-how-cheap-ai-inference-providers-steal-keys-and-snoop-on-users/
- https://www.dragos.com/blog/ai-supply-chain-security-canary-tokens

### 2. [新機能+仕様] Copilot Studio のエージェントのメモリが GA 展開に入った — 利用者ごとの記憶は28日使われないと消え、管理者はサポート依頼なしには中身を見られない

**要点**: Microsoft Copilot ハーネスで作ったエージェントは、利用者の役割・好み・訂正を会話をまたいで覚えられるようになり、Learn の表記がプレビューから「GA 展開中」に変わった。記憶は28日使われないと削除され、延長できない。

**詳細**: `agents-experience/memory-*` の4ページ（11/20 01:04Z `90b63603`・`ms.date` 11/18）。日本語版は「Memory (preview)」の題のままで、What's New（`1e58d09d`）にはまだ載っていない（Copilot）。
- 有効化: メーカーが Build タブの Memory トグルで切り替える。オフにしても保存済みの記憶はすぐには消えない
- 分離: テナント・環境・エージェント・利用者ごとに Microsoft 管理のストレージに分けて保存され、他のエージェントへ移せない。独自のアカウントを持つエージェントは全員で共有するメモリを使う
- 保持: 最後に使われてから28日で削除される。ポータルで閲覧しても期間はリセットされない
- 利用者の操作: メモリポータルとチャットで確認・訂正・削除ができる。記憶を消しても会話履歴は残り、元のメッセージは回答に影響しうる
- 課金: このハーネスは従量課金で、利用・作成・テストで Copilot Credits を消費しうる

出典:
- https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-experience/memory-overview
- https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-experience/memory-manage-privacy

### 3. [新機能] ChatGPT Space が Plus に展開され、Library を置き換えた — Plus のページ・スライド・画像・アップロードファイルの置き場所が Space に移り、共有ページは無料ユーザーに開けない

**要点**: OpenAI が 11/20 から、Pro / Business / Enterprise 向けだった ChatGPT Space を18歳以上の Plus ユーザーに展開した。Library に代わってページ・スライド・画像・アップロードファイルがここに集まり、共有ページを見られるのは Space を使える有料アカウントだけになった。

**詳細**: `help.openai.com` が週次復旧チェックで読めるようになり、一次で確認した（Master）。
- 対象: 全地域の Plus（18歳以上）。Web・デスクトップアプリ・iOS・Android で作成と編集ができる
- できること: 対話的なページとプレゼンテーションを作り、Space を使える相手を共同編集に招く。接続したアプリやツールからページとスライドを自動で更新させられる
- 共有の制約: 閲覧には Plus / Pro / Business / Enterprise の Space が要り、公開リンクは無い。管理者向けの設定は release notes に書かれていない
- 経緯: ChatGPT Space / Pages は 9/29 の DevDay で Pro / Business / Enterprise 向けに出ていた

出典:
- https://help.openai.com/en/articles/6825453-chatgpt-release-notes

## カテゴリ別まとめ

### Anthropic / Claude

- [新機能] **Claude Mobile の新デザイン** — Anthropic が 11/20 から、Claude for iOS を先頭に新しいデザインを段階的に展開し始めた。チャット・プロジェクト・プランは変わらず、設定は要らない。iOS 26 以降が必要である（Master）
  - https://support.claude.com/en/articles/12138966-release-notes
- [予定] **Opus 4.5 の暫定退役日が明日（残り1日）** — `claude-opus-4-5-20251101` の「Not sooner than November 24, 2026」が明日に迫ったが、退役の告知は出ていない。Anthropic は最低60日前に通知すると書いており、明日退役することはない。モデル退役一覧の Active は17件のままである（Master・industry）
  - https://platform.claude.com/docs/en/about-claude/model-deprecations
- [据え置き] **Claude Code と Anthropic のその他の一次** — Claude Code の changelog は `2.1.330`（11/20）、npm は `{stable: 2.1.323, latest: 2.1.330, next: 2.1.330}` のままで、課金付き分類フォールバックの削除もまだ書かれていない。Platform release notes（11/17）、廃止履歴（9/30）、`/news`（11/20）、`/research`（11/17）、`claude.com/resources/articles`（11/17）も動いていない（Master・industry）
  - https://code.claude.com/docs/en/changelog

### OpenAI / Codex / ChatGPT

- **ChatGPT Space の Plus 展開**（ハイライト3参照）
- [新機能] **ChatGPT release notes の未掲載分4件** — OpenAI が 11/18〜11/19 に、Live Dictation を全プランに出し、Enterprise では管理者の承認が要る会計プラグインを出していた（Master）
  - Live Dictation（11/18）: 話しながら文字になり、10分の録音上限が無くなった。全プラン・iOS / Android / Web / デスクトップ
  - Accounting プラグイン（11/18）: 取引の照合、請求書の仕訳案、月次レポートの作成を手伝う。デスクトップアプリで computer use の設定が要り、Enterprise は管理者の承認後にメンバーがインストールできる
  - 新しいモバイル体験（11/19）: dot 専用のタブが付き、Codex・Projects・Images をタブバーに固定できる。Pro から順に展開し、EEA・英国・スイス・韓国は対象外
  - Health（11/19）: Android（Health Connect）・デスクトップアプリ・dots・sites に広がった
  - https://help.openai.com/en/articles/6825453-chatgpt-release-notes
- [観測] **Usage Policies の事前審査の範囲を一次で確認** — 前日のサマリーが二次で「第三者に直接アクセスを提供するサービス」と書いた条文を一次で読むと、対象は「第三者が OpenAI モデルに直接アクセスできるようにするモデルアクセス仲介プラットフォーム」だった。アプリの機能に OpenAI モデルを組み込んだだけでは対象にならない。発効は 11/20（Master）
  - https://openai.com/policies/usage-policies/
- [動向] **事前学習のパープレキシティの公開と上限案** — OpenAI のチーフサイエンティスト Jakub Pachocki が 11/22、社内のコードベースから作った評価用データで測った事前学習のパープレキシティを公開した。各社が共通の上限を決め、監視手法が育つまで超えないようにする案も示した。製品やモデルの発表は無い（Master）
  - https://openai.com/index/perplexity-and-intelligence/
- [観測] **misalignment reports の URL 移転** — 一覧が `alignment.openai.com` から `openai.com/safety-alignment/misalignment-reports/` に 308 で移った。First posted の最新は 11/18 のままで、新しいレポートは無い（Master・B-092）
  - https://openai.com/safety-alignment/misalignment-reports/
- [据え置き] **OpenAI のその他の一次** — Codex（安定版 `0.171.0`・pre-release `0.173.0-alpha.4`）、API changelog（11/19）、deprecations（11/18）、`learn.chatgpt.com` changelog（11/20）、community Announcements（11/20）、Deployment Safety Hub（11/17）は動いていない。料金ページの GPT-5.6 Sol の期間限定価格は「until November 30, 2026」のままである（Master・industry）

### GitHub Copilot / GitHub

- [版更新] **Copilot CLI `v1.0.115-6` / `-7`** — GitHub が pre-release（11/21〜22）で、プラグインのインストールの再試行、`/delegate` のサインイン表示、Unix で残るシェルの子プロセス、再開したセッションでの `--ui-server` の接続タイミングを直した。安定版は `v1.0.114` のままである（Master）
  - https://github.com/github/copilot-cli/releases
- [据え置き] **GitHub changelog と Windows Command Line ブログ** — `github.blog/changelog` は 11/20、Copilot ラベルは 11/18 のコネクタ追加、Windows Command Line ブログは 11/4 の Intelligent Terminal 0.3 から動いていない（Master・industry）

### Copilot Studio / Power Platform

- **Copilot Studio のエージェントのメモリ**（ハイライト2参照）
- [仕様] **外部モデルの選択ページ** — Microsoft が `authoring-select-external-response-model`（11/20 01:04Z `c64b09c2`）で、標準ハーネスのメーカーが Overview の Model 欄で Anthropic・Mistral・xAI のモデルを主モデルに選べることを明文化した。Mistral と xAI は Microsoft の外でホストされ、管理者が各社の条件に同意するまで使えない。preview / experimental のモデルは本番に使わないよう明記している（Copilot）
  - https://learn.microsoft.com/en-us/microsoft-copilot-studio/authoring-select-external-response-model
- [観測] **Learn 週次突合** — Copilot の Learn 週次突合で、目次3本は Copilot Studio 486・Microsoft Copilot 145・Cowork 39 リンク（11/16 は 478 / 140 / 29）となり、666ページすべてが 200 を返した。11/16 以降の改訂約250本は Ignite の既報の範囲か差分を特定できず、増えた20ページの内訳も前回のリンク一覧が無いため分からない（Copilot・B-082）
  - https://learn.microsoft.com/en-us/copilot/cowork/toc.json
- [据え置き] **Copilot Studio と Power Platform の一次** — Copilot Studio What's New（`1e58d09d`）、レート表、PPAC 容量管理、ガイダンスハブ、モデル表、非推奨一覧、Released Versions（2026.6.3）は前日から変わっておらず、ブログ RSS にも新しい記事は無い（Copilot）
  - https://learn.microsoft.com/en-us/microsoft-copilot-studio/whats-new

### Microsoft 365 Copilot

- [観測] **Roadmap の総項目数が9件減少** — Release Communications の API と RSS は 2,392 項目を返し、前日の 2,401 から9件減った。最終 `modified` は 11/21 02:55Z のままで新しいバッチは無く、Copilot Studio タグは33件で増減はない（Copilot）
  - https://www.microsoft.com/releasecommunications/api/v1/m365
- [据え置き] **Release Notes・Purview・Cowork・Partner Center・Message Center** — M365 Copilot Release Notes（先頭 November 17）、Purview・拡張機能・Cowork の What's New、Partner Center 11月ページは前日のまま変化がない。Message Center は 11/20 23:37Z の後に新しい通知が出ていない（Copilot）
  - https://learn.microsoft.com/en-us/microsoft-365/copilot/release-notes

### Google

- [新機能] **Gemini API のツール検索（Tool Retrieval）** — TLDR AI（11/20）によると、Google は登録した関数の中から入力に合うものを API が探して実行する機能を Gemini API に加えた。今日はじめて捕捉したが、Google の一次（`blog.google`・`aistudio.google.com`）には届かず、対象モデルと料金は確認できていない（industry）
  - https://blog.google/innovation-and-ai/technology/developers-tools/gemini-api-tool-retrieval/
- [観測] **Gemini API changelog に届かない** — Gemini API changelog は転送先 `aistudio.google.com` に届かないままで、WebSearch でも 10/27 より新しい項目を確かめられない。Workspace Updates（11/20）・Gemini アプリ（11/19）・`blog.google` AI RSS（11/19）は動いていない（Master・B-088）

### 開発ツール・エージェント

- [新機能] **Perplexity Monitor API** — The Decoder（11/22）によると、Perplexity が、検索を15分ごと〜週1回（または cron）で自動実行し、目的に合う変化だけを署名付き Webhook で送る API を公開した。ページ監視は1監視で最大10ページを対象にし、料金は Web 監視が成功1,000回あたり $1、ページ監視が取得1,000 URL あたり $1 である。他社比較の数字は Perplexity 社内のもので第三者の検証は無い（industry）
  - https://the-decoder.com/perplexitys-new-monitor-api-turns-web-search-from-a-one-off-query-into-a-nonstop-watchdog/
- [新機能] **Vercel eve 1.0 の一般提供** — TLDR AI（11/18）によると、Vercel がオープンソースのエージェント開発フレームワーク eve 1.0 を一般提供にした。モデル呼び出しとツール実行のループに加え、メモリー・承認・監視を受け持つ。`vercel.com` には届かず、ライセンスと対応モデルは未確認である（industry）
  - https://vercel.com/blog/eve-is-now-generally-available
- [動向] **職場を模した環境でのエージェント評価** — The Decoder（11/22）によると、同僚・プロジェクトボード・チャット履歴をそろえた架空のソフトウェア会社に置いた実験で、Claude Opus 5.5 も GPT-6 Astra も完了できたタスクは10件に1件未満だった。詳しい数値と実験名は有料部分にあり確認できていない（industry）
  - https://the-decoder.com/ai-coding-agents-ace-isolated-tests-but-complete-fewer-than-one-in-ten-tasks-in-a-simulated-workplace/
- [据え置き] **Cursor・Orca・Devin・xAI・TypeSafe AI・MCP・オープンウェイト** — Cursor の changelog（11/6）とフォーラム（10/12）、Orca（`v1.4.269`）、Devin（11/20）、xAI（11/19）、TypeSafe AI（9件）、MCP blog（11/11）、Obsidian（1.15.1）は動いていない。Hugging Face の8 org に新しいリポジトリは無い（Master）

### 市場・企業

- [据え置き] **Amazon × Decart、Nvidia × Inception、Nvidia × Reflection AI** — 3件の買収協議に続報はない。Decart は FT（11/21）の「合意に近づく」から動きがなく未成立のままで、Nvidia の後任 CEO も確認できなかった。MM総研・IDC Japan の新しい公表も無い（industry）

## 直近の注目予定

- **11/24 以降**: `claude-opus-4-5-20251101` の暫定退役日（確定日ではない・告知なし）
- **11月下旬**: Copilot ライセンスの無い利用者の検索画面が新しくなる（MC1562275）。Copilot Code のローカル Sandbox が既定でオンになる（MC1519871）
- **11月中**: GitHub の cloud sandbox の課金が始まる（日付は明記なし）
- **11/29**: OpenAI が Daybreak Blue のセッションデータの学習利用を始める（二次）
- **11/30**: `claude-sonnet-4-5-20250929` が退役し、Opus 4.8 の fast mode が削除される。OpenAI の `/v1/prompts`・Evals・Agent Builder が停止する。Power Automate デザイナーの Copilot と Copilot Studio の Mistral Medium 3.5 が退役する。GPT-5.6 Sol の期間限定価格と Gemini 4 Argon・Carbon の導入価格が終わる
- **12/1**: OpenAI `gpt-image-1-mini` / `gpt-image-1.5` / `chatgpt-image-latest` が停止する。Gemini 4 Argon・Carbon の単価が $4/$20 に倍増する。Copilot Studio のワークフローの Code ノードが GA になる
- **12/2**: GitHub が公開リポジトリの `pull_request_target` を既定でブロックする。Power Platform のプロンプトから Anthropic・Grok・旧 GPT 系が退役する（MC1536101）
- **12/3**: Agent ノードからのファイル生成が GA になる（MC1561859）
- **12月上旬**: Teams のチャネル単位の Copilot がパブリックプレビューに入る（MC1562277）
- **12/8**: GitHub が活動の無いリポジトリの Dependabot アラートを停止し、ARM32 ジョブのサポートを終える。Dataverse のエージェントユーザーが GA、M365 Copilot in Power BI が既定でオンになる
- **12/9**: EU / EFTA / UK で Claude モデルが既定で有効になる（MC1546438）
- **12/11**: OpenAI `gpt-5` 系 / `o3` / `o3-pro` が停止する。ChatGPT の Advanced / Standard 音声モードが退役する（二次）
- **12/14**: Copilot から Claude Fable 5 / Haiku 4.5 / Gemini 3.8 Flash / Gemini 4 Argon / Grok 4.6 / Kimi K3 が廃止される。claude.ai/design の単体サイトが閉鎖する
- **12/15**: アンマネージドの開発者環境の削除が始まる（MC1515303）
- **12月中旬**: Copilot デスクトップアプリと Edge の同期が展開される（MC1562269）。Chat と Office のモデルの従量課金が GA になる（MC1557754）
- **12/17**: Copilot Studio のワークフローのサービスプリンシパル認証が GA になる（MC1557509）
- **12/18**: Copilot から MAI-Code-1.1-Flash が廃止される
- **12/31**: Copilot の Fable 5 系の ZDR 例外が終わる。Claude Security の無償クレジットの対象期間が終わる
- **2027-01-03**: Copilot デスクトップアプリのアプリ内ブラウズの既定オンに備える期限（MC1560922）
- **2027-01-06**: OpenAI `tts-1` / `tts-1-hd` / `gpt-4o-mini-tts` が停止する
- **2027-01-11**: OpenAI の EU データレジデンシーで GPT-5.2 / 5.4 / 5.4 mini の `fast` / `priority` 処理が停止する
- **2027-01-14**: OpenAI `gpt-4o` / `gpt-4o-mini` / `gpt-4.1` / `gpt-4.1-mini` が停止する
- **2027-01-15**: アンマネージドの開発者環境が完全に削除される
- **2027-01-20**: OpenAI `gpt-realtime` / `gpt-audio` 系が停止する
- **2027-02-15**: Copilot Studio の Claude Opus 4.8・Opus 5・Sonnet 4.6・Sonnet 5 が退役する
- **2027-03-01**: GPT-6.2 Astra・Sol の Ultrafast が Standard の3倍から6倍になる

## 改善メモ

- Master: B-092（misalignment reports の URL を 308 の転送先に改める）を新規起票。`openai.com`・`help.openai.com` が週次復旧チェックで復旧した。継続提案 8件（最多: B-088 Gemini API changelog の URL 差し替え、20回目）
- Copilot: 新規提案・障害の変化なし。継続提案 5件（最多: B-080 Cowork の Learn URL の移設、25回目）。B-082 は週次突合で再確認（4回目）
- industry: `www.dragos.com`・`vercel.com`・`arstechnica.com` がゲートウェイ拒否（新規）。継続提案 7件（最多: B-040・B-048、21回目）
- ソース間の訂正: 前日（11-22）のサマリーは OpenAI Usage Policies の事前審査を二次情報で `[破壊的変更]` とし対象を広く書いたが、Master が本日一次で読んだ条文ではモデルアクセス仲介プラットフォームに限られる。前日分は書き換えていない
- ソース間の差: Opus 4.5 の暫定退役日について、Master は「告知が無いので明日退役しない」、industry は「下限日・告知なし」と書き、結論は一致している
</content>
</invoke>
