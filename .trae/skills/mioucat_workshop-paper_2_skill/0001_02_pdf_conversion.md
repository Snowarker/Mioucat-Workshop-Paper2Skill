# PDF 转换

## 1. 准备工作

### 1.1 激活虚拟环境

确保在执行任何操作前，虚拟环境已激活：

```powershell
# 激活虚拟环境
venv\Scripts\activate
```

### 1.2 准备 PDF 文件

将原始 PDF 文件放入 `pdf/input` 目录：

```powershell
# 创建输入目录（如果不存在）
New-Item -ItemType Directory -Path "pdf\input" -Force

# 查看输入目录内容
Get-ChildItem -Path "pdf\input"
```

## 2. 运行 PDF 转换

### 2.1 执行转换脚本

```powershell
# 运行 PDF 转换脚本
python scripts/process_pdf.py
```

### 2.2 脚本功能

- 自动遍历 `pdf/input` 目录下的所有子目录
- 对每个 PDF 文件进行处理，生成结构化的 Markdown 文档
- 提取并保存 PDF 中的图片到对应的图片文件夹
- 优先使用 GPU 进行加速（如果可用）
- 使用 GPU 处理速度远快于 CPU

## 3. 转换结果

### 3.1 查看转换结果

```powershell
# 查看转换结果目录
Get-ChildItem -Path "pdf\output" -Recurse
```

### 3.2 结果结构

转换后的文件结构示例：

```
pdf/output/
└── [论文名称]/
    ├── [论文名称].md     # Markdown 文档
    └── images/           # 提取的图片
        ├── image_1.png
        ├── image_2.png
        └── ...
```

## 4. 图片分析（可选）

### 4.1 分析 PDF 图片

如果需要分析 PDF 中的图片信息，可以使用以下命令：

```powershell
# 分析 PDF 图片
python scripts/analyze_pdf_images.py
```

### 4.2 分析结果

该命令会输出每个 PDF 文件中的图片数量、格式、尺寸和类型等信息，有助于识别图片处理问题。

## 5. 常见问题

### 5.1 转换失败

**问题**：PDF 转换失败

**解决方案**：
```powershell
# 检查 PDF 文件是否损坏
# 尝试使用其他 PDF 阅读器打开

# 检查内存使用情况
# 处理大型 PDF 文件时，确保有足够的内存

# 查看错误信息
# 检查脚本输出的错误信息
```

### 5.2 图片提取失败

**问题**：图片无法正确提取

**解决方案**：
```powershell
# 检查 PDF 文件中的图片格式
# 尝试使用 analyze_pdf_images.py 分析图片

# 检查存储空间
# 确保有足够的存储空间用于保存图片
```

### 5.3 GPU 加速未启用

**问题**：脚本未使用 GPU 加速

**解决方案**：
```powershell
# 检查 GPU 可用性
python scripts/check_gpu_pytorch.py

# 确保安装了正确版本的 CUDA
# 检查 PyTorch 配置
```

## 6. 性能优化

### 6.1 使用 GPU 加速

确保 GPU 可用并正确配置，这将显著提高转换速度。

### 6.2 批量处理

对于多个 PDF 文件，可以一次性放入 `pdf/input` 目录，脚本会自动批量处理。

### 6.3 分割大型 PDF

对于非常大的 PDF 文件，可以考虑分割后处理，以减少内存使用。

## 7. 后续步骤

PDF 转换完成后，可以继续执行以下步骤：

1. **LLM 处理**：查看 `0001_03_llm_processing.md` 了解如何使用 LLM 处理转换后的 Markdown 文档
2. **Skill 提取**：查看 `0001_04_skill_extraction.md` 了解如何从处理后的文档中提取 skill 信息