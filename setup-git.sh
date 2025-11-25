#!/bin/bash

# Setup Git Repository for Olympic Informatics Vietnam
echo "🚀 Setting up Git repository for Olympic Informatics Vietnam..."

# Initialize git if not already initialized
if [ ! -d ".git" ]; then
    echo "📁 Initializing Git repository..."
    git init
else
    echo "✅ Git repository already initialized"
fi

# Add remote origin
echo "🔗 Adding remote origin..."
git remote remove origin 2>/dev/null || true
git remote add origin https://github.com/thienph3/olympic-informatics-vietnam.git

# Create .gitignore if not exists
if [ ! -f ".gitignore" ]; then
    echo "📝 Creating .gitignore..."
    cat > .gitignore << EOF
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# IDE
.vscode/settings.json
.vscode/launch.json
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
.DS_Store?
._*
.Spotlight-V100
.Trashes
ehthumbs.db
Thumbs.db

# Logs
*.log
debug.log

# Temporary files
*.tmp
*.temp
*.backup

# Test outputs
test_output/
temp_files/
EOF
fi

# Add all files
echo "📦 Adding files to Git..."
git add .

# Commit
echo "💾 Creating initial commit..."
git commit -m "🎯 Initial commit: Olympic Informatics Vietnam - Month 1 Complete

✅ Features:
- Complete Month 1 curriculum (Day 1-12)
- 94 practice problems with solutions
- Comprehensive Python fundamentals
- From zero to Olympic-ready foundation

📚 Content:
- Python basics, data types, I/O
- Control structures and loops
- Lists, tuples, strings
- Functions and recursion
- Modules, file I/O, error handling
- Debugging and testing

🎯 Ready for Month 2: Algorithms and Data Structures"

# Set main branch
echo "🌟 Setting main branch..."
git branch -M main

# Push to GitHub
echo "🚀 Pushing to GitHub..."
echo "⚠️  You may need to authenticate with GitHub..."
echo "💡 If prompted, use your GitHub username and personal access token"

git push -u origin main

echo ""
echo "🎉 Setup complete!"
echo "📍 Repository URL: https://github.com/thienph3/olympic-informatics-vietnam"
echo ""
echo "📋 Next steps:"
echo "1. Visit the repository on GitHub"
echo "2. Add a description and topics"
echo "3. Enable GitHub Pages if needed"
echo "4. Start working on Month 2 content"
echo ""
echo "🏆 Happy coding for Olympic Informatics!"