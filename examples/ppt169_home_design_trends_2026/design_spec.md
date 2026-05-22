# 2026家居趨勢 - Design Spec

> This document is the human-readable design narrative — rationale, audience, style, color choices, content outline. It is read once by downstream roles for context.
>
> The machine-readable execution contract lives in `spec_lock.md` (short form of color / typography / icon / image decisions). Executor re-reads `spec_lock.md` before every SVG page to resist context-compression drift. Keep the two files in sync; if they diverge, `spec_lock.md` wins.

## I. Project Information

| Item | Value |
| ---- | ----- |
| **Project Name** | 2026家居趨勢：迴歸"人的尺度" |
| **Canvas Format** | PPT 16:9 (1280×720) |
| **Page Count** | 12 |
| **Design Style** | General Versatile (A) |
| **Target Audience** | 室內設計師、家居愛好者、裝修計劃者 |
| **Use Case** | 家居設計趨勢分享/培訓演示 |
| **Created Date** | 2026-04-22 |

---

## II. Canvas Specification

| Property | Value |
| -------- | ----- |
| **Format** | PPT 16:9 |
| **Dimensions** | 1280×720 |
| **viewBox** | `0 0 1280 720` |
| **Margins** | left/right 60px, top/bottom 50px |
| **Content Area** | 1160×620 |

---

## III. Visual Theme

### Theme Style

- **Style**: General Versatile — 雜誌質感的圖文混排風格
- **Theme**: Dark theme（深色暖調底色）
- **Tone**: 高階、溫暖、自然、人文、雜誌感

### Color Scheme

| Role | HEX | Purpose |
| ---- | --- | ------- |
| **Background** | `#1A1714` | 深棕暖黑底色 |
| **Secondary bg** | `#2A2520` | 卡片/區域背景 |
| **Primary** | `#C4A882` | 標題裝飾、金色暖調 |
| **Accent** | `#D4956A` | 資料高亮、關鍵資訊 |
| **Secondary accent** | `#8B7355` | 漸變過渡、次要裝飾 |
| **Body text** | `#E8E0D4` | 主體文字（淺暖白） |
| **Secondary text** | `#B0A08E` | 註釋說明 |
| **Tertiary text** | `#7A6E60` | 補充資訊、頁尾 |
| **Border/divider** | `#3D362E` | 卡片邊框、分隔線 |
| **Success** | `#7BA37B` | 可持續/正向指標 |
| **Warning** | `#C06048` | 強調/警示 |

### Gradient Scheme

```xml
<!-- Title gradient -->
<linearGradient id="titleGradient" x1="0%" y1="0%" x2="100%" y2="0%">
  <stop offset="0%" stop-color="#C4A882"/>
  <stop offset="100%" stop-color="#D4956A"/>
</linearGradient>

<!-- Background decorative gradient -->
<radialGradient id="bgDecor" cx="80%" cy="20%" r="50%">
  <stop offset="0%" stop-color="#C4A882" stop-opacity="0.08"/>
  <stop offset="100%" stop-color="#C4A882" stop-opacity="0"/>
</radialGradient>
```

---

## IV. Typography System

### Font Plan

**Typography direction**: Editorial Display（雜誌展示風）— 標題使用襯線字型傳遞高階感，正文使用無襯線保證閱讀性。

| Role | Chinese | English | Fallback tail |
| ---- | ------- | ------- | ------------- |
| **Title** | `SimSun` | `Georgia` | `serif` |
| **Body** | `"Microsoft YaHei"`, `"PingFang SC"` | `Arial` | `sans-serif` |
| **Emphasis** | `SimSun` | `Georgia` | `serif` |
| **Code** | — | `Consolas, "Courier New"` | `monospace` |

**Per-role font stacks**:

- Title: `Georgia, SimSun, serif`
- Body: `"Microsoft YaHei", "PingFang SC", Arial, sans-serif`
- Emphasis: `Georgia, SimSun, serif`
- Code: `Consolas, "Courier New", monospace`

### Font Size Hierarchy

**Baseline**: Body font size = 22px（內容密度適中，每頁 3-5 要點為主）

| Purpose | Ratio to body | Size | Weight |
| ------- | ------------- | ---- | ------ |
| Cover title | 3.6x | 80px | Bold |
| Chapter opener | 2.2x | 48px | Bold |
| Page title | 1.5x | 32px | Bold |
| Subtitle | 1.3x | 28px | SemiBold |
| **Body content** | **1x** | **22px** | Regular |
| Annotation / caption | 0.73x | 16px | Regular |
| Page number / footnote | 0.55x | 12px | Regular |

---

## V. Layout Principles

### Page Structure

- **Header area**: 50-80px, 含頁面標題及裝飾元素
- **Content area**: 560-620px, 主要圖文內容區域
- **Footer area**: 30-40px, 頁碼及來源資訊

### Layout Pattern Library

本專案以圖文並茂為核心，主要使用以下佈局模式：

| Pattern | Used In |
| ------- | ------- |
| **Full-bleed + floating text** | P01 封面、P10 可持續奢華 |
| **Asymmetric split (4:6 / 3:7)** | P03 色彩、P05 材質、P06 紋理、P08 奶油風 |
| **Symmetric split (5:5)** | P04 色彩實踐、P09 波西米亞&復古 |
| **Center-radiating** | P07 CMT體系 |
| **Single column centered** | P02 引言 |
| **Three-column cards** | P11 書籍推薦 |
| **Negative-space-driven** | P12 結語 |

### Spacing Specification

**Universal**:

| Element | Current Project |
| ------- | --------------- |
| Safe margin from canvas edge | 60px |
| Content block gap | 30px |
| Icon-text gap | 10px |

**Card-based layouts** (P07, P11):

| Element | Current Project |
| ------- | --------------- |
| Card gap | 24px |
| Card padding | 24px |
| Card border radius | 12px |

---

## VI. Icon Usage Specification

### Source

- **Built-in icon library**: `templates/icons/tabler-filled/` — 圓潤貝塞爾曲線，契合家居/生活方式溫暖調性
- **Usage method**: Placeholder format `{{icon:tabler-filled/icon-name}}`

### Recommended Icon List

| Purpose | Icon Path | Page |
| ------- | --------- | ---- |
| 色彩主題 | `{{icon:tabler-filled/palette}}` | P03, P04 |
| 材質主題 | `{{icon:tabler-filled/diamond}}` | P05 |
| 紋理主題 | `{{icon:tabler-filled/paint}}` | P06 |
| 家居 | `{{icon:tabler-filled/home}}` | P01, P02 |
| 太陽/光線 | `{{icon:tabler-filled/sun}}` | P05 |
| 樹葉/自然 | `{{icon:tabler-filled/leaf}}` | P10 |
| 星星/亮點 | `{{icon:tabler-filled/sparkles}}` | P07 |
| 心/情感 | `{{icon:tabler-filled/heart}}` | P12 |
| 書籍 | `{{icon:tabler-filled/book}}` | P11 |
| 眼睛/視覺 | `{{icon:tabler-filled/eye}}` | P06 |
| 調整 | `{{icon:tabler-filled/adjustments}}` | P07 |
| 星標 | `{{icon:tabler-filled/star}}` | P08 |

---

## VII. Visualization Reference List

| Visualization Type | Reference Template | Used In |
| ------------------ | ------------------ | ------- |
| concentric_circles | `templates/charts/concentric_circles.svg` | P07 (CMT三層體系) |

---

## VIII. Image Resource List

| Filename | Dimensions | Ratio | Purpose | Intent | Type | Status |
| -------- | ---------- | ----- | ------- | ------ | ---- | ------ |
| intro_living.png | 1080x608 | 1.78 | P01 封面全屏背景 | Hero | Photography | Existing |
| space_overview.png | 800x540 | 1.48 | P02 引言配圖 | Side-by-side | Photography | Existing |
| color_wheel.png | 559x823 | 0.68 | P03 色彩理論配圖 | Side-by-side | Diagram | Existing |
| brown_cozy.png | 658x496 | 1.33 | P03 棕色舒適空間 | Accent | Photography | Existing |
| light_tone_room.png | 749x749 | 1.00 | P04 淺色調空間 | Side-by-side | Photography | Existing |
| saturated_room.png | 853x671 | 1.27 | P04 高飽和度空間 | Side-by-side | Photography | Existing |
| material_detail.png | 749x708 | 1.06 | P05 材質細節 | Side-by-side | Photography | Existing |
| light_material.png | 800x1000 | 0.80 | P05 光與材質 | Accent | Photography | Existing |
| texture_tactile.png | 615x398 | 1.55 | P06 觸覺紋理 | Side-by-side | Photography | Existing |
| texture_visual.png | 519x569 | 0.91 | P06 視覺紋理 | Side-by-side | Photography | Existing |
| cmt_overview.png | 990x744 | 1.33 | P07 CMT體系總覽 | Side-by-side | Photography | Existing |
| cmt_neutral_mix.png | 1023x636 | 1.61 | P07 中性色搭配 | Accent | Photography | Existing |
| dark_tone_luxury.png | 614x423 | 1.45 | P07 深色調奢華 | Accent | Photography | Existing |
| cream_style.png | 681x499 | 1.36 | P08 奶油風空間 | Side-by-side | Photography | Existing |
| bohemian_style.png | 615x924 | 0.67 | P09 波西米亞風 | Side-by-side | Photography | Existing |
| retro_style.png | 1080x608 | 1.78 | P09 懷舊復古風 | Side-by-side | Photography | Existing |
| sustainable_luxury.png | 417x500 | 0.83 | P10 可持續奢華 | Side-by-side | Photography | Existing |
| book_cover1.png | 1080x732 | 1.48 | P11 書籍封面 | Side-by-side | Photography | Existing |
| book_cover2.png | 1080x735 | 1.47 | P11 書籍封面背面 | Accent | Photography | Existing |
| book_inside1.png | 1080x741 | 1.46 | P11 書籍內頁展示 | Accent | Photography | Existing |
| book_inside2.png | 1080x738 | 1.46 | P11 書籍內頁展示 | Accent | Photography | Existing |
| book_display1.png | 1080x727 | 1.49 | P12 書籍展示 | Side-by-side | Photography | Existing |
| book_display2.png | 1080x743 | 1.45 | P12 書籍展示 | Accent | Photography | Existing |

---

## IX. Content Outline

### Part 1: 開篇

#### Slide 01 - 封面

- **Layout**: Full-bleed + floating text
- **Title**: 2026家居趨勢
- **Subtitle**: 迴歸"人的尺度"，讓色彩、材質與紋理塑造"空間的高階感"
- **Info**: 基於《空間的高階感》· 2026
- **Images**: `intro_living.png`（hero全屏，暗色漸變疊加層保證文字可讀）

#### Slide 02 - 從"網紅風"到"人的尺度"

- **Layout**: Single column centered + side-by-side image
- **Title**: 從"網紅風"到"人的尺度"
- **Images**: `space_overview.png`
- **Content**:
  - 過去幾年家居"網紅風"迅速更迭
  - 2026年轉向：從視覺符號堆砌迴歸人本關懷
  - 高階感 = 色彩 + 材質 + 紋理的精妙搭配
  - 有顏值，更有溫度與情感

### Part 2: 三大底層元素

#### Slide 03 - 色彩：空間的情緒魔法師

- **Layout**: Asymmetric split (4:6) — 左圖右文
- **Title**: 色彩：空間的"情緒魔法師"
- **Images**: `color_wheel.png`（左側主圖），`brown_cozy.png`（右下小圖點綴）
- **Content**:
  - 色彩是空間的第一印象
  - 能改變視覺尺度、營造氛圍
  - 暖色調 → 溫柔包裹感；冷色調 → 開闊冷靜
  - 不同色彩傳遞不同訊號與心理反應

#### Slide 04 - 色彩實踐：冷暖色調的空間效果

- **Layout**: Symmetric split (5:5) — 左右對比
- **Title**: 冷暖色調的空間效果對比
- **Images**: `light_tone_room.png`（左，淺色調），`saturated_room.png`（右，高飽和度）
- **Content**:
  - 左：淺色調 → 增大光線反射 → 空間顯得寬敞
  - 右：高飽和度 → 房間緊湊小巧
  - 灰綠 → 平靜專注；咖色 → 陽光包裹；跳色 → 個性活力

#### Slide 05 - 材質：觸手可及的空間語言

- **Layout**: Asymmetric split (3:7) — 右側大圖
- **Title**: 材質：觸手可及的空間語言
- **Images**: `material_detail.png`（主圖），`light_material.png`（次圖/accent）
- **Content**:
  - 材料是色彩搭配的物理基礎
  - 原木地板 → 質樸溫暖；手工編織 → 慵懶鬆弛
  - 光本身也是一種材質
  - 巧妙照明 + 色彩光影 → 不依賴昂貴材料也能實現高階感

#### Slide 06 - 紋理：賦予空間靈魂的細節

- **Layout**: Asymmetric split (5:5) — 左右並列
- **Title**: 紋理：賦予空間靈魂的細節
- **Images**: `texture_tactile.png`（左，觸覺），`texture_visual.png`（右，視覺）
- **Content**:
  - 紋理 = 空間的"指紋"，獨一無二的辨識度
  - 觸覺紋理：羊毛地毯 → 柔軟溫暖；粗陶花瓶 → 凹凸肌理
  - 視覺紋理：桌布圖案 → 眼睛"感受"肌理

### Part 3: CMT 體系

#### Slide 07 - CMT 體系：色彩·材質·紋理的交響

- **Layout**: Center-radiating + accent images
- **Title**: CMT 體系：編織全方位感官體驗
- **Visualization**: concentric_circles (CMT三層)
- **Images**: `cmt_overview.png`（主視覺），`cmt_neutral_mix.png`（中性色案例），`dark_tone_luxury.png`（深色調案例）
- **Content**:
  - CMT = Colour + Material + Texture
  - 物理層：光滑/粗糙、透明/不透明、高光/亞光
  - 心理層：手工/工業、簡樸/奢華、安慰/刺激
  - 不是簡單疊加，是系統性編織 — 如交響樂團的指揮

### Part 4: 2026 流行風格

#### Slide 08 - 奶油風進化論

- **Layout**: Asymmetric split (4:6) — 左文右圖
- **Title**: 奶油風 2.0：從公式化到細膩表達
- **Images**: `cream_style.png`
- **Content**:
  - 奶油風正經歷深刻"進化"
  - 不再只是"米白牆面+原木傢俱"的公式
  - 顏色基底：奶油色、燕麥色、米白色
  - 材質點睛：羊毛、亞麻、天然結疤原木、手工陶瓷
  - 真正的治癒空間 = 可觸控 + 可感知

#### Slide 09 - 波西米亞 & 懷舊復古

- **Layout**: Symmetric split (5:5) — 左右雙風格
- **Title**: 自由靈魂與時間記憶
- **Images**: `bohemian_style.png`（左，波西米亞），`retro_style.png`（右，懷舊復古）
- **Content**:
  - 波西米亞：大膽色彩 + 自由織物 + 手工掛毯 → "有層次的不羈感"
  - 懷舊復古：風化木材 + 熟鐵 + 柳編 → 帶有使用痕跡的"時間感"
  - 共同特點：對真實與情感的渴望

#### Slide 10 - 可持續奢華

- **Layout**: Full-bleed + floating text（breathing頁）
- **Title**: 可持續奢華：負責任的審美
- **Images**: `sustainable_luxury.png`
- **Content**:
  - 2026 奢華不再是昂貴材料的堆砌
  - 環保飾面、自然光照、再生木材、軟木、黃麻纖維
  - 從"炫耀性消費"轉向"負責任的審美"
  - 與世界和諧共存的生活哲學

### Part 5: 結語

#### Slide 11 - 一本書解鎖空間高階感

- **Layout**: Three-column cards（書籍展示）
- **Title**: 《空間的高階感》— 可拆解、可複製、可驗證的美學體系
- **Images**: `book_cover1.png`, `book_cover2.png`, `book_inside1.png`, `book_inside2.png`
- **Content**:
  - 作者：宋文雯（清華大學色彩研究所常務副所長）
  - 創新引入 CMF → CMT 體系
  - 色彩篇 + 材料篇 + 紋理篇 + 綜合篇
  - 適合：設計師專業提升 / 裝修業主自學

#### Slide 12 - 結語

- **Layout**: Negative-space-driven + accent image
- **Title**: 讓家迴歸"人的尺度"
- **Images**: `book_display1.png`, `book_display2.png`
- **Content**:
  - 高階感的本質：色彩、材質、紋理的精妙共鳴
  - 有顏值，更有溫度與情感
  - 參考來源：《空間的高階感——設計師的色彩、材質、紋理搭配指南》

---

## X. Speaker Notes Requirements

Generate corresponding speaker note files for each page, saved to the `notes/` directory:

- **File naming**: Match SVG names, e.g., `01_cover.md`
- **Content includes**: Script key points, timing cues, transition phrases
- **Style**: 自然對話式（conversational），適合設計趨勢分享場景
- **Duration**: 約 15-20 分鐘總時長
- **Purpose**: Inform + Inspire

---

## XI. Technical Constraints Reminder

### SVG Generation Must Follow:

1. viewBox: `0 0 1280 720`
2. Background uses `<rect>` elements
3. Text wrapping uses `<tspan>` (`<foreignObject>` FORBIDDEN)
4. Transparency uses `fill-opacity` / `stroke-opacity`; `rgba()` FORBIDDEN
5. FORBIDDEN: `clipPath`, `mask`, `<style>`, `class`, `foreignObject`
6. FORBIDDEN: `textPath`, `animate*`, `script`
7. `marker-start` / `marker-end` conditionally allowed: `<marker>` must be in `<defs>`, `orient="auto"`, shape must be triangle / diamond / circle

### PPT Compatibility Rules:

- `<g opacity="...">` FORBIDDEN (group opacity); set opacity on each child element individually
- Image transparency uses overlay mask layer (`<rect fill="bg-color" opacity="0.x"/>`)
- Inline styles only; external CSS and `@font-face` FORBIDDEN
