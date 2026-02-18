# PDF 转换

## 概述

PDF 转换是 Paper2Skill 工具的第一步操作，负责将 PDF 格式的论文和专利转换为可编辑的文本格式，为后续的 LLM 处理和 Skill 提取做准备。本指南将详细介绍 PDF 转换的操作步骤和注意事项。

## 转换原理

Paper2Skill 工具使用 Marker 库进行 PDF 转换，Marker 是一个专门用于学术论文 PDF 转换的先进工具，具有以下特点：

- **高精度转换**：能够准确识别论文的标题、摘要、章节等结构
- **公式处理**：支持数学公式的识别和转换
- **表格识别**：能够识别和转换论文中的表格
- **参考文献处理**：专门处理论文的参考文献部分

## 准备工作

### 1. 确保环境已配置

- **Marker 模型已下载**：确保 Marker 模型已正确下载到 `models` 目录
- **依赖项已安装**：确保所有必要的依赖项都已安装
- **输入文件准备**：准备好需要转换的 PDF 文件

### 2. 创建输入输出目录

```powershell
# Windows
New-Item -ItemType Directory -Path "input_pdfs" -Force
New-Item -ItemType Directory -Path "converted_text" -Force

# WSL
touch -p input_pdfs converted_text
```

## 转换操作

### 基本转换命令

```powershell
# Windows
python -m marker.convert --model-path "./models" --input "input_pdfs/sample_paper.pdf" --output "converted_text/sample_paper.md"

# WSL
python3 -m marker.convert --model-path "./models" --input "input_pdfs/sample_paper.pdf" --output "converted_text/sample_paper.md"
```

### 批量转换

```powershell
# Windows
$pdfFiles = Get-ChildItem -Path "input_pdfs" -Filter "*.pdf"
foreach ($pdf in $pdfFiles) {
    $outputFile = Join-Path "converted_text" "$($pdf.BaseName).md"
    Write-Host "Converting $($pdf.Name) to $outputFile"
    python -m marker.convert --model-path "./models" --input $pdf.FullName --output $outputFile
}

# WSL
for pdf in input_pdfs/*.pdf; do
    output="converted_text/$(basename "$pdf" .pdf).md"
    echo "Converting $pdf to $output"
    python3 -m marker.convert --model-path "./models" --input "$pdf" --output "$output"
done
```

## 转换参数

### 常用参数

| 参数 | 说明 | 默认值 |
|------|------|--------|
| `--model-path` | Marker 模型路径 | `./models` |
| `--input` | 输入 PDF 文件路径 | 无（必需） |
| `--output` | 输出 Markdown 文件路径 | 无（必需） |
| `--batch-size` | 批处理大小 | 4 |
| `--max-pages` | 最大处理页数 | 无限制 |
| `--lang` | 文档语言 | `en` |

### 高级参数

| 参数 | 说明 | 默认值 |
|------|------|--------|
| `--ocr` | 是否使用 OCR | `False` |
| `--skip-layout` | 是否跳过布局分析 | `False` |
| `--parallel` | 是否并行处理 | `True` |
| `--verbose` | 是否显示详细信息 | `False` |

## 转换结果检查

### 检查转换质量

1. **打开输出文件**：
   - 打开生成的 Markdown 文件
   - 检查文本是否完整
   - 检查格式是否正确

2. **常见问题检查**：
   - **文本乱码**：检查 PDF 是否加密或扫描版
   - **格式错误**：检查章节结构是否正确
   - **内容缺失**：检查是否有页面未转换

### 手动调整

如果转换结果不理想，可以进行以下调整：

1. **调整参数**：
   ```powershell
   # 尝试使用 OCR
   python -m marker.convert --model-path "./models" --input "input_pdfs/sample_paper.pdf" --output "converted_text/sample_paper.md" --ocr
   ```

2. **分段转换**：
   - 将大型 PDF 分割为多个小文件
   - 分别转换后合并结果

3. **手动编辑**：
   - 直接编辑生成的 Markdown 文件
   - 修复格式和内容问题

## 最佳实践

### 1. 文件准备

- **选择高质量 PDF**：优先使用出版商提供的原始 PDF
- **避免扫描版 PDF**：扫描版 PDF 转换质量较差
- **检查文件大小**：过大的 PDF 可能需要分段处理

### 2. 转换设置

- **模型选择**：根据文档类型选择合适的模型
- **参数调整**：根据 PDF 质量调整转换参数
- **批量处理**：对于多个文件，使用批量转换脚本

### 3. 结果处理

- **及时检查**：转换完成后立即检查结果
- **建立规范**：建立统一的文件命名和存储规范
- **备份原始**：保留原始 PDF 文件作为备份

## 故障排除

### 常见问题

| 问题 | 原因 | 解决方案 |
|------|------|----------|
| 转换失败 | PDF 加密 | 尝试解密 PDF 或使用其他工具转换 |
| 内存不足 | PDF 过大 | 分段转换或增加系统内存 |
| 模型未找到 | 模型路径错误 | 检查 `MARKER_MODEL_DIR` 环境变量 |
| 依赖缺失 | 缺少必要库 | 重新安装依赖项 |

### 错误信息处理

| 错误信息 | 含义 | 解决方案 |
|----------|------|----------|
| `Model not found` | 模型文件未找到 | 检查模型路径，重新下载模型 |
| `PDF encrypted` | PDF 已加密 | 解密 PDF 后再转换 |
| `Memory error` | 内存不足 | 减小批量大小或分段转换 |
| `Permission denied` | 权限不足 | 检查文件和目录权限 |

## 后续步骤

PDF 转换完成后，您可以进行以下操作：

1. **检查转换结果**：确保文本质量满足要求
2. **进行 LLM 处理**：使用大语言模型分析转换后的文本
3. **提取 Skill 信息**：从处理后的文本中提取结构化的技能信息

## 示例

### 示例 1: 转换单篇论文

```powershell
# 转换单篇论文
python -m marker.convert --model-path "./models" --input "input_pdfs/attention_is_all_you_need.pdf" --output "converted_text/attention_is_all_you_need.md"

# 检查结果
Get-Content "converted_text/attention_is_all_you_need.md" | Select-Object -First 20
```

### 示例 2: 批量转换期刊论文

```powershell
# 创建期刊目录
New-Item -ItemType Directory -Path "input_pdfs/icml2023" -Force
New-Item -ItemType Directory -Path "converted_text/icml2023" -Force

# 批量转换
$pdfFiles = Get-ChildItem -Path "input_pdfs/icml2023" -Filter "*.pdf"
foreach ($pdf in $pdfFiles) {
    $outputFile = Join-Path "converted_text/icml2023" "$($pdf.BaseName).md"
    Write-Host "Converting $($pdf.Name)"
    python -m marker.convert --model-path "./models" --input $pdf.FullName --output $outputFile
}

Write-Host "Batch conversion completed!"
```