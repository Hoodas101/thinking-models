#!/bin/bash
# Thinking Models Skill - 一键安装脚本
# 支持 macOS / Linux
# 用法: curl -fsSL https://raw.githubusercontent.com/Mihooni/thinking-models/main/install.sh | bash

set -e

REPO_URL="https://github.com/Mihooni/thinking-models.git"
SKILL_NAME="thinking-models"

# 检测操作系统
detect_os() {
    case "$(uname -s)" in
        Darwin)  echo "macOS" ;;
        Linux)   echo "Linux" ;;
        *)       echo "unknown" ;;
    esac
}

OS=$(detect_os)
echo "🔍 检测到操作系统: $OS"

# 确定安装目录
get_install_dir() {
    if [ -d "$HOME/.claude/skills" ]; then
        echo "$HOME/.claude/skills"
    elif [ -d "$HOME/.config/claude/skills" ]; then
        echo "$HOME/.config/claude/skills"
    else
        echo "$HOME/.claude/skills"
    fi
}

INSTALL_DIR=$(get_install_dir)
SKILL_DIR="$INSTALL_DIR/$SKILL_NAME"

# 检查是否已安装
if [ -d "$SKILL_DIR" ] || [ -L "$SKILL_DIR" ]; then
    echo "⚠️  检测到已安装版本: $SKILL_DIR"
    read -p "是否覆盖安装？(y/n): " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo "❌ 已取消安装"
        exit 0
    fi
    rm -rf "$SKILL_DIR"
fi

# 创建 skills 目录（如果不存在）
mkdir -p "$INSTALL_DIR"

# 安装方式：symlink 或 clone
if [ -d "$HOME/.cc-switch/skills/$SKILL_NAME" ]; then
    # 如果已有 cc-switch 中的副本，创建 symlink
    echo "🔗 创建 symlink..."
    ln -s "$HOME/.cc-switch/skills/$SKILL_NAME" "$SKILL_DIR"
else
    # 否则直接 clone
    echo "📦 克隆仓库..."
    git clone --depth 1 "$REPO_URL" "$SKILL_DIR"
fi

echo ""
echo "✅ 安装完成！"
echo ""
echo "📍 安装位置: $SKILL_DIR"
echo ""
echo "🚀 下一步："
echo "   1. 重启 Claude Code"
echo "   2. 试试问：'帮我分析一下该不该换工作'"
echo "   3. 或说：'用大白话简单说' 体验简洁模式"
echo ""
echo "📖 文档: $SKILL_DIR/README.md"
echo "🔄 更新: cd $SKILL_DIR && git pull"
echo "🗑️  卸载: rm $SKILL_DIR"
