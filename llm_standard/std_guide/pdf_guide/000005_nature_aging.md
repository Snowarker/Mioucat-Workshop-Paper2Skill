# Nature Aging 期刊处理规则

## 基本信息
- **出版社**：Springer Nature
- **期刊**：Nature Aging

## 结构要求

### 章节顺序（按文章中首次出现顺序）
1. Authors
2. Correspondence
3. Abstract
4. Introduction
5. Results
6. Discussion
7. Methods
8. Acknowledgments
9. Author Contributions
10. Competing Interests
11. Additional Information
12. Extended Data Figure
13. References

### 必需部分
- Authors
- Correspondence
- Abstract
- Introduction
- Results
- Discussion
- Methods
- Acknowledgments
- Author Contributions
- Competing Interests
- References

### 可选部分
- Additional Information
- Extended Data Figure
- Data Availability
- Code Availability

### 处理原则
- **必需章节**：一般来说论文的MD文档必定会含有的部分，只要出现就必须提取；如果在原始文档中未发现，必须提醒用户进行检查确认
- **可选章节**：这些章节的标题字符必须在原始MD文档中明确出现才被视为匹配；只要匹配上就必须提取，只有在原始文档中确实不存在时才可以不提取
- 所有章节的提取都应保持内容的完整性和结构的准确性

## 章节结构

### 主文档结构
```
文章ID/
├── chapters/      # 章节目录
│   ├── authors.md              # 作者
│   ├── correspondence.md       # 通信作者
│   ├── abstract.md             # 摘要部分
│   ├── introduction.md         # 引言部分
│   ├── results.md              # 结果部分
│   ├── discussion.md           # 讨论部分
│   ├── methods.md              # 方法部分
│   ├── data_availability.md    # 数据可用性
│   ├── code_availability.md    # 代码可用性
│   ├── references.md           # 参考文献
│   ├── acknowledgments.md      # 致谢
│   ├── author_contributions.md # 作者贡献
│   ├── competing_interests.md  # 利益冲突声明
│   ├── additional_information.md # 附加信息
│   ├── extended_data_figure.md # 扩展数据图表
└── images/        # 图片目录
    ├── figure_1.jpeg
    ├── figure_2.jpeg
    ├── figure_s1.jpeg
    └── ...
```

### 常见章节顺序参考

**Nature Aging 期刊文章的常见章节顺序（基于实际文章分析）：**

1. **前置信息**
   - Authors（作者）
   - Correspondence（通信作者）

2. **核心内容**
   - Abstract（摘要）
   - Introduction（引言）
   - Results（结果）
   - Discussion（讨论）
   - Methods（方法）

3. **数据与代码**
   - Data Availability（数据可用性）
   - Code Availability（代码可用性）

4. **参考文献**
   - References（参考文献）

5. **后置信息**
   - Acknowledgments（致谢）
   - Author Contributions（作者贡献）
   - Competing Interests（利益冲突声明）
   - Additional Information（附加信息）
   - Extended Data Figure（扩展数据图表）

### 章节顺序处理原则

**抽象化处理原则：**

1. **层次化结构**：将章节分为前置信息、核心内容、数据与代码、参考文献、后置信息五个层次
2. **灵活性**：不同文章可能在每个层次内有不同的章节组合和顺序
3. **完整性**：确保所有存在的章节都被识别和提取
4. **一致性**：入口文档的章节顺序必须与原始文档一致
5. **可拓展性**：为可能出现的新章节类型预留空间

**处理建议：**

- **识别层次**：首先识别文章的整体层次结构
- **顺序确认**：在每个层次内确认具体章节的顺序
- **灵活调整**：根据实际文章结构进行适当调整
- **完整性检查**：确保所有章节都被提取和记录
- **顺序验证**：验证入口文档的章节顺序与原始文档一致

通过这种层次化和抽象化的处理方法，可以有效避免章节丢失和顺序错误，同时保持足够的灵活性以适应不同文章的结构变化。

## 章节处理规则

### 章节分割标识
- **主要章节**：使用 "# " 开头的标题进行分割
- **子章节**：使用 "## " 或 "### " 开头的标题进行分割
- **方法部分**：使用 "# Methods" 标题进行识别，包含多个子章节
- **扩展数据**：使用 "# Extended Data Figure" 标题进行识别
- **附加信息**：使用 "# Additional Information" 标题进行识别

### 章节查找方法
1. **全局搜索**：使用关键词搜索（如 "Additional Information"、"Extended Data Figure"、"Data Availability"、"Code Availability"）
2. **文档末尾检查**：检查文档末尾部分，这些章节通常位于参考文献之前或之后
3. **标题格式识别**：注意不同的标题格式，如 "#### **Additional information**"、"**Extended Data Fig. 1**"、"#### **Data availability**"、"#### **Code availability**"
4. **内容特征识别**：根据章节内容特征识别，如补充信息链接、同行评审信息、数据存储库链接、代码存储链接等
5. **图片关联**：通过图片引用（如 "Extended Data Fig. 1"）识别相关章节

### 主要章节处理

#### 前置章节
- **Authors**：查找 "# Authors" 标题，提取完整作者列表
- **Correspondence**：查找 "Correspondence:" 文本，提取完整通信作者信息
- **Abstract**：查找 "# Abstract" 标题，提取完整摘要内容

#### 核心章节
- **Introduction**：查找 "# Introduction" 标题，提取完整引言内容
- **Results**：查找 "# Results" 标题，提取完整结果部分，保持子章节结构
- **Discussion**：查找 "# Discussion" 标题，提取完整讨论部分
- **Methods**：查找 "# Methods" 标题，提取完整方法部分，包括所有子部分

#### 后置章节
- **Acknowledgments**：查找 "# Acknowledgments" 标题，提取完整致谢内容，包括基金信息和感谢对象
- **Author Contributions**：查找 "# Author Contributions" 标题，提取完整作者贡献信息，保持列表格式
- **Competing Interests**：查找 "# Competing Interests" 标题，提取完整利益冲突声明
- **Additional Information**：查找 "# Additional Information" 标题，提取完整附加信息
- **Extended Data Figure**：查找 "# Extended Data Figure" 标题，提取完整扩展数据图表信息
- **Data Availability**：查找 "# Data Availability" 或 "# Data availability" 标题，提取完整数据可用性信息
- **Code Availability**：查找 "# Code Availability" 或 "# Code availability" 标题，提取完整代码可用性信息
- **References**：查找 "# References" 标题或文章末尾的引用列表，提取完整参考文献列表

## 图片处理规则

### 图片命名规则
- **正文图表**：`figure_1.jpeg`, `figure_2.jpeg`, ...
- **补充图表**：`figure_s1.jpeg`, `figure_s1a.jpeg`, `figure_s2.jpeg`, ...
- **扩展数据图表**：`extended_data_figure_1.jpeg`, `extended_data_figure_2.jpeg`, ...

### 图片引用格式
- **主文档**：`![Figure 1](images/figure_1.jpeg)`
- **补充图表**：`![Figure S1](images/figure_s1.jpeg)`
- **扩展数据图表**：`![Extended Data Figure 1](images/extended_data_figure_1.jpeg)`

### 杂志期刊相关图片处理
- **识别**：使用 `scripts/check_image_sizes.py` 脚本检查图片尺寸特征
- **特征**：
  - 宽高比非常大（>10）的长条形图片（可能是页眉、页脚或分隔线）
  - 中等宽度（240-260px）、高度（70-80px）的图片（可能是小图标或装饰元素）
  - 小尺寸（48-52px）的方形图片（可能是符号或标记）
  - Nature Aging 特有的噪音图片：宽度约212px、高度约40px、宽高比约5.30的图片（通常是页面顶部的装饰元素）
- **处理**：这些图片通常是 PDF 转换过程中的中间产物，与文章内容无关，可考虑删除
- **检查方法**：
  ```bash
  # 在项目虚拟环境中运行
  venv\Scripts\python.exe scripts/check_image_sizes.py "path/to/images"
  ```

## 特殊格式处理

### 结果子章节
- **识别**：查找 "# " 开头的子章节标题
- **处理**：保持子章节结构，确保层次清晰

### 方法子部分
- **识别**：查找 "## " 开头的子部分标题
- **处理**：保持子部分结构，确保层次清晰

### 表格处理
- **识别**：查找表格内容
- **处理**：保持表格格式，确保数据完整

## 入口文档模板

### 模板结构

```markdown
# [文章标题]

**[作者列表]**

## Publication Information

- **DOI:** [DOI链接]
- **Published:** [发布日期]
- **Received:** [接收日期]
- **Revised:** [修订日期]
- **Accepted:** [接受日期]

## Authors

- [作者1]: [单位信息]
- [作者2]: [单位信息]
- ...

## Correspondence

- [通信作者1]: [邮箱]
- [通信作者2]: [邮箱]
- ...

## Document Structure

This document is organized into the following sections:

1. [Abstract](#abstract)
2. [Introduction](#introduction)
3. [Results](#results)
4. [Discussion](#discussion)
5. [Methods](#methods)
6. [Acknowledgments](#acknowledgments)
7. [Author Contributions](#author-contributions)
8. [Competing Interests](#competing-interests)
9. [Additional Information](#additional-information)
10. [Extended Data Figure](#extended-data-figure)
11. [References](#references)

## Chapter Navigation

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

### Methods

Detailed methods section including experimental design and procedures.

**Full content:** [Methods](chapters/methods.md)

### Acknowledgments

Acknowledgments to contributors, funding sources, and supporting entities.

**Full content:** [Acknowledgments](chapters/acknowledgments.md)

### Author Contributions

Detailed information about the contributions of each author to the study.

**Full content:** [Author Contributions](chapters/author_contributions.md)

### Competing Interests

Declaration of any competing interests by the authors.

**Full content:** [Competing Interests](chapters/competing_interests.md)

### Additional Information

Additional information associated with this article.

**Full content:** [Additional Information](chapters/additional_information.md)

### Extended Data Figure

Extended data figures and their descriptions.

**Full content:** [Extended Data Figure](chapters/extended_data_figure.md)

### References

Comprehensive list of references cited in this study.

**Full content:** [References](chapters/references.md)

## Figures

### Figure 1: [Figure 1标题]

![Figure 1](images/figure_1.jpeg)

**Description:** [Figure 1描述]

### Figure 2: [Figure 2标题]

![Figure 2](images/figure_2.jpeg)

**Description:** [Figure 2描述]

...

## Extended Data Figures

### Extended Data Figure 1: [Extended Data Figure 1标题]

![Extended Data Figure 1](images/extended_data_figure_1.jpeg)

**Description:** [Extended Data Figure 1描述]

### Extended Data Figure 2: [Extended Data Figure 2标题]

![Extended Data Figure 2](images/extended_data_figure_2.jpeg)

**Description:** [Extended Data Figure 2描述]

...

## Chapter Files

The complete document is available as separate chapter files for easier navigation and processing:

- [Abstract](chapters/abstract.md)
- [Introduction](chapters/introduction.md)
- [Results](chapters/results.md)
- [Discussion](chapters/discussion.md)
- [Methods](chapters/methods.md)
- [Acknowledgments](chapters/acknowledgments.md)
- [Author Contributions](chapters/author_contributions.md)
- [Competing Interests](chapters/competing_interests.md)
- [Additional Information](chapters/additional_information.md)
- [Extended Data Figure](chapters/extended_data_figure.md)
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
- [ ] 附加信息是否完整提取（检查文档末尾，包含补充信息、同行评审信息等）
- [ ] 扩展数据图表是否完整提取（检查文档末尾，包含扩展数据图表及其描述）

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

Nature Aging 期刊的处理规则旨在确保论文文档的结构、格式和内容得到一致、准确的处理。通过遵循本规则，您可以有效地处理 Nature Aging 期刊的论文，为后续的技能提取做好准备。

随着期刊格式的不断变化，本规则将持续更新和优化，以适应 Nature Aging 期刊的处理需求。