# MiouCat Workshop - Paper2Skill

## 项目概述

本项目是 MiouCat Workshop 体系中的一个衍生模块，专注于多源信息的处理流程，包括科研文献、专利、GitHub 仓库和公众号文章的处理，将提取的内容转换为规范化的 Markdown 文档并提取结构化的技能知识。

## 工作流程

本项目的完整工作流程分为三个主要部分：

1. **源文档处理**：处理不同类型的源文档（PDF、HTML、GitHub 仓库），提取内容和相关资源
2. **Markdown 文档结构化处理**：利用 LLM（大语言模型）对提取的内容进行进一步处理，生成结构化的 Markdown 文档
3. **Skill 信息提取与凝练**：从结构化处理后的 Markdown 文档中提取和凝练 Skill 相关信息

## 核心脚本工具

本项目提供以下核心 Python 脚本：

- **process_pdf.py**：处理 PDF 文档，提取文字内容和图片，生成对应的 Markdown 文档和图片文件夹。
- **analyze_pdf_images.py**：分析 PDF 文档中的图片信息，用于调试和问题排查。
- **check_gpu_pytorch.py**：检查设备是否有 GPU 可用，验证 PyTorch 配置。

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

### 核心目录说明

1. **pdf/**：PDF文件相关目录
   - **pdf/input/**：存放原始PDF文件
   - **pdf/output/**：存放初始PDF处理输出（Markdown和图片）

2. **html/**：HTML网页文件目录
   - 按平台 → 账号 → 文章的层级组织
   - 存放从网页保存的HTML文件，如微信公众号文章

3. **models/**：存放Marker工具用于PDF转换时的模型文件
   - 集中存储所有模型文件
   - 通过环境变量配置，确保Marker工具能够正确找到模型
   - 避免重复下载模型，提高处理速度

4. **llm_processed/**：存放使用大语言模型（LLM）处理后的文档
   - 按出版社/平台 → 期刊/账号 → 文章的层级组织
   - 每篇文章单独一个文件夹，包含处理后的Markdown文档和相关图片

5. **paper_skills/**：存放提取的技能文档
   - 按主题、方法、期刊三种方式分类
   - 每篇文章可能出现在多个分类中，形成结构化记忆
   - 每个分类下有总领性文件，提供层级式索引

6. **source/**：存放源代码和仓库
   - 按来源组织，如GitHub仓库等
   - 便于代码管理、版本控制和分析

7. **scripts/**：存放项目脚本工具
   - **process_pdf.py**：处理PDF文档，提取文字和图片
   - **analyze_pdf_images.py**：分析PDF中的图片信息，用于调试
   - **check_gpu_pytorch.py**：检查GPU可用性，验证PyTorch配置

8. **venv/**：虚拟环境目录
   - 存放项目依赖和Python环境配置

## 技术栈

- **PDF 处理**：使用 Marker 工具进行 PDF 到 Markdown 的转换
- **依赖管理**：Python 包安装（pip）
- **GPU 加速**：PyTorch 与 CUDA

### 关于 Marker 工具

本项目使用 [Marker](https://github.com/VikParuchuri/marker) 工具进行 PDF 到 Markdown 的转换，这是一个功能强大的开源工具，能够高效地提取 PDF 文档中的文字和图片。

**Marker GitHub 主页**：[https://github.com/VikParuchuri/marker](https://github.com/VikParuchuri/marker)

**致谢**：

- 本项目对 Marker 团队及其社区贡献者表示诚挚的感谢，感谢他们开发和维护了如此优秀的 PDF 处理工具，为科研文献和专利的数字化处理提供了有力支持。
- 本项目对 Trae IDE 开发团队及其社区贡献者表示诚挚的感谢，特别是中文版 Trae IDE（https://www.trae.cn/），为项目的开发和使用提供了强大的集成环境支持。

## 许可证

本项目采用 MIT 许可证。

## 版本信息与项目进展

### 当前版本

- **版本号**：0.2.0
- **开发状态**：活跃开发中
- **主要功能**：
  - PDF 到结构化 Markdown 转换
  - HTML 网页文件处理
  - GitHub 仓库处理
  - 多源信息 Skill 提取

### 项目进展

本项目处于功能扩展阶段，核心功能已基本实现并持续完善：

- **技术实现**：PDF 处理、HTML 处理和 GitHub 仓库处理功能已实现
- **Skill 提取**：支持从科研文献、专利、GitHub 仓库和公众号文章中提取技能信息
- **系统集成**：相关工具和功能的集成工作正在有序推进
- **版本迭代**：从 0.1.0 版本扩展到 0.2.0 版本，增加了对 GitHub 仓库和公众号文章的支持

### 开发说明

- 项目采用模块化设计，便于后续功能扩展和优化
- 部分高级功能和专业领域的 Skill 处理可能会在后续版本中进一步完善
- 如需了解更多开发细节或讨论相关合作，可通过联系邮箱与作者沟通

**联系邮箱**：snowaker@zhuyintech.cn

## 公众号

关注我们的公众号获取更多信息：

### 咪噢喵

![公众号二维码](images/wechat_qrcode.png)

扫描上方二维码关注 "咪噢喵" 公众号，获取项目最新动态、技术分享和更多科研工具。