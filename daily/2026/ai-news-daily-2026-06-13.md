# AI News Daily Summary — 2026-06-13

> 本サマリーは 01_ai-news-Master・02_ai-news-Copilot・03_ai-news-industry の3ソース（6/13分）を統合して作成。

## 今日のハイライト

### 1. OpenAI が Ona（旧 Gitpod）を買収 — Codex の常駐型クラウドエージェントでエンタープライズ防衛を強化

**事実**: OpenAI は 6/11、クラウド開発環境スタートアップ Ona（旧 Gitpod）の買収を発表した。Ona は安全な分離クラウドサンドボックスを提供し、開発者がワークステーションを閉じてもエージェントの作業が継続する。これにより Codex の長時間ジョブ（従来の分単位から数時間〜数日規模）を顧客自身のクラウド内で実行可能にする。買収額は非開示で規制当局の承認待ち。Ona チームは CEO Johannes Landgraf 氏を含め全員が Codex グループへ合流する。

**根拠**: 本買収は 6/11 の Oracle Cloud 提携に続く Codex エコシステム拡張であり、「エージェントが常駐し、ユーザー環境とは独立して長時間稼働する」というアーキテクチャへの明確な投資を示す。Anthropic が Claude Code でエンタープライズ統制（後述の `enforceAvailableModels` 等）を固める中、OpenAI は「顧客クラウド内で完結する常駐エージェント」という対抗軸を取った。

**影響**: エンタープライズの AI コーディング基盤の競争軸が、対話レイテンシから「分離環境での長時間自律実行」へ移りつつある。Codex を検討中の組織は、自社クラウド（特に Oracle/顧客 VPC）内でのエージェント常駐実行という選択肢が現実味を帯びる。Claude Code・Cursor・Devin との比較では「セルフホスト型サンドボックスの有無」が新たな評価軸になる。

**行動指針**: 長時間バッチ的なコード生成・リファクタリングを自社クラウド内で完結させたい場合は、Codex + Ona の GA 時期と対応クラウドを追跡する。規制当局の承認待ちのため正式提供時期は流動的であり、現時点では PoC 段階にとどめ、データ境界（顧客 VPC で完結するか）を契約前に確認する。

- https://siliconangle.com/2026/06/11/openai-acquires-ai-agent-orchestration-startup-ona/
- https://www.techzine.eu/news/devops/142087/as-anthropic-claims-the-enterprise-openai-fights-back-with-ona-deal/

### 2. Anthropic が「Claude Corps」を始動 — $150M で 1,000 名のフェローを米国の非営利団体へ 12 か月配置

**事実**: Anthropic は総額 $150M の「Claude Corps」プログラムを発表した。1,000 名のフェローを米国の非営利団体に 12 か月間配置し、参加者には「年収 $85,000 + Claude トークン予算」を提供する。応募締切は 7/17、最初の 100 名は 2026 年 10 月に活動を開始する。

**根拠**: 単なる助成ではなく「人材を実地配置 + ツール予算付与」という構造で、非営利セクターに Claude の実運用を埋め込む設計になっている。$150M / 1,000 名という規模は、AI ベンダーによる社会実装プログラムとしては大型の部類で、Anthropic の「公共・社会インフラ領域での定着」戦略を反映する。

**影響**: 非営利団体にとっては実務人材と AI ツールを同時に確保できる機会となる一方、Anthropic にとっては公共セクターでの Claude 利用実績とユースケースの蓄積につながる。OpenAI/Google の類似プログラムとの差別化が進む。

**行動指針**: 米国非営利団体で AI 活用を検討している場合は 7/17 の締切までに応募を検討する。フェロー側（個人）も同締切。日本の組織は対象外の可能性が高いため、応募条件（米国所在・対象団体の定義）を一次情報で確認する。

- （出典: 01_ai-news-Master 6/13 ダイジェスト）

### 3. Power Platform「June 2026 Feature Update」公開 — ガバナンスとエージェント運用系の GA が一斉到来

**事実**: 6/11、未公開だった 6 月の月次 What's New 記事が公開された。ガバナンスとエージェント運用系の GA が中心。主な GA: ①Power Apps MCP Server クローズドループ学習（エージェントがユーザーの修正を agent feed 経由で自動学習し構造化メモリとして保持）、②高度なコネクタポリシー（AI ツールが使うコネクタを「アクション・内部 MCP サーバー」単位でガバナンス可能）、③Power Automate デスクトップフローのバージョン比較、④Release Planner Code App（code apps + React のサンプル）。Public Preview として Power Platform インベントリにコネクタ利用データが追加され、コネクタ廃止・変更の影響範囲を全リソースで特定可能になった。

**根拠**: 今回の更新は「エージェントの自律学習（クローズドループ学習）」と「大規模統制（アクション/MCP 単位のポリシー）」を同時に GA させており、エージェント運用の現場ニーズ — 自動改善とガバナンスの両立 — に正面から応えている。インベントリのコネクタ利用可視化は、コネクタ廃止時の影響範囲特定という運用上の実需に直結する。

**影響**: Power Platform 上でエージェントを本番運用している組織は、コネクタ単位・MCP サーバー単位での統制を即適用できる。クローズドループ学習の GA により、ユーザー修正を手動でプロンプトに反映する運用から、自動学習を前提とした運用設計へ移行できる。

**行動指針**: ガバナンス担当は「高度なコネクタポリシー」を棚卸しし、AI ツールが利用するコネクタ/MCP の許可範囲を再定義する。エージェント運用者はクローズドループ学習を有効化する前に、agent feed に流れる修正データの取り扱い（学習対象の範囲）を確認する。

- https://www.microsoft.com/en-us/power-platform/blog/2026/06/11/whats-new-in-power-platform-june-2026-feature-update/

## カテゴリ別まとめ

### Anthropic / Claude
- **Claude Corps（$150M / 1,000 フェロー）**（ハイライト参照）。
- **Claude Code v2.1.174 / v2.1.175（6/12）**: v2.1.175 で `enforceAvailableModels` 管理設定を追加。有効時、`availableModels` 許可リストが Default モデルも制約し、ユーザー/プロジェクト設定で管理リストを拡大できない（エンタープライズのモデルガバナンス強化）。v2.1.174 は `/model` ピッカーの表示修正、「Fable 5 がクレジット消費中」バナーの従量課金エンタープライズでの誤表示修正、Bedrock GovCloud 推論プロファイルの 400 エラー修正、バックグラウンドセッションの `ANTHROPIC_*` 環境変数継承問題の修正、`wheelScrollAccelerationEnabled` 追加。VS Code の `/usage` にサブエージェント・スキル・MCP 別の利用内訳（24時間/7日窓）を追加。https://code.claude.com/docs/en/changelog
- **Fable 5 安全議論が継続**: 機微なクエリでの Opus 4.8 への自動フォールバックをセキュリティ研究者が批判。Anthropic は複数リクエストにまたがる攻撃検知のため「30 日保持ポリシー」を文書化（6/12 の Microsoft 社内利用制限と同一論点）。

### OpenAI
- **Ona（旧 Gitpod）買収**（ハイライト参照）。6/11 の Oracle Cloud 提携に続く Codex エコシステム拡張。

### Google / DeepMind
- **Gemini 3.5 Pro が未リリースのまま**: 5 月のコミットにもかかわらず未提供。市場予想では 6 月下旬（6/22-26 が GA 想定窓）の投入、2M トークンコンテキストと deep thinking 機能が見込まれる。

### Microsoft / GitHub / Copilot Studio
- **Power Platform June 2026 Feature Update**（ハイライト参照）。
- **Copilot Studio Build 2026.5.5（6/9 first available）**: A2A プロトコルで `tasks/get`（外部エージェントが現在のタスク状態を取得可能）、GPT-5.5 Chat でインラインエージェント実行、環境レベルの平均エージェント品質・健全性メトリクス表示、評価シナリオでプロンプト単位のクライアント側モデレーションレベル設定、es-PR（プエルトリコ・スペイン語）GA。**セキュリティ強化**: Anthropic レスポンスのエラー詳細をログから秘匿、情報バリア有効テナントでの Embedded Knowledge 利用エージェントの共有制限、AI 生成 URL の抑制/無害化を既定有効化、Agent Status が DLP 違反詳細を表示。**破壊的変更**: カスタムメトリクス分析サマリに label trend・over-time フィールドが常時含まれる（空でも）。日本は引き続き 2026.5.4。https://learn.microsoft.com/en-us/power-platform/released-versions/copilotstudio/2026.5.5

### 資金調達・IPO
- **Mistral AI、€20B 評価で €3B 調達交渉中**（6/12 報道、Bloomberg/TechCrunch）: 昨年 9 月の Series C（€11.7B、ASML が €1.3B 出資・11% 取得）からほぼ倍増。欧州ソブリン AI の旗手として計算資源競争に対応する資金。協議は初期段階で条件・評価額は変動の可能性あり。https://techcrunch.com/2026/06/12/mistral-is-rumored-to-be-raising-e3b-at-e20-valuation/ / https://www.bloomberg.com/news/articles/2026-06-12/france-s-mistral-in-funding-talks-at-about-20-billion-valuation

### 規制・政策
- **G7 サミット（フランス）に AI3 社トップが出席へ**（6/12 報道、Bloomberg）: 来週フランス開催の G7 に OpenAI の Sam Altman、Google DeepMind の Demis Hassabis、Anthropic の Dario Amodei が揃って参加予定。AI 規制・国際協調・計算資源を各国が「国家インフラ」として扱う流れの中での会合。https://www.bloomberg.com/news/articles/2026-06-12/anthropic-openai-google-executives-plan-to-attend-g7-summit

### 市場データ（前回から変化なし）
- **Similarweb AI トラッカー（2026 年 4 月時点）**: ChatGPT 54.7%、Gemini 27.4%、Claude 8.2%（四半期 306% 増）、DeepSeek 4.1%、Grok 2.8%。
- **MM 総研（2025 年 8 月調査）**: 生成 AI 個人利用率 21.8%、市場規模 2024 年度 1,679 億円 → 2030 年度 5,618 億円予測。

## 直近の注目予定

- **6/15**: Anthropic Sonnet 4 / Opus 4 API 退役 / Programmatic Credit Pool 有効化 / Agent SDK 課金分離（オプトイン必要）
- **6/16**: Work IQ APIs GA 予定 / M365 Copilot Release Notes 次回更新見込み
- **6/22**: Fable 5 Pro/Max/Team/Enterprise 無料期間終了
- **6/22-26**: Gemini 3.5 Pro GA 想定窓
- **6/30**: Copilot Studio Teams クラシック作成廃止・感度ラベル GA / Devin Classic 環境セットアップ廃止 / Security Copilot E5 展開完了 / M365 価格ロックイン期限
- **7/1**: M365 価格改定発効 / Cursor 新価格 / Devin Cascade 完全削除
- **7/17**: Claude Corps 応募締切（フェロー・団体）
- **2026 年 10 月**: Claude Corps 最初の 100 名が活動開始

## 改善メモ

- **[03_ai-news-industry]** 全 RSS フィード（Google News、GIGAZINE、The Decoder、VentureBeat、Publickey、hnrss.org、Product Hunt、GitHub Trending）が引き続き 403。全ソース WebSearch フォールバックで対応。
- **[03_ai-news-industry]** OpenAI Ona 買収（6/11）は前日（6/12）ダイジェストで Oracle 提携のみ掲載し Ona 分が漏れていたため本日掲載。日付・取りこぼし確認の重要性を再確認。
- **[03_ai-news-industry]** Microsoft India $17.5B 投資は WebSearch 上位に出たが 2025 年 12 月発表の既報のため除外。
- **[02_ai-news-Copilot]** フォールバック発生なし（Power Platform Blog / Copilot Studio Released Versions とも WebFetch・Microsoft Learn MCP で取得成功）。M365 Copilot Release Notes は 6/2 が最新のまま（次回 6/16 頃見込み）、Tech Community「What's New | June」も未公開。
- **[01_ai-news-Master]** Gemini 3.5 Pro が 5 月コミットから未リリースのまま。リリース確認を継続。
- **ソース間整合**: `enforceAvailableModels`（Claude Code v2.1.175）は 01_ai-news-Master と 02_ai-news-Copilot の両方に出現。本サマリーでは Anthropic / Claude カテゴリに統合。Fable 5 の 30 日 retention 論点も両ソースで一貫しており矛盾なし。
