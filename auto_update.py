import os
import subprocess
import time
import datetime
import signal

# リポジトリのパス（必要に応じて修正）
REPO_PATH = r"C:\Users\Administrator\Desktop\mio-local-agent"
SERVER_SCRIPT = os.path.join(REPO_PATH, "backend", "server.py")
PYTHON_PATH = r"C:\Users\Administrator\AppData\Local\Programs\Python\Python313\python.exe"

# サーバープロセスを保持
server_process = None

def log(message):
    with open(os.path.join(REPO_PATH, "auto_update.log"), "a", encoding="utf-8") as f:
        f.write(f"[{datetime.datetime.now()}] {message}\n")

def start_server():
    global server_process
    log("サーバーを起動中...")
    server_process = subprocess.Popen([PYTHON_PATH, SERVER_SCRIPT], cwd=REPO_PATH)

def stop_server():
    global server_process
    if server_process and server_process.poll() is None:
        log("サーバーを停止中...")
        server_process.terminate()
        try:
            server_process.wait(timeout=5)
        except subprocess.TimeoutExpired:
            server_process.kill()
    server_process = None

def git_pull():
    result = subprocess.run(["git", "pull"], cwd=REPO_PATH, capture_output=True, text=True)
    log(result.stdout + result.stderr)
    return "Already up to date" not in result.stdout

if __name__ == "__main__":
    log("===== 自動更新スクリプト開始 =====")
    while True:
        try:
            log("GitHubから更新確認中...")
            updated = git_pull()
            if updated:
                log("更新を検出。サーバーを再起動します。")
                stop_server()
                start_server()
            elif server_process is None:
                log("サーバーが未起動のため起動します。")
                start_server()
        except Exception as e:
            log(f"エラー: {e}")
        time.sleep(300)  # 5分ごとにチェック
