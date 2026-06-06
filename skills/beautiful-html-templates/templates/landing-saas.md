# Landing SaaS Template

SaaS 产品落地页模版 — 适合产品展示、官网首页、营销落地页。

## 完整 HTML

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Product Name</title>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
  <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.1/dist/chart.umd.min.js"></script>
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }

    body {
      font-family: 'Inter', -apple-system, sans-serif;
      background: #0A0A0F;
      color: #fff;
      -webkit-font-smoothing: antialiased;
      overflow-x: hidden;
    }

    .container {
      max-width: 1200px;
      margin: 0 auto;
      padding: 0 24px;
    }

    /* Nav */
    nav {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 20px 0;
      border-bottom: 1px solid rgba(255,255,255,0.06);
    }

    .logo {
      font-size: 22px;
      font-weight: 700;
      background: linear-gradient(135deg, #6C5CE7, #00CEC9);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      background-clip: text;
    }

    .nav-links { display: flex; gap: 32px; align-items: center; }

    .nav-links a {
      color: #8888AA;
      text-decoration: none;
      font-size: 14px;
      font-weight: 500;
      transition: color 0.2s;
    }

    .nav-links a:hover { color: #fff; }

    .btn {
      display: inline-block;
      padding: 10px 24px;
      border-radius: 8px;
      font-size: 14px;
      font-weight: 600;
      text-decoration: none;
      cursor: pointer;
      border: none;
      transition: transform 0.2s, box-shadow 0.2s;
    }

    .btn:hover { transform: translateY(-1px); }

    .btn-primary {
      background: linear-gradient(135deg, #6C5CE7, #00CEC9);
      color: #fff;
      box-shadow: 0 4px 24px rgba(108,92,231,0.3);
    }

    .btn-secondary {
      background: rgba(255,255,255,0.06);
      color: #fff;
      border: 1px solid rgba(255,255,255,0.1);
    }

    /* Hero */
    .hero {
      text-align: center;
      padding: 100px 0 80px;
    }

    .hero-tag {
      display: inline-block;
      padding: 6px 16px;
      border-radius: 20px;
      font-size: 12px;
      font-weight: 500;
      background: rgba(108,92,231,0.12);
      color: #6C5CE7;
      border: 1px solid rgba(108,92,231,0.2);
      margin-bottom: 24px;
    }

    .hero h1 {
      font-size: clamp(40px, 6vw, 72px);
      font-weight: 800;
      line-height: 1.1;
      margin-bottom: 20px;
      letter-spacing: -0.02em;
    }

    .hero h1 span {
      background: linear-gradient(135deg, #6C5CE7, #00CEC9);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      background-clip: text;
    }

    .hero p {
      font-size: clamp(16px, 2vw, 20px);
      color: #8888AA;
      max-width: 600px;
      margin: 0 auto 32px;
      line-height: 1.6;
    }

    .hero-cta { display: flex; gap: 12px; justify-content: center; }

    /* Features */
    .features {
      padding: 80px 0;
      border-top: 1px solid rgba(255,255,255,0.06);
    }

    .features h2 {
      text-align: center;
      font-size: clamp(28px, 3vw, 40px);
      font-weight: 700;
      margin-bottom: 60px;
    }

    .feature-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 24px;
    }

    .feature-card {
      background: rgba(255,255,255,0.03);
      border: 1px solid rgba(255,255,255,0.06);
      border-radius: 16px;
      padding: 32px;
      transition: transform 0.3s, border-color 0.3s;
    }

    .feature-card:hover { transform: translateY(-4px); border-color: rgba(108,92,231,0.2); }

    .feature-icon {
      width: 48px; height: 48px;
      border-radius: 12px;
      background: linear-gradient(135deg, rgba(108,92,231,0.15), rgba(0,206,201,0.15));
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 22px;
      margin-bottom: 16px;
    }

    .feature-card h3 { font-size: 18px; font-weight: 600; margin-bottom: 8px; }
    .feature-card p { font-size: 14px; color: #8888AA; line-height: 1.6; }

    /* Stats */
    .stats {
      display: flex;
      justify-content: center;
      gap: 60px;
      padding: 60px 0;
      border-top: 1px solid rgba(255,255,255,0.06);
    }

    .stat-item { text-align: center; }

    .stat-item .number {
      font-size: 40px;
      font-weight: 700;
      background: linear-gradient(135deg, #6C5CE7, #00CEC9);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      background-clip: text;
    }

    .stat-item .label { font-size: 14px; color: #8888AA; margin-top: 4px; }

    /* CTA */
    .cta-section {
      text-align: center;
      padding: 80px 0;
      border-top: 1px solid rgba(255,255,255,0.06);
    }

    .cta-section h2 {
      font-size: clamp(28px, 3vw, 42px);
      font-weight: 700;
      margin-bottom: 16px;
    }

    .cta-section p {
      color: #8888AA;
      margin-bottom: 32px;
      font-size: 16px;
    }

    .footer {
      text-align: center;
      padding: 24px 0;
      border-top: 1px solid rgba(255,255,255,0.06);
      color: #555577;
      font-size: 13px;
    }

    @media (max-width: 768px) {
      .feature-grid { grid-template-columns: 1fr; }
      .stats { flex-direction: column; gap: 32px; }
      .nav-links { display: none; }
    }
  </style>
</head>
<body>
  <div class="container">
    <nav>
      <div class="logo">Product</div>
      <div class="nav-links">
        <a href="#">Features</a>
        <a href="#">Pricing</a>
        <a href="#">Docs</a>
        <a href="#" class="btn btn-primary">Get Started</a>
      </div>
    </nav>

    <section class="hero">
      <div class="hero-tag">Now in Public Beta</div>
      <h1>Build faster with <span>Product</span></h1>
      <p>Description of your product and its key value proposition. Explain what makes it different.</p>
      <div class="hero-cta">
        <a href="#" class="btn btn-primary">Start Free Trial</a>
        <a href="#" class="btn btn-secondary">Book a Demo</a>
      </div>
    </section>

    <section class="features">
      <h2>Everything you need</h2>
      <div class="feature-grid">
        <div class="feature-card">
          <div class="feature-icon">⚡</div>
          <h3>Fast Performance</h3>
          <p>Built for speed with optimized infrastructure and edge deployment.</p>
        </div>
        <div class="feature-card">
          <div class="feature-icon">🔒</div>
          <h3>Enterprise Security</h3>
          <p>SOC 2 compliant with end-to-end encryption and access controls.</p>
        </div>
        <div class="feature-card">
          <div class="feature-icon">📊</div>
          <h3>Analytics Dashboard</h3>
          <p>Real-time insights with customizable dashboards and reports.</p>
        </div>
      </div>
    </section>

    <div class="stats">
      <div class="stat-item"><div class="number">99.9%</div><div class="label">Uptime</div></div>
      <div class="stat-item"><div class="number">10M+</div><div class="label">Requests/mo</div></div>
      <div class="stat-item"><div class="number">50K+</div><div class="label">Users</div></div>
    </div>

    <section class="cta-section">
      <h2>Ready to get started?</h2>
      <p>Start your free trial today. No credit card required.</p>
      <a href="#" class="btn btn-primary">Start Free Trial →</a>
    </section>

    <div class="footer">© 2026 Product. All rights reserved.</div>
  </div>

  <script>
    // Scroll-triggered animation
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.style.opacity = '1';
          entry.target.style.transform = 'translateY(0)';
        }
      });
    }, { threshold: 0.1 });

    document.querySelectorAll('.feature-card').forEach(el => {
      el.style.opacity = '0';
      el.style.transform = 'translateY(20px)';
      el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
      observer.observe(el);
    });
  </script>
</body>
</html>
```

## 特色元素

- 全功能 SaaS 落地页结构（导航 → Hero → 特性 → 统计 → CTA → Footer）
- IntersectionObserver 滚动入场动画
- 三种 CTA 按钮
- 响应式三列网格 → 单列
- 统计数字渐变色
- Beta 标签
