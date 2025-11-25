# 🚨 Khắc phục lỗi 403 Permission Denied

## ❌ Lỗi gặp phải:
```
remote: Permission to thienph3/olympic-informatics-vietnam.git denied to thienph3.
fatal: unable to access 'https://github.com/thienph3/olympic-informatics-vietnam.git/': The requested URL returned error: 403
```

## 🔍 Nguyên nhân có thể:

### 1. **Repository chưa được tạo trên GitHub**
### 2. **Personal Access Token chưa đúng**
### 3. **Token không có quyền repo**

## 🛠️ Giải pháp:

### **Bước 1: Tạo Repository trên GitHub**

1. **🌐 Vào GitHub.com**
2. **➕ Click nút "+" (góc phải) → "New repository"**
3. **📝 Điền thông tin:**
   ```
   Repository name: olympic-informatics-vietnam
   Description: 6-month intensive Olympic Informatics training program for Vietnamese high school students
   ✅ Public (để mọi người có thể truy cập)
   ❌ KHÔNG chọn "Add a README file" (vì ta đã có)
   ❌ KHÔNG chọn .gitignore (vì ta đã có)
   ❌ KHÔNG chọn license (có thể thêm sau)
   ```
4. **🎯 Click "Create repository"**

### **Bước 2: Kiểm tra Personal Access Token**

1. **🔗 Vào**: https://github.com/settings/tokens
2. **✅ Kiểm tra token có:**
   - ✅ `repo` scope (full control of private repositories)
   - ✅ Chưa hết hạn
   - ✅ Đang active

### **Bước 3: Tạo token mới (nếu cần)**

```
🔑 Generate new token → Generate new token (classic)
📝 Note: Olympic Informatics Vietnam
⏰ Expiration: No expiration (hoặc 90 days)
✅ Scopes: 
   ☑️ repo (full control of private repositories)
   ☑️ workflow (nếu cần GitHub Actions)
🎯 Generate token → Copy ngay!
```

### **Bước 4: Test kết nối**

```bash
# Xóa credential cũ (nếu có)
git config --global --unset credential.helper

# Test push với token mới
git push -u origin main
```

**Khi Git hỏi:**
```
Username: thienph3
Password: ghp_xxxxxxxxxxxxxxxxxxxx (token mới)
```

## 🚀 Script khắc phục tự động:

```bash
#!/bin/bash
echo "🔧 Khắc phục lỗi 403..."

# Xóa credential cũ
git config --global --unset credential.helper 2>/dev/null || true

# Xóa remote cũ và thêm lại
git remote remove origin 2>/dev/null || true
git remote add origin https://github.com/thienph3/olympic-informatics-vietnam.git

echo "✅ Đã reset Git config"
echo "🔑 Bây giờ hãy:"
echo "1. Tạo repository trên GitHub (nếu chưa có)"
echo "2. Tạo Personal Access Token mới"
echo "3. Chạy: git push -u origin main"
```

## 📋 Checklist khắc phục:

- [ ] **Repository đã tồn tại** trên GitHub
- [ ] **Token đã được tạo** với scope `repo`
- [ ] **Token chưa hết hạn** và đang active
- [ ] **Username chính xác**: `thienph3`
- [ ] **URL chính xác**: `https://github.com/thienph3/olympic-informatics-vietnam.git`

## 🎯 Sau khi khắc phục:

```bash
# Test push
git push -u origin main

# Nếu thành công sẽ thấy:
# Enumerating objects: xxx, done.
# Counting objects: 100% (xxx/xxx), done.
# Writing objects: 100% (xxx/xxx), xxx KiB | xxx MiB/s, done.
# Total xxx (delta x), reused x (delta x), pack-reused x
# To https://github.com/thienph3/olympic-informatics-vietnam.git
#  * [new branch]      main -> main
```

## 🆘 Vẫn lỗi?

1. **🔄 Thử SSH thay vì HTTPS:**
   ```bash
   git remote set-url origin git@github.com:thienph3/olympic-informatics-vietnam.git
   ```

2. **📞 Liên hệ để được hỗ trợ trực tiếp**

---

**🏆 Chúc bạn khắc phục thành công!**