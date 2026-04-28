#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
使用svglib将SVG转换为PNG
"""

from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF, renderPM
import os

def convert_svg_to_png(svg_file, output_dir):
    sizes = [512, 256, 128, 64, 32]
    
    drawing = svg2rlg(svg_file)
    
    if drawing:
        for size in sizes:
            output_file = os.path.join(output_dir, f'avatar-pm-ai-opensource-{size}x{size}.png')
            renderPM.drawToFile(drawing, output_file, fmt='PNG', width=size, height=size)
            print(f'✓ 已生成: {output_file}')
        
        main_output = os.path.join(output_dir, 'avatar-pm-ai-opensource.png')
        renderPM.drawToFile(drawing, main_output, fmt='PNG', width=512, height=512)
        print(f'✓ 已生成: {main_output}')
        print('\n🎉 所有PNG格式头像已生成完成！')
    else:
        print('❌ SVG文件加载失败')

if __name__ == '__main__':
    svg_path = 'avatar-pm-ai-opensource.svg'
    output_directory = '.'
    convert_svg_to_png(svg_path, output_directory)
