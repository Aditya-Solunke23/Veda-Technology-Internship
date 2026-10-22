
from pathlib import Path
import shutil

print("========================================")
print("            FILE ORGANIZER")
print("========================================")


def get_unique_path(destination):
    """Return a unique destination path if a filename already exists."""
    if not destination.exists():
        return destination

    counter = 1
    while True:
        new_destination = destination.with_name(
            f"{destination.stem}_{counter}{destination.suffix}"
        )
        if not new_destination.exists():
            return new_destination
        counter += 1


def organize_files(folder_path):
    folder = Path(folder_path).expanduser()

    if not folder.exists():
        print("Error: The specified folder does not exist.")
        return

    if not folder.is_dir():
        print("Error: The specified path is not a directory.")
        return

    organized_count = 0
    skipped_count = 0

    for item in folder.iterdir():
        # Only organize files directly inside the selected folder.
        if not item.is_file():
            continue

        # Files without extensions go into the No Extension folder.
        extension = item.suffix.lower().lstrip(".")
        category = extension if extension else "No Extension"

        destination_folder = folder / category
        destination_folder.mkdir(exist_ok=True)

        destination = get_unique_path(destination_folder / item.name)

        try:
            shutil.move(str(item), str(destination))
            print(f"Moved: {item.name} -> {category}/{destination.name}")
            organized_count += 1
        except OSError as error:
            print(f"Could not move {item.name}: {error}")
            skipped_count += 1

    print("\n========== ORGANIZATION SUMMARY ==========")
    print(f"Files organized : {organized_count}")
    print(f"Files skipped   : {skipped_count}")
    print("===========================================")


try:
    folder_input = input(
        "\nEnter the path of the folder to organize: "
    ).strip()

    if not folder_input:
        print("Error: Folder path cannot be empty.")
    else:
        organize_files(folder_input)

except PermissionError:
    print("Error: You do not have permission to access this folder.")
except OSError as error:
    print(f"Filesystem error: {error}")
