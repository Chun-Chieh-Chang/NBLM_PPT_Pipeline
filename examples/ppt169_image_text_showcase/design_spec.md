# Image-Text Showcase — Design Spec

> Human-readable design narrative. Machine-readable contract: `spec_lock.md`. On divergence, `spec_lock.md` wins.

## I. Project Information

| Item | Value |
| ---- | ----- |
| **Project Name** | Image-Text Showcase |
| **Canvas Format** | PPT 16:9 (1280×720) |
| **Page Count** | 20 |
| **Design Style** | A) General Versatile + editorial-showcase |
| **Target Audience** | 設計師、PPT製作者、AI工具使用者 |
| **Use Case** | 圖文結合能力展示 / 視覺樣例集 |
| **Created Date** | 2026-05-15 |

---

## II. Canvas Specification

| Property | Value |
| -------- | ----- |
| **Format** | PPT 16:9 |
| **Dimensions** | 1280×720 |
| **viewBox** | `0 0 1280 720` |
| **Margins** | left/right 60px, top/bottom 50px |
| **Content Area** | 1160×620 (x=60, y=50) |

---

## III. Visual Theme

### Theme Style

- **Style**: A) General Versatile + editorial-showcase
- **Theme**: 每頁獨立主題（dark/light 隨各頁 rendering 而異）
- **Tone**: 多元視覺語言並置；每頁是一個獨立的視覺風格樣本

### Color Scheme

> 每頁顏色服從該頁 rendering × palette 組合，以下為 SVG 結構色（非影象色）

| Role | HEX | Purpose |
| ---- | --- | ------- |
| **Background** | `#0F1117` | 預設深底（各頁可覆蓋） |
| **Secondary bg** | `#1A1D2E` | 卡片/區塊底色 |
| **Primary** | `#7C6FF7` | 主調紫藍 |
| **Accent** | `#F5A623` | 金橙強調 |
| **Secondary accent** | `#4ECDC4` | 青綠對比 |
| **Body text** | `#E8E8F0` | 正文淺灰白 |
| **Secondary text** | `#9090A0` | 說明文字 |
| **Tertiary text** | `#5A5A72` | 頁碼/補充 |
| **Border/divider** | `#2A2D3E` | 邊框分割線 |
| **Success** | `#4CAF50` | 正向指標 |
| **Warning** | `#EF5350` | 警示標記 |

### AI Image Strategy

每頁影象獨立指定 rendering × palette（見 §VIII 及 §IX），非統一鎖定。

---

## IV. Typography System

**Typography direction**: contrast — serif title × sans body

| Role | Chinese | English | Fallback tail |
| ---- | ------- | ------- | ------------- |
| **Title** | `"Microsoft YaHei"` | `Georgia` | `serif` |
| **Body** | `"Microsoft YaHei", "PingFang SC"` | `Arial` | `sans-serif` |
| **Emphasis** | `"Microsoft YaHei"` | `Georgia` | `serif` |
| **Code** | — | `Consolas, "Courier New"` | `monospace` |

**Per-role font stacks**:
- Title: `Georgia, "Microsoft YaHei", serif`
- Body: `Arial, "Microsoft YaHei", "PingFang SC", sans-serif`
- Emphasis: `Georgia, "Microsoft YaHei", serif`
- Code: `Consolas, "Courier New", monospace`

**Baseline**: Body = 20px

| Purpose | Ratio | @ 20px |
| ------- | ----- | ------ |
| Cover title | 3-5x | 60-100px |
| Chapter opener | 2-2.5x | 40-50px |
| Page title | 1.5-2x | 30-40px |
| Subtitle | 1.2-1.5x | 24-30px |
| **Body** | **1x** | **20px** |
| Annotation | 0.7-0.85x | 14-17px |
| Page number | 0.5-0.65x | 10-13px |

---

## V. Layout Principles

### Page Structure

- **Header area**: y=0~80px，頁面標題或留白
- **Content area**: y=80~670px，主內容區
- **Footer area**: y=670~720px，頁碼/標註

### Layout Pattern Library

本專案每頁使用不同佈局，詳見 §IX Content Outline。

### Spacing Specification

| Element | Value |
| ------- | ----- |
| Safe margin | 60px (left/right), 50px (top/bottom) |
| Content block gap | 32px |
| Card gap | 24px |
| Card padding | 28px |
| Card border radius | 12px |

---

## VI. Icon Usage Specification

**Library**: `tabler-outline`, stroke-width `2`

| Purpose | Icon Path | Page |
| ------- | --------- | ---- |
| 圖文結合 | `tabler-outline/layout-collage` | P02 目錄 |
| 全出血佈局 | `tabler-outline/frame` | P02 目錄 |
| 左右分欄 | `tabler-outline/layout-columns` | P02 目錄 |
| 圖文疊壓 | `tabler-outline/layers-intersect` | P02 目錄 |
| 卡片網格 | `tabler-outline/layout-grid` | P02 目錄 |
| 圖片 | `tabler-outline/photo` | P02 目錄 |
| 調色盤 | `tabler-outline/palette` | P02 目錄 |
| 畫板 | `tabler-outline/artboard` | P02 目錄 |

---

## VII. Visualization Reference List

Catalog read: 71 templates

本專案以圖文佈局展示為主，無資料圖表頁，不使用 charts 模板庫。

No-template-match: all pages use custom layouts designed to demonstrate image-text composition patterns.

---

## VIII. Image Resource List

每頁一張AI圖，rendering × palette 各頁獨立。

| Filename | Dimensions | Ratio | Purpose | Type | Acquire Via | Status | Reference | text_policy | page_role |
| -------- | ---------- | ----- | ------- | ---- | ----------- | ------ | --------- | ----------- | --------- |
| p01_cover.png | 1280×720 | 1.78 | 封面全出血背景 | Background | ai | Pending | Futuristic frosted glass panels layered over deep space; calm center reserved for title overlay; subtle light refractions at edges | none | hero_page |
| p03_left_img.png | 427×620 | 0.69 | 左1/3豎版圖 | Photography | ai | Pending | Professional editorial portrait: diverse creative team collaborating, modern studio, natural sidelighting, shallow depth of field | none | local |
| p04_right_img.png | 800×720 | 1.11 | 右側出血大圖 | Illustration | ai | Pending | Bold flat vector composition: abstract geometric cityscape with sharp color blocks; right edge bleeds off canvas | none | local |
| p05_top_img.png | 1280×320 | 4.0 | 頂部全幅橫圖 | Background | ai | Pending | Soft watercolor wash: mountain lake at dawn, wide panoramic, muted pastel reflections, top-heavy composition leaving bottom clear | none | local |
| p06_bottom_img.png | 1280×360 | 3.56 | 底部全幅圖 | Illustration | ai | Pending | Hand-drawn sketch: cozy reading corner, warm pencil lines, pastel color fills, bottom-weighted scene with open sky at top | none | local |
| p07_z_img1.png | 560×200 | 2.8 | Z型第一段圖 | Illustration | ai | Pending | Isometric 3D tech object: server rack or CPU chip, clean shadows, top-left anchor composition | none | local |
| p07_z_img2.png | 560×200 | 2.8 | Z型第三段圖 | Illustration | ai | Pending | Isometric 3D network diagram: connected nodes and cables, same isometric angle as img1 | none | local |
| p08_grid_center.png | 400×400 | 1.0 | 九宮格中心圖 | Illustration | ai | Pending | Blueprint-style technical schematic: circuit board with grid lines, monospace annotations, monochrome blue-on-dark | none | local |
| p09_circle_img.png | 400×400 | 1.0 | 圓形中心圖 | Illustration | ai | Pending | Digital dashboard interface fragment: glowing circular gauge, data rings, dark background, high-tech UI aesthetic | none | local |
| p10_bg_texture.png | 1280×720 | 1.78 | 全幅底紋背景 | Background | ai | Pending | Pixel art cityscape at night: 8-bit buildings and neon signs tiled across the full canvas, vibrant saturated colors | none | hero_page |
| p11_papercut.png | 1280×720 | 1.78 | 剪紙分層背景 | Illustration | ai | Pending | Layered paper-cut landscape: 4 depth layers of mountains and trees, each layer a different green-earth tone, soft cast shadows | none | hero_page |
| p12_poster_img.png | 256×720 | 0.36 | 豎版雜誌窄圖 | Illustration | ai | Pending | Mid-century vintage poster fragment: bold geometric shapes, halftone texture, limited 3-color palette, vertical composition | none | local |
| p13_diagonal_img.png | 700×420 | 1.67 | 對角線上半圖 | Illustration | ai | Pending | Fantasy animation style: dreamy forest scene with soft glowing particles, warm amber light filtering through canopy, Ghibli-inspired atmosphere | none | local |
| p14_fade_bg.png | 1280×720 | 1.78 | 褪色底圖 | Background | ai | Pending | Ink wash painting: abstract brushstrokes suggesting mountains and mist, desaturated earthy tones, large central negative space | none | hero_page |
| p15_bottom_img.png | 1280×360 | 3.56 | 下半幅圖 | Illustration | ai | Pending | Flat design scene: modern office workspace seen from above, geometric furniture shapes, jewel-tone color palette, clean isometric-free flat view | none | local |
| p16_center_img.png | 480×480 | 1.0 | 中心圓形圖 | Illustration | ai | Pending | Minimalist swiss-style graphic: single bold geometric form (circle or square) centered on white field, aggressive negative space, Helvetica-era precision | none | local |
| p17_strip_img.png | 1280×240 | 5.33 | 橫貫中部窄條圖 | Illustration | ai | Pending | Screen-print style banner: bold halftone pattern, limited 2-color duotone treatment, horizontal rhythm of repeated graphic motifs | none | local |
| p18_polygon_img.png | 600×500 | 1.2 | 不規則多邊形圖 | Illustration | ai | Pending | Organic nature illustration: lush tropical leaves and botanical elements arranged in a loose hexagonal cluster, earthy warm greens | none | local |
| p19_collage1.png | 380×320 | 1.19 | 蒙太奇圖1 | Photography | ai | Pending | Editorial magazine photo: urban architecture detail, dramatic shadow play, high contrast, cropped unconventionally | none | local |
| p19_collage2.png | 380×320 | 1.19 | 蒙太奇圖2 | Photography | ai | Pending | Editorial magazine photo: close-up texture surface — fabric or concrete, abstract pattern, monochromatic | none | local |
| p19_collage3.png | 460×320 | 1.44 | 蒙太奇圖3（寬） | Photography | ai | Pending | Editorial magazine photo: motion blur street scene, long exposure light trails, cool blue atmosphere | none | local |
| p20_closing.png | 1280×720 | 1.78 | 結尾背景 | Background | ai | Pending | Chalk drawing on blackboard: simple constellation of dots and hand-drawn lines forming a subtle geometric pattern, warm white chalk marks on dark green surface | none | hero_page |

---

## IX. Content Outline

### Part 1: 封面與導航

#### Slide 01 — 封面

- **Layout**: 全出血背景圖 + 居中懸浮標題塊
- **Rendering × Palette**: `glassmorphism` × `dark-cinematic`
- **Image**: p01_cover.png (hero_page，全出血)
- **Title**: 圖文結合
- **Subtitle**: 20種視覺語言的並置實驗
- **Info**: PPT Master · 2026

#### Slide 02 — 目錄

- **Layout**: 左側深色色塊 + 右側編號列表（無圖）
- **Rendering × Palette**: 無圖，使用專案主配色
- **Content**: 列出20頁風格速覽，每條一行

### Part 2: 圖文組合樣本

#### Slide 03 — 左1/3豎圖 + 右文字主體

- **Layout**: 左側豎版圖 width=427px，右側文字區 width=733px
- **Rendering × Palette**: `corporate-photo` × `cool-corporate`
- **Image**: p03_left_img.png
- **Title**: 編輯攝影 × 專業藍
- **Content**: 豎版人物圖左置，文字在右大面積展開；圖文比例約3:7，適合以文字為主的敘述型頁面

#### Slide 04 — 右圖左文，圖出血至右邊緣

- **Layout**: 左側文字區 width=440px，右側圖出血至邊緣 width=840px
- **Rendering × Palette**: `vector-illustration` × `frost-ice`
- **Image**: p04_right_img.png
- **Title**: 向量插畫 × 冰霜白
- **Content**: 扁平向量圖佔據右側並出血，文字在左浮動；大圖小字製造張力

#### Slide 05 — 頂部全幅圖 + 底部三欄文字

- **Layout**: 上半 height=360px 全幅圖，下半 height=310px 三欄等寬文字
- **Rendering × Palette**: `watercolor` × `warm-earth`
- **Image**: p05_top_img.png
- **Title**: 水彩渲染 × 暖土色
- **Content**: 寬幅水彩圖壓頂，下方三欄簡短文字如圖注般排列

#### Slide 06 — 底部全幅圖 + 頂部標題 + 中段文字

- **Layout**: 頂部 height=120px 標題區，中段 height=200px 文字，底部 height=360px 全幅圖
- **Rendering × Palette**: `sketch-notes` × `macaron`
- **Image**: p06_bottom_img.png
- **Title**: 手繪速寫 × 馬卡龍
- **Content**: 圖在底部如舞臺佈景，文字浮於上方；溫暖手繪感

#### Slide 07 — Z型圖文交替三段蛇形

- **Layout**: 三行交替：圖左文右 → 文左圖右 → 圖左文右，每段 height≈190px
- **Rendering × Palette**: `3d-isometric` × `tech-neon`
- **Image**: p07_z_img1.png, p07_z_img2.png
- **Title**: 等距3D × 霓虹科技
- **Content**: Z型視線引導；兩張等距3D圖與三段文字交織排列

#### Slide 08 — 九宮格圖文混排網格

- **Layout**: 3×3 grid，中心格放圖，其餘8格放文字/色塊
- **Rendering × Palette**: `blueprint` × `editorial-classic`
- **Image**: p08_grid_center.png
- **Title**: 藍圖技術 × 編輯經典
- **Content**: 電路板圖居中，周圍8格填充標題、說明、標註等文字元素

#### Slide 09 — 圓形影象居中 + 四角文字放射

- **Layout**: 圓形裁切圖居中 diameter=380px，四個角落各一文字塊
- **Rendering × Palette**: `digital-dashboard` × `mono-ink`
- **Image**: p09_circle_img.png (clipPath圓形裁切)
- **Title**: 數字儀表 × 墨黑單色
- **Content**: 高科技儀表盤影象圓形展示，四角文字如標註向外發散

#### Slide 10 — 圖作全幅底紋 + 文字資訊密鋪

- **Layout**: 圖全幅平鋪為背景，深色遮罩overlay，文字分四區域密鋪
- **Rendering × Palette**: `pixel-art` × `vivid-launch`
- **Image**: p10_bg_texture.png (hero_page)
- **Title**: 畫素復古 × 活力發射
- **Content**: 8-bit畫素背景上鋪設四塊資訊卡片，霓虹文字與畫素感呼應

#### Slide 11 — 剪紙分層疊疊 + 文字嵌入各層

- **Layout**: 圖全出血為剪紙背景，文字塊嵌入各剪紙層之間
- **Rendering × Palette**: `paper-cut` × `nature-organic`
- **Image**: p11_papercut.png (hero_page)
- **Title**: 剪紙藝術 × 自然有機
- **Content**: 多層剪紙山景，文字分佈於不同景深層，模擬紙層嵌字

#### Slide 12 — 豎版雜誌：窄圖佔左20% + 大標題橫排

- **Layout**: 左側豎條圖 width=256px，右側大標題 + 正文佔餘下1024px
- **Rendering × Palette**: `vintage-poster` × `duotone`
- **Image**: p12_poster_img.png
- **Title**: 復古海報 × 雙色調
- **Content**: 窄豎圖如書脊般立於左緣，右側大號字排版如雜誌封面

#### Slide 13 — 對角線分割：左上圖，右下文

- **Layout**: 對角線切割，左上三角區域放圖，右下三角區域放文字
- **Rendering × Palette**: `fantasy-animation` × `sunset-gradient`
- **Image**: p13_diagonal_img.png
- **Title**: 奇幻動畫 × 落日漸變
- **Content**: 吉卜力風森林圖佔左上，文字在右下三角內排列；對角張力

#### Slide 14 — 圖片褪色為底色 + 大字疊壓

- **Layout**: 圖全出血低飽和度處理，大字（font-size≈80px）直接疊壓其上
- **Rendering × Palette**: `ink-notes` × `earthy-dusty`
- **Image**: p14_fade_bg.png (hero_page，低飽和底圖)
- **Title**: 水墨筆記 × 塵土大地
- **Content**: 水墨山水褪為底色，單行超大字疊壓；圖為紋理，字為主角

#### Slide 15 — 上下各半：上段文字，下段圖

- **Layout**: 上半 height=340px 文字區，下半 height=340px 全幅圖（有細分割線）
- **Rendering × Palette**: `flat` × `jewel-tone`
- **Image**: p15_bottom_img.png
- **Title**: 扁平設計 × 寶石色調
- **Content**: 上方大標題+正文，下方扁平俯檢視；圖文各佔半幅，對等對話

#### Slide 16 — 中心大圖 + 環繞一圈文字標註

- **Layout**: 正方形圖居中 size=480×480，周圍六個方向標註文字帶指示線
- **Rendering × Palette**: `minimalist-swiss` × `editorial-classic`
- **Image**: p16_center_img.png
- **Title**: 極簡瑞士 × 編輯經典
- **Content**: 包豪斯感極簡圖形居中，六條標註線向外輻射，文字像產品圖解

#### Slide 17 — 窄條圖片橫貫中部 + 上下各一段文字

- **Layout**: 頂部文字區 height=200px，中部圖條 height=240px，底部文字區 height=240px
- **Rendering × Palette**: `screen-print` × `vivid-launch`
- **Image**: p17_strip_img.png
- **Title**: 網版印刷 × 活力發射
- **Content**: 絲網印刷風橫條圖貫穿頁面中腰，上下文字各成一節，圖將文切開

#### Slide 18 — 不規則多邊形影象 + 文字填縫

- **Layout**: 六邊形裁切圖 (clipPath polygon) 居左偏，文字塊填入右側和角落空隙
- **Rendering × Palette**: `nature` × `sunset-gradient`
- **Image**: p18_polygon_img.png (clipPath六邊形裁切)
- **Title**: 自然插畫 × 落日漸變
- **Content**: 熱帶植物圖以六邊形呈現，文字在圖形外圍和角落自由填充

#### Slide 19 — 多圖拼貼蒙太奇 + 大字壓跨多圖

- **Layout**: 三張圖拼接平鋪全幅，大號文字（font-size≈72px）橫跨多圖之上
- **Rendering × Palette**: `editorial` × `dark-cinematic`
- **Image**: p19_collage1.png, p19_collage2.png, p19_collage3.png
- **Title**: 雜誌編輯 × 暗黑影院
- **Content**: 三張編輯攝影拼貼鋪滿頁面，超大標題字橫壓其上；蒙太奇敘事

#### Slide 20 — 結尾：暗底反白 + 單句居中收場

- **Layout**: 圖全出血黑板背景，單行文字絕對居中，頁面留白≥60%
- **Rendering × Palette**: `chalkboard` × `mono-ink`
- **Image**: p20_closing.png (hero_page)
- **Title**: 黑板粉筆 × 墨黑單色
- **Content**: 黑板星座底圖，正中一句話收尾；負空間即內容

---

## X. Speaker Notes Requirements

- 檔案命名與SVG對應：`01_cover.md` ↔ `01_cover.svg`
- 演講時長：約15分鐘
- 備註風格：簡潔說明，指出每頁圖文結合要點
- 演示目的：展示（showcase）

---

## XI. Technical Constraints Reminder

1. viewBox: `0 0 1280 720`
2. 背景用 `<rect>`
3. 文字換行用 `<tspan>`，禁止 `<foreignObject>`
4. 透明度用 `fill-opacity` / `stop-opacity`，禁止 `rgba()`
5. 禁止：`mask`, `<style>`, `class`, `foreignObject`, `textPath`, `animate*`, `script`
6. 文字元號寫原始 Unicode，禁止 HTML 實體（&nbsp; &mdash; 等）
7. `clipPath` 僅用於 `<image>` 裁切（P09圓形、P18六邊形）
8. 圖示使用 `<use data-icon="tabler-outline/xxx"/>` 佔位符
