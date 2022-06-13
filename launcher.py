from utils.win32 import registry
import subprocess
from MixacLib import cons
import sys
import os

if __name__ == "__main__":
    print("Checking runtime environment...")

    # 检查Python安装状态
    python_installed = registry.python_installed()
    if not python_installed:
        print("Python not found, please install one")
        cons.pause()
        sys.exit()
    else:
        print("Python found.")

    # 使用Pip自动检查支持库
    print("Checking packages...")
    os.system("python -m pip install -r requirements.txt")

    print("Starting O2T...")

    # 启动子进程
    O2T = subprocess.Popen("python .\\app\\main.py")
    O2T.wait()
    # 异常退出码处理
    if O2T.returncode != 0:
        print("O2T exited with a non-zero code: " + str(O2T.returncode))
        cons.pause()
        sys.exit(O2T.returncode)
