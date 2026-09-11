# Molecular Systems Biology 期刊处理规则

## 基本信息
- **出版社**：Wiley_Blackwell
- **期刊**：Molecular Systems Biology

## 结构要求

### 必需部分
- Authors
- Correspondence
- Abstract
- Introduction
- Results
- Discussion
- Methods
- References
- Acknowledgments
- Author Contributions

### 可选部分
- Data Availability
- Peer Review Information
- Disclosure and Competing Interests Statement
- Abbreviations
- Supporting Information

### 处理原则
- **核心原则**：能够拆就一定要拆（只要文档中存在的章节，就必须提取）
- **必需章节**：必须提取，无论原始文档中是否存在
- **可选章节**：只要原始MD文档中存在，就必须提取；只有在原始文档中确实不存在时才可以不提取
- 所有章节的提取都应保持内容的完整性和结构的准确性

## 章节结构

### 主文档结构
```
文章ID/
├── chapters/      # 章节目录
│   ├── authors.md               # 作者信息
│   ├── correspondence.md        # 通讯作者信息
│   ├── abstract.md              # 摘要部分
│   ├── introduction.md          # 引言部分
│   ├── results.md               # 结果部分
│   ├── discussion.md            # 讨论部分
│   ├── methods.md               # 方法部分
│   ├── data_availability.md     # 数据可用性
│   ├── peer_review_information.md # 同行评审信息
│   ├── references.md            # 参考文献
│   ├── acknowledgments.md       # 致谢
│   ├── author_contributions.md  # 作者贡献
│   ├── disclosure_and_competing_interests.md # 利益冲突声明
│   ├── abbreviations.md         # 缩写
│   └── supporting_information.md # 支持信息
└── images/        # 图片目录
    ├── figure_1.jpeg
    ├── figure_2.jpeg
    └── ...
```

## 特殊处理

### 1. 章节识别与提取

#### Authors
- **识别**：查找作者列表部分
- **处理**：提取完整作者信息，包括姓名和所属机构

#### Correspondence
- **识别**：查找通讯作者信息（通常包含邮箱地址）
- **处理**：提取完整通讯作者信息

#### Abstract
- **识别**：查找 "# Abstract" 标题
- **处理**：提取完整摘要文本，包括关键词和DOI信息

#### Introduction
- **识别**：查找 "# Introduction" 标题
- **处理**：提取完整引言内容，包括背景信息和研究动机

#### Results
- **识别**：查找 "# Results" 标题
- **处理**：提取完整结果部分，不拆分小节

#### Discussion
- **识别**：查找 "# Discussion" 标题
- **处理**：提取完整讨论部分，包括研究意义和未来展望

#### Methods
- **识别**：查找 "# Methods" 标题
- **处理**：提取完整方法部分，包括实验设计和流程

#### Data Availability
- **识别**：查找 "Data availability" 或类似标题
- **处理**：提取完整数据可用性信息，包括数据存储位置和访问链接

#### Peer Review Information
- **识别**：查找 "Peer review information" 或类似标题
- **处理**：提取完整同行评审信息

#### References
- **识别**：查找 "# References" 标题
- **处理**：提取完整参考文献列表

#### Acknowledgments
- **识别**：查找 "Acknowledgments" 或 "Acknowledgements" 标题
- **处理**：提取完整致谢内容，包括基金信息和感谢对象

#### Author Contributions
- **识别**：查找 "# Author contributions" 标题
- **处理**：提取完整作者贡献信息，保持列表格式

#### Disclosure and Competing Interests Statement
- **识别**：查找 "Disclosure and competing interests statement" 或类似标题
- **处理**：提取完整利益冲突声明

#### Abbreviations
- **识别**：查找 "Abbreviations" 或类似标题
- **处理**：提取完整缩写列表，保持格式清晰

#### Supporting Information
- **识别**：查找 "Supporting Information" 或类似标题
- **处理**：提取完整支持信息描述和链接

### 2. 图片处理

#### 图片命名规则
- **正文图表**：`figure_1.jpeg`, `figure_2.jpeg`, ...
- **补充图表**：`figure_s1.jpeg`, `figure_s2.jpeg`, ...
- **多小图图表**：`figure_1a.jpeg`, `figure_1b.jpeg`, ...

#### 图片引用格式
- **主文档**：`![Figure 1](images/figure_1.jpeg)`

### 3. 特殊格式处理

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
# Systematic identification of structure-specific protein–protein interactions

# Authors
Aleš Holfeld1, Dina Schuster1,2,3, Fabian Sesterhenn1, ...

# Abstract
The physical interactome of a protein can be altered upon perturbation, modulating cell physiology and contributing to disease...

# Introduction
Many cellular processes are governed by proteins assembled into complexes; thus, protein–protein interactions (PPIs) have multiple essential roles in cells...

# Results

# Protein–protein interactions can be detected by LiP–MS
We tested the feasibility of identifying PPIs using the LiP–MS workflow...

# LiP–MS detects protein–protein interactions with integral membrane proteins
Integral membrane proteins (IMPs) represent a biologically interesting set of proteins...

# Differential interactomes of alpha-synuclein monomer and amyloid fibrils
Having established that LiP–MS can detect known protein–protein interactions, we next applied it in a discovery context...

# Differential interactomes of Rab GTPases
To assess whether our approach could detect candidate interactors of different protein conformations...

# Discussion
```

### 输出：处理后的目录结构
```
s44320-024-00037-6/
├── chapters/
│   ├── abstract.md
│   ├── introduction.md
│   ├── results.md
│   ├── discussion.md
│   └── references.md
└── images/
    ├── figure_1.jpeg
    ├── figure_2.jpeg
    ├── figure_3.jpeg
    ├── figure_4.jpeg
    └── figure_5.jpeg
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
Molecular Systems Biology 期刊入口文档应采用以下统一结构：

1. **标题部分**
   - 主标题：期刊名称 "Molecular Systems Biology"
   - 副标题：文章标题
   - 作者列表：所有作者姓名

2. **出版信息**
   - **Journal**：Molecular Systems Biology
   - **Publisher**：Wiley_Blackwell
   - **Year**：发表年份
   - **DOI**：数字对象标识符（带链接）
   - **Published**：发布日期
   - **Received**：接收日期
   - **Revised**：修订日期
   - **Accepted**：接受日期
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

7. **图表**
   - 所有图表的列表
   - 每个图表的图片和描述（如有）

8. **章节文件**
   - 完整的章节文件列表
   - 每个文件的链接

### 章节顺序
Molecular Systems Biology 期刊入口文档的章节应按照以下顺序排列：

1. Authors
2. Correspondence
3. Abstract
4. Introduction
5. Results
6. Discussion
7. Methods
8. Data Availability
9. Peer Review Information
10. References
11. Acknowledgments
12. Author Contributions
13. Disclosure and Competing Interests Statement
14. Abbreviations
15. Supporting Information

### 格式规范
- 使用 Markdown 格式
- 标题层次清晰
- 链接格式统一：`[章节名称](chapters/章节文件.md)`
- 图片引用格式：`![图片描述](images/图片文件.png)`
- 保持一致的缩进和间距

### 应用方法
1. **创建新文档**：按照此规范创建 Molecular Systems Biology 期刊文章的入口文档
2. **更新现有文档**：将现有 Molecular Systems Biology 文章的入口文档调整为符合此规范
3. **技能提取**：基于此结构从文档中提取技能知识
4. **索引更新**：更新期刊分类索引，添加新文档信息

### 注意事项
- 保留原文章的章节标题，不进行术语修改
- 确保所有链接正确指向对应的章节文件
- 保持结构一致性，便于后续的自动化处理
- 遵循学术规范，确保文档的专业性和可读性

## 总结

Molecular Systems Biology 期刊的处理规则旨在确保论文文档的结构、格式和内容得到一致、准确的处理。通过遵循本规则，您可以有效地处理 Molecular Systems Biology 期刊的论文，为后续的技能提取做好准备。

随着期刊格式的不断变化，本规则将持续更新和优化，以适应 Molecular Systems Biology 期刊的处理需求。