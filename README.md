<p align="center">
  <img src="https://img.shields.io/badge/status-live-brightgreen?style=flat-square" alt="status">
  <img src="https://img.shields.io/badge/license-MIT-blue?style=flat-square" alt="license">
  <img src="https://img.shields.io/badge/python-3.10+-blue?style=flat-square" alt="python">
  <img src="https://img.shields.io/badge/format%20types-28-orange?style=flat-square" alt="types">
</p>

<h1 align="center">🏭 FileForge · 文件转换工坊</h1>
<p align="center"><b>在线万能文件格式转换工具 · 28种格式互转 · 无需安装</b></p>
<p align="center"><a href="https://fileforge.cn"><b>🌐 fileforge.cn</b></a></p>

---

## ✨ 特色功能 | Features

| 功能 | 说明 |
|------|------|
| 🔄 28种格式 | 文档 · 图片 · 音频 · 视频 · 表格全覆盖 |
| 📦 批量转换 | 多文件同时上传，独立设置每文件输出格式 |
| 🎵 音乐 + 雨声 | 内置三首曲目，支持切换、暂停、音量调节 |
| 📊 真实进度 | 基于 ffprobe 精确计算，不掺假不卡条 |
| 💬 弹幕提示 | 转换中飘过暖心小提示 |
| ⚡ 极速下载 | X-Accel · BBR · HTTP/2 · Gzip 全链路优化 |
| 🔒 安全加固 | HSTS · CSP · 速率限制 · 完整安全头 |
| 📱 响应式 | 手机平板电脑都能用 |

## 🔧 支持格式 | Formats

| 类别 | 输入 → 输出 |
|------|------------|
| 📄 文档 | PDF ↔ DOCX ↔ TXT · MD → PDF · HTML → PDF |
| 🖼 图片 | PNG ↔ JPG ↔ WebP ↔ GIF ↔ BMP ↔ TIFF |
| 🎵 音频 | WAV ↔ MP3 ↔ OGG ↔ FLAC ↔ AAC |
| 🎬 视频 | MP4 → WebM/MKV/AVI/MOV · 提取 MP3/WAV/GIF |
| 📊 表格 | CSV ↔ XLSX |

## 🛠 技术栈 | Tech Stack

**后端** Python · Flask · Gunicorn  
**前端** 原生 HTML/CSS/JS（零框架）  
**引擎** FFmpeg · Pillow · python-docx · fpdf2 · markdown  
**部署** Nginx · Let's Encrypt · Ubuntu · systemd  

## 🚀 快速部署 | Deploy

```bash
# 1. 安装系统依赖
sudo apt install -y python3 python3-venv ffmpeg nginx certbot python3-certbot-nginx

# 2. 克隆项目
git clone https://github.com/Feciliawish/FileForge.git
cd FileForge

# 3. 安装 Python 依赖
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt

# 4. 准备音乐文件（可选）
# 将 .mp3 放入 static/ 目录，参考 static/README.txt

# 5. 部署 Nginx（替换域名）
sudo cp deploy/nginx-site.conf /etc/nginx/sites-enabled/fileforge
sudo nano /etc/nginx/sites-enabled/fileforge  # 改域名

# 6. 启动服务
sudo cp deploy/fileforge.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable --now fileforge
sudo systemctl reload nginx

# 7. SSL 证书
sudo certbot --nginx -d yourdomain.com -d www.yourdomain.com
```

## 📂 项目结构 | Structure

```
.
├── app.py                  # Flask 后端主程序
├── gunicorn_conf.py        # Gunicorn 生产配置
├── requirements.txt        # Python 依赖
├── templates/
│   ├── index.html          # 单文件转换页
│   └── batch.html          # 批量转换页
├── static/                 # 静态资源（音乐文件放这里）
└── deploy/                 # 部署参考
    ├── nginx-site.conf     # Nginx 站点配置
    ├── nginx.conf          # Nginx 全局配置
    └── fileforge.service   # systemd 服务文件
```

## 💝 赞助 | Support

如果这个项目帮到了你，欢迎支持：[爱发电 · afdian.net](https://ifdian.net/a/Fecilia)

---

<p align="center"><sub>MIT License · Made with ❤️</sub></p>
