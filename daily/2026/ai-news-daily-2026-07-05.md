# AI News Daily Summary — 2026-07-05

> 本サマリーは 01_ai-news-Master・02_ai-news-Copilot・03_ai-news-industry の3ソース（7/5分）を統合して作成。

## 今日のハイライト

### 1. Anthropic「Claude apps gateway」提供開始 — 自己ホスト型でエンタープライズ統制を集約（IdP認証・モデルallowlist・支出上限）

**事実**: Anthropic が **Claude apps gateway**（自己ホスト型サービス）を公開。企業導入向けに (1) **社内 IdP 経由の OIDC ソーシャルログイン**でAPIクレデンシャル露出を回避、(2) **IdP グループ単位のモデル allowlist・managed settings をサーバ側で強制**（非許可モデルを拒否）、(3) トークン数・モデル利用・ユーザーID・レイテンシを **Datadog / Splunk 等の可観測性基盤に統合**、(4) 組織/グループ/ユーザー単位の**日次・週次・月次の支出上限**、を提供。バックエンドは Amazon Bedrock / Google Cloud / Microsoft Foundry / Anthropic API 間の**フェイルオーバールーティング**に対応し、データレジデンシー要件に応える。

**根拠**: 01（Master）が一次報告。**制約**として web 検索なし・長期キャッシュなし・**OIDC のみ（SAML/LDAP 非対応）**・Windows Server 非サポートを明記。

**影響**: これまで API キー配布やアプリ側設定に依存していた Claude のエンタープライズ統制を、ゲートウェイ層に集約できる。特に「グループ単位のモデル制御をサーバ側で強制」「マルチクラウドのフェイルオーバー」は、規制業種や大規模組織の調達要件を直接満たす。

**行動指針**: Claude を組織展開中／検討中のチームは、既存 IdP が OIDC 対応かを確認しゲートウェイ PoC を計画。SAML/LDAP 前提の環境や Windows Server 依存がある場合は非対応点を回避策込みで評価する。可観測性は既存の Datadog/Splunk 連携に載せる前提で設計。

- 出典: 01_ai-news-Master ダイジェスト（7/5）

### 2. M365 Copilot「July 01」Release Notes バッチ回収 — AI生成物の透かし＆秘密度ラベル自動継承がガバナンスの目玉

**事実**: M365 Copilot の **July 01 Release Notes バッチ**（対象 6/17〜7/1、7/1公開分を本日一次確認で回収）。ガバナンス2件が最重要——(A) **AI生成コンテンツの透かし**: Cloud Policy「Include a watermark when content from Microsoft 365 is generated or altered by AI」で AI が生成/改変した**動画・音声**に視覚/音声の透かしを付与（**画像は対象外**、ユーザーが `myaccount.microsoft.com` で個別設定、Roadmap 547831）。(B) **生成ファイルの秘密度ラベル自動継承**: Copilot がファイル生成時に**参照元データの最高ラベルを自動適用**し、付与不可時はユーザーへ通知（Purview/DLP 運用と直結、未ラベル流出リスクを低減）。

**根拠**: 02（Copilot）が Learn MCP 一次確認で捕捉。7/4 ダイジェストは「7月バッチ未公開」としていたが実際は 7/1 に公開済みだった点を補正。エージェント系では **Scheduled prompts**（declarative agent の定期プロンプト予約が Power Automate 依存から脱却、Roadmap 531759）、長時間タスクの **Windows タスクバー表示**、**Copilot Studio エージェントの Teams チーム共有**を追加。

**影響**: 透かしと秘密度ラベル自動継承は、AI生成物の透明性・誤帰属防止と情報漏えい対策に直結する組織導入の要件。Copilot Chat（M365 Copilot ライセンス不要版）でも Outlook が受信トレイ・予定表・エンタープライズデータ全体を推論対象に拡大する。

**行動指針**: Purview/DLP 運用チームは秘密度ラベル自動継承の挙動を検証し、未ラベルファイルの手当てフローを整備。透かしポリシーは Cloud Policy で段階適用を計画。Scheduled prompts へ移行する場合は旧 preview の Power Automate 動作期限を確認。

- https://learn.microsoft.com/en-us/microsoft-365/copilot/release-notes

### 3. 生成AIのトークンコストが「人件費並みの管理対象」へ — 従量課金の実質値上げで隠れコストが表面化（国内企業が対応加速）

**事実**: LayerX・ラクス・Sansan・freee・メルカリ等の国内企業が、**生成AIのトークンコストを人件費と同等の管理対象**として扱い始めた。従量課金の実質値上げにより、これまでサブスクリプション契約に隠れていたコストが表面化しているのが背景。

**根拠**: 03（industry）が報告。直近の Anthropic **Fable 5 の従量課金移行**（7/7 以降 入力 $10 / 出力 $50 per M tokens、7/4ダイジェスト参照）とも整合する、業界全体の「トークン単価上昇 → コスト可視化圧力」トレンドの一環。

**影響**: AI 導入の ROI 計算がサブスク定額前提から従量・可変前提へ移行。プロンプト設計・モデル選定・キャッシュ活用がそのままコスト最適化の実務になり、FinOps 的なトークン予算管理が経営指標化しつつある。

**行動指針**: 部門/ユースケース単位のトークン消費を可視化し予算を設定。モデル選定はコスト効率（訓練/推論単価）と品質のバランスで継続評価し、キャッシュ・バッチ・軽量モデルの併用で単価上昇を吸収する。ハイライト1のゲートウェイ支出上限機能も統制手段になる。

- 出典: 03_ai-news-industry ダイジェスト（7/5）

## カテゴリ別まとめ

### Anthropic / Claude
- Claude apps gateway 提供開始（ハイライト参照）
- **Claude Code v2.1.201**（7/3）— **Claude Sonnet 5 セッションで harness reminder に mid-conversation の system role を使わなくなった**（内部挙動の調整、変更は1点のみ）— https://github.com/anthropics/claude-code/releases
- **本日 7/5 は Claude 3.5 Haiku 退役日**（01 の予定より）
- **Fable 5** は従来通りの価格体系を継続（03、7/7 の従量課金移行を控える）

### Microsoft / GitHub Copilot
- M365 Copilot July 01 Release Notes バッチ（ハイライト参照）— 他に Copilot Notebooks からの PowerPoint 生成/マインドマップ、Copilot Chat 内での Word/Excel/PPT/PDF 直接オープン、Word「Audio Overview」のリアルタイム音声対話、PowerPoint への画像モデル **MAI-Image-2-Efficient**、モバイル版 Siri 連携
- **PowerPoint Agent Mode 強化** — Teams 会議/チャットを参照したデッキ生成、Work IQ による関連ファイル/会議/メールの自動収集、既存デッキのスタイル/テーマ再利用
- **Copilot Studio は一次情報静穏** — What's New は6月分のまま、基盤は Build 2026.6.3（6/30初出）が11リージョンへ展開拡大、次ビルドは **7/7 見込み**（版ページは火曜更新）。Copilot Studio Blog / Message Center も 7/3〜7/5 新着なし

### Cursor / 開発ツール
- **Cursor for iOS 公開ベータ**（6/29、全有料プラン・iOS 26.0+）— iPhone/iPad からクラウド/ローカル coding agent を起動・操作、音声入力・push通知・スマホからの PR マージに対応。**Composer 2.5 実行は本日 7/5 まで75%オフ**
- **Team MCP 対応拡大** — 管理者が一度設定すればクラウドエージェント/エージェントウィンドウ/IDE/CLI へ一括配布（MCP のテナント配布ガバナンス強化）— https://cursor.com/changelog/ios-mobile-app

### OpenAI / Google
- **GPT-5.6**: 限定プレビュー継続、**広域リリースは7月中旬見込み**（03）
- **Gemini 3.5 Pro**: エンタープライズプレビュー段階、**7月 GA 予定だが具体日未発表**（03）

### 業界・インフラ投資
- **Switch が $2B 調達ラウンド開始**（a16z 主導、a16z は $400M コミット、評価額 約 **$50B**）— JPMorgan / Goldman Sachs が関与、来年 IPO 検討予定。データセンター事業の資本集約が続く（03）
- 生成AIトークンコストの人件費並み管理化（ハイライト参照）

## 直近の注目予定

- **7/5**: Claude 3.5 Haiku 退役 / Cursor Composer 2.5 割引（75%オフ）終了
- **7/7**: Fable 5 週次50%上限撤廃 → 従量課金（$10/$50 per M tokens）移行 / Copilot Studio 次ビルド見込み
- **7/8**: Anthropic 政府発行ID検証ポリシー施行
- **7/14**: Visio → Power Automate エクスポート廃止発効（Current Channel は6/30適用済み）
- **7月中旬**: GPT-5.6 広域リリース見込み
- **7/21**: Copilot Cowork GA 発表イベント
- **7月中（具体日未発表）**: Gemini 3.5 Pro GA 見込み
- **8/1**: covered frontier model 60日 EO 期限
- **8/31**: Sonnet 5 促進価格終了（$2/$10 → $3/$15）

## 改善メモ

- **02 の補正**: 7/4 ダイジェストが M365 Copilot「7月バッチ未公開」としていたが、実際は **7/1 に公開済み**だった（本日 Learn MCP 一次確認で回収）。WebSearch のみの確認では一次バッチの公開を取りこぼす場合があるため、Learn MCP 一次確認を優先する運用を継続。
- **02 の障害メモ**: qiita RSS（copilotstudio/powerplatform）と mc.merill.net が 7/2 復旧後に**再び 403（7/5、断続的）**。WebSearch フォールバックで対応（台帳に再発を記録）。B-005（Qiita 取得の WebSearch 前提化、4回目）は復旧/再発の反復のため提案価値を維持。
- **03 の出典追跡性**: industry ダイジェスト原文に個別出典URLの記載が乏しい（Switch 調達・国内トークンコスト管理・GPT-5.6/Gemini 予定等）。統合時の出典追跡性が低いため、当該ソース側で各項目に出典URLを付与する運用改善を継続提案。
- ソース間の重複（Claude Code v2.1.201、Fable 5 従量課金、GPT-5.6、Gemini 3.5 Pro）は情報量の多い記述をベースに統合。矛盾は検出されず。
