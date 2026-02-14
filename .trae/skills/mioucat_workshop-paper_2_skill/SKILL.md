---
name: "MiouCat_Workshop-Paper_2_Skill"
description: "介绍 Paper2Skill 工具的使用方法，包括从 PDF 转换为 Markdown、LLM 处理、skill 提炼和代码工具管理的完整流程。"
---

# Paper2Skill 工具指南

## 1. 概述

Paper2Skill 是一个专门用于从学术论文中提取和组织知识技能（skill）的工具套件，通过标准化流程将原始 PDF 文档转换为结构化的知识体系。

## 2. 文档结构

```
MiouCat_Workshop-Paper_2_Skill/
├── SKILL.md                  # 主入口文档
├── 0001_usage_guide.md       # 工具使用指南（概述）
├── 0001_01_environment_setup.md  # 环境设置
├── 0001_02_pdf_conversion.md     # PDF 转换
├── 0001_03_llm_processing.md     # LLM 处理（概述）
├── 0001_03_01_basic_processing.md    # 基础规范化处理
├── 0001_03_02_publisher_guidelines.md # 出版社处理指南
├── 0001_03_02_01_springer_nature.md  # Springer Nature 处理指南
├── 0001_03_03_journal_guidelines.md  # 期刊处理指南
├── 0001_03_03_01_nature_computational_science.md # Nature Computational Science 处理指南
├── 0001_04_skill_extraction.md   # Skill 提取
├── 0002_skill_creation_guide.md  # Skill 创建指南
├── 0002_01_logical_structure.md   # 逻辑层级结构
└── 0002_02_document_length.md     # 文档长度规范
```

## 3. 内容导航

### 3.1 工具使用指南
- `0001_usage_guide.md` - 工具使用指南（概述）
  - `0001_01_environment_setup.md` - 环境设置
  - `0001_02_pdf_conversion.md` - PDF 转换
  - `0001_03_llm_processing.md` - LLM 处理（概述）
    - `0001_03_01_basic_processing.md` - 基础规范化处理
    - `0001_03_02_publisher_guidelines.md` - 出版社处理指南
      - `0001_03_02_01_springer_nature.md` - Springer Nature 处理指南
    - `0001_03_03_journal_guidelines.md` - 期刊处理指南
      - `0001_03_03_01_nature_computational_science.md` - Nature Computational Science 处理指南
  - `0001_04_skill_extraction.md` - Skill 提取

### 3.2 Skill 创建指南
- `0002_skill_creation_guide.md` - Skill 创建指南
  - `0002_01_logical_structure.md` - 逻辑层级结构
  - `0002_02_document_length.md` - 文档长度规范

## 4. 文档原则

### 4.1 结构原则
- **分层设计**：采用三层结构（主题 → 功能模块 → 详细说明）
- **单一职责**：每个文档专注于一个特定主题
- **逻辑递进**：从宏观到微观，从基础到高级

### 4.2 长度原则
- **主题文档**：50-100行，最大150行
- **功能模块文档**：100-200行，最大250行
- **详细说明文档**：150-250行，最大300行

### 4.3 扩展性原则
- **模块化设计**：支持出版社和期刊的无限扩展
- **引用完整**：文档间建立清晰的引用关系
- **规范化处理**：为每个出版社和期刊创建专门的处理指南

## 5. 项目定位

Paper2Skill 工具套件旨在通过标准化流程，将学术论文转换为结构化的知识体系，支持科研工作者快速提取和应用论文中的关键知识点和技能点。