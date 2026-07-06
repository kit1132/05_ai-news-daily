# AI News Daily Summary — 2026-07-07

> 本サマリーは 01_ai-news-Master・02_ai-news-Copilot・03_ai-news-industry の3ソース（7/7分）を統合して作成。

火曜。**大型発表なしの静かな一日だが、実務に効く節目が2つ**。本日発効の Anthropic Fable 5「無償枠終了→従量課金」移行と、前日まで「7/7に約74%」で織り込まれていた GPT-5.6 広域GAの空振り（市場は7/9へ再プライシング）。開発ツールでは Copilot CLI に LLM 判定ベースの自動承認モードが入り、運用上の注目度が高い。

## 今日のハイライト

### 1. Anthropic Fable 5、本日 7/7 に無償枠終了 → usage credits（従量課金）へ移行 — 未有効化テナントはアクセス不可

**事実** Fable 5 の暫定「週次利用上限の最大50%まで無償利用可」枠が **本日 7/7 で終了**。以降は **usage credits（API 準拠レート＝入力 $10／出力 $50 per M tokens）** での従量利用に移行する。Pro/Max/Team/一部 Enterprise が対象で、**credits 未有効化のテナント／シートは Fable 5 へアクセス不可**になる。標準 Enterprise シートに無償枠はなく、credits 有効化が前提。

**根拠** 商務省による 6/30 の輸出規制解除を受けた 7/1 グローバル復帰時の導入枠が期限を迎えた形。Anthropic は「capacity が回復し次第サブスク標準機能へ戻す一時措置」と説明。3ソースとも本日発効で一致（industry は課金開始を「7/8 から」と表記＝実質同義）。

**影響** これまで無償枠内で Fable 5 を回していたワークロードのコスト構造が本日から変わる。credits を有効化していないテナントは即アクセス断のリスクがあり、Claude 常用チームは本日以降のコスト増に直面する。

**行動指針** Fable 5 / Mythos 5 利用テナントは usage credits の有効化状況を即確認。従量課金前提でコスト試算・予算枠を再設定し、無償枠依存だったバッチ処理は優先度を棚卸しする。

- https://www.anthropic.com/news/redeploying-fable-5
- https://www.searchenginejournal.com/anthropics-claude-fable-5-is-back-with-new-usage-limits-and-safeguards/581231/
- https://releasebot.io/updates/anthropic

### 2. GPT-5.6 広域GAは 7/7 も空振り — 予測市場は「7/9」へ再プライシング、実質ゲートは 8/1 の政府枠組み確定

**事実** 前日（7/6）は Polymarket が 7/7 を約74%で織り込んでいたが、**7/7 も限定プレビュー（米政府承認の約20組織・API＋Codex）のまま経過し広域GAは実現せず**。「GPT-5.6 released on…?」市場は **7/9 が約59%で首位**（7/7 残り約12%・7/14 が続く）に再プライシングされた。個人 ChatGPT への搭載可否・提供プランは依然未確定。

**根拠** ゲートは日付ではなく、6/2 大統領令（EO 14409）に基づく **任意フレームワークの finalize（8/1 期限）**。公開前に最大30日、政府が事前アクセス・協働で信頼パートナーを選定する枠組みで、AIサイバーセキュリティ・クリアリングハウスは 7/2 設置期限、枠組み本体は 8/1 に確定予定。「GA の遅延＝モデル性能ではなく政府枠組みの確定待ち」という構図。

**影響** フロンティアモデルの出荷カレンダーを規制枠組みが実質規定する構図が一段と鮮明に。GA 日を前提にした導入・評価計画は繰り返し後ろ倒しされるため、日付ベースの計画立ては引き続きリスク。

**行動指針** 7/9 前後の OpenAI 公式アナウンスを監視しつつ、実質ゲートである 8/1 の枠組み確定をマイルストーンに据える。API/Codex 利用チームは GA 後のモデル切替・価格・レート制限変更に備える。

- https://polymarket.com/event/gpt-5pt6-released-onptptpt-20260623051439980
- https://www.whitehouse.gov/presidential-actions/2026/06/promoting-advanced-artificial-intelligence-innovation-and-security/
- https://en.wikipedia.org/wiki/GPT-5.6

### 3. GitHub Copilot CLI に「自動承認モード」— LLM ジャッジが許容可と判断したリクエストを自動許可

**事実** GitHub Copilot CLI の pre-release で **auto allow-all モード**（LLM ジャッジが許容可と判断したリクエストを自動承認）と `stayInAutopilot` 設定（継続 autopilot 運転）が追加された（**v1.0.69-1・7/4**）。加えて **v1.0.69-2（7/6）** で `/rubber-duck` の pre-auth ヘルプ表示、MCP サーバの CLI OAuth 認証、新規ディレクトリのファイル追跡・プロンプトスクロールの修正。安定版は v1.0.68（7/1）のまま。

**根拠** GitHub の Copilot CLI releases が一次ソース。OpenAI Codex CLI も pre-release 0.143.0-alpha.37（7/6）を日次で刻むが機能追加は小粒、Claude Code は v2.1.201（7/3）で新版なし。

**影響** LLM 判定ベースの自動承認は、エージェント運用の摩擦を下げる一方で、承認ゲートを AI に委ねることになる。CI やローカル自動化で使う場合、意図しないコマンド実行・ファイル変更のリスク評価が必要。

**行動指針** pre-release のため本番導入は慎重に。まずサンドボックス／権限を絞った環境で挙動を検証し、auto allow-all の適用範囲（許可コマンド・ディレクトリ）を明示的に制限してから採用する。

- https://github.com/github/copilot-cli/releases
- https://github.com/openai/codex/releases

## カテゴリ別まとめ

### Anthropic / Claude
- **Fable 5 usage credits 移行（本日発効）**（ハイライト参照）。Fable 5/Mythos 5 仕様は据え置き（1M context / 128k output / $10・$50）
- **Anthropic × Samsung、独自AIチップを協議（7/2・補足掲載）**: The Information/TechCrunch/Bloomberg 報。Samsung の 2nm プロセスと先端パッケージング活用を評価するも用途・仕様・電力性能は未定の「予備協議」段階で、量産・出荷は早くて 2027 年後半。元 OpenAI チップ設計チームの Clive Chan が Anthropic に合流。Anthropic は「Google/Amazon/Nvidia を含む多様なハードスタックが引き続き中核」とコメント。OpenAI「Jalapeño」（6/24・Broadcom 協業）に続き主要ラボが揃って脱 Nvidia・自社シリコンへ動く構図。 https://techcrunch.com/2026/07/02/anthropic-is-discussing-a-new-custom-chip-with-samsung/
- **Claude Science**（6/30 GA）継続。**Claude Code** は v2.1.201 が最新のまま（github raw CHANGELOG 一次確認、7/6 から新版なし）

### OpenAI / フロンティアモデル
- **GPT-5.6 広域GA 空振り・7/9 へ再プライシング**（ハイライト参照）。Sol/Terra/Luna は約20組織限定プレビュー継続、一般提供「数週間内」、価格据え置き（Sol $5/$30・Terra $2.5/$15・Luna $1/$6）

### 開発ツール
- **Copilot CLI 自動承認モード**（ハイライト参照）
- **GitHub Copilot（本体）**: 7/2 changelog（CLI が Actions で PAT 不要・エージェントセッションストリーミング Public Preview・AI credit pools 等）と 7/1 の Vision GA／Browser tools GA が最新。7/3 以降の新規 changelog なし
- **Cursor**: 3.9（Customize ページ・6/22）と iOS 公開ベータ（6/29）が最新。Team MCP 配布も既報。新規なし
- **Devin**: Security Swarm（7/1）が最新。Devin Desktop（旧 Windsurf）は auto-reconnect／reviewable diffs 等の細かな改善継続。7/3 以降の大型発表なし

### Microsoft / Copilot Studio
- **Copilot Studio 基盤（Released Versions）**: 最新は Build 2026.6.3（6/30初出）のまま。**版ページは火曜更新だが本日時点で次ビルド（2026.7.x）は未反映**（日中に反映される可能性あり・要再確認）。リージョン展開も 7/6 から変化なし（Preview 系11リージョンが 2026.6.3、UK/Asia/Japan/Europe/UAE が 2026.6.2、US 本体/Australia/GCC が 2026.6.1）
- **Copilot Studio - What's New**: June 2026 セクションのまま7月項目なし（Learn MCP 一次確認）
- **M365 Copilot Release Notes**: July 01 バッチ（透かし／秘密度ラベル継承／エージェントのスケジュール実行／Outlook Copilot Chat のメールボックス・予定表全体への拡大／PowerPoint Agent Mode で Teams 会議・チャット参照）が最新。次バッチは隔週傾向で **7/14〜7/15 前後見込み**
- **Power Platform Blog**: 「What's New in Power Platform: July 2026」は未公開（最新は 6/11 の June 2026 Feature Update）。月内早めに出る傾向のため要監視
- **Message Center / Roadmap**: 7/3 以降の新規 MC 番号は未検出（一次の網羅は手動確認推奨）

### 国内データ
- **JUAS「企業IT動向調査2026」速報 — 生成AI 導入済み33.9%、超大企業は85.1%**: JUAS（日本情報システム・ユーザー協会）が東証上場企業等4,500社対象（有効回答957社・調査期間2025年9〜10月）の速報を公開。言語系生成AI「導入済み」33.9%、試験含め53.4%、売上1兆円以上は85.1%が導入済み。国内エンプラの生成AI浸透度・企業規模別の導入格差を提案資料で引用できる一次データ。 https://prtimes.jp/main/html/rd/p/000000013.000160762.html / https://juas.or.jp/news/topics/6124/

### 継続ウォッチ（変化なし）
- **Google Gemini 3.5 Pro**: 7月第2週入りもなお限定プレビュー。GA 日・公開ベンチマーク・確定価格いずれも未発表（Google 広報ノーコメント）。2M トークン文脈・Deep Think は $250/月 Ultra 想定で据え置き。一部報道で 7/17 説。 https://www.marketscale.com/industries/software-and-technology/gemini-3-5-pro-still-in-preview-what-enterprise-teams-evaluating-a-model-should-do-now
- **xAI / Grok**: Voice Agent Builder ベータ（7/1・$0.05/分）・Grok Build への `/voice` 統合（7/2）は既報。Musk が「Grok Imagine 完了」を投稿（7/5）。旗艦 Grok 5（噂 6T）未出荷

## 直近の注目予定

- **7/8** Anthropic 政府発行 ID・生体検証ポリシー施行（Fable 5 課金開始も実質この前後）
- **7/9** GPT-5.6 広域GA見込み（予測市場 約59%）
- **7/13** Claude Code の週次上限+50%プロモ（5月開始）の期限（延長なき場合）
- **7/14** 破壊的変更: Visio → Power Automate エクスポート廃止発効／M365 Copilot Release Notes 次バッチ見込み
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

- **前日（7/6）欠損の 01_ai-news-Master が本日取得可能に**: 7/6 サマリーで未取得だった Master の 7/6 分ダイジェストが取得できたため、7/6 サマリーを3ソースで再生成・上書き（別コミット）した。ソース側ルーチンの遅延は解消済み。
- **RSS/WebFetch 全ソース403継続**（03_industry）: WebSearch で収集。取得方法の WebSearch 優先化提案（B-004）が8回目の継続。
- ソース間で本日の Fable 5 usage credits 移行・GPT-5.6 GA 空振りの記述が一致。矛盾は検出されず（industry の課金開始「7/8」表記は Master/Copilot の「7/7 発効」と実質同義）。
