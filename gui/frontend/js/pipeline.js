/*
  PPT Master GUI - Pipeline Control & SSE Listener (pipeline.js)
*/

// Premium Custom Async Modal Engine
function showSmartGuidanceModal({ title, content, icon = '💡', actions = [] }) {
  return new Promise((resolve) => {
    const modal = document.getElementById('guidance-modal');
    const titleEl = document.getElementById('guidance-modal-title');
    const iconEl = document.getElementById('guidance-modal-icon');
    const bodyEl = document.getElementById('guidance-modal-body');
    const footerEl = document.getElementById('guidance-modal-footer');
    
    if (!modal || !titleEl || !iconEl || !bodyEl || !footerEl) {
      console.warn("Guidance modal elements not found in DOM.");
      // Fallback
      if (actions.length > 1) {
        const result = confirm(`${title}\n\n${content.replace(/<[^>]*>/g, '')}`);
        resolve(result ? actions[0].value : actions[1].value);
      } else {
        alert(`${title}\n\n${content.replace(/<[^>]*>/g, '')}`);
        resolve(actions[0] ? actions[0].value : true);
      }
      return;
    }
    
    // Set text and HTML contents
    titleEl.innerText = title;
    iconEl.innerText = icon;
    bodyEl.innerHTML = content;
    
    // Populate footer action buttons
    footerEl.innerHTML = '';
    actions.forEach(act => {
      const btn = document.createElement('button');
      btn.className = act.className || 'btn btn-secondary';
      btn.innerHTML = act.text;
      btn.style.minHeight = '44px';
      btn.style.padding = '8px 16px';
      btn.style.fontSize = '14px';
      btn.style.fontWeight = '600';
      btn.style.borderRadius = '8px';
      btn.style.cursor = 'pointer';
      btn.addEventListener('click', () => {
        modal.classList.remove('active');
        resolve(act.value);
      });
      footerEl.appendChild(btn);
    });
    
    // Open modal
    modal.classList.add('active');
  });
}

function showSmartAlert(title, content, icon = '💡') {
  return showSmartGuidanceModal({
    title: title,
    content: content,
    icon: icon,
    actions: [
      {
        text: '確定',
        value: true,
        className: 'btn btn-primary'
      }
    ]
  });
}

// Bind to window for global access
window.showSmartGuidanceModal = showSmartGuidanceModal;
window.showSmartAlert = showSmartAlert;

// Extract project directory name from path (/project/project_dir_name)
const pathSegments = window.location.pathname.split('/');
const projectDirName = pathSegments[pathSegments.length - 1];

let activePipeline = 'standard';
let eventSource = null;

document.addEventListener('DOMContentLoaded', () => {
  if (!projectDirName) {
    showSmartAlert('錯誤', '無法識別此專案的識別碼 (Project ID)，請返回儀表板重新點擊專案！', '❌').then(() => {
      window.location.href = '/';
    });
    return;
  }
  
  refreshProjectInfo();

  // Attach change listener to nblm-source dropdown to dynamically update NotebookLM guidance
  const nblmSourceEl = document.getElementById('nblm-source');
  if (nblmSourceEl) {
    nblmSourceEl.addEventListener('change', () => {
      if (window.currentProjectInfo) {
        updateGuidance(window.currentProjectInfo);
      }
    });
  }
});

// Switch between standard and notebooklm pipelines
function switchPipeline(pipeline) {
  activePipeline = pipeline;
  
  document.querySelectorAll('.tab-btn').forEach(btn => btn.classList.remove('active'));
  document.querySelectorAll('.pipeline-panel').forEach(panel => panel.classList.remove('active'));
  
  if (pipeline === 'standard') {
    document.querySelector('.tab-btn:nth-child(1)').classList.add('active');
    document.getElementById('panel-standard').classList.add('active');
  } else {
    document.querySelector('.tab-btn:nth-child(2)').classList.add('active');
    document.getElementById('panel-notebooklm').classList.add('active');
  }
}

// Refresh project information (sources, exports, status)
async function refreshProjectInfo() {
  try {
    const res = await fetch(`/api/projects/${projectDirName}/info?t=${Date.now()}`);
    if (!res.ok) throw new Error('Failed to load project details');
    
    const info = await res.json();
    window.currentProjectInfo = info; // Save globally
    
    // Update titles & headers
    document.getElementById('breadcrumb-project').innerText = info.name;
    document.getElementById('project-title').innerText = info.name;
    document.getElementById('project-subtitle').innerText = `目錄: ${info.dir_name} | 尺寸格式: ${info.format_name}`;
    
    // Set external SVG Editor Link
    const editorLink = document.getElementById('svg-editor-link');
    editorLink.href = `/project/${info.dir_name}/edit`;
    
    // Render sidebar sources list
    renderSources(info.source_files);
    
    // Render sidebar exports list
    renderExports(info.export_files);
    
    // Populate NotebookLM Select Dropdowns
    populateNotebookLMDropdowns(info.source_files);
    
    // Set active visual markers in Standard Timeline
    updateTimelineNodes(info);
    
    // Update Smart Guidance
    updateGuidance(info);
    
  } catch (error) {
    console.error('Error refreshing project info:', error);
    logToTerminal(`[SYSTEM ERROR] 無法同步專案屬性: ${error.message}`, 'error');
  }
}

// Update Standard Timeline checkmarks based on actual file state
function updateTimelineNodes(info) {
  // Step 2: Import Sources
  const importNode = document.getElementById('step-node-import');
  const importBadge = document.getElementById('badge-step-import');
  if (info.source_files && info.source_files.length > 0) {
    importNode.className = "step-node completed";
    importBadge.className = "badge badge-exported";
    importBadge.innerText = "已載入";
  } else {
    importNode.className = "step-node active";
    importBadge.className = "badge";
    importBadge.innerText = "待執行";
  }
  
  // Step 3: Split notes
  const splitNode = document.getElementById('step-node-split');
  const splitBadge = document.getElementById('badge-step-split');
  if (info.has_total_md && (info.has_split || info.svg_count > 0)) {
    // If outline split completed
    splitNode.className = "step-node completed";
    splitBadge.className = "badge badge-exported";
    splitBadge.innerText = "已分割";
  } else if (info.has_total_md) {
    splitNode.className = "step-node active";
    splitBadge.className = "badge badge-designing";
    splitBadge.innerText = "就緒";
  } else {
    splitNode.className = "step-node";
    splitBadge.className = "badge";
    splitBadge.innerText = "待執行";
  }
  
  // Step 4: AI Image Gen
  const imageNode = document.getElementById('step-node-image');
  const imageBadge = document.getElementById('badge-step-image');
  if (info.svg_count > 0) {
    imageNode.className = "step-node completed";
    imageBadge.className = "badge badge-exported";
    imageBadge.innerText = "配圖完成";
  } else if (info.has_total_md) {
    imageNode.className = "step-node active";
    imageBadge.className = "badge";
    imageBadge.innerText = "待生成";
  } else {
    imageNode.className = "step-node";
    imageBadge.className = "badge";
    imageBadge.innerText = "待執行";
  }
  
  // Step 5: SVG Finalize
  const finalizeNode = document.getElementById('step-node-finalize');
  const finalizeBadge = document.getElementById('badge-step-finalize');
  // If finalized svg has been processed (we check if exports exists or svg_count > 0)
  if (info.svg_count > 0 && info.export_files && info.export_files.length > 0) {
    finalizeNode.className = "step-node completed";
    finalizeBadge.className = "badge badge-exported";
    finalizeBadge.innerText = "優化完成";
  } else if (info.svg_count > 0) {
    finalizeNode.className = "step-node active";
    finalizeBadge.className = "badge";
    finalizeBadge.innerText = "待優化";
  } else {
    finalizeNode.className = "step-node";
    finalizeBadge.className = "badge";
    finalizeBadge.innerText = "待執行";
  }
  
  // Step 6: Export PPTX
  const exportNode = document.getElementById('step-node-export');
  const exportBadge = document.getElementById('badge-step-export');
  const downloadBtn = document.getElementById('btn-download-pptx');
  
  if (info.export_files && info.export_files.length > 0) {
    exportNode.className = "step-node completed";
    exportBadge.className = "badge badge-exported";
    exportBadge.innerText = "已匯出";
    downloadBtn.disabled = false;
  } else {
    exportNode.className = "step-node";
    exportBadge.className = "badge";
    exportBadge.innerText = "待執行";
    downloadBtn.disabled = true;
  }
  
  // Update NotebookLM badges
  const nblmSetupNode = document.getElementById('step-node-nblm-setup');
  const nblmSetupBadge = document.getElementById('badge-step-nblm-setup');
  if (info.has_notebooklm_sync) {
    nblmSetupNode.className = "step-node completed";
    nblmSetupBadge.className = "badge badge-exported";
    nblmSetupBadge.innerText = "同步完成";
  } else {
    nblmSetupNode.className = "step-node active";
    nblmSetupBadge.className = "badge";
    nblmSetupBadge.innerText = "待執行";
  }
  
  const nblmExportNode = document.getElementById('step-node-nblm-export');
  const nblmExportBadge = document.getElementById('badge-step-nblm-export');
  if (info.export_files && info.export_files.length > 0) {
    nblmExportNode.className = "step-node completed";
    nblmExportBadge.className = "badge badge-exported";
    nblmExportBadge.innerText = "匯出完成";
  } else if (info.has_notebooklm_sync) {
    nblmExportNode.className = "step-node active";
    nblmExportBadge.className = "badge";
    nblmExportBadge.innerText = "待匯出";
  } else {
    nblmExportNode.className = "step-node";
    nblmExportBadge.className = "badge";
    nblmExportBadge.innerText = "待執行";
  }
}

// Sidebars: Render files list
function renderSources(files) {
  const container = document.getElementById('source-list');
  if (!container) return;
  
  if (!files || files.length === 0) {
    container.innerHTML = `<li style="text-align: center; padding: 16px; color: var(--secondary-text); font-size: 13px;">無素材，請在步驟 2 上傳檔案</li>`;
    return;
  }
  
  let html = '';
  files.forEach(f => {
    html += `
      <li class="item-row">
        <div class="item-info">
          <svg class="item-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
          </svg>
          <span class="item-name" title="${f}">${f}</span>
        </div>
      </li>
    `;
  });
  container.innerHTML = html;
}

function renderExports(files) {
  const container = document.getElementById('export-list');
  if (!container) return;
  
  if (!files || files.length === 0) {
    container.innerHTML = `<li style="text-align: center; padding: 16px; color: var(--secondary-text); font-size: 13px;">尚未進行 PPTX 匯出編譯</li>`;
    return;
  }
  
  let html = '';
  files.forEach(f => {
    html += `
      <li class="item-row">
        <div class="item-info">
          <svg class="item-icon" style="color: var(--success);" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 21h10a2 2 0 002-2V9.414a1 1 0 00-.293-.707l-5.414-5.414A1 1 0 0012.586 3H7a2 2 0 00-2 2v14a2 2 0 002 2z" />
          </svg>
          <span class="item-name" title="${f}">${f}</span>
        </div>
        <a href="/api/projects/${projectDirName}/export" class="nav-link" style="padding: 4px 8px; font-size: 13px;" download>
          下載
        </a>
      </li>
    `;
  });
  container.innerHTML = html;
}

// Populate NotebookLM selection inputs
function populateNotebookLMDropdowns(files) {
  const sourceSelect = document.getElementById('nblm-source');
  const podcastSelect = document.getElementById('nblm-podcast');
  const transcriptSelect = document.getElementById('nblm-transcript');
  
  if (!sourceSelect) return;
  
  // Clear lists, keep standard first
  sourceSelect.innerHTML = '<option value="">-- 選擇 Study Guide / FAQ (MD) --</option>';
  podcastSelect.innerHTML = '<option value="">-- 選擇 Podcast 音訊 (MP3) [選填] --</option>';
  transcriptSelect.innerHTML = '<option value="">-- 選擇字幕 Transcript (TXT) [選填] --</option>';
  
  if (!files) return;
  
  files.forEach(f => {
    const ext = f.split('.').pop().toLowerCase();
    
    if (ext === 'md' || ext === 'markdown') {
      const opt = document.createElement('option');
      opt.value = f;
      opt.text = f;
      sourceSelect.appendChild(opt);
    } else if (ext === 'mp3' || ext === 'm4a') {
      const opt = document.createElement('option');
      opt.value = f;
      opt.text = f;
      podcastSelect.appendChild(opt);
    } else if (ext === 'txt') {
      const opt = document.createElement('option');
      opt.value = f;
      opt.text = f;
      transcriptSelect.appendChild(opt);
    }
  });
}

// Subprocess Command execution over Server-Sent Events (SSE)
function runPipelineStep(step) {
  if (eventSource) {
    showSmartAlert('系統忙碌中', '已有背景腳本正在執行，請稍候當前任務完成！', '⚠️');
    return;
  }
  
  clearConsole();
  setTerminalPulseState('running');
  logToTerminal(`[SYSTEM] 發起腳本執行步驟: ${step}...`, 'system');
  
  // Disable all execution buttons temporarily
  togglePipelineButtons(true);
  
  eventSource = new EventSource(`/api/projects/${projectDirName}/run/${step}`);
  
  eventSource.onmessage = (event) => {
    const data = event.data;
    
    if (data.startsWith('[START]')) {
      logToTerminal(data, 'system');
    } else if (data.startsWith('[SUCCESS]')) {
      logToTerminal(data, 'success');
      finishStepRun(true);
    } else if (data.startsWith('[ERROR]') || data.startsWith('[EXCEPTION]')) {
      logToTerminal(data, 'error');
      finishStepRun(false);
    } else {
      // Normal logs
      logToTerminal(data);
    }
  };
  
  eventSource.onerror = (err) => {
    console.error('SSE connection error:', err);
    logToTerminal('[SYSTEM ERROR] 即時日誌通道異常中斷。', 'error');
    finishStepRun(false);
  };
}

// Special notebooklm trigger
function runNotebookLMPipeline(phase) {
  if (eventSource) {
    showSmartAlert('系統忙碌中', '已有背景腳本正在執行，請稍候當前任務完成！', '⚠️');
    return;
  }
  
  let step = '';
  let urlParams = '';
  
  if (phase === 'setup') {
    const source = document.getElementById('nblm-source').value;
    const podcast = document.getElementById('nblm-podcast').value;
    const transcript = document.getElementById('nblm-transcript').value;
    
    if (!source) {
      showSmartAlert('尚未設定素材源', '請先選擇上傳的 NotebookLM 來源 Markdown 檔案！', '⚠️').then(() => {
        document.getElementById('nblm-source').focus();
      });
      return;
    }
    
    step = 'notebooklm_setup';
    urlParams = `?source=${encodeURIComponent(source)}&podcast=${encodeURIComponent(podcast)}&transcript=${encodeURIComponent(transcript)}`;
  } else {
    step = 'notebooklm_export';
  }
  
  clearConsole();
  setTerminalPulseState('running');
  logToTerminal(`[SYSTEM] 發起 NotebookLM Phase ${phase.toUpperCase()} 流水線...`, 'system');
  togglePipelineButtons(true);
  
  eventSource = new EventSource(`/api/projects/${projectDirName}/run/${step}${urlParams}`);
  
  eventSource.onmessage = (event) => {
    const data = event.data;
    if (data.startsWith('[START]')) {
      logToTerminal(data, 'system');
    } else if (data.startsWith('[SUCCESS]')) {
      logToTerminal(data, 'success');
      finishStepRun(true);
    } else if (data.startsWith('[ERROR]') || data.startsWith('[EXCEPTION]')) {
      logToTerminal(data, 'error');
      finishStepRun(false);
    } else {
      logToTerminal(data);
    }
  };
  
  eventSource.onerror = (err) => {
    console.error('SSE Error:', err);
    logToTerminal('[SYSTEM ERROR] 即時日誌通道異常中斷。', 'error');
    finishStepRun(false);
  };
}

function finishStepRun(isSuccess) {
  if (eventSource) {
    eventSource.onerror = null;
    eventSource.onmessage = null;
    eventSource.close();
    eventSource = null;
  }
  
  setTerminalPulseState(isSuccess ? 'success' : 'error');
  togglePipelineButtons(false);
  
  // Refresh stats and files
  refreshProjectInfo();
}

function togglePipelineButtons(disabled) {
  document.querySelectorAll('.step-control button, .notebooklm-workflow select').forEach(el => {
    el.disabled = disabled;
  });
}

// Log Terminal handlers
function logToTerminal(text, type = '') {
  const terminal = document.getElementById('console-terminal');
  if (!terminal) return;
  
  const div = document.createElement('div');
  div.className = `console-line ${type}`;
  
  // Parse ANSI colors
  div.innerHTML = parseAnsiColor(text);
  
  terminal.appendChild(div);
  
  // Auto scroll to bottom
  terminal.scrollTop = terminal.scrollHeight;
}

function clearConsole() {
  const terminal = document.getElementById('console-terminal');
  if (terminal) {
    terminal.innerHTML = '[SYSTEM] 日誌快取已清除。\n';
  }
}

function setTerminalPulseState(state) {
  const pulse = document.getElementById('terminal-pulse');
  if (!pulse) return;
  
  pulse.className = 'status-dot';
  if (state === 'running') {
    pulse.style.backgroundColor = 'var(--accent)';
    pulse.style.boxShadow = '0 0 10px var(--accent)';
  } else if (state === 'success') {
    pulse.style.backgroundColor = 'var(--success)';
    pulse.style.boxShadow = '0 0 10px var(--success)';
  } else if (state === 'error') {
    pulse.style.backgroundColor = 'var(--warning)';
    pulse.style.boxShadow = '0 0 10px var(--warning)';
  } else {
    pulse.style.backgroundColor = 'var(--secondary-text)';
    pulse.style.boxShadow = 'none';
  }
}

// Action helpers
function downloadLatestPPTX() {
  window.location.href = `/api/projects/${projectDirName}/export`;
}

function copyAIPrompt() {
  const prompt = `請擔任資深諮詢顧問與視覺傳達設計大師，檢視專案中的 sources 來源素材。
請參照 Consulting Box 諮詢卡片風格，設計專案簡報大綱架構：
1. 建立一個 total.md，內容為各張投影片的排版與講稿
2. 每一頁大綱使用前置雙位數標題，例如 "# 01 Cover" 或 "# 02 FAQ"
3. 善用 2x2 Grid 卡片與分欄雙排版，並以 markdown 表格或條列項目組織資訊，字體與佈局尺寸嚴格遵循 4px 對齊規範。
4. 提供 AI 配圖生成描述符註解，例如 "<!-- IMAGE: illustration, flat vectors, high contrast, royalty blue accent -->"
5. 為每一張投影片撰寫豐富、充實的備忘錄 (notes) 當作配音逐字講稿，並標記說話者。`;

  navigator.clipboard.writeText(prompt).then(() => {
    showSmartAlert('複製成功', 'AI 指令 Prompt 已成功複製到您的剪貼簿，請至 NotebookLM 或 Gemini 聊天視窗中貼上！', '📋');
  }).catch(err => {
    console.error('Copy failed:', err);
    showSmartAlert('複製失敗', '無法自動複製 Prompt 到剪貼簿，請手動複製上方文字框內容。', '❌');
  });
}

// Helper to clear all breathing lights
function clearAllPulses() {
  const ids = [
    'upload-dropzone',
    'btn-auto-standard',
    'svg-editor-link',
    'btn-download-pptx',
    'nblm-source',
    'btn-auto-notebooklm'
  ];
  ids.forEach(id => {
    const el = document.getElementById(id);
    if (el) {
      el.classList.remove('pulse-glow-accent', 'pulse-glow-success');
    }
  });
  
  // Also clear standard timeline step control buttons
  document.querySelectorAll('.step-control button, .step-node').forEach(el => {
    el.classList.remove('pulse-glow-accent', 'pulse-glow-success');
  });
}

// ─────────────────────────────────────────────────────────────
// Dynamic Smart Guidance and Instruction Generator (with Breathing Lights)
// ─────────────────────────────────────────────────────────────
function updateGuidance(info) {
  // Clear all pulsing glows first to avoid overlapping or outdated highlights
  clearAllPulses();

  // 1. Standard Pipeline Smart Guidance
  const standardTextEl = document.getElementById('guidance-text-standard');
  if (standardTextEl) {
    if (!info.source_files || info.source_files.length === 0) {
      standardTextEl.innerHTML = `⚠️ <strong>偵測到本專案尚無任何簡報素材。</strong><br>👉 <strong>指引與步驟：</strong>請點選下方的「步驟 2」區塊，將您的 Word (.docx)、PDF、Markdown (.md) 檔案拖曳上傳至此專案中！這是簡報生成的基礎素材。`;
      
      const dropzone = document.getElementById('upload-dropzone');
      if (dropzone) {
        dropzone.classList.add('pulse-glow-accent');
      }
    } else if (!info.has_total_md) {
      standardTextEl.innerHTML = `💡 <strong>素材檔案已成功載入！</strong><br>👉 <strong>指引與推薦操作：</strong>請直接點擊上方的<strong>「✨ 一鍵自動生成簡報」</strong>按鈕，系統將自動為您完成「步驟 3：分割大綱」並呼叫 AI 進行視覺佈局與 DrawingML 原生 PPTX 匯出！<br>若您希望微調簡報內容大綱，可以點擊「步驟 4」複製 AI 任務 Prompt 拷貝至您的 AI 聊天室，將大綱 total.md 重新定稿後上傳。`;
      
      const btnAuto = document.getElementById('btn-auto-standard');
      if (btnAuto) {
        btnAuto.classList.add('pulse-glow-accent');
      }
    } else if (info.svg_count === 0) {
      standardTextEl.innerHTML = `🎨 <strong>瑞士格線系統與大綱結構分割已完成！</strong><br>👉 <strong>指引與推薦操作：</strong>請點擊上方的<strong>「✨ 一鍵自動生成簡報」</strong>按鈕以啟動 AI 配圖生成與 SVG 設計圖層定稿！`;
      
      const btnAuto = document.getElementById('btn-auto-standard');
      if (btnAuto) {
        btnAuto.classList.add('pulse-glow-accent');
      }
    } else if (!info.export_files || info.export_files.length === 0) {
      standardTextEl.innerHTML = `⚡ <strong>設計圖層已完成編譯與定稿！</strong><br>👉 <strong>指引與指引操作：</strong><br>1. <strong>【推薦視覺微調】</strong>：您可以點選右上角的『編輯投影片 (SVG Editor)』按鈕進行視覺化互動調校（修改字體、形狀顏色、漸層、陰影邊框）；<br>2. <strong>【一鍵打包 PPTX】</strong>：如果您對當前版型滿意，請直接點擊上方的<strong>「✨ 一鍵自動生成簡報」</strong>按鈕，系統將完成 DrawingML 向量形狀編譯並自動打包下載！`;
      
      const btnAuto = document.getElementById('btn-auto-standard');
      if (btnAuto) {
        btnAuto.classList.add('pulse-glow-accent');
      }
      const editorLink = document.getElementById('svg-editor-link');
      if (editorLink) {
        editorLink.classList.add('pulse-glow-accent');
      }
    } else {
      standardTextEl.innerHTML = `🎉 <strong>恭喜！原生 PowerPoint DrawingML 簡報已成功匯出！</strong><br>👉 <strong>引導操作：</strong>您現在可以點擊右上角<strong>『下載簡報 PPTX』</strong>按鈕獲取該簡報！這是一個百分之百原生、字體與圖形完全可自由雙擊編輯的完美 PowerPoint！`;
      
      const downloadBtn = document.getElementById('btn-download-pptx');
      if (downloadBtn) {
        downloadBtn.classList.add('pulse-glow-success');
      }
    }
  }

  // 2. NotebookLM Pipeline Smart Guidance
  const notebooklmTextEl = document.getElementById('guidance-text-notebooklm');
  if (notebooklmTextEl) {
    const selectedSource = document.getElementById('nblm-source') ? document.getElementById('nblm-source').value : "";
    
    // Check if there are any MD files in sources
    const hasMdFiles = info.source_files && info.source_files.some(f => f.toLowerCase().endsWith('.md') || f.toLowerCase().endsWith('.markdown'));

    if (!hasMdFiles) {
      notebooklmTextEl.innerHTML = `⚠️ <strong>尚未上傳 NotebookLM 來源 Markdown。</strong><br>👉 <strong>指引與推薦操作：</strong>請先於「步驟 2」將您從 NotebookLM 匯出的 Markdown 學習指南/FAQ 檔案拖曳上傳至此專案，再進行後續對齊設定！`;
      
      const dropzone = document.getElementById('upload-dropzone');
      if (dropzone && activePipeline === 'notebooklm') {
        dropzone.classList.add('pulse-glow-accent');
      }
    } else if (!selectedSource) {
      notebooklmTextEl.innerHTML = `⚠️ <strong>尚未設定 NotebookLM 素材源。</strong><br>👉 <strong>指引與推薦操作：</strong>請先在下方的<strong>「NotebookLM 來源檔案」</strong>下拉選單中選擇您剛剛上傳的 Markdown 筆記檔案！`;
      
      const nblmSelect = document.getElementById('nblm-source');
      if (nblmSelect && activePipeline === 'notebooklm') {
        nblmSelect.classList.add('pulse-glow-accent');
      }
    } else if (!info.has_notebooklm_sync) {
      notebooklmTextEl.innerHTML = `🎙️ <strong>語音對齊素材已選定！</strong><br>👉 <strong>指引與推薦操作：</strong>請直接點選上方的<strong>「✨ 一鍵自動對齊與匯出」</strong>按鈕，系統將自動解析 Study Guide 筆記為雙欄卡片版型，同時解析 Podcast 對話時間軸完成切片，產出對齊的 Swiss-Grid 骨架！`;
      
      const btnAutoNblm = document.getElementById('btn-auto-notebooklm');
      if (btnAutoNblm && activePipeline === 'notebooklm') {
        btnAutoNblm.classList.add('pulse-glow-accent');
      }
    } else if (!info.export_files || info.export_files.length === 0) {
      notebooklmTextEl.innerHTML = `⏳ <strong>Phase A 語音同步與 Consulting-Box 大綱已生成！</strong><br>👉 <strong>指引與推薦操作：</strong>如果您此時需要進行視覺美化與設計，請點擊右上角『編輯投影片 (SVG Editor)』進行調校；若您希望直接得到簡報，請直接點擊上方的<strong>「✨ 一鍵自動對齊與匯出」</strong>繼續以完成 Phase B 後製與 PPTX 打包匯出！`;
      
      const btnAutoNblm = document.getElementById('btn-auto-notebooklm');
      if (btnAutoNblm && activePipeline === 'notebooklm') {
        btnAutoNblm.classList.add('pulse-glow-accent');
      }
      const editorLink = document.getElementById('svg-editor-link');
      if (editorLink && activePipeline === 'notebooklm') {
        editorLink.classList.add('pulse-glow-accent');
      }
    } else {
      notebooklmTextEl.innerHTML = `🎉 <strong>恭喜！一鍵語音同步 DrawingML 原生簡報已成功打包！</strong><br>👉 <strong>引導操作：</strong>點選右上角的<strong>『下載簡報 PPTX』</strong>按鈕獲取成果！您本人的/雙人 Podcast 切片語音已經原生嵌入對應的投影片音軌中，打開簡報即可連動播放！`;
      
      const downloadBtn = document.getElementById('btn-download-pptx');
      if (downloadBtn) {
        downloadBtn.classList.add('pulse-glow-success');
      }
    }
  }
}

// ─────────────────────────────────────────────────────────────
// Promise-Based Subprocess Command Runner over Server-Sent Events (SSE)
// ─────────────────────────────────────────────────────────────
function runPipelineStepPromise(step, urlParams = "") {
  return new Promise((resolve, reject) => {
    if (eventSource) {
      reject(new Error("已有背景腳本正在執行，請稍候。"));
      return;
    }
    
    clearConsole();
    setTerminalPulseState('running');
    logToTerminal(`[SYSTEM] 發起自動步驟: ${step}...`, 'system');
    togglePipelineButtons(true);
    
    eventSource = new EventSource(`/api/projects/${projectDirName}/run/${step}${urlParams}`);
    
    eventSource.onmessage = (event) => {
      const data = event.data;
      
      if (data.startsWith('[START]')) {
        logToTerminal(data, 'system');
      } else if (data.startsWith('[SUCCESS]')) {
        logToTerminal(data, 'success');
        if (eventSource) {
          eventSource.onerror = null;
          eventSource.onmessage = null;
          eventSource.close();
          eventSource = null;
        }
        setTerminalPulseState('success');
        togglePipelineButtons(false);
        resolve(true);
      } else if (data.startsWith('[ERROR]') || data.startsWith('[EXCEPTION]')) {
        logToTerminal(data, 'error');
        if (eventSource) {
          eventSource.onerror = null;
          eventSource.onmessage = null;
          eventSource.close();
          eventSource = null;
        }
        setTerminalPulseState('error');
        togglePipelineButtons(false);
        reject(new Error(data));
      } else {
        logToTerminal(data);
      }
    };
    
    eventSource.onerror = (err) => {
      console.error('SSE connection error:', err);
      logToTerminal('[SYSTEM ERROR] 即時日誌通道異常中斷。', 'error');
      if (eventSource) {
        eventSource.onerror = null;
        eventSource.onmessage = null;
        eventSource.close();
        eventSource = null;
      }
      setTerminalPulseState('error');
      togglePipelineButtons(false);
      reject(new Error("即時日誌通道異常中斷。"));
    };
  });
}

// ─────────────────────────────────────────────────────────────
// One-Click Automated Pipeline Orchestrators (with Custom Choice Modals)
// ─────────────────────────────────────────────────────────────
async function startAutoStandardPipeline() {
  await refreshProjectInfo();
  
  if (!window.currentProjectInfo) {
    showSmartAlert("錯誤", "無法成功獲取當前專案的屬性與狀態資訊，請點擊『重新整理』重試！", "❌");
    return;
  }
  
  const info = window.currentProjectInfo;
  
  if (!info.source_files || info.source_files.length === 0) {
    showSmartAlert(
      "無素材檔案",
      "專案中目前沒有任何素材檔案。<br><br>👉 <strong>操作指引：</strong>請先於「步驟 2」拖曳或點選上傳您的 Word (.docx)、PDF 或 Markdown (.md) 檔案！這是簡報生成的基礎素材。",
      "⚠️"
    );
    return;
  }
  
  let runSplit = !info.has_total_md;
  let splitParams = "";
  
  // Clean Rebuild vs Keep Outline choice dialog
  if (info.has_total_md) {
    const choice = await showSmartGuidanceModal({
      title: '偵測到現有大綱 (total.md)',
      icon: '❓',
      content: `<p>偵測到本專案已存在大綱結構檔案！請選擇您希望一鍵執行的模式：</p>
                <div style="margin-top: 14px; padding: 12px; border-radius: 8px; background-color: var(--bg-base); font-size: 13px; line-height: 1.6;">
                  <p><strong>1. 全新乾淨重建 (Clean Rebuild)</strong>: 重新解析並覆蓋現有大綱，適合上傳了新素材或需要全面重新排版的情況。系統將清空舊有投影片。</p>
                  <p style="margin-top: 6px;"><strong>2. 保留現有大綱 (Keep Outline)</strong>: 保留您已微調的大綱內容，直接執行後續的 AI 配圖、設計定稿與 DrawingML 匯出打包。</p>
                </div>`,
      actions: [
        { text: '全新乾淨重建', value: 'rebuild', className: 'btn btn-primary' },
        { text: '保留現有大綱', value: 'keep', className: 'btn btn-secondary' },
        { text: '取消', value: 'cancel', className: 'btn btn-secondary' }
      ]
    });
    
    if (choice === 'cancel') {
      logToTerminal("[AUTO PIPELINE] ⏳ 使用者取消了一鍵自動流水線執行。", "system");
      return;
    } else if (choice === 'rebuild') {
      runSplit = true;
      splitParams = "?rebuild=true";
    } else {
      runSplit = false;
    }
  }
  
  try {
    // Stage 1: Split outline (if needed)
    if (runSplit) {
      logToTerminal("[AUTO PIPELINE] 🚀 正在自動執行步驟一：大綱結構分割 (split)...", "system");
      await runPipelineStepPromise('split', splitParams);
      await refreshProjectInfo();
    } else {
      logToTerminal("[AUTO PIPELINE] 📝 已跳過大綱切割，保留現有 total.md 進度。", "system");
    }
    
    // Stage 2: AI Image Gen (if SVGs are not generated yet)
    if (window.currentProjectInfo.svg_count === 0) {
      logToTerminal("[AUTO PIPELINE] 🚀 正在自動執行步驟二：AI 配圖與批量繪圖 (image_gen)...", "system");
      await runPipelineStepPromise('image_gen');
      await refreshProjectInfo();
    } else {
      logToTerminal("[AUTO PIPELINE] 🎨 偵測到已有投影片 SVG 骨架，跳過 AI 配圖重繪。", "system");
    }
    
    // Stage 3: SVG Finalize
    logToTerminal("[AUTO PIPELINE] 🚀 正在自動執行步驟三：設計圖層定稿優化 (finalize)...", "system");
    await runPipelineStepPromise('finalize');
    await refreshProjectInfo();
    
    // Stage 4: Export PPTX
    logToTerminal("[AUTO PIPELINE] 🚀 正在自動執行步驟四：匯出 DrawingML PPTX (export)...", "system");
    await runPipelineStepPromise('export');
    await refreshProjectInfo();
    
    logToTerminal("[AUTO PIPELINE] 🎉 一鍵自動生成流水線執行成功！", "success");
    
    // Show premium alert with beautiful actions
    const afterSuccess = await showSmartGuidanceModal({
      title: "一鍵簡報生成成功！",
      icon: "🎉",
      content: `<p>完美的可編輯 Office 原生 PowerPoint 簡報已經編譯完成！</p>
                <div style="margin-top: 14px; padding: 12px; border-radius: 8px; background-color: var(--bg-base); font-size: 13px; line-height: 1.6;">
                  <p>💡 <strong>系統後續操作指引：</strong></p>
                  <p>1. 點擊 <strong>「下載簡報 PPTX」</strong> 即可取得 100% 原生向量形狀與可二次自由編輯字型的簡報檔案！</p>
                  <p style="margin-top: 6px;">2. 若想進行細部視覺調校，可點選 <strong>「編輯投影片 (SVG Editor)」</strong> 調整漸層、形狀或顏色，並可隨時回來重新一鍵匯出打包！</p>
                </div>`,
      actions: [
        { text: '📥 下載簡報 PPTX', value: 'download', className: 'btn btn-primary' },
        { text: '🎨 編輯投影片 (SVG Editor)', value: 'edit', className: 'btn btn-secondary' },
        { text: '關閉', value: 'close', className: 'btn btn-secondary' }
      ]
    });
    
    if (afterSuccess === 'download') {
      downloadLatestPPTX();
    } else if (afterSuccess === 'edit') {
      window.open(`/project/${window.currentProjectInfo.dir_name}/edit`, '_blank');
    }
  } catch (err) {
    console.error("Auto pipeline failed:", err);
    showSmartAlert(
      "流水線執行中斷",
      "一鍵自動執行在步驟中發生錯誤而中斷。<br><br><strong>錯誤原因：</strong>" + err.message + "<br><br>👉 請參考右側的「即時執行終端機 (Live Log)」日誌以進行排查與修復！",
      "❌"
    );
  }
}

async function startAutoNotebookLMPipeline() {
  const source = document.getElementById('nblm-source').value;
  const podcast = document.getElementById('nblm-podcast').value;
  const transcript = document.getElementById('nblm-transcript').value;
  
  if (!source) {
    showSmartAlert(
      "尚未設定素材源",
      "請先在下方「設定素材對齊源」中，選擇上傳的 NotebookLM Markdown 學習指南檔案 (MD)！",
      "⚠️"
    ).then(() => {
      document.getElementById('nblm-source').focus();
    });
    return;
  }
  
  const urlParams = `?source=${encodeURIComponent(source)}&podcast=${encodeURIComponent(podcast)}&transcript=${encodeURIComponent(transcript)}`;
  
  try {
    // Phase A: Setup & sync
    logToTerminal("[AUTO PIPELINE] 🚀 正在自動執行 Phase A：語音對齊與大綱解析 (notebooklm_setup)...", "system");
    await runPipelineStepPromise('notebooklm_setup', urlParams);
    await refreshProjectInfo();
    
    // Ask user with elegant instructions before compiling to PPTX
    const userProceed = await showSmartGuidanceModal({
      title: "🎙️ Phase A 執行成功！",
      icon: "🎙️",
      content: `<p><strong>語音對齊、時間軸定時與 Consulting Box 瑞士格線骨架已生成！</strong></p>
                <div style="margin-top: 14px; padding: 12px; border-radius: 8px; background-color: var(--bg-base); font-size: 13px; line-height: 1.6;">
                  <p>👉 <strong>請選擇下一步操作：</strong></p>
                  <p>1. <strong>直接匯出簡報 (推薦)</strong>: 系統將自動進行 Phase B 定稿、並打包 DrawingML PowerPoint 簡報與 Podcast 音訊。</p>
                  <p style="margin-top: 6px;">2. <strong>暫停微調設計</strong>: 暫停一鍵流水線，您可以先點擊右上角的「編輯投影片 (SVG Editor)」進行版面、字體或漸層微調，微調完畢後再手動執行 Phase B 匯出。</p>
                </div>`,
      actions: [
        { text: '直接匯出簡報', value: true, className: 'btn btn-primary' },
        { text: '暫停微調設計', value: false, className: 'btn btn-secondary' }
      ]
    });
    
    if (userProceed) {
      logToTerminal("[AUTO PIPELINE] 🚀 正在自動執行 Phase B：合併語音切片並編譯匯出 PPTX (notebooklm_export)...", "system");
      await runPipelineStepPromise('notebooklm_export');
      await refreshProjectInfo();
      logToTerminal("[AUTO PIPELINE] 🎉 NotebookLM 語音同步流水線執行成功！", "success");
      
      const afterSuccess = await showSmartGuidanceModal({
        title: "語音同步簡報打包成功！",
        icon: "🎉",
        content: `<p>一鍵雙人 Podcast 語音同步與 DrawingML 原生簡報已成功打包！</p>
                  <div style="margin-top: 14px; padding: 12px; border-radius: 8px; background-color: var(--bg-base); font-size: 13px; line-height: 1.6;">
                    <p>💡 <strong>系統後續操作指引：</strong></p>
                    <p>原生音軌與各頁投影片的播放定時已完美嵌入 PPTX 簡報中。您現在可以直接下載簡報，在 PowerPoint 中打開即可連動播放！</p>
                  </div>`,
        actions: [
          { text: '📥 立即下載簡報', value: 'download', className: 'btn btn-primary' },
          { text: '關閉', value: 'close', className: 'btn btn-secondary' }
        ]
      });
      
      if (afterSuccess === 'download') {
        downloadLatestPPTX();
      }
    } else {
      logToTerminal("[AUTO PIPELINE] ⏳ 已應您的要求暫停一鍵執行。您可以點擊右上角『編輯投影片 (SVG Editor)』進行視覺設計，設計完畢後，點選左側「Phase B：整合 SVG 向量並打包 PPTX」之按鈕，即可完成最終簡報打包！", "system");
    }
  } catch (err) {
    console.error("Auto NotebookLM pipeline failed:", err);
    showSmartAlert(
      "一鍵對齊執行中斷",
      "一鍵語音對齊執行在步驟中發生錯誤而中斷。<br><br><strong>錯誤原因：</strong>" + err.message + "<br><br>👉 請根據即時終端機日誌進行排查與調校！",
      "❌"
    );
  }
}

