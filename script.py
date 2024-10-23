import os
import shutil
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Get the directory path from the environment variable
directory_path = os.getenv('DIRECTORY_PATH')

# Check if the directory_path is set correctly
if directory_path is None:
    raise ValueError("DIRECTORY_PATH not set in .env file")

def organize_files(directory_path, file_types):
    try:
        # Lese das angegebene Verzeichnis
        items = os.listdir(directory_path)
    except OSError as e:
        print(f'Error reading directory: {e}')
        return

    other_folder = os.path.join(directory_path, 'other')
    if not os.path.exists(other_folder):
        os.makedirs(other_folder)

    # Dateien organisieren
    for item in items:
        item_path = os.path.join(directory_path, item)

        if os.path.isfile(item_path):
            file_ext = os.path.splitext(item)[1].lower()
            file_type_folder = file_ext[1:] if file_ext in file_types else 'other'

            # Erstelle den Ordner für den Dateityp, falls er nicht existiert
            file_type_folder_path = os.path.join(directory_path, file_type_folder)
            if not os.path.exists(file_type_folder_path):
                os.makedirs(file_type_folder_path)

            # Verschiebe die Datei in den entsprechenden Ordner
            old_path = item_path
            new_path = os.path.join(file_type_folder_path, item)

            try:
                shutil.move(old_path, new_path)
                print(f'Moved {item} to {file_type_folder}')
            except OSError as e:
                print(f'Error moving file {item} to {file_type_folder}: {e}')

def move_folders_up(directory):
    try:
        # Lese das angegebene Verzeichnis
        items = os.listdir(directory)
    except OSError as e:
        print(f'Error reading directory: {e}')
        return

    for item in items:
        item_path = os.path.join(directory, item)

        # Überprüfe, ob es sich um ein Verzeichnis handelt
        if os.path.isdir(item_path):
            new_path = os.path.join(directory, '..', item)

            try:
                shutil.move(item_path, new_path)
                print(f'Moved folder {item} up')
            except OSError as e:
                print(f'Error moving folder {item} up: {e}')

if __name__ == "__main__":
    file_types = ['.pdf', '.png', '.jpg', '.svg', '.zip', '.mp4']

    organize_files(directory_path, file_types)
    # Optional: Aufrufen, um Ordner nach oben zu verschieben
    # move_folders_up(directory_path)
