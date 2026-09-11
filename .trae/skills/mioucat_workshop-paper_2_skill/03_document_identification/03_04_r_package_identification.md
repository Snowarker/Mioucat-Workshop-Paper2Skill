# R 包文档识别指南

## 概述

本指南详细介绍如何识别 R 语言代码包文档，包括常用仓库、识别特征、识别方法、获取方案和版本管理。R 包是科研数据分析中常见的工具材料，准确识别其来源与版本，是将其纳入 Wiki 知识库体系（见[项目理念与工程化框架](../SKILL.md#项目理念与工程化框架)）的第一步。

## 常用仓库

R 包的公共分发渠道主要有以下四类，识别时需区分包来自哪个仓库：

| 仓库 | 域名/入口 | 特点 |
|------|----------|------|
| CRAN | cran.r-project.org | R 官方综合档案网络，稳定版的主要来源 |
| Bioconductor | bioconductor.org | 生物信息学领域包，按版本（如 3.18）发布 |
| r-universe | r-universe.dev | 社区维护的包聚合平台 |
| GitHub | github.com | 开发版源码，经 `remotes`/`pak` 安装 |

## 识别特征

### 1. 包元数据（DESCRIPTION 文件）

R 包的核心元数据存储在 `DESCRIPTION` 文件中，包含以下关键字段：

- **Package**：包名（如 `dplyr`、`limma`）
- **Version**：版本号（如 `1.1.4`）
- **Title / Description**：包功能说明
- **Author / Maintainer**：作者与维护者信息
- **License**：许可证（如 `GPL-3`、`MIT`）
- **URL**：项目主页，常指向 GitHub 或 CRAN 页面
- **BugReports**：问题反馈地址
- **Imports / Suggests**：依赖的包列表

**示例**：

```
Package: dplyr
Version: 1.1.4
Title: A Grammar of Data Manipulation
URL: https://dplyr.tidyverse.org, https://github.com/tidyverse/dplyr
Imports: cli, generics, glue, lifecycle, magrittr, methods, pillar, R6, rlang, tibble, tidyselect, utils, vctrs
```

### 2. 仓库来源标识

- **CRAN 包**：CRAN 页面结构（`cran.r-project.org/web/packages/{包名}/`），含 Published 日期、License 等栏目
- **Bioconductor 包**：页面含 Bioconductor 版本号（如 `biocViews`、`3.18`）、维护者、依赖的 Bioconductor 版本
- **GitHub 开发版**：含 `Remotes` 字段或安装命令 `remotes::install_github("用户/仓库")`

### 3. 包内文档结构

R 包源码/二进制包内的典型文件：

- `DESCRIPTION`：元数据（ground truth 的核心）
- `NAMESPACE`：导出与导入声明
- `NEWS.md`（或 `NEWS`）：版本变更记录
- `man/`：函数帮助文档（Rd 格式）
- `vignettes/`：包的使用教程（vignette）
- `R/`：包源代码
- `CITATION`：引用信息（`citation("包名")` 可读取）

### 4. 版本命名格式

- 语义化版本：`主版本.次版本.修订号`（如 `1.1.4`）
- 源码包文件名：`包名_版本号.tar.gz`（如 `dplyr_1.1.4.tar.gz`）
- Bioconductor 包常附加发布版本信息

## 识别方法

### 1. 搜索包元数据

- 在文档中搜索 `Package:`、`Version:` 等 DESCRIPTION 字段
- 分析包名、版本号、作者与许可证信息

### 2. 查找仓库来源

- 检查 `URL:` 与 `BugReports:` 字段指向的域名
- 判断包属于 CRAN、Bioconductor、r-universe 还是 GitHub

### 3. 分析依赖关系

- 查看 `Imports`、`Suggests`、`Depends` 字段，判断包在依赖网络中的位置
- 依赖关系是知识库交叉引用的重要组成部分

### 4. 识别文档类型

- `NEWS.md`：版本变更记录，用于版本追踪
- `vignettes/`：使用教程，属于文档材料
- `man/`：API 参考文档

## 获取方案

| 场景 | 命令/方式 | 说明 |
|------|----------|------|
| 安装 CRAN 稳定版 | `install.packages("包名")` | 最常用，安装最新稳定版 |
| 安装 Bioconductor 包 | `BiocManager::install("包名")` | 需先安装 `BiocManager` |
| 安装 GitHub 开发版 | `remotes::install_github("用户/仓库")` | 需指定用户与仓库名 |
| 下载源码包 | CRAN 页面下载 `包名_版本号.tar.gz` | 保留 ground truth 文件 |
| 本地安装 | `R CMD INSTALL 包名_版本号.tar.gz` | 适用于离线环境 |

## 版本管理

R 包材料入库时，必须记录以下版本信息作为知识网络节点的属性：

1. **包名 + 版本号**：如 `dplyr_1.1.4`
2. **来源仓库**：CRAN / Bioconductor / r-universe / GitHub
3. **GitHub 仓库信息**（如适用）：用户/仓库名、commit 哈希
4. **依赖记录**：`renv.lock` 或 `sessionInfo()` 输出，锁定分析环境版本

版本变更记录以 `NEWS.md` 为准，处理历史版本材料时需核对所用版本与论文/项目记录的一致性。

## 实践示例

### 示例 1：CRAN 包材料

**识别信息**：
- 包名：`DESeq2`
- 版本：`1.42.1`
- 来源：Bioconductor（非 CRAN）
- 元数据来源：`DESCRIPTION` 文件
- 安装方式：`BiocManager::install("DESeq2")`
- 文档：`DESeq2_1.42.1.tar.gz`（ground truth）

### 示例 2：GitHub 开发版包

**识别信息**：
- 包名：`Seurat`
- 版本：`5.0.1`
- 来源：GitHub（`satijalab/seurat`）
- 安装方式：`remotes::install_github("satijalab/seurat")`
- 版本管理：记录 commit 哈希，与 CRAN 稳定版区分

通过上述方法，可以准确识别 R 包材料的来源、版本与获取方式，并将其作为 Wiki 知识库中的一个可追溯节点。
