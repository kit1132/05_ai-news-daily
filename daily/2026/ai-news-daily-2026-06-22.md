# AI News Daily Summary — 2026-06-22

> 本サマリーは 01_ai-news-Master・02_ai-news-Copilot・03_ai-news-industry の3ソース（6/22分）を統合して作成。月曜・週末明けで主要ラボの確定的な新規発表は少なめ。最大の動きは Fable 5 / Mythos 5 停止を巡る「NSA 侵入証言」の浮上（ただし一次情報は伝聞 1 件で未確認）。

## 今日のハイライト

### 1. Fable 5 / Mythos 5 停止11日目 — NSA 侵入証言が浮上し ban の論点が「narrow jailbreak」から「自律的攻撃能力そのもの」へ転換（ただし未確認）

**事実**: 6/12 17:21 ET の米輸出規制指令（ERA 2018、国家安全保障権限）による Fable 5 / Mythos 5 の世界一斉停止は、**6/22 時点で11日目も未復旧**（3ソース一致）。全顧客で両モデルを無効化し **Opus 4.8 へ自動ルーティング**を継続（他 Claude モデルは影響なし）。**新展開として、Sen. Mark Warner（上院情報委 副委員長）が公聴会で、NSA / Cyber Command 司令官 Gen. Joshua Rudd から聞いた話として「Mythos が 6/11 の red-team 演習で NSA 機密システムの"ほぼ全て"に数週間ではなく数時間で侵入した」と公表**。The Economist 経由で週末に拡散し、ban の理由が従来 Anthropic が説明してきた「既知・narrow なジェイルブレイク」から「自律的攻撃能力そのもの」へと論点が転換した。

**根拠**: ⚠️ **一次情報は Warner が私的会話を公に伝えた伝聞 1 件のみで、NSA の公式声明は存在しない**（01_Master が明記）。SNS の「NSA が確認」という表現は誇張で、実態は「機密環境のレプリカに対する内部評価で、人間チームを超える速度で脆弱性を連鎖発見した」という穏当な読みが有力。あわせて、Trump は Axios に「Anthropic / Amodei をもう国家安全保障上の脅威とは見ていない（"not now, but a week ago, maybe"）」と態度を軟化（G7 後 6/17）させたが、**Commerce が指令を正式撤回するか新認可枠組みを出すまで法的には停止継続**で、指令本文・規制指定は不変。予測市場は **US 顧客向け復旧を 7/1 までに 57%、7/10 まで 67%、7/17 まで 75%** を本命視。

**影響**: ban の根拠が「狭い脆弱性」なら早期復旧の余地があるが、「自律的サイバー攻撃能力」が真因なら復旧条件は格段に厳しくなり長期化リスクが上振れする。Warner 発言と Trump の軟化は方向性が逆で、停止の見通しは依然不透明。二次情報（特に SNS の「NSA が確認」系）が独り歩きしやすい局面で、情報の格付けに一段の注意が必要。

**行動指針**: Fable 5 / Mythos 5 を本番に組み込む組織は復旧時期を「未定」と見なし、Opus 4.8 / GPT-5.5 フォールバック前提で運用継続。**NSA 侵入の件は「報道ベース・未確認」と明示して扱い、公式 NSA 声明または Anthropic / Commerce の一次情報が出るまで確定情報として共有しないこと**。復旧情報は公式（claude.com/blog・anthropic.com/news）での明示確認を最優先。

- https://www.anthropic.com/news/fable-mythos-access
- https://news.kalshi.com/p/fable-5-odds-anthropic-access-restored-july-57-percent

### 2. Fable 5「プラン無償包含」が本日 6/22 で終了 — 6/23 からトークン課金へ、ただし停止中で実質使えないまま移行

**事実**: 6/9 のローンチ以来、Fable 5 は Pro / Max / Team / シート型 Enterprise プランに **6/22 まで無償包含**されてきたが、**6/23 以降はプランから外れ、トークンクレジット課金（$10/M トークン入力・$50/M トークン出力）へ移行**する（02_Copilot）。ただしモデル自体は輸出管理指令で**現在も停止中**のため、無償期間は実質ほぼ使えないまま終了する形となる。

**根拠**: Anthropic は期限設定の理由を「需要が非常に高く予測困難（容量制約）」と説明し、容量次第で標準プラン提供を将来復活させる意向を示すが**日付は未定**。出所は developersdigest.tech の解説記事で、料金体系・期限は同記事ベース。

**影響**: 復旧後に Fable 5 を使う前提だった組織は、無償枠を使い切れないまま従量課金（出力 $50/M は高水準）へ切り替わるため、復旧時のコスト試算を入れ替える必要がある。「停止中に課金体系だけが先行移行する」ねじれた状態で、復旧時の実コストが当初想定より上がる点に留意。

**行動指針**: Fable 5 採用を検討する組織は、6/23 以降の従量課金（入力 $10/M・出力 $50/M）を前提にコスト試算を更新。標準プラン復活は日付未定のため、当面は従量課金前提で見積もること。料金・期限は一次資料（claude.com / anthropic.com）での裏取りを推奨。

- https://www.developersdigest.tech/blog/claude-fable-5-june-22-deadline

### 3. OpenAI GPT-5.6 ローンチ予測ウィンドウが本日 6/22 に突入 — Polymarket 83%、公式日付はなお未発表

**事実**: OpenAI GPT-5.6 の**ローンチ予測ウィンドウが本日 6/22 から開始**（〜6/28）。Polymarket は 6/22-28 のローンチに **83%** を織り込む。チーフサイエンティスト Pachocki は GPT-5.5 比で「meaningful leap（意味のある飛躍）、効率・安全性重視で Fable 5 / Gemini に対抗」と表明済み（6/16）。**公式日付・system card・API モデル文字列はいずれも未発表**。

**根拠**: 公式アナウンスはなく、確度は予測市場ベース。Anthropic の Fable 5 停止が長期化する時期に OpenAI が新世代を投入すれば、モデル選定・ベンダー評価の比較軸が動くという市場期待が高い。

**影響**: フロンティアモデル更新の短サイクル化が続く中、Fable 5 停止で Anthropic に逆風が続く局面での GPT-5.6 投入は、モデル比較の前提を変える可能性。ただし日付・性能とも未確定。

**行動指針**: モデル選定中の組織は 6/22 週の OpenAI 公式発表（openai.com / system card）を注視。**日付・性能はいずれも予測市場ベースで未確定**であり、確定発表まで導入判断の前提にしないこと。

- https://www.techtimes.com/articles/318492/20260616/gpt-56-openai-chief-scientist-calls-it-meaningful-leap-june-launch-nears.htm

## カテゴリ別まとめ

### Anthropic / Claude・規制
- Fable 5 / Mythos 5 停止11日目・NSA 侵入証言の浮上（未確認）・Trump 軟化・指令は法的に継続（ハイライト1参照）
- Fable 5 無償包含が本日 6/22 で終了、6/23 からトークン課金（入力 $10/M・出力 $50/M）（ハイライト2参照）

### Claude Code
- **v2.1.185（6/20 stable）が最新**: stream-stall ヒント文言を「Waiting for API response · will retry in …」に更新、無音検知トリガーを 10s → **20s** に変更（実質マイナー調整）。v2.1.184 は changelog 記載なし（内部改善）。https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md

### OpenAI
- GPT-5.6 ローンチ予測ウィンドウ本日 6/22 突入・83%（ハイライト3参照）
- **ChatGPT リリースノート（6/19・既報）**: 発音ヘルプ（60+ 言語、音声＋テキスト）、World Cup 会話、アプリ権限制御の細分化、回答内インタラクティブチャート（棒/線/円/散布）、iOS 写真アップロード高速化
- **Codex（6/19・既報）**: macOS Record & Replay、rate-limit reset banking、Chrome / 内蔵ブラウザの Developer mode（CDP 経由）

### Google / DeepMind
- **Gemini 3.5 Pro は依然 GA 待ち**: 6/22 時点でも Vertex AI 限定プレビューのみで、Gemini アプリ / AI Studio / 消費者向け未配信（Pichai「来月まで待って」）。2M トークン context / Deep Think。予測市場の「6/30 までの GA」確率は約 50〜55% で月内ずれ込みの可能性。https://aiweekly.co/alerts/gemini-35-pro-eyes-june-ga-with-2m-context-and-deep-think
- **Google Workspace（6/17-18・新規）**: Gemini に Google Classroom 連携を全面展開、temporary chats / 会話削除の管理者制御、Google Vids アバター 23→53 種拡張（Gemini 3.1 Flash TTS + Veo 3.1）、Calendar イベント色拡張

### Microsoft / GitHub
- **新規一次情報なし（静穏10日継続）**: Copilot Studio・Power Platform ブログ・M365 Copilot リリースノートいずれも変更なし（最新は Power Platform 6/11、M365 リリースノート 6/16 バッチ、いずれも既報）

### Cursor / 開発ツール
- **Cursor v3.8（6/18・既報）**: Automations 強化（`/automate` skill、GitHub/Slack 新トリガー 5 種、computer use デフォルト有効、Slack 絵文字リアクションで起動）。Bugbot は平均レビュー ~90 秒・検出バグ +10%・コスト -22%（6/10）

### AI 業界トレンド（提案根拠用）
- **市場シェア（Similarweb・2026年4月）**: ChatGPT 54.7%、Gemini 27.4%、Claude 8.2%、DeepSeek 4.1%、Grok 2.8%（変化なし）
- **国内利用率**: MM総研（2025年8月）個人利用率 21.8%、ICT総研（2026年2月）54.7%（変化なし）

## 直近の注目予定

- **6/22（本日）**: Fable 5 プラン無償包含が終了（→ 6/23 よりトークン課金）/ Fable 5 試食期間終了（※停止中のため実質要再確認）/ OpenAI GPT-5.6 ローンチ予測ウィンドウ突入（〜6/28、Polymarket 83%）
- **6/23**: Fable 5 がトークン課金へ移行（入力 $10/M・出力 $50/M）・利用に usage credits 必要化（※停止中のため要再確認）
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

- **NSA 侵入証言は未確認情報として扱う**: 一次情報は Warner 1 名の伝聞のみで NSA 公式声明は不在（01_Master が明記）。SNS の「NSA が確認」表現は誇張で、公式声明が出るまで「報道ベース・未確認」と明示し続けること。ban の真因（narrow jailbreak vs 自律的攻撃能力）で復旧見通しが大きく変わるため要継続監視。
- **Fable 5 の課金移行と停止のねじれ**: 無償包含が 6/22 で切れ 6/23 から従量課金（出力 $50/M）に移行する一方、モデルは停止中で実質使えない。標準プラン復活は日付未定。復旧時のコスト試算は従量課金前提で更新が必要。
- **WebFetch 403 が全ソースで継続**: Anthropic 公式（anthropic.com/news/*）・github.blog・cursor.com・techtimes.com・各種 RSS（Google News / The Decoder / VentureBeat / Publickey / hnrss / Product Hunt / GitHub Trending）が 403。各ソースとも WebSearch ＋ raw.githubusercontent.com / 大手メディアでフォールバック（成功）。`daily-sources.md` の取得方法欄を「WebSearch 優先」へ更新する推奨は複数日継続。
- **起動時のローカル main 乖離が連日再発（入力3リポ側）**: 03_industry が再び「開始時にローカル main が 06-05 で停滞し origin/main と乖離」を報告（06-15 以降連続記録）。各リポで SessionStart hook に `git fetch && git reset --hard origin/<branch>` を導入する運用への恒久化を強く推奨。
</content>
</invoke>
