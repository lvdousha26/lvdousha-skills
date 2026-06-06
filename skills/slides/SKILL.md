---
name: ckm:slides
description: Create strategic HTML presentations with Chart.js, design tokens, responsive layouts, copywriting formulas, and contextual slide strategies. 自动调用 beautiful-html-templates 技能选择精美主题模板。
argument-hint: "[topic] [slide-count] [--template <dark|light|glassmorphism|gradient|minimal>]"
metadata:
  author: claudekit
  version: "2.0.0"
---

# Slides

Strategic HTML presentation design with data visualization.

<args>$ARGUMENTS</args>

## When to Use

- Marketing presentations and pitch decks
- Data-driven slides with Chart.js
- Strategic slide design with layout patterns
- Copywriting-optimized presentation content

## Subcommands

| Subcommand | Description | Reference |
|------------|-------------|-----------|
| `create` | Create strategic presentation slides | `references/create.md` |

## External Skill Integration

`slides` 自动调用 `beautiful-html-templates` 技能获取精美 HTML 模板。

### 模板选择逻辑

1. 用户指定 `--template` 参数 → 使用对应模板
2. 根据演示场景自动匹配：
   - 投资人/路演 → `slides-dark`
   - 商业/销售 → `slides-light`
   - 产品发布/品牌 → `slides-glassmorphism`
   - 营销/创意 → `slides-gradient`
   - 学术/设计/评审 → `slides-minimal`
3. 未指定时默认 `slides-dark`

### 模板文件位置

```
C:/Users/25097/.claude/skills/beautiful-html-templates/templates/
  ├── slides-dark.md
  ├── slides-light.md
  ├── slides-glassmorphism.md
  ├── slides-gradient.md
  ├── slides-minimal.md
  └── landing-saas.md
```

## References (Knowledge Base)

| Topic | File |
|-------|------|
| Layout Patterns | `references/layout-patterns.md` |
| HTML Template | `references/html-template.md` |
| Copywriting Formulas | `references/copywriting-formulas.md` |
| Slide Strategies | `references/slide-strategies.md` |
| Template Selection | `references/template-selection.md` |

## Routing

1. Parse subcommand and args from `$ARGUMENTS`
2. Detect `--template` parameter or infer template from context
3. Load `beautiful-html-templates` template file for selected theme
4. Load corresponding `references/{subcommand}.md`
5. Execute with remaining arguments
