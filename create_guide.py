#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
使用Pillow转换PNG - 基础版本
由于SVG渲染需要Cairo库，我们创建一个HTML预览页面提供在线转换
"""

def create_download_html():
    html_content = '''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>SVG转PNG工具</title>
    <style>
        body { 
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
            max-width: 800px; 
            margin: 50px auto; 
            padding: 20px;
            background: #f5f5f5;
        }
        .container {
            background: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        h1 { color: #333; }
        .info {
            background: #e3f2fd;
            padding: 15px;
            border-radius: 5px;
            margin: 20px 0;
        }
        .svg-preview {
            text-align: center;
            margin: 20px 0;
        }
        .svg-preview img {
            max-width: 256px;
            border-radius: 50%;
            box-shadow: 0 4px 20px rgba(0,0,0,0.2);
        }
        .download-links {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 15px;
            margin: 20px 0;
        }
        .download-btn {
            display: block;
            padding: 15px 20px;
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
            text-decoration: none;
            border-radius: 8px;
            text-align: center;
            transition: transform 0.2s;
        }
        .download-btn:hover {
            transform: translateY(-2px);
        }
        .tool-list {
            margin-top: 30px;
            padding: 20px;
            background: #f9f9f9;
            border-radius: 8px;
        }
        .tool-list h3 { margin-top: 0; }
        .tool-list ul { padding-left: 20px; }
        .tool-list li { margin: 10px 0; }
        code {
            background: #eee;
            padding: 2px 6px;
            border-radius: 3px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🎨 产品经理AI开源头像</h1>
        
        <div class="svg-preview">
            <img src="avatar-pm-ai-opensource.svg" alt="头像预览">
        </div>
        
        <h2>📥 下载PNG格式</h2>
        <p>由于环境限制，请使用以下方法转换为PNG：</p>
        
        <div class="tool-list">
            <h3>方法1：在线转换工具</h3>
            <ul>
                <li><a href="https://svgtopng.com" target="_blank">svgtopng.com</a> - 快速在线转换</li>
                <li><a href="https://convertio.co/svg-png/" target="_blank">convertio.co</a> - 支持批量转换</li>
                <li><a href="https://onlineconvertfree.com/convert/svg-to-png/" target="_blank">onlineconvertfree</a></li>
            </ul>
            
            <h3>方法2：本地工具转换</h3>
            <ul>
                <li><strong>Windows:</strong> 安装 <a href="https://inkscape.org" target="_blank">Inkscape</a>，打开SVG文件另存为PNG</li>
                <li><strong>VS Code:</strong> 安装 "SVG to PNG" 扩展</li>
                <li><strong>命令行:</strong> <code>npm install -g svgexport && svgexport input.svg output.png 512:512</code></li>
            </ul>
            
            <h3>方法3：浏览器转换</h3>
            <ul>
                <li>用浏览器打开 avatar-pm-ai-opensource.svg</li>
                <li>右键选择 "另存为" → 选择位置后输入文件名加 .png 后缀</li>
                <li>或者使用截图工具截取需要的尺寸</li>
            </ul>
        </div>
        
        <div class="info">
            <strong>💡 提示：</strong> SVG是矢量格式，可以在任何尺寸下保持清晰。
            建议直接使用SVG格式，在需要时再转换为PNG。
        </div>
        
        <h2>📁 文件说明</h2>
        <ul>
            <li><strong>avatar-pm-ai-opensource.svg</strong> - 矢量格式，推荐使用</li>
            <li><strong>avatar-pm-ai-opensource-512x512.png</strong> - 大尺寸头像</li>
            <li><strong>avatar-pm-ai-opensource-256x256.png</strong> - 标准头像</li>
            <li><strong>avatar-pm-ai-opensource-128x128.png</strong> - 列表头像</li>
            <li><strong>avatar-pm-ai-opensource-64x64.png</strong> - 小图标</li>
            <li><strong>avatar-pm-ai-opensource-32x32.png</strong> - 迷你图标</li>
        </ul>
    </div>
</body>
</html>'''
    
    with open('svg_to_png_guide.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    print('✓ 转换指南页面已创建: svg_to_png_guide.html')

if __name__ == '__main__':
    create_download_html()
