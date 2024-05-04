import os
from block_markdown import markdown_to_html_node


def extract_title(markdown):
    lines = markdown.split("\n")
    if not lines[0].startswith("# "):
        raise ValueError("No header")
    return lines[0][2:]


def generate_page(from_path, template_path, dest_path):
    print(
        f"Generating page from {from_path} to {dest_path} using {template_path}......."
    )
    with open(from_path) as f:
        markdown = f.read()

    with open(template_path) as f:
        template = f.read()

    parent_node = markdown_to_html_node(markdown=markdown)
    html = parent_node.to_html()

    title = extract_title(markdown)

    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    to_file = open(dest_path, "w")
    to_file.write(template)
