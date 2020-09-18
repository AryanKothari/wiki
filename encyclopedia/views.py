from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from . import util
import random
import sys
from .forms import NewEntryForm, EditEntryForm



def index(request):
    all_entries = util.list_entries()
    rand_int = random.randint(0,len(all_entries)-1)
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        "rand_title": all_entries[rand_int],
        })

def display_entry(request, title):
    return render(request, "encyclopedia/display_entry.html", {
       "title": title.capitalize(),
       "content": util.get_entry(title)
    })

def edit_entry(request, title):
    if request.method == "POST":
        form = EditEntryForm(request.POST)
        if form.is_valid():
            content_new = form.cleaned_data['content_new']
            title = title.capitalize()
            util.save_entry(title, content_new)
            return HttpResponseRedirect(f'/wiki/{title}')
        else:
            return render(request, "encyclopedia/edit_entry.html", {
                "form": form,
                "content_current": util.get_entry(title),
            })
    else:
         return render(request, "encyclopedia/edit_entry.html", {
             "content_current": util.get_entry(title),
             "form": EditEntryForm({'content_new': util.get_entry(title)}),
             "title": title.capitalize()
        })

def create_entry(request):
    if request.method == "POST":
        form = NewEntryForm(request.POST)
        all_titles = util.list_entries()
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            if not title.capitalize() in all_titles:
                util.save_entry(title, content)
            return HttpResponseRedirect(f'wiki/{title}')
        else:
            return render(request, "encyclopedia/create_entry.html", {
                "form": form
            })
    else:
        return render(request, "encyclopedia/create_entry.html", {
       "form": NewEntryForm()
       })

def random_page(request):
    return True
