# 环境设置

## 1. 系统要求

- **Python 版本**：必须使用 Python 3.10.11 或更高版本
- **操作系统**：优先适配 Windows 10/11（其他系统未测试）
- **内存**：推荐 16GB RAM 或更高
- **存储空间**：推荐至少 20GB 可用空间
- **GPU**：推荐使用 NVIDIA GPU（支持 CUDA）以获得最佳性能

## 2. 虚拟环境设置

### 2.1 创建虚拟环境

在项目根目录下执行以下命令：

```powershell
# 创建虚拟环境
python -m venv venv
```

### 2.2 激活虚拟环境

```powershell
# 激活虚拟环境
venv\Scripts\activate
```

### 2.3 升级 pip

```powershell
# 升级 pip
pip install --upgrade pip
```

### 2.4 安装依赖

```powershell
# 安装依赖
pip install -r requirements.txt
```

## 3. 环境验证

### 3.1 检查 Python 版本

```powershell
# 检查 Python 版本
python --version
```

### 3.2 检查虚拟环境

```powershell
# 检查虚拟环境是否激活
# 查看命令提示符是否显示 (venv)
# 或者执行以下命令
where python
```

### 3.3 检查 GPU 可用性

```powershell
# 检查 GPU 可用性
python scripts/check_gpu_pytorch.py
```

## 4. 常见问题

### 4.1 虚拟环境激活失败

**问题**：无法激活虚拟环境

**解决方案**：
```powershell
# 尝试使用完整路径
.envcriptsctivate.ps1

# 或者检查执行策略
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### 4.2 依赖安装失败

**问题**：pip install 命令失败

**解决方案**：
```powershell
# 尝试使用 --no-cache-dir
pip install --no-cache-dir -r requirements.txt

# 或者使用国内镜像源
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt
```

### 4.3 GPU 检测失败

**问题**：check_gpu_pytorch.py 显示没有可用 GPU

**解决方案**：
```powershell
# 检查 NVIDIA 驱动是否安装
nvidia-smi

# 确保安装了正确版本的 CUDA
# 访问 NVIDIA 官网下载对应驱动
```

## 5. 后续步骤

环境设置完成后，可以继续执行以下步骤：

1. **PDF 转换**：查看 `0001_02_pdf_conversion.md` 了解如何转换 PDF 文件
2. **LLM 处理**：查看 `0001_03_llm_processing.md` 了解如何处理转换后的文档
3. **Skill 提取**：查看 `0001_04_skill_extraction.md` 了解如何提取 skill 信息