# Slides Reference

Strategic HTML presentation design with Chart.js data visualization, design tokens, responsive layouts, and copywriting formulas.

## Usage

Activate the `design` skill and specify slides task, e.g. "create a pitch deck".

## Knowledge Base

| Topic | File | Purpose |
|-------|------|---------|
| Creation Guide | `references/slides-create.md` | Step-by-step slide creation workflow |
| Layout Patterns | `references/slides-layout-patterns.md` | Slide layout templates and grid systems |
| HTML Template | `references/slides-html-template.md` | Base HTML structure for presentations |
| Copywriting | `references/slides-copywriting-formulas.md` | AIDA, PAS, FAB for slide content |
| Strategies | `references/slides-strategies.md` | Contextual strategies by presentation type |

## When to Use

- Marketing presentations and pitch decks
- Data-driven slides with Chart.js visualizations
- Strategic slide design with layout patterns
- Copywriting-optimized presentation content
- Investor decks, sales presentations, team updates

## Key Features

- **Chart.js Integration**: Bar, line, pie, doughnut, radar charts
- **Design Tokens**: Consistent spacing, colors, typography
- **Responsive**: Works on desktop and mobile
- **Copywriting**: Built-in AIDA, PAS, FAB formulas
- **Layout Patterns**: Hero, split, grid, comparison, timeline

## External Template Integration

自动调用 `beautiful-html-templates` 技能获取精美主题模板（详见 `C:/Users/25097/.claude/skills/beautiful-html-templates/SKILL.md`）。

场景-模板映射：
- 投资人/路演 → `slides-dark`（深色科技风）
- 商业/销售 → `slides-light`（简约明亮风）
- 产品发布 → `slides-glassmorphism`（玻璃拟态）
- 营销/创意 → `slides-gradient`（渐变炫彩）
- 学术/设计 → `slides-minimal`（极简留白）

## Workflow

1. Parse presentation type from user request
2. Detect template from context → load from `beautiful-html-templates/templates/`
3. Load `references/slides-create.md` for creation guide
4. Select layout patterns from `references/slides-layout-patterns.md`
5. Apply copywriting formulas from `references/slides-copywriting-formulas.md`
6. Use HTML template from `references/slides-html-template.md` (fallback) or selected beautiful template
7. Apply strategy from `references/slides-strategies.md`
