# 中科智农官网 - 添加微信二维码 PRD

## Overview
- **Summary**: 在联系我们页面添加微信二维码展示，方便客户扫码添加客服微信进行咨询。
- **Purpose**: 提供多渠道联系方式，提升客户咨询便捷性，促进潜在客户转化。
- **Target Users**: 浏览网站的潜在客户、合作伙伴

## Goals
- [ ] 检查 public/opc.png 文件是否存在且为有效图片
- [ ] 在联系页面添加微信二维码展示区域
- [ ] 在页脚添加微信联系方式
- [ ] 确保二维码展示美观且响应式

## Non-Goals (Out of Scope)
- [ ] 不创建新页面或新功能
- [ ] 不修改其他页面内容
- [ ] 不更换配色方案

## Background & Context
- public/opc.png 文件已存在，推测为微信二维码图片
- 当前联系页面已有电话、邮箱、地址等联系方式
- 需要在左侧联系方式区域添加微信二维码

## Functional Requirements
- **FR-1**: 在联系页面左侧联系方式区域添加微信二维码卡片
- **FR-2**: 二维码下方显示"扫码添加客服"提示文字
- **FR-3**: 在页脚添加微信联系方式

## Non-Functional Requirements
- **NFR-1**: 二维码图片清晰可扫描
- **NFR-2**: 响应式显示，移动端适配良好
- **NFR-3**: 与现有设计风格一致

## Constraints
- **Technical**: 使用 Astro 静态资源，图片存储在 public 目录
- **Dependencies**: opc.png 文件必须是有效的图片文件

## Assumptions
- [ ] opc.png 是有效的微信二维码图片
- [ ] 图片尺寸适合网页展示

## Acceptance Criteria

### AC-1: 微信二维码展示
- **Given**: 用户浏览联系页面
- **When**: 页面加载完成
- **Then**: 左侧联系方式区域显示微信二维码卡片
- **Verification**: `human-judgment`

### AC-2: 二维码图片有效
- **Given**: opc.png 文件存在
- **When**: 查看文件属性
- **Then**: 文件为有效的 PNG 图片格式
- **Verification**: `programmatic`

### AC-3: 响应式显示
- **Given**: 在不同屏幕尺寸下浏览
- **When**: 调整窗口大小
- **Then**: 二维码正常显示，布局不混乱
- **Verification**: `human-judgment`

## Open Questions
- [ ] opc.png 是否为有效的微信二维码图片？
