# AI News Daily Summary — 2026-06-17

> 本サマリーは 01_ai-news-Master・02_ai-news-Copilot・03_ai-news-industry の3ソース（6/17分）を統合して作成。

## 今日のハイライト

### 1. Fable 5 / Mythos 5 の世界停止が6日目 — 政治問題化、Sacks「Anthropicが修正を拒否」/ 同盟国の反発拡大

**事実**: 6/12 の米輸出規制に端を発した Fable 5 / Mythos 5 の全世界停止は **6/17 時点も継続（6日目）**。Anthropic は引き続き全顧客を Opus 4.8 へリルートしている。トランプ政権の AI 担当 David Sacks は X で、**信頼できるパートナーがテスト中に safeguard を回避する jailbreak 手法を発見→米政府へ報告→政府が修正（パッチ）を要請したが、Anthropic 経営陣が修正要請を拒否したため輸出規制を発動した**と主張。中国系とみられるグループが Mythos へリバースエンジニアリングでアクセスした疑い・蒸留（distillation）リスクも理由に挙げられている。

**根拠**: Anthropic 公式（anthropic.com/news/fable-mythos-access、ただし 403 継続で各社は WebSearch フォールバック）は「これは narrow / 汎用ではない jailbreak で、数億ユーザーに影響するリコールの根拠としては不十分。同等の結果は他の公開モデルにも現れる」と反論。停止解除には Anthropic 側のパッチ適用が条件とされ、市場予測は **7月までの復旧確率を約75%** と見込む。Business Today は「White House がわずか90分の猶予で制限を要求した」と報道。

**影響**: 政府指示によるモデル供給停止が1週間規模で続く前例として、単一フロンティアモデル依存リスクが一段と顕在化。英国 MP は病院・研究運用への支障を批判し、英国向けの carve-out 要請は却下された。フランスは国産AI支援を主張、EU は戦略的依存リスクを警告、インドは重要サービスが外国政府の管理下に置かれる懸念を表明するなど、地政学・主権の論点へ拡大している。

**行動指針**: Fable 5 / Mythos 5 を本番に組み込む組織は復旧時期を「未定」と見なし、Opus 4.8 / GPT-5.5 フォールバック前提で運用継続。輸出規制・モデル提供停止系イベントは Anthropic 公式＋大手メディア（Bloomberg / Al Jazeera / Tom's Hardware 等）＋政府発信を毎日クロスチェックし、6/22 試食期間終了・6/23 クレジット移行などの既定スケジュールは「停止中ゆえ要再確認」として追跡すること。

- https://www.anthropic.com/news/fable-mythos-access
- https://www.bloomberg.com/news/articles/2026-06-16/trump-s-anthropic-crackdown-sets-off-ai-alarms-for-us-allies
- https://www.aljazeera.com/news/2026/6/14/us-asks-anthropic-to-block-global-access-to-top-ai-models-why-it-matters
- https://www.tomshardware.com/tech-industry/artificial-intelligence/trump-adviser-david-sacks-says-anthropic-refused-to-fix-fable-5-jailbreak-before-us-export-controls
- https://www.businesstoday.in/technology/artificial-intelligence/story/anthropic-had-90-minutes-to-restrict-claude-fable-5-as-white-house-feared-chinese-access-537095-2026-06-16

### 2. G7エビアン・サミットが6/17閉幕 — 「AI・サイバーセキュリティに関する宣言」を正式成果に採択

**事実**: フランス議長下の **第52回 G7 サミット（エビアン、6/15-17）が 6/17 に閉幕**し、正式な成果文書として **「Declaration on AI and cybersecurity（AI・サイバーセキュリティに関する宣言）」を採択**。デジタル経済・AI・量子技術・貿易を包括的に扱った。

**根拠**: カナダの前回「AI for Prosperity」枠組みを発展させ、協調的な AI ガバナンス構造を前進させる内容。カナダは未成年者向けデータ保護基準を重視。あわせて G7 のデータ保護当局がパリで4日間のラウンドテーブルを開催し、AI のエンフォースメントと越境データ移転規制を議論した。

**影響**: 主要国による AI ガバナンスの方向性が「宣言」という形で明文化されたことで、透明性・倫理・データ保護・安全といった原則が国際的な参照点になる。具体的な拘束力や各国実装は今後の課題だが、規制動向のベースラインとして押さえる価値がある。

**行動指針**: グローバル展開を行う組織は宣言の原文（European Council ページ）を確認し、データ保護・越境移転・未成年者保護に関する論点を自社のAIガバナンス方針に照合しておくこと。

- https://www.cigionline.org/articles/%C3%A9vian-g7-summit-digital-economy-trade-and-emerging-technology/
- https://www.consilium.europa.eu/en/meetings/international-summit/2026/06/15-17/

### 3. Claude Code v2.1.178（6/15 stable）— パラメータ単位のツールブロック等の新権限構文、過去版表記を訂正

**事実**: Claude Code の最新 stable は **v2.1.178（6/15）**。**パラメータ単位でのツールブロックを可能にする新しい permission 構文**、ネストした skills のコンテキスト読み込み、classifier 評価の強化を導入。直前のダイジェストが「v2.1.176 が最新」と誤記していたが、実際には v2.1.177 / v2.1.178 が既にリリース済みだった。

**根拠**: 01_Master が公式 changelog（code.claude.com/docs/en/changelog）で確認。changelog 上位3バージョンを `.last-check-state.md` と突き合わせ、バージョン番号の飛びを検知するプロセスが推奨されている。

**影響**: パラメータ単位のツール制御は、エージェント運用時の最小権限設計（特定コマンドの特定引数だけを許可/拒否）を実装しやすくする実用的な改善。前日サマリーの「6/12 stable が最新のまま」という記述は本日の v2.1.178 確認で更新される。

**行動指針**: Claude Code を運用する組織は v2.1.178 へ更新し、新 permission 構文でツール呼び出しのパラメータレベル許可リストを見直すこと。

- https://code.claude.com/docs/en/changelog

## カテゴリ別まとめ

### Anthropic / Claude
- **Fable 5 / Mythos 5 の世界停止が6日目・政治問題化**（ハイライト参照）。市場は ~7月までの復旧確率を約75%と見込むが、Anthropic のパッチ適用が解除条件とされ確定日程なし
- 同盟国の反発が拡大（英MPの批判・UK carve-out 却下、仏=国産AI支援、EU=依存リスク警告、印=外国政府管理への懸念）

### Claude Code
- **v2.1.178（6/15 stable）が最新**（ハイライト参照）。パラメータ単位のツールブロック等の新 permission 構文を導入。前日サマリーの v2.1.176 表記は訂正

### Google / DeepMind
- **Gemini 3.5 Flash の機能トグルが 6/16 に全リージョンで廃止** — モデルがデフォルトで恒久的に有効化（個別 OFF 不可に） https://workspaceupdates.googleblog.com/
- **Gemini Spark が Workspace 連携機能を拡張中**（継続） https://gemini.google/release-notes/
- 6/18 に Gemini CLI / Gemini Code Assist IDE 拡張のサービス終了（Antigravity CLI 移行）

### Microsoft / GitHub
- **本日は Copilot Studio / M365 Copilot / Power Platform とも新規の一次発表なし**（02_Copilot 確認）。前日 6/16 GA の Work IQ API に続く新情報は未インデックス

### OpenAI / ChatGPT
- 本日固有の新規一次情報は薄め。既定の退役スケジュール（GPT-4.5 退役 6/27、GPT-5.2 / GPT-5.3-Codex の新規 API リクエスト不可化 6/30）が継続

### 規制・政策
- **G7エビアン・サミット 6/17 閉幕、「AI・サイバーセキュリティ宣言」採択**（ハイライト参照）。G7 データ保護当局がパリで4日間ラウンドテーブル（AI エンフォースメント・越境データ）

### 市場データ（前回から変化なし）
- **Similarweb AIトラッカー（2026年4月）**: ChatGPT 54.7%、Gemini 27.4%、Claude 8.2%（四半期306%増）、DeepSeek 4.1%、Grok 2.8%
- **MM総研（2025年8月調査）**: 生成AI個人利用率21.8%、市場規模2024年度1,679億円→2030年度5,618億円予測

## 直近の注目予定

- **6/18**: Gemini CLI / Gemini Code Assist IDE 拡張のサービス終了（Antigravity CLI 移行）
- **6/22**: Fable 5 が Pro/Max/Team/Enterprise の追加料金なし期間終了（※停止中のため実質保留）
- **6/22-26**: Gemini 3.5 Pro GA 推定ウィンドウ（最終週ドロップ予想・未確定）
- **6/23**: Fable 5 利用に usage credits 必要化（※停止中のため実質保留）
- **6/25**: gemini-3.1-flash-image-preview / gemini-3-pro-image-preview 廃止
- **6/27**: GPT-4.5 が ChatGPT から退役
- **6/30**: Devin クラシック環境セットアップ廃止 / GPT-5.2・GPT-5.3-Codex 新規 API リクエスト不可化 / Copilot Studio Teams クラシック作成終了・感度ラベルGA / Security Copilot E5 展開完了 / M365 価格ロックイン期限
- **〜7月（予測）**: Fable 5 / Mythos 5 の復旧（市場予測 約75%・未確定）
- **7/1**: M365価格改定発効（E3 $36→$39、E5 $57→$61、Copilot Business $18→$21）/ Cursor 新価格 / Devin Cascade 完全廃止
- **7/17**: Claude Corps 第1期応募締切
- **8/5**: Claude Opus 4.1 が Claude API から退役
- **8/26**: OpenAI Assistants API 廃止 / o3 退役

## 改善メモ

- **Fable 5 / Mythos 5 停止は政治・地政学イベントへ発展** — 「7月までに約75%復旧」は市場予測（Polymarket 等）であり Anthropic 公式の確定日程ではない。Sacks 発言（修正拒否）と Anthropic の反論（narrow な jailbreak）は両論併記が必要。Anthropic 公式（anthropic.com/news/*）の WebFetch 403 が3ソースとも継続しており、Bloomberg / Al Jazeera / Tom's Hardware / Business Today 等の大手メディアと政府発信のクロスチェックを推奨
- **changelog バージョン取りこぼしの再発防止** — 01_Master メモより、前回 v2.1.176 を最新と誤記（実際は v2.1.177 / v2.1.178 既出）。changelog 上位3バージョンを `.last-check-state.md` と突き合わせてバージョン番号の飛びを検知するプロセスを推奨
- **アグリゲータの誤日付に注意** — 03_industry メモより、Crescendo.ai 等が記事を誤った日付で掲載（例: Gemini 3.5 Flash を6/16表記だが実体は5/20、Meta capex ガイダンスは4月の旧情報、BMW ベンチャーファンドは6/16表記だが4/29発表）。一次ソースでの日付検証を徹底すること
- **RSS / WebFetch 403 継続** — 03_industry は全RSS（Google News、GIGAZINE、The Decoder、VentureBeat、Publickey、hnrss.org、Product Hunt、GitHub Trending）が403で WebSearch フォールバック。`daily-sources.md` を RSS より WebSearch 優先へ更新する推奨が継続
- **03_industry のローカルクローン停滞が再発** — 起動時ローカル main が 06-05 で停滞し origin/main（06-16）と乖離。常態化しているため起動時 `git pull origin main` を含む環境セットアップ見直しを強く推奨
- **本日は新規一次情報が少なめ** — 実質的な当日新規は Fable 5/Mythos 5 の続報（政治化）、G7 宣言採択、Gemini 3.5 Flash トグル廃止、Claude Code v2.1.178 確認が中心。Microsoft / OpenAI 側は当日固有の一次発表なし
