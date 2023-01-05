import os
import shutil
import markdown as md


def build_entry(source_file, header):
    '''Create a blog entry from the source file and the common header'''

    with open("content/" + source_file) as f:
        entry_html = md.markdown(
            f.read(), extensions=["fenced_code", "codehilite", "wikilinks"], extension_configs={
                "wikilinks": {
                    "end_url": ".html"
                }
            })

    out_file = "static/" + source_file.replace(".md", "") + ".html"
    with open(out_file, "w") as f:
        f.write(header)
        f.write(entry_html)
        f.write("</body></html>")


def generate():
    '''
    Generate html content from Markdown files and assets in content/ directory
    '''

    # Create output directory if it doesn't exist
    if not os.path.exists("static/"):
        os.mkdir("static/")
    if not os.path.exists("static/assets/"):
        os.mkdir("static/assets/")
    if not os.path.exists("static/style/"):
        os.mkdir("static/style/")

    # Store the common header
    with open("content/header.html") as f:
        header = f.read()

    for current_dir, dirs, files in os.walk("content/"):
        # In content/ directory, take each markdown file and create a blog
        # entry based on it
        if current_dir == "content/":
            for f in files:
                if f.split(".")[-1] == "md":
                    build_entry(f, header)

        # Copy all files in content/assets/ to the assets/ directory of the
        # static website
        if current_dir == "content/assets":
            for f in files:
                shutil.copy(current_dir + "/" + f, "static/assets/" + f)

        if current_dir == "content/style":
            shutil.copy(current_dir + "/styles.css", "static/style/styles.css")


if __name__ == "__main__":
    generate()
