#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
IDE环境检测和路径同步工具
自动检测Cursor、Trae、VS Code等IDE环境
并同步project rules文件到相应的固定路径
"""

import os
import shutil
import json
import time
from pathlib import Path
from typing import Dict, List, Optional

class IDEDetector:
    """IDE环境检测器"""
    
    def __init__(self, project_root: str):
        self.project_root = Path(project_root)
        self.ide_configs = {
            'cursor': {
                'name': 'Cursor',
                'paths': ['.cursor/project_rules.md', 'project_rules.md'],
                'config_files': ['.cursor/settings.json', 'cursor.json'],
                'detected': False,
                'active_path': None
            },
            'trae': {
                'name': 'Trae',
                'paths': ['.trae/project_rules.md', 'trae_rules/project_rules.md'],
                'config_files': ['trae.json', '.trae/config.json'],
                'detected': False,
                'active_path': None
            },
            'vscode': {
                'name': 'VS Code',
                'paths': ['.vscode/project_rules.md', 'project_rules.md'],
                'config_files': ['.vscode/settings.json', '.vscode/extensions.json'],
                'detected': False,
                'active_path': None
            }
        }
        self.main_rules_file = 'trae_rules/project_rules.md'
        
    def detect_ide_environment(self) -> Dict[str, bool]:
        """检测IDE环境"""
        print("🔍 开始检测IDE环境...")
        
        for ide_key, ide_info in self.ide_configs.items():
            # 检查配置文件
            for config_file in ide_info['config_files']:
                if (self.project_root / config_file).exists():
                    ide_info['detected'] = True
                    print(f"✅ 检测到 {ide_info['name']} 配置文件: {config_file}")
                    break
            
            # 检查project rules路径
            for path in ide_info['paths']:
                if (self.project_root / path).exists():
                    ide_info['active_path'] = path
                    print(f"📍 {ide_info['name']} 使用路径: {path}")
                    break
            
            if not ide_info['active_path']:
                # 创建默认路径
                default_path = ide_info['paths'][0]
                ide_info['active_path'] = default_path
                print(f"📁 为 {ide_info['name']} 创建默认路径: {default_path}")
        
        return {ide: info['detected'] for ide, info in self.ide_configs.items()}
    
    def create_ide_directories(self):
        """创建IDE配置目录"""
        print("📁 创建IDE配置目录...")
        
        for ide_key, ide_info in self.ide_configs.items():
            if ide_info['active_path']:
                path = Path(ide_info['active_path'])
                path.parent.mkdir(parents=True, exist_ok=True)
                print(f"✅ 创建目录: {path.parent}")
    
    def sync_project_rules(self):
        """同步project rules文件到所有IDE路径"""
        print("🔄 开始同步project rules文件...")
        
        main_file = self.project_root / self.main_rules_file
        if not main_file.exists():
            print(f"❌ 主规则文件不存在: {self.main_rules_file}")
            return False
        
        # 读取主规则文件内容
        with open(main_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 同步到所有IDE路径
        for ide_key, ide_info in self.ide_configs.items():
            if ide_info['active_path']:
                target_file = self.project_root / ide_info['active_path']
                
                # 更新IDE特定的头部信息
                ide_content = self._update_ide_header(content, ide_info)
                
                # 写入文件
                with open(target_file, 'w', encoding='utf-8') as f:
                    f.write(ide_content)
                
                print(f"✅ 同步到 {ide_info['name']}: {ide_info['active_path']}")
        
        return True
    
    def _update_ide_header(self, content: str, ide_info: Dict) -> str:
        """更新IDE特定的头部信息"""
        lines = content.split('\n')
        updated_lines = []
        
        # 检查是否已经有IDE类型行
        has_ide_type = any('**IDE类型：**' in line for line in lines)
        
        for i, line in enumerate(lines):
            if line.startswith('# '):
                # 更新标题
                updated_lines.append(f'# {ide_info["name"]} 项目规则文件')
            elif line.startswith('**IDE类型：**'):
                updated_lines.append(f'**IDE类型：** {ide_info["name"]}')
            elif line.startswith('**配置文件路径：**'):
                updated_lines.append(f'**配置文件路径：** `{ide_info["active_path"]}`')
            elif line.startswith('**更新时间：**'):
                updated_lines.append(f'**更新时间：** {time.strftime("%Y-%m-%d %H:%M")}')
            elif not has_ide_type and line.startswith('**更新时间：**'):
                # 如果没有IDE类型行，在更新时间后添加
                updated_lines.append(line)
                updated_lines.append(f'**IDE类型：** {ide_info["name"]}')
                updated_lines.append(f'**配置文件路径：** `{ide_info["active_path"]}`')
            else:
                updated_lines.append(line)
        
        return '\n'.join(updated_lines)
    
    def run_full_detection(self):
        """运行完整的检测和同步流程"""
        print("🚀 开始IDE环境检测和同步...")
        print("=" * 50)
        
        # 1. 检测IDE环境
        detection_results = self.detect_ide_environment()
        
        # 2. 创建目录
        self.create_ide_directories()
        
        # 3. 同步规则文件
        sync_success = self.sync_project_rules()
        
        # 4. 生成报告
        report = self.generate_status_report()
        
        print("=" * 50)
        print("📊 检测完成！状态报告：")
        print(json.dumps(report, indent=2, ensure_ascii=False))
        
        return report
    
    def generate_status_report(self) -> Dict:
        """生成状态报告"""
        report = {
            'timestamp': time.strftime("%Y-%m-%d %H:%M:%S"),
            'project_root': str(self.project_root),
            'main_rules_file': self.main_rules_file,
            'ide_environments': {},
            'sync_status': 'completed'
        }
        
        for ide_key, ide_info in self.ide_configs.items():
            report['ide_environments'][ide_key] = {
                'name': ide_info['name'],
                'detected': ide_info['detected'],
                'active_path': ide_info['active_path'],
                'exists': (self.project_root / ide_info['active_path']).exists() if ide_info['active_path'] else False
            }
        
        return report

def main():
    """主函数"""
    project_root = os.getcwd()
    detector = IDEDetector(project_root)
    
    try:
        report = detector.run_full_detection()
        print(f"📄 检测完成！")
        
    except Exception as e:
        print(f"❌ 检测过程中出现错误: {e}")
        return False
    
    return True

if __name__ == "__main__":
    main()