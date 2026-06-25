# AI News Daily Summary — 2026-06-26

> 本サマリーは 01_ai-news-Master・02_ai-news-Copilot・03_ai-news-industry の3ソース（6/26分）を統合して作成。金曜・主要ラボの新規フロンティアモデル発表は引き続きなし。中心は (1) Fable 5 / Mythos 5 停止15日目 — 本日6/26が議会回答期限、初の顧客提訴、交渉団刷新で予測市場の復旧確率が急上昇、(2) Copilot Studio の6月What's New公開（新エージェント体験・Microsoft IQ・Skills・Memory）、(3) OpenAI×Broadcom 初の自社推論チップ「Jalapeño」。

## 今日のハイライト

### 1. Fable 5 / Mythos 5 停止15日目 — 本日6/26が議会回答期限・初の顧客提訴・交渉団刷新で復旧確率が急上昇

**事実**: 6/12 17:21 ET の米輸出規制指令（Commerce/BIS が国家安全保障権限で foreign national への Fable 5 / Mythos 5 アクセス停止を命令）による世界一斉停止は、**6/26 時点で15日目（停止から14日経過）も未復旧**（全顧客で両モデルを無効化し Opus 4.8 へ自動ルーティング継続、他 Claude モデルは影響なし）。本日3つの節目が重なる: (a) **本日6/26 が議会回答期限** — Sam Liccardo ら超党派4議員が Lutnick 商務長官に求めた、輸出管理措置の法的根拠（14 C.F.R. §744.22(b) の "is informed" letter、ERA 2018 権限）・技術評価・復旧/ライセンス基準の文書回答の締切。(b) **初の顧客提訴** — Legion LegalTech が 6/23 にワシントン D.C. 連邦地裁で米政府を提訴、6/12 の BIS 命令が違法に「any foreign national」へのアクセス遮断を強制したと主張し、損害を「即時・回復不能・存続に関わる（existential）」と表現、命令の無効化と差止め（preliminary injunction）を請求（**AIモデルアクセス禁止に対する初の顧客法的挑戦**、Bloomberg）。(c) **交渉団刷新** — Anthropic は Commerce 省との交渉担当を Dario Amodei CEO から **Tom Brown（共同創業者・チーフコンピュート責任者・GPT-3 アーキテクト）**に交代、公共政策責任者 Sarah Heck と共に対応し、政権との協議は「より円滑」と報じられる。これを受け **Polymarket の「来週中の復旧」確率は約15%→60%に急上昇**。ただし商務省の正式な解除命令は依然未発出。

**根拠**: 顧客提訴は Bloomberg（01_Master）、交渉団刷新と予測市場の急騰は 02_Copilot、議会回答期限は 01/02 双方。Anthropic は提訴の当事者ではなく「政権との協働で早期解決に努める」と従来声明を引用。なお予測市場はソース・対象窓で数値に幅があり、Polymarket「6/26 までに US 再開」は **41%（24h で 16pt 低下）**、長期マーカーは「8/31 まで」92%/「12/31 まで」96%（01_Master、累積市場）。ホワイトハウスと Anthropic の「共同リスクフレームワーク」起草は継続中（6/25 既出）。

**影響**: 政治・交渉シグナル（交渉団刷新・フレームワーク起草・予測市場の上振れ）と司法シグナル（初の顧客提訴）が同時進行し、「目前」と「未確定」が併存する状態が続く。顧客提訴は、政府によるAIモデルアクセス遮断の適法性を司法の場に持ち込む先例となり、フレームワーク交渉とは別軸で復旧経路に影響しうる。Fable 5 / Mythos 5 を本番前提にしていた組織にとって復旧時期は依然「未定（ただし上振れ材料あり）」。

**行動指針**: Fable 5 / Mythos 5 を本番に組み込む組織は復旧を「目前の可能性ありだが未確定」と扱い、Opus 4.8 等へのフォールバック前提の運用を継続。本日6/26 の議会回答（Lutnick → Liccardo ら）と、商務省の正式解除命令／anthropic.com/news での明示確認を最優先の確証とし、予測市場の急騰や暗号メディア速報を確定根拠として扱わない。復旧経路の構造マーカーとして **7/8（Anthropic 政府発行 ID 検証ポリシー施行 → US 先行復旧の有力経路）**、**8/1（covered frontier model フレームワークの60日大統領令期限）**を継続ウォッチ。

- https://www.anthropic.com/news/fable-mythos-access

### 2. Microsoft Copilot Studio — 6月What's New公開：新エージェント体験・Microsoft IQ・Skills・Memory

**事実**: 数週間「May 2026 が最新」で静穏だった Copilot Studio の What's New に、ついに **June 2026 セクション**が追加された（02_Copilot の最優先項目）。4本柱: (1) **新エージェント体験（Production-ready Preview）** — 強化されたオーケストレーションランタイムで応答品質・推論を改善、クラシック体験と並行提供、(2) **Microsoft IQ** — 新体験でエージェントを組織データ（メール・予定・ファイル・Teams メッセージ・人物情報）に接続、(3) **Skills** — モジュール化された自己完結型の指示セットを一度作成して複数エージェントで再利用、Markdown/パッケージとしてエクスポート共有可能、(4) **Memory** — ユーザー単位で永続コンテキストを保持し設定・行動パターンを蓄積、対話をまたいでパーソナライズ。既報の Release Wave 計画（6月GA: マルチターン会話評価・脅威保護強化・統合ビュー）と整合し、新体験は Wave 1 の主要施策。

**根拠**: Microsoft Learn の Copilot Studio What's New 一次情報を Microsoft Learn MCP（docs_fetch）経由で確認（02_Copilot）。数週間続いた Microsoft 一次情報の静穏に動きが出た。

**影響**: 「Skills（再利用可能な指示セット）」「Memory（永続コンテキスト）」「Microsoft IQ（組織データ接続）」は、Copilot Studio を単発フローからエージェント協働基盤へ寄せる動き。Claude Code / Cursor 等の skills・subagents 管理と並ぶ業界共通トレンド（再利用・永続化・組織データ接続）として整理できる。

**行動指針**: Copilot Studio を運用する組織は、新エージェント体験を Production-ready Preview としてクラシック体験と並行検証し、Skills のエクスポート/再利用設計と Memory のデータ保持ポリシー（ユーザー単位の永続コンテキストの権限・監査）を事前に詰めてから本番投入を判断する。

- https://learn.microsoft.com/en-us/microsoft-copilot-studio/whats-new

### 3. OpenAI×Broadcom 初の自社推論チップ「Jalapeño」発表 — フロンティアラボのハード内製化が一段と鮮明に

**事実**: OpenAI と Broadcom が、OpenAI 初の推論専用チップ「**Jalapeño**」を発表（6/24、過去ダイジェスト未掲載）。OpenAI 初の「Intelligence Processor」で、LLM 推論専用に設計した reticle サイズの巨大 ASIC。カーネル/メモリ移動/ネットワーク/サービングをフロンティアモデル向けに最適化し、性能/電力効率は現行 SOTA を「大幅に上回る」とする。設計から **tape-out まで9ヶ月**という高性能半導体として異例の短期開発で、**2026年末に初期展開**開始予定。両社が共同で築く複数世代コンピュート基盤の第一歩。

**根拠**: OpenAI 公式（openai.com/index）/ TechCrunch / Tom's Hardware（03_industry）。過去に扱った「Anthropic×Google×Broadcom コンピュート拡張」（6/10）とは別件の OpenAI 独自チップ。

**影響**: OpenAI の「フルスタック内製化」と NVIDIA 一極依存からの分散戦略を象徴。Anthropic（Google TPU / Amazon Trainium）に続き、主要ラボがそろって推論ハードの内製・自社最適化に動く構図が鮮明になり、コンピュート調達・コスト構造の中長期前提が変わりうる。

**行動指針**: 推論コスト・供給を前提に中長期計画を立てる組織は、主要ラボのカスタムシリコン化（OpenAI Jalapeño / Anthropic TPU・Trainium）を「NVIDIA 単一依存リスクの低減」と「ラボ別の価格・可用性の分岐」という二面で監視。2026年末の初期展開時期と、性能/電力効率の実測ベンチマーク公開を確証材料とする。

- https://openai.com/index/openai-broadcom-jalapeno-inference-chip/
- https://techcrunch.com/2026/06/24/openai-unveils-its-first-custom-chip-built-by-broadcom/

## カテゴリ別まとめ

### Anthropic / Claude・規制
- Fable 5 / Mythos 5 停止15日目・議会回答期限6/26・初の顧客提訴（Legion LegalTech）・交渉団刷新（Tom Brown）・予測市場急騰（ハイライト1参照）
- **Claude Tag（Slack 常駐の共有AIチームメイト）**: 6/23 ベータ公開分を 01_Master が改めてキャッチアップ（チャンネル常駐・全員共有・アンビエントモード、Opus 4.8 動作、Team/Enterprise 向け、旧「Claude in Slack」は8/3退役）。本サマリーでは6/25にハイライト済み。https://www.anthropic.com/news/introducing-claude-tag

### Claude / 開発ツール（Claude Code・Cursor・Devin）
- **Claude Code v2.1.191（6/24 stable・最新）**: `/rewind` が `/clear` 実行前からの会話再開に対応、ストリーミング中のスクロール位置ジャンプ修正、**停止後に background agent が復活するバグ修正**、MCP サーバの一時的ネットワークエラーへのリトライ追加（OAuth・headless 対応含む）、**ストリーミング中の CPU 使用を text update coalescing で約37%削減**、長時間セッションの terminal 出力キャッシュによるメモリ増加抑制。https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
- **Cursor / Devin**: 6/25 以降の新規リリースなし。Devin は classic 環境設定の **6/30 廃止**（→ blueprints、7/31 まで read-only 参照可）、Enterprise 向けに秘密情報の組織横断管理・MCP allowlist・ビルドピン留め/ロールバックを追加（既報）

### OpenAI
- **ChatGPT 機能更新**: **Pulse を sunset**（proactive 更新は scheduled tasks へ移行、Pro は14日間継続）、**メモリ削除・無効化 UI**（memory summary から「Delete and turn off memory」）、**GPT-5.5 Instant の会話品質アップデート**（意思決定・助言・計画・比較検討での意図把握と複数ターン文脈保持を強化）、セキュリティ機能 **Active sessions**（不審セッションの確認・サインアウト）。https://help.openai.com/en/articles/6825453-chatgpt-release-notes
- **GPT-5.6: ローンチ予測窓（6/22–28）が崩壊**: Polymarket の同窓オッズは 83%→約18% に低下、**7月ローンチ説が優勢（7月末までに ~94%）**。公式の発表・system card・API モデルページは依然なし。リーク（未確認）: context 1.5M tokens、GPT-5.5 比 10–15% のトークン効率改善
- **OpenAI×Broadcom「Jalapeño」推論チップ**（ハイライト3参照）

### Google / DeepMind
- **Gemini 3.5 Pro は依然 GA 待ち**: 6/26 時点も Vertex AI 限定プレビューのみ（2M context / Deep Think）。Pichai「来月中に届ける」の月内期限まで残り**約4日**、予測市場の「6/30 までの GA」確率は約50〜55%で月内ずれ込みの可能性も残る
- **Google → Anthropic への人材流出が株価に波及（6/24, Bloomberg）**: Gemini 主要貢献者 Jonas Adler・Alexander Pritzel が Anthropic へ移籍見込み。Noam Shazeer（→OpenAI）、John Jumper（AlphaFold、→Anthropic）に続く流出で、**Alphabet 株は一時最大 -7.2%**（2月以来最大の日中下落）。https://www.bloomberg.com/news/articles/2026-06-24/google-poised-to-lose-two-more-high-profile-ai-staffers-to-anthropic

### Microsoft / GitHub
- Copilot Studio 6月 What's New 公開（ハイライト2参照）
- **その他 Microsoft 一次情報は新規なし**: Power Platform ブログ（最新 6/11「June 2026 Feature Update」）、M365 Copilot リリースノート（最新 6/16 バッチ）、Tech Community「What's New in M365 Copilot」（6月号未公開）は変更なし。GitHub Copilot も 6/25 以降の新規リリースなし

### AI 業界トレンド・資金調達（提案根拠用）
- **エンタープライズ向け「実務に効くAI」へ資金集中（6/24）**: Taktile が $110M シリーズC（Goldman Sachs 主導、金融機関向け AI 意思決定）、Assort Health が $120M シリーズC（医療の患者アクセス自動化）。Q1 の記録的調達（AI に VC 全体の約80%＝$242B）の流れを継ぐ
- **市場シェア（Similarweb・2026年4月）**: ChatGPT 54.7%、Gemini 27.4%、Claude 8.2%、DeepSeek 4.1%、Grok 2.8%（変化なし）

## 直近の注目予定

- **6/26（本日）**: 議会（Liccardo ら）への Lutnick 回答期限 / Polymarket「Fable 5 US 復旧」予測対象日（41%）
- **6/27**: GPT-4.5 が ChatGPT から退役
- **6/30**: Devin classic 環境セットアップ廃止 / GPT-5.2・5.3-Codex 新規 API 不可化 / Anthropic サイエンスイベント / Copilot Studio for Teams クラシック作成終了 / 感度ラベル表示 GA / Security Copilot E5 展開完了 / M365 価格ロックイン期限 / Gemini 3.5 Pro GA 予測窓（約50〜55%）
- **7/1**: M365 価格改定発効（E3 $36→$39、E5 $57→$61、Copilot Business $18→$21）/ Cursor 新価格 / Devin Cascade 完全廃止 / Anthropic Claude Partner Network 初回階層昇格レビュー
- **〜7/1（予測・未確定）**: Fable 5 / Mythos 5 の US 顧客向けアクセス復旧（交渉団刷新で Polymarket「来週中」約60%）
- **7/8**: Anthropic 政府発行 ID 検証ポリシー施行（Fable 5 の US 先行復旧経路の最有力候補）
- **7/17**: Claude Corps 第1期応募締切
- **8/1**: covered frontier model フレームワークの60日大統領令期限
- **8/3**: 旧「Claude in Slack」アプリ退役（Claude Tag へ移行）
- **8/5**: Claude Opus 4.1 が Claude API から退役
- **8/26**: OpenAI Assistants API 廃止 / o3 退役 / GPT-4.5 完全廃止
- **9月**: iOS 27 / macOS 27 GA（AFM 3 本番）

## 改善メモ

- **Fable 5 の停止日数カウントがソース間で不一致（継続）**: 01_Master は「15日目」、02_Copilot は「Day 14」。6/12 停止を起点に inclusive（停止日を1日目）で15日目、elapsed（経過日数）で14日。本サマリーは「15日目（停止から14日経過）」と両表記で明記。日数は起算方法の差であり実態の矛盾ではない。
- **予測市場の数値がソース間・対象窓で食い違い**: 02_Copilot は交渉団刷新を受け Polymarket「来週中の復旧」約15%→60%の急騰を強調、01_Master は Polymarket「6/26 までに US 再開」41%（24h で 16pt 低下）と長期マーカー（8/31 まで92%）を記載。市場・対象窓・時点の差と見られ、両論併記とした。確証は商務省の正式解除命令を最優先とする方針を継続。
- **交渉団の主体に関する表現差**: 02_Copilot は「6/26 に Dario → Tom Brown へ交代」と明記、01_Master は「Tom Brown 登板後に協議が好転」（6/25 既出の文脈）。実態は同一の交渉団刷新を指すと判断し統合した。
- **取りこぼし検知（複数ソース）**: 01_Master は Claude Tag（6/23 発表）の前回取りこぼし、03_industry は OpenAI×Broadcom「Jalapeño」チップ（6/24 発表）の6/24・6/25 取りこぼしを報告。ラボの大型ハード発表・新プロダクトは WebSearch の「June 2026」上位に埋もれやすく、各社公式 newsroom（openai.com/index・anthropic.com/news）を定点ソースに追加する推奨が複数ソースで重なった。
- **WebFetch / RSS 403 が全ソースで継続**: 入力3リポとも anthropic.com / github.blog / cursor.com / 各種 RSS（Google News / GIGAZINE / The Decoder / VentureBeat / Publickey / hnrss / Product Hunt / GitHub Trending 等）が 403。WebSearch ＋ raw.githubusercontent.com / Microsoft Learn MCP / 大手メディアでフォールバック。03_industry が `daily-sources.md` の取得方法欄を「WebSearch 優先」へ更新する推奨を複数日継続で「要対応」と記録。
- **入力3リポ側で起動時のローカル main 乖離が連日再発**: 01_Master（4回連続）・03_industry がともに「開始時にローカル main が 06-05 で停滞し origin/main と乖離（merge-base 空／多数コミット）」を報告。各リポで SessionStart hook に `git fetch && git reset --hard origin/<branch>` 相当を導入する恒久対策を強く推奨。
- **本サマリーの入力取得方法に関する注記**: 本セッションでは GitHub MCP・ローカル git とも入力3リポ（01/02/03）へのアクセスが scope 制限・git proxy 403 で不可だったため、`raw.githubusercontent.com` 経由（WebFetch）で当日ダイジェストを取得した。3ソースとも当日分を取得できており欠損なし。
