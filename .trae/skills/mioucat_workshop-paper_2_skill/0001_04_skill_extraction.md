# Skill 提取

## 概述

Skill 提取是 Paper2Skill 工具的核心功能，负责从 LLM 处理后的文档中提取结构化的技能知识，生成规范化的技能文档。本指南将详细介绍 Skill 提取的操作步骤和参数配置。

## 提取原理

Paper2Skill 工具使用专门的提取算法，从处理后的文档中识别和提取技能相关的信息，主要包括以下功能：

- **技能识别**：识别文档中与技能相关的内容
- **信息结构化**：将提取的信息组织成结构化格式
- **关系构建**：构建技能之间的层次和关联关系
- **文档生成**：生成规范化的技能文档

## 技能分类

Paper2Skill 工具提取的技能主要分为以下几类：

| 技能类型 | 描述 | 示例 |
|---------|------|------|
| 技术技能 | 具体的技术能力和方法 | 机器学习、数据分析、编程 |
| 方法技能 | 研究方法和方法论 | 实验设计、统计分析、文献综述 |
| 领域知识 | 特定领域的专业知识 | 人工智能、生物信息学、金融学 |
| 工具技能 | 特定工具和软件的使用 | Python、TensorFlow、Excel |
| 软技能 | 非技术性的能力 | 批判性思维、问题解决、团队协作 |

## 准备工作

### 1. 环境配置

- **依赖项检查**：确保所有必要的依赖项都已安装
- **输入文件准备**：准备好 LLM 处理后的文档
- **输出目录创建**：创建存储提取结果的目录

### 2. 创建目录结构

```powershell
# Windows
New-Item -ItemType Directory -Path "paper_skills" -Force
New-Item -ItemType Directory -Path "paper_skills\by_topic" -Force
New-Item -ItemType Directory -Path "paper_skills\by_method" -Force
New-Item -ItemType Directory -Path "paper_skills\by_journal" -Force

# WSL
mkdir -p paper_skills/by_topic paper_skills/by_method paper_skills/by_journal
```

## 提取操作

### 基本提取命令

```powershell
# Windows - 基本提取
python -m paper2skill.skill_extract --input "llm_processed/sample_paper_processed.md" --output "paper_skills/sample_paper_skill.md"

# WSL - 基本提取
python3 -m paper2skill.skill_extract --input "llm_processed/sample_paper_processed.md" --output "paper_skills/sample_paper_skill.md"
```

### 分类提取

```powershell
# Windows - 按主题分类
python -m paper2skill.skill_extract --input "llm_processed/sample_paper_processed.md" --output "paper_skills/by_topic/machine_learning/sample_paper_skill.md" --category "machine_learning"

# WSL - 按方法分类
python3 -m paper2skill.skill_extract --input "llm_processed/sample_paper_processed.md" --output "paper_skills/by_method/deep_learning/sample_paper_skill.md" --category "deep_learning" --classify-by "method"
```

### 批量提取

```powershell
# Windows
$processedFiles = Get-ChildItem -Path "llm_processed" -Filter "*_processed.md"
foreach ($file in $processedFiles) {
    $outputFile = Join-Path "paper_skills" "$($file.BaseName.Replace('_processed', ''))_skill.md"
    Write-Host "Extracting skills from $($file.Name) to $outputFile"
    python -m paper2skill.skill_extract --input $file.FullName --output $outputFile
}

# WSL
for file in llm_processed/*_processed.md; do
    output="paper_skills/$(basename "$file" _processed.md)_skill.md"
    echo "Extracting skills from $file to $output"
    python3 -m paper2skill.skill_extract --input "$file" --output "$output"
done
```

## 提取参数

### 常用参数

| 参数 | 说明 | 默认值 |
|------|------|--------|
| `--input` | 输入文件路径 | 无（必需） |
| `--output` | 输出文件路径 | 无（必需） |
| `--category` | 技能分类 | 无 |
| `--classify-by` | 分类方式 | `topic` |
| `--min-confidence` | 最小置信度 | 0.7 |

### 高级参数

| 参数 | 说明 | 默认值 |
|------|------|--------|
| `--skill-types` | 技能类型过滤 | 所有类型 |
| `--max-skills` | 最大技能数量 | 50 |
| `--include-context` | 是否包含上下文 | `False` |
| `--verbose` | 是否显示详细信息 | `False` |

## 提取结果检查

### 检查提取质量

1. **打开输出文件**：
   - 打开生成的技能文档
   - 检查提取的技能是否完整
   - 检查技能分类是否准确

2. **常见问题检查**：
   - **技能遗漏**：检查是否有重要技能未提取
   - **分类错误**：检查技能分类是否正确
   - **冗余技能**：检查是否有重复或冗余的技能

### 结果结构

提取生成的技能文档通常包含以下部分：

- **技能概览**：提取的技能总数和分类统计
- **核心技能**：按重要性排序的核心技能列表
- **详细技能**：包含详细描述的技能列表
- **技能关系**：技能之间的层次和关联关系
- **应用场景**：技能的具体应用场景

## 最佳实践

### 1. 提取设置

- **参数调整**：根据文档类型调整提取参数
- **分类策略**：选择合适的分类方式
- **质量控制**：设置适当的置信度阈值

### 2. 结果优化

- **人工审核**：对提取结果进行必要的人工审核
- **技能合并**：合并相似或相关的技能
- **层次调整**：调整技能之间的层次关系

### 3. 文档管理

- **命名规范**：建立统一的文件命名规范
- **分类存储**：按照分类存储技能文档
- **索引创建**：为技能文档创建索引

## 故障排除

### 常见问题

| 问题 | 原因 | 解决方案 |
|------|------|----------|
| 提取结果为空 | 输入文件格式错误 | 检查输入文件格式 |
| 技能提取少 | 置信度阈值过高 | 降低最小置信度参数 |
| 技能重复 | 分类策略不当 | 调整分类参数或手动合并 |
| 处理速度慢 | 文档过大 | 分割文档或增加系统资源 |

### 错误信息处理

| 错误信息 | 含义 | 解决方案 |
|----------|------|----------|
| `Input file not found` | 输入文件不存在 | 检查文件路径 |
| `Output directory not found` | 输出目录不存在 | 创建相应目录 |
| `Invalid skill type` | 技能类型无效 | 检查技能类型参数 |
| `Memory error` | 内存不足 | 减少批量大小或增加内存 |

## 后续步骤

Skill 提取完成后，您可以进行以下操作：

1. **检查提取结果**：确保提取的技能质量满足要求
2. **组织技能文档**：按照分类组织技能文档
3. **创建技能索引**：为提取的技能创建索引
4. **应用技能知识**：将提取的技能知识应用到实际场景

## 示例

### 示例 1: 基本提取

```powershell
# 基本技能提取
python -m paper2skill.skill_extract --input "llm_processed/attention_is_all_you_need_processed.md" --output "paper_skills/attention_is_all_you_need_skill.md"

# 检查结果
Get-Content "paper_skills/attention_is_all_you_need_skill.md" | Select-Object -First 50
```

### 示例 2: 按主题分类提取

```powershell
# 创建主题目录
New-Item -ItemType Directory -Path "paper_skills\by_topic\natural_language_processing" -Force

# 按主题分类提取
python -m paper2skill.skill_extract --input "llm_processed/attention_is_all_you_need_processed.md" --output "paper_skills/by_topic/natural_language_processing/attention_is_all_you_need_skill.md" --category "natural_language_processing"

Write-Host "Skill extraction completed!"
```

### 示例 3: 批量提取并分类

```powershell
# 批量提取多个文档
$processedFiles = Get-ChildItem -Path "llm_processed" -Filter "*_processed.md"
foreach ($file in $processedFiles) {
    # 提取文件名中的主题信息
    $fileName = $file.BaseName
    $topic = $fileName -split "_" | Select-Object -First 1
    
    # 创建主题目录
    $topicDir = Join-Path "paper_skills\by_topic" $topic
    New-Item -ItemType Directory -Path $topicDir -Force
    
    # 提取技能
    $outputFile = Join-Path $topicDir "$($file.BaseName.Replace('_processed', ''))_skill.md"
    Write-Host "Extracting skills from $($file.Name) to $outputFile"
    python -m paper2skill.skill_extract --input $file.FullName --output $outputFile --category $topic
}

Write-Host "Batch skill extraction completed!"
```