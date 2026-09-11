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

- **Marker 模型已下载**：`process_pdf.py` 启动时会自动调用 `scripts/manage_models.py` 检查并补齐缺失的必需模型（详见 [环境设置](01_02_environment_setup.md) 的模型管理章节）；也可手动运行 `python scripts/manage_models.py --check` 查看模型状态
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

### 基本转换命令（marker-pdf 2.x）

> 注意：marker-pdf 2.x 已不再支持 1.x 的 `python -m marker.convert` 命令。日常使用请直接运行 `python scripts/process_pdf.py`（见下节）。如需 CLI 方式：

```powershell
# 转换整个目录下的 PDF（输出到 converted_text/）
marker input_pdfs --output_dir converted_text

# GPU 上默认使用 balanced 模式（VLM 版面模型 + 全页 OCR）；CPU 可用 fast 模式
marker input_pdfs --output_dir converted_text --mode balanced
```

### 批量转换

```powershell
# 推荐：直接使用项目脚本，自动处理 pdf/input/ 下所有 PDF 并跳过已处理文件
python scripts/process_pdf.py

# 或使用 2.x CLI 批量处理（输入为文件夹）
marker input_pdfs --output_dir converted_text --workers 4
```

## 使用项目脚本进行转换

### process_pdf.py 脚本

**功能**：自动处理 `pdf/input/` 目录下的所有 PDF 文件，生成 Markdown 文档和图片文件夹。

**特点**：
- 自动检测输入和输出目录
- 跳过已经处理过的文件
- 仅对部分处理的文件进行必要的处理（如仅提取图片）
- 支持嵌套目录结构

**使用方法**：

1. **激活虚拟环境**：
   ```powershell
   # Windows
   venv\Scripts\activate
   ```

2. **运行脚本**：
   ```powershell
   python scripts/process_pdf.py
   ```

**输出结构**：
- 输出目录：`pdf/output/`
- 每个 PDF 文件会在输出目录中创建对应的子目录
- 生成的文件：
  - `{filename}.md`：转换后的 Markdown 文档
  - `{filename}_images/`：提取的图片文件夹

### analyze_pdf_images.py 脚本

**功能**：分析 PDF 文件中的图片类型和属性，包括格式、尺寸、大小等。

**使用方法**：

1. **激活虚拟环境**：
   ```powershell
   # Windows
   venv\Scripts\activate
   ```

2. **运行脚本**：
   ```powershell
   python scripts/analyze_pdf_images.py
   ```

**分析内容**：
- PDF 页数
- 每页的图片数量
- 图片格式（JPEG、PNG等）
- 图片尺寸
- 图片大小
- 图片类型（矢量图或光栅图）

## 转换参数

### 常用参数（marker-pdf 2.x）

| 参数 | 说明 | 默认值 |
|------|------|--------|
| `--mode` | 转换模式：`balanced`（VLM 版面模型+全页 OCR，GPU）或 `fast`（轻量 CPU 检测器） | 按设备自动 |
| `--output_dir` | 输出目录 | 当前目录 |
| `--workers` | 并行 worker 数 | 自动 |
| `--max_files` | 最大转换文件数 | 无限制 |
| `--page_range` | 指定页范围，如 `0,5-10,20` | 全部 |
| `--output_format` | 输出格式：`markdown` / `json` / `html` / `chunks` | `markdown` |

> **模式与后端选择**：`balanced` 与 `fast` 的适用场景、模型依赖（`gguf_vlm` / `fast_layout` / `vlm_torch`）及推理后端选择详见 [环境设置](01_02_environment_setup.md) 的"模型清单与用途说明"章节。

### 高级参数

| 参数 | 说明 | 默认值 |
|------|------|--------|
| `--disable_ocr` | 禁用 OCR 处理 | `False` |
| `--disable_image_extraction` | 禁用图片提取 | `False` |
| `--llm_service` | 使用的 LLM 服务（阅读顺序/版面后处理） | 默认服务 |
| `--config_json` | 附加配置文件路径 | 无 |

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
   # 强制 OCR（扫描版 PDF）
   marker input_pdfs --output_dir converted_text --mode balanced
   # 或使用脚本配置（修改 scripts/process_pdf.py 中的参数）
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
# 将单篇 PDF 放入 input_pdfs/ 目录后转换
marker input_pdfs --output_dir converted_text

# 检查结果
Get-Content "converted_text/attention_is_all_you_need.md" | Select-Object -First 20
```

### 示例 2: 批量转换期刊论文

```powershell
# 推荐：使用项目脚本自动处理 pdf/input/ 目录（支持嵌套结构）
python scripts/process_pdf.py

# 或使用 2.x CLI 批量转换（输入为文件夹）
marker input_pdfs --output_dir converted_text --workers 4
Write-Host "Batch conversion completed!"
```