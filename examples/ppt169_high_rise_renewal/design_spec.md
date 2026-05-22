# 高層住宅"主動再生" - Design Spec

> 基於微信公眾號文章《香港火災之後，再也不敢買高層了，"主動再生"能解決高層住宅難題嗎？》的簡報設計規範。

## I. Project Information

| Item | Value |
| ---- | ----- |
| **Project Name** | 高層住宅"主動再生" — 從悉尼範本到中國困局 |
| **Canvas Format** | PPT 16:9 (1280×720) |
| **Page Count** | 15 |
| **Design Style** | A) General Versatile + Editorial Magazine（編輯雜誌風） |
| **Target Audience** | 城市更新/建築/地產從業者、政策研究者、關心居住安全的城市居民 |
| **Use Case** | 議題分享 / 行業沙龍 / 內部傳閱 |
| **Created Date** | 2026-05-16 |

---

## II. Canvas Specification

| Property | Value |
| -------- | ----- |
| **Format** | PPT 16:9 |
| **Dimensions** | 1280×720 |
| **viewBox** | `0 0 1280 720` |
| **Margins** | 左右 60px，上下 50px |
| **Content Area** | 1160×620（安全區） |

---

## III. Visual Theme

### Theme Style

- **Style**: 編輯雜誌風（editorial magazine） — 長文摘編 + 案例圖片 + 觀點提煉
- **Theme**: 淺色主題（米白紙感）
- **Tone**: 沉穩、有思辨張力、可讀性強；像《三聯生活週刊》《看理想》專題

### Color Scheme

| Role | HEX | Purpose |
| ---- | --- | ------- |
| **Background** | `#F5F2EC` | 米白紙感頁面底色 |
| **Secondary bg** | `#EBE6DC` | 卡片/分欄次級底 |
| **Primary** | `#2B3A4A` | 深石板藍灰 — 標題、正文主色 |
| **Secondary accent** | `#5A6B7A` | 次級文字、分割線 |
| **Accent (warning)** | `#C2410C` | 警示橙紅 — 火災、風險話題 |
| **Accent (regen)** | `#6B7A4F` | 苔綠 — 再生、可持續話題 |
| **Accent (heritage)** | `#8B7355` | 磚褐 — 建築、歷史話題 |
| **Body text** | `#2B3A4A` | 正文 |
| **Secondary text** | `#5A6B7A` | 註釋、來源 |
| **Tertiary text** | `#8A8275` | 頁碼、頁尾 |
| **Border/divider** | `#D6CFC0` | 分割線 |

> 60-30-10：米白底 60% / 深藍灰 30% / 橙紅+苔綠+磚褐合計 10%。每頁主題色按內容選用（火災頁用橙紅、再生頁用苔綠、建築案例頁用磚褐）。

---

## IV. Typography System

### Font Plan

**Typography direction**: Cool serif（學術編輯） + 中文楷體引言

| Role | Chinese | English | Fallback tail |
| ---- | ------- | ------- | ------------- |
| **Title** | `KaiTi` | `Georgia` | `serif` |
| **Body** | `"Microsoft YaHei", "PingFang SC"` | `Arial` | `sans-serif` |
| **Emphasis** | `KaiTi` | `Georgia` | `serif` |
| **Code** | — | `Consolas, "Courier New"` | `monospace` |

**Per-role font stacks**:

- Title: `Georgia, KaiTi, serif`（拉丁先行，雜誌感）
- Body: `"Microsoft YaHei", "PingFang SC", Arial, sans-serif`
- Emphasis: `KaiTi, Georgia, serif`（楷體引言/案例名）
- Code: `Consolas, "Courier New", monospace`

### Font Size Hierarchy

**Baseline**: Body = 20px（中等密度，適合科普長文）

| Purpose | Ratio | Px | Weight |
| ------- | ----- | -- | ------ |
| Cover title | 3-4x | 60-80 | Bold |
| Chapter opener | 2.2-2.5x | 44-50 | Bold |
| Page title | 1.6-1.8x | 32-36 | Bold |
| Subtitle | 1.2-1.4x | 24-28 | SemiBold |
| **Body** | **1x** | **20** | Regular |
| Annotation | 0.7-0.8x | 14-16 | Regular |
| Page number | 0.6x | 12 | Regular |

---

## V. Layout Principles

### Page Structure

- **Header area**: 80px — 章節編號（羅馬數字）+ 頁碼 + 細分割線
- **Content area**: 540px — 自由排布，多種 image-layout-pattern 混用
- **Footer area**: 40px — 頁尾來源/頁碼

### Layout Pattern Library

按內容選用：單欄居中（封面/結語）、不對稱分欄（案例對照）、全屏圖+浮字（章節扉頁/hero 頁）、圖文疊壓、並置對照（改造前後）、多圖拼貼（全球案例巡覽）、負空間驅動（金句頁）。

### Spacing Specification

**Universal**:
- Safe margin: 60px 左右 / 50px 上下
- Content block gap: 28-36px
- Icon-text gap: 12px

**Non-card containers**（編輯雜誌風以分割線和留白為主，少量卡片）:
- Line-height: 1.5× body
- Full-bleed text: 文字浮於圖上時加 0.4-0.6 不透明遮罩

---

## VI. Icon Usage Specification

### Source

- **Library**: `tabler-outline`（線條 stroke=2，編輯風格首選）
- **Usage**: SVG 佔位 `<use data-icon="tabler-outline/icon-name" .../>`

### Recommended Icon List

| Purpose | Icon Path | Page |
| ------- | --------- | ---- |
| 火災/警示 | `tabler-outline/flame` | P03 |
| 時間/樓齡 | `tabler-outline/clock` | P03 |
| 建築/塔樓 | `tabler-outline/building-skyscraper` | P04, P12 |
| 維修/工具 | `tabler-outline/tool` | P04 |
| 再生/迴圈 | `tabler-outline/refresh` | P06, P07 |
| 樹葉/可持續 | `tabler-outline/leaf` | P07 |
| 拆除/爆破 | `tabler-outline/bomb` | P05 |
| 地圖/位置 | `tabler-outline/map-pin` | P09, P10, P11 |
| 資金/錢袋 | `tabler-outline/coin` | P12 |
| 使用者/居民 | `tabler-outline/users` | P13 |
| 檢查/體檢 | `tabler-outline/clipboard-check` | P13 |
| 引用/金句 | `tabler-outline/quote` | P14 |

> Executor 生成時如發現額外圖示需求，在 `tabler-outline/` 目錄內 `ls | grep` 查詢最近鄰；不混庫。

---

## VII. Visualization Reference List

Catalog read: 71 templates

| Page | Template | Path | Summary-quote (verbatim) | Usage |
| ---- | -------- | ---- | ------------------------ | ----- |
| P02 | agenda_list | `templates/charts/agenda_list.svg` | "Pick for table of contents, meeting agendas, or presentation roadmap — numbered items + brief description + duration / owner per row." | 全篇議程導覽（4 部分） |
| P13 | numbered_steps | `templates/charts/numbered_steps.svg` | "Pick for 3-6 horizontal sequential steps with numeric emphasis — how-it-works section, getting-started guide, methodology overview, implementation phases." | "先體檢、後更新"治理流程 4 步 |

**Runners-up considered**:

- `vertical_list` | rejected for P02：議程頁通常需要章節編號 + 簡述列項，agenda_list 更專門，vertical_list 過於通用
- `process_flow` | rejected for P13：內容是治理理念的並列階段而非箭頭連線的工作流，numbered_steps 更貼合
- `pros_cons_chart` | rejected for P12：高層住宅改造困局是單邊複雜論述，不是清晰的利弊對照，故走自由設計

> 其它頁面以敘述 + 圖片為主，走自由設計（編輯雜誌拼貼/分欄/hero），不強行套圖表模板。

---

## VIII. Image Resource List

> 使用者提供 25 張原文配圖，全部已就位 `images/`。佈局採用多樣化 image-layout-pattern，不全用左右/上下分欄。

| Filename | Dimensions | Ratio | Purpose | Type | Layout pattern | Acquire Via | Status | Reference |
| -------- | --------- | ----- | ------- | ---- | -------------- | ----------- | ------ | --------- |
| 640.png | 606x991 | 0.61 | 香港高層夜景（封面背景） | Background | #1 full-bleed background with floating title | user | Existing | 城市夜景，燈火密集的超高層建築 |
| 640_1.png | 1080x917 | 1.18 | 電影《焚城》劇照 | Photography | #38 background image + annotation cards | user | Existing | 高層火災電影場景，警示氛圍 |
| 640_2.png | 1080x648 | 1.67 | 普魯特·艾格住宅區 | Photography | #48 side-by-side comparison（與 640_3 並置） | user | Existing | 美國失敗住宅區原貌 |
| 640_3.png | 660x521 | 1.27 | 普魯特·艾格被爆破 | Photography | #48 side-by-side comparison（與 640_2 並置） | user | Existing | 1972 年爆破拆除瞬間 |
| 640_4.png | 801x1200 | 0.67 | 改造前 AMP 中心 | Photography | #44 before-after split-screen（與 640_5 並置） | user | Existing | 老舊辦公塔樓原貌 |
| 640_5.png | 1080x2172 | 0.50 | 改造後 Quay Quarter Tower | Photography | #44 before-after split-screen（與 640_4 並置） | user | Existing | 全新摩天樓正面豎幅 |
| 640_6.png | 750x1000 | 0.75 | Quay Quarter Tower 細節 1 | Photography | #2 left-third image / right-side text | user | Existing | 弧形頂部呼應港灣 |
| 640_7.png | 1080x440 | 2.45 | Quay Quarter Tower 細節 2 | Photography | #5 top-bottom band（超寬） | user | Existing | 摩天樓遠景超寬幅 |
| 640_8.png | 1080x1166 | 0.93 | Quay Quarter Tower 細節 3 | Photography | #41 image-as-canvas + KPI overlay | user | Existing | 建築近景，疊加環保資料 |
| 640_9.png | 640x345 | 1.86 | 改造前深圳婦兒大廈 | Photography | #44 before-after split-screen（與 640_10 並置） | user | Existing | 老舊大廈原貌 |
| 640_10.png | 1080x1620 | 0.67 | 改造後深圳婦兒大廈 | Photography | #44 before-after split-screen（與 640_9 並置） | user | Existing | 彩色網格立面新貌 |
| 640_11.png | 600x781 | 0.77 | 改造前華東電力大樓 | Photography | #44 before-after split-screen（與 640_12 並置） | user | Existing | 1988 年原貌 |
| 640_12.png | 1080x720 | 1.50 | 改造後艾迪遜酒店 | Photography | #44 before-after split-screen（與 640_11 並置） | user | Existing | 節能改造後立面 |
| 640_13.png | 1080x718 | 1.50 | 紐約 One Wall Street 改造後 | Photography | #2 left-third image / right-side text | user | Existing | 裝飾藝術風格摩天樓 |
| 640_14.png | 1080x608 | 1.78 | One Wall Street 公寓內景 | Photography | #20 polaroid stack | user | Existing | 室內空間細節 |
| 640_15.png | 469x581 | 0.81 | 城市建築氛圍 | Atmosphere | #6 atmospheric backdrop with overlay | user | Existing | 玻璃幕牆仰視 |
| 640_16.png | 1080x1439 | 0.75 | 北京"辦公環橙"專案 | Photography | #3 right-third image / left-side text | user | Existing | 高層住宅改辦公樓案例 |
| 640_17.png | 640x400 | 1.60 | MUJI 改造老舊公寓 | Photography | #20 polaroid stack（與 640_16 拼貼） | user | Existing | 日式翻新房間 |
| 640_18.png | 1080x1440 | 0.75 | 高層住宅外景氛圍 | Atmosphere | #6 atmospheric backdrop with overlay | user | Existing | 高層樓群仰視 |
| 640_19.png | 1080x810 | 1.33 | 改造前浙工新村 | Photography | #44 before-after split-screen（與 640_20 並置） | user | Existing | 80 年代老舊小區 |
| 640_20.png | 1080x619 | 1.74 | 浙工新村建成效果圖 | Photography | #44 before-after split-screen（與 640_19 並置） | user | Existing | 原拆原建效果圖 |
| 640_21.png | 870x580 | 1.50 | 居民議事氛圍 | Atmosphere | #38 background image + annotation cards | user | Existing | 社群共建共治氛圍 |
| 640_22.png | 1074x806 | 1.33 | 城市更新/體檢氛圍 | Photography | #2 left-third image / right-side text | user | Existing | 城市俯瞰，體檢意象 |
| 640_23.png | 1080x723 | 1.49 | 城市天際線（結語） | Background | #1 full-bleed background with floating title | user | Existing | 結語 hero 大圖 |
| 640_24.png | 640x640 | 1.00 | 圓形建築裝飾元素 | Decorative | #21 circular crop accent | user | Existing | 裝飾圓圖，章節扉頁 accent |

> Layout 多樣性自檢：含 #1（hero）、#2/#3（不對稱分欄）、#5（超寬 band）、#6（氛圍背景）、#20（polaroid 拼貼）、#21（圓裁飾角）、#38（背景+卡）、#41（image-as-canvas + 疊資料）、#44（before-after 對照）、#48（並置對比）共 10 種 pattern；Group D 覆蓋：P08（#41 image-as-canvas + KPI 疊層）。

---

## IX. Content Outline

### Part 1: 引子 — 從一場火災說起

#### Slide 01 - Cover

- **Layout**: 全屏 hero 背景 + 浮字標題（Pattern #1）
- **Title**: 主動再生
- **Subtitle**: 香港火災之後，老舊高層何去何從
- **Info**: 基於公眾號《孫琬童》原文 · 2026.05
- **Image**: 640.png（高層夜景）

#### Slide 02 - Agenda

- **Layout**: 單列議程（agenda_list）
- **Title**: 本次議程
- **Visualization**: agenda_list（4 項）
- **Content**:
  - I. 警鐘：高層老齡化與消防困局
  - II. 範本：悉尼摩天樓的"再生革命"
  - III. 巡覽：全球功能再造案例
  - IV. 困局：中國老舊高層住宅的硬骨頭

### Part 2: 警鐘 — 高層老齡化與消防困局

#### Slide 03 - 香港火災敲響警鐘

- **Layout**: 背景圖 + 註釋卡（Pattern #38）
- **Title**: 一場火災，暴露的不只是消防隱患
- **Content**:
  - 2025.11.26 香港大埔宏福苑：7 棟 30 層以上、近百米高、樓齡 42 年
  - 2025 年前 8 個月全國高層建築火災 **3.6 萬起**，超 2023 全年總量
  - 地面消防救援高度通常 50–80 米；超過 100 米主要靠建築自救
- **Image**: 640_1.png（《焚城》劇照背景）

#### Slide 04 - 高層正在老去

- **Layout**: 不對稱分欄 #2（左圖右文）
- **Title**: 當年的繁榮象徵，正在變成沉重的維修負擔
- **Content**:
  - 建成 10 餘年後，結構、消防、電梯、外牆等風險密集顯現
  - 維護成本隨樓齡陡增；願意住高層的人正在變少
  - "高層住宅是未來的貧民窟" — 西方已有先例
- **Image**: 640_18.png（高層樓群仰視）

#### Slide 05 - 前車之鑑：普魯特·艾格

- **Layout**: 並置對照（Pattern #48）
- **Title**: 老舊高層只有"被爆破"一條路嗎？
- **Content**:
  - 美國普魯特·艾格：33 棟高層，公共空間長期失養 → 1972 年全部爆破
  - 富裕居民遷出 → 中低收入聚居 → 設施破敗 → 高犯罪率 → 拆除
- **Images**: 640_2.png（原貌） + 640_3.png（爆破瞬間）

### Part 3: 範本 — 悉尼摩天樓的"再生革命"

#### Slide 06 - 章節扉頁 II

- **Layout**: 全屏背景 + 浮字 + 圓形裝飾（Pattern #1 + #21）
- **Title**: II
- **Subtitle**: 悉尼範本 — 一座摩天樓的"再生"革命
- **Image**: 640_24.png（圓形裝飾）

#### Slide 07 - Quay Quarter Tower：從拆到改

- **Layout**: Before-after 對照（Pattern #44）
- **Title**: 世界上第一座"全面升級改造"的摩天大樓
- **Content**:
  - 原 AMP 中心：1976 年，206 米，49 層
  - 設計：3XN — "最大化保留、高質量升級"
  - 保留 65% 主體結構 + 95% 核心筒，轉型多功能綜合體
- **Images**: 640_4.png（改造前） + 640_5.png（改造後）

#### Slide 08 - 環保資料：再生的真正分量

- **Layout**: Image-as-canvas + KPI 疊層（Pattern #41）
- **Title**: 入圍"為地球奮鬥獎"決賽的關鍵
- **Visualization**: 三個大數字（hero number）疊在建築圖上
- **Content**:
  - **−80%** 建築垃圾（結構複用）
  - **−40%** 碳排放（相比推倒重建）
  - **−30%** 能源消耗（智慧通風+光伏幕牆+雨水回收）
- **Image**: 640_8.png（建築近景作底）

### Part 4: 巡覽 — 全球功能再造案例

#### Slide 09 - 深圳婦兒大廈（MVRDV）

- **Layout**: Before-after 對照（Pattern #44）
- **Title**: 給老建築穿一件"彩色網格外衣"
- **Content**:
  - 1994 年建成，MVRDV 主導改造
  - 彩色網格立面增 1 米進深 → 遮陽 + 自然通風
  - 引入酒店、兒童探索館、圖畫書博物館等多種業態
- **Images**: 640_9.png（改造前） + 640_10.png（改造後）

#### Slide 10 - 上海艾迪遜酒店（華東電力大樓）

- **Layout**: Before-after 對照（Pattern #44）
- **Title**: 全國首家城市更新領域**碳中和酒店**
- **Content**:
  - 原 1988 年華東電力大樓，126 米，南京東路第一棟高層
  - 2018 改擴建為艾迪遜酒店；2023 完成節能改造
  - 高效能外窗 + 空氣源熱泵 + 節能電梯 + 節水器具
- **Images**: 640_11.png（改造前） + 640_12.png（改造後）

#### Slide 11 - 紐約 One Wall Street：辦公變住宅

- **Layout**: 不對稱分欄 #2（左圖右文） + polaroid 拼貼 #20
- **Title**: 1931 年的裝飾藝術摩天樓，變成 566 套公寓
- **Content**:
  - 50 層辦公塔 → 單間到四居室全戶型公寓
  - 辦公/商業改住宅是全球趨勢：結構強度高、靈活性大
- **Images**: 640_13.png（外景） + 640_14.png（公寓內景 polaroid）

### Part 5: 困局 — 中國老舊高層住宅的硬骨頭

#### Slide 12 - 章節扉頁 IV

- **Layout**: 氛圍背景 + 浮字（Pattern #6）
- **Title**: IV
- **Subtitle**: 高層住宅老了、壞了，該怎麼辦？
- **Image**: 640_15.png（玻璃幕牆仰視）

#### Slide 13 - 試點案例：北京"辦公環橙" + 浙工新村

- **Layout**: 雙列拼貼（#3 右圖左文 + #44 對照）
- **Title**: 已有的嘗試：從功能再造到原拆原建
- **Content**:
  - **辦公環橙**（北京天通苑）：高層住宅 → 辦公樓，緩解"職住分離"
  - **浙工新村**（杭州）：首個原拆原建老舊小區
    - 拆 13 幢，新建 7 幢 11 層；總投資 5.3 億，居民自籌 4.7 億
    - 每戶出資 10–100 萬元
- **Images**: 640_16.png（辦公環橙） + 640_19.png + 640_20.png（浙工新村對照）

#### Slide 14 - 真正的難題：讓每家掏錢

- **Layout**: 負空間驅動 — 大字金句 + 註釋（Pattern #11）
- **Title**: "原拆原建"在高層專案中，註定極其複雜
- **Content**:
  - **金句**："高層住宅區戶數更多，全體業主達成共識的難度大。"
  - 資金從哪來、由誰出 → 仍在探索
  - 出路可能在"共建共治共享"治理模式 — 設立"養老金"、引入"居委會"自管
- **Image**: 640_21.png（社群議事氛圍背景）

#### Slide 15 - 結語：先體檢、後更新

- **Layout**: 全屏 hero + numbered_steps 4 步
- **Title**: 從追求高度，到沉澱厚度
- **Visualization**: numbered_steps（4 步）
- **Content**:
  - **1. 體檢** — 截至 2025.11，全國 297 個地級市 + 150+ 縣級市啟動城市體檢
  - **2. 設計** — 專業機構提供安全可靠方案
  - **3. 協調** — 政府平臺 + 社群基層組織
  - **4. 再生** — 多方合力，老舊超高層煥發新機
- **Image**: 640_23.png（城市天際線 hero 背景）

---

## X. Speaker Notes Requirements

- 每頁 100–180 字，對應 SVG 同名（`01_cover.md` ↔ `01_cover.svg`）
- 風格：解說式，雜誌主持口吻；不堆砌資料，提煉觀點
- `notes/total.md` 主文件使用 `#` 章節標題；分頁檔案不使用 `#`

---

## XI. Technical Constraints Reminder

### SVG Generation Must Follow:

1. viewBox: `0 0 1280 720`
2. 背景使用 `<rect>` 元素
3. 文字換行使用 `<tspan>`（`<foreignObject>` 禁用）
4. 透明度使用 `fill-opacity` / `stroke-opacity`；`rgba()` 禁用
5. 禁用：`mask`、`<style>`、`class`、`foreignObject`、`textPath`、`animate*`、`script`
6. 字元使用原生 Unicode（— – © ® → NBSP），HTML 命名實體禁用；`&` `<` `>` `"` `'` 必須轉義
7. `clipPath` 僅允許用於 `<image>` 元素

### PPT Compatibility Rules:

- `<g opacity="...">` 禁用（設到每個子元素）
- 圖片透明用疊加 `<rect>` 蒙版
- 僅內聯樣式；外部 CSS 與 `@font-face` 禁用
