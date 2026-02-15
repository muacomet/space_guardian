#!/bin/bash
# Space Guardian Auto-Deployment Script
# Usage: ./deploy.sh

SERVER="192.168.0.40"
USER="muaco"
PASS="950315"
TARGET_DIR="~/space_guardian"

echo "🚀 Deploying Space Guardian to $SERVER..."

# Check if sshpass is installed
if ! command -v sshpass &> /dev/null; then
    echo "⚠️  sshpass not found. Installing via Homebrew..."
    if command -v brew &> /dev/null; then
        brew install hudochenkov/sshpass/sshpass
    else
        echo "❌ Homebrew not found. Please install sshpass manually: brew install hudochenkov/sshpass/sshpass"
        exit 1
    fi
fi

# 1. Create Directory
echo "📂 Creating remote directory..."
sshpass -p "$PASS" ssh -o StrictHostKeyChecking=no $USER@$SERVER "mkdir -p $TARGET_DIR"

# 2. Upload Files
echo "VkUl Uploading game files..."
sshpass -p "$PASS" scp -o StrictHostKeyChecking=no index.html $USER@$SERVER:$TARGET_DIR/
sshpass -p "$PASS" scp -o StrictHostKeyChecking=no inject_assets.py $USER@$SERVER:$TARGET_DIR/
sshpass -p "$PASS" scp -o StrictHostKeyChecking=no README.md $USER@$SERVER:$TARGET_DIR/

# 3. Setup Web Server (Simple Python Server for testing)
echo "🌐 Starting temporary web server on port 8000..."
echo "👉 Game will be available at: http://$SERVER:8000"
sshpass -p "$PASS" ssh -o StrictHostKeyChecking=no $USER@$SERVER "cd $TARGET_DIR && nohup python3 -m http.server 8000 > server.log 2>&1 &"

echo "✅ Deployment Complete!"
