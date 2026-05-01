# omni-skills

[English](README.md) | 中文

这是一个面向用户的 skills 仓库，当前包含四类常用能力：

- 把 Spec 转成实施策略、阶段顺序和 rollout 路径
- 把 Plan 转成可以执行、可以追踪、可以验收的 Task 系统
- 为 `egui` / `eframe` 应用添加截图能力、截图测试和图片导出流程
- 为 AI Coding 项目维护 Snapshot + Patch 的 Spec source of truth

你可以通过 [`skills.sh`](https://skills.sh/) 安装本仓库中的任意 skill。

## 使用 `skills.sh` 安装

安装单个 skill：

```bash
npx skills add https://github.com/aiomni/omni-skills --skill egui-screenshot
```

本仓库当前提供的 skill 名称：

- `writing-plan`
- `writing-tasks`
- `egui-screenshot`
- `writing-spec`

> [!NOTE]
> 运行安装命令前，请确保你的环境中可以使用 `npx`。

## 快速安装

如果你已经克隆了这个仓库，可以用下面的脚本一次安装全部 skills：

```bash
bash scripts/install-skills.sh
```

如果你更喜欢直接运行一段命令，而不是使用脚本：

```bash
REPO="https://github.com/aiomni/omni-skills"
for skill in writing-plan writing-tasks egui-screenshot writing-spec; do
  npx skills add "$REPO" --skill "$skill"
done
```

## Skills 说明

### `writing-plan`

创建 Spec 和可执行 Task 之间的策略层。

适合这些场景：

- 需要把 Spec 或需求转成技术路线
- 需要定义阶段顺序、依赖关系、编排方式和 rollout 路径
- 需要记录 tradeoff、假设、风险、验证方式和回滚策略
- 需要先识别 task candidates，而不是过早创建原子任务卡
- 需要判断缺失事实是否应该回写为 Spec Patch 建议

安装：

```bash
npx skills add https://github.com/aiomni/omni-skills --skill writing-plan
```

### `writing-tasks`

把 Plan 或明确研发目标下沉成真正可执行、可追踪、可 review 的任务系统。

适合这些场景：

- 需要创建可调度、可重试的任务卡
- 需要明确验收标准，而不是停留在模糊目标
- 需要建立任务卡、dashboard、inbox、执行日志和 review 节点
- 需要把真实开发进展持续回写到任务系统中

安装：

```bash
npx skills add https://github.com/aiomni/omni-skills --skill writing-tasks
```

### `egui-screenshot`

为 `egui` / `eframe` 应用添加、排查或评审截图工作流。

适合这些场景：

- 用 `ViewportCommand::Screenshot` 触发视口截图
- 从 `Event::Screenshot` 获取异步返回的截图结果
- 正确把 `ColorImage` 导出成 PNG
- 增加截图驱动测试或视觉回归测试
- 把截图能力暴露给 AI 工具或宿主桥接层

安装：

```bash
npx skills add https://github.com/aiomni/omni-skills --skill egui-screenshot
```

### `writing-spec`

为 AI Coding 项目创建和维护结构化 Spec System。

适合这些场景：

- 把 `specs/current/` 设为唯一有效的 Spec source of truth
- 分离 Current State Snapshot、Patch Log 和 Archive
- 通过 Patch + Compiler 演进 Spec，而不是整篇重写
- 避免 `log/` 和 `archive/` 污染 LLM context
- 把 Capability、System、Contract Spec Object 维护成小型 Spec Graph

安装：

```bash
npx skills add https://github.com/aiomni/omni-skills --skill writing-spec
```

## 应该先装哪个？

- 如果你的问题主要是 Spec source of truth、Snapshot、Patch、Archive 和 LLM context 治理，先装 `writing-spec`。
- 如果你的问题主要是技术路线、阶段顺序、迁移路径、rollout 或 tradeoff，先装 `writing-plan`。
- 如果你的问题主要是任务卡、执行日志、状态跟踪、验收和 review，先装 `writing-tasks`。
- 如果你的问题主要是 `egui` 界面截图、图片导出或截图测试，先装 `egui-screenshot`。
- 如果你同时需要 Spec governance、实施策略、执行跟踪和 UI 截图，可以一起安装。

## 仓库内容

```text
principles.md
skills/
├── writing-plan/
├── writing-tasks/
├── egui-screenshot/
└── writing-spec/
```

`principles.md` 是一份中文长文参考，覆盖程序设计原则、设计模式、架构模式和并发模式。`writing-spec` skill 仍然把面向 Spec 边界判断的小型原则文件放在 `skills/writing-spec/references/principles/`，方便按需加载。
