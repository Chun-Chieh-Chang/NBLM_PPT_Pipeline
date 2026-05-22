# 林徽因：重識建築師，而非傳說 - Design Spec

> This document is the human-readable design narrative — rationale, audience, style, color choices, content outline. It is read once by downstream roles for context.
>
> The machine-readable execution contract lives in `spec_lock.md` (short form of color / typography / icon / image decisions). Executor re-reads `spec_lock.md` before every SVG page to resist context-compression drift. Keep the two files in sync; if they diverge, `spec_lock.md` wins.

## I. Project Information

| Item | Value |
| ---- | ----- |
| **Project Name** | 林徽因：重識建築師，而非傳說 |
| **Canvas Format** | PPT 16:9 (1280×720) |
| **Page Count** | 9 |
| **Design Style** | General Versatile (A) |
| **Target Audience** | 建築與人文興趣受眾、文化傳播從業者、講座觀眾 |
| **Use Case** | 紀念專題短講、展陳式內容演示、公眾號內容延展分享 |
| **Created Date** | 2026-04-22 |

---

## II. Canvas Specification

| Property | Value |
| -------- | ----- |
| **Format** | PPT 16:9 |
| **Dimensions** | 1280×720 |
| **viewBox** | `0 0 1280 720` |
| **Margins** | 左右 64px，上下 48px |
| **Content Area** | 1152×624 (64,48 → 1216,672) |

---

## III. Visual Theme

### Theme Style

- **Style**: General Versatile — 博物館展陳感、建築圖志感、編輯化版式
- **Theme**: Light theme（淺底展籤式視覺）
- **Tone**: 剋制、考據、現代，避免“厚重紀念片”套路，強調“重新認識”與“建築專業身份”

### Color Scheme

| Role | HEX | Purpose |
| ---- | --- | ------- |
| **Background** | `#F6F1E8` | 主背景，紙張感米白 |
| **Secondary bg** | `#EFE7DA` | 分割槽底色、卡片淺底 |
| **Primary** | `#A44A3F` | 建築磚紅，主標題、關鍵引導線 |
| **Accent** | `#6E7C80` | 青灰，用於結構線與輔助標籤 |
| **Secondary accent** | `#B6915E` | 金棕，用於強調與頁碼裝飾 |
| **Body text** | `#1F1B16` | 主正文深墨黑 |
| **Secondary text** | `#6A6258` | 圖注、說明、註解 |
| **Tertiary text** | `#978C7E` | 頁尾、輔助資訊 |
| **Border/divider** | `#D8CBB8` | 細分隔線、輪廓線 |
| **Success** | `#4F7A59` | 正向標記 |
| **Warning** | `#B45B4C` | 風險、爭議、歷史張力標記 |

### Gradient Scheme (if needed, using SVG syntax)

```xml
<linearGradient id="titleGradient" x1="0%" y1="0%" x2="100%" y2="0%">
  <stop offset="0%" stop-color="#A44A3F"/>
  <stop offset="100%" stop-color="#B6915E"/>
</linearGradient>

<linearGradient id="paperFade" x1="0%" y1="0%" x2="0%" y2="100%">
  <stop offset="0%" stop-color="#F6F1E8"/>
  <stop offset="100%" stop-color="#EFE7DA"/>
</linearGradient>
```

---

## IV. Typography System

### Font Plan

**Typography direction**: editorial display + modern CJK sans

| Role | Chinese | English | Fallback |
| ---- | ------- | ------- | -------- |
| **Title** | Songti SC | Georgia | SimSun |
| **Body** | PingFang SC | Arial | Microsoft YaHei |
| **Emphasis** | SimHei | Arial | Microsoft YaHei |
| **Code** | - | Consolas | Courier New |

**Per-role font stacks**:
- Title: `Georgia, "Times New Roman", "Songti SC", SimSun, serif`
- Body: `"PingFang SC", "Microsoft YaHei", Arial, sans-serif`
- Emphasis: `"Microsoft YaHei", Arial, sans-serif`
- Code: `Consolas, "Courier New", monospace`

### Font Size Hierarchy

**Baseline**: Body font size = 20px

| Purpose | Ratio to body | 24px baseline (relaxed) | 18px baseline (dense) | Weight |
| ------- | ------------- | ---------------------- | -------------------- | ------ |
| Cover title (hero headline) | 2.5-5x | 60-120px | 45-90px | Bold / Heavy |
| Chapter / section opener | 2-2.5x | 48-60px | 36-45px | Bold |
| Page title | 1.5-2x | 36-48px | 27-36px | Bold |
| Hero number (consulting KPIs) | 1.5-2x | 36-48px | 27-36px | Bold |
| Subtitle | 1.2-1.5x | 29-36px | 22-27px | SemiBold |
| **Body content** | **1x** | **24px** | **18px** | Regular |
| Annotation / caption | 0.7-0.85x | 17-20px | 13-15px | Regular |
| Page number / footnote | 0.5-0.65x | 12-16px | 9-12px | Regular |

**Current project anchors**:
- Cover title: 64px
- Page title: 34px
- Subtitle: 24px
- Body: 20px
- Annotation: 14px
- Page number: 11px

---

## V. Layout Principles

### Page Structure

- **Header area**: 88px，高標題區，含頁碼與章節標識
- **Content area**: 560px，主內容區
- **Footer area**: 24px，來源/頁碼/說明資訊

### Layout Pattern Library (combine or break as content demands)

| Pattern | Suitable Scenarios |
| ------- | ----------------- |
| **Single column centered** | 封面、結尾、核心判斷 |
| **Asymmetric split (4:6 / 5:5)** | 圖文敘事、作品說明 |
| **Three-column cards** | 作品拼圖、貢獻拆解 |
| **Matrix grid (2×2)** | 多圖現場對照 |
| **Z-pattern / waterfall** | 生平與方法論展開 |
| **Figure-text overlap** | 封面、人物頁、紀念碑頁 |
| **Negative-space-driven** | “重新認識”式強調頁 |

### Spacing Specification

**Universal**:

| Element | Recommended Range | Current Project |
| ------- | ---------------- | --------------- |
| Safe margin from canvas edge | 40-60px | 48-64px |
| Content block gap | 24-40px | 28px |
| Icon-text gap | 8-16px | 10px |

**Card-based layouts**:

| Element | Recommended Range | Current Project |
| ------- | ---------------- | --------------- |
| Card gap | 20-32px | 24px |
| Card padding | 20-32px | 22px |
| Card border radius | 8-16px | 14px |
| Single-row card height | 530-600px | 540px |
| Double-row card height | 265-295px each | 268px |
| Three-column card width | 360-380px each | 356px |

**Non-card containers**:

- 用留白和細分隔線，而非大量深色大卡片
- 圖注與正文分層明確，影象邊緣允許與文字輕微疊壓形成編輯感
- breathing 頁避免多卡片並列

---

## VI. Icon Usage Specification

### Source

- **Built-in icon library**: `templates/icons/tabler-outline/`
- **Library**: `tabler-outline`
- **Usage method**: Placeholder format `{{icon:tabler-outline/icon-name}}`

### Recommended Icon List (fill as needed)

| Purpose | Icon Path | Page |
| ------- | --------- | ---- |
| 建築身份 | `{{icon:tabler-outline/building}}` | Slide 01, 03 |
| 紀念性建築 | `{{icon:tabler-outline/building-monument}}` | Slide 05, 09 |
| 校園與教育 | `{{icon:tabler-outline/school}}` | Slide 04, 07 |
| 交通建築 | `{{icon:tabler-outline/train}}` | Slide 03 |
| 測繪與勘察 | `{{icon:tabler-outline/compass}}` | Slide 07, 08 |
| 論文與著述 | `{{icon:tabler-outline/article}}` | Slide 06 |
| 學術出版 | `{{icon:tabler-outline/book-2}}` | Slide 07 |
| 重識/觀看 | `{{icon:tabler-outline/eye}}` | Slide 02 |
| 歷史節點 | `{{icon:tabler-outline/timeline}}` | Slide 03 |
| 先驅/方向 | `{{icon:tabler-outline/flag}}` | Slide 07 |
| 人文溫度 | `{{icon:tabler-outline/heart}}` | Slide 08, 09 |
| 世界眼光 | `{{icon:tabler-outline/globe}}` | Slide 06 |

---

## VII. Visualization Reference List (if needed)

| Visualization Type | Reference Template | Used In |
| ------------------ | ------------------ | ------- |
| timeline | `templates/charts/timeline.svg` | Slide 03 |
| icon_grid | `templates/charts/icon_grid.svg` | Slide 07 |
| vertical_list | `templates/charts/vertical_list.svg` | Slide 06 |

---

## VIII. Image Resource List (if needed)

| Filename | Dimensions | Ratio | Purpose | Type | Status | Generation Description |
| -------- | --------- | ----- | ------- | ---- | ------ | --------------------- |
| lin_portrait.png | 640x703 | 0.91 | 封面人物主視覺 | Photography | Existing | - |
| jihai_station_old.png | 670x346 | 1.94 | 吉海鐵路總站歷史照片 | Photography | Existing | - |
| jihai_station_new.png | 1080x608 | 1.78 | 吉海鐵路總站修復後照片 | Photography | Existing | - |
| pku_geology.png | 745x414 | 1.80 | 北大地質館舊址 | Photography | Existing | - |
| yingqiu_yuan.png | 792x606 | 1.31 | 映秋院歷史照片 | Photography | Existing | - |
| kunming_site.png | 1080x783 | 1.38 | 昆明自宅相關照片 | Photography | Existing | - |
| babaoshan.png | 1080x712 | 1.52 | 八寶山革命公墓 | Photography | Existing | - |
| monument.png | 960x1280 | 0.75 | 人民英雄紀念碑 | Photography | Existing | - |
| lin_tomb.png | 1080x796 | 1.36 | 林徽因墓碑 | Photography | Existing | - |
| first_paper.png | 1080x810 | 1.33 | 首篇建築論文影象 | Photography | Existing | - |
| liang_lin_together.png | 1000x710 | 1.41 | 梁思成與林徽因合影 | Photography | Existing | - |
| lin_survey.png | 1080x1145 | 0.94 | 實地考察古建築照片 | Photography | Existing | - |
| lin_later.png | 640x640 | 1.00 | 晚年肖像 | Photography | Existing | - |

---

## IX. Content Outline

### Part 1: 重新認識她

#### Slide 01 - 封面

- **Layout**: 左側大標題 + 右側豎向人物照片 + 下方展籤式副標題
- **Title**: 林徽因
- **Subtitle**: 重識建築師，而非傳說
- **Content**:
  - 小標題：逝世 70 週年
  - 輔助說明：從作品、理論與行動三個維度，重看她在中國建築史中的位置
- **Image**: lin_portrait.png

#### Slide 02 - 為什麼今天要重識林徽因

- **Layout**: breathing 頁，中央判斷句 + 三個並列觀察維度
- **Title**: 被看見的，常常不是她最重要的部分
- **Content**:
  - 她長期被“才女”“愛情故事”“文學光環”覆蓋
  - 但真正支撐其歷史地位的是建築實踐、理論建構與學科奠基
  - 這份重新認識，不是糾偏趣聞，而是重寫知識座標

### Part 2: 她作為建築師

#### Slide 03 - 建築實踐並不缺席

- **Layout**: 上方橫向時間軸 + 下方三段作品節點
- **Title**: 從墓碑到車站，她的建築實踐有清晰軌跡
- **Visualization**: timeline
- **Content**:
  - 1929 梁啟超墓碑：學成歸國後的起點
  - 1929 石頭樓與吉海鐵路總站：現代性與民族象徵並置
  - 1932—1940 北大、映秋院、西南聯大、昆明自宅：在戰亂中堅持建築理想

#### Slide 04 - 作品現場：建築不是抽象名詞

- **Layout**: 2×2 影象矩陣 + 右側註釋欄
- **Title**: 四個現場，四種建築回應
- **Content**:
  - 吉海鐵路總站：地標性公共建築的象徵表達
  - 北大地質館：現代主義轉向
  - 映秋院：地方材料與民居經驗
  - 昆明自宅：戰時條件下的自我建造
- **Image**: jihai_station_new.png, pku_geology.png, yingqiu_yuan.png, kunming_site.png

#### Slide 05 - 國家尺度上的建築參與

- **Layout**: 左圖右文，紀念碑大圖做視覺錨點
- **Title**: 她的建築工作，最終進入國家記憶
- **Content**:
  - 八寶山革命公墓：主體格局設計
  - 人民英雄紀念碑：提出擴大碑座與雙層臺階的關鍵修改
  - 紋樣與尺度處理體現其對中國傳統建築語彙的理解
  - 她最終也安葬在自己參與設計的空間中
- **Image**: monument.png, babaoshan.png

### Part 3: 她作為理論奠基者

#### Slide 06 - 她不是“輔助者”，而是理論提出者

- **Layout**: 左側論文影象 + 右側縱向要點
- **Title**: 1932 年，她已在定義“中國建築”
- **Visualization**: vertical_list
- **Content**:
  - 《論中國建築之幾個特徵》是中國專業學者首次系統論述中國建築
  - 她反駁了西方知識框架中的誤讀
  - 她提出了中國木構架體系的關鍵特徵
  - 她為之後的中國建築史敘述打下理論骨架
- **Image**: first_paper.png

#### Slide 07 - 學科、方法與遠見

- **Layout**: 三列方法卡片 + 下方補充帶
- **Title**: 她真正留下的，是一套方法
- **Visualization**: icon_grid
- **Content**:
  - 研究方法：測繪、考察、史料與型別分析並重
  - 學科建設：參與東北大學、清華大學建築系建設
  - 理論前瞻：民居保護、現代住宅、普通人居住問題
  - 關鍵詞：建築意、營造則例、住宅概論、民間建築保護
- **Image**: liang_lin_together.png

### Part 4: 她作為行動者

#### Slide 08 - 她如何穿過戰火與病痛

- **Layout**: 左文右圖，非卡片式長段落 + 引語強調
- **Title**: 她不是“被陪伴的人”，她本身就是行動者
- **Content**:
  - 實地考察古建築，翻山涉水並非旁觀
  - 戰亂流亡與長期病痛，沒有中止她的研究和寫作
  - “我還有好多事要做呢”呈現的是職業使命感，而非姿態
  - 她把個人生命壓進了中國建築學的奠基時刻
- **Image**: lin_survey.png, lin_later.png

#### Slide 09 - 結尾

- **Layout**: 單圖紀念式收束 + 中央引文
- **Title**: 墓碑上的七個字，已經足夠準確
- **Subtitle**: 建築師林徽因墓
- **Content**:
  - 重新認識她，不是從傳奇回到八卦，而是從八卦回到專業
  - 她是中國第一代建築學人中的關鍵建構者
  - 她留下的，不只是作品，更是中國如何理解自身建築的一套語言
- **Image**: lin_tomb.png

---

## X. Speaker Notes Requirements

- **File naming**: Match SVG names (e.g., `01_封面.svg` → `notes/01_封面.md`)
- **Total duration**: ~12 minutes
- **Notes style**: 講解型 + 展籤式敘述，剋制、準確、少煽情
- **Presentation purpose**: 糾偏認知 + 建立專業印象
- **Content includes**: 每頁講解要點、頁間過渡、必要的史實強調

---

## XI. Technical Constraints Reminder

### SVG Generation Must Follow:

1. viewBox: `0 0 1280 720`
2. Background uses `<rect>` elements
3. Text wrapping uses `<tspan>` (`<foreignObject>` FORBIDDEN)
4. Transparency uses `fill-opacity` / `stroke-opacity`; `rgba()` FORBIDDEN
5. FORBIDDEN: `mask`, `<style>`, `class`, `foreignObject`
6. FORBIDDEN: `textPath`, `animate*`, `script`
7. Built-in icons use one library only: `tabler-outline`

### PPT Compatibility Rules:

- `<g opacity="...">` FORBIDDEN (group opacity); set on each child element individually
- Image transparency uses overlay mask layer (`<rect fill="bg-color" opacity="0.x"/>`)
- Inline styles only; external CSS and `@font-face` FORBIDDEN
