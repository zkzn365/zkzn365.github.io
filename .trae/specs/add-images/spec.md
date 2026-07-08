# 中科智农官网 - 图片资源补齐 PRD

## Overview
- **Summary**: 为中科智农企业官网补齐图片资源，包括案例图片、服务板块图片、公司宣传图片等，替换当前的渐变占位背景，提升视觉效果和专业度。
- **Purpose**: 当前网站案例卡片和部分板块使用渐变背景和 SVG 图案作为占位，缺乏真实图片支撑，影响视觉吸引力和专业形象。需要通过 AI 生成或网络搜索获取相关领域的高质量图片。
- **Target Users**: 浏览网站的潜在客户、合作伙伴、投资者

## Goals
- [ ] 为 9 个案例卡片添加真实主题图片
- [ ] 为首页核心技术板块添加展示图片
- [ ] 为服务项目页添加业务板块配图
- [ ] 优化 CaseCard 组件支持图片展示
- [ ] 使用 Astro Image 组件优化图片加载

## Non-Goals (Out of Scope)
- [ ] 不创建新页面或新功能
- [ ] 不修改现有页面布局结构
- [ ] 不更换配色方案
- [ ] 不修改网站文案内容

## Background & Context
- 当前网站基于 Astro 5 + Tailwind CSS 4 + shadcn/ui 构建
- 案例卡片使用渐变背景 + SVG 图案作为占位（[CaseCard.astro](src/components/CaseCard.astro)）
- 需要替换的图片位置：案例卡片、核心技术板块、服务展示区
- 图片资源将使用 AI 文本生成图片 API 获取

## Functional Requirements
- **FR-1**: CaseCard 组件支持接收 imageUrl 属性并展示图片
- **FR-2**: 9 个案例分别配备符合主题的真实图片
- **FR-3**: 首页核心技术板块添加 AI 大模型和 Agent 平台相关图片
- **FR-4**: 服务项目页各业务板块添加主题配图
- **FR-5**: 使用 Astro Image 组件优化图片加载性能

## Non-Functional Requirements
- **NFR-1**: 图片风格统一，符合嫩绿主色 #BDDD22 和科技感主题
- **NFR-2**: 图片分辨率不低于 800x600，支持响应式显示
- **NFR-3**: 图片加载速度快，支持懒加载
- **NFR-4**: 图片内容与业务主题高度相关

## Constraints
- **Technical**: 使用 Astro Image 组件，图片存储在 public 目录或使用远程 URL
- **Dependencies**: 依赖 AI 图片生成 API（trae-api-cn.mchost.guru）
- **Budget**: 使用免费 AI 图片生成服务

## Assumptions
- [ ] AI 图片生成 API 可用且生成质量满足需求
- [ ] 生成的图片版权可用于商业网站展示
- [ ] 网络连接稳定可正常下载图片

## Acceptance Criteria

### AC-1: 案例卡片图片展示
- **Given**: 用户浏览案例页面
- **When**: 页面加载完成
- **Then**: 9 个案例卡片均显示与案例主题相关的真实图片
- **Verification**: `human-judgment`

### AC-2: CaseCard 组件支持图片
- **Given**: CaseCard 组件接收 imageUrl 属性
- **When**: 组件渲染
- **Then**: 图片正确显示在卡片顶部区域，尺寸适配卡片宽度
- **Verification**: `programmatic`

### AC-3: 首页核心技术板块图片
- **Given**: 用户浏览首页核心技术区域
- **When**: 页面加载完成
- **Then**: AI 大模型和 Agent 平台板块显示相关主题图片
- **Verification**: `human-judgment`

### AC-4: 服务项目页配图
- **Given**: 用户浏览服务项目页
- **When**: 页面加载完成
- **Then**: 四大业务板块均有主题配图
- **Verification**: `human-judgment`

### AC-5: 图片加载优化
- **Given**: 用户访问网站
- **When**: 图片加载
- **Then**: 图片懒加载，加载速度不影响页面渲染
- **Verification**: `human-judgment`

## Open Questions
- [ ] 是否需要将图片下载到本地 public 目录还是使用远程 URL？
- [ ] 图片尺寸和比例有什么具体要求？
