#!/bin/bash

# 颜色定义
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}"
echo "========================================"
echo "    IDE环境检测和同步工具"
echo "========================================"
echo -e "${NC}"

# 检查Python是否安装
if ! command -v python3 &> /dev/null; then
    if ! command -v python &> /dev/null; then
        echo -e "${RED}❌ 错误：未检测到Python，请先安装Python${NC}"
        echo "下载地址：https://www.python.org/downloads/"
        exit 1
    else
        PYTHON_CMD="python"
    fi
else
    PYTHON_CMD="python3"
fi

echo -e "${GREEN}✅ Python已安装${NC}"
echo

# 运行IDE检测
echo -e "${YELLOW}🚀 开始检测IDE环境...${NC}"
$PYTHON_CMD tools/ide_detector.py

echo
echo -e "${BLUE}========================================"
echo "    检测完成！"
echo "========================================"
echo -e "${NC}"
echo "如果检测成功，您应该能看到："
echo -e "${GREEN}- .cursor/project_rules.md (Cursor IDE)${NC}"
echo -e "${GREEN}- .trae/project_rules.md (Trae IDE)${NC}"
echo -e "${GREEN}- .vscode/project_rules.md (VS Code)${NC}"
echo