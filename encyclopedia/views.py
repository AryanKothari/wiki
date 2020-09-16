from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from . import util
import sys


class NewEntryForm(forms.Form):
    title = forms.CharField(label="Title:")
    content = forms.CharField(label="Content:", widget=forms.Textarea(attrs={"rows":10, "cols":80}))

class EditEntryForm(forms.Form):
    content_new = forms.CharField(label="Content:", widget=forms.Textarea(attrs={"rows":10, "cols":80}))


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def display_entry(request, title):
    return render(request, "encyclopedia/display_entry.html", {
       "title": title.capitalize(),
       "content": util.get_entry(title)
    })

def edit_entry(request, title):
        return render(request, "encyclopedia/edit_entry.html", {
            "content_current": util.get_entry(title)
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
