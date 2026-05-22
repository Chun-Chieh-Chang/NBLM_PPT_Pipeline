# 藏拙 - Design Spec

## I. Project Information

| Item | Value |
| ---- | ----- |
| **Project Name** | cangzhuo (《男人最頂級的城府：藏拙》) |
| **Canvas Format** | PPT 16:9 (1280×720) |
| **Page Count** | 14 |
| **Design Style** | A) 通用大眾 + 新中式水墨留白 |
| **Target Audience** | 30+ 男性職場人 / 自我修養讀者 / 公眾號轉發場景 |
| **Use Case** | 朋友圈傳播、讀書分享、個人成長課件 |
| **Created Date** | 2026-05-16 |

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

- **Style**: 新中式 / 水墨留白 / 文人氣質
- **Theme**: Light theme（宣紙底）
- **Tone**: 靜、剋制、文氣、東方哲思

### Color Scheme

| Role | HEX | Purpose |
| ---- | --- | ------- |
| **Background** | `#F5F1E8` | 宣紙米白，全頁底色 |
| **Secondary bg** | `#EFEAD9` | 副底色 / 卡片背景（比主底色略深） |
| **Primary** | `#1A1A1A` | 墨黑，標題、主體文字、深色塊 |
| **Accent** | `#A52A2A` | 硃砂，重點字、印章、關鍵論點強調 |
| **Body text** | `#1A1A1A` | 正文 |
| **Secondary text** | `#5C5852` | 副文、引文出處 |
| **Tertiary text** | `#8B8680` | 遠山灰，輔助元素、頁碼、註釋 |
| **Border/divider** | `#C8C0AE` | 分割線、印章描邊 |

### AI Image Strategy

- **Image Rendering**: `ink-notes`
- **Image Palette**: `mono-ink`

---

## IV. Typography System

### Font Plan

**Typography direction**: 楷書標題 + 現代黑體正文（Kai × Hei 對比軸）

| Role | Chinese | English | Fallback tail |
| ---- | ------- | ------- | ------------- |
| **Title** | `KaiTi` | `Georgia` | `serif` |
| **Body** | `"Microsoft YaHei", "PingFang SC"` | `Arial` | `sans-serif` |
| **Emphasis** | `KaiTi` | `Georgia` | `serif` |
| **Code** | — | `Consolas, "Courier New"` | `monospace` |

**Per-role font stacks**:

- Title: `KaiTi, Georgia, serif`
- Body: `"Microsoft YaHei", "PingFang SC", Arial, sans-serif`
- Emphasis: `KaiTi, Georgia, serif`
- Code: `Consolas, "Courier New", monospace`

### Font Size Hierarchy

**Baseline**: Body = 24px（輕鬆節奏，傳播閱讀優先）

| Purpose | Ratio | Size |
| ------- | ----- | ---- |
| Cover title | 3.3x | 80px |
| Chapter / section opener | 2.5x | 60px |
| Page title | 1.5–1.8x | 36–44px |
| Hero number / 引文大字 | 2x | 48px |
| Subtitle | 1.3x | 32px |
| **Body** | **1x** | **24px** |
| Annotation / caption | 0.75x | 18px |
| Page number / footer | 0.6x | 14px |

---

## V. Layout Principles

### Page Structure

- **Header area**: 60–80px（頁首印章或章節號，可省略）
- **Content area**: 500–560px（主內容）
- **Footer area**: 40px（頁碼 / 落款）

### Layout Pattern Library (combine or break as content demands)

| Pattern | Use in this deck |
| ------- | ----------------- |
| Single column centered | 封面 / 引子 / 結語 |
| Symmetric split (5:5) | 藏拙 vs 消極避世 對照 |
| Asymmetric split (3:7 / 2:8) | 引言 + 釋義 |
| Three/four column cards | 頂級城府的三件事 |
| Full-bleed + floating text | breathing 頁（封面、引子、章節轉場） |
| Negative-space-driven | 單獨印證頁（潛龍勿用 / 木秀於林） |
| Figure-text overlap | 韓信典故頁 |

### Spacing Specification

**Universal**:

| Element | Value |
| ------- | ----- |
| Safe margin | 左右 60px / 上下 50px |
| Content block gap | 32px |
| Icon-text gap | 12px |

**Card-based**:

| Element | Value |
| ------- | ----- |
| Card gap | 24px |
| Card padding | 28px |
| Card border radius | 8px |
| Three-column card width | 360px |
| Four-column card width | 268px |

**Non-card**: 行距 1.6×；breathing 頁正文寬度 720–900px 居中，依資訊體量自由收放。

---

## VI. Icon Usage Specification

### Source

- **Built-in icon library**: `tabler-outline`（stroke_width = 1.5，線性輕盈，與水墨留白調性契合）
- **Usage method**: SVG 佔位符 `<use data-icon="tabler-outline/<name>" stroke-width="1.5"/>`

### Recommended Icon List

| Purpose | Icon Path | Page |
| ------- | --------- | ---- |
| 章節符號 / 引文 | `tabler-outline/quote` | P02, P05, P10 |
| 不亮牌 / 隱藏 | `tabler-outline/eye-off` | P04, P07 |
| 鋒芒 / 武器 | `tabler-outline/sword` | P06, P09 |
| 盾 / 防禦 | `tabler-outline/shield` | P09 |
| 時間 / 等待 | `tabler-outline/hourglass` | P10, P12 |
| 山 / 沉穩 | `tabler-outline/mountain` | P12 |
| 心 / 情緒 | `tabler-outline/heart` | P13 |
| 圓點 / 列表 | `tabler-outline/point-filled` | 通用 |

---

## VII. Visualization Reference List

> 本篇為人文哲思散文，資料視覺化頁很少。僅 2 頁採用 charts 模板作為結構骨架；其餘頁面均為自由排版。

Catalog read: 71 templates

| Page | Template | Path | Summary-quote (verbatim from `charts_index.json`) | Usage |
| ---- | -------- | ---- | ------------------------------------------------- | ----- |
| P11 | pros_cons_chart | `templates/charts/pros_cons_chart.svg` | "Pick for bilateral pros/cons list, 2-5 items per side. Skip for full feature comparison (use comparison_table) or numeric A/B mirror data (u…)" | 藏拙 vs 消極避世 四維對照 |
| P13 | vertical_list | `templates/charts/vertical_list.svg` | "Pick for 3-6 numbered key points each with a short description — design principles, core tenets, action items, key takeaways, recommendation…" | 藏住四件事 → 養出四種力（核心輸出頁） |

**Runners-up considered** (fewer than 3 viz pages, runners-up listed per page):

- `comparison_table` | rejected for P11: 僅四個維度、兩欄對比，pros_cons 視覺更利落；comparison_table 適合多列多行密集矩陣
- `principles_grid` (不在庫內) → `vertical_pillars` | rejected for P13: 四組"藏 → 養"是同質化條目，vertical_list 的"序號 + 標題 + 說明"格式更貼合
- `numbered_steps` | rejected for P13: 該頁是平行四條原則，不是順序步驟；步驟化會誤導讀者以為有先後

---

## VIII. Image Resource List

| Filename | Dimensions | Ratio | Purpose | Type | Layout pattern | Acquire Via | Status | Reference | text_policy | page_role |
| -------- | --------- | ----- | ------- | ---- | -------------- | ----------- | ------ | --------- | ----------- | --------- |
| cover_bg.png | 1280×720 | 1.78 | 封面背景：水墨遠山留白 | Background | #1 full-bleed background with floating title + #29 two-stop scrim | ai | Pending | Distant misty mountain range in ink wash style, vast empty paper sky on top three-fifths reserved for vertical title, sparse brushstrokes, a single tiny boatman silhouette on a lake at lower right; deep silence and restraint | none | hero_page |
| yinzi_bg.png | 1280×720 | 1.78 | 引子背景：藏鋒 atmosphere | Background | #12 faded image as backdrop with oversized overlay text + #30 flat semi-transparent rectangle overlay | ai | Pending | Half-sheathed brushstroke or ink-trail receding into white paper, calm left two-thirds reserved for floating quote text, single faint seal mark at lower right corner; suggests withdrawn force without revealing it | none | hero_page |
| hanxin_bridge.png | 1280×720 | 1.78 | 韓信胯下之辱場景 | Illustration | #4 right image bleeding off the canvas edge + #29 two-stop scrim | ai | Pending | Lone scholar-warrior figure standing quietly under a stone bridge in ancient market street, ink-wash brushwork, no facial detail, body language steady not humbled, crowd as faint ink dots in background; restraint as strength | none | local |
| qianlong_pool.png | 1280×720 | 1.78 | 潛龍勿用 atmosphere | Background | #1 full-bleed background with floating title + #28 radial gradient vignette | ai | Pending | Deep still pool surrounded by craggy ink-wash cliffs, suggestion of a coiled dragon shape barely visible beneath the water surface as faint darker ink swirls, mist rising; latent power waiting for time | none | hero_page |
| zengguofan_lamp.png | 1280×720 | 1.78 | 曾國藩 笨功夫 atmosphere | Illustration | #2 left-third image + right text body + #21 rounded rectangle crop | ai | Pending | Single oil lamp on a wooden desk with stacked ancient books and an open ink-stone, no human figure, view through a paper window showing pre-dawn darkness; persistence in solitude | none | local |
| closing_mountain.png | 1280×720 | 1.78 | 結語：山外有山 | Background | #1 full-bleed background with floating title + #29 two-stop scrim | ai | Pending | Layered ink-wash mountain ridges receding into distance, foreground sharp dark mountain, middle and far ridges progressively lighter into mist, vast empty sky reserved for closing quote; depth and patience | none | hero_page |

> **Image-as-canvas (#38–#46) coverage note**: 本篇為文學哲思散文，無 KPI / 流程節點 / 儀表盤 / 網路架構圖等需"在圖上疊加結構化資訊層"的頁面；所有 image-bearing 頁面均為氛圍烘托型（hero / atmosphere），原生 SVG 文字層獨立承擔資訊，無需 #38–46 family。這是該 deck 內容性質決定的合理偏移。

---

## IX. Content Outline

### Part 1: 開篇

#### Slide 01 — Cover

- **Layout**: Full-bleed background image + 居中豎排標題 + 副標題 + 落款（page_rhythm: anchor）
- **Title**: 男人最頂級的城府：藏拙
- **Subtitle**: 沉得住，藏得住，等得起
- **Info**: 謀事論 · 論盡成事邏輯

#### Slide 02 — 引子

- **Layout**: Full-bleed faded backdrop + 中央大字引言（page_rhythm: breathing）
- **Title**: （無標題，引文即主體）
- **Content**: "男人太早亮牌，就是給別人遞刀。"

### Part 2: 看見問題

#### Slide 03 — 燒烤攤故事

- **Layout**: 左右對照（5:5 split）+ 底部一行總結（page_rhythm: dense）
- **Title**: 燒烤攤上的兩種人
- **Content**:
  - 左：剛升職的人——開口講資源、人脈、專案；旁人嘴上恭維、眼裡盤算
  - 右：另一個男人——話不多，只問關鍵問題，散場時把每人底牌看了七八分
  - 底部："世上的局，很多不是輸在沒本事，而是輸在太早讓別人知道你有什麼本事"

#### Slide 04 — 什麼是藏拙

- **Layout**: 三列卡片（page_rhythm: dense）
- **Title**: 藏拙 ≠ 裝傻 ≠ 認慫
- **Content**: 三個核心動作
  - 把鋒芒收起來
  - 把慾望壓下去
  - 把自己從別人的視線中心挪開

#### Slide 05 — 木秀於林

- **Layout**: Full-bleed + 居中大字引文（page_rhythm: breathing）
- **Title**: （引文頁，無小標題）
- **Content**: "木秀於林，風必摧之"——《增廣賢文》
- 解讀：實力沒強到能自保時，鋒芒就是風險

### Part 3: 常見錯誤

#### Slide 06 — 年輕人最容易犯的錯

- **Layout**: 2x2 grid 卡片 + 底部一句話（page_rhythm: dense）
- **Title**: 把"被看見"誤以為"被尊重"
- **Content**:
  - 剛有點成績，就想讓所有人知道
  - 剛有點資源，就忍不住展示
  - 剛看透一點人性，就急著戳破
  - 底部：明處的人沒有遮擋，所有試探、嫉妒、借力、拆臺，都會先衝他來

#### Slide 07 — 會藏拙的人怎麼做

- **Layout**: 三列對照 + 底部引言（page_rhythm: dense）
- **Title**: 不在小場面裡浪費鋒芒
- **Content**:
  - 飯局上 — 不搶話
  - 會議裡 — 不亂表態
  - 人群中 — 不急著顯擺關係
  - 底部："沉默不是空白，是在收集資訊；退讓不是無能，是不把彈藥浪費在無價值的目標上"

### Part 4: 歷史佐證

#### Slide 08 — 韓信胯下之辱

- **Layout**: 右側出血圖 + 左側文字（page_rhythm: anchor）
- **Title**: 韓信胯下之辱
- **Content**:
  - 不是為了歌頌屈辱
  - 而是他沒有把人生押在一場街頭衝突裡
  - 小局贏了，可能只是出口氣；大局贏了，才有翻身的資格

#### Slide 09 — 藏拙的高明

- **Layout**: 四行表格（page_rhythm: dense）
- **Title**: 把"拙"變成盾
- **Content**: 表現 × 旁人反應 四行對照
  - 太聰明 → 防他
  - 太強勢 → 躲他
  - 太急切 → 資源方壓價
  - 太想贏 → 對手拖他入局
  - 底部：適當慢一點、鈍一點、淡一點，反而能減少無謂的消耗

#### Slide 10 — 潛龍勿用

- **Layout**: Full-bleed + 居中引文（page_rhythm: breathing）
- **Title**: （引文頁）
- **Content**: "潛龍勿用"——《易經》
- 解讀：龍在深淵時，不是沒有力量，而是時機未到

### Part 5: 辨明區分

#### Slide 11 — 藏拙 ≠ 消極避世

- **Layout**: pros_cons_chart 雙列對照（page_rhythm: dense）
- **Title**: 藏拙 ≠ 消極避世
- **Visualization**: pros_cons_chart
- **Content**: 四維對照
  - 動機：消極=怕輸 vs 藏拙=為贏
  - 狀態：消極=越躲越廢 vs 藏拙=越藏越厚
  - 沉默：消極=藉口 vs 藏拙=蓄力
  - 內心：消極=委屈 vs 藏拙=佈局

#### Slide 12 — 曾國藩典範

- **Layout**: 左圖 + 右文字（page_rhythm: anchor）
- **Title**: 曾國藩：笨功夫、慢功夫、深功夫
- **Content**:
  - 早年並不以聰明見長，甚至常被認為遲鈍
  - 靠的是：笨功夫 / 慢功夫 / 深功夫
  - 不爭一時快，不貪一寸巧
  - 拙到深處，是定力；定力夠了，局勢才會慢慢站到他這邊

### Part 6: 核心輸出

#### Slide 13 — 藏住四件事 養出四種力

- **Layout**: vertical_list 四條編號原則（page_rhythm: dense）
- **Title**: 藏住四件事，養出四種力
- **Visualization**: vertical_list
- **Content**:
  - 01 藏住情緒 → 不被幾句話激怒
  - 02 藏住野心 → 不被人提前設防
  - 03 藏住實力 → 不被人過早消耗
  - 04 藏住判斷 → 不在局勢未明時被迫站隊

#### Slide 14 — 結語

- **Layout**: Full-bleed 遠山 + 中央三行短語 + 落款（page_rhythm: anchor）
- **Title**: 頂級城府 = 壓表現欲 × 穩勝負心 × 延遲滿足
- **Content**:
  - 沉得住，才不怕暫時被低估
  - 藏得住，才不怕一時沒掌聲
  - 等得起，才有資格在該出手的時刻，讓結果替自己說話

---

## X. Speaker Notes Requirements

- 檔案命名：`notes/01_cover.md` … `notes/14_closing.md`
- 風格：conversational（散文氣，避免商務術語）
- 目的：inspire（傳播 / 共鳴 / 觸發反思）
- 單頁時長：約 30–45 秒口述

---

## XI. Technical Constraints Reminder

### SVG Generation Must Follow:

1. viewBox: `0 0 1280 720`
2. 背景用 `<rect>` 元素鋪底色
3. 文字換行用 `<tspan>`（禁止 `<foreignObject>`）
4. 透明度用 `fill-opacity` / `stroke-opacity`（禁止 `rgba()`）
5. 禁止：`mask` / `<style>` / `class` / `foreignObject` / `textPath` / `animate*` / `script`
6. 文字中的字元直接寫 Unicode（— · → " " ©），禁止 HTML 實體（`&nbsp;` `&mdash;` 等）；XML 保留字按需轉義（`&amp;` `&lt;`）

### PPT Compatibility Rules:

- 禁止 `<g opacity="...">`，opacity 寫在子元素上
- 圖片半透明用覆蓋矩形（`<rect fill="bg-color" opacity="0.x"/>`）
- 僅允許行內樣式；禁止外部 CSS 和 `@font-face`
