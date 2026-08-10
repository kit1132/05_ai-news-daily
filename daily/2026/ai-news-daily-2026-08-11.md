# AI News Daily Summary — 2026-08-11

火曜は「誰に何を配るか」の線引きが同時に動いた。OpenAI は拒否を意図的に減らしたサイバー特化モデルを審査付きで防御側にだけ配り始め、3日前には自社の未公開モデルの開発を止めている。AWS は逆に、2023年から提供してきた Bedrock Agents を 7/30 付で新規顧客に閉じ、カタログごと凍結していた。Meta は 30B のエージェントモデルを Apache 2.0 で全員に開いた。手元のツールでは Copilot CLI が安定版で設定キーを2組リネームし、旧キーを移行なしで黙って無視するようになっている。Microsoft 側は Copilot Studio のビルドが4回連続の空振りに終わった一方、これまで所在不明としてきたクレジット消費レートの一次ページが見つかり、本サマリーが 08-09・08-10 に書いた記述を訂正することになった。

## 今日のハイライト

### 1. OpenAI が「拒否を減らしたモデル」を審査付きで配り始めた — 同じ週に止める側と配る側の両方を実行した

**要点**: OpenAI が拒否を意図的に減らした **GPT-5.6-Cyber** を、審査を通した防御側にだけ配り始めた。exploit chain 開発は「モデルが断るもの」から「審査を通れば使えるもの」へ変わる。9/1 から Daybreak 全アカウントでハードウェアキーが必須になる。

**詳細**: 8/10 に Daybreak を2層へ分割した。

- Daybreak Blue: GPT-5.6 Sol を含む汎用フロンティアモデルを、承認済みの防御担当者へ日常的なセキュリティ業務向けに開放する
- Daybreak Red: GPT-5.6-Cyber を、認可された脆弱性研究・exploit 検証・セキュリティテスト向けに、より厳しい審査を通した相手にだけ開放する
- 両層とも身元確認・アカウント保護・監視・法的宣誓を必須とし、9/1 からハードウェアセキュリティキーが全アカウント必須になる

GPT-5.6-Cyber は GPT-5.6 Sol を基盤に、ゼロデイ発見と exploit chain 構築の性能を上げ、dual-use 領域の拒否を減らすよう訓練されている。社内テストでは高度なセキュリティ要求の **95%** に応答し、対象には exploit chain 開発・認証バイパス・権限昇格が含まれる。実績として Chrome の JS エンジン V8 で未知の脆弱性2件を発見し、連鎖させるとメモリ破壊と V8 heap sandbox のバイパスが可能だった。Google が協調開示を経て修正し `CVE-2026-15903` を割り当てている。Preparedness Framework では GPT-5.6 Sol・GPT-5.6-Cyber とも cybersecurity を High と評価し、Critical 閾値には達していないとした。

3日前の 8/7 には、未公開モデル Astra について cybersecurity 能力が Critical である可能性を排除できないとして、OpenAI が開発の一部を停止している。安全要件を満たさない社内テストは即時中止し、政府機関と選定した安全性組織との追加試験を準備するとした。フロンティアラボがサイバー能力を理由に自社モデルの進行を公に減速した初の事例にあたる。

⚠️ 一次 `openai.com/index/expanding-daybreak-as-the-cyber-defense-window-narrows/` はオリジン403で未読のため、数値は公式フォーラム告知と二次報道の一致で採っている。

- https://community.openai.com/c/announcements/6
- https://openai.com/index/expanding-daybreak-as-the-cyber-defense-window-narrows/ （一次・403で未読）
- https://help.openai.com/en/articles/20001258-openai-daybreak-trusted-access-for-cyber-overview
- https://www.axios.com/2026/08/10/openai-gpt-astra-restrictions-safety-hacking-defenders
- https://techcrunch.com/2026/08/07/openai-says-it-slowed-astra-model-development-over-security-concerns/

### 2. Copilot CLI v1.0.79 が安定版になり、設定キー2組が移行なしでリネームされた — dev ツールの絞り込みが黙って外れる

**要点**: GitHub が Copilot CLI v1.0.79 を安定版として公開し、設定キーを2組リネームした。旧キーは移行なしで黙って無視されるため、`allowDevToolCaches: false` で dev ツールアクセスを絞っていた環境は、更新すると既定の on に戻る。

**詳細**: 公開は 8/10 16:19 UTC で、安定版としては 1.0.78（8/3）以来1週間ぶりにあたる。破壊的変更は2件ある。

- `allowDevToolCaches` → `allowDevToolAccess`: キャッシュだけでなく dev ツールの設定とレジストリまで許可する意味に拡張された。旧キーは黙って無視され、既存の `false` オプトアウトは既定（on）へ戻る。settings.json と MDM ポリシーの両方を更新する必要がある
- `sandbox.gitAuth` / `sandbox.ghAuth` → `sandbox.auth.git` / `sandbox.auth.gh`: 1.0.79-8 で先行していた変更が安定版に入った。後方互換はなく、旧キーは SDK リクエストで invalid として拒否される

機能面では、モデルピッカーが Recent / Recommended / New 等にグループ化され Shift+Tab で移動できるようになり、選択肢に kimi-k3 が加わった。大規模モノレポの正規表現検索は ripgrep から tgrep に替わり、`/model` は既定でセッションスコープになった（将来のセッション既定は `/config model` で指定する）。Sessions タブとサイドバーから複数セッションを同時に管理でき、`--plan` と `--mode autopilot` を併用すると承認待ちなしで計画から実装まで進む。サンドボックス側は Windows Dev Drive での実行に対応し、macOS の UNIX ドメインソケット（tsx / vite / esbuild 等）が復活し、Azure DevOps / GitHub Enterprise / GitLab への HTTPS 認証つき git も通るようになった。

- https://github.com/github/copilot-cli/releases/tag/v1.0.79
- https://github.com/github/copilot-cli/releases

### 3. AWS が Bedrock Agents を Classic 化していた — 7/30 で新規受付が終わりカタログも凍結された

**要点**: Amazon Bedrock Agents が Classic へ改称され、7/30 から新規顧客に開かれなくなった。モデルカタログも同日時点で凍結され、以降に出る新モデルは AgentCore 経由でしか使えない。AWS 上のエージェント構成は AgentCore 前提へ引き直すことになる。

**詳細**: 2023年11月提供の Amazon Bedrock Agents が **Amazon Bedrock Agents Classic** へ改称され、2026年7月30日から新規顧客に開放されなくなった。同日以降は maintenance mode に入り、Classic で選べるモデルカタログは同日時点の内容で固定される。既存の Bedrock モデル・Knowledge Bases・Guardrails は影響を受けず、許可済みアカウントは従来どおり利用できる。提供終了日は未告知で、AWS は Classic のワークロードを Amazon Bedrock AgentCore へ移行するよう推奨している。

⚠️ 一次ドキュメント（`docs.aws.amazon.com`）はゲートウェイ拒否で本文を取得できず、内容は二次まとめと検索スニペットの突き合わせによる。7/30 の変更を12日遅れで捕捉した。

- https://docs.aws.amazon.com/bedrock/latest/userguide/agents-classic-maintenance-mode.html （一次・ゲートウェイ拒否で未読）
- https://www.westloop.io/post/amazon-bedrock-agents-classic-availability-change-amazon-bedrock-agents-launched-november-2023-is-now-amazon-bedrock-agents-classic-and-will-no-longer-be-open-to-new-customers-starting-on-july-30-2026-if-you-would-like-to-use-bedrock-agents-classic-sign-up
- https://servergurus.com/blog/aws-bedrock-agentcore-2026

## カテゴリ別まとめ

### Anthropic / Claude

- Claude Code は **v2.1.226**（8/8 02:48 UTC）が最新のままで、8/9・8/10 の新版はない。`code.claude.com/docs/en/changelog`・`raw.githubusercontent.com` の CHANGELOG.md・`github.com/anthropics/claude-code/releases` の3ソースで最上位が一致した
- Claude API の release notes は 8/7 が最上位のままで、8/8〜8/10 の追加はない。既報の4件は Managed Agents のセッション予算 / advisor / `inference_geo` / GitHub リポジトリからの skill 読み込みである
- Claude Code の既定権限モードは 8/14 に auto mode へ切り替わる（Pro / Max / Team）。残り3日で、管理は managed settings の `defaultMode` / `disableAutoMode`、分類器設定は `autoMode` の `environment` / `allow` / `soft_deny` / `hard_deny` で行う
- Claude for Government の「1機関 $1・シート無制限」プログラムが8月末で終了する（本日初検出）。FedRAMP High 環境で提供され、認可は Palantir Federal Cloud Service 経由・監査は Schellman Compliance が担う。商用テナントとは論理的に分離され、環境によってはアプリ層で分類バナーを表示する。会話とアップロード内容は既定でモデル訓練に使われない。通常は年次・シート単位のライセンスで、調達は Anthropic 直販か Carahsoft の GSA 承認ビークル経由になる。⚠️ サポート記事に開始日の記載がなく、プログラム開始日は特定できていない
- Claude の利用枠は期限が2つ走っている。週次上限50%増は 8/19 まで、Sonnet 5 の促進価格 $2/$10 は 8/31 に終了して $3/$15 へ戻る
- `claude.com/blog` は 8/7 の auto mode 2件が最上位のままで、`support.claude.com` の Release Notes も 8/6 の skill / plugin セキュリティスキャン beta から動いていない。Anthropic 側の新規発表はない
- https://code.claude.com/docs/en/changelog

### OpenAI / Codex / ChatGPT

- OpenAI が GPT-5.6-Cyber と Daybreak Blue / Red を公開し、未公開モデル Astra の開発の一部を停止していた（ハイライト1参照）
- OpenAI が ChatGPT Business に **Premium シート**を追加した（8/10）。Premium は月 $125/ユーザー（年契約は月 $100）で、標準シートの月 $25（年契約 $20）に対して5倍の利用量を与え、5時間の利用上限を撤廃する。同一ワークスペース内で標準と Premium を混在させ、人ごとに割り当てられるため、法人の座席試算は全員同一単価から利用量による2階層へ移る。先着 10,000 社を対象に Premium シート1席あたり $100 分（2,500 クレジット）のワークスペースクレジットを最大5席まで付与する販促があり、受付は 8/20 までである。エンタープライズ ARR は 2025年末の約 $2.4B から 2026年半ばに $5B 超へ伸びており、報道は本件を IPO 準備下の収益積み上げの文脈に置いている
- GPT-5.4 と GPT-5.4 mini は 8/31 に Codex（ChatGPT ログイン）から外れる。移行先は `gpt-5.4` → `gpt-5.6-terra`、`gpt-5.4-mini` → `gpt-5.6-luna` で、保存済み設定・カスタムエージェント・スケジュール済みタスクの書き換えが要る。API キー認証の Codex セッションと OpenAI API 側は対象外で従来どおり使えるため、認証方式を社内で混在させている場合は棚卸しが必要になる
- Codex CLI は安定版 0.147.0（8/7 01:41 UTC）が据え置きで、pre-release が 0.148.0-alpha.6（8/10 10:17 UTC）へ進んだ。0.148.0 の安定版はまだ出ていない
- `developers.openai.com/changelog` に 8/6 と 8/7 の2件が入っていた（前回チェックでは 8/5 が最上位と記録しており、取りこぼしにあたる）。8/6 は `chat-latest` スナップショットが最新の ChatGPT モデルを指すよう更新された件、8/7 は GPT-5.6 Cyber と Daybreak 向けモデルのリリースである
- OpenAI が Apple の営業秘密訴訟に対して 8/5 に31ページの却下申立を連邦地裁へ提出した。Apple が営業秘密と主張する情報を十分に特定できておらず、保護対象の営業秘密の所有も被告による不正取得も立証できていないと主張し、あわせて Apple 自身が業務端末上の従業員の個人 iMessage を閲覧していた点と、業務に個人 iCloud アカウントを使うよう指示していた点を反論材料に挙げている。Apple は 8/4 に使用差止の仮処分を申し立てており、審尋は 10/1 に設定されている
- OpenAI が 6/8 に SEC へ提出した S-1 ドラフトは非公開のままで、公開目論見書は本日時点でも EDGAR に現れていない。慣行ではロードショーの約15日前に公開されるため、報道は8月中旬〜下旬の掲載を見込んでいる。⚠️ 収益の水準は報道系統によって幅があり（月次売上約 $2B・年換算ランレート $25B 超）、引用する際は計測期間を明示する必要がある
- 既報の期限は据え置きで、公式 DALL·E GPT が 8/30、o3 と Assistants API が 8/26 に退役する
- https://openai.com/index/premium-seats-chatgpt-business/ ／ https://learn.chatgpt.com/docs/changelog

### GitHub Copilot

- GitHub が Copilot CLI v1.0.79 を安定版として公開した（ハイライト2参照）
- GitHub が Copilot on web の会話コントロールを 8/10 に GA にした。会話中に画面を最小化して GitHub を見て回り、専用メニューから直近の会話へ戻れるようになり、あわせてトークン支出インジケーターがセッション単位とメッセージ単位のクォータを表示する。対象は全 Copilot サブスクリプション階層で、提供は `github.com/copilot` である。08-09 収録の impact dashboard の ROI 節が管理者向けの費用可視化だったのに対し、こちらは利用者本人が消費量を見る側の手当てにあたる
- GitHub が 8/7 付で、Code Quality が Copilot を自動的にレビュアーとして追加する挙動を廃止した（Changelog の分類は Retired）。同日には Copilot code review の効力段階 Lite / Balanced が GA になっており、レビュー起動を自動付与から明示指定へ寄せる方向で揃っている
- `github.blog/changelog` は 8/10 の会話コントロール1件が新規で、8/8・8/9 の追加はない
- 既報の期限は3つとも動いていない。GitHub Spark の既存ユーザーアクセス終了が 8/31、既定モデル有効化ポリシーの発効が 8/26、全体験でのモデル廃止が 9/1 である
- https://github.blog/changelog/2026-08-10-copilot-on-web-expands-conversation-controls/

### Microsoft 365 Copilot / Copilot Studio

- Copilot Studio のクレジット消費レート表を一次で確認した。同じ処理でもモデル階層を変えるだけで消費が **100倍**変わるため、金額を伴わない試算はこのページだけで組める。対象は `microsoft-copilot-studio/requirements-messages-management`（`ms.date` 2026-08-03 / `updated_at` 2026-08-03T14:59Z）で、8/3 に更新された課金ドキュメント群と同じバッチにあたる
  - 機能別レート（1操作あたり）: クラシック回答 1 / 生成回答 2 / エージェントアクション 5 / テナントグラフグラウンディング 10 / エージェントフローアクション 13（100アクションあたり）/ コンテンツ処理ツール 8（1ページあたり）
  - 生成 AI ツールの階層別レート: basic 1・standard 15・premium 100 クレジット（いずれも10応答あたり）。トークン建てでは1Kトークンあたり basic 0.1 / standard 1.5 / premium 10 クレジットで、比率は同じである
  - 推論モデルは二重課金になる: 推論可能なモデルを使うと、操作の feature rate に加えて text and generative AI tools（premium）が1,000トークンあたり10クレジットで別途課金される
  - M365 Copilot ライセンスユーザーの社内向け利用は No charge だが、Computer-Using Agents（CUA）は対象外である。エージェントフローも「When an agent calls the flow」トリガーで起動した実行に限られ、他のトリガーは通常レートで課金される
  - 枯渇時の挙動は2系統に分かれる: カスタムエージェントは前払い容量の125%でエンフォースメントが働き無効化されるのに対し、エージェントフローは容量を使い切った時点で新規実行だけがブロックされ、エージェント自体はクラシック回答・生成回答・エージェントアクションで動き続ける
  - 音声はティア別に分かれ、クラシック音声10 / GenAI 音声35 / プレミアム GenAI 音声75 クレジット（いずれも1分あたり）で、コアのエージェント動作を含む
  - ⚠️ 本サマリーが 08-09・08-10 に「Copilot Credits の単価は Learn 側に一切載っていない」と書いた点を訂正する。Learn に無いのは1クレジットあたりの USD 価格で、これは今も Licensing Guide の PDF（403 で取得不可）にしかない。消費レートそのものは上記のとおり Learn に載っている
- Copilot Studio の Released Versions は定例更新日（火曜）の本日も新ビルドが出ず、最新は 2026.6.3（6/30 初出）のままだった。空振りは4回連続で、6/30 以降6週間にわたって新ビルドが出ていないことになる。リージョン分布と UX 版 26.06.21-24 にも変化はない
- Copilot Studio の What's New は節構成が June 2026 のままで、7月節も8月節も追加されていない。GitHub Copilot ハーネスは 8/3 に GA しているのに `(Production-ready preview)` の表記が残ったままで、未反映が8日連続になった
- M365 Copilot の Release Notes は先頭が July 29, 2026 バッチのままで、8/10 から変化がない。節構成5本（Microsoft 365 Copilot / OneNote / Copilot Chat / 拡張性 / SharePoint）・全10項目が一致することを確認した。次バッチは隔週傾向どおりなら8月中旬見込みである
- 拡張機能の What's New は「July 2026」節が最新のままで、8月節は作成されていない（`ms.date` 7/15 / `updated_at` 7/29）。掲載2件（宣言型エージェント manifest 1.8、Copilot 利用状況レポート API 3種への `version` パラメーター追加）にも変化はない
- 二次メディアの「8月の大型アップデート」は4例目の空振りになった。英語圏の記事と動画が挙げ続ける Word の変更履歴リライトと Cowork のイベントスケジューリングは July 29 バッチにどちらも収録されておらず、前者は 2026-04-16・04-27 に掲載済みの既報である
- Microsoft 365 Roadmap は 7/9 の GPT-5.6 告知が Latest announcements の最新のままで、Tech Community も 8/5 の ICYMI 記事、Microsoft 365 Blog 本体も 7/30 の記事から動いていない。M365 Developer Blog は 8/6 の Work IQ Developer Tools プレビューが最新である
- https://learn.microsoft.com/en-us/microsoft-copilot-studio/requirements-messages-management ／ https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-experience/billing-credit-overview

### Power Platform / ライセンス

- 非推奨一覧の週次確認を本日実施したが、新規の非推奨項目は追加されておらず、先頭は Power Automate モバイルアプリの廃止（2026-08-31 発効）のままだった。廃止までの残りは20日で、アプリはストアから削除され、プッシュ通知とホーム画面ウィジェットが機能しなくなる。既存のクラウドフロー自体は通常どおり動く
  - ⚠️ Fluent UI (v8) コントロールの非推奨は本日も本ページに記載がない。機能個別ページ2本が「deprecated」と明記しているのに一覧側へ反映されない状態が続いており、本ページを網羅的な破壊的変更の一覧として使えないことが改めて裏づけられた
- Release Wave（全体版）は緑チェックの追加・期日の変更・行の削除がいずれも発生せず、期日超過は延べ **12行**のまま3日連続で完全に同一だった（`ms.date` 8/4 / `updated_at` 8/7 20:59Z も据え置き）
  - GA 列が当月より前の月表記のまま: 7件（統合 Power Apps によるフォーム UI / マシン・フロー稼働率のダッシュボード / ワークキュー項目の CSV エクスポート / code apps のコネクタ CLI 対応 / FetchXML エディターでのオフラインプロファイル構成 / カスタムブランドアプリのプッシュ通知〔Jun〕/ デスクトップ版の以前のプロンプト参照〔May〕）
  - Public preview 列が当月より前の月表記のまま: 6件（デスクトップフローの直接スケジュール実行 / フローチャート表示 / 現行 Python 実行 / PowerPoint 操作の4件が Jul、ローカル AI モデル接続と code apps のコネクタ CLI 対応が Jun）。GA 列と重複するのは code apps のコネクタ CLI 対応の1件のみである
  - 8月に期日がある7件（ライセンスダッシュボード改善〔GA〕/ デスクトップフローのカスタムダッシュボードタイル〔Preview〕/ Process Intelligence Studio〔Preview〕/ Fabric セマンティックモデルへのエクスポート〔GA〕/ 正規化スキーマインポート〔GA〕/ Dataverse オンラインモード〔Preview〕/ ヘッダーとナビゲーションの刷新〔GA〕）はいずれも未達である。2026 Wave 1 の対象期間は9月までで残り約1か月半になる
- Power Platform Blog の月次記事は 8/6 の July/August 2026 合併号が最新のままで、前月号・当月号・合併号の3通りで照合しても新規はなかった。Power Automate Blog / Power Apps Blog も子カテゴリページ上の最新が 4/8 と 5/13 のままで、これは不完全レンダリングによる。GA の検知は引き続き Release Wave の緑チェックに依存する
- Partner Center の8月アナウンスは 8/7 付の7件目「Invoice generation delayed for some partners」までで、`updated_at` も 8/7 22:02Z のままだった。月内追記のない日は2日連続になり、8/5〜8/9 に毎日1件ずつ増えていた流れは止まっている
- Microsoft Purview の `whats-new` は7月節に Copilot 関連の新規追加がなく、8月節は未作成である。Copilot in SharePoint も 8/6 の月次記事が最新のままで、続報は出ていない

### Google

- Gemini in Classroom が予定どおり 8/10 から全年齢の生徒へ開放された（web）。管理者が Gemini in Classroom / Gemini / Gemini Notebook へのアクセスを付与済みの K-12・高等教育の生徒が対象で、授業資料や課題に紐づいたフラッシュカード・小テスト・学習ガイド・ガイド付きプロンプトが使える。モバイルは 8/17 である
- Gemini Spark が 7/30 から利用者の実機 Chrome を操作できるようになり、その後 AI Pro / AI Ultra の有料契約者向けに160カ国超へ拡大した（本日初検出）。従来は Google 側インフラ上のリモートブラウザを使っていたが、利用者のマシン上の実際の Chrome セッションで動くため、ログイン済みアカウントと保存済みパスワードをそのまま使って社内で実際に使っているツールへ到達できる。要件は Windows / macOS の最新版 Chrome と個人 Google アカウントで、オンライン決済など機微な操作は人の承認を要し、プロンプトインジェクション対策を追加したとしている。ブラウザ操作型エージェントが「隔離環境で動く」前提から「利用者の資格情報をそのまま持つ」前提へ移った点が統制上の変化にあたる。7/30 の提供開始を12日遅れで捕捉した
- Gemini API の changelog は 7/30 の Gemini Robotics ER 2 public preview が最上位のままで、8月の追加はない。`gemini-robotics-er-1.6-preview` の 8/31 停止予定も据え置きである
- Gemini API の単価は9日連続で据え置きだった。3.6 Flash（$1.50／$7.50）と 3.5 Flash（$1.50／$9.00）の出力単価の逆転、3.1 Flash-Lite（$0.25／$1.50）が 3.5 Flash-Lite（$0.30／$2.50）より安い関係のいずれも継続している
- Gemini 3.5 Pro の GA は未ローンチが継続している。8/12 のリーク報道はあるが Google 自身は未発表で、I/O（5/19）発表後に 6月 → 7月 → 7/17 と3回スリップしている
- https://9to5google.com/2026/07/30/gemini-spark-chrome-auto-browse/ ／ https://ai.google.dev/gemini-api/docs/pricing

### MCP / オープンウェイト

- Meta が **Muse Glimmer 30B** を Apache 2.0 で公開した（8/9 に Hugging Face 作成・8/10 告知）。上位モデル Muse Spark から蒸留した 30B の dense multimodal モデルで、エージェント基盤の前提が「クラウド API に接続する」から「手元の GPU 1枚でも完結しうる」へ広がった
  - 構成: 約 29.6B の dense causal transformer に約 1.8B の ViT-G/14 perception encoder を組み合わせ、52層・sliding-window attention（2048トークン）・コンテキスト 131,072+ を持つ。入力はテキストと画像、出力はテキストのみで、画像1枚あたりの視覚トークン上限は 4,096 である
  - ベンチマーク: SWE-Bench Verified 76.0% / SWE-Bench Pro 51.2% / AIME 2026 94.7% / MCP Atlas 75.5 / DeepSearch QA 74.6 / GAIA2 43.3 で同クラス優位だが、Terminal-Bench 2.1 は 51.7 と Meta 自身の比較表でも Qwen の 60.7 に劣る
  - VRAM と加速: 量子化で 24GB VRAM の単一 GPU に収まり、劣化は 0.2〜1.0% とされる。DFlash 投機デコーダによる高速化は RTX 5090 で 3.1倍・M5 Max で 1.8倍・M4 Max で 1.5倍である
  - 配布: 公式の GGUF と ExecuTorch-PTE に加え、8/10 のうちに unsloth / mlx-community / lmstudio-community / RedHatAI などサードパーティの量子化が出そろい、ローカル実行の経路は当日から整っている。上位の Muse Spark 1.2 はクローズドウェイトのままである
  - ⚠️ full precision の VRAM は Master 側が 64GB、industry 側が 55GB と食い違っており、量子化後も「K-Quant-17GB で 24GB」と「4bit で 18〜20GB」で表記が異なる。導入判定に使う場合は一次モデルカードで確認する必要がある
- Qwen3.8-Max / Qwen3.8-27B の open weights は 8/11 時点で未公開である。Alibaba は「8/10 の週」に Hugging Face と ModelScope へ出すと表明しているが、HF の作成日降順走査と trending 上位のいずれにも現れていない。Qwen3.8-Max は 2.4T パラメータ MoE（アクティブ 95B）・1M コンテキストで 8/3 に API 提供済みで、ライセンスは未開示のままである
- DeepSeek が 8/6 に告知した API の「大幅値上げ」は、本日時点でも幅も実施日も公表されていない。現行の V4-Flash は入力 $0.14／出力 $0.28（100万トークン）で据え置きが続き、08-09 に収録した北京時間の平日ピーク時間帯（9〜12時・14〜18時）の単価2倍も未発動である。⚠️ 一次の `api-docs.deepseek.com` はゲートウェイ拒否のため、公式料金ページの改定は検知できない
- MCP 公式ブログは 7/28 の `The 2026-07-28 Specification` が最新のままで、14日連続で動きがない。Tier 1 SDK も変化がなく、TypeScript は `@modelcontextprotocol/server` / `client` とも 2.0.0、Python `mcp` 2.0.0、C# v2.0、Go は v2 未発行で `go-sdk` v1.7.0 が仕様対応である
- Hugging Face の trending 上位に変化はない: `moonshotai/Kimi-K3`・`MiniMaxAI/MiniMax-H3`・`deepseek-ai/DeepSeek-V4-Flash-0731`
- https://huggingface.co/meta-models/Muse-Glimmer-30B ／ https://www.cnbc.com/2026/08/10/meta-muse-glimmer-open-weight-ai.html

### Cursor / 開発ツール

- AWS が Bedrock Agents を Classic 化していた（ハイライト3参照）
- Cursor は changelog・フォーラムとも更新がない。changelog は 8/3 の Google Workspace Plugins、Announcements は 7/28 の Cursor Start が最上位のままである。⚠️ `cursor.com` は WebFetch 503 が継続しているため `curl` で取得した（RSS 200 / `application/rss+xml` / 131,910 bytes / item 50件）
- Devin が Automations に Queueing Support を追加していた（8/7・本日初検出）。automation ごとに同時実行数の上限とキュー深度を設定でき、キューのライフサイクル状態を events テーブルで確認し、automation events を集計したアクティビティチャートを見られる
- Grok 4.6 は一次確認が依然できない。二次サイトは「8/7 ローンチ・1.5T パラメータ・V9 基盤据え置き・post-training 主体の改善」と書き、2.1T の Grok 4.7 が数週間後に続くとするが、`x.ai` / `docs.x.ai` / `openrouter.ai` がいずれもゲートウェイ拒否のため裏取り経路がない
- Apple Developer News は 8/5 の「Get ready for new creative assets on the App Store」が最上位のままで、AI 関連の新規はない。iOS 27 / iPadOS 27 は developer beta 4（7/20・ビルド 23G71）が最新で、GA は9月（予想 9/14 前後）である

### 国内

- NEC が「コーポレートAI・Workforce部門」の新設を 8/10 に発表した（設置は 8/1 付）。部門長から社員まですべての役割を AI が担い、人は最終的な評価・意思決定と品質・ガバナンスの統制のみを持つ。定量成果を伴う国内の組織レベル導入事例として引用できる
  - 構成: AI部門長・AIボード（CxO 機能）・AIマネージャー・AI社員の4階層で、社内からの業務要請に応じて AIマネージャーが AI社員を都度生成し役割を割り当てる
  - オンボーディング: AI社員は NEC グループのパーパス・行動規範・社内規程を組み込んだオンボーディングを受けたうえで業務にあたり、不足するスキルは各 AI が自ら学習して更新を続ける
  - 検証結果: 7月からの1カ月間の社内検証では、経営会議に提示する経営分析・シミュレーション・リスク予測の所要時間が約7分の1に短縮された
  - ⚠️ `jpn.nec.com` はゲートウェイ拒否として本日新規に記録されており、一次プレスリリースの本文は二次報道との突き合わせによる
- Qiita / Zenn は厳選掲載に値する新規記事を検出していない。Copilot Studio のクレジット課金を扱う解説記事が引き続き出ており、「モデル選択で消費が100倍変わる」旨に触れる記事があった。本日の Copilot Studio 項目はこの指摘を手がかりに一次ページを特定して裏を取ったもので、根拠は二次記事ではなく Learn の一次ページに置いている
- https://jpn.nec.com/press/202608/20260810_01.html ／ https://www.itmedia.co.jp/aiplus/article/2608/10/2000000484/

## 直近の注目予定

- **8/12**: Made by Google ／ Gemini 3.5 Pro ローンチの噂（Google 未発表）
- **8/14**: Claude Code の既定権限モードが auto mode へ（Pro / Max / Team）／ Copilot Success Planner の提供開始 ／ DOE Genesis 寄与プログラムの第1次応募締切
- **8/16**: Power CAT（Copilot Agent Kit）・PnP の週次確認
- **8/17**: Claude Console 旧 Workbench 退役 ＋ 実験的プロンプトツール API 廃止 ／ Gemini API の Imagen 4.0 系3本停止 ／ Gemini in Classroom のモバイル開放 ／ MS-4005 の週次確認
- **8/18**: Copilot Studio Released Versions の次の定例更新日（更新がなければ空振り5回目）
- **8/18〜9/8**: M365 Copilot Agent's Playbook ライブストリーム（各回 9AM PT）
- **8/19**: Claude Code 週次上限50%増の終了
- **8/20**: ChatGPT Business Premium シートのクレジット販促の受付終了 ／ Gemini Enterprise Agent Platform の Grok 4.1 ファミリー停止（一次未確認）
- **8/22**: M365 Copilot アプリのチャット中心 UI が Deferred リングへ展開開始
- **8/26**: OpenAI Assistants API 廃止 / o3 退役 / GPT-4.5 完全廃止 ／ Copilot 既定モデル有効化ポリシー発効
- **8/30**: 公式 DALL·E GPT の退役
- **8/31**: GitHub Spark の既存ユーザーアクセス終了 ／ Sonnet 5 促進価格終了（→ $3/$15） ／ `gemini-robotics-er-1.6-preview` 停止 ／ GPT-5.4・5.4 mini が Codex から除外 ／ Claude for Government の $1/機関プログラム終了 ／ Power Automate モバイルアプリの廃止
- **9/1**: GitHub Copilot の全体験でモデル廃止 ／ OpenAI Daybreak 全アカウントでハードウェアセキュリティキー必須化
- **9/2**: Windows 365 Frontline 名称での購入最終日 ／ **9/3**: Windows 365 Flex へ改称
- **9/30**: M365 E7 プロモーションの対象購入最終日 ／ M365 E5 / E3 の CSP 割引終了 ／ **10/1**: E7 プロモーションの新規取引停止
- **10/1**: OpenAI 対 Apple の営業秘密訴訟の審尋
- **10/27〜29**: Power Platform Community Conference 2026（MGM Grand ラスベガス）
- **11/1**: パートナー特典の有効期限がオファー購入日基準へ移行
- **12/2**: EU AI Act の生成コンテンツ標識義務、8/2 以前に市場投入済みシステムへの猶予終了
- **12/31**: M365 E3 プロモーション ／ Copilot in 30 ／ Purview Suite 50%オフの提供終了
- **8月中旬**: M365 Copilot Release Notes の次バッチ見込み ／ OpenAI の公開 S-1 掲載見込み
- **9月**: iOS 27 / macOS 27 GA ／ auto mode の既定化を Enterprise・API・各クラウドへ拡大予定
- **時期未定**: ドメイン除外の再提供 ／ Cowork 1 の提供開始 ／ Copilot Studio What's New への7月・8月節の追加とハーネス GA の反映 ／ Fluent UI (v8) コントロールの廃止日 ／ Bedrock Agents Classic の提供終了日

## 改善メモ

- 本サマリーの訂正: 08-09・08-10 に「Copilot Credits の単価は Learn 側に一切載っていない」と書いた点を、02 の一次確認に沿って訂正した。Learn に無いのは1クレジットあたりの USD 価格（Licensing Guide の PDF・403）であり、消費レート自体は `requirements-messages-management` に載っている
- Master: 新規提案 B-030（OpenAI Blog / News の検索キーワードにも当日・前日の日付を含む形を必須化）を出した。継続提案は10件で、最多は B-013（403の2分類記録・15回目）である
- Copilot: 新規提案 B-031（課金レートページ `requirements-messages-management` をソース定義に追加）を出した。B-022 のソース候補4本に含まれておらず本日まで未巡回だった点が発端である。継続提案は19件で、最多は B-011（Power Platform Blog のトピック記事照合・23回目）である
- industry: 新規提案 B-024（AWS のサービス廃止・移行告知を定点ソースに追加）を出した。継続提案は5件で、最多は B-004（取得方法欄の WebSearch 優先化・43回目）である
- ⚠️ 提案番号の重複: industry の新規 B-024 は、Copilot 側の B-024（board RSS の `pubDate` 突合）と番号が重なっている。台帳がソースごとに独立しているためだが、本サマリーで横断して参照する際は必ずソース名を添える必要がある
- ソース間の矛盾: Muse Glimmer の full precision VRAM が Master 64GB / industry 55GB で食い違い、量子化後の表記も「K-Quant-17GB で 24GB」と「4bit で 18〜20GB」で異なる（カテゴリ側にも注記した）
- 障害の変化（Master）: `the-decoder.com` / `www.unite.ai` をゲートウェイ拒否として最終確認日を更新した。`cursor.com` の WebFetch 503 は継続しており、`curl` 200 で代替している
- 障害の変化（Copilot）: `www.microsoft.com` 配下3 URL（M365 Roadmap / M365 Blog RSS / Copilot Blog RSS）が WebFetch で一時的に HTTP 503 を返した。同一セッションの `curl` はいずれも 200 で、URL 末尾のスラッシュを変えた再取得も3本とも成功したため、WebFetch 層の一時的な失敗として扱っている
- 障害の変化（industry）: `docs.aws.amazon.com` / `research.meta.ai` / `jpn.nec.com` の3ドメインを新規のゲートウェイ拒否として記録した。`huggingface.co` のモデルカードは本日も WebFetch 成功で、08-03 の復旧が継続している
- Power Platform Weekly は 8/10 の休刊明けを判定できないまま2日目に入った。`ppweekly.com` の疎通そのものが塞がれており、新号の有無を確かめる手段が現在ない
