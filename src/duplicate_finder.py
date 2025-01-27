import hashlib
import os

def get_file_hash(file_path):
    """Berechnet den SHA256-Hash einer Datei."""
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        # Lese die Datei in Blöcken, um Speicher zu sparen
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def find_duplicates(directory_path):
    """Findet doppelte Dateien im angegebenen Verzeichnis und gibt sie als Liste zurück."""
    seen_hashes = {}
    duplicates = []

    # Durchlaufe alle Dateien im Verzeichnis und seine Unterverzeichnisse
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            file_hash = get_file_hash(file_path)

            # Wenn der Hash bereits gesehen wurde, ist dies ein Duplikat
            if file_hash in seen_hashes:
                duplicates.append((seen_hashes[file_hash], file_path))
            else:
                seen_hashes[file_hash] = file_path

    return duplicates

def show_and_remove_duplicates(directory_path):
    """Findet Duplikate und gibt dem Benutzer die Möglichkeit, sie zu entfernen."""
    duplicates = find_duplicates(directory_path)

    if not duplicates:
        print("Keine doppelten Dateien gefunden.")
        return

    print("Doppelte Dateien gefunden:\n")
    for index, (original, duplicate) in enumerate(duplicates, 1):
        print(f"{index}. {original} == {duplicate}")
    
    print("\nGeben Sie die Nummer der Duplikate ein, die Sie löschen möchten (oder 'q' zum Abbrechen):")

    user_input = input().strip()
    
    if user_input.lower() == 'q':
        print("Vorgang abgebrochen.")
        return

    try:
        indices_to_delete = [int(i) - 1 for i in user_input.split(',') if i.isdigit()]
    except ValueError:
        print("Ungültige Eingabe.")
        return

    for index in indices_to_delete:
        if 0 <= index < len(duplicates):
            duplicate = duplicates[index][1]
            try:
                os.remove(duplicate)
                print(f"Duplikat entfernt: {duplicate}")
            except OSError as e:
                print(f"Fehler beim Löschen der Datei {duplicate}: {e}")
        else:
            print(f"Ungültige Nummer {index + 1}")
