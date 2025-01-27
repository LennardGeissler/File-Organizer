import os
import argparse
from dotenv import load_dotenv
from file_organizer import organize_files
from folder_mover import move_folders_up, move_existing_folders_to_category
from duplicate_finder import show_and_remove_duplicates

# Lade Umgebungsvariablen aus der .env-Datei
load_dotenv()

def parse_arguments():
    """Liest die Argumente aus der Kommandozeile."""
    parser = argparse.ArgumentParser(description="Organize files by type and move folders up.")
    parser.add_argument('--directory', type=str, help='Directory to organize')
    parser.add_argument('--move-folders', action='store_true', help='Move subfolders up')
    parser.add_argument('--file-types', type=str, help='Comma separated list of file types to organize (e.g. ".pdf,.png,.jpg")')
    parser.add_argument('--find-duplicates', action='store_true', help='Find and remove duplicate files')

    return parser.parse_args()

def main():
    args = parse_arguments()

    # Verwende das Verzeichnis aus den Argumenten oder lade es aus der .env-Datei
    directory_path = args.directory or os.getenv('DIRECTORY_PATH')
    if directory_path is None:
        raise ValueError("DIRECTORY_PATH not set in .env file or via argument.")

    # Die Dateitypen aus den Argumenten oder der Standardwert
    file_types = args.file_types.split(',') if args.file_types else ['.pdf', '.png', '.jpg', '.svg', '.zip', '.mp4']

    # Dateien organisieren
    organize_files(directory_path, file_types)
    
    # ggf. Ordner verschieben
    move_existing_folders_to_category(directory_path)
    
    if args.find_duplicates:
        show_and_remove_duplicates(directory_path)

    # Optional: Verschiebe Unterordner nach oben
    if args.move_folders:
        move_folders_up(directory_path)

if __name__ == "__main__":
    main()