#!/usr/bin/env node
/**
 * SVG转PNG转换脚本
 * 使用sharp库将产品经理AI开源头像转换为多种尺寸的PNG格式
 */

const sharp = require('sharp');
const fs = require('fs');
const path = require('path');

const svgFile = 'avatar-pm-ai-opensource.svg';
const sizes = [512, 256, 128, 64, 32];

async function convertSvgToPng() {
    // 检查SVG文件是否存在
    if (!fs.existsSync(svgFile)) {
        console.log(`❌ 文件不存在: ${svgFile}`);
        return;
    }

    // 读取SVG文件
    const svgBuffer = fs.readFileSync(svgFile);
    console.log('🔄 开始转换SVG到PNG...\n');

    // 生成不同尺寸的PNG
    for (const size of sizes) {
        const outputFile = `avatar-pm-ai-opensource-${size}x${size}.png`;
        try {
            await sharp(svgBuffer)
                .resize(size, size)
                .png()
                .toFile(outputFile);
            console.log(`✓ 已生成: ${outputFile}`);
        } catch (err) {
            console.log(`❌ 生成 ${outputFile} 失败: ${err.message}`);
        }
    }

    // 生成主文件 (512x512)
    try {
        await sharp(svgBuffer)
            .resize(512, 512)
            .png()
            .toFile('avatar-pm-ai-opensource.png');
        console.log('✓ 已生成: avatar-pm-ai-opensource.png');
    } catch (err) {
        console.log(`❌ 生成主文件失败: ${err.message}`);
    }

    console.log('\n🎉 所有PNG格式头像已生成完成！');
}

convertSvgToPng();
