""""3. Scrie o functie care afiseaza un mesaj de salut. Mesajul de salut trebuie sa contina numele utilzatorului
curent (se obtine cu modulul os) si cati GB (cu doua zecimale) ocupa directorul home. Ex: Salut mdinu!
Spatiu utilizat de tine: 4.55 GB"""

import os
from pathlib import Path
from datetime import datetime
import shutil


def hello():
    user_logged_in = os.getlogin()
    print(f"Salut {user_logged_in}!")
    HOME_DIR = Path.home()
    total_size = 0
    for path in HOME_DIR.glob("**/*"):
        total_size += path.stat().st_size
    print(f"The size occupied by the home folder is: {round(total_size / 1000000, 2)} GB")


# hello()

""""4. Scrie un script care face curatenie pe desktop. Cand executi scriptul toate fisierele (mai putin shortcuts)
vor fi mutate intr-un folder denumit de forma 2022-10-30_11-20 (ora data curenta). Noul folder creat
va sta intr-un folder definit de utilizator intr-un fisier de configurare. Fisierul de config se gaseste
pe acelasi nivel ca si scriptul si contine pe prima linie calea catre folderul parinte al arhivei."""

DESKTOP_PATH = Path.home() / "Desktop" / "Trash"
now = datetime.now()
folder_name = now.strftime("%Y""-""%m""-""%d""_""%H""-""%m")
FOLDER_PATH = Path.home() / "Desktop" / folder_name
FILE_PATH = Path(__file__).parent
CONFIG_FILE = FILE_PATH / "config_file.config"

with CONFIG_FILE.open("w") as config_file:
    config_file.write(f"{FOLDER_PATH}")

with CONFIG_FILE.open("r") as config_file:
    NEW_FOLDER_PATH = config_file.read()

NEW_FOLDER_PATH = Path(NEW_FOLDER_PATH)
NEW_FOLDER_PATH.mkdir(exist_ok=True)

for path in DESKTOP_PATH.glob("**/*"):
    if path.suffix != ".lnk":
        shutil.move(path, NEW_FOLDER_PATH)
