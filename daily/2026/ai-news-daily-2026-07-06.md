# AI News Daily Summary — 2026-07-06

> 本サマリーは 01_ai-news-Master・02_ai-news-Copilot・03_ai-news-industry の3ソース（7/6分）を統合して作成。
> ※ 当初 01_ai-news-Master の当日分（7/6）が未取得だったが、7/7 に取得可能となったため3ソースで再生成（欠損リカバリ）。

月曜。**新規のフロンティアモデル・一次情報の動きは乏しい静かな1日**だが、明日 7/7 が節目集中日。GPT-5.6 の広域GA（予測市場が7/7を約74%で織り込み）、Anthropic Fable 5 の usage credits 移行、Copilot Studio 次ビルドが重なる。

## 今日のハイライト

### 1. GPT-5.6 広域GAが目前 — 予測市場「7/7」を約74%織り込み — 出荷日は政府承認が実質規定

**事実** OpenAI の次世代フロンティアモデル GPT-5.6（Sol/Terra/Luna）の広域GAが目前に迫った。6/26 開始の限定プレビュー（米政府承認の約20組織向け・API＋Codex）から「7月中旬」観測が続いていたが、予測市場（Polymarket/CryptoSlate）はリリース日を **7/7 に約74%（次点7/8が9%）** で織り込んでいる。

**根拠** ゲートは日付ではなく、6/2 大統領令に基づく **任意フレームワーク**（フロンティアモデルを公開前に最大30日、政府が事前テスト）。White House の任意事前レビューが最終ゲートで、承認が下りたタイミングでGAとなる。

**影響** 「政府承認制がフロンティアモデルの出荷カレンダーを実質規定する」構図が定着。個人 ChatGPT への搭載可否・提供プランは未確定で、GA後の提供形態を注視する必要がある。

**行動指針** 7/7 前後の OpenAI 公式アナウンスを監視。API/Codex 利用チームは GA 後のモデル切替・価格・レート制限の変更に備える。

- https://openai.com/index/previewing-gpt-5-6-sol/
- https://polymarket.com/event/gpt-5pt6-released-onptptpt-20260623051439980

### 2. GitHub Models が 7/30 に全面廃止 — Azure AI Foundry への移行が必須（猶予なし）

**事実** GitHub Models が **2026-07-30 に全面リタイア**（7/1告知）。プレイグラウンド／モデルカタログ／推論API／BYOKエンドポイントを含む全機能が Free/Team/Enterprise すべてで停止する。猶予・grandfathering はなし。

**根拠** 移行先は **Azure AI Foundry**（GitHub 上のワークフローは Copilot 経由）。移行前の予行として **7/16・7/23 にブラウンアウト**（一時的にエラー返却）を実施予定。

**影響** GitHub Models を推論APIやプロトタイピングに組み込んでいるチームは、残り約3週間で移行を完了する必要がある。企業は送信先許可リストに `*.azure.com` とFoundryエンドポイントを追加するIT/セキュリティレビューが発生し、期間内に間に合わないリスクが指摘されている。

**行動指針** 利用有無を棚卸しし、Azure AI Foundry への移行計画を即着手。7/16・7/23 のブラウンアウトを移行検証のマイルストーンに設定する。

- https://github.blog/changelog/2026-07-01-github-models-is-being-fully-retired-on-july-30-2026/

### 3. Anthropic Fable 5 — 7/7 に週次上限50%制限が解除、usage credits（従量課金）へ移行

**事実** Anthropic Fable 5 / Mythos 5 は 7/1 のグローバル復帰（輸出規制解除に伴う）から新規進展はないが、**7/7 に導入価格の週次利用上限50%制限が解除され、usage credits（従量課金）へ移行**する。API 直販の従量価格は入力 $10／出力 $50（per M tokens）。

**根拠** 商務省による 6/30 の輸出規制解除を受けた Anthropic の 7/1 復旧開始からの規定路線。Copilot・industry の2ソースが一致して 7/7 移行を記載。

**影響** **credits を未有効化のテナントは 7/7 以降アクセス不可**になる恐れ。従量課金への移行で、これまで上限50%枠内で利用していたワークロードのコスト構造が変わる。

**行動指針** Fable 5 / Mythos 5 を利用中のテナントは 7/7 までに usage credits を有効化。従量課金前提でコスト試算・予算枠を再設定する。

- https://www.techtimes.com/articles/319318/20260629/gemini-35-pro-cleared-july-launch-fable-5-nears-return-gpt-56-stays-locked.htm

## カテゴリ別まとめ

### OpenAI / フロンティアモデル
- **GPT-5.6 広域GA目前**（ハイライト参照）

### 資本・政策
- **SoftBank、OpenAI 第2トランシェ $10B を 7/1 実行**: 2/27 公表の総額$30B追加出資の一環（Vision Fund 2 経由、3/27 締結のブリッジ facility で調達）。**第3トランシェ $10B は 2026-10-01 実行予定**（IPO時は前倒しの可能性）。 https://group.softbank/en/news/press/20260701
- **OpenAI、米政府への5%出資（約$42.6B相当）を提案と報道（7/2 FT/Bloomberg/Forbes）**: Altman が Trump 大統領・Lutnick商務長官・Bessent財務長官と直接協議。アラスカ永久基金を範に、他の主要AIラボにも同様の政府出資を求める構図。現時点は「概念的」段階で議会承認が必要、実施可否は不透明。 https://www.forbes.com/sites/siladityaray/2026/07/02/openai-reportedly-pitches-granting-us-government-5-stake/

### Anthropic / Claude
- **Fable 5 usage credits 移行（7/7）**（ハイライト参照）
- **Claude Code**: v2.1.201 が最新のまま（7/3〜7/6 新版なし）
- **競争構図**: Anthropic 売上ラン・レート $30B 超で自己申告売上ベース逆転（7/4既往）から新規なし

### OpenAI / ChatGPT
- **ChatGPT 新ディクテーション（音声→テキスト）モデルを全プラン展開**: 多言語混在・言語スイッチ・騒がしい環境・小声/ささやき・英数字混在の書き起こし精度を改善。併せて ChatGPT Business に **plugin 管理者統制**（discovery/policy/install の一元管理、状態・ロール・カテゴリでの絞り込み）、Remote Control の **1対1 認証付き QR ペアリング**を追加。 https://help.openai.com/en/articles/6825453-chatgpt-release-notes

### Microsoft / Copilot Studio
- **Copilot Studio - What's New**: June 2026 セクションのまま、7月項目なし（Learn MCP で一次確認）。新エージェント体験（Production-ready Preview）／Microsoft IQ／Skills／Memory
- **Copilot Studio 基盤（Released Versions）**: 最新は Build 2026.6.3（6/30初出）で変化なし。版ページは火曜更新のため**次ビルドは 7/7 見込み**
- **M365 Copilot Release Notes**: July 01 バッチ（透かし／秘密度ラベル継承／エージェントのスケジュール実行・Teams共有／Outlook Copilot Chat 拡大）が最新。次バッチは隔週傾向で **7/14〜7/15 前後見込み**
- **Message Center / Roadmap**: 7/3〜7/6 の新規 MC 未検出。MC1325422（Copilot アプリ再設計＝Tasks タブ・ピン留め、〜7月中旬展開）は既報

### 開発ツール
- **GitHub Models 全面廃止（7/30）**（ハイライト参照）
- **GitHub Copilot CLI**: pre-release v1.0.69-1（7/4）で接続中 MCP サーバ・ステータスの一覧表示、ターン途中での設定変更に対応。安定版は v1.0.68（7/1）のまま
- **OpenAI Codex CLI**: pre-release 0.143.0-alpha.36（7/5）。alpha は日次で刻まれ機能追加は小粒。安定版は 0.142.5（7/1）のまま
- **GitHub Copilot（本体）**: 7/2 changelog（CLI が Actions で PAT 不要、エージェントセッションストリーミング Public Preview 等）が最新。7/3〜7/6 新規なし
- **Cursor**: 3.9（Customize ページ＝プラグイン/スキル/MCP/サブエージェント一元管理・6/22）と iOS 公開ベータ（6/29）が最新。7/3〜7/6 新規なし
- **Devin**: Security Swarm（7/1）が最新。Devin Desktop（旧 Windsurf）は既報。7/3〜7/6 新規なし

### 継続ウォッチ（変化なし）
- **Google Gemini 3.5 Pro**: 据え置き。7月GA目標だが具体日未発表（Google広報ノーコメント）。Vertex AI 限定エンタープライズプレビュー継続、200万トークン文脈・Deep Think は $250/月 Ultra 限定。 https://www.techtimes.com/articles/319318/20260629/gemini-35-pro-cleared-july-launch-fable-5-nears-return-gpt-56-stays-locked.htm

## 直近の注目予定

- **7/7** GPT-5.6 広域GA見込み（予測市場74%）／Fable 5 週次上限50%制限が解除→usage credits へ移行／Copilot Studio 次ビルド見込み（版ページ火曜更新）
- **7/8** Anthropic 政府 ID 検証ポリシー発効
- **7/14** 破壊的変更: Visio → Power Automate エクスポート廃止発効／M365 Copilot Release Notes 次バッチ見込み
- **7/16・7/23** GitHub Models ブラウンアウト（移行予行）
- **7/21** Copilot Cowork GA 告知イベント
- **7/30** GitHub Models 全面廃止 → Azure AI Foundry 移行必須
- **8/1** フロンティアモデル枠組みの大統領令60日期限
- **10/1** SoftBank OpenAI 第3トランシェ $10B 実行予定
- 7月中旬〜下旬 2026 Release Wave 2 計画ページ公開見込み（wave2 URL は現在404・要監視）／M365 Copilot サービスプラン挙動変更（Premium/Basic のアクセス制御がサービスプラン主導に）

## 改善メモ

- **欠損リカバリ実施**: 当初未取得だった 01_ai-news-Master の 7/6 分が 7/7 に取得可能となり、本サマリーを3ソースで再生成・上書きした。追加された主な内容は ChatGPT 新ディクテーションモデル・Copilot CLI / Codex CLI の小刻み更新。Master 側ルーチンの遅延は解消済み。
- **取得方法の確定（B-006）**: 01_Master 側で宿題ソース `platform.claude.com`（Fable 5/Mythos 5 ドキュメント）の WebFetch 疎通を確認し、取得方法欄をプライマリに確定。
- **RSS/WebFetch 全ソース403継続**（03_industry）: WebSearch で収集。取得方法の WebSearch 優先化提案（B-004）が7回目の継続。主要ソース一括403は月曜復旧チェック（B-001）でも継続を確認。
- ソース間で 7/7 の Fable 5 usage credits 移行・GPT-5.6 GA・Copilot Studio 次ビルドの記述が一致。矛盾は検出されず。
