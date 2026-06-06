---
name: beautiful-html-templates
description: 精美 HTML 模板库 — 提供多主题幻灯片、看板、落地页 HTML 模板，支持 Chart.js 集成和响应式布局。供 slides/design 等技能自动调用。
metadata:
  author: claudekit
  version: "2.0.0"
---

# Beautiful HTML Templates

精美 HTML 模板集合，供 slides、design 等技能自动调用生成视觉惊艳的演示文稿。

## 模板目录

| 模板 | 风格 | 适用场景 |
|------|------|----------|
| `slides-dark` | 深色科技风 | 技术演讲、投资人 Deck |
| `slides-light` | 简约明亮风 | 商业演示、团队分享 |
| `slides-glassmorphism` | 玻璃拟态 | 产品发布会、品牌展示 |
| `slides-gradient` | 渐变炫彩 | 营销演示、创意提案 |
| `slides-minimal` | 极简留白 | 学术报告、设计评审 |
| `landing-saas` | SaaS 落地页 | 产品展示、官网 |

## 选择规则

根据演示类型自动匹配合适模板：

| 场景 | 推荐模板 |
|------|----------|
| 投资人/路演 | `slides-dark` |
| 商业/销售 | `slides-light` |
| 产品发布/品牌 | `slides-glassmorphism` |
| 营销/创意 | `slides-gradient` |
| 学术/设计 | `slides-minimal` |

## 模板加载

```markdown
当 slides 技能需要生成 HTML 时，按以下优先级选择模板：
1. 用户显式指定的模板（如 "glassmorphism风格" → `slides-glassmorphism`）
2. 根据场景自动匹配（映射表见上方）
3. 未指定时默认使用 `slides-dark`
```

## 模板格式

每个模板文件包含：
- 完整 HTML 骨架（DOCTYPE + head + body）
- CSS 变量驱动的主题系统
- Chart.js 集成代码段
- 导航交互脚本
- 响应式断点
