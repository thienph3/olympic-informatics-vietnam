# 🚀 Hướng dẫn Setup Repository

## Cách 1: Sử dụng script tự động (Khuyến nghị)

```bash
# Chạy script setup tự động
./setup-git.sh
```

## Cách 2: Setup thủ công

### Bước 1: Khởi tạo Git repository

```bash
# Khởi tạo git (nếu chưa có)
git init

# Thêm remote origin
git remote add origin https://github.com/thienph3/olympic-informatics-vietnam.git
```

### Bước 2: Tạo .gitignore

```bash
# Tạo file .gitignore
cat > .gitignore << 'EOF'
# Python
__pycache__/
*.py[cod]
*.so
.Python
build/
dist/
*.egg-info/

# IDE
.vscode/settings.json
.idea/
*.swp
*~

# OS
.DS_Store
Thumbs.db

# Logs
*.log
debug.log

# Temporary files
*.tmp
*.backup
EOF
```

### Bước 3: Commit và push

```bash
# Add tất cả files
git add .

# Commit với message mô tả
git commit -m "🎯 Initial commit: Olympic Informatics Vietnam - Month 1 Complete"

# Set main branch
git branch -M main

# Push lên GitHub
git push -u origin main
```

## 🔐 Xác thực GitHub

Khi push lần đầu, bạn sẽ cần xác thực:

### Option 1: Personal Access Token (Khuyến nghị)

**Bước 1: Tạo Personal Access Token**
1. 🌐 Vào GitHub.com → Click avatar (góc phải) → **Settings**
2. 📋 Scroll xuống → Click **Developer settings** (menu trái)
3. 🔑 Click **Personal access tokens** → **Tokens (classic)**
4. ✨ Click **Generate new token** → **Generate new token (classic)**
5. 📝 Điền thông tin:
   - **Note**: `Olympic Informatics Vietnam`
   - **Expiration**: `90 days` (hoặc `No expiration`)
   - **Scopes**: ✅ Chọn `repo` (full control of private repositories)
6. 🎯 Click **Generate token**
7. 📋 **QUAN TRỌNG**: Copy token ngay (chỉ hiện 1 lần!)

**Bước 2: Sử dụng Token**
- Username: `thienph3`
- Password: `ghp_xxxxxxxxxxxxxxxxxxxx` (token vừa tạo)

**🔗 Link trực tiếp**: https://github.com/settings/tokens

### Option 2: SSH Key
```bash
# Tạo SSH key
ssh-keygen -t ed25519 -C "your_email@example.com"

# Add SSH key vào ssh-agent
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519

# Copy public key và add vào GitHub
cat ~/.ssh/id_ed25519.pub

# Thay đổi remote URL sang SSH
git remote set-url origin git@github.com:thienph3/olympic-informatics-vietnam.git
```

## 📋 Checklist sau khi setup

- [ ] Repository đã được tạo trên GitHub
- [ ] Code đã được push thành công
- [ ] README.md hiển thị đúng trên GitHub
- [ ] Thêm description cho repository
- [ ] Thêm topics: `python`, `olympic`, `informatics`, `competitive-programming`, `vietnam`
- [ ] Enable GitHub Pages (nếu cần)

## 🎯 Cấu trúc repository sau khi push

```
olympic-informatics-vietnam/
├── README.md              # Trang chủ repository
├── SETUP.md              # Hướng dẫn setup (file này)
├── setup-git.sh          # Script setup tự động
├── month1/               # Tháng 1 - Python fundamentals
│   ├── day01.md          # 12 files markdown
│   ├── ...
│   ├── day12.md
│   └── problem*.py       # 94 files bài tập
├── month2/               # Tháng 2 - Algorithms (sẽ tạo)
├── month3/               # Tháng 3 - Data structures (sẽ tạo)
├── month4/               # Tháng 4 - Graphs (sẽ tạo)
├── month5/               # Tháng 5 - Advanced (sẽ tạo)
└── month6/               # Tháng 6 - Contest prep (sẽ tạo)
```

## 🔄 Workflow cho tương lai

```bash
# Khi thêm nội dung mới
git add .
git commit -m "✨ Add Month 2 Day 1: Linear Search and Binary Search"
git push

# Tạo branch cho feature mới
git checkout -b month2-development
# ... làm việc ...
git add .
git commit -m "🚧 WIP: Month 2 content"
git push -u origin month2-development

# Merge về main khi hoàn thành
git checkout main
git merge month2-development
git push
```

## 🏆 Mục tiêu

Repository này sẽ trở thành:
- 📚 **Tài liệu học tập** hoàn chỉnh cho Olympic Tin học
- 🎯 **Lộ trình rõ ràng** từ zero đến Olympic level
- 💻 **Bộ sưu tập bài tập** với lời giải chi tiết
- 🌟 **Tài nguyên mở** cho cộng đồng học sinh Việt Nam

**Chúc bạn thành công! 🚀**