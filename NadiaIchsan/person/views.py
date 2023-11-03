from django.shortcuts import render

# Create your views here.
from django.template.defaultfilters import slugify

def process_name(request, name):
    formatted_name = name.replace('-', ' ')

    return render(request, './index.html', {'formatted_name': formatted_name})