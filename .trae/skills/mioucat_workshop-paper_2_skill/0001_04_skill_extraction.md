# Skill 提取

## 1. 准备工作

### 1.1 激活虚拟环境

确保在执行任何操作前，虚拟环境已激活：

```powershell
# 激活虚拟环境
venv\Scripts\activate
```

### 1.2 准备处理后的文档

确保 LLM 处理后的文档已准备就绪：

```powershell
# 查看 LLM 处理后的文档
Get-ChildItem -Path "llm_processed" -Recurse
```

## 2. Skill 提取流程

### 2.1 提取关键知识点

从处理后的 Markdown 文档中提取关键知识点和技能点：

1. **研究背景**：提取研究的背景和动机
2. **研究问题**：提取研究解决的核心问题
3. **研究方法**：提取研究使用的方法和技术
4. **实验设计**：提取实验设计和流程
5. **关键发现**：提取研究的主要发现和结果
6. **创新点**：提取研究的创新之处
7. **技术应用**：提取技术的应用场景和潜力
8. **局限性**：提取研究的局限性
9. **未来方向**：提取研究建议的未来研究方向

### 2.2 按不同角度提取

#### 2.2.1 按研究主题提取

- 识别论文的主要研究主题
- 提取与主题相关的所有知识点
- 组织成主题相关的 skill 集合

#### 2.2.2 按研究方法提取

- 识别论文使用的主要研究方法
- 提取方法的原理、步骤和应用
- 组织成方法相关的 skill 集合

#### 2.2.3 按技术应用提取

- 识别论文中涉及的技术和应用
- 提取技术的原理、实现和应用场景
- 组织成技术相关的 skill 集合

#### 2.2.4 按期刊分类提取

- 根据论文发表的期刊特点
- 提取符合期刊风格和要求的知识点
- 组织成期刊相关的 skill 集合

## 3. Skill 组织

### 3.1 创建 paper_skills 目录

```powershell
# 创建 paper_skills 目录
New-Item -ItemType Directory -Path "paper_skills" -Force
```

### 3.2 按分类方式组织

#### 3.2.1 按主题分类

```powershell
# 创建主题分类目录
New-Item -ItemType Directory -Path "paper_skills\by_topic" -Force

# 创建具体主题目录
New-Item -ItemType Directory -Path "paper_skills\by_topic\single_cell_analysis" -Force
```

#### 3.2.2 按方法分类

```powershell
# 创建方法分类目录
New-Item -ItemType Directory -Path "paper_skills\by_method" -Force

# 创建具体方法目录
New-Item -ItemType Directory -Path "paper_skills\by_method\machine_learning" -Force
```

#### 3.2.3 按期刊分类

```powershell
# 创建期刊分类目录
New-Item -ItemType Directory -Path "paper_skills\by_journal" -Force

# 创建具体期刊目录
New-Item -ItemType Directory -Path "paper_skills\by_journal\Nature" -Force
```

### 3.3 Skill 文档结构

每个 skill 文档应包含以下结构：

```markdown
# [Skill 标题]

## 1. 概述

[Skill 的简要介绍和目的]

## 2. 核心内容

[Skill 的详细内容]

## 3. 应用场景

[Skill 的应用场景和示例]

## 4. 相关技能

[与本 Skill 相关的其他技能]

## 5. 参考文献

[参考的原始论文]
```

## 4. 提取结果存储

### 4.1 结果结构

提取后的 skill 存储结构示例：

```
paper_skills/
├── by_topic/
│   └── single_cell_analysis/
│       ├── topic_overview.md
│       └── paper_1_skill.md
├── by_method/
│   └── machine_learning/
│       ├── method_overview.md
│       └── paper_1_skill.md
└── by_journal/
    └── Nature/
        ├── journal_overview.md
        └── paper_1_skill.md
```

### 4.2 总领性文件

为每个分类创建总领性文件，提供该分类的概述和索引：

```powershell
# 创建主题总领性文件
New-Item -ItemType File -Path "paper_skills\by_topic\single_cell_analysis\topic_overview.md" -Force
```

## 5. 质量检查

### 5.1 检查提取完整性

- 确保所有关键知识点都已提取
- 检查是否有遗漏的重要内容
- 确保提取的内容准确反映原始论文

### 5.2 检查组织合理性

- 确保 skill 组织逻辑清晰
- 检查分类方式是否合理
- 确保文档结构一致

### 5.3 检查引用正确性

- 确保 skill 文档正确引用原始论文
- 检查引用格式是否规范
- 确保引用链接可访问

## 6. 常见问题

### 6.1 提取不完整

**问题**：Skill 提取不完整

**解决方案**：
```powershell
# 重新阅读原始论文
# 确保理解论文的全部内容

# 使用结构化模板
# 按照模板逐一提取每个部分

# 多人审核
# 由多人分别提取，然后合并结果
```

### 6.2 组织不合理

**问题**：Skill 组织不合理

**解决方案**：
```powershell
# 重新评估分类方式
# 选择更适合的分类标准

# 调整目录结构
# 根据实际情况调整目录结构

# 参考其他论文的组织方式
# 参考已有的组织良好的 skill 文档
```

### 6.3 质量不一致

**问题**：不同论文的 skill 质量不一致

**解决方案**：
```powershell
# 制定提取标准
# 创建统一的提取标准和模板

# 培训提取人员
# 确保提取人员理解标准和要求

# 定期审核
# 定期审核提取结果，确保质量一致
```

## 7. 性能优化

### 7.1 批量提取

对于多个文档，可以批量进行 Skill 提取，提高效率。

### 7.2 模板化提取

创建标准化的提取模板，提高提取速度和一致性。

### 7.3 自动化辅助

开发自动化工具辅助提取过程，减少手动工作。

## 8. 后续步骤

Skill 提取和组织完成后，可以：

1. **技能关联**：建立不同技能之间的关联
2. **技能评估**：评估技能的重要性和实用性
3. **技能更新**：定期更新技能内容，保持时效性
4. **技能应用**：将技能应用到实际问题中

## 9. 预留扩展

### 9.1 技能图谱

未来可以开发技能图谱，展示技能之间的关系和层次结构。

### 9.2 技能推荐

可以开发技能推荐系统，根据用户需求推荐相关技能。

### 9.3 技能评估

可以开发技能评估体系，评估技能的质量和实用性。