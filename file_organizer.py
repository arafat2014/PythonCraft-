import os
import shutil

def organize_files(folder_path):
    for file in os.listdir(folder_path):
        name, ext = os.path.splitext(file)
        ext_folder = ext[1:] if ext else 'others'
        os.makedirs(os.path.join(folder_path, ext_folder), exist_ok=True)
        shutil.move(os.path.join(folder_path, file), os.path.join(folder_path, ext_folder, file))

# Example
# organize_files('C:/Users/YourName/Downloads')
