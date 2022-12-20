from django.shortcuts import render
from django.http import HttpResponse
from .models import items, menuSections, design

def show_menu(request):
    a = set(items.objects.all())
    a_sections = set(map(lambda x: x.section.id, a))
    
    sections = menuSections.objects.filter(id=3)

    #1 in sections

    menu_positions = items.objects.all()
    # not_empty_sections = items.all().menusections_set.all()
    # for i in items.objects.count():
    #     if 
    #     not_empty_sections = items.all().menusections_set.all()



    designn  = design.objects.all().first()
    if design.objects.all().first().style:
        return render(request, 'menu.html',{'all_items':menu_positions, 'all_sections':sections, 'design':designn})
    else:
        return render(request, 'menusecond.html',{'all_items':menu_positions, 'all_sections':sections, 'design':designn})

# , 'all_not_empty':not_empty_sections