from django.shortcuts import render
from django.http import HttpResponse
from .models import item, menuSection, design

def show_menu(request):
    a = set(item.objects.all())
    a_sections = set(map(lambda x: x.section.id if x.status=='a' else -1, a))
    if -1 in a_sections:
        a_sections.remove(-1)
    sections = menuSection.objects.filter(id__in=a_sections)

    #1 in sections

    menu_positions = item.objects.all()


    designn  = design.objects.first()
    return render(request, 'menu.html',{'all_items':menu_positions, 'all_sections':sections, 'design':designn})

# , 'all_not_empty':not_empty_sections