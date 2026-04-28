#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SVG转PNG格式转换脚本
将产品经理AI开源头像转换为多种尺寸的PNG格式
"""

import cairosvg
import os

def convert_svg_to_png(svg_file, output_dir):
    """
    将SVG文件转换为多种尺寸的PNG格式
    
    Args:
        svg_file: 输入的SVG文件路径
        output_dir: 输出目录
    """
    sizes = [512, 256, 128, 64, 32]
    
    for size in sizes:
        output_file = os.path.join(output_dir, f'avatar-pm-ai-opensource-{size}x{size}.png')
        cairosvg.svg2png(
            url=svg_file,
            write_to=output_file,
            output_width=size,
            output_height=size
        )
        print(f'✓ 已生成: {output_file}')

    main_output = os.path.join(output_dir, 'avatar-pm-ai-opensource.png')
    cairosvg.svg2png(
        url=svg_file,
        write_to=main_output,
        output_width=512,
        output_height=512
    )
    print(f'✓ 已生成: {main_output}')

if __name__ == '__main__':
    svg_path = 'avatar-pm-ai-opensource.svg'
    output_directory = '.'
    convert_svg_to_png(svg_path, output_directory)
    print('\n🎉 所有PNG格式头像已生成完成！')
