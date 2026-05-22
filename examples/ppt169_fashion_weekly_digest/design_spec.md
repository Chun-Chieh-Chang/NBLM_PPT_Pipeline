# 美學周鑑 · 解鎖潮流序章 - Design Spec

> This document is the human-readable design narrative — rationale, audience, style, color choices, content outline. It is read once by downstream roles for context.
>
> The machine-readable execution contract lives in `spec_lock.md` (short form of color / typography / icon / image decisions). Executor re-reads `spec_lock.md` before every SVG page to resist context-compression drift. Keep the two files in sync; if they diverge, `spec_lock.md` wins.

## I. Project Information

| Item | Value |
| ---- | ----- |
| **Project Name** | 美學周鑑 · 解鎖潮流序章 |
| **Canvas Format** | PPT 16:9 (1280×720) |
| **Page Count** | 16 |
| **Design Style** | General Versatile — Magazine Editorial |
| **Target Audience** | 時尚行業從業者、奢侈品愛好者、品牌營銷人員 |
| **Use Case** | 時尚資訊分享、品牌動態播報、社交傳播 |
| **Created Date** | 2026-04-26 |

---

## II. Canvas Specification

| Property | Value |
| -------- | ----- |
| **Format** | PPT 16:9 |
| **Dimensions** | 1280×720 |
| **viewBox** | `0 0 1280 720` |
| **Margins** | 左右 50px, 上下 40px |
| **Content Area** | 1180×640 |

---

## III. Visual Theme

### Theme Style

- **Style**: Magazine Editorial — 高階時尚雜誌編輯風格
- **Theme**: Dark theme — 深色背景突出品牌視覺
- **Tone**: 奢華、精緻、現代、雜誌感

### Color Scheme

| Role | HEX | Purpose |
| ---- | --- | ------- |
| **Background** | `#0A0A0A` | 深黑底色，奢侈品雜誌調性 |
| **Secondary bg** | `#1A1A1A` | 卡片/區塊底色 |
| **Primary** | `#C9A96E` | 金色，奢侈品標誌色，標題裝飾、圖示 |
| **Accent** | `#E8D5B5` | 淺金/米白，副標題、關鍵資訊高亮 |
| **Secondary accent** | `#8B7355` | 暗金/古銅，漸變過渡、輔助裝飾 |
| **Body text** | `#F5F0EB` | 暖白色正文 |
| **Secondary text** | `#9E9690` | 灰棕色註釋文字 |
| **Border/divider** | `#2A2520` | 深棕色邊框、分割線 |

### Gradient Scheme

```xml
<!-- Title accent gradient -->
<linearGradient id="titleGradient" x1="0%" y1="0%" x2="100%" y2="0%">
  <stop offset="0%" stop-color="#C9A96E"/>
  <stop offset="100%" stop-color="#E8D5B5"/>
</linearGradient>

<!-- Decorative radial glow -->
<radialGradient id="bgDecor" cx="80%" cy="20%" r="50%">
  <stop offset="0%" stop-color="#C9A96E" stop-opacity="0.08"/>
  <stop offset="100%" stop-color="#C9A96E" stop-opacity="0"/>
</radialGradient>

<!-- Image overlay gradient (bottom fade) -->
<linearGradient id="imageOverlay" x1="0%" y1="0%" x2="0%" y2="100%">
  <stop offset="0%" stop-color="#0A0A0A" stop-opacity="0"/>
  <stop offset="60%" stop-color="#0A0A0A" stop-opacity="0.3"/>
  <stop offset="100%" stop-color="#0A0A0A" stop-opacity="0.85"/>
</linearGradient>
```

---

## IV. Typography System

### Font Plan

**Typography direction**: Editorial display — 標題襯線體營造雜誌質感，正文無襯線體保證可讀性

| Role | Chinese | English | Fallback tail |
| ---- | ------- | ------- | ------------- |
| **Title** | `SimSun` | `Georgia` | `serif` |
| **Body** | `"Microsoft YaHei", "PingFang SC"` | `Arial` | `sans-serif` |
| **Emphasis** | `SimSun` | `Georgia` | `serif` |
| **Code** | — | `Consolas, "Courier New"` | `monospace` |

**Per-role font stacks** (CSS `font-family` strings):

- Title: `Georgia, SimSun, serif`
- Body: `"Microsoft YaHei", "PingFang SC", Arial, sans-serif`
- Emphasis: `Georgia, SimSun, serif`
- Code: `Consolas, "Courier New", monospace`

> **Stack ordering rationale**: Title stack is Latin-led (`Georgia` first) because brand names dominate headline text — Georgia's elegant serifs display English brand names beautifully, while CJK characters fall through to SimSun. Body stack is CJK-led because the main content is in Chinese.

### Font Size Hierarchy

**Baseline**: Body font size = 18px (dense — accommodating 16 brand stories across 16 pages)

| Purpose | Ratio to body | Size | Weight |
| ------- | ------------- | ---- | ------ |
| Cover title | 3.3x | 60px | Bold |
| Brand name heading | 2x | 36px | Bold |
| Page title | 1.7x | 30px | Bold |
| Subtitle | 1.3x | 24px | SemiBold |
| **Body content** | **1x** | **18px** | Regular |
| Brand tag / label | 0.8x | 14px | SemiBold |
| Annotation / caption | 0.7x | 13px | Regular |
| Page number / footnote | 0.6x | 11px | Regular |

---

## V. Layout Principles

### Page Structure

- **Header area**: 40px — 品牌名/欄目標識區，金色細線分割
- **Content area**: 640px — 主內容區，根據品牌數量靈活分配
- **Footer area**: 40px — 頁碼、來源標註

### Layout Pattern Library

本專案以雜誌編輯風格為核心，採用多樣化佈局避免 AI 生成感：

| Pattern | Usage |
| ------- | ----- |
| **Full-bleed + floating text** | 封面頁，品牌圖片鋪滿畫布，標題浮於圖上 |
| **Asymmetric split (3:7 / 4:6)** | 單品牌專題頁，圖片佔主導，文字簡潔 |
| **Figure-text overlap** | 品牌標題疊於圖片邊緣，雜誌排版感 |
| **Two-column magazine** | 雙品牌合併頁，左右各一品牌 |
| **Negative-space-driven** | 呼吸頁，留白突出單一品牌視覺 |
| **Top-bottom split** | 寬幅品牌圖 + 下方文案 |

### Spacing Specification

**Universal**:

| Element | Value |
| ------- | ----- |
| Safe margin | 50px |
| Content block gap | 30px |
| Icon-text gap | 10px |

**Card-based layouts** (where applicable):

| Element | Value |
| ------- | ----- |
| Card gap | 24px |
| Card padding | 24px |
| Card border radius | 12px |

---

## VI. Icon Usage Specification

### Source

- **Built-in icon library**: `phosphor-duotone` — 雙色調風格，層次豐富，時尚現代
- **Brand icons**: `simple-icons` — 品牌 logo 標識（如需展示品牌標誌）
- **Usage method**: SVG placeholder `<use data-icon="library/icon-name" .../>`

### Recommended Icon List

| Purpose | Icon Path | Page |
| ------- | --------- | ---- |
| 時尚/潮流 | `phosphor-duotone/dress` | 封面、多頁 |
| 高階珠寶 | `phosphor-duotone/diamond` | P07 |
| 腕錶 | `phosphor-duotone/watch` | P04 |
| 家居/設計 | `phosphor-duotone/house` | P02, P05 |
| 展覽/藝術 | `phosphor-duotone/palette` | P06, P08 |
| 香氛/美妝 | `phosphor-duotone/flower` | P11 |
| 手袋/配飾 | `phosphor-duotone/handbag` | P10 |
| 活動/明星 | `phosphor-duotone/star` | P12 |
| 聯名/合作 | `phosphor-duotone/handshake` | P13 |
| 剪刀/裁縫 | `phosphor-duotone/scissors` | P09 |
| 商店/零售 | `phosphor-duotone/storefront` | P07 |
| 相機/攝影 | `phosphor-duotone/camera` | P08 |
| 皇冠/奢華 | `phosphor-duotone/crown` | 封面 |
| 閃耀/亮點 | `phosphor-duotone/sparkle` | 多頁 |
| 標籤/品牌 | `phosphor-duotone/tag` | 多頁 |
| 全球/國際 | `phosphor-duotone/globe` | P07 |

---

## VII. Visualization Reference List

```
Catalog read: 40+ templates / 8 categories
Runners-up considered: fewer than 3 viz pages — this is a magazine-style news digest, not a data-driven deck
```

本專案為時尚資訊彙編，內容以品牌敘事和圖片展示為主，不包含資料視覺化需求。所有頁面採用圖文編輯排版，無需引用圖表模板。

---

## VIII. Image Resource List

| Filename | Dimensions | Ratio | Intent | Purpose | Type | Status |
| -------- | ---------- | ----- | ------ | ------- | ---- | ------ |
| cover_hermes.jpg | 1080x997 | 1.08 | Hero / full-bleed | 封面主視覺 | Photography | Existing |
| hermes_home.jpg | 1080x772 | 1.40 | Side-by-side | Hermès 家居世界 | Photography | Existing |
| chanel_coco.jpg | 1080x608 | 1.78 | Hero / full-bleed | CHANEL COCO BEACH | Photography | Existing |
| dior_fashion.jpg | 1080x1080 | 1.00 | Side-by-side | Dior 時裝 | Photography | Existing |
| dior_watch1.jpg | 1080x1080 | 1.00 | Side-by-side | Dior Chiffre Rouge 腕錶 | Photography | Existing |
| lv_objets.jpg | 1080x608 | 1.78 | Hero / full-bleed | LV Objets Nomades | Photography | Existing |
| gucci_memoria1.jpg | 1080x810 | 1.33 | Side-by-side | Gucci Memoria 展覽 | Photography | Existing |
| gucci_memoria2.jpg | 1080x810 | 1.33 | Accent | Gucci 展覽補充 | Photography | Existing |
| vhernier_jewelry.jpg | 1080x720 | 1.50 | Side-by-side | Vhernier 珠寶 | Photography | Existing |
| celine_summer.jpg | 1080x1350 | 0.80 | Side-by-side | CELINE 夏季 | Photography | Existing |
| bv_arts.jpg | 1080x1350 | 0.80 | Side-by-side | BV 藝術攝影 | Photography | Existing |
| mcqueen_exhibition.jpg | 1080x721 | 1.50 | Side-by-side | McQueen 表象之下 | Photography | Existing |
| maxmara_show.jpg | 1080x634 | 1.70 | Hero / full-bleed | Max Mara 首秀 | Photography | Existing |
| chloe_tomato.jpg | 1080x1440 | 0.75 | Side-by-side | Chloé Tomato 座椅 | Photography | Existing |
| tadfab_bag.jpg | 1080x1440 | 0.75 | Side-by-side | TAD FAB 包袋 | Photography | Existing |
| apedemod_fold.jpg | 1080x1619 | 0.67 | Side-by-side | Apede Mod 摺紙 | Photography | Existing |
| boss_fragrance.jpg | 1080x1440 | 0.75 | Side-by-side | BOSS 香氛 | Photography | Existing |
| fresh_event.jpg | 1080x721 | 1.50 | Side-by-side | fresh 釋出會 | Photography | Existing |
| jorya_popup.jpg | 1080x810 | 1.33 | Side-by-side | JORYA 快閃 | Photography | Existing |
| arket_gohar.jpg | 1080x720 | 1.50 | Side-by-side | ARKET 聯名 | Photography | Existing |
| stevemadden_lexie.jpg | 1080x721 | 1.50 | Side-by-side | Steve Madden 代言人 | Photography | Existing |
| crocs_molly.jpg | 1080x608 | 1.78 | Side-by-side | Crocs × MOLLY | Photography | Existing |

---

## IX. Content Outline

### Part 1: 開篇

#### Slide 01 — 封面

- **Layout**: Full-bleed + floating text — cover_hermes.jpg 鋪滿畫布，標題浮於暗色漸變層上
- **Title**: NEWS Café | 美學周鑑
- **Subtitle**: 解鎖潮流序章
- **Info**: 本週時尚熱點 · 2026年4月

### Part 2: 頂級奢侈品牌

#### Slide 02 — Hermès 家居世界

- **Layout**: Asymmetric split (4:6) — 左側文字，右側 hermes_home.jpg
- **Title**: Hermès 家居世界
- **Content**:
  - 米蘭設計周全新家居系列釋出
  - 三十根矩形立柱構築沉浸式佈景
  - 金屬鍛打、皮革鑲嵌、織物雕琢，材質對話與物件敘事
  - 延續匠心工藝與雋永美學

#### Slide 03 — CHANEL COCO BEACH

- **Layout**: Hero / full-bleed — chanel_coco.jpg 作為背景，文字浮於底部漸變層
- **Title**: CHANEL COCO BEACH 2026
- **Content**:
  - 上海市中心限時精品店啟幕
  - 面朝花園的度假別墅概念
  - 田園風光與黑色沙灘靈感
  - Matthieu Blazy 創作的首個 COCO BEACH 系列

#### Slide 04 — Dior：時裝與時計

- **Layout**: Two-column — 左 dior_fashion.jpg，右 dior_watch1.jpg + 文案
- **Title**: Dior 雙面魅力
- **Content**:
  - 左欄：Sabrina Carpenter 身著 Jonathan Anderson 設計禮服亮相 Coachella
  - 右欄：Chiffre Rouge 腕錶系列煥新，三款限量臻品
  - 紅色秒針致敬迪奧心中的生命之色
  - 迪奧先生鍾愛數字"8"化作護身符

#### Slide 05 — Louis Vuitton Objets Nomades

- **Layout**: Hero / full-bleed — lv_objets.jpg 背景 + 浮動文字塊
- **Title**: Louis Vuitton Objets Nomades
- **Content**:
  - 米蘭設計周全新旅行家居系列
  - 致敬 Art Deco 與 Pierre Legrain 大師
  - 坎帕納工作室、Raw Edges、Franck Genser 當代設計師新作
  - Collar 休閒椅、Aqua 餐桌等新品

#### Slide 06 — Gucci Memoria

- **Layout**: Asymmetric split (3:7) — 右 gucci_memoria1.jpg 主導 + 左文案，gucci_memoria2.jpg 作小圖點綴
- **Title**: Gucci Memoria
- **Content**:
  - 米蘭聖辛普利齊亞諾迴廊沉浸式展覽
  - Demna 策劃，追溯品牌 105 年曆程
  - 十二幅掛毯凝練品牌關鍵發展節點
  - Flora 花卉主題花園裝置及專享預售

### Part 3: 高階珠寶與時裝

#### Slide 07 — Vhernier × CELINE

- **Layout**: Two-column magazine — 左 Vhernier (vhernier_jewelry.jpg)，右 CELINE (celine_summer.jpg)
- **Title**: 珠寶新境 · 法式靈韻
- **Content**:
  - 左欄：Vhernier 正式進駐中國內地，北京上海雙店開幕，米蘭純粹設計
  - 右欄：Été CELINE 廣告大片，海濱假日靈感，法式海岸隨性魅力

#### Slide 08 — BV × McQueen：藝術的兩種表達

- **Layout**: Two-column magazine — 左 BV (bv_arts.jpg)，右 McQueen (mcqueen_exhibition.jpg)
- **Title**: 藝術的兩種表達
- **Content**:
  - 左欄：BV "for the Arts" 攝影集，Peter Fraser 鏡頭下的威尼斯，編織美學
  - 右欄：McQueen "表象之下" 上海沉浸式展覽，Manta 手袋復刻 2010 經典

### Part 4: 設計與生活方式

#### Slide 09 — Max Mara × Chloé

- **Layout**: Two-column — 左 Max Mara (maxmara_show.jpg)，右 Chloé (chloe_tomato.jpg)
- **Title**: 傳承新章
- **Content**:
  - 左欄：Max Mara 2027 早春系列上海首秀，"THE MAX!" 75 週年檔案展
  - 右欄：Chloé × Poltronova Tomato 座椅限量復刻，1970 年義大利激進設計運動標誌

#### Slide 10 — TAD FAB × Apede Mod

- **Layout**: Two-column — 左 TAD FAB (tadfab_bag.jpg)，右 Apede Mod (apedemod_fold.jpg)
- **Title**: 結構重塑
- **Content**:
  - 左欄：TAD FAB 全新系列，拉鍊設計語言，環繞拉鍊 Hobo 包，鬆弛精緻格調
  - 右欄：Apede Mod 十週年 PF 2026 摺紙系列，摺疊結構設計進階

### Part 5: 美妝與香氛

#### Slide 11 — BOSS × fresh

- **Layout**: Two-column — 左 BOSS (boss_fragrance.jpg)，右 fresh (fresh_event.jpg)
- **Title**: 感官新篇
- **Content**:
  - 左欄：BOSS 王者之心香氛，清新木質皮革調，雙極香型，王天辰等出席
  - 右欄：fresh 馥蕾詩「酵」你去野新品，CORTIS 全員代言，茶飲文化靈感

### Part 6: 聯名與跨界

#### Slide 12 — JORYA × ARKET

- **Layout**: Two-column — 左 JORYA (jorya_popup.jpg)，右 ARKET (arket_gohar.jpg)
- **Title**: 跨界新風
- **Content**:
  - 左欄：JORYA × YVMIN「公主日記」成都快閃，趙露思亮相，千金輕紗疊穿概念
  - 右欄：ARKET × Laila Gohar 米蘭裝置，十八世紀旋轉木馬改造，27 款聯名單品

#### Slide 13 — Steve Madden × Crocs

- **Layout**: Two-column — 左 Steve Madden (stevemadden_lexie.jpg)，右 Crocs (crocs_molly.jpg)
- **Title**: 潮流共振
- **Content**:
  - 左欄：劉柏辛成為 Steve Madden 中國區代言人，「不趕潮流，踩點登場」
  - 右欄：Crocs × 泡泡瑪特 MOLLY 20 週年聯名，三款洞洞鞋，易夢玲助陣

### Part 7: 收尾

#### Slide 14 — 本週亮點回顧

- **Layout**: Matrix grid — 6 個品牌亮點卡片，每卡一行品牌名 + 一行關鍵詞
- **Title**: 本週亮點一覽
- **Content**:
  - Hermès 家居世界 | CHANEL COCO BEACH | Dior 雙面魅力
  - LV Objets Nomades | Gucci Memoria | McQueen 表象之下
  - 六個精選亮點品牌的微型視覺回顧

#### Slide 15 — 品牌全景

- **Layout**: Three-row layout — 按品類分行展示所有品牌名
- **Title**: 本期品牌全景
- **Content**:
  - 頂奢：Hermès · CHANEL · Dior · Louis Vuitton · Gucci
  - 輕奢/設計師：Vhernier · CELINE · BV · McQueen · Max Mara · Chloé
  - 潮流/生活方式：TAD FAB · Apede Mod · BOSS · fresh · JORYA · ARKET · Steve Madden · Crocs

#### Slide 16 — 結尾

- **Layout**: Negative-space-driven — 極簡結尾，品牌/欄目標識居中
- **Title**: NEWS Café
- **Subtitle**: 下期見 See You Next Week
- **Info**: 美學周鑑，解鎖潮流序章

---

## X. Speaker Notes Requirements

- **File naming**: Match SVG names (e.g., `01_cover.md`)
- **Total duration**: 15-20 minutes（每頁約 1 分鐘）
- **Notes style**: Conversational — 資訊播報式，輕鬆專業
- **Presentation purpose**: Inform — 傳遞本週時尚行業資訊

---

## XI. Technical Constraints Reminder

### SVG Generation Must Follow:

1. viewBox: `0 0 1280 720`
2. Background uses `<rect>` elements
3. Text wrapping uses `<tspan>` (`<foreignObject>` FORBIDDEN)
4. Transparency uses `fill-opacity` / `stroke-opacity`; `rgba()` FORBIDDEN
5. FORBIDDEN: `mask`, `<style>`, `class`, `foreignObject`
6. FORBIDDEN: `textPath`, `animate*`, `script`
7. Text characters: write typography & symbols as raw Unicode; HTML named entities FORBIDDEN. XML reserved chars use `&amp;` `&lt;` `&gt;` `&quot;` `&apos;`
8. `clipPath` conditionally allowed only on `<image>` elements
9. `<g opacity>` FORBIDDEN — set opacity on each child individually
10. Dark theme: all text must use light colors (contrast ratio >= 4.5:1 against #0A0A0A)
