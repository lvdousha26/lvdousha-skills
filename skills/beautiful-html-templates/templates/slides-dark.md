# Slides Dark Template

深色科技风幻灯片模板 — 适合技术演讲、投资人 Deck、产品发布。

## 主题变量

```css
:root {
  /* 品牌色 */
  --color-primary: #6C5CE7;
  --color-secondary: #00CEC9;
  --color-accent: #FD79A8;

  /* 背景 */
  --color-bg-primary: #0A0A0F;
  --color-bg-secondary: #13131A;
  --color-bg-card: rgba(255,255,255,0.04);

  /* 文字 */
  --color-text-primary: #FFFFFF;
  --color-text-secondary: #8888AA;
  --color-text-muted: #555577;

  /* 渐变 */
  --gradient-primary: linear-gradient(135deg, #6C5CE7, #00CEC9);
  --gradient-accent: linear-gradient(135deg, #FD79A8, #6C5CE7);

  /* 排版 */
  --font-heading: 'Space Grotesk', 'Inter', sans-serif;
  --font-body: 'Inter', -apple-system, sans-serif;

  /* 间距 */
  --slide-padding: 64px;
  --content-gap: 20px;

  /* 边框 */
  --border-radius: 12px;
  --border-subtle: 1px solid rgba(255,255,255,0.06);

  /* 阴影 */
  --shadow-glow: 0 0 40px rgba(108, 92, 231, 0.15);
  --shadow-card: 0 8px 32px rgba(0,0,0,0.4);
}
```

## 完整 HTML

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Dark Theme Presentation</title>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Space+Grotesk:wght@400;500;600;700&display=swap" rel="stylesheet">
  <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.1/dist/chart.umd.min.js"></script>
  <style>
    /* === 主题变量 === */
    :root {
      --color-primary: #6C5CE7;
      --color-secondary: #00CEC9;
      --color-accent: #FD79A8;
      --color-bg-primary: #0A0A0F;
      --color-bg-secondary: #13131A;
      --color-bg-card: rgba(255,255,255,0.04);
      --color-text-primary: #FFFFFF;
      --color-text-secondary: #8888AA;
      --color-text-muted: #555577;
      --gradient-primary: linear-gradient(135deg, #6C5CE7, #00CEC9);
      --gradient-accent: linear-gradient(135deg, #FD79A8, #6C5CE7);
      --font-heading: 'Space Grotesk', 'Inter', sans-serif;
      --font-body: 'Inter', -apple-system, sans-serif;
      --slide-padding: 64px;
      --content-gap: 20px;
      --border-radius: 12px;
      --border-subtle: 1px solid rgba(255,255,255,0.06);
      --shadow-glow: 0 0 40px rgba(108, 92, 231, 0.15);
      --shadow-card: 0 8px 32px rgba(0,0,0,0.4);
    }

    * { margin: 0; padding: 0; box-sizing: border-box; }

    body {
      background: var(--color-bg-primary);
      color: var(--color-text-primary);
      font-family: var(--font-body);
      overflow: hidden;
      -webkit-font-smoothing: antialiased;
    }

    /* 背景粒子网格 */
    body::before {
      content: '';
      position: fixed;
      inset: 0;
      background-image:
        radial-gradient(circle at 20% 50%, rgba(108,92,231,0.08) 0%, transparent 50%),
        radial-gradient(circle at 80% 20%, rgba(0,206,201,0.06) 0%, transparent 50%),
        radial-gradient(circle at 50% 80%, rgba(253,121,168,0.05) 0%, transparent 50%);
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
      transition: opacity 0.5s ease, transform 0.5s ease;
      transform: scale(0.97);
      background: var(--color-bg-primary);
      overflow: hidden;
    }

    .slide.active {
      opacity: 1;
      visibility: visible;
      transform: scale(1);
    }

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
      position: relative;
      z-index: 1;
    }

    h1, h2, h3 { font-family: var(--font-heading); font-weight: 600; }

    .slide-title {
      font-size: clamp(36px, 6vw, 80px);
      font-weight: 700;
      line-height: 1.1;
      background: var(--gradient-primary);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      background-clip: text;
    }

    .slide-subtitle {
      font-size: clamp(16px, 2vw, 24px);
      color: var(--color-text-secondary);
      font-weight: 400;
    }

    h2 {
      font-size: clamp(28px, 4vw, 52px);
      color: var(--color-text-primary);
      margin-bottom: 8px;
    }

    p, li {
      font-size: clamp(14px, 1.8vw, 22px);
      color: var(--color-text-secondary);
      line-height: 1.6;
    }

    /* 卡片样式 */
    .card-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
      gap: 16px;
      width: 100%;
      max-width: 900px;
    }

    .card {
      background: var(--color-bg-card);
      border: var(--border-subtle);
      border-radius: var(--border-radius);
      padding: 24px 20px;
      transition: transform 0.3s, box-shadow 0.3s;
      backdrop-filter: blur(10px);
    }

    .card:hover {
      transform: translateY(-4px);
      box-shadow: var(--shadow-glow);
    }

    .card h3 {
      font-size: clamp(14px, 1.4vw, 18px);
      color: var(--color-primary);
      margin-bottom: 8px;
    }

    .card p { font-size: clamp(12px, 1.2vw, 15px); }

    /* 标签 */
    .tag {
      display: inline-block;
      padding: 4px 14px;
      border-radius: 20px;
      font-size: 12px;
      font-weight: 500;
      background: rgba(108,92,231,0.15);
      color: var(--color-primary);
      border: 1px solid rgba(108,92,231,0.25);
    }

    /* 大数字 */
    .stat-number {
      font-size: clamp(40px, 6vw, 72px);
      font-weight: 700;
      font-family: var(--font-heading);
      background: var(--gradient-primary);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      background-clip: text;
    }

    .stat-label {
      font-size: clamp(12px, 1.2vw, 16px);
      color: var(--color-text-muted);
      text-transform: uppercase;
      letter-spacing: 2px;
    }

    /* 图表容器 */
    .chart-container {
      width: min(85%, 700px);
      height: clamp(200px, 45vh, 400px);
      margin: 8px 0;
    }

    /* 进度条 */
    .progress-bar {
      position: fixed;
      top: 0; left: 0;
      height: 3px;
      background: var(--gradient-primary);
      transition: width 0.4s ease;
      z-index: 1000;
    }

    /* 导航 */
    .nav-controls {
      position: fixed;
      bottom: 32px;
      left: 50%;
      transform: translateX(-50%);
      display: flex;
      align-items: center;
      gap: 16px;
      z-index: 1000;
      background: rgba(255,255,255,0.04);
      backdrop-filter: blur(20px);
      border: var(--border-subtle);
      border-radius: 50px;
      padding: 8px 20px;
    }

    .nav-btn {
      background: rgba(255,255,255,0.08);
      border: none;
      color: #fff;
      width: 36px; height: 36px;
      border-radius: 50%;
      cursor: pointer;
      font-size: 16px;
      transition: background 0.2s, transform 0.2s;
      display: flex;
      align-items: center;
      justify-content: center;
    }

    .nav-btn:hover {
      background: var(--color-primary);
      transform: scale(1.1);
    }

    .slide-counter {
      color: var(--color-text-muted);
      font-size: 13px;
      font-variant-numeric: tabular-nums;
      min-width: 50px;
      text-align: center;
    }

    /* 动画 */
    .animate-fade-up {
      animation: fadeUp 0.6s ease-out forwards;
      opacity: 0;
    }
    @keyframes fadeUp {
      from { opacity: 0; transform: translateY(30px); }
      to { opacity: 1; transform: translateY(0); }
    }

    .animate-scale {
      animation: scaleIn 0.5s ease-out forwards;
    }
    @keyframes scaleIn {
      from { opacity: 0; transform: scale(0.9); }
      to { opacity: 1; transform: scale(1); }
    }

    .animate-stagger > * {
      opacity: 0;
      animation: fadeUp 0.5s ease-out forwards;
    }
    .animate-stagger > *:nth-child(1) { animation-delay: 0.1s; }
    .animate-stagger > *:nth-child(2) { animation-delay: 0.2s; }
    .animate-stagger > *:nth-child(3) { animation-delay: 0.3s; }
    .animate-stagger > *:nth-child(4) { animation-delay: 0.4s; }
    .animate-stagger > *:nth-child(5) { animation-delay: 0.5s; }

    /* 响应式 */
    @media (max-width: 768px) {
      :root { --slide-padding: 32px; }
      .card-grid { grid-template-columns: 1fr 1fr; }
    }
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

    <!-- 标题页 -->
    <div class="slide active">
      <div class="slide-content animate-stagger">
        <div class="tag">PRESENTATION</div>
        <h1 class="slide-title">Your Title Here</h1>
        <p class="slide-subtitle">Subtitle or tagline</p>
      </div>
    </div>

    <!-- 更多幻灯片...（在 .slide-content 内放置内容） -->

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

- **径向渐变背景光晕** — 3 个不同颜色的光晕点
- **毛玻璃卡片** — backdrop-filter blur + 半透明背景
- **渐变文字标题** — primary → secondary 渐变
- **胶囊标签** — tag 组件
- **卡片悬停动效** — 上浮 + 发光阴影
- **进度条渐变** — 跟随品牌色
- **毛玻璃导航栏** — 半透明悬浮导航
