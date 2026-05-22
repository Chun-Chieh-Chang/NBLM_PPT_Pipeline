# 裁雲織月 草木成詩 — Design Spec

> 本文件為人類可讀的設計敘事 — 包含設計動機、受眾、風格、色彩選擇與內容大綱。由下游角色（Executor）一次性讀取以獲得語境。
>
> 機器可讀執行契約存放在 `spec_lock.md`（色彩 / 字型 / 圖示 / 圖片決策的簡化短表）。Executor 在生成每一頁 SVG 之前會重新讀取 `spec_lock.md` 以抵抗長文件語境漂移。兩份檔案須保持同步，若出現衝突以 `spec_lock.md` 為準。

## I. Project Information

| Item | Value |
| ---- | ----- |
| **Project Name** | liziqi-plant-dye-colors |
| **Canvas Format** | PPT 16:9 (1280×720) |
| **Page Count** | 12 |
| **Design Style** | A) General Versatile — 東方文化敘事風 |
| **Target Audience** | 文化愛好者、設計師、傳統美學學習者、博物館/教育工作者 |
| **Use Case** | 文化分享會 / 設計師講座 / 博物館講解 / 美學課程 |
| **Created Date** | 2026-04-21 |

---

## II. Canvas Specification

| Property | Value |
| -------- | ----- |
| **Format** | PPT 16:9 |
| **Dimensions** | 1280×720 |
| **viewBox** | `0 0 1280 720` |
| **Margins** | 左右 60px，上下 50px |
| **Content Area** | 1160×620 |

---

## III. Visual Theme

### Theme Style

- **Style**: 東方植物染美學 · 文化敘事
- **Theme**: 淺色（宣紙米白底）
- **Tone**: 典雅 · 含蓄 · 詩意 · 溫潤 · 手作溫度

### Color Scheme（取自文章中真實存在的傳統色譜）

| Role | HEX | Purpose |
| ---- | --- | ------- |
| **Background (宣紙白)** | `#F7F2E8` | 頁面主背景，仿宣紙質感 |
| **Secondary bg (月白)** | `#EDE5D3` | 卡片/章節底/次級區域 |
| **Primary (雨過天青)** | `#6B9AAE` | 主視覺、章節主色、裝飾線 |
| **Accent (黃櫨黃)** | `#C99E62` | 副標題、強調色、副主視覺 |
| **Secondary accent (馬蘭青)** | `#6F8F75` | 漸變過渡、次要強調 |
| **Accent 2 (酡紅)** | `#B04A5C` | 關鍵字、重點高亮（剋制使用） |
| **Body text (茶墨)** | `#3A3530` | 正文主色 |
| **Secondary text (暮雲灰)** | `#7A7068` | 註釋、副文、引文 |
| **Tertiary text (淡墨)** | `#9B948B` | 頁尾、元資訊 |
| **Border/divider (淡米灰)** | `#D7CEB9` | 分隔線、描邊、卡片邊 |

### Gradient Scheme（使用 SVG 語法，無 rgba）

```xml
<!-- 戰袍吊染漸變：黃櫨 → 馬蘭青 -->
<linearGradient id="diaoyanGradient" x1="0%" y1="0%" x2="0%" y2="100%">
  <stop offset="0%" stop-color="#C99E62"/>
  <stop offset="100%" stop-color="#6F8F75"/>
</linearGradient>

<!-- 章節扉頁雨過天青漸變 -->
<linearGradient id="titleGradient" x1="0%" y1="0%" x2="100%" y2="0%">
  <stop offset="0%" stop-color="#6B9AAE"/>
  <stop offset="100%" stop-color="#6F8F75"/>
</linearGradient>

<!-- 背景裝飾（雨過天青暈染） -->
<radialGradient id="bgDecor" cx="85%" cy="15%" r="55%">
  <stop offset="0%" stop-color="#6B9AAE" stop-opacity="0.10"/>
  <stop offset="100%" stop-color="#6B9AAE" stop-opacity="0"/>
</radialGradient>
```

---

## IV. Typography System

### Font Plan

**Recommended preset**: P3（文化/藝術）

| Role | Chinese | English | Fallback |
| ---- | ------- | ------- | -------- |
| **Title** | KaiTi / STKaiti | Georgia | serif |
| **Body** | Microsoft YaHei / PingFang SC | Arial | sans-serif |
| **Code** | - | Consolas | Monaco |
| **Emphasis (引文/色名)** | KaiTi | Georgia | serif |

**Font stack**: `"KaiTi", "STKaiti", "Microsoft YaHei", "PingFang SC", Georgia, serif`

### Font Size Hierarchy

**Baseline**: Body font size = **22px**（中等密度，利於閱讀古典長句）

| Purpose | Ratio | Size | Weight |
| ------- | ----- | ---- | ------ |
| Cover title | 3x | 66px | Bold |
| Chapter title | 2.3x | 50px | Bold |
| Content title | 1.6x | 36px | Bold |
| Subtitle | 1.2x | 26px | SemiBold |
| **Body content** | **1x** | **22px** | Regular |
| Annotation | 0.8x | 18px | Regular |
| Page number/date | 0.6x | 13px | Regular |

---

## V. Layout Principles

### Page Structure

- **Header area**: 高 72px（頁碼 + 章節線 + 小裝飾印章）
- **Content area**: 高 580px（主視覺區）
- **Footer area**: 高 40px（頁尾 / 專案名 / 分隔線）

### Common Layout Modes

| Mode | 使用頁 |
| ---- | ------ |
| **Single column centered** | 封面、引子、結語 |
| **Left-right split (5:5)** | 兩色並列對照頁 |
| **Left-right split (4:6)** | 圖文混排（圖左文右） |
| **Top-bottom split** | 歷史時間線、流程頁 |
| **Four column cards** | 染料植物分類 |

### Spacing Specification

| Element | Value |
| ------- | ----- |
| Card gap | 28px |
| Content block gap | 36px |
| Card padding | 26px |
| Card border radius | 12px |
| Icon-text gap | 12px |
| Single-row card height | 540px |
| Double-row card height | 275px each |

---

## VI. Icon Usage Specification

### Source

- **Library**: `tabler-filled`（貝塞爾曲線圓潤風格，契合植物/自然/東方美學）
- **Usage method**: `{{icon:tabler-filled/<name>}}`

### Recommended Icon List

| Purpose | Icon Path | Page |
| ------- | --------- | ---- |
| 植物/葉 | `{{icon:tabler-filled/leaf}}` | 03, 09, 10 |
| 花朵 | `{{icon:tabler-filled/flower}}` | 09, 11 |
| 水滴/染料 | `{{icon:tabler-filled/droplet}}` | 03, 10 |
| 調色盤 | `{{icon:tabler-filled/palette}}` | 05, 06, 07, 08 |
| 書籍 | `{{icon:tabler-filled/book}}` | 04, 12 |
| 歷史 | `{{icon:tabler-filled/history}}` | 04 |
| 心/療愈 | `{{icon:tabler-filled/heart}}` | 10 |
| 星光 | `{{icon:tabler-filled/sparkles}}` | 02, 12 |
| 畫筆 | `{{icon:tabler-filled/brush}}` | 03, 11 |
| 月 | `{{icon:tabler-filled/moon}}` | 06, 08 |

> 最終可用名單由 Executor 以 `ls templates/icons/tabler-filled/ | grep <keyword>` 確認後鎖定。

---

## VII. Visualization Reference List

| Visualization Type | Reference Template | Used In |
| ------------------ | ------------------ | ------- |
| `timeline` | `templates/charts/timeline.svg` | Slide 04（植物染歷史脈絡） |
| `numbered_steps` | `templates/charts/numbered_steps.svg` | Slide 10（植物染工藝步驟） |
| `icon_grid` | `templates/charts/icon_grid.svg` | Slide 09（染料植物分類） |

---

## VIII. Image Resource List

> 圖片源自公眾號原文，直接使用於演示（文化分享場景）。所有圖片已存放於 `images/`。

| Filename | Dimensions | Ratio | Purpose | Type | Status |
| -------- | --------- | ----- | ------- | ---- | ------ |
| `640.png` | 1080×605 | 1.79 | 春晚開場視覺秀截圖（李子柒） | Photography | Existing |
| `640_4.png` | 800×1291 | 0.62 | 李子柒戰袍全身特寫 | Photography | Existing |
| `640.jpg` | 900×1200 | 0.75 | 李子柒與黃榮華協作吊染 | Photography | Existing |
| `640_1.png` | 1080×279 | 3.87 | 唐·張萱《搗練圖》區域性 | Illustration | Existing |
| `640_5.png` | 1024×802 | 1.28 | 宋·汝窯天青釉圓洗 | Photography | Existing |
| `640_1.jpg` | 943×602 | 1.57 | 黃榮華染制雨過天青絲巾 | Photography | Existing |
| `640_6.png` | 1080×720 | 1.50 | 蒼黃色意境圖 | Photography | Existing |
| `640_7.png` | 1080×720 | 1.50 | 暮雲灰意境圖 | Photography | Existing |
| `640_8.png` | 400×265 | 1.51 | 天水碧色卡 | Photography | Existing |
| `640_10.png` | 800×600 | 1.33 | 黃榮華染制銀紅色絲巾 | Photography | Existing |
| `640_11.png` | 1080×684 | 1.58 | 《霸王別姬》酡色劇照 | Photography | Existing |
| `640_12.png` | 403×228 | 1.77 | 黛青色卡 | Photography | Existing |
| `640_13.png` | 1080×721 | 1.50 | 相思灰意境圖 | Photography | Existing |
| `640_14.png` | 1080×699 | 1.55 | 染料植物（茜草/紅花等） | Photography | Existing |
| `640_15.png` | 640×640 | 1.00 | 植物染操作過程 | Photography | Existing |
| `640_17.png` | 1080×1072 | 1.01 | 《夢華錄》薛濤箋意象 | Photography | Existing |
| `640_18.png` | 974×731 | 1.33 | 薛濤箋染色成品 | Photography | Existing |

---

## IX. Content Outline

### Part 1：啟幕 — 春晚驚豔

#### Slide 01 - Cover（封面）

- **Layout**: 單列居中 + 左側豎排印章式標題 + 右側配圖
- **Title**: 裁雲織月 · 草木成詩
- **Subtitle**: 揭秘李子柒春晚戰袍背後，植物染成的 300 種中國傳統色
- **Image**: `640.png`（春晚截圖）右側圖 · 左側豎排主標
- **Footer**: 源自 · 鳳凰空間 | 2026.04

#### Slide 02 - 引子

- **Layout**: 左右分欄（圖左文右，圖 0.62 豎圖放左側居中）
- **Title**: 最動人的色彩
- **Image**: `640_4.png`（戰袍特寫，portrait 0.62）
- **Content**:
  - 核心觀點："最動人的色彩不在潘通色卡里，而早已藏在山河草木之間"
  - 2025 春晚《迎福》視覺秀
  - 13 項非遺技藝集於一身
  - 黃青漸變 · 化身蝴蝶仙子

---

### Part 2：戰袍解密

#### Slide 03 - 戰袍解密：五方正色 × 手工吊染

- **Layout**: 上下分欄 · 上方兩色色塊並列 + 下方吊染工藝示意
- **Title**: 戰袍解密 · 五方正色 × 手工吊染
- **Image**: `640.jpg`（李子柒與黃榮華協作吊染）右側小圖
- **Content**:
  - **黃色**：取材湖北神農架黃櫨 → 代表**土地**
  - **青色**：取材江南初春馬蘭草 → 代表**春天**
  - **寓意**：中華土地 · 生生不息
  - **吊染工藝**：布料吊起 → 浸入染料 → 每 30 秒上拉 1 釐米 → 水墨暈染般漸變

#### Slide 04 - 植物染：千年染技的時間長河

- **Layout**: 上下分欄（頂部《搗練圖》裝飾條 + 下方 timeline）
- **Title**: 染色之術 · 遠始軒轅之世
- **Visualization**: `timeline`
- **Image**: `640_1.png`（《搗練圖》超寬圖 3.87 作頂部裝飾條）
- **Content**（5 個時間節點）：
  - **軒轅之世**：黃帝制玄冠黃裳，以草木之汁染成文彩
  - **西周**：設專職"染人"
  - **秦朝**：設"染色司"
  - **唐宋**：設"染院"
  - **明清**：設"藍靛所"；《齊民要術》《天工開物》記載技藝

---

### Part 3：草木之色 — 染出自然萬物

#### Slide 05 - 草木之色（上）：雨過天青 × 蒼黃

- **Layout**: 左右分欄（5:5），兩色並列
- **Title**: 草木之色（上）· 染出自然萬物
- **Image**: `640_5.png`（汝窯圓洗）左 + `640_6.png`（蒼黃）右
- **Content**:
  - **雨過天青 `#7AA4B6`** | 宋徽宗"雨過天青雲破處，這般顏色做將來" | 土靛 95% + 黃芩 5% 套染
  - **蒼黃 `#B29A55`** | 報春鳥 · 麛鹿之色 | 大黃+蘇木，藍礬媒染

#### Slide 06 - 草木之色（下）：暮雲灰 × 天水碧

- **Layout**: 左右分欄（5:5），兩色並列
- **Title**: 草木之色（下）· 日暮雲彩與露染青碧
- **Image**: `640_7.png`（暮雲灰）左 + `640_8.png`（天水碧）右
- **Content**:
  - **暮雲灰 `#7D6E74`** | 柳永"千里煙波暮靄沉沉"，李清照"落日熔金，暮雲合璧" | 蘇木為染料，藍礬+皂礬媒染
  - **天水碧 `#8FB09A`** | 南唐李煜妃 · 絲帛露宿染成 | 藍靛染月白，極少黃色套染

---

### Part 4：詩意之色 — 還原文學意境

#### Slide 07 - 詩意之色（上）：銀紅 × 酡色

- **Layout**: 左右分欄（5:5），兩色並列
- **Title**: 詩意之色（上）· 朝霞初染與飲酒顏酡
- **Image**: `640_10.png`（銀紅絲巾）左 + `640_11.png`（霸王別姬）右
- **Content**:
  - **銀紅 `#E49AA5`** | 淺緋色 · 朝霞初染 · 黛玉窗前霞影紗 | 紅花+蘇木+硃砂，明礬媒染
  - **酡色 `#C86868`** | "美人慾醉朱顏酡" · 貴妃醉酒 | 紅藍/蘇木/茜草，明礬媒染

#### Slide 08 - 詩意之色（下）：黛青 × 相思灰

- **Layout**: 左右分欄（5:5），兩色並列
- **Title**: 詩意之色（下）· 畫眉深青與相思成灰
- **Image**: `640_12.png`（黛青）左 + `640_13.png`（相思灰）右
- **Content**:
  - **黛青 `#3D4A5A`** | 畫眉之色 · 王實甫《西廂記》"眉黛青顰" | 藍草提取青黛
  - **相思灰 `#A69E98`** | 李商隱"春心莫共花爭發，一寸相思一寸灰" | 茶葉+石榴皮，皂礬媒染

---

### Part 5：草木療愈 — 親手染色

#### Slide 09 - 染料植物：四色取自草木

- **Layout**: 四列卡片（icon_grid）
- **Title**: 染料植物 · 四色皆取自草木
- **Visualization**: `icon_grid`
- **Image**: `640_14.png`（染料植物）作頁首裝飾
- **Content**（4 色卡）：
  - **紅**：茜草根 / 蘇木莖 / 紅花花瓣
  - **黃**：槐花花蕾 / 梔子果實 / 薑黃根莖
  - **藍**：藍草 / 鼠李葉莖
  - **黑**：胡桃果殼 / 板栗果殼

#### Slide 10 - 親手植物染 · 自我療愈的過程

- **Layout**: 左圖右流程（4:6）
- **Title**: 親手植物染 · 自我療愈的過程
- **Visualization**: `numbered_steps`
- **Image**: `640_15.png`（染色過程）左
- **Content**（5 步）：
  1. **燒水** — 清水入鍋煮沸
  2. **投料** — 植物染料浸入
  3. **熬製** — 1-2 小時濾出染液
  4. **浸染** — 布料入染液
  5. **定色** — 陽光曬暖固定色彩
  - 結語："緊張焦慮的情緒漸漸消失不見"

---

### Part 6：文脈與傳承

#### Slide 11 - 薛濤箋 · 風雅可復刻

- **Layout**: 圖左文右（4:6）
- **Title**: 薛濤箋 · 千年風雅可復刻
- **Image**: `640_17.png`（夢華錄）左，`640_18.png` 作副圖
- **Content**:
  - 唐代才女**薛濤**用**浣花溪水 + 木芙蓉皮 + 芙蓉花**搗汁
  - 染成**"芙蓉紅"**信箋
  - 今日復刻：**蘇木 + 明礬**效果最佳
  - "這是一扇通往東方美學的窗"

#### Slide 12 - 結語：色彩，文化記憶的承載者

- **Layout**: 單列居中 + 印章式收尾
- **Title**: 色彩不止於視覺 · 更是文化記憶的承載者
- **Content**:
  - 從天地造化的草木之色
  - 到流轉千年的絹帛華章
  - **中國傳統色彩** = 視覺體驗 × 文化記憶
  - 參考：《國色 300 色》(黃榮華 著 · 江蘇人民出版社)
- **Footer**: 完

---

## X. Speaker Notes Requirements

- **Total duration**: 約 12-15 分鐘
- **Notes style**: 講解式 · 典雅書面語 · 適量詩詞引用
- **Purpose**: 分享（inspire + instruct）
- **File naming**: `notes/<slide_name>.md`（與 SVG 同名）
- **Content per slide**: 3-5 句關鍵講稿 + 過渡銜接 + 節奏提示

---

## XI. Technical Constraints Reminder

### SVG 生成必須遵守：

1. viewBox: `0 0 1280 720`
2. 背景用 `<rect>`
3. 文字換行使用 `<tspan>`（`<foreignObject>` 禁用）
4. 透明度使用 `fill-opacity` / `stroke-opacity`；禁止 `rgba()`
5. 禁用：`clipPath`（image 除外）、`mask`、`<style>`、`class`、`foreignObject`
6. 禁用：`textPath`、`<animate*>`、`<script>`、`<symbol>+<use>`
7. `marker-start` / `marker-end` 條件允許（定義在 `<defs>`，箭頭為三角形/菱形/圓）

### PPT 相容規則：

- 禁止 `<g opacity="...">`（分組不透明度）；分別在子元素上設定
- 圖片透明度使用遮罩矩形覆蓋
- 僅內聯樣式；禁止外部 CSS 和 `@font-face`
- 圖示一律使用 `tabler-filled/` 字首（本專案鎖定單一圖示庫）
