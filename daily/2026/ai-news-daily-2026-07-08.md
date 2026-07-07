# AI News Daily Summary — 2026-07-08

> 本サマリーは 01_ai-news-Master・02_ai-news-Copilot・03_ai-news-industry の3ソース（7/8分）を統合して作成。

水曜。**大型モデル発表はなく、主役はセキュリティと開発ツール、そして規制連動の「本人確認」**。最重要は Sysdig が公開した初のエージェント型ランサムウェア **JADEPUFFER**（Langflow の既知RCE 起点）。制度面では **Anthropic の ID 検証ポリシーが本日 7/8 発効**し、昨日終了した Fable 5 無償枠 → 従量課金と連動して「消費者プランでの Fable 5 利用は本人確認が前提」という体制が整った。開発ツールは GitHub が Copilot デスクトップアプリを全プランに開放。

## 今日のハイライト

### 1. 初の「エージェント型ランサムウェア」JADEPUFFER — Langflow RCE 起点でAIが攻撃を自動実行 — AIエージェント/OSSツール導入のセキュリティ論点が現実に

**事実** Sysdig Threat Research Team が「初のエージェント型ランサムウェア」として **JADEPUFFER** を公開。AIエージェントが偵察〜認証情報窃取〜横展開〜暗号化まで攻撃ライフサイクルを自動実行する。侵入口は公開状態の **Langflow インスタンスの未認証RCE（CVE-2025-3248・CVSS 9.8、v1.3.0未満）**。約600ペイロードを実行し、身代金要求文まで自動生成した。

**根拠** LLM 駆動の証跡として、①各操作の理由・ROI優先度を自己記述するコード、②失敗ログインを31秒で修正する適応的リトライ、③JSON要求にXMLが返るや即座にパーサを切替える実行時適応、が確認された。ただし TechCrunch（7/6）によれば「完全自律」ではなく、セットアップ・標的選定・C2構築・認証情報供給は人間が実施。CVE-2025-3248 は 2025年5月に CISA KEV 収録済みで、パッチ放置＝既知リスクの放置に当たる。

**影響** ランサムウェア運用のスキル床が「エージェントを走らせるコスト」まで低下（盗用クレデンシャル利用なら実質ゼロ）。社内で AIエージェント／OSSツール（Langflow 等）を導入する組織にとって、公開エンドポイントの露出・CVE パッチ遅延・クレデンシャル衛生が具体的なインシデント要因として顕在化した。

**行動指針** Langflow 等の LLM オーケストレーション OSS を利用中なら、公開エンドポイントの即時遮断と CVE-2025-3248 パッチ適用状況を最優先で確認。AI導入の提案・要件定義に「公開エンドポイント遮断・CVE即時パッチ・クレデンシャル衛生」をセキュリティ要件として明記する。

- https://www.sysdig.com/blog/jadepuffer-agentic-ransomware-for-automated-database-extortion
- https://techcrunch.com/2026/07/06/the-first-ai-run-ransomware-attack-still-needed-a-human/
- https://thehackernews.com/2026/07/ai-agent-exploits-langflow-rce-to.html

### 2. Anthropic の ID 検証ポリシーが本日 7/8 発効 — 消費者プランの Fable 5 利用は本人確認が前提に

**事実** Anthropic の更新プライバシーポリシーが **本日 7/8 施行**。**消費者プラン（Free/Pro/Max）**のユーザーが一部機能（特に **Fable 5 の credits 購入**）を使う際、**Persona 経由の本人確認**が必要になる。取得データは政府発行 ID の画像・顔写真/動画・**顔ジオメトリテンプレート（一部法域では生体データに該当と Anthropic 自身が明記）**。**API・Team・Enterprise は対象外（免除）**。実運用では 7/7 から Pro/Max へのアップグレード時に「Quick identity check」モーダルが出現している。

**根拠** ID 検証テスト自体は 4/14 開始で export control 指令以前から進行しており、Fable 5 停止への直接対応ではない。ただし昨日（7/7）に Fable 5 の週次50%無償枠が終了し従量課金へ移行したことと合わせ、「モデル全体を止める代わりに検証済みユーザー単位で Fable 5 をゲートできる」体制が今回整った、という構図。

**影響** 消費者プランで Fable 5 を業務利用しているユーザーは、本人確認（政府発行 ID＋セルフィー＋顔ジオメトリ）を通さないと credits 購入・利用ができなくなる。生体データ取得を含むため、組織のプライバシー方針・従業員への案内が必要になる場合がある。

**行動指針** チームで Fable 5 を消費者プラン経由で使っている場合は、Team/Enterprise（免除対象）への移行を検討。個人利用継続なら本人確認フローの発生を前提に運用を案内する。生体データ取扱いへの懸念があれば、API/Enterprise 経路の利用に切り替える。

- https://www.anthropic.com/news/redeploying-claude-fable-5
- https://techcrunch.com/2026/06/22/anthropic-says-claude-may-want-to-see-your-id/
- https://www.techtimes.com/articles/318778/20260621/claude-identity-verification-starts-july-8-what-facial-data-anthropic-collects.htm

### 3. GitHub、Copilot デスクトップアプリを全プランに開放（7/7）＋ Claude Code v2.1.202 — エージェント駆動開発の裾野が広がる

**事実** GitHub が **Copilot デスクトップアプリ（macOS/Windows/Linux）を Free・Education を含む全 Copilot プランに開放（7/7）**。GitHub アカウントでサインインし、デスクトップからエージェント駆動開発を開始できる。CLI に続きアプリ本体も一般化した。あわせて **Claude Code v2.1.202（7/6）** が `/config` に「Dynamic workflow size」設定（動的ワークフローが生成するエージェント数を小/中/大で制御。強制上限ではなく助言的ガイドライン）と `workflow.run_id`/`workflow.name` の OTel 属性を追加。

**根拠** GitHub Copilot app changelog（7/7）と Claude Code の github raw CHANGELOG が一次ソース。Copilot CLI も pre-release v1.0.69-3（7/7）で承認済みファイル編集のサンドボックスバイパス・`/diff` 描画性能改善等、Codex CLI も 0.143.0-alpha.38（7/7）を日次で刻むが機能追加は小粒。

**影響** デスクトップアプリの全プラン開放で、エージェント駆動開発の入口が無償ユーザーまで広がる。Claude Code 側の動的ワークフロー規模制御・OTel 属性は、多エージェント運用のコスト管理・可観測性を実務で扱えるようにする。

**行動指針** Copilot アプリを Free/Education 環境で試すなら本日以降すぐ利用可。Claude Code で動的ワークフローを使うチームは `/config` の「Dynamic workflow size」でエージェント数を制御し、OTel 属性でワークフロー実行のコスト・挙動を可視化する。

- https://github.blog/changelog/2026-07-07-github-copilot-app-available-to-all/
- https://code.claude.com/docs/en/changelog
- https://github.com/github/copilot-cli/releases

## カテゴリ別まとめ

### Anthropic / Claude
- **ID 検証ポリシー本日発効**（ハイライト参照）。Fable 5 無償枠終了（7/7）との連動体制が整う
- **Alberta 州政府の Claude Code 導入事例を公開（7/6）**: 州の技術・イノベーション省が Opus/Sonnet で「4.66 億行のコードを 20 時間でスキャン」、脆弱性を横断修正し安全化ツールも新規構築。政府系レガシー刷新での大規模適用・セキュリティ観点の実績値。 https://www.anthropic.com/news/alberta-government-claude-cybersecurity
- **Enterprise でカスタムロール別のコネクタ/ツール制御を追加**。Claude Science（6/30 GA）継続。Fable 5/Mythos 5 仕様は据え置き（1M context / 128k output / $10・$50）

### OpenAI / フロンティアモデル
- **GPT-5.6 広域GA は 7/8 も未達**: 約20組織限定プレビュー継続、予測市場「GPT-5.6 released on…?」は **7/9 が約64%で首位**（次点 7/10 約7%）。GA は「数週間内」（7/10–17 目安）。Sol を Cerebras 上で最大 750 tok/s 提供予告。個人 ChatGPT 搭載可否・提供プランは未確定。価格据え置き（Sol $5/$30・Terra $2.5/$15・Luna $1/$6）。実質ゲートは 8/1 の EO 14409 任意フレームワーク finalize。 https://polymarket.com/event/gpt-5pt6-released-onptptpt-20260623051439980
- **ChatGPT 側**: Codex Remote の全プラン GA・macOS 版 Record & Replay 等

### 開発ツール
- **Copilot アプリ全プラン開放 / Claude Code v2.1.202**（ハイライト参照）
- **GitHub Copilot CLI**: pre-release v1.0.69-3（7/7）で承認済み組込みファイル編集のサンドボックスバイパス・`/sandbox add-path` サジェスト・大規模 diff の `/diff` 描画性能改善・自動承認タイムラインにリクエスト詳細表示。安定版は v1.0.68（7/1、kimi-k2.7-code 対応）のまま
- **OpenAI Codex CLI**: pre-release 0.143.0-alpha.38（7/7）。alpha は日次更新で機能追加は小粒、安定版 0.142.5（7/1）のまま
- **Cursor**: 3.9（Customize ページ・6/22）／iOS 公開ベータ（6/29）が最新。新規 changelog なし（cursor.com/changelog は本日も 403）
- **Devin**: Security Swarm（7/1）が最新。大型発表なし
- **xAI / Grok**: Grok Build に `/goal`（長時間自律モード）等の小改善、Batch API が画像/動画生成に対応。旗艦 Grok 5（噂 6T）未出荷

### Google / DeepMind
- **Gemini 3.5 Pro**: 7月第2週入りもなお限定プレビュー（Vertex AI 限定 Enterprise preview のみ）。GA 日・公開ベンチマーク・確定価格いずれも未発表、報道で 7/17 説。2M context / Deep Think は据え置き。 https://www.marketscale.com/industries/software-and-technology/gemini-3-5-pro-still-in-preview-what-enterprise-teams-evaluating-a-model-should-do-now

### Microsoft / Copilot Studio（一次情報の動きなし）
- **Copilot Studio 基盤（Released Versions）**: 最新は Build 2026.6.3（6/30初出）のまま。版ページ（火曜更新）に次ビルド 2026.7.x は依然未反映。リージョン展開も変化なし（Preview 系11リージョンが 2026.6.3、UK/Asia/Japan/Europe/UAE が 2026.6.2、US 本体/Australia/GCC が 2026.6.1）。次回火曜 7/14 と併せ要監視
- **M365 Copilot Release Notes**: July 01 バッチが最新。Learn MCP で off-cycle バッチなしを一次確認。次バッチは隔週傾向で 7/14〜7/15 前後見込み
- **Power Platform Blog**: 「What's New in Power Platform: July 2026」は未公開（最新は 6/11 の June 2026 Feature Update）。月内早めに出る傾向のため要監視
- **Message Center / Roadmap**: 7/8 の新規 MC 番号・大型発表は未検出（固有MC番号の網羅は手動確認推奨）

### セキュリティ
- **JADEPUFFER**（ハイライト参照）。CVE-2025-3248（Langflow・CVSS 9.8）は CISA KEV 収録済み、要即時パッチ

### 国内・業界提案素材
- **AI法律スタートアップ Norm が $120M Series C（Khosla主導）、評価額 $1.2B でユニコーン化（TechCrunch、7/7）**: 「AIエージェント＋人間弁護士の監督」による AIネイティブ法律事務所。時間課金ではなく**成果（アウトカム）ベース課金**が特徴。専門サービス業の AI 置換が資本市場で評価される流れ。「AI導入の価値を成果報酬で回収する」料金モデルの実例として提案に引用可。 https://techcrunch.com/2026/07/07/ai-law-startup-norm-raises-120m-hits-unicorn-valuation/

## 直近の注目予定

- **7/8（本日）** Anthropic ID 検証ポリシー発効（消費者プランは Persona 経由の本人確認が Fable 5 credits 購入等の前提に）
- **7/9** GPT-5.6 広域GA見込み（予測市場 約64%）
- **7/13** Claude Code の週次上限+50%プロモ（5月開始）の期限（延長なき場合）
- **7/14** 破壊的変更: Visio → Power Automate エクスポート廃止発効／M365 Copilot Release Notes 次バッチ見込み／Copilot Studio 版ページ次更新
- **7/15** Claude Science（AI for Science）応募締切
- **7/16・7/23** GitHub Models ブラウンアウト（7/30 全面廃止に向けた移行予行）
- **7/17** Claude Corps 第1期応募締切／Gemini 3.5 Pro GA 候補日（未確定）
- **7/21** Copilot Cowork GA 告知イベント
- **7/23** OpenAI computer-use-preview シャットダウン
- **7/30** GitHub Models 全面廃止 → Azure AI Foundry 移行必須
- **7/31** Devin classic 環境設定の read-only 参照終了
- **8/1** covered frontier model 60 日 EO 期限（GPT-5.6/Gemini 3.5 Pro の広域リリース条件を規定）
- **8/3** 旧「Claude in Slack」退役
- **8/5** Opus 4.1 Claude API 退役
- **8/26** OpenAI Assistants API 廃止／o3 退役／GPT-4.5 完全廃止
- **8/31** Sonnet 5 促進価格終了（$2/$10 → $3/$15）
- **9月** iOS 27 / macOS 27 GA（AFM 3 本番）

## 改善メモ

- **RSS/WebFetch 全ソース403継続**（03_industry）: WebSearch で収集。取得方法の WebSearch 優先化提案（B-004）が9回目の継続。
- ソース間で本日の Anthropic ID 検証発効（7/8）・GPT-5.6 GA 未達・Claude Code v2.1.202 の記述が一致。矛盾は検出されず（industry は Fable 5 課金開始を「7/8 から」、Master/Copilot は「7/7 無償枠終了」と表記するが実質同義）。
- Master/Copilot は新規提案・障害の変化なし。
