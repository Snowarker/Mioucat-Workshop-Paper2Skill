# Python 包文档识别指南

## 概述

本指南详细介绍如何识别 Python 语言代码包文档，包括常用仓库、识别特征、识别方法、获取方案和版本管理。Python 包与 R 包类似，是科研数据分析中常见的工具材料，准确识别其来源与版本，是将其纳入 Wiki 知识库体系（见[项目理念与工程化框架](../SKILL.md#项目理念与工程化框架)）的第一步。

## 常用仓库

Python 包的分发渠道以 PyPI 为核心，辅以 conda 生态与源码仓库：

| 仓库 | 域名/入口 | 特点 |
|------|----------|------|
| PyPI | pypi.org | Python 官方包索引，`pip` 的默认来源 |
| conda-forge | anaconda.org/conda-forge | conda 生态社区频道，科学计算包齐全 |
| GitHub | github.com | 源码仓库，开发版的主要来源 |
| 私有源 | 如企业内部 index | 组织内部发布的包 |

**说明**：Python 生态以 PyPI 为事实上的公共包仓库；conda-forge 是科学计算场景下常用的预编译分发渠道。二者均可作为包的公共来源，识别时需区分。

## 识别特征

### 1. 包元数据（pyproject.toml / setup.py / setup.cfg）

Python 包的核心元数据声明在 `pyproject.toml`（现代标准）或 `setup.py`/`setup.cfg`（传统方式）中：

- **name**：包名（如 `pandas`、`scikit-learn`）
- **version**：版本号（如 `2.2.2`）
- **requires-python**：支持的 Python 版本范围
- **dependencies**：运行时依赖列表
- **project.urls**：项目主页，常指向 GitHub 或文档站
- **license**：许可证（如 `BSD-3-Clause`、`MIT`）

**示例（pyproject.toml）**：

```toml
[project]
name = "pandas"
version = "2.2.2"
requires-python = ">=3.9"
dependencies = ["numpy>=1.22.4", "python-dateutil>=2.8.2", ...]

[project.urls]
Homepage = "https://pandas.pydata.org"
Source = "https://github.com/pandas-dev/pandas"
```

### 2. 仓库来源标识

- **PyPI 包**：PyPI 页面（`pypi.org/project/{包名}/`），含版本列表、发布文件（wheel/sdist）、项目链接
- **conda-forge 包**：anaconda.org 页面，含 `conda install -c conda-forge 包名` 安装指令
- **GitHub 源码**：`project.urls.Source` 或 `Home-page` 指向的仓库

### 3. 发布文件命名

PyPI 发布文件命名包含包名、版本与平台信息：

- **sdist**：`包名-版本号.tar.gz`（如 `pandas-2.2.2.tar.gz`）
- **wheel**：`包名-版本号-{py版本}-{abi}-{平台}.whl`（如 `pandas-2.2.2-cp311-cp311-win_amd64.whl`）

文件名中的包名与版本号是识别与版本管理的关键标识。

### 4. 版本变更记录

- `CHANGELOG.md` / `HISTORY.md`：版本变更记录
- `docs/` 或官方文档站：发布说明（release notes）
- 版本号遵循 [PEP 440](https://peps.python.org/pep-0440/) 语义化版本规范（`X.Y.Z`，可选 `rc`、`post`、`dev` 后缀）

## 识别方法

### 1. 搜索包元数据

- 在文档中搜索 `[project]`、`name =`、`version =` 等字段
- 分析包名、版本号、依赖与许可证信息

### 2. 查找仓库来源

- 检查 `project.urls`、`Home-page` 字段指向的域名
- 判断包来自 PyPI、conda-forge 还是 GitHub 源码

### 3. 分析依赖关系

- 查看 `dependencies`、`[project.optional-dependencies]` 字段
- 依赖关系是知识库交叉引用的重要组成部分

### 4. 识别文档类型

- `CHANGELOG.md`：版本变更记录，用于版本追踪
- `docs/`：官方文档材料
- 源码 `src/` 或 `包名/` 目录：代码材料

## 获取方案

| 场景 | 命令/方式 | 说明 |
|------|----------|------|
| 安装 PyPI 包 | `pip install 包名==版本号` | 指定版本安装 |
| 仅下载不安装 | `pip download 包名==版本号 -d 目录` | 获取 wheel/sdist 文件作为 ground truth |
| 安装 conda-forge 包 | `conda install -c conda-forge 包名=版本号` | 科学计算场景常用 |
| 获取源码 | GitHub 仓库 clone 或 sdist 解压 | 记录 commit 哈希 |
| 私有源安装 | `pip install --index-url 内部源 包名` | 适用于企业内部包 |

## 版本管理

Python 包材料入库时，必须记录以下版本信息作为知识网络节点的属性：

1. **包名 + 版本号**：如 `pandas-2.2.2`（遵循 PEP 440）
2. **来源仓库**：PyPI / conda-forge / GitHub / 私有源
3. **GitHub 仓库信息**（如适用）：用户/仓库名、commit 哈希
4. **环境锁定文件**：`requirements.txt`、`environment.yml`、`poetry.lock`、`pip-tools` 输出，锁定分析环境的完整依赖版本

版本变更记录以 `CHANGELOG.md` 与官方发布说明为准，处理历史版本材料时需核对所用版本与论文/项目记录的一致性。

## 实践示例

### 示例 1：PyPI 包材料

**识别信息**：
- 包名：`scikit-learn`
- 版本：`1.5.1`
- 来源：PyPI
- 元数据来源：`pyproject.toml`
- 获取方式：`pip download scikit-learn==1.5.1 -d ./ground_truth/`
- 文档：`scikit-learn-1.5.1-cp311-cp311-win_amd64.whl`（ground truth）

### 示例 2：conda-forge 包材料

**识别信息**：
- 包名：`scanpy`
- 版本：`1.10.2`
- 来源：conda-forge
- 获取方式：`conda install -c conda-forge scanpy=1.10.2`
- 环境锁定：`environment.yml` 记录完整依赖版本

通过上述方法，可以准确识别 Python 包材料的来源、版本与获取方式，并将其作为 Wiki 知识库中的一个可追溯节点。
