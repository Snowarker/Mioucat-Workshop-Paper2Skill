# 入口文档与图片处理规范

## 入口文档要求

### 入口文档结构

每个资源目录必须包含一个入口文档，命名为 `{资源标识}.md`，作为整个资源的导航中心。入口文档应包含以下内容：

- **资源信息**：资源类型、来源名称
- **标题**：完整标题
- **作者/创建者信息**：作者列表及 affiliations或创建者信息
- **发布信息**：DOI、URL、发布日期、接收日期、修订日期、接受日期等
- **文档结构**：章节导航链接
- **章节摘要**：各章节的简短摘要
- **图表导航**：主要图表的预览和链接

### 章节引用要求

**核心原则**：但凡拆分出来的章节一定需要被引用，而且一定要按照原始Markdown文档中的章节顺序进行引用。

**具体要求**：
1. **完整性**：所有拆分出来的章节文件必须在入口文档中被引用
2. **顺序性**：章节引用顺序必须与原始Markdown文档中的章节顺序一致
3. **一致性**：入口文档中多个位置的章节引用顺序必须保持一致

### 章节引用检查流程

**第一步：数量检查**
1. **统计章节文件数量**：使用 `LS` 工具查看 `chapters/` 目录下的所有文件
   - 命令：`LS path="{资源标识}/chapters"`
2. **统计入口文档引用数量**：使用 `Grep` 工具搜索入口文档中所有章节引用
   - 命令：`Grep pattern="\[.*\]\(chapters/.*\.md\)" path="{资源标识}/{资源标识}.md" output_mode="content"`
3. **对比数量**：确保两个数量一致
   - 如果一致，进入第二步
   - 如果不一致，将缺失的章节引用添加到入口文档中

**第二步：顺序检查**
1. **提取原始MD文档章节顺序**：使用 `Grep` 工具搜索原始MD文档中的所有章节标题
   - 命令：`Grep pattern="^#\s+" path="{原始MD文档路径}" output_mode="content"`
   - 按照行号顺序记录章节出现的先后顺序
2. **提取入口文档章节顺序**：
   - 查看 `Document Structure` 部分的章节列表顺序
   - 查看 `Chapter Files` 部分的章节列表顺序
3. **对比顺序**：
   - 将原始MD文档的章节顺序与入口文档的两个部分进行对比
   - 确保三个顺序完全一致
   - 如果不一致，调整入口文档中的章节顺序

**第三步：完整性验证**
1. **检查 Document Structure**：确保列出了所有章节
2. **检查 Chapter Navigation**：确保为每个章节提供了摘要和链接
3. **检查 Chapter Files**：确保列出了所有章节文件
4. **检查链接格式**：验证所有章节链接都使用了正确的相对路径格式

**常见错误与解决方案**

| 错误类型 | 可能原因 | 解决方案 |
|---------|---------|---------|
| 章节顺序不一致 | 手动编辑时未参考原始MD文档 | 使用 `Grep` 工具提取原始MD文档章节顺序，按照此顺序调整入口文档 |
| 作者与摘要顺序倒置 | 未遵循标准顺序规范 | 确保 Authors 和 Correspondence 章节在 Abstract 章节之前 |
| 章节数量不匹配 | 遗漏了某些章节的引用 | 使用 `LS` 工具统计章节文件数量，确保所有章节都被引用 |
| 链接格式错误 | 路径格式不正确 | 确保使用相对路径格式：`[章节名称](chapters/章节文件名.md)` |
| 部分顺序不一致 | 只更新了入口文档的部分区域 | 确保同时更新 `Document Structure`、`Chapter Navigation` 和 `Chapter Files` 三个部分的顺序 |

**验证方法**

1. **视觉检查**：手动对比原始MD文档和入口文档的章节顺序
2. **工具检查**：使用 `Grep` 工具提取并对比章节顺序
3. **完整性检查**：确保所有章节都在入口文档中被引用
4. **一致性检查**：确保入口文档中所有部分的章节顺序一致

### PDF文档入口文档模板

```markdown
# {期刊名称}

**{文章标题}**

**{作者列表}**

## Publication Information

- **DOI:** [{DOI}](https://doi.org/{DOI})
- **Published:** {发布日期}
- **Received:** {接收日期}
- **Revised:** {修订日期}
- **Accepted:** {接受日期}

## Authors

- {作者1}：{ affiliations }
- {作者2}：{ affiliations }
...

## In Brief

{ In Brief 内容 }

## Highlights

- { highlight 1 }
- { highlight 2 }
...

## Document Structure

This document is organized into the following sections:

1. [Abstract](#abstract)
2. [Introduction](#introduction)
3. [Results](#results)
4. [Discussion](#discussion)
5. [Methods](#methods)
6. [References](#references)

## Chapter Navigation

### Abstract

{ Abstract 摘要 }

**Full content:** [Abstract](chapters/abstract.md)

### Introduction

{ Introduction 摘要 }

**Full content:** [Introduction](chapters/introduction.md)

...

## Graphical Abstract

![Graphical Abstract](images/figure_abstract.jpeg)

## Figures

### Figure 1: { Figure 标题 }

![Figure 1](images/figure_1.jpeg)

**Description:** { Figure 描述 }

...

## Chapter Files

The complete document is available as separate chapter files for easier navigation and processing:

- [Abstract](chapters/abstract.md)
- [Introduction](chapters/introduction.md)
- [Results](chapters/results.md)
- [Discussion](chapters/discussion.md)
- [Methods](chapters/methods.md)
- [References](chapters/references.md)
```

### HTML文档入口文档模板

```markdown
# {网站名称}

**{文章标题}**

**{作者/创建者}**

## Publication Information

- **URL:** [{URL}]({URL})
- **Published:** {发布日期}

## Authors/Creators

- {作者1}
- {作者2}
...

## Document Structure

This document is organized into the following sections:

1. [Introduction](#introduction)
2. [Content](#content)
3. [References](#references)

## Chapter Navigation

### Introduction

{ 介绍摘要 }

**Full content:** [Introduction](chapters/introduction.md)

### Content

{ 内容摘要 }

**Full content:** [Content](chapters/content.md)

...

## Images

### Image 1: { 图片标题 }

![Image 1](images/image_1.jpeg)

**Description:** { 图片描述 }

...

## Chapter Files

The complete document is available as separate chapter files for easier navigation and processing:

- [Introduction](chapters/introduction.md)
- [Content](chapters/content.md)
- [References](chapters/references.md)
```

### GitHub项目入口文档模板

```markdown
# {项目名称}

**{项目描述}**

**{创建者/组织}**

## Project Information

- **GitHub URL:** [{URL}]({URL})
- **Last Updated:** {更新日期}

## Creators/Contributors

- {贡献者1}
- {贡献者2}
...

## Document Structure

This document is organized into the following sections:

1. [Overview](#overview)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Contributing](#contributing)

## Chapter Navigation

### Overview

{ 项目概述 }

**Full content:** [Overview](chapters/overview.md)

### Installation

{ 安装说明摘要 }

**Full content:** [Installation](chapters/installation.md)

...

## Screenshots

### Screenshot 1: { 截图标题 }

![Screenshot 1](images/screenshot_1.jpeg)

**Description:** { 截图描述 }

...

## Chapter Files

The complete document is available as separate chapter files for easier navigation and processing:

- [Overview](chapters/overview.md)
- [Installation](chapters/installation.md)
- [Usage](chapters/usage.md)
- [Contributing](chapters/contributing.md)
```

## 图片处理规范

### 完整图像处理流程

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
     ```powershell
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
   - 在原始MD文档中查找图片的标注（如 "Fig. 1", "Extended Data Fig. 1" 等）
   - 建立图片文件与原文标注的对应关系
   - 确认每个图片在原文中的位置和引用关系

4. **图片重命名**
   - **PDF文档图片命名规则**：
     - **图表摘要**：`figure_abstract.jpeg`
     - **正文图表**：`Fig_1.jpeg`, `Fig_2.jpeg`, ...（对应原文中的 "Fig. 1", "Fig. 2" 等，保持大小写一致，点号替换为下划线）
     - **补充信息图表**：`Fig_S1.jpeg`, `Fig_S1a.jpeg`, ...（对应原文中的 "Fig. S1", "Fig. S1a" 等，保持大小写一致，点号替换为下划线）
     - **扩展数据图表**：`Extended_Data_Fig_1.jpeg`, `Extended_Data_Fig_2.jpeg`, ...（对应原文中的 "Extended Data Fig. 1", "Extended Data Fig. 2" 等，保持大小写一致，空格和点号替换为下划线）
     - **期刊封面**：`journal_cover.jpeg`
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

### 示例

- 原文标注："Fig. 1" → 文件名：`Fig_1.jpeg`
- 原文标注："Fig. 2a" → 文件名：`Fig_2a.jpeg`
- 原文标注："Extended Data Fig. 1" → 文件名：`Extended_Data_Fig_1.jpeg`
- 原文标注："Extended Data Fig. 2b" → 文件名：`Extended_Data_Fig_2b.jpeg`

### HTML文档图片命名规则

- **主图片**：`image_1.jpeg`, `image_2.jpeg`, ...
- **插图**：`illustration_1.jpeg`, `illustration_2.jpeg`, ...
- **截图**：`screenshot_1.jpeg`, `screenshot_2.jpeg`, ...

### GitHub项目图片命名规则

- **截图**：`screenshot_1.jpeg`, `screenshot_2.jpeg`, ...
- **示意图**：`diagram_1.jpeg`, `diagram_2.jpeg`, ...
- **图标**：`icon_1.jpeg`, `icon_2.jpeg`, ...

### 图片重命名要求

**重要**：必须将从原始资源提取的图片文件重命名为标准格式，确保图片名称与引用一致：

1. **识别图片类型**：根据图片内容和位置确定图片类型
2. **确定图片顺序**：按照文档中出现的顺序对图片进行编号
3. **标准化命名**：使用适当的前缀 + 数字/字母的格式
4. **处理多小图情况**：
   - 识别聚集在一起的图片文件，它们通常对应同一个大图的不同小图
   - 观察图片后的统一标题和描述，确定小图的标识（如A、B、C等）
   - 按照顺序为小图命名，如 `figure_5a.jpeg`、`image_3b.jpeg` 等
5. **更新引用**：确保所有文档中的图片引用路径正确
6. **质量控制**：宁可保留所有小图标记，后续再删除不需要的，也不要丢失信息

### 图片引用格式

- **入口文档**：`![Figure 1](images/figure_1.jpeg)` 或 `![Image 1](images/image_1.jpeg)`
- **章节文档**：`![Figure 1](../images/figure_1.jpeg)` 或 `![Image 1](../images/image_1.jpeg)`
- **补充信息**：`![Figure S1](images/figure_s1.jpeg)`

### 图片质量控制

- **分辨率**：确保图片分辨率适中，清晰可读
- **格式**：统一使用 JPEG 格式
- **大小**：优化图片大小，避免过大文件
- **命名**：严格按照命名规则重命名图片
- **一致性**：确保图片引用与实际文件名一致
- **标题完整**：必须使用原始文档中图片的完整标题，不得使用简略标题
- **描述完整**：必须包含原始文档中图片legend的完整内容，不得使用简略描述
- **内容完整性**：确保图片的所有面板、注释和说明都被包含在描述中
- **格式保持**：保持原始文档中的格式和符号，确保信息的准确性
- **多小图处理**：
  - 识别文档中聚集在一起的图片文件，它们通常对应同一个大图的不同小图
  - 观察图片后的统一标题和描述，确定小图的标识（如A、B、C等）
  - 确保所有小图都被正确命名和引用，宁可保留所有小图标记，后续再删除不需要的，也不要丢失信息

### 图片信息提取流程

**核心原则**：入口文档中的图片描述必须包含完整的原始legend信息，确保看图说话的完整性和准确性。由于章节拆分文件中通常不包含图片内容，入口文档是记录完整图片信息的唯一位置。

**为避免figure标题和描述缺失，必须遵循以下提取流程：**

1. **图片识别与定位**
   - 遍历原始MD文档中的所有图片引用
   - 记录每个图片的文件路径和在文档中的位置
   - 建立图片与文档内容的对应关系

2. **标题提取**
   - **图片前标题**：检查图片前的文本，寻找以"Fig."、"Figure"、"图"等开头的标题
   - **图片后标题**：检查图片后的文本，寻找图片描述的第一句话
   - **编号匹配**：确保标题中的编号与图片文件名一致（如Figure 1对应figure_1.jpeg）

3. **描述提取**
   - **直接描述**：提取图片后紧跟的描述文本
   - **段落描述**：如果图片后有完整段落描述，提取整个段落
   - **上下文关联**：结合图片前后的文本，确保描述准确反映图片内容
   - **完整legend**：提取完整的图片legend，包括所有子图的详细信息

4. **扩展数据图表处理**
   - 特别注意文档末尾的Extended Data Figure
   - 提取完整的图表标题和详细描述
   - 确保描述包含图表的所有小图（如Extended Data Fig. 1a, 1b等）

5. **质量控制检查**
   - **完整性检查**：确保每个图片都有对应的标题和描述
   - **一致性检查**：确保标题编号与图片文件名一致
   - **准确性检查**：确保描述准确反映图片内容
   - **完整性验证**：对比原始文档，确保没有遗漏任何图片信息
   - **legend完整性**：确保描述包含完整的原始legend信息，不遗漏任何细节

6. **入口文档集成**
   - 在入口文档的Figures部分为每个图片创建完整条目
   - 包含图片引用、完整标题和详细描述
   - 确保所有图片信息按文档顺序排列
   - **完整legend记录**：在描述中包含完整的原始legend信息

**提取技巧：**
- 使用正则表达式搜索"Fig\.|Figure|图\s*\d"等关键词
- 检查图片前后的文本段落，通常包含标题和描述
- 对于复杂图表，提取完整的描述段落
- 注意文档格式变化，如粗体、斜体等格式标记
- 对于多个小图组成的大图，提取整体标题和每个小图的描述
- 确保提取的描述与原始文档中的legend完全一致

通过严格遵循此流程，可以确保所有figure的标题和描述都被完整提取，避免在入口文档中出现信息缺失的问题。

### 图片尺寸检查

**使用 check_image_sizes.py 脚本**：

该脚本用于检查图片文件的尺寸，特别是 PDF 转换过程中生成的 `_page_*` 文件。

**使用方法**：

1. **激活虚拟环境**：
   ```powershell
   # Windows
   venv\Scripts\activate
   ```

2. **运行脚本**：
   ```powershell
   python scripts/check_image_sizes.py <image_directory>
   ```

   **示例**：
   ```powershell
   python scripts/check_image_sizes.py "pdf/output/Lip_MS_20260227/03LipMS_NatureAging_CSFAging_2022_TonyWyssCoray_36741774_images"
   ```

**检查内容**：
- 图片宽度和高度
- 图片宽高比
- 图片类型分类（非常宽、宽、适中、方形）

**用途**：
- 识别异常尺寸的图片
- 检测可能的图片处理问题
- 确保图片尺寸符合要求

## 补充信息处理

### 补充图表处理

- **编号**：正确编号补充图表（如 Figure S1, Figure S2 等）
- **小图**：对于包含多个小图的补充图表，使用 `figure_s1a.jpeg`, `figure_s1b.jpeg` 等命名
- **描述**：为每个补充图表提供详细的文字描述

### 补充表格处理

- **编号**：正确编号补充表格（如 Table S1, Table S2 等）
- **格式**：确保表格格式清晰，易于阅读
- **内容**：完整保留表格内容，确保数据准确