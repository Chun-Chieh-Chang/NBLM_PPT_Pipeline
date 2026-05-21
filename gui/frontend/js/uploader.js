/*
  PPT Master GUI - File Uploader Logic (uploader.js)
*/

document.addEventListener('DOMContentLoaded', () => {
  initUploader();
});

function initUploader() {
  const dropzone = document.getElementById('upload-dropzone');
  const fileInput = document.getElementById('file-uploader');
  
  if (!dropzone || !fileInput) return;
  
  // Click dropzone to trigger input click
  dropzone.addEventListener('click', () => {
    fileInput.click();
  });
  
  // Input change handler
  fileInput.addEventListener('change', () => {
    if (fileInput.files.length > 0) {
      handleFilesUpload(fileInput.files);
    }
  });
  
  // Drag and drop event styling
  ['dragenter', 'dragover'].forEach(eventName => {
    dropzone.addEventListener(eventName, (e) => {
      e.preventDefault();
      e.stopPropagation();
      dropzone.classList.add('dragover');
    }, false);
  });
  
  ['dragleave', 'drop'].forEach(eventName => {
    dropzone.addEventListener(eventName, (e) => {
      e.preventDefault();
      e.stopPropagation();
      dropzone.classList.remove('dragover');
    }, false);
  });
  
  // Drop handler
  dropzone.addEventListener('drop', (e) => {
    const dt = e.dataTransfer;
    const files = dt.files;
    if (files.length > 0) {
      handleFilesUpload(files);
    }
  });
}

// Upload processing
async function handleFilesUpload(files) {
  const dropzoneText = document.querySelector('#upload-dropzone .dropzone-text');
  const dropzoneSub = document.querySelector('#upload-dropzone .dropzone-sub');
  
  if (!dropzoneText) return;
  
  const originalText = dropzoneText.innerText;
  const originalSub = dropzoneSub.innerText;
  
  const filesArray = Array.from(files);
  let uploadErrors = 0;
  
  // Upload sequentially
  for (let i = 0; i < filesArray.length; i++) {
    const file = filesArray[i];
    
    dropzoneText.innerText = `正在上傳 (${i + 1}/${filesArray.length}): ${file.name}...`;
    dropzoneSub.innerText = `請勿重新整理網頁...`;
    
    const formData = new FormData();
    formData.append('file', file);
    
    try {
      logToTerminal(`[SYSTEM] 正在上傳檔案: ${file.name} (${formatBytes(file.size)})...`, 'system');
      
      const response = await fetch(`/api/projects/${projectDirName}/upload`, {
        method: 'POST',
        body: formData
      });
      
      const result = await response.json();
      
      if (result.success) {
        logToTerminal(`[SUCCESS] 檔案 ${file.name} 上傳成功！`, 'success');
      } else {
        logToTerminal(`[ERROR] 檔案 ${file.name} 上傳失敗: ${result.error || '未知錯誤'}`, 'error');
        uploadErrors++;
      }
    } catch (err) {
      logToTerminal(`[ERROR] 檔案 ${file.name} 上傳異常: ${err.message}`, 'error');
      uploadErrors++;
    }
  }
  
  // Restore uploader layout
  dropzoneText.innerText = originalText;
  dropzoneSub.innerText = originalSub;
  
  if (uploadErrors === 0) {
    window.showSmartAlert('上傳成功', '所有簡報素材檔案皆已成功上傳！', '🎉');
  } else {
    window.showSmartAlert('上傳完成', `檔案上傳完成，其中有 ${uploadErrors} 個檔案失敗，請檢視終端機日誌。`, '⚠️');
  }
  
  // Reset input value to allow uploading same file again
  document.getElementById('file-uploader').value = '';
  
  // Refresh sources list in project details
  refreshProjectInfo();
}

// Format bytes to readable size
function formatBytes(bytes, decimals = 2) {
  if (bytes === 0) return '0 Bytes';
  const k = 1024;
  const dm = decimals < 0 ? 0 : decimals;
  const sizes = ['Bytes', 'KB', 'MB', 'GB', 'TB'];
  const i = Math.floor(Math.log(bytes) / Math.log(k));
  return parseFloat((bytes / Math.pow(k, i)).toFixed(dm)) + ' ' + sizes[i];
}
