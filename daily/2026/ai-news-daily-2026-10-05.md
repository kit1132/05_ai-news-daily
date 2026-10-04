# AI News Daily Summary — 2026-10-05

週末明けで一次ソースの更新は少ない日である。Google は Gemini アプリの無料ユーザーを 10/9 から Gemini 3.5 Flash-Lite だけに絞ると報じられた。Anthropic は Claude Code `2.1.289` を `latest` に上げ、管理端末の deny / ask ルールが mod やシンボリックリンクに迂回されていた穴を塞いだ。Microsoft は M365 Copilot の従量課金（UBB）ドキュメント8本を改訂し、グループを移っても Copilot Credits の消費量がリセットされないと明記した。

## 今日のハイライト

### 1. [破壊的変更+料金] Google が Gemini アプリの無料ユーザーを 10/9 から Flash-Lite だけに絞ると報じられた — 無料枠で Flash / Pro を試せる前提が4日後に消える

**要点**: Google が Gemini アプリのモデル選択をプラン別に制限し、10/9 から無料ユーザーは Gemini 3.5 Flash-Lite 1モデルのみ、AI Plus も Pro を失うと複数媒体が報じた。回数ではなくモデルへのアクセス自体が切られるので、Pro を使う評価・検証は AI Pro 以上の契約が前提に変わる。

**詳細**:

- 無料: Gemini 3.5 Flash-Lite のみ。Gemini 3.6 Flash / Gemini 3.1 Pro へ切り替えられなくなる
- Google AI Plus（**$4.99/月**）: Flash-Lite と Flash は残り、Pro を失う。発効日はアカウントごとにメールで通知される
- Google AI Pro（$19.99/月）/ Ultra: 3モデルとも維持する。AI Pro には、これまで上位プラン限定だった Deep Think が付く
- 利用上限は5時間ごとにリセットされ、週次の上限もある。今月中に各モデルへ low / medium / high の effort 設定が入り、高い effort ほど枠を多く消費する
- 対象は個人の Gemini アカウント（Web・モバイル）で、Workspace・企業アカウントは報道上は対象外である。Gemini API（開発者向け）の changelog には載っていない
- 一次（Gemini アプリのリリースノート）は未読。登録 URL（`support.google.com/gemini/answer/13594961`）の本文は Privacy Hub でリリースノートではなかった

- https://www.newsbytesapp.com/news/science/google-limits-gemini-model-access-by-subscription-from-october-9/tldr
- https://aiweekly.co/alerts/google-caps-free-gemini-at-flash-lite-starting-october-9
- https://www.storyboard18.com/digital/google-gemini-model-access-changes-on-october-9-what-free-and-paid-users-need-to-know-111951.htm
- https://xenospectrum.com/en/gemini-october-model-access-limits/

### 2. [セキュリティ+新機能] Anthropic が Claude Code `2.1.289` を npm の `latest` に上げた — 管理端末の deny / ask ルールが mod・プラグイン・シンボリックリンクに迂回されていた穴を塞いだ

**要点**: Anthropic が 10/3 に `2.1.289` を公開し `latest` へ昇格させた。組織が置いた権限ルールや MCP の表示が、ユーザー導入の mod・プラグインやシンボリックリンク経由のファイル参照で迂回・改変され得た不具合を直したので、組織ポリシーの効き目はこの版以降が前提になる。

**詳細**:

- 権限まわりの修正:
  - 管理端末で、複合シェルコマンドの入れ子部分に掛けた deny / ask ルールが、ユーザー導入 mod の承認に負けていた
  - サンドボックスの自動許可下で、値を展開する環境変数プレフィックス付きコマンド（例: `TZ="$HOME" rm -rf build`）や直前に変数代入があるコマンドに deny / ask ルールが効いていなかった
  - IDE からシンボリックリンク経由で @ 参照・選択したファイルに `Read` の deny ルールが掛かっていなかった
  - ユーザー導入のプラグインが、組織管理の MCP サーバーのサインイン用ツールの説明文を書き換えられた
- そのほかの修正: 閉じていない `<script>` タグを含む短いコードブロックや深く入れ子の `${` でターミナルが固まる問題
- 追加: チームメイト向けの `agent.spawn`、プラグインのフックイベントをまたいだ単一のエージェント ID、`$.agent.list()` の idle / waiting 状態
- [VSCode] 2.1.288 の `claude auth status` の変更を差し戻した（サインアウトが増えた可能性があるため）
- dist-tags は `{stable: 2.1.285, latest: 2.1.289, next: 2.1.289}`（publish 10/3 20:12 UTC）

- https://code.claude.com/docs/en/changelog
- https://www.npmjs.com/package/@anthropic-ai/claude-code

### 3. [仕様] Entra ID グループを移っても Copilot Credits の消費量はリセットされない — 上限はポリシー単位ではなく課金期間内の利用者単位で効く

**要点**: Microsoft が UBB の支出ポリシー解説を 10/2 に改訂し、課金期間中に利用者が別グループへ移ると移動先のポリシーが効く一方、それまでの消費量は新しい上限の判定に算入されると明記した。部署異動で上限を取り直す運用はできない前提に変わる。

**詳細**: `usage-based-billing-manage-copilot-credits`（`ms.date` 2026-10-01・`updated_at` 10/2 17:48Z）に「Users who move between Microsoft Entra ID groups」節が加わった。ポリシー A で 500 クレジットを使った利用者がポリシー B のグループへ移ると、500 を算入したまま B の上限まで使える、という例示である。同じコミットで UBB 系8ページが改訂され、ほかに次の2点が読める。

- 上限超過中のタスク: 実行中のタスクが利用者単位の上限を超えても中断されずに完了する。超過分はポリシーの上限に数えず、課金せず（Microsoft の裁量）、Cost Management のダッシュボードにも出ない
- 表示との食い違い: 監視ページの Consumption タブの説明は「移動前の消費は利用者単位では追跡されず、現在のポリシーに対する使用量だけを表示する」としている。管理画面の数字と上限判定の数字が一致しない可能性がある

- https://learn.microsoft.com/en-us/microsoft-365/copilot/usage-based-billing-manage-copilot-credits
- https://learn.microsoft.com/en-us/microsoft-365/copilot/usage-based-billing-copilot-credits-monitor-spending

## カテゴリ別まとめ

### Claude / Anthropic

- **Claude Code 2.1.289**（ハイライト参照・2）
- [据え置き] **API release notes・製品側の定点** — Anthropic の API release notes は 9/30 の Sonnet 4.5 退役告知が最上位のままで、`claude-haiku-4-5-20251001` の退役告知は出ていない。`anthropic.com/news` は 10/2、`claude.com/blog` は 10/1、`support.claude.com` は 9/28、`status.claude.com` は 10/1 が最上位のままである。

### OpenAI / Codex / ChatGPT

- [予定] **GPT-Rosalind の課金開始（本日 10/5）** — OpenAI が API 料金表で、承認済みの生命科学研究向けモデル GPT-Rosalind の課金を本日 10/5 に始めると示している。単価は入力 $5・キャッシュ入力 $0.50・出力 $25（/1M トークン）である。https://developers.openai.com/api/docs/changelog
- [版更新] **Codex pre-release** — OpenAI が Codex の pre-release を `rust-v0.162.0-alpha.13`（10/4）まで進めた。安定版は `rust-v0.160.0`（10/1）のままである。https://github.com/openai/codex/releases
- [据え置き] **API changelog・退役ページ・Community** — OpenAI の API changelog は 9/29、退役ページは 10/1 の2件、community Announcements は 9/30、`learn.chatgpt.com` の changelog は 10/1 が最上位のままである。

### Google

- **Gemini アプリ無料枠の Flash-Lite 限定**（ハイライト参照・1）
- [新機能] **DiarizationLM-Gemma-4-E4B-v1** — Google が話者分離（diarization）向けのモデル `google/DiarizationLM-Gemma-4-E4B-v1` を Hugging Face で公開した（10/4 作成）。非公開・ゲートなしの Apache-2.0 で、safetensors 約8.0B パラメータに加え q4_0 / q4_k_m の GGUF を同梱している。https://huggingface.co/google/DiarizationLM-Gemma-4-E4B-v1
- [据え置き] **Gemini API changelog** — Gemini API の changelog は 9/22 が最上位のままで、Gemini 4 Argon（9/30 報道）はまだ載っていない。

### GitHub Copilot / GitHub

- [据え置き] **Copilot changelog・CLI** — GitHub の changelog は 10/2 の Copilot code review API 対応が最上位のままで、10/3〜10/5 の掲載は無い。Copilot CLI も安定版 `v1.0.91`、pre-release `v1.0.92-3` から進んでいない。

### Microsoft 365 Copilot / Copilot Studio / Power Platform

- **Copilot Credits の消費量はグループ移動で引き継がれる**（ハイライト参照・3）
- [仕様] **Cowork プラグイン開発ガイドの `wiqd` 化** — Microsoft が `cowork/cowork-plugin-development` を 10/2 に改訂し、Work IQ Developer Tools の `wiqd` CLI を主経路に構成し直した。9/30 に告知された `wiqd`（既報）の具体的な挙動が Learn に載った。
  - マニフェスト版: `wiqd plugin create` は `manifestVersion` 1.29 で固定する。1.29 ではコネクタが URL だけで済み、`mcpToolDescription` が必須でなくなる（手書き例の 1.28 では必須）
  - 取り込みの制約: `wiqd plugin import` で取り込んだプロジェクトは検証・表示しかできず、パッケージ化・プロビジョニング・共有ができない。すぐ公開したい場合は従来の `atk import openplugin` を使う
  - 書き出し: `wiqd plugin export --format claude-plugin` / `cursor-plugin` で他の Agent Skills ホスト向けに書き出せる
  - https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-plugin-development
- [仕様] **Copilot Studio のプロンプト実行上限** — Microsoft が標準ハーネスのプロンプト解説 `prompts-performance-execution`（`ms.date` 10/2）で、プロンプトの実行は **100秒**で打ち切られると明記した。大きなツール出力は自動では縮約されないため、モデルのコンテキストを超えないよう返す前に前処理するよう求めている。https://learn.microsoft.com/en-us/microsoft-copilot-studio/prompts-performance-execution
- [仕様] **Copilot Credits の容量画面** — 管理者が PPAC の容量画面で見ると、Copilot Studio でアプリを作るとき（プレビュー）に消費したクレジットは当面 Top Agents の欄にまとめて表示され、エージェント一覧では Billable features の「App」に分類される（`ms.date` 10/2）。https://learn.microsoft.com/en-us/power-platform/admin/manage-copilot-studio-copilot-credits-capacity
- [仕様] **PPAC の Agentic Support FAQ** — Microsoft が、管理者・作成者が PPAC で Get support を選ぶと開く AI サポートエージェントの FAQ を公開した（`ms.date` 10/1）。参照するのは Learn・既知の問題・テナントのサービス正常性などの読み取り専用ソースだけで、課金・返金・ライセンス例外は判断しないと明記している。https://learn.microsoft.com/en-us/power-platform/admin/agentic-support-faq
- [観測] **GitHub Copilot ハーネスのモデル表** — Microsoft が `agents-experience/authoring-agent-model-availability` を 10/3 に改訂したが、掲載モデルは 9/20 時点と同じ11種で改訂差分は特定できていない。9/30 に M365 Copilot へ追加された GPT-6.1 Sol と Claude Sonnet 5.5 はこの表に載っていない。https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-experience/authoring-agent-model-availability
- [据え置き] **Release Notes・Roadmap・What's New・Power Platform の定点** — M365 Copilot Release Notes の先頭は September 23, 2026 のままで、Roadmap も 10/2 22:01Z のバッチ以降は新規が無い（総数 1,892）。Copilot Studio What's New は July 2026 節のまま GitHub Copilot ハーネスの GA（8/3）を63日反映しておらず、Copilot Studio の最新ビルドも 2026.6.3 のまま96日である。

### Cursor / xAI / その他エージェント

- [据え置き] **Cursor・xAI・Devin・MCP・Apple** — Cursor の changelog は 9/23、フォーラム Announcements は 9/21 が最上位のままである。xAI・Devin に日付つきの新規は無く、`blog.modelcontextprotocol.io` は 8/22、`developer.apple.com/news/` は 10/2 が最上位で、Hugging Face の登録 org も Google 以外は新規リポジトリが無い。

### 業界・政策

- [動向] **ThinkingBox** — Microsoft が Hugging Face と、エージェント実行後の業務レコードが正しい状態にあるかを採点するベンチマーク ThinkingBox を公開した（10/3）。小売・旅行・保険など507の業務ワークフローを各20回走らせる設計で、Kimi-K3 は476件を1回以上解けたが20回すべて成功したのは68件、Claude Opus 5.5 は241件で20回すべて成功した。失敗の77.5%はツール層で起きている（数値は二次情報）。https://runtimewire.com/article/microsoft-thinkingbox-agent-stateful-workflow-benchmark
- [動向] **Super Intelligence Force** — トランプ大統領が、AI で米国の主導を保つための連邦政府の調整組織を新設した（10/4）。Jay Clayton 国家情報長官・Andrew Ferguson FTC 委員長・Emil Michael 国防次官・Scott Kupor 人事管理局長の4人を率いる役に指名し、大統領と首席補佐官に直属させるが、法的権限・予算はまだ無い。https://www.cnn.com/2026/10/04/politics/trump-ai-task-force-jay-clayton
- [据え置き] **市場データ** — IDC Japan・MM総研・NRC・Similarweb はいずれも新規公表が無く、Similarweb の9月分トラッカーも未検知である。

## 直近の注目予定

- **10/5**: Gemini の `antigravity-preview-05-2026` が停止 ／ Workspace で skills の展開開始（Rapid Release） ／ GPT-Rosalind の課金開始 ／ Anthropic Wellbeing Research Grants の選考結果通知
- **10/7**: GHE.com が X25519 単独の TLS 接続を拒否
- **10/9**: Gemini アプリの無料ユーザーが Flash-Lite のみ、AI Plus が Pro を失う（報道）
- **10/13**: Gemini アプリで skills の展開開始 ／ Office / Project / Visio LTSC 2021 のサポート終了 ／ 新しい Copilot の Partner Digital Airlift
- **10/14**: GitHub SSH の新規 RSA 鍵が 3072 ビット以上必須に ／ GPT-5.5 が ChatGPT / Codex から退役 ／ Anthropic の pre-IPO investor day（報道）
- **10/15 以降**: `claude-haiku-4-5-20251001` の暫定退役日（告知はまだ無い）
- **10月**: Copilot Chat の UBB モデル選択 GA（571400） ／ SharePoint の画像生成・Advanced Autofill・サイト分析が Copilot Credits の消費対象に ／ Copilot Studio エージェントがコスト管理の対象に ／ スキルカタログ GA（571880） ／ 自己学習 GA（570432） ／ Copilot UX components GA（SPFx 1.24） ／ Teams 通話委任の Preview（565216） ／ Gemini アプリの effort 設定（報道）
- **10/19**: GitHub Copilot が5モデルを廃止 ／ Workspace の skills 展開開始（Scheduled Release）
- **10/21**: GitHub Copilot の新機能既定ポリシーの設定期限（10/22 発効）
- **10/23**: OpenAI のレガシースナップショット12件が停止
- **10/27〜29**: PPCC 2026（ラスベガス）
- **10/29**: ChatGPT Pro 200 の現行枠の最終日（二次）
- **10/30**: ChatGPT Pro 200 の Work / Codex 利用枠が半減（二次）
- **10/31**: MCP サーバー認定の旧申請経路が終了 ／ OpenAI Evals が読み取り専用化
- **11月**: 永続的なエージェント ID GA（570430） ／ Maker guidelines GA（570967） ／ Teams 通話委任 GA（565216） ／ Purview 自動ラベル付け上限の引き上げ（571309） ／ Work IQ 拡張2件の GA ／ 政府クラウドの Outlook 対話型下書き GA（573280） ／ Edge の Commercial Journeys Preview（561040）
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
- **12/31**: 非営利向け M365 Copilot の併用プロモーション終了 ／ Gemini 3.8 Flash の導入価格が終了 ／ Pro 200 既存契約者の $2,500 クレジットが失効（二次） ／ MAI-Transcribe-2-Streaming の導入価格が終了（二次）
- **2027-01**: Edge の Commercial Journeys GA（561040）
- **2027-01-06**: OpenAI `tts-1` / `tts-1-hd` / `gpt-4o-mini-tts` 2版が停止
- **2027-03-01 以降**: Gems 廃止（Business / Enterprise）
- **2027-04-01**: OpenAI `gpt-5.1` / `gpt-5.3-codex` / `gpt-5.4-nano` が停止
- **2027-06-01 以降**: Gems 廃止（Education）

## 改善メモ

- 新規提案: Master が B-083（Gemini App Release Notes の登録 URL が Privacy Hub を返すため差し替え）を起票した。Copilot・industry は無し
- 継続提案: Master は B-035 npm dist-tags を再確認（50回目）／ Copilot は B-074（docset 全件突合を3日ぶりに実施し、10/2〜10/3 の改訂を2〜3日遅れで検知）・B-076（モデル表の改訂差分が特定できない）・B-037（96日）を更新 ／ industry は3件を更新（最多 B-004・97回目）。B-008・B-029 に Gemini アプリ利用枠変更の捕捉遅れ（2〜3日）を追記
- 障害の変化: Master の週次復旧チェックは復旧0件。industry が `aiweekly.co` / `llm-stats.com` / `tech-insider.org` / `www.digitaltrends.com` / `www.androidheadlines.com` を新規ゲートウェイ拒否として記録した。Copilot は無し
- ソース間の差分・矛盾:
  - Gemini アプリの利用枠変更は Master と industry の両方がハイライト1にしていた。タグは Master が [破壊的変更+料金]、industry が [料金] で割れたため、モデルへのアクセス自体が切られる点を主に取り Master に揃えた。報道日は Master が 10/3〜10/4、industry が 10/2〜10/3 と書いており、industry はサポートページ「Changes to Gemini model access and limits」での告知としているが、Master は一次未読としている
  - Claude Code `2.1.289` は Master と industry の両方がハイライトにしていた。権限修正は Master が4件、industry が2件（ターミナルが固まる問題の修正は industry のみ）を挙げており、両方を統合した。タグは Master の [セキュリティ+新機能]（industry は [セキュリティ]）
  - GitHub changelog の据え置きは Master と industry の記載を1件に統合した
  - industry が開発ツール節に載せた IBM Bob のセルフホスト対応は、本サマリーが 10/4 に収録済みのため再掲しなかった
