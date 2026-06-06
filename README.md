# lvdousha-skills

> Claude Code 技能聚合仓库——日常收集整理自社区的实用技能合集

本仓库收录了大量 **Claude Code** 可用的技能（skills），涵盖学术研究、论文写作、代码审查、UI 设计、专利分析、AI 开发等多个领域。绝大多数技能为社区收集整理，非原创。来源包括 oh-my-claude-code、社区成员及网络资源。

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

| 来源 | 说明 |
|------|------|
| 社区收集 | 绝大多数技能来自开源社区，原作者请参考各 SKILL.md 内的注释 |
| [wncfht](https://github.com/wncfht) | memory-skill, agent-basic-skill, writing-skills 中的 25+ 技能 |
| oh-my-claude-code | CCG 工作流框架、部分 ccg 领域知识 |

## 使用方法

```bash
# 克隆整个技能库
git clone https://github.com/lvdousha26/lvdousha-skills.git

# 安装单个技能到 Claude Code
cp -r skills/<skill-name> ~/.claude/skills/
```

## 许可

MIT License
