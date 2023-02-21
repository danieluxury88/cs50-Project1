from django.shortcuts import render
from django.contrib import messages

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


def search(request):
    page_search = request.POST['q']
    page_search_content = util.get_entry(page_search)
    if (page_search_content != None):
        return page(request, page_search)
    else:
        similar_entries = []
        entry_list = util.list_entries()
        for entry in entry_list:
            if page_search.lower() in entry.lower():
                similar_entries.append(entry)
        return render(request, "encyclopedia/search_page.html", {
            "similar_entries": similar_entries
        })

def new_page(request):
    if request.method == "GET":
        return render(request, "encyclopedia/new_page.html")
    else:
        title = request.POST['title']
        if (util.get_entry(title) is None):
            util.save_entry(title, request.POST['content'])
            return page(request, title)
        else:
            messages.warning(request, 'Entry already exists')
            return render(request, "encyclopedia/new_page.html")
