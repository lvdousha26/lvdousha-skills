# Slides Gradient Template

渐变炫彩风幻灯片模板 — 适合营销演示、创意提案、品牌推广。

## 主题变量

```css
:root {
  --color-primary: #FF6B6B;
  --color-secondary: #FF8E53;
  --color-accent: #FFD93D;
  --color-bg-primary: #0A0A0A;
  --color-bg-card: rgba(255,255,255,0.03);
  --color-text-primary: #FFFFFF;
  --color-text-secondary: #B8B8D0;
  --color-text-muted: #6B6B80;
  --gradient-primary: linear-gradient(135deg, #FF6B6B, #FF8E53 50%, #FFD93D);
  --gradient-secondary: linear-gradient(135deg, #6C5CE7, #A29BFE);
  --gradient-hero: linear-gradient(135deg, #0A0A0A 0%, #1A0A2E 50%, #0A0A1A 100%);
  --font-heading: 'Space Grotesk', 'Inter', sans-serif;
  --font-body: 'Inter', -apple-system, sans-serif;
  --slide-padding: 64px;
  --content-gap: 20px;
  --border-radius: 12px;
  --border-subtle: 1px solid rgba(255,255,255,0.06);
  --shadow-glow: 0 0 60px rgba(255,107,107,0.15);
}
```

## 完整 HTML

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Gradient Presentation</title>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Space+Grotesk:wght@400;500;600;700&display=swap" rel="stylesheet">
  <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.1/dist/chart.umd.min.js"></script>
  <style>
    :root {
      --color-primary: #FF6B6B;
      --color-secondary: #FF8E53;
      --color-accent: #FFD93D;
      --color-bg-primary: #0A0A0A;
      --color-bg-card: rgba(255,255,255,0.03);
      --color-text-primary: #FFFFFF;
      --color-text-secondary: #B8B8D0;
      --color-text-muted: #6B6B80;
      --gradient-primary: linear-gradient(135deg, #FF6B6B, #FF8E53 50%, #FFD93D);
      --gradient-secondary: linear-gradient(135deg, #6C5CE7, #A29BFE);
      --gradient-hero: linear-gradient(135deg, #0A0A0A 0%, #1A0A2E 50%, #0A0A1A 100%);
      --font-heading: 'Space Grotesk', 'Inter', sans-serif;
      --font-body: 'Inter', -apple-system, sans-serif;
      --slide-padding: 64px;
      --content-gap: 20px;
      --border-radius: 12px;
      --border-subtle: 1px solid rgba(255,255,255,0.06);
      --shadow-glow: 0 0 60px rgba(255,107,107,0.15);
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
      background:
        radial-gradient(ellipse at 10% 30%, rgba(255,107,107,0.08) 0%, transparent 50%),
        radial-gradient(ellipse at 90% 20%, rgba(255,142,83,0.06) 0%, transparent 50%),
        radial-gradient(ellipse at 50% 80%, rgba(108,92,231,0.08) 0%, transparent 50%);
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
      transition: opacity 0.5s ease;
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

    h2 { font-size: clamp(28px, 4vw, 52px); }

    p, li {
      font-size: clamp(14px, 1.6vw, 20px);
      color: var(--color-text-secondary);
      line-height: 1.6;
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
      border: var(--border-subtle);
      border-radius: var(--border-radius);
      padding: 24px 20px;
      transition: transform 0.3s, border-color 0.3s;
      position: relative;
      overflow: hidden;
    }

    .card::before {
      content: '';
      position: absolute;
      top: 0; left: 0;
      width: 100%; height: 3px;
      background: var(--gradient-primary);
      opacity: 0;
      transition: opacity 0.3s;
    }

    .card:hover::before { opacity: 1; }
    .card:hover { transform: translateY(-4px); border-color: rgba(255,107,107,0.2); }

    .card h3 {
      font-size: clamp(14px, 1.3vw, 17px);
      color: var(--color-primary);
      margin-bottom: 6px;
    }

    .card p { font-size: clamp(12px, 1.1vw, 14px); }

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
      font-size: clamp(11px, 1.2vw, 14px);
      color: var(--color-text-muted);
      text-transform: uppercase;
      letter-spacing: 2px;
    }

    .tag {
      display: inline-block;
      padding: 4px 14px;
      border-radius: 20px;
      font-size: 11px;
      font-weight: 500;
      background: linear-gradient(135deg, rgba(255,107,107,0.15), rgba(255,142,83,0.15));
      border: 1px solid rgba(255,107,107,0.2);
      color: var(--color-primary);
      text-transform: uppercase;
      letter-spacing: 1px;
    }

    .chart-container {
      width: min(85%, 700px);
      height: clamp(200px, 45vh, 400px);
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
      background: rgba(255,255,255,0.04);
      backdrop-filter: blur(20px);
      border: var(--border-subtle);
      border-radius: 50px;
      padding: 8px 20px;
    }

    .nav-btn {
      background: rgba(255,255,255,0.06);
      border: none;
      color: #fff;
      width: 36px; height: 36px;
      border-radius: 50%;
      cursor: pointer;
      font-size: 16px;
      transition: background 0.2s, transform 0.2s;
    }

    .nav-btn:hover {
      background: var(--gradient-primary);
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
      animation: fadeUp 0.6s ease-out forwards;
      opacity: 0;
    }
    @keyframes fadeUp {
      from { opacity: 0; transform: translateY(30px); }
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

    @media (max-width: 768px) { :root { --slide-padding: 32px; } }
    @media (max-width: 480px) {
      :root { --slide-padding: 20px; }
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
        <div class="tag">CREATIVE</div>
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

- 三色渐变标题（红→橙→黄）
- 卡片顶部 hover 渐变色条
- 标签使用渐变背景
- 三个光晕点（红、橙、紫）
- 导航按钮 hover 渐变填充
