# AI News Daily Summary — 2026-06-28

> 本サマリーは 01_ai-news-Master・02_ai-news-Copilot・03_ai-news-industry の3ソース（6/28分）を統合して作成。

本日の主題は、**6/26 に米政府が Anthropic「Mythos 5」を約100の信頼組織へ限定再開**したこと。3ソースとも前日（6/27）ダイジェストでこの動きを取りこぼしており、本日まとめて初反映。OpenAI の GPT-5.6 段階出荷と合わせ、フロンティアモデルが「政府承認制（managed-release）」へ移行する構図が二大ラボで同時進行している。

## 今日のハイライト

### 1. 米政府、Mythos 5 を約100組織へ限定再開 — 2週間のブラックアウトに初の風穴

**事実** — 6/26（金）、Lutnick 商務長官が Anthropic 宛て書簡で、Mythos 5 を米国内の約100組織（多数のフォーチュン500企業＋連邦政府機関、サイバー防御の中核含む）へ限定再開することを許可した。6/12 の輸出規制指令による全世界停止からちょうど2週間での部分解除。書簡付属の組織リストは非公開。

**根拠** — Lutnick は「Anthropic が導入したガードレールに自信がある」と表明し、信頼できるユーザーへの提供を認めた。NBC / CNBC / The Hill / CNN など複数の一次報道で確認。

**影響** — **Fable 5 は今回の許可に含まれず、依然として全世界でオフライン**（選択時は「Claude Fable 5 is currently unavailable」表示が継続）。Anthropic と政権は Fable 5 復旧に向け協議継続中だが時期は不透明。一般・国外向けの全面復旧は未達で、7/8 の政府ID検証ポリシー発効が一般再開の最有力経路と見られる。

**行動指針** — 自社が約100組織に含まれるか書面で確認できない場合は Mythos 5 を本番依存にしない。Fable 5 利用前提のワークフローは Opus 4.8 等への自動ルーティングを当面の既定とし、輸出規制案件は公式声明を待たず大手メディアの一次報道を当日中に拾う運用へ。

出典:
- https://www.nbcnews.com/tech/tech-news/us-government-gives-anthropic-green-light-limited-re-release-mythos-5-rcna352018
- https://www.cnbc.com/2026/06/26/us-government-anthropic-claude-mythos5-ai.html
- https://thehill.com/policy/technology/5943549-anthropic-mythos-5-access/
- https://www.anthropic.com/news/fable-mythos-access

### 2. OpenAI GPT-5.6 をプレビュー、一般提供目前 — 政府承認制が二社で定着

**事実** — 6/26、OpenAI が GPT-5.6 ファミリー（Sol＝フラッグシップ / Terra＝低コスト / Luna＝最速最安）を、政府要請に沿って信頼できる Codex / API パートナー（〜20社、政府審査済み）へ限定プレビュー。System Card も公開。予測市場 Polymarket は 6/28 の一般提供（GA）を約83%で織り込み。

**根拠** — Lutnick が Altman に「政府承認前の一般公開をしないよう」警告したと報じられ、ONCD / OSTP / Commerce が顧客単位でアクセスを承認。Mythos 5 許可はこの GPT-5.6 発表の数時間後で、Anthropic と同型の「banhammer」が適用された形。

**影響** — frontier モデルの政府事前審査が Anthropic・OpenAI の二社で前例化。現行確定世代は GPT-5.5、GPT-4.5 は 6/27 に ChatGPT 退役予定。先端AI調達が政策リスクに直結する局面に入った。

**行動指針** — GPT-5.6 採用検討中の組織は、自社が政府審査済みパートナー枠に入るかをまず確認。GA 時期は数週間内〜6/28 GA 観測まで幅があるため、移行計画は GPT-5.5 を当面の安定基盤として組む。

出典:
- https://www.axios.com/2026/06/25/trump-administration-openai-gpt-model-release
- https://openai.com/index/previewing-gpt-5-6-sol/
- https://www.tomshardware.com/tech-industry/artificial-intelligence/openais-chatgpt-5-6-gets-the-same-banhammer-treatment-as-anthropics-mythos-from-the-federal-government-source-says-that-washington-cautioned-openai-against-releasing-the-model-without-receiving-approval

### 3. Devin / Cognition、v3 API が GA 化＋MCP マーケットプレイス大幅拡張

**事実** — Cognition が Devin の v3 API を beta から卒業させメイン API 化（RBAC・セッション帰属対応）。MCP コネクタを48種以上追加（Miro、Mixpanel、Honeycomb、Postman、monday.com、Klaviyo 等）し、beta だった42 MCP を GA 化。computer use による Linux デスクトップアプリの E2E テストにも対応。

**根拠** — Devin Docs（release-notes/2026）および Cognition Blog で確認。Google Drive MCP は全ユーザーへ開放、Enterprise 管理者向けに MCP 利用状況ページを追加。

**影響** — エージェント型開発ツールの企業導入で、コネクタ網羅性とガバナンス（RBAC・利用可視化）が競争軸として強化。classic 環境設定は 6/30 に廃止される点に注意。

**行動指針** — Devin を評価中のチームは、6/30 の classic 廃止前に v3 API ベースの環境へ移行。必要 MCP コネクタが新規48種に含まれるか棚卸しし、管理者は MCP 利用状況ページで利用統制を設計する。

出典:
- https://docs.devin.ai/release-notes/2026
- https://cognition.com/blog

## カテゴリ別まとめ

### Anthropic / Claude
- Mythos 5 限定再開・Fable 5 凍結継続（ハイライト参照）
- 経緯整理: 6/9 公開 → 6/12 17:21 ET に BIS 輸出規制指令で全世界停止 → Opus 4.8 へ自動ルーティング。発端は Amazon 研究者による Mythos safeguard 突破報告（Fortune 6/14）。顧客提訴も継続（Legion LegalTech、6/23、D.C. 連邦地裁）

### Claude Code
- **v2.1.195（6/26）が最新** — ハイフン入り識別子の hook matcher を部分一致→完全一致に修正（`code-reviewer`、`mcp__brave-search` 等）、`CLAUDE_CODE_DISABLE_MOUSE_CLICKS`（フルスクリーンのクリック/ドラッグ/ホバー無効化、ホイールスクロールは維持）、**スペース無し言語（日本語・中国語・タイ語）の音声入力 auto-submit 不発を修正**、background job のデータ消失・クラッシュ後の空白画面・background agent デーモン不達を修正、プロジェクトレベル設定のプラグイン同意要件・`/plugin` 有効化を修正
- https://code.claude.com/docs/en/changelog

### OpenAI
- GPT-5.6 ファミリー プレビュー／GA 目前（ハイライト参照）
- 既報: GPT-4.5 が 6/27 ChatGPT 退役（予定通り）。現行確定世代は GPT-5.5

### Google / DeepMind
- **Gemini 3.5 Pro は 7 月延期が定着** — コーディング・トークン効率・長タスク性能の改善のため 6 月→7 月へ延期（未公式）。3.5 Flash は提供済み、3.5 Pro は内部テスト＋限定 Enterprise preview（Vertex AI、200万トークン・Deep Think）のみ。Pichai I/O 発言の月内（6/30）期限まで残り約2日、予測市場の月内 GA 確率は約50〜55%
- https://cryptobriefing.com/google-delays-gemini-35-pro-launch-to-july-2026/

### Microsoft / GitHub / Copilot
- **新規一次情報なし** — Copilot Studio What's New（最新6/26の6月更新: 新エージェント体験・Microsoft IQ・Skills・Memory）、Power Platform ブログ（最新6/11）、M365 Copilot リリースノート（最新6/16バッチ）はいずれも変更なし。GitHub Copilot も 6/26 以降の新規リリースなし

### Cursor / 開発ツール
- 既報の安定運用が継続: Automations（6/18）、Customize ページ（6/22、プラグイン/スキル/MCP/subagent 管理＋マーケットプレイス）、SDK アップデート（6/4）、Bugbot ~90秒レビュー（6/10）。本日（週末）新規なし
- Devin / Cognition v3 API GA・MCP 拡張（ハイライト参照）

### 市場・その他
- **市場シェア（Similarweb・2026年4月時点、変化なし）**: ChatGPT 54.7%、Gemini 27.4%、Claude 8.2%、DeepSeek 4.1%、Grok 2.8%
- **保留**: 「Anthropic がアリババを2,880万件の不正交換（distillation 攻撃）で告発」は WebSearch 上で言及増も一次情報未確認のため引き続き不採用

## 直近の注目予定

- **6/30**: Devin classic setup 廃止 / GPT-5.2・5.3-Codex 新規 API 不可化 / Anthropic サイエンスイベント / Copilot Studio for Teams クラシック作成終了・感度ラベル表示 GA / M365 価格ロックイン期限 / Gemini 3.5 Pro 月内公開期限（7月延期報道優勢）
- **7/1**: M365 価格改定発効（E3 $36→$39、E5 $57→$61、Copilot Business $18→$21）/ Cursor 新価格 / Devin Cascade 削除
- **7/8**: Anthropic 政府発行 ID・生体情報検証ポリシー施行（Fable 5 一般再開の最有力経路）
- **〜7月上旬**: Fable 5 US 復旧交渉 / GPT-5.6 一般提供（数週間内）/ Claude Partner Network 初回昇格レビュー
- **7月中旬**: GPT-5.6・Gemini 3.5 Pro・Claude Opus 4.7 のローンチ集中報道
- **7/17**: Claude Corps 第1期応募締切
- **8/1**: covered frontier model フレームワーク 60日 EO 期限
- **8/3**: 旧「Claude in Slack」アプリ退役
- **8/5**: Opus 4.1 Claude API 退役
- **8/26**: OpenAI Assistants API 廃止 / o3 退役 / GPT-4.5 完全廃止
- **9月**: iOS 27 / macOS 27 GA（AFM 3 本番）

## 改善メモ

- **3ソース共通の取りこぼし検知**: Mythos 5 の約100組織への限定再開（6/26 Lutnick 書簡）と GPT-5.6 プレビュー（6/26）を、3ソースとも 6/27 ダイジェストで反映できておらず本日まとめて反映。輸出規制・モデル提供停止系は「公式声明待ち」で止めず、大手メディア（NBC/CNBC/CNN/The Hill）の一次報道を当日中に拾う運用を全ソースで徹底する。
- **政府による frontier モデル出荷ゲート**（Anthropic Mythos / OpenAI GPT-5.6）は新カテゴリとして継続追跡が必要。`anthropic.com/news` と政府/主要紙（CNBC/The Hill）を規制トピックの定点ソースに追加推奨。OpenAI 側の段階出荷状況も daily-sources の OpenAI 枠でクロスチェック対象に。
- **取得方法**: 全ソースで RSS / WebFetch の 403 が継続（nbcnews.com / thehill.com / mlq.ai / anthropic.com / explainx.ai 等）。WebSearch フォールバックで全件対応中。`daily-sources.md` の取得方法欄を「WebSearch 優先」へ更新する提案が複数回記録済み（要対応）。
- **03_ai-news-industry 側の環境課題**: 起動時にローカルクローンが古い `main` で停滞する問題が 06-15 以降ほぼ毎回継続（要対応）。`git fetch && git reset --hard origin/main` 相当を実行する SessionStart フックの導入を推奨。
- **矛盾の注記**: GPT-5.6 の GA 時期について、Master/Copilot は「数週間内」、industry は Polymarket が「6/28 GA を約83%で織り込み」と前倒し観測。幅があるため移行計画では保守的に「数週間内」を採用。
