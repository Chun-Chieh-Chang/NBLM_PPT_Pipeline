# PPT Master — AI 生成原生可編輯 PPTX，支援任意檔案輸入


---

丟進一份 PDF、DOCX、網址或 Markdown，拿回一份**原生可編輯的 PowerPoint**——真正的形狀、真正的文字框、真正的圖表，不是圖片。點選任何元素即可編輯。

> **⚠️ PPT Master 是 harness，不是完整的 agent。** `harness + model = agent`——工具負責工作流，模型決定上限。要組成真正高質量的 agent，推薦組合是：**Claude 大上下文視窗（~100 萬 token）+ AI 生圖（`gpt-image-2`）**。其他模型能跑流程，但達不到同等質量上限。效果不理想，請先換模型，不要質疑 harness。

> **實時預覽與視覺化修改** —— 生成過程中會自動開啟瀏覽器預覽 `http://localhost:5050`。點選任意元素，寫一句要改成什麼，點 **Submit annotations**，回到對話說一句"應用註解"（或 "apply my annotations"），AI 就會改寫 SVG 並重新匯出 PPTX。最初我只想做純對話驅動，但很多使用者希望能視覺化看到效果再改，所以把這條路徑融進了主流程。詳見 [實時預覽工作流 →](./skills/ppt-master/workflows/live-preview.md)。

> **模板復刻** —— 把任何一份你喜歡的 `.pptx` 丟給 AI，一句"用 `/create-template` 復刻成模板"，就能拿到一套可被 PPT Master 直接呼叫的頁面佈局——主題色、字型、母版/版式結構、複用圖片、甚至精靈圖裁剪關係都按 OOXML 真實抽取，封面/章節/裝飾繁複的頁面都能穩定還原。從此你不再受限於內建模板：公司品牌 deck、客戶中標模板、找的高質量參考稿，都能一鍵變成你的私人模板庫。詳見 [模板指南 →](./docs/zh-TW/templates-guide.md)。

> **動畫** —— 匯出的 deck 支援**頁間轉場**和**頁內元素入場動畫**，輸出為真正的 OOXML 動畫（不是嵌入影片）。預設進入頁面後元素按順序自動級聯入場，無需點選；在 PowerPoint 和 Keynote 中原生播放，無需額外工具。詳見 [轉場與動畫使用指南 →](./docs/zh-TW/animations.md)。

> **旁白與影片** —— 把演講者備註按頁生成語音旁白（預設 `edge-tts`，也可配置雲端 TTS 獲得高質量音色），把音訊嵌回 PPTX，再用 PowerPoint 自帶"匯出影片"產出帶旁白和轉場的 MP4，全程無需第三方工具。詳見 [音訊旁白與影片匯出 →](./docs/zh-TW/audio-narration.md)。
>
> **聲音復刻** —— 用 ElevenLabs / MiniMax / Qwen / CosyVoice 復刻出你自己的聲音（或在授權前提下復刻演講者的聲音），讓整份 deck 用 *你的聲音* 念出來。在 provider 控制檯復刻一次，把得到的 `voice_id` 傳進來，PPT Master 就會用這個音色逐頁朗讀備註並嵌入回 PPTX。詳見 [使用復刻音色 →](./docs/zh-TW/audio-narration.md#使用復刻音色)。

> **運作方式** —— PPT Master 是一套在 AI IDE（Claude Code / Cursor / VS Code + Copilot / Codebuddy 等）裡執行的工作流（一個 "skill"）。你在 IDE 的對話方塊裡跟 AI 說"用這份 PDF 做一份 PPT"，AI 按這套工作流在你本機生成一個真正可編輯的 `.pptx`。你不寫任何程式碼——IDE 只是你和 AI 對話的地方。
>
> **你要做的**：裝 Python、裝一個 AI IDE、把資料放進來。

PPT Master 不一樣：

- **真正的 PPT** — 如果一個檔案在 PowerPoint 裡打不開、不能編輯，它就不應該被叫做 PPT。PPT Master 輸出的每個元素都能直接點選修改
- **成本透明可控** — 工具免費開源，唯一成本是你自己的 AI 模型用量。當前主流 AI 工具都已轉向按量計費，你用多少付多少——PPT Master 不在此之外增加任何額外訂閱費用
- **資料不出本地** — 你的檔案不應該為了做一份 PPT 就被上傳到別人的伺服器。除與 AI 模型的對話外，全流程在你的電腦上完成
- **不鎖定平臺** — 你的工作流不應該被任何一家公司綁架。Claude Code、Cursor、VS Code Copilot 等均可驅動；Claude、GPT、Gemini、Kimi 等模型均可使用

市面上的 AI PPT 工具大致分四類，PPT Master 只做最後一類：

| 型別 | 產物形態 | 能在 PowerPoint 裡逐元素改嗎 |
|---|---|:---:|
| 模板填空 | 套模板的 PPTX | 部分可以，受模板限制 |
| 圖片式 | 一頁一張大圖拼成 PPTX | ❌ 整頁是圖片 |
| HTML 演示 | 網頁演示 | ❌ 不是 PPTX |
| **原生可編輯（PPT Master）** | **真 DrawingML 形狀、文字框、圖表** | ✅ 每個元素都能點開改 |



## 快速開始

### 1. 前置條件

**只需裝 Python 即可。** 其餘依賴透過 `pip install -r requirements.txt` 一次裝齊。

| 依賴 | 是否必須 | 用途 |
|------|:--------:|------|
| [Python](https://www.python.org/downloads/) 3.10+ | ✅ **必需** | 核心執行時——唯一真正需要安裝的東西 |

> **一句話總結** — 裝好 Python，跑一行 `pip install -r requirements.txt`，就可以開始生成 PPT 了。

<details open>
<summary><strong>Windows</strong> — 請看專門的手把手安裝指南 ⚠️</summary>

Windows 需要一些額外步驟（PATH 設定、執行策略等）。我們為 Windows 使用者寫了一份**手把手安裝指南**：

**📖 [Windows 安裝指南](./docs/zh-TW/windows-installation.md)** — 從零到跑通第一份 PPT，10 分鐘搞定。

簡要流程：從 [python.org](https://www.python.org/downloads/) 下載 Python → **安裝時勾選 "Add to PATH"** → `pip install -r requirements.txt` → 完成。
</details>

<details>
<summary><strong>macOS / Linux</strong> — 安裝即用</summary>

```bash
# macOS
brew install python
pip install -r requirements.txt

# Ubuntu / Debian
sudo apt install python3 python3-pip
pip install -r requirements.txt
```
</details>

<details>
<summary><strong>邊緣場景備用方案</strong> — 99% 的使用者用不到</summary>

**Pandoc** — 只在需要轉小眾格式時才裝：`.doc`、`.odt`、`.rtf`、`.tex`、`.rst`、`.org`、`.typ`。`.docx`、`.html`、`.epub`、`.ipynb` 已由 Python 原生處理，不需要 pandoc。

```bash
# macOS
brew install pandoc

# Ubuntu / Debian
sudo apt install pandoc
```
</details>

### 2. 選擇一個 Agent

PPT Master 在**任何具備 agent 能力**（可讀寫檔案、執行命令、持續多輪對話）的工具裡都能跑。

| 型別 | 代表工具 | 說明 |
|---|---|---|
| **IDE 內建 agent** | • VS Code 架構（含 [VS Code](https://code.visualstudio.com/) 本體及分支與衍生）：[Cursor](https://cursor.sh/)、Trae、Codebuddy IDE、[Windsurf](https://codeium.com/windsurf)、Void 等<br>• 其他架構：[Zed](https://zed.dev/) 等 | 編輯器原生整合 agent |
| **IDE 外掛 / 擴充套件** | [GitHub Copilot](https://github.com/features/copilot)、[Claude Code](https://claude.ai/code)（VS Code / JetBrains 擴充套件）、[Cline](https://cline.bot/)、[Continue](https://continue.dev/)、Roo Code、通義靈碼、CodeGeeX 等 | 裝在 VS Code / JetBrains 等宿主裡使用 |
| **CLI agent** | [Claude Code](https://claude.ai/code) CLI、[Codex CLI](https://github.com/openai/codex)、[Aider](https://aider.chat/)、Gemini CLI 等 | 終端裡執行，適合指令碼化 / 遠端 / 伺服器場景 |

> **模型推薦**：優先選 **Claude Opus / Sonnet**，搭配大上下文視窗和 `gpt-image-2` 生圖——原因見上方說明。


### 3. 配置專案

**方式 A — 下載 ZIP**（無需安裝 Git）：
[GitHub]([Local Repository]) → **Code → Download ZIP** · [AtomGit]([Local Repository]) → **克隆/下載 → 下載ZIP**（國內網速更快）

**方式 B — Git clone**（需先安裝 [Git](https://git-scm.com/downloads)）：

```bash
# GitHub
git clone [Repository URL]
# AtomGit（國內網速更快）
git clone [Repository URL]
cd ppt-master
```

然後安裝依賴：

```bash
pip install -r requirements.txt
```

日常更新（方式 A / B）：`python3 skills/ppt-master/scripts/update_repo.py`

> **方式 C — Skill marketplace**：倉庫已新增 `.claude-plugin/marketplace.json` 後設資料，可透過 [Claude Code plugin marketplace](https://code.claude.com/docs/en/plugin-marketplaces) 生態一行安裝：
>
> ```bash
> # 跨 agent CLI（Claude Code、Cursor、Codex 等）

> ```
>
> 上述兩種安裝方式都只會拉取 skill 檔案本身（不含完整倉庫），後處理指令碼仍需在安裝目錄跑 `pip install -r requirements.txt`。

### 4. 開始創作

**提供原始材料（推薦）：** 將 PDF、DOCX、圖片等檔案放入 `projects/` 目錄下，在 AI 聊天面板中告訴它使用哪些檔案。獲取路徑的最快方式：在檔案管理器或 IDE 側邊欄中右鍵檔案 → **複製路徑**（Copy Path / Copy Relative Path），直接貼上進聊天框。

```
你：請用 projects/q3-report/sources/report.pdf 這份檔案生成一份 PPT
```

**直接輸入內容：** 也可以把文字內容直接貼上進聊天視窗，AI 會根據這些內容生成 PPT。

```
你：請根據以下內容製作成 PPT：[貼上你的文字內容...]
```

兩種方式下 AI 都會先確認設計規範：

```
AI：好的，先確認設計規範：
   [模板] B) 自由設計
   [格式] PPT 16:9
   [頁數] 8-10 頁
   ...
```

AI 全程處理——內容分析、視覺設計、SVG 生成、PPTX 匯出。

> **輸出說明：** 原生形狀版 `.pptx`（可直接編輯）儲存至 `exports/<name>_<timestamp>.pptx`；`svg_output/` 始終映象到 `backup/<timestamp>/svg_output/`，便於歸檔或後續重跑。加 `--svg-snapshot` 時，額外在 `exports/` 內並排生成 SVG 快照版 pptx（詳見[常見問題](./docs/zh-TW/faq.md)）。需要 Office 2016+。

> **AI 迷失上下文？** 讓它先讀 `skills/ppt-master/SKILL.md`。

> **遇到問題？** 檢視 **[常見問題](./docs/zh-TW/faq.md)** — 涵蓋模型選擇、排版問題、匯出異常等，基於真實使用者反饋持續更新。

### 5. 圖片獲取（可選）

非使用者自帶圖片有兩條路徑，可在同一份 deck 裡按行混用：

需要 API 的功能統一透過 `.env` 配置。clone 安裝可以用 `cp .env.example .env`；skill marketplace 安裝建議使用持久的使用者級配置：

```bash
mkdir -p ~/.ppt-master
cp /path/to/installed/ppt-master/.env.example ~/.ppt-master/.env
```

PPT Master 會優先讀取當前程式環境變數，然後按順序讀取第一個存在的 `.env`：當前工作目錄、clone 倉庫根目錄、`~/.ppt-master/.env`。

**A) AI 生圖** — `image_gen.py`。設定 `IMAGE_BACKEND` 和對應 `*_API_KEY`（`OPENAI_API_KEY`、`GEMINI_API_KEY` 等），流程會自動呼叫。`python3 skills/ppt-master/scripts/image_gen.py --list-backends` 檢視完整後端清單。`gpt-image-2` 目前綜合質量最佳。

**B) 網路圖片搜尋** — `image_search.py`。**零配置**可用，但高質量使用建議配置 `PEXELS_API_KEY` / `PIXABAY_API_KEY`（都免費申請）。不配置時只使用 Openverse / Wikimedia Commons，適合作為兜底，但容易出現普通使用者上傳、構圖隨意、清晰度不穩定的圖片；配置後預設搜尋鏈會追加 Pexels / Pixabay，現代商業攝影、人物、辦公、生活方式和插畫類圖片質量會明顯更穩定。預設以圖片質量和匹配度優先，直接把 CC0、公有領域、Pexels / Pixabay 免署名許可、CC BY、CC BY-SA 一起納入候選；如果選中的圖片需要署名，Executor 會在該幻燈片自動新增小字署名。只有明確不能出現署名時，才使用 `--strict-no-attribution` 限制為免署名圖片。對視覺要求高的封面、產品圖、人物圖和品牌場景，優先順序建議是：使用者自帶高畫質素材 / AI 生圖 > 配置 Pexels / Pixabay 的網路搜尋 > 零配置網路搜尋。

> 完整說明：[`image-generator.md`](./skills/ppt-master/references/image-generator.md)（AI）·[`image-searcher.md`](./skills/ppt-master/references/image-searcher.md)（網路）。

---

## 檔案導航

| | 檔案 | 說明 |
|---|------|------|
| 🆚 | [為什麼選 PPT Master](./docs/zh-TW/why-ppt-master.md) | 與 Gamma、Copilot 等工具的對比 |
| 🪟 | [Windows 安裝指南](./docs/zh-TW/windows-installation.md) | Windows 使用者手把手安裝教程 |
| 📖 | [SKILL.md](./skills/ppt-master/SKILL.md) | 核心流程與規則 |
| 🎨 | [模板指南](./docs/zh-TW/templates-guide.md) | 選用、派生新模板（重點）、模板邊界；含 standard / fidelity 模式選型 |
| 📐 | [畫布格式](./skills/ppt-master/references/canvas-formats.md) | PPT 16:9、小紅書、朋友圈等 10+ 種格式 |
| 🎬 | [轉場與動畫](./docs/zh-TW/animations.md) | 頁間轉場和頁內元素入場動畫 |
| 🎙️ | [音訊旁白與影片匯出](./docs/zh-TW/audio-narration.md) | 90+ 語種 TTS 旁白、音訊嵌入 PPTX、匯出為 MP4 |
| � | [諮詢風格 PPT](./skills/ppt-master/workflows/consultant-ppt.md) | MBB 級證據分析、SCR 論證、8 種固定視覺風格、14 層門禁 QA |
| �🛠️ | [指令碼與工具](./skills/ppt-master/scripts/README.md) | 所有指令碼和命令 |
| 💼 | [示例](./examples/README.md) | 17 個專案，229 頁 |
| 🏗️ | [技術路線](./docs/zh-TW/technical-design.md) | 架構、設計哲學、為什麼選 SVG |
| ❓ | [常見問題](./docs/zh-TW/faq.md) | 模型選擇、費用、排版問題排查、自定義模板 |

---

