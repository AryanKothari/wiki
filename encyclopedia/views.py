from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def display_entry(request, title):
    return render(request, "encyclopedia/display_entry.html", {
       "title": title.capitalize(),
       "content": util.get_entry(title)
    } 
        )
