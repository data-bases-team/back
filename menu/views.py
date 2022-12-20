from django.shortcuts import render
from django.http import HttpResponse
from .models import items, menuSections, design

def show_menu(request):
    menu_positions = items.objects.all()
    sections = menuSections.objects.all()
    # not_empty_sections = items.all().menusections_set.all()
    # for i in items.objects.count():
    #     if 
    #     not_empty_sections = items.all().menusections_set.all()



    designn  = design.objects.all().first()
    return render(request, 'menu.html',{'all_items':menu_positions, 'all_sections':sections, 'design':designn})
# , 'not_empty':not_empty_sections