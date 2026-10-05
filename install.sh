#!/bin/bash
# Thinking Models Skill - 一键安装脚本
# 支持 macOS / Linux
# 用法:
#   首次安装（curl 管道）: curl -fsSL https://raw.githubusercontent.com/Hoodas101/thinking-models/main/install.sh | bash
#   本地克隆后执行:        bash install.sh
#   从已有目录复制:        bash install.sh --dir ~/.cc-switch/skills/thinking-models
#   覆盖已装版本(非交互):  bash install.sh --force

set -e

REPO_URL="https://github.com/Hoodas101/thinking-models.git"
SKILL_NAME="thinking-models"

# 解析可选参数（必须在任何 stdin 检测之前完成）
SOURCE_DIR="${SOURCE_DIR:-}"
FORCE=0
while [ $# -gt 0 ]; do
    case "$1" in
        --dir)
            SOURCE_DIR="$2"
            shift 2
            ;;
        --force)
            FORCE=1
            shift
            ;;
        *)
            echo "⚠️  未知参数: $1（忽略）"
            shift
            ;;
    esac
done

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
    if [ "$FORCE" = "1" ]; then
        echo "🔁 --force 指定，覆盖安装"
    elif [ -t 0 ]; then
        read -p "是否覆盖安装？(y/n): " -n 1 -r
        echo
        if [[ ! $REPLY =~ ^[Yy]$ ]]; then
            echo "❌ 已取消安装"
            exit 0
        fi
    else
        # 非交互且未指定 --force：绝不动已有安装
        echo "❌ 非交互模式下不覆盖已有安装。"
        echo "   更新方式一（symlink/clone 安装）: 更新源目录或 cd $SKILL_DIR && git pull"
        echo "   更新方式二（强制覆盖）:          bash install.sh --force"
        echo "   从本地仓库复制:                  bash install.sh --dir <仓库目录> --force"
        exit 1
    fi
    rm -rf "$SKILL_DIR"
fi

# 创建 skills 目录（如果不存在）
mkdir -p "$INSTALL_DIR"

# 安装方式：复制 / symlink / clone
if [ -n "$SOURCE_DIR" ]; then
    # 指定了源目录：校验后直接复制
    if [ ! -f "$SOURCE_DIR/SKILL.md" ]; then
        echo "❌ 源目录无效（未找到 SKILL.md）: $SOURCE_DIR"
        exit 1
    fi
    echo "📋 从 $SOURCE_DIR 复制..."
    mkdir -p "$SKILL_DIR"
    cp -R "$SOURCE_DIR/." "$SKILL_DIR/"
    rm -rf "$SKILL_DIR/.git"   # 复制安装不带 git 元数据，避免后续 git pull 误操作源仓库
elif [ -d "$HOME/.cc-switch/skills/$SKILL_NAME" ]; then
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
if [ -d "$SKILL_DIR/.git" ]; then
    echo "🔄 更新: cd $SKILL_DIR && git pull"
fi
echo "🗑️  卸载: rm -rf $SKILL_DIR"
