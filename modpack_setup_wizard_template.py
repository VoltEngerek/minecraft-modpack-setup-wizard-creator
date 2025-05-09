# zip dosyasının adıyla, zip dosyasının içindeki klasörün adı aynı olmalıdır.
# derleme için 'pyinstaller --onefile --windowed --icon=logo.ico mod_installer.py' komudunu kullan mod_installer.py kısmında mod_installeri .py kaynak dosyasının adı yap, logo içinse --icon=logo.ico yerinde logo yazan yeri, logonun ismiyle değiştir.


import os
import zipfile
import shutil
import gdown
import tkinter as tk
import threading
import time

# Mod adı değişkeni
mod_name = "mod_pack_name"
file_id = "drive_file_id"
url = f"https://drive.google.com/uc?id={file_id}"

# Geçici klasör
download_dir = os.path.join(os.getcwd(), 'temp_download')
os.makedirs(download_dir, exist_ok=True)

# .minecraft/versions klasörü (Windows için)
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
    root.title("Mod Kuruluyor")
    root.geometry("600x300")
    root.configure(bg="#121212")

    label = tk.Label(root, text="", font=("Helvetica", 14), fg="#D4D4D4", bg="#121212", justify="center")
    label.place(relx=0.5, rely=0.5, anchor="center")

    poetry_lines = [
        "Her yükleme, rûhuma bir şevk verip, gurbetteki bir dostun gülüşü gibi gönlümü aydınlatır.",
        "Zamanın yelinde savrulurken, her yeni dosya gönlümde bir bahar açar.",
        "Varlıkların her biri yüklenirken, kalbim bir parça daha huzur bulur, sükûneti arar.",
        "Her yükleme bir sefâ, her indirme bir elem taşır gönül sahrâsında."
    ]

    def show_poems():
        for line in poetry_lines:
            label.config(text=line)
            time.sleep(2)

    threading.Thread(target=show_poems, daemon=True).start()
    root.mainloop()

# GUI başlat
threading.Thread(target=create_gui, daemon=True).start()

# Kurulum işlemi
download_and_extract()
