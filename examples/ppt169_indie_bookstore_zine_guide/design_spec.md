# ppt169_indie_bookstore_zine_guide_20260517 - Design Spec

> Human-readable design narrative — rationale, audience, style, color choices, content outline. Read once by downstream roles for context.
>
> Machine-readable execution contract: `spec_lock.md` (color / typography / icon / image short form). Executor re-reads `spec_lock.md` before every SVG page to resist context-compression drift. Keep both in sync; on divergence, `spec_lock.md` wins.

## I. Project Information

| Item | Value |
| ---- | ----- |
| **Project Name** | ppt169_indie_bookstore_zine_guide_20260517 |
| **Canvas Format** | PPT 16:9 (1280×720) |
| **Page Count** | 18 |
| **Design Style** | A) General Versatile + Risograph zine 印刷工藝 / DIY 海報美學 |
| **Target Audience** | 對獨立出版 / zine / 藝術書感興趣的入門讀者；可二次用於獨立書店推廣、設計教學、城市文化分享會 |
| **Use Case** | 線下分享會 / 咖啡館放映 / 設計學院 onboarding / 文化媒體二創素材 |
| **Created Date** | 2026-05-17 |

---

## II. Canvas Specification

| Property | Value |
| -------- | ----- |
| **Format** | PPT 16:9 |
| **Dimensions** | 1280×720 |
| **viewBox** | `0 0 1280 720` |
| **Margins** | 左右 60px / 上下 50px |
| **Content Area** | 1160×620 |

---

## III. Visual Theme

### Theme Style

- **Style**: Risograph zine —— 套色錯位 + 半色調網點 + 限定調色 + zine 手作粗糲
- **Theme**: Light theme (暖米色紙底)
- **Tone**: 印刷工藝感、海報感、DIY 張力、復古獨立出版氣質

### Color Scheme

| Role | HEX | Purpose |
| ---- | --- | ------- |
| **Background (paper)** | `#F5EFE0` | 暖米色仿牛皮紙 / 再生紙感頁面底色 |
| **Secondary bg** | `#EAE2CC` | 卡片 / 節區微差異底色 |
| **Primary (Riso Federal Blue)** | `#1E4DBC` | 主色塊、標題描邊、關鍵圖形 |
| **Accent (Riso Fluorescent Pink)** | `#FF5C8A` | 強對比色、套色錯位的另一層、裝飾 |
| **Secondary accent (Mustard)** | `#E8A02E` | 第三色 <5%，用於焦點強調 |
| **Body text** | `#1A1A1A` | 近黑（貼近 Riso 油墨的不純黑） |
| **Secondary text** | `#5A5A5A` | 註解、頁碼、caption |
| **Tertiary text** | `#8C8275` | 極淡背景文字 |
| **Border/divider** | `#1A1A1A` | 主分隔線一律近黑（zine 印刷感） |

> **Riso 美學硬約束**：套色錯位 1–3px、半色調網點紋理、相同色塊疊加產生第三色錯覺。SVG 上以多個偏移色塊 + opacity + 網點 `<pattern>` 模擬。

### AI Image Strategy

- **Image Rendering**: `screen-print`
- **Image Palette**: `duotone`

> 使用者預先鎖定（繞過三候選呈現）。screen-print × duotone 在矩陣中為 ✓✓ 推薦組合。所有 ai 圖都使用同一 rendering + palette，HEX 從上表實色值注入（Federal Blue + Fluorescent Pink + 偶用 Mustard）。

### Gradient Scheme

> Risograph zine 一般不用漸變（違反扁平套色邏輯）；只在極少數處用 stop-opacity 模擬紙紋暈染。

```xml
<!-- 紙面半色調暈染（輕微，0.05–0.12 opacity） -->
<radialGradient id="paperHalftone" cx="50%" cy="50%" r="60%">
  <stop offset="0%" stop-color="#F5EFE0" stop-opacity="0"/>
  <stop offset="100%" stop-color="#5A5A5A" stop-opacity="0.08"/>
</radialGradient>
```

---

## IV. Typography System

### Font Plan

**Typography direction**: Contrast 方案 —— zine punk DIY 張力，標題用 Impact 海報字型，body 用 YaHei，annotation 用等寬 Consolas 製造"打字機/影印機"感

| Role | Chinese | English | Fallback tail |
| ---- | ------- | ------- | ------------- |
| **Title** | `"Microsoft YaHei"` | `Impact, "Arial Black"` | `sans-serif` |
| **Body** | `"Microsoft YaHei", "PingFang SC"` | `Arial` | `sans-serif` |
| **Emphasis** | `SimHei` | `Impact, "Arial Black"` | `sans-serif` |
| **Code (annotation)** | — | `Consolas, "Courier New"` | `monospace` |

**Per-role font stacks**:

- Title: `Impact, "Arial Black", "Microsoft YaHei", sans-serif`
- Body: `"Microsoft YaHei", "PingFang SC", Arial, sans-serif`
- Emphasis: `Impact, "Arial Black", SimHei, "Microsoft YaHei", sans-serif`
- Code: `Consolas, "Courier New", monospace`

### Font Size Hierarchy

**Baseline**: Body font size = **20px**（zine 資訊密度適中，介於 dense 18 和 relaxed 24 之間）

| Purpose | Ratio to body | Example @ body=20 | Weight |
| ------- | ------------- | ----------------- | ------ |
| Cover title (Impact 大字) | 4-5x | 80-100px | Heavy |
| Chapter / section opener | 2.5-3x | 50-60px | Bold |
| Page title | 1.6-2x | 32-40px | Bold |
| Hero number / 大字強調 | 2.5-4x | 50-80px | Heavy |
| Subtitle | 1.2-1.4x | 24-28px | SemiBold |
| **Body content** | **1x** | **20px** | Regular |
| Annotation / caption | 0.7-0.85x | 14-17px | Regular |
| Page number / footnote | 0.55-0.65x | 11-13px | Regular |

---

## V. Layout Principles

### Page Structure

- **Header area**: 60px 高（頁碼 + 節標識 + 裝飾條）
- **Content area**: 600px 高（主資訊區）
- **Footer area**: 40px 高（頁碼 + footer 裝飾條）

### Layout Pattern Library

> **原則 —— 比例服從資訊權重，不拘泥固定網格。** zine 美學鼓勵打破均勻網格、有意"亂排"、保留留白與高密度的對位。

| Pattern | Suitable Scenarios |
| ------- | ----------------- |
| **Single column centered** | 封面 / 封底 / 大字 outro |
| **Asymmetric split (3:7 / 2:8)** | 章節圖 + 大字標題 / 單 hero + 邊欄 |
| **Top-bottom split** | banner 圖 + 多列內容 |
| **Three/four column cards** | 四浪潮 / 城市並列 / 工具列舉 |
| **Full-bleed + floating text** | hero_page 封面 / Jimbocho / 柏林 |
| **Figure-text overlap** | 大字與圖邊緣交疊（zine 經典手法） |
| **Negative-space-driven** | breathing 頁 —— 單元素 + 大量留白 |
| **Z-pattern waterfall** | 步驟型頁（八頁摺疊 / Risograph 流程） |

### Spacing Specification

**Universal**:

| Element | Recommended Range | Current Project |
| ------- | ---------------- | --------------- |
| Safe margin from canvas edge | 40-60px | **60px 左右 / 50px 上下** |
| Content block gap | 24-40px | **32px** |
| Icon-text gap | 8-16px | **12px** |

**Card-based layouts** (used on P12 表 / P08 內容型別 grid / P10 三城並列 / P13 雙書展卡 / P14-P15 vertical_list):

| Element | Recommended Range | Current Project |
| ------- | ---------------- | --------------- |
| Card gap | 20-32px | **24px** |
| Card padding | 20-32px | **24px** |
| Card border radius | 8-16px | **0px**（Risograph 美學 = 硬邊、無圓角）|
| Three-column card width | 360-380px each | **360px** |

**Non-card containers** (breathing 頁 / hero pages):

- Line-height: 1.5x body (= 30px @ body 20)
- Full-bleed text placement: 大字標題與圖邊緣交疊為常見手法
- 資訊按權重排版，不回算"列寬"

---

## VI. Icon Usage Specification

### Source

- **Built-in icon library**: `templates/icons/chunk-filled/` (粗實心幾何，與 Riso 色塊面感最協調)
- **Library lock**: **chunk-filled**（全 deck 單一庫；混用 forbidden）
- **Usage method**: SVG placeholder `<use data-icon="chunk-filled/icon-name" .../>`

### Recommended Icon List

| Purpose | Icon Path | Page |
| ------- | --------- | ---- |
| zine / 雜誌 / 書 | `chunk-filled/book` | P03, P14 |
| 翻開的書 | `chunk-filled/book-open` | P02 (TOC) |
| 多本書 / 書架 | `chunk-filled/books` | P09, P10, P11 |
| 報刊 | `chunk-filled/newspaper` | P04 |
| 便籤 / 短文 | `chunk-filled/sticky-note` | P08 |
| 印表機 | `chunk-filled/printer` | P05, P06 |
| 複製 / 影印 | `chunk-filled/copy` | P06 |
| 油墨 / 筆刷 | `chunk-filled/brush` | P05 |
| 剪刀（折 zine 工具） | `chunk-filled/scissors` | P07 |
| 鉛筆 / 內容創作 | `chunk-filled/pencil` | P08 |
| 鋼筆 / 寫作 | `chunk-filled/pen-nib` | P08 |
| 工具箱 | `chunk-filled/toolbox` | P07 |
| 地圖 | `chunk-filled/map` | P12 |
| 地圖針 / 定位 | `chunk-filled/map-pin` | P09, P10, P11, P12 |
| 地球 / 全球 | `chunk-filled/globe` | P09 |
| 日曆 / 書展 | `chunk-filled/calendar` | P13 |
| 時鐘 | `chunk-filled/clock` | P13 |
| 心 / 收藏 | `chunk-filled/heart` | P15 |
| 星 / 推薦 | `chunk-filled/star` | P12 |
| 旗幟 / 行動 | `chunk-filled/flag` | P16 |
| 箭頭 right | `chunk-filled/arrow-right` | 多處 |
| 圓形箭頭 | `chunk-filled/circle-arrow-right` | P02, P16 |
| 建築 / 書店 | `chunk-filled/building` | P12 |
| 購物袋 / 買買 | `chunk-filled/shopping-bag` | P14 |
| 資料夾 / 收藏 | `chunk-filled/folders` | P15 |
| 網格 / 庫 | `chunk-filled/grid` | P02 |
| 手 / 自制 | `chunk-filled/hand` | P07, P16 |
| 使用者 / 社群 | `chunk-filled/users` | P04 (Riot grrrl) |

---

## VII. Visualization Reference List

> Catalog read: 71 templates

| Page | Template | Path | Summary-quote (verbatim from `charts_index.json`) | Usage |
| ---- | -------- | ---- | ------------------------------------------------- | ----- |
| P02 | agenda_list | `templates/charts/agenda_list.svg` | "Pick for table of contents, meeting agendas, or presentation roadmap — numbered items + brief description + duration / owner per row. Skip for substantive content lists (use vertical_list) or single-page section dividers (use a cover layout)." | 18 頁 deck 的目錄（5 節 + 簡述 + 頁碼區間） |
| P04 | timeline | `templates/charts/timeline.svg` | "Pick for 3-8 milestone events on a horizontal time axis (no duration). Skip for tasks with start/end ranges (use gantt_chart) or vertical layout (use roadmap_vertical)." | zine 簡史四浪潮（業餘出版 1920s / 科幻 1930s / 朋克 1976 / Riot grrrl 1991 / 當代 2010s）= 5 milestones |
| P05 | vertical_list | `templates/charts/vertical_list.svg` | "Pick for 3-6 numbered key points each with a short description — design principles, core tenets, action items, key takeaways, recommendations, executive summary points. Skip for icon-style cards (use icon_grid) or sequential steps (use numbered_steps)." | Risograph 4 大視覺特徵：限定調色盤 / 套色錯位 / 網點紋理 / 油墨氣味 |
| P06 | numbered_steps | `templates/charts/numbered_steps.svg` | "Pick for 3-6 horizontal sequential steps with numeric emphasis — how-it-works section, getting-started guide, methodology overview, implementation phases. Skip if steps need connector arrows (use process_flow) or named output artifacts (use pipeline_with_stages)." | Risograph 工作流 5 步：數字影象 → 燒蝕母版 → 包裹墨筒 → 滾壓油墨 → 多次過紙 |
| P07 | numbered_steps | `templates/charts/numbered_steps.svg` | "Pick for 3-6 horizontal sequential steps with numeric emphasis — how-it-works section, getting-started guide, methodology overview, implementation phases. Skip if steps need connector arrows (use process_flow) or named output artifacts (use pipeline_with_stages)." | 八頁摺疊法 4 步：摺疊 → 關鍵剪口 → 組裝 → 填內容 |
| P08 | icon_grid | `templates/charts/icon_grid.svg` | "Pick for 4-9 parallel features/capabilities/services as icon cards — feature grid, service lineup, benefits matrix, brand values, product highlights. Skip for sequential ordering (use numbered_steps) or hierarchical layers (use pyramid_chart)." | zine 6 大內容型別：草圖 / 詩 + 宣言 / 食譜插圖 / 私人寫作 / 拼貼 / 漫畫 |
| P10 | vertical_pillars | `templates/charts/vertical_pillars.svg` | "Pick for 1×3 / 1×4 / 1×5 vertical column layout where each pillar = one independent category with title + bullets — PEST (Political/Economic/Social/Technological), four-pillar strategy overview, side-by-side independent categories. Skip for 2×2 quadrant (use quadrant_text_bullets), pricing tiers (use comparison_columns), or 2×2 parallel aspects (use labeled_card)." | 三城三店並列：Shakespeare and Company（巴黎）/ Daunt + Word on the Water（倫敦）/ Strand + Yu and Me（紐約） |
| P12 | basic_table | `templates/charts/basic_table.svg` | "Pick for plain tabular text/number grid, 3-8 columns. Skip if cells need visual bars (use consulting_table) or qualitative scores (use harvey_balls_table)." | 中國大陸 15 家 zine 傾向獨立書店地圖（書店 / 城市 / 特色 / zine 傾向 4 列） |
| P13 | labeled_card | `templates/charts/labeled_card.svg` | "Pick for 3-4 parallel aspects of one subject with per-aspect titles + short body (self-introduction, four-pillar overview, capability quadrant). Skip for plain feature lists (use icon_grid), sequential steps (use numbered_steps), or strategic quadrants (use quadrant_text_bullets / matrix_2x2)." | 雙書展並列卡：abC（2015 創辦，京滬雙城）+ UNFOLD（高攤位費，大客流） |
| P14 | vertical_list | `templates/charts/vertical_list.svg` | "Pick for 3-6 numbered key points each with a short description — design principles, core tenets, action items, key takeaways, recommendations, executive summary points. Skip for icon-style cards (use icon_grid) or sequential steps (use numbered_steps)." | 怎麼逛獨立書店 4 條要點：看選品 / 留 1 小時 / 帶現金 / 拍照先問 |
| P15 | vertical_list | `templates/charts/vertical_list.svg` | "Pick for 3-6 numbered key points each with a short description — design principles, core tenets, action items, key takeaways, recommendations, executive summary points. Skip for icon-style cards (use icon_grid) or sequential steps (use numbered_steps)." | 怎麼收藏 zine 4 條：從興趣切入 / 塑封保護 / 跟蹤作者 IG / 參加 zine fair |
| P16 | numbered_steps | `templates/charts/numbered_steps.svg` | "Pick for 3-6 horizontal sequential steps with numeric emphasis — how-it-works section, getting-started guide, methodology overview, implementation phases. Skip if steps need connector arrows (use process_flow) or named output artifacts (use pipeline_with_stages)." | 第一本 zine 行動清單 4 步：選主題 / 折一張 A4 / 填 8 頁 / 印 10 份送出去 |

**Runners-up considered**:

- `roadmap_vertical` | rejected for P04: timeline 資料是橫向年代軸的"事件 milestone"（無 duration），roadmap_vertical 適用"專案里程碑+狀態"，本頁是文化史軸更貼 timeline
- `agenda_list` | rejected for P02 備選 `vertical_list`: agenda_list 含 duration/owner 列匹配"目錄+頁碼區間"語義；vertical_list 是"原則/要點"型清單，語義不符
- `process_flow` | rejected for P06: process_flow 有連線箭頭適合審批流；Riso 工作流是"工藝步驟"無分叉無審批語義，numbered_steps 更輕
- `icon_grid` | rejected for P08 內容型別本身就是 icon_grid（用作正選）；rejected for P14/P15 因 P14/P15 是"原則要點"非"能力/特性"
- `consulting_table` | rejected for P12: 表格是純文字+定性標籤（★），無 micro bar 資料可視；basic_table 正解

---

## VIII. Image Resource List

> Layout pattern 列內的 `#<id>` 全部 verbatim 引用 `references/image-layout-patterns.md`（Part 1 Primary + Part 2 Modifiers）。Image-as-canvas coverage（#38–#46）由 P07 + P09 承擔。

| Filename | Dimensions | Ratio | Purpose | Type | Layout pattern | Acquire Via | Status | Reference | text_policy | page_role |
| -------- | --------- | ----- | ------- | ---- | -------------- | ----------- | ------ | --------- | ----------- | --------- |
| cover_hero.png | 1280×720 | 1.78 | P01 封面 hero | Background | `#1 Full-bleed background with floating title + #27 Linear gradient mask for text legibility + #29 Two-stop scrim — opaque on text side, transparent on focal side` | ai | Pending | "A risograph print studio scene: a hand-pulled silkscreen 'pull' of a two-color zine sheet rising from a paper stack; ink rollers and color drums visible in the lower edge; left side reserved as calm flat color block for large title overlay; bold silhouette composition" | none | hero_page |
| zine_history_collage.png | 760×420 | 1.81 | P03 裝飾圖：zine 是什麼 | Illustration | `#13 Narrow vertical image strip + giant horizontal title + #21 Rounded rectangle crop` | ai | Pending | "Collage silhouette of stacked zines across eras: a sci-fi pulp magazine corner, a punk fanzine front, a riot grrrl xeroxed page, a modern art-book spine — overlapping at slight angles like a desk pile; the stack is the only motif, off-white paper background visible behind" | none | local |
| risograph_machine.png | 720×900 | 0.80 | P05 Risograph 工藝側欄 | Illustration | `#18 Image as full-height sidebar column + #21 Rounded rectangle crop` | ai | Pending | "Front-three-quarter view of a vintage Risograph duplicator (Riso EZ200 era), boxy industrial silhouette, two color drums visible through a side panel slot, paper tray protruding from front; clean stencil-cut machine outline, no operator, isolated against off-white paper field" | none | local |
| risograph_process_banner.png | 1280×280 | 4.57 | P06 工藝橫幅 | Diagram | `#14 Horizontal banner strip cutting through mid-section + #29 Two-stop scrim` | ai | Pending | "Horizontal silkscreen frieze depicting Risograph workflow: from left to right — a digital file glyph, a stencil master sheet, a wrapped color drum, an inked roller pressing paper, a paper output stack; five stages connected by subtle ink-trail lines; bold stencil silhouettes, no text labels on the image" | none | local |
| zine_folding_hands.png | 1080×720 | 1.50 | P07 八頁摺疊示意 hero | Illustration | `#38 Background image + annotation cards with bezier leader lines + #21 Rounded rectangle crop` | ai | Pending | "Overhead view of two hands folding a single A4 sheet into an 8-page zine; the sheet partially folded mid-crease, scissors and pencil nearby; composition leaves four open negative-space pockets in corners for native SVG annotation cards to overlay; soft top-down vantage" | none | local |
| jimbocho_hero.png | 1280×720 | 1.78 | P09 神保町 hero | Background | `#1 Full-bleed background with floating title + #29 Two-stop scrim + #27 Linear gradient mask for text legibility` | ai | Pending | "Tokyo Jimbocho bookstore street at evening: rows of paper-lantern shop signs glowing, stacked secondhand books spilling onto sidewalk shelves, narrow alley vanishing into perspective; bold silhouette of pedestrian browsing in foreground; cinematic poster framing" | none | hero_page |
| three_cities_triptych.png | 1160×400 | 2.90 | P10 三城三店三聯 | Illustration | `#56 Image triptych + #21 Rounded rectangle crop + #70 Image with thin colored matte frame` | ai | Pending | "Three-panel triptych baked in one image, panels equal width separated by 4px gutters. Left panel: Paris's Shakespeare and Company exterior — narrow green-fronted shop with cobbled foreground. Middle panel: London Word-on-the-Water bookbarge on canal at dusk. Right panel: New York Strand Bookstore corner with the red awning visible. All three panels in matching screen-print silhouette style, unified color treatment for visual continuity" | none | local |
| berlin_bucherbogen.png | 1280×720 | 1.78 | P11 柏林 hero | Background | `#1 Full-bleed background with floating title + #12 Faded image as backdrop with oversized overlay text` | ai | Pending | "Berlin Bücherbogen under S-Bahn arches: arched brick vault interior, light spilling from book-lined walls under the curved ceiling, a single train rumble silhouette implied above; central calm zone reserved for huge overlay title; atmospheric depth via halftone gradation" | none | hero_page |
| zine_fair_scene.png | 720×720 | 1.00 | P13 書展現場氛圍 | Illustration | `#2 Left-third image + right text body + #21 Rounded rectangle crop + #70 Image with thin colored matte frame` | ai | Pending | "Art-book-fair booth aisle scene: rows of low tables stacked with zines and small-press books, a few visitor silhouettes browsing, hand-lettered booth signs visible but unreadable, ceiling string-lights overhead; bold flat composition, no readable text in scene" | none | local |
| zine_action_outro.png | 1280×720 | 1.78 | P18 封底 outro hero | Background | `#1 Full-bleed background with floating title + #12 Faded image as backdrop with oversized overlay text + #29 Two-stop scrim` | ai | Pending | "Single open hand from above holding up a small folded zine toward the viewer; the zine cover slightly halftoned; rest of canvas is open paper field; composition designed to host enormous closing-line typography overlay in upper region" | none | hero_page |

> **User-provided photos** (in `sources/`, available as visual references for Image_Generator prompts — not embedded directly): `riso_ez200_printer.jpg`, `risograph_two_color_print.jpg`, `shakespeare_and_company_paris.jpg`, `jimbocho_yaguchi_koga.jpg`, `jimbocho_used_books.jpg`, `sanseido_bookstore.jpg`. Strategist 不將其作為 §VIII 資源行（避免與 ai 行 hero 衝突）；Image_Generator 在 prompt 撰寫時可參照其構圖與氛圍。

---

## IX. Content Outline

### Part 1: 開篇

#### Slide 01 - Cover 封面

- **Layout**: Full-bleed hero image + floating Impact 大字標題（zine 海報感）
- **Title**: 「Zine 文化指南 / INDIE BOOKSTORE × ZINE」
- **Subtitle**: 一份從一張紙到一家書店的獨立出版地圖
- **Info**: PPT Master Risograph 風格演示 · 2026

#### Slide 02 - 目錄

- **Layout**: agenda_list（5 節 + 簡述 + 頁碼區間）
- **Title**: 目錄 / TABLE OF CONTENTS
- **Visualization**: agenda_list
- **Content**:
  - 01 zine 是什麼 + 簡史四浪潮（P03–P04）
  - 02 Risograph：zine 工藝的靈魂載體（P05–P06）
  - 03 怎麼自己做一本 zine（P07–P08）
  - 04 全球 + 中國獨立書店地圖（P09–P13）
  - 05 怎麼逛 / 怎麼收藏 / 行動清單（P14–P18）

### Part 2: zine 是什麼

#### Slide 03 - zine 是什麼

- **Layout**: 大字定義 + 左側 narrow vertical image strip + 三條特徵列舉
- **Title**: ZINE = MAGAZINE − 商業邏輯
- **Content**:
  - 自制、非商業、印量極小（多在 1000 份以內，常少於 100）
  - 裝訂簡單 / 內容混合 / 完全作者主權
  - 與 magazine / book 的邊界：印量 + 商業意圖 + 編輯流程

#### Slide 04 - zine 簡史四浪潮

- **Layout**: timeline 橫向年代軸
- **Title**: 一百年裡 zine 的四次浪潮
- **Visualization**: timeline
- **Content**:
  - 1920s 業餘出版 + 哈萊姆 *Fire!!*
  - 1930s 科幻同人誌 *The Comet* / "fanzine" 一詞 1940 由 Russ Chauvenet 創
  - 1976 朋克 *Sniffin' Glue* 影印機普及
  - 1991 Riot Grrrl *Bikini Kill* + Riot Grrrl Press
  - 2010s 當代復興 + zine fair 爆發

### Part 3: Risograph

#### Slide 05 - Risograph 起源 + 視覺特徵

- **Layout**: 左側 full-height 機器側欄圖 + 右側 vertical_list 4 視覺特徵
- **Title**: Risograph：zine 工藝的靈魂載體
- **Visualization**: vertical_list
- **Content**:
  - 起源：Riso Kagaku 1946 / Risograph 007 1986
  - 視覺特徵 1：限定調色盤（一墨筒一色）
  - 視覺特徵 2：套色錯位 1–3px（misregistration）
  - 視覺特徵 3：半色調網點 + 油墨氣味
  - 視覺特徵 4：色塊疊加產生第三色

#### Slide 06 - Risograph 工作流程

- **Layout**: 中段橫幅圖（工藝示意）+ 下方 numbered_steps 5 步
- **Title**: 工藝：5 步從數字影象到印張
- **Visualization**: numbered_steps
- **Content**:
  - ① 接收數字影象
  - ② 燒蝕畫素化母版
  - ③ 母版包裹彩色墨筒
  - ④ 墨筒滾壓油墨到紙
  - ⑤ 多次過紙完成多色

### Part 4: 怎麼自己做一本 zine

#### Slide 07 - 八頁摺疊法

- **Layout**: 中央 hero 圖（摺疊的手）+ 四角 annotation cards（image-as-canvas + bezier 引線 #38）
- **Title**: 一張紙 → 一本 zine
- **Visualization**: numbered_steps（疊加在 image-as-canvas 上）
- **Content**:
  - ① 摺疊：長邊對摺 → 短邊對摺 → 中線對摺，得 8 矩形
  - ② 關鍵剪口：從對摺邊沿剪到中心點
  - ③ 組裝：雙手兩端往中心推
  - ④ 填內容：沒有規則

#### Slide 08 - 內容型別

- **Layout**: icon_grid 2×3 或 3×2
- **Title**: 你能填的東西
- **Visualization**: icon_grid
- **Content**:
  - 草圖 / 塗鴉 / 迷你漫畫（pencil）
  - 詩 / 宣言 / 短文（pen-nib）
  - 帶插圖的食譜（sticky-note）
  - 家庭照片 + 私人寫作（book）
  - 拼貼 + 混合媒材（scissors）
  - 實驗性視覺（brush）

### Part 5: 全球獨立書店

#### Slide 09 - 東京 Jimbōchō 神保町

- **Layout**: Full-bleed hero + 大字 + 左下三條事實條
- **Title**: 神保町 / JIMBŌCHŌ
- **Content**:
  - 全球最大舊書街之一：130–180 家書店
  - 1875 Takayama Honten / 1902 Kitazawa English Books / 2015 Morioka Shoten（一週一本）
  - 2025 Time Out "全球最酷街區"

#### Slide 10 - 巴黎 / 倫敦 / 紐約

- **Layout**: vertical_pillars 1×3
- **Title**: 三座城市，三種姿態
- **Visualization**: vertical_pillars
- **Content**:
  - **巴黎 Shakespeare and Company**：1951 George Whitman 現址；曾接納數千 tumbleweeds 寫作者
  - **倫敦 Daunt + Word on the Water**：Daunt 按國家分類；Word on the Water 1920s 荷蘭運河船
  - **紐約 Strand + Yu and Me**：1927 Strand 18 英里書架；2021 Yu and Me 華埠亞裔女性書店

#### Slide 11 - 柏林 Bücherbogen

- **Layout**: Full-bleed hero + 大字 + 浮動定義文字
- **Title**: BÜCHERBOGEN
- **Content**:
  - 位於 S-Bahn 高架橋下，磚砌拱頂
  - 專攻藝術、設計、攝影、電影、建築

#### Slide 12 - 中國大陸書店地圖

- **Layout**: basic_table（4 列 × 15 行）
- **Title**: 中國獨立書店地圖（zine 傾向）
- **Visualization**: basic_table
- **Content**: 15 家書店表 —— 書店 / 城市 / 特色 / zine 傾向（★/★★/★★★）

#### Slide 13 - 中國藝術書展

- **Layout**: labeled_card 雙卡並列（abC + UNFOLD）
- **Title**: 中國藝術書展雙子星
- **Visualization**: labeled_card
- **Content**:
  - **abC Art Book Fair**：2015 創辦，京滬雙城，第 6 屆上海 145 中國 + 41 國際 + 10,000 參觀
  - **UNFOLD Shanghai Art Book Fair**：abC 後一週舉辦，更高攤位費 + 更大客流

### Part 6: 怎麼逛 / 怎麼收藏 / 行動

#### Slide 14 - 怎麼逛獨立書店

- **Layout**: vertical_list 4 條
- **Title**: 進店前的 4 條
- **Visualization**: vertical_list
- **Content**:
  - ① 看選品 = 看店主 —— 獨立書店本質是"精神書架"
  - ② 留至少 1 小時 —— 瀏覽本身就是產品
  - ③ 帶現金 —— 一些小店不接受電子支付
  - ④ 拍照前先問 —— 多數獨立書店對拍照敏感

#### Slide 15 - 怎麼收藏 zine

- **Layout**: vertical_list 4 條
- **Title**: 收藏 zine 的 4 條
- **Visualization**: vertical_list
- **Content**:
  - ① 從一本起步 —— 找你最關心的主題
  - ② 用塑膠封套保護 —— 二次印刷罕見
  - ③ 跟蹤作者 / 出版方 Instagram
  - ④ 參加 abC / UNFOLD —— 新刊首發就是現場

#### Slide 16 - 行動清單：你的第一本 zine

- **Layout**: numbered_steps 4 步
- **Title**: 你的第一本 zine：4 步起手
- **Visualization**: numbered_steps
- **Content**:
  - ① 選一個真心關心的主題（不必宏大）
  - ② 折一張 A4 —— 用本 deck P07 的方法
  - ③ 填 8 頁 —— 手寫 / 拼貼 / 影印的舊照片
  - ④ 印 10 份 —— 5 份送朋友，5 份寄給獨立書店

#### Slide 17 - Sources & 致謝

- **Layout**: 雙列 sources 羅列 + 致謝小字
- **Title**: Sources / References
- **Content**: 來源連結清單（Wikipedia / My Modern Met / AFAR / The Creative Independent / 數英 / Sixth Tone 等）

#### Slide 18 - 封底 outro

- **Layout**: Full-bleed hero（手舉 zine）+ 大字 outro
- **Title**: 「印一份。送一份。換一份。」
- **Subtitle**: A zine is the world's smallest publishing house. It can also be yours.

---

## X. Speaker Notes Requirements

- **Filename**: 與 SVG 名一一對應（`01_cover.svg` → `notes/01_cover.md`）
- **Style**: conversational（適合咖啡館 / 分享會場景，不走正式）
- **Total duration**: ~12-15 分鐘（每頁 40-50 秒）
- **Purpose**: inspire（讓人想做一本 zine 而不只是知道 zine）

---

## XI. Technical Constraints Reminder

### SVG Generation Must Follow

1. viewBox: `0 0 1280 720`
2. Background uses `<rect>` elements with `#F5EFE0` paper color
3. Text wrapping uses `<tspan>` (`<foreignObject>` FORBIDDEN)
4. Transparency uses `fill-opacity` / `stroke-opacity`; `rgba()` FORBIDDEN
5. FORBIDDEN: `mask`, `<style>`, `class`, `foreignObject`, `textPath`, `animate*`, `script`
6. Text characters: raw Unicode (`—`, `→`, `©`, NBSP); HTML named entities (`&nbsp;`, `&mdash;`) FORBIDDEN. XML reserved chars escape as `&amp; &lt; &gt; &quot; &apos;`
7. **Risograph 美學專項**：
   - 套色錯位用偏移色塊疊加模擬（如同一形狀的 Federal Blue 與 Fluorescent Pink 副本 offset 1-3px）
   - 半色調網點用 `<pattern>` + 小 circles 模擬（dot density 控制）
   - 卡片無圓角（border-radius: 0）—— 與 Riso 印刷工藝一致
8. `clipPath` 僅允許應用於 `<image>` 元素；卡片 / 塊面用原生 `<rect>` 描述
9. Icon 嚴格只用 `chunk-filled/` 庫列表中的 27 個；缺失圖示在庫內找最近替代，禁止混庫

### PPT Compatibility Rules

- `<g opacity="...">` FORBIDDEN；每個子元素單獨設定 opacity
- Image transparency 用覆蓋層 (`<rect fill="bg-color" opacity="0.x"/>`)
- Inline styles only；external CSS 與 `@font-face` FORBIDDEN
- Impact 字型是 PPT 內建 display 字型，可安全使用；Microsoft YaHei / Consolas 同樣 Windows 預裝

---

## ✅ Design spec complete.

Next step:
- Images include AI generation → Invoke Image_Generator
