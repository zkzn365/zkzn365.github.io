# 案例页优化 Spec

## Why
用户反馈案例页存在三个问题：1) 案例数量太少（仅9个），2) 部分图片质量/匹配度不够好，3) 卡片上的"周期"字段不需要显示。需要全面优化案例页内容和视觉效果。

## What Changes
- 增加案例数量（从 9 个增加到 12+ 个），覆盖更多业务场景
- 更换更高质量、更贴合案例主题的 Pexels 图片
- 删除案例卡片中的"周期"字段显示
- 确保所有案例卡片都有清晰、匹配的配图

## Impact
- Affected code: `src/pages/cases.astro`（数据 + 模板）
- Affected code: `public/` 目录（图片文件）
- 无 breaking change，纯内容和视觉优化

## ADDED Requirements
### Requirement: 增加案例数量
系统 SHALL 在案例页展示至少 12 个案例，覆盖 AI 智能体、小程序开发、跨境电商、应用开发、网络安全五大类。

#### Scenario: 新增案例
- **WHEN** 用户访问案例页
- **THEN** 至少展示 12 个不同的案例卡片，每个分类至少有 2 个案例

### Requirement: 删除周期显示
系统 SHALL 不在案例卡片上显示"周期"字段。

#### Scenario: 卡片不显示周期
- **WHEN** 用户查看案例卡片
- **THEN** 卡片底部不显示"周期：xxx"文字

### Requirement: 高质量配图
系统 SHALL 为每个案例卡片配置与案例主题高度匹配的高质量 Pexels 免费可商用图片。

#### Scenario: 图片匹配度高
- **WHEN** 用户浏览案例卡片
- **THEN** 每张图片都能直观反映案例的业务场景，图片清晰、专业

## MODIFIED Requirements
### Requirement: 案例卡片布局
原案例卡片底部显示"周期"和"查看详情"，修改为仅显示"查看详情"或其他相关信息。
