# AI News Daily Summary — 2026-10-10

Google は Gemini API の Deep Research エージェント旧版を 10/23 に止めると告知した。GitHub は Copilot code review の費用を組織負担に切り替えられる設定を出した。Microsoft は Grok を独立プロセッサとして使える面に Copilot Cowork を加え、Office in Copilot の展開を Frontier で始めた。Anthropic は Managed Agents に dynamic workflows をベータで入れ、Claude Code 2.1.296 で非 UTF-8 ファイルの文字化けを止めた。

## 今日のハイライト

### 1. [廃止] Google が Gemini API の Deep Research エージェント `deep-research-pro-preview-12-2025` を 10/23 に止める — 告知から停止まで15日しかない

**要点**: Google が Gemini API changelog で、Deep Research エージェントの旧版 `deep-research-pro-preview-12-2025` を deprecated にし、10/23 に停止すると告知した（10/8）。旧 ID を指定したままの呼び出しは月内に失敗する前提に変わった。

**詳細**:

- 移行先: `deep-research-preview-04-2026`（速度重視・クライアント UI へのストリーミング向け）と `deep-research-max-preview-04-2026`（網羅性重視）の2つで、どちらもプレビューのまま
- 移行方法: `interactions.create` の `agent` パラメーターを旧 ID から新 ID に書き換える
- 料金差・機能差は changelog に書かれていない。停止の扱いは deprecations ページの Managed Agents 節に載る

- https://ai.google.dev/gemini-api/docs/changelog

### 2. [料金+新機能] GitHub が Copilot code review の費用を組織負担に切り替えられるようにした — 既定のままだと依頼者の枠が尽きた時点でレビューが失敗する

**要点**: GitHub が Copilot code review に、レビュー費用を誰が払うかを選ぶ組織設定と、レビュー依頼を組織付与ライセンスの持ち主に限る設定を加えた（10/8）。既定は従来どおり依頼者の枠消費で、組織負担には AI Credits の従量課金の有効化が要る。

**詳細**:

- 「Choose how members with a Copilot license are billed」（組織設定 > Copilot > Policies）
  - Member（既定）: 依頼したメンバーの Copilot 枠を使う。枠が尽きるとレビューは失敗する
  - Organization: リポジトリを所有する組織に課金し、メンバーの枠を減らさない。AI Credits の従量課金の有効化が必須で、予算上限も設定できる
- 「Only allow Copilot code review to be triggered by authorized users」: オンにすると、組織またはエンタープライズが付与したライセンスの持ち主だけがレビューを依頼できる。外部の個人ライセンスは使えない。組織レベルでオンにするとリポジトリ管理者は外せない
- いずれも既定の挙動は変えない（オプトイン）

- https://github.blog/changelog/2026-10-08-copilot-code-review-new-organization-billing-options-and-controls

### 3. [仕様] Grok を Copilot Cowork で使うと Microsoft の契約保護の外で処理される — 独立プロセッサ経路の対象が Copilot Studio から Cowork へ広がった

**要点**: Microsoft が Learn の `connect-to-ai-models` を改訂し、SpaceXAI モデルを独立プロセッサとして使える面を「Copilot Studio と Copilot Cowork」に書き直した（10/9）。Cowork で Grok を選ぶと Product Terms・DPA・著作権補償が外れ、保護が付くのは Word / Excel / PowerPoint のサブプロセッサ経路だけになる。

**詳細**: `connect-to-ai-models` と `spacexai-subprocessor` が、どちらも 10/9 17:43Z に `ms.date` 10/9 で改訂された。9/13 時点の `connect-to-ai-models` は対象を「Copilot Studio in Microsoft 365」としか書いていなかった。

- 独立プロセッサ経路（Copilot Studio / Cowork）: データは Microsoft 管理環境と監査統制の外で処理され、データ所在地・SLA・Customer Copyright Commitment も適用されない。xAI Enterprise Terms と xAI DPA に従う。有効化は M365 管理センター > Copilot > Settings > View all > AI providers for other large language models で、Global administrator が要る
- サブプロセッサ経路（Word / Excel / PowerPoint のモデルセレクター）: 9/21 に既報で変化はない。Frontier 加入テナントに限られ、EU・EFTA・英国と政府・ソブリンクラウドは対象外
- Cowork のモデルピッカーを定める `cowork-models` は `updated_at` 9/14 のままで、Grok はまだ一覧に無い

- https://learn.microsoft.com/en-us/microsoft-365/copilot/connect-to-ai-models
- https://learn.microsoft.com/en-us/microsoft-365/copilot/spacexai-subprocessor

## カテゴリ別まとめ

### Claude / Anthropic

- [新機能] **Managed Agents の dynamic workflows** — Anthropic が Managed Agents に、エージェント自身がワークフローのプログラムを書き、多数のサブエージェントを段階実行させて結果をまとめる dynamic workflows をベータで出した（10/9）。`managed-agents-2026-04-01` ヘッダーのもと、`multiagent` を `{"type": "multiagent_20261001", "workflows": {"type": "enabled"}}` にすると有効になる。
  - 上限: 1回の実行あたり起動エージェント1,000、同時実行はセッションあたり既定10、実行の寿命は既定24時間
  - 課金: 実行そのものは無料で、各エージェントのトークンがモデル単価で課金され、セッションの予算に達すると止まる
  - 追跡: 起動条件はシステムプロンプトで指示し、進捗は `workflow_run.*` イベントで追う
  - https://platform.claude.com/docs/en/release-notes/overview / https://platform.claude.com/docs/en/managed-agents/workflow-runs
- [セキュリティ+新機能] **Claude Code 2.1.296** — Anthropic が Claude Code `2.1.296` を出し、Edit / NotebookEdit が Shift-JIS などの非 UTF-8 ファイルを壊していた問題を、編集自体を拒否する形で止めた（10/9）。npm では `next` にある。
  - セキュリティ修正: `BASH_ARGV0` を代入して使うコマンドを Bash の権限チェックが自動承認していた問題と、フォルダー単位で無効にした MCP サーバーをヘッドレス実行が起動していた問題を直した
  - 管理設定のフック: `"continue": false` で拒否する `PreToolUse` フックが、ターンを終わらせず呼び出しだけを拒否するようになった
  - 新設定: サブエージェント定義の `autoCompactWindow`、ワークフローの全エージェントのモデルを揃える `CLAUDE_CODE_WORKFLOW_SUBAGENT_MODEL`
  - 既定の変更: MCP ツール説明とサーバー指示の上限を 4,096字にし、`/cost` と `--max-budget-usd` が Sonnet 5.5 のキャッシュ読みを $0.10 で計算するようにした
  - https://code.claude.com/docs/en/changelog
- [新機能] **Claude Code 2.1.295 の `latest` 昇格** — Anthropic が `2.1.295` を npm の `latest` に上げた（`{stable: 2.1.286, latest: 2.1.295, next: 2.1.296}`）。フックの `onFailure: "block"` は前日掲載済みで、日次に未掲載だった変更は次のとおり。
  - Claude apps gateway: アップストリームごとの `models` リスト、Bedrock / Vertex / Foundry での `timeouts.upstream_ttfb_ms`、監査イベントの `upstream_request_id`
  - 不具合修正: `[1m]` モデルで context-1m ベータを拒否されると全リクエストが失敗していた問題、ヘッドレス / SDK でリモート MCP サーバーが15秒超の障害後に切断されたままになる問題
  - https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
- [据え置き] **Usage Policy 改定・Cyber Mission・Genesis Mission** — 3件とも 10/8 公表で前日掲載済みであり、続報は無い。`anthropic.com/news`・`claude.com/blog`・`support.claude.com` の最上位も前日から変わっていない
- [据え置き] **Claude Haiku 4.5 の退役告知** — `claude-haiku-4-5-20251001` は退役下限日の5日前でも Active のままである。Anthropic は退役の60日以上前に通知するとしており、10/15 の退役は起こらない見込み。https://platform.claude.com/docs/en/about-claude/model-deprecations

### OpenAI / Codex / ChatGPT

- [新機能+予定] **EU での出力テキスト透かし** — OpenAI が EU AI Act 第50条への対応として、EU の対象ユーザーの ChatGPT / Codex の出力に数週間で見えない透かし「textGrain」を入れると発表した（10/5）。API 利用者は全世界で同日からオプトインでき、既定はオフである。語の約10%を言い換えると検出率が約92%から66%に落ちると報じられた（二次のみ・5日遅れの捕捉）。https://www.computing.co.uk/news/2026/ai/openai-to-watermark-chatgpt-text-insert-visual-ads / https://bleepingcomputer.com/news/artificial-intelligence/openai-is-adding-invisible-watermarks-to-chatgpt-and-codex-text-in-the-eu
- [版更新] **Codex CLI 0.163.0-alpha.4** — OpenAI が Codex CLI の安定版を `0.162.0`（10/8）のまま据え置き、pre-release を `0.163.0-alpha.4`（10/9）まで進めた。community Announcements・API changelog・`learn.chatgpt.com` は 10/8 の GPT-6.1 Sol Ultrafast が最上位のままである。https://github.com/openai/codex/releases

### GitHub Copilot / GitHub

- **Copilot code review の課金と依頼制限**（ハイライト参照・2）
- [新機能] **Copilot CLI v1.0.95** — GitHub が Copilot CLI の安定版 `v1.0.95` を出した（10/9）。macOS で Microsoft Entra のネイティブ broker 認証を使えるようにし（使えなければブラウザーへ戻る）、`copilot config` でサンドボックスの資格情報 `injectHosts` を設定できるようにした。前日の安定版 `v1.0.94` は Haiku 5.5 のモデル選択と、管理ポリシーで Assisted Permissions を無効にする設定を含む。https://github.com/github/copilot-cli/releases

### Microsoft 365 Copilot / Copilot Studio / Power Platform

- **Grok の Cowork 独立プロセッサ経路**（ハイライト参照・3）
- [新機能] **Office in Copilot の展開開始** — Microsoft が、Copilot アプリ内で Word / Excel / PowerPoint を編集・共同編集できる Office in Copilot を Frontier 顧客の Chat と Cowork で展開し始めた（10/9）。9/26 時点では告知だけだった。
  - 編集: Copilot が作ったファイルは会話の横に開き、プロンプトでもキャンバス上の直接編集でも直せる
  - 共同作業: 共有・コメント・共同編集・プレゼンスが同じ画面で使える
  - 保存と統制: ファイルは OneDrive に保存され、書式・共有権限・版履歴と秘密度ラベルを引き継ぐ
  - https://techcommunity.microsoft.com/t5/microsoft-copilot-blog/introducing-office-in-the-new-microsoft-copilot-app/ba-p/4561230
- [新機能] **Copilot Notebooks 10月更新** — Microsoft が Notebooks の参照ソースに Markdown / TXT / RTF を加え、成果物の提案機能とあわせて GA にした（10/9）。Frontier では新 UX・モデル選択・Office の直接編集・PDF 生成が使え、今後数週間でノートブックの自動作成・定期タスク・音声概要の更新（Roadmap 570966）が出る。https://techcommunity.microsoft.com/t5/microsoft-copilot-blog/what-s-new-in-notebooks-october-2026/ba-p/4559105
- [予定] **Roadmap の新規3件** — Microsoft が Roadmap に次の3件を起票した。
  - 573446: OneNote の Copilot Chat が編集モードでページ・セクション・ノートブックを作成・編集できるようになる（GA November CY2026）
  - 573169: Viva Insights の Agent 365 Dashboard がサードパーティのエージェントを集計する（Preview / GA October CY2026）
  - 574106: SharePoint の Copilot が保存前のプレビューをチャットの横に並べ、生成した HTML フォームの回答を送れるようになる（GA November CY2026）
  - https://www.microsoft.com/microsoft-365/roadmap?id=573446
- [観測] **10/9 の Learn 改訂3本** — Microsoft が `openai-subprocessor`・`people-skills-sharing-inferencing-controls`・`cowork-available-plugins` を 10/9 20:42Z に同時に改訂した。`openai-subprocessor` の記載は既報の範囲で、公開ミラーが3月版のため差分は特定できていない
- [据え置き] **Release Notes / Copilot Studio / Power Platform の定点** — M365 Copilot Release Notes の先頭は October 06, 2026 のまま、Copilot Studio What's New は `ms.date` 10/5 のまま、Released Versions は 2026.6.3 のまま（101日）である。Release Wave の製品別ページも 9/3 のままで、Roadmap の Copilot Studio 25件にも増減は無い。https://learn.microsoft.com/en-us/power-platform/released-versions/copilotstudio

### Google / Cursor / 市場・その他

- **Deep Research エージェント旧版の停止**（ハイライト参照・1）
- [観測] **Gemini アプリ無料枠の Flash-Lite 限定** — Gemini アプリの無料枠を 10/9 から 3.5 Flash-Lite のみにする変更は、発効日を過ぎても一次で確認できていない。二次は、無料は Flash-Lite のみ・AI Plus は Flash-Lite と Flash・AI Pro は Deep Think を含む全モデルとしている。https://ud.hk/en/blogs/insight/article/gemini-free-flash-lite-guide-2026-10-06
- [据え置き] **Cursor・xAI・MCP・HF・Apple** — Cursor changelog は 10/6 の Remote control、フォーラム Announcements は 9/21 の Grok 4.7 が最上位のままである。Hugging Face の登録 org では Qwen の画像生成と Mistral の音声系が増えたが、テキスト系 LLM の重み公開は無い。MCP ブログと Apple Developer News にも新規は無い
- [据え置き] **市場データ** — IDC Japan・MM総研・NRC・Similarweb はいずれも新規公表が無い。Similarweb の9月分は未検知で、二次で確認できる最新は8月分（ChatGPT 55.5%・Gemini 25.6%・Claude 9.3%）である

## 直近の注目予定

- **10月**: Copilot Chat の UBB モデル選択（571400） ／ デスクトップフローのスケジュールトリガー GA（573278） ／ Notebooks 音声概要の更新（570966） ／ Agent 365 Dashboard のサードパーティ集計（573169）
- **10/13**: Gemini アプリで skills の展開開始 ／ Partner Digital Airlift（新しい Copilot）
- **10/14**: GPT-5.5 が ChatGPT / Codex から退役 ／ Anthropic の pre-IPO investor day（報道）
- **10/15 以降**: `claude-haiku-4-5-20251001` の暫定退役日（告知はまだ無い）
- **10/19**: GitHub Copilot が5モデルを廃止
- **10/22**: Copilot Business / Enterprise の機能既定有効化が発効
- **10/23**: Gemini API の `deep-research-pro-preview-12-2025` が停止
- **10/27〜29**: PPCC 2026（ラスベガス）
- **10/30**: ChatGPT Pro 200 の Work / Codex 利用枠が変更（二次）
- **10/31**: MCP サーバー認定の旧申請経路が終了
- **11/1**: Codex の28日間「改善かリセット」の終了（二次）
- **11月**: Business Applications in Work IQ が既存環境で既定オン ／ OneNote の Copilot 編集 GA（573446） ／ SharePoint の Copilot プレビュー並列表示 GA（574106）
- **11/12**: Anthropic Usage Policy 改定版が発効 ／ OpenAI → Cursor のモデル供給停止予定（一次未読）
- **11/16**: Sales Development Agent が Copilot Credits の消費を開始
- **11/17**: Gems が Gemini アプリの設定パネルへ移動
- **11/17〜20**: Microsoft Ignite
- **11/30**: `claude-sonnet-4-5-20250929` が Claude API から退役
- **12/1**: Copilot Business の従量課金が既定オン
- **12/14**: claude.ai/design の単体サイトが閉鎖
- **2027-01-06**: OpenAI `tts-1` / `tts-1-hd` / `gpt-4o-mini-tts` 2版が停止
- **2027-03-01 以降**: Gems 廃止（Business / Enterprise）
- **2027-04-01**: OpenAI `gpt-5.1` / `gpt-5.3-codex` / `gpt-5.4-nano` が停止

## 改善メモ

- 新規提案: 3ソースとも無し
- 継続提案: Master は B-035 npm dist-tags（55回目）・B-079 HF の ID 集合差分（9回目）・B-082 最上位エントリ基準の差分判定（16回目）を再確認 ／ Copilot は B-074（docset 全件突合・1,487ページ）・B-079（公開ミラーでの差分取得）・B-065（モデル告知と一次の提供面の不一致）・B-037（101日）を更新 ／ industry は2件を更新（最多 B-004・102回目）。B-031 に 10/8 付3ソース（Gemini changelog・GitHub changelog・Anthropic /news）の取りこぼしを追記
- 障害の変化: 3ソースとも無し
- ソース間の差分・矛盾:
  - Claude Code `2.1.296` は Master が「changelog 未掲載」、industry が公式 changelog（10/9）を出典に詳細を載せており、確認時刻の差とみられる。industry の記述を採り、`2.1.295` の `latest` 昇格は別項目に分けた（1項目に2リリースを同居させない補則）
  - Usage Policy 改定は industry がハイライト2 [仕様+予定] にしたが、日次では 10/9 に掲載済みで続報が無いため [据え置き] にまとめた。Cyber Mission・Genesis Mission も同じ扱い
  - Copilot code review は Master が [料金+新機能]、industry が [料金] で割れた。依頼制限の設定が今日から使える機能として加わるため、Master と同じ [料金+新機能] とした
  - Deep Research 旧版の停止は industry が 10/9 に同ページを確認しながら 10/8 付を取りこぼし、1日遅れの捕捉だった（industry B-031 に記録済み）
