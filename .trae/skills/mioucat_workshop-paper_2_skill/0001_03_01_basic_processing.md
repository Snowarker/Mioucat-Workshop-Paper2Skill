# 基础规范化处理流程

## 1. 概述

基础规范化处理流程是 LLM 处理的核心环节，负责对转换后的 Markdown 文档进行标准化处理，提高文档质量和可读性，为后续的 Skill 提取做准备。

## 2. 前提条件

- 虚拟环境已激活
- PDF 已成功转换为 Markdown 文档
- 图片文件夹存在且包含所有图片

## 3. 操作步骤

### 3.1 准备工作

1. **激活虚拟环境**：
   ```powershell
   # 激活虚拟环境
   venv\Scripts\activate
   ```

2. **检查原始文件**：
   ```powershell
   # 查看转换后的文件
   Get-ChildItem -Path "pdf\output" -Recurse
   ```

### 3.2 规范化处理

使用 LLM 对转换后的 Markdown 文档进行规范化处理：

1. **格式规范化**：
   - 统一标题层级
   - 调整段落间距
   - 规范列表格式
   - 统一引用格式

2. **内容结构化**：
   - 确保文档结构清晰
   - 包含完整的章节：摘要、引言、方法、结果、讨论、参考文献等
   - 优化章节标题
   - 确保内容逻辑连贯
   - **参考文献处理**：将参考文献作为独立章节处理，创建单独的章节文件

3. **图片引用**：
   - 确保图片引用正确
   - 与图片文件对应
   - 优化图片说明

4. **术语统一**：
   - 统一专业术语的表述方式
   - 确保术语使用一致
   - 标准化缩写和符号

## 4. 示例

### 4.1 格式规范化示例

**处理前**：
```markdown
# 摘要
Accurately annotating cell types is essential for extracting biological insight from single-cell RNA sequencing data.

## 介绍
Cell-type annotation is a core step in single-cell RNA sequencing (RNA-seq) pipelines.
```

**处理后**：
```markdown
# 摘要
Accurately annotating cell types is essential for extracting biological insight from single-cell RNA sequencing data.

## 引言
Cell-type annotation is a core step in single-cell RNA sequencing (RNA-seq) pipelines.
```

### 4.2 内容结构化示例

**处理前**：
```markdown
# 结果
We trained three methods with increasingly complex architectures...
```

**处理后**：
```markdown
# 结果

## 模型训练
We trained three methods with increasingly complex architectures...

## 性能评估
We evaluated each method on 2.6 million human cells...

## 结果分析
The results showed significant improvements...
```

## 5. 常见问题

### 5.1 格式不一致

**问题**：文档格式不一致，标题层级混乱

**解决方案**：
- 使用统一的标题层级
- 确保章节结构清晰
- 检查并调整段落间距

### 5.2 图片引用错误

**问题**：图片引用路径错误或缺失

**解决方案**：
- 检查图片文件是否存在
- 确保引用路径正确
- 添加适当的图片说明

### 5.3 术语使用不一致

**问题**：同一术语在文档中使用不同的表述方式

**解决方案**：
- 统一术语表述
- 创建术语表
- 使用查找替换功能统一术语

## 6. 最佳实践

- **保持一致性**：确保文档格式和术语使用一致
- **关注细节**：注意图片引用、标题层级等细节
- **逐步处理**：分步骤进行规范化处理，确保质量
- **定期检查**：处理过程中定期检查文档质量

## 7. 目录命名规范

在创建 LLM processed 目录结构时，应遵循以下命名规范：

### 7.1 出版商名称
- **处理规则**：将空格替换为下划线 (_)
- **示例**："Springer Nature" → "Springer_Nature"

### 7.2 期刊名称
- **处理规则**：将空格替换为下划线 (_)
- **示例**："Nature Computational Science" → "Nature_Computational_Science"

### 7.3 文章目录名称
- **处理规则**：使用文章的 DOI 编号作为目录名
- **示例**："Improving atlas-scale single-cell annotation models with hierarchical cross-entropy loss" → "s43588-025-00945-z"

### 7.4 最终目录结构示例

```
llm_processed/
└── Springer_Nature/           # 出版商名称（空格替换为下划线）
    └── Nature_Computational_Science/  # 期刊名称（空格替换为下划线）
        └── s43588-025-00945-z/        # 文章目录（使用 DOI 编号）
            ├── chapters/              # 章节文件
            │   ├── abstract.md        # 摘要
            │   ├── introduction.md    # 引言
            │   ├── methods.md         # 方法
            │   ├── results.md         # 结果
            │   ├── discussion.md      # 讨论
            │   └── references.md      # 参考文献（作为独立章节）
            ├── images/                # 图片文件
            └── s43588-025-00945-z.md  # 主 Markdown 文件（使用 DOI 编号）
```

## 8. 处理流程规范

### 8.1 安全处理原则

1. **禁止删除现有目录**：
   - 不得删除 `llm_processed` 目录或其下的任何现有文件
   - 即使需要重新处理，也应在不影响现有内容的前提下进行

2. **正确的处理顺序**：
   - **第一步**：分析 PDF output 中的 Markdown 文档内容
   - **第二步**：提取关键信息（出版商、期刊、DOI 编号等）
   - **第三步**：根据提取的信息创建新的目录结构
   - **第四步**：对文档内容进行规范化处理，包括识别和提取参考文献部分
   - **第五步**：将处理后的内容保存到新创建的目录中，确保参考文献作为独立章节文件保存

3. **文档分析优先**：
   - 必须先使用大模型分析 Markdown 文档内容
   - 不得直接使用命令行复制文件
   - 所有处理决策应基于文档内容分析结果

4. **图片处理**：
   - 图片文件需要单独处理和重命名
   - 确保图片引用路径正确更新
   - 保持图片质量和原始信息

### 8.2 错误避免

- **避免路径长度问题**：使用 DOI 编号替代长文章标题
- **避免空格问题**：使用下划线替代目录名中的空格
- **避免数据丢失**：不得删除或覆盖现有文件
- **避免盲目复制**：所有文件操作必须基于内容分析

### 8.3 质量控制

- **内容完整性**：确保处理后的文档内容完整，包括参考文献部分
- **格式一致性**：保持文档格式的一致性
- **引用正确性**：确保所有引用（包括图片引用和参考文献引用）正确
- **结构清晰度**：确保目录结构清晰易理解，参考文献作为独立章节存在
- **章节独立性**：确保每个章节（包括参考文献）都作为独立文件存在

## 9. 后续步骤

基础规范化处理完成后，可以：

1. **按出版社处理**：根据文档的出版社选择相应的处理指南
2. **按期刊处理**：根据文档的期刊选择相应的处理指南
3. **质量检查**：确保处理后的文档质量
4. **存储结果**：将处理后的文档存储到指定目录

## 10. 参考资料

- `0001_03_02_publisher_guidelines.md` - 出版社处理指南
- `0001_03_03_journal_guidelines.md` - 期刊处理指南
- `0001_03_05_quality_check.md` - 质量检查方法