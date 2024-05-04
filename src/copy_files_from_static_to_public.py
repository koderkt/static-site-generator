import os
import shutil


def copy_files_from_static_to_public(source_dir_path, dest_dir_path):
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)
    for file in os.listdir(source_dir_path):
        souce_path = os.path.join(source_dir_path, file)
        dest_path = os.path.join(dest_dir_path, file)
        print(f"{souce_path} ------------> {dest_path}")
        if os.path.isfile(souce_path):
            shutil.copy(souce_path, dest_path)
        else:
            copy_files_from_static_to_public(souce_path, dest_path)
