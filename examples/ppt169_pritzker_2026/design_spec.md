# pritzker_2026_test_20260516 - Design Spec

## I. Project Information

| Item | Value |
| ---- | ----- |
| **Project Name** | pritzker_2026_test_20260516 |
| **Canvas Format** | PPT 16:9 (1280×720) |
| **Page Count** | 11 |
| **Design Style** | A) General Versatile + 編輯設計 / 雜誌感 / 建築攝影主導 |
| **Target Audience** | 建築/設計愛好者、設計行業從業者、文化媒體讀者 |
| **Use Case** | 行業分享、設計課堂、自媒體長圖、讀書會演講 |
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

- **Style**: 編輯雜誌感 + 建築攝影主導
- **Theme**: Light theme
- **Tone**: 剋制、克難、克重——大圖說話，文字點題；混凝土質感的米白底色 + 墨黑文字 + 暖金強調

### Color Scheme

| Role | HEX | Purpose |
| ---- | --- | ------- |
| **Background** | `#F5F2EC` | 米白宣紙底（主背景） |
| **Secondary bg** | `#EDE8DE` | 卡片/側欄 |
| **Primary** | `#1C1C1C` | 標題、正文 |
| **Accent** | `#B8935A` | 編號、分隔線、強調 |
| **Body text** | `#1C1C1C` | 正文主色 |
| **Secondary text** | `#5C5852` | 副文、圖注 |
| **Tertiary text** | `#8B8680` | 混凝土灰，頁尾、輔助 |
| **Border/divider** | `#D4CFC4` | 分隔線 |

---

## IV. Typography System

### Font Plan

**Typography direction**: editorial CJK — 西文襯線 × 中文黑體，雜誌專欄感

| Role | Chinese | English | Fallback tail |
| ---- | ------- | ------- | ------------- |
| **Title** | `"Microsoft YaHei", "PingFang SC"` | `Georgia` | `serif` |
| **Body** | `"Microsoft YaHei", "PingFang SC"` | `Arial` | `sans-serif` |
| **Emphasis** | `KaiTi` | `Georgia` | `serif` |
| **Code** | — | `Consolas, "Courier New"` | `monospace` |

**Per-role font stacks**:

- Title: `Georgia, "Microsoft YaHei", "PingFang SC", serif`
- Body: `"Microsoft YaHei", "PingFang SC", Arial, sans-serif`
- Emphasis: `KaiTi, Georgia, "Microsoft YaHei", serif`
- Code: `Consolas, "Courier New", monospace`

### Font Size Hierarchy

**Baseline**: Body = 22px (中等密度)

| Purpose | Ratio | Project value | Weight |
| ------- | ----- | ------------- | ------ |
| Cover title | 3.3x | 72px | Bold |
| Chapter / section opener | 2.2x | 48px | Bold |
| Page title | 1.6-1.8x | 36-40px | Bold |
| Project number (01-08 大編號) | 4x | 88px | Light Italic (Georgia) |
| Subtitle | 1.3x | 28px | SemiBold |
| **Body** | **1x** | **22px** | Regular |
| Annotation / caption | 0.7x | 15px | Regular |
| Page number / footnote | 0.55x | 12px | Regular |

---

## V. Layout Principles

### Page Structure

- **Header area**: 50-100px（編號 + 章節錨標）
- **Content area**: ~520px（圖文主體）
- **Footer area**: 30-40px（頁碼、來源、品牌錨）

### Layout Pattern Library

不預設主導 pattern。每頁按內容性格挑節奏（詳見 §VIII 表中 `Layout pattern` 列），原則：
1. 相鄰兩頁不重複 pattern
2. 同一 pattern 全 deck 不超過 2 次
3. 圖比例驅動方向（橫圖優先 hero/上下帶，方圖優先並置，豎圖優先左右帶）
4. 同主題多圖合併到一頁（多圖組合）而非拆頁

### Spacing Specification

**Universal**:

| Element | Range | Project |
| ------- | ----- | ------- |
| Safe margin | 40-60px | 60px |
| Content block gap | 24-40px | 32px |
| Icon-text gap | 8-16px | 12px |

**Non-card containers** (大量 breathing/hero 頁):

- 行高 1.5×
- 全幅大圖採用 `xMidYMid slice`；hero 文字浮層有 35-55% 半透明黑底 scrim
- 不強求等寬欄；文字寬度按可讀性（每行 24-32 漢字）

---

## VI. Icon Usage Specification

### Source

- **Built-in icon library**: `tabler-outline`（描邊 1.5px）
- 僅用於章節編號點綴、地理標識、年份徽章；不強加於每頁

### Recommended Icon List

| Purpose | Icon Path | Page |
| ------- | --------- | ---- |
| 地點定位 | `tabler-outline/map-pin` | P03-P10（每頁右上） |
| 時間/年份 | `tabler-outline/calendar` | P02（總覽） |
| 建築師章 | `tabler-outline/blockquote` | P11（結語） |
| 翻頁指示 | `tabler-outline/arrow-right` | P02 |

---

## VII. Visualization Reference List

無資料視覺化頁。本 deck 完全圖文敘事驅動，無圖表。

---

## VIII. Image Resource List

> Layout pattern 全部 verbatim from `references/image-layout-patterns.md`。覆蓋 Group A / C / D / E 至少 4 組；同組內 id 輪換；相鄰頁不重複。

| Filename | Dimensions | Ratio | Purpose | Type | Layout pattern | Acquire Via | Status | Reference |
| -------- | --------- | ----- | ------- | ---- | -------------- | ----------- | ------ | --------- |
| ando_h_rooftop.png | 685×514 | 1.33 | P01 封面背景（混凝土水景） | Photography | #1 full-bleed background with floating title | user | Existing | 安藤忠雄 H+ 美術館屋頂水景 |
| ando_h_exterior.png | 1080×810 | 1.33 | P03 安藤代表作主圖 | Photography | #41 background image with native callout cards floating over | user | Existing | H+ 美術館臨河外觀 |
| ando_h_interior.png | 667×937 | 0.71 | P03 安藤副圖（豎圖） | Photography | (同上多圖組合) | user | Existing | H+ 美術館室內空間 |
| chipperfield_milan_exterior.png | 1080×810 | 1.33 | P04 奇普菲爾德主圖 | Photography | #48 side-by-side comparison (古羅馬 vs 當代) | user | Existing | 米蘭冰球館外觀 |
| chipperfield_roman_amphitheater.png | 800×533 | 1.50 | P04 古羅馬參照 | Photography | (與主圖並置) | user | Existing | 古羅馬圓形劇場 |
| chipperfield_milan_facade.png | 1024×1365 | 0.75 | P04 立面細節（豎圖） | Photography | (副圖條帶) | user | Existing | 場館立面金屬環帶 |
| zaha_tamkang_bridge.png | 960×640 | 1.50 | P05 扎哈大橋主視覺 | Photography | #15 multi-image montage with bold text spanning across | user | Existing | 淡江大橋流線姿態 |
| zaha_tamkang_structure.png | 960×640 | 1.50 | P05 大橋結構 | Photography | (蒙太奇成員) | user | Existing | 大橋單塔斜拉結構 |
| zaha_tamkang_full.png | 831×554 | 1.50 | P05 大橋遠景 | Photography | (蒙太奇成員) | user | Existing | 大橋跨江全景 |
| foster_shanghai_exterior.png | 1080×652 | 1.66 | P06 福斯特大圖 | Photography | #12 faded image as backdrop with oversized overlay text | user | Existing | 上海嘉藝術外觀全景 |
| foster_shanghai_petal.png | 1080×1368 | 0.79 | P06 花瓣細節 | Photography | (浮層旁置小圖框) | user | Existing | 花瓣立面細節 |
| oma_new_museum_before.png | 1080×809 | 1.33 | P07 OMA 擴建前後 (前) | Photography | #50 before/after slider-style side-by-side | user | Existing | 紐約新美術館擴建前 |
| oma_new_museum_after.png | 1080×921 | 1.17 | P07 OMA 擴建前後 (後) | Photography | (#50 配對) | user | Existing | 紐約新美術館擴建後 |
| oma_new_museum_massing.png | 1080×608 | 1.78 | P07 體塊模型條帶 | Photography | (#50 下方副條) | user | Existing | OMA 體塊模型 |
| oma_new_museum_interior.png | 1080×896 | 1.21 | P07 室內（備用） | Photography | (內嵌副圖框) | user | Existing | 美術館內部 |
| zumthor_lacma_exterior.png | 1080×608 | 1.78 | P08 卒姆託主圖 | Photography | #14 horizontal banner strip cutting through mid-section | user | Existing | LACMA 大衛·格芬畫廊橫幅 |
| zumthor_lacma_underside.png | 1080×720 | 1.50 | P08 底部公共空間 | Photography | (mid-section 橫條之下副圖) | user | Existing | 懸浮架空底部空間 |
| zumthor_lacma_interior.png | 1080×608 | 1.78 | P08 內部（備用） | Photography | (右上小景) | user | Existing | LACMA 室內 |
| gehry_abu_dhabi_render1.png | 1080×608 | 1.78 | P09 蓋裡渲染主圖 | Photography | #19 image floating in whitespace with thin frame and caption | user | Existing | 阿布扎比古根海姆主渲染 |
| gehry_abu_dhabi_render2.png | 1080×607 | 1.78 | P09 渲染輔圖 | Photography | (#19 第二浮層框) | user | Existing | 第二角度渲染 |
| gehry_abu_dhabi_render3.png | 1000×1000 | 1.00 | P09 方圖輔 | Photography | (#19 第三浮層) | user | Existing | 鳥瞰渲染 |
| kere_senegal_exterior.png | 818×546 | 1.50 | P10 凱雷主圖（土磚外觀） | Photography | #38 background image + annotation cards | user | Existing | 塞內加爾歌德學院外觀 |
| kere_senegal_courtyard.png | 630×944 | 0.67 | P10 院落（豎圖） | Photography | (annotation 中嵌入小圖) | user | Existing | 猴麵包樹核心院落 |
| kere_senegal_interior.png | 980×654 | 1.50 | P10 內部 | Photography | (annotation 中嵌入小圖) | user | Existing | 學院內部空間 |

**Layout pattern 覆蓋審計**:
- Group A (容器): #1 cover, #12 faded backdrop, #14 mid-section banner, #15 montage with text → 4 patterns
- Group C (overlay): #19 floating frame → 1 pattern
- Group D (image-as-canvas): #38 background + cards, #41 background + callouts → **2 patterns，滿足 Group D 覆蓋硬約束**
- Group E (multi-image): #48 side-by-side, #50 before/after → 2 patterns
- 共 9 個不同 pattern 跨 4 組，無任何 pattern 使用 >2 次，相鄰頁無重複

---

## IX. Content Outline

### Part 1: 開篇

#### Slide 01 - 封面

- **Layout**: #1 Full-bleed background + floating title（混凝土水景為視覺錨）
- **Title**: 2026 普利茲克獎大師季
- **Subtitle**: 8 座新作，8 種深耕
- **Info**: 從蘇州河畔到沙漠腹地·讀懂頂級建築師的思考與堅守 / 來源：公眾號孫琬童 / 2026

#### Slide 02 - 8 位大師總覽

- **Layout**: Negative-space-driven + 8 卡（4×2 方陣），每卡只放編號 + 大師名 + 一行專案名 + 地理標識
- **Title**: 八位大師，八種堅守
- **Content**:
  - 01 安藤忠雄 · 蘇州 H+ 美術館 · 中國蘇州
  - 02 戴衛·奇普菲爾德 · 米蘭聖朱利亞冰球館 · 義大利米蘭
  - 03 扎哈·哈迪德（遺作）· 淡江大橋 · 中國臺北
  - 04 諾曼·福斯特 · 上海嘉藝術 · 中國上海
  - 05 OMA + SANAA · 紐約新美術館擴建 · 美國紐約
  - 06 彼得·卒姆託 · LACMA 大衛·格芬畫廊 · 美國洛杉磯
  - 07 弗蘭克·蓋裡（遺作）· 阿布扎比古根海姆博物館 · 阿聯酋阿布扎比
  - 08 迪埃貝多·凱雷 · 塞內加爾歌德學院 · 塞內加爾達喀爾

### Part 2: 8 座新作逐一深耕

#### Slide 03 - 01 安藤忠雄 · 蘇州 H+ 美術館

- **Layout**: #41 image-as-canvas + 浮層 annotation cards（橫圖為底，左側浮一張卡片承載文字，豎圖作為右上小內嵌圖）
- **Title**: 在江南園林裡寫一首混凝土詩
- **Subtitle**: 安藤忠雄 · 1995 年普利茲克獎 · 2026.1 開館
- **Content**:
  - 設計理念：立體園林—迴游性，從蘇州土地記憶中汲取園林精髓
  - 材質語言：清水混凝土肌理，摒棄裝飾，幾何線條 × 光影留白
  - 空間敘事：屋頂以水為主題，迴游中抵達面向天空與水的場所
  - 核心理念："讓建築歸於自然，讓藝術治癒人心"

#### Slide 04 - 02 戴衛·奇普菲爾德 · 米蘭聖朱利亞冰球館

- **Layout**: #48 side-by-side comparison（左側主圖當代場館，右側古羅馬劇場參照，下方副圖橫向立面條帶）
- **Title**: 千年羅馬競技場的現代迴響
- **Subtitle**: 戴衛·奇普菲爾德 · 2023 年普利茲克獎 · 2026 冬奧會場館
- **Content**:
  - 容量：16,000 名觀眾，本屆冬奧唯一新建永久場館
  - 造型源流：呼應米蘭古羅馬圓形劇場橢圓形態
  - 立面：三道金屬環帶 + 玻璃腰線 + LED 燈帶
  - 設計精神：極致剋制與精確，公共建築服務於人

#### Slide 05 - 03 扎哈·哈迪德（遺作）· 淡江大橋

- **Layout**: #15 multi-image montage + 上方半透明深色橫幅承載大標題（三張圖橫向蒙太奇拼貼）
- **Title**: 跨越江河的流動態勢
- **Subtitle**: 扎哈·哈迪德 · 2004 年普利茲克獎 · 2026.5.12 通車
- **Content**:
  - 全長 920 米，全球同型別最長跨度單塔不對稱斜拉橋
  - 100% 還原扎哈生前理想化設計
  - 工程力學 × 先鋒美學的完美融合
  - "永不設限"——大師已逝，思想延續

#### Slide 06 - 04 諾曼·福斯特 · 上海嘉藝術

- **Layout**: #12 faded image as backdrop + 巨號疊加文字（橫圖壓暗作底紋，巨號"04"和短標題壓上，右側細長豎圖作小框）
- **Title**: 蘇州河畔綻放的鋼鐵花瓣
- **Subtitle**: 諾曼·福斯特 · 1999 年普利茲克獎 · 2026.4 開放
- **Content**:
  - 不是白盒子，是城市中緩慢生長的生命體
  - 仿花朵紮根地面、向天空延展的生長軌跡
  - 三重體驗：觀展、觀景、觀城
  - 高技派外殼之下，古典人文精神透過現代材料重獲新生

#### Slide 07 - 05 OMA + SANAA · 紐約新美術館擴建

- **Layout**: #50 before/after side-by-side（上方左右並置擴建前/後，下方加體塊模型橫條）
- **Title**: 雙強聯動，新舊藝術共生
- **Subtitle**: OMA (庫哈斯, 2000) × SANAA (妹島+西澤, 2010) · 2026.3.21 開放
- **Content**:
  - 投資 8200 萬美元，新增 5,574 ㎡
  - OMA 先鋒解構 × SANAA 輕盈通透的碰撞
  - 通透立面 + 錯落空間 + 開放佈局，讓城市街景與藝術空間相互滲透
  - "迭代更新、相容幷蓄"——百年美術館獲新活力

#### Slide 08 - 06 彼得·卒姆託 · LACMA 大衛·格芬畫廊

- **Layout**: #14 horizontal banner strip 中段貫穿（頂部留標題，中段橫幅大圖，底部承載敘事文字）
- **Title**: 20 年打磨的詩意藝術方舟
- **Subtitle**: 彼得·卒姆託 · 2009 年普利茲克獎 · 2026.5.4 開放
- **Content**:
  - 耗資 7.24 億美元，32,293 ㎡，歷時 20 年
  - 七座極簡混凝土亭子橫跨威爾希爾大道之上
  - 摒棄藝術品等級化，古典與當代平等共生
  - "建築是場所的詩意容器"

#### Slide 09 - 07 弗蘭克·蓋裡（遺作）· 阿布扎比古根海姆博物館

- **Layout**: #19 image floating in whitespace + 多浮層細框（三張渲染圖錯落浮於米白底，細框 + 小圖注，文字以負空間承載）
- **Title**: 沙漠中的"解構主義絕唱"
- **Subtitle**: 弗蘭克·蓋裡（1929-2025）· 1989 年普利茲克獎 · 2026 開幕
- **Content**:
  - 大師生命尾聲 20 年心血，金屬外立面隨日光變換肌理
  - 不規則曲面 + 靈動褶皺 + 極致衝擊的幾何
  - 針對沙漠極端氣候的先進遮陽與隔熱系統
  - "建築無邊界、創意無極限"——解構主義大師的收官終篇

#### Slide 10 - 08 迪埃貝多·凱雷 · 塞內加爾歌德學院

- **Layout**: #38 background image + annotation cards（橫圖作底，2-3 張半透明資訊卡浮上，豎圖與內部圖嵌入卡內）
- **Title**: 夯土磚"屏風"，紮根鄉土的溫暖建築
- **Subtitle**: 迪埃貝多·凱雷 · 2022 年普利茲克獎 · 2026.4 開幕
- **Content**:
  - 核心院落置入猴麵包樹（生命象徵）
  - 本土壓制土磚 + 自然通風系統，擺脫空調依賴
  - "順應自然，而非與之對抗"
  - 全球建築同質化時代，凱雷再證：頂級建築紮根土地、溫暖人心

### Part 3: 收束

#### Slide 11 - 結語：所有傳世，皆源於深耕

- **Layout**: Negative-space-driven 單元素 + 暖金強調引語（無大圖，文字為主，留白為主）
- **Title**: 所有傳世的經典，皆源於日復一日的堅守
- **Content**:
  - 有人耗時二十年打磨一座場館 — 卒姆託
  - 有人堅守本土人文，讓建築紮根土地 — 凱雷
  - 有人突破邊界、顛覆常規 — 扎哈、蓋裡
  - 收束語：對空間、自然、人文的極致敬畏與深度思考
- **Footer**: 資料來源：公眾號"孫琬童" / 致敬 8 位大師 / 2026

---

## X. Speaker Notes Requirements

- **Filename**: 與 SVG 同名（`01_cover.svg` → `notes/01_cover.md`）
- **Total duration**: 約 12 分鐘
- **Notes style**: 文化隨筆式，敘述溫度優先於技術引數
- **Purpose**: inform + inspire

---

## XI. Technical Constraints Reminder

1. viewBox: `0 0 1280 720`
2. `<rect>` 背景，`<tspan>` 文字換行
3. 透明度用 `fill-opacity` / `stroke-opacity`，禁用 `rgba()`
4. 禁用：`mask`, `<style>`, `class`, `foreignObject`, `textPath`, `<animate*>`, `<script>`, `<g opacity>`
5. 字元：`—` `·` `→` 等用原生 Unicode，禁用 HTML named entities
6. 全幅圖用 `preserveAspectRatio="xMidYMid slice"`；半透明 scrim 用 `<rect fill-opacity>`
