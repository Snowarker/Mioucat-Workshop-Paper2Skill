# Nature Computational Science 期刊处理指南

## 1. 期刊概述

- **出版社**：Springer Nature
- **期刊类型**：计算科学领域专业期刊
- **特点**：
  - 数学公式和算法描述详细
  - 实验结果可视化要求高
  - 代码和数据集引用重要
  - 注重创新性和学术严谨性

## 2. 处理流程

### 2.1 准备工作

1. **创建目录结构**：
   ```powershell
   # 创建出版社目录
   New-Item -ItemType Directory -Path "llm_processed\Springer Nature" -Force
   
   # 创建期刊目录
   New-Item -ItemType Directory -Path "llm_processed\Springer Nature\Nature Computational Science" -Force
   
   # 创建文章目录
   New-Item -ItemType Directory -Path "llm_processed\Springer Nature\Nature Computational Science\[文章名称]" -Force
   
   # 创建图片目录
   New-Item -ItemType Directory -Path "llm_processed\Springer Nature\Nature Computational Science\[文章名称]\images" -Force
   ```

2. **准备原始文件**：
   - 确保 PDF 已转换为 Markdown 文档
   - 确认图片文件夹存在且包含所有图片

### 2.2 文档规范化处理

1. **格式规范化**：
   - 统一标题层级（#、##、###）
   - 规范段落间距和缩进
   - 统一列表格式
   - 确保代码块格式正确

2. **内容结构化**：
   - 确保文档包含摘要、引言、方法、结果、讨论等部分
   - 突出创新点和技术贡献
   - 确保数学公式和算法描述清晰

3. **图片处理**：
   - 识别图片对应关系
   - 复制并命名图片文件
   - 更新图片引用路径

### 2.3 质量检查

- **文档结构检查**：确保目录结构正确，文档包含完整结构
- **内容质量检查**：确保专业术语使用正确，逻辑连贯
- **图片引用检查**：确保图片引用正确，图片文件存在

## 3. 处理要点

### 3.1 出版社通用要点

- **Springer Nature 特点**：
  - 注重创新性和可读性
  - 摘要简洁明了
  - 方法部分详细
  - 结果部分突出创新点

### 3.2 期刊特定要点

- **Nature Computational Science 特点**：
  - 计算科学领域专业期刊
  - 数学公式和算法描述详细
  - 实验结果可视化要求高
  - 代码和数据集引用重要

### 3.3 处理注意事项

1. **目录结构**：
   - 严格按照 "出版社 → 期刊 → 文章名称" 层级
   - 保持目录名称与文章信息一致

2. **文档内容**：
   - 保留原文完整性
   - 确保专业术语翻译准确
   - 参考文献不需要翻译
   - 确保所有链接为相对路径

3. **图片处理**：
   - 只保留有实际意义的图片（如 Figure 1, Figure 2 等）
   - 忽略无意义的图片（如页面装饰、水印等）
   - 确保图片命名与文档引用对应

4. **格式规范**：
   - 标题层级统一
   - 段落间距一致
   - 代码块格式规范
   - 数学公式显示正确

## 4. 常见问题及解决方案

### 4.1 图片对应关系识别困难

**问题**：原始图片文件名与文档中的图片引用不匹配

**解决方案**：
- 分析原始 Markdown 文档中的图片引用位置
- 查看图片内容，与文档中图片描述对比
- 使用图片内容特征（如图表类型、数据点等）进行匹配

### 4.2 数学公式处理

**问题**：数学公式在 Markdown 中显示不正确

**解决方案**：
- 确保数学公式使用正确的 Markdown 语法
- 检查公式中的特殊字符是否正确转义
- 验证公式在渲染后是否显示正常

### 4.3 代码块格式

**问题**：代码块格式不规范

**解决方案**：
- 使用三个反引号 (```) 标记代码块开始和结束
- 为代码块指定正确的语言类型
- 确保代码缩进和格式一致

## 5. 示例参考

### 5.1 文章目录结构示例

```
llm_processed/
└── Springer Nature/
    └── Nature Computational Science/
        └── Improving atlas-scale single-cell annotation models with hierarchical cross-entropy loss/
            ├── Improving atlas-scale single-cell annotation models with hierarchical cross-entropy loss.md
            └── images/
                ├── figure_1.jpeg
                └── figure_2.jpeg
```

### 5.2 文档内容示例

```markdown
# Improving atlas-scale single-cell annotation models with hierarchical cross-entropy loss

## 基本信息

- **出版社**: Springer Nature
- **期刊**: Nature Computational Science
- **发表日期**: 2026-01-30
- **DOI**: https://doi.org/10.1038/s43588-025-00945-z

## 摘要

Accurately annotating cell types is essential for extracting biological insight from single-cell RNA sequencing data...

## 引言

Cell-type annotation is a core step in single-cell RNA sequencing (RNA-seq) pipelines...

## 方法

### 层次化交叉熵损失

We propose a hierarchical cross-entropy (HCE) loss function that explicitly incorporates the hierarchical structure of cell types...

## 结果

### 性能评估

Our experiments show that the HCE loss improves performance across different architectures...

## 讨论

The hierarchical structure of cell types is a biological prior that can be leveraged to improve model performance...

## 参考文献

1. Author, A., et al. (2025). Title of reference. Journal, 1(1), 1-10.
```

## 6. 扩展建议

### 6.1 自动化处理

- 开发脚本自动识别文章结构
- 实现图片自动对应和命名
- 构建规范化质量评估工具

### 6.2 出版社扩展

- 为 Springer Nature 出版社的其他期刊创建类似的处理指南
- 总结 Springer Nature 出版社的通用处理规则

### 6.3 质量优化

- 建立翻译质量评估体系
- 开发格式一致性检查工具
- 构建规范化文档模板库

## 7. 相关文档

- `0001_03_01_basic_processing.md` - 基础规范化处理流程
- `0001_03_02_publisher_guidelines.md` - 出版社处理指南
- `0001_03_02_01_springer_nature.md` - Springer Nature 处理指南
