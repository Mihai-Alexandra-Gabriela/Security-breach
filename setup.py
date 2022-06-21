import sys
from cx_Freeze import, Executable

base = None

#Checking the version of Windows
if sys.platform == "Win32":
    base = "Win32GUI"

setup(name="client",
      version="0.1",
      description="backdoor",
      executables=[Executable("client.py", base=base)])