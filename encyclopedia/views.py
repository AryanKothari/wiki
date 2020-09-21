from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from . import util
import random
import sys
from .forms import NewEntryForm, EditEntryForm
import markdown2



def index(request):
    all_entries = util.list_entries()
    rand_int = random.randint(0,len(all_entries)-1)
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        "rand_title": all_entries[rand_int],
        })

def display_entry(request, title):
    if title in util.list_entries():
        title = title.capitalize()
    else:
        title = ""
    return render(request, "encyclopedia/display_entry.html", {
       "title": title,
       "content": markdown2.markdown(util.get_entry(title))
    })

def search_results(request):
    if request.method == "GET":
        query = request.GET.get('q', None)
        query = query.capitalize()
        matching_substrings = []
        all_entries = util.list_entries()
        if query in all_entries:
            return HttpResponseRedirect(f'/wiki/{query}')
        else:
            for entry in all_entries:
                if query.capitalize() in entry:
                    matching_substrings.append(entry)
            return render(request, "encyclopedia/search_results.html", {
                "entries": matching_substrings
            })
    else:
        return render(request, "encyclopedia/search_results.html", {
            "entries": matching_substrings
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
            title = title.capitalize()
            content = form.cleaned_data['content']
            if not title.capitalize() in all_titles:
                util.save_entry(title, content)
                return HttpResponseRedirect(f'wiki/{title}')
            else: 
                return render(request, "encyclopedia/create_entry.html", {
                "form": form,
                "give_error": True
            })    
        else:
            return render(request, "encyclopedia/create_entry.html", {
                "form": form
            })
    else:
        return render(request, "encyclopedia/create_entry.html", {
       "form": NewEntryForm()
       })

def random_entry(request):
    all_entries = util.list_entries()
    rand_int = random.randint(0,len(all_entries)-1)
    return HttpResponseRedirect(f'/wiki/{all_entries[rand_int]}')
