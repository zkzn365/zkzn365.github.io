# AGENTS.md

这是智科智能的企业官网，基于 Nuxt.js 构建，部署在 GitHub Pages。

## 技术栈
- Nuxt 4 + Vue 3 + Tailwind CSS
- 静态生成模式 (`npm run generate`)
- 部署到 GitHub Pages

## 开发命令
```bash
npm run dev      # 开发服务器
npm run generate # 生成静态文件到 .output/public
npm run preview # 预览静态输出
```

## 项目结构
- `app/pages/` - 页面文件
- `app/layouts/` - 布局文件
- `app/assets/css/` - 样式文件
- `.output/public/` - 生成的静态文件（部署时提交）

## 部署流程
1. `npm run generate` 生成静态文件
2. 提交 `.output/public/` 到 `main` 分支
3. GitHub Actions 自动部署到 https://zkzn365.com

## 注意事项
- 页面放在 `app/pages/` 目录下
- 布局放在 `app/layouts/` 目录下
- 修改后需重新 `generate`
- 这是 Nuxt 4 项目，使用了 `app/` 目录结构