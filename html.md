<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CRM System Prototype</title>
    <style>
        :root { --primary: #1890ff; --sidebar-bg: #001529; --text-main: #333; --text-sub: #666; --bg-body: #f0f2f5; --header-h: 60px; --sidebar-w: 240px; }
        * { box-sizing: border-box; margin: 0; padding: 0; outline: none; }
        body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; background: var(--bg-body); color: var(--text-main); height: 100vh; overflow: hidden; display: flex; }
        #app { display: flex; width: 100%; height: 100%; }
        .sidebar { width: var(--sidebar-w); background: var(--sidebar-bg); color: rgba(255,255,255,0.65); display: flex; flex-direction: column; flex-shrink: 0; }
        .main { flex: 1; display: flex; flex-direction: column; min-width: 0; }
        .logo { height: var(--header-h); display: flex; align-items: center; padding-left: 24px; font-size: 20px; font-weight: bold; color: #fff; background: rgba(255,255,255,0.1); }
        .nav-item { padding: 0 24px; height: 50px; line-height: 50px; cursor: pointer; transition: 0.3s; }
        .nav-item:hover { color: #fff; }
        .nav-item.active { background: var(--primary); color: #fff; }
        .header { height: var(--header-h); background: #fff; box-shadow: 0 1px 4px rgba(0,21,41,0.08); display: flex; align-items: center; justify-content: space-between; padding: 0 24px; z-index: 10; }
        .content-area { flex: 1; overflow-y: auto; padding: 24px; position: relative; }
        .card { background: #fff; border-radius: 4px; padding: 24px; margin-bottom: 24px; box-shadow: 0 1px 2px rgba(0,0,0,0.05); }
        .btn { background: var(--primary); color: #fff; border: none; padding: 8px 16px; border-radius: 4px; cursor: pointer; transition: 0.3s; }
        .btn:hover { opacity: 0.9; }
        .grid-4 { display: grid; grid-template-columns: repeat(4, 1fr); gap: 24px; }
        .hidden { display: none !important; }
        table { width: 100%; border-collapse: collapse; }
        th { text-align: left; padding: 16px; background: #fafafa; border-bottom: 1px solid #f0f0f0; font-weight: 600; }
        td { padding: 16px; border-bottom: 1px solid #f0f0f0; }
        tr:hover td { background: #fafafa; }
    </style>
</head>
<body>
    <div id="app">
        <aside class="sidebar">
            <div class="logo">CRM PRO</div>
            <nav>
                <div class="nav-item active" onclick="switchTab('dashboard', this)">仪表盘</div>
                <div class="nav-item" onclick="switchTab('customers', this)">客户管理</div>
                <div class="nav-item" onclick="switchTab('sales', this)">销售机会</div>
                <div class="nav-item" onclick="switchTab('contacts', this)">联系人</div>
                <div class="nav-item" onclick="switchTab('tasks', this)">任务管理</div>
            </nav>
        </aside>
        <main class="main">
            <header class="header">
                <div style="font-weight: 500;">工作台</div>
                <div style="width:32px; height:32px; background:var(--primary); border-radius:50%; color:#fff; display:flex; align-items:center; justify-content:center; font-size:14px;">A</div>
            </header>
            <div class="content-area">
                <!-- 1. Dashboard -->
                <section id="page-dashboard">
                    <div class="grid-4">
                        <div class="card"><h3>总销售额</h3><div style="font-size:28px; color:var(--primary); font-weight:bold; margin-top:10px;">¥1,280,000</div></div>
                        <div class="card"><h3>新增客户</h3><div style="font-size:28px; color:#52c41a; font-weight:bold; margin-top:10px;">+320</div></div>
                        <div class="card"><h3>待办事项</h3><div style="font-size:28px; color:#faad14; font-weight:bold; margin-top:10px;">12</div></div>
                        <div class="card"><h3>转化率</h3><div style="font-size:28px; color:#f5222d; font-weight:bold; margin-top:10px;">24.5%</div></div>
                    </div>
                    <div class="card">
                        <h3>销售漏斗</h3>
                        <div style="margin-top:20px; display:flex; flex-direction:column; gap:10px;">
                            <div style="background:#e6f7ff; height:40px; display:flex; align-items:center; padding-left:10px; border-radius:4px;">线索 (100%)</div>
                            <div style="background:#bae7ff; width:80%; height:40px; display:flex; align-items:center; padding-left:10px; border-radius:4px;">初步沟通 (80%)</div>
                            <div style="background:#91d5ff; width:60%; height:40px; display:flex; align-items:center; padding-left:10px; border-radius:4px;">方案报价 (60%)</div>
                            <div style="background:#69c0ff; width:40%; height:40px; display:flex; align-items:center; padding-left:10px; border-radius:4px;">谈判成交 (40%)</div>
                        </div>
                    </div>
                </section>

                <!-- 2. Customers -->
                <section id="page-customers" class="hidden">
                    <div style="margin-bottom:20px;"><button class="btn">新增客户</button></div>
                    <div class="card">
                        <table>
                            <thead><tr><th>客户名称</th><th>联系人</th><th>电话</th><th>状态</th><th>最后跟进</th></tr></thead>
                            <tbody>
                                <tr><td>先锋科技有限公司</td><td>张经理</td><td>13800138000</td><td><span style="color:green">合作中</span></td><td>2024-10-20</td></tr>
                                <tr><td>蓝天物流集团</td><td>王总监</td><td>13912345678</td><td><span style="color:orange">意向中</span></td><td>2024-10-18</td></tr>
                                <tr><td>深海创意工作室</td><td>李设计</td><td>13787654321</td><td><span style="color:#999">流失</span></td><td>2024-09-01</td></tr>
                            </tbody>
                        </table>
                    </div>
                </section>

                <!-- 3. Sales -->
                <section id="page-sales" class="hidden">
                    <div class="grid-4">
                        <div class="card">
                            <div style="font-weight:bold; font-size:16px;">企业采购平台</div>
                            <div style="color:#888; font-size:12px; margin:5px 0;">先锋科技</div>
                            <div style="margin:10px 0;">¥50,000</div>
                            <div style="height:6px; background:#f0f0f0; border-radius:3px;"><div style="width:70%; height:100%; background:var(--primary); border-radius:3px;"></div></div>
                            <div style="font-size:12px; margin-top:5px;">方案阶段</div>
                        </div>
                        <div class="card">
                            <div style="font-weight:bold; font-size:16px;">年度维护合同</div>
                            <div style="color:#888; font-size:12px; margin:5px 0;">云端网络</div>
                            <div style="margin:10px 0;">¥12,000</div>
                            <div style="height:6px; background:#f0f0f0; border-radius:3px;"><div style="width:30%; height:100%; background:var(--primary); border-radius:3px;"></div></div>
                            <div style="font-size:12px; margin-top:5px;">初步沟通</div>
                        </div>
                    </div>
                </section>

                <!-- 4. Contacts -->
                <section id="page-contacts" class="hidden">
                    <h2 style="margin-bottom:20px;">联系人管理</h2>
                    <div style="display:flex; justify-content:space-between; margin-bottom:20px;">
    <input type="text" placeholder="搜索联系人..." style="padding:8px; border:1px solid #ddd; border-radius:4px; width:240px;">
    <button class="btn">+ 新增</button>
</div>
<div class="grid-4">
    <div class="card" style="display:flex; align-items:center; gap:15px;">
        <div style="width:48px; height:48px; background:#1890ff; color:#fff; border-radius:50%; display:flex; align-items:center; justify-content:center; font-weight:bold;">A</div>
        <div><div style="font-weight:bold;">艾伦</div><div style="font-size:12px; color:#888; margin-top:4px;">产品总监 | 未来科技</div></div>
    </div>
    <div class="card" style="display:flex; align-items:center; gap:15px;">
        <div style="width:48px; height:48px; background:#52c41a; color:#fff; border-radius:50%; display:flex; align-items:center; justify-content:center; font-weight:bold;">B</div>
        <div><div style="font-weight:bold;">鲍勃</div><div style="font-size:12px; color:#888; margin-top:4px;">销售经理 | 全球贸易</div></div>
    </div>
    <div class="card" style="display:flex; align-items:center; gap:15px;">
        <div style="width:48px; height:48px; background:#faad14; color:#fff; border-radius:50%; display:flex; align-items:center; justify-content:center; font-weight:bold;">C</div>
        <div><div style="font-weight:bold;">查理</div><div style="font-size:12px; color:#888; margin-top:4px;">技术顾问 | 创新工场</div></div>
    </div>
    <div class="card" style="display:flex; align-items:center; gap:15px;">
        <div style="width:48px; height:48px; background:#f5222d; color:#fff; border-radius:50%; display:flex; align-items:center; justify-content:center; font-weight:bold;">D</div>
        <div><div style="font-weight:bold;">大卫</div><div style="font-size:12px; color:#888; margin-top:4px;">采购专员 | 阳光集团</div></div>
    </div>
</div>
                </section>

                <!-- 5. Tasks -->
                <section id="page-tasks" class="hidden">
                    <h2 style="margin-bottom:20px;">任务清单</h2>
                    <div style="margin-bottom:15px; display:flex; gap:15px; border-bottom:1px solid #eee; padding-bottom:10px;">
    <span style="font-weight:bold; color:#1890ff; cursor:pointer;">全部</span>
    <span style="color:#666; cursor:pointer;">待处理</span>
    <span style="color:#666; cursor:pointer;">进行中</span>
</div>
<div style="display:flex; flex-direction:column; gap:12px;">
    <div class="card" style="margin:0; padding:15px; display:flex; align-items:center; gap:12px;">
        <input type="checkbox" style="width:16px; height:16px;">
        <div style="flex:1;"><div style="font-weight:bold;">Q3 季度销售汇报PPT</div><div style="font-size:12px; color:#888; margin-top:4px;">截止: 2024-10-30</div></div>
        <span style="background:#ff4d4f; color:#fff; font-size:12px; padding:2px 8px; border-radius:4px;">高优先级</span>
    </div>
    <div class="card" style="margin:0; padding:15px; display:flex; align-items:center; gap:12px;">
        <input type="checkbox" style="width:16px; height:16px;">
        <div style="flex:1;"><div style="font-weight:bold;">客户拜访：XX公司</div><div style="font-size:12px; color:#888; margin-top:4px;">截止: 2024-11-05</div></div>
        <span style="background:#faad14; color:#fff; font-size:12px; padding:2px 8px; border-radius:4px;">中优先级</span>
    </div>
    <div class="card" style="margin:0; padding:15px; display:flex; align-items:center; gap:12px;">
        <input type="checkbox" style="width:16px; height:16px;">
        <div style="flex:1;"><div style="font-weight:bold;">更新CRM客户数据</div><div style="font-size:12px; color:#888; margin-top:4px;">截止: 2024-11-10</div></div>
        <span style="background:#d9d9d9; color:#fff; font-size:12px; padding:2px 8px; border-radius:4px;">低优先级</span>
    </div>
</div>
                </section>
            </div>
        </main>
    </div>

    <script>
        /**
         * 切换页面标签
         * @param {string} pageId - 页面ID
         * @param {HTMLElement} navElement - 导航元素
         */
        function switchTab(pageId, navElement) {
            document.querySelectorAll('.content-area section').forEach(el => el.classList.add('hidden'));
            document.getElementById('page-' + pageId).classList.remove('hidden');
            document.querySelectorAll('.nav-item').forEach(el => el.classList.remove('active'));
            navElement.classList.add('active');
        }
    </script>
</body>
</html>