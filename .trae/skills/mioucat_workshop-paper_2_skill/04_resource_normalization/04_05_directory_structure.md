# 目录结构规范

## 概述

本文档详细说明 Paper2Skill 工具的目录结构规范，包括标准目录结构、目录层级对齐逻辑和示例结构。通过本章节，您将了解如何正确组织和管理不同类型资源的目录结构。

## 标准目录结构

### 基本原则

**重要说明**：`llm_processed/` 目录是项目的固有目录，不需要创建，直接在其下创建相应的子目录结构。

所有资源类型均采用三级目录结构，各层级对应关系如下：

**项目整体目录结构**：请参考 [资料管理](../05_data_management/05_data_management.md) 文档中的标准目录结构说明。

### PDF 文档目录结构

```
llm_processed/
└── {出版社名称}/          # 一级目录：出版社名称（如 Elsevier、Springer_Nature）
    └── {期刊名称}/       # 二级目录：期刊名称（如 Cell、Nature）
        └── {唯一标识符}/  # 三级目录：文章唯一标识符（优先使用 DOI 后缀）
            ├── {唯一标识符}.md        # 入口文档
            ├── chapters/            # 章节文件
            │   ├── abstract.md     # 摘要
            │   ├── introduction.md # 引言
            │   ├── methods.md      # 方法
            │   ├── results.md      # 结果
            │   ├── discussion.md   # 讨论
            │   └── references.md   # 参考文献
            └── images/             # 图片文件
                ├── figure_1.jpeg
                ├── figure_2.jpeg
                └...
```

### HTML 文档目录结构

```
llm_processed/
└── {网站来源}/          # 一级目录：网站来源（如 Wechat、Xiaohongshu、Nature）
    └── {二级标识}/       # 二级目录：公众号名称、栏目名称等（如 科研圈、技术专栏）
        └── {唯一标识符}/  # 三级目录：文章唯一标识符（如 URL 后缀、文章标题标准化形式）
            ├── {唯一标识符}.md        # 入口文档
            ├── chapters/            # 章节文件
            │   ├── abstract.md     # 摘要
            │   ├── introduction.md # 引言
            │   ├── content.md      # 内容
            │   └── references.md   # 参考文献/链接
            └── images/             # 图片文件
                ├── image_1.jpeg
                ├── image_2.jpeg
                └...
```

### GitHub 项目目录结构

```
llm_processed/
└── {代码托管平台}/      # 一级目录：代码托管平台（如 GitHub、GitLab）
    └── {用户名}/         # 二级目录：GitHub 用户名或组织名
        └── {仓库名称}/    # 三级目录：仓库名称
            ├── {仓库名称}.md        # 入口文档
            ├── chapters/            # 章节文件
            │   ├── overview.md     # 项目概述
            │   ├── installation.md # 安装说明
            │   ├── usage.md        # 使用指南
            │   └── contributing.md # 贡献指南
            └── images/             # 图片文件
                ├── screenshot_1.jpeg
                ├── screenshot_2.jpeg
                └...
```

## 目录层级对齐逻辑

| 资源类型 | 一级目录（对应出版社） | 二级目录（对应期刊） | 三级目录（对应文章独有标识） |
|----------|----------------------|----------------------|------------------------------|
| PDF 文档 | 出版社名称（如 Elsevier） | 期刊名称（如 Cell） | 文章 DOI 后缀 |
| HTML 文档 | 网站来源（如 Wechat） | 公众号/栏目名称 | 文章 URL 或标题标准化形式 |
| GitHub 项目 | 代码托管平台（如 GitHub） | 用户名/组织名 | 仓库名称 |

## 层级对齐说明

- **一级目录**：代表资源的主要来源，对应 PDF 文档的出版社层级
- **二级目录**：代表资源的具体分类，对应 PDF 文档的期刊层级
- **三级目录**：代表资源的唯一标识，对应 PDF 文档的文章独有标识层级

这种层级对齐确保了不同资源类型的目录结构保持一致的组织逻辑，便于统一管理和后续处理。

## 示例结构

```
llm_processed/
├── Elsevier/
│   ├── Cell/
│   │   └── 10.1016_j.cell.2025.01.001/
│   │       ├── Cell_Article_2025.md
│   │       ├── chapters/
│   │       │   ├── abstract.md
│   │       │   ├── introduction.md
│   │       │   ├── methods.md
│   │       │   ├── results.md
│   │       │   ├── discussion.md
│   │       │   └── references.md
│   │       └── images/
│   │           ├── figure_1.jpeg
│   │           ├── figure_2.jpeg
│   │           └...
│   └── Molecular_Cellular_Proteomics/
│       └── 10.1016_j.mcp.2025.01.001/
│           ├── MCP_Article_2025.md
│           ├── chapters/
│           │   ├── abstract.md
│           │   ├── introduction.md
│           │   ├── methods.md
│           │   ├── results.md
│           │   ├── discussion.md
│           │   └── references.md
│           └── images/
│               ├── figure_1.jpeg
│               ├── figure_2.jpeg
│               └...
└── Springer_Nature/
    └── Nature/
        └── 10.1038_nature.2025.12345/
            ├── Nature_Article_2025.md
            ├── chapters/
            │   ├── abstract.md
            │   ├── introduction.md
            │   ├── methods.md
            │   ├── results.md
            │   ├── discussion.md
            │   └── references.md
            └── images/
                ├── figure_1.jpeg
                ├── figure_2.jpeg
                └...
```

## 目录创建流程

1. **识别资源类型**：确定资源的类型（PDF 文档、HTML 文档、GitHub 项目）
2. **确定一级目录**：根据资源类型确定一级目录名称
3. **确定二级目录**：根据资源的具体分类确定二级目录名称
4. **确定三级目录**：使用唯一标识符作为三级目录名称
5. **创建目录结构**：按照层级结构创建相应的子目录
6. **验证目录结构**：确保目录结构符合规范要求

## 常见问题及解决方案

| 问题类型 | 可能原因 | 解决方案 |
|---------|---------|---------|
| 目录结构错误 | 出版社或期刊分类错误 | 参考官方信息，修正分类 |
| 唯一标识符重复 | DOI 信息提取错误 | 仔细检查 DOI 信息，确保使用正确的 DOI 后缀 |
| 目录名称格式错误 | 未遵循命名规范 | 使用下划线替代空格，确保目录名称符合规范 |
| 目录层级不正确 | 资源类型判断错误 | 重新识别资源类型，创建正确的目录层级 |

## 最佳实践

1. **预先规划**：在处理资源前，先规划好目录结构
2. **命名规范**：严格遵循命名规范，确保目录名称一致
3. **层级一致性**：保持不同资源类型的目录层级一致
4. **唯一性**：确保每个资源都有唯一的目录路径
5. **可追溯性**：通过目录结构能够快速定位和访问资源

## 总结

目录结构规范是 Paper2Skill 工具资源管理的重要组成部分。通过遵循本章节的规范，您可以创建和维护一致、清晰的目录结构，确保资源的有效组织和管理。

合理的目录结构不仅便于资源的存储和访问，也为后续的技能提取和文档管理提供了良好的基础。