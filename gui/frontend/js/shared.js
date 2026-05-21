/*
  PPT Master GUI - Shared Utilities & Theme Control (shared.js)
*/

document.addEventListener('DOMContentLoaded', () => {
  initTheme();
  injectNavBar();
});

// Theme Management
function initTheme() {
  const savedTheme = localStorage.getItem('ppt-theme') || localStorage.getItem('theme') || 'dark';
  if (savedTheme === 'light') {
    document.body.classList.add('light-theme');
    document.documentElement.setAttribute('data-theme', 'light');
  } else {
    document.body.classList.remove('light-theme');
    document.documentElement.setAttribute('data-theme', 'dark');
  }
}

function toggleTheme() {
  const isLight = document.body.classList.toggle('light-theme');
  const newTheme = isLight ? 'light' : 'dark';
  document.documentElement.setAttribute('data-theme', newTheme);
  
  localStorage.setItem('ppt-theme', newTheme);
  localStorage.setItem('theme', newTheme); // Keep both in sync
  
  // Toggle the icon
  const themeIcon = document.getElementById('theme-icon');
  if (themeIcon) {
    themeIcon.innerHTML = isLight 
      ? '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z" />' // Moon
      : '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364-6.364l-.707.707M6.343 17.657l-.707.707m0-12.728l.707.707m12.728 12.728l.707-.707M12 8a4 4 0 100 8 4 4 0 000-8z" />'; // Sun
  }
}

// Global NavBar Injection for MECE cleanliness
function injectNavBar() {
  const headerContainer = document.getElementById('navbar-container');
  if (!headerContainer) return;
  
  const currentPath = window.location.pathname;
  const isIndex = currentPath === '/' || currentPath.endsWith('index.html');
  const isSettings = currentPath.includes('/settings');
  const isProject = currentPath.includes('/project/');
  const isGuide = currentPath.includes('/guide');
  
  const isLight = document.body.classList.contains('light-theme');
  const themeIconSVG = isLight
    ? '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z" />'
    : '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364-6.364l-.707.707M6.343 17.657l-.707.707m0-12.728l.707.707m12.728 12.728l.707-.707M12 8a4 4 0 100 8 4 4 0 000-8z" />';

  const html = `
    <nav class="navbar">
      <div class="nav-brand">
        <a href="/" style="display: flex; align-items: center; gap: 12px;">
          <svg class="nav-logo" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2" fill="none">
            <path stroke-linecap="round" stroke-linejoin="round" d="M7 12l3-3 3 3 4-4M8 21h8a2 2 0 002-2V5a2 2 0 00-2-2H8a2 2 0 00-2 2v14a2 2 0 002 2z" />
          </svg>
          <span class="nav-title">NBLM PPT Pipeline</span>
        </a>
      </div>
      <div class="nav-links">
        <a href="/" class="nav-link ${isIndex ? 'active' : ''}">
          <svg width="18" height="18" fill="none" stroke="currentColor" viewBox="0 0 24 24" stroke-width="2">
            <path stroke-linecap="round" stroke-linejoin="round" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6" />
          </svg>
          儀表板
        </a>
        <a href="/settings" class="nav-link ${isSettings ? 'active' : ''}">
          <svg width="18" height="18" fill="none" stroke="currentColor" viewBox="0 0 24 24" stroke-width="2">
            <path stroke-linecap="round" stroke-linejoin="round" d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z" />
            <path stroke-linecap="round" stroke-linejoin="round" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
          </svg>
          全域設定
        </a>
        <a href="/guide" class="nav-link ${isGuide ? 'active' : ''}">
          <svg width="18" height="18" fill="none" stroke="currentColor" viewBox="0 0 24 24" stroke-width="2">
            <path stroke-linecap="round" stroke-linejoin="round" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253" />
          </svg>
          使用說明
        </a>
        <button id="theme-toggler" class="theme-toggle" onclick="toggleTheme()" aria-label="Toggle Theme">
          <svg id="theme-icon" width="20" height="20" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            ${themeIconSVG}
          </svg>
        </button>
      </div>
    </nav>
  `;
  
  headerContainer.innerHTML = html;
}

// Clean ANSI styling into styled HTML spans
function parseAnsiColor(text) {
  if (!text) return "";
  
  // Basic ANSI escape code mappings
  const ansiMap = {
    '\\033[31m': 'color: var(--warning); font-weight: 600;', // Red
    '\\033[32m': 'color: var(--success); font-weight: 600;', // Green
    '\\033[33m': 'color: #FBBF24; font-weight: 600;',         // Yellow
    '\\033[34m': 'color: var(--accent); font-weight: 600;',   // Blue
    '\\033[35m': 'color: #D946EF;',                           // Magenta
    '\\033[36m': 'color: #22D3EE;',                           // Cyan
    '\\033[0m': '',                                           // Reset
    '\x1b[31m': 'color: var(--warning); font-weight: 600;',
    '\x1b[32m': 'color: var(--success); font-weight: 600;',
    '\x1b[33m': 'color: #FBBF24; font-weight: 600;',
    '\x1b[34m': 'color: var(--accent); font-weight: 600;',
    '\x1b[35m': 'color: #D946EF;',
    '\x1b[36m': 'color: #22D3EE;',
    '\x1b[0m': '',
  };
  
  let html = escapeHtml(text);
  
  // Replace markers
  Object.keys(ansiMap).forEach(code => {
    // Regex escape
    const escaped = code.replace(/[-\/\\^$*+?.()|[\]{}]/g, '\\$&');
    const regex = new RegExp(escaped, 'g');
    const style = ansiMap[code];
    
    if (style) {
      html = html.replace(regex, `<span style="${style}">`);
    } else {
      // Reset is a closing span
      html = html.replace(regex, '</span>');
    }
  });
  
  // Close any unclosed tags
  const openCount = (html.match(/<span/g) || []).length;
  const closeCount = (html.match(/<\/span/g) || []).length;
  if (openCount > closeCount) {
    html += '</span>'.repeat(openCount - closeCount);
  }
  
  return html;
}

function escapeHtml(text) {
  const map = {
    '&': '&amp;',
    '<': '&lt;',
    '>': '&gt;',
    '"': '&quot;',
    "'": '&#039;'
  };
  return text.replace(/[&<>"']/g, function(m) { return map[m]; });
}
