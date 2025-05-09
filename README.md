minecraft-modpack-setup-wizard-creator
This project provides the source code for a simple Minecraft mod pack installer built using Python 3.13. The installer automates the process of downloading, extracting, and installing mod packs from Google Drive to the appropriate Minecraft directory.

Features:
Google Drive Integration: Downloads mod pack ZIP files directly from a provided Google Drive link.

Automatic Installation: Extracts the ZIP contents and moves them to the correct versions directory in your .minecraft folder.

Graphical User Interface (GUI): A simple, user-friendly interface built with Tkinter, which shows progress during the installation.

Customizable: Allows users to input their own mod pack name and Google Drive file ID, making it adaptable to different mod packs.

Requirements:
To run this project, you need:

Python 3.13 or higher.

Tkinter: A GUI library used in this project.

gdown: Python library to download files from Google Drive.

Installation:
To set up and run the project, follow these steps:

Install Python 3.13:
Ensure you have Python 3.13 or higher installed on your machine. You can download Python from the official website: https://www.python.org/downloads/.

Install Dependencies:
Open your terminal or command prompt and run the following commands to install the required libraries:

'pip install tkinter' and 'pip install gdown'

Customize the Script:

Open the mod_installer.py file.

Modify the mod_name variable with the name of your mod pack.

Replace the file_id variable with the ID of the Google Drive file link for your mod pack.

Optionally, you can change the GUI text or customize the installer’s behavior.

Run the Installer:
After customization, run the script with the following command:

'modpack_setup_wizard_template.py'

Usage:
Step 1: The user is prompted to input the mod pack name and Google Drive file ID.

Step 2: The script will download the .zip file from the provided Google Drive link.

Step 3: The contents of the ZIP file will be extracted to the correct Minecraft directory.

Step 4: The mod pack will be installed and ready to use in the versions directory of your .minecraft folder.

DISCLAIMER:
This project is provided as-is and without warranty of any kind.
The creator is not liable for any damage or loss arising from the use or modification of this code.
Use at your own risk.

License:
This project is licensed under the CC BY-NC-SA 4.0 License. You may modify and share the code, but you cannot use it for commercial purposes. Any modifications made to this project should also be licensed under the same terms and must attribute the original author.

You can find the full text of the license here: CC BY-NC-SA 4.0 License.

Contributing:
If you'd like to contribute to the project, feel free to fork this repository, make changes, and create a pull request. Any contributions are welcome!
