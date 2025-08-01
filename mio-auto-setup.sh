#!/bin/bash
# ==============================
#  Mio Local Agent 自動セットアップ
# ==============================

# 1️⃣ 依存パッケージのインストール
echo "[1/4] 必要パッケージをインストール中..."
sudo apt-get update -y
sudo apt-get install -y git python3 python3-pip

# 2️⃣ Python 仮想環境の作成
echo "[2/4] Python仮想環境を作成中..."
python3 -m venv venv
source venv/bin/activate

# 3️⃣ 必要なPythonライブラリをインストール
echo "[3/4] Pythonライブラリをインストール中..."
pip install --upgrade pip
pip install requests flask openai

# 4️⃣ 設定完了メッセージ
echo "[4/4] セットアップ完了！"
echo "-----------------------------------"
echo "Mio Local Agentを起動するには以下を実行してください:"
echo "source venv/bin/activate && python3 backend/server.py"
echo "-----------------------------------"
