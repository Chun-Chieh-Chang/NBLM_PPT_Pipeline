/*
  PPT Master GUI - Dashboard Logic (dashboard.js)
*/

document.addEventListener('DOMContentLoaded', () => {
  loadProjects();
  checkSkillsBuilderStatus();
});

// Load and render all project cards
async function loadProjects() {
  const listContainer = document.getElementById('project-list');
  if (!listContainer) return;
  
  try {
    const response = await fetch('/api/projects');
    const projects = await response.json();
    
    // Update stats
    document.getElementById('stats-total').innerText = projects.length;
    const exportedCount = projects.filter(p => p.state === 'Exported').length;
    document.getElementById('stats-exported').innerText = exportedCount;
    
    if (projects.length === 0) {
      listContainer.innerHTML = `
        <div style="grid-column: 1 / -1; text-align: center; padding: 48px; border: 1px dashed var(--border); border-radius: 16px; background-color: var(--surface);">
          <svg style="width: 48px; height: 48px; color: var(--secondary-text); margin-bottom: 12px;" fill="none" stroke="currentColor" viewBox="0 0 24 24" stroke-width="2">
            <path stroke-linecap="round" stroke-linejoin="round" d="M9 13h6m-3-3v6m-9 1V4a2 2 0 012-2h6l2 2h6a2 2 0 012 2v8a2 2 0 01-2 2H5a2 2 0 01-2-2z" />
          </svg>
          <p style="font-size: 16px; font-weight: 600; color: var(--primary-text);">目前尚未建立任何簡報專案</p>
          <p style="font-size: 13px; color: var(--secondary-text); margin-top: 4px; margin-bottom: 16px;">
            按右上方按鈕或下方按鈕來建立您的第一個 PPT 專案。
          </p>
          <button class="btn btn-primary" onclick="openCreateModal()">立即建立新專案</button>
        </div>
      `;
      return;
    }
    
    let html = '';
    projects.forEach(project => {
      // Determine badge class and label
      let badgeClass = '';
      let badgeText = '';
      let completionPercent = 0;
      
      switch (project.state) {
        case 'Exported':
          badgeClass = 'badge-exported';
          badgeText = '已匯出 PPTX';
          completionPercent = 100;
          break;
        case 'Designing':
          badgeClass = 'badge-designing';
          badgeText = 'SVG 製作中';
          completionPercent = project.svg_count > 0 ? Math.min(85, 30 + project.svg_count * 10) : 40;
          break;
        case 'Outline Ready':
          badgeClass = 'badge-designing';
          badgeText = '大綱已解析';
          completionPercent = 25;
          break;
        case 'Sources Loaded':
          badgeClass = '';
          badgeText = '素材已載入';
          completionPercent = 15;
          break;
        default:
          badgeClass = '';
          badgeText = '已初始化';
          completionPercent = 5;
      }
      
      html += `
        <div class="card">
          <div class="card-header">
            <div>
              <h3 class="card-title">${project.name}</h3>
              <p style="font-size: 13px; color: var(--secondary-text); font-family: var(--font-mono); margin-top: 4px;">
                ${project.dir_name}
              </p>
            </div>
            <span class="badge ${badgeClass}">${badgeText}</span>
          </div>
          
          <div class="card-meta">
            <span>
              <strong>尺寸:</strong> ${project.format_name}
            </span>
            <span>
              <strong>SVG 數:</strong> ${project.svg_count}
            </span>
            <span>
              <strong>素材數:</strong> ${project.source_count}
            </span>
          </div>
          
          <div class="card-progress">
            <div class="progress-info">
              <span>流水線進度</span>
              <span>${completionPercent}%</span>
            </div>
            <div class="progress-bar-container">
              <div class="progress-bar" style="width: ${completionPercent}%"></div>
            </div>
          </div>
          
          <div class="card-actions">
            <a href="/project/${project.dir_name}" class="btn btn-primary" style="flex: 1; text-align: center;">
              開啟工作台
            </a>
            ${project.svg_count > 0 
              ? `<a href="/project/${project.dir_name}/edit" target="_blank" class="btn btn-secondary" title="開啟 SVG 即時預覽">
                  <svg width="18" height="18" fill="none" stroke="currentColor" viewBox="0 0 24 24" stroke-width="2">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
                    <path stroke-linecap="round" stroke-linejoin="round" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z" />
                  </svg>
                 </a>`
              : ''
            }
            <button class="btn btn-secondary" onclick="deleteProject('${project.dir_name}', '${project.name}')" title="刪除簡報專案" style="border-color: rgba(239, 68, 68, 0.4); color: var(--warning); padding: 8px 12px; display: flex; align-items: center; justify-content: center; transition: all 0.2s ease;" onmouseover="this.style.backgroundColor='rgba(239, 68, 68, 0.15)'; this.style.borderColor='var(--warning)'" onmouseout="this.style.backgroundColor='transparent'; this.style.borderColor='rgba(239, 68, 68, 0.4)'">
              <svg width="18" height="18" fill="none" stroke="currentColor" viewBox="0 0 24 24" stroke-width="2">
                <path stroke-linecap="round" stroke-linejoin="round" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
              </svg>
            </button>
          </div>
        </div>
      `;
    });
    
    listContainer.innerHTML = html;
    
  } catch (error) {
    console.error('Error fetching projects:', error);
    listContainer.innerHTML = `
      <div style="grid-column: 1 / -1; text-align: center; padding: 48px; color: var(--warning); border: 1px solid var(--border); border-radius: 16px;">
        <p style="font-weight: 700; font-size: 16px;">讀取專案發生錯誤</p>
        <p style="font-size: 13px; color: var(--secondary-text); margin-top: 4px;">請確認後端 Python Flask 伺服器正在執行，並重試。</p>
      </div>
    `;
  }
}

// Check SkillsBuilder integration status
async function checkSkillsBuilderStatus() {
  const container = document.getElementById('stats-skills');
  if (!container) return;
  
  try {
    const response = await fetch('/api/skillsbuilder/status');
    const status = await response.json();
    
    if (status.integrated) {
      container.innerHTML = `
        <span class="status-dot active"></span>
        <span style="font-size: 14px; font-weight: 600; color: var(--success);">雙向對齊正常</span>
      `;
    } else if (status.skills_builder_exists) {
      container.innerHTML = `
        <span class="status-dot inactive"></span>
        <span style="font-size: 14px; font-weight: 600; color: var(--accent);">已偵測 (未同步)</span>
      `;
    } else {
      container.innerHTML = `
        <span class="status-dot inactive" style="background-color: var(--warning);"></span>
        <span style="font-size: 14px; font-weight: 600; color: var(--secondary-text);">未啟用</span>
      `;
    }
  } catch (e) {
    container.innerHTML = `
      <span class="status-dot inactive" style="background-color: var(--warning);"></span>
      <span style="font-size: 14px; font-weight: 600; color: var(--secondary-text);">連線中斷</span>
    `;
  }
}

// Modal Form Controllers
function openCreateModal() {
  document.getElementById('create-modal').classList.add('active');
  document.getElementById('project-name').value = '';
  document.getElementById('project-name').focus();
}

function closeCreateModal() {
  document.getElementById('create-modal').classList.remove('active');
}

async function submitCreateProject() {
  const nameInput = document.getElementById('project-name');
  const formatSelect = document.getElementById('project-format');
  
  const name = nameInput.value.trim();
  const format = formatSelect.value;
  
  if (!name) {
    alert('請輸入專案名稱！');
    nameInput.focus();
    return;
  }
  
  // Update button visual state
  const btn = document.querySelector('#create-modal .btn-primary');
  const origHtml = btn.innerHTML;
  btn.disabled = true;
  btn.innerHTML = `<svg style="animation: spin 1s linear infinite; width:16px; height:16px; stroke: currentColor;" fill="none" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4z"/></svg> 建立中...`;
  
  try {
    const response = await fetch('/api/projects/create', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ name, format })
    });
    
    const result = await response.json();
    
    if (result.success) {
      closeCreateModal();
      // Redirect to the newly created project workspace
      window.location.href = `/project/${result.dir_name}`;
    } else {
      alert('建立專案失敗：' + (result.error || '未知錯誤'));
      btn.disabled = false;
      btn.innerHTML = origHtml;
    }
  } catch (error) {
    alert('網路連線或伺服器發生異常');
    btn.disabled = false;
    btn.innerHTML = origHtml;
  }
}

// Delete an existing project with safety double check
async function deleteProject(dirName, projectName) {
  if (!confirm(`⚠️ 您確定要刪除簡報專案「${projectName}」嗎？\n\n此操作會將該專案的所有素材、大綱草稿、向量 SVG 資產以及編譯完成的 PPTX 投影片全部永久刪除，且無法還原！`)) {
    return;
  }
  
  try {
    const response = await fetch(`/api/projects/${dirName}`, {
      method: 'DELETE'
    });
    const result = await response.json();
    
    if (result.success) {
      // Reload projects list to reflect deletion
      loadProjects();
    } else {
      alert('刪除專案失敗：' + (result.error || '未知錯誤'));
    }
  } catch (error) {
    alert('與伺服器連線中斷或發生異常，無法刪除專案');
  }
}
