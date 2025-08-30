@echo off
chcp 65001 >nul
echo.
echo ========================================
echo    IDE环境检测和同步工具
echo ========================================
echo.

REM 检查Python是否安装
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ 错误：未检测到Python，请先安装Python
    echo 下载地址：https://www.python.org/downloads/
    pause
    exit /b 1
)

echo ✅ Python已安装
echo.

REM 运行IDE检测
echo 🚀 开始检测IDE环境...
python tools/ide_detector.py

echo.
echo ========================================
echo    检测完成！
echo ========================================
echo.
echo 如果检测成功，您应该能看到：
echo - .cursor/project_rules.md (Cursor IDE)
echo - .trae/project_rules.md (Trae IDE)  
echo - .vscode/project_rules.md (VS Code)
echo.
pause