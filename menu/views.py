from django.shortcuts import render
from django.http import HttpResponse
from .models import item, menuSection, design

def show_menu(request):
    a = set(item.objects.all())
    a_sections = set(map(lambda x: x.section.id, a))
    sections = menuSection.objects.filter(id__in=a_sections)

    #1 in sections

    menu_positions = item.objects.all()


    designn  = design.objects.first()
    return render(request, 'menu.html',{'all_items':menu_positions, 'all_sections':sections, 'design':designn})

# , 'all_not_empty':not_empty_sections