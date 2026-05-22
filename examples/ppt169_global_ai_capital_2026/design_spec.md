# global_ai_capital_2026 - Design Spec

## I. Project Information

| Item | Value |
| ---- | ----- |
| **Project Name** | global_ai_capital_2026 |
| **Canvas Format** | PPT 16:9 (1280×720) |
| **Page Count** | 18 |
| **Design Style** | B) General Consulting + Bloomberg/Economist 新聞資訊圖風 |
| **Target Audience** | 科技/金融行業研究者、AI 從業者、風險投資圈、媒體編輯 |
| **Use Case** | 行業洞察分享 / 投資簡報 / 媒體解讀專欄 |
| **Created Date** | 2026-05-16 |

---

## II. Canvas Specification

| Property | Value |
| -------- | ----- |
| **Format** | PPT 16:9 |
| **Dimensions** | 1280×720 |
| **viewBox** | `0 0 1280 720` |
| **Margins** | 左右 60px / 上下 50px |
| **Content Area** | 1160×620（頁首 80 + 主體 560 + 頁尾 30） |

---

## III. Visual Theme

### Theme Style

- **Style**: B) General Consulting + Bloomberg/Economist 新聞資訊圖風
- **Theme**: Dark theme
- **Tone**: 冷靜、剋制、出版級、資料導向；不是 keynote 衝擊力，而是夜讀財經長稿的深思感

### Color Scheme

| Role | HEX | Purpose |
| ---- | --- | ------- |
| **Background** | `#0E1116` | 深石墨黑（不是純黑） |
| **Secondary bg** | `#1A1F26` | 卡片 / 分割槽底色 |
| **Primary** | `#E8E6E1` | 報紙暖白 — 主文字、標題 |
| **Accent** | `#E63946` | 財經紅 — 風險、警示、關鍵數字 |
| **Secondary accent** | `#F4A261` | 琥珀金 — 次級強調（中國 / 二線公司） |
| **Body** | `#C9C5BE` | 暖灰白 — 正文 |
| **Secondary text** | `#8A857E` | 註釋 / 頁尾 |
| **Tertiary text** | `#5C5852` | 極輕資訊 / 來源行 |
| **Border** | `#2A2F36` | 極細分割線 |
| **Success** | `#52B788` | 正向趨勢（綠漲） |
| **Warning** | `#E63946` | 複用 accent |

### AI Image Strategy

- **Image Rendering**: editorial
- **Image Palette**: dark-cinematic

### Gradient Scheme

```xml
<linearGradient id="scrim_v" x1="0%" y1="0%" x2="0%" y2="100%">
  <stop offset="0%" stop-color="#0E1116" stop-opacity="0.3"/>
  <stop offset="100%" stop-color="#0E1116" stop-opacity="0.92"/>
</linearGradient>

<linearGradient id="accentLine" x1="0%" y1="0%" x2="100%" y2="0%">
  <stop offset="0%" stop-color="#E63946" stop-opacity="1"/>
  <stop offset="100%" stop-color="#E63946" stop-opacity="0"/>
</linearGradient>
```

---

## IV. Typography System

**Typography direction**: 報刊編輯派 — 西文襯線 Cambria 扛標題與大字 hero number，中文走 Microsoft YaHei，正文 Latin 用 Arial 走數字精度

| Role | Chinese | English | Fallback tail |
| ---- | ------- | ------- | ------------- |
| **Title** | `"Microsoft YaHei"` | `Cambria` | `serif` |
| **Body** | `"Microsoft YaHei", "PingFang SC"` | `Arial` | `sans-serif` |
| **Emphasis** | `"Microsoft YaHei"` | `Georgia` | `serif` |
| **Code** | — | `Consolas, "Courier New"` | `monospace` |

**Per-role font stacks**:

- Title: `Cambria, "Microsoft YaHei", serif`
- Body: `"Microsoft YaHei", "PingFang SC", Arial, sans-serif`
- Emphasis: `Georgia, "Microsoft YaHei", serif`
- Code: `Consolas, "Courier New", monospace`

### Font Size Hierarchy

**Baseline**: Body font size = **16px**（chart-heavy 高密度）

| Purpose | Ratio to body | Px @ 16 | Weight |
| ------- | ------------- | ------- | ------ |
| Cover title (hero headline) | 4-5x | 64-80px | Bold |
| Chapter / section opener | 2.5-3x | 40-48px | Bold |
| Page title | 1.5-2x | 24-32px | Bold |
| Hero number (大數字) | 4-6x | 64-96px | Bold（Cambria） |
| Subtitle | 1.2-1.5x | 19-24px | SemiBold |
| **Body content** | **1x** | **16px** | Regular |
| Annotation / caption | 0.7-0.85x | 11-14px | Regular |
| Page number / footnote | 0.6-0.7x | 10-11px | Regular |

---

## V. Layout Principles

### Page Structure

- **Header area**: 上 50px — 章節番號 + 章節名（左對齊，11px tertiary） + 極細分割線
- **Content area**: 中 560px — 主視覺化 / hero number / chart
- **Footer area**: 下 30px — 頁碼 + Sources 註腳 + 極細頂部分割線

### Layout Pattern Library

> 本 deck 主導佈局：**Asymmetric split（3:7 chart vs 註解）/ Single column centered（封面 / 章節）/ Three-column（KPI cards）/ Top-bottom split（帶 hero band 的圖表 + 註腳）/ Full-bleed + floating text（3 張氛圍圖章節頁）**。Z-pattern 與 Matrix grid 出現在 quadrant_text_bullets 頁。

### Spacing Specification

**Universal**:

| Element | Range | This Deck |
| ------- | ----- | --------- |
| Safe margin | 40-60px | 60px |
| Content block gap | 24-40px | 28px |
| Icon-text gap | 8-16px | 10px |

**Card-based**:

| Element | Range | This Deck |
| ------- | ----- | --------- |
| Card gap | 20-32px | 24px |
| Card padding | 20-32px | 22px |
| Card border radius | 8-16px | 6px（剋制，不要圓胖） |

**Non-card** (breathing 頁 / 氛圍底圖):
- Line-height: 1.5× body
- Full-bleed text 用 `scrim_v` 漸變扛 legibility
- 不強行列寬對齊，按報刊導語自由 inset

---

## VI. Icon Usage Specification

### Source

- **Library**: `tabler-outline`（stroke 1.5）
- **Brand-logo library**: `simple-icons`（用於 OpenAI / Anthropic / xAI / Nvidia / Google / Microsoft / Amazon / Meta / Oracle / SoftBank 等 logo 標識）
- **Usage**: `<use data-icon="library/icon-name" .../>`

### Recommended Icon List

| Purpose | Icon Path | Page |
| ------- | --------- | ---- |
| Trending up（資本流入） | `tabler-outline/trending-up` | P04, P05, P11 |
| Currency dollar（估值） | `tabler-outline/currency-dollar` | P04, P06, P09 |
| Building（公司） | `tabler-outline/building` | P06, P09 |
| Chart bar（資料） | `tabler-outline/chart-bar` | P05, P15 |
| Server（基建） | `tabler-outline/server` | P14, P15 |
| Bolt（電力） | `tabler-outline/bolt` | P05, P14 |
| Alert triangle（風險） | `tabler-outline/alert-triangle` | P15, P16, P17 |
| Globe（全球） | `tabler-outline/globe` | P04, P09 |
| Cpu（晶片） | `tabler-outline/cpu` | P12, P13 |
| Trending down（衰減） | `tabler-outline/trending-down` | P15, P16 |
| Arrow right（流向） | `tabler-outline/arrow-right` | P12, P14 |
| Bookmark（章節標誌） | `tabler-outline/bookmark` | 章節頁 |
| OpenAI 品牌 | `simple-icons/openai` | P06, P08, P14 |
| Anthropic | `simple-icons/anthropic` | P06 |
| Nvidia | `simple-icons/nvidia` | P12, P13 |
| Google | `simple-icons/google` | P05, P06 |
| Microsoft | `simple-icons/microsoft` | P05 |
| Amazon | `simple-icons/amazon` | P05 |
| Meta | `simple-icons/meta` | P05 |
| Oracle | `simple-icons/oracle` | P14 |
| SoftBank | `simple-icons/softbank` | P14 |

---

## VII. Visualization Reference List

Catalog read: 71 templates

| Page | Template | Path | Summary-quote (verbatim) | Usage |
| ---- | -------- | ---- | ------------------------ | ----- |
| P04 | kpi_cards | `templates/charts/kpi_cards.svg` | "Pick for 4-8 standalone numeric metrics shown as overview cards (2x2 or 1x4) — exec summary opener, " | Q1 風投總盤子四大 KPI（VC 總額 / AI 佔比 / 三筆大單 / 集中度） |
| P05 | bar_chart | `templates/charts/bar_chart.svg` | "Pick for single-series category value comparison, 3-8 categories. Skip for >12 long-label items (use" | Amazon / Microsoft / Google / Meta 四家 capex 對比 |
| P07 | dumbbell_chart | `templates/charts/dumbbell_chart.svg` | "Pick for before-vs-after or two-state difference across 5-10 items. Skip for single snapshot (use ba" | OpenAI/Anthropic/xAI 估值前後對比（年初 vs Q2） |
| P08 | bubble_chart | `templates/charts/bubble_chart.svg` | "Pick for 3-axis data (x position, y position, size). Skip for plain x-y correlation (use scatter_cha" | 三巨頭 估值 × ARR × 投資人數 散點 |
| P09 | donut_chart | `templates/charts/donut_chart.svg` | "Pick for 3-6 part proportions where a center KPI/total deserves emphasis. Skip if no center value to" | OpenAI $122B 投資人構成（Amazon/Nvidia/SoftBank/MSFT/其他） |
| P10 | horizontal_bar_chart | `templates/charts/horizontal_bar_chart.svg` | "Pick for ranking 5-12 items, especially with long labels. Skip if <=8 short-label items (use bar_cha" | 中國陣營 5 家估值排名（DeepSeek/Zhipu/MiniMax/Moonshot/StepFun） |
| P11 | comparison_table | `templates/charts/comparison_table.svg` | "Pick for 2-4 plans/products compared across many feature rows (dense matrix). Skip for pricing-tier " | 中美 AI 資本路徑雙軌對比（私募規模/IPO/政府/估值峰值/退出方式） |
| P12 | sankey_chart | `templates/charts/sankey_chart.svg` | "Pick for 3-stage flow with magnitude (sources -> nodes -> sinks). Skip for simple linear conversion " | Nvidia 閉環：股權投資 → AI 公司 → 晶片採購迴流 |
| P13 | pareto_chart | `templates/charts/pareto_chart.svg` | "Pick for 80/20 contribution: descending bars + cumulative line. Skip if cumulative line is not t" | Nvidia 客戶集中度 85% 來自 6 家 |
| P14 | hub_spoke | `templates/charts/hub_spoke.svg` | "Pick for 1 core capability + 4-8 surrounding capabilities (platform/ecosystem); each spoke = title o" | Stargate 專案 hub + 7 個資料中心站點 |
| P16 | dual_axis_line_chart | `templates/charts/dual_axis_line_chart.svg` | "Pick when 2 metrics with different units/scales must be compared over time. Skip if both metrics sha" | 2020-2026 Capex（左軸 $B）vs Enterprise AI Revenue（右軸 $B）剪刀差 |
| P17 | quadrant_text_bullets | `templates/charts/quadrant_text_bullets.svg` | "Pick for any 2×2 framework where each quadrant holds a titled bullet list — SWOT (Strengths/Weakness" | 四大風險象限：資本鴻溝 / 企業 ROI / 客戶集中 / 融資結構 |

**Runners-up considered**:

- `donut_chart` | rejected for P04: KPI cards 更適合 4 個獨立指標並列展示，donut 強調比例切分而非單獨讀取
- `stacked_bar_chart` | rejected for P05: 單一指標（capex 金額）對比，無內部分組結構
- `grouped_bar_chart` | rejected for P07: dumbbell 更適合"兩狀態差值"敘事，grouped bar 適合 YoY 多類別
- `treemap_chart` | rejected for P09: OpenAI 投資人只有 5-6 個獨立份額，donut 中心可顯總額 $122B，treemap 強調層級
- `radar_chart` | rejected for P10: 5 家公司單一指標（估值）排名，radar 適合多維能力
- `hub_inward_arrows` | rejected for P12: sankey 才能表達"金額流量"，hub_inward 只有方向無量值
- `bar_chart` | rejected for P13: pareto 同時顯示個體貢獻 + 累積佔比，bar 只有前者
- `process_flow` | rejected for P14: hub_spoke 表達"一箇中樞 + 多個外圍站點"的 Stargate 拓撲，process_flow 暗示線性

---

## VIII. Image Resource List

| Filename | Dimensions | Ratio | Purpose | Type | Layout pattern | Acquire Via | Status | Reference | text_policy | page_role |
| -------- | --------- | ----- | ------- | ---- | -------------- | ----------- | ------ | --------- | ----------- | --------- |
| cover_atmosphere.png | 1280×720 | 1.78 | 封面氛圍底圖 | Background | #1 full-bleed background with floating title + #29 two-stop scrim | ai | Pending | Abstract nighttime aerial of a vast data-center campus, faint server-rack lights forming a constellation pattern; quiet wide-angle composition with reserved dark sky for title overlay; sense of capital flowing through silent infrastructure | none | hero_page |
| nvidia_circular.png | 1280×720 | 1.78 | Part V Nvidia 閉環章節錨點 | Background | #1 full-bleed background with floating title + #29 two-stop scrim | ai | Pending | Abstract macro shot of a circular wafer-like geometry with subtle red glow at the rim suggesting circulation; central dark void reserved for chapter title; metallic finish but no recognizable logos | none | hero_page |
| bubble_tension.png | 1280×720 | 1.78 | Part VI 泡沫論章節錨點 | Background | #1 full-bleed background with floating title + #29 two-stop scrim | ai | Pending | Abstract atmospheric image of a single iridescent soap-bubble suspended in deep dark space, surface tension catching a faint warning-red highlight; quiet composition with negative space; sense of fragile inflation | none | hero_page |

---

## IX. Content Outline

### Part 0: 開場（封面 + 導語 + 目錄）

#### Slide 01 - 封面

- **Layout**: Full-bleed 氛圍底圖 + 底部 scrim + 左下大字標題
- **Title**: 2026 全球 AI 資本格局
- **Subtitle**: Capital, Compute, and the Closed Loop
- **Info**: 2026 年 5 月 · 行業洞察 · 資料截至 2026-05-15

#### Slide 02 - 編輯導語

- **Layout**: 單欄居中 + 大引號 + 三行核心敘述
- **Title**: 編輯導語 | Editor's Note
- **Content**:
  - 單季 2970 億美元 VC，AI 拿走 81%
  - 四筆交易 1880 億美元，65% 流向四家公司
  - 資本與商業 ROI 的鴻溝，已超 2001 電信泡沫期

#### Slide 03 - 目錄

- **Layout**: 左側六部分羅馬字 + 右側每部分頁碼與一句話標題
- **Title**: 目錄 | Contents
- **Content**:
  - I. 全景 — P04-P05
  - II. 三巨頭 — P06-P09
  - III. 中國陣營 — P10-P11
  - IV. 二線梯隊 — P12
  - V. 基建與閉環 — P13-P15
  - VI. 泡沫與判斷 — P16-P18

### Part I: 全景

#### Slide 04 - Q1 風投全景

- **Layout**: 四象限 KPI cards + 頂部小字章節標記
- **Title**: 2026 Q1 全球風投：$297B 創紀錄，AI 拿走 81%
- **Visualization**: kpi_cards
- **Content**:
  - $297B — 單季 VC 總額（Crunchbase）
  - 81% — AI 佔比（約 $242B）
  - $188B — Top 4 筆大單合計（OpenAI + Anthropic + xAI + Waymo）
  - 65% — 集中度（前 4 單佔全季 VC）

#### Slide 05 - Hyperscaler Capex

- **Layout**: Bar chart 左 7 右 3 + 右側三條關鍵註解
- **Title**: 四家 Hyperscaler 2026 年 Capex：$725B，同比 +77%
- **Visualization**: bar_chart
- **Content**:
  - Amazon $200B / Microsoft $190B / Alphabet $190B / Meta $145B+
  - 60%+ 流向電力 / 冷卻 / 土建，非晶片
  - 資源約束已從"算力"轉向"電力"

### Part II: 三巨頭

#### Slide 06 - 估值前後對比

- **Layout**: Dumbbell chart + 頂部章節標記
- **Title**: 三巨頭 2026 估值躍遷：從年初到 Q2 的雙倍線
- **Visualization**: dumbbell_chart
- **Content**:
  - OpenAI: $300B → $852B（Mar 2026）
  - Anthropic: $61.5B → $380B（Series G）→ $900B（在談）
  - xAI: $50B → $230B（Jan 2026）→ $1.25T 合併 SpaceX

#### Slide 07 - 估值 × 收入 × 投資人

- **Layout**: Bubble chart 全屏 + 角落資料來源
- **Title**: 估值兌現度：收入越高，估值越實
- **Visualization**: bubble_chart
- **Content**:
  - X 軸：ARR（$B），Y 軸：估值（$B），氣泡大小：投資人數量
  - OpenAI: ARR $24B / Val $852B / 7 大投資人
  - Anthropic: ARR $30B+ / Val $380B（在談 $900B）/ 5 大投資人
  - xAI: ARR $5B（est）/ Val $230B / 8+ 投資人

#### Slide 08 - OpenAI 投資人結構

- **Layout**: Donut chart 居左 + 右側投資人列表
- **Title**: OpenAI $122B 這筆錢從哪來
- **Visualization**: donut_chart
- **Content**:
  - Amazon $50B（41%）
  - Nvidia $30B（25%）
  - SoftBank $30B（25%）
  - Microsoft + 其他 $12B（10%）
  - 中心：$122B / $852B 估值

#### Slide 09 - 三巨頭綜合對比

- **Layout**: 三列對照 + 頂部小標 + 底部一行總結
- **Title**: OpenAI vs Anthropic vs xAI：三種成長曲線
- **Content**:
  - OpenAI：消費驅動 + 強 IPO 預期
  - Anthropic：企業驅動 + 估值反超 OpenAI（$900B vs $852B）
  - xAI：合併敘事 + SpaceX 協同

### Part III: 中國陣營

#### Slide 10 - 中國五雄

- **Layout**: Horizontal bar chart + 頂部一行總結
- **Title**: 中國 AI 五雄：DeepSeek 領跑，估值階梯分明
- **Visualization**: horizontal_bar_chart
- **Content**:
  - DeepSeek $50B（國家大基金領投）
  - Zhipu AI（港股市值）$56B
  - MiniMax（港股市值）$37B
  - Moonshot (Kimi) $20B
  - StepFun ~$8B

#### Slide 11 - 中美雙軌

- **Layout**: Comparison table（5 行 × 2 列）+ 頂部小標
- **Title**: 中美 AI 資本：兩條路徑，兩種節奏
- **Visualization**: comparison_table
- **Content**:
  - 私募規模：美國 $30-122B 單輪 vs 中國 $2-4B 單輪
  - IPO 節奏：美國推遲 vs 中國 Q1 已落港
  - 政府角色：美國市場驅動 vs 中國大基金領投
  - 估值峰值：美 $852B vs 中 $56B（市值）
  - 退出方式：私募延後 IPO vs 二級市場優先

### Part IV: 二線梯隊

#### Slide 12 - 二線 $10-50B 陣營

- **Layout**: 四列卡片（每列：公司 logo + 估值 hero number + 一行特點）+ 頂部小標
- **Title**: 二線梯隊：$10-50B 的精英層
- **Content**:
  - SSI $32B（Sutskever，6 倍跳漲）
  - Perplexity $21B（月活 4500 萬）
  - Mistral $13.7B（巴黎資料中心 13800 GPU）
  - Cohere + Aleph Alpha 合併 $20B（跨大西洋主權 AI）

### Part V: 基建與閉環

#### Slide 13 - Nvidia 閉環（章節錨點頁）

- **Layout**: Full-bleed 氛圍底圖（nvidia_circular.png）+ 大字章節標 + 底部 scrim + 三句導語
- **Title**: V. 閉環
- **Subtitle**: 當晶片商同時是大股東
- **Content**:
  - Nvidia 2026 至今股權投資 $40B+
  - OpenAI $30B + xAI + Anthropic + Mistral 全到位
  - 收入 85% 來自 6 個客戶

#### Slide 14 - Nvidia 資本流圖

- **Layout**: Sankey chart 全幅 + 頂部章節標 + 底部 source
- **Title**: 錢怎麼轉：Nvidia 的圓形投資
- **Visualization**: sankey_chart
- **Content**:
  - 左側：Nvidia $40B 投資
  - 中間：OpenAI / xAI / Anthropic / Mistral / CoreWeave
  - 右側：Nvidia 晶片銷售迴流（數百億美元算力承諾）

#### Slide 15 - Nvidia 客戶集中度

- **Layout**: Pareto chart + 右下風險註解
- **Title**: 單點風險：Nvidia 收入 85% 來自 6 個客戶
- **Visualization**: pareto_chart
- **Content**:
  - 前 4 名客戶佔近 60%（MSFT / Meta / Google / Amazon）
  - 6 名累積 85%
  - 任一家砍 capex 都會級聯打擊全鏈

#### Slide 16 - Stargate

- **Layout**: Hub-spoke chart（中心 Stargate logo + 7 個站點輻射）+ 頂部章節標
- **Title**: Stargate：$500B / 10GW / 7 個站點
- **Visualization**: hub_spoke
- **Content**:
  - 中心：Stargate（OpenAI + Oracle + SoftBank）
  - 7 輻射：Abilene TX（執行）/ Shackelford TX / Doña Ana NM / Midwest / Lordstown OH / Milam TX / Saline MI
  - 已規劃近 7GW，未來 3 年投入 $400B

### Part VI: 泡沫與判斷

#### Slide 17 - 泡沫論章節錨點

- **Layout**: Full-bleed 氛圍底圖（bubble_tension.png）+ 章節大字 + 底部 scrim + 三行核心論點
- **Title**: VI. 泡沫
- **Subtitle**: 資本主義 vs 商業現實的剪刀差
- **Content**:
  - Capex 增速比 AI 收入快 46 個百分點
  - 2001 電信泡沫期差距為 32%
  - **當前差距已超 2001 電信泡沫**

#### Slide 18 - Capex vs Revenue 剪刀差

- **Layout**: Dual-axis line chart + 頂部章節標 + 底部 source
- **Title**: 資本與營收的鴻溝：$400B 投入 vs $100B 營收
- **Visualization**: dual_axis_line_chart
- **Content**:
  - 左軸：Hyperscaler Capex（$B）2020-2026
  - 右軸：Enterprise AI Revenue（$B）2020-2026
  - 陰影：兩線之間的 ROI Gap

#### Slide 19 - 四大風險

- **Layout**: 2×2 quadrant + 每象限標題 + 2-3 行 bullet
- **Title**: 四大風險，互相放大
- **Visualization**: quadrant_text_bullets
- **Content**:
  - 左上 Capex/Revenue 鴻溝：差距已超 2001 電信泡沫
  - 右上 企業 ROI：MIT 95% 試點未產生商業價值
  - 左下 客戶集中：Nvidia 85% 來自 6 家
  - 右下 融資結構：經營現金流 → 舉債融資

#### Slide 20 - 六大判斷與結語

- **Layout**: 單欄 6 行編號列表 + 底部 Sources 致謝
- **Title**: 六大判斷 | Closing
- **Content**:
  - ① 資本集中度是 2026 主旋律
  - ② 算力是真硬通貨
  - ③ 電力 > 晶片
  - ④ 中美雙軌結構
  - ⑤ 真實 ROI 滯後但巨頭未止血
  - ⑥ Anthropic 估值反超 OpenAI

> 注：實際頁數 = 20（封面 1 + 導語 1 + 目錄 1 + 內容 16 + 結語 1）。Strategist 在八項確認中報告 18 頁，含編輯導語後微調至 20 頁以保持單頁一論點的密度。

---

## X. Speaker Notes Requirements

- 檔案命名：與 SVG 同名（`01_cover.svg` → `notes/01_cover.md`）
- 單頁 100-150 字，編輯導語派口吻，不是銷售也不是教學
- 全 deck 總時長目標：15-20 分鐘

---

## XI. Technical Constraints Reminder

### SVG Generation Must Follow:

1. viewBox: `0 0 1280 720`
2. Background 用 `<rect>`
3. Text wrap 用 `<tspan>`
4. 透明度用 `fill-opacity` / `stroke-opacity`
5. FORBIDDEN: `mask`, `<style>`, `class`, `foreignObject`, `textPath`, `animate*`, `script`, `<symbol>`+`<use>` 自定義, `<g opacity>`, rgba()
6. HTML named entities 禁用，寫 raw Unicode
7. `marker-start` / `marker-end` 僅 `<marker>` in `<defs>` 且 orient="auto"
8. `clipPath` 僅作用於 `<image>`，且 single shape child

### PPT Compatibility:

- Inline styles only
- 每個元素單獨設 opacity
- 字型棧每條以預裝字型收尾
