# 案例页图片补齐 Spec

## Why
案例页 (`/cases/`) 的卡片数据中已有 `imageUrl`，但页面模板未渲染图片，只显示渐变色背景。用户看到的是空白色块，没有真实的案例配图，影响视觉专业度。

## What Changes
- 修改 cases.astro 中的内联卡片模板，渲染 `imageUrl` 为 `<img>` 标签
- 从 Pexels 免费可商用图库下载更贴合案例场景的真实照片替换现有图片
- 确保图片在卡片中正确显示（object-cover、懒加载、hover 缩放效果）

## Impact
- Affected code: `src/pages/cases.astro`（卡片模板）、`public/` 目录（图片文件）
- 无 breaking change，仅视觉增强

## ADDED Requirements
### Requirement: 案例卡片图片展示
系统 SHALL 在案例页每个案例卡片的顶部区域显示与案例主题相关的真实照片。

#### Scenario: 案例卡片显示图片
- **WHEN** 用户访问 `/cases/` 页面
- **THEN** 每个案例卡片顶部显示 `imageUrl` 对应的图片，图片使用 `object-cover` 填充卡片区域，支持懒加载

#### Scenario: 图片来源于 Pexels 免费图库
- **WHEN** 案例图片需要下载
- **THEN** 从 Pexels（CC0 协议，免费可商用）获取与案例场景匹配的真实照片

### Requirement: 案例卡片交互效果
系统 SHALL 在鼠标悬停时对案例卡片图片应用缩放效果。

#### Scenario: 悬停缩放
- **WHEN** 用户鼠标悬停在案例卡片上
- **THEN** 卡片图片平滑放大（scale-105），过渡时间 500ms
