@echo off
@echo Packaging launcher EXE...
pyinstaller -F launcher.py

@echo Copying utils...
xcopy .\utils .\Release\app\utils
xcopy .\utils\translator .\Release\app\utils\translator
xcopy .\utils\win32 .\Release\app\utils\win32

@echo Copying application...
copy .\main.py .\Release\app
copy .\mainwindow.py .\Release\app
copy .\window.py .\Release\app
copy .\requirements.txt .\Release

@echo Copying launcher...
copy .\dist\launcher.exe .\Release
