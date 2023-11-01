from django.urls import path
from person.views import process_name

app_name = 'person'

urlpatterns = [
    path('to=<str:name>', process_name, name='process_name'),
]
