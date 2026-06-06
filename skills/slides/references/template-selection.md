# Template Selection Guide

自动选择 beautiful-html-templates 主题模板的规则和流程。

## 场景-模板映射表

| 场景 | 关键词 | 模板 | 风格 |
|------|--------|------|------|
| 投资人路演 | investor, pitch, fund, vc, seed, 融资, 路演 | `slides-dark` | 深色科技风 |
| 商业演示 | business, sales, pitch, commercial, 销售, 商业 | `slides-light` | 简约明亮风 |
| 产品发布 | launch, product, brand, release, 发布, 品牌 | `slides-glassmorphism` | 玻璃拟态 |
| 营销创意 | marketing, creative, campaign, 营销, 创意 | `slides-gradient` | 渐变炫彩 |
| 学术报告 | academic, research, presentation, 学术, 研究 | `slides-minimal` | 极简留白 |
| 设计评审 | design, review, portfolio, 设计, 评审 | `slides-minimal` | 极简留白 |
| 团队分享 | team, all-hands, internal, 团队, 内部 | `slides-light` | 简约明亮风 |
| 技术演讲 | tech, engineering, technical, 技术 | `slides-dark` | 深色科技风 |
| 数据分析 | data, analytics, metrics, chart, 数据 | `slides-dark` | 深色科技风 |
| 默认 | (fallback) | `slides-dark` | 深色科技风 |

## 模板加载流程

```
1. 解析 $ARGUMENTS 中 --template 参数
   → 若找到，直接使用：beautiful-html-templates/templates/{name}.md
   
2. 若未指定，分析演示类型关键词
   → 从映射表匹配最佳模板
   
3. 加载模板文件
   → 读取模板文件中的 CSS 变量和 HTML 骨架
   → 替换标题/内容占位符
   
4. 注入自定义内容
   → 根据 Slide Strategy 生成各页内容
   → 添加 Chart.js 图表
   → 应用布局模式
```

## 参数语法

```
slides create "投资人路演 Deck" 12 --template dark
slides create "产品发布会" 10 --template glassmorphism
slides create "学术报告: Transformer 综述" 15 --template minimal
```

## 模板文件结构

每个模板文件包含：

```markdown
# 模板名称
## 主题变量
```css 中的 CSS 变量定义```

## 完整 HTML
```html 中的完整 HTML 骨架```

## 特色元素
模板独有的视觉亮点
```

## 新增模板

如需添加新模板：

1. 在 `beautiful-html-templates/templates/` 下创建 `slides-{name}.md`
2. 在本文件的映射表中添加新场景映射
