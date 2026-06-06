Invoke `slides` skill to create persuasive HTML slides using design tokens, Chart.js, and the slide knowledge database.

## Workflow

1. **解析参数** — 提取演示主题、页数、`--template` 参数
2. **选择模板** — 参考 `template-selection.md` 从 `beautiful-html-templates/templates/` 加载对应模板
3. **选择策略** — 从 `slide-strategies.md` 匹配合适的 Deck 结构
4. **生成内容** — 使用 copywriting formulas 编写每页文案
5. **填充 HTML** — 按模板结构填充各页内容，嵌入 Chart.js 图表
6. **输出** — 输出完整单文件 HTML

## Template Loading

```python
# 模板加载逻辑（伪代码）
template_name = detect_template_from_args(args)
if not template_name:
    template_name = match_template_by_context(topic)
template_path = f"C:/Users/25097/.claude/skills/beautiful-html-templates/templates/slides-{template_name}.md"
template_content = read_file(template_path)
html = extract_html_block(template_content)
css_vars = extract_css_vars(template_content)
```

## Task
<task>$ARGUMENTS</task>
