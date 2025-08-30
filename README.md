# 🚀 TraeAI智能提示词集

> 专为Cursor、Trae、VS Code等IDE环境设计的智能代码分析提示词系统，支持自动环境检测、路径适配和规则同步。

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey.svg)](https://github.com/minshengzhong3-byte/ide-prompts-collection)
[![IDE Support](https://img.shields.io/badge/IDE-Cursor%20%7C%20Trae%20%7C%20VS%20Code-green.svg)](https://github.com/minshengzhong3-byte/ide-prompts-collection)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/minshengzhong3-byte/ide-prompts-collection/blob/main/LICENSE)

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

## 📚 **提示词集分类**

### **🔧 核心基础层 (Core Layer)**
- **base_rules.md** - 基础行为规则和状态管理
- **error_handling.md** - 错误处理和恢复机制
- **tools_config.md** - 工具配置和集成指南
- **ide_adapter.md** - IDE环境检测和路径适配

### **🎭 身份专属层 (Identity Layer)**
- **code_analyst/** - 代码分析师提示词集
- **architect/** - 架构师提示词集
- **code_reviewer/** - 代码审查员提示词集
- **developer/** - 开发者提示词集
- **qa/** - 测试员提示词集

### **🛠️ 技术路径层 (Technical Path Layer)**
- **code_analysis/** - 代码分析技术路径
- **static_review/** - 静态审查技术路径
- **pattern_matching/** - 模式匹配技术路径
- **general_research/** - 通用研究技术路径

### **📋 阶段特定层 (Stage Specific Layer)**
- **analysis/** - 分析阶段提示词
- **design/** - 设计阶段提示词
- **implementation/** - 实现阶段提示词
- **testing/** - 测试阶段提示词
- **deployment/** - 部署阶段提示词

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

## 🔍 **智能拉取指南**

### **按功能拉取**
```bash
# 拉取代码分析相关提示词
git clone https://github.com/minshengzhong3-byte/ide-prompts-collection.git
cp -r ide-prompts-collection/trae_prompt_sets/code_analysis/ your-project/
cp -r ide-prompts-collection/trae_prompt_sets/identities/code_analyst/ your-project/
```

### **按身份拉取**
```bash
# 拉取架构师相关提示词
cp -r ide-prompts-collection/trae_prompt_sets/identities/architect/ your-project/
cp -r ide-prompts-collection/trae_prompt_sets/technical_paths/ your-project/
```

### **按阶段拉取**
```bash
# 拉取设计阶段提示词
cp -r ide-prompts-collection/trae_prompt_sets/stages/design/ your-project/
cp -r ide-prompts-collection/trae_prompt_sets/identities/architect/ your-project/
```

## 📁 **项目结构**

```
ide-prompts-collection/
├── .cursor/                       # Cursor IDE配置
│   └── project_rules.md          # Cursor固定规则文件
├── .trae/                        # Trae IDE配置
│   └── project_rules.md          # Trae固定规则文件
├── .vscode/                      # VS Code兼容配置
│   └── project_rules.md          # VS Code规则文件
├── trae_rules/                   # 项目规则管理
│   ├── project_rules.md          # 主规则文件
│   ├── last_status.json          # 状态备份
│   └── ide_detection_report.json # IDE检测报告
├── trae_prompt_sets/             # 提示词集
│   ├── core/                     # 核心基础层
│   │   ├── base_rules.md         # 基础规则
│   │   ├── error_handling.md     # 错误处理
│   │   ├── tools_config.md       # 工具配置
│   │   └── ide_adapter.md        # IDE适配器
│   ├── identities/               # 身份专属层
│   │   ├── code_analyst/         # 代码分析师
│   │   ├── architect/            # 架构师
│   │   ├── code_reviewer/        # 代码审查员
│   │   ├── developer/            # 开发者
│   │   └── qa/                   # 测试员
│   ├── technical_paths/          # 技术路径层
│   │   ├── code_analysis/        # 代码分析路径
│   │   ├── static_review/        # 静态审查路径
│   │   ├── pattern_matching/     # 模式匹配路径
│   │   └── general_research/     # 通用研究路径
│   └── stages/                   # 阶段特定层
│       ├── analysis/             # 分析阶段
│       ├── design/               # 设计阶段
│       ├── implementation/       # 实现阶段
│       ├── testing/              # 测试阶段
│       └── deployment/           # 部署阶段
├── tools/                        # 工具集
│   ├── ide_detector.py           # IDE检测器
│   ├── detect_ide.bat            # Windows检测脚本
│   ├── detect_ide.sh             # Linux/macOS检测脚本
│   ├── deploy.py                 # 部署工具
│   ├── setup.bat                 # Windows安装脚本
│   ├── setup.sh                  # Linux/macOS安装脚本
│   └── validate.py               # 验证工具
├── config/                       # 配置文件
│   ├── ide_setup/                # IDE设置
│   └── language_support/         # 语言支持
├── examples/                     # 使用示例
├── templates/                    # 模板文件
├── docs/                         # 详细文档
├── deploy.bat                    # Windows一键部署
├── deploy.sh                     # Linux/macOS一键部署
├── requirements.txt              # Python依赖
└── README.md                     # 项目说明
```

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

*此项目由TraeAI智能协调系统自动生成和维护*