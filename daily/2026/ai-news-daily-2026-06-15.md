# AI News Daily Summary — 2026-06-15

> 本サマリーは 01_ai-news-Master・02_ai-news-Copilot・03_ai-news-industry の3ソース（6/15分）を統合して作成。日曜〜月曜の端境で一次ニュースは少なめ。本日は「予告済みスケジュールの当日施行（Anthropic 課金転換）」と「G7サミット開幕」が中心。

## 今日のハイライト

### 1. 【本日 6/15 施行】Anthropic 課金構造の転換点 — Sonnet 4 / Opus 4 退役 + Programmatic Credit Pool

**事実**: 本日 6/15、Claude API から `claude-sonnet-4-20250514` / `claude-opus-4-20250514`（旧 Sonnet 4 / Opus 4）が退役。旧 ID を直接指定しているコードは本日以降エラーとなり、Sonnet 4.6 / Opus 4.6〜4.8 + Fable 5 への移行が必須となる。同時に Programmatic Credit Pool が施行され、Agent SDK / `claude -p` / Claude Code GitHub Actions / SDK 認証のサードパーティアプリが通常サブスク枠から分離された。

**根拠**: Anthropic のリリース告知に基づく確定スケジュール。プログラム利用にはプラン料金連動の月次ドルクレジット（Pro ≈$20 / Max 5x ≈$100 / Max 20x ≈$200、API 標準レート）が付与され、従来の「実質無制限」サブスク補助を置換。クレジット枯渇後はオーバーフロー課金を手動有効化しない限り自動リクエストが停止（フォールバック・繰越なし）。対話利用（チャット、ターミナルの Claude Code）は影響を受けない。

**影響**: CI / cron / agent ループで Claude Code を回しているチームは、これまで interactive 価格で流せていた自動化が credit 消費 → API 課金に変わる。月次クレジット枠の監視と、重い自動化ワークロードのコスト再見積もりが必要。Fable 5 試食終了（6/22-23、※停止中につき実質保留）と合わせ、6月後半は credit 消費前倒し設計が連続しており、IPO 前の収益体質シグナルとも読める。

**行動指針**: 旧モデル（Sonnet 4 / Opus 4）を直接指定している API クライアント・スクリプトを本日中に棚卸しし、新モデルへ差し替える。自動化ワークフローはクレジット枠の消費状況を可視化し、枠枯渇時の停止挙動（自動リクエスト停止）を踏まえてオーバーフロー課金の要否を判断、月次予算へ credit 消費を織り込むこと。

- https://codersera.com/blog/anthropic-june-2026-billing-change-claude-code/
- https://enterprisedna.co/resources/news/anthropic-claude-june-15-retirements-billing-2026/
- https://releasebot.io/updates/anthropic/claude

### 2. G7サミット（フランス・エビアン）が本日開幕 — AI主権をめぐり同盟国間に亀裂

**事実**: 6/15-17 開催。OpenAI の Sam Altman、Google DeepMind の Demis Hassabis、Anthropic の Dario Amodei の3社トップが出席する初の G7。水曜の政財界ワーキングランチで AI インフラ・ネットワーク・規制が議題となる。

**根拠**: OpenAI の Chris Lehane 氏は「自主的コミットメントのパッケージ」合意で退席する見込みと表明し、Altman の最優先は若年層の安全と説明。一方、報道は米欧間で「AI主権（sovereignty）」をめぐる対立が拡大していると指摘し、共同歩調の難しさを示唆している。

**影響**: フロンティアAIの規制・安全枠組みが主要国間でどこまで収斂するかの試金石。3社が先週連名で合成DNA・AI生物リスクの規制強化を米議会に求めた書簡の流れと連動し、自主規制 vs 国家による輸出管理（Fable 5 停止の文脈）という緊張が表面化している。

**行動指針**: 規制・輸出管理の方向性は単一モデル供給の安定性に直結する。サミットの合意内容（自主コミットメントの範囲、主権をめぐる米欧の分岐）を 6/17 閉幕まで注視し、フロンティアモデル依存の運用は供給途絶リスクを織り込んでおくこと。

- https://www.techpolicy.press/g7-summit-set-to-kick-off-amidst-allies-widening-rift-over-ai-sovereignty/
- https://thenextweb.com/news/g7-ai-summit-altman-amodei-hassabis

### 3. 【明日 6/16 GA】Microsoft Work IQ API — agent の M365 アクセスが Copilot Credits 従量課金に統一

**事実**: 6/16 に Work IQ API が GA。agent が M365 データ（メール / カレンダー / 会議 / チャット / ファイル / 人物 / 業務システム）にアクセスする公式手段として、A2A + 再設計された remote MCP server + REST API の3エンドポイントを提供する。

**根拠**: 専用 SKU / per-user ライセンスはなく、Copilot Credits（Copilot Studio 等と共通の消費通貨）で従量課金。query 系（grounding / retrieval / reasoning）の変動分 + actions/tools 起動の固定分の2部構成。GA 前に管理者が consumptive billing を有効化し、Admin Center で支払方法・アクセス・上限/アラートを設定する必要がある。

**影響**: Anthropic の Programmatic Credit Pool（6/15）と1日違いで、主要2プロバイダの「自動化 / programmatic 利用＝専用クレジット従量課金」標準化が同週に揃う。エンタープライズの agent 運用は、ユーザーライセンス前提のコスト計算から「消費通貨」前提へ移行が求められる。

**行動指針**: M365 agent を運用 / 計画している組織は、GA 前に管理者側で consumptive billing と上限・アラートを設定。Copilot Credits の消費見積もりを query 量 + action 起動回数の2軸で立て、Anthropic 側のクレジット枠と合わせて「自動化の従量課金」を月次予算に統合すること。

- https://devblogs.microsoft.com/microsoft365dev/work-iq-production-ready-intelligence-for-every-agent/
- https://learn.microsoft.com/en-us/partner-center/announcements/2026-june

## カテゴリ別まとめ

### Anthropic / Claude
- **6/15 Claude API で Sonnet 4 / Opus 4 退役 + Programmatic Credit Pool / Agent SDK 課金分離 施行**（ハイライト参照）
- **Fable 5 / Mythos 5 停止（6/12〜）は 6/15 時点で復旧なし** — 米商務省 BIS 指示によるアクセス停止が継続。Anthropic は「誤解と考えており早期復旧に取り組む」との 6/12 声明から進展の公表なし。Opus 4.8 / GPT-5.5 へのフォールバック運用を引き続き前提とすること。6/22 の Fable 5 無料期間終了は停止中につき実質保留 https://www.anthropic.com/news/claude-fable-5-mythos-5
- 6/15 付の Anthropic blog / Claude release notes の新規エントリは未確認。Claude Corps（応募 7/17 締切）、30日 retention は変化なし
- **ソース間の提供状態の食い違い**: 01_Master は Fable 5 を 6/22 無料期間終了・6/23 credits 必要化として稼働中スケジュールに記載、02_Copilot は 6/12 停止継続と報道。本サマリーは両論併記（改善メモ参照）

### Claude Code
- **v2.1.176（6/12 stable）が最新**。6/13-15 の新規 stable リリースは未確認。v2.1.175 `enforceAvailableModels` + v2.1.176 抜け穴修正で managed model allowlist 強制が完成した状態が継続。Fable 提供は 6/12 停止のまま無効
- 02_Copilot は v2.1.176 として「セッションタイトルを会話言語で生成、Opus 4.8 非対応組織向け Auto モードのフォールバック調整」を挙げる https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md

### OpenAI
- ChatGPT release notes / OpenAI news に 6/15 付の新規エントリなし。直近は Codex の ChatGPT 統合ロールアウト（6/2 発表、「数週間以内」）+ 6業界別プラグイン + Computer Use on Windows
- Codex CLI changelog（developers.openai.com/codex/changelog）は 403 継続。GitHub Releases 側で `0.140.0-alpha` 系（Extensions Unification / Multi-Agent v2 / Python SDK）が進行中、stable 着地は未確認
- 6/27 GPT-4.5（ChatGPT）退役 / 6/30 GPT-5.2・GPT-5.3-Codex 新規 API リクエスト不可化が直近の確定スケジュール

### Google / DeepMind
- **Gemini 3.5 Pro GA は依然未着地** — I/O 2026（5/19）で公約した6月内 GA は本日時点で未発表。市場推定は最終週（6/22-26、予測市場は 6/23・6/30 前後を注視）。2M tokens context / Deep Think / frontier multimodal、価格は Flash の約10倍（$15/$60 ／100万トークン前後）見込み。公開済みは Gemini 3.5 Flash（5/19）のみ
- **6/15 から Google × Kaggle「AI Agents Intensive」無償5日間コース開始（〜6/19）** — foundational concepts → production-ready agent、vibe coding 重視 https://blog.google/innovation-and-ai/technology/developers-tools/kaggle-genai-intensive-course-vibe-coding-june-2026/
- 6/18 に Gemini CLI / Gemini Code Assist IDE 拡張の consumer 提供終了（Antigravity CLI 移行）まで3日

### Microsoft / GitHub
- **Work IQ API が 6/16 GA**（ハイライト参照）
- **Copilot in SharePoint がオプトアウトプレビューへ（6月中旬ロールアウト開始）** — オプトインからオプトアウトへ移行。M365 Copilot ライセンス保有者にはサイト/ページ/ライブラリ/リスト/チャット全体で AI 機能が自動表示（テナント/サイト単位でオプトアウト可）。意図せぬ露出を避けたい組織は事前のガバナンス確認が必要 https://m365admin.handsontek.net/copilot-sharepoint-will-start-rolling-tenants-opt-preview-starting-mid-june-2026/
- 公式定例ソース（M365 Copilot Release Notes は 6/2 が最新で次回 6/16 頃、Copilot Studio What's New 6月セクション未公開、Power Platform Blog は 6/11 以降なし）は前日から新規なし

### Cursor / Devin / xAI / Mistral
- **Cursor**: 6/15 付の新規 changelog なし。Bugbot 大型更新（~90秒 / 3x 高速 / 90% が3分以内）+ `/review` コマンド（6/10 頃）+ Design Mode 視覚プロンプト（6/5）が直近
- **Devin**: v3 API GA（6/5、v1/v2 は将来 deprecate）以降の公式新規なし。Cascade EOL 7/1 / classic environment setup 廃止 6/30
- **xAI**: **Grok V9-Medium（1.5T params、Cursor coding data 訓練、Tesla / X 配信予定）の「mid-June 公開」は本日時点で未着地**。訓練完了は 6/5、RL/fine-tuning 段階の報道。Grok 5 とは別物
- **Mistral**: Vibe の Slack 連携 Code Mode 6月中提供、Mistral Medium 3.5（dense 128B / 256k）が default

### 業界動向
- **「自動化＝従量課金」の標準化が同週に集中** — Anthropic Programmatic Credit Pool（6/15）+ Microsoft Work IQ の Copilot Credits 課金（6/16）が1日違いで、主要2プロバイダが agent / programmatic 利用を専用クレジット消費へ寄せる方向で揃う
- **frontier 新モデルの「6月内 GA」公約が軒並み最終週へ後ろ倒し** — Gemini 3.5 Pro（最終週推定）/ Grok V9-Medium（mid-June 未着地）。発表ラッシュは6月最終週に集中の見込み

### 市場データ（前回から変化なし）
- **Similarweb AIトラッカー（2026年4月）**: ChatGPT 54.7%、Gemini 27.4%、Claude 8.2%（四半期306%増）、DeepSeek 4.1%、Grok 2.8%
- **MM総研（2025年8月調査）**: 生成AI個人利用率21.8%、市場規模2024年度1,679億円→2030年度5,618億円予測

## 直近の注目予定

- **6/15（本日）**: Anthropic Programmatic Credit Pool / Agent SDK 課金分離 施行 / Claude API で Sonnet 4 / Opus 4 退役 / Google × Kaggle「AI Agents Intensive」開始 / G7サミット開幕
- **6/15-17**: G7サミット（フランス・エビアン）— AI3社トップ出席
- **6/15-19**: Google × Kaggle「AI Agents Intensive」無償5日間コース
- **6/16**: Microsoft Work IQ API GA（A2A + remote MCP + REST、Copilot Credits 課金）/ M365 Copilot Release Notes 次回更新見込み
- **6/18**: Gemini CLI / Gemini Code Assist IDE 拡張の consumer 提供終了（Antigravity CLI 移行）
- **6/22**: Fable 5 が Pro/Max/Team/Enterprise の追加料金なし期間終了（※停止中のため実質保留）
- **6/22-26**: Gemini 3.5 Pro GA 推定ウィンドウ（最終週ドロップ予想）
- **6/23**: Fable 5 利用に usage credits 必要化
- **6/25**: gemini-3.1-flash-image-preview / gemini-3-pro-image-preview 廃止
- **6/27**: GPT-4.5 が ChatGPT から退役
- **6/30**: Devin クラシック環境セットアップ廃止 / GPT-5.2・GPT-5.3-Codex 新規 API リクエスト不可化 / Copilot Studio Teams クラシック作成廃止・感度ラベルGA / Security Copilot E5 展開完了 / M365 価格ロックイン期限
- **6月中旬**: Grok V9-Medium 公開予定（未着地）
- **7/1**: M365価格改定発効 / Cursor 新価格 / Anthropic Claude Partner Network 初回階層昇格レビュー / Devin Cascade 完全廃止
- **7/17**: Claude Corps 第1期応募締切
- **7/31**: Devin classic machine configuration 読取専用参照終了
- **8/5**: Claude Opus 4.1 が Claude API から退役
- **8/26**: OpenAI Assistants API 廃止 / o3 退役
- **9月**: iOS 27・iPadOS 27・macOS 27 Golden Gate GA（Apple Intelligence Extensions + AFM 3 本番ローンチ）
- **10月**: Claude Corps 第1期 100名フェロー配置開始
- **12/1**: 旧 GPT Image モデル API 廃止
- **Q4 2026**: Azure Agent Mesh GA 目標

## 改善メモ

- **ソース間の矛盾（要注視・継続）**: 01_Master は Fable 5 を稼働中扱い（6/22 無料期間終了・6/23 credits 必要化をスケジュールに記載）だが、02_Copilot は 6/12 の米政府 BIS 指示による全世界停止が 6/15 時点で継続中と報道。01 が停止ニュースを反映していない可能性が高い。本サマリーは両論併記とし、6/16 以降の各ソースで Fable 5 の提供状態を再確認すること
- **Fable 5 / Mythos 5 の復旧は流動的** — 02_Copilot メモより、翌日以降も「Anthropic / Claude」「規制・輸出管理」キーワードの WebSearch を定例巡回と別枠で優先実行すること
- **「予告済みスケジュール期日の当日」は最重要セクション化が有効**（01_Master メモ）— 6/15 のように予告だけだった期日が施行日になると、それ自体が当日の最大ニュース。`注目予定` の当日項目をハイライトへ昇格させる運用が機能した
- **週初・週末は changelog 系のみ実質有効** — 6/15 は各社公式に当日付エントリなし。releasebot.io / 集約系（codersera 等）が日次更新の代替として有用。OpenAI Codex CLI changelog 403 継続（5回目）で GitHub Releases を fallback として `daily-sources.md` に正式反映を推奨
- **各種 RSS / WebFetch 403 継続**: 03_industry は全RSS/WebFetch（Google News、GIGAZINE、The Decoder、VentureBeat、Publickey、hnrss.org、Product Hunt、GitHub Trending、TechPolicy.press）が引き続き403で WebSearch フォールバック対応。02_Copilot も `anthropic.com/news`・`mc.merill.net` の WebFetch 403 継続のため固有 MC 番号の網羅は手動確認推奨
