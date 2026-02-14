# 工具使用指南

## 1. 概述

本指南提供了使用 Paper2Skill 工具的完整流程，包括从环境设置到 Skill 提取的所有步骤。所有操作均通过命令行执行，确保每条命令都能独立运行并获得较高的成功率。

## 2. 目录结构

### 2.1 核心目录

```
├── pdf/                # 原始 PDF 文档
│   └── input/          # 输入 PDF 目录
├── models/             # Marker 工具模型文件
├── llm_processed/      # LLM 处理后的文档
├── paper_skills/       # 提取的 skill 文档
├── source/             # 工具源代码
├── scripts/            # 处理脚本
└── venv/               # 虚拟环境
```

### 2.2 目录用途

- **pdf/input/**：存放原始 PDF 文件
- **models/**：存放 Marker 工具的模型文件
- **llm_processed/**：存放 LLM 处理后的文档
- **paper_skills/**：存放提取的 skill 文档
- **source/**：存放从论文中提取的工具源代码
- **scripts/**：存放处理脚本

## 3. 工作流程

Paper2Skill 工具的使用流程分为以下几个主要步骤：

### 3.1 环境设置
- 创建并激活虚拟环境
- 安装项目依赖
- 验证环境配置

### 3.2 PDF 转换
- 将 PDF 文件放入 `pdf/input` 目录
- 运行 `process_pdf.py` 脚本转换为 Markdown
- 提取并保存文档中的图片资源

### 3.3 LLM 处理
- 使用 LLM 对转换后的 Markdown 文档进行规范化处理
- 按出版社和期刊分类存储到 `llm_processed` 目录

### 3.4 Skill 提取
- 从处理后的 Markdown 文档中提取关键知识点和技能点
- 按照主题、方法、期刊等分类方式组织
- 将提取的 skill 存储到 `paper_skills` 目录

## 4. 核心脚本工具

### 4.1 process_pdf.py

**作用**：处理 PDF 文档，提取文字内容和图片，生成对应的 Markdown 文档和图片文件夹。

**特点**：
- 自动遍历 `pdf/input` 目录下的所有子目录
- 对每个 PDF 文件进行处理，生成结构化的 Markdown 文档
- 提取并保存 PDF 中的图片到对应的图片文件夹
- 优先使用 GPU 进行加速（如果可用）
- 使用 GPU 处理速度远快于 CPU

### 4.2 analyze_pdf_images.py

**作用**：分析 PDF 文档中的图片信息，用于调试和问题排查。

**特点**：
- 遍历 `pdf/input` 目录下的所有 PDF 文件
- 详细分析每个 PDF 文件中的图片数量、格式、尺寸和类型
- 帮助识别图片处理问题，便于调整 `process_pdf.py` 中的参数

### 4.3 check_gpu_pytorch.py

**作用**：检查设备是否有 GPU 可用，验证 PyTorch 配置。

**特点**：
- 检查 PyTorch 版本和 CUDA 可用性
- 验证 GPU 设备信息
- 测试 GPU 功能是否正常
- 确保 `process_pdf.py` 能够正确使用 GPU 加速

## 5. 详细指南

### 5.1 环境设置

详细的环境设置指南，请参考：
- `0001_01_environment_setup.md` - 环境设置

### 5.2 PDF 转换

详细的 PDF 转换指南，请参考：
- `0001_02_pdf_conversion.md` - PDF 转换

### 5.3 LLM 处理

详细的 LLM 处理指南，请参考：
- `0001_03_llm_processing.md` - LLM 处理

### 5.4 Skill 提取

详细的 Skill 提取指南，请参考：
- `0001_04_skill_extraction.md` - Skill 提取

## 6. 性能说明

- **GPU 加速**：如果设备有可用的 NVIDIA GPU，`process_pdf.py` 会自动使用 GPU 进行加速，处理速度远快于 CPU
- **内存使用**：处理大型 PDF 文件时，建议使用 16GB 或更多 RAM 以避免内存不足问题
- **存储空间**：模型文件和处理结果可能占用较多存储空间，请确保有足够的可用空间

## 7. 技术栈

- **PDF 处理**：使用 Marker 工具进行 PDF 到 Markdown 的转换
- **依赖管理**：Python 包安装（pip）
- **GPU 加速**：PyTorch 与 CUDA

### 7.1 关于 Marker 工具

本项目使用 [Marker](https://github.com/VikParuchuri/marker) 工具进行 PDF 到 Markdown 的转换，这是一个功能强大的开源工具，能够高效地提取 PDF 文档中的文字和图片。