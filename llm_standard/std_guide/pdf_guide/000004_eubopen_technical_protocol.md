# EUBOPEN 技术协议处理规则

## 基本信息
- **适用对象**：EUBOPEN 机构发布的技术协议、实验指南和操作手册
- **机构**：EUBOPEN（欧洲生物信息学开放联盟）

## 结构要求

### 必需部分
- 概述/目的（Rationale/Aim）
- 实验条件（Experimental conditions）
- 协议流程（Protocol）

### 可选部分
- 关键要求（Key Requirement）
- 资源清单（Key Resources Table）
- 工作流程（Workflow）
- 预期结果（Anticipated results）

## 目录结构

**重要说明**：`llm_processed/` 目录是项目的固有目录，不需要创建，直接在其下创建相应的子目录结构。

**标准目录结构**：
```
llm_processed/
└── {机构名称}/          # 一级目录：机构名称
    └── {文档类型}/       # 二级目录：文档类型（如Technical_Protocols）
        └── {文档标识}/  # 三级目录：使用机构-文档类型-版本号作为标识
            ├── {文档标题}.md        # 入口文档
            ├── chapters/            # 章节文件
            │   ├── rationale.md     # 概述/目的
            │   ├── experimental_conditions.md  # 实验条件
            │   ├── key_requirement.md  # 关键要求
            │   ├── key_resources_table.md  # 资源清单
            │   ├── protocol.md       # 协议流程
            │   ├── workflow.md       # 工作流程
            │   └── anticipated_results.md  # 预期结果
            └── images/             # 图片文件
                ├── figure_1.jpeg
                ├── figure_2.jpeg
                └...
```

**示例**：
```
llm_processed/
└── EUBOPEN/
    └── Technical_Protocols/
        └── EUBOPEN-LiP-MS-Protocol-v1.0/
            ├── EUBOPEN-LiP-MS-Protocol-v1.0.md
            ├── chapters/
            │   ├── rationale.md
            │   ├── experimental_conditions.md
            │   ├── key_requirement.md
            │   ├── key_resources_table.md
            │   ├── protocol.md
            │   ├── workflow.md
            │   └── anticipated_results.md
            └── images/
                ├── figure_1.jpeg
                ├── figure_2.jpeg
                └...
```

## 章节拆分规则

### 1. 章节识别

从原始 MD 文档中识别以下章节：

| 原始章节标题 | 标准化章节文件名 | 说明 |
|-------------|-----------------|------|
| 1. Rationale/Aim | rationale.md | 概述协议的目的和原理 |
| 2. Experimental conditions | experimental_conditions.md | 实验条件总览 |
| 2.1 Key Requirement: | key_requirement.md | 关键要求 |
| 2.2 Key Resources Table: | key_resources_table.md | 资源清单 |
| 3. Protocol | protocol.md | 协议总览 |
| 3.1 Workflow | workflow.md | 工作流程 |
| 3.2 Protocol: | protocol_steps.md | 详细协议步骤 |
| 8. Anticipated results | anticipated_results.md | 预期结果 |

### 2. 拆分原则

- **最小拆分单位**：子章节级别（如 2.1 Key Requirement:）
- **不拆分内容**：协议步骤的子步骤（如 Native lysis and dilution、LiP Step 等）保持在同一章节内
- **保持完整性**：确保每个章节的内容完整，不遗漏任何信息

## 图片处理规则

### 1. 图片识别

- **保留原则**：保留所有与实验流程相关的图片
- **筛选标准**：
  - 保留包含实验流程、结果或数据的图片
  - 移除无关的装饰性图片

### 2. 图片命名

- **命名规则**：使用 `figure_{序号}.{扩展名}` 格式
- **示例**：`figure_1.jpeg`、`figure_2.jpeg`

### 3. 图片存储

- **存储位置**：`images/` 目录
- **路径引用**：使用相对路径引用图片，如 `![](images/figure_1.jpeg)`

## 入口文档结构

**入口文档**（{文档标题}.md）应包含以下内容：

- **文档标题**：机构名称和文档标题
- **版本信息**：文档版本号
- **文档结构**：章节导航列表
- **章节摘要**：各章节的简要摘要
- **图片展示**：所有figure的图片和说明
- **章节文件链接**：指向各章节文件的链接

**示例**：
```markdown
# EUBOPEN

**Limited Proteolysis Coupled to Mass Spectrometry (LiP-MS)**

**Version: v1.0**

## Document Structure
1. [Rationale/Aim](#rationale)
2. [Experimental conditions](#experimental-conditions)
3. [Key Requirement](#key-requirement)
4. [Key Resources Table](#key-resources-table)
5. [Protocol](#protocol)
6. [Workflow](#workflow)
7. [Protocol Steps](#protocol-steps)
8. [Anticipated results](#anticipated-results)

## Chapter Navigation
### Rationale/Aim
This protocol describes the LiP-MS method for profiling structural changes in complex proteomes...
**Full content:** [Rationale/Aim](chapters/rationale.md)

## Figures
### Figure 1: LiP-MS Workflow
![](images/figure_1.jpeg)
**Description:** Experimental LiP-MS workflow...
```

## 唯一标识符生成

### 1. 标识符格式

- **格式**：`{机构名称小写}.{文档类型小写}.{版本号}`
- **示例**：`eubopen.lipms.protocol.v1.0`

### 2. 目录命名

- **三级目录**：使用 `{机构名称}-{文档类型}-{版本号}` 格式
- **示例**：`EUBOPEN-LiP-MS-Protocol-v1.0`

## 处理流程

1. **确定处理文件**：明确要处理的原始MD文档
2. **识别机构信息**：从文档中识别机构名称
3. **确定文档类型**：确定文档类型（如Technical_Protocols）
4. **识别版本号**：从文档或文件名中识别版本号
5. **创建目录结构**：在 `llm_processed/` 目录下创建 `机构名称/文档类型/文档标识/` 三级目录结构
6. **建立内层目录**：在文档标识目录下创建 `chapters/`（章节）和 `images/`（图片）目录
7. **创建空入口文档**：创建空的 `{文档标识}.md` 入口文档
8. **确认原始MD文档章节结构**：仔细阅读原始MD文档，识别所有章节标题和结构
9. **章节拆分**：按照本规则，将内容拆分为多个章节文件
10. **处理图片文件**：复制图片文件到 `images/` 目录并按规则重命名
11. **完善入口文档**：更新入口文档，添加章节导航和图片引用
12. **质量检查**：检查处理结果的质量和完整性

## 最佳实践

### 1. 预处理检查

- **文件完整性**：确保所有必要的文件都已提取
- **结构检查**：检查文档结构是否完整
- **图片检查**：检查图片是否完整且清晰

### 2. 处理流程

1. **分类归档**：将文档分类到正确的机构和文档类型目录
2. **结构整理**：整理文档结构，确保所有部分完整
3. **章节分离**：直接分析原始Markdown文档，将内容分离为多个章节
4. **章节存储**：将分离的章节存放在chapters目录中
5. **图片处理**：将图片文件移动到images目录中并按照规则重命名
6. **引用更新**：更新文档中的图片引用
7. **质量检查**：检查处理结果的质量

### 3. 质量控制

- **一致性**：确保同一机构的处理结果一致
- **准确性**：确保内容和引用的准确性
- **完整性**：确保所有内容都被正确处理
- **可读性**：确保处理后的文档易于阅读和理解

## 常见问题与解决方案

### 1. 机构识别错误

- **问题**：将文档错误分类到错误的机构目录
- **解决方案**：参考文档中的机构标识，确保机构分类准确

### 2. 版本号识别错误

- **问题**：版本号提取错误或缺失
- **解决方案**：从文档标题或内容中提取版本号，确保版本信息准确

### 3. 章节拆分不完整

- **问题**：部分章节内容未被正确拆分
- **解决方案**：仔细阅读原始文档，确保所有章节都被识别和拆分

### 4. 图片处理错误

- **问题**：图片命名或引用错误
- **解决方案**：按照规则重命名图片并更新引用路径

## 故障排除

### 1. 常见错误

| 错误类型 | 原因 | 解决方案 |
|---------|------|----------|
| 目录结构错误 | 机构或文档类型分类错误 | 参考文档信息，修正分类 |
| 图片丢失 | 图片提取失败 | 从原始 PDF 重新提取图片 |
| 引用错误 | 图片路径或文件名错误 | 检查并修正引用路径 |
| 内容缺失 | PDF 提取不完整 | 重新处理 PDF，确保完整提取 |
| 格式不一致 | 处理规则不统一 | 统一处理规则，确保格式一致 |

### 2. 错误处理策略

- **记录错误**：记录处理过程中的错误和异常
- **分析原因**：分析错误产生的原因
- **制定方案**：制定针对性的解决方案
- **实施修复**：实施修复措施
- **验证效果**：验证修复效果

## 总结

EUBOPEN 技术协议的规范化处理是 Paper2Skill 工具的重要环节，它确保了 EUBOPEN 发布的技术文档的结构、格式和内容得到一致、准确的处理。通过遵循本规则的流程和最佳实践，您可以有效地处理 EUBOPEN 的技术协议，为后续的技能提取做好准备。

随着 EUBOPEN 发布新的技术文档，本规则将持续更新和扩展，以适应不同类型技术文档的处理需求。通过模块化的设计和可扩展的框架，Paper2Skill 工具可以灵活应对 EUBOPEN 技术文档的处理挑战，为用户提供高质量的文档处理服务。