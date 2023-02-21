from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def page(request, item):
    content = util.get_entry(item)
    if (content != None):
        content = util.convert_md_to_html(content)
    return render(request, "encyclopedia/wiki_page.html", {
        "page": item,
        "content": content
    })

