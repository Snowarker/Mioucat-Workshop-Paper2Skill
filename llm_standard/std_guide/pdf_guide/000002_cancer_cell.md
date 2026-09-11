# Cancer Cell 期刊处理规则

## 基本信息
- **出版社**：Elsevier
- **期刊**：Cancer Cell

## 结构要求

### 章节顺序（按文章中首次出现顺序）
1. Authors
2. Correspondence
3. Graphical Abstract
4. In Brief
5. Highlights
6. Abstract (SUMMARY)
7. Introduction
8. Results
9. Discussion
10. Limitations of the study
11. STAR Methods
12. Supplemental Information
13. Acknowledgments
14. Author Contributions
15. Conflict of Interest
16. References

### 必需部分
- In Brief
- Highlights
- Graphical Abstract
- Abstract
- Introduction
- Results
- Discussion
- STAR Methods
- References

### 可选部分
- Authors
- Correspondence
- Limitations of the study
- Supplemental Information
- Acknowledgments
- Author Contributions
- Conflict of Interest
- Data Availability
- Abbreviations
- Supporting Information
- Experimental Model and Study Participant Details
- Method Details
- Quantification and Statistical Analysis

### 处理原则
- **必需章节**：必须提取，无论原始文档中是否存在
- **可选章节**：只要原始MD文档中存在，就必须提取；只有在原始文档中确实不存在时才可以不提取
- 所有章节的提取都应保持内容的完整性和结构的准确性

## 章节结构

### 主文档结构
```
文章ID/
├── chapters/      # 章节目录
│   ├── authors.md              # 作者
│   ├── correspondence.md       # 通信作者
│   ├── graphical_abstract.md   # 图表摘要
│   ├── in_brief.md             # In Brief部分
│   ├── highlights.md           # Highlights部分
│   ├── abstract.md             # 摘要部分
│   ├── introduction.md         # 引言部分
│   ├── results.md              # 结果部分
│   ├── discussion.md           # 讨论部分
│   ├── limitations.md          # 研究局限性
│   ├── star_methods.md         # STAR Methods部分
│   ├── key_resources_table.md  # 关键资源表
│   ├── resource_availability.md # 资源可用性
│   ├── experimental_model.md   # 实验模型和研究参与者详情
│   ├── method_details.md       # 方法详情
│   ├── quantification.md       # 量化和统计分析
│   ├── supplemental_information.md  # 补充信息
│   ├── acknowledgments.md      # 致谢
│   ├── author_contributions.md # 作者贡献
│   ├── conflict_of_interest.md # 利益冲突
│   ├── data_availability.md    # 数据可用性
│   ├── abbreviations.md        # 缩写
│   ├── supporting_information.md  # 支持信息
│   └── references.md           # 参考文献
└── images/        # 图片目录
    ├── figure_abstract.jpeg    # 图表摘要图片
    ├── figure_1.jpeg
    ├── figure_2.jpeg
    └── ...
```

## 章节处理规则

### 章节分割标识
- **主要章节**：使用 "# " 开头的标题进行分割
- **子章节**：使用 "## " 或 "#### " 开头的标题进行分割
- **STAR Methods**：使用 "# STAR+METHODS" 标题进行识别，包含多个子章节
- **Supplemental Information**：可能出现多次，需要合并处理

### 主要章节处理

#### 前置章节
- **Authors**：查找 "# Authors" 标题，提取完整作者列表
- **Correspondence**：查找 "# Correspondence" 标题，提取完整通信作者信息
- **Graphical Abstract**：查找 "# Graphical abstract" 标题，提取图片引用和相关描述
- **In Brief**：查找 "# In brief" 标题，提取完整内容，包括段落文本
- **Highlights**：查找 "# Highlights" 标题，提取要点列表，保持项目符号格式

#### 核心章节
- **Abstract**：查找 "# SUMMARY" 标题，提取完整摘要文本
- **Introduction**：查找 "# INTRODUCTION" 标题，提取完整引言内容
- **Results**：查找 "# RESULTS" 标题，提取完整结果部分，保持子章节结构
- **Discussion**：查找 "# DISCUSSION" 标题，提取完整讨论部分
- **Limitations of the study**：查找 "# Limitations of the study" 标题，提取完整研究局限性内容

#### STAR Methods 相关章节
- **STAR Methods**：查找 "# STAR+METHODS" 标题，位于 "Limitations of the study" 之后、"Supplemental Information" 之前，提取完整STAR Methods部分，包括子章节
- **Key Resources Table**：从STAR Methods中提取或查找 "# KEY RESOURCES TABLE" 标题，提取完整关键资源表
- **Resource Availability**：从STAR Methods中提取或查找 "# RESOURCE AVAILABILITY" 标题，提取完整资源可用性信息
- **Experimental Model and Study Participant Details**：从STAR Methods中提取或查找 "# EXPERIMENTAL MODEL AND STUDY PARTICIPANT DETAILS" 标题，提取完整实验模型和研究参与者详情
- **Method Details**：从STAR Methods中提取或查找 "# METHOD DETAILS" 标题，提取完整方法详情，包括所有子部分
- **Quantification and Statistical Analysis**：从STAR Methods中提取或查找 "# QUANTIFICATION AND STATISTICAL ANALYSIS" 标题，提取完整量化和统计分析内容

#### 后置章节
- **Supplemental Information**：查找 "# SUPPLEMENTAL INFORMATION" 或 "# Supplemental Information" 标题，位于 "STAR Methods" 之后和 "Acknowledgments" 之前，提取完整补充信息，可能包含多个部分，需要合并处理
- **Acknowledgments**：查找 "# ACKNOWLEDGMENTS" 或 "# Acknowledgments" 标题，位于 "Supplemental Information" 之后，提取完整致谢内容，包括基金信息和感谢对象
- **Author Contributions**：查找 "# AUTHOR CONTRIBUTIONS" 或 "# Author Contributions" 标题，提取完整作者贡献信息，保持列表格式
- **Conflict of Interest**：查找 "# DECLARATION OF INTERESTS" 或 "# Conflict of Interest" 标题，提取完整利益冲突声明
- **Data Availability**：查找 "# DATA AVAILABILITY" 或 "# Data Availability" 标题，提取完整数据可用性信息，包括数据存储位置和访问链接
- **Abbreviations**：查找 "# ABBREVIATIONS" 或 "# Abbreviations" 标题，提取完整缩写列表，保持格式清晰
- **Supporting Information**：查找 "# SUPPORTING INFORMATION" 或 "# Supporting Information" 标题，提取完整支持信息描述和链接
- **References**：查找 "# REFERENCES" 标题或文章末尾的引用列表，提取完整参考文献列表

## 图片处理规则

### 图片命名规则
- **图表摘要**：`figure_abstract.jpeg`
- **正文图表**：`figure_1.jpeg`, `figure_2.jpeg`, ...
- **补充图表**：`figure_s1.jpeg`, `figure_s1a.jpeg`, `figure_s2.jpeg`, ...
- **期刊封面**：`journal_cover.jpeg`

### 图片引用格式
- **主文档**：`![Figure 1](images/figure_1.jpeg)`
- **图表摘要**：`![Graphical Abstract](images/figure_abstract.jpeg)`
- **补充图表**：`![Figure S1](images/figure_s1.jpeg)`

### 杂志期刊相关图片处理
- **识别**：使用 `scripts/check_image_sizes.py` 脚本检查图片尺寸特征
- **特征**：
  - 宽高比非常大（>10）的长条形图片（可能是页眉、页脚或分隔线）
  - 中等宽度（240-260px）、高度（70-80px）的图片（可能是小图标或装饰元素）
  - 小尺寸（48-52px）的方形图片（可能是符号或标记）
- **处理**：这些图片通常是 PDF 转换过程中的中间产物，与文章内容无关，可考虑删除
- **检查方法**：
  ```bash
  # 在项目虚拟环境中运行
  venv\Scripts\python.exe scripts/check_image_sizes.py "path/to/images"
  ```

## 特殊格式处理

### 实验方法子部分
- **识别**：查找 "#### " 开头的子部分标题
- **处理**：保持子部分结构，确保层次清晰

### 结果子章节
- **识别**：查找 "# " 开头的子章节标题
- **处理**：保持子章节结构，确保层次清晰

### 表格处理
- **识别**：查找表格内容
- **处理**：保持表格格式，确保数据完整

### STAR Methods 处理
- **识别**：查找 "# STAR+METHODS" 及其子章节
- **处理**：保持完整的 STAR Methods 结构，包括 Key Resources Table

## 入口文档模板

### 模板结构

```markdown
# [文章标题]

**[作者列表]**

## Publication Information

- **DOI:** [DOI链接]

## Authors

- [作者1]: [单位信息]
- [作者2]: [单位信息]
- ...

## Correspondence

- [通信作者1]: [邮箱]
- [通信作者2]: [邮箱]
- ...

## In Brief

[In Brief内容]

## Highlights

- [Highlight 1]
- [Highlight 2]
- [Highlight 3]
- [Highlight 4]

## Document Structure

This document is organized into the following sections:

1. [In Brief](#in-brief)
2. [Highlights](#highlights)
3. [Graphical Abstract](#graphical-abstract)
4. [Abstract](#abstract)
5. [Introduction](#introduction)
6. [Results](#results)
7. [Discussion](#discussion)
8. [Star Methods](#star-methods)
9. [Experimental Model](#experimental-model)
10. [Method Details](#method-details)
11. [Quantification](#quantification)
12. [Acknowledgments](#acknowledgments)
13. [Author Contributions](#author-contributions)
14. [Conflict of Interest](#conflict-of-interest)
15. [Supplemental Information](#supplemental-information)
16. [References](#references)

## Chapter Navigation

### In Brief

[In Brief内容]

**Full content:** [In Brief](chapters/in_brief.md)

### Highlights

Key findings and significant contributions of the study.

**Full content:** [Highlights](chapters/highlights.md)

### Graphical Abstract

Visual summary of the study's key findings and workflow.

**Full content:** [Graphical Abstract](chapters/graphical_abstract.md)

### Abstract

[摘要内容]

**Full content:** [Abstract](chapters/abstract.md)

### Introduction

Introduction to the study background and objectives.

**Full content:** [Introduction](chapters/introduction.md)

### Results

Comprehensive analysis of the study results.

**Full content:** [Results](chapters/results.md)

### Discussion

Discussion of the study findings and implications.

**Full content:** [Discussion](chapters/discussion.md)

### Star Methods

Detailed methods section including experimental design and procedures.

**Full content:** [Star Methods](chapters/star_methods.md)

### Experimental Model

Details of experimental models used in the study.

**Full content:** [Experimental Model](chapters/experimental_model.md)

### Method Details

Detailed methodology for experiments and analyses.

**Full content:** [Method Details](chapters/method_details.md)

### Quantification

Statistical analysis and quantification methods used in the study.

**Full content:** [Quantification](chapters/quantification.md)

### Acknowledgments

Acknowledgments to contributors, funding sources, and supporting entities.

**Full content:** [Acknowledgments](chapters/acknowledgments.md)

### Author Contributions

Detailed information about the contributions of each author to the study.

**Full content:** [Author Contributions](chapters/author_contributions.md)

### Conflict of Interest

Declaration of any competing interests by the authors.

**Full content:** [Conflict of Interest](chapters/conflict_of_interest.md)

### Supplemental Information

Supplemental data associated with this article.

**Full content:** [Supplemental Information](chapters/supplemental_information.md)

### References

Comprehensive list of references cited in this study.

**Full content:** [References](chapters/references.md)

## Graphical Abstract

![Graphical Abstract](images/figure_abstract.jpeg)

## Figures

### Figure 1: [Figure 1标题]

![Figure 1](images/figure_1.jpeg)

**Description:** [Figure 1描述]

### Figure 2: [Figure 2标题]

![Figure 2](images/figure_2.jpeg)

**Description:** [Figure 2描述]

...

## Supplemental Figures

### Figure S1: [Figure S1标题]

![Figure S1](images/figure_s1.jpeg)

**Description:** [Figure S1描述]

### Figure S2: [Figure S2标题]

![Figure S2](images/figure_s2.jpeg)

**Description:** [Figure S2描述]

...

## Chapter Files

The complete document is available as separate chapter files for easier navigation and processing:

- [In Brief](chapters/in_brief.md)
- [Highlights](chapters/highlights.md)
- [Graphical Abstract](chapters/graphical_abstract.md)
- [Abstract](chapters/abstract.md)
- [Introduction](chapters/introduction.md)
- [Results](chapters/results.md)
- [Discussion](chapters/discussion.md)
- [Star Methods](chapters/star_methods.md)
- [Experimental Model](chapters/experimental_model.md)
- [Method Details](chapters/method_details.md)
- [Quantification](chapters/quantification.md)
- [Acknowledgments](chapters/acknowledgments.md)
- [Author Contributions](chapters/author_contributions.md)
- [Conflict of Interest](chapters/conflict_of_interest.md)
- [Supplemental Information](chapters/supplemental_information.md)
- [References](chapters/references.md)
```

### 使用说明

1. **填充内容**：将模板中的占位符（如 [文章标题]、[作者列表] 等）替换为实际内容
2. **调整章节**：根据具体文章的结构，调整章节列表和顺序
3. **图片描述**：为每个图片添加准确的标题和描述
4. **保持一致性**：确保入口文档的结构与章节文件保持一致
5. **更新链接**：确保所有章节链接指向正确的文件路径

此模板旨在提供一个标准化的入口文档结构，便于后续的处理和阅读。

## 处理流程

1. **文档分析**：分析原始MD文档结构，识别各章节
2. **章节分离**：将内容分离为多个章节文件
3. **图片处理**：提取图片并按照规则重命名
4. **引用更新**：更新文档中的图片引用
5. **质量检查**：检查处理结果的完整性和准确性

## 质量控制

### 检查项
- [ ] 所有必需章节是否完整提取
- [ ] 所有存在的可选章节是否完整提取
- [ ] 图片是否正确命名和引用
- [ ] 章节结构是否保持完整
- [ ] 特殊格式是否正确处理
- [ ] 参考文献是否完整提取
- [ ] 数据可用性信息是否完整提取
- [ ] 致谢内容是否完整提取
- [ ] 作者贡献信息是否完整提取
- [ ] 利益冲突声明是否完整提取
- [ ] 缩写列表是否完整提取
- [ ] 支持信息是否完整提取
- [ ] 补充信息是否完整提取
- [ ] STAR Methods 是否完整提取

### 常见问题

1. **章节识别错误**
   - **原因**：标题格式不一致
   - **解决方案**：检查标题格式，确保正确识别

2. **图片丢失**
   - **原因**：图片提取失败或命名错误
   - **解决方案**：重新提取图片，按照规则重命名

3. **结构不完整**
   - **原因**：章节边界识别不准确
   - **解决方案**：调整章节识别规则，确保完整提取

4. **格式问题**
   - **原因**：特殊格式处理不当
   - **解决方案**：优化格式处理规则，确保正确显示

## 总结

Cancer Cell 期刊的处理规则旨在确保论文文档的结构、格式和内容得到一致、准确的处理。通过遵循本规则，您可以有效地处理 Cancer Cell 期刊的论文，为后续的技能提取做好准备。

随着期刊格式的不断变化，本规则将持续更新和优化，以适应 Cancer Cell 期刊的处理需求。