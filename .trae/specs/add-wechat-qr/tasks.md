# 中科智农官网 - 添加微信二维码实现计划

## [ ] Task 1: 检查 opc.png 文件有效性
- **Priority**: high
- **Depends On**: None
- **Description**: 
  - 检查 public/opc.png 文件是否存在
  - 验证文件是否为有效的 PNG 图片格式
  - 确认文件大小和尺寸适合网页展示
- **Acceptance Criteria Addressed**: AC-2
- **Test Requirements**:
  - `programmatic` TR-1.1: opc.png 文件存在且文件大小 > 0
  - `programmatic` TR-1.2: 文件 MIME 类型为 image/png
- **Notes**: 如果文件无效，需要提示用户提供有效图片

## [ ] Task 2: 更新联系页面添加微信二维码
- **Priority**: high
- **Depends On**: Task 1
- **Description**: 
  - 在联系页面左侧联系方式区域添加微信二维码卡片
  - 使用 public/opc.png 作为二维码图片
  - 添加"扫码添加客服"提示文字
- **Acceptance Criteria Addressed**: AC-1, AC-3
- **Test Requirements**:
  - `human-judgment` TR-2.1: 微信二维码卡片显示在联系方式区域
  - `human-judgment` TR-2.2: 二维码清晰可扫描，布局美观
  - `human-judgment` TR-2.3: 移动端显示正常

## [ ] Task 3: 更新页脚添加微信联系方式
- **Priority**: medium
- **Depends On**: Task 1
- **Description**: 
  - 在页脚区域添加微信联系图标和二维码
- **Acceptance Criteria Addressed**: FR-3
- **Test Requirements**:
  - `human-judgment` TR-3.1: 页脚显示微信联系方式

## [ ] Task 4: 构建验证
- **Priority**: high
- **Depends On**: Task 2, Task 3
- **Description**: 
  - 运行 npm run build 验证构建无错误
- **Acceptance Criteria Addressed**: All
- **Test Requirements**:
  - `programmatic` TR-4.1: npm run build 成功完成

## [ ] Task 5: 推送代码到 GitHub
- **Priority**: high
- **Depends On**: Task 4
- **Description**: 
  - 提交代码变更并推送到 GitHub
- **Acceptance Criteria Addressed**: All
- **Test Requirements**:
  - `programmatic` TR-5.1: git push 成功完成
