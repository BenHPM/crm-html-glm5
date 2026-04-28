#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
使用Node.js svgexport将SVG转换为PNG
"""

import subprocess
import os
import sys

def convert_svg_to_png():
    svg_file = 'avatar-pm-ai-opensource.svg'
    sizes = [512, 256, 128, 64, 32]
    
    if not os.path.exists(svg_file):
        print(f'❌ 文件不存在: {svg_file}')
        return
    
    print('🔄 开始转换SVG到PNG...\n')
    
    for size in sizes:
        output_file = f'avatar-pm-ai-opensource-{size}x{size}.png'
        try:
            subprocess.run(
                ['svgexport', svg_file, output_file, f'{size}:{size}'],
                check=True,
                capture_output=True,
                text=True
            )
            print(f'✓ 已生成: {output_file}')
        except Exception as e:
            print(f'❌ 生成 {output_file} 失败: {e}')
    
    # 生成主文件
    try:
        subprocess.run(
            ['svgexport', svg_file, 'avatar-pm-ai-opensource.png', '512:512'],
            check=True,
            capture_output=True,
            text=True
        )
        print(f'✓ 已生成: avatar-pm-ai-opensource.png')
    except Exception as e:
        print(f'❌ 生成主文件失败: {e}')
    
    print('\n🎉 所有PNG格式头像已生成完成！')

if __name__ == '__main__':
    convert_svg_to_png()
