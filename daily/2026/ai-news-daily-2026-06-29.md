# AI News Daily Summary — 2026-06-29

> 本サマリーは 01_ai-news-Master・02_ai-news-Copilot・03_ai-news-industry の3ソース（6/29分）を統合して作成。

月曜。新規ニュースは少なめの静かな1日。本日の二大テーマは、**(1) Anthropic Fable 5 の輸出規制停止（18〜19日目）に「今週中復旧」観測**が出たこと、**(2) OpenAI GPT-5.6 の 6/28 一般提供（GA）が予測市場の約83%織り込みに反して見送られ**、政府承認制下のフロンティアモデルが GA スケジュールの不確実性を露呈したこと。明日 **6/30 は廃止・GA期限・予測期限が集中する節目**で、Anthropic サイエンスイベントや Gemini 3.5 Pro「月内公開」期限が控える。

## 今日のハイライト

### 1. Anthropic Fable 5、「今週中復旧」観測 — 2週間超のブラックアウトに出口の兆し

**事実** — Axios（6/27）が、トランプ政権が Fable 5 の全面復旧を「早ければ今週（6/29 の週）にも」認める方向だと関係者の話として報じた。6/26 の Mythos 5 限定再開（Annex A、約100組織）に続く次段階として Fable 5 解禁が視野に入る。ただし正式な日付・条件は未確定で、6/12 の輸出規制指令による罰則措置は依然有効。本日時点で Fable 5 は引き続き全世界オフライン（選択時は「Claude Fable 5 is currently unavailable」表示が継続し Opus 4.8 へ自動ルーティング）。

**根拠** — Axios 報道が一次。経緯は 6/9 公開 → 6/12 17:21 ET に BIS 輸出規制指令で全世界停止 → 6/26 Lutnick 書面で Mythos 5 を約100組織へ限定再開。発端は Amazon 研究者による Mythos safeguard 突破報告（Fortune 6/13）。顧客提訴も継続中（Legion LegalTech、6/23、D.C. 連邦地裁）。

**影響** — Fable 5 復旧は2週間超ぶりの一般再開の最有力経路となるが、観測段階で確定ではない。**明日 6/30 の Anthropic サイエンスイベント**で復旧や次の方針への公式言及があるかが直近の焦点。次の制度的節目は 7/8 の政府ID・生体情報検証ポリシー発効。

**行動指針** — Fable 5 前提のワークフローは Opus 4.8 等への自動ルーティングを当面の既定として維持。復旧は「今週中」観測どまりのため本番依存の前倒しは避け、6/30 イベントと公式声明を当日中に確認する運用を継続。輸出規制系は公式＋大手メディア＋予測市場の毎日クロスチェックを推奨。

出典:
- https://www.axios.com/2026/06/27/anthropic-fable-5-return-soon
- https://www.cnn.com/2026/06/26/tech/anthropic-mythos-release
- https://www.anthropic.com/news/claude-fable-5-mythos-5
- https://explainx.ai/blog/when-will-fable-5-be-available-again-2026

### 2. OpenAI GPT-5.6、6/28 GA見送り — 政府承認制が GA 予測の不確実性を露呈

**事実** — 6/26 にプレビューされた GPT-5.6 3モデル構成（Sol＝フラッグシップ / Terra＝低コスト / Luna＝最速最安）は、6/29 時点でも**米政府の事前承認を受けた約20組織への限定プレビュー（API＋Codex 経由）にとどまる**。一般 ChatGPT には未搭載で個人は利用不可。前日 Polymarket が Codex バックエンドログ追跡を根拠に「6/28 GA」を約83%で織り込んでいたが**実現せず**、GA は限定プレビュー開始（6/26）の2〜3週間後＝**7/10-17 頃が最有力**との観測へ修正。

**根拠** — 6/2 の大統領令（先端モデルの事前評価プロセス）下で出荷される初の主要モデルとして、政府承認制（managed-release）の運用実態が GA スケジュールの不確実性に直結。Sol は新「max reasoning effort」と複数 subagent で複雑タスクを加速する「ultra mode」を搭載し、ExploitBench で Mythos Preview と競合する性能を出力トークン約1/3で達成と主張。API 価格は Sol $5/$30、Terra $2.5/$15、Luna $1/$6（入力/出力・100万トークンあたり）。

**影響** — フロンティアモデルの GA 時期は予測市場の数字より遅れる傾向が確認された。Anthropic Mythos / OpenAI GPT-5.6 と、政府承認制が二大ラボで並走。現行確定世代は GPT-5.5、GPT-4.5 は 6/26 に ChatGPT 退役済み。

**行動指針** — GPT-5.6 採用検討中の組織は自社が政府審査済みパートナー枠に入るか確認し、移行計画は GPT-5.5 を当面の安定基盤として組む。GA 時期は予測市場を鵜呑みにせず「政府協議の進捗」を一次変数として保守的に見る。

出典:
- https://openai.com/index/previewing-gpt-5-6-sol/
- https://venturebeat.com/technology/openai-unveils-gpt-5-6-sol-terra-and-luna-models-but-only-accessible-to-limited-preview-partners-for-now-per-us-gov
- https://www.axios.com/2026/06/26/openai-gpt-sol-terra-luna-trump

### 3. Copilot Studio 2026.6.2 — エージェントID周りに破壊的変更、本日唯一の新規一次リリース

**事実** — Microsoft が Copilot Studio 基盤ビルド **2026.6.2** を公開（[2026.5.5（6/9）](./ai-news-daily-2026-06-28.md) に続く更新）。エージェントアイデンティティ移行が安全な再バインドのため新IDをプロビジョニング可能になった一方、**顧客指定のエージェントID識別子は受け付けなくなった**（破壊的変更）。

**根拠** — Microsoft Learn のリリースバージョン公式ページに記載。あわせて、ストリーミング応答が切断後に `Last-Event-Id` ヘッダーで欠落イベントをリプレイ可能に、エージェント単位での AI プロンプト同意カード必須化、Maker Evaluation のテストセット別サマリ返却、共有への共有権限必須化・Information Barriers 準拠の公開/共有ブロックなどセキュリティ強化を追加。

**影響** — 既存の独自エージェントID運用がある組織は再バインド前の確認が必須。明日 6/30 の Copilot Studio for Teams クラシック作成終了・感度ラベル表示GA とあわせ、組織導入観点で影響が大きい。

**行動指針** — 独自IDを使っているエージェントの移行手順を 2026.6.2 の仕様にあわせて見直す。6/30 期限の廃止・GA は本日のうちにチェックリスト化して周知（末尾「直近の注目予定」参照）。

出典:
- https://learn.microsoft.com/en-us/power-platform/released-versions/copilotstudio/2026.6.2

## カテゴリ別まとめ

### Anthropic / Claude
- Fable 5「今週中復旧」観測・Mythos 5 限定再開（約100組織）（ハイライト参照）。3ソースとも 6/26 以降の検証可能な新展開なしの holding pattern と一致
- Claude Code は **v2.1.195（6/26）が最新のまま**、6/27〜6/29 に新リリースなし。既報: ハイフン入り識別子の hook matcher 完全一致修正、`CLAUDE_CODE_DISABLE_MOUSE_CLICKS`、スペース無し言語（日本語・中国語・タイ語）の音声入力 auto-submit 修正、background job/agent 安定化 — https://code.claude.com/docs/en/changelog

### OpenAI / ChatGPT
- GPT-5.6 の 6/28 GA見送り（ハイライト参照）
- **Codex Remote が全プランで GA** — ChatGPT モバイルアプリから接続済み Mac/Windows ホストの作業を開始・継続・承認可能。新 DigitalOcean Droplet Workspace プラグインでリモートワークスペースを provision
- **個人財務（Personal Finance）機能** — 米国 Plus（Web/iOS）へ展開、Android は Pro/Plus 向け。金融口座を安全に連携しダッシュボード表示・文脈付き質問が可能
- **新音声認識（STT）モデル** — 全プランでディクテーションの裏側を刷新（多言語・アクセント・言語混在の精度向上、UI 変更なし） — https://help.openai.com/en/articles/6825453-chatgpt-release-notes

### Google / DeepMind
- **Gemini 3.5 Pro は 6/29 時点も未GA** — Vertex AI 限定エンタープライズプレビュー継続（2M context・Deep Think、モデルカード/ベンチマーク/価格すべて未公開）。コンシューマ Gemini アプリ・AI Studio・一般API のいずれにも安定版未登場。Pichai の月内期限（6/30）まで残り約1日で、月内GAか7月初旬ずれ込みかの分岐が目前。予測市場は「6/30 までに公開」を約50〜55%と拮抗 — https://www.frankx.ai/blog/gemini-3-5-pro-analysis-2026

### Microsoft / GitHub
- Copilot Studio 2026.6.2 の破壊的変更（ハイライト参照）
- その他 Microsoft 一次情報（Copilot Studio What's New 最新6/26、Power Platform ブログ6/11、M365 Copilot リリースノート6/16バッチ、Tech Community「What's New in M365 Copilot」6月号）はいずれも変更なし

### Cursor / 開発ツール
- **Cursor**: 週末・本日とも新規なし。既報安定運用（Automations 6/18、Customize ページ 6/22、SDK 6/4、Bugbot ~90秒 6/10）
- **Devin / Cognition**: 明日 6/30 に classic 環境設定が廃止 → 全組織が declarative blueprints へ移行。既報: MCP マーケットプレイス拡張・v3 API GA、AI Productivity Guarantee（上限 $10M） — https://docs.devin.ai/release-notes/overview

### 市場・トレンド（変化なし）
- 市場シェア（Similarweb・2026年4月）: ChatGPT 54.7%、Gemini 27.4%、Claude 8.2%、DeepSeek 4.1%、Grok 2.8%
- エンタープライズLLM API 支出シェア: 2025年末で Anthropic Claude が首位、OpenAI・Google と合わせ3社で約88%。「効率シフト（Claude→DeepSeek 移行等）」がシェアに反映されるか引き続き要観察
- Z.ai（GLM系）が Mythos 同等ベンチを主張し、輸出規制の空白を突く動き（explainx 追跡）

## 直近の注目予定

- **6/30（明日）**: Anthropic サイエンスイベント / Gemini 3.5 Pro「6月内公開」予測の期限 / Devin classic 環境セットアップ廃止 / Copilot Studio for Teams クラシック作成終了（[MC1315217](https://mc.merill.net/message/MC1315217)）/ Copilot Studio 感度ラベル表示GA / Security Copilot E5 展開完了 / M365 価格ロックイン期限 / GPT-5.2・5.3-Codex 新規 API 不可化
- **7/1**: M365 価格改定発効（E3 $36→$39、E5 $57→$61、Copilot Business $18→$21）/ Cursor 新価格 / Devin Cascade 削除
- **〜7 月上旬**: Fable 5 US 復旧（Axios「今週中」観測）/ Gemini 3.5 Pro 月内GA見送り時の代替期日
- **7/8**: Anthropic 政府発行ID・生体情報検証ポリシー施行（Fable 5 一般再開の経路候補）
- **7/10-17 頃**: GPT-5.6 一般提供（GA）最有力観測 / Gemini 3.5 Pro・Claude Opus 4.7 のローンチ集中報道
- **7/17**: Claude Corps 第1期応募締切
- **8/1**: covered frontier model フレームワーク 60日 EO 期限
- **8/3**: 旧「Claude in Slack」アプリ退役
- **8/5**: Opus 4.1 Claude API 退役
- **8/26**: OpenAI Assistants API 廃止 / o3 退役 / GPT-4.5 完全廃止
- **9 月**: iOS 27 / macOS 27 GA（AFM 3 本番）

## 改善メモ

- **【ウォッチ項目の予測精度】GPT-5.6 の「6/28 GA」予測（Polymarket 約83%）が外れ、限定プレビュー継続・GA は7月中旬へスリップ。** 政府承認制下のモデルは GA スケジュールが予測市場の織り込みより遅れる傾向が確認された。今後フロンティアモデルの GA 時期は予測市場の数字を鵜呑みにせず「政府協議の進捗」を一次変数として保守的に扱う。Gemini 3.5 Pro の 6/30 期限も同様。
- **【再発・要対応】起動時にローカルクローンが古い `main` で停滞する問題が3ソースで継続記録**（01 は〜6/05、03 は〜6/05 で停滞、origin/main は 6/28 まで反映済）。起動時に `git fetch && git reset --hard origin/main` 相当を行う SessionStart フックの導入を強く推奨。本サマリーリポジトリでも開始時に `git merge-base main origin/main` で共通祖先を確認する運用を推奨。
- **【再発・要対応】全ソースの RSS/WebFetch が引き続き 403**（axios.com・venturebeat.com の直接 WebFetch も 403）。各ソースとも WebSearch フォールバックで対応。`daily-sources.md` の取得方法欄を「WebSearch 優先」へ更新することを複数回記録済み・要対応。
- ソース間の整合: Fable 5 ステータス（凍結継続）、GPT-5.6 GA見送り、Gemini 未GA、Copilot Studio 2026.6.2 など主要項目で3ソースに矛盾なし。Master のみ Fable 5「今週中復旧」観測（Axios 6/27）を反映、Industry/Copilot は holding pattern と記述 — 観測 vs 確定の温度差として両論を併記。
