# AI News Daily Summary — 2026-06-18

> 本サマリーは 01_ai-news-Master・02_ai-news-Copilot・03_ai-news-industry の3ソース（6/18分）を統合して作成。

## 今日のハイライト

### 1. Fable 5 / Mythos 5 停止が7日目 — G7で「AI主権」議論の前面へ、米政府との交渉続くも復旧なし

**事実**: 6/12 の米輸出規制指令に端を発した Fable 5 / Mythos 5 の世界一斉停止は **6/18 時点も未復旧（7日目）**。Anthropic は全顧客で両モデルを無効化し **Opus 4.8 へ自動ルーティング**を継続（他 Claude モデルは影響なし）。6/15-16 に Anthropic はトランプ政権と協議し**復旧合意を模索中**との報道。David Sacks は「政権は jailbreak 修正後できるだけ早く輸出規制を解除したい、ボールは Anthropic 側にある」と表明。

**根拠**: Anthropic は上級技術スタッフを Commerce 省に派遣し交渉継続（WSJ）。政府は「米国を害さない保証」を要求、Anthropic は top-tier モデルの復旧を要求。報道は割れており、TechCrunch は「禁止措置は当初から jailbreak が本質ではなく対中アクセス懸念が主因」と分析、Fortune は Katie Moussouris らの公開書簡（当該 jailbreak は実質「このコードを直して」程度の指示にすぎない）を報じ措置の妥当性に疑問。Alex Stamos ら cybersecurity リーダーは政権に復旧を要請。市場予測（Kalshi / Polymarket）は **US 顧客向け復旧を 7/1 までに 57〜67%、7/10 までに 67〜74%** と見込む。

**影響**: G7サミット（仏 Évian-les-Bains, 6/15-17）で Amodei / Altman / Hassabis が working lunch に初めて揃って同席し、ホストの Macron が掲げる digital sovereignty と欧州の対米AI依存への警戒が前面化。Fable 5 停止が格好の実例となり、単一フロンティアモデル依存リスクが地政学イベント化している。確定した deal・復旧タイムラインの公式発表は 6/18 時点でなし。

**行動指針**: Fable 5 / Mythos 5 を本番に組み込む組織は復旧時期を「未定」と見なし、Opus 4.8 / GPT-5.5 フォールバック前提で運用継続。Anthropic 公式＋大手メディア（CNBC / Globe and Mail / Axios 等）＋各国政府・予測市場の反応を毎日クロスチェック。6/22-23 の試食期間終了・クレジット移行などの既定日程は「停止中ゆえ要再確認」として追跡すること。

- https://www.cnbc.com/2026/06/17/g7-trump-ai-tech-leaders-openai-anthropic-google.html
- https://www.theglobeandmail.com/business/article-anthropic-trump-officials-deal-restore-fable-5-mythos-5/
- https://www.axios.com/2026/06/15/anthropic-fable-security-leaders-trump-admin
- https://techcrunch.com/2026/06/15/the-us-governments-anthropic-models-ban-was-never-about-an-ai-jailbreak/
- https://www.benzinga.com/markets/tech/26/06/53185788/sacks-us-wants-to-lift-anthropic-export-controls-as-soon-as-possible-after-fable-5-fix

### 2. Google: Gemini CLI / Code Assist IDE 拡張が本日6/18で消費者向け終了 — 後継は Antigravity CLI

**事実**: **6/18 から Gemini CLI / Gemini Code Assist IDE 拡張が AI Pro / Ultra / 無償個人向けでリクエスト処理を停止**。**Gemini Code Assist for GitHub も新規インストール不可化＋数週内にリクエスト停止**。後継は closed-source・Go 製の **Antigravity CLI（バイナリ `agy`）**。

**根拠**: 移行時の機能パリティは初日から 1:1 ではないが、**agent skills / hooks / subagents / extensions は launch 時点でサポート**。Google Developers Blog および 9to5Google が報道。

**影響**: 個人開発者は本日中に Antigravity CLI（`agy`）への移行が必要。一方 **エンタープライズは適用除外**で、Code Assist Standard / Enterprise ライセンスおよび enterprise Google Cloud 経由の GitHub 利用はアクセス変更なし。

**行動指針**: Gemini CLI / Code Assist を個人プランで CI・ローカル開発に組み込んでいる場合は即時に `agy` へ切り替え、hooks / subagents 等の依存機能のパリティを launch ノートで確認すること。エンタープライズ契約は当面影響なしだが移行ロードマップを把握しておく。

- https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/
- https://9to5google.com/2026/06/17/gemini-cli-code-assist-shutting-down/

### 3. OpenAI Partner Network 発表（$150M投資・7月稼働）— 「harness競争」へ軸足、Anthropic と直接競合へ

**事実**: OpenAI が **$150M 投資の初の公式パートナープログラム**を発表（6/14、7月稼働）。**2026年末までに30万人のコンサルタント認定**を目標とし、**Select / Advanced / Elite の3階層**に Codex / cybersecurity / AI agents の専門クレデンシャルを別途付与する。

**根拠**: launch partner は **BCG / Accenture / Bain / Artium**。複雑な enterprise 案件向けに **Forward Deployed Experts パイロット**（パートナー実務者を OpenAI エンジニアリングと連携）を提供。

**影響**: モデル性能競争から「harness（導入・運用）競争」へ軸足を移すシグナル。Anthropic の Claude Partner Network（7/1 初回階層昇格レビュー）と直接競合フェーズに入る。

**行動指針**: SI・コンサル経由で生成AI導入を進める企業は、両陣営のパートナー認定・クレデンシャル体系を調達時の評価軸に追加すると有用。

- https://openai.com/index/introducing-openai-partner-network/
- https://www.channelinsider.com/news-and-trends/openai-debuts-partner-network-backed-by-150m-investment/

## カテゴリ別まとめ

### Anthropic / Claude・規制
- Fable 5 / Mythos 5 停止7日目・G7議題化・米政府との交渉継続（ハイライト参照）
- 7/1 に Anthropic Claude Partner Network の初回階層昇格レビュー予定（ハイライト3参照）

### Google / DeepMind
- Gemini CLI / Code Assist IDE 拡張・GitHub 版が本日6/18終了、Antigravity CLI（`agy`）へ移行（ハイライト参照）
- Gemini 3.5 Pro GA は出荷日未確定（6月後半予定）

### OpenAI
- OpenAI Partner Network 発表（ハイライト参照）
- 研究「Predicting model behavior before release by simulating deployment」（6/16）— 展開前にモデル挙動をシミュレートし予測する安全性評価寄りの手法。https://openai.com/news/
- ChatGPT: memory 完全OFF・web 画像検索・model picker 簡素化から新規進展なし。GPT-5.2 は ChatGPT から退役済み（既存会話は GPT-5.5 へ自動継続）

### Microsoft / Copilot
- **M365 Copilot リリースノート更新 — Learning Agent（Work IQ駆動、AI Skills Navigator連携=Preview）が6月ロールアウト**。ロール・業務に合わせた「in-the-flow」学習で Copilot/AI スキル習得を支援。Copilot Notebooks が Teams 会議個別を知識ソースとして参照可能に。https://learn.microsoft.com/en-us/microsoft-365/copilot/release-notes
- **Agent 365 のガバナンス Public Preview（6月）**: コンテキストマッピング・ポリシーベース制御・ランタイムのブロック/アラートを Intune / Defender 経由で提供。エージェント統制を組織の EDR/MDM 基盤に統合（新規 Agent 365 購入は M365 E5 前提）。https://techcommunity.microsoft.com/blog/microsoft_365blog/microsoft-365-e7-and-agent-365-are-now-generally-available/4516295

### Cursor / 開発ツール
- **Claude Code v2.1.179（6/16 stable・バグ修正のみ）**: コネクション切断時の部分応答保持、WSL2 マウスホイールスクロール修正（v2.1.172 のリグレッション）、JetBrains 系ターミナル（2026.1+）のちらつき修正ほか。6/17-18 の新規 stable はなし。https://code.claude.com/docs/en/changelog
- **Z.ai GLM-5.2（6/13）**: 全 GLM Coding Plan ティアで提供開始。実用的な 1M トークン context ＋ High / Max effort レベル。https://www.marktechpost.com/2026/06/10/ai-coding-agents-development-platforms-2026/
- Cursor: Bugbot 90秒レビュー / `/review` / Enterprise Organizations GA から新規進展なし
- Devin: Devin Desktop GA / Work IQ API GA 後、大きな進展なし

### エンタープライズ事例・市場データ
- **KPMG が Microsoft Agent 365 と M365 Copilot を全世界276,000人超・138カ国へ展開（6/9）**。Agent 365 は組織内の全AIエージェントを登録・可視化・保護・計測する「コントロールプレーン」。「エージェントの管理・監査能力そのものが購買理由」という"ガバナンス＝プロダクト"の流れを象徴。https://news.microsoft.com/source/2026/06/09/kpmg-and-microsoft-scale-trusted-enterprise-ai-agents-globally-through-deployment-of-agent-365-and-copilot/
- Gartner予測: エンタープライズアプリの40%が2026年末までにタスク特化型AIエージェントを組み込む（2025年は5%未満、一次資料での裏取り推奨）
- Similarweb AIトラッカー（2026年4月・変化なし）: ChatGPT 54.7%、Gemini 27.4%、Claude 8.2%、DeepSeek 4.1%、Grok 2.8%

## 直近の注目予定

- **〜7/1（予測・未確定）**: Fable 5 / Mythos 5 の US 顧客向けアクセス復旧（市場本命、7/1 までに 57〜67%）
- **6/22-23**: Fable 5 試食期間終了 → 利用に usage credits 必要化（※停止中のため実質保留・要再確認）
- **6/25**: gemini-3.1-flash-image-preview / gemini-3-pro-image-preview 廃止
- **6/27**: GPT-4.5 が ChatGPT から退役
- **6/30**: GPT-5.2・GPT-5.3-Codex 新規 API リクエスト不可化 / Devin クラシック環境セットアップ廃止 / Copilot Studio for Teams クラシック作成終了 / M365 価格ロックイン期限 / Security Copilot E5 展開完了
- **7/1**: Anthropic Claude Partner Network 初回階層昇格レビュー / OpenAI Partner Network 稼働 / Devin Cascade 完全廃止 / M365 価格改定発効（E3 $36→$39、E5 $57→$61、Copilot Business $18→$21）/ Cursor 新価格
- **6月後半**: Grok V9-Medium 公開予定 / Gemini 3.5 Pro GA（出荷日未確定）

## 改善メモ

- **Anthropic 公式（`anthropic.com/news/*`）への WebFetch は本日も 403**。WebSearch ＋ 大手メディア（CNBC / Globe and Mail / Axios）で代替（成功）。tomshardware.com / cursor.com / github.blog も 403 継続。
- **Claude Code Changelog の取りこぼし継続**: 6/17 時点で最新を v2.1.178 と記載していたが実際は v2.1.179（6/16 stable）が既出。毎回トップ3バージョンの番号・日付を突合し番号飛びを検出すること。
- **03_ai-news-industry のローカルクローン乖離が再々発**: 起動時のローカル main が 06-05 で停滞し origin/main（06-17）と乖離。06-15〜06-17 連続記録の常態化問題で、起動時に `git pull origin main` を確実に実行する環境セットアップの見直しが必要。
- **RSS/WebFetch 全般の 403 常態化**（Google News / GIGAZINE / The Decoder / VentureBeat / Publickey / hnrss.org / Product Hunt / GitHub Trending）。`daily-sources.md` の取得方法欄を「WebSearch 優先」に更新することを強く推奨。
- 事実確認の教訓: M365 E7 / Agent 365 / KPMG 展開の GA・発表は過去日付（5/1・6/9 等）。リリースノートやキャッチアップ項目を「本日の新規」と誤認しないよう GA 日付を都度確認すること。
- Fable 5 停止の続報は報道が割れている（jailbreak 本質説 vs 対中アクセス懸念主因説）。両論併記でクロスチェックを継続。
