from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def page(request, page):
    content = util.get_entry(page)
    if (content == None):
        print ("error")
    else:
        return render(request, "encyclopedia/wiki_page.html", {
            "page":page,
            "content": content
        })

