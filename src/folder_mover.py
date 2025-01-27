import os
import shutil
from categories import folder_categories as categories

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
                
def move_existing_folders_to_category(directory_path):
    """Verschiebt bereits existierende Ordner, die sich nicht im richtigen Kategorie-Ordner befinden, dorthin."""
    
    # Gehe jede Kategorie durch und verschiebe die Ordner
    for category, extensions in categories.items():
        category_folder = os.path.join(directory_path, category)

        # Stelle sicher, dass der Kategorie-Ordner existiert
        if not os.path.exists(category_folder):
            os.makedirs(category_folder)

        # Durchlaufe alle Ordner im Hauptverzeichnis
        for item in os.listdir(directory_path):
            item_path = os.path.join(directory_path, item)

            # Überprüfe, ob es sich um einen Ordner handelt
            if os.path.isdir(item_path):
                # Prüfe, ob der Ordnername einer der Dateitypen der Kategorie entspricht
                # Hier vergleichen wir den Ordnernamen mit den Extensions (Dateiendungen)
                for ext in extensions:
                    if ext.lower() in item.lower():  # Verwendet den Ordnernamen ohne Punkt
                        # Wenn der Ordner nicht bereits im richtigen Kategorie-Ordner ist
                        if item_path != category_folder:
                            try:
                                shutil.move(item_path, os.path.join(category_folder, item))
                                print(f'Moved folder {item} to {category}')
                            except OSError as e:
                                print(f'Error moving folder {item} to {category}: {e}')
                        break
