# Slides Glassmorphism Template

玻璃拟态风幻灯片模板 — 适合产品发布会、品牌展示、创意提案。

## 主题变量

```css
:root {
  --color-primary: #E879F9;
  --color-secondary: #60A5FA;
  --color-accent: #34D399;
  --color-bg-primary: #0F0A1A;
  --color-bg-card: rgba(255,255,255,0.06);
  --color-text-primary: #FFFFFF;
  --color-text-secondary: #C4B5D4;
  --color-text-muted: #7C6A8A;
  --gradient-primary: linear-gradient(135deg, #E879F9, #60A5FA);
  --gradient-accent: linear-gradient(135deg, #34D399, #E879F9);
  --font-heading: 'Space Grotesk', 'Inter', sans-serif;
  --font-body: 'Inter', -apple-system, sans-serif;
  --slide-padding: 64px;
  --content-gap: 20px;
  --border-radius: 16px;
  --border-glass: 1px solid rgba(255,255,255,0.12);
  --shadow-glass: 0 8px 32px rgba(0,0,0,0.3);
  --blur-glass: blur(16px);
}
```

## 完整 HTML

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Glassmorphism Presentation</title>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Space+Grotesk:wght@400;500;600;700&display=swap" rel="stylesheet">
  <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.1/dist/chart.umd.min.js"></script>
  <style>
    :root {
      --color-primary: #E879F9;
      --color-secondary: #60A5FA;
      --color-accent: #34D399;
      --color-bg-primary: #0F0A1A;
      --color-bg-card: rgba(255,255,255,0.06);
      --color-text-primary: #FFFFFF;
      --color-text-secondary: #C4B5D4;
      --color-text-muted: #7C6A8A;
      --gradient-primary: linear-gradient(135deg, #E879F9, #60A5FA);
      --gradient-accent: linear-gradient(135deg, #34D399, #E879F9);
      --font-heading: 'Space Grotesk', 'Inter', sans-serif;
      --font-body: 'Inter', -apple-system, sans-serif;
      --slide-padding: 64px;
      --content-gap: 20px;
      --border-radius: 16px;
      --border-glass: 1px solid rgba(255,255,255,0.12);
      --shadow-glass: 0 8px 32px rgba(0,0,0,0.3);
      --blur-glass: blur(16px);
    }

    * { margin: 0; padding: 0; box-sizing: border-box; }

    body {
      background: var(--color-bg-primary);
      color: var(--color-text-primary);
      font-family: var(--font-body);
      overflow: hidden;
      -webkit-font-smoothing: antialiased;
    }

    /* 动态渐变背景 */
    body::before {
      content: '';
      position: fixed;
      width: 600px; height: 600px;
      top: -200px; right: -100px;
      background: radial-gradient(circle, rgba(232,121,249,0.2) 0%, transparent 70%);
      border-radius: 50%;
      pointer-events: none;
      z-index: 0;
      animation: floatA 8s ease-in-out infinite alternate;
    }

    body::after {
      content: '';
      position: fixed;
      width: 500px; height: 500px;
      bottom: -150px; left: -100px;
      background: radial-gradient(circle, rgba(96,165,250,0.15) 0%, transparent 70%);
      border-radius: 50%;
      pointer-events: none;
      z-index: 0;
      animation: floatB 10s ease-in-out infinite alternate;
    }

    @keyframes floatA {
      from { transform: translate(0, 0); }
      to { transform: translate(-60px, 40px); }
    }

    @keyframes floatB {
      from { transform: translate(0, 0); }
      to { transform: translate(60px, -40px); }
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
      transition: opacity 0.5s ease;
      overflow: hidden;
    }

    .slide.active { opacity: 1; visibility: visible; }

    .slide-content {
      width: 100%;
      max-width: 90%;
      max-height: 100%;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      gap: var(--content-gap);
      background: var(--color-bg-card);
      backdrop-filter: var(--blur-glass);
      -webkit-backdrop-filter: var(--blur-glass);
      border: var(--border-glass);
      border-radius: var(--border-radius);
      padding: 48px 40px;
      box-shadow: var(--shadow-glass);
    }

    h1, h2, h3 { font-family: var(--font-heading); font-weight: 600; }

    .slide-title {
      font-size: clamp(32px, 5vw, 72px);
      font-weight: 700;
      line-height: 1.1;
      background: var(--gradient-primary);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      background-clip: text;
    }

    .slide-subtitle {
      font-size: clamp(15px, 1.8vw, 22px);
      color: var(--color-text-secondary);
      font-weight: 400;
    }

    h2 { font-size: clamp(26px, 3.5vw, 48px); }

    p, li {
      font-size: clamp(13px, 1.5vw, 18px);
      color: var(--color-text-secondary);
      line-height: 1.6;
    }

    .card-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
      gap: 14px;
      width: 100%;
    }

    .card {
      background: rgba(255,255,255,0.04);
      backdrop-filter: blur(12px);
      -webkit-backdrop-filter: blur(12px);
      border: 1px solid rgba(255,255,255,0.08);
      border-radius: 12px;
      padding: 20px 16px;
      transition: transform 0.3s, border-color 0.3s;
    }

    .card:hover {
      transform: translateY(-4px);
      border-color: rgba(232,121,249,0.3);
    }

    .card h3 {
      font-size: clamp(13px, 1.3vw, 16px);
      color: var(--color-primary);
      margin-bottom: 6px;
    }

    .stat-number {
      font-size: clamp(36px, 5vw, 60px);
      font-weight: 700;
      font-family: var(--font-heading);
      background: var(--gradient-primary);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      background-clip: text;
    }

    .tag {
      display: inline-block;
      padding: 4px 14px;
      border-radius: 20px;
      font-size: 11px;
      font-weight: 500;
      background: rgba(232,121,249,0.12);
      border: 1px solid rgba(232,121,249,0.2);
      color: var(--color-primary);
      text-transform: uppercase;
      letter-spacing: 1px;
    }

    .chart-container {
      width: min(80%, 600px);
      height: clamp(180px, 40vh, 350px);
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
      background: rgba(255,255,255,0.05);
      backdrop-filter: blur(20px);
      -webkit-backdrop-filter: blur(20px);
      border: var(--border-glass);
      border-radius: 50px;
      padding: 8px 20px;
    }

    .nav-btn {
      background: rgba(255,255,255,0.06);
      border: 1px solid rgba(255,255,255,0.08);
      color: #fff;
      width: 36px; height: 36px;
      border-radius: 50%;
      cursor: pointer;
      font-size: 16px;
      transition: background 0.2s, transform 0.2s;
    }

    .nav-btn:hover {
      background: rgba(232,121,249,0.3);
      transform: scale(1.15);
    }

    .slide-counter {
      color: var(--color-text-muted);
      font-size: 12px;
      font-variant-numeric: tabular-nums;
      min-width: 48px;
      text-align: center;
    }

    .animate-fade-up {
      animation: fadeUp 0.6s ease-out forwards;
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
    .animate-stagger > *:nth-child(1) { animation-delay: 0.1s; }
    .animate-stagger > *:nth-child(2) { animation-delay: 0.2s; }
    .animate-stagger > *:nth-child(3) { animation-delay: 0.3s; }
    .animate-stagger > *:nth-child(4) { animation-delay: 0.4s; }

    @media (max-width: 768px) {
      :root { --slide-padding: 32px; }
      .slide-content { padding: 32px 20px; max-width: 95%; }
    }
    @media (max-width: 480px) {
      :root { --slide-padding: 16px; }
      .slide-content { padding: 24px 16px; max-width: 98%; }
      .card-grid { grid-template-columns: 1fr; }
      .nav-controls { bottom: 16px; padding: 6px 14px; }
    }
  </style>
</head>
<body>
  <div class="progress-bar" id="progressBar"></div>
  <div class="slide-deck">

    <div class="slide active">
      <div class="slide-content animate-stagger">
        <div class="tag">LAUNCH</div>
        <h1 class="slide-title">Your Title Here</h1>
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

- 浮动动态光晕动画（两个渐变光晕球左右浮动）
- 毛玻璃内容卡片（backdrop-filter: blur + 半透明背景）
- 毛玻璃导航同款风格
- 紫→蓝渐变品牌色
- 所有卡片 hover 时边框变色
- 大圆角（16px）营造柔和感
