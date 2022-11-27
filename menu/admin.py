from django.contrib import admin
from .models import items
from .models import menuSections

@admin.register(items)
class itemsAdmin(admin.ModelAdmin):
    list_display = ('name', 'description','price','gramms','calories',)
    ordering = ('section',)
    search_fields = ('name', 'description',)
    list_filter = ('name', 'price', 'section',)
    fields = (('name','section'), 'description', ('gramms', 'calories'), 'price', 'image')

admin.site.register(menuSections)
