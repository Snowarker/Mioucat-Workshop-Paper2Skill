# LLM 处理

## 1. 概述

LLM 处理是 Paper2Skill 工具套件中的关键步骤，用于对转换后的 Markdown 文档进行规范化处理，提高文档质量和可读性。本文档提供 LLM 处理的概述和导航，详细内容请参考相关子文档。

## 2. 处理流程

### 2.1 基本流程

1. **准备工作**：激活虚拟环境，准备转换后的 Markdown 文档
2. **规范化处理**：使用 LLM 对文档进行格式规范化、内容结构化等处理
3. **分类存储**：按出版社和期刊分类存储处理结果
4. **质量检查**：检查处理后的文档质量
5. **后续处理**：进行 Skill 提取和组织

### 2.2 详细指南

- **基础规范化处理**：`0001_03_01_basic_processing.md` - 详细的基础规范化处理流程
- **出版社处理指南**：`0001_03_02_publisher_guidelines.md` - 出版社特定的处理指南
  - **Springer Nature**：`0001_03_02_01_springer_nature.md` - Springer Nature 出版社处理指南
- **期刊处理指南**：`0001_03_03_journal_guidelines.md` - 期刊特定的处理指南
  - **Nature Computational Science**：`0001_03_03_01_nature_computational_science.md` - Nature Computational Science 期刊处理指南

## 3. 目录结构

### 3.1 处理结果目录

```
llm_processed/
└── [出版社]/              # 如：Springer Nature
    └── [期刊]/            # 如：Nature Computational Science
        └── [论文名称]/    # 如：Improving atlas-scale single-cell annotation models with hierarchical cross-entropy loss
            ├── [论文名称].md     # 规范化后的 Markdown 文档
            └── images/           # 图片目录
                ├── image_1.png
                ├── image_2.png
                └── ...
```

### 3.2 目录创建方法

```powershell
# 创建 LLM 处理根目录
New-Item -ItemType Directory -Path "llm_processed" -Force

# 创建出版社目录示例
New-Item -ItemType Directory -Path "llm_processed\Springer Nature" -Force

# 创建期刊目录示例
New-Item -ItemType Directory -Path "llm_processed\Springer Nature\Nature Computational Science" -Force

# 创建文章目录示例
New-Item -ItemType Directory -Path "llm_processed\Springer Nature\Nature Computational Science\Improving atlas-scale single-cell annotation models with hierarchical cross-entropy loss" -Force
```

## 4. 质量检查

### 4.1 检查要点

- **文档结构**：确保文档包含完整的结构，标题层级正确
- **图片引用**：确保图片引用正确，图片文件存在
- **内容质量**：确保专业术语使用正确，句子通顺，逻辑连贯

### 4.2 常见问题

| 问题 | 解决方案 | 参考文档 |
|------|---------|----------|
| 处理时间过长 | 检查网络连接，分批处理，优化提示词 | `0001_03_01_basic_processing.md` |
| 处理质量不佳 | 调整提示词，多次处理，人工干预 | `0001_03_01_basic_processing.md` |
| 内存不足 | 分割文档，增加虚拟内存，使用更高配置设备 | `0001_03_01_basic_processing.md` |

## 5. 性能优化

- **批量处理**：对多个文档进行批量处理，提高效率
- **缓存机制**：使用缓存避免重复处理
- **并行处理**：在支持的情况下使用并行处理

## 6. 后续步骤

- **Skill 提取**：查看 `0001_04_skill_extraction.md` 了解如何提取 skill 信息
- **Skill 组织**：将提取的 skill 按照主题、方法、期刊等分类方式组织

## 7. 扩展建议

### 7.1 出版社扩展

为新的出版社创建处理指南：
1. 创建出版社处理指南文档：`0001_03_02_XX_[publisher].md`
2. 在 `0001_03_02_publisher_guidelines.md` 中添加引用
3. 更新目录结构以支持新出版社

### 7.2 期刊扩展

为新的期刊创建处理指南：
1. 创建期刊处理指南文档：`0001_03_03_XX_[journal].md`
2. 在 `0001_03_03_journal_guidelines.md` 中添加引用
3. 更新目录结构以支持新期刊

### 7.3 自动化扩展

- 开发期刊特定的处理脚本
- 实现从 PDF 转换到 LLM 处理的全流程自动化
- 开发质量评估工具，自动评估处理后的文档质量

## 8. 相关文档

- `0001_03_01_basic_processing.md` - 基础规范化处理流程
- `0001_03_02_publisher_guidelines.md` - 出版社处理指南
- `0001_03_02_01_springer_nature.md` - Springer Nature 处理指南
- `0001_03_03_journal_guidelines.md` - 期刊处理指南
- `0001_03_03_01_nature_computational_science.md` - Nature Computational Science 处理指南
- `0001_04_skill_extraction.md` - Skill 提取指南