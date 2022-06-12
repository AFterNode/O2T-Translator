from utils.win32 import registry
import subprocess
from MixacLib import cons
import sys
import os

if __name__ == "__main__":
    print("Checking runtime environment...")
    python_installed = registry.python_installed()
    if not python_installed:
        print("Python not found, please install one")
        cons.pause()
        sys.exit()
    else:
        print("Python found.")

    print("Checking packages...")
    os.system("python -m pip install -r requirements.txt")

    print("Starting O2T...")

    O2T = subprocess.Popen("python .\\app\\main.py")
    O2T.wait()
    if O2T.returncode != 0:
        print("O2T exited with a non-zero code: " + str(O2T.returncode))
        cons.pause()
        sys.exit(O2T.returncode)
