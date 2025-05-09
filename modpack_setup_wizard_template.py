# The name of the ZIP file must be the same as the name of the folder inside the ZIP file.
# To compile, use the command: 'pyinstaller --onefile --windowed --icon=logo.ico mod_installer.py'.
# Replace 'mod_installer.py' with the name of your source file, and replace 'logo.ico' with the name of your logo file.


import os
import zipfile
import shutil
import gdown
import tkinter as tk
import threading
import time

# Mod name variable
mod_name = "mod_pack_name"
file_id = "drive_file_id"
url = f"https://drive.google.com/uc?id={file_id}"

# Temporary folder
download_dir = os.path.join(os.getcwd(), 'temp_download')
os.makedirs(download_dir, exist_ok=True)

# .minecraft/versions directory (For Windows)
minecraft_versions_dir = os.path.join(os.environ['APPDATA'], '.minecraft', 'versions')
os.makedirs(minecraft_versions_dir, exist_ok=True)

def download_and_extract():
    zip_path = os.path.join(download_dir, f'{mod_name}.zip')
    gdown.download(url, zip_path, quiet=False)

    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(download_dir)

    source_path = os.path.join(download_dir, mod_name)
    target_path = os.path.join(minecraft_versions_dir, mod_name)

    if os.path.exists(target_path):
        shutil.rmtree(target_path)

    shutil.move(source_path, target_path)
    shutil.rmtree(download_dir)

def create_gui():
    root = tk.Tk()
    root.title("Mod Installing")
    root.geometry("600x300")
    root.configure(bg="#121212")

    label = tk.Label(root, text="", font=("Helvetica", 14), fg="#D4D4D4", bg="#121212", justify="center")
    label.place(relx=0.5, rely=0.5, anchor="center")

    poetry_lines = [
        "The installation begins, sparking anticipation.",
        "As files download, progress is made.",
        "With each step, the system gains stability.",
        "Every download brings us closer to completion."
    ]

    def show_poems():
        for line in poetry_lines:
            label.config(text=line)
            time.sleep(2)

    threading.Thread(target=show_poems, daemon=True).start()
    root.mainloop()

# Start GUI
threading.Thread(target=create_gui, daemon=True).start()

# Installation process
download_and_extract()
