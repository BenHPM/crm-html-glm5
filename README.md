# CRM PRO - 客户关系管理系统

一个现代化的纯前端CRM（客户关系管理）系统，采用原生HTML/CSS/JavaScript开发，无需后端依赖，开箱即用。

## 功能特性

### 核心模块

- **仪表盘** - 数据概览，展示销售额、新增客户、待办事项、转化率等关键指标
- **客户管理** - 客户信息的增删改查，支持多维度筛选和搜索
- **销售机会** - 销售漏斗可视化，跟踪销售进度
- **联系人管理** - 联系人信息管理
- **任务管理** - 任务清单，支持优先级分类
- **操作日志** - 系统操作记录追踪

### 特色功能

- 敏感信息脱敏显示（模糊处理）
- 客户重复检测与预警
- 多标签筛选（行业、规模、状态、标签）
- 响应式设计，适配移动端
- 现代化UI设计风格

## 技术栈

- **HTML5** - 语义化标签
- **CSS3** - CSS变量、Flexbox、Grid布局、动画
- **JavaScript (ES6+)** - 原生JS，无框架依赖
- **LocalStorage** - 本地数据持久化

## 快速开始

### 在线预览

直接在浏览器中打开 `crm-system.html` 文件即可使用。

### 本地运行

```bash
# 克隆仓库
git clone https://github.com/你的用户名/crm-html-glm5.git

# 进入项目目录
cd crm-html-glm5

# 用浏览器打开
start crm-system.html  # Windows
open crm-system.html   # macOS
xdg-open crm-system.html  # Linux
```

## 项目结构

```
crm-html-glm5/
├── crm-system.html    # 主程序文件（包含HTML/CSS/JS）
├── html.md            # 原型设计文档
└── README.md          # 项目说明文档
```

## 界面预览

### 仪表盘
![仪表盘](docs/dashboard.png)

### 客户管理
![客户管理](docs/customers.png)

### 销售机会
![销售机会](docs/sales.png)

## 主要功能说明

### 客户管理

- 支持新增、编辑、删除客户
- 多条件筛选：行业、规模、状态、标签
- 关键词搜索
- 客户详情查看
- 联系人关联管理
- 跟进记录时间线

### 数据统计

- 总销售额统计
- 新增客户数量
- 待办事项提醒
- 销售转化率分析
- 销售漏斗可视化

## 浏览器支持

- Chrome (推荐)
- Firefox
- Safari
- Edge
- 不支持IE浏览器

## 开发计划

- [ ] 数据导入导出功能
- [ ] 更多图表可视化
- [ ] 多语言支持
- [ ] 暗黑模式
- [ ] 移动端App适配

## 贡献指南

欢迎提交Issue和Pull Request！

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 创建 Pull Request

## 许可证

本项目采用 MIT 许可证 - 详见 [LICENSE](LICENSE) 文件

## 联系方式

如有问题或建议，欢迎通过以下方式联系：

- 提交 Issue
- 发送邮件

---

**CRM PRO** - 让客户管理更简单高效
