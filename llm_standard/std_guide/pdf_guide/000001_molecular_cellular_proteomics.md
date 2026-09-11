# Molecular & Cellular Proteomics 期刊处理规则

## 基本信息
- **出版社**：Elsevier
- **期刊**：Molecular & Cellular Proteomics (MCP)

## 结构要求

### 必需部分
- In Brief
- Highlights
- Graphical Abstract
- Abstract
- Introduction
- Experimental Procedures
- Results
- Discussion
- References

### 可选部分
- Author Contributions
- Conflict of Interest
- Acknowledgements
- Data Availability
- Abbreviations
- Supporting Information
- Supplemental Data

### 处理原则
- **必需章节**：必须提取，无论原始文档中是否存在
- **可选章节**：只要原始MD文档中存在，就必须提取；只有在原始文档中确实不存在时才可以不提取
- 所有章节的提取都应保持内容的完整性和结构的准确性

## 章节结构

### 主文档结构
```
文章ID/
├── chapters/      # 章节目录
│   ├── in_brief.md             # In Brief部分
│   ├── highlights.md           # Highlights部分
│   ├── graphical_abstract.md   # 图表摘要
│   ├── abstract.md             # 摘要部分
│   ├── introduction.md         # 引言部分
│   ├── experimental_procedures.md  # 实验方法部分
│   ├── results.md              # 结果部分
│   ├── discussion.md           # 讨论部分
│   ├── data_availability.md    # 数据可用性
│   ├── acknowledgments.md      # 致谢
│   ├── author_contributions.md # 作者贡献
│   ├── conflict_of_interest.md # 利益冲突
│   ├── abbreviations.md        # 缩写
│   ├── supporting_information.md  # 支持信息
│   ├── supplemental_data.md    # 补充数据
│   └── references.md           # 参考文献
└── images/        # 图片目录
    ├── figure_abstract.jpeg    # 图表摘要图片
    ├── figure_1.jpeg
    ├── figure_2.jpeg
    └── ...
```

## 特殊处理

### 1. 章节识别与提取

#### In Brief
- **识别**：查找 "# In Brief" 标题
- **处理**：提取完整内容，包括段落文本

#### Highlights
- **识别**：查找 "# Highlights" 标题
- **处理**：提取要点列表，保持项目符号格式

#### Graphical Abstract
- **识别**：查找 "# Graphical Abstract" 标题
- **处理**：提取图片引用和相关描述

#### Abstract
- **识别**：查找文章标题下方的摘要内容
- **处理**：提取完整摘要文本

#### Introduction
- **识别**：从摘要之后到 "# EXPERIMENTAL PROCEDURES" 之前的内容
- **处理**：提取完整引言内容

#### Experimental Procedures
- **识别**：查找 "# EXPERIMENTAL PROCEDURES" 标题
- **处理**：提取完整方法部分，包括所有子章节
- **子章节**：
  - 样品制备
  - 实验处理
  - 质谱分析
  - 数据处理

#### Results
- **识别**：查找 "# RESULTS" 标题
- **处理**：提取完整结果部分，保持子章节结构

#### Discussion
- **识别**：查找 "# DISCUSSION" 标题
- **处理**：提取完整讨论部分

#### References
- **识别**：查找 "# REFERENCES" 标题或文章末尾的引用列表
- **处理**：提取完整参考文献列表

#### Data Availability
- **识别**：查找 "# DATA AVAILABILITY" 或 "# Data Availability" 标题
- **处理**：提取完整数据可用性信息，包括数据存储位置和访问链接

#### Acknowledgments
- **识别**：查找 "# ACKNOWLEDGMENTS" 或 "# Acknowledgments" 标题
- **处理**：提取完整致谢内容，包括基金信息和感谢对象

#### Author Contributions
- **识别**：查找 "# AUTHOR CONTRIBUTIONS" 或 "# Author Contributions" 标题
- **处理**：提取完整作者贡献信息，保持列表格式

#### Conflict of Interest
- **识别**：查找 "# CONFLICT OF INTEREST" 或 "# Conflict of Interest" 标题
- **处理**：提取完整利益冲突声明

#### Abbreviations
- **识别**：查找 "# ABBREVIATIONS" 或 "# Abbreviations" 标题
- **处理**：提取完整缩写列表，保持格式清晰

#### Supporting Information
- **识别**：查找 "# SUPPORTING INFORMATION" 或 "# Supporting Information" 标题
- **处理**：提取完整支持信息描述和链接

#### Supplemental Data
- **识别**：查找 "# SUPPLEMENTAL DATA" 或 "# Supplemental Data" 标题
- **处理**：提取完整补充数据描述和链接

### 2. 图片处理

#### 图片命名规则
- **图表摘要**：`figure_abstract.jpeg`
- **正文图表**：`figure_1.jpeg`, `figure_2.jpeg`, ...
- **补充图表**：`figure_s1.jpeg`, `figure_s2.jpeg`, ...
- **多小图图表**：`figure_1a.jpeg`, `figure_1b.jpeg`, ...

#### 图片引用格式
- **主文档**：`![Figure 1](images/figure_1.jpeg)`
- **图表摘要**：`![Graphical Abstract](images/figure_abstract.jpeg)`

### 3. 特殊格式处理

#### 实验方法子部分
- **识别**：查找 "#### " 开头的子部分标题
- **处理**：保持子部分结构，确保层次清晰

#### 结果子章节
- **识别**：查找 "# " 开头的子章节标题
- **处理**：保持子章节结构，确保层次清晰

#### 数学公式
- **识别**：查找数学公式和符号
- **处理**：保持公式格式，确保正确显示

#### 表格处理
- **识别**：查找表格内容
- **处理**：保持表格格式，确保数据完整

## 处理流程

1. **文档分析**：分析原始MD文档结构，识别各章节
2. **章节分离**：将内容分离为多个章节文件
3. **图片处理**：提取图片并按照规则重命名
4. **引用更新**：更新文档中的图片引用
5. **质量检查**：检查处理结果的完整性和准确性

## 示例处理

### 输入：原始MD文档
```markdown
# Benchmarking of Quantitative Proteomics Workflows for Limited Proteolysis Mass Spectrometry

# Authors
Tomas Koudelka, Claudio Bassot, and Ilaria Piazza

# In Brief
We evaluate different mass spectrometry-based workflows for quantifying protein structural changes using limited proteolysis coupled with mass spectrometry (LiP-MS)...

# Highlights
- LiP-MS experiments face unique challenges due to peptide-level quantification.
- Benchmarking 12 workflows to evaluate LiP-MS for protein structural change detection.

# Graphical Abstract
![](_page_0_Figure_9.jpeg)

# Benchmarking of Quantitative Proteomics Workflows for Limited Proteolysis Mass Spectrometry

Limited proteolysis coupled with mass spectrometry (LiP-MS) has emerged as a powerful technique...

#### EXPERIMENTAL PROCEDURES

# K562 Proteome Preparation for MS Analysis
K562 cells were grown in RPMI 1640 medium...

#### RESULTS

# Experimental Design for Assessing LiP-MS Efficiency in Detecting Protein Structural Changes
To create a benchmark experiment for systematically assessing protein structural changes...

#### DISCUSSION

In this study, we performed a comprehensive benchmarking of quantitative proteomics workflows for LiP-MS...
```

### 输出：处理后的目录结构
```
LipMS_2025_MCP_Benchmark_PIIS153594762500043X/
├── chapters/
│   ├── in_brief.md
│   ├── highlights.md
│   ├── graphical_abstract.md
│   ├── abstract.md
│   ├── introduction.md
│   ├── experimental_procedures.md
│   ├── results.md
│   ├── discussion.md
│   └── references.md
└── images/
    ├── figure_abstract.jpeg
    ├── figure_1.jpeg
    └── ...
```

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
- [ ] 补充数据是否完整提取

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

## 入口文档结构规范

### 标准结构框架
MCP 期刊入口文档应采用以下统一结构：

1. **标题部分**
   - 主标题：期刊名称 "Molecular & Cellular Proteomics"
   - 副标题：文章标题
   - 作者列表：所有作者姓名

2. **出版信息**
   - **Journal**：Molecular & Cellular Proteomics
   - **Publisher**：Elsevier
   - **Year**：发表年份
   - **DOI**：数字对象标识符（带链接）
   - **Unique Identifier**：文章唯一标识符

3. **作者信息**
   - 作者姓名
   - 作者机构（如有）
   - 通讯作者及联系方式（如有）

4. **摘要**
   - 文章摘要内容
   - 链接到完整摘要文件：`[Abstract](chapters/abstract.md)`

5. **文档结构**
   - 章节列表及顺序
   - 每个章节的链接

6. **章节导航**
   - 每个章节的简短描述
   - 链接到完整章节文件

7. **图形摘要**
   - 图形摘要图片

8. **图表**
   - 所有图表的列表
   - 每个图表的图片和描述（如有）

9. **章节文件**
   - 完整的章节文件列表
   - 每个文件的链接

### 章节顺序
MCP 期刊入口文档的章节应按照以下顺序排列：

1. In Brief
2. Highlights
3. Graphical Abstract
4. Abstract
5. Introduction
6. Experimental Procedures
7. Results
8. Discussion
9. Data Availability
10. Acknowledgments
11. Author Contributions
12. Conflict of Interest
13. Abbreviations
14. Supporting Information/Supplemental Data
15. References

### 格式规范
- 使用 Markdown 格式
- 标题层次清晰
- 链接格式统一：`[章节名称](chapters/章节文件.md)`
- 图片引用格式：`![图片描述](images/图片文件.png)`
- 保持一致的缩进和间距

### 应用方法
1. **创建新文档**：按照此规范创建 MCP 期刊文章的入口文档
2. **更新现有文档**：将现有 MCP 文章的入口文档调整为符合此规范
3. **技能提取**：基于此结构从文档中提取技能知识
4. **索引更新**：更新期刊分类索引，添加新文档信息

### 注意事项
- 保留原文章的章节标题，不进行术语修改
- 确保所有链接正确指向对应的章节文件
- 保持结构一致性，便于后续的自动化处理
- 遵循学术规范，确保文档的专业性和可读性

## 总结

Molecular & Cellular Proteomics 期刊的处理规则旨在确保论文文档的结构、格式和内容得到一致、准确的处理。通过遵循本规则，您可以有效地处理 MCP 期刊的论文，为后续的技能提取做好准备。

随着期刊格式的不断变化，本规则将持续更新和优化，以适应 MCP 期刊的处理需求。