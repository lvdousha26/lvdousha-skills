# Slides Light Template

简约明亮风幻灯片模板 — 适合商业演示、团队分享、销售 Pitch。

## 主题变量

```css
:root {
  --color-primary: #2563EB;
  --color-secondary: #7C3AED;
  --color-accent: #F59E0B;
  --color-bg-primary: #FFFFFF;
  --color-bg-secondary: #F8FAFC;
  --color-bg-card: #F1F5F9;
  --color-text-primary: #0F172A;
  --color-text-secondary: #475569;
  --color-text-muted: #94A3B8;
  --gradient-primary: linear-gradient(135deg, #2563EB, #7C3AED);
  --gradient-accent: linear-gradient(135deg, #F59E0B, #EF4444);
  --font-heading: 'Inter', 'SF Pro Display', sans-serif;
  --font-body: 'Inter', -apple-system, sans-serif;
  --slide-padding: 64px;
  --border-radius: 12px;
  --border-subtle: 1px solid #E2E8F0;
  --shadow-card: 0 4px 24px rgba(0,0,0,0.06);
  --shadow-glow: 0 4px 32px rgba(37,99,235,0.12);
}
```

## 完整 HTML

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Light Theme Presentation</title>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
  <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.1/dist/chart.umd.min.js"></script>
  <style>
    :root {
      --color-primary: #2563EB;
      --color-secondary: #7C3AED;
      --color-accent: #F59E0B;
      --color-bg-primary: #FFFFFF;
      --color-bg-secondary: #F8FAFC;
      --color-bg-card: #F1F5F9;
      --color-text-primary: #0F172A;
      --color-text-secondary: #475569;
      --color-text-muted: #94A3B8;
      --gradient-primary: linear-gradient(135deg, #2563EB, #7C3AED);
      --gradient-accent: linear-gradient(135deg, #F59E0B, #EF4444);
      --font-heading: 'Inter', 'SF Pro Display', sans-serif;
      --font-body: 'Inter', -apple-system, sans-serif;
      --slide-padding: 64px;
      --border-radius: 12px;
      --border-subtle: 1px solid #E2E8F0;
      --shadow-card: 0 4px 24px rgba(0,0,0,0.06);
      --shadow-glow: 0 4px 32px rgba(37,99,235,0.12);
      --content-gap: 20px;
    }

    * { margin: 0; padding: 0; box-sizing: border-box; }

    body {
      background: var(--color-bg-primary);
      color: var(--color-text-primary);
      font-family: var(--font-body);
      overflow: hidden;
      -webkit-font-smoothing: antialiased;
    }

    body::before {
      content: '';
      position: fixed;
      inset: 0;
      background: radial-gradient(ellipse at 80% 20%, rgba(37,99,235,0.04) 0%, transparent 60%),
                  radial-gradient(ellipse at 20% 80%, rgba(124,58,237,0.03) 0%, transparent 60%);
      pointer-events: none;
      z-index: 0;
    }

    .slide-deck {
      position: relative;
      width: 100vw;
      height: 100vh;
      overflow: hidden;
      z-index: 1;
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
      align-items: center;
      text-align: center;
      padding: var(--slide-padding);
      opacity: 0;
      visibility: hidden;
      transition: opacity 0.45s ease;
      background: var(--color-bg-primary);
      overflow: hidden;
    }

    .slide.active { opacity: 1; visibility: visible; }

    .slide-content {
      width: 100%;
      max-width: 100%;
      max-height: 100%;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      gap: var(--content-gap);
    }

    h1, h2, h3 { font-family: var(--font-heading); font-weight: 600; }

    .slide-title {
      font-size: clamp(32px, 5vw, 72px);
      font-weight: 700;
      line-height: 1.1;
      color: var(--color-text-primary);
      letter-spacing: -0.02em;
    }

    .slide-title .highlight {
      background: var(--gradient-primary);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      background-clip: text;
    }

    .slide-subtitle {
      font-size: clamp(16px, 2vw, 24px);
      color: var(--color-text-secondary);
      font-weight: 400;
      line-height: 1.5;
    }

    h2 {
      font-size: clamp(28px, 3.5vw, 48px);
      color: var(--color-text-primary);
      letter-spacing: -0.01em;
    }

    p, li {
      font-size: clamp(14px, 1.6vw, 20px);
      color: var(--color-text-secondary);
      line-height: 1.7;
    }

    .card-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
      gap: 16px;
      width: 100%;
      max-width: 900px;
    }

    .card {
      background: var(--color-bg-card);
      border-radius: var(--border-radius);
      padding: 24px 20px;
      text-align: left;
      transition: transform 0.25s, box-shadow 0.25s;
    }

    .card:hover {
      transform: translateY(-3px);
      box-shadow: var(--shadow-card);
    }

    .card h3 {
      font-size: clamp(14px, 1.3vw, 17px);
      color: var(--color-primary);
      margin-bottom: 6px;
    }

    .card p { font-size: clamp(12px, 1.1vw, 14px); }

    .stat-number {
      font-size: clamp(40px, 5vw, 64px);
      font-weight: 700;
      font-family: var(--font-heading);
      color: var(--color-primary);
    }

    .stat-label {
      font-size: clamp(12px, 1.2vw, 15px);
      color: var(--color-text-muted);
      text-transform: uppercase;
      letter-spacing: 2px;
      margin-top: 4px;
    }

    .tag {
      display: inline-block;
      padding: 4px 16px;
      border-radius: 20px;
      font-size: 12px;
      font-weight: 500;
      background: rgba(37,99,235,0.08);
      color: var(--color-primary);
    }

    .divider {
      width: 60px;
      height: 3px;
      background: var(--gradient-primary);
      border-radius: 2px;
    }

    .chart-container {
      width: min(85%, 700px);
      height: clamp(200px, 45vh, 400px);
      margin: 8px 0;
    }

    .progress-bar {
      position: fixed;
      top: 0; left: 0;
      height: 3px;
      background: var(--gradient-primary);
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
      background: var(--color-bg-primary);
      border: var(--border-subtle);
      border-radius: 50px;
      padding: 8px 20px;
      box-shadow: 0 4px 20px rgba(0,0,0,0.08);
    }

    .nav-btn {
      background: var(--color-bg-card);
      border: none;
      color: var(--color-text-secondary);
      width: 36px; height: 36px;
      border-radius: 50%;
      cursor: pointer;
      font-size: 16px;
      transition: background 0.2s, color 0.2s, transform 0.2s;
      display: flex;
      align-items: center;
      justify-content: center;
    }

    .nav-btn:hover {
      background: var(--color-primary);
      color: white;
      transform: scale(1.1);
    }

    .slide-counter {
      color: var(--color-text-muted);
      font-size: 13px;
      font-variant-numeric: tabular-nums;
      min-width: 50px;
      text-align: center;
    }

    .animate-fade-up {
      animation: fadeUp 0.5s ease-out forwards;
      opacity: 0;
    }
    @keyframes fadeUp {
      from { opacity: 0; transform: translateY(24px); }
      to { opacity: 1; transform: translateY(0); }
    }

    .animate-stagger > * {
      opacity: 0;
      animation: fadeUp 0.5s ease-out forwards;
    }
    .animate-stagger > *:nth-child(1) { animation-delay: 0.05s; }
    .animate-stagger > *:nth-child(2) { animation-delay: 0.1s; }
    .animate-stagger > *:nth-child(3) { animation-delay: 0.15s; }
    .animate-stagger > *:nth-child(4) { animation-delay: 0.2s; }
    .animate-stagger > *:nth-child(5) { animation-delay: 0.25s; }

    @media (max-width: 768px) { :root { --slide-padding: 32px; } }
    @media (max-width: 480px) {
      :root { --slide-padding: 20px; }
      .card-grid { grid-template-columns: 1fr; }
      .nav-controls { bottom: 16px; padding: 6px 14px; gap: 10px; }
    }
  </style>
</head>
<body>
  <div class="progress-bar" id="progressBar"></div>
  <div class="slide-deck">

    <div class="slide active">
      <div class="slide-content animate-stagger">
        <div class="tag">PRESENTATION</div>
        <h1 class="slide-title">Your <span class="highlight">Title</span> Here</h1>
        <p class="slide-subtitle">Subtitle or tagline</p>
        <div class="divider"></div>
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

- 纯白背景 + 极浅蓝色光晕
- 渐变强调色文字（.highlight）
- 蓝色分割线分隔内容
- 卡片 hover 投射阴影
- 白色导航栏 + 浅色边框阴影
