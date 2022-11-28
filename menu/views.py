from django.shortcuts import render
from django.http import HttpResponse
from .models import items, menuSections

def show_menu(request):
    menu_positions = items.objects.all()
    sections = menuSections.objects.all()
    return render(request, 'menu.html',{'all_items':menu_positions, 'all_sections':sections})
