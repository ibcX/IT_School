"""" PROIECT: Downloads folder watcher
Pe acelasi nivel cu directorul Downloads se creeaza un director DownloadsClean, in el se creeaza
folderele Music, Pictures, Videos, Documents, Executables, Others. (automat la pornirea scriptului)
Scriptul urmareste folderul Downloads al uilizatorul curent.
La fiecare modificare se citeste continutul si apoi se face clasificarea si mutarea."""


import os
import shutil
from pathlib import Path
from datetime import datetime

DOWNLOADS_DIR = Path.home()/"Downloads"
DOWNLOADS_CLEAN = Path.home()/"Downloads_Clean"
MUSIC = DOWNLOADS_CLEAN/"Music"
PICTURES = DOWNLOADS_CLEAN/"Pictures"
VIDEOS = DOWNLOADS_CLEAN/"Videos"
DOCUMENTS = DOWNLOADS_CLEAN/"Documents"
EXECUTABLES = DOWNLOADS_CLEAN/"Executables"
OTHERS = DOWNLOADS_CLEAN/"Others"

DOWNLOADS_CLEAN.mkdir(parents=True, exist_ok=True)
MUSIC.mkdir(parents=True, exist_ok=True)
PICTURES.mkdir(parents=True, exist_ok=True)
VIDEOS.mkdir(parents=True, exist_ok=True)
DOCUMENTS.mkdir(parents=True, exist_ok=True)
EXECUTABLES.mkdir(parents=True, exist_ok=True)
OTHERS.mkdir(parents=True, exist_ok=True)

initial_time_delta = DOWNLOADS_DIR.stat().st_mtime
while True:
    if DOWNLOADS_DIR.stat().st_mtime != initial_time_delta:
        initial_time_delta = DOWNLOADS_DIR.stat().st_mtime
        print("Downloads folder has been modified.")
        for path in DOWNLOADS_DIR.glob("**/*"):
            if path.suffix in [".mp3", ".wav", ".m4a", "wma", ".aac"]:
                shutil.move(path, MUSIC)
                print(f"File {path.name} has been moved to {MUSIC} folder")
            elif path.suffix in [".jpeg", ".png", ".jpg", ".bmp", ".gif"]:
                shutil.move(path, PICTURES)
                print(f"File {path.name} has been moved to {PICTURES} folder")
            elif path.suffix in [".mov", ".avi", ".mp4", ".wmv", ".mkv"]:
                shutil.move(path, VIDEOS)
                print(f"File {path.name} has been moved to {VIDEOS} folder")
            elif path.suffix in [".docx", ".doc", ".xls", ".xlsx", ".txt", ".pdf"]:
                shutil.move(path, DOCUMENTS)
                print(f"File {path.name} has been moved to {DOCUMENTS} folder")
            elif path.suffix == ".exe":
                shutil.move(path, EXECUTABLES)
                print(f"File {path.name} has been moved to {EXECUTABLES} folder")
            else:
                shutil.move(path, OTHERS)
                print(f"File {path.name} has been moved to {OTHERS} folder")

