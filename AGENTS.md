# AGENTS.md

这是中科智农的企业官网，基于 Astro 构建，部署在 GitHub Pages。

## 技术栈
- Astro 5 + Tailwind CSS v4
- 静态生成模式
- 部署到 GitHub Pages

## 开发命令
```bash
npm run dev      # 开发服务器
npm run build    # 构建静态文件
npm run preview  # 预览静态输出
```

## 项目结构
- `src/pages/` - 页面文件
- `src/layouts/` - 布局文件
- `src/components/` - 组件
- `src/styles/` - 样式文件
- `public/` - 静态资源（图片等）

## 部署流程
1. `npm run build` 生成静态文件到 `dist/`
2. 提交代码到 `main` 分支
3. GitHub Actions 自动部署到 https://zkzn365.com
