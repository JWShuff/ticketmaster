from django.conf import settings
from django.shortcuts import render,redirect,HttpResponse

def home(request):
    return render(request, 'home.html')

def _generate_google_address(address):
    modified_address = address.replace(' ', '%20')
    return f"https://www.google.com/maps/embed/v1/place?q={modified_address}&key={settings.MAPS_EMBED_KEY}"

def _generate_ticket_artist_search(artist):
    ticket_artist_search=artist
    return f"https://developer.ticketmaster.com/products-and-docs/apis/discovery-api/v2/"
