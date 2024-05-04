# from htmlnode import HTMLNode
import os
import shutil
from copy_files_from_static_to_public import copy_files_from_static_to_public
from generate_page import generate_page


source_path = "./static"
dest_path = "./public"
dir_path_content = "./content"
template_path = "./template.html"


def main():
    print("Deleting public directory....")

    if os.path.exists(dest_path):
        shutil.rmtree(dest_path)
    print("Copying static files to public directory....")
    copy_files_from_static_to_public(source_path, dest_path)

    print("Generating page...")
    generate_page(
        os.path.join(dir_path_content, "index.md"),
        template_path,
        os.path.join(dest_path, "index.html"),
    )


main()
