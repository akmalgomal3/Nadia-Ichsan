from django.shortcuts import render

# Create your views here.
from django.template.defaultfilters import slugify

def process_name(request, name):
    # Replace hyphen with space
    formatted_name = name.replace('-', ' ')
    
    # Another way to format the string is by using slugify
    # formatted_name = slugify(name).replace('-', ' ')

    return render(request, 'index.html', {'formatted_name': formatted_name})