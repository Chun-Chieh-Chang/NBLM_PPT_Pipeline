# sugar_rush_memphis - Design Spec

> Human-readable design narrative. Machine-readable execution contract: `spec_lock.md`. Executor re-reads `spec_lock.md` before every SVG page. On divergence, `spec_lock.md` wins.

## I. Project Information

| Item | Value |
| ---- | ----- |
| **Project Name** | sugar_rush_memphis |
| **Canvas Format** | PPT 16:9 (1280×720) |
| **Page Count** | 14 |
| **Design Style** | A) General Versatile + Memphis / Pop |
| **Target Audience** | 音樂節觀眾（18-35）+ 品牌贊助方 + 媒體 |
| **Use Case** | 虛構音樂節年度手冊（翻閱 + 媒體投放） |
| **Created Date** | 2026-05-17 |

---

## II. Canvas Specification

| Property | Value |
| -------- | ----- |
| **Format** | PPT 16:9 |
| **Dimensions** | 1280×720 |
| **viewBox** | `0 0 1280 720` |
| **Margins** | 左右 60px / 上下 50px |
| **Content Area** | 1160×620（安全區） |

---

## III. Visual Theme

### Theme Style

- **Style**: A) General Versatile + Memphis / Pop
- **Theme**: Light theme（奶油底）
- **Tone**: 張揚、糖果感、80s 回潮、撞色狂歡

### Color Scheme

| Role | HEX | Purpose |
| ---- | --- | ------- |
| **Background** | `#FFF8EE` | 奶油白頁面底（55%） |
| **Secondary bg** | `#FFE9C7` | 淺奶油卡片底（特定卡片） |
| **Primary** | `#FF3DA5` | 泡泡糖粉 — 標題 / 重音色塊 |
| **Accent** | `#00B8D9` | 電光藍 — 次級強調 / 連結 |
| **Secondary accent** | `#FFD93D` | 鮮黃 — 高亮 / 數字 |
| **Tertiary accent** | `#00C896` | 薄荷綠 — 章節分色 |
| **Quaternary accent** | `#FF6B4A` | 珊瑚紅 — 裝飾碎片 |
| **Body text** | `#1A1A2E` | 墨黑 — 正文 |
| **Secondary text** | `#5C5C7A` | 灰紫 — 註釋 |
| **Border/divider** | `#1A1A2E` | 墨黑粗描邊（2-4px） |
| **Success** | `#00C896` | 複用薄荷綠 |
| **Warning** | `#FF6B4A` | 複用珊瑚紅 |

> 撞色合計佔比 ≤ 40%；每頁正面只用 2-3 個撞色，不全堆。文字對比度 #1A1A2E on #FFF8EE = 15.5:1（遠超 4.5:1）。

### AI Image Strategy

- **Image Rendering**: `flat`
- **Image Palette**: `vivid-launch`

> 鎖全 deck — 每張 AI 圖共享 flat 渲染 + vivid-launch 配色行為。Image_Generator 自動注入。

### Gradient Scheme

```xml
<!-- 章節扉頁 scrim 漸變 -->
<linearGradient id="heroScrim" x1="0%" y1="100%" x2="0%" y2="0%">
  <stop offset="0%" stop-color="#1A1A2E" stop-opacity="0.55"/>
  <stop offset="60%" stop-color="#1A1A2E" stop-opacity="0"/>
</linearGradient>

<!-- 收尾頁融入背景 -->
<linearGradient id="fadeToBg" x1="0%" y1="0%" x2="0%" y2="100%">
  <stop offset="0%" stop-color="#FFF8EE" stop-opacity="0"/>
  <stop offset="100%" stop-color="#FFF8EE" stop-opacity="0.95"/>
</linearGradient>
```

---

## IV. Typography System

### Font Plan

**Typography direction**: Display × Neutral 強對比 — 標題用 Impact 製造海報張力，正文用 Arial / 微軟雅黑保證可讀。

| Role | Chinese | English | Fallback tail |
| ---- | ------- | ------- | ------------- |
| **Title** | `"Microsoft YaHei"` | `Impact, "Arial Black"` | `sans-serif` |
| **Body** | `"Microsoft YaHei", "PingFang SC"` | `Arial` | `sans-serif` |
| **Emphasis** | `"Microsoft YaHei"` | `Impact` | `sans-serif` |
| **Code** | — | `Consolas, "Courier New"` | `monospace` |

**Per-role font stacks**:

- Title: `Impact, "Arial Black", "Microsoft YaHei", sans-serif`
- Body: `Arial, "Microsoft YaHei", "PingFang SC", sans-serif`
- Emphasis: `Impact, "Microsoft YaHei", sans-serif`
- Code: `Consolas, "Courier New", monospace`

> Title/Emphasis Latin-led（Impact 優先）→ 英文承擔海報張力；CJK 回落到 Microsoft YaHei。Body 改為 Arial-led 以保證 Latin 字元現代感，正文中文仍走 YaHei。

### Font Size Hierarchy

**Baseline**: Body font size = **20px**（中等密度，海報感）

| Purpose | Ratio to body | Px | Weight |
| ------- | ------------- | ---- | ------ |
| Cover hero headline | 4-5x | 80-100px | Black |
| Chapter opener | 2.8-3.6x | 56-72px | Black |
| Page title | 1.8-2.2x | 36-44px | Black |
| Hero number | 4-6x | 80-120px | Black |
| Subtitle | 1.4-1.6x | 28-32px | Bold |
| **Body content** | **1x** | **20px** | Regular |
| Annotation / caption | 0.7-0.85x | 14-17px | Regular |
| Page number / footnote | 0.55-0.65x | 11-13px | Regular |

---

## V. Layout Principles

### Page Structure

- **Header area**: 頂部 50-80px — 章節標識 / 頁碼 / 裝飾碎片
- **Content area**: 中部 540-600px — 主要內容
- **Footer area**: 底部 30-50px — 頁尾 / Logo / 頁碼

### Layout Pattern Library

| Pattern | Suitable Scenarios |
| ------- | ----------------- |
| **Single column centered** | 封面、章節扉頁、收尾 |
| **Asymmetric split (3:7 / 2:8)** | 內容主頁（左標題 + 右圖卡） |
| **Top-bottom split** | 票務頁（上對比 + 下贊助） |
| **Three/four column cards** | KPI / 風格陣營 / 票檔 |
| **Matrix grid (2×2)** | 風格陣營四分類 |
| **Center-radiating** | 5 舞臺 hub_spoke |
| **Full-bleed + floating text** | 6 個章節扉頁與封面 |
| **Figure-text overlap** | 頭牌藝人頁（粗描邊塊疊在人像上） |
| **Z-pattern / waterfall** | 時間軸日程（蛇形） |

### Memphis 裝飾碎片（每頁可疊加 1-3 個）

- 圓點陣 (3-5 個 #FF3DA5 圓點排成不規則排列)
- 波浪線 (3-5 個起伏的 #00B8D9 波浪)
- Z 字閃電 (#FFD93D / #FF6B4A 幾何 Z 字)
- 三角塊 (45° 旋轉的實心三角)
- 棋盤條紋 (黑白小方塊組成的邊角條帶)
- 粗黑描邊 (2-4px 墨黑邊框，所有塊都加)

### Spacing Specification

**Universal**:

| Element | Range | Project Value |
| ------- | ----- | ------------- |
| Safe margin from canvas edge | 40-60px | 60px |
| Content block gap | 24-40px | 32px |
| Icon-text gap | 8-16px | 12px |

**Card-based**:

| Element | Range | Project Value |
| ------- | ----- | ------------- |
| Card gap | 20-32px | 24px |
| Card padding | 20-32px | 24px |
| Card border radius | 8-16px | 12px |
| Card border (Memphis 必備) | 2-4px | 3px solid #1A1A2E |

**Non-card / breathing pages**:

- Line-height: 1.4-1.5× body font size
- Full-bleed text placement: 留焦點區域，文字側加 scrim

---

## VI. Icon Usage Specification

### Source

- **Library**: `chunk-filled`（粗實、幾何、與孟菲斯硬邊性格契合）
- **Usage**: SVG `<use data-icon="chunk-filled/<name>" .../>` 佔位符

### Recommended Icon List

| Purpose | Icon | Page |
| ------- | ---- | ---- |
| 天數 | `chunk-filled/calendar` | P03 |
| 舞臺 / 音樂 | `chunk-filled/music` | P03, P09 |
| 藝人 | `chunk-filled/microphone` | P03, P05 |
| 觀眾 | `chunk-filled/users` | P03 |
| 時間 | `chunk-filled/clock` | P10 |
| 閃電 / 能量 | `chunk-filled/bolt` | P04, P07 |
| 心 / 愛 | `chunk-filled/heart` | P04, P14 |
| 星 / 頭牌 | `chunk-filled/star` | P06 |
| 場地 / 定位 | `chunk-filled/map-pin` | P09 |
| 太陽 / 夏日 | `chunk-filled/sun` | P02, P14 |
| 閃爍裝飾 | `chunk-filled/sparkles` | 全 deck 裝飾 |
| 耳機 / 電子 | `chunk-filled/headphones` | P07 |
| 周邊市集 | `chunk-filled/shopping-bag` | P12 |
| 遊戲 / 互動 | `chunk-filled/game-controller` | P12 |
| 票務 | `chunk-filled/ticket` | P13 |
| 贊助 / 禮物 | `chunk-filled/gift` | P13 |
| 流程箭頭 | `chunk-filled/arrow-right` | P10 |

---

## VII. Visualization Reference List

Catalog read: 71 templates

| Page | Template | Path | Summary-quote (verbatim) | Usage |
| ---- | -------- | ---- | ------------------------ | ----- |
| P03 | kpi_cards | `templates/charts/kpi_cards.svg` | "Pick for 4-8 standalone numeric metrics shown as overview cards (2x2 or 1x4) — exec summary opener, dashboard headline, quarterly recap, res..." | 4 個核心數字：7天 / 5舞臺 / 80組藝人 / 50000觀眾 |
| P04 | vertical_pillars | `templates/charts/vertical_pillars.svg` | "Pick for 1×3 / 1×4 / 1×5 vertical column layout where each pillar = one independent category with title + bullets — PEST (Political/Economic..." | 三大理念：FREE / FUN / FOREVER YOUNG |
| P06 | icon_grid | `templates/charts/icon_grid.svg` | "Pick for 4-9 parallel features/capabilities/services as icon cards — feature grid, service lineup, benefits matrix, brand values, product hi..." | 4 組頭牌藝人卡片 |
| P07 | quadrant_text_bullets | `templates/charts/quadrant_text_bullets.svg` | "Pick for any 2×2 framework where each quadrant holds a titled bullet list — SWOT (Strengths/Weaknesses/Opportunities/Threats, internal-exter..." | 4 風格陣營：搖滾 / 電子 / 民謠 / 嘻哈 |
| P09 | hub_spoke | `templates/charts/hub_spoke.svg` | "Pick for 1 core capability + 4-8 surrounding capabilities (platform/ecosystem); each spoke = title or title + 1-2 line description. Skip if..." | 中央主舞臺 + 4 個分舞臺輻射 |
| P10 | timeline | `templates/charts/timeline.svg` | "Pick for 3-8 milestone events on a horizontal time axis (no duration). Skip for tasks with start/end ranges (use gantt_chart) or vertical la..." | 7 天音樂節日程 |
| P12 | comparison_columns | `templates/charts/comparison_columns.svg` | "Pick for 2-4 pricing/service tier cards in side-by-side columns (marketing layout). Skip for dense feature comparison (use comparison_table)..." | 周邊市集 vs 互動裝置（兩欄對照） |
| P13 | comparison_columns | `templates/charts/comparison_columns.svg` | "Pick for 2-4 pricing/service tier cards in side-by-side columns (marketing layout). Skip for dense feature comparison (use comparison_table)..." | 票務 EARLY / REGULAR / VIP 三檔 |

**Runners-up considered**:

- `team_roster` | rejected for P06: 專案用插畫化頭像而非真人員工照，且需要嵌入"專輯代表作"等非身份欄位；icon_grid 更自由
- `numbered_steps` | rejected for P10: 7 天日程是固定日期里程碑而非"如何做"步驟，timeline 才匹配時間軸語義
- `comparison_table` | rejected for P13: 票檔只有 4-5 行屬性，列式營銷卡片更孟菲斯波普；表格密度過高反而壓住視覺

---

## VIII. Image Resource List

| Filename | Dimensions | Ratio | Purpose | Type | Layout pattern | Acquire Via | Status | Reference | text_policy | page_role |
| -------- | --------- | ----- | ------- | ---- | -------------- | ----------- | ------ | --------- | ----------- | --------- |
| cover_bg.png | 1280×720 | 1.78 | P01 封面主視覺 | Illustration | #1 full-bleed background with floating title + #29 two-stop scrim | ai | Pending | 夏日狂歡主視覺：糖果色霓虹燈牌「SUGAR RUSH」橫向居中懸浮於熱帶叢林夜空，左下角圓點群+右上角波浪閃電裝飾碎片，左側留出大面積冷色暗區供副標題疊加，鳥瞰人群剪影沿底部成弧線 | embedded | hero_page |
| ch1_what.png | 1280×720 | 1.78 | P02 章節1 WHAT 扉頁 | Illustration | #12 faded image as backdrop with oversized overlay text + #27 linear gradient mask | ai | Pending | 夏日沙灘派對俯視全景：撞色傘群+人群塗鴉風輪廓，畫面中央保留 50% 留白讓標題壓上去，右下角棋盤條紋邊角裝飾 | none | hero_page |
| ch2_who.png | 1280×720 | 1.78 | P05 章節2 WHO 扉頁 | Illustration | #1 full-bleed background with floating title + #38 background image + annotation cards with bezier leader lines | ai | Pending | 五位風格化音樂人剪影並排站在霓虹聚光燈下的舞臺，手持麥克風/吉他/合成器，背景為粉/藍/黃撞色光柱，畫面留有空氣感不擁擠 | none | hero_page |
| headliners.png | 1200×500 | 2.40 | P06 頭牌藝人四聯畫 | Illustration | #26 triptych baked into a single wide image + #21 rounded rectangle crop | ai | Pending | 四聯橫幅插畫：4 位風格化虛構音樂人正面半身像並排，左到右為電吉他女主唱（粉發）/ 電子合成器男 DJ（金色墨鏡）/ 民謠女吉他手（薄荷綠襯衫）/ 嘻哈男 rapper（鮮黃連帽衫），每位人物背後是與其音樂風格匹配的撞色塊背景，統一粗黑描邊 | none | local |
| ch3_where.png | 1280×720 | 1.78 | P08 章節3 WHERE & WHEN 扉頁 | Illustration | #41 background image + measurement lines and module tags (engineering overlay) + #29 two-stop scrim | ai | Pending | 鳥瞰視角的虛構音樂節場地全景：椰林環抱、中央大舞臺與四個衛星舞臺呈放射狀分佈、彩色帳篷與霓虹路燈點綴、人流以柔和粉色向量化暗示，畫面留出頂部三分之一空區供標題 | none | hero_page |
| ch4_vibes.png | 1280×720 | 1.78 | P11 章節4 VIBES 扉頁 | Illustration | #1 full-bleed background with floating title + #28 radial gradient vignette | ai | Pending | 夜場氛圍全景：熒光手環與彩色煙霧在人群上方騰起，遠處舞臺 LED 螢幕顯示巨型抽象波浪圖案，前景設定一個跳躍中的人物剪影做視覺焦點，左上保留暗區供標題 | none | hero_page |
| market.png | 600×400 | 1.50 | P12 周邊市集場景 | Illustration | #19 image floating in whitespace with thin frame and caption + #21 rounded rectangle crop | ai | Pending | 戶外周邊市集攤位：撞色雨篷下陳列著印有 SUGAR RUSH 字樣的 T 恤、帆布袋、貼紙、霓虹光劍，攤主向顧客遞商品的瞬間，畫面充滿波普海報感 | none | local |
| installation.png | 600×400 | 1.50 | P12 互動裝置場景 | Illustration | #19 image floating in whitespace with thin frame and caption + #21 rounded rectangle crop | ai | Pending | 沉浸式互動藝術裝置：巨型充氣幾何雕塑（粉色圓球+藍色三角+黃色波浪）矗立在草坪，兩三個觀眾在裝置間穿梭、自拍、躍起，藍天白雲作背景 | none | local |
| closing.png | 1280×720 | 1.78 | P14 收尾頁 | Illustration | #1 full-bleed background with floating title + #66 image fading into the solid background | ai | Pending | 夕陽下空蕩的舞臺後景：散落的彩色紙屑、被風揚起的氣球、遠處地平線的紫粉色霞光，畫面底部 1/3 用漸變融入奶油色背景，整體悠長懷念感 | none | hero_page |

> 9 張 AI 圖全 deck 共享 `flat × vivid-launch`（h.5 鎖定）。其中 6 張 hero_page（P01/P02/P05/P08/P11/P14）+ 3 張 local（P06 / P12 ×2）。#38 image-as-canvas + native overlay 覆蓋在 P05；#41 用於 P08，滿足"≥4 image-bearing pages 至少 1 個 #38–#46"的硬性要求。

---

## IX. Content Outline

### Part 1: WHAT — 是什麼

#### Slide 01 - Cover

- **Layout**: Full-bleed + floating title（hero_page）
- **Title**: `SUGAR RUSH`
- **Subtitle**: 2026 夏日音樂節 · 年度手冊
- **Info**: 7.18 – 7.24 · 椰島大草原 · 讓甜炸的夏天到來

#### Slide 02 - Chapter 1: WHAT IS SUGAR RUSH

- **Layout**: 章節扉頁 — Faded image backdrop + 巨字標題
- **Title**: `WHAT.`
- **Subtitle**: 當全世界都在變熱，我們決定，讓它變甜。

#### Slide 03 - 關鍵數字

- **Layout**: Four-column cards（2×2 or 1×4）
- **Title**: BY THE NUMBERS
- **Visualization**: kpi_cards
- **Content**:
  - `7` DAYS · 7 天連續狂歡（icon: calendar）
  - `5` STAGES · 5 個主題舞臺（icon: music）
  - `80` ARTISTS · 80 組藝人陣容（icon: microphone）
  - `50K` FANS · 50000 名觀眾預期（icon: users）

#### Slide 04 - 三大理念

- **Layout**: Three-column vertical pillars
- **Title**: WHAT WE STAND FOR
- **Visualization**: vertical_pillars
- **Content**:
  - **FREE**（icon: bolt）— 不設鄙視鏈，所有風格都是好風格
  - **FUN**（icon: sparkles）— 玩到極致，留下最甜回憶
  - **FOREVER YOUNG**（icon: heart）— 18 歲還是 80 歲，舞池裡沒有年紀

### Part 2: WHO — 誰來玩

#### Slide 05 - Chapter 2: WHO

- **Layout**: Full-bleed + 標題壓音樂人剪影 + annotation cards
- **Title**: `WHO.`
- **Subtitle**: 80 組藝人，5 個風格陣營，1 張你忘不掉的臉。

#### Slide 06 - 頭牌藝人

- **Layout**: 2×2 grid，4 張頭像 + 名字 + 風格 + 代表作
- **Title**: THE HEADLINERS
- **Visualization**: icon_grid（每格 = 頭像 + 文字）
- **Content**:
  - **CHERRY BOMB**（粉發女主唱 · 搖滾 · 代表作 "Pink Static"）
  - **NEON CLOUD**（金色墨鏡 DJ · 電子 · 代表作 "3AM Mirror"）
  - **MINT FOLK**（薄荷綠襯衫 · 民謠 · 代表作 "Slow Lemon"）
  - **YELLOW HUSTLE**（鮮黃連帽 · 嘻哈 · 代表作 "Sugar High"）

#### Slide 07 - 四大風格陣營

- **Layout**: 2×2 quadrant matrix
- **Title**: FOUR FLAVORS, ONE FESTIVAL
- **Visualization**: quadrant_text_bullets
- **Content**:
  - 搖滾（icon: bolt）— 噪音、燃、釋放 · 25 組藝人
  - 電子（icon: headphones）— 律動、深夜、迷幻 · 30 組藝人
  - 民謠（icon: heart）— 故事、慢、溫度 · 15 組藝人
  - 嘻哈（icon: music）— 街頭、節拍、態度 · 10 組藝人

### Part 3: WHERE & WHEN — 何時何地

#### Slide 08 - Chapter 3: WHERE & WHEN

- **Layout**: Full-bleed 鳥瞰圖 + 模組標籤 + scrim
- **Title**: `WHERE.`
- **Subtitle**: 椰島大草原 · 一座為夏天造的城市。

#### Slide 09 - 5 個主題舞臺

- **Layout**: Hub-spoke center-radiating
- **Title**: 5 STAGES, ONE WORLD
- **Visualization**: hub_spoke
- **Content**:
  - **中央 · SUGAR DOME**（主舞臺，最大容量 30000）
  - **粉 · CHERRY STAGE**（搖滾，5000）
  - **藍 · NEON GRID**（電子，5000）
  - **綠 · MINT GROVE**（民謠，3000）
  - **黃 · YELLOW BLOCK**（嘻哈，7000）

#### Slide 10 - 7 天日程

- **Layout**: Horizontal timeline
- **Title**: SEVEN DAYS OF SUGAR
- **Visualization**: timeline
- **Content**:
  - Day 1 (7.18) · OPENING · 開幕之夜
  - Day 2 (7.19) · ROCK DAY
  - Day 3 (7.20) · ELECTRO NIGHT
  - Day 4 (7.21) · FOLK AFTERNOON
  - Day 5 (7.22) · HIPHOP MIDNIGHT
  - Day 6 (7.23) · CROSSOVER · 跨界之夜
  - Day 7 (7.24) · CLOSING · 閉幕大狂歡

### Part 4: VIBES — 玩什麼

#### Slide 11 - Chapter 4: VIBES

- **Layout**: Full-bleed + radial vignette
- **Title**: `VIBES.`
- **Subtitle**: 音樂之外，還有十種甜的方式。

#### Slide 12 - 周邊市集 + 互動裝置

- **Layout**: Two-column comparison
- **Title**: BEYOND THE MUSIC
- **Visualization**: comparison_columns（左：MARKET / 右：ART INSTALL）
- **Content**:
  - **左 · MARKET**（icon: shopping-bag）— 50+ 攤位、限定周邊、手作市集、本地小吃
  - **右 · ART INSTALL**（icon: game-controller）— 10 件巨型裝置、AR 互動、彩繪工坊、夜光塗鴉牆

#### Slide 13 - 票務 + 贊助

- **Layout**: Top three-column tickets + bottom sponsor strip
- **Title**: GET YOUR TICKET
- **Visualization**: comparison_columns
- **Content**:
  - **EARLY BIRD** · ¥499（限 5000 張 · 已售罄字樣）
  - **REGULAR** · ¥799（含 1 杯指定飲品）
  - **VIP 7-DAY PASS** · ¥1999（含全程通票 + VIP 專區 + 會面機會）
  - 底部 sponsor 行：5-7 個虛構贊助 logo（佔位文字 + icon 裝飾）

#### Slide 14 - Closing

- **Layout**: Full-bleed + fade to background
- **Title**: `SEE YOU IN SUMMER.`
- **Subtitle**: SUGAR RUSH 2026 · 7.18 – 7.24
- **Info**: Get tickets at sugarrush.fest

---

## X. Speaker Notes Requirements

- **Total duration**: ~15 分鐘（演示性朗讀 · 1 分鐘/頁）
- **Notes style**: 對話式 + 略帶營銷感 — 像一個 host 在介紹音樂節
- **Presentation purpose**: 激發興趣 + 傳達品牌調性 + 引導購票
- **File naming**: 對齊 SVG `01_cover.svg → notes/01_cover.md`

---

## XI. Technical Constraints Reminder

### SVG Generation Must Follow:

1. viewBox: `0 0 1280 720`
2. Background uses `<rect>` elements（#FFF8EE 奶油底）
3. Text wrapping uses `<tspan>`（`<foreignObject>` FORBIDDEN）
4. Transparency uses `fill-opacity` / `stroke-opacity`；`rgba()` FORBIDDEN
5. FORBIDDEN: `mask`, `<style>`, `class`, `foreignObject`, `textPath`, `animate*`, `script`
6. 文字字元直接寫 Unicode（`—` `→` `·` 等），HTML 命名實體 FORBIDDEN；`&` 在文字裡必須 `&amp;`
7. `clipPath` 只用於 `<image>`（圓 / 圓角矩形 / 多邊形），不用於 shape / group / text
8. Memphis 粗描邊：所有幾何塊加 `stroke="#1A1A2E" stroke-width="2-4"`

### PPT Compatibility Rules:

- `<g opacity="...">` FORBIDDEN — 設在子元素上
- Image 透明走 overlay 蒙層
- 僅 inline 樣式；`@font-face` FORBIDDEN
- Memphis 裝飾碎片用基礎 SVG 圖元（circle / rect / path / polygon），不用 `<pattern>`+`<use>`
