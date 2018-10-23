from django.shortcuts import render
from .forms import IndexForm

def render_index(request):

    index_form = IndexForm()

    return render(request, "index.html", {'index_form': index_form})
