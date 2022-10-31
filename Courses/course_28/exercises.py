
#
# 1. Scrie un script care creeaza un fisier text. In fisierul text trebuie sa se regaseasca
# o lista cu toate fisierele dll din directoru C:\Windows\System32

from pathlib import Path

ROOT = Path("C:\Windows\System32")
ROOT_2 = Path(__file__).parent

OUTPUT_FILE = ROOT_2/"dll_files.txt"

# with OUTPUT_FILE.open("w") as dll_file:
#     for path in ROOT.glob("**/*.dll"):
#         dll_file.write(f"{path}\n")

print("________________________________")

# watcher
# time-stamp TS
# numarul de secunde de la Epoch Time - 01.01.1970

import time

DOWNLOADS_DIR = Path.home()/"Downloads"
print(time.time())
print(DOWNLOADS_DIR.is_dir())
for path in DOWNLOADS_DIR.iterdir():
    print(path)

initial_time_delta = DOWNLOADS_DIR.stat().st_mtime
while True:
    if DOWNLOADS_DIR.stat().st_mtime != initial_time_delta:
        initial_time_delta = DOWNLOADS_DIR.stat().st_mtime
        print("Folderul downloads s-a modificat")







