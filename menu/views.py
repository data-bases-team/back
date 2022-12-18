from django.shortcuts import render
from django.http import HttpResponse
from .models import items, menuSections, design

def show_menu(request):
    menu_positions = items.objects.all()
    sections = menuSections.objects.all()
    designn  = design.objects.all()[:1].get()  
    return render(request, 'menu.html',{'all_items':menu_positions, 'all_sections':sections, 'design':designn})
