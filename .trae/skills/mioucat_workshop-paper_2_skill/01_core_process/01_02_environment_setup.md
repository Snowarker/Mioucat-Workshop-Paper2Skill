# 环境设置

## 系统要求

在开始使用 Paper2Skill 工具之前，请确保您的系统满足以下要求：

### 硬件要求
- **内存**：至少 8GB RAM（推荐 16GB 或更高）
- **存储空间**：至少 50GB 可用空间
- **处理器**：4 核或更多核心的 CPU
- **网络连接**：稳定的互联网连接（用于模型下载和更新）

### 软件要求
- **操作系统**：Windows 10/11 (64位)
- **Python**：Python 3.10.x（推荐版本，如 3.10.11）
- **Git**：最新版本的 Git
- **PDF 处理库**：Poppler 或 Ghostscript

## Windows 环境设置

### 步骤 1: 安装 Python

1. **下载 Python**：
   - 访问 [Python Windows 版本下载页面](https://www.python.org/downloads/windows/)
   - 下载 Python 3.10.x 版本（推荐版本，如 3.10.11）
   - 确保勾选 "Add Python to PATH"

2. **验证安装**：
   ```powershell
   python --version
   pip --version
   ```

### 步骤 2: 安装 Git

1. **下载 Git**：
   - 访问 [Git 官方网站](https://git-scm.com/downloads)
   - 下载并安装适合 Windows 的版本

2. **验证安装**：
   ```powershell
   git --version
   ```

### 步骤 2.5: 一键重建虚拟环境（推荐）

`scripts/setup_venv.ps1` 一条命令完成整个环境构建，**内置镜像源连通性与带宽检测**：对每个资产类别（PyPI 包 / PyTorch 索引 / HuggingFace / GitHub）逐一检测候选源，综合 **HEAD 延迟 + 实测下载带宽**（下载索引小文件测 KB/s）选出最快的下载路径；不可达的源如实显示并自动剔除。

**路径约定**：所有脚本固定放在 `scripts/` 目录，一律以"脚本自身的相对位置"定位项目根（脚本目录的父目录），因此**从任意工作目录运行均可正常工作**。所有文件（venv、requirements_frozen.txt、models、tools）均相对项目根定位。

检测的镜像源清单（含已知可能不可达的源，检测结果如实显示）：
- **PyPI**：官方 / 清华 TUNA / 阿里云 / 中科大 / 腾讯云 / 华为云 / 豆瓣 / 北外 BFSU / 南大 NJU / 浙大 ZJU / 哈工大 HIT
- **PyTorch (cu126)**：官方 / 上海交大 SJTU / 阿里云 / 清华 TUNA
- **HuggingFace**：官方 / hf-mirror
- **GitHub (llama.cpp)**：官方 / gh-proxy / ghfast.top / ghproxy.net / mirror.ghproxy

```powershell
# 只检测各镜像源连通性、带宽并输出（不构建）
.\scripts\setup_venv.ps1 -CheckMirrorsOnly

# 一键重建：创建 venv → 安装 torch(CUDA12.6) + 全部锁定依赖(requirements_frozen.txt)
#           → 下载 llama.cpp CUDA 双包 → 补齐模型 → 验证 GPU
.\scripts\setup_venv.ps1

# 指定 Python 3.10 解释器 / 跳过模型检查 / 强制重下 llama.cpp
.\scripts\setup_venv.ps1 -Python "D:\...\Python310\python.exe" -SkipModels
.\scripts\setup_venv.ps1 -ForceLlama
```

说明：
- 依赖锁定文件为 `requirements_frozen.txt`（114 个包全量版本锁定），`requirements.txt` 为可读的核心依赖清单
- torch 三件套（+cu126 构建）从测速选出的 PyTorch 镜像安装，其余包从最快的 PyPI 镜像安装
- 选择逻辑为**带宽优先**（下载索引小文件实测 KB/s），带宽相同再比延迟
- 实测示例：PyPI 清华 TUNA（189 ms / 611 KB/s）、Torch 上海交大（360 ms / 704 KB/s）被自动选用；华为云、豆瓣等不可达源被自动剔除

### 3. 安装依赖项

1. **克隆仓库**：
   ```powershell
   git clone https://github.com/Snowarker/Mioucat-Workshop-Paper2Skill.git
   cd Mioucat-Workshop-Paper2Skill
   ```

2. **创建虚拟环境**：
   ```powershell
   python -m venv venv
   .\venv\Scripts\activate
   ```

3. **安装依赖**：
   ```powershell
   pip install -r requirements.txt
   ```

4. **PyTorch 版本说明**：
   - 默认通过 `requirements.txt` 安装的是 **CPU 版本**的 PyTorch
   - 如果您的系统有 NVIDIA GPU，建议安装 **GPU 版本**的 PyTorch 以获得更好的性能
   - 本项目当前实际使用 **torch 2.14.0+cu126**（CUDA 12.6 构建，对应驱动 CUDA 13.x，向下兼容）

5. **检测 CUDA 版本**：
   ```powershell
   # 查看当前系统的 CUDA 版本
   nvidia-smi
   ```
   输出中 "CUDA Version: X.X" 即为您的 CUDA 版本

6. **安装 GPU 版本的 PyTorch**：
   根据检测到的 CUDA 版本选择合适的安装命令：
   - CUDA 12.1：
     ```powershell
     pip uninstall torch torchvision torchaudio
     pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
     ```
   - CUDA 11.8：
     ```powershell
     pip uninstall torch torchvision torchaudio
     pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
     ```

7. **验证 GPU 安装**：
   ```powershell
   python -c "import torch; print('CUDA available:', torch.cuda.is_available()); print('GPU name:', torch.cuda.get_device_name(0) if torch.cuda.is_available() else 'No GPU')"
   ```

8. **使用 GPU 检查脚本**：
   ```powershell
   # 激活虚拟环境
   venv\Scripts\activate
   
   # 运行 GPU 检查脚本
   python scripts/check_gpu_pytorch.py
   ```
   
   该脚本会详细检查：
   - PyTorch 版本
   - CUDA 可用性
   - CUDA 版本
   - GPU 设备信息
   - 基本功能测试

### 步骤 4: 配置环境变量

1. **设置 Marker 模型路径**：
   ```powershell
   # 设置 Marker 模型目录
   $env:MARKER_MODEL_DIR = "$PWD\models"
   ```

2. **创建必要的目录**：
   ```powershell
   New-Item -ItemType Directory -Path "models" -Force
   New-Item -ItemType Directory -Path "llm_processed" -Force
   New-Item -ItemType Directory -Path "paper_skills" -Force
   ```

## marker-pdf 2.x GPU 推理适配（Windows）

marker-pdf 2.x 将阅读顺序/版面分析交给一个 **VLM 推理服务器**（surya-ocr-2 GGUF 模型）。Windows 上使用 **llama.cpp 本地后端**：

1. **下载 llama.cpp 发行版**（[GitHub releases](https://github.com/ggml-org/llama.cpp/releases)）：
   - 需要两个包，解压到 `tools/llama_cpp/`（与 `llama-server.exe` 同目录）：
     - `llama-<b版本>-bin-win-cuda-12.4-x64.zip`：主程序
     - `cudart-llama-bin-win-cuda-12.4-x64.zip`：**CUDA 运行时 DLL**（cudart64_12 / cublas64_12 / cublasLt64_12）
   - 缺少 cudart DLL 时 llama-server 会**静默回退 CPU 推理**（生成速度仅 ~5 t/s），两个包都必须安装

2. **配置推理后端环境变量**（在运行转换脚本前）：
   ```powershell
   $env:SURYA_INFERENCE_BACKEND = "llamacpp"
   $env:LLAMA_CPP_BINARY = "$PWD\tools\llama_cpp\llama-server.exe"
   $env:LLAMA_CPP_NGL = "99"   # 全量 GPU offload
   ```

3. **验证 CUDA 生效**：`nvidia-smi` 的进程列表中应能看到 `llama-server.exe`（加载 GGUF 后占用约 9GB 显存）；若不在列表中则说明退回 CPU 推理

4. **VLM 模型（GGUF）**：从 [datalab-to/surya-ocr-2-gguf](https://huggingface.co/datalab-to/surya-ocr-2-gguf) 下载 `surya-2.gguf` 与 `surya-2-mmproj.gguf`，放入 `models/gguf/`

## 模型目录统一管理

所有模型统一存放在项目 `models/` 目录（不占用 C 盘），`scripts/manage_models.py` 是独立的模型目录与版本管理脚本，`scripts/process_pdf.py` 启动时会自动调用它：

- `MODEL_CACHE_DIR` / `MARKER_MODEL_DIR` → `models/`（surya 文本检测、OCR 错误检测等模型）
- `SURYA_GGUF_LOCAL_MODEL_PATH` / `SURYA_GGUF_LOCAL_MMPROJ_PATH` → `models/gguf/`（VLM GGUF 模型）
- `HF_HOME` → `models/hf_home`（其余 HuggingFace 下载）

### manage_models.py 用法

```powershell
# 检查并自动补齐缺失的必需模型（process_pdf.py 启动时内部调用）
venv\Scripts\python scripts\manage_models.py

# 仅检查并报告（不下载），显示本地版本与远程最新版本
venv\Scripts\python scripts\manage_models.py --check

# 强制对照远程最新版本并更新（重新下载 GGUF 等）
venv\Scripts\python scripts\manage_models.py --update

# 清理不再被当前 surya 版本引用的旧版模型目录（如 1.x 遗留 text_recognition/table_recognition）
venv\Scripts\python scripts\manage_models.py --prune
```

管理范围（surya 2.x 实际使用的模型）：
- `gguf_vlm`（必需）：surya-ocr-2-gguf 的 `surya-2.gguf` + `surya-2-mmproj.gguf`，balanced/GPU 模式版面+识别一体模型
- `text_detection`（必需）：`s3://text_detection/2025_05_07`
- `ocr_error_detection`（必需）：`s3://ocr_error_detection/2025_02_18`
- `fast_layout`（可选，CPU fast 模式用）：`datalab-to/surya_layout2`
- `vlm_torch`（可选，torch 后端用）：`datalab-to/surya-ocr-2`

### 模型清单与用途说明

| 模型 | 来源（HuggingFace） | 用途 | 必需性 | 当前状态 |
|------|---------------------|------|--------|---------|
| `gguf_vlm` | [datalab-to/surya-ocr-2-gguf](https://huggingface.co/datalab-to/surya-ocr-2-gguf)（`surya-2.gguf` + `surya-2-mmproj.gguf`） | balanced 模式下版面分析 + 全页 OCR 一体的 VLM 模型，经 llama.cpp 推理（CUDA 加速） | 必需 | 已就绪 |
| `text_detection` | surya 官方 s3（`2025_05_07`） | 文本区域检测 | 必需 | 已就绪 |
| `ocr_error_detection` | surya 官方 s3（`2025_02_18`） | OCR 错误检测与修正 | 必需 | 已就绪 |
| `fast_layout` | [datalab-to/surya_layout2](https://huggingface.co/datalab-to/surya_layout2) | fast 模式（纯 CPU、无 VLM）下替代 VLM 的轻量版面分析模型 | 可选 | 未下载（当前不需要） |
| `vlm_torch` | [datalab-to/surya-ocr-2](https://huggingface.co/datalab-to/surya-ocr-2) | 与 `gguf_vlm` 同一 VLM 的 PyTorch 权重版，用于 torch 推理后端 | 可选 | 未下载（当前不需要） |

### 转换模式选择（balanced vs fast）

| 维度 | balanced（默认，GPU） | fast（CPU） |
|------|----------------------|------------|
| 版面识别方式 | VLM 模型（`gguf_vlm`） | 轻量布局模型（`fast_layout`） |
| 适用硬件 | 有 NVIDIA GPU（CUDA） | 纯 CPU |
| 速度 | 慢（VLM 推理），GPU 下约 108 t/s | 快（轻量模型） |
| 精度 | 高（复杂版面、公式、表格可靠） | 较低（复杂版面精度下降） |
| 触发方式 | `mode: "balanced"`（process_pdf.py 默认） | 改 `mode: "fast"` 并下载 `fast_layout` |

**选择建议**：科研文献转换对公式、表格、版面结构精度要求高，有 GPU 时一律使用 balanced 模式；fast 模式仅在无 GPU 的机器（如云主机批量转换）上作为降级方案，此时需先通过 `manage_models.py` 补齐 `fast_layout`。

### 推理后端选择（llama.cpp GGUF vs torch）

| 维度 | llama.cpp（GGUF，当前配置） | torch（PyTorch） |
|------|------------------------------|------------------|
| 权重格式 | `surya-2.gguf` + `surya-2-mmproj.gguf` | `surya-ocr-2`（PyTorch 权重） |
| 依赖 | llama.cpp + CUDA 运行时 DLL（cudart64_12.dll 等） | 仅 PyTorch（CUDA 版） |
| 性能 | 显存占用约 9GB，实测约 108 t/s | 与 GGUF 功能等价 |
| 使用场景 | 当前默认配置 | 仅在 llama.cpp 链路出现不可修复问题时作为替代 |

**选择建议**：当前默认使用 llama.cpp + GGUF 后端（已在环境变量 `SURYA_GGUF_LOCAL_MODEL_PATH` / `SURYA_GGUF_LOCAL_MMPROJ_PATH` 中配置）；`vlm_torch` 与 `gguf_vlm` 二选一，无需同时下载。若 GGUF 推理出现无法修复的问题，才需下载 `vlm_torch` 并切换推理后端。

### 工具版本参考

| 工具 | 版本 | 说明 |
|------|------|------|
| marker-pdf | 2.0.0 | PDF 转换引擎（marker 2.x API） |
| surya-ocr | 0.22.1 | 底层 OCR/版面模型运行库 |
| torch | 2.14.0+cu126 | PyTorch（CUDA 12.6 构建） |

转换模式与参数的具体用法见 [PDF 转换](01_03_pdf_conversion.md) 文档。



## 验证环境

### 检查安装状态

1. **验证 Python 包**：
   ```powershell
   pip list
   ```

2. **检查目录结构**：
   ```powershell
   Get-ChildItem -Directory
   ```

### 测试基本功能

1. **运行版本检查**：
   ```powershell
   # 检查工具版本
   python -c "print('Paper2Skill environment setup completed successfully!')"
   ```

2. **测试 PDF 转换**（可选）：
   如果您有测试 PDF 文件，可以运行简单的转换测试

## 常见问题

### 1. Python 版本问题
- **症状**：`python --version` 显示错误版本
- **解决**：确保正确的 Python 版本在 PATH 中优先级最高

### 2. 依赖安装失败
- **症状**：`pip install` 命令失败
- **解决**：
  - 升级 pip：`pip install --upgrade pip`
  - 检查网络连接
  - 尝试使用镜像源：`pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple`

### 3. 目录权限问题
- **症状**：无法创建目录或写入文件
- **解决**：确保您对当前目录有写入权限

### 4. Marker 模型下载失败
- **症状**：模型下载超时或失败
- **解决**：
  - 检查网络连接
  - 手动下载模型并放置到 `models` 目录

### 5. GPU 未生效（CPU 推理）
- **症状**：转换速度极慢（~5 t/s），CPU 占用高而 GPU 占用低，`nvidia-smi` 进程列表中没有 `llama-server.exe`
- **解决**：
  - 确认 `tools/llama_cpp/` 下存在 cudart64_12.dll / cublas64_12.dll / cublasLt64_12.dll（需安装 `cudart-llama-bin-win-cuda-12.4-x64.zip`）
  - 确认环境变量 `SURYA_INFERENCE_BACKEND=llamacpp`、`LLAMA_CPP_BINARY`、`LLAMA_CPP_NGL=99` 已设置
  - 确认端口 8080/8081 未被其他程序占用（Trae 本身占用 8080，可改用其他端口）

## 后续步骤

环境设置完成后，您可以开始使用 Paper2Skill 工具的核心功能：

- [PDF 转换](01_03_pdf_conversion.md)：将 PDF 文档转换为文本格式
- [LLM 处理](01_04_llm_processing.md)：使用大语言模型处理文档
- [Skill 提取](01_05_skill_extraction.md)：从文档中提取技能信息