# 🚀 TraeAI 智能提示词集合

> **TraeAI Prompt Collection** - 专为Cursor、Trae、VS Code等IDE环境设计的智能代码分析提示词系统，支持自动环境检测、路径适配和规则同步。

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey.svg)](https://github.com/minshengzhong3-byte/ide-prompts-collection)
[![IDE Support](https://img.shields.io/badge/IDE-Cursor%20%7C%20Trae%20%7C%20VS%20Code-green.svg)](https://github.com/minshengzhong3-byte/ide-prompts-collection)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/minshengzhong3-byte/ide-prompts-collection/blob/main/LICENSE)

## ✨ **核心特性**

- 🔍 **自动IDE检测**：智能识别Cursor、Trae、VS Code等IDE环境
- 🎯 **固定路径适配**：为每个IDE创建专门的`project_rules.md`文件路径
- 🔄 **实时同步机制**：主规则文件更新时自动同步到所有IDE路径
- 🌍 **跨平台支持**：Windows、Linux、macOS全平台兼容
- 🧠 **分层规则体系**：核心基础层、研究类型层、阶段特定层
- 🎭 **身份切换机制**：代码分析师、架构师、代码审查员等角色
- 🛠️ **技术路径支持**：代码分析、静态审查、模式匹配等

## 🎯 **支持的IDE**

| IDE | 检测方式 | 固定路径 | 状态 |
|-----|----------|----------|------|
| **Cursor** | `.cursor/`目录 | `.cursor/project_rules.md` | ✅ 完全支持 |
| **Trae** | `.trae/`目录 | `.trae/project_rules.md` | ✅ 完全支持 |
| **VS Code** | `.vscode/`目录 | `.vscode/project_rules.md` | ✅ 完全支持 |

## 🚀 **快速开始**

### **1. 克隆项目**
```bash
git clone https://github.com/minshengzhong3-byte/ide-prompts-collection.git
cd ide-prompts-collection
```

### **2. 运行IDE检测（推荐）**

#### **Windows用户**
```bash
# 双击运行
tools/detect_ide.bat

# 或命令行运行
python tools/ide_detector.py
```

#### **Linux/macOS用户**
```bash
# 添加执行权限
chmod +x tools/detect_ide.sh

# 运行检测
./tools/detect_ide.sh

# 或直接运行Python脚本
python3 tools/ide_detector.py
```

### **3. 验证安装**
检测完成后，您应该能看到：
- `.cursor/project_rules.md` (Cursor IDE)
- `.trae/project_rules.md` (Trae IDE)  
- `.vscode/project_rules.md` (VS Code)

## 📁 **提示词集结构**

```
traeai-prompts/
├── 🧠 **核心基础层** (Core Layer)
│   ├── base_rules.md          # 基础规则和状态管理
│   ├── error_handling.md      # 错误处理和恢复机制
│   ├── tools_config.md        # 工具配置和集成
│   └── ide_adapter.md         # IDE环境适配器
│
├── 🎭 **身份专属层** (Identity Layer)
│   ├── code_analyst/          # 代码分析师提示词
│   ├── architect/             # 架构师提示词
│   ├── code_reviewer/         # 代码审查员提示词
│   ├── developer/             # 开发者提示词
│   └── qa/                    # 测试员提示词
│
├── 🛠️ **技术路径层** (Technical Path Layer)
│   ├── code_analysis/         # 代码分析路径
│   ├── static_review/         # 静态审查路径
│   └── pattern_matching/      # 模式匹配路径
│
└── 🔧 **工具集成层** (Tools Integration Layer)
    ├── ide_detector.py        # IDE检测器
    ├── detect_ide.bat         # Windows脚本
    └── detect_ide.sh          # Linux/macOS脚本
```

## 🧠 **提示词分类系统**

### **1. 核心基础层 (Core Layer)**
- **用途**：所有提示词的基础，必须继承
- **包含**：状态管理、流程控制、异常处理、IDE适配
- **特点**：通用性强，适用于所有项目

### **2. 身份专属层 (Identity Layer)**
- **用途**：根据不同角色提供专业提示词
- **包含**：代码分析师、架构师、代码审查员、开发者、测试员
- **特点**：角色专业化，任务导向

### **3. 技术路径层 (Technical Path Layer)**
- **用途**：根据技术需求选择合适的方法
- **包含**：代码分析、静态审查、模式匹配
- **特点**：技术专业化，方法导向

### **4. 工具集成层 (Tools Integration Layer)**
- **用途**：提供自动化工具和脚本
- **包含**：IDE检测、路径同步、状态监控
- **特点**：自动化程度高，易于集成

## 🔧 **使用方法**

### **自动同步**
- 系统会自动检测IDE环境
- 创建必要的配置目录和文件
- 同步主规则文件到所有IDE路径
- 生成检测报告和状态信息

### **手动同步**
```bash
# 手动运行IDE检测器
python tools/ide_detector.py

# 查看同步状态
cat trae_rules/ide_detection_report.json
```

### **身份切换**
系统支持多种身份角色：
- **🔍 代码分析师**：分析代码结构和逻辑
- **🎯 架构师**：设计解决方案和架构
- **🔧 代码审查员**：执行代码审查和静态分析
- **💻 开发者**：编写和修改代码
- **✅ 测试员**：验证代码功能和稳定性

## 📊 **技术特性**

### **IDE环境检测**
- 自动识别IDE类型和版本
- 检测配置文件位置
- 创建标准化路径结构

### **路径适配策略**
- 固定路径：每个IDE都有专门的配置路径
- 备用路径：提供多个备用路径确保兼容性
- 优先级策略：优先使用IDE原生路径

### **同步机制**
- 实时同步：主规则文件更新时自动同步
- 一致性保证：所有IDE路径保持规则文件一致
- 错误恢复：提供手动恢复和重试机制

## 🛠️ **系统要求**

- **Python**: 3.7 或更高版本
- **操作系统**: Windows 10+, Linux, macOS 10.14+
- **内存**: 建议 4GB 或更高
- **磁盘空间**: 至少 100MB 可用空间

## 📦 **安装依赖**

```bash
# 安装Python依赖
pip install -r requirements.txt

# 或使用conda
conda install --file requirements.txt
```

## 🔍 **故障排除**

### **常见问题**

#### **1. Python未安装**
```bash
# 下载安装Python
# https://www.python.org/downloads/
```

#### **2. 权限不足**
```bash
# Linux/macOS下添加执行权限
chmod +x tools/detect_ide.sh
```

#### **3. 路径创建失败**
```bash
# 检查磁盘空间
# 检查目录权限
# 手动创建目录
mkdir -p .cursor .trae .vscode
```

### **手动恢复**
```bash
# 1. 检查主规则文件
cat trae_rules/project_rules.md

# 2. 手动创建IDE目录
mkdir -p .cursor .trae .vscode

# 3. 复制规则文件
cp trae_rules/project_rules.md .cursor/
cp trae_rules/project_rules.md .trae/
cp trae_rules/project_rules.md .vscode/
```

## 📈 **性能优化**

### **建议配置**
- 使用SSD存储提高文件同步速度
- 定期清理临时文件和缓存
- 监控磁盘空间使用情况
- 优化文件监听器配置

### **监控指标**
- IDE检测响应时间
- 文件同步速度
- 路径一致性状态
- 错误率和重试次数

## 🤝 **贡献指南**

我们欢迎所有形式的贡献！请查看 [CONTRIBUTING.md](CONTRIBUTING.md) 了解详情。

### **如何贡献**
1. Fork 这个项目
2. 创建您的特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交您的更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 打开一个 Pull Request

### **贡献类型**
- 🐛 Bug 修复
- ✨ 新功能
- 📚 文档改进
- 🎨 代码优化
- 🧪 测试用例

## 📄 **许可证**

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。

## 🙏 **致谢**

- 感谢所有贡献者的支持
- 感谢开源社区的力量
- 特别感谢 Cursor、Trae、VS Code 等IDE团队

## 📞 **联系我们**

- **GitHub Issues**: [报告问题](https://github.com/minshengzhong3-byte/ide-prompts-collection/issues)
- **GitHub Discussions**: [参与讨论](https://github.com/minshengzhong3-byte/ide-prompts-collection/discussions)
- **Email**: minshengzhong3@gmail.com

## 🌟 **Star History**

如果这个项目对您有帮助，请给我们一个 ⭐️ Star！

---

**让AI编程更智能，让开发更高效！** 🚀

*此项目由智能协调AI自动生成和维护*