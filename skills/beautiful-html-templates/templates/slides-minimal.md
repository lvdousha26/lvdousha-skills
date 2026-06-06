# Slides Minimal Template

极简留白风幻灯片模板 — 适合学术报告、设计评审、产品文档。

## 主题变量

```css
:root {
  --color-primary: #1A1A2E;
  --color-secondary: #16213E;
  --color-accent: #E94560;
  --color-bg-primary: #F5F5F0;
  --color-bg-secondary: #EEEDE8;
  --color-text-primary: #1A1A2E;
  --color-text-secondary: #555566;
  --color-text-muted: #9999AA;
  --font-heading: 'EB Garamond', 'Georgia', serif;
  --font-body: 'Inter', -apple-system, sans-serif;
  --slide-padding: 80px;
  --content-gap: 24px;
  --border-radius: 4px;
}
```

## 完整 HTML

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Minimal Presentation</title>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&family=EB+Garamond:ital,wght@0,400;0,600;0,700;1,400&display=swap" rel="stylesheet">
  <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.1/dist/chart.umd.min.js"></script>
  <style>
    :root {
      --color-primary: #1A1A2E;
      --color-secondary: #16213E;
      --color-accent: #E94560;
      --color-bg-primary: #F5F5F0;
      --color-bg-secondary: #EEEDE8;
      --color-text-primary: #1A1A2E;
      --color-text-secondary: #555566;
      --color-text-muted: #9999AA;
      --font-heading: 'EB Garamond', 'Georgia', serif;
      --font-body: 'Inter', -apple-system, sans-serif;
      --slide-padding: 80px;
      --content-gap: 24px;
      --border-radius: 4px;
    }

    * { margin: 0; padding: 0; box-sizing: border-box; }

    body {
      background: var(--color-bg-primary);
      color: var(--color-text-primary);
      font-family: var(--font-body);
      overflow: hidden;
      -webkit-font-smoothing: antialiased;
    }

    .slide-deck {
      position: relative;
      width: 100vw;
      height: 100vh;
      overflow: hidden;
    }

    @media (min-width: 769px) {
      .slide-deck {
        max-width: calc(100vh * 16 / 9);
        max-height: calc(100vw * 9 / 16);
        margin: auto;
        position: absolute;
        inset: 0;
      }
    }

    .slide {
      position: absolute;
      width: 100%; height: 100%;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: flex-start;
      text-align: left;
      padding: var(--slide-padding);
      opacity: 0;
      visibility: hidden;
      transition: opacity 0.5s ease;
      background: var(--color-bg-primary);
      overflow: hidden;
    }

    .slide.active { opacity: 1; visibility: visible; }

    .slide-content {
      width: 100%;
      max-width: 800px;
      max-height: 100%;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      gap: var(--content-gap);
    }

    h1, h2, h3 { font-family: var(--font-heading); }

    .slide-title {
      font-size: clamp(40px, 5vw, 80px);
      font-weight: 700;
      line-height: 1.1;
      color: var(--color-text-primary);
      letter-spacing: -0.01em;
    }

    .slide-subtitle {
      font-size: clamp(16px, 2vw, 24px);
      color: var(--color-text-secondary);
      font-weight: 400;
      font-style: italic;
      font-family: var(--font-heading);
    }

    h2 {
      font-size: clamp(32px, 4vw, 56px);
      font-weight: 600;
      color: var(--color-text-primary);
    }

    p, li {
      font-size: clamp(15px, 1.6vw, 20px);
      color: var(--color-text-secondary);
      line-height: 1.7;
    }

    .card-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
      gap: 12px;
      width: 100%;
    }

    .card {
      border-left: 2px solid var(--color-accent);
      padding: 16px 20px;
      transition: background 0.2s;
    }

    .card:hover { background: var(--color-bg-secondary); }

    .card h3 {
      font-size: clamp(16px, 1.4vw, 20px);
      color: var(--color-text-primary);
      font-weight: 600;
      margin-bottom: 4px;
    }

    .card p { font-size: clamp(13px, 1.1vw, 15px); }

    .stat-number {
      font-size: clamp(44px, 5vw, 72px);
      font-weight: 700;
      font-family: var(--font-heading);
      color: var(--color-text-primary);
    }

    .stat-label {
      font-size: clamp(11px, 1vw, 13px);
      color: var(--color-text-muted);
      text-transform: uppercase;
      letter-spacing: 3px;
    }

    .tag {
      display: inline-block;
      font-size: 11px;
      font-weight: 500;
      color: var(--color-accent);
      text-transform: uppercase;
      letter-spacing: 3px;
    }

    hr {
      width: 60px;
      border: none;
      height: 2px;
      background: var(--color-accent);
      margin: 0;
    }

    .chart-container {
      width: min(85%, 650px);
      height: clamp(200px, 45vh, 400px);
    }

    .progress-bar {
      position: fixed;
      top: 0; left: 0;
      height: 2px;
      background: var(--color-accent);
      transition: width 0.4s ease;
      z-index: 1000;
    }

    .nav-controls {
      position: fixed;
      bottom: 32px;
      left: 50%;
      transform: translateX(-50%);
      display: flex;
      align-items: center;
      gap: 16px;
      z-index: 1000;
    }

    .nav-btn {
      background: none;
      border: 1px solid var(--color-text-muted);
      color: var(--color-text-secondary);
      width: 34px; height: 34px;
      border-radius: 0;
      cursor: pointer;
      font-size: 14px;
      transition: border-color 0.2s, color 0.2s;
    }

    .nav-btn:hover {
      border-color: var(--color-text-primary);
      color: var(--color-text-primary);
    }

    .slide-counter {
      color: var(--color-text-muted);
      font-size: 12px;
      font-variant-numeric: tabular-nums;
      min-width: 50px;
      text-align: center;
      letter-spacing: 1px;
    }

    .animate-fade-up {
      animation: fadeUp 0.6s ease-out forwards;
      opacity: 0;
    }
    @keyframes fadeUp {
      from { opacity: 0; transform: translateY(20px); }
      to { opacity: 1; transform: translateY(0); }
    }

    .animate-stagger > * {
      opacity: 0;
      animation: fadeUp 0.5s ease-out forwards;
    }
    .animate-stagger > *:nth-child(1) { animation-delay: 0.1s; }
    .animate-stagger > *:nth-child(2) { animation-delay: 0.2s; }
    .animate-stagger > *:nth-child(3) { animation-delay: 0.3s; }

    @media (max-width: 768px) { :root { --slide-padding: 40px; } }
    @media (max-width: 480px) {
      :root { --slide-padding: 24px; }
      .card-grid { grid-template-columns: 1fr; }
      .nav-controls { bottom: 16px; }
    }
  </style>
</head>
<body>
  <div class="progress-bar" id="progressBar"></div>
  <div class="slide-deck">

    <div class="slide active">
      <div class="slide-content">
        <div class="tag">Presentation</div>
        <h1 class="slide-title">Your Title Here</h1>
        <hr>
        <p class="slide-subtitle">Subtitle or tagline</p>
      </div>
    </div>

  </div>

  <div class="nav-controls">
    <button class="nav-btn" onclick="prevSlide()">←</button>
    <span class="slide-counter"><span id="current">1</span> / <span id="total">1</span></span>
    <button class="nav-btn" onclick="nextSlide()">→</button>
  </div>

  <script>
    let current = 1;
    const total = document.querySelectorAll('.slide').length;
    document.getElementById('total').textContent = total;

    function showSlide(n) {
      if (n < 1) n = 1;
      if (n > total) n = total;
      current = n;
      document.querySelectorAll('.slide').forEach((s, i) => {
        s.classList.toggle('active', i === n - 1);
      });
      document.getElementById('current').textContent = n;
      document.getElementById('progressBar').style.width = (n / total * 100) + '%';
    }

    function nextSlide() { showSlide(current + 1); }
    function prevSlide() { showSlide(current - 1); }

    document.addEventListener('keydown', (e) => {
      if (e.key === 'ArrowRight' || e.key === ' ') { e.preventDefault(); nextSlide(); }
      if (e.key === 'ArrowLeft') { e.preventDefault(); prevSlide(); }
    });

    document.addEventListener('click', (e) => {
      if (!e.target.closest('.nav-controls')) nextSlide();
    });

    showSlide(1);
  </script>
</body>
</html>
```

## 特色元素

- 米白/米灰柔和底色
- EB Garamond 衬线字体标题（学术感）
- 左对齐布局（非居中）
- 红色强调线（2px 竖线/横线）
- 极简导航无背景
- 大量留白
- 字母间距宽松
