# AI News Daily Summary — 2026-07-10

> 本サマリーは 01_ai-news-Master・02_ai-news-Copilot・03_ai-news-industry の3ソース（7/10分）を統合して作成。

金曜。**競争軸が「モデル性能」から「業務を完遂する常駐エージェント製品」へ移った1日**。最重要は **OpenAI「ChatGPT Work」** — Codex 内蔵のエージェントが業務アプリを横断し、シート/スライド/ドキュメント/Web アプリを数時間かけて「完成品」として自律生成する。Claude Cowork への正面対抗であり、コンサル提案の中核論点に直結。あわせて **旧 xAI が「SpaceXAI」へ改称し Grok 4.5 を一般公開**（コーディング特化・Cursor 搭載・攻めの価格）、**Anthropic が利用分析ダッシュボード「Reflect」** を beta 提供開始。フロンティア主要ラボが同一週にプロダクトを出揃わせた。Microsoft の一次情報は静穏が継続。

## 今日のハイライト

### 1. OpenAI「ChatGPT Work」投入 — Codex 内蔵の常駐エージェントが業務を完遂 — Claude Cowork に正面対抗、選定基準は「監査・事前レビューの有無」へ

**事実** OpenAI が **ChatGPT Work（7/9）** を公開。GPT-5.6 を基盤に、接続済みアプリ・ファイル・ワークフローから文脈を収集 → ゴールをステップ分解 → スプレッドシート/スライド/ドキュメント/Web アプリを完成させる常駐エージェント。大プロジェクトを小タスクへ分解して**数時間連続稼働**し、スケジュール実行にも対応。Web/モバイル/デスクトップ横断で起動・管理でき、ローカルファイル/アプリまたは新内蔵ブラウザで Web を操作、Plugins で外部アプリ連携。あわせて **Codex 単体アプリを ChatGPT デスクトップアプリに統合**（macOS/Windows、Mac は Chat/Work/Codex を1アプリに集約）、レポート/ライブダッシュボード用の **Sites（beta）** も提供。Pro/Enterprise/Edu で先行提供、数日内に Plus/Business へ拡大。

**根拠** OpenAI 公式・Bloomberg・MacRumors・9to5Mac（7/9）が一致して報道。エンタープライズ統制を標準装備し、管理者は接続ツール・社内データ・実行アクションを中央管理、**Compliance API** で会話・アクションを可視化、機微なアクションは実行前に自動レビューを通す。3ソースが本件を本日の最重要と評価。

**影響** 「チャットで答える AI」から「業務成果物を納品する常駐エージェント」への移行を、OpenAI（ChatGPT Work）と Anthropic（Claude Cowork）が同型プロダクトで正面から競う構図が確定。M365 Copilot を加えた三つ巴で、社内データ接続の権限設計とガバナンスが前提論点になる。

**行動指針** 導入検討では **compliance/監査 API とアクション事前レビューの有無を実質的な選定基準**に据える。エージェントに与える社内データ接続の権限設計・ガバナンスを提案の前提に置く。Claude Cowork（7/21 GA 告知イベント）との比較検証を並行で準備する。

- https://openai.com/index/introducing-the-codex-app/
- https://www.bloomberg.com/news/articles/2026-07-09/openai-unveils-chatgpt-work-agent-to-field-tasks-for-hours
- https://9to5mac.com/2026/07/09/openai-announcing-the-next-chapter-for-chatgpt-today-watch-here/
- https://www.macrumors.com/2026/07/09/openai-chatgpt-work/

### 2. xAI が「SpaceXAI」へ改称し Grok 4.5 を一般公開 — コーディング特化・Cursor 搭載・「Opus クラスを低価格で」 — 比較軸は「1タスク単価 × 既存ツール統合」

**事実** 旧 xAI が **SpaceXAI へリブランド**（2月の SpaceX による xAI 合併、6月の SpaceX IPO を経て新ロゴ・新 X ハンドル）し、初モデルとして **Grok 4.5 を一般公開（7/9）**。コーディング/エージェント/知識作業に特化し「汎用チャットボットでなく実務向け」と明言、**Cursor と共同訓練（Cursor-Trained）**。価格は **入力$2／出力$6（キャッシュ入力$0.50）** で、Opus 4.8（$5/$25）を大幅に下回る。80 tokens/秒。SpaceXAI コンソール・Grok Build に加え **Cursor（全プラン）に即日搭載**。EU は7月中旬提供予定。

**根拠** SpaceXAI 公式・InfoWorld・Axios・MarkTechPost・Techweez（7/8-9）が報道。ベンチ試算では1コーディングタスク当たり **Grok 4.5 $2.49 対 GPT-5.5(Codex) $5.07・Fable 5(Claude Code) $11.80**。「Opus クラス性能を低コストで」と自称するが**独立検証は未公開**（長コンテキスト/ツール多用時は上振れの余地）。

**影響** フロンティア各社が同一週に投入するなか、Grok 4.5 は「Cursor 経由の流通」と「タスク単価の明示」で効率重視トレンドに乗る。API 競争でなく既存の開発環境経由で開発者に到達する点が特徴。Cursor（Anysphere、6/16 に $60B で買収合意・Q3 クローズ予定）は今後 SpaceXAI 傘下として追跡。

**行動指針** AI コーディング支援の提案では、モデル単体性能でなく **「1タスク当たりコスト × 既存ツール（Cursor 等）への統合」** で比較する枠組みを用いる。「Opus クラス」の主張は独立ベンチが出るまで留保し、自社ワークロードでの実測を推奨。

- https://x.ai/news/grok-4-5
- https://www.infoworld.com/article/4194895/spacexai-launches-grok-4-5-touts-lower-coding-task-costs-than-ai-rivals.html
- https://www.axios.com/2026/07/08/spacexai-grok-new-model
- https://www.marktechpost.com/2026/07/08/spacexai-releases-grok-4-5/

### 3. Anthropic、利用分析ダッシュボード「Reflect」beta 提供開始 — 個人の AI 利用を可視化 — 組織導入時の利用実態把握にも波及

**事実** Anthropic が **Claude Reflect（7/9）** を提供開始。Claude の利用状況・AI 利用習慣を可視化する組み込みダッシュボードで、過去 1/3/6/12 ヶ月のチャット活動を**月次リキャップ**（話題別の時間配分・最も活発だった日/ピーク時間帯・作業観察）として提示。フォーカス設定、休憩リマインダー、**quiet hours（静音時間）** などウェルネス機能も内蔵。memory を有効にした **Free / Pro / Max ユーザー向けにベータ提供**（Web / Claude Desktop の設定から生成）。incognito チャット・連携ツールの元ファイル・健康連携の会話は insights から除外。

**根拠** Anthropic 公式・TechCrunch（7/9）が報道。個人の AI 利用可視化という新しい方向性で、TechCrunch は「AI 利用を静かに後押しする設計」と評する。

**影響** 個人のウェルネス/振り返り機能だが、組織導入時の**利用実態把握**（誰が何にどれだけ使っているか）にも波及余地がある。利用分析は OpenAI の管理者向け統制（ChatGPT Work の Compliance API）と対照的に、まず個人体験から入る Anthropic のアプローチを示す。

**行動指針** 社内で Claude を利用するチームは、Reflect の利用傾向データを**定着度・活用領域の把握**に活用できる。ただし insights の除外仕様（incognito/健康連携等）を理解したうえで、組織の可視化ニーズには別途 admin 機能の有無を確認する。

- https://www.anthropic.com/news/reflect-with-claude
- https://techcrunch.com/2026/07/09/anthropics-new-claude-feature-is-quietly-selling-you-on-ai/

## カテゴリ別まとめ

### OpenAI
- **ChatGPT Work + Codex 統合デスクトップアプリ / Sites（beta）**（ハイライト参照）
- **GPT-5.6 が ChatGPT/Codex/API で GA、Plus は本日 7/10 順次**: 7/9 の広域公開に続き、24時間かけて全世界へ段階展開。Plus/Pro/Business/Enterprise は Sol を medium 以上の effort で利用可、Pro/Enterprise は最高品質の GPT-5.6 Pro も選択可。開放順は Enterprise API 7/7 → **ChatGPT Plus 7/10** → Team 全面 7/14。命名は「数字＝世代、Sol/Terra/Luna＝能力ティア」、料金据え置き（Sol $5/$30、Terra $2.5/$15、Luna $1/$6）。 https://x.com/OpenAI/status/2075271435573244008

### SpaceXAI（旧 xAI）/ Grok
- **SpaceXAI へ改称 + Grok 4.5 一般公開**（ハイライト参照）。Cursor 買収（$60B、Q3 クローズ予定）後・SpaceX IPO 後の初モデル

### Anthropic / Claude
- **Claude Reflect（利用分析ダッシュボード）beta**（ハイライト参照）
- **Claude Code**: 7/10 の新バージョンなし（最新は **v2.1.205**〔7/8〕、[7/9 サマリー](./ai-news-daily-2026-07-09.md)で詳述済）。auto mode の transcript 改ざんブロック・`rm -rf` 事前確認・`/doctor` 総合診断格上げが直近の目玉。 https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md

### 開発ツール
- **OpenAI Codex CLI 安定版 0.144.0（7/9）**: 使用上限リセットのクレジット表示、読み取り専用アクションを確認する `writes` 承認モード追加、MCP ツールが対話認証に対応。Intel Mac の Code Mode クラッシュ・Windows サンドボックスのファイル削除不具合を修正（0.143.0〔7/8〕から更新）。 https://github.com/openai/codex/releases
- **GitHub Copilot CLI pre-release v1.0.70-0（7/9）**: プラグインの commit SHA ピン留め、`/refine` によるプロンプト精緻化、セッション単位のサンドボックス制御フラグ追加（安定版は v1.0.69〔7/7〕のまま）。 https://github.com/github/copilot-cli/releases
- **MCP に Enterprise-Managed Authorization（EMA）拡張が安定版（7/7）**: 組織が MCP 経由のアクセスを中央で一括管理できる拡張。ChatGPT Work / Claude Cowork のようなアプリ横断エージェントの普及に伴い、MCP 接続の権限統制が実運用課題として前面化。 https://www.publickey1.jp/
- **GitHub Copilot VS Code 6月版 / Devin SWE-1.7（7/8・回収）**: Copilot は **OpenAI Codex をエージェントプロバイダー化（Public Preview）**・Customizations に Hooks サポート・**Kimi K2.7 Code（オープンウェイト）をモデルピッカーに GA 追加**・Inline Chat GA。Devin は **SWE-1.7**（Kimi K2.7 Code をベースに Devin ハーネス内で RL 事後学習、SWE-Bench Multilingual で GPT-5.5 を上回るがフロンティアには数ポイント届かず）。※両ツールで Kimi K2.7 Code 系が採用され、オープンウェイトの実装採用が進む。 https://github.blog/changelog/2026-07-08-github-copilot-in-visual-studio-code-june-2026-releases/
- **Cursor**: 新規の日付確定情報なし（cursor.com/changelog は本日も 403）。集約サイトに Automations・Grok 4.5 搭載の記載があるが一次未確認。3.9（Customize ページ・6/22）／iOS 公開ベータ（6/29）が確認済みの最新

### Google / DeepMind
- **Gemini 3.5 Pro、7/17 GA 目標・2.5 Pro 基盤を破棄して再構築**: 当初6月GA目標から遅延し、DeepMind は 2.5 Pro のベースモデルを破棄して完全な事前学習をやり直す判断。数学的推論・SVG 生成・画質を GPT-5.6/Fable 5 対抗に引き上げる狙い（2M トークン文脈・Deep Think 層を予告）。7/17 GA 目標は第三者報道が複数だが、モデルカード・API ドキュメント・確定価格による公式確認は未発表で日付保証はない。 https://finance.biggo.com/news/6f0c6bb2-795f-4c57-9d09-6db691d7638a

### Microsoft / Copilot Studio（一次情報は静穏）
- **一次情報の動きなし**（いずれも Learn MCP で一次確認）: Released Versions は Build 2026.6.3（6/30初出）のまま次ビルド 2026.7.x 未反映（次回火曜 **7/14** 監視）。What's New は June 2026 のまま7月項目なし。M365 Copilot Release Notes は July 01 バッチが最新で off-cycle なし（次バッチ 7/14〜7/15 前後見込み）
- **Power Platform / Copilot Studio ブログ**: 「What's New in Power Platform: July 2026」は未公開（最新は 6/11）。Copilot Studio 公式ブログも 6/25「Building reliable voice agents」が最新のまま。7/8〜7/10 の新規 MC 番号・大型発表は未検出（固有 MC 番号の網羅は手動確認推奨）

### Apple
- **iOS 27 Public Beta は7月中旬（〜7/14 頃）予定**: Developer Beta 3（7/6）まで、GA 9月。WWDC の Foundation Models Framework 路線に変更なし

## 直近の注目予定

- **7/10（本日）** ChatGPT Plus への GPT-5.6 開放（順次）
- **7/13** Claude Code の週次上限+50%プロモ（5月開始）の期限（延長なき場合）
- **7/14** ChatGPT Work が Plus・Business へ拡大予定 / GPT-5.6 Team 全面開放 / 破壊的変更: Visio → Power Automate エクスポート廃止発効 / M365 Copilot Release Notes 次バッチ見込み / Copilot Studio 版ページ次更新（2026.7.x 反映見込み）
- **7 月中旬** Grok 4.5 EU 提供予定 / iOS 27 Public Beta 公開予定
- **7/15** Claude Science（AI for Science）応募締切
- **7/17** Gemini 3.5 Pro GA 候補日（未確定）/ Claude Corps 第1期応募締切
- **7/21** Copilot Cowork GA 告知イベント
- **7/23** OpenAI computer-use-preview シャットダウン
- **7/31** Devin classic 環境設定の read-only 参照終了
- **8/1** covered frontier model 60 日 EO 期限
- **8/3** 旧「Claude in Slack」退役
- **8/5** Opus 4.1 Claude API 退役
- **8/26** OpenAI Assistants API 廃止 / o3 退役 / GPT-4.5 完全廃止
- **8/31** Sonnet 5 促進価格終了（$2/$10 → $3/$15）
- **9 月** iOS 27 / macOS 27 GA（AFM 3 本番）

## 改善メモ

- **前日（7/9）分の欠損リカバリを実施**: 当初欠損だった 01_ai-news-Master の 7/9 分ダイジェストが本日取得可能となったため、7/9 サマリーを3ソースで再生成・上書き（別コミット）。Master 側ルーチンは7/8夜の失敗から復旧したとみられる。
- **障害の変化**: xAI/SpaceXAI `x.ai/*`・Anthropic news・github.blog・cursor.com/changelog・9to5Mac の WebFetch 403 継続（3ソースとも WebSearch/二次ソースで補完）。取得方法の WebSearch 優先化提案（B-004）が継続中（11回目）。
- **ソース間整合**: ChatGPT Work（7/9）・Grok 4.5/SpaceXAI 改称・Reflect・GPT-5.6 GA 続報が3ソースで整合。Grok 4.5 の「Opus クラス性能」は独立検証未公開の点を各ソースが明記。矛盾は検出されず。
