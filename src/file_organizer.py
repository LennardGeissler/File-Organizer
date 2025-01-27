import os
import shutil
from categories import file_categories as categories

def organize_files(directory_path, file_types):
    """Organisiert Dateien in einer tieferen Struktur basierend auf ihrem Dateityp."""
    
    try:
        # Lese das angegebene Verzeichnis
        items = os.listdir(directory_path)
    except OSError as e:
        print(f'Error reading directory: {e}')
        return

    # Gehe durch alle Kategorien und erstelle sie, falls noch nicht vorhanden
    for category, extensions in categories.items():
        category_folder = os.path.join(directory_path, category)
        if not os.path.exists(category_folder):
            os.makedirs(category_folder)

    # Durchlaufe alle Dateien und verschiebe sie entsprechend ihrer Kategorie
    for item in items:
        item_path = os.path.join(directory_path, item)

        if os.path.isfile(item_path):
            file_ext = os.path.splitext(item)[1].lower()
            moved = False

            # Bestimme die Kategorie basierend auf der Dateiendung
            for category, extensions in categories.items():
                if file_ext in extensions:
                    category_folder = os.path.join(directory_path, category)
                    new_path = os.path.join(category_folder, item)

                    try:
                        shutil.move(item_path, new_path)
                        print(f'Moved {item} to {category}')
                        moved = True
                        break

                    except OSError as e:
                        print(f'Error moving file {item} to {category}: {e}')
                        continue
            
            # Wenn die Datei in keine der Kategorien passt, verschiebe sie in "Other"
            if not moved:
                other_folder = os.path.join(directory_path, 'Other')
                new_path = os.path.join(other_folder, item)

                try:
                    shutil.move(item_path, new_path)
                    print(f'Moved {item} to Other')
                except OSError as e:
                    print(f'Error moving file {item} to Other: {e}')
