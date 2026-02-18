# 网络文章处理

## 概述

网络文章处理是 Paper2Skill 工具的扩展功能，负责爬取和处理微信公众号、小红书等网络文章，为大模型分析准备结构化的内容。本指南将详细介绍网络文章处理的操作步骤和注意事项。

## 处理原理

Paper2Skill 工具使用专门的网络文章处理模块，为大模型分析准备结构化内容，主要包括以下功能：

- **文章爬取**：爬取网络文章的完整内容（支持浏览器模拟）
- **内容提取**：提取文章的标题、正文、图片等信息
- **格式处理**：处理 HTML 格式，转换为标准化的 Markdown 格式
- **内容结构化**：为大模型处理准备干净的文本内容和关键观点
- **目录对应**：与 llm_processed 目录结构保持一致，便于内容组织和访问

## 准备工作

### 1. 确保环境已配置

- **依赖项已安装**：确保所有必要的依赖项都已安装
- **网络连接正常**：确保系统网络连接正常
- **浏览器驱动已配置**：如需使用浏览器模拟，确保已配置相应驱动

### 2. 目录结构（自动创建）

处理脚本会自动创建以下目录结构：

```
└── llm_processed/
    └── web/                   # 网络文章处理结果
        ├── platform/          # 平台分类（如wechat、xiaohongshu）
        │   ├── account/       # 账号名称
        │   │   └── article/   # 文章目录
        │   │       ├── content.md # 文章内容
        │   │       ├── summary.md # 文章摘要
        │   │       ├── key_points.md # 关键观点
        │   │       └── images/    # 文章图片
        │   └── account2/
        └── platform2/
```

## 处理操作

### 基本处理命令

```powershell
# Windows - 处理单个网络文章
python scripts/process_web_article.py --url "https://example.com/article"

# WSL - 处理单个网络文章
python3 scripts/process_web_article.py --url "https://example.com/article"
```

### 批量处理

```powershell
# Windows - 批量处理多个网络文章
$urls = @(
    "https://example.com/article1",
    "https://example.com/article2",
    "https://example.com/article3"
)

foreach ($url in $urls) {
    Write-Host "Processing $url"
    python scripts/process_web_article.py --url $url
}

# WSL - 批量处理多个网络文章
urls=("https://example.com/article1" "https://example.com/article2" "https://example.com/article3")

for url in "${urls[@]}"; do
    echo "Processing $url"
    python3 scripts/process_web_article.py --url "$url"
done
```

## 处理参数

### 常用参数

| 参数 | 说明 | 默认值 |
|------|------|--------|
| `--url` | 网络文章 URL | 无（必需） |
| `--platform` | 文章平台 | `auto` |
| `--include-images` | 是否包含图片 | `True` |
| `--timeout` | 超时时间（秒） | 30 |

### 高级参数

| 参数 | 说明 | 默认值 |
|------|------|--------|
| `--use-browser` | 是否使用浏览器模拟 | `False` |
| `--user-agent` | 自定义 User-Agent | 内置默认值 |
| `--proxy` | 代理服务器 | 无 |
| `--max-retries` | 最大重试次数 | 3 |
| `--verbose` | 是否显示详细信息 | `False` |

## 支持的平台

| 平台 | 支持状态 | 特点 |
|------|---------|------|
| 微信公众号 | ✅ 完全支持 | 需要特殊处理，支持文章和图片提取 |
| 小红书 | ✅ 完全支持 | 支持图文内容提取 |
| 知乎 | ✅ 完全支持 | 支持问答和文章内容提取 |
| 博客网站 | ✅ 完全支持 | 支持大多数博客平台 |
| 新闻网站 | ⚠️ 部分支持 | 可能有付费墙和反爬限制 |

## 处理结果检查

### 检查处理质量

1. **打开输出目录**：
   - 打开生成的 llm_processed/web/platform/account/article 目录
   - 检查提取的内容是否完整
   - 检查生成的摘要文件是否合理

2. **常见问题检查**：
   - **文章爬取失败**：检查网络连接和反爬机制
   - **内容提取不完整**：检查平台类型和页面结构
   - **图片下载失败**：检查网络连接和图片权限
   - **目录结构不匹配**：检查脚本执行是否成功

### 结果结构

处理后的目录通常包含以下文件：

- **content.md**：提取的文章完整内容
- **summary.md**：文章的核心观点和摘要
- **key_points.md**：文章中的关键观点和技能点
- **images/**：提取的文章图片（如果启用）

## 最佳实践

### 1. 文章选择

- **选择高质量文章**：优先选择内容丰富、结构清晰的文章
- **选择与技能相关的文章**：优先选择包含实用技能和方法的文章
- **选择权威来源**：优先选择权威平台和作者的文章

### 2. 处理设置

- **合理设置超时**：对于网络状况不佳的情况，适当增加超时时间
- **选择性包含图片**：对于图片重要的文章，启用图片包含
- **使用浏览器模拟**：对于反爬严格的网站，启用浏览器模拟

### 3. 结果处理

- **及时检查**：处理完成后立即检查结果
- **人工审核**：对重要文章的处理结果进行人工审核
- **建立规范**：建立统一的文件命名和存储规范

## 故障排除

### 常见问题

| 问题 | 原因 | 解决方案 |
|------|------|----------|
| 文章爬取失败 | 网络连接问题 | 检查网络连接，增加超时时间 |
| 反爬机制阻止 | 网站反爬限制 | 启用浏览器模拟，使用代理 |
| 内容提取不完整 | 页面结构复杂 | 调整提取参数，使用浏览器模拟 |
| 图片下载失败 | 图片权限限制 | 检查图片链接，使用浏览器模拟 |

### 错误信息处理

| 错误信息 | 含义 | 解决方案 |
|----------|------|----------|
| `Connection error` | 连接错误 | 检查网络连接，重试操作 |
| `Timeout error` | 超时错误 | 增加超时时间，检查网络状况 |
| `Access denied` | 访问被拒绝 | 使用浏览器模拟，更换 User-Agent |
| `Content not found` | 内容未找到 | 检查 URL 是否正确，页面是否存在 |

## 反爬策略

### 1. 基本反爬措施

- **合理的请求间隔**：避免频繁请求同一网站
- **随机 User-Agent**：使用不同的 User-Agent 轮换
- **IP 轮换**：对于大规模爬取，使用代理 IP 轮换

### 2. 高级反爬措施

- **浏览器模拟**：使用 Selenium 等工具模拟真实浏览器行为
- **Cookie 管理**：维护会话 Cookie，模拟登录状态
- **JavaScript 渲染**：处理需要 JavaScript 渲染的页面

## 后续步骤

网络文章处理完成后，您可以进行以下操作：

1. **检查处理结果**：确保提取的内容质量满足要求
2. **进行 LLM 处理**：使用大语言模型分析提取的文章内容
3. **提取 Skill 信息**：从处理后的内容中提取结构化的技能信息

## 示例

### 示例 1: 处理微信公众号文章

```powershell
# 处理微信公众号文章
python scripts/process_web_article.py --url "https://mp.weixin.qq.com/s/example" --platform "wechat"

# 检查结果
Get-ChildItem "llm_processed/web/wechat/account/article"
Get-Content "llm_processed/web/wechat/account/article/summary.md" | Select-Object -First 30
```

### 示例 2: 处理小红书文章

```powershell
# 处理小红书文章
python scripts/process_web_article.py --url "https://www.xiaohongshu.com/example" --platform "xiaohongshu"

# 检查结果
Get-Content "llm_processed/web/xiaohongshu/account/article/key_points.md"
```

### 示例 3: 批量处理多个平台文章

```powershell
# 创建文章 URL 列表文件
@"https://mp.weixin.qq.com/s/example1"
"https://www.xiaohongshu.com/example2"
"https://zhuanlan.zhihu.com/p/example3"
@" | Out-File -FilePath "llm_processed/web/articles.txt" -Encoding utf8

# 批量处理
$urls = Get-Content "llm_processed/web/articles.txt"
foreach ($url in $urls) {
    Write-Host "Processing $url"
    python scripts/process_web_article.py --url $url
}

Write-Host "Batch processing completed!"
```

## 注意事项

1. **遵守网站规则**：在爬取网络文章时，务必遵守目标网站的 robots.txt 规则和使用条款
2. **合理使用资源**：避免对目标网站造成过大负担，合理控制请求频率
3. **尊重版权**：提取的内容仅用于个人学习和研究，不得用于商业用途
4. **数据隐私**：注意保护文章中的个人隐私信息，避免泄露敏感数据

通过本指南的操作步骤，您可以有效地处理网络文章，提取其中的有价值信息，并将其转换为结构化的 Skill 文档。