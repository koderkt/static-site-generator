# from htmlnode import HTMLNode
import os
import shutil
from copy_files_from_static_to_public import copy_files_from_static_to_public
from generate_page import generate_page, generate_pages_recursively


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
    generate_pages_recursively(
        dir_path_content,
        template_path,
        dest_path,
    )


main()
