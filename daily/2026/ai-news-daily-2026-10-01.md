# AI News Daily Summary — 2026-10-01

期限が確定した日である。Anthropic は `claude-sonnet-4-5-20250929` の API 退役日を 11/30 に決め、Google は Gemini の Gems を skills へ置き換えて Business / Enterprise では 2027-03-01 以降に使えなくすると告知した。Microsoft は従量課金の対象を3種から6種に広げ、既存の支出ポリシーが新サービスへ自動で掛かる。Copilot の「エージェント」画面はプラグイン画面に置き換わった。本日 10/1 は OpenAI `gpt-5.4-cyber` の停止日にあたる。

## 今日のハイライト

### 1. [廃止] Anthropic が Claude Sonnet 4.5 の API 退役日を 11/30 に決めた — 「9/29 以降」とだけあった期限が、残り61日の移行締め切りに変わった

**要点**: Anthropic が 9/30 付で `claude-sonnet-4-5-20250929` を deprecated にし、Claude API での退役日を **2026-11-30** とした。退役ページはこれまで下限日しか書いておらず、告知も出ていなかった。移行先の Sonnet 5.5 は破壊的変更を含むので、ID の差し替えだけでは済まない場合がある。

**詳細**:

- 退役ページの行: `claude-sonnet-4-5-20250929` ／ Deprecated ／ 告知 September 30, 2026 ／ 退役 November 30, 2026 ／ 推奨移行先 `claude-sonnet-5-5`。退役日以降のリクエストは失敗する
- 適用範囲: Claude API・Claude Platform on AWS・Microsoft Foundry。Bedrock と Google Cloud は各社が独自に日程を決める
- Sonnet 5.5（9/28 公開）への移行で要る対応: `thinking: {"type": "disabled"}` を `between_tools` に置き換える。`tool_choice` の any / tool は 400 を返す
- ほかに下限日が近いのは Haiku 4.5（10/15 以降）と Opus 4.5（11/24 以降）で、どちらも本日時点で Active のままである

- https://platform.claude.com/docs/en/about-claude/model-deprecations
- https://platform.claude.com/docs/en/release-notes/overview

### 2. [廃止+新機能] Google が Gemini の Gems を skills に置き換えると告知した — Business / Enterprise では 2027-03-01 以降 Gems が使えず、「Ask a Gem」を含む Workspace Studio フローも止まる

**要点**: Google が 9/30、Gemini アプリと Workspace に skills（再利用できるカスタム指示）を入れ、Gems を段階的に廃止すると発表した。skills は SKILL.md 形式なので、Claude など他のツールで書いた skill を持ち込める。Gems で組んだ業務フローは期限までに作り直しが要る。

**詳細**:

- 日程（一次）:
  - 10/5: Workspace で skills の展開開始（11月中旬に完了予定）
  - 10/13: Gemini アプリで skills の展開開始（11月中旬に完了予定）
  - 11/17: Gems が Gemini アプリの設定パネルへ移る（作成・編集・利用は継続）
  - 2027-03-01 以降（Business / Enterprise）: Gems の作成・編集・利用ができなくなり、残った Gems は下書きの skill に自動移行する。「Ask a Gem」ステップを含む Workspace Studio フローは動かなくなる
  - 2027-06-01 以降（Education）: 同様。Classroom と Gemini LTI 対応 LMS からも消える
- 「Ask a Gem」ステップを含む Workspace Studio フローは、すでに新規作成できない（既存は動く）
- skills は1つのプロンプトで複数を重ねて使える。Gemini アプリと Workspace の間では同期しないので、両方で使うなら別々に作る

- https://workspaceupdates.googleblog.com/2026/09/

### 3. [料金] Microsoft 365 の従量課金の対象が3種から6種に増えた — 既存の支出ポリシーは既定で新サービスにも自動で掛かる

**要点**: 管理者が M365 管理センターの Cost management で統制する従量課金サービスに、Teams Phone Agent・SharePoint / OneDrive の Advanced work・Copilot Managed Runtime が加わった。支出ポリシーの Auto-apply new services は既定で有効なので、設定を変えなくても既存ポリシーが追加分に適用される。

**詳細**: 一次は Learn `usage-based-billing-overview-copilot-credits`（`ms.date` **2026-09-30**）である。

- 追加: Advanced work in SharePoint / Advanced work in OneDrive（どちらも Copilot ライセンス必須）・Copilot Managed Runtime・Teams Phone Agent
- 従来から: Cowork・Work IQ API
- Managed Runtime: 構築時の消費は作成した製品側のポリシーに従う。実行時の消費は M365 管理センターで別のポリシーと割り当てを設定できる
- 自動適用を止めたい場合は、ポリシーごとに Auto-apply new services をオフにする。Code は本日もこの一覧に無い

- https://learn.microsoft.com/en-us/microsoft-365/copilot/usage-based-billing-overview-copilot-credits

## カテゴリ別まとめ

### Claude / Anthropic

- **Claude Sonnet 4.5 の退役日確定**（ハイライト参照・1）
- [破壊的変更] **Claude Code 2.1.286** — Anthropic が 9/30 の `2.1.286` で、失敗した API 呼び出しの再送上限を1回のモデル呼び出し単位で数えるようにした。前版で最大21回まで膨らんだ再送は、既定設定で最大14リクエストで止まる。
  - プラグイン: npm ソースが git リポジトリやフォルダーの場合はインストールを拒否し、依存関係もレジストリのパッケージからだけ入れる
  - `--bare`: コマンドラインで指定した MCP サーバーだけに接続し、システムリマインダーもバックグラウンドタスクも送らない
  - 費用メーター: Claude apps gateway が1時間キャッシュ書き込みを5分の単価で計算していた誤りと、サーバー側ツールを使うストリーミングのターンで入力トークンを数え漏らしていた誤りが直り、表示額は増える方向に変わる
  - 既定モデルが API に拒否されたとき、同じ階層の1つ前のモデルで1回だけ再試行する
  - npm は `{stable: 2.1.280, latest: 2.1.286, next: 2.1.286}` で、`stable` が `2.1.277` から前進した
  - https://code.claude.com/docs/en/changelog
- [新機能] **Claude for Government の GA** — Anthropic が 9/30、連邦・州政府機関向けの Claude for Government を GA にした。FedRAMP High 認可環境で動き、7月から公開ベータだった。
  - 課金: 席単位の料金は無く、使用量を固定単位で前払いし上限を超えない。管理者はグループごとに支出上限と使えるモデルを決める
  - 管理: SCIM のグループで席ごとのレート制限・金額上限・許可モデルを設定し、管理操作は監査ログに残る
  - 同じ環境で Claude Code CLI と Claude for Microsoft 365 が early access で使える
  - https://claude.com/blog/claude-for-government-is-now-generally-available
- [セキュリティ] **GLM-5.3 のサイバー能力評価** — Anthropic の Frontier Red Team が 9/29、Zhipu AI のオープンウェイトモデル GLM-5.3 のサイバー攻撃能力の評価を公開した。ExploitBench（Chrome V8）の end-to-end エクスプロイト作成成功率は GLM-5.3 が **12%**、Claude Mythos Preview が14%だった。偽の口実で64%、推論の prefill で92%が悪意ある依頼に応じ、abliteration（約 $4,400）で拒否率は90%超から約3%に下がった。https://www.anthropic.com/research/glm-5-3-and-the-spread-of-advanced-cyber-capabilities
- [動向] **営業チームの Managed Agents 事例** — Anthropic が 9/30、自社の営業チームが Claude Managed Agents でインバウンド対応を作り直した事例を公開した。https://claude.com/blog/how-anthropics-sales-team-rebuilt-inbound-with-claude-managed-agents
- [据え置き] **status とサポート側リリースノート** — `status.claude.com` に 9/29 以降の新しいインシデントは無く、`support.claude.com` のリリースノートは 9/28 の Sonnet 5.5 が最上位のままである。

### OpenAI / Codex / ChatGPT

- [廃止] **`gpt-5.4-cyber` の停止日** — OpenAI の `gpt-5.4-cyber` が本日 10/1 に停止する。9/11 に告知された期日で、移行先は `gpt-5.6-cyber` である。9/30 以降、新たな廃止告知は無い。https://developers.openai.com/api/docs/deprecations
- [仕様] **DevDay 発表の一次掲載** — OpenAI が Developer Community に DevDay の発表一覧を公式に掲載し（9/29）、前日に二次のみとした Pro 500・dots・ChatGPT Space / Pages・Codex Security Cloud・Decisions API が一次で確認できた。
  - Ultrafast: 提供中なのは Astra で、Sol は「近日」
  - Agents API: public beta
  - Amazon Bedrock Managed Agents: OpenAI 系エージェントが AWS 内で動く
  - Sign in with ChatGPT: サブスクリプションの利用枠を16のローンチパートナーで使える
  - https://community.openai.com/t/devday-2026-announcements-and-developer-resources/1402006
- [新機能] **Codex rust-v0.159.1** — OpenAI が Codex `rust-v0.159.1`（9/29）で、同梱カタログと Amazon Bedrock カタログの既定モデルを GPT-6.1 Sol にした。`rust-v0.159.2` は Windows でコンソールが点滅する問題の修正である。https://github.com/openai/codex/releases
- [動向] **$300億の追加調達** — OpenAI が評価額約 **$1.4兆**で $300億以上の調達を目指していると Bloomberg が報じた（9/29）。3月の評価額 $852B から約64%の上昇で、年換算売上は $70B に近い。交渉は初期段階で、アルトマン CEO は年内の IPO を見送る考えを示している。https://www.bloomberg.com/news/articles/2026-09-29/openai-targets-30-billion-in-new-funding-at-1-4-trillion-value
- [据え置き] **API changelog・退役ページ・alignment** — OpenAI の API changelog は 9/29 の GPT-6.1 Sol ほか3件、退役ページは 9/11 の `gpt-5.4-cyber`、`alignment.openai.com` は 9/25 の報告が最上位のままである。

### GitHub Copilot / GitHub

- [新機能] **HydraFusion（research preview）** — GitHub が 9/30、複数モデルを組み合わせる HydraFusion を Copilot CLI に続き VS Code（1.140 以降）と GitHub Copilot アプリでも使えるようにした。タスクごとに Single（1モデル）・Cascade（軽いモデルの下書きを品質ゲートで上位モデルへ）・Critique（別系統モデルが読み取り専用でレビューし1回修正）を選ぶ。対象は Pro / Pro+ / Business / Enterprise で、Business / Enterprise は管理者がプレビュー機能を許可する必要がある。倍率の記載は無い。https://github.blog/changelog/2026-09-30-hydrafusion-in-vs-code-and-the-github-copilot-app
- [破壊的変更] **GHE.com の X25519 単独 TLS 終了（10/7）** — GitHub が 9/30、データレジデンシー付き GitHub Enterprise Cloud が 10/7 から X25519 だけを提示する TLS 接続を受け付けなくなると告知した。X25519 だけに明示設定したプロキシやセキュリティ機器・TLS ライブラリは HTTPS で接続できなくなるため、P-256（`secp256r1`）を有効にする必要がある。SSH は影響を受けない。https://github.blog/changelog/2026-09-30-x25519-only-tls-ends-for-ghe-com-on-september-15
- [新機能] **Advanced Security の Team 向け試用** — GitHub が 9/30、Code Security と Secret Protection のセルフサービス試用を GitHub Team の組織に開放した。組織の Overview・請求画面・リスク評価の完了画面から始められ、試用期間と価格は告知に記載が無い。https://github.blog/changelog/2026-09-30-github-advanced-security-trials-for-github-team
- [版更新] **Copilot CLI の pre-release** — GitHub が Copilot CLI の pre-release を `v1.0.90-7`（9/30 18:17 UTC）まで進め、`-6` でモデル選択に GPT-6.1 Sol が加わった。安定版は `v1.0.89` のままである。https://github.com/github/copilot-cli/releases

### Microsoft 365 Copilot / Copilot Studio / Power Platform

- **従量課金の対象拡大**（ハイライト参照・3）
- [新機能] **プラグインレジストリ** — 利用者は Home（Chat / Cowork）・Code・Autopilot・Word / Excel / PowerPoint・SharePoint で、承認済みプラグインを共通の Plugins メニューから使えるようになった（9/30・展開中）。既存の Agents ページは Plugins ページに置き換わり、配布と統制の単位がエージェント単体からプラグイン（スキル＋コネクタ＋エージェント）に移る。
  - 管理: M365 管理センターの Agent 365 体験で Agents > Tools から、Microsoft・自社開発・パートナーのプラグインを有効化・ブロックし、ユーザーやグループに割り当てる
  - 規模: 公開時点で **100超**（HubSpot / Linear / Atlassian / Asana / Canva / Notion 等）。Copilot Studio・GitHub Copilot・Microsoft Foundry も対象になる予定
  - 開発: Work IQ Developer Tools の `wiqd plugin` で作成・検証・公開する（public preview）。既存の Agent Plugins 形式は `wiqd plugin import` で取り込める。既存の API プラグインは宣言型エージェントのアクションとして引き続きサポートされる
  - https://techcommunity.microsoft.com/blog/microsoft-copilot-blog/introducing-the-plugin-registry---one-place-to-discover-and-govern-plugins-for-m/4559682
  - https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/plugins-overview
- [新機能] **Microsoft Copilot の9月 What's New** — Tech Community の月次記事（9/30）が、9月に展開した機能を挙げた。
  - 権威ソース: 管理者が最大 **100** の SharePoint サイトを Copilot Search / Chat の権威ソースに指定できる
  - PowerPoint のスキル: 管理者が承認済みスキルを特定のユーザー・グループ・全社に配布できる
  - プロンプト内呼び出し: 利用者が `/` でエージェント、`@` でスキルを呼び出せる
  - Teams Phone Agent: 60超の言語で着信に応答し、質問対応・予約・部署への転送を担う
  - https://techcommunity.microsoft.com/t5/microsoft-copilot-blog/what-s-new-in-microsoft-copilot-september-2026/ba-p/4559107
- [新機能] **Cowork の個人アカウント版** — Learn の Cowork 概要（`ms.date` 2026-09-29）が、職場・学校アカウント版は GA、個人アカウント版はプレビューだと書くようになった。https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/
- [仕様] **Copilot Studio のアップロード文書の読み取り範囲** — Learn `code-interpreter-for-prompts`（`ms.date` 2026-09-30）が、エージェントは Word 文書のテキストボックス・図形・SmartArt・ヘッダー / フッター・埋め込みオブジェクト内の文字を読まない場合があると明記した。https://learn.microsoft.com/en-us/microsoft-copilot-studio/code-interpreter-for-prompts
- [予定] **Copilot Studio のスキルカタログ** — Microsoft が Roadmap **571880** で、メーカーが M365 App Store を基盤とする共有カタログから承認済みの組織スキルを探して再利用・共有できるようになると起票した（Preview September・GA October CY2026）。共有スキルは M365 Copilot と Cowork にも広がる。
- [予定] **Work IQ の拡張2件** — Microsoft が Roadmap **570854**（プロンプト作成中に追加のエージェント・スキル・コンテンツソースを選べる ExpandedContextIQ）と **570853**（Work IQ からカスタムエージェントと他社ツールを呼ぶエージェントを起動）を起票した。どちらも Preview October・GA November CY2026 である。
- [予定] **Copilot Studio の9月 GA 期日を超過** — Roadmap の Copilot Studio 起票は571880を含め **23件**で全件 `In development` のままであり、GA 期日が September CY2026 の **14件**は期日を過ぎても1件も `Rolling out` / `Launched` に移っていない。
- [動向] **Frontier Partner スペシャライゼーション** — Microsoft が 9/30 から、適格パートナーが Frontier Partner スペシャライゼーションを取得できるようにした。M365 Copilot・Azure AI Foundry・GitHub Copilot・Defender・Entra・Purview にまたがるエージェントの設計から統制までを認定し、特典に Agent P3 クレジットと M365 E7 ライセンスを含む。https://learn.microsoft.com/en-us/partner-center/announcements/2026-september
- [観測] **Learn の改訂差分が特定できないページ** — Copilot Studio の MCP ツールページ8本・`admin-agent-inventory`・`harnesses-overview`・評価3本と、Power Platform の `capacity-storage`（`ms.date` 2026-09-30）が 9/30 に更新されたが、改訂差分は特定できていない。`capacity-storage` は、Dataverse search を Off から Default に戻すと索引が再生成されコストが再開する旨を書いている。
- [据え置き] **Release Notes・What's New・Power Platform の定点** — M365 Copilot Release Notes の先頭は **September 23, 2026** のままで、Copilot Studio What's New は July 2026 節のまま GitHub Copilot ハーネスの GA（8/3）を59日反映していない。Power Platform のブログ・Release Wave・Released Versions（Copilot Studio 最新ビルド 2026.6.3）も動いていない。https://learn.microsoft.com/en-us/copilot/microsoft-365/release-notes

### Google

- **Gems から skills への移行**（ハイライト参照・2）
- [据え置き] **Gemini API changelog** — Google の Gemini API changelog は 9/22 の 3.8 Flash TTS GA が最上位のままである。https://ai.google.dev/gemini-api/docs/changelog

### Cursor / Devin / xAI / オープンウェイト

- [据え置き] **Cursor の新モデル告知** — Cursor の changelog は 9/23、フォーラム Announcements は 9/21 の Grok 4.7 が最上位のままで、Opus 5.5・GPT-6 Sol / Luna・Sonnet 5.5・GPT-6.1 Sol の提供開始告知は無い。
- [観測] **xAI・Devin の一次** — xAI と Devin に 9/29〜30 付の新規は検出していない。
- [据え置き] **MCP・Hugging Face・Apple** — `blog.modelcontextprotocol.io` は 8/22、`developer.apple.com/news/` は 9/18 が最上位のままで、Hugging Face の登録8 org にも新規リポジトリは無い。

### 規制・政策 / 市場

- [動向] **ホワイトハウスの自主的 AI 安全協定** — OpenAI・Google・Meta・Anthropic・Nvidia・xAI が 9/29、ホワイトハウスで自主的な AI 安全協定に署名した。1ページの文書で、社内統制を整え、外部監査人に有効性を評価させ、取締役会に報告を審査する委員会を置く内容である。監査人は各社が選び、罰則も実施期限も無い。https://www.forbes.com/sites/saradorn/2026/09/29/white-house-releases-accord-between-billionaire-ai-execs-heres-what-it-says/
- [据え置き] **市場データ** — IDC Japan・MM総研・NRC・Similarweb はいずれも新規公表が無く、MM総研の2026年版個人利用率調査もまだ見つかっていない。

## 直近の注目予定

- **10/1（本日）**: OpenAI `gpt-5.4-cyber` が停止（移行先 `gpt-5.6-cyber`） ／ Copilot 既存顧客の前払い必須化 ／ CSP 成長マージンの取引開始 ／ Microsoft CSP ソフトウェア価格改定が発効 ／ ChatGPT for Word の Word アクセスが既定オンへ
- **10/2**: GitHub Copilot が4モデルを廃止 ／ Gemini の `gemini-2.5-flash-image` が停止
- **10/5**: Gemini の `antigravity-preview-05-2026` が停止 ／ Workspace で skills の展開開始 ／ GPT-Rosalind の課金開始
- **10/7**: GHE.com が X25519 単独の TLS 接続を拒否
- **10/13**: Gemini アプリで skills の展開開始 ／ Office / Project / Visio LTSC 2021 のサポート終了 ／ 新しい Copilot の Partner Digital Airlift
- **10/14**: GitHub SSH の新規 RSA 鍵が 3072 ビット以上必須に ／ GPT-5.5 が ChatGPT / Codex から退役
- **10/15 以降**: `claude-haiku-4-5-20251001` の暫定退役日
- **10月**: Copilot Studio エージェントがコスト管理の対象に ／ スキルカタログ GA（571880） ／ Word・Cowork の Legal plugins GA（571884） ／ OneDrive の Prompt Gallery（571308） ／ Work IQ 拡張2件の Preview（570853・570854）
- **10/19**: GitHub Copilot が5モデルを廃止
- **10/21**: GitHub Copilot の新機能既定ポリシーの設定期限（10/22 発効）
- **10/23**: OpenAI のレガシースナップショット12件が停止
- **10/27〜29**: PPCC 2026（ラスベガス）
- **10/29**: ChatGPT Pro 200 の現行枠の最終日（二次）
- **10/30**: ChatGPT Pro 200 の Work / Codex 利用枠が半減（二次）
- **10/31**: MCP サーバー認定の旧申請経路が終了 ／ OpenAI Evals が読み取り専用化
- **11月**: Copilot Studio の Maker guidelines（570967）GA ／ Purview 自動ラベル付け上限の引き上げ（571309） ／ Work IQ 拡張2件の GA
- **11/2**: GitHub Actions の `pull_request_target` 既定無効化が公開リポジトリで強制開始 ／ M365 Copilot Business の従量課金が既定オン
- **11/4**: GitHub SSH `ssh-rsa` の1回目のブラウンアウト
- **11/12**: OpenAI → Cursor のモデル供給停止予定（一次未読）
- **11/15**: Microsoft Release Planner 退役
- **11/17**: Gems が Gemini アプリの設定パネルへ移動
- **11/17〜20**: Microsoft Ignite
- **11/21**: OpenAI GPT-5.6 Sol の期間限定価格の下限
- **11/24 以降**: Claude Opus 4.5 の暫定退役日
- **11/30**: `claude-sonnet-4-5-20250929` が Claude API から退役 ／ OpenAI の `v1/prompts`・Evals・Agent Builder が停止
- **12/1**: OpenAI `gpt-image-1-mini` / `gpt-image-1.5` / `chatgpt-image-latest` が停止
- **12/9**: GitHub SSH `ssh-rsa` の2回目のブラウンアウト
- **12/11**: OpenAI GPT-5 / o3 系スナップショットが停止
- **12/31**: 非営利向け M365 Copilot の併用プロモーション終了 ／ Gemini 3.8 Flash の導入価格が終了 ／ Pro 200 既存契約者の $2,500 クレジットが失効（二次）
- **2027-03-01 以降**: Gems 廃止（Business / Enterprise）
- **2027-06-01 以降**: Gems 廃止（Education）

## 改善メモ

- 新規提案: 3ソースとも無し
- 継続提案: Master は2件を再確認（最多 B-035 npm dist-tags・46回目）／ Copilot は B-037・B-061（9/29 の Roadmap バッチを1日遅れで検知）・B-074・B-077 の回数を更新 ／ industry は継続分のみ
- 障害の変化: 3ソースとも無し
- ソース間の差分・矛盾:
  - Claude Code `2.1.286` について、Master（04:10 頃生成）は「npm に出たが changelog 未掲載で中身不明」、industry（05:10 頃生成）は changelog の記載で再送上限などを報じた。前日の `2.1.285` と同じく、Master の生成時点では未掲載だったと判断し industry の記載を採った
  - GHE.com の X25519 告知は、URL の slug が `on-september-15`、記事タイトルと本文が October 7 である。本サマリー生成時に一次で本文の「Beginning October 7, 2026」を確認したため 10/7 と記載し、URL は原文のまま残した
  - OpenAI の調達報道は、Master が Bloomberg ニュースレター（9/30）、industry が Bloomberg 記事（9/29）を出典にしている。内容は一致するため1件に統合した
  - タグ: industry の非定義語を11語へ直した（`[資金調達]`・`[政策]` → 動向、`[期限]` の X25519 → 破壊的変更、`[破壊的変更+修正]` の 2.1.286 → 破壊的変更）。Copilot の Roadmap 9月 GA 期日（観測）は既知の期日の超過が主旨のため予定とした。Copilot の Qiita の別筆者記事（本文未読）は採録しなかった
- 手順の不整合（前日から継続）: `scripts/check-update-tags.py` は「ハイライト参照」を含む行だけを検査対象外にするため、本日も `（ハイライト参照・N）` の形で参照行を置いた
