# 技術路線

[English](../technical-design.md) | [中文](./technical-design.md)

---

## 設計哲學 —— AI 是你的設計師，不是完工師

生成的 PPTX 是一份**設計稿**，而非成品。把它理解成建築師的效果圖：AI 負責視覺設計、排版佈局和內容結構，交付給你一個高質量的起點。要想獲得真正精良的成品，**需要你自己在 PowerPoint 裡做精裝修**：換掉形狀、細化圖表、調整配色、把佔點陣圖形替換成原生物件。這個工具的目標是消除 90% 的從零開始的工作量，而不是替代人在最後一公里的判斷。不要指望 AI 一遍搞定所有——好的簡報從來不是這樣做出來的。

**工具的上限是你的上限。** PPT Master 放大的是你已有的能力——你有設計感和內容判斷力，它幫你快速落地；你不知道一個好的簡報應該長什麼樣，它也沒法替你知道。輸出的質量，歸根結底是你自身品味與判斷力的對映。

---

## 系統架構

```
使用者輸入 (PDF/DOCX/XLSX/URL/Markdown)
    ↓
[源內容轉換] → source_to_md/pdf_to_md.py / doc_to_md.py / excel_to_md.py / ppt_to_md.py / web_to_md.py
    ↓
[建立專案] → project_manager.py init <專案名> --format <格式>
    ↓
[模板處理（可選）] — 預設跳過，直接自由設計
    使用者主動點名模板時：複製模板檔案到專案目錄
    需要新建全域性模板：使用 /create-template 工作流單獨完成
    ↓
[Strategist] 策略師 - 八項確認與設計規範 → design_spec.md + spec_lock.md
    ↓
[Image Acquisition] 圖片獲取（當資源列表中有需要 AI 生成或網路搜尋的圖片時）
    ↓
[Executor] 執行師
    ├── 視覺構建：連續生成所有 SVG 頁面 → svg_output/
    ├── [Quality Check] svg_quality_checker.py（強制透過，0 錯誤）
    └── 講稿生成：完整講稿 → notes/total.md
    ↓
[圖表校準（可選）] → verify-charts 工作流（含資料圖表的幻燈片在此步驟校準座標）
    ↓
[視覺自檢（可選，opt-in）] → visual-review 工作流（僅在使用者明確請求時觸發）
    ↓
[後處理] → total_md_split.py（拆分講稿）→ finalize_svg.py → svg_to_pptx.py
    ↓
輸出：
    exports/
    ├── presentation_<timestamp>.pptx          ← 原生形狀版（DrawingML）— 唯一標準產物，編輯/交付從這裡走
    └── presentation_<timestamp>_svg.pptx      ← SVG 快照版 pptx — 畫素級視覺參考（加 --svg-snapshot 時生成）

    # 預設流程（未指定 -o）始終寫入
    backup/<timestamp>/
    └── svg_output/                            ← Executor 原始 SVG 備份（重跑 finalize_svg → svg_to_pptx 即可重建 pptx）
```

---

## 技術流程

**核心流程：AI 生成 SVG → 後處理轉換為 DrawingML（PPTX）。**

整個流程分為三個階段：

**第一階段：內容理解與設計規劃**
原始檔（PDF/DOCX/URL/Markdown）經過轉換變為結構化文字，由 Strategist 角色完成內容分析、頁面規劃和設計風格確認，輸出完整的設計規格。

**第二階段：AI 視覺生成**
Executor 角色逐頁生成簡報的視覺內容，輸出為 SVG 檔案。這個階段的產物是**設計稿**，而非成品。

**第三階段：工程化轉換**
後處理指令碼將 SVG 轉換為 DrawingML，每一個形狀都變成真正的 PowerPoint 原生物件——可點選、可編輯、可改色，而不是嵌入的圖片。

---

## 為什麼是 SVG？

SVG 是這套流程的核心樞紐。這個選擇是透過逐一排除其他方案得出的。

**直接生成 DrawingML** 看起來最直接——跳過中間格式，AI 直接輸出 PowerPoint 的底層 XML。但 DrawingML 極其繁瑣，一個簡單的圓角矩形就需要數十行巢狀 XML，AI 的訓練資料中遠少於 SVG，生成質量不穩定，除錯幾乎無法肉眼完成。

**HTML/CSS** 是 AI 最熟悉的格式之一，但 HTML 和 PowerPoint 有根本不同的世界觀。HTML 描述的是**檔案**——標題、段落、列表，元素的位置由內容流動決定。PowerPoint 描述的是**畫布**——每個元素都是獨立的、絕對定位的物件，沒有流，沒有上下文關係。這不只是排版計算的問題，而是兩種完全不同的內容組織方式之間的鴻溝。就算解決了瀏覽器排版引擎的問題（Chromium 用數百萬行程式碼做這件事），HTML 裡的一個 `<table>` 也沒法自然地變成 PPT 裡的幾個獨立形狀。

**WMF/EMF**（Windows 圖元檔案）是微軟自家的原生向量圖形格式，與 DrawingML 有直接的血緣關係——理論上轉換損耗最小。但 AI 對它幾乎沒有訓練資料，這條路死在起點。值得注意的是：連微軟自家的格式在這裡都輸給了 SVG。

**SVG 作為嵌入圖片** 是最簡單的路線——把整張幻燈片渲染成圖片塞進 PPT。但這樣完全喪失可編輯性，形狀變成畫素，文字無法選中，顏色無法修改，和截圖沒有本質區別。

SVG 勝出，因為它與 DrawingML 擁有相同的世界觀：兩者都是絕對座標的二維向量圖形格式，共享同一套概念體系：

| SVG | DrawingML |
|---|---|
| `<path d="...">` | `<a:custGeom>` |
| `<rect rx="...">` | `<a:prstGeom prst="roundRect">` |
| `<circle>` / `<ellipse>` | `<a:prstGeom prst="ellipse">` |
| `transform="translate/scale/rotate"` | `<a:xfrm>` |
| `linearGradient` / `radialGradient` | `<a:gradFill>` |
| `fill-opacity` / `stroke-opacity` | `<a:alpha>` |

轉換不是格式錯配，而是兩種方言之間的精確翻譯。

SVG 也是唯一同時滿足流程中所有角色需要的格式：**AI 能可靠地生成它，人能在任意瀏覽器裡直接預覽和除錯，指令碼能精確地轉換它**——在生成任何 DrawingML 之前，設計稿就已經完全透明可見。

---

## 源內容轉換

原始檔（PDF / DOCX / EPUB / XLSX / PPTX / 網頁）在流水線啟動前先被歸一化為 Markdown——這是 Strategist 閱讀的事實源。兩個設計選擇塑造了轉換器：

**Native-Python 優先，外部二進位制兜底。** 常見格式由純 Python wheel 處理，pandoc 僅在長尾的小眾格式時才被呼叫。讓每個使用者都去裝一份可能沒有許可權裝的系統級二進位制是一種可用性稅，而 95% 的輸入是 docx / pdf / html，付這種稅不划算。

**TLS 指紋模擬應對高安全站點。** 網頁抓取預設模擬 Chrome TLS 指紋。微信公眾號和不少 CDN 直接遮蔽 Python 預設 `requests` 握手；用一個依賴把這事一併解決，比維持一份 Node.js 抓取器作為主路徑更划算。

---

## 專案結構與生命週期

專案佈局裡非顯然的一點是 `import-sources` 的**非對稱預設**：倉庫**外**的檔案預設 *copy*（保留使用者原件），倉庫**內**的檔案預設 *move*（避免中間產物被誤提交）。這種不對稱恰好對應自然的風險畫像——倉庫外的檔案一般是使用者資產、不該動；倉庫內的檔案一般是臨時產物、應該清理。一個統一預設無論選 copy 還是 move，每次都會在另一種場景出錯。

---

## Canvas 格式系統

PPT Master 不只服務 PPT——同一套 SVG → DrawingML 流水線還能產出方形海報、9:16 故事、A4 印刷品。各格式特定的約定（比例、安全區、品牌區等）住在 [`references/canvas-formats.md`](../../skills/ppt-master/references/canvas-formats.md)。

值得標註的架構選擇：**viewBox 是畫素，不是絕對單位。** 畫素空間讓 AI Executor 思考佈局沒有歧義（`x="100"` 就是左緣 +100px），人類在瀏覽器裡檢查也直接。到 EMU 的換算只在匯出時發生一次——選畫素意味著流水線的其餘環節（Strategist、Executor、質量檢查、後處理）永遠不需要在 EMU 思維下工作，那對 AI 生成和人類除錯都是敵對的。

---

## 模板系統與可選路徑

模板是**可選項，不是預設**。Strategist 預設走自由設計——AI 完全憑源內容創造視覺系統。模板路徑只在使用者顯式觸發時啟用。

**為什麼預設自由設計。** 模板是地板，但很容易變成天花板：它會把整個 deck 鎖進模板自有的視覺慣用語，無視內容本身想要怎樣被呈現。自由設計的佈局從源內容的結構推導而來，而不是從一套固定語法套上去——視覺節奏跟著內容走，而不是跟內容打架。約束模式在窄場景裡確實更好（品牌鎖定的 deck、強型別場景如學術答辯或政府報告），所以它一直在；但 AI 不主動去抓，是使用者去抓。

**不主動匹配。** AI 不會基於內容向使用者推薦、暗示或自動對映模板。即便某份 deck 看起來"明顯適合"庫裡某個模板，沒有使用者點名，AI 也保持沉默，按自由設計走。理由是可靠性優先於發現性：把內容與模板做匹配是會隨庫演進而漂移的判斷，一句錯誤的"或許你想用 X"會把使用者推向 AI 本就無法可靠承諾的選擇。發現性交給檔案（`templates/layouts/README.md`）和顯式查詢路徑（"有哪些模板可以用？"）承擔，不放進執行時 prompt。

**佈局是 opt-in，圖表和圖示不是。** 這種不對稱不是矛盾——*佈局*正是鎖定視覺慣用語的那一層（地板/天花板問題），而圖表和圖示是不會施加 deck 級風格約束的複用原語。同一個 `templates/` 目錄，但在視覺契約裡扮演的角色不同。

---

## 角色系統：單一流水線中的三個專業代理

PPT Master 用的是**單主代理內的角色切換**，不是並行子代理。這個選擇有三條互相支撐的理由：

**為什麼是單代理而非並行子代理。** 頁面設計依賴完整的上游上下文——Strategist 的色彩選擇、圖片資源是否成功獲取（還是失敗被替代）、之前幾頁的視覺節奏。子代理拿到的只能是這個上下文的過期區域性快照，產出的 deck 視覺會逐頁漂。同一邏輯也禁止分批生成（比如一次 5 頁）：分批加速上下文壓縮，deck 的視覺一致性下降速度比節省的速度更快——不划算。

**為什麼是角色專屬 reference 而不是一個超大 prompt。** Strategist 跑的是「跟使用者協商」模式（開放式、對話式、可以回退），Executor 跑的是「產出嚴格 XML」模式（不準即興、不準漏屬性）。把兩者塞進同一個 prompt，強迫模型在同一個 turn 裡持守相互矛盾的紀律——所有混合模式的 prompt 工程病灶都會出現。按角色拆開，每個角色只載入它需要的、扔掉其他。

**Eight Confirmations 是唯一的阻塞 gate。** Strategist 階段以八項打包確認（畫布 / 頁數 / 受眾 / 風格 / 配色 / 圖示 / 排版 / 影象）作為單一阻塞決策點呈現給使用者。確認後，流水線一路跑到結束，不再有使用者中斷點。打包且單一的理由：設計選項之間是相關的（配色影響圖示庫、影響排版），一起決能產出一致的決策；分散到各階段確認會引入互相矛盾的使用者輸入，最後被迫回退重做。

**使用者已有圖片走後設資料，不讀畫素。** 使用者自帶圖片時，Strategist 跑的是一個抽取器，把尺寸、EXIF 方向、主色調、主體內容總結成文字，然後基於這份文字推理。直接讀圖片位元組是被禁的，因為 LLM 做佈局決策不需要畫素，需要的是能塞進一頁的事實（用寬高比定位置、用色調判定調色盤相容、用主體決定哪頁放）。讀畫素只會消耗上下文而不帶來決策質量收益。

**逐頁 spec_lock 重讀** 是長 deck 的抗漂移機制——完整理由見下面的 § 設計規範的傳播。

---

## 執行紀律

流水線由 [`SKILL.md` § 全域性執行紀律](../../skills/ppt-master/SKILL.md) 中的 8 條規則強制——那份檔案是權威，規則住在那裡。它們看起來很官僚，但存在的理由是：LLM 預設行為是「讓我在這一 turn 裡把整個問題搞定」，而這恰好是序列流水線最不該有的形狀——序列流水線要求每一步的輸出都是有界、過 checkpoint、被下一步消費的。這套規則共同關閉了實際反覆出現的失敗模式：亂序執行、AI 代為做使用者設計決策、跨階段打包、前置條件未滿足、投機預先準備、子代理上下文丟失、分批漂移、長 deck 色彩字型漂移。

角色切換協議（切換模式前必須 `read_file references/<role>.md`）有兩個互相支撐的作用：把新鮮的角色指令載入上下文，覆蓋前一模式的漂移；對話 transcript 中的可見標記構成審計軌跡，讓使用者能看到 agent 何時切換了模式——回看一個具體決策為什麼這樣做時，這條線索很關鍵。

---

## 設計規範的傳播：spec_lock.md 作為執行契約

Strategist 階段產出兩份看起來冗餘但服務不同物件的產物：

- `design_spec.md` —— 人類可讀敘述；設計的「為什麼」（目標受眾、風格目標、配色理由、頁面大綱）
- `spec_lock.md` —— 機器可讀執行契約；Executor 必須**字面照搬**的「是什麼」（HEX 顏色、確切的 font family 字串、圖示庫選擇、帶狀態的圖片資源列表）

為什麼兩份都要？沒有 `spec_lock.md` 的話，Executor 在長 deck 裡會逐頁重讀 `design_spec.md`，LLM 上下文壓縮漂移會逐漸扭曲色值和字型。`spec_lock.md` 是**抗漂移機制**——SKILL.md 強制要求生成每一頁前 `read_file <project>/spec_lock.md`，讓數值在 20+ 頁裡保持字面一致。

`update_spec.py` 把生成後的修改用兩個協調步驟傳播：把新值寫入 `spec_lock.md`，然後字面替換到每一份 `svg_output/*.svg`。工具的範圍**故意收得很窄**——只支援 `colors.*`（HEX 值，大小寫不敏感替換）和 `typography.font_family`（屬性級）。其他欄位（字號、圖示、圖片、畫布）**有意不支援**——它們的替換需要屬性級或語義級理解，風險/收益不值得做批次傳播。這些情況手動改 `spec_lock.md` 然後重做受影響的頁面。

工具拒絕做備份：依賴 git 回滾。加備份機制只是重複 git 的工作，還會留下過時快照。

---

## 圖片獲取與嵌入

這一階段有三個架構層面的決策：

**provider 專屬 config key，不用通用 `IMAGE_API_KEY`。** 每個 backend 用自己的 `OPENAI_API_KEY` / `MINIMAX_API_KEY` 等等，當前 backend 由顯式的 `IMAGE_BACKEND=<name>` 選定。統一的 `IMAGE_API_KEY` 欄位第一眼看著乾淨，但當使用者同時配了多個 provider 又不確定哪個在生效時會造成靜默混亂——這種 fault 通常只表現為「影象生成結果怪怪的」，找不到清晰失敗點。強制 per-provider key 讓「我現在用的是哪個 backend」從推理變成可讀配置。

**預設寬鬆 license 過濾，配以嚴格模式應對沒法放致謝的版面。** 網路圖片搜尋預設允許 CC BY / CC BY-SA 加內聯致謝——大部分幻燈片都有視覺空間放一個致謝元素。`--strict-no-attribution` 是給全屏 hero image 和緊湊構圖的逃生口，那些場景沒法放致謝又不打破設計。NC（CC BY-NC*）和 ND（CC BY-ND*）自動拒絕，因為 PPT Master 的典型產物會用於商用或修改場景；寬鬆預設 + 這個底線正好對應使用者實際想要的 fail-mode。

**開發期外部引用，交付期分叉成兩套嵌入策略。** 在 `svg_output/` 裡編輯時，圖片是外部檔案引用——快速迭代、單點替換。兩份交付產物隨後分叉：`svg_final/` 走 Base64 內聯（產出一組自包含 SVG，IDE 預覽、瀏覽器、preview pptx 都能開而不丟點陣圖依賴）；native pptx 反過來把點陣圖複製進 PPTX 的 media 資料夾，用 `<a:srcRect>` 表達裁剪。分叉的理由：在 DrawingML 裡塞 Base64 能跑但檔案膨脹 3-4 倍；檔案引用的點陣圖是 PowerPoint 原生表達方式，配 `<a:srcRect>` 的裁剪也是 DrawingML 的規範寫法——任一方向用錯工具都要付出可編輯性或檔案大小的代價。

**AI 圖片三維繫統：Strategist 階段就鎖定。** 當 deck 包含 AI 生成圖片時，Strategist 在前置階段一次性確定三個正交維度——`rendering`（視覺風格家族：vector-illustration / editorial / 3d-isometric / sketch-notes / ……）、`palette`（deck 的 HEX 在圖裡**怎麼用**：比例 + 角色 + 氣質）、`type`（每張圖的內部構圖：background / hero / framework / comparison / ……）。前兩個是 deck 級、寫進 `spec_lock.md`；Image_Generator 此後每張圖的 prompt 都從同一份鎖定的 rendering + palette 加上該圖的 type 組裝出來，而不是逐圖重決風格。沒有這層鎖定，每張圖都會自己風格漂移，整套 deck 讀起來就是一摞互不相關的插畫。這是 `spec_lock` 字型/色彩抗漂移機制在畫素上游的對偶——同一思路，往前推一層。Strategist 在八項確認階段會向使用者呈現 **≥3 個 `rendering × palette` 候選**，絕不靜默地自動鎖定單一組合，因為這是一個會牽動全 deck 視覺的選擇，唯一權威只有使用者的品味。

---

## 圖文版式：Primary 主結構 + Modifier 修飾層

「圖片**怎麼放上幻燈片**」的詞表（完整詞彙在 [`references/image-layout-patterns.md`](../../skills/ppt-master/references/image-layout-patterns.md)）把 72 條編號技法拆成兩層、自由組合：

- **Primary 主結構**（容器佈局 / 圖作畫布 + 原生覆蓋 / 多圖組合）—— 頁面的骨架。一頁可一個也可多個；跨 Primary 的組合，如「側邊對比 + 圖作畫布的註解卡」，是合規的。
- **Modifier 修飾層**（非矩形裁剪 / 遮罩與疊加 / 紋理 / 特殊技法）—— 裝飾層。一頁可疊任意多個，附著在 Primary 之上。

**為什麼顯式鼓勵複合，而不是「一頁一個 primary」。** 這份詞表對抗的 AI 失敗模式不是「疊太多」，而是「用得太少」——把每頁圖片預設堆成裸的 `#2 左三分` 或 `#48 側邊對比`，Modifier 層完全不動，產出視覺扁平的「AI 預設感」版式。早先的規則「一頁一個 primary，modifier 可疊」聽起來有原則，實際上加劇了 Modifier 層的棄用——AI 把它讀作「可以不疊」的許可。現在的措辭反過來：組合是常態，單 Primary + 無 Modifier 才需要解釋。

**為什麼物理拆分兩層，而不是隻打標籤。** 詞表被重排成「Primary 全部在前，Modifier 全部在後」——Strategist 或 Executor 讀一次目錄，就能從結構上內化「兩層」心智模型。編號是穩定 id（`#38` 永遠是「圖作畫布 + 註解卡」，不論它在檔案裡的物理位置），所以 `spec_lock.md`、`design_spec.md §VIII`、歷史 executor 輸出、過往示例裡所有 `#<id>` 引用照樣解析。

**為什麼組合走 Strategist 資源列表，不只交給 Executor 臨場發揮。** `§VIII 圖片資源列表` 的 `Layout pattern` 列接受 `#<id> + #<id> ...` 表示式——Primary id 加可選 Modifier id——所以組合在 SVG 生成**之前**就被宣告、被 `svg_quality_checker` 審計、並能在 session 重入後存活。把組合責任只壓在 Executor 身上，長 deck 上下文壓縮時就會丟；把它編碼進 spec_lock 旁的資源列表，組合就成為設計契約的一部分。

**為什麼真正的硬約束留在上游。** 跨切的技術硬約束（`<clipPath>` 只能用在 `<image>` 上、用 `fill-opacity` 而非 `rgba()`、禁 `<mask>`、alpha 效果的路由表）獨家住在 [`shared-standards.md`](../../skills/ppt-master/references/shared-standards.md)。版式詞表只用一行指標指向它們，不復述——這樣某條約束放開時（比如某個 DrawingML 特性變得可靠），只有一個檔案要改，詞表裡也不會留下一份過期副本繼續暗中強制舊規則。

---

## SVG 約束：禁用特性與條件允許

PowerPoint 的 DrawingML 是 SVG 表達力的嚴格子集。Executor 在一份經驗生長起來的黑名單（mask、style/class、`@font-face`、foreignObject、symbol+use、textPath、animate*、script/iframe ……）裡執行，外加對 `marker-start`/`marker-end` 和僅 `<image>` 上的 `clip-path` 的窄條件允許。權威清單和每條特性的具體約束——包括 `<mask>` 的替代效果路由表（漸變疊加、clipPath、filter shadow、源圖烘焙）——住在 [`references/shared-standards.md`](../../skills/ppt-master/references/shared-standards.md)。

值得在架構層標記的理由：

- **為什麼是黑名單，不是白名單。** SVG 是個寬規範；窮舉允許特性會隨著 Executor 不斷髮現新的有用構造而要持續維護。黑名單隻圈住語義上沒有 DrawingML 表達的窄集合，其餘隱式可用。
- **為什麼是經驗性，不是從規範推導。** 這份清單從真實的 PPT 匯出失敗長出來，不是讀 OOXML 規範讀出來的。有幾個特性（如 `<mask>`）理論上能在 DrawingML 表達，但跨 PowerPoint 版本不可靠；黑名單反映的是實際能交付的子集。
- **XML 良構性陷阱。** 兩個獨立於 DrawingML 的跨切陷阱：排版字元必須用裸 Unicode（`—`、`→`、`©`、NBSP），HTML 命名實體（`&mdash;`）在 SVG 裡是非法 XML；XML 保留字元（`& < >`）必須實體轉義，否則 `R&D` 直接終止匯出。這兩個坑出現頻率高到值得在架構層 flag 一下。
- **黑名單在後處理之前執行。** `svg_quality_checker.py` 在 `svg_output/` 上執行；後處理會重寫 SVG，會掩蓋源級別違規。修復永遠是 Executor 重新寫——有意沒有 auto-fix 模式（見 § 質量門）。

---

## 質量門

**為什麼需要這道檢查器。** LLM 生成的 SVG 不是確定性的——禁用特性會在長 deck 中悄悄混入，只在 `svg_to_pptx` 中途崩或 PowerPoint 靜默丟元素時才暴露。檢查器把「PowerPoint 在第 14 頁匯出失敗」轉化為「Executor 在第 14 頁用了 `<style>`，重新生成它」，診斷速度提升一個數量級——這正是讓長 deck 在經濟上可迭代的關鍵。

**為什麼放在後處理之前，而不是之後。** 後處理會重寫 SVG（圖示嵌入、圖片內聯），會掩蓋源級別違規。直接讀 `svg_output/` 抓的是 Executor 的實際輸出，先於任何可能掩蓋 bug 的清理動作。

**嚴重性模型：error 阻塞、warning 不阻塞，且有意沒有 auto-fix。** error 要求 Executor 在上下文裡重新寫出錯的頁面——一個被禁的 `<style>` 元素不是機械 patch，因為 Executor 用它是有原因的，替代方案（比如改成內聯屬性）需要帶著同樣的設計意圖重新落地。Auto-fix 會靜默丟失這份意圖，交付一個更難看的頁面。

**為什麼圖表座標驗證掛在同一道 gate。** 圖表頁面有幾何正確性需求（柱高、餅圖扇角、座標軸刻度位置），這些不是結構問題，SVG 合法性規則也抓不到。最自然的捕捉位置就是已經要求 AI 回看自己輸出的那道 gate——把「看一眼你剛生成的東西然後修」的認知上下文打包到一個階段，比把結構和幾何審查分到兩輪 review 更高效。

---

## 後處理流水線

> 工程化轉換階段中每一份產物和每一個模組為何存在，刪除它會破壞哪些工作流。在考慮簡化 `svg_final/` / `finalize_svg.py` / `svg_to_pptx.py` 之前，先讀這一節。

### 四份產物，四種工作流

後處理階段產生四份產物。每一份都服務於一種流水線中無法替代的工作流。

| 產物 | 服務的工作流 | 為何無可替代 |
| --- | --- | --- |
| `svg_output/` | 唯一源、手工編輯入口、`update_spec.py`、`svg_quality_checker.py` | 流水線中唯一**手寫**而非派生的目錄 |
| `svg_final/` | IDE 內即時預覽（VSCode/Cursor 直接開啟 `.svg`）、瀏覽器單頁預覽 | `.pptx` 在 IDE 裡打不開；`svg_output/` 因圖示 / 圖片是外部引用，IDE 中渲染不完整 |
| `exports/<name>_<ts>.pptx`（native） | 主交付物——PowerPoint 中以 DrawingML 形狀形態可編輯 | 唯一一份使用者可在 PowerPoint 中原生改尺寸 / 改色 / 改樣式的產物 |
| `exports/<name>_<ts>_svg.pptx`（preview，需 `--svg-snapshot` 顯式開啟） | 跨平臺單檔案分發、整體多頁瀏覽、郵件附件 | 自包含、多頁、PowerPoint / Keynote / WPS / LibreOffice 都能直接開啟；`svg_final/` 是資料夾，分發不便。預設關閉——live preview 已經覆蓋 dev / 診斷場景的 SVG 視覺參考需求 |
| `backup/<ts>/svg_output/`（預設流程下始終生成） | 不重跑 LLM 的前提下從凍結 SVG 源重建 pptx、長期存檔 | 專案下游被改動後，Executor 原始 SVG 唯一的留存副本 |

### `svg_finalize/` 包有**兩種**消費者

這是讀程式碼時容易忽略的關鍵事實。同一組 `skills/ppt-master/scripts/svg_finalize/` 下的模組，在兩個地方被使用，服務兩份不同的產物。

**寫盤消費者** —— `finalize_svg.py` 每次執行都把 `svg_output/` → `svg_final/` 寫到磁碟一次。`svg_final/` 隨後供 IDE 預覽和 preview pptx 使用。

**記憶體消費者** —— native pptx 直接讀 `svg_output/`（不經磁碟中轉），但 DrawingML 無法內聯處理兩種 SVG 特性，所以轉換器在記憶體中呼叫 `svg_finalize` 模組：

| 記憶體呼叫點 | 複用的模組 | native pptx 為何需要 |
| --- | --- | --- |
| `svg_to_pptx/use_expander.py` | `svg_finalize.embed_icons` | DrawingML 不識別 `<use data-icon="...">`；不展開圖示會靜默丟失 |
| `svg_to_pptx/tspan_flattener.py` | `svg_finalize.flatten_tspan` | DrawingML 文字塊無法在段落中跳位置；`dy` 堆疊的多行 `<tspan>` 會塌成一行，`x` 錨定的 tspan 會跑到錯誤的列 |

### 各模組消費者一覽

| 模組 | 寫盤消費者 | 記憶體消費者 | 刪除影響 |
| --- | --- | --- | --- |
| `embed_icons.py` | `finalize_svg` 的 `embed-icons` 步驟 | `svg_to_pptx/use_expander.py` | native pptx 丟失全部圖示 + `svg_final/` 不再自包含 |
| `flatten_tspan.py` | `finalize_svg` 的 `flatten-text` 步驟 | `svg_to_pptx/tspan_flattener.py` | **native pptx 中 `dy` 堆疊的多行文字塌成一行** |
| `align_embed_images.py` | `finalize_svg` 的 `align-images` 步驟 | — | `svg_final/` 失去圖片嵌入 → IDE 預覽 / preview pptx 都沒圖 |
| `crop_images.py` / `embed_images.py` / `fix_image_aspect.py` | 被 `align_embed_images.py` import | — | `align_embed_images` `ImportError`，整條鏈路 broken |
| `svg_rect_to_path.py` | `finalize_svg` 的 `fix-rounded` 步驟 | — | 隻影響 PowerPoint 內手動「Convert to Shape」時圓角丟失；瀏覽器 / IDE / PowerPoint 自帶的 SVG 渲染器都正常 |

---

## Native PPTX 轉換器內部

**為什麼是逐元素派發而不是整體翻譯。** SVG 的層級模型乾淨地對映到 DrawingML 的 group / shape / picture 型別——不需要一個全域性最佳化器去重新規劃幻燈片。每種形狀都有自己窄的翻譯器，簡單到能單獨除錯和單元測試。一張幻燈片的最終質量等於這些獨立區域性轉換之和；這個性質在整體翻譯下脆弱，在元素派發下穩健。

**為什麼 Office 相容模式預設開啟。** 2019 之前的 PowerPoint 不能原生渲染 SVG。轉換器為每頁生成 PNG 兜底，與原生形狀並存——新版 Office 仍顯示可編輯形狀，舊版回退到 PNG。預設開啟的取捨是：用適度的檔案大小代價換取「不會靜默地把打不開的 deck 交給跑老版本的使用者」；逃生口給那些明確知道自己在新棧上、想要更小檔案的使用者。

---

## 動畫與轉場模型

值得講的設計選擇是動畫**錨點**，不是效果列表。

**為什麼把入場動畫錨在頂層 `<g>` group。** PowerPoint 的動畫時序基於形狀 ID——每個被動畫的物件需要穩定的 shape ID。給單個原語做動畫會產出每頁 30+ 個分別飛入的原子（動感氾濫），只給整頁做動畫又損失視覺敘事。頂層 group 是自然粒度：Executor 本來就被強制要求用 `<g id="...">` 標記邏輯內容塊，而這些塊正是觀眾讀作「一個東西到達」的單位——動畫對齊了已有的邏輯結構，而不是另立門戶。

**為什麼頁面裝飾自動跳過。** 名為 `background` / `header` / `footer` / `decoration` / `watermark` / `page_number` 的 group 代表靜態頁面框架，不是內容；讓它們飛入會讓人出戏（頁面本身在每次切換時具象化），幾乎不會是使用者想要的。按 id token 過濾原則上脆弱，實際上可靠——因為 token 詞表很小，命名權又掌握在 Executor 手裡。

**為什麼物件級動畫用 sidecar，而不是 SVG 屬性。** SVG 繼續作為靜態視覺源。自定義 PPTX 動畫屬於匯出策略，所以物件級覆蓋放在可選的 `animations.json`，按 slide stem 和頂層 group id 關聯。這樣不會把 PowerPoint 專用後設資料塞進 SVG，同時仍能在預設全域性動畫不夠用時調整順序、效果、延遲和時長。

**為什麼錄製旁白讓自動推進時長跟著片段時長走。** 嵌入旁白意味著 deck 目標是影片匯出——影片裡沒有演講者去點選。把每頁自動推進時長設為該頁音訊片段的實際時長，PowerPoint 能幹淨地匯出為 MP4，無需人工配時。任何其他時長來源（估算朗讀速度、固定每頁時長）都會破壞音畫同步。

**為什麼錄製旁白拒絕 on-click 物件動畫。** PowerPoint 可以在真實排練時記錄點選計時，但 PPT Master 不合成物件級點選事件。錄製旁白路徑只寫頁面級音訊和頁面自動推進計時，所以單擊觸發的物件入場會讓匯出依賴額外的 PowerPoint 人工排練。帶旁白的 deck 必須使用無點選入場（`after-previous` 或 `with-previous`）。

---

## Standalone Workflows（獨立工作流）

六個能力（`create-template`、`verify-charts`、`customize-animations`、`live-preview`、`generate-audio`、`visual-review`）作為獨立工作流存在，而不是流水線步驟。每個都是稀疏觸發的——按模板、按含圖表的 deck、按一次動畫微調、按一次具體抱怨、按一次影片匯出、按使用者明確請求的一次視覺自檢，而不是按每個 deck。把任何一個塞進預設流水線，要麼對大多數使用者執行無意義的步驟（增加延遲和失敗面），要麼強制一刀切收窄主流程。保持 opt-in 讓 deck 生成主流水線保持緊湊、可預期，同時在觸發條件命中時仍提供這些能力；每個 `workflows/<name>.md` 是自包含的、按需載入——所以 prompt context 的開銷也是 opt-in。
