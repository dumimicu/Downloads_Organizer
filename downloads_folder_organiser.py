import os
import shutil

file_categories = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".avi", ".mkv"],
    "Applications": [".exe"],
    "Torrents": [".torrent"],
    "Others": []
}


def organize_downloads_folder():
    downloads_path = os.path.expanduser("~/Downloads")
    for filename in os.listdir(downloads_path):
        if os.path.isfile(os.path.join(downloads_path, filename)):
            file_extension = os.path.splitext(filename)[1].lower()
            target_folder = None

            for category, extensions in file_categories.items():
                if file_extension in extensions:
                    target_folder = os.path.join(downloads_path, category)
                    break

            if target_folder is None:
                target_folder = os.path.join(downloads_path, "Others")

            if not os.path.exists(target_folder):
                os.makedirs(target_folder)

            source_file = os.path.join(downloads_path, filename)
            destination_file = os.path.join(target_folder, filename)

            shutil.move(source_file, destination_file)
            print(f"Moved {filename} to {target_folder}")


if __name__ == "__main__":
    print("Starting Downloads Organizer...")
    organize_downloads_folder()
    print("Done! You have organized your messy Downloads folder! ")
    print("Don't forget to move/save/backup or delete files from there to maintained it clean")
    print("Or RUN this script from time to time,it's easier! :) ")
