# 🔐 Hướng dẫn tạo GitHub Personal Access Token

## 🚀 Tạo PAT trong 2 phút

### Bước 1: Vào GitHub Settings
```
🌐 GitHub.com → Click avatar (góc phải) → Settings
```

### Bước 2: Developer Settings
```
📋 Scroll xuống → Developer settings (menu trái)
```

### Bước 3: Personal Access Tokens
```
🔑 Personal access tokens → Tokens (classic)
```

### Bước 4: Generate New Token
```
✨ Generate new token → Generate new token (classic)
```

### Bước 5: Cấu hình Token
```
📝 Note: Olympic Informatics Vietnam
⏰ Expiration: 90 days (hoặc No expiration)
✅ Scopes: Chọn "repo" (full control of private repositories)
```

### Bước 6: Generate và Copy
```
🎯 Click "Generate token"
📋 Copy token ngay lập tức (chỉ hiện 1 lần!)
```

## 🔗 Link trực tiếp
**👉 https://github.com/settings/tokens**

## 💡 Sử dụng Token

Khi Git hỏi thông tin đăng nhập:
```
Username: thienph3
Password: ghp_xxxxxxxxxxxxxxxxxxxx (token vừa tạo)
```

## ⚠️ Lưu ý quan trọng

1. **🔒 Bảo mật**: Token = password, không chia sẻ!
2. **💾 Lưu trữ**: Copy và lưu token an toàn
3. **⏰ Hết hạn**: Đặt reminder để renew token
4. **🗑️ Xóa**: Xóa token cũ khi không dùng

## 🆘 Nếu quên token

1. Tạo token mới theo hướng dẫn trên
2. Xóa token cũ trong GitHub Settings
3. Sử dụng token mới cho Git

## 🎯 Token đã tạo thành công?

Test bằng cách:
```bash
git push -u origin main
```

Nếu thành công → ✅ Setup hoàn tất!
Nếu lỗi → 🔄 Kiểm tra lại token và quyền repo

---

**🏆 Chúc bạn setup thành công!**