# 工具配置核心提示词

**文件类型：** 核心基础层
**用途：** 工具配置、集成管理、最佳实践
**继承：** 必须继承
**版本：** 1.0.0

## 🎯 **核心功能**

### **代码质量工具**
- **ESLint**: JavaScript/TypeScript代码检查
- **Pylint**: Python代码质量分析
- **Checkstyle**: Java代码规范检查
- **PMD**: Java代码质量分析

### **代码格式化工具**
- **Prettier**: JavaScript/TypeScript格式化
- **Black**: Python代码格式化
- **Checkstyle**: Java代码格式化
- **clang-format**: C/C++代码格式化

### **类型检查工具**
- **TypeScript**: JavaScript类型检查
- **MyPy**: Python类型检查
- **Checkstyle**: Java类型检查

## 🔧 **配置管理**

### **ESLint配置**
```javascript
// .eslintrc.js
module.exports = {
  extends: ['eslint:recommended', '@typescript-eslint/recommended'],
  rules: {
    'no-unused-vars': 'error',
    'no-console': 'warn',
    'prefer-const': 'error'
  }
};
```

### **Pylint配置**
```ini
# .pylintrc
[MASTER]
disable=
    C0111, # missing-docstring
    C0103, # invalid-name
    C0303, # trailing-whitespace

[MESSAGES CONTROL]
disable=
    C0111, # missing-docstring
    C0103, # invalid-name
```

### **Checkstyle配置**
```xml
<!-- checkstyle.xml -->
<module name="Checker">
  <module name="TreeWalker">
    <module name="AvoidStarImport"/>
    <module name="OneTopLevelClass"/>
    <module name="NoLineWrap"/>
  </module>
</module>
```

## 📋 **必须执行的任务**

### **工具安装任务**
- [ ] 检查工具是否已安装
- [ ] 安装缺失的工具
- [ ] 验证工具版本
- [ ] 配置工具环境

### **配置验证任务**
- [ ] 验证配置文件格式
- [ ] 测试工具功能
- [ ] 检查规则设置
- [ ] 验证集成状态

### **最佳实践任务**
- [ ] 应用推荐规则
- [ ] 自定义项目规则
- [ ] 配置忽略文件
- [ ] 设置预提交钩子

## ⚠️ **注意事项**

### **工具选择原则**
- 选择成熟稳定的工具
- 考虑项目技术栈
- 评估工具性能影响
- 确保工具兼容性

### **配置管理原则**
- 使用版本控制管理配置
- 提供配置模板和示例
- 支持环境特定配置
- 定期更新配置规则

### **集成最佳实践**
- 集成到CI/CD流程
- 配置编辑器插件
- 设置预提交检查
- 提供配置文档

## 🚀 **现在开始执行**

**[状态] 工具配置系统初始化 | 任务: 检测工具环境，配置代码质量工具，验证集成状态**

---
*此文件是工具配置的核心提示词，必须被所有其他提示词继承*