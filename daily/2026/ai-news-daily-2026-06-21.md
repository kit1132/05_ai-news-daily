# AI News Daily Summary — 2026-06-21

> 本サマリーは 01_ai-news-Master・02_ai-news-Copilot・03_ai-news-industry の3ソース（6/21分）を統合して作成。週末（日曜）のため主要ラボの確定的な新規発表は少なめ。

## 今日のハイライト

### 1. Fable 5 / Mythos 5 停止10日目 — 未復旧のまま、Anthropic が技術幹部を DC へ派遣し商務省と対面交渉に着手

**事実**: 6/12 17:21 ET の米輸出規制指令に端を発した Fable 5 / Mythos 5 の世界一斉停止は、**6/21 時点で10日目も未復旧**（01_Master・02_Copilot で一致）。全顧客で両モデルを無効化し **Opus 4.8 へ自動ルーティング**を継続（他 Claude モデルは影響なし）。**新展開として、Anthropic が上級技術スタッフをワシントンに派遣し、Commerce（商務省）担当者と輸出規制を巡る対面協議に入った**と報道。Chris Ciauri 氏の「coming days に復旧、非常に自信がある」（6/18 ソウル）以降で初の具体的アクションだが、**公式の確定復旧日・復旧発表は 6/21 時点でなし**。

**根拠**: 02_Copilot は、6/16 に流れた「48時間以内に復旧」説の出所が **X 上の非公式アカウント（BridgeMind）であり Anthropic 公式発表ではない**ことを確認（前日まで残っていた復旧説の根拠が崩れた）。利用者向け返金期限（6/20）は経過済み。予測市場（Kalshi / Polymarket / Manifold）は引き続き **US 顧客向け復旧を 7/1 までに 57% 前後**を本命視。ライブトラッカー（isfable5back 系）・Polymarket も「未復旧」表示が継続。

**影響**: 単一フロンティアモデル依存リスクが地政学イベントとして長期化。商務省との直接交渉入りは前進だが、非公式アカウント発の「近日復旧」情報が独り歩きしていた構図が明らかになり、二次情報の信頼性に一段の注意が必要。6/22 の Fable 5「試食期間」終了・6/23 の usage credits 必要化など既定日程は、停止継続を前提に実質保留（要再確認）。

**行動指針**: Fable 5 / Mythos 5 を本番に組み込む組織は復旧時期を依然「未定」と見なし、Opus 4.8 / GPT-5.5 フォールバック前提で運用継続。**復旧情報は公式（claude.com/blog・anthropic.com/news）での明示確認を最優先**し、X 等の非公式アカウント発の「○時間以内に復旧」を判断材料にしないこと。

- https://www.androidauthority.com/anthropic-fable-5-ai-models-optimistic-return-3679377/
- https://news.kalshi.com/p/fable-5-odds-anthropic-access-restored-july-57-percent
- https://www.koreajoongangdaily.com/business/anthropic-confident-of-reenabling-mythos-fable-5-access-in-coming-days-executive/12727522

### 2. OpenAI Codex「Record & Replay」（macOS）— 作業を一度実演すれば再現可能な SKILL.md に、RPA 的定型業務をエージェントで代替

**事実**: macOS 版 Codex が **Record & Replay** を追加。経費精算・休暇申請・動画アップロード等の繰り返し作業を一度実演すると、操作手順を**編集可能な `SKILL.md`** として保存し、以降は変数入力（日付・ファイル等）を受け付けて自動再現する（要 Computer Use 有効化、EU/UK/スイスは未提供）。あわせて automation run history で**一括アクション（bulk actions）**、ローカル↔リモートホスト間の **thread handoff**、SSH ディープリンク改善、Browser Use のセッション永続化も提供（01_Master・03_industry が一致報告）。

**根拠**: 実演ベースで業務手順をスキル化する方式は、従来の RPA（画面操作の固定的記録）と異なり、変数を受け付ける汎用スキルとして再利用できる点が新しい。01_Master・03_industry の2ソースで内容が整合。

**影響**: 経費・申請・アップロードといった定型業務をエージェントで代替する方向性が具体化し、「業務自動化提案」の文脈で訴求材料になる。一方 EU/UK/スイス未提供という地域制約があり、グローバル展開時は対象地域の確認が必要。

**行動指針**: 定型業務の自動化検討では、Record & Replay を「実演→スキル化→変数入力で再現」の PoC 候補に。ただし公開日が「June 2026」表記で**正確な日付・提供条件は一次資料（openai.com / developers.openai.com/codex/changelog）で裏取り**してから提案資料に反映すること。

- https://the-decoder.com/openais-codex-can-now-watch-you-work-once-and-repeat-the-task-forever/
- https://help.openai.com/en/articles/6825453-chatgpt-release-notes

### 3. OpenAI GPT-5.6 ローンチ予測ウィンドウが明日 6/22 開始 — チーフサイエンティストは「meaningful leap」、Polymarket 83%

**事実**: OpenAI GPT-5.6 の**ローンチ予測ウィンドウが明日 6/22 から開始**（〜6/28）。チーフサイエンティストは GPT-5.5 比で「meaningful leap（意味のある飛躍）」と表明済み（6/16）。**公式日付は未発表**だが、Polymarket は 6/22-28 のローンチに **83%** を織り込む。

**根拠**: 公式アナウンスはなく、確度は予測市場ベース。GPT-5.5 からの世代更新が近いという市場期待が高く、出来高も伴う（前日 6/20 サマリーで $96 万）。

**影響**: フロンティアモデル更新が短サイクル化する中、Fable 5 停止で Anthropic 側に逆風が続く時期に OpenAI が新世代を投入すれば、モデル選定・ベンダー評価の比較軸が動く可能性。

**行動指針**: モデル選定中の組織は、6/22 週の OpenAI 公式発表を注視。ただし**日付・性能はいずれも未確定（予測市場ベース）**であり、確定発表まで導入判断の前提にしないこと。

- https://www.techtimes.com/articles/318492/20260616/gpt-56-openai-chief-scientist-calls-it-meaningful-leap-june-launch-nears.htm

## カテゴリ別まとめ

### Anthropic / Claude・規制
- Fable 5 / Mythos 5 停止10日目・DC 対面交渉入り・「48時間復旧」説は X 非公式アカウント発と判明（ハイライト1参照）

### OpenAI
- Codex「Record & Replay」macOS 追加（ハイライト2参照）
- GPT-5.6 ローンチ予測ウィンドウ 6/22 開始・83%（ハイライト3参照）
- **ChatGPT リリースノート（6/19）**: 60+ 言語で単語の**発音ガイド（音声＋テキスト）**を会話内提示、World Cup をより会話的にフォロー、iOS 写真アップロード高速化、Android 有料プランで送信ボタン長押しによる**その1回だけのモデル選択**・コンポーザの inline mentions・Plugins メニュー刷新。https://help.openai.com/en/articles/6825453-chatgpt-release-notes

### Cursor / 開発ツール
- **Cursor v3.8 Automations（6/18・既報）**: `/automate` skill で自然言語から自動化を構成、GitHub / Slack 向け新トリガー（指定絵文字リアクションで起動）、クラウドエージェントの Computer Use 対応。02_Copilot が本日も差分として記録。https://cursor.com/changelog/06-18-26
- **Claude Code は v2.1.183（6/19/20 stable）が最新で新バージョンなし**。**Cursor も v3.8（6/18）以降の新規 changelog なし**。両ツールとも本日更新なし

### Google / DeepMind
- **Gemini 3.5 Pro は依然 GA 待ち**: 6/21 時点でも限定 Vertex AI エンタープライズ向けプレビューのみで、Gemini アプリ / AI Studio / 消費者向けには未配信。Pichai の「来月まで待って」6 月 GA 目標は終盤に。2M トークン context / Deep Think。https://www.techtimes.com/articles/317919/20260606/google-gemini-35-pro-nears-june-launch-2-million-token-context-deep-think-reasoning.htm

### Microsoft / GitHub
- **新規一次情報なし（静穏9日継続）**: Copilot Studio・Power Platform ブログ・M365 Copilot リリースノートいずれも 6/20 から変更なし（最新は Power Platform 6/11、M365 リリースノート 6/16 バッチ、いずれも既報）

### AI 業界トレンド（提案根拠用）
- **Pew 調査（6月）**: 米成人の **49% が AI チャットボットを利用**する一方、**社会便益を信じるのは 16%** にとどまる。「導入は活発、信頼は静か（Adoption is Loud, Trust is Quiet）」の乖離が鮮明で、「導入加速 vs 信頼・ガバナンス課題」の論拠に。https://asanify.com/blog/news/ai-adoption-trust-gap-june-19-2026/
- **市場シェア（Similarweb・2026年4月）**: ChatGPT 54.7%、Gemini 27.4%、Claude 8.2%、DeepSeek 4.1%、Grok 2.8%（変化なし）
- **国内利用率**: MM総研（2025年8月）個人利用率 21.8%、ICT総研（2026年2月）54.7%（変化なし）

## 直近の注目予定

- **明日 6/22**: Fable 5 試食期間終了（※停止中のため実質日程は要再確認）/ OpenAI GPT-5.6 ローンチ予測ウィンドウ開始（〜6/28、Polymarket 83%）
- **6/23**: Fable 5 利用に usage credits 必要化（※停止中のため要再確認）
- **6/25**: gemini-3.1-flash-image-preview / gemini-3-pro-image-preview 廃止
- **6/27**: GPT-4.5 が ChatGPT から退役
- **6/30**: GPT-5.2・GPT-5.3-Codex 新規 API リクエスト不可化 / Devin クラシック環境セットアップ廃止 / Copilot Studio for Teams クラシック作成終了 / 感度ラベル表示 GA / Security Copilot E5 展開完了 / M365 価格ロックイン期限
- **7/1**: M365 価格改定発効（E3 $36→$39、E5 $57→$61、Copilot Business $18→$21）/ Cursor 新価格 / Anthropic Claude Partner Network 初回階層昇格レビュー / Devin Cascade 完全廃止
- **〜7/1（予測・未確定）**: Fable 5 / Mythos 5 の US 顧客向けアクセス復旧（市場本命 57%）
- **7/10 / 7/17**: Fable 5 復旧予測の中間マイルストーン（67% / 75%）
- **7/17**: Claude Corps 第1期応募締切
- **8/5**: Claude Opus 4.1 が Claude API から退役
- **8/26**: OpenAI Assistants API 廃止 / o3 退役

## 改善メモ

- **Fable 5 復旧情報の信頼性**: 前日まで残っていた「48時間以内に復旧」説の出所が **X 上の非公式アカウント（BridgeMind）**だったと 02_Copilot が確認。06-20 サマリーで記録した「ソース間の復旧有無の矛盾」は、6/21 時点で**3ソースとも「未復旧」で一致**し収束した。今後も復旧情報は公式一次情報での確定を最優先。
- **Codex Record & Replay の日付未確定**: 公開日が「June 2026」表記で正確な日付が不明（03_industry）。一次資料（openai.com / developers.openai.com/codex/changelog）での裏取りを次回推奨。
- **WebFetch 403 が全ソースで継続**: Anthropic 公式（`anthropic.com/news/*`）・github.blog・isfable5back 系・各種 RSS（Google News / The Decoder / VentureBeat / Publickey / hnrss / Product Hunt / GitHub Trending）が 403。各ソースとも WebSearch ＋ raw.githubusercontent.com / 大手メディアでフォールバック（成功）。`daily-sources.md` の取得方法欄を「WebSearch 優先」に更新する推奨は複数日継続。
- **起動時のローカル main 乖離が連日再発（入力3リポ側）**: 01_Master・03_industry がともに「開始時にローカル main が古い日付（06-05 等）で停滞し origin/main と乖離」を 3 日連続で報告。各リポで SessionStart hook に `git fetch origin main && git reset --hard origin/main` を明示実行する運用への恒久化を強く推奨（複数回記録済み）。なお本日の 05_daily 側は `git pull` で正常 fast-forward 済み。
