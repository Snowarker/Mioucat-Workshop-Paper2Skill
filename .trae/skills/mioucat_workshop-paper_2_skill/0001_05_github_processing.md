# GitHub 仓库处理

## 概述

GitHub 仓库处理是 Paper2Skill 工具的扩展功能，负责将 GitHub 仓库克隆到本地并为大模型分析准备结构化的内容。本指南将详细介绍 GitHub 仓库处理的操作步骤和注意事项。

## 处理原理

Paper2Skill 工具使用专门的 GitHub 处理模块，为大模型分析准备结构化内容，主要包括以下功能：

- **仓库克隆**：将 GitHub 仓库克隆到本地 source 目录
- **结构分析**：分析仓库的目录结构和文件组织
- **关键文件提取**：提取 README、入口文件、核心模块等关键文件
- **内容结构化**：为大模型处理准备结构化的文件列表和内容摘要
- **目录对应**：与 llm_processed 目录结构保持一致，便于内容组织和访问

## 准备工作

### 1. 确保环境已配置

- **Git 已安装**：确保系统已安装 Git
- **依赖项已安装**：确保所有必要的依赖项都已安装
- **GitHub 访问权限**：确保有权限访问目标 GitHub 仓库

### 2. 目录结构（自动创建）

处理脚本会自动创建以下目录结构：

```
├── source/
│   └── github/              # GitHub 仓库代码
│       └── username/        # GitHub 用户名
│           └── repository/   # 仓库名
└── llm_processed/
    └── github/              # 处理结果
        └── username/        # GitHub 用户名
            └── repository/   # 仓库名
                ├── summary.md     # 仓库摘要
                ├── structure.md   # 目录结构分析
                ├── tech_stack.md  # 技术栈分析
                ├── architecture.md # 架构设计分析
                └── key_files/      # 关键文件内容
```

## 处理操作

### 基本处理命令

```powershell
# Windows - 处理单个 GitHub 仓库
python scripts/process_github.py --repo-url "https://github.com/username/repository"

# WSL - 处理单个 GitHub 仓库
python3 scripts/process_github.py --repo-url "https://github.com/username/repository"
```

### 批量处理

```powershell
# Windows - 批量处理多个 GitHub 仓库
$repos = @(
    "https://github.com/username/repo1",
    "https://github.com/username/repo2",
    "https://github.com/username/repo3"
)

foreach ($repo in $repos) {
    Write-Host "Processing $repo"
    python scripts/process_github.py --repo-url $repo
}

# WSL - 批量处理多个 GitHub 仓库
repos=("https://github.com/username/repo1" "https://github.com/username/repo2" "https://github.com/username/repo3")

for repo in "${repos[@]}"; do
    echo "Processing $repo"
    python3 scripts/process_github.py --repo-url "$repo"
done
```

## 处理参数

### 常用参数

| 参数 | 说明 | 默认值 |
|------|------|--------|
| `--repo-url` | GitHub 仓库 URL | 无（必需） |
| `--branch` | 仓库分支 | `main` |
| `--depth` | 克隆深度 | 1 |
| `--file-types` | 要处理的文件类型 | `py,md,js,ts,html,css` |

### 高级参数

| 参数 | 说明 | 默认值 |
|------|------|--------|
| `--max-files` | 最大处理文件数 | 100 |
| `--max-file-size` | 最大文件大小（KB） | 500 |
| `--exclude-patterns` | 排除的文件模式 | `test,__pycache__,node_modules` |
| `--verbose` | 是否显示详细信息 | `False` |

## 处理结果检查

### 检查处理质量

1. **打开输出目录**：
   - 打开生成的 llm_processed/github/username/repository 目录
   - 检查提取的文件是否完整
   - 检查生成的摘要文件是否合理

2. **检查 source 目录**：
   - 打开 source/github/username/repository 目录
   - 确认仓库代码是否完整克隆
   - 检查目录结构是否与远程仓库一致

3. **常见问题检查**：
   - **仓库克隆失败**：检查网络连接和访问权限
   - **文件提取不完整**：检查文件大小限制和排除模式
   - **目录结构不匹配**：检查脚本执行是否成功

### 结果结构

处理后的目录通常包含以下文件：

- **summary.md**：仓库的整体摘要和核心功能
- **structure.md**：仓库的目录结构分析
- **tech_stack.md**：仓库使用的技术栈
- **architecture.md**：仓库的架构设计分析
- **key_files/**：提取的关键文件内容

## 最佳实践

### 1. 仓库选择

- **选择活跃仓库**：优先选择维护活跃的仓库
- **选择文档完善的仓库**：优先选择有详细 README 和文档的仓库
- **选择规模适中的仓库**：过大的仓库可能处理时间长，过小的仓库可能信息不足

### 2. 处理设置

- **调整文件类型**：根据仓库类型调整要处理的文件类型
- **合理设置深度**：对于大型仓库，使用较浅的克隆深度
- **适当排除文件**：排除测试文件和依赖目录，提高处理效率

### 3. 结果处理

- **及时检查**：处理完成后立即检查结果
- **人工审核**：对重要仓库的处理结果进行人工审核
- **建立规范**：建立统一的文件命名和存储规范

## 故障排除

### 常见问题

| 问题 | 原因 | 解决方案 |
|------|------|----------|
| 仓库克隆失败 | 网络连接问题 | 检查网络连接，使用代理（如果需要） |
| 仓库访问被拒绝 | 权限不足 | 确保有访问权限，使用 SSH 认证 |
| 处理超时 | 仓库过大 | 减小处理范围，增加超时时间 |
| 内存不足 | 处理文件过多 | 减小最大文件数，增加系统内存 |

### 错误信息处理

| 错误信息 | 含义 | 解决方案 |
|----------|------|----------|
| `Git command failed` | Git 命令执行失败 | 检查 Git 安装和配置 |
| `Repository not found` | 仓库未找到 | 检查仓库 URL 是否正确 |
| `Permission denied` | 权限被拒绝 | 检查访问权限，使用正确的认证方式 |
| `Network error` | 网络错误 | 检查网络连接，重试操作 |

## 后续步骤

GitHub 仓库处理完成后，您可以进行以下操作：

1. **检查处理结果**：确保提取的信息质量满足要求
2. **进行 LLM 处理**：使用大语言模型分析提取的仓库信息
3. **提取 Skill 信息**：从处理后的信息中提取结构化的技能信息

## 示例

### 示例 1: 处理单个 GitHub 仓库

```powershell
# 处理单个 GitHub 仓库
python scripts/process_github.py --repo-url "https://github.com/Snowarker/Mioucat-Workshop-Paper2Skill"

# 检查结果
Get-ChildItem "llm_processed/github/Snowarker/Mioucat-Workshop-Paper2Skill"
Get-Content "llm_processed/github/Snowarker/Mioucat-Workshop-Paper2Skill/summary.md" | Select-Object -First 30

# 检查 source 目录
Get-ChildItem "source/github/Snowarker/Mioucat-Workshop-Paper2Skill"
```

### 示例 2: 处理指定分支

```powershell
# 处理指定分支
python scripts/process_github.py --repo-url "https://github.com/username/repository" --branch "develop"

# 检查结果
Get-Content "llm_processed/github/username/repository/structure.md"
```

### 示例 3: 批量处理多个仓库

```powershell
# 创建仓库列表文件
@"https://github.com/Snowarker/Mioucat-Workshop-Paper2Skill"
"https://github.com/openai/whisper"
"https://github.com/microsoft/playwright"
@" | Out-File -FilePath "source/github/repos.txt" -Encoding utf8

# 批量处理
$repos = Get-Content "source/github/repos.txt"
foreach ($repo in $repos) {
    Write-Host "Processing $repo"
    python scripts/process_github.py --repo-url $repo
}

Write-Host "Batch processing completed!"
```