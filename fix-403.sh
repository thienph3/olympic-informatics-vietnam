#!/bin/bash

echo "🚨 Khắc phục lỗi 403 Permission Denied"
echo "======================================"

# Xóa credential cũ
echo "🔧 Xóa credential cũ..."
git config --global --unset credential.helper 2>/dev/null || true

# Xóa remote cũ và thêm lại
echo "🔗 Reset remote origin..."
git remote remove origin 2>/dev/null || true
git remote add origin https://github.com/thienph3/olympic-informatics-vietnam.git

# Kiểm tra status
echo "📊 Git status:"
git status --porcelain

echo ""
echo "✅ Đã reset Git configuration"
echo ""
echo "🎯 BƯỚC TIẾP THEO:"
echo "=================="
echo ""
echo "1. 🌐 TẠO REPOSITORY TRÊN GITHUB:"
echo "   👉 https://github.com/new"
echo "   📝 Repository name: olympic-informatics-vietnam"
echo "   ✅ Public"
echo "   ❌ KHÔNG chọn README, .gitignore, license"
echo ""
echo "2. 🔑 TẠO PERSONAL ACCESS TOKEN:"
echo "   👉 https://github.com/settings/tokens"
echo "   📝 Note: Olympic Informatics Vietnam"
echo "   ✅ Scope: repo (full control)"
echo ""
echo "3. 🚀 PUSH CODE:"
echo "   git push -u origin main"
echo ""
echo "   Khi Git hỏi:"
echo "   Username: thienph3"
echo "   Password: ghp_xxxxxxxxxxxxxxxxxxxx (token vừa tạo)"
echo ""
echo "🏆 Chúc bạn thành công!"