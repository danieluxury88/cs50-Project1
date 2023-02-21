import re
import markdown2
import html2text
import random




from django.core.files.base import ContentFile
from django.core.files.storage import default_storage


def list_entries():
    """
    Returns a list of all names of encyclopedia entries.
    """
    _, filenames = default_storage.listdir("entries")
    return list(sorted(re.sub(r"\.md$", "", filename)
                for filename in filenames if filename.endswith(".md")))


def save_entry(title, content):
    """
    Saves an encyclopedia entry, given its title and Markdown
    content. If an existing entry with the same title already exists,
    it is replaced.
    """
    filename = f"entries/{title}.md"
    if default_storage.exists(filename):
        default_storage.delete(filename)
    include_title = '\n'.join(["#"+title, content])
    default_storage.save(filename, ContentFile(include_title))


def edit_entry(title, content):
    """
    Edits an encyclopedia entry, given its title and Markdown
    content.
    """
    filename = f"entries/{title}.md"
    if default_storage.exists(filename):
        default_storage.delete(filename)
    default_storage.save(filename, ContentFile(content))


def get_entry(title):
    """
    Retrieves an encyclopedia entry by its title. If no such
    entry exists, the function returns None.
    """
    try:
        f = default_storage.open(f"entries/{title}.md")
        return f.read().decode("utf-8")
    except FileNotFoundError:
        return None


def get_random_entry():
    """
    Returns a random entry from list_entries
    """
    return random.choice(list_entries())


def convert_md_to_html(content):
    return markdown2.markdown(content)


def convert_html_to_md(content):
    escaped_html = markdown2.markdown(content, extras=['safe-mode'])
    return html2text.html2text(escaped_html).strip()
