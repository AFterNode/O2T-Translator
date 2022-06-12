import win32api
import win32con
from win32ctypes.pywin32 import pywintypes


def find_path(name="CST DESIGN ENVIRONMENT_AMD64.exe"):
    path = None
    key = rf'SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\{name}'

    key = win32api.RegOpenKey(win32con.HKEY_LOCAL_MACHINE, key, 0, win32con.KEY_READ)
    info2 = win32api.RegQueryInfoKey(key)
    for j in range(0, info2[1]):
        key_value = win32api.RegEnumValue(key, j)[1]
        if key_value.upper().endswith(name.upper()):
            path = key_value
            break
    win32api.RegCloseKey(key)
    return path

def python_installed():
    try:
        name = r"SOFTWARE\Python\PythonCore"
        key = win32api.RegOpenKey(win32con.HKEY_LOCAL_MACHINE, name)
        return True
    except Exception as e:
        return False


if __name__ == "__main__":
    python_installed()
