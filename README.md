# MiouCat Workshop - Paper2Skill

## 项目概述

本项目是 MiouCat Workshop 体系中的一个衍生模块，专注于多源信息的处理流程，包括科研文献、专利、GitHub 仓库、公众号文章、R 包和 Python 包的处理，将提取的内容转换为规范化的 Markdown 文档并提取结构化的技能知识。

## 工作流程

本项目的完整工作流程分为三个主要部分：

1. **源文档处理**：处理不同类型的源文档（PDF、HTML、GitHub 仓库、R 包、Python 包），提取内容和相关资源
2. **Markdown 文档结构化处理**：利用 LLM（大语言模型）对提取的内容进行进一步处理，生成结构化的 Markdown 文档
3. **Skill 信息提取与凝练**：从结构化处理后的 Markdown 文档中提取和凝练 Skill 相关信息

## 核心脚本工具

本项目提供以下核心 Python 脚本：

- **process_pdf.py**：处理 PDF 文档，提取文字内容和图片，生成对应的 Markdown 文档和图片文件夹。
- **manage_models.py**：独立的模型目录与版本管理脚本，支持检查（--check）、更新（--update）、清理（--prune）模型，process_pdf.py 启动时自动调用。
- **analyze_pdf_images.py**：分析 PDF 文档中的图片信息，用于调试和问题排查。
- **check_image_sizes.py**：检查图片尺寸信息，用于调试和问题排查。
- **check_gpu_pytorch.py**：检查设备是否有 GPU 可用，验证 PyTorch 配置。
- **setup_venv.ps1**：虚拟环境重建脚本，包含动态镜像源检测。

## 系统要求

- **Python 版本**：必须使用 Python 3.10.11 或更高版本
- **操作系统**：优先适配 Windows 10/11（其他系统未测试）
- **内存**：推荐 16GB RAM 或更高
- **存储空间**：推荐至少 20GB 可用空间（用于模型文件和处理结果）
- **GPU**：推荐使用 NVIDIA GPU（支持 CUDA）以获得最佳性能

## 使用指南

详细的使用指南请参考项目中的面向用户的 Skill 文档。在使用本工具时，您可以向 Trae 询问：

"请参考 MiouCat_Workshop-Paper_2_Skill skill 文档，提供 Paper2Skill 工具的使用指南。"

## 项目目录结构

目录按用途分为五类，由主到次依次为：**配置目录、处理工具与模型、标准与项目文档、源材料、处理产物**。

### 配置目录

- **.trae/**：Trae IDE 内置配置目录
  - **.trae/skills/**：面向用户的 Skill 文档（使用指南、项目理念、版本更新记录）

### 处理工具与模型目录

- **models/**：模型文件目录
  - 集中存储 PDF 转换所需模型（版面、文本、GGUF）
  - 通过环境变量统一管理，避免重复下载、占用系统盘
- **tools/**：本地工具链目录
  - **llama_cpp/**：llama.cpp 工具链（含 CUDA 运行时 DLL），用于 GPU 加速推理
- **scripts/**：脚本工具目录
  - **process_pdf.py**：处理 PDF 文档，提取文字和图片
  - **manage_models.py**：模型目录与版本管理（检查/更新/清理）
  - **analyze_pdf_images.py**：分析 PDF 中的图片信息，用于调试
  - **check_image_sizes.py**：检查图片尺寸信息，用于调试
  - **check_gpu_pytorch.py**：检查 GPU 可用性，验证 PyTorch 配置
  - **setup_venv.ps1**：虚拟环境重建脚本

### 标准与项目文档目录

- **llm_standard/**：LLM 处理标准
  - **std_guide/pdf_guide/**：特定期刊的 PDF 处理规范指南
- **docs/**：项目文档目录
  - **docs/images/**：图片资源（如公众号二维码）
  - **docs/work_logs/**：工作日志

### 源材料目录

- **pdf/**：PDF 文件相关目录
  - **pdf/input/**：存放原始 PDF 文件
  - **pdf/output/**：存放初始 PDF 处理输出（Markdown 和图片）
- **html/**：HTML 网页文件目录
  - 按平台 → 账号 → 文章的层级组织
  - 存放从网页保存的 HTML 文件，如微信公众号文章
- **source/**：源代码和仓库目录
  - 按来源组织，如 GitHub 仓库等

### 处理产物目录

- **llm_processed/**：LLM 处理后文档目录
  - 按出版社/平台 → 期刊/账号 → 文章的层级组织
  - 每篇文章单独一个文件夹，包含处理后的 Markdown 文档和相关图片
- **paper_skills/**：提取的技能文档目录
  - 按主题、方法、期刊三种方式分类
  - 每个分类下有总领性文件，提供层级式索引

## 技术栈

- **PDF 处理**：使用 Marker 工具进行 PDF 到 Markdown 的转换
- **GPU 加速**：llama.cpp + CUDA（GGUF 推理）
- **环境管理**：Python 3.10 虚拟环境，一键重建（scripts/setup_venv.ps1）

### 环境构筑材料

项目根目录下的三个文件共同定义了可复刻的虚拟环境，分工如下：

| 文件 | 作用 |
|------|------|
| `pyproject.toml` | 项目元数据：名称、版本、作者、许可证与顶层核心依赖声明 |
| `requirements.txt` | 核心依赖清单：Marker（marker-pdf 2.0.0）与 PyMuPDF，含 PyTorch CUDA 安装提示 |
| `requirements_frozen.txt` | 完整锁定版本快照（pip freeze）：`scripts/setup_venv.ps1` 实际安装依据，保证环境可精确复刻 |

**一键重建环境**：在项目根目录运行 `.\scripts\setup_venv.ps1`，脚本会自动检测镜像源、安装 PyTorch CUDA 与锁定依赖、补齐 llama.cpp 工具链与模型，并验证 GPU 加速是否生效。

### 关于 Marker 工具

本项目使用 [Marker](https://github.com/VikParuchuri/marker) 工具进行 PDF 到 Markdown 的转换，这是一个功能强大的开源工具，能够高效地提取 PDF 文档中的文字和图片。

**Marker GitHub 主页**：[https://github.com/VikParuchuri/marker](https://github.com/VikParuchuri/marker)

**致谢**：

- 本项目对 Marker 团队及其社区贡献者表示诚挚的感谢，感谢他们开发和维护了如此优秀的 PDF 处理工具，为科研文献和专利的数字化处理提供了有力支持。
- 本项目对 Trae IDE 开发团队及其社区贡献者表示诚挚的感谢，特别是中文版 Trae IDE（https://www.trae.cn/），为项目的开发和使用提供了强大的集成环境支持。

## 许可证

本项目采用 MIT 许可证。

## 版本信息与项目进展

> 说明：本页只记录最近两个版本之间的变化（当前版本相对上一版本的变更），完整版本历史请参考 Skill 文档中的[版本更新记录](.trae/skills/mioucat_workshop-paper_2_skill/05_data_management/05_05_version_history.md)。

### 当前版本：0.3.0（自 0.2.0 以来的变化）

- **版本号**：0.3.0
- **开发状态**：活跃开发中
- **主要变更**：
  - 新增 `manage_models.py` 独立模型管理脚本（检查/更新/清理），`process_pdf.py` 启动时自动调用
  - 接入 GPU 加速（llama.cpp + CUDA 运行时），实测推理速度提升约 20 倍
  - 模型统一存放于 `models/` 目录，通过环境变量管理，避免占用系统盘
  - Skill 文档结构化重构（7 大分类），确立 Wiki 知识库体系理念（入库即构建知识网络、保留 ground truth）
  - 新增 R 包（CRAN/Bioconductor）与 Python 包（PyPI/conda-forge）来源识别

### 开发说明

- 项目采用模块化设计，便于后续功能扩展和优化
- 部分高级功能和专业领域的 Skill 处理可能会在后续版本中进一步完善
- 如需了解更多开发细节或讨论相关合作，可通过联系邮箱与作者沟通

**联系邮箱**：service@zhuyintech.cn

## 公众号

关注我们的公众号获取更多信息：

### 咪噢喵

![公众号二维码](docs/images/wechat_qrcode.png)

扫描上方二维码关注 "咪噢喵" 公众号，获取项目最新动态、技术分享和更多科研工具。