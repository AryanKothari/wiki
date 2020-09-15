from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from . import util

class NewEntryForm(forms.Form):
    title = forms.CharField(label="Title:")
    content = forms.CharField(label="Content:", widget=forms.Textarea(attrs={"rows":10, "cols":80}))

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def display_entry(request, title):
    return render(request, "encyclopedia/display_entry.html", {
       "title": title.capitalize(),
       "content": util.get_entry(title)
    })

def create_page(request):
    if request.method == "POST":
        form = NewEntryForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            util.save_entry(title, content)
            return HttpResponseRedirect(f'wiki/{title}')
        else:
            return render(request, "encyclopedia/create_page.html", {
                "form": form
            })
    else:
        return render(request, "encyclopedia/create_page.html", {
       "form": NewEntryForm()})       
