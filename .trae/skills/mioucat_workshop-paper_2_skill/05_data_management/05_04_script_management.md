# 脚本管理

## 概述

本指南介绍 Paper2Skill 工具中实际存在的脚本及其使用方法。脚本是项目中重要的辅助工具，用于自动化处理任务，提高工作效率。

## 脚本存储位置与路径约定

所有脚本均存储在项目根目录的 `scripts/` 文件夹中。

**路径约定（重要）**：所有脚本一律以"脚本自身的相对位置"定位项目根（脚本位于 `scripts/`，其父目录即项目根），不使用当前工作目录（cwd）。因此**从任意工作目录运行脚本均可正常工作**，只要脚本固定在 `scripts/` 目录内。

## 实际脚本列表

项目中目前包含以下六个脚本：

1. **setup_venv.ps1** - 一键重建虚拟环境（含镜像源连通性与带宽检测）
2. **manage_models.py** - 模型目录与版本管理
3. **process_pdf.py** - 核心PDF处理脚本
4. **analyze_pdf_images.py** - PDF图像分析脚本
5. **check_gpu_pytorch.py** - GPU和PyTorch检查脚本
6. **check_image_sizes.py** - 图像尺寸检查脚本

## 脚本详细说明

### 0. setup_venv.ps1

**功能**：一条命令重建整个虚拟环境，内置镜像源连通性与带宽检测，自动选择最快下载源。

**主要特性**：
- 检测 Python 3.10 并创建 venv
- 对 PyPI（11 个源）/ PyTorch（4 个源）/ HuggingFace / GitHub 各镜像做 HEAD 延迟 + 实测带宽检测，带宽优先选择
- 从最快源安装 torch（CUDA 12.6）与全部锁定依赖（requirements_frozen.txt）
- 自动下载部署 llama.cpp CUDA 12.4 双包
- 调用 manage_models.py 补齐模型并验证 GPU

**使用方法**：
```powershell
.\scripts\setup_venv.ps1 -CheckMirrorsOnly   # 仅检测镜像源
.\scripts\setup_venv.ps1                     # 一键重建
```

### 0.5 manage_models.py

**功能**：独立的模型目录与版本管理脚本（详见 [环境设置](../01_core_process/01_02_environment_setup.md) 模型管理章节）。

**主要特性**：
- 统一配置模型路径（MODEL_CACHE_DIR / HF_HOME / SURYA_GGUF_LOCAL_*）
- 检查本地模型状态（就绪/缺失），对比远程最新版本
- 下载缺失模型、更新到最新、清理旧版遗留
- 被 process_pdf.py 启动时自动调用

**使用方法**：
```powershell
venv\Scripts\python scripts\manage_models.py --check    # 仅检查报告
venv\Scripts\python scripts\manage_models.py --update   # 对照远程更新
venv\Scripts\python scripts\manage_models.py --prune    # 清理旧版遗留
```

### 1. process_pdf.py

**功能**：使用Marker PDF工具处理PDF文档，将其转换为Markdown格式并提取图片。

**主要特性**：
- 自动检测项目结构，定位input和output目录
- 支持批量处理多个PDF文件
- 智能检查处理状态，避免重复处理
- 自动下载和管理Marker所需的模型文件
- 支持CPU核心限制，优化处理性能

**使用方法**：
```bash
python scripts/process_pdf.py
```

**工作流程**：
1. 检查模型可用性，自动下载所需模型
2. 扫描pdf/input目录中的所有PDF文件
3. 为每个PDF文件创建对应的输出目录
4. 转换PDF为Markdown格式
5. 提取并保存PDF中的图片
6. 生成处理报告

### 2. analyze_pdf_images.py

**功能**：分析PDF文件中的图像，识别图像类型和属性。

**主要特性**：
- 分析PDF中的图像格式、尺寸和大小
- 区分矢量图像和光栅图像
- 批量处理多个PDF文件
- 生成详细的图像分析报告

**使用方法**：
```bash
python scripts/analyze_pdf_images.py
```

**分析内容**：
- 图像格式（JPEG、PNG等）
- 图像尺寸（宽度×高度）
- 图像大小（KB）
- 图像类型（矢量或光栅）

### 3. check_gpu_pytorch.py

**功能**：检查GPU可用性和PyTorch配置，确保系统准备好进行GPU加速处理。

**主要特性**：
- 检查PyTorch版本
- 检查CUDA可用性和版本
- 检查GPU设备信息
- 测试基本PyTorch功能
- 提供使用建议

**使用方法**：
```bash
python scripts/check_gpu_pytorch.py
```

**输出信息**：
- PyTorch版本
- CUDA可用性
- CUDA版本
- GPU设备数量和名称
- 功能测试结果
- 性能建议

### 4. check_image_sizes.py

**功能**：检查指定目录中图像文件的尺寸，特别关注PDF转换过程中生成的页面图像。

**主要特性**：
- 分析图像宽度、高度和 aspect ratio
- 对aspect ratio进行分类（非常宽、宽、适中、方形）
- 仅处理特定命名模式的图像文件（_page_*.jpeg）

**使用方法**：
```bash
python scripts/check_image_sizes.py <image_directory>
```

**示例**：
```bash
python scripts/check_image_sizes.py "pdf/output/example_paper/example_paper_images"
```

## 脚本执行环境

所有脚本应在项目的虚拟环境中运行：

**虚拟环境位置**：`./venv`

**激活虚拟环境（Windows）**：
```bash
venv\Scripts\activate
```

## 依赖项

脚本依赖以下主要包：

- **process_pdf.py**：marker-pdf, pytorch, numpy, pandas, fitz (PyMuPDF), pillow, base64
- **analyze_pdf_images.py**：PyMuPDF (fitz)
- **check_gpu_pytorch.py**：pytorch
- **check_image_sizes.py**：Pillow (PIL)

## 最佳实践

1. **顺序执行**：建议按照以下顺序执行脚本：
   - `setup_venv.ps1`（一键重建环境）
   - `manage_models.py`（检查/补齐模型）
   - `check_gpu_pytorch.py`（检查环境）
   - `process_pdf.py`（处理PDF）
   - `analyze_pdf_images.py`（分析图像）
   - `check_image_sizes.py`（检查图像尺寸）

2. **环境准备**：确保虚拟环境已激活，所有依赖项已安装

3. **输入准备**：将PDF文件放入 `pdf/input` 目录

4. **结果检查**：处理完成后，检查 `pdf/output` 目录中的结果

## 故障排除

| 问题 | 可能原因 | 解决方案 |
|------|---------|----------|
| 模型下载失败 | 网络连接问题 | 检查网络连接，重试脚本 |
| PDF处理失败 | PDF文件损坏 | 检查PDF文件完整性 |
| GPU不可用 | CUDA未安装 | 安装CUDA或使用CPU模式 |
| 依赖项缺失 | 虚拟环境未正确设置 | 重新创建虚拟环境并安装依赖 |

通过这些脚本的协同工作，可以高效地处理PDF文档，为技能提取和分析提供结构化的输入数据。