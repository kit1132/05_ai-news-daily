# AI News Daily Summary — 2026-06-20

> 本サマリーは 01_ai-news-Master・02_ai-news-Copilot・03_ai-news-industry の3ソース（6/20分）を統合して作成。

## 今日のハイライト

### 1. Fable 5 / Mythos 5 停止9日目 — 6/20 も未復旧で返金期限が本日到来、ソース間で「6/18復旧」説と矛盾

**事実**: 6/12 17:21 ET の米輸出規制指令に端を発した Fable 5 / Mythos 5 の世界一斉停止は、**01_Master・02_Copilot の両ソースで 6/20 時点も未復旧（9日目）** と報告。Anthropic は全顧客で両モデルを無効化し **Opus 4.8 へ自動ルーティング**を継続（他 Claude モデルは影響なし）。一方 **03_industry は「約6日間の政府命令停止後、6/18 に当局と是正措置で合意し Fable 5 へのアクセスが復旧」と記載しており、ソース間で復旧有無が矛盾**（→改善メモ参照）。Anthropic 国際担当 MD Chris Ciauri 氏の「coming days に再開、非常に自信がある」（6/18 ソウル）以降、**新たな確定タイムライン・公式復旧発表は 6/20 時点で確認されず**。

**根拠**: 6/9〜6/14 に課金した利用者向けの**返金期限が本日 6/20 到来**。6/22 の Fable 5「試食期間」終了、6/23 の usage credits 必要化など既定日程が迫るが、停止が続く前提では実質保留で「要再確認」。予測市場（Kalshi / Polymarket / Manifold）は引き続き **US 顧客向け復旧を 7/1 までに 57% 前後**を本命視し、幹部の「近日中」前倒し示唆は 6/20 までに実現に至っていない。

**影響**: 単一フロンティアモデル依存リスクが地政学イベントとして長期化。公式の確定復旧アナウンスが出ない一方、課金・移行など商用フローの締切だけが先に到来し、利用者側の不確実性が増大。03_industry の「6/18 復旧済み」記述が正しければ「外国籍ユーザー限定の部分復旧」など条件付きの可能性もあり、復旧の定義（全顧客か/地域・国籍限定か）自体が曖昧。

**行動指針**: Fable 5 / Mythos 5 を本番に組み込む組織は復旧時期を依然「未定」と見なし、Opus 4.8 / GPT-5.5 フォールバック前提で運用継続。**「復旧した/していない」の食い違いがあるため、公式リリース（claude.com/blog・anthropic.com/news）での明示確認を最優先**し、メディア二次情報のみで「復旧」と判断しないこと。

- https://en.softonic.com/articles/anthropic-says-fable-5-and-mythos-5-could-return-within-days-freeze-called-temporary
- https://news.kalshi.com/p/fable-5-odds-anthropic-access-restored-july-57-percent
- https://www.techtimes.com/articles/318637/20260619/anthropic-opens-its-seoul-office-even-us-export-ban-cuts-korean-access-its-top-models.htm

### 2. MCP Enterprise-Managed Authorization が stable 化（6/18-19）— Okta が初の IdP、ゼロタッチ SSO で組織導入を加速

**事実**: **MCP の「Enterprise-Managed Authorization」拡張が 6/18-19 に stable 化**。組織が MCP サーバーへの認可を ID プロバイダ（IdP）側で一元管理でき、**エンドユーザーは初回ログインだけで接続済み MCP コネクタへ自動アクセス**（zero-touch OAuth / SSO）できる。Team / Enterprise プラン向け。

**根拠**: **Okta が初の対応 IdP** で、Cross App Access 経由で対応クライアントに MCP アクセスを provision。ローンチ時点で **Anthropic（Claude chat / Claude Code / Cowork）・VS Code・9 つの MCP サーバー**が対応し、対応コネクタは **Asana / Atlassian / Canva / Figma / Granola / Linear / Supabase**（Slack は近日対応）。

**影響**: エンタープライズの「MCP コネクタ棚卸し・権限統制」を IdP に寄せる動きで、個別 OAuth 同意の手間と野良コネクタのガバナンス問題を解消。MCP がエンタープライズ標準として定着する上での導入障壁を大きく下げ、Claude Code / Cowork / VS Code 横断の集中認可が実用段階に入った。

**行動指針**: Okta を IdP に使う組織は、MCP コネクタの権限を Cross App Access で一元管理する PoC を開始できる。情シス/セキュリティ部門は「ユーザー個別同意」から「IdP 集中認可」へ統制モデルを移行する検討に着手すると良い。

- https://www.techtimes.com/articles/318708/20260619/mcp-enterprise-authorization-goes-stable-zero-touch-sso-okta-anthropic-vs-code.htm
- https://claude.com/blog/enterprise-managed-auth

### 3. ノーベル賞 John Jumper 氏が Google DeepMind を退社し Anthropic へ（6/19）— トップ研究者流出が続く Google

**事実**: **AlphaFold を率い 2024 年ノーベル化学賞を Demis Hassabis 氏と共同受賞した John Jumper 氏が、約9年在籍した Google DeepMind を離れ Anthropic に合流**（6/19 報道）。役割は非公表で、当面は休養とされる。

**根拠**: Bloomberg / The Decoder が報じた。Jumper 氏は DeepMind のフロンティア研究を象徴する人物で、Anthropic はソウルオフィス開設・韓国大手一斉導入・IPO 前のアジア拡大に続き、トップ人材獲得でも攻勢。

**影響**: フロンティアモデル競争において、Google からの著名研究者流出が続く構図が鮮明化。Anthropic の人材吸引力と研究基盤の厚みを示す一方、輸出規制でのモデル停止という逆風下でも採用面では優位を保っていることを印象づける。

**行動指針**: モデル選定・ベンダー評価では、短期の可用性リスク（Fable 5 停止）と中長期の研究競争力（人材獲得）を分けて評価する。Anthropic の研究ロードマップに Jumper 氏の専門（構造生物学/科学応用）が反映されるか、今後の発表を追跡。

- https://www.bloomberg.com/news/articles/2026-06-19/nobel-winner-john-jumper-to-leave-google-deepmind-for-anthropic
- https://the-decoder.com/google-deepmind-loses-another-top-ai-researcher-as-nobel-laureate-john-jumper-leaves-for-anthropic/

## カテゴリ別まとめ

### Anthropic / Claude・規制
- Fable 5 / Mythos 5 停止9日目・返金期限本日到来・ソース間で復旧有無が矛盾（ハイライト1参照）
- MCP Enterprise-Managed Authorization stable 化（ハイライト2参照）
- John Jumper 氏が Google DeepMind から Anthropic へ移籍（ハイライト3参照）
- **韓国市場進出（6/17-18・既報）**: ソウルオフィス開設＋ NAVER / Samsung SDS / LG CNS / Nexon / Hanwha / Channel Corp の一斉導入＋ MSIT と AI 安全性 MOU。03_industry が本日も詳報。定量成果が出れば「大規模採用事例」として追跡推奨
- **Claude のデザイン機能更新**: デザインシステム整合、Claude Code 連携強化、キャンバス直接編集、design-to-code 連携（02_Copilot）

### Cursor / 開発ツール
- **Claude Code v2.1.183（6/19 stable）**: auto mode が**破壊的 git コマンドをブロック**（明示要求がない限り `git reset --hard` / `git checkout -- .` / `git clean -fd` / `git stash drop` / 当該セッション外コミットの `git commit --amend` / `terraform destroy`・`pulumi destroy`・`cdk destroy`）。**非推奨モデル警告**追加（`-p` モードと agent frontmatter 指定で stderr に表示）、**`attribution.sessionUrl`** 設定で commit/PR から claude.ai セッションリンクを省略可能、`/config --help` に shorthand キー一覧。修正: subagent spawn 時の `thinking.disabled.display` 400 エラー、subagent 内 WebSearch 空応答、vim カーソル、Windows Terminal フルスクリーン TUI 破損、thinking のみで無音完了する問題、認証付き MCP の auth-stub ツール露出。https://code.claude.com/docs/en/changelog
- **Cursor v3.8（6/18）— Automations 強化**: `/automate` skill 追加（自然言語からトリガー・指示・ツールを自動構成）、**GitHub / Slack 向け新トリガー**、computer use 対応。**Slack の任意メッセージに指定絵文字でリアクションして automation を起動**可能。https://cursor.com/changelog/06-18-26

### OpenAI
- **GPT-5.6 が月内ローンチ間近**: チーフサイエンティストが GPT-5.5 比「meaningful leap」と表明（6/16）。公式日付は未発表だが Polymarket は **6/22-28 ローンチに 83%**（出来高 $96 万）を織り込み。https://www.techtimes.com/articles/318492/20260616/gpt-56-openai-chief-scientist-calls-it-meaningful-leap-june-launch-nears.htm

### Google / DeepMind
- **Gemini 3.5 Pro は依然 GA 待ち**: 6/20 時点でも限定 Vertex AI プレビューのみで、Gemini アプリ / AI Studio / 消費者向けには未配信。Pichai の「来月まで待って」（I/O 2026）の 6 月 GA 目標は終盤に。2M トークン context / Deep Think。https://www.techtimes.com/articles/317919/20260606/google-gemini-35-pro-nears-june-launch-2-million-token-context-deep-think-reasoning.htm

### Microsoft / GitHub
- **新規一次情報なし**: Copilot Studio・Power Platform ブログ・M365 Copilot リリースノートいずれも 6/19 から変更なし（最新は Power Platform 6/11、M365 リリースノート 6/16 バッチ、いずれも既報）。2026 Release Wave 1（Computer Use GA、Workflows 再設計、Work IQ 拡張）は既報範囲内

### 規制・インフラ（要追検）
- **中国の 2,950 億ドル AI インフラ計画**: 5年で2兆元規模の相互接続型国家 AI データセンター構想との報道（The Decoder 6/18）。規模・確度とも一次資料での裏取りを推奨

### 市場データ（変化なし・参考）
- AI チャットボット市場シェア（2026年4月）: ChatGPT 54.7%、Gemini 27.4%、Claude 8.2%、DeepSeek 4.1%、Grok 2.8%（Similarweb）
- クラウドインフラ Q1 2026: 四半期 $129B（年率 $500B 超）・前年比 +35%、AWS 28% / Azure 21% / GCP 14%（Synergy）。AI データセンター用半導体は NVIDIA 約81% / AMD 約10%（IDC）

## 直近の注目予定

- **6/20（本日）**: Fable 5 返金期限（6/9〜6/14 課金分）
- **〜7/1（予測・未確定）**: Fable 5 / Mythos 5 の US 顧客向けアクセス復旧（市場本命 57%）
- **6/22**: Fable 5 試食期間終了（※停止中のため実質日程は要再確認）
- **6/22-28**: OpenAI GPT-5.6 ローンチ予測ウィンドウ（Polymarket 83%）
- **6/23**: Fable 5 利用に usage credits 必要化（※停止中のため要再確認）
- **6/25**: gemini-3.1-flash-image-preview / gemini-3-pro-image-preview 廃止
- **6/27**: GPT-4.5 が ChatGPT から退役
- **6/30**: GPT-5.2・GPT-5.3-Codex 新規 API リクエスト不可化 / Devin クラシック環境セットアップ廃止 / Copilot Studio for Teams クラシック作成終了 / 感度ラベル表示 GA / Security Copilot E5 展開完了 / M365 価格ロックイン期限
- **7/1**: Anthropic Claude Partner Network 初回階層昇格レビュー / Devin Cascade 完全廃止 / M365 価格改定発効（E3 $36→$39、E5 $57→$61、Copilot Business $18→$21）/ Cursor 新価格
- **7/10 / 7/17**: Fable 5 復旧予測の中間マイルストーン（67% / 75%）
- **8/5**: Claude Opus 4.1 が Claude API から退役
- **8/26**: OpenAI Assistants API 廃止 / o3 退役

## 改善メモ

- **ソース間の矛盾（重要）**: Fable 5 / Mythos 5 の復旧有無で食い違い。01_Master・02_Copilot は「6/20 時点も未復旧（9日目）」、03_industry は「6/18 に当局と合意し Fable 5 アクセス復旧」と記載。03_industry の記述は 6/19 付メディア（TechTimes）を典拠とし「外国籍アクセス停止→6/18 復旧」という文脈で、**全顧客復旧か国籍/地域限定の部分復旧かが不明瞭**。公式（claude.com/blog・anthropic.com/news）での確定確認を最優先し、両論併記でクロスチェック継続。
- **WebFetch 403 が全ソースで継続**: Anthropic 公式（`anthropic.com/news/*`）・AWS Blog・github.blog・softonic・各種 RSS（Google News / The Decoder / VentureBeat / Publickey / hnrss / Product Hunt / GitHub Trending）が 403。各ソースとも WebSearch ＋ raw.githubusercontent.com / 大手メディアでフォールバック（成功）。`daily-sources.md` の取得方法欄を「WebSearch 優先」に更新する推奨は複数日継続。
- **起動時のローカル main 乖離が連日再発**: 複数ソースで「開始時にローカル main が古い日付（06-05 等）で停滞し origin/main と共通祖先を持たず乖離」を継続報告。SessionStart hook で `git reset --hard origin/main` を明示実行する運用への恒久化を強く推奨（CLAUDE.md の「main 直 push」ルールだけでは初期乖離を防げていない）。本日の 05_daily 側は `git pull` で正常 fast-forward 済み。
- **AWS の「Fable 5 with built-in safeguards on AWS」記事**は 403 で日付確証が取れず、輸出規制で全環境停止中の現状と矛盾しうるため本日も本文採用を見送り（01_Master）。復旧後に safeguarded 版の提供形態として再確認すること。
- 韓国大手の Claude 一斉導入は提案資料の「エンタープライズ大規模採用事例」として有用。定量成果（工数削減率等）が出れば追跡推奨。
