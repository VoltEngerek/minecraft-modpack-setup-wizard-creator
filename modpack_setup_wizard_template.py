##To compile 'pyinstaller --onefile --console --icon=logo.ico file_name.py'
##Change file_name to the name of the source code. Make the logo.ico file what you want to appear in your .exe file, 'important; the logo file must be in .ico format.'
##Made By VoltEngerek

import os
import zipfile
import shutil
import gdown

# Settings
mod_name = "DegisikCraft"  # ZIP and the folder inside must have the same name
file_id = "1b0SnHOvXGMH3uPLn7uBuZt5vcwhmhEPP"  # Put the Drive file ID here
url = f"https://drive.google.com/uc?id={file_id}"

# Paths
download_dir = os.path.join(os.getcwd(), 'temp_download')
zip_path = os.path.join(download_dir, f"{mod_name}.zip")
extract_dir = os.path.join(download_dir, 'extracted')
target_dir = os.path.join(os.environ['APPDATA'], '.minecraft', 'versions', mod_name)

# 1. Create temporary folders
os.makedirs(download_dir, exist_ok=True)
os.makedirs(extract_dir, exist_ok=True)

print(f"[1] Downloading ZIP: {zip_path}")
gdown.download(url, zip_path, quiet=False)

print(f"[2] Extracting ZIP to: {extract_dir}")
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(extract_dir)

# 3. Source folder inside the ZIP
source_dir = os.path.join(extract_dir, mod_name)

if not os.path.exists(source_dir):
    print(f"[ERROR] Folder named '{mod_name}' not found inside the ZIP!")
    exit(1)

# 4. Delete the existing target folder if it exists
if os.path.exists(target_dir):
    print(f"[3] Removing old folder: {target_dir}")
    shutil.rmtree(target_dir)

# 5. Move the folder to the target directory
print(f"[4] Moving new version folder to: {target_dir}")
shutil.move(source_dir, target_dir)

# 6. Cleanup
print(f"[5] Cleaning up temporary files...")
os.remove(zip_path)
shutil.rmtree(download_dir)

print(f"[✔] Installation completed successfully: {target_dir}")