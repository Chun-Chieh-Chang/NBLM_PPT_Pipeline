# 林徽因：被文學光環遮蔽的建築巨匠 - Design Spec

> This document is the human-readable design narrative — rationale, audience, style, color choices, content outline. It is read once by downstream roles for context.
>
> The machine-readable execution contract lives in `spec_lock.md` (short form of color / typography / icon / image decisions). Executor re-reads `spec_lock.md` before every SVG page to resist context-compression drift. Keep the two files in sync; if they diverge, `spec_lock.md` wins.

## I. Project Information

| Item | Value |
| ---- | ----- |
| **Project Name** | 林徽因：被文學光環遮蔽的建築巨匠 |
| **Canvas Format** | PPT 16:9 (1280×720) |
| **Page Count** | 10 |
| **Design Style** | General Versatile (A) |
| **Target Audience** | 文化愛好者、建築學關注者、歷史人文讀者 |
| **Use Case** | 知識分享、紀念專題、文化傳播 |
| **Created Date** | 2026-04-21 |

---

## II. Canvas Specification

| Property | Value |
| -------- | ----- |
| **Format** | PPT 16:9 |
| **Dimensions** | 1280×720 |
| **viewBox** | `0 0 1280 720` |
| **Margins** | 左右 60px，上下 50px |
| **Content Area** | 1160×620 (60,50 → 1220,670) |

---

## III. Visual Theme

### Theme Style

- **Style**: General Versatile — 圖文並茂、視覺敘事
- **Theme**: Dark theme（深色主題）
- **Tone**: 中式古典建築美學 × 人文紀念感。以深藏青為底、古銅金為魂，營造莊重典雅、跨越時空的歷史感

### Color Scheme

| Role | HEX | Purpose |
| ---- | --- | ------- |
| **Background** | `#1A1A2E` | 深藏青頁面背景，沉穩厚重 |
| **Secondary bg** | `#16213E` | 卡片底色、分割槽背景 |
| **Primary** | `#C9A96E` | 古銅金，標題裝飾、關鍵區塊、圖示 |
| **Accent** | `#E8D5B7` | 暖象牙，高光資料、重點資訊 |
| **Secondary accent** | `#8B6F47` | 深棕色，輔助強調、漸變過渡 |
| **Body text** | `#E8E8E8` | 淺灰白正文文字 |
| **Secondary text** | `#A0A0B0` | 灰色註釋說明 |
| **Tertiary text** | `#6B6B80` | 頁碼、輔助資訊 |
| **Border/divider** | `#2A2A4A` | 卡片邊框、分隔線 |
| **Success** | `#4CAF50` | 正向指標（綠色系） |
| **Warning** | `#E57373` | 問題標記（紅色系） |

### Gradient Scheme

```xml
<!-- 標題漸變（金色系） -->
<linearGradient id="titleGradient" x1="0%" y1="0%" x2="100%" y2="100%">
  <stop offset="0%" stop-color="#C9A96E"/>
  <stop offset="100%" stop-color="#E8D5B7"/>
</linearGradient>

<!-- 背景裝飾光暈 -->
<radialGradient id="bgDecor" cx="80%" cy="20%" r="50%">
  <stop offset="0%" stop-color="#C9A96E" stop-opacity="0.08"/>
  <stop offset="100%" stop-color="#C9A96E" stop-opacity="0"/>
</radialGradient>

<!-- 卡片漸變底色 -->
<linearGradient id="cardGradient" x1="0%" y1="0%" x2="0%" y2="100%">
  <stop offset="0%" stop-color="#16213E"/>
  <stop offset="100%" stop-color="#1A1A2E"/>
</linearGradient>
```

---

## IV. Typography System

### Font Plan

**Recommended preset**: P3 — Culture/Arts/Humanities

| Role | Chinese | English | Fallback |
| ---- | ------- | ------- | -------- |
| **Title** | KaiTi | Georgia | serif |
| **Body** | Microsoft YaHei | Arial | sans-serif |
| **Code** | - | Consolas | Monaco |
| **Emphasis** | SimHei | Arial | sans-serif |

**Font stack**: `"KaiTi", Georgia, serif` (標題) / `"Microsoft YaHei", Arial, sans-serif` (正文)

### Font Size Hierarchy

**Baseline**: Body font size = 22px (內容密度適中)

| Purpose | Ratio | Size | Weight |
| ------- | ----- | ---- | ------ |
| Cover title | 2.5x | 54px | Bold |
| Chapter title | 2x | 44px | Bold |
| Content title | 1.5x | 32px | Bold |
| Subtitle | 1.3x | 28px | SemiBold |
| **Body content** | **1x** | **22px** | Regular |
| Annotation | 0.73x | 16px | Regular |
| Page number/date | 0.55x | 12px | Regular |

---

## V. Layout Principles

### Page Structure

- **Header area**: 高 80px — 頁面標題 + 金色裝飾線
- **Content area**: 高 540px — 主要內容區域
- **Footer area**: 高 40px — 頁碼 + 來源資訊

### Common Layout Modes

| Mode | Suitable Scenarios |
| ---- | ----------------- |
| **Single column centered** | 封面、結尾、關鍵引言 |
| **Left-right split (4:6)** | 圖文混排（圖片+文字說明） |
| **Left-right split (5:5)** | 雙概念對比 |
| **Three-column cards** | 並列要點、作品展示 |
| **Top-bottom split** | 超寬圖片 + 文字 |
| **Timeline** | 人生軌跡、編年概述 |

### Spacing Specification

| Element | Value |
| ------- | ----- |
| Card gap | 24px |
| Content block gap | 32px |
| Card padding | 24px |
| Card border radius | 12px |
| Icon-text gap | 12px |
| Single-row card height | 540px |
| Double-row card height | 260px each |
| Three-column card width | 360px each |

---

## VI. Icon Usage Specification

### Source

- **Built-in icon library**: `templates/icons/chunk/` (直線幾何風格，適配典雅莊重調性)
- **Library**: `chunk`
- **Usage method**: Placeholder format `{{icon:chunk/icon-name}}`

### Recommended Icon List

| Purpose | Icon Path | Page |
| ------- | --------- | ---- |
| 建築/設計 | `{{icon:chunk/building}}` | Slide 03, 04 |
| 古堡/歷史建築 | `{{icon:chunk/castle}}` | Slide 03 |
| 博物館/文化 | `{{icon:chunk/museum}}` | Slide 04 |
| 地圖/考察 | `{{icon:chunk/map}}` | Slide 05 |
| 圓規/製圖 | `{{icon:chunk/compass-drafting}}` | Slide 06 |
| 書籍/學術 | `{{icon:chunk/book-open}}` | Slide 07 |
| 鋼筆/寫作 | `{{icon:chunk/pen-nib}}` | Slide 08 |
| 皇冠/巨匠 | `{{icon:chunk/crown}}` | Slide 01, 10 |
| 星星/成就 | `{{icon:chunk/star}}` | Slide 09 |
| 旗幟/先驅 | `{{icon:chunk/flag}}` | Slide 09 |
| 心/情懷 | `{{icon:chunk/heart}}` | Slide 10 |
| 眼睛/重識 | `{{icon:chunk/eye}}` | Slide 02 |
| 時鐘/時光 | `{{icon:chunk/clock}}` | Slide 02 |
| 全球/影響力 | `{{icon:chunk/globe}}` | Slide 07 |

---

## VII. Visualization Reference List

| Visualization Type | Reference Template | Used In | Purpose |
| ------------------ | ------------------ | ------- | ------- |
| timeline | `templates/charts/timeline.svg` | Slide 02 | 林徽因人生關鍵節點時間軸 |
| icon_grid | `templates/charts/icon_grid.svg` | Slide 03 | 建築作品一覽（多專案卡片） |
| vertical_list | `templates/charts/vertical_list.svg` | Slide 07 | 學術貢獻要點列表 |

---

## VIII. Image Resource List

| Filename | Dimensions | Ratio | Purpose | Type | Status | Generation Description |
| -------- | --------- | ----- | ------- | ---- | ------ | --------------------- |
| cover_bg.png | 1280x720 | 1.78 | 封面背景 | Background | Pending generation | Chinese traditional architectural elements (curved tile rooflines, wooden brackets/dougong) silhouetted against a deep navy-to-midnight blue gradient sky (#1A1A2E to #16213E), golden light (#C9A96E) glowing along the roofline edges, subtle mist/cloud in lower third, clean center area reserved for title text overlay, cinematic atmospheric style |
| lin_portrait.png | 640x703 | 0.91 | 封面人物肖像 | Photography | Existing | - |
| jihai_station_old.png | 670x346 | 1.94 | 吉海鐵路總站歷史照片 | Photography | Existing | - |
| jihai_station_new.png | 1080x608 | 1.78 | 修復後的吉海鐵路總站 | Photography | Existing | - |
| pku_geology.png | 745x414 | 1.80 | 北大地質館舊址 | Photography | Existing | - |
| yingqiu_院.png | 792x606 | 1.31 | 映秋院歷史照片 | Photography | Existing | - |
| kunming_site.png | 1080x783 | 1.38 | 昆明建築工地 | Photography | Existing | - |
| babaoshan.png | 1080x712 | 1.52 | 八寶山革命公墓 | Photography | Existing | - |
| lin_tomb.png | 1080x796 | 1.36 | 林徽因墓碑 | Photography | Existing | - |
| monument.png | 960x1280 | 0.75 | 人民英雄紀念碑 | Photography | Existing | - |
| liang_lin_together.png | 1000x710 | 1.41 | 梁思成與林徽因合影 | Photography | Existing | - |
| first_paper.png | 1080x810 | 1.33 | 首篇建築論文 | Photography | Existing | - |
| lin_survey.png | 1056x1080 | 0.98 | 林徽因考察古建築 | Photography | Existing | - |
| lin_later.png | 857x804 | 1.07 | 林徽因晚年照片 | Photography | Existing | - |

---

## IX. Content Outline

### Part 1: 開篇

#### Slide 01 - 封面

- **Layout**: 全屏背景圖 + 居中豎排標題 + 人物剪影
- **Title**: 林徽因：被文學光環遮蔽的建築巨匠
- **Subtitle**: 逝世70週年 · 重識中國建築史上的女性力量
- **Info**: 鳳凰空間 · 2025
- **Image**: cover_bg.png (全屏底), lin_portrait.png (右側)

#### Slide 02 - 人生軌跡概覽

- **Layout**: 橫向時間軸
- **Title**: 建築巨匠的一生
- **Visualization**: timeline
- **Content**:
  - 1904 出生於杭州
  - 1924 赴美留學賓夕法尼亞大學
  - 1928 與梁思成結婚，歸國
  - 1930 加入中國營造學社
  - 1932 發表首篇建築論文
  - 1937-1946 戰時流亡，堅持研究
  - 1949 參與國徽設計
  - 1952 參與人民英雄紀念碑設計
  - 1955 逝世，墓碑刻"建築師林徽因墓"

### Part 2: 建築師林徽因

#### Slide 03 - 為數不多的建築作品（上）

- **Layout**: 三列卡片佈局
- **Title**: 歸國初期的建築實踐
- **Visualization**: icon_grid
- **Content**:
  - 1929 梁啟超墓碑設計 — 學成歸來第一件作品
  - 1929 吉林大學石頭樓 — 參與"梁陳童蔡營造事務所"設計
  - 1929 吉海鐵路總站 — 林徽因設計總體風貌，哥特式雄獅造型

#### Slide 04 - 為數不多的建築作品（下）

- **Layout**: 左右分欄（4:6），左圖右文
- **Title**: 戰火中的建築理想
- **Content**:
  - 1932 北大地質館與女生宿舍 — 中國最早引入西方現代主義建築
  - 1938 雲南大學映秋院 — 融合雲南民間建築元素
  - 1938 西南聯大校舍 — "一生中最痛苦、最委屈的設計"
  - 1940 昆明自宅 — 兩位建築師一生唯一為自己設計的房子
- **Image**: kunming_site.png

#### Slide 05 - 豐碑之作

- **Layout**: 左右分欄（5:5），左文右圖
- **Title**: 國之重器上的建築印記
- **Content**:
  - 1950 八寶山革命公墓 — 主體建築格局設計
  - 1952 人民英雄紀念碑 — 提出創造性修改方案
  - 親自設計碑座全套飾紋與花環浮雕
  - 以唐代風格為藍本，展現中國傳統建築美學
  - 墓碑上只有七個字：建築師林徽因墓
- **Image**: monument.png

### Part 3: 被低估的學術先驅

#### Slide 06 - 中國建築理論的奠基者

- **Layout**: 左右分欄（4:6），左圖右文
- **Title**: 首篇建築論文：技驚四座
- **Content**:
  - 1932《論中國建築之幾個特徵》— 首次由中國專業學者發表的建築理論文章
  - 首次在理論上定義了中國建築木框架結構體系的基本特徵
  - 反駁西方學者對中國建築的誤讀
  - 描繪出關於中國建築史的完整概念框架
- **Image**: first_paper.png

#### Slide 07 - 獨創概念與超前思想

- **Layout**: 縱向要點列表
- **Title**: 學術貢獻一覽
- **Visualization**: vertical_list
- **Content**:
  - "建築意"概念 — 原創性的中國建築美學理念，建築是技術、美、歷史與人情的凝聚
  - 《清式營造則例》緒論 — 歸納中國建築理論框架
  - 民居研究先驅 — 在中國建築界率先提出保護民間建築
  - 《現代住宅設計的參考》 — 遠見性地提出戰後為普通人設計建築
  - 首開"住宅概論"課 — 1949年清華大學首次系統教授現代住宅設計理論

### Part 4: 強者與精神

#### Slide 08 - 遠比傳聞更震撼的一生

- **Layout**: 左右分欄（5:5），左文右圖
- **Title**: 穿越戰火的建築鬥士
- **Content**:
  - 荒郊野谷考察古建築，風餐露宿不退縮
  - "只要梁先生敢爬敢上的，林先生就敢上"
  - 戰亂流亡中肺炎發作，此後再未恢復健康
  - 帶病堅持在偏遠小鎮一筆一筆書寫中國建築史
  - "什麼美人不美人，我還有好多事要做呢！"
- **Image**: lin_survey.png

#### Slide 09 - 她想要終生奮鬥的事業

- **Layout**: 引言卡片 + 成就總結
- **Title**: 當之無愧的建築師
- **Content**:
  - 引言："我自己也到了相當年紀，也沒有什麼成就…我禁不住傷心起來" — 28歲寫給胡適的信
  - 與梁思成共同創辦東北大學、清華大學建築系
  - 深入荒涼之地一寸寸測量古建築
  - 在國徽和紀念碑上傾注最後心血
  - 她是學科的奠基者，更是思想上的先行者

#### Slide 10 - 結尾

- **Layout**: 單列居中，引言式
- **Title**: 建築師林徽因墓
- **Subtitle**: 她用一生證明，她是當之無愧的建築師
- **Content**:
  - 中央金色豎線裝飾
  - 墓碑銘文引用
  - 致敬語
  - 來源資訊

---

## X. Speaker Notes Requirements

- **File naming**: Match SVG names (e.g., `01_cover.svg` → `notes/01_cover.md`)
- **Total duration**: ~15 minutes
- **Notes style**: 敘述型（Narrative），兼具歷史厚重感與人文溫度
- **Presentation purpose**: Inspire + Inform（致敬與知識傳遞）
- **Content includes**: 每頁演講要點、補充歷史細節、過渡銜接語

---

## XI. Technical Constraints Reminder

### SVG Generation Must Follow:

1. viewBox: `0 0 1280 720`
2. Background uses `<rect>` elements
3. Text wrapping uses `<tspan>` (`<foreignObject>` FORBIDDEN)
4. Transparency uses `fill-opacity` / `stroke-opacity`; `rgba()` FORBIDDEN
5. FORBIDDEN: `mask`, `<style>`, `class`, `foreignObject`
6. FORBIDDEN: `textPath`, `animate*`, `script`
7. `marker-start` / `marker-end` conditionally allowed: `<marker>` must be in `<defs>`, `orient="auto"`, shape must be triangle / diamond / circle

### PPT Compatibility Rules:

- `<g opacity="...">` FORBIDDEN (group opacity); set on each child element individually
- Image transparency uses overlay mask layer (`<rect fill="bg-color" opacity="0.x"/>`)
- Inline styles only; external CSS and `@font-face` FORBIDDEN
