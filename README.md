# FileForge 文件转换工坊 🏭

在线万能文件格式转换工具，支持28种格式互转，无需安装任何软件。

**🌐 在线体验：[fileforge.cn](https://fileforge.cn)**

---

## ✨ 特色功能

- 🔄 **28种转换格式** — 文档、图片、音频、视频、表格全覆盖
- 📦 **批量转换** — 多文件同时上传，独立设置每个文件的输出格式
- 🎵 **背景音乐 + 雨声白噪音** — 内置三首曲目，可切换可调音量
- 📊 **真实进度条** — 基于文件时长精确计算，不掺假不卡条
- 💬 **趣味弹幕** — 转换过程中飘过暖心小提示
- ⚡ **极速下载** — X-Accel + BBR + HTTP/2，国内用户畅快下载
- 🔒 **安全加固** — HSTS、CSP、限速、完整安全头
- 📱 **响应式设计** — 手机电脑都能用

## 🛠 技术栈

**后端** Python · Flask · Gunicorn  
**前端** 原生 HTML/CSS/JS（零框架依赖）  
**转换** FFmpeg · Pillow · python-docx · fpdf2 · markdown  
**部署** Nginx · Let's Encrypt · Ubuntu · systemd  

## 🚀 快速部署

```bash
# 1. 安装系统依赖
sudo apt install -y python3 python3-venv ffmpeg nginx certbot python3-certbot-nginx

# 2. 安装 Python 依赖
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt

# 3. 配置 Nginx
sudo cp deploy/nginx-site.conf /etc/nginx/sites-enabled/fileforge
# 编辑域名 → sudo nano /etc/nginx/sites-enabled/fileforge

# 4. 启动服务
sudo cp deploy/fileforge.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable --now fileforge
sudo systemctl reload nginx

# 5. 申请 SSL 证书
sudo certbot --nginx -d yourdomain.com
```

## 📂 项目结构

```
├── app.py              # Flask 主程序
├── gunicorn_conf.py    # 生产配置
├── requirements.txt    # Python 依赖
├── templates/
│   ├── index.html      # 单文件转换页
│   └── batch.html      # 批量转换页
├── static/             # 静态资源（音乐放这里）
└── deploy/             # Nginx + systemd 参考配置
```

## 💝 赞助

喜欢这个项目？[请我喝杯咖啡 ☕](https://ifdian.net/a/Fecilia)

---

## FileForge — Online File Converter 🏭

A universal online file format converter supporting 28 conversion types. No installation required.

**🌐 Live Demo: [fileforge.cn](https://fileforge.cn)**

### ✨ Highlights

- 🔄 **28 Conversion Types** — Documents, images, audio, video, spreadsheets
- 📦 **Batch Processing** — Upload multiple files, set per-file output format
- 🎵 **Built-in Music Player + Rain Sounds** — 3 tracks with volume control & playlist
- 📊 **Real Progress Tracking** — ffprobe-based duration calculation, no fake percentages
- 💬 **Fun Danmaku Messages** — Floating encouragement messages during conversion
- ⚡ **Blazing Fast Downloads** — X-Accel + BBR congestion control + HTTP/2
- 🔒 **Hardened Security** — HSTS, CSP, rate limiting, full security headers
- 📱 **Fully Responsive** — Works great on desktop and mobile

### 🛠 Tech Stack

**Backend** Python · Flask · Gunicorn  
**Frontend** Vanilla HTML/CSS/JS (zero framework dependencies)  
**Engines** FFmpeg · Pillow · python-docx · fpdf2 · markdown  
**Infra** Nginx · Let's Encrypt · Ubuntu · systemd  

### 💝 Support

Like this project? [Buy me a coffee ☕](https://ifdian.net/a/Fecilia)

---

**MIT License**
