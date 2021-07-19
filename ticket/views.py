from django.conf import settings
from django.shortcuts import render,redirect,HttpResponse

def home(request):
    return HttpResponse(_generate_google_address('Space+Needle,Seattle+WA'))

def _generate_google_address(address):
    modified_address = address.replace(' ', '%20')
    return f"https://www.google.com/maps/embed/v1/place?q={modified_address}&key={settings.MAPS_EMBED_KEY}"
