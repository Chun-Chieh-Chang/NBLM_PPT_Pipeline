# swiss_grid_systems — Design Spec

> Human-readable design narrative for a Swiss International Typographic Style lecture deck. Machine-readable contract: `spec_lock.md`.

## I. Project Information

| Item | Value |
| ---- | ----- |
| **Project Name** | swiss_grid_systems |
| **Canvas Format** | PPT 16:9 (1280×720) |
| **Page Count** | 14 |
| **Design Style** | A) General Versatile + Swiss International Typographic Style / minimalist grid / Müller-Brockmann hommage |
| **Target Audience** | 設計師 / 設計學生 / 文化機構活動觀眾 |
| **Use Case** | 約 25 分鐘設計史小型 lecture |
| **Created Date** | 2026-05-17 |

---

## II. Canvas Specification

| Property | Value |
| -------- | ----- |
| **Format** | PPT 16:9 |
| **Dimensions** | 1280×720 |
| **viewBox** | `0 0 1280 720` |
| **Margins** | left/right 64px, top/bottom 56px（4×16 模數） |
| **Content Area** | 1152×608（嚴格 4 列網格：列寬 264px，列間距 32px） |

---

## III. Visual Theme

### Theme Style

- **Style**: Swiss International Typographic Style，純白紙面 + 黑色字型 + 硃紅點睛
- **Theme**: Light theme
- **Tone**: 剋制、理性、可讀、版面衝擊；網格是骨架，留白是語言

### Color Scheme

| Role | HEX | Purpose |
| ---- | --- | ------- |
| **Background** | `#FFFFFF` | 紙白底，留白主體 |
| **Secondary bg** | `#F4F4F4` | 極淡淺灰，僅用於 P10/P11 的圖樣區分塊 |
| **Primary** | `#1A1A1A` | 文字、主幾何、海報黑 |
| **Accent** | `#D9251D` | 瑞士硃紅（點睛 / 紅圓 / 標尺） |
| **Secondary accent** | `#1A4FA0` | 印刷克萊因藍（備用，僅章節區分） |
| **Body text** | `#1A1A1A` | 主體文字 |
| **Secondary text** | `#666666` | 註釋、副標、年份 |
| **Tertiary text** | `#999999` | 頁碼、footer |
| **Border/divider** | `#E8E8E8` | 極淡網格線 / 分隔 |
| **Success** | `#1A4FA0` | （備用，本 deck 不需要狀態色，使用藍替代以避免色彩汙染） |
| **Warning** | `#D9251D` | （備用，與 Accent 共用） |

> 60-30-10 嚴格執行：白 (≥60%) + 黑 (~30%) + 紅 (≤10%)。藍僅作章節/類別區分備用，全文最多出現 1-2 次。

### AI Image Strategy

- **Image Rendering**: `minimalist-swiss`
- **Image Palette**: `mono-ink`

> 鎖定一次，三張 AI 圖全部沿用：紙白 60-70% + 近黑 25-30% + 硃紅 <10%。

### Gradient Scheme

不使用漸變。瑞士極簡風格的核心之一是拒絕漸變和陰影；所有色彩都是純色塊。

---

## IV. Typography System

**Typography direction**: 單一家族（Arial 系，Helvetica 的 Windows 等價）內部以 weight + size 做層級。瑞士國際主義的核心字型語法。

| Role | Chinese | English | Fallback tail |
| ---- | ------- | ------- | ------------- |
| **Title** | `"Microsoft YaHei"` | `"Arial Black"` | `sans-serif` |
| **Body** | `"Microsoft YaHei"` | `Arial` | `sans-serif` |
| **Emphasis** | `"Microsoft YaHei"` | `Arial`（weight 700） | `sans-serif` |
| **Code** | — | `Consolas, "Courier New"` | `monospace` |

**Per-role font stacks**:

- Title: `"Arial Black", "Microsoft YaHei", sans-serif`
- Body: `Arial, "Microsoft YaHei", sans-serif`
- Emphasis: `Arial, "Microsoft YaHei", sans-serif`（with `font-weight="700"`）
- Code: `Consolas, "Courier New", monospace`

### Font Size Hierarchy

**Baseline**: Body = **18px**（lecture 資訊密度中等偏緊湊，瑞士本色"密而清"）

| Purpose | Ratio to body | Example @ body=18 | Weight |
| ------- | ------------- | ----------------- | ------ |
| Cover title (hero headline) | 2.5-5x | 60-90px | Bold/Heavy |
| Chapter / section opener | 2-2.5x | 36-45px | Bold |
| Page title | 1.5-2x | 27-36px | Bold |
| Hero number | 1.5-2x | 27-36px | Bold |
| Subtitle | 1.2-1.5x | 22-27px | SemiBold |
| **Body** | **1x** | **18px** | Regular |
| Annotation / caption | 0.7-0.85x | 13-15px | Regular |
| Page number / footnote | 0.5-0.65x | 9-12px | Regular |

---

## V. Layout Principles

### Page Structure

- **Header area**: 頂部 56px 內不放標題（瑞士風常將頁碼/章節號置頂左對齊，標題壓在內容區上沿）
- **Content area**: 64px 邊距內自由排布；多頁採用 4 列 264×608 網格
- **Footer area**: 底部 32px 高，左側"頁碼 / 14"右對齊，中央 / 右側空

### Layout Pattern Library

本 deck 主要採用以下模式：

| Pattern | Used in pages |
| ------- | ------------- |
| **Single column centered** | P14 結語 |
| **Asymmetric split (2:8 / 3:7)** | P02 引言 / P09 模數示意 |
| **Three/four column cards** | P05 人物 / P07 字型 / P11 應用 |
| **Matrix grid (2×2)** | P08 網格四類 |
| **Top-bottom split** | P03 起源 / P06 生平 / P12 數字時代 |
| **Negative-space-driven** | P10 留白即結構 |
| **Full-bleed + floating text** | P01 封面 / P14 結語 |
| **Vertical list** | P04 八條原則 |
| **Icon-grid** | P13 當代品牌 |

### Spacing Specification

**Universal**:

| Element | Range | This deck |
| ------- | ----- | --------- |
| Safe margin | 40-60px | **64px**（4×16 模數） |
| Content block gap | 24-40px | **32px** |
| Icon-text gap | 8-16px | **12px** |

**Cards** (P05 / P07 / P11 / P13):

| Element | Range | This deck |
| ------- | ----- | --------- |
| Card gap | 20-32px | **32px** |
| Card padding | 20-32px | **24px** |
| Card border radius | 8-16px | **0**（瑞士極簡嚴格無圓角） |
| Three-column card width | 360-380px | **361px**（4 列網格中三列合併） |

**Non-card containers** (P02 / P09 / P10 / P14):
- 行高 = 1.5 × body
- 全幅留白驅動，文字塊用大段空白分隔，不依賴分隔線

---

## VI. Icon Usage Specification

### Source

- **Generic library**: `tabler-outline`（stroke-width **1.5**）—— 僅在極少處點綴
- **Brand library**: `simple-icons`（僅 P13 當代品牌牆使用）

> 瑞士極簡的本意是去裝飾，本 deck 主體不依賴圖示承擔資訊；圖示只在 P13 充當品牌識別符號。其他頁面以純字型 + 幾何 + 留白構成。

### Recommended Icon List

| Purpose | Icon Path | Page |
| ------- | --------- | ---- |
| 引文符號（可選） | `tabler-outline/blockquote` | P02 |
| 網格示意 | `tabler-outline/grid-3x3` | P08（小標記） |
| Apple logo | `simple-icons/apple` | P13 |
| Google logo | `simple-icons/google` | P13 |
| Spotify logo | `simple-icons/spotify` | P13 |
| Airbnb logo | `simple-icons/airbnb` | P13 |
| IBM logo | `simple-icons/ibm` | P13 |
| Lufthansa logo | `simple-icons/lufthansa` | P13 |

---

## VII. Visualization Reference List

Catalog read: 71 templates

| Page | Template | Path | Summary-quote (verbatim) | Usage |
| ---- | -------- | ---- | ------------------------- | ----- |
| P03 | timeline | `templates/charts/timeline.svg` | "Pick for 3-8 milestone events on a horizontal time axis (no duration). Skip for tasks with start/end ranges (use gantt_chart) or vertical layout (use roadmap_vertical)." | 瑞士風格的雙源頭年代節點（1896 Akzidenz / 1908 Basel / 1918 Keller / 1936 JMB / 1957 Helvetica） |
| P04 | vertical_list | `templates/charts/vertical_list.svg` | "Pick for 3-6 numbered key points each with a short description — design principles, core tenets, action items, key takeaways, recommendations, executive summary points. Skip for icon-style cards (use icon_grid) or sequential steps (use numbered_steps)." | 八條核心原則（8 項編號清單 + 極短描述） |
| P05 | team_roster | `templates/charts/team_roster.svg` | "Pick for 3-12 leadership/team profile cards (photo + name + title + short bio). Skip for reporting hierarchy (use top_down_tree)." | 關鍵人物群像（8 位代表性設計師卡片，無照片用名字 + 生卒 + 一行貢獻） |
| P06 | timeline | `templates/charts/timeline.svg` | "Pick for 3-8 milestone events on a horizontal time axis (no duration). Skip for tasks with start/end ranges (use gantt_chart) or vertical layout (use roadmap_vertical)." | Müller-Brockmann 生平節點（1914 / 1936 / 1950 / 1957 / 1958 / 1981 / 1996） |
| P07 | comparison_columns | `templates/charts/comparison_columns.svg` | "Pick for 2-4 pricing/service tier cards in side-by-side columns (marketing layout). Skip for dense feature comparison (use comparison_table)." | 三款字型對比（Akzidenz-Grotesk / Helvetica / Univers）卡片化對比 |
| P08 | quadrant_text_bullets | `templates/charts/quadrant_text_bullets.svg` | "Pick for any 2×2 framework where each quadrant holds a titled bullet list — SWOT (Strengths/Weaknesses/Opportunities/Threats, internal-external × helpful-harmful), Ansoff (Existing/New Markets × Existing/New Products), or any named two-axis matrix with text content. Skip for items plotted as points (use matrix_2x2) or bubble-sized portfolios (use quadrant_bubble_scatter)." | 網格四種型別 2×2（手稿 / 列狀 / 模數 / 層級） |
| P11 | icon_grid | `templates/charts/icon_grid.svg` | "Pick for 4-9 parallel features/capabilities/services as icon cards — feature grid, service lineup, benefits matrix, brand values, product highlights. Skip for sequential ordering (use numbered_steps) or hierarchical layers (use pyramid_chart)." | 輸出到企業 VI / 機場標識 / 出版業 / 教育的四象限（這裡用文字而非彩色 icon） |
| P12 | numbered_steps | `templates/charts/numbered_steps.svg` | "Pick for 3-6 horizontal sequential steps with numeric emphasis — how-it-works section, getting-started guide, methodology overview, implementation phases. Skip if steps need connector arrows (use process_flow) or named output artifacts (use pipeline_with_stages)." | 數字時代延續（960 Grid → Bootstrap 12 → CSS Grid → Design Systems 四階段） |
| P13 | icon_grid | `templates/charts/icon_grid.svg` | （same as P11） | 當代品牌身影（六個品牌 logo 網格） |

**Runners-up considered**:

- `numbered_steps` | rejected for P04: 八原則不是 sequential 步驟，更適合 vertical_list 的"編號 + 描述卡"形式，避免暗示順序依賴
- `concentric_circles` | rejected for P10: 同心圓把"留白即結構"具象化反而破壞了 negative-space-driven 的本意；P10 走 no-template 自由留白
- `comparison_table` | rejected for P07: 三款字型只需簡潔三列卡，feature-row 矩陣密度過高，違反"密而清"中"清"的邊界

---

## VIII. Image Resource List

| Filename | Dimensions | Ratio | Purpose | Type | Layout pattern | Acquire Via | Status | Reference | text_policy | page_role |
| -------- | --------- | ----- | ------- | ---- | -------------- | ----------- | ------ | --------- | ----------- | --------- |
| cover_bg.png | 1280×720 | 1.78 | 封面 hero 背景 | Background | #38 image-as-canvas with text-block inset + #1 full-bleed background with floating title | ai | Pending | 一組瑞士網格幾何抽象：橫豎黑色細線網格在純白底上構成 4×3 矩陣，一枚紅圓懸於第三列第二行的網格交點，左下區域留大塊純白用於壓標題；構圖嚴格對稱去中心，幾何 absolutely 主導 | none | hero_page |
| negative_space.png | 1280×720 | 1.78 | P10 留白即結構 hero | Background | #46 image-as-canvas with caption-stripe overlay + #39 image-as-canvas with mega-headline | ai | Pending | 純白畫面中央偏左 1/3 處一枚 80px 直徑紅色實心圓，右下角一根 1px 黑色水平基線長度僅佔畫面 12%；其餘 90% 純白；紅圓與黑線之間形成隱性張力，整畫是"留白"本身的論證 | none | hero_page |
| closing_grid.png | 1280×720 | 1.78 | P14 結語 hero | Background | #38 image-as-canvas with text-block inset + #29 two-stop scrim | ai | Pending | 由細密的黑色網格線（間距 16px）鋪滿整個畫面，網格交點處部分高亮成紅點形成稀疏星圖，構圖嚴格幾何；左下 1/3 留出 8% 不透明白色疊層用於浮文字 | none | hero_page |

> 三張圖全部 `minimalist-swiss × mono-ink`，rendering + palette 由 §III AI Image Strategy 提供；Reference 欄位不重複 style 詞與 HEX。

---

## IX. Content Outline

### Part 1: 引入

#### Slide 01 - 封面

- **Layout**: Full-bleed + floating text（封面 hero）
- **Title**: 網格系統
- **Subtitle**: The Grid as a Way of Seeing
- **Info**: A Lecture on Swiss International Typographic Style · 2026

#### Slide 02 - 引言

- **Layout**: Asymmetric split 3:7（左側大引號 + 右側引文）
- **Title**: （無標題；引文直接是 hero）
- **Content**:
  - "The grid system is an aid, not a guarantee. It permits a number of possible uses and each designer can look for a solution appropriate to his personal style. But one must learn how to use the grid; it is an art that requires practice."
  - — Josef Müller-Brockmann, *Grid Systems in Graphic Design*, 1981

### Part 2: 歷史與原則

#### Slide 03 - 雙源頭

- **Layout**: Top-bottom split（上方時間軸，下方簡短敘述）
- **Title**: 雙源頭 · 1896 → 1957
- **Visualization**: timeline
- **Content**:
  - 1896 Akzidenz-Grotesk 由 Berthold 鑄字行發行
  - 1908 Basel School of Design 改革
  - 1918 Ernst Keller 入蘇黎世應用藝術學院
  - 1936 Müller-Brockmann 開設工作室
  - 1957 Helvetica + Univers 同年問世
  - 一句結論：理性主義不是憑空到來，而是來自半個世紀的字型 + 學校 + 教學

#### Slide 04 - 八條核心原則

- **Layout**: Vertical list（編號 + 一行原則 + 註釋）
- **Title**: 八條核心原則
- **Visualization**: vertical_list
- **Content**:
  1. 客觀先於表達 · Objectivity over expression
  2. 數學網格為骨架 · Mathematical grid
  3. 非對稱構圖 · Asymmetric layout
  4. 無襯線字型 · Sans-serif typography
  5. 齊左不齊右 · Flush-left ragged-right
  6. 客觀攝影 · Objective photography
  7. 留白是結構 · Negative space as structure
  8. 可重複可規模化 · Reproducible at scale

#### Slide 05 - 關鍵人物

- **Layout**: Four-column cards × 2 行（8 人）
- **Title**: 八位塑造者
- **Visualization**: team_roster
- **Content**:
  - Ernst Keller (1891–1968) · 蘇黎世學派奠基
  - Théo Ballmer (1902–1965) · 網格早期實驗者
  - Max Bill (1908–1994) · 包豪斯→烏爾姆
  - Emil Ruder (1914–1970) · 巴塞爾 Typographie
  - Armin Hofmann (1920–2020) · 巴塞爾海報
  - Josef Müller-Brockmann (1914–1996) · 蘇黎世 Grid Systems
  - Max Miedinger (1910–1980) · 1957 設計 Helvetica
  - Adrian Frutiger (1928–2015) · 1957 設計 Univers

#### Slide 06 - Müller-Brockmann

- **Layout**: Top-bottom split（上方時間軸，下方關鍵事件文字）
- **Title**: Josef Müller-Brockmann · 1914–1996
- **Visualization**: timeline
- **Content**:
  - 1914 生於瑞士拉珀斯維爾
  - 1936 蘇黎世獨立工作室
  - 1950 Tonhalle Musica Viva 海報系列起
  - 1957 蘇黎世應用藝術學院教授
  - 1958 創辦 *Neue Grafik* 期刊
  - 1981 出版 *Grid Systems in Graphic Design*
  - 1996 在 Unterengstringen 逝世

### Part 3: 字型與網格

#### Slide 07 - 三款決定性字型

- **Layout**: Three-column cards
- **Title**: 三款決定性字型
- **Visualization**: comparison_columns
- **Content**:
  - **Akzidenz-Grotesk · 1896** · Berthold · 第一款現代意義的商業無襯線 · 瑞士學派早期首選
  - **Helvetica · 1957** · Miedinger + Hoffmann · 拉丁文"瑞士"為名 · 中性客觀可讀至極
  - **Univers · 1957** · Frutiger · 21 字重首次數字座標系統化 · 字型家族工程的開端

#### Slide 08 - 網格四種型別

- **Layout**: Matrix grid 2×2
- **Title**: 網格四種型別
- **Visualization**: quadrant_text_bullets
- **Content**:
  - **手稿網格 Manuscript** · 單欄 · 古老 · 長文唯一選項
  - **列狀網格 Column** · 多欄並列 · 期刊與報紙的語法
  - **模數網格 Modular** · 橫列 × 縱行的方格矩陣 · 海報與目錄利器
  - **層級網格 Hierarchical** · 不規則但內部有邏輯 · 複合排版

#### Slide 09 - 模數網格示意

- **Layout**: Asymmetric split 2:8（左側數值說明，右側 SVG 幾何繪製 8×6 模數圖）
- **Title**: 一切都是可計算的
- **Content**:
  - 列寬 = 264px · 列間距 = 32px · 行高 = body × 1.5
  - 安全邊距 = 64px = 4 × 16px 基礎模數
  - 右側畫出 4×6 模數網格，每格 264×96，紅色線標記一個跨 3 列的影象區

#### Slide 10 - 留白即結構

- **Layout**: Negative-space-driven（90% 純白 + 一枚紅圓 + 一行短句）
- **Title**: 留白即結構
- **Content**:
  - 一句：留白不是剩餘，留白是資訊的載體
  - 一句：The space between is the message
  - hero 圖作為整頁主體（red dot + 極細水平線）

### Part 4: 影響與遺產

#### Slide 11 - 輸出到現代世界

- **Layout**: Four cards
- **Title**: 輸出到現代世界 · 1960s →
- **Visualization**: icon_grid
- **Content**:
  - **企業 VI** · IBM、Knoll、Lufthansa · 把瑞士理性變成"識別系統"產業
  - **機場 / 地鐵標識** · 紐約 Unimark、巴黎機場 Frutiger 字型
  - **出版業** · *Du* 雜誌、*Eye*、*Domus* 的版面語法
  - **設計教育** · 巴塞爾與蘇黎世學派學生散播至全球

#### Slide 12 - 數字時代的延續

- **Layout**: Top-bottom split（上方四階段，下方一行論斷）
- **Title**: 數字時代的延續
- **Visualization**: numbered_steps
- **Content**:
  - 01. 960 Grid System · 2008 · 第一次把網格語法搬上 Web
  - 02. Bootstrap 12 欄 · 2011 · 模數網格民主化
  - 03. CSS Grid · 2017 · 瀏覽器原生網格
  - 04. Design Systems · 2020s · 大企業 VI 在螢幕上的延續

#### Slide 13 - 當代品牌的瑞士血脈

- **Layout**: Six icon cards 3×2
- **Title**: 當代品牌的瑞士血脈
- **Visualization**: icon_grid
- **Content**:
  - Apple · 極簡理性產品語言
  - Google · Material 網格 + 幾何字型
  - Spotify · 雜誌感版面語法
  - Airbnb · 模數 grid + 極簡識別
  - IBM · 1967 起的瑞士血統（JMB 任顧問）
  - Lufthansa · Otl Aicher 1962 VI 至今

#### Slide 14 - 結語

- **Layout**: Full-bleed + floating text（封面回聲）
- **Title**: 網格不是限制
- **Subtitle**: 是自由的語法
- **Info**: The grid is not a constraint. It is a grammar of freedom.

---

## X. Speaker Notes Requirements

- **Filename**: 對應 SVG 檔名（`01_cover.svg` → `notes/01_cover.md`）
- **Tone**: 半正式的 lecture 口吻 + 偶爾現場示例（指代臺上視覺元素）
- **Length per page**: 80-180 字中文（約 30-60 秒語速）
- **Total presentation duration**: 25 分鐘（14 頁平均 ~107 秒/頁）
- **Purpose**: 教學 + 啟發，讓設計師重新理解"網格作為系統而非裝飾"

---

## XI. Technical Constraints Reminder

### SVG Generation Must Follow

1. viewBox: `0 0 1280 720`
2. 背景用 `<rect>`
3. 文字換行用 `<tspan>`（禁 `<foreignObject>`）
4. 透明度用 `fill-opacity` / `stroke-opacity`；禁 `rgba()`
5. 禁 `mask` / `<style>` / `class` / `foreignObject`
6. 禁 `textPath` / `animate*` / `script`
7. 字元用 Unicode（`—` `–` `©` `®` `→` 等），HTML 實體禁
8. `marker-start` / `marker-end` 僅在 `<defs>` 內三角/菱形/圓形且 `orient="auto"`
9. `clipPath` 僅用於 `<image>`，單 shape 子元素

### Project-specific

- 嚴格無圓角（rx = 0）—— 瑞士極簡核心；唯一例外是品牌 logo 來自 simple-icons 內建
- 嚴格無漸變 —— `linearGradient` / `radialGradient` 整 deck 不出現
- 嚴格無陰影 —— `filter` 整 deck 不出現
- 僅四色 —— 白 / 黑 / 硃紅 / 淺灰（border）；藍色每次出現需自檢為何不能用紅替代
