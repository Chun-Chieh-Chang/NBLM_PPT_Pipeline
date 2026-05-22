# 頁間轉場與頁內元素動畫

PPT Master 匯出的 PPTX 同時支援**頁間轉場**（page transition）與**頁內元素入場動畫**（per-element entrance animation）。兩者都透過 `svg_to_pptx.py` 的 CLI 引數控制，輸出為真正的 OOXML 動畫——在 PowerPoint 和 Keynote 中原生播放，不是嵌入影片。

## 預設行為

| 層級 | 預設 | 原因 |
|---|---|---|
| 頁間轉場 | `fade`，0.4 秒 | 適合大多數 deck 的中性基線 |
| 頁內元素動畫 | `mixed` 效果 + `after-previous` 觸發，0.4 秒時長 + 0.5 秒間隔 | 進入頁面後元素自動按順序級聯入場，零互動即可看到完整動畫過程，最能體現 deck 的動畫能力 |

修改設定只需對同一份 `svg_output/`（或 `svg_final/`）重跑 `svg_to_pptx.py`，無需重新跑 LLM。如要徹底關閉頁內動畫，加 `-a none`。

## 物件級自定義動畫

預設動畫是全域性策略。若需要更具體的演示節奏，例如標題先淡入、圖表第二個出現、關鍵註釋最後飛入，可以使用可選的 `animations.json` sidecar。SVG 仍然只儲存靜態視覺結構；sidecar 只控制 PPTX 匯出動畫。

當使用者要求調整動畫順序、效果、時長或具體物件出現方式時，執行獨立 [`customize-animations`](../../skills/ppt-master/workflows/customize-animations.md) 工作流。

```bash
# 從真實頂層 <g id> 錨點生成可編輯模板
python3 skills/ppt-master/scripts/animation_config.py scaffold <project>

# 匯出前校驗引用是否存在
python3 skills/ppt-master/scripts/animation_config.py validate <project>

# 匯出時會自動讀取 <project>/animations.json
python3 skills/ppt-master/scripts/svg_to_pptx.py <project>
```

最小 sidecar：

```json
{
  "version": 1,
  "slides": {
    "03_market": {
      "groups": {
        "title": { "effect": "fade", "order": 1 },
        "chart": { "effect": "wipe", "order": 2, "duration": 0.6 },
        "insight": { "effect": "fly", "order": 3, "delay": 0.2 },
        "footer": { "effect": "none" }
      }
    }
  }
}
```

規則：

- `slides` key 匹配 SVG 檔案 stem（`03_market.svg` → `03_market`）。
- `groups` key 匹配頂層 `<g id="...">` 錨點。
- `effect: none` 會把該組移出入場動畫序列。
- `order` 只改變動畫順序，不改變頁面圖層順序。
- `delay` 是 `after-previous` 模式下該組開始前的秒數。
- `duration` 覆蓋該組的入場時長。
- `--animation none` 覆蓋 sidecar，強制關閉所有頁內動畫。

## 頁間轉場

```bash
# 換效果
python3 skills/ppt-master/scripts/svg_to_pptx.py <project> -t push --transition-duration 0.6

# 關閉轉場
python3 skills/ppt-master/scripts/svg_to_pptx.py <project> -t none

# 每 5 秒自動翻頁（展廳 / 自動迴圈）
python3 skills/ppt-master/scripts/svg_to_pptx.py <project> --auto-advance 5
```

可選效果：`fade`、`push`、`wipe`、`split`、`strips`、`cover`、`random`。

引數：

- `-t/--transition` — 效果名，或 `none` 禁用。預設 `fade`。
- `--transition-duration` — 秒數，預設 `0.4`。
- `--auto-advance` — 秒數；不寫則由演示者手動翻頁。

## 頁內元素動畫

預設開啟（`mixed` 效果 + `after-previous` 觸發）。共有三種 Start 模式，**與 PowerPoint 動畫窗格的 Start 下拉選單一一對應**：

- **`on-click`**（單擊時）—— 進入頁面 → 第一次點選顯示第一個語義組，後續每次點選按 z-order 顯示下一個組。適合現場演講，演講者控制節奏。與 `--recorded-narration` 互斥，因為帶旁白的影片匯出需要無點選播放。
- **`with-previous`**（與上一動畫同時）—— 所有組在進入頁面時一起入場，並行播放各自的入場動畫。`--animation-stagger` 不生效。
- **`after-previous`**（預設，在上一動畫之後）—— 第一組進入頁面時入場，後續組在前一個結束後接著出現，並按 `--animation-stagger` 增加額外間隔。適合展廳迴圈、錄屏走查，或者只是想看流動效果不想點選。

```bash
# 預設即開啟：mixed 效果 + after-previous 觸發，無需任何引數
python3 skills/ppt-master/scripts/svg_to_pptx.py <project>

# 關閉頁內動畫
python3 skills/ppt-master/scripts/svg_to_pptx.py <project> -a none

# 改用單一效果（仍走預設的 after-previous 自動級聯）
python3 skills/ppt-master/scripts/svg_to_pptx.py <project> --animation fade

# 改為單擊觸發（演講者控制節奏）
python3 skills/ppt-master/scripts/svg_to_pptx.py <project> --animation-trigger on-click

# 自定義節奏
python3 skills/ppt-master/scripts/svg_to_pptx.py <project> --animation mixed \
        --animation-stagger 0.6 --animation-duration 0.5

# 所有組進入頁面時同時入場
python3 skills/ppt-master/scripts/svg_to_pptx.py <project> --animation-trigger with-previous
```

22 種單一效果：`appear`、`fade`、`fly`、`cut`、`zoom`、`wipe`、`split`、`blinds`、`checkerboard`、`dissolve`、`random_bars`、`peek`、`wheel`、`box`、`circle`、`diamond`、`plus`、`strips`、`wedge`、`stretch`、`expand`、`swivel`。再加兩種自動輪換模式：

- `mixed` — 確定性輪換。每頁第一個動畫組使用 `fade`，後續組在整份 deck 範圍內按精選效果池連續輪換。
- `random` — 在同一效果池中隨機抽取。

效果池排除了 `appear`，因為它沒有可見動畫過程。

引數：

- `-a/--animation` — 效果名、`mixed`、`random` 或 `none`。預設 `mixed`。
- `--animation-trigger` — Start 模式（與 PowerPoint 一致）：`on-click`、`with-previous`、`after-previous`（預設）。
- `--animation-duration` — 單個元素入場秒數，預設 `0.4`。
- `--animation-stagger` — `after-previous` 模式下兩組之間的額外間隔（秒，預設 `0.5`）。其他模式忽略。
- `--animation-config` — sidecar 路徑。預設自動讀取 `<project>/animations.json`（如果存在）。

> Note: `--recorded-narration` 會拒絕 `on-click`；帶旁白的影片匯出請使用 `after-previous` 或 `with-previous`。

## 錨點機制 — 頂層 `<g id="...">`

頁內動畫錨定在 SVG 的**頂層 `<g id="...">` 內容組**上（如 `<g id="cover-title">`、`<g id="card-1">`），一個組對應一次點選入場。

每頁建議 **3–8 個內容組**。這同時也是 PowerPoint 框選 / 整體移動的顆粒度，與是否啟用動畫無關，都能改善編輯體驗。

**裝飾類分組自動跳過。** 頂層中看起來屬於頁面裝飾的組（背景、頁頭頁尾、裝飾元素、水印、頁碼）會被排除在點選序列外，跟隨頁面立即顯示。識別基於 `id`：按 `-` 和 `_` 切分後，若任一 token 命中 `background` / `bg` / `decoration` / `decorations` / `decor` / `header` / `footer` / `chrome` / `watermark` / `pagenumber` / `pagenum`，則視為裝飾類。會自動跳過的例子：`<g id="background">`、`<g id="bg-texture">`、`<g id="cover-footer">`、`<g id="p03-header">`、`<g id="bottom-decor">`、`<g id="watermark">`。仍會動畫的例子：`<g id="card-1">`、`<g id="cover-title">`、`<g id="step-discover">`。**不要為了規避動畫去掉 `<g>` 包裹**——保留分組（PowerPoint 框選需要），只要給個合適的 id 即可。

**扁平 SVG 的回退邏輯**（頂層沒有 `<g>`，只有裸 `<rect>` / `<text>` / `<path>`）：

- 頂層可見圖元 ≤ 8 → 每個圖元作為一個錨點（設上限以避免密集頁面出現 70+ 次點選）。
- 頂層可見圖元 > 8 → 該頁跳過頁內動畫。頁面照常顯示，只是不帶入場。

無論是否打算開啟動畫，Executor 都應該把邏輯分塊包進 `<g id>`。`skills/ppt-master/references/shared-standards.md` 已將這一點列為強制要求。

## 限制

- **僅原生形狀模式生效。** 頁內動畫需要可編輯形狀作為錨點。`--only legacy` 模式每頁一張大圖，沒有元素粒度，因此不響應 `-a/--animation`，只受 `-t/--transition` 影響。
- **不同 Office 版本對元素動畫存在輕微差異。** 實現走 `<p:animEffect filter=...>` 路徑（而非 `presetID` 查詢表），在 PowerPoint 2016+ 上表現一致；更老的 Office 可能把部分效果降級為 Appear。
- **相容模式的 PNG fallback 只用於顯示。** 轉場與動畫都在 slide XML 裡，不在 PNG 中；關掉相容模式不影響兩個動畫層。

## 常用速查

| 目標 | 命令 |
|---|---|
| 關閉轉場 | `-t none` |
| 切換轉場效果 | `-t push`（或上文列表中任一） |
| 轉場放慢 | `--transition-duration 0.8` |
| 自動播放 | `--auto-advance 5` |
| 關閉頁內動畫 | `-a none` |
| 改為單擊觸發 | `--animation-trigger on-click` |
| 切換為單一效果 | `--animation fade` |
| 所有組同時入場 | `--animation-trigger with-previous` |
| 元素入場放慢 | `--animation-duration 0.5` |
| after-previous 拉大間隔 | `--animation-stagger 0.8` |

完整 `svg_to_pptx.py` 參考：[`scripts/docs/svg-pipeline.md`](../../skills/ppt-master/scripts/docs/svg-pipeline.md)。
