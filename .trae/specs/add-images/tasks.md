# 中科智农官网 - 图片资源补齐实现计划

## [x] Task 1: 更新 CaseCard 组件支持图片展示
- **Priority**: high
- **Depends On**: None
- **Description**: 
  - 修改 CaseCard.astro 组件，添加 imageUrl 属性
  - 使用 Astro Image 组件或 img 标签展示图片
  - 保留渐变背景作为图片加载时的占位
- **Acceptance Criteria Addressed**: AC-2
- **Test Requirements**:
  - `programmatic` TR-1.1: CaseCard 组件接收 imageUrl 属性后能正常渲染图片
  - `human-judgment` TR-1.2: 图片显示在卡片顶部，尺寸适配，加载正常

## [x] Task 2: 生成并配置案例卡片图片
- **Priority**: high
- **Depends On**: Task 1
- **Description**: 
  - 为 9 个案例分别生成主题相关的 AI 图片
  - 更新 cases.astro 和 index.astro 中案例数据，添加图片 URL
  - 案例主题：AI 智能客服、跨境电商、小程序商城、Agent 平台、IoT 系统、网络安全、餐饮管理、政务 AI、跨境分销
- **Acceptance Criteria Addressed**: AC-1
- **Test Requirements**:
  - `human-judgment` TR-2.1: 所有案例卡片显示真实图片，内容与案例主题相关
  - `human-judgment` TR-2.2: 图片风格统一，符合科技感主题

## [x] Task 3: 更新首页核心技术板块图片
- **Priority**: medium
- **Depends On**: None
- **Description**: 
  - 为首页核心技术板块（AI 大模型开发、Agent 平台）添加展示图片
  - 更新 index.astro 中的核心技术区域，使用真实图片替代当前的背景色块
- **Acceptance Criteria Addressed**: AC-3
- **Test Requirements**:
  - `human-judgment` TR-3.1: 核心技术板块显示相关主题图片
  - `human-judgment` TR-3.2: 图片与文案内容匹配，视觉效果良好

## [x] Task 4: 更新服务项目页配图
- **Priority**: medium
- **Depends On**: None
- **Description**: 
  - 为服务项目页四大业务板块添加主题配图
  - 更新 services/index.astro，在各板块添加代表性图片
- **Acceptance Criteria Addressed**: AC-4
- **Test Requirements**:
  - `human-judgment` TR-4.1: 四大业务板块均有主题配图
  - `human-judgment` TR-4.2: 图片内容与服务描述一致

## [x] Task 5: 构建验证与图片优化
- **Priority**: high
- **Depends On**: Task 1, Task 2, Task 3, Task 4
- **Description**: 
  - 运行 npm run build 验证构建无错误
  - 检查图片加载性能，确保懒加载生效
  - 验证响应式显示效果
- **Acceptance Criteria Addressed**: AC-5
- **Test Requirements**:
  - `programmatic` TR-5.1: npm run build 成功完成
  - `human-judgment` TR-5.2: 图片加载速度正常，懒加载有效
  - `human-judgment` TR-5.3: 不同屏幕尺寸下图片显示正常

## [x] Task 6: 推送代码到 GitHub
- **Priority**: high
- **Depends On**: Task 5
- **Description**: 
  - 提交代码变更
  - 推送到 GitHub 远程仓库
  - 验证 GitHub Actions 自动部署成功
- **Acceptance Criteria Addressed**: All
- **Test Requirements**:
  - `programmatic` TR-6.1: git push 成功完成
  - `programmatic` TR-6.2: GitHub Actions 构建成功
