# AI News Daily Summary — 2026-06-23

> 本サマリーは 01_ai-news-Master・02_ai-news-Copilot・03_ai-news-industry の3ソース（6/23分）を統合して作成。火曜・主要ラボの新規モデル発表は引き続きなし。最大の動きは Google からの看板研究者2名の流出（Shazeer→OpenAI / Jumper→Anthropic）と、Fable 5 のトークン課金移行が停止中のまま予定どおり実行された点。

## 今日のハイライト

### 1. Google から看板研究者2名が48時間で流出 — Shazeer が OpenAI へ、Jumper が Anthropic へ

**事実**: Google の中核研究者2名が相次いで離脱した。**Noam Shazeer（Gemini co-lead, VP Eng）が OpenAI へ移籍（6/18 発表）**。"Attention Is All You Need"（2017, Transformer 論文）の共著者で、2024 年に Google が **$2.7B** で Character.AI から呼び戻したばかり、2 年未満での再離脱となる。続けて **John Jumper（AlphaFold 創出、2024 年ノーベル化学賞、DeepMind VP）が Anthropic へ移籍（6/19-20 発表）**。約 9 年在籍後の離脱で、Anthropic の生命科学・計算生物学への本格進出と整合する。役割は未開示。Anthropic は **6/30 にサイエンスイベント**を予定しており、Jumper 関連の発表の可能性がある。

**根拠**: CNBC / TechCrunch 等の一次報道に加え、本人の X 投稿も確認済みで信頼度は高い（01_Master）。Hassabis は X で Jumper に謝意を表明。構図としては **Anthropic が科学的正統性（ノーベル級）を、OpenAI が Transformer の生みの親を獲得**した形で、Google にとっては 48 時間で看板級2名の損失。

**影響**: フロンティアモデル各社の人材獲得競争が一段と激化していることを示す象徴的な動き。特に Anthropic の Jumper 獲得は、同社が LLM 単独から生命科学・科学計算へドメインを広げる戦略の本気度を裏付ける。モデル選定の中長期評価において、各社の研究人材ポートフォリオが差別化軸になりつつある。

**行動指針**: ベンダー評価では「現在のモデル性能」に加え、研究人材の集積動向を中期シグナルとして織り込む。Anthropic を科学・研究用途で評価している組織は **6/30 のサイエンスイベント**を注視し、Jumper 参画後のロードマップ更新を待つ。人材移籍系は一次報道＋本人投稿での裏取りを前提に扱うこと。

- https://www.cnbc.com/
- https://techcrunch.com/

### 2. Fable 5 / Mythos 5 停止12日目 — 復旧なしのまま本日 6/23 でトークン課金へ移行（実質使えないまま課金体系だけ先行）

**事実**: 6/12 17:21 ET の米輸出規制指令による Fable 5 / Mythos 5 の世界一斉停止は、**6/23 時点で12日目も未復旧**（3ソース一致）。全顧客で両モデルを無効化し **Opus 4.8 へ自動ルーティング**を継続（他 Claude モデルは影響なし）。一方で**予定どおり本日 6/23 から Fable 5 は Pro / Max / Team / シート型 Enterprise プランの無償包含を外れ、トークンクレジット課金（入力 $10/M・出力 $50/M）へ移行**した。停止が続く中で課金体系だけが先行移行する、ねじれた状態となっている。

**根拠**: 停止根拠について、報道で framing が明確化した。**Lutnick（Commerce 長官）は停止理由を「中国・ロシア等の懸念国による軍事インテリジェンス利用への懸念」と説明**。Anthropic 側は「バイパスで見つかる脆弱性は minor で、公開モデルでも発見可能なレベル」と反論しており、技術的見解の対立が継続している。Anthropic の Chris Ciauri（International MD）はソウル会見で「coming days で復旧する」と楽観発言を維持するが**公式復旧日は未発表**。なお Claude モバイルアプリのモデルピッカーには Fable 5 が表示されるが選択しても動作しない（失敗するか Opus 4.8 へ無言フォールバック）— UI 上の残骸であり部分復旧ではない（02_Copilot）。予測市場は **US 顧客向け復旧を 7/1 まで 57%、7/10 まで 67%、7/17 まで 75%** とし前回から変化なし。

**影響**: 復旧後に Fable 5 を使う前提だった組織は、無償枠を実質使い切れないまま従量課金（出力 $50/M は高水準）へ切り替わるため、復旧時のコスト試算を入れ替える必要がある。停止が長引く中、オープンウェイト系モデルが受け皿として動く動きも報じられており、長期化リスクは依然残る。標準プラン提供の復活は容量次第で日付未定。

**行動指針**: Fable 5 / Mythos 5 を本番に組み込む組織は復旧時期を「未定」と見なし、Opus 4.8 / GPT-5.5 フォールバック前提で運用継続。6/23 以降の従量課金（入力 $10/M・出力 $50/M）を前提にコスト試算を更新する。復旧情報は公式（claude.com/blog・anthropic.com/news）での明示確認を最優先とすること。

- https://www.anthropic.com/news/fable-mythos-access
- https://www.koreajoongangdaily.com/business/anthropic-confident-of-reenabling-mythos-fable-5-access-in-coming-days-executive/12727522

### 3. AWS Summit NYC 2026 — セキュリティAIエージェント「AWS Continuum」と「AWS Transform 継続的モダナイゼーション」を発表（プレビュー）

**事実**: AWS Summit New York 2026 で、エンタープライズ開発者向けの自律型 AI エージェント2製品が発表された。**「AWS Continuum」（限定プレビュー）**は、コードに加えインフラ構成・権限・ネットワークトポロジ・社内ドキュメント等を文脈に脆弱性を「推論」し、悪用可能性を立証して優先順位付け→既存プロセスで修正まで駆動するセキュリティエージェント群。ペネトレーションテスト／コードスキャン／脅威モデリングを束ね、既存 AWS Security Agent は Continuum 傘下に再編される。**「AWS Transform – continuous modernization」（プレビュー）**は、AI エージェントがリポジトリを常時自動スキャンし技術的負債を検出→修正→検証まで自律実行、CodePipeline / Jenkins / GitHub Actions / GitLab 等の既存パイプラインに接続して修正対象リポジトリへ自動で PR を生成する。

**根拠**: Publickey / InfoWorld / AWS 公式ブログの一次報道（03_industry）。Continuum の設計上の特徴は **特定 AI モデルに非依存（複数モデルを得意領域で使い分ける）**点で、Anthropic Fable 5 停止のようなベンダー単独障害のリスクを設計レベルで回避する思想がうかがえる。AWS Transform は所見生成を「数週間→数時間」に短縮すると主張。

**影響**: セキュリティと技術的負債削減という運用コストの大きい領域に、マルチモデル前提の自律エージェントが本格投入される流れ。モデル単独障害（Fable 5 停止が典型）が現実リスク化する中で、「モデル非依存」を明示する設計は調達側にとって安心材料となり、ベンダーロックイン回避の評価軸を後押しする。

**行動指針**: 脆弱性管理・モダナイゼーションを抱える組織は両プレビューの適用範囲・対応言語・課金体系を確認し、既存 CI/CD（GitHub Actions / GitLab 等）との接続前提で PoC を検討。特に「モデル非依存」設計の実効性（フォールバック挙動・精度のモデル間差）を評価項目に加えること。

- https://www.publickey1.jp/blog/26/awsaws_contiuumai.html
- https://aws.amazon.com/blogs/aws/proactively-reduce-tech-debt-autonomously-with-aws-transform-continuous-modernization-preview/

## カテゴリ別まとめ

### Anthropic / Claude・規制
- Fable 5 / Mythos 5 停止12日目・Lutnick の停止根拠「懸念国の軍事インテリジェンス利用」が明確化・本日 6/23 でトークン課金へ移行（ハイライト2参照）
- John Jumper（AlphaFold / ノーベル化学賞）が Anthropic へ移籍、6/30 サイエンスイベント予定（ハイライト1参照）

### Claude Code
- **v2.1.186（最新）**: **MCP サーバー認証用 CLI コマンドを追加**（対話メニューを開かず `claude mcp login/logout` 系で認証可能）、Bash コマンドが自動的に Claude 応答をトリガー（settings で設定可）、スリープ/復帰後のストリーミング失敗を修正。その他: workflows エージェント詳細ビューにステータスフィルタ、プラグイン Installed タブに「Skills」セクション、teammate モードの `iterm2` 設定（自動検出対応）、`CLAUDE_CODE_MAX_RETRIES` 上限を 15 に調整、バックグラウンドサブエージェントの権限プロンプトをメインセッションに表示。https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md

### OpenAI
- **GPT-5.6 ローンチ予測ウィンドウ継続中（窓2日目）**: Polymarket は 6/22-28 のローンチに **83%**。Pachocki「GPT-5.5 比 meaningful leap、効率・安全性重視」（6/16）。コンテキスト ~1.5M token への拡張観測。**公式日付・system card・API 文字列は依然未発表**
- **ChatGPT リリースノート（直近）**: サイドバーから chats / projects を pin（Pinned セクションに両方表示）、共有が 1 クリックフロー化（別ポップアップ廃止）、iOS 写真アップロード高速化。GPT-5.2 は 6/12 に ChatGPT から退役済み（既存会話は GPT-5.5 へ）

### Google / DeepMind
- **Gemini 3.5 Pro は依然 GA 待ち**: 6 月後半も Vertex AI 限定プレビューのみで、消費者向け Gemini アプリ / AI Studio 未提供（Pichai「来月まで待って」）。2M context / Deep Think。予測市場の「6/30 までの GA」確率は約 50〜55% で月内ずれ込みの可能性。https://aiweekly.co/alerts/gemini-35-pro-eyes-june-ga-with-2m-context-and-deep-think
- Noam Shazeer（Gemini co-lead, Transformer 共著者）が OpenAI へ移籍、看板研究者2名流出の一角（ハイライト1参照）
- Google Workspace（6/17-18・既報）: Gemini に Google Classroom 連携を全面展開、temporary chats / 会話削除の管理者制御、Google Vids アバター 23→53 種拡張

### Microsoft / GitHub
- **新規一次情報なし（静穏継続）**: Copilot Studio What's New（最新 May 2026）、Power Platform ブログ（最新 6/11）、M365 Copilot リリースノート（最新 6/16 バッチ）、Tech Community「What's New in M365 Copilot」（6 月号未公開）いずれも変更なし
- **Microsoft Copilot Cowork が従量課金（消費ベース）へ移行＋モデル選択解禁（6/16 GA・既報）**: エージェント処理を「per-agent 計算ユニット」課金化、M365 Copilot 顧客が初めて基盤 LLM を選択可能（GPT-4o・Phi-3 系で開始）。Azure 上で DeepSeek の MS ホスト版を低コスト選択肢として評価中との報道も。https://windowsnews.ai/article/microsoft-debuts-copilot-cowork-in-general-availability-shifting-to-consumption-pricing-and-model-fl.427613

### 開発者ツール・エンタープライズAI
- AWS Continuum（セキュリティAIエージェント、モデル非依存）/ AWS Transform 継続的モダナイゼーション（自律 PR 生成）を AWS Summit NYC 2026 で発表（ハイライト3参照）
- **Cursor v3.8（6/18・既報）**: Automations 強化（`/automate` skill、GitHub/Slack 新トリガー、computer use デフォルト有効）。新規変更なし
- GitHub Copilot: 全プラン usage-based billing + AI Credits へ移行済み（6/1）

### AI 業界トレンド（提案根拠用）
- **市場シェア（Similarweb・2026年4月）**: ChatGPT 54.7%、Gemini 27.4%、Claude 8.2%、DeepSeek 4.1%、Grok 2.8%（変化なし）

## 直近の注目予定

- **6/23（本日）**: Fable 5 がトークン課金へ移行（入力 $10/M・出力 $50/M）・利用に usage credits 必要化（※停止継続で実質無効）
- **6/25**: gemini image preview（gemini-3.1-flash-image-preview / gemini-3-pro-image-preview）廃止
- **6/27**: GPT-4.5 が ChatGPT から退役
- **6/30**: Anthropic サイエンスイベント（Jumper 関連の可能性）/ GPT-5.2・GPT-5.3-Codex 新規 API リクエスト不可化 / Devin クラシック環境セットアップ廃止 / Copilot Studio for Teams クラシック作成終了 / 感度ラベル表示 GA / Security Copilot E5 展開完了 / M365 価格ロックイン期限
- **〜7/1（予測・未確定）**: Fable 5 / Mythos 5 の US 顧客向けアクセス復旧（市場本命 57%）
- **7/1**: M365 価格改定発効（E3 $36→$39、E5 $57→$61、Copilot Business $18→$21）/ Cursor 新価格 / Anthropic Claude Partner Network 初回階層昇格レビュー / Devin Cascade 完全廃止
- **7/10 / 7/17**: Fable 5 復旧予測の中間マイルストーン（67% / 75%）
- **7/17**: Claude Corps 第1期応募締切
- **8/5**: Claude Opus 4.1 が Claude API から退役
- **8/26**: OpenAI Assistants API 廃止 / o3 退役

## 改善メモ

- **人材移籍系（Shazeer / Jumper）は信頼度高**: CNBC / TechCrunch 等の一次報道に加え本人の X 投稿も確認済み（01_Master）。Anthropic の 6/30 サイエンスイベントで Jumper 関連の発表があるか要追跡。
- **Fable 5 の課金移行と停止のねじれが本日確定**: トークン課金移行（6/23）は予定どおり実行されたが、モデルは停止12日目で実質使えないまま。Lutnick の停止根拠「懸念国の軍事インテリジェンス利用」と Anthropic の「脆弱性は minor」反論で技術的対立が継続。復旧ウォッチ継続。
- **WebFetch / RSS 403 が全ソースで継続**: anthropic.com / github.blog / cursor.com / mc.merill.net、および全 RSS（Google News / GIGAZINE / The Decoder / VentureBeat / Publickey / hnrss / Product Hunt / GitHub Trending / llm-stats / pricepertoken）が 403。各ソースとも WebSearch ＋ raw.githubusercontent.com / 大手メディアでフォールバック（成功）。`daily-sources.md` の取得方法欄を「WebSearch 優先」へ更新する推奨は複数日継続。
- **起動時のローカル main 乖離が連日再発（入力3リポ側）**: 01_Master・03_industry がともに「開始時にローカル main が 06-05 で停滞し origin/main と乖離（28コミット）」を報告（06-15 以降ほぼ連続）。各リポで SessionStart hook に `git fetch && git reset --hard origin/<branch>` を導入する運用への恒久化を強く推奨。
- **AWS Summit NYC 2026 を一次情報源として追加検討**: 開発者ツール・セキュリティの有用な一次情報源。年次イベントとして `daily-sources.md` の重点確認時期への追加を検討（03_industry 提案）。
</content>
</invoke>
