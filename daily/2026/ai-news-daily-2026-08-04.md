# AI News Daily Summary — 2026-08-04

火曜は「前日までの前提が誤りだった」と分かる項目が並んだ。Copilot Studio は GitHub Copilot ハーネスの課金が公開前の作成・テスト段階から始まる仕様を一次で明記し、MCP の Tier 1 SDK は4本とも既に安定版に届いていたことが判明した。Cursor の DeepJack は最新ビルドでも再現するとされ、リンクを踏む側の統制が論点になる。ゲートウェイ拒否の大規模な解消により OpenAI・Google・Hugging Face の一次確認が同時に進み、これまで二次情報で保留していた値下げ幅・退役日・重み公開がまとめて確定した。Microsoft の定例ソースは据え置きで、7月 GA 予定だった Power Platform の7機能は依然として未 GA である。

## 今日のハイライト

### 1. Copilot Studio の課金開始点が「公開後」から「作り始めた瞬間」へ動いた — GitHub Copilot ハーネスは作成・テストから従量課金

**要点**: GitHub Copilot ハーネスで作るエージェントは、公開前の作成・プレビュー・評価生成の段階から **Copilot Credits** を消費する。ハーネスは後から変更できないため、前提は「公開してから課金」から「作り始める前に選び切る」へ変わる。

**詳細**: Copilot Studio のドキュメントが *harness*（ランタイム層）を軸に再編された。ハーネスは設計物とモデルの間に位置し、いつモデルを呼ぶか・何を送るか・返答をどう解釈してどのツールを呼ぶかを決める。3種類が定義されている。

- GitHub Copilot ハーネス: 推論重視の多段階業務向け。Word / Excel / PowerPoint / PDF をネイティブに作成・編集し、Skills と Memory に対応する。各タスクはサンドボックスで実行され、課金は Copilot Credits
- 標準ハーネス: ルールベースのエージェントとエージェントフロー向け。ライセンス・課金は従来の `billing-licensing` の体系のまま
- Copilot チャットハーネス: M365 Copilot Chat の拡張向け。消費ベース、または M365 Copilot ユーザーサブスクリプションライセンスに含まれる

課金対象は LLM トークン・ツール（ナレッジと MCP を含む）・ハーネス自体の3つで、いずれかを使う体験はすべてクレジットを消費する。標準ハーネスが publish 後に課金を始めるのに対し、GitHub Copilot ハーネスは**構築を始めた時点から**課金し、自然言語でのソリューション作成・エージェントのプレビューとテスト・評価の生成がいずれも消費対象になる。クレジットが尽きると、エンドユーザー側はエージェントが応答を停止し、メーカー側は自然言語オーサリング・プレビュー/テスト・評価生成ができなくなる（業務停止を避けるため一定のオーバレージは猶予される）。調達は Azure サブスクリプション経由の従量課金メーターと、1年前払いの事前購入プラン（CCCU プール）の2通りで、配分と監視は Power Platform 管理センター、エージェント単位の消費は Monitor ページで確認する。

あわせて、選んだハーネスを後から変更できない制約も一次ページに明記された。

- 移行不可: GitHub Copilot ハーネスで作ったエージェントは標準ハーネスへ移せず、逆方向も同様に移せない。どちらを使うかは新規作成時に決める
- 共有は閲覧まで: 共有パネルで付与できるのは閲覧権限だけで、編集を許可するにはホーム画面で「Use GitHub Copilot harness」をオフにする必要がある。共有先は Copilot Studio のユーザー単位ライセンス保有者に限られ、対象エージェントのユーザー認証が Authenticate with Microsoft に設定されていることが前提になる
- 実行だけ許す場合: Organization & data の End user access を「Everyone in your organization」に切り替えると、相手はエージェントを探して使えるが詳細の閲覧も編集もできない
- 前提条件: 自然言語での作成体験は Anthropic モデルを使うため、Anthropic モデルへのアクセスが有効な環境でしか利用できない

- https://learn.microsoft.com/en-us/microsoft-copilot-studio/harnesses-overview
- https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-experience/billing-credit-overview
- https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-experience/enforcement-policy-credits
- https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-experience/authoring-share-agent

### 2. MCP の Tier 1 SDK は4本とも既に安定版に到達していた — 「beta が取れるまで待つ」という保留理由が消えた

**要点**: TypeScript・Python・C# の MCP SDK が 7/27〜7/28 に **2.0.0** として出ており、Go も v1.7.0 で新仕様に対応済みだと本日パッケージレジストリで確認した。前提は「Tier 1 の GA は C# だけ」から「ステートレス化の保留理由はもう無い」へ変わる。

**詳細**: 前日の当サマリーは「Tier 1 のうち GA 到達は C# が最初で、Python / TypeScript / Go は beta のまま」と書いたが、これは誤りだった。npm / PyPI / GitHub Releases を直接照会した結果は次のとおり。

- TypeScript: `@modelcontextprotocol/server` と `@modelcontextprotocol/client` がともに 2.0.0（2026-07-27 23:55 UTC）。4本のうち最初の安定版で、C# より半日早い
- Python: `mcp` 2.0.0（2026-07-28 13:45 UTC）。`2.0.0rc1` は前日の 7/27 13:35 UTC
- C#: v2.0（7/28）
- Go: v2 を出していない。`modelcontextprotocol/go-sdk` は **v1.7.0**（7/28）のまま、仕様 `2026-07-28` のステートレス・Multi Round-Trip Requests・HTTP 標準化に対応した

メジャーバージョンで揃っていないため、SDK 名とバージョン番号から対応状況を推測すると読み違える。TypeScript はパッケージ名そのものが変わっている点にも注意が要る。旧 `@modelcontextprotocol/sdk` は 1.30.0（7/27 17:56 UTC）で更新が止まり、server / client の2パッケージへ分割された。依存を `@modelcontextprotocol/sdk` のまま上げても新仕様には移れない。

- https://www.npmjs.com/package/@modelcontextprotocol/server
- https://pypi.org/project/mcp/
- https://github.com/modelcontextprotocol/go-sdk/releases
- https://blog.modelcontextprotocol.io/posts/2026-07-28/

### 3. Cursor の DeepJack が最新ビルド 3.9.8 でも再現する — 1クリックと1承認で攻撃者の MCP サーバーが常駐する

**要点**: 細工した `cursor://` ディープリンクを1回クリックし確認ダイアログを1回承認するだけで、攻撃者が用意した MCP サーバーが開発者の権限で常駐する。前提は「MCP は配る側を統制すれば足りる」から「リンクを踏む側の統制が要る」へ変わる。

**詳細**: Adversa AI が 7/15 に公開した脆弱性クラスで、**3.9.8** でも再現するとされる。手口は2段構えになっている。

- 表示の回避: インストールダイアログの1行テキストボックスに空白を詰め、悪意あるコマンドを右端の画面外へ押し出す
- 検知の回避: `pr-review` の URL パラメータ内に別の `mcp/install` URI を入れ子にすると、Cursor が再帰的にデコードしないため気づけない

これは引数を表示する修正が入っていた **CVE-2025-54133** の回避にあたる。Cursor は 4/27 に社内で根本原因を確認していたが、8月時点のビルドでも再現するとされており、修正の到達が確認できていない。07-31 の Claude 共有リンクの検索エンジン露出、08-01 の Ruflo と同じく、既定設定と導線に起因する類型である。

- https://adversa.ai/blog/cursor-security-deepjack-deeplink-vulnerability-mcp-rce/
- https://www.proofpoint.com/us/blog/threat-insight/cursorjack-weaponizing-deeplinks-exploit-cursor-ide
- https://adversa.ai/blog/top-agentic-ai-security-resources-august-2026/

## カテゴリ別まとめ

### Anthropic / Claude

- Anthropic の一時的な上限緩和2本は、期限が2週間ずれて切れる — Cowork のモバイル・Web 展開（7/7 ベータ開始）に合わせた利用上限の倍増措置は **8/5** で終了し、Claude Code の週次利用上限+50% は **8/19** まで再延長された。Cowork 側はセッションのクラウド実行やデバイス間の引き継ぎといった機能自体は残るが、消費枠だけが通常に戻る。Claude Code 側の対象は Pro / Max / Team / シート課金の Enterprise で、Free と従量課金 Enterprise は対象外、適用に設定は不要で CLI・IDE 拡張・デスクトップ・Web のすべてに効く。5月開始の措置が 7/19 → 8/19 と月単位で更新されている形にあたる。
  https://claude.com/blog/cowork-web-mobile
- Anthropic は Claude Code を10日連続で更新していない — 最新は v2.1.220（7/25）のままで、Claude Platform の release notes も 7/24 エントリが最新（11日間追加なし）である。一次 changelog の WebFetch は本日も成功しているため、取得失敗ではなくリリースが出ていない状態にあたる。
  https://code.claude.com/docs/en/changelog
- Cognizant が Claude Partner Network の Global Premier Partner に昇格した（7/27・本日初検出）— 2025年後半に始めた提携の拡張で、Cognizant の業務・エンジニアリングプラットフォームへ Claude を組み込み、自社の Frontier Certified ワークフォースモデルの一部として Claude 認定人材を増やす。Claude トレーニング修了者は **30,000人超**で、製薬の契約レビュー40%高速化、保険引受担当者あたり週8時間の削減という運用実績を挙げている。
  https://news.cognizant.com/2026-07-27-Cognizant-and-Anthropic-expand-partnership-to-embed-Claude-in-Cognizants-industry-platforms,-helping-clients-close-the-gap-between-AI-promise-and-business-outcomes

### OpenAI

- OpenAI が Priority Processing を廃して Fast mode に置き換えていたことを、一次 changelog で確認した — 到達不可だった `developers.openai.com/changelog` と `community.openai.com` が本日読めるようになり、7/30 エントリの本文を確認できた。速度を金で買う経路が別物になり、二次報道の一致に頼っていた値下げ幅も一次の数値に置き換わった。
  https://developers.openai.com/changelog/
  - 値下げ幅: GPT-5.6 **Luna は 80% 減**、Terra は 20% 減。当リポジトリが 07-31 以降 CNBC / Axios 等の一致で採ってきた数値と一致した
  - Fast mode: GPT-5.6 Sol で標準比 最大2.5倍速・2倍価格。既存の priority リクエストは後方互換で受け付けられる
  - 値下げの根拠: GPU カーネル改善によるサービングコスト20%減と、トークン生成効率15%改善と説明されている
- 同じ経路で 7/28〜7/29 の未検出項目も確定した — 公式 Terraform provider が出ており、プロジェクト・ユーザー・グループ・ロール・サービスアカウント・証明書・招待・プロジェクト単位のレート上限を IaC で管理できる。あわせて文字起こしモデル2種が加わった。
  - `GPT-Transcribe`: 非同期の文字起こし
  - `GPT-Live-Transcribe`: 低遅延ストリーミング。いずれも自由記述の文脈指定・キーワードヒント・複数の想定入力言語に対応し、Common Voice 22言語で 19.70% の誤り率
- OpenAI は Codex CLI の pre-release 0.147.0-alpha.1.2 を公開した（8/3 17:22 UTC）— 安定版 0.146.0（7/29）は据え置きで、リリースノートが付いておらず内容は不明である。
  https://github.com/openai/codex/releases

### Google / DeepMind・xAI

- Google が Gemini API の8月停止スケジュールを一次で確定させた — 当リポジトリは 08-01 以降これらを「一次未確認」と注記してきたが、`ai.google.dev` の到達性が回復し deprecations ページ本体を読めた。表に載る停止日は「最も早い可能性のある日付」であり、実際の廃止前に別途予告が出るとページに明記されている。
  https://ai.google.dev/gemini-api/docs/deprecations
  - **8/17 停止**: `imagen-4.0-generate-001` / `imagen-4.0-ultra-generate-001` / `imagen-4.0-fast-generate-001` の3本。移行先はいずれも `gemini-3.1-flash-image`
  - **8/31 停止**: `gemini-robotics-er-1.6-preview`。後継の Gemini Robotics ER 2 は 7/30 に public preview へ入り、`gemini-robotics-er-2-preview` と `gemini-robotics-er-2-streaming-preview` の2本が使える
- Gemini API のティア別単価も一次ページで確定できた — 料金ページが復旧し、二次スニペットに頼らず単価を確認できた（`ai.google.dev` の成功は2日連続）。Paid Tier ではコンテキストキャッシングと Batch API（50%減）が使え、入力コンテンツは製品改善に使われない。Free Tier は逆に製品改善に使われる。
  https://ai.google.dev/gemini-api/docs/pricing
  - Gemini 3.6 Flash: 入力 $1.50 / 出力 $7.50（100万トークン）、Batch は半額の $0.75 / $3.75
  - Gemini 3.5 Flash-Lite: 入力 $0.30 / 出力 $2.50、Batch $0.15 / $1.25
  - Gemini 2.5 Flash-Lite: 入力 $0.10 / 出力 $0.40
  - Google Search Grounding は Gemini 3.x で月5,000件まで無料
- Gemini 3.6 Flash と 3.5 Flash-Lite の 7/21 GA が一次 changelog でも裏づけられた — 前日は公式ブログ URL の検索出現で確定扱いにしていた。changelog 側は 3.6 Flash について「トークン効率とコード/エージェント計画能力の改善」と記載し、`temperature` / `top_p` / `top_k` の非推奨化を明示している。
  https://ai.google.dev/gemini-api/docs/changelog
- Gemini Enterprise アプリの global リージョンから、本日 8/4 に Gemini 3.5 Flash が削除される — モデル ID を直書きした Gemini Enterprise 上のワークフローは今日から動作が変わる。移行先は 7/21 に安定版が出た Gemini 3.6 Flash と 3.5 Flash-Lite が前提になっている。⚠️ `docs.cloud.google.com` はゲートウェイ拒否が続いており、Master 側は一次未確認としている。
  https://docs.cloud.google.com/gemini/enterprise/docs/release-notes
- xAI の Grok 4.6 は本日 8/4 時点で未公開のままである — 8/7 前後という目標時期は変わっておらず、1.5T・Grok 4.5 と同じ V9 基盤を再利用し SFT と RL で伸ばす位置づけ、後続の 2.1T Grok 4.7 は数週間後とされる。⚠️ SEO 系サイトが「8/7 に launched」と完了形で書く状態が続いているが、xAI はモデルカード・API ドキュメント・価格・ベンチマークのいずれも出していない。

### Microsoft / Copilot Studio / Power Platform

- GitHub Copilot ハーネスの従量課金とハーネス移行不可（ハイライト参照）
- Copilot Studio の製品チームが 8/3 付でハーネス導入記事を公開した — 「More powerful agents and workflows for autonomous business processes: Introducing a new harness for Copilot Studio」（記事ID 4542969）で、6/17 の「Meet the new Copilot Studio」以来約7週ぶりの新規記事にあたる。⚠️ 本文は techcommunity が 403 のため一次未確認で、記事の存在と日付は board RSS で確認した。内容面の裏づけはハイライト1の Learn 一次ページによる。
  https://techcommunity.microsoft.com/t5/copilot-studio-blog/more-powerful-agents-and-workflows-for-autonomous-business/ba-p/4542969
- Copilot Studio の定例ソースはハーネス再編を反映していない — What's New は June 2026 節が最新のままで7月節も8月節も立っておらず、June 節の10項目に増減はない。火曜が週次更新日の Released Versions も Build **2026.6.3**（6/30 初出）から動かず、7月ビルドがゼロのまま8月に入った。リージョン分布も UX 版（26.06.21-24）も据え置きである。
  https://learn.microsoft.com/en-us/power-platform/released-versions/copilotstudio
- 7月 GA 予定だった Power Platform の7機能は、8月に入って4日が経っても未 GA のままである — Release Wave の GA 列に新しい緑チェックは付かず、直近の GA は 7/16 の3機能（PGP 暗号化・復号、時間/コスト削減の自動計測、チェッカーの管理者通知）から動いていない。Power Platform Blog も月次「What's New」の7月号を出さないまま8月に入り、最新は 6/11 の June Feature Update のままである。
  - Power Automate（5件）: 削除したクラウドフローの復元、Process ライセンス容量の複数ワークフロー間での共有、統合 Power Apps によるフォーム UI、ワークキュー項目の CSV エクスポート、マシン・フロー稼働率のダッシュボード表示
  - Power Apps（2件）: code apps のコネクタ CLI 対応、FetchXML エディターでのオフラインプロファイル構成
  - 8月予定4件: Power Automate ライセンスダッシュボード改善（GA）、デスクトップフローのカスタムダッシュボードタイル（Preview）、Dataverse オンラインモードのキャンバスアプリ対応（Preview）、モデル駆動アプリの行要約強化（GA）
- Tech Community の board RSS が復旧し、403 期間中の取りこぼし2件が判明した — 7/4 以降続いていた 403 が本日 200 に戻り、7月号「What's New in Microsoft 365 Copilot | July 2026」の公開日が 7/31 であることを一次で確認できた。B-021 で起票した「月次記事の検知が単一経路に依存する」問題は、実際に単発記事も落としていたことになる。⚠️ いずれも本文は techcommunity 403 のため一次未確認である。
  - 7/23「1 million documents to 300+ agents: Building an enterprise-scale Microsoft 365 Copilot connector」— 100万文書・300超エージェント規模のコネクタ構築事例
  - 7/16「Join Us Live: Understanding Copilot Cowork and Managing Copilot Credits」— Cowork とクレジット管理のライブ配信告知
- M365 Copilot 側の一次ソースは本日いずれも据え置きだった — Release Notes は「July 29, 2026」節が最新のままで対象期間 7/15〜7/29 の全10項目に増減がなく、次バッチは隔週傾向どおりなら8月中旬の見込みである。拡張機能 What's New も「July 2026」節の2項目（宣言型エージェント manifest 1.8、利用状況レポート API 3種への `version` 追加）のままで8月節が立たず、M365 Blog 本体は 7/30 記事、Roadmap の Latest announcements は 7/9 の GPT-5.6、Developer Blog は 7/17 の統合マニフェスト GA 記事が最新である。
  https://learn.microsoft.com/en-us/copilot/microsoft-365/release-notes
- ガバナンス側も動きが小さい — Purview の What's new は7月節に Copilot 関連の新規項目が追加されておらず、Power Platform の非推奨一覧も先頭が Power Automate モバイルアプリの廃止（8/31 発効）のままである。Partner Center の8月アナウンスページ（`announcements/2026-august`）は本日も 404 で、8/1 に CSP 提供が始まった SMB 向け「Copilot in 30」（25ユーザー・30日）以降の変更は確認できていない。SharePoint Blog も 7月号（記事ID 4535420）が最新である。
  https://learn.microsoft.com/en-us/power-platform/important-changes-coming
- Microsoft のエージェント型セキュリティ基盤 Project Perception が 8/3 にパブリックプレビューへ移行した（7/27 発表）— 赤（攻撃経路と脆弱性のマッピング）・青（検出の調査と実リスク判定）・緑（是正措置と防御強化）のエージェントを協調させ、クラウド・エンドポイント・アプリ横断で脅威の発見から是正までを自動化する。初期リリースは MDASH 経由のソフトウェア脆弱性管理に絞り、Microsoft Defender のワークフローに攻撃シミュレーション・防御テスト・脅威シナリオ計画を統合する。あわせてセキュリティ専用の自社モデル MAI-Cyber-1-Flash も投入された。
  https://futurumgroup.com/insights/microsofts-project-perception-bets-on-agents-that-act-not-just-alert/
- 未発表の全二重音声モデル MAI-Realtime が MAI Playground 上で観測された（8/2・TestingCatalog のスクープ）— 同社初のネイティブ全二重（聞きながら話す）音声モデルで、音声2種（Victoria / Grant）・17言語・ターンテイキング2モード・遅延を出すデバッグパネルを備え、Web 検索などのツールを操作できる。会話の途中で言語を自動検出して切り替える設計で、MAI-Transcribe-1（聞く）・MAI-Voice-1（話す）と合わせ音声スタックの垂直統合が揃った。⚠️ 発表・モデルカード・価格・提供リージョンのいずれも無く、公開版カタログにも載っていない。
  https://www.testingcatalog.com/exclusive-microsoft-tests-new-mai-realtime-voice-model/
- GitHub が Copilot から Gemini 2.5 Pro と Gemini 3 Flash を廃止した（7/31）— 同日に Enterprise teams model policy targeting が public preview に入り、エンタープライズ内の特定チーム単位でモデルポリシーを当てられるようになった。8/26 発効の既定モデル有効化ポリシーと合わせ、8月中にモデル選択まわりの管理設定が2段階で変わる。モデル指定を固定している運用は選択肢の入れ替わりを前提にする必要がある。
  https://github.blog/changelog/label/copilot/

### 開発ツール

- MCP Tier 1 SDK の安定版到達と Cursor の DeepJack 再現（ハイライト参照）
- GitHub が Copilot CLI の pre-release v1.0.78-3 を公開した（8/3 16:35 UTC）— 安定版は v1.0.77（7/30）のままである。
  https://github.com/github/copilot-cli/releases
  - `/new-worktree`: worktree を新規作成してその中で新しい会話を開始する実験的コマンド。エージェントの並行作業を CLI 側で分離する初の仕組みにあたる
  - `$` が armed 状態のとき、Enter でインタラクティブシェルショートカットが起動しインラインヒントが出る
  - TTY を持たないローカルデスクトップのサブプロセス（IDE 統合を含む）で `copilot login` の既定がブラウザフローになった。リモート・ヘッドレスは device code のまま
- Cursor は本日 changelog と Announcements フォーラムの両方を一次で確認できたが、新規エントリは無かった — changelog の最新は iPad 対応と PR レビュー刷新（7/29）、フォーラムの最新は Cursor Start（7/28）である。ゲートウェイ拒否が解けたため、07-27 以降 WebSearch 頼りだった Cursor の追跡が一次に戻った。
  https://cursor.com/changelog
- Cognition の Devin は `docs.devin.ai` のゲートウェイ拒否が続いており、日付を確定できる新規リリースを検出できなかった — 既報の Devin Outposts（7/21 alpha）が最新のままである。
- Atlassian が AI ブラウザ Dia の Windows 版でウェイトリスト受付を開始した — 2025年9月に約 **$610M** で買収した The Browser Company の製品で、Windows 版の提供を今秋に予定する。Chromium ベースで Chrome の拡張エコシステムとの互換を保ちつつ、AI を「表示するもの」でなく情報収集・整理・作成の協働者として据える設計をとる。今後 iOS / Android / エンタープライズ版へ展開する。業務端末が Windows 中心の国内企業では、これまで macOS 限定で検証できなかった AI ブラウザが評価対象に入る。
  https://www.publickey1.jp/blog/26/aidiawindows.html

### オープンウェイト / ローカル LLM

- DeepSeek-V4-Flash-0731 の重み公開を Hugging Face の一次データで確認した — `huggingface.co` の到達性回復後はじめての一次確認で、08-02〜08-03 の二次情報依存が解消した。作成は 2026-07-31 07:30 UTC、最終更新 2026-08-01 03:07 UTC、ライセンス **MIT**、ファイル74件、ダウンロード **236,076** である。
  https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-0731
  - ⚠️ 前日の記述の訂正: `safetensors.total` は 304,180,418,494（≒304B）で、一次では総パラメータ 304B しか確認できない。08-03 に書いた「HF 表示の 304B は DSpark 投機的デコードのドラフトモデル込みで、本体は 284B 総 / 13B アクティブ」は二次情報側の主張であり、内訳の分離は引き続き二次情報依存である
- 本日新規に公開された注目のオープンウェイトモデルは無い — HF の trending 上位30件を照会したところ、`zai-org/GLM-5.2`（6/16 作成）・`Kwaipilot/KAT-Coder-V2.5-Dev`（7/23）・`poolside/Laguna-S-2.1`（7/13）・`upstage/Solar-Open2-250B`（7/22）はいずれも既存で、8/3〜8/4 の新規作成は無かった。

### 規制・政策

- Anthropic がオープンウェイトモデルへの立場を公式に表明していた（7/27・本日初検出）— 7/24 に NVIDIA のサイトでホストされた公開書簡「Open Weights and American AI Leadership」に Anthropic だけが署名せず、立場を巡る憶測が広がったことへの回答である。Dario Amodei は「Anthropic はオープンウェイトモデルの禁止を主張したことはない」と書き、危険な能力を持たないオープンウェイトモデルは実行コスト以外の負担がない公共財だとした。
  https://www.anthropic.com/news/position-open-weights-models
  - 規制の焦点として挙げた3点: 強力なチップを権威主義国家の手に渡さないこと、産業規模の蒸留を止めること、十分に高性能なモデルは開放・閉鎖を問わず安全性テストを義務化すること
  - ⚠️ 「オープンウェイトの方が安全策の開発が容易になる」「広い利用機会は攻撃側より防御側を利する」という主張には、とくに生物兵器分野で同意しないと明示している
- FCC が中国製のヒト型・四足ロボットを Covered List に追加した（7/28）— 新規・未認証機種は米国内の機器認証を受けられなくなる。対象はヒト型ロボットと四足歩行ロボット（ロボット犬）、および系統連系用のネットワーク接続型パワーインバーターで、既に認証済みの機種・購入済みの機体・連邦政府の利用は対象外である。国防総省（Department of War）が Conditional Approval を出せば個別に例外となる。中国は世界のヒト型ロボット供給の推定約 **85%** を占めており、フィジカルAI の調達先は価格より認証可否が先に来る。7/30 の Gemini Robotics 2（08-02 収録）で VLA モデルのオンデバイス実行が実用段階に入った直後に、機体側の調達経路が地政学で分断された形にあたる。
  https://www.nbcnews.com/tech/tech-news/us-bans-foreign-made-humanoid-robots-targeting-china-national-security-rcna589777
  https://www.therobotreport.com/industry-reacts-fcc-ban-u-s-imports-new-humanoid-quadruped-robots/
- Google Earth の AI 衛星画像生成が公開1日で撤回された — 7/30 に Nano Banana 2 の画像生成を組み込み、プロンプトから実際の衛星・航空・3D 画像の上にフォトリアルな AI シーンを重ねてダウンロード・共有できるようにしたが、翌 7/31 に停止した。公開直後から倒壊したエッフェル塔、炎上する都市、サンフランシスコのクレーターなどが生成され、検証した調査者は「何も拒否されなかった」と述べている。8/2 に適用開始した EU AI Act 第50条（AI生成コンテンツの機械可読マーキング・既収録）が問題にしているのはまさにこの類型で、マーキング義務の実効性がベンダー側の自主判断に依存していることを示す実例になった。
  https://www.npr.org/2026/07/31/nx-s1-5914652/google-adds-ai-to-satellite-images-raising-fears-of-deepfakes-in-the-sky
- 米政府のフロンティアモデル事前審査枠組みは 8/1 の期限を越えて未公表のままである — EO 14409（6/2 署名）が課した60日期限は 8/1 に満了したが、本日時点でも Federal Register 告示・NIST / CISA 公表・OSTP 声明のいずれも確認できていない。OpenAI / Anthropic / Google と最終調整段階で Meta は不参加、対象モデルの判定は NSA 長官の単独権限という構図は 08-03 から変化がない。OpenAI の Astra（08-02 収録）がこの枠組みを通る最初のモデルになる見込みである。

### 市場・エコシステム

- クラウドインフラ市場が四半期 **$143.4B**・前年同期比 **+43%** へ伸びた — Synergy の Q2 2026 で、成長率は過去8年で最高、加速は11四半期連続で、その間に市場規模は倍になった。世界シェアは AWS 28%（据え置き）・Microsoft Azure 20%（前四半期21%から-1pt）・Google Cloud 15%（同14%から+1pt）で上位3社が63%を占める。加速の主因は生成AIで、生成AI関連クラウドサービスは+165%だった。7/29〜7/30 の各社決算（Azure +43%・AWS +36.7%）とも整合し、決算単体でなくシェアの分母つきで引用できる。⚠️ 国内報道（Publickey）は成長率を42%としているが、Synergy 一次リリースの値は43%である。
  https://www.srgresearch.com/articles/q2-cloud-market-passes-143-billion-highest-growth-rate-in-eight-years
  https://www.publickey1.jp/blog/26/aws28google_cloud1154220262synergy_research.html
- AI が見つけた脆弱性は「量は増えたが危険度は変わらない」と VulnCheck が報告した — State of Exploitation 1H-2026 で、AI支援によって発見された脆弱性 1,061件のうち実環境での悪用が確認されたのは **14件（1.3%）**にとどまり、同期間の全脆弱性の悪用率とほぼ同水準だった。Anthropic の Project Glasswing は23,000件超の指摘を出したが、CVE として公開されたのは126件、悪用確認は1件のみである。一方で悪用そのものは速くなっており、CVE 公開から KEV 登録までの中央値は2025年の120日から2026年上期は80日へ短縮し、上期の KEV は約500件だった。AIセキュリティ製品の評価で「発見数」を成果指標に置くと過大評価になる根拠になる。
  https://www.vulncheck.com/blog/state-of-exploitation-1h-2026
- CNCF と SlashData が国内クラウドネイティブ開発者を約95万人と推計した — 「日本におけるクラウドネイティブ開発の現状 2026」で、2026年Q1 時点の数値である（国内報道の見出しは「約100万人」）。95カ国12,500人超の開発者調査に日本市場の分析を重ねたもので、KubeCon + CloudNativeCon Japan 2026 に合わせて発表された。日本固有のインフラ戦略、プラットフォームエンジニアリングの成熟、AI需要が牽引要因として挙がっている。
  https://www.linuxfoundation.org/ja-jp/news/cncf-and-slashdata-report-finds-japans-cloud-native-community-reaches-nearly-1-million-developers
- AIデータセンター向けメモリの争奪が消費者向け PC の納期に出てきた — Apple の MacBook Air が全ベース構成で8月末出荷、構成によっては9月初旬着という異例の品薄になっている。原因は需要増ではなく、メーカーがより収益性の高い AIデータセンター向け HBM へ生産能力を意図的に振り向けている構造的な再配分で、データセンター向け DRAM の需要は世界消費量の約50%（5年前は32%）に達した。7/30 の Amazon 決算（08-01 収録）で Jassy が capex 増額分をメモリ価格上昇に帰した話が、川下の完成品側に出てきた形にあたる。ハードウェア更新を含む計画は調達リードタイムを2026年後半にわたって見込む必要がある。
  https://gigazine.net/news/20260803-apple-macbook-air-shortage/
- Horizon3.ai が Series E で $250M を調達し評価額 $2B 超になった（8/3 発表）— 1年強前の Series D（評価額$650M）から評価額が3倍になった。オーバーサブスクライブしたラウンドは既存投資家の NightDragon と NEA が共同リードし、新規7社・再参加5社が加わった。自律ペンテスト基盤 NodeZero は銀行や病院を含む本番稼働環境で人間を介さずに侵入テストを実行する設計で、ARR は前年比+120%、保護対象は7,000組織超（Fortune 10 のうち4社を含む）である。08-01 の Anthropic 評価用モデルによる実在3組織への不正アクセス、上記 VulnCheck のデータと合わせ、攻撃側の自動化を前提にした検証サービスへ資本が集中している。
  https://horizon3.ai/news/press-release/horizon3-raises-250m-series-e-at-2b-valuation-to-lead-the-ai-vs-ai-cybersecurity-era/
- Ai4 2026 が本日 8/4 に開幕し、主題が「エージェントの概念」から「大規模運用の統制」へ移った — ラスベガス The Venetian で 8/4〜8/6 に開催され、本日 8:30（PT）から基調講演が始まる。8/5 のメインステージには Geoffrey Hinton・Fei-Fei Li・Andrew Ng が同席し、展示は約400社規模である。エンタープライズ向けの大型カンファレンスとしてはじめて「大規模なエージェント運用」が最大クラスタになったと報じられており、論点は「エージェントに何ができるか」から「人間がレビューできる速度を超えて意思決定するエージェントをどう統制・認可・監査するか」へ移っている。
  https://ai4.io/

## 直近の注目予定

- **8/4（本日）**: Gemini Enterprise の global リージョンから Gemini 3.5 Flash を除外 ／ Copilot Studio Released Versions の火曜定例更新（本日時点で 2026.6.3 据え置き） ／ Ai4 2026 開幕（〜8/6）
- **8/5**: Opus 4.1 の Claude API 退役 ／ Cowork 倍増利用枠終了 ／ Ai4 メインステージ（Hinton・Fei-Fei Li・Ng）
- **8/6**: ChatGPT Business の利用無償期間終了（以後は柔軟課金へ）
- **8/7 前後（推定）**: Grok 4.6（1.5T）
- **8/9**: ChatGPT Atlas シャットダウン
- **8/10（月）**: 週次復旧チェック ／ Power Platform Weekly の夏季休刊明け
- **8/17**: Claude Console 旧 Workbench 退役 ＋ 実験的プロンプトツール API 廃止 ／ Gemini API の Imagen 4.0 系3本を停止（一次確認済み）
- **8/18〜9/8**: Microsoft 365 Copilot Agent's Playbook ライブストリーム（各回 9AM PT）
- **8/19**: Claude Code 週次上限50%増の終了
- **8/20**: Gemini Enterprise Agent Platform の Grok 4.1 ファミリー停止（一次未確認）
- **8/26**: OpenAI Assistants API 廃止 ／ o3 退役 ／ GPT-4.5 完全廃止 ／ Copilot 既定モデル有効化ポリシー発効
- **8/31**: Sonnet 5 導入価格終了（→ $3/$15） ／ Power Automate モバイルアプリ廃止 ／ `gemini-robotics-er-1.6-preview` 停止（一次確認済み）
- **8月上旬**: Partner Center 8月アナウンスの公開（本日時点で 404）
- **8月中旬**: M365 Copilot Release Notes 次バッチ見込み（7/29 バッチから隔週）
- **8月見込み**: 7月 GA 予定から持ち越した Power Platform 7機能 ／ Release Wave の8月予定4件
- **9月**: iOS 27 / macOS 27 GA。App Store の新規申請・更新で Social Media 用の年齢レーティング回答が必須化
- **秋**: Dia ブラウザ Windows 版の提供
- **11/12**: EU AI ギガファクトリー入札の応募締切
- **12/2**: EU AI Act の生成コンテンツ標識義務、8/2 以前に市場投入済みシステムへの猶予が終了

## 改善メモ

- B-023（Master・新規）: 復旧したソースの取得方法欄を WebSearch から一次へ戻す一括改訂を行う
- B-022（Copilot・新規）: Copilot Studio のライセンス・課金ドキュメント群が未登録で、ハーネス別課金への再編を偶然検知した
- Industry: 新規提案なし
- 継続提案: Master 7件（最多 B-013 9回目）、Copilot 13件（最多 B-011 16回目）、Industry 5件（最多 B-004 36回目）
- 障害の変化（復旧）: Master 側でゲートウェイ拒否が大規模に解消し、`cursor.com` / `forum.cursor.com` / `claude.com` / `support.claude.com` / `community.openai.com` / `github.blog` / `aws.amazon.com` / `devblogs.microsoft.com` の8ホストが curl 200 に復帰した。Copilot 側は `learn.microsoft.com` の WebFetch 直取得（`/api/lists/` を含む）・techcommunity board RSS 2本・devblogs RSS が復旧し、Industry 側は `ai.google.dev` の成功を2日連続で確認した
- 障害の変化（未復旧）: `www.testingcatalog.com` / `simonwillison.net` / `x.ai` / `docs.devin.ai` / `obsidian.md` / `deepmind.google` / `blog.google` / `workspaceupdates.googleblog.com` / `docs.cloud.google.com` / `learn.chatgpt.com` / `techcrunch.com` / `thinkingmachines.ai` はゲートウェイ拒否のまま。`www.anthropic.com` / `openai.com` / `help.openai.com` / `alignment.anthropic.com` はオリジン403、`www.publickey1.jp` / `www.srgresearch.com` も403が続く
- 前日からの訂正2件
  - MCP Tier 1 SDK の GA 状況: 08-03 に「GA 到達は C# が最初、他3本は beta」と書いたが、TypeScript が半日早く、Python も 7/28 に 2.0.0 が出ていた（ハイライト参照）
  - DeepSeek-V4-Flash-0731 のパラメータ内訳: 08-03 の「本体 284B 総 / 13B アクティブ」は二次情報側の主張で、一次で確認できるのは総 304B のみである（カテゴリ参照）
- ソース間の差分: MAI-Realtime について、Master は「発表・モデルカード・価格・提供リージョンのいずれも無く公開版カタログにも載っていない」という未確認性の警告を、Industry は17言語・音声2種・言語自動切り替え・MAI 音声スタックの垂直統合という位置づけを持っていた。いずれも他方には無い情報のため両方を採用した
- ソース間の矛盾: 本日は確認されなかった（クラウド市場成長率の 43% と 42% の差は Industry 内で一次側 43% に寄せて解決済み）
