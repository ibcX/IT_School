

# https://docs.python.org/3/library/pathlib.html
# https://docs.python.org/3/library/shutil.html
# https://docs.python.org/3/library/datetime.html
# https://docs.python.org/3/library/os.html


# Linux
# /usr/bin/python


# Windows

 # C:\Windows\System32

# Absolute
#    C:\Users\Bogdan\Downloads\pic.jpeg

# Relative
#      practice.txt

from pathlib import Path

print(__file__)

ROOT = Path(__file__).parent
print(ROOT)
print(ROOT.is_file())

LOGS_DIR = ROOT/"logs"/"error"
print(LOGS_DIR)
print(LOGS_DIR.exists())

# create a DIR
LOGS_DIR.mkdir(parents=True, exist_ok=True)
print(LOGS_DIR.exists())

# create new file
OUTPUT_FILE = ROOT/"output.log"
with OUTPUT_FILE.open("w") as fout:
    fout.write("Test")

# se afiseaza fiecare fisier si director din path-ul respectiv - este iterabil
print(ROOT.iterdir())
for path in ROOT.iterdir():
    if path.is_dir():
        for path_2 in path.iterdir():
            print(path_2)
        print(path)
print("__________________________________")
# intra si in directoare si afiseaza toate fisierele si folderele sau doar un tip de fisiere (.log)
for path in ROOT.glob("**/*.log"):
    print(path)


print(OUTPUT_FILE.stat())

print("________________________________")

import shutil
# copiere si redenumire in acelasi timp
shutil.copy2(OUTPUT_FILE, LOGS_DIR/"log.log")
#
# # mutarea unui fisier
# shutil.move(OUTPUT_FILE, LOGS_DIR)
#
# # copiere recursiva (folder cu fisiere)
# shutil.copytree(LOGS_DIR, ROOT/"backup")
#
# # stergere recursiva
# shutil.rmtree(ROOT/"backup")

import os

print(os.getlogin())
print(os.getpid())  #process ID

from datetime import timedelta, date, time, datetime

now = datetime.now()
print(now.day)
print(now.month)
print(now.minute)
print(now.second)
print(now.timestamp())
ts1 = 1667242874.036118
dt1 = datetime.fromtimestamp(ts1)
print(dt1.year)

b_day = datetime(1993, 8, 28)
print(b_day)
print(now)
delta1 = now - b_day
print(delta1.total_seconds())

# https://strftime.org/