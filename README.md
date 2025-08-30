# 🚀 IDE智能代码分析提示词集

> 专为Cursor、Trae、VS Code等IDE环境设计的智能代码分析提示词系统，支持自动环境检测、路径适配和规则同步。

## ✨ **核心特性**

- 🔍 **自动IDE检测**：智能识别Cursor、Trae、VS Code等IDE环境
- 🎯 **固定路径适配**：为每个IDE创建专门的`project_rules.md`文件路径
- 🔄 **实时同步机制**：主规则文件更新时自动同步到所有IDE路径
- 🌍 **跨平台支持**：Windows、Linux、macOS全平台兼容

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

### **2. 运行IDE检测**
```bash
# Windows用户
tools/detect_ide.bat

# Linux/macOS用户
./tools/detect_ide.sh
```

## 📁 **项目结构**

```
ide-prompts-collection/
├── .cursor/                       # Cursor IDE配置
├── .trae/                        # Trae IDE配置
├── .vscode/                      # VS Code兼容配置
├── trae_rules/                   # 项目规则管理
├── trae_prompt_sets/             # 提示词集
├── tools/                        # 工具集
└── config/                       # 配置文件
```

## 🤝 **贡献指南**

我们欢迎所有形式的贡献！请查看 [CONTRIBUTING.md](CONTRIBUTING.md) 了解详情。

## 📄 **许可证**

本项目采用 MIT 许可证。

---

**让AI编程更智能，让开发更高效！** 🚀