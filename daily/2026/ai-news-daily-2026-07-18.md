# AI News Daily Summary — 2026-07-18

> 本サマリーは 01_ai-news-Master・02_ai-news-Copilot・03_ai-news-industry の3ソース（7/18分）を統合して作成。

土曜。**大型ローンチの乏しい静かな一日**で、主軸は「地政学」「実装ツール」「待機案件」の3方向。地政学では **WAIC 2026 で主権AIブロック『WAICO』に29カ国が正式署名**し、中国 NDRC が「AI関連産業 2025年 1兆元超（約$147B）」の一次データを公表。実装面では **Claude Code v2.1.212** が `/fork` 刷新・セッション上限新設に加え、**plan モードが権限確認なしにファイル変更 Bash を自動実行する脆弱性**などセキュリティ修正を伴って着地（Master／Copilot 一致）。待機案件では **Gemini 3.5 Pro GA が目標日 7/17 を過ぎても公式発表なし**（予測市場は 7/30 を最有力視）、**Anthropic IPO** は投資家面談が進行し公開S-1が8〜9月・プライシング10〜11月との観測が加わった。Microsoft 一次情報源は静穏（Copilot Studio 版は 2026.6.3 据え置き、7/21 が要監視日）。

## 今日のハイライト

### 1. WAIC 2026 — 主権AIブロック「WAICO」に29カ国署名、中国AI産業「1兆元超」の一次データ公表 — 西側ガバナンスへの対抗軸が制度化

**事実**: 7/16 に29カ国が「世界AI協力機構（WAICO）」創設協定に署名し、西側主導のAIガバナンス体制に対抗するブロックが正式発足（習近平が同 summit 史上初の基調講演）。中国 NDRC は会場で「中国のAI関連産業が2025年に1兆元（約$147B）を超え、2026年は30%超成長見込み」と公表。7/18 は学術会議 WAICA が開幕（282投稿中57採択・採択率約20%・10カ国超）。展示規模は108チップ・261基盤モデル・208身体性端末。

**根拠**: 03_ai-news-industry が一次。署名国数（29）・市場規模（1兆元／$147B）・成長率（30%超）・展示定量（108/261/208）が具体的に示され、前日（7/17）の「WAIC 開幕・中国勢インフラ攻勢」報の裏づけとなる一次データ。

**影響**: AIガバナンスが「単一のグローバル規範」から「西側 vs WAICO」の二極構造へ制度的に分岐しつつある。調達・モデル選定では「対中モデル／インフラ採用の是非」が地政学リスク項目として現実味を増す。中国の市場規模データは、低価格×大規模インフラ攻勢（前日の MiniMax M3・Huawei Atlas 950）を裏づける根拠として提案資料に引用可能。

**出典**:
- https://www.techtimes.com/articles/320812/20260717/china-launches-rival-ai-governance-bloc-waic-2026-opens-300-product-debuts.htm
- https://en.people.cn/n3/2026/0708/c90000-20475542.html

### 2. Claude Code v2.1.212 — `/fork` 刷新・セッション上限新設と、plan モードの権限バイパス脆弱性を修正

**事実**: Claude Code v2.1.212（7/17）が着地。`/fork` は会話を新規バックグラウンドセッションへコピーする方式へ変更（現行作業を維持）、セッション内サブエージェント起動は `/subtask` に置換。`claude auto-mode reset`（確認プロンプト付き）追加。**WebSearch のセッション全体上限（既定200・`CLAUDE_CODE_MAX_WEB_SEARCHES_PER_SESSION`）とサブエージェント生成上限（既定200・`CLAUDE_CODE_MAX_SUBAGENTS_PER_SESSION`）を新設**（暴走ループ防止）、2分超の MCP ツール呼び出しは自動でバックグラウンド移行。セキュリティ修正として **plan モードが権限プロンプトなしにファイル変更 Bash を自動実行する不具合**、**worktree 作成時の symlink 追従脆弱性**を是正。ほか Windows print/SDK の SIGTERM 孤児化、hosted セッションの mTLS 証明書・OAuth スコープ不具合等も修正。

**根拠**: 01_ai-news-Master（changelog 一次）と 02_ai-news-Copilot（Microsoft 静穏日の実質唯一の新規動向として詳報）が独立に観測し、版数・機能・修正内容が一致。

**影響**: plan モードの権限バイパスは、自動化ワークフローで「確認なしにファイルが書き換わりうる」実害を持つため、v2.1.212 への更新は優先度が高い。WebSearch／サブエージェントのセッション上限新設は、CI やルーチンでの暴走・コスト膨張の抑止に効く一方、既定200を超える大規模ワークフローは環境変数での明示調整が必要になる。

**出典**:
- https://code.claude.com/docs/en/changelog
- https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md

### 3. Gemini 3.5 Pro GA — 目標日 7/17 を過ぎても公式発表なし、予測市場は 7/30 を最有力視

**事実**: 7/18 確認時点で、リーク報の GA 目標日 7/17 を過ぎても Google は公式発表（モデルカード／価格ページ／`gemini-3.5-pro` API リスティング）を出していない。公開API は gemini-3.5-flash / gemini-3.1-pro-preview のまま、Vertex AI 限定 preview 継続。予測市場は **7/30 を最有力（約52%）**、7/31 までにリリースなしの可能性も約23%と見込む。噂ベースの想定仕様は 2Mトークン文脈・Deep Think 推論層・プレミアム価格 $15/$60（100万トークン、Deep Think は Ultra 月$250 ティアにゲート）。

**根拠**: 01_ai-news-Master と 03_ai-news-industry が一致して「目標日超過・公式未発表」を報告。日付・仕様・ベンチはいずれも公式 launch post が出るまで「報道」扱いと明記。

**影響**: モデル選定・ベンチ比較の確定判断は保留が妥当。WAIC の米中発表集中週と重なり公式発表が後ろ倒しになった構図で、7/30 前後の再確認が現実的な次アクション。価格が噂どおり $15/$60 なら Claude Opus・GPT-5.5 級との比較でコスト面の位置づけが焦点になる。

**出典**:
- https://www.techtimes.com/articles/320308/20260713/gemini-35-pro-targets-july-17-after-full-rebuild-every-spec-remains-unconfirmed.htm
- https://startupfortune.com/google-delays-gemini-35-pro-launch-to-july-17-after-scrapping-its-base-model/

## カテゴリ別まとめ

### Anthropic / Claude
- **Anthropic IPO**: 7/15 開始の投資家プレ面談が進行中。慣行タイムラインなら公開S-1が8〜9月、ロードショー・プライシングが10〜11月との観測が加わった（主幹事 Goldman/Morgan Stanley/JPMorgan、6/1 SEC 極秘申請済、$965B評価）。OpenAI が IPO を2027へ後ろ倒ししたため、フロンティア初の公開となる可能性は不変。 https://www.cnbc.com/2026/07/15/anthropic-ipo-banks-investor-meetings.html
- **Claude Code v2.1.212**（ハイライト参照）
- Anthropic は 7/14 のヘルスケア提携（Optum / UST）・「Claude for Teachers」以降、新規発表なし。**Opus 4.1 の Claude API 提供終了が 8/5 予定**（要注意日程）。

### OpenAI
- **GPT-Live-1（全二重音声モデル）をグローバル展開**（7/8 投入・state 未収録だったため補足）。従来の Advanced Voice Mode を置換し、聞きながら同時に話せる全二重アーキテクチャで相槌・割り込み・沈黙に対応。Web検索や深い推論はバックのフロンティアモデル（launch時 GPT-5.5）へ委譲。既定音声は Go/Plus/Pro が GPT-Live-1、Free が GPT-Live-1 mini。API は近日提供予告。音声フロント×バックエンド推論の分離という設計トレンドの実例。 https://openai.com/index/introducing-gpt-live/
- **Codex CLI 安定版は 0.144.5 据え置き**（新規安定版なし）。alpha は自動リリースで 0.145.0-alpha.22（7/17）まで進行（リリースノート詳細なし）。 https://github.com/openai/codex/releases

### Google / DeepMind
- **Gemini 3.5 Pro GA 未発表**（ハイライト参照）

### Microsoft / Copilot（一次情報源は静穏・確認のみ）
- **Copilot Studio - What's New**: June 2026 セクションのまま（7月セクション未公開）。 https://learn.microsoft.com/en-us/microsoft-copilot-studio/whats-new
- **M365 Copilot Release Notes**: 「July 15, 2026」バッチが最新のまま（次バッチは隔週傾向で 7/29 前後見込み）。 https://learn.microsoft.com/en-us/copilot/microsoft-365/release-notes
- **Copilot Studio Released Versions**: 2026.6.3（6/30初出）が最新のまま。リージョン分布も無変化。**次回火曜 7/21 が 2026.7.x 反映の要監視日**。 https://learn.microsoft.com/en-us/power-platform/released-versions/copilotstudio
- **Power Platform Blog / Roadmap / Message Center**: 7/18 の新規検出なし（Roadmap は 7/2 の MC1413298 以降 ID 変化なし）。

### コーディングエージェント / 開発ツール
- **GitHub Copilot CLI**: Master は **v1.0.72-1（7/17 pre-release）**を観測（`--plugin`/`--mcp`/`--skill` フラグ対応、`copilot plugins remove --skill` でスキル削除、フルファイルパス表示、plan 承認メニューのモデル間決定的挙動統一、ターンをまたぐディレクトリ可視性の文脈保持）。一方 Copilot ソースは **v1.0.71（Latest）据え置き・次のプレリリース系列は未検出**と報告。両者に版数の食い違いあり（改善メモ参照）。 https://github.com/github/copilot-cli/releases
- **据え置き**: Cursor 3.11（7/10）／Devin SWE-1.7（7/8・Kimi K2.7 Code ベース、Cerebras 1,000 TPS）。7/18 の新版なし。

### 規制・政策 / 業界
- **WAIC 2026 / WAICO**（ハイライト参照）。7/18 は学術会議 WAICA 開幕（採択率約20%）。

## 直近の注目予定

- **7/19（明日）**: Fable 5 無償提供終了（→ 7/20 から前払いクレジット $10/$50）/ Claude Code 週次上限 +50% 終了
- **7/21**: Copilot Studio Released Versions 次更新（火曜・2026.7.x 反映見込み）
- **7/23**: OpenAI computer-use-preview シャットダウン
- **7/29 前後**: M365 Copilot Release Notes 次バッチ見込み（隔週）
- **7/30**: Gemini 3.5 Pro GA 予測市場 最有力日（約52%）/ Copilot「メモリ活用エージェント提案」GA 見込み
- **7/31**: Devin classic 環境設定 read-only 参照終了
- **8/1**: covered frontier model 大統領令60日期限
- **8/3**: 旧「Claude in Slack」退役
- **8/5**: Opus 4.1 Claude API 退役 / Cowork 倍増利用枠終了
- **8/9**: ChatGPT Atlas シャットダウン
- **8/26**: OpenAI Assistants API 廃止 / o3 退役 / GPT-4.5 完全廃止
- **8/31**: Sonnet 5 促進価格終了（→ $3/$15）
- **8〜9月（見込み）**: Anthropic 公開S-1 提出観測
- **9月**: iOS 27 / macOS 27 GA（AFM 3 本番）
- **10〜11月（見込み）**: Anthropic ロードショー・プライシング（早ければ上場、フロンティアAI初）

## 改善メモ

- **ソース間の版数矛盾（要確認）**: GitHub Copilot CLI で観測が食い違う。01_ai-news-Master は「v1.0.72-1（7/17 pre-release）／前 1.0.72-0（7/16）」を報告、02_ai-news-Copilot は「v1.0.71（Latest）据え置き・次のプレリリース系列は未検出」と報告。Master は releases ページ（pre-release 含む）、Copilot は Latest 安定版のみを見ている観測範囲の差と推測されるが、両ソースの取得対象（pre-release を含むか）の突き合わせを要望。
- **ソース間整合（良好）**: Claude Code v2.1.212 は Master・Copilot で版数・機能（`/fork` 刷新・セッション上限・plan モード脆弱性修正）が一致。Gemini 3.5 Pro GA 未発表は Master・industry で一致。
- **障害状況（Master・継続監視）**: `developers.openai.com/changelog` と `community.openai.com/c/announcements/6.rss` が本日 403（07-15 の codex/changelog 障害が OpenAI 開発ドメイン全体へ拡大）。WebSearch フォールバックで情報欠落なし。次回月曜 07-20 の復旧チェック対象。
- **前日欠損リカバリ**: 対象なし（7/17 分サマリーは3ソース完全統合で欠損記録なし）。
- **継続提案（引き継ぎ）**: B-005 Qiita RSS の WebSearch 前提化（Copilot・6回目）、B-004 取得方法欄を WebSearch 優先へ（industry・19回目）。
