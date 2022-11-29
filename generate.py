import os
import shutil
import markdown

def generate_index():
    with open('index.html') as f:
        index_contents = f.read()

    with open('static/index.html', mode='w') as f:
        f.write(index_contents)

def generate():
    """
    Generate html content from Markdown files and assets in content/ directory
    """
    # Generate index.html
    generate_index()

    if not os.path.exists('static/'):
        os.mkdir('static/')
    if not os.path.exists('static/assets/'):
        os.mkdir('static/assets/')

    for root, dirs, files in os.walk('content/'):
        # In content/ directory, take each markdown file and create a blog entry based on it
        if root == 'content/':
            for f in files:
                if f.split('.')[-1] == 'md':
                    blog_entry_html = markdown.markdownFromFile(input=root + f, output='static/' + f + '.html')
        print(root)
        # Copy all files in content/assets/ to the assets/ directory of the static website
        if root == 'content/assets':
            for f in files:
                shutil.copy(root + '/' + f, 'static/assets/' + f)
