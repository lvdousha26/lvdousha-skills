# lvdousha-skills

> Claude Code 技能集合——lvdousha 的实用技能库

本仓库包含大量 **Claude Code** 可用的技能（skills），涵盖学术研究、论文写作、代码审查、UI 设计、专利分析、AI 开发等多个领域。部分技能来自社区贡献（[wncfht](https://github.com/wncfht) 等）。

## 结构

```
lvdousha-skills/
├── skills/          # 独立技能定义（每个子目录一个 skill，含 SKILL.md）
├── agents/          # Agent 定义（ccg, code-simplifier, 及 Codex CLI agents）
```

## 技能分类

| 类别 | 包含技能 |
|------|---------|
| **学术研究** | arxiv, research-lit, research-writing, paper-writing, paper-compile, citation-audit, novelty-check, experiment-plan, deepresearch-skill |
| **论文写作** | paper-write, paper-plan, paper-slides, paper-poster, paper-figure, paper-illustration, rebuttal, paper-note-skill |
| **专利** | patent-pipeline, patent-review, patent-novelty-check, prior-art-search, jurisdiction-format |
| **代码开发** | test-driven-development, code-review-assistant, debug-detective, unit-test-generator, systematic-debugging, git-commit, jujutsu |
| **UI/UX 设计** | ui-ux-pro-max, ui-styling, design, design-system, banner-design, pixel-art, frontend-slides, frontend-style-mimic |
| **AI/ML** | ml-trainer, experiment-queue, monitor-experiment, analyze-results, result-to-claim |
| **前端/Web** | web-devtools, tauri-devtools, frontend-developer, BetterGPT |
| **视频/笔记** | video-note-render-pdf-v0/v1/v2, bilinote-video-note, bilibili-up-digest |
| **幻灯片** | slidev, slides, slides-polish |
| **绘图/可视化** | plot-skill, mermaid-diagram |
| **记忆系统** | memory-skill |
| **日常工具** | humanizer, humanizer-zh, gemini-search, exa-search |
| **项目管理** | planning-with-files, writing-plans, dispatching-parallel-agents, using-superpowers |

## 来源

| 来源 | 包含技能 |
|------|---------|
| lvdousha (本仓库) | 100+ 原创技能（学术、写作、UI、专利等） |
| [wncfht](https://github.com/wncfht) | memory-skill, agent-basic-skill, writing-skills 中的 25+ 技能 |

## 使用方法

```bash
# 克隆整个技能库
git clone https://github.com/lvdousha26/lvdousha-skills.git

# 安装单个技能到 Claude Code
cp -r skills/<skill-name> ~/.claude/skills/
```

## 许可

MIT License
