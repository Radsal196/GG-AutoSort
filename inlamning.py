import os
import shutil

# Ändra detta till den mapp du vill organisera
source_folder = r"C:\Users\Abdulrazzak Saleh\Downloads"



# Filtyper och tillhörande mappar
file_types = {
    "Bilder": [".jpg", ".jpeg", ".png", ".gif"],
    "Dokument": [".pdf", ".docx", ".txt", ".xlsx"],
    "Program": [".exe", ".msi"],
    "Zipfiler": [".zip", ".rar", ".7z"],
    "Kod": [".py", ".js", ".html", ".css"]
}

def create_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)

def organize_folder(folder):
    for filename in os.listdir(folder):
        filepath = os.path.join(folder, filename)
        if os.path.isfile(filepath):
            moved = False
            for folder_name, extensions in file_types.items():
                if filename.lower().endswith(tuple(extensions)):
                    target_folder = os.path.join(folder, folder_name)
                    create_folder(target_folder)
                    shutil.move(filepath, os.path.join(target_folder, filename))
                    moved = True
                    break
            if not moved:
                # Okända filer hamnar i "Övrigt"
                target_folder = os.path.join(folder, "Övrigt")
                create_folder(target_folder)
                shutil.move(filepath, os.path.join(target_folder, filename))

if __name__ == "__main__":
    organize_folder(source_folder)
    print("Klart! Filerna har organiserats.")
