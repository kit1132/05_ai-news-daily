# AI News Daily Summary — 2026-06-16

> 本サマリーは 01_ai-news-Master・02_ai-news-Copilot・03_ai-news-industry の3ソース（6/16分）を統合して作成。

## 今日のハイライト

### 1. Microsoft Work IQ API が本日 6/16 GA — Copilot クレジット従量課金、専用SKU/ライセンス不要

**事実**: 予定通り **Work IQ API が本日 6/16 に GA**（メッセージ RM559020）。提供は **A2A / 再設計された remote MCP server / REST API** の3エンドポイントで、エージェントが M365 の業務コンテキスト（メール・カレンダー・会議・チャット・ファイル・組織関係・基幹システム）に直接アクセスできる標準経路となる。

**根拠**: Microsoft 公式 devblogs およびライセンスニュースに基づく確定 GA。課金は **Copilot Credits の従量制**（Copilot Studio 等と共通通貨）で、**専用サブスク・SKU・per-user ライセンスは不要**。Admin Center に billing setup・spend policy・usage limit・monitoring の新コスト管理が追加される。

**影響**: 自社エージェントへ M365 コンテキストを統合するハードルが大きく下がる。一方で課金が Copilot Credits 消費に一本化されるため、エージェントの稼働量がそのままクレジット消費＝コストに直結する。Foundry / Copilot Studio で agent を量産している組織はクレジット予算の設計が必須となる。

**行動指針**: M365 連携エージェントを検討中の組織は、Work IQ API（A2A / MCP / REST）を第一候補として PoC を開始してよい。ただし per-user ライセンスではなく従量課金なので、Admin Center の spend policy / usage limit を初期段階で必ず設定し、想定クレジット消費を月次予算に織り込むこと。

- https://devblogs.microsoft.com/microsoft365dev/work-iq-production-ready-intelligence-for-every-agent/
- https://www.microsoft.com/en-us/licensing/news/work-iq-general-availability
- https://www.microsoft.com/en-us/microsoft-365/blog/2026/06/02/announcing-the-new-work-iq-apis/

### 2. Fable 5 / Mythos 5 の世界停止が継続 — 6/16 時点も未復旧、市場は「7/1 までに US 顧客向け復旧」を本命視

**事実**: 6/12 の米政府輸出規制指令による Fable 5 / Mythos 5 の全世界停止は、**6/15-16 時点でも復旧の公表なし・復旧日未定**のまま継続。Anthropic 技術スタッフは White House とのオンライン協議を継続しており、現在は新規クエリを **Opus 4.8 へ自動ルーティング**している。他の Claude モデルは影響なし。

**根拠**: 政府は Fable 5 の jailbreak 手法を懸念と説明。Anthropic は「これは Mythos の cyber 能力を1ケースのみ解放する narrow なもので、全 safeguard を破る universal なものではない。誤解だ」と反論。市場/予測は **7/1 までに US 顧客向け復旧**を本命視するが、具体日程は未提示。

**影響**: Claude Code の auto / Fable 5 利用は当面 Opus 4.8 へフォールバック。6/22 の試食期間終了・6/23 のクレジット消費移行といった既定スケジュールは、停止中のため実質的に日程要再確認の状態が続く。政府指示による供給停止が1週間近く解消しない事例として、単一モデル依存リスクが改めて顕在化している。

**行動指針**: Fable 5 / Mythos 5 を本番に組み込んでいた組織は、復旧時期を未定と見なし Opus 4.8 / GPT-5.5 でのフォールバック前提で運用を継続すること。復旧・条件付き再開・課金スケジュールの再調整について翌日以降も継続フォローが必要。

- https://www.anthropic.com/news/fable-mythos-access
- https://www.cnbc.com/2026/06/12/anthropic-disables-access-to-fable-5-and-mythos-5-to-comply-with-government-directive.html
- https://simonwillison.net/2026/Jun/13/us-government-directive-to-suspend-access/

### 3. Jeff Bezos の Prometheus が 120億ドル調達 / 評価額410億ドル — 「物理AI」への大型資金流入

**事実**: Jeff Bezos の AI スタートアップ **Prometheus が120億ドルを調達、評価額410億ドル**（6/11）。「物理AI（physical AI）」を掲げ、ジェットエンジンから創薬まで設計〜製造の全パイプラインを end-to-end の AI 問題として扱う。テキスト生成ではなく実物の設計・製造支援が狙い。

**根拠**: 共同CEOは Vik Bajaj（Verily 共同創業者）。投資家に JPMorgan / BlackRock / Goldman Sachs / DST Global / Arch Venture 等。昨年の62億ドルと合わせ累計180億ドル超。Amazon / Blue Origin とは資本関係なし。

**影響**: フロンティアLLM以外の AI 投資が大型化している兆候。同日には DeepSeek が Ramp の「トレンドソフトウェアベンダー」で首位（米企業が安価なAIを直接利用）という報も出ており、(a) 物理・産業ドメインへの巨額投資と (b) コモディティ化したテキストLLMの価格競争、という二極化が同時進行している。

**行動指針**: LLM中心のAI戦略を立てる組織も、設計・製造・創薬など物理ドメインのAI化が資本面で本格化している事実を中期ロードマップに織り込むこと。直近の調達・買収動向の追跡対象に加える価値がある。

- https://techcrunch.com/2026/06/11/jeff-bezoss-prometheus-raises-12b-to-build-an-artificial-general-engineer-for-the-physical-world/
- https://www.axios.com/2026/06/11/prometheus-bezos-industrial-ai

## カテゴリ別まとめ

### Anthropic / Claude
- **Fable 5 / Mythos 5 の世界停止が継続、6/16 時点も未復旧**（ハイライト参照）。市場は ~7/1 までの US 顧客向け復旧を本命視
- **Agent SDK 課金分離（6/15発効）への開発者反応は否定的** — コミュニティは「プログラム利用の実質値上げ」と受け止め。Anthropic の Lydia Hallie 氏の X 投稿は数時間で Community Note 付き。背景は「$20 Pro でも $500 相当の API ワークロードを回せた」compute 裁定取引の終了で、今年3度目の構造的経済問題への対処。クレジット枯渇後はオーバーフロー課金を手動有効化しない限り自動リクエストは停止 https://thenewstack.io/anthropic-agent-sdk-credits/
- **$150M「Claude Corps」フェローシップ開始（6/11-12）** — 早期キャリア人材1,000人を週5時間のAI研修付きで全米の非営利団体に12カ月フルタイム配置。給与$85,000＋$10,000グラント＋Claudeトークン予算。第1コホート100名は応募締切7/17・開始10月、以降2027年1月・8月コホート https://www.anthropic.com/news/claude-corps

### Claude Code
- **新規リリースなし** — v2.1.176（6/12 stable）が最新のまま。6/13-16 の新規 stable リリースは確認されず（WebFetch 安定確認済み）

### OpenAI / ChatGPT
- **ChatGPT 新機能（memory 制御・web 画像検索・model picker 簡素化）** — Memory summary ページから個別 memory 削除＋「Delete and turn off memory」で memory 完全 OFF が可能に（全ユーザー web、mobile 展開中）。Web search が text と並んで画像結果も返却。Model picker を Instant / Medium / High / Pro-only に簡素化（Plus/Pro の web/iOS/Android）。既報通り 6/12 で GPT-5.2 は ChatGPT から退役、既存会話は GPT-5.5 系に自動継続 https://help.openai.com/en/articles/6825453-chatgpt-release-notes
- **OpenAI が Anthropic に料金で対抗検討** — Sam Altman が「利用コストは企業にとって大きな問題」と認め、エンタープライズ顧客を Anthropic から取り戻すためトークン価格引き下げを検討中と報道。背景に Anthropic の $965B 評価・年率 $47B 超ランレート。あわせて Partner Network（$150M投資）と Codex のビジネスプラグイン6種を投入、ChatGPT は月間アクティブ10億人突破と報じられる https://the-decoder.com/

### Microsoft / GitHub
- **Work IQ API 本日 6/16 GA**（ハイライト参照）
- M365 Copilot Release Notes は 6/2 が最新のまま（次バッチは 6/16-18 前後見込み）

### Google / DeepMind
- **Gemini 3.5 Pro は依然 limited preview** — I/O（5/19）発表の 2M context・Deep Think は「6月内 GA 目標」も確定出荷日なし
- 6/18 に Gemini CLI / Gemini Code Assist IDE 拡張のサービス終了（Antigravity CLI 移行）

### Cursor / Devin / xAI
- **Cursor**: Bugbot 90秒レビュー / `/review`（Bugbot + Security 同時）/ 増分 review・Enterprise Organizations GA から新規進展なし
- **Devin**: Desktop 正式ローンチ / v3 API GA / Devin Review から新規進展なし。Fable 5 / Mythos 5 依存部は Opus 4.8 / GPT-5.5 で継続稼働
- **xAI**: Grok V9-Medium の「6月中旬公開」は本日時点で未着地

### 市場・競争
- **DeepSeek が Ramp「トレンドソフトウェアベンダー」で首位（6月）** — 米企業が安価なAIを求め DeepSeek へ直接データを送る有償利用が増加。エンタープライズのコスト最適化志向と安価モデルへのシフトを示す市場シグナル https://the-decoder.com/deepseek-topped-ramps-trending-software-vendors-in-june-2026-as-us-companies-chase-cheaper-ai/

### 規制・政策
- **G7サミット（フランス・エビアン、6/15-17）2日目** — 初日に続き AI 主権・共有ルール（透明性・倫理・データプライバシー・安全）が議題。OpenAI / DeepMind / Anthropic トップが出席。具体的な合意文書は会期末（6/17）にかけて公表見込みで、現時点で確定的な成果報道は未インデックス https://www.consilium.europa.eu/en/meetings/international-summit/2026/06/15-17/

### 市場データ（前回から変化なし）
- **Similarweb AIトラッカー（2026年4月）**: ChatGPT 54.7%、Gemini 27.4%、Claude 8.2%（四半期306%増）、DeepSeek 4.1%、Grok 2.8%
- **MM総研（2025年8月調査）**: 生成AI個人利用率21.8%、市場規模2024年度1,679億円→2030年度5,618億円予測

## 直近の注目予定

- **6/16（本日）**: Microsoft Work IQ API GA
- **6/15-17**: G7サミット（フランス・エビアン）— AI3社トップ出席（本日2日目）
- **6/18**: Gemini CLI / Gemini Code Assist IDE 拡張のサービス終了（Antigravity CLI 移行）
- **6/22**: Fable 5 が Pro/Max/Team/Enterprise の追加料金なし期間終了（※停止中のため実質保留）
- **6/22-26**: Gemini 3.5 Pro GA 推定ウィンドウ（最終週ドロップ予想・未確定）
- **6/23**: Fable 5 利用に usage credits 必要化（※停止中のため実質保留）
- **6/25**: gemini-3.1-flash-image-preview / gemini-3-pro-image-preview 廃止
- **6/27**: GPT-4.5 が ChatGPT から退役
- **6/30**: Devin クラシック環境セットアップ廃止 / GPT-5.2・GPT-5.3-Codex 新規 API リクエスト不可化 / Copilot Studio Teams クラシック作成終了・感度ラベルGA / Security Copilot E5 展開完了 / M365 価格ロックイン期限
- **〜7/1（予測）**: Fable 5 / Mythos 5 の US 顧客向けアクセス復旧（市場本命・未確定）
- **7/1**: M365価格改定発効（E3 $36→$39、E5 $57→$61、Copilot Business $18→$21）/ Cursor 新価格 / Devin Cascade 完全廃止
- **6月中旬**: Grok V9-Medium 公開予定（未着地）
- **7/17**: Claude Corps 第1期応募締切
- **8/5**: Claude Opus 4.1 が Claude API から退役
- **8/26**: OpenAI Assistants API 廃止 / o3 退役

## 改善メモ

- **Fable 5 / Mythos 5 停止は複数ソースで報じられているが復旧情報が流動的** — 「~7/1 までに US 顧客向け復旧」は市場予測（Polymarket 等）であり Anthropic 公式の確定日程ではない点に注意。01/02 とも当日復旧なしで一致。復旧・条件付き再開・課金スケジュールの再調整は翌日以降も継続フォロー
- **速報性の高い規制・モデル提供イベントは別枠巡回を** — 01_Master メモより、Fable 5 / Mythos 5 世界停止（6/12発生）が 6/15 の `.last-check-state.md` に未記載だった取りこぼしを記録。輸出規制・モデル提供停止系は Anthropic 公式＋大手メディア（CNBC/Fortune/Al Jazeera）を毎日クロスチェック推奨
- **03_industry のローカルクローン停滞問題が再発** — 起動時のローカル main が 06-05 で停滞し origin/main（06-15）と乖離。06-15 メモでも同事象。常態化しているため起動時の `git pull origin main` を含む環境セットアップ見直しを強く推奨
- **各種 RSS / WebFetch 403 継続** — 03_industry は全RSS（Google News、GIGAZINE、The Decoder、VentureBeat、Publickey、hnrss.org、Product Hunt、GitHub Trending）が403で WebSearch フォールバック。Anthropic Blog 公式（anthropic.com/news/*）/ mc.merill.net / cursor.com / github.blog の WebFetch 403 も継続。releasebot.io を日次更新の代替集約源として `daily-sources.md` に正式反映を推奨
- **本日は新規一次情報が少なめ** — 実質的な当日新規は Work IQ API GA とChatGPT機能更新が中心で、他は既報の続報＋大型ディール2件（Prometheus・Claude Corps）のキャッチアップ。03 のメモより Bezos Prometheus（6/11）と Claude Corps（6/11-12）は 06-11〜06-15 で未掲載だったため本日収録
