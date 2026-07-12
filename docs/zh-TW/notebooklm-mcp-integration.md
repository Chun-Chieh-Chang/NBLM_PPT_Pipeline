---
description: 說明如何在 Trae IDE (VS Code 架構) 中註冊 notebooklm-py 的 MCP Server，讓 AI agent 直接呼叫 NotebookLM 工具。
---

# MCP 整合指南 — Trae IDE + NotebookLM

> 本文說明如何在 Trae IDE 中註冊 `notebooklm-py` 的 MCP Server，讓 AI agent 能直接呼叫 NotebookLM 的 32 個工具（notebook 管理、來源新增、聊天、產物生成等）。

## 前置條件

1. **Trae IDE** 已安裝（基於 VS Code 架構）
2. **Python 3.10+** 已安裝
3. **uv** 已安裝（用於執行 uvx）：
   ```bash
   pip install uv
   ```

## Step 1: 安裝 notebooklm-py

```bash
cd d:\Self-developed_Apps\NBLM_PPT_Pipeline
pip install "notebooklm-py[browser,mcp]"
```

## Step 2: 認證

```bash
notebooklm login   # 開啟瀏覽器進行 Google OAuth
notebooklm list    # 驗證認證是否成功
```

## Step 3: 在 Trae IDE 中註冊 MCP Server

Trae IDE 使用 VS Code 的 MCP 配置格式。找到或建立 Trae 的 MCP 設定檔：

### 方式 A：使用 Trae 內建設定 UI

1. 開啟 Trae IDE 設定 (`Ctrl+,`)
2. 搜尋 "mcp" 或 "Model Context Protocol"
3. 找到 MCP Server 設定區域
4. 新增一個新的 MCP Server：

```json
{
  "mcpServers": {
    "notebooklm": {
      "command": "uvx",
      "args": ["--from", "notebooklm-py[mcp]", "notebooklm-mcp"]
    }
  }
}
```

### 方式 B：手動編輯設定檔

Trae IDE 的 MCP 設定通常位於：

- **Windows**: `%APPDATA%\Trae\User\globalStorage\settings.json` 或專案級的 `.trae\settings.json`
- **macOS**: `~/Library/Application Support/Trae/User/globalStorage/settings.json`
- **Linux**: `~/.config/Trae/User/globalStorage/settings.json`

在設定檔中加入：

```json
{
  "mcp.servers": {
    "notebooklm": {
      "command": "uvx",
      "args": ["--from", "notebooklm-py[mcp]", "notebooklm-mcp"]
    }
  }
}
```

### 方式 C：使用自動安裝指令

notebooklm-py 提供自動安裝指令：

```bash
notebooklm mcp install cursor
# 注意：cursor 指令會寫入適用的 MCP 設定檔，
# 如果 Trae 使用相同的設定格式，此指令可能適用。
# 否則請使用方式 A 或 B。
```

## Step 4: 重啟 Trae IDE

重新啟動 Trae IDE 以載入新的 MCP Server 設定。

## Step 5: 驗證整合

在 Trae 的 AI 對話中測試：

1. 輸入："列出可用的 NotebookLM 工具"
2. AI 應該能看到 `notebook_create`、`source_add`、`chat_ask`、`studio_generate` 等 32 個工具
3. 嘗試："用 NotebookLM 分析 projects/my-project/sources/ 中的檔案"

## 可用工具列表

MCP Server 暴露以下工具類別：

### Notebook 管理
- `notebook_create` — 建立新 notebook
- `notebook_list` — 列出所有 notebooks
- `notebook_rename` — 重新命名 notebook
- `notebook_delete` — 刪除 notebook

### 來源管理
- `source_add` — 新增來源（URL / 文字 / 檔案 / YouTube / Drive）
- `source_list` — 列出來源
- `source_delete` — 刪除來源
- `source_fulltext` — 取得來源完整文字
- `source_guide` — 取得來源摘要指南

### 聊天與研究
- `chat_ask` — 提問（帶引用）
- `chat_history` — 查看對話歷史
- `research_start` — 啟動網路研究
- `research_status` — 檢查研究狀態

### 產物生成
- `studio_generate` — 生成產物（podcast / video / slide-deck / report / quiz / flashcards）
- `studio_status` — 檢查產物狀態
- `studio_download` — 下載產物
- `studio_delete` — 刪除產物

### 筆記管理
- `note_create` — 建立筆記
- `note_list` — 列出筆記
- `note_rename` — 重新命名筆記
- `note_delete` — 刪除筆記

## 進階設定

### 多帳號隔離

如需同時使用多個 Google 帳號：

```bash
# 建立新 profile
notebooklm profile create work
notebooklm -p work login

# 在 MCP 設定中指定 profile
{
  "mcp.servers": {
    "notebooklm-work": {
      "command": "uvx",
      "args": ["--from", "notebooklm-py[mcp]", "notebooklm-mcp", "--profile", "work"]
    }
  }
}
```

### 環境變數

| 變數 | 用途 |
|------|------|
| `NOTEBOOKLM_HOME` | 自訂設定目錄（預設 `~/.notebooklm`） |
| `NOTEBOOKLM_PROFILE` | 活躍 profile 名稱（預設 `default`） |
| `NOTEBOOKLM_AUTH_JSON` | 內嵌認證 JSON（適合 CI/CD） |
| `NOTEBOOKLM_MCP_TOKEN` | HTTP 傳輸的 bearer token |

### Strict IDs 模式

在自動化流程中，建議啟用 strict IDs 模式以避免名稱解析的不確定性：

```bash
export NOTEBOOKLM_MCP_STRICT_IDS=1
```

## 疑難排解

### 問題：MCP Server 無法啟動

**原因**：uvx 找不到或 notebooklm-py 未正確安裝。

**解決**：
```bash
# 確認安裝
pip show notebooklm-py

# 手動測試
uvx --from "notebooklm-py[mcp]" notebooklm-mcp --help

# 確認認證
notebooklm auth check --test --json
```

### 問題：認證過期

**解決**：
```bash
# 伺服器端刷新（推薦）
notebooklm auth refresh

# 或從瀏覽器重新提取 cookies
notebooklm auth refresh --browser-cookies chrome
```

### 問題：Trae IDE 看不到 MCP 工具

**檢查清單**：
1. 確認 MCP 設定檔路徑正確
2. 確認 Trae IDE 已完全重啟（不只是重新載視窗）
3. 檢查 Trae 的開發者工具中是否有 MCP 連線錯誤訊息
4. 確認 `uvx` 可在系統 PATH 中找到：
   ```bash
   where uvx   # Windows
   which uvx   # macOS/Linux
   ```

## 與 PPT Master 工作流的協同

註冊 MCP Server 後，AI agent 可以在 PPT Master 流程中直接呼叫 NotebookLM：

```
使用者：用 NotebookLM 先分析這些 PDF，然後做 PPT

AI：
1. [透過 MCP] notebook_create("PPT-Analysis")
2. [透過 MCP] source_add(notebook="PPT-Analysis", source_type="file", path="./sources/report.pdf")
3. [透過 MCP] chat_ask(notebook="PPT-Analysis", question="請整理出 5 個關鍵洞察")
4. [結果] 將 Gemini 的分析結果餵入 SKILL.md Step 2
```

這比手動執行 CLI 指令更流暢，因為 AI agent 可以直接在對話中調用 MCP 工具。
