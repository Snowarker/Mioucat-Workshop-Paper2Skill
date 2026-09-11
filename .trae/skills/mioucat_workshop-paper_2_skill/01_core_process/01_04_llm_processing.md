# LLM 处理

## 概述

LLM 处理是 Paper2Skill 工具的核心步骤，负责使用大语言模型分析和处理转换后的文档内容，为后续的 Skill 提取做准备。本指南将详细介绍 LLM 处理的操作步骤和参数配置。

## 处理原理

Paper2Skill 工具使用先进的大语言模型（LLM）对转换后的文档进行深度分析，主要包括以下功能：

- **内容理解**：理解文档的整体结构和核心内容
- **信息提取**：提取文档中的关键概念、方法和结论
- **关系分析**：分析文档中各个部分之间的逻辑关系
- **知识结构化**：将非结构化文本转换为结构化知识

## 支持的模型

Paper2Skill 工具支持多种大语言模型，包括但不限于：

| 模型类型 | 适用场景 | 特点 |
|---------|---------|------|
| GPT-4 | 复杂文档分析 | 高精度，理解能力强 |
| GPT-3.5 | 一般文档处理 | 速度快，成本低 |
| Claude | 长文档处理 | 上下文窗口大 |
| Llama 3 | 本地部署 | 隐私性好，无 API 限制 |

## 准备工作

### 1. 环境配置

- **API 密钥设置**：如果使用云端模型，需要设置 API 密钥
- **模型下载**：如果使用本地模型，需要下载相应模型
- **输入文件准备**：准备好转换后的 Markdown 文件

### 2. API 密钥配置

```powershell
# Windows - 设置 OpenAI API 密钥
$env:OPENAI_API_KEY = "your-api-key-here"

# WSL - 设置 OpenAI API 密钥
export OPENAI_API_KEY="your-api-key-here"
```

### 3. 创建目录结构

```powershell
# Windows
New-Item -ItemType Directory -Path "llm_processed" -Force

# WSL
mkdir -p llm_processed
```

## 处理操作

### 基本处理命令

```powershell
# Windows - 使用 OpenAI GPT-4
python -m paper2skill.llm_process --model "gpt-4" --input "converted_text/sample_paper.md" --output "llm_processed/sample_paper_processed.md"

# WSL - 使用 OpenAI GPT-3.5
python3 -m paper2skill.llm_process --model "gpt-3.5-turbo" --input "converted_text/sample_paper.md" --output "llm_processed/sample_paper_processed.md"
```

### 本地模型处理

```powershell
# Windows - 使用本地 Llama 3 模型
python -m paper2skill.llm_process --model "llama3" --model-path "./local_models/llama3" --input "converted_text/sample_paper.md" --output "llm_processed/sample_paper_processed.md"

# WSL - 使用本地 Llama 3 模型
python3 -m paper2skill.llm_process --model "llama3" --model-path "./local_models/llama3" --input "converted_text/sample_paper.md" --output "llm_processed/sample_paper_processed.md"
```

### 批量处理

```powershell
# Windows
$mdFiles = Get-ChildItem -Path "converted_text" -Filter "*.md"
foreach ($md in $mdFiles) {
    $outputFile = Join-Path "llm_processed" "$($md.BaseName)_processed.md"
    Write-Host "Processing $($md.Name) to $outputFile"
    python -m paper2skill.llm_process --model "gpt-3.5-turbo" --input $md.FullName --output $outputFile
}

# WSL
for md in converted_text/*.md; do
    output="llm_processed/$(basename "$md" .md)_processed.md"
    echo "Processing $md to $output"
    python3 -m paper2skill.llm_process --model "gpt-3.5-turbo" --input "$md" --output "$output"
done
```

## 处理参数

### 常用参数

| 参数 | 说明 | 默认值 |
|------|------|--------|
| `--model` | 模型名称 | `gpt-3.5-turbo` |
| `--model-path` | 本地模型路径 | 无 |
| `--input` | 输入文件路径 | 无（必需） |
| `--output` | 输出文件路径 | 无（必需） |
| `--temperature` | 生成温度 | 0.3 |
| `--max-tokens` | 最大令牌数 | 4096 |

### 高级参数

| 参数 | 说明 | 默认值 |
|------|------|--------|
| `--system-prompt` | 系统提示模板 | 内置模板 |
| `--few-shot` | 是否使用少样本学习 | `False` |
| `--batch-size` | 批处理大小 | 1 |
| `--verbose` | 是否显示详细信息 | `False` |

## 处理结果检查

### 检查处理质量

1. **打开输出文件**：
   - 打开生成的处理后文件
   - 检查内容是否完整
   - 检查结构是否清晰

2. **常见问题检查**：
   - **内容丢失**：检查是否有部分内容未处理
   - **理解错误**：检查模型是否正确理解了文档内容
   - **结构混乱**：检查生成的结构是否合理

### 结果分析

处理后的文件通常包含以下部分：

- **文档摘要**：对文档的整体概括
- **核心概念**：提取的关键概念和术语
- **方法分析**：对文档中方法的详细分析
- **结果解读**：对文档结果的解读
- **结论提炼**：提炼的核心结论

## 最佳实践

### 1. 模型选择

- **复杂文档**：选择 GPT-4 或 Claude 等高级模型
- **一般文档**：选择 GPT-3.5 或 Llama 3 等模型
- **长文档**：选择 Claude 或支持长上下文的模型

### 2. 参数调优

- **温度设置**：对于需要准确性的任务，使用较低的温度（0.1-0.3）
- **令牌限制**：对于长文档，设置较大的令牌限制
- **批处理**：对于多个文档，使用批量处理提高效率

### 3. 结果优化

- **多次处理**：对于重要文档，可以尝试不同模型和参数
- **人工审核**：对处理结果进行必要的人工审核和调整
- **反馈循环**：根据处理结果调整模型和参数

## 故障排除

### 常见问题

| 问题 | 原因 | 解决方案 |
|------|------|----------|
| API 调用失败 | API 密钥错误或配额不足 | 检查 API 密钥和配额 |
| 处理超时 | 文档过大或网络问题 | 分割文档或检查网络 |
| 内存不足 | 本地模型过大 | 选择较小的模型或增加内存 |
| 结果质量差 | 模型选择不当 | 尝试不同的模型和参数 |

### 错误信息处理

| 错误信息 | 含义 | 解决方案 |
|----------|------|----------|
| `API key not found` | API 密钥未设置 | 设置相应的环境变量 |
| `Context length exceeded` | 上下文长度超出限制 | 分割文档或选择支持长上下文的模型 |
| `Model not available` | 模型不可用 | 检查模型名称或下载状态 |
| `Rate limit exceeded` | API 速率限制 | 减少请求频率或升级 API 计划 |

## 性能优化

### 1. 处理速度优化

- **模型选择**：选择速度较快的模型
- **批处理**：使用批量处理减少 API 调用次数
- **并行处理**：对于多个文档，使用并行处理

### 2. 成本优化

- **模型选择**：对于非关键任务，使用成本较低的模型
- **令牌管理**：优化提示词，减少不必要的令牌使用
- **缓存机制**：对相同内容使用缓存，避免重复处理

## 后续步骤

LLM 处理完成后，您可以进行以下操作：

1. **检查处理结果**：确保处理质量满足要求
2. **进行 Skill 提取**：从处理后的文档中提取结构化的技能信息
3. **生成最终文档**：基于提取的技能信息生成最终文档

## 示例

### 示例 1: 使用 GPT-4 处理

```powershell
# 设置 API 密钥
$env:OPENAI_API_KEY = "your-api-key-here"

# 使用 GPT-4 处理文档
python -m paper2skill.llm_process --model "gpt-4" --input "converted_text/attention_is_all_you_need.md" --output "llm_processed/attention_is_all_you_need_processed.md"

# 检查结果
Get-Content "llm_processed/attention_is_all_you_need_processed.md" | Select-Object -First 30
```

### 示例 2: 批量处理期刊论文

```powershell
# 批量处理多个文档
$mdFiles = Get-ChildItem -Path "converted_text/icml2023" -Filter "*.md"
foreach ($md in $mdFiles) {
    $outputDir = Join-Path "llm_processed" "icml2023"
    New-Item -ItemType Directory -Path $outputDir -Force
    $outputFile = Join-Path $outputDir "$($md.BaseName)_processed.md"
    Write-Host "Processing $($md.Name)"
    python -m paper2skill.llm_process --model "gpt-3.5-turbo" --input $md.FullName --output $outputFile
}

Write-Host "Batch processing completed!"
```