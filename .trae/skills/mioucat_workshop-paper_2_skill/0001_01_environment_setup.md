# 环境设置

## 系统要求

在开始使用 Paper2Skill 工具之前，请确保您的系统满足以下要求：

### 硬件要求
- **内存**：至少 8GB RAM（推荐 16GB 或更高）
- **存储空间**：至少 50GB 可用空间
- **处理器**：4 核或更多核心的 CPU
- **网络连接**：稳定的互联网连接（用于模型下载和更新）

### 软件要求
- **操作系统**：
  - Windows 10/11 (64位)
  - 或 WSL2 (Ubuntu 20.04 或更高版本)
- **Python**：Python 3.8 或更高版本
- **Git**：最新版本的 Git
- **PDF 处理库**：Poppler 或 Ghostscript

## Windows 环境设置

### 步骤 1: 安装 Python

1. **下载 Python**：
   - 访问 [Python 官方网站](https://www.python.org/downloads/)
   - 下载最新版本的 Python（3.8 或更高）
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

### 步骤 3: 安装依赖项

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

## WSL 环境设置

### 步骤 1: 安装 WSL

1. **启用 WSL**：
   ```powershell
   wsl --install
   ```

2. **重启系统**：
   安装完成后重启计算机

3. **设置 Ubuntu**：
   首次启动时设置用户名和密码

### 步骤 2: 安装依赖项

1. **更新系统**：
   ```bash
   sudo apt update && sudo apt upgrade -y
   ```

2. **安装必要软件**：
   ```bash
   sudo apt install -y python3 python3-pip python3-venv git poppler-utils
   ```

3. **克隆仓库**：
   ```bash
   git clone https://github.com/Snowarker/Mioucat-Workshop-Paper2Skill.git
   cd Mioucat-Workshop-Paper2Skill
   ```

4. **创建虚拟环境**：
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

5. **安装依赖**：
   ```bash
   pip install -r requirements.txt
   ```

### 步骤 3: 配置环境变量

1. **设置 Marker 模型路径**：
   ```bash
   # 添加到 .bashrc
   echo "export MARKER_MODEL_DIR=$(pwd)/models" >> ~/.bashrc
   source ~/.bashrc
   ```

2. **创建必要的目录**：
   ```bash
   mkdir -p models llm_processed paper_skills
   ```

## 验证环境

### 检查安装状态

1. **验证 Python 包**：
   ```powershell
   # Windows
   pip list
   
   # WSL
   pip3 list
   ```

2. **检查目录结构**：
   ```powershell
   # Windows
   Get-ChildItem -Directory
   
   # WSL
   ls -la
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

## 后续步骤

环境设置完成后，您可以开始使用 Paper2Skill 工具的核心功能：

- [PDF 转换](0001_02_pdf_conversion.md)：将 PDF 文档转换为文本格式
- [LLM 处理](0001_03_llm_processing.md)：使用大语言模型处理文档
- [Skill 提取](0001_04_skill_extraction.md)：从文档中提取技能信息