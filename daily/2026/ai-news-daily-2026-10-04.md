# AI News Daily Summary — 2026-10-04

土曜で一次ソースの更新が少ない日である。Microsoft は Roadmap 571400 で、Copilot Chat の上位モデルを管理者が割り当てた Copilot Credits の範囲で使う形にすると示した。Anthropic は Claude Code `2.1.288` の変更内容を公開して `latest` に上げ、`rm` の保護が外れる不具合と応答途中のタイムアウトを直した。GitHub は Copilot code review を API から依頼できるようにした。

## 今日のハイライト

### 1. [料金+予定] Copilot Chat のモデルセレクターで、Copilot Credits を消費するモデルを選べるようになる — 上位モデルの利用枠はライセンス込みから管理者のクレジット割り当てに変わる

**要点**: Microsoft が Roadmap **571400** で、Copilot Chat の利用者が従量課金（UBB）対象のモデルをモデルセレクターから選べるようになると示した（GA 期日 October CY2026）。管理者がクレジットを割り当てないと使えないので、Chat の上位モデルは「ライセンス込み」から「割り当てたクレジットの範囲内」に変わる。

**詳細**:

- 一次は Release Communications RSS の 10/2 22:01Z バッチ（`In development`・GA・Worldwide・Desktop / Web）
- 区分（Learn の USL / UBB 解説）: GPT 5.6 と Sonnet は公正利用の範囲で込み、Opus は上限付きで込み、Astra / Fable などの新しいフロンティアモデルは UBB
- クレジットを使い切った利用者は管理者に追加を要求し、管理者は M365 管理センターの **Copilot > Cost Management** の Credit requests で処理する

- https://www.microsoft.com/microsoft-365/roadmap?id=571400
- https://learn.microsoft.com/microsoft-365/copilot/user-subscription-license-usage-based-billing

### 2. [セキュリティ+新機能] Anthropic が Claude Code `2.1.288` を `latest` に上げ、`rm` の保護が外れる不具合を直した — 長時間の無人実行も応答途中のタイムアウトで落ちなくなった

**要点**: Anthropic が 10/2 に `next` へ出していた `2.1.288` の変更内容を changelog に載せ、npm の `latest` に昇格させた。`~` やワイルドカードへのリダイレクトで危険な `rm` の確認が飛ばされていた不具合を直し、非対話セッションとサブエージェントは応答途中のタイムアウトから部分応答で続行するようになった。

**詳細**:

- 修正:
  - セキュリティ: `~` やワイルドカードのパスへリダイレクトすると `rm` の保護が効かなかった。Bash の権限判定で、算術評価される `BASHPID` 代入を黙って通していたのも確認対象にした
  - 安定性: 応答途中の API タイムアウト（thinking のみの応答は再試行）、トークン使用量 0 の応答で自動 compact せず「Prompt is too long」で落ちる問題、`--resume` で compact 直後のファイルが落ちる問題
- 追加:
  - Ctrl+C で消したプロンプトを、空のプロンプトで ↑ を押すと貼り付けた文字・画像ごと戻せる
  - `/code-review` に `--max-findings <n>|all` を追加した
  - `gh` の無いクラウドセッションに組み込みの `gh api` を入れ、構造化出力を拒むゲートウェイ向けに `CLAUDE_CODE_DISABLE_STRUCTURED_OUTPUTS` を加えた
- dist-tags は `{stable: 2.1.285, latest: 2.1.288, next: 2.1.288}`

- https://code.claude.com/docs/en/changelog
- https://www.npmjs.com/package/@anthropic-ai/claude-code

### 3. [新機能] GitHub が Copilot code review を REST / GraphQL API から依頼できるようにした — レビューの起点が PR 画面の手操作から自社のスクリプトや CI に変わる

**要点**: GitHub が 10/2 に、Copilot code review を REST と GraphQL の API から依頼でき、依頼ごとに effort level（Lite / Balanced）を指定できるようにした（GA）。レビューは「人が PR で呼ぶもの」から「既存の自動化から起動できるもの」に変わる。

**詳細**:

- 対象プラン: Copilot Pro / Pro+ / Max / Business / Enterprise。課金への言及は告知に無い
- 既定 effort の Balanced 化（8/28 予告）は 9/28 に発効した。明示的に Lite を選んでいた設定はそのまま残る
- Lite に戻す場所は Enterprise / Organization / Repository / 個人設定の4階層で、下位が上位を上書きする

- https://github.blog/changelog/2026-10-02-copilot-code-review-api-support-and-new-default-effort-level

## カテゴリ別まとめ

### Claude / Anthropic

- **Claude Code 2.1.288**（ハイライト参照・2）
- [据え置き] **API release notes・製品側の定点** — Anthropic の API release notes は 9/30 の Sonnet 4.5 退役告知が最上位のままで、`claude-haiku-4-5-20251001` の退役告知も Claude Haiku 5.5 も出ていない。`anthropic.com/news`・`claude.com/blog`・`support.claude.com`・`status.claude.com` にも 10/3 付の新規は無い。

### OpenAI / Codex / ChatGPT

- [新機能] **ChatGPT Finances の Free / Go 開放** — OpenAI が ChatGPT の Finances を米国の Free / Go ユーザーにも広げた（10/2）。Plaid 経由で銀行・カード・証券口座をつなぎ、支出・定期支払い・純資産を会話とダッシュボードで扱え、米国では全プランで使えるようになった。一次（`help.openai.com`）はオリジン403で未読である。https://www.datastudios.org/post/openai-finances-chatgpt-free-go-connected-accounts-spending-savings-investments
- [版更新] **Codex pre-release** — OpenAI が Codex の pre-release を `rust-v0.162.0-alpha.10`（10/3）まで進めた。安定版は `rust-v0.160.0`（10/1）のままである。https://github.com/openai/codex/releases
- [据え置き] **API changelog・退役ページ・Community** — OpenAI の API changelog は 9/29、退役ページは 10/1 の2件、community Announcements は 9/30、`learn.chatgpt.com` の changelog は 10/1 が最上位のままである。

### GitHub Copilot / GitHub

- **Copilot code review の API 対応**（ハイライト参照・3）
- [版更新] **Copilot CLI v1.0.92-3** — GitHub が Copilot CLI の pre-release `v1.0.92-3`（10/2）を出し、ローカル実行とクラウド実行を切り替える環境ピッカーを付け、10/2 に廃止したモデルを選択肢から外した。安定版は `v1.0.91` のままである。https://github.com/github/copilot-cli/releases

### Microsoft 365 Copilot / Copilot Studio / Power Platform

- **Copilot Chat の UBB モデル選択**（ハイライト参照・1）
- [仕様] **Copilot Studio のハーネス選定ガイド** — Microsoft が Copilot Studio ガイダンスハブに、標準ハーネスと GitHub Copilot ハーネスの選定基準を示す記事 `guidance/choose-harness`（`ms.date` 2026-09-30）を公開した。9/3 の白書を Learn に載せたもので、次の3点を明文化している。
  - 課金: GitHub Copilot ハーネスは構築から実行まで従量課金で、標準ハーネスは従来のライセンスモデルのまま
  - 移行: 動いている標準ハーネスのエージェントを移す必要はなく、移行は部品の変換ではなく再設計として扱う
  - 使い分け: 短く範囲の決まったタスクは標準、長時間・複数システム横断・反復推論は GitHub Copilot ハーネス。推論モデルの一部は GitHub Copilot ハーネスでしか使えない
  - https://learn.microsoft.com/en-us/microsoft-copilot-studio/guidance/choose-harness
- [新機能] **埋め込みモデル駆動型アプリの新しい外観** — 別ホストに埋め込んだ Power Apps のモデル駆動型アプリでも、半期チャネルの 2609.3 から Fluent の新しい外観が既定で有効になった。Microsoft が Roadmap **571682** を Launched にした（GCC / GCC High を含む。月次チャネルは 2602.1 で先行）。https://www.microsoft.com/microsoft-365/roadmap?id=571682
- [予定] **Outlook の対話型下書き（政府クラウド）** — GCC / GCC High / DoD の Outlook（Web）利用者が、対話しながらメールを下書き・修正・書式設定できるようになる。Microsoft が Roadmap **573280** で GA 期日を November CY2026 とした。https://www.microsoft.com/microsoft-365/roadmap?id=573280
- [予定] **Edge の Commercial Journeys** — Edge の Copilot 新しいタブページが、未完了・定例のタスクをカードで示し、ワンクリックでメールや文書まで作れるようになる。Microsoft が Roadmap **561040** で Preview を November CY2026、GA を January CY2027 とし、対象を「Microsoft 365 Copilot Premium」ライセンスの利用者と書いている。https://www.microsoft.com/microsoft-365/roadmap?id=561040
- [観測] **Learning Coach の退役時期（MC1454391）** — 二次情報によると Microsoft は Learning Coach エージェントを Learning Agent へ移して退役させるが、時期は「10月第1週」と「10月第1週から移行バナー、12月最終週に退役」で割れている。一次（Message Center 本文）は `mc.merill.net` のゲートウェイ拒否で未確認である。https://mwpro.co.uk/blog/2026/09/17/mc1454391-microsoft-365-copilot-retires-learning-coach-and-shifts-to-learning-agent/
- [新機能] **MAI-Transcribe-2-Streaming** — Microsoft AI がストリーミング音声認識 MAI-Transcribe-2-Streaming を Foundry で出した（10/1 ごろ）。話している途中で暫定の文字起こしを返し、60言語に対応し、導入価格は年末まで1音声時間あたり $0.54 である。音声合成の MAI-Voice-2.1 は100万文字あたり $22（Flash 版 $15）で、料金は二次情報による。https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/build-expressive-voice-experiences-with-new-mai-models-in-microsoft-foundry/4524637
- [据え置き] **Release Notes・What's New・Power Platform の定点** — M365 Copilot Release Notes の先頭は September 23, 2026 のままで、Copilot Studio What's New は July 2026 節のまま GitHub Copilot ハーネスの GA（8/3）を62日反映していない。Power Platform のブログ・Release Wave・Released Versions（Copilot Studio 最新ビルド 2026.6.3 のまま95日）も動いていない。

### Google

- [仕様] **Gemini 4 Argon の続報** — Google DeepMind の Gemini 4 Argon（10/3 に収録）について、キャッシュ入力が入力単価の95%引きで、導入期間の終了日は示されていないと報じられた。一般提供の前に米政府の自主的な事前アクセス手続きにも参加する。Google 公表のベンチマークは DeepSWE v1.1 で 77.9%、Vals Index で 68.9%（Claude Opus 5.5 67.0%・GPT-6 Astra 63.1%）で、外部の再現は無い。`ai.google.dev` の changelog・料金ページには 10/4 時点で載っていない。https://venturebeat.com/technology/google-unveils-gemini-4-argon-retaking-benchmark-lead-over-openai-and-anthropic-but-in-limited-release / https://apidog.com/blog/gemini-4-argon-pricing/
- [新機能] **Gemini Enterprise の federated query** — Google Cloud が Gemini Enterprise の Data Cloud コネクタに federated query モードを Preview で入れた（10/2）。AlloyDB / BigQuery / Cloud SQL / Spanner のデータを取り込まずに、ファーストパーティの MCP サーバー経由でユーザー本人の権限（IAM または OAuth 2.1）のまま問い合わせられる。一次（`docs.cloud.google.com`）はゲートウェイ拒否で、WebSearch の本文相当で確認した。https://docs.cloud.google.com/release-notes

### Cursor / xAI / その他エージェント

- [新機能] **Grok 4.7 の Gemini Enterprise 提供** — xAI の Grok 4.7 が Gemini Enterprise Agent Platform の Model Garden に Preview で入ったと報じられた（9/30〜10/1）。xAI API・Cursor・GitHub Copilot に続く提供先になる。一次（`docs.cloud.google.com` / `docs.x.ai`）はいずれもゲートウェイ拒否で未読である。https://huggingnews.com/ai/spacexai-launches-grok-47-on-gemini-enterprise-agent-platform-7e0fcb37
- [新機能] **IBM Bob のセルフホスト対応** — IBM がコーディングエージェント IBM Bob をセルフホストで動かせるようにした（10/1 発表）。Red Hat OpenShift 上のオンプレミス・ソブリンクラウド・エアギャップ環境に置け、切断環境では NVIDIA Nemotron か Poolside Laguna を自社 GPU で回す。https://www.marktechpost.com/2026/10/02/ibm-brings-bob-to-self-hosted-and-air-gapped-environments/
- [据え置き] **Cursor・MCP・Hugging Face・Apple** — Cursor の changelog は 9/23、フォーラム Announcements は 9/21 が最上位のままである。`blog.modelcontextprotocol.io` は 8/22、`developer.apple.com/news/` は 10/2 が最上位で、Hugging Face の登録8 org にも新規リポジトリは無い。

### 市場

- [据え置き] **市場データ** — IDC Japan・MM総研・NRC・Similarweb はいずれも新規公表が無く、Similarweb の9月分トラッカーも未検知である。

## 直近の注目予定

- **10/5**: Gemini の `antigravity-preview-05-2026` が停止 ／ Workspace で skills の展開開始（Rapid Release） ／ GPT-Rosalind の課金開始 ／ Anthropic Wellbeing Research Grants の選考結果通知
- **10/7**: GHE.com が X25519 単独の TLS 接続を拒否
- **10/13**: Gemini アプリで skills の展開開始 ／ Office / Project / Visio LTSC 2021 のサポート終了 ／ 新しい Copilot の Partner Digital Airlift
- **10/14**: GitHub SSH の新規 RSA 鍵が 3072 ビット以上必須に ／ GPT-5.5 が ChatGPT / Codex から退役 ／ Anthropic の pre-IPO investor day（報道）
- **10/15 以降**: `claude-haiku-4-5-20251001` の暫定退役日（告知はまだ無い）
- **10月**: Copilot Chat の UBB モデル選択 GA（571400） ／ SharePoint の画像生成・Advanced Autofill・サイト分析が Copilot Credits の消費対象に ／ Copilot Studio エージェントがコスト管理の対象に ／ スキルカタログ GA（571880） ／ 自己学習 GA（570432） ／ Copilot UX components GA（SPFx 1.24） ／ Teams 通話委任の Preview（565216） ／ Word・Cowork の Legal plugins GA（571884） ／ Work IQ 拡張2件の Preview（570853・570854）
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

- 新規提案: 3ソースとも無し
- 継続提案: Master は2件を再確認（最多 B-035 npm dist-tags・49回目。`2.1.288` は changelog 掲載と `latest` 昇格に追いついた）／ Copilot は B-034（ガイダンスハブ 9/30 改訂を4日遅れで検知）・B-036（MC1454391 の退役時期が二次で割れ一次未確認）・B-037（95日）の回数を更新 ／ industry は3件を更新（最多 B-004・96回目）し、B-008・B-029 に Gemini 4 Argon の4日遅れを追記
- 障害の変化: industry が `9to5google.com` / `www.datacamp.com` / `www.aipricing.guru` / `www.cyberkendra.com` を新規ゲートウェイ拒否として記録した。Master・Copilot は無し
- ソース間の差分・矛盾:
  - Gemini 4 Argon は industry がハイライト1（[料金+予定]）にしていたが、本サマリーが 10/3 に収録済みのため、キャッシュ割引・事前アクセス・ベンチマークの続報だけを [仕様] で残した
  - Claude Code `2.1.288` は Master と industry の両方がハイライトにしていた。`rm` 保護の修正は industry だけが挙げ、`BASHPID` の判定強化は Master だけが挙げていたため、両方を統合した。タグは industry と同じ [セキュリティ+新機能]（Master は [新機能]）
  - Copilot code review の API 対応は Master がハイライト、industry がカテゴリで扱っていた。記載は一致するため Master をベースにした
  - MAI-Transcribe-2-Streaming は industry の「料金・モデル」から Microsoft 節へ移した
