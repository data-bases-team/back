from django.shortcuts import render
from django.http import HttpResponse
from .models import items

def show_menu(request):
    menu_positions = items.objects.all()
    return render(request, 'menu.html',{'all':menu_positions})
