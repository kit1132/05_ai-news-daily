# AI News Daily Summary — 2026-06-14

> 本サマリーは 01_ai-news-Master・02_ai-news-Copilot・03_ai-news-industry の3ソース（6/14分）を統合して作成。

## 今日のハイライト

### 1. Claude Fable 5 / Mythos 5 が全世界で停止 — 米政府指示でAnthropicが即時無効化

**事実**: 6/12、米商務省（BIS、Lutnick長官名）が国家安全保障・輸出管理を理由に「外国籍ユーザーへの Fable 5 / Mythos 5 アクセス停止」を要求。Anthropic は外国籍をリアルタイムに識別・除外できないため、有料エンタープライズ・自社従業員を含む全ユーザー向けに両モデルを全世界で停止した。公開からわずか3日での最上位モデル無効化となる。

**根拠**: 6/12 17:21 ET 着の指示書に基づく対応。進行中の Fable 5 / Mythos 5 セッションはエラー終了し、新規クエリは Opus 4.8 など下位モデルへ自動ルーティング。Opus 4.8 / Sonnet / Haiku は影響なし。Anthropic は「これは誤解だと考えており、可能な限り早期のアクセス復旧に取り組む」と表明し顧客に謝罪。背景に Fable 5 のジェイルブレイクによるコード脆弱性解析手法への懸念が報じられるが、指示書は具体的な懸念を明示せず。

**影響**: M365 Copilot / GitHub Copilot / Foundry / Devin / Claude Code など Anthropic 最新モデルに依存する全レイヤーに波及。Devin は 6/12 に Fable 5 を製品から削除（Opus 4.8 / GPT-5.5 は継続）、Claude Code は `/model fable` が利用不可に。なお 01_Master は Fable 5 を引き続き「6/22 に追加料金なし期間終了」と扱っており、両ソースで提供状態の記述が食い違う（改善メモ参照）。

**行動指針**: Fable 5 / Mythos 5 を本番ワークフローに組み込んでいた組織は、当面 Opus 4.8 / GPT-5.5 へのフォールバックを前提に運用すること。復旧時期は未定で「誤解の解消次第」と流動的。政府指示で一夜にしてモデル供給が止まるリスクが顕在化したため、単一モデル依存を避けフォールバック先を事前定義しておくこと。

- https://www.anthropic.com/news/claude-fable-5-mythos-5
- https://www.cnbc.com/2026/06/12/anthropic-disables-access-to-fable-5-and-mythos-5-to-comply-with-government-directive.html
- https://venturebeat.com/technology/anthropic-blocks-all-public-access-to-claude-fable-5-mythos-5-following-us-government-order-what-enterprises-should-do

### 2. 【明日 6/15 施行】Claude API で Sonnet 4 / Opus 4 退役 + Programmatic Credit Pool — 課金体系が変わる

**事実**: 6/15、Claude API から Claude Sonnet 4 / Claude Opus 4 が退役（残り1日）。同時に Programmatic Credit Pool が施行され、subscription プランでの Claude のプログラム利用（Claude Code 自動化・agent 系ツール）が別建ての月次 credit pool へ移行する。

**根拠**: Anthropic のリリース告知に基づく確定スケジュール。Agent SDK 課金分離はオプトインが必要と報じられている。

**影響**: Opus 4.6 / 4.7 / 4.8 + Fable 5 への移行が未完の場合、本日中に確認が必要。Claude Code を CI / 自動化で回しているチームは課金体系の変化に直撃する。Fable 5 試食終了（6/22-23）と合わせ、6月後半は Anthropic の credit 消費前倒し設計が連続しており、IPO 前の収益体質シグナルとも読める。

**行動指針**: 旧モデル（Sonnet 4 / Opus 4）を直接指定している API クライアント・スクリプトを今日中に棚卸しし、新モデルへ差し替える。自動化ワークフローは Programmatic Credit Pool への移行とオプトイン要否を確認し、月次予算へ credit 消費を織り込むこと。

- https://releasebot.io/updates/anthropic/claude
- https://devtoolpicks.com/blog/anthropic-splits-claude-subscriptions-agent-sdk-credit-june-2026

### 3. Moonshot AI、Kimi K2.7-Code をオープンソース公開 — 1Tパラメータの自律型コーディングモデル

**事実**: 6/12 公開。1兆パラメータの MoE（アクティブ32B、384エキスパート）、256K コンテキスト。Modified MIT ライセンスで Hugging Face 公開＋自社 API で提供。

**根拠**: 前世代 K2.6 比で推論トークン消費を約30%削減しつつ、Kimi Code Bench v2 で +21.8%、Program Bench +11.0%、MLS Bench Lite +31.5% を主張。ただし VentureBeat は実務家から「ベンチマークが実利用と乖離」との指摘があると報道しており、定量値は割り引いて評価が必要。

**影響**: 中国勢のオープンウェイト攻勢が継続し、Claude Code / Codex のエンタープライズ防衛に価格・自己ホスト面で揺さぶり。Fable 5 停止でクローズドモデル供給の不安定さが露呈した直後だけに、自己ホスト可能なオープンウェイトの選択肢としての注目度は相対的に高まる。

**行動指針**: コーディング用途の二次候補・フォールバックとして Kimi K2.7-Code を評価対象に加える価値がある。ただしベンチ値は鵜呑みにせず、自社の実コードベースでのリアルタスク評価を前提とすること。

- https://www.marktechpost.com/2026/06/12/moonshot-ai-releases-kimi-k2-7-code-a-coding-model-reporting-21-8-on-kimi-code-bench-v2-over-k2-6/
- https://venturebeat.com/technology/kimi-k2-7-code-cuts-thinking-tokens-30-practitioners-say-benchmarks-dont-check-out

## カテゴリ別まとめ

### Anthropic / Claude
- **Fable 5 / Mythos 5 全世界停止**（ハイライト参照）
- **6/15 Claude API で Sonnet 4 / Opus 4 退役 + Programmatic Credit Pool 施行**（ハイライト参照）
- Claude Corps（$150M / 1,000 fellows、応募 7/17 締切）、30日 retention 公式根拠ページは変化なし

### Claude Code
- **v2.1.176（6/12 stable）リリース** — `availableModels` 強制の抜け穴修正（alias model 経由で環境変数からブロック済みモデルへリダイレクトする問題を塞ぐ）、Opus 4.8 を持たない組織で auto mode が Fable 5 で失敗する問題の修正、session title をセッション言語で生成、`footerLinksRegexes` 設定追加、Bedrock credential caching 改善。Fable 5 GA（6/9）から v2.1.170→176 と6連続 stable release の最終分。なお Fable 5 停止により `/model fable` 関連機能は実質無効化 https://code.claude.com/docs/en/changelog
- v2.1.175 の `enforceAvailableModels`（managed model ガバナンス）と合わせ、enterprise の model allowlist 運用をツール側で確実に強制する基盤が2リリースで完成

### OpenAI
- ChatGPT release notes / OpenAI news に 6/14 付の新規エントリなし。直近は Codex の ChatGPT 統合ロールアウト（6/2 発表）、Codex Sites、Computer Use on Windows
- 6/27 GPT-4.5（ChatGPT）退役 / 6/30 GPT-5.2・GPT-5.3-Codex 新規 API リクエスト不可化が直近の確定スケジュール

### Google / DeepMind
- **Gemini 3.5 Pro GA は依然未着地** — I/O 2026 で公約した6月内 GA は未発表。市場推定は 6/22-26（最終週ドロップ、Polymarket / Manifold）
- 6/18 に Gemini CLI / Gemini Code Assist IDE 拡張の consumer 提供終了（Antigravity CLI 移行）
- 6/15-19 Google × Kaggle「AI Agents Intensive」無償5日間コースが明日開始

### Microsoft / GitHub
- 外部顧客は Foundry・GitHub Copilot 経由で Fable 5 を利用できていたが今回の停止で不可。Microsoft は社内では既に Fable 5 を遮断済み（データ保持ポリシーを法務がレビュー中）。Foundry 提携・Copilot Cowork 等の協業自体は継続 https://winbuzzer.com/2026/05/15/microsoft-starts-canceling-claude-code-licenses-xcxwbn/
- M365 Copilot Release Notes は 6/2 が最新のまま（次回 6/16 頃見込み）。Copilot Studio What's New 6月セクションも未公開で変化なし

### Cursor / Devin / xAI / Mistral
- **Cursor**: 6/14 付の新規 changelog なし。Bugbot 大型更新（~90秒 / 22% cheaper / Composer 2.5 駆動）+ `/review` コマンド（6/10 頃）が直近
- **Devin**: Fable 5 を 6/12 に製品から削除（Opus 4.8 / GPT-5.5 は継続）。v3 API GA（6/5）以降の公式新規なし。Cascade EOL（7/1）継続
- **xAI**: Grok V9-Medium（1.5T params、Blackwell GPU 訓練、Cursor workflow post-training）の「mid-June 公開」は本日時点で未着地
- **Mistral**: Vibe の Slack 連携 Code Mode 6月中提供、Mistral Medium 3.5（dense 128B / 256k）が default。$3.5B 調達/$23B 評価・物理AI用途の続報は大きな進展なし

### 規制・政策
- **G7サミット（フランス・エビアン、6/15-17）にAI3社トップ出席** — OpenAI の Sam Altman、Google DeepMind の Demis Hassabis、Anthropic の Dario Amodei が出席。各社が「自主的コミットメントのパッケージ」に合意して退席する見込み（OpenAI Chris Lehane 氏）。若年層の安全、フロンティアのサイバー・生物リスクが重点議題。3社が先週連名で合成DNA・AI生物リスクの規制強化を米議会に求めた書簡と連動 https://www.bloomberg.com/news/articles/2026-06-12/anthropic-openai-google-executives-plan-to-attend-g7-summit

### 市場データ（前回から変化なし）
- **Similarweb AIトラッカー（2026年4月）**: ChatGPT 54.7%、Gemini 27.4%、Claude 8.2%（四半期306%増）、DeepSeek 4.1%、Grok 2.8%
- **MM総研（2025年8月調査）**: 生成AI個人利用率21.8%、市場規模2024年度1,679億円→2030年度5,618億円予測

## 直近の注目予定

- **6/15**: Anthropic Programmatic Credit Pool 施行 / Claude API で Sonnet 4 / Opus 4 退役 / Agent SDK 課金分離（オプトイン必要）
- **6/15-17**: G7サミット（フランス・エビアン）— AI3社トップ出席
- **6/15-19**: Google × Kaggle「AI Agents Intensive」無償5日間コース
- **6/16**: Microsoft Work IQ API GA
- **6/18**: Gemini CLI / Gemini Code Assist IDE 拡張の consumer 提供終了（Antigravity CLI 移行）
- **6/22**: Fable 5 が Pro/Max/Team/Enterprise の追加料金なし期間終了（※停止中のため実質保留）
- **6/22-26**: Gemini 3.5 Pro GA 推定ウィンドウ（最終週ドロップ予想）
- **6/23**: Fable 5 利用に usage credits 必要化
- **6/25**: gemini-3.1-flash-image-preview / gemini-3-pro-image-preview 廃止
- **6/27**: GPT-4.5 が ChatGPT から退役
- **6/30**: Devin クラシック環境セットアップ廃止 / GPT-5.2・GPT-5.3-Codex 新規 API リクエスト不可化 / Copilot Studio Teams クラシック作成廃止・感度ラベルGA / M365 価格ロックイン期限
- **6月中旬**: Grok V9-Medium 公開予定（未着地）
- **7/1**: M365価格改定発効 / Cursor 新価格 / Anthropic Claude Partner Network 初回階層昇格レビュー / Devin Cascade 完全廃止
- **7/17**: Claude Corps 第1期応募締切
- **8/5**: Claude Opus 4.1 が Claude API から退役
- **8/26**: OpenAI Assistants API 廃止 / o3 退役
- **9月**: iOS 27・iPadOS 27・macOS 27 Golden Gate GA
- **Q4 2026**: Azure Agent Mesh GA 目標

## 改善メモ

- **ソース間の矛盾（要注視）**: 01_Master は Fable 5 を稼働中扱い（6/22 追加料金なし期間終了・6/23 credits 必要化を継続スケジュールに記載）だが、02_Copilot は 6/12 に米政府指示で Fable 5 / Mythos 5 が全世界停止と報道。01 が当日の停止ニュースを取りこぼした可能性が高い。本サマリーは両論併記とし、6/15 以降の各ソースで Fable 5 の提供状態を再確認すること
- **速報性の高い規制・モデル提供イベントは別枠巡回を**: 02_Copilot メモより、前日（6/13）は本停止ニュースを取りこぼし。定例ソース巡回と別枠で「Anthropic/Claude」「規制」キーワードの WebSearch を優先実行することを推奨
- **Fable 5 / Mythos 5 停止は極めて流動的** — 復旧・条件付き再開・Anthropic の法的対応について翌日以降も継続フォロー
- **週末は changelog 系のみ実質有効**（01_Master メモ）— 6/14 は Claude Code Changelog で v2.1.176 を取得できたのが唯一の新規。週末は Claude Code Changelog + GitHub Releases を軸に
- **各種 RSS / WebFetch 403 継続**: 03_industry は全RSSフィード（Google News、GIGAZINE、The Decoder、VentureBeat 等）が403で WebSearch フォールバック対応。OpenAI Codex CLI changelog 403 継続（4回目）。releasebot.io を日次更新の代替フォールバック集約源として `daily-sources.md` に正式反映を推奨
