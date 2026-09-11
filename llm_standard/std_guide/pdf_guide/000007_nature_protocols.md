# Nature Protocols 期刊处理规则

## 基本信息
- **出版社**：Springer Nature
- **期刊**：Nature Protocols

## 标准处理流程

### 1. 文档分析与识别
- **目的**：分析PDF文档结构，识别文档类型和来源信息
- **内容**：
  - 识别PDF文档类型为Nature Protocols期刊论文
  - 识别出版社为Springer Nature
  - 识别期刊为Nature Protocols
- **特征**：包含DOI链接、作者列表、摘要、方法等典型科研论文结构

### 2. 唯一标识符确认
- **目的**：确认文章的唯一标识符，用于目录命名
- **方法**：
  - 优先从DOI链接中提取后缀（如s41596-022-00771-x）
  - 在文档开头或引用部分查找DOI信息
  - 确保标识符的唯一性和准确性

### 3. 目录结构创建
- **目的**：在llm_processed目录下创建标准三级目录结构
- **结构**：
  ```
  llm_processed/
  └── Springer_Nature/          # 出版社
      └── Nature_Protocols/     # 期刊
          └── [DOI后缀]/        # 唯一标识符
              ├── chapters/     # 章节目录
              └── images/       # 图片目录
  ```
- **说明**：前两级目录（出版社和期刊）固定，第三级目录使用唯一标识符

### 4. 章节拆解
- **目的**：将文档拆分为多个章节文件，便于后续处理

- **必需章节**：
  - Authors
  - Abstract
  - Introduction
  - Materials
  - Procedures
  - Troubleshooting
  - Anticipated Results
  - References
  - Acknowledgements
  - Author Contributions
  - Competing Interests
  - Additional Information
  - Extended Data Figure

- **可选章节**：
  - Box 1
  - Box 2
  - Table 1
  - Table 2
  - ... (其他表格)

- **处理原则**：
  - 必需章节：只要在原始文档中出现就必须提取；如未发现，需提醒用户检查
  - 可选章节：标题在原始MD文档中明确出现才提取；不存在时可跳过
  - 保持内容完整性和结构准确性
  - 章节顺序排列原则：在撰写入口文档时，应严格按照原始MD文档中章节标题的实际位置顺序排列章节内容
  - **章节文件命名规则**：
    - 文件名使用大写字母开头
    - 标题中的空格替换为下划线（如"Anticipated Results" → "Anticipated_Results.md"）
    - 确保文件名符合操作系统命名规范，避免使用特殊字符
- **Authors章节处理原则**：
    - 将Authors章节分为三个部分：Authors List（作者列表）、Affiliations（单位信息）、Contact Information（联系方式）
    - 保留原始文档中的上标格式，确保上标与单位信息的对应关系清晰
    - 每个单位信息单独一行，便于阅读
    - 确保单位名称完整准确，保持与原始文档的一致性
- **章节拆解完整性原则**：
    - 仔细阅读完整的原始MD文档，确保不遗漏任何内容
    - 注意章节的层次结构，确保所有子章节都被包含在对应主章节中
    - 特别注意Materials章节，它通常包含Reagents、Equipment、Equipment setup和Software等多个子部分
    - 特别注意Procedures章节，Nature Protocols文章的实验步骤通常非常详细，包含多个子步骤和关键注意事项
    - 验证每个章节的内容是否完整，避免因文档长度限制或边界识别不准确导致的内容遗漏
    - 对于长章节，确保所有细节内容都被包含，不要只提取标题或概要
    - 建立系统性的检查机制，确保所有章节都被正确处理

- **长文档处理经验教训**：
    - **问题**：处理Nature Protocols等长文档时，部分内容被遗漏，特别是详细的实验步骤和材料信息
    - **原因**：
      - 文档理解不全面，对章节边界的判断不够准确
      - 文件读取限制，可能受到文件大小限制的影响
      - 处理流程不完善，缺乏系统性的检查机制
      - 注意力分配问题，对长章节的关注度不够
      - 标准不明确，对长章节的处理标准不够清晰
    - **解决方案**：
      - 完整读取原始MD文档，确保获取所有内容
      - 建立更系统的章节拆解流程，确保每个章节都包含完整信息
      - 对长章节进行详细分析，确保所有重要细节都被包含
      - 参考原始文档的结构，确保章节内容的完整性
      - 增加质量检验步骤，验证每个章节的内容是否完整
      - 特别关注Procedures章节，确保所有实验步骤、关键注意事项和时间估计都被包含
      - 特别关注Materials章节，确保所有试剂、设备、设备设置和软件信息都被包含

### 5. 图片处理
- **目的**：处理图片文件，确保正确命名和引用

- **完整图像处理流程**：

  0. **预处理检查**
     - **检查原始PDF处理目录**：确保原始PDF处理后的MD文档目录下存在 `{文档标识}_images` 文件夹，并且该文件夹中包含所有图片文件
       - **错误处理**：如果 `{文档标识}_images` 文件夹不存在或为空，停止处理并与用户交互，提供详细信息包括：检查的目录路径、期望的文件夹结构
     - **检查LLM process目录结构**：确保 `llm_processed` 目录下的对应文章目录中除了 `chapters` 目录外，还存在 `images` 目录；如果不存在，需先创建
       - **错误处理**：如果 `images` 目录不存在，创建该目录；如果创建失败，停止处理并与用户交互，提供详细信息包括：检查的目录路径、创建失败的原因
     - **用户交互原则**：在检查过程中发现任何错误或不合理的情况，应及时停止流程，向用户提供详细信息（包括检查的目录路径、发现的问题），等待用户确认后再继续处理

  1. **图片复制**
     - 将前期脚本处理生成的图片文件复制到 `llm_processed` 目录下的对应 `images` 文件夹中
     - 确保所有图片文件都被正确复制，包括正文图片和扩展数据图片

  2. **图片尺寸检查**
     - 运行 `scripts/check_image_sizes.py` 脚本检查图片尺寸特征
     - 识别并排除PDF转换过程中的无关图片（如页眉、页脚、分隔线等）
     - **关键图片识别**：只对在原始MD文档中有明确标注的图片（如Fig. 1, Extended Data Fig. 1等）进行重命名
     - **非关键图片处理**：对于无明确标注的图片（如期刊标识、补充材料标识等），不需要进行重命名，保持原始命名
     - 检查方法：
       ```bash
       # 在项目虚拟环境中运行
       venv\Scripts\python.exe scripts/check_image_sizes.py "path/to/images"
       ```
     - 分析脚本输出，识别异常尺寸的图片（如非常宽的图片可能是期刊标识或分隔线）
     - **Nature Protocols 期刊常见非关键图片特征**：
       | 图片类型 | 文件名 | 宽度 | 高度 | 宽高比 | 特征 |
       |---------|--------|------|------|--------|------|
       | 期刊标识 | journal_cover.jpeg | 297 | 104 | 2.86 | Nature Protocols 期刊的商标标识，通常位于文档开头 |
       | Check for Update 链接 | supplementary_material.jpeg | 201 | 39 | 5.15 | 引导到补充信息更新网站的链接图片，通常位于标题附近 |

  3. **图片标注匹配**
     - **正确方法**：使用文本搜索工具（如Grep）在原始MD文档中搜索所有图片标注（如 "Fig. \d+", "Extended Data Fig. \d+" 等）
     - **建立对应关系**：
       - 逐页检查文档，找到每个图片文件对应的实际标注
       - 创建图片文件与标注的映射表，确保一一对应
       - 特别注意文档末尾的Extended Data Fig. 部分
     - **常见错误与解决方案**：
       - **错误**：仅根据页面编号和图片编号进行顺序匹配
       - **后果**：将正文图片错误分类为Extended Data Fig.，或匹配到错误的标注
       - **解决方案**：
         - 使用文本搜索工具搜索所有图片标注
         - 逐页检查图片的实际标注和上下文
         - 建立完整的映射表后再进行重命名
     - **验证对应关系**：确保重命名后的文件与原文中的标注一一对应

  4. **图片重命名**
     - **图片命名规则**：
       - 正文图表：`Fig_1.jpeg`, `Fig_2.jpeg`, ...（对应原文中的 "Fig. 1", "Fig. 2" 等，保持大小写一致，点号替换为下划线）
       - 补充图表：`Fig_S1.jpeg`, `Fig_S1a.jpeg`, ...（对应原文中的 "Fig. S1", "Fig. S1a" 等，保持大小写一致，点号替换为下划线）
       - 扩展数据图表：`Extended_Data_Fig_1.jpeg`, `Extended_Data_Fig_2.jpeg`, ...（对应原文中的 "Extended Data Fig. 1", "Extended Data Fig. 2" 等，保持大小写一致，空格和点号替换为下划线）
     - **Nature Protocols 期刊图片标签规范**：
       - **正文图片**：原文中使用 "Fig. 1", "Fig. 2" 等格式
       - **扩展数据图片**：原文中使用 "Extended Data Fig. 1", "Extended Data Fig. 2" 等格式
       - **图片编号**：严格按照原文中的编号进行命名，确保与原文一致
       - **大小写保持**：文件名应保持与原文标注一致的大小写
       - **格式转换**：将原文中的点号(.)和空格替换为下划线(_)作为文件名
       - **多小图处理**：对于包含多个小图的图片，使用 "Fig_1a.jpeg", "Extended_Data_Fig_2b.jpeg" 等格式（对应原文中的 "Fig. 1a", "Extended Data Fig. 2b" 等）
     - **图片文件重命名步骤**：
       1. **识别原文标注**：在原始MD文档中找到图片的标注
       2. **保持大小写**：确保文件名的大小写与原文标注一致
       3. **格式转换**：将点号(.)和空格替换为下划线(_)
       4. **添加扩展名**：添加 ".jpeg" 扩展名
       5. **验证对应关系**：确保重命名后的文件与原文中的标注一一对应

  5. **处理结果总结**
     - 在聊天框中总结图像处理结果
     - 列出排除的图片（如页眉、页脚等无关图片）
     - 列出重命名的图片及其对应的原文标注
     - 请用户确认图片标注是否正确

  6. **文档更新**
     - 在入口文档中添加图片引用、完整标题和详细描述
     - 确保所有图片信息按文档顺序排列
     - 检查章节文档中是否需要建立图片相关的引用关系

- **示例**：
  - 原文标注："Fig. 1" → 文件名：`Fig_1.jpeg`
  - 原文标注："Fig. 2a" → 文件名：`Fig_2a.jpeg`
  - 原文标注："Extended Data Fig. 1" → 文件名：`Extended_Data_Fig_1.jpeg`
  - 原文标注："Extended Data Fig. 2b" → 文件名：`Extended_Data_Fig_2b.jpeg`

- **图片引用格式**：
  - 入口文档：`![Fig. 1](images/Fig_1.jpeg)`
  - 章节文档：`![Fig. 1](../images/Fig_1.jpeg)`
  - 补充图表：`![Fig. S1](images/Fig_S1.jpeg)`
  - 扩展数据图表：`![Extended Data Fig. 1](images/Extended_Data_Fig_1.jpeg)`

- **图片标题和描述要求**：
  - **标题**：必须使用原始文档中图片的完整标题
  - **描述**：必须包含原始文档中图片legend的完整内容，不得使用简略描述
  - **完整性**：确保图片的所有面板、注释和说明都被包含在描述中
  - **格式**：保持原始文档中的格式和符号，确保信息的准确性

### 6. 入口文档创建
- **目的**：创建标准化的入口文档，包含导航和图片
- **模板结构**：

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

## Document Structure

This document is organized into the following sections:

[按照原始MD文档中章节标题的实际位置顺序排列]

## Chapter Navigation

[按照原始MD文档中章节标题的实际位置顺序排列，每个章节包含简要描述和完整内容链接]

## Figures

### Figure 1: [Figure 1标题]

![Figure 1](images/figure_1.jpeg)

**Description:** [Figure 1描述]

### Figure 2: [Figure 2标题]

![Figure 2](images/figure_2.jpeg)

**Description:** [Figure 2描述]

...

## Chapter Files

The complete document is available as separate chapter files for easier navigation and processing:

[按照原始MD文档中章节标题的实际位置顺序排列]
```

- **使用说明**：
  1. 填充模板中的占位符（如 [文章标题]、[作者列表] 等）
  2. **关键原则**：严格按照原始MD文档中章节标题的实际位置顺序排列章节内容
  3. 为每个图片添加准确的标题和描述
  4. 确保入口文档结构与章节文件保持一致
  5. 确保所有章节链接指向正确的文件路径

- **章节顺序参考示例**（具体顺序以原始文档为准）：
  1. Authors
  2. Abstract
  3. Introduction
  4. Box 1 (可选)
  5. Materials
  6. Procedures
  7. Troubleshooting
  8. Anticipated Results
  9. References
  10. Extended Data Figure

### 7. 质量检验
- **目的**：检查处理结果的质量和完整性
- **检查项**：
  - [ ] 所有必需章节是否完整提取（Authors、Abstract、Introduction、Materials、Procedures、Troubleshooting、Anticipated Results、References、Extended Data Figure）
- [ ] 所有存在的可选章节是否完整提取（Box 1、Box 2、Table 1等）
- [ ] 图片是否正确命名和引用
- [ ] 章节结构是否保持完整
- [ ] 特殊格式是否正确处理
- [ ] 参考文献是否完整提取
- [ ] 实验步骤是否完整提取
- [ ] 材料和试剂信息是否完整提取
- [ ] 注意事项和安全信息是否完整提取
- [ ] 预期结果是否完整提取
- [ ] 表格是否作为独立文档提取并保持完整结构
- [ ] 原章节中是否正确引用表格文档

- **常见问题及解决方案**：
  1. **章节识别错误**：检查标题格式，确保正确识别
  2. **图片丢失**：重新提取图片，按照规则重命名
  3. **结构不完整**：调整章节识别规则，确保完整提取
  4. **格式问题**：优化格式处理规则，确保正确显示
  5. **实验步骤处理**：保持步骤的层次结构，确保清晰可读
  6. **图legend与章节内容混淆**：注意区分图legend和章节内容，确保正确识别章节边界
  7. **章节边界判断错误**：分析上下文，确保正确识别章节的开始和结束
  8. **内容提取不完整**：确保提取整个章节的所有内容，包括子部分
  9. **参考标准不明确**：建立明确的章节边界识别标准

- **章节拆解经验教训**：
  - **问题**：处理Nature Protocols等长文档时，容易出现章节内容提取不完整或错误的情况
  - **原因**：
    - 图legend与章节内容混淆，特别是当图legend中包含与章节标题相似的文本
    - 章节边界识别不准确，缺乏对文档结构的全局理解
    - 内容提取范围判断错误，只提取了部分内容
    - 处理流程不完善，缺乏系统性的检查机制
  - **解决方案**：
    - 增强上下文分析，不仅关注标题本身，还要分析其上下文
    - 建立章节边界识别标准，区分章节标题和图legend
    - 确保提取整个章节的所有内容，包括其下的子部分
    - 在提取后进行质量检查，验证内容是否与原始文档一致
    - 参考期刊特定规范，针对不同期刊的结构特点调整拆解策略

## 特殊格式处理

### 实验步骤处理
- **识别**：查找 "# Procedure" 标题下的子章节
- **处理**：保持子章节结构，确保步骤清晰

### 材料和试剂处理
- **识别**：查找 "# Materials"、"# Reagents" 等标题
- **处理**：保持列表格式，确保内容完整

### 表格处理
- **识别**：查找表格内容，包括表格标题和表格数据
- **处理**：
  - 保持表格格式，确保数据完整
  - 将每个表格作为独立的章节文档进行提取
  - 表格文档命名规则：`Table_[序号].md`（如`Table_1.md`）
  - 在原章节中添加对表格文档的引用
  - 确保表格的结构和格式在提取过程中保持不变
- **引用方式**：在原章节中使用Markdown链接引用表格文档，如`[Table 1](Table_1.md)`
- **处理原则**：
  - 每个表格都应作为独立的章节文档进行拆分
  - 表格文档应保持原始表格的完整结构
  - 原章节中应包含对表格文档的引用
  - 表格文档的命名应遵循标准命名规则
  - 确保表格内容的完整性和准确性

### 注意事项处理
- **识别**：查找 "!CAUTION"、"CRITICAL" 等标记
- **处理**：保持这些标记和相关内容，确保安全信息完整

## 8. 文档翻译

### 8.1 翻译范围

#### 入口文档翻译内容：
- **文档标题**：需要翻译
- **Chapter Navigation 部分**：需要翻译
- **Figure 的 Title 和 Description**：需要翻译
- **除作者部分和 Document Structure 外的其他大段文字内容**：需要翻译
- **作者部分**：不需要翻译
- **Document Structure 部分**：不需要翻译

#### 章节文件翻译内容：
- **需要翻译的章节**：
  - Abstract
  - Introduction
  - Box 1
  - Materials
  - Procedures
  - Troubleshooting
  - Anticipated Results
  - Table 1
  - Extended Data Figure 中的所有 Figure Title 和 Description
- **不需要翻译的章节**：
  - Authors
  - References
  - Acknowledgements
  - Author Contributions
  - Competing Interests
  - Additional Information
- **章节文件名称**：不需要翻译

### 8.2 翻译模式

#### 入口文档翻译模式：
- **格式**：英文内容保持在上方，对应的中文翻译在下方（行对应行的翻译方式）
- **空行要求**：英文内容和中文翻译之间必须添加空行，以提高可读性
- **示例**：
  ```markdown
  # Proteome-wide structural changes measured with limited proteolysis-mass spectrometry: an advanced protocol for high-throughput applications
  
  # 利用有限 proteolysis-质谱技术测量蛋白质组范围内的结构变化：高通量应用的高级协议
  
  **Liliana Malinovska <sup>1,6</sup>, Valentina Cappelletti<sup>1,6</sup>, Devon Kohler<sup>2,6</sup>, Ilaria Piazza <sup>3</sup>, Tsung-Heng Tsai <sup>4</sup>, Monika Pepelnjak<sup>1</sup>, Patrick Stalder<sup>1</sup>, Christian Dörig <sup>1</sup>, Fabian Sesterhenn<sup>1</sup>, Franziska Elsässer<sup>1</sup>, Lucie Kralickova<sup>1</sup>, Nigel Beaton<sup>5</sup>, Lukas Reiter <sup>5</sup>, Natalie de Souza , Olga Vitek<sup>2</sup> and Paola Picotti <sup>1</sup>**
  
  **Liliana Malinovska <sup>1,6</sup>, Valentina Cappelletti<sup>1,6</sup>, Devon Kohler<sup>2,6</sup>, Ilaria Piazza <sup>3</sup>, Tsung-Heng Tsai <sup>4</sup>, Monika Pepelnjak<sup>1</sup>, Patrick Stalder<sup>1</sup>, Christian Dörig <sup>1</sup>, Fabian Sesterhenn<sup>1</sup>, Franziska Elsässer<sup>1</sup>, Lucie Kralickova<sup>1</sup>, Nigel Beaton<sup>5</sup>, Lukas Reiter <sup>5</sup>, Natalie de Souza , Olga Vitek<sup>2</sup> 和 Paola Picotti <sup>1</sup>**
  ```

#### 章节文件翻译模式：
- **格式**：采用分段翻译方式，翻译一段，记录一段，中英文交杂
- **分割**：每段英文内容后用水平线分割，然后添加对应中文翻译；中文翻译后也用水平线分割，然后添加下一段英文内容
- **原则**：对于长章节，避免一次性翻译过长内容，采用分段翻译方式确保翻译过程不中断
- **要求**：严格按照"翻译一段，记录一段"的模式进行，确保每段英文内容后立即添加对应的中文翻译，中间用水平线分割；中文翻译后也用水平线分割，然后添加下一段英文内容
- **示例**：
  ```markdown
  # Abstract
  
  Proteins regulate biological processes by changing their structure or abundance to accomplish a specific function.
  
  ---  
  
  蛋白质通过改变其结构或丰度来调节生物过程，以完成特定功能。
  
  ---  
  
  In response to a perturbation, protein structure may be altered by various molecular events, such as post-translational modifications, protein-protein interactions, aggregation, allostery or binding to other molecules.
  
  ---  
  
  响应于扰动，蛋白质结构可能会被各种分子事件改变，例如翻译后修饰、蛋白质-蛋白质相互作用、聚集、变构或与其他分子的结合。
  
  ---  
  ```

### 8.3 翻译要求

1. **准确性**：确保翻译准确反映原文内容，专业术语翻译正确
2. **完整性**：完整翻译所有需要翻译的内容，不遗漏任何部分
3. **格式一致性**：保持与原文相同的格式和结构
4. **专业术语**：使用正确的科学和技术术语
5. **可读性**：确保中文翻译通顺易懂，符合中文表达习惯

## 总结

Nature Protocols 期刊的处理规则旨在确保论文文档的结构、格式和内容得到一致、准确的处理。通过遵循本规则，您可以有效地将PDF转换后的MD文档和图片规整化，生成标准化的目录结构和文件，为后续的处理做好准备。

### 标准处理流程回顾

1. **文档分析与识别**：分析PDF文档结构，识别文档类型和来源信息
2. **唯一标识符确认**：确认文章的唯一标识符，用于目录命名
3. **目录结构创建**：在llm_processed目录下创建标准三级目录结构
4. **章节拆解**：将文档拆分为多个章节文件，便于后续处理
5. **图片处理**：处理图片文件，确保正确命名和引用
6. **入口文档创建**：创建标准化的入口文档，包含导航和图片
7. **质量检验**：检查处理结果的质量和完整性
8. **文档翻译**：对指定内容进行中英双语翻译

### 关键原则

1. **语言一致性**：对于需要翻译的内容，提供准确的中英双语版本
2. **图片规范**：按照标准规则命名和引用图片
3. **结构清晰**：使用标准目录结构和文档格式
4. **内容完整**：保留原始文档的所有内容和格式
5. **引用正确**：使用相对路径引用图片和章节文件，符合 Obsidian 格式要求

随着期刊格式的不断变化，本规则将持续更新和优化，以适应 Nature Protocols 期刊的处理需求。