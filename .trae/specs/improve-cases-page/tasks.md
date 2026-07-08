# Tasks

- [x] Task 1: 删除案例卡片中的"周期"字段显示
  - [x] 修改 cases.astro 卡片模板，移除周期显示区域
  - [x] 保留"查看详情 →"按钮

- [x] Task 2: 增加案例数量到 12+ 个
  - [x] 新增 5 个案例，覆盖更多业务场景
  - [x] 确保 5 个分类每个至少 2 个案例
  - [x] 新增案例配置 imageUrl 字段

- [x] Task 3: 更换更高质量的 Pexels 图片
  - [x] 搜索并下载更贴合 AI 客服场景的图片替换 ai-chatbot.jpg
  - [x] 搜索并下载更贴合电商网站场景的图片替换 ecommerce-dashboard.jpg
  - [x] 搜索并下载更贴合移动端购物的图片替换 mini-program.jpg
  - [x] 搜索并下载更贴合企业平台/数据仪表盘的图片替换 ai-agent-platform.jpg
  - [x] 搜索并下载更贴合智慧农业的图片替换 agri-iot.png
  - [x] 搜索并下载更贴合网络安全的图片替换 cybersecurity.jpg
  - [x] 搜索并下载更贴合 AI/神经网络的图片替换 ai-neural-network.jpg
  - [x] 搜索并下载更贴合餐饮管理的图片替换 restaurant-pos.jpg
  - [x] 搜索并下载更贴合政务服务的图片替换 government-service.jpg
  - [x] 搜索并下载更贴合跨境物流的图片替换 cross-border.jpg
  - [x] 为新增案例下载对应的新图片

- [x] Task 4: 构建验证并推送代码
  - [x] 运行 npm run build 验证构建无错误
  - [x] 推送代码到 GitHub

# Task Dependencies
- Task 2 depends on Task 1 (可并行，但先改模板)
- Task 3 depends on Task 2 (需要知道新增案例的图片需求)
- Task 4 depends on Task 1, Task 2, Task 3