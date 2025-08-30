# 核心基础层提示词 - 工具配置

**文件类型：** 核心基础层
**用途：** 工具配置和集成指南
**继承：** 必须继承

## 🎯 **代码质量工具**

### **JavaScript/TypeScript**
- **ESLint**：代码质量检查
- **Prettier**：代码格式化
- **TypeScript**：类型检查
- **Jest**：单元测试
- **Webpack**：模块打包

### **Python**
- **Pylint**：代码质量检查
- **Black**：代码格式化
- **MyPy**：类型检查
- **Pytest**：单元测试
- **Flake8**：代码风格检查

### **Java**
- **Checkstyle**：代码风格检查
- **PMD**：代码质量分析
- **SpotBugs**：Bug检测
- **JUnit**：单元测试
- **Maven/Gradle**：构建工具

## 🔧 **安全扫描工具**

### **依赖扫描**
- **npm audit**：Node.js依赖漏洞扫描
- **pip-audit**：Python依赖漏洞扫描
- **OWASP Dependency Check**：Java依赖漏洞扫描
- **Snyk**：多语言依赖漏洞扫描

### **代码安全**
- **Bandit**：Python安全漏洞检测
- **ESLint Security**：JavaScript安全规则
- **SpotBugs Security**：Java安全漏洞检测
- **SonarQube**：综合代码质量分析

## 📊 **性能分析工具**

### **内存分析**
- **Valgrind**：内存泄漏检测
- **Python Memory Profiler**：Python内存分析
- **Chrome DevTools**：JavaScript内存分析
- **JProfiler**：Java性能分析

### **性能监控**
- **cProfile**：Python性能分析
- **Node.js Profiler**：JavaScript性能分析
- **JProfiler**：Java性能分析
- **Visual Studio Profiler**：C++性能分析

## 🎨 **重构工具**

### **代码重构**
- **VS Code Refactor**：多语言重构支持
- **IntelliJ IDEA**：Java重构工具
- **PyCharm**：Python重构工具
- **WebStorm**：JavaScript重构工具

### **模式识别**
- **SonarQube**：代码异味检测
- **PMD**：设计模式识别
- **ESLint**：代码模式检查
- **Pylint**：Python代码模式

## 📋 **配置示例**

### **ESLint配置**
```javascript
module.exports = {
  extends: ['eslint:recommended'],
  rules: {
    'no-console': 'warn',
    'no-unused-vars': 'error',
    'prefer-const': 'error'
  }
};
```

### **Pylint配置**
```ini
[MASTER]
disable=all

[MESSAGES CONTROL]
enable=C0111,C0103,C0303,W0611

[FORMAT]
max-line-length=100
```

### **Checkstyle配置**
```xml
<module name="Checker">
  <module name="TreeWalker">
    <module name="AvoidStarImport"/>
    <module name="OneTopLevelClass"/>
  </module>
</module>
```

## ⚙️ **集成配置**

### **IDE集成**
- **VS Code**：扩展配置和设置
- **IntelliJ IDEA**：插件配置
- **Eclipse**：插件和首选项
- **Vim/Emacs**：插件配置

### **CI/CD集成**
- **GitHub Actions**：工作流配置
- **Jenkins**：流水线配置
- **GitLab CI**：配置文件
- **Travis CI**：构建配置

## 🚀 **工具安装**

### **Node.js工具**
```bash
npm install -g eslint prettier typescript jest
```

### **Python工具**
```bash
pip install pylint black mypy pytest flake8
```

### **Java工具**
```bash
# 通过Maven安装
mvn dependency:resolve

# 通过Gradle安装
gradle dependencies
```

## ⚠️ **注意事项**

### **版本兼容性**
- 确保工具版本兼容
- 定期更新工具版本
- 测试新版本兼容性
- 保持配置一致性

### **性能影响**
- 监控工具执行时间
- 优化工具配置
- 避免重复检查
- 合理设置检查范围

### **配置管理**
- 版本控制配置文件
- 环境特定配置
- 团队配置标准
- 配置文档维护

## 🚀 **现在开始执行**

**[状态] 工具配置系统初始化 | 任务: 配置开发工具，建立代码质量检查体系**

---
*此文件是工具配置的核心提示词，确保所有工具正确配置和集成*