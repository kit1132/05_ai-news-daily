# AI News Daily Summary — 2026-06-19

> 本サマリーは 01_ai-news-Master・02_ai-news-Copilot・03_ai-news-industry の3ソース（6/19分）を統合して作成。

## 今日のハイライト

### 1. Fable 5 / Mythos 5 停止8日目 — Anthropic幹部「近日中に再開」と楽観、発端は「Amazon の Mythos jailbreak 通報」と判明

**事実**: 6/12 17:21 ET の米輸出規制指令に端を発した Fable 5 / Mythos 5 の世界一斉停止は **6/19 時点も未復旧（8日目）**。Anthropic は全顧客で両モデルを無効化し **Opus 4.8 へ自動ルーティング**を継続（他 Claude モデルは影響なし）。Anthropic International 担当 MD の **Chris Ciauri 氏がソウル記者会見で「近日中（in the coming days）にモデルは再び利用可能になると非常に確信している」と明言**（6/18）。一方、確定した deal・復旧タイムラインの公式発表は 6/19 時点でなし。

**根拠**: 発端の新事実として、**Amazon の研究者が Mythos の安全機構をジェイルブレイクで突破**し、Andy Jassy CEO が直接米当局に脆弱性を通報したことが White House のシャットダウン命令の引き金だったと判明（Fortune 6/14）。規制対象は「ソフトウェア脆弱性特定など cyber 関連タスクの safeguard バイパス」。予測市場（Kalshi / Polymarket）は **US 顧客向け復旧を 7/1 までに 57%、7/10 までに 67%、7/17 までに 75%** と見込み、幹部発言が前倒し方向に作用する可能性。

**影響**: 単一フロンティアモデル依存リスクが地政学イベント化。発端が「Amazon による競合モデルの脆弱性通報」と明らかになったことで、安全性検証と競争・通報インセンティブが絡む構図が浮上。会社側が公に復旧を確信する段階に進み、解除は時間の問題との見方が強まる一方、6/22-23 のクレジット移行など既定日程は「停止中ゆえ要再確認」。

**行動指針**: Fable 5 / Mythos 5 を本番に組み込む組織は復旧時期を依然「未定」と見なし、Opus 4.8 / GPT-5.5 フォールバック前提で運用継続。Anthropic 公式＋大手メディア（Korea JoongAng Daily / Fortune / KED Global）＋予測市場を毎日クロスチェックし、「近日中」発言の具体化（公式リリース）を待って復旧を確認すること。

- https://www.koreajoongangdaily.com/business/anthropic-confident-of-reenabling-mythos-fable-5-access-in-coming-days-executive/12727522
- https://fortune.com/2026/06/14/how-a-warning-from-amazon-led-the-white-house-to-shut-down-anthropics-mythos-model/

### 2. Anthropic がソウルオフィス開設＋韓国大手と一斉提携 — APAC 3拠点目、IPO 前のアジア拡大

**事実**: **6/17-18、Anthropic が東京・ベンガルールに次ぐ APAC 3拠点目としてソウルオフィスを正式開設**（責任者 KiYoung Choi）。IPO 前のアジア事業拡大と、米輸出規制下での「AI 主権」対応を兼ねた布石。

**根拠**: 韓国大手の Claude 導入を一挙発表 — **NAVER**（全エンジニア組織に Claude Code）、**Samsung SDS**（Samsung Electronics 全体で Claude Cowork / Claude Code）、**LG CNS**（LG Group 全体に Claude）、**Nexon**（ライブサービスゲーム開発で Claude Code）、**Hanwha Solutions**（AWS Bedrock 経由・in-region データ管理）、**Channel Corp**（230,000+ 事業者の Channel Talk に Claude）。さらに **科学技術情報通信部（MSIT）と AI 安全性で MOU 締結**、国家 AI 研究ラボ **NAIRL**（KAIST / 高麗大 / 延世大 / POSTECH）の研究者最大 60 名に Claude を提供。

**影響**: Fable 5 停止で「単一国・単一ベンダー依存」リスクが顕在化する中、in-region データ管理（Hanwha の Bedrock 経由）や国家研究機関連携を前面に出すことで、地政学リスクを織り込んだエンタープライズ展開モデルを提示。IPO（6/1 予備目論見書提出済み）を控えた APAC 商用基盤の厚みづくり。

**行動指針**: 日本・韓国のエンタープライズで Claude 導入を検討する組織は、in-region データ管理や Bedrock 経由のデータ統制パターンを調達要件の参考にできる。Samsung SDS / LG CNS など SI 経由の大規模展開事例として動向を追跡。

- https://www.anthropic.com/news/seoul-office-partnerships-korean-ai-ecosystem
- https://www.kedglobal.com/artificial-intelligence/newsView/ked202606180004

### 3. GitHub Copilot デスクトップアプリが GA（6/17）— エージェント駆動開発の「拠点」へ

**事実**: **GitHub Copilot アプリが macOS / Windows / Linux で正式 GA**。Issue / PR / プロンプトからセッションを開始し、差分レビュー → 既存チェック / マージ要件で PR 作成まで一気通貫の、エージェント駆動開発のデスクトップ拠点という位置づけ。

**根拠**: 主要機能は **Canvases**（計画・PR・ターミナル・ブラウザセッションをエージェントと双方向共有し作業を可視化・操作）、**並列セッション**（リポジトリ横断でブランチ / worktree 単位の並行実行）、**Cloud Automations**（マシン起動に依存しないクラウド上の定期エージェント実行）。管理者向けに `disableBypassPermissionsMode`（権限スキップを無効化するエンタープライズ制御）を追加。

**影響**: Claude Code / Cursor / Antigravity に続き、GitHub も「IDE 内補完」から「デスクトップ常駐エージェント拠点」へ製品形態を移す流れが鮮明に。Cloud Automations はクラウド定期実行という点で各社の cloud agent 競争（Cursor の cloud subagents 等）と直接重なる。

**行動指針**: 既に GitHub を中核に CI / PR フローを回す組織は、Canvases と Cloud Automations を PoC 対象に。権限スキップ無効化など統制機能が揃ったため、エンタープライズでも評価フェーズに進めやすい。

- https://github.blog/changelog/2026-06-17-github-copilot-app-generally-available/

## カテゴリ別まとめ

### Anthropic / Claude・規制
- Fable 5 / Mythos 5 停止8日目・「近日中に再開」発言・発端は Amazon の jailbreak 通報（ハイライト1参照）
- Anthropic ソウルオフィス開設＋韓国大手一斉提携＋MSIT MOU＋NAIRL 研究者支援（ハイライト2参照）
- **Anthropic IPO**: 6/1 に予備目論見書提出済み、trillion-dollar 規模デビュー観測。ソウル拡大はその布石の一環

### Microsoft / GitHub
- GitHub Copilot デスクトップアプリ GA（ハイライト3参照）
- **Microsoft（Copilot Studio / Power Platform / M365 Copilot）は新規一次情報なし**。Copilot Studio・Power Platform ブログは最新 6/11 で既報、M365 Copilot リリースノートも 6/18 から実質変更なし（Copilot Notebooks→Excel エージェント生成、Teams Rooms 向け Facilitator エージェント等は既報範囲内）

### Cursor / 開発ツール
- **Claude Code v2.1.181（6/17 stable）**: `/config key=value` 構文追加（プロンプトから任意設定を即変更、例 `/config thinking=false`）、`sandbox.allowAppleEvents` 設定、`CLAUDE_CLIENT_PRESENCE_FILE` 環境変数（モバイル push 抑制）、bundled Bun を 1.4 へ更新。長い段落の line-by-line ストリーミング、thinking 中の API 切断時 auto-retry、subagent パネル改善。v2.1.180 は changelog 記載なし（内部改善のみと推定）。https://code.claude.com/docs/en/changelog
- **Cursor**: Agents Window の cloud agent 更新（cloud 環境セットアップ < 10 分、再利用 snapshot、専用 VM で並列実行する cloud subagents）、canvas 向け **Design Mode**（UI 要素を直接選択・注釈してエージェント編集を誘導）、SDK に auto-review / nested subagents / run correlation ID。https://cursor.com/changelog

### OpenAI
- **ChatGPT Scheduled Tasks に専用「Scheduled」ページ（6/17）**: Web / モバイルでタスク一覧・次回実行時刻の確認、pause / resume / edit / delete を一元管理。「朝 / 午後 / 夜」等の broad window 指定、monitoring タスクは変化がある時だけ通知。**Pulse を sunset し proactive update を scheduled tasks に統合**（Pro は 14 日間 Pulse 継続可）、タスクは最大 1 時間に 1 回。https://help.openai.com/en/articles/6825453-chatgpt-release-notes
- **OpenAI Codex**: ChatGPT Business 向け role-specific plugins（Sales / Data Analytics / Product Design / Creative Production / Investment Banking / Public Equity Investing）。EEA / UK / スイスで Computer Use（macOS / Windows）・Chrome 拡張・Memories・Chronicle を解禁。https://developers.openai.com/codex/changelog
- **Deployment Simulation**: 過去の会話を候補モデルで再生し、ロールアウト前にリグレッションを検出する手法を導入

### Google / DeepMind
- **Gemini CLI → Antigravity CLI 消費者向け移行は 6/18 で実施済み**（エンタープライズは Gemini CLI 継続、open-source 開発者は Antigravity の closed-source 配布に懸念）
- **Gemini 3.5 Pro** は依然 GA 待ち（I/O 2026 で Pichai「来月まで待ってほしい」）。2M トークン context / Deep Think

### 市場データ
- AI チャットボット市場シェア（2026年4月・変化なし）: ChatGPT 54.7%、Gemini 27.4%、Claude 8.2%
- 日本の生成AI個人利用率は 2025年で 21.8%

## 直近の注目予定

- **〜7/1（予測・未確定）**: Fable 5 / Mythos 5 の US 顧客向けアクセス復旧（市場本命 57%、Anthropic 幹部は「近日中」と楽観）
- **6/22-23**: Fable 5 試食期間終了 → 利用に usage credits 必要化（※停止中のため実質保留・要再確認）
- **6/25**: gemini-3.1-flash-image-preview / gemini-3-pro-image-preview 廃止
- **6/27**: GPT-4.5 が ChatGPT から退役
- **6/30**: GPT-5.2・GPT-5.3-Codex 新規 API リクエスト不可化 / Devin クラシック環境セットアップ廃止 / Copilot Studio for Teams クラシック作成終了 / 感度ラベル表示 GA / Security Copilot E5 展開完了 / M365 価格ロックイン期限
- **7/1**: Anthropic Claude Partner Network 初回階層昇格レビュー / Devin Cascade 完全廃止 / M365 価格改定発効（E3 $36→$39、E5 $57→$61、Copilot Business $18→$21）/ Cursor 新価格
- **7/10 / 7/17**: Fable 5 復旧予測の中間マイルストーン（67% / 75%）
- **8/5**: Claude Opus 4.1 が Claude API から退役
- **8/26**: OpenAI Assistants API 廃止 / o3 退役

## 改善メモ

- **Anthropic 公式（`anthropic.com/news/*`）・github.blog・koreajoongangdaily.com への WebFetch は本日も 403 継続**。WebSearch ＋ 大手メディア（Korea JoongAng Daily / Fortune / KED Global）で代替（成功）。`daily-sources.md` の取得方法欄を「WebSearch 優先」に更新する推奨は継続。
- **Claude Code Changelog の番号飛び再発防止が奏功**: トップ版を突合した結果 v2.1.180 / v2.1.181（6/17）を取りこぼさず捕捉。v2.1.180 は changelog 記載なしで番号のみ確認。
- **03_ai-news-industry のローカルクローン乖離が再々発**: 起動時にローカル main と origin/main が共通祖先を持たず乖離する事象が複数ソースで継続報告。起動時に `git pull origin main`（または `git reset --hard origin/main`）を確実に実行する環境セットアップの見直しが必要。
- **Fable 5 停止の発端が「Amazon の Mythos jailbreak 通報」と判明**（Fortune 6/14）。従来の「対中アクセス懸念主因説」「jailbreak 本質ではない説」と合わせ、競合による脆弱性通報という新しい論点が加わったため両論併記でクロスチェックを継続。
- Microsoft 一次情報は引き続き静穏（複数日連続で新規発表なし）。既報の GA・ロールアウトを「本日の新規」と誤認しないよう日付確認を継続。
