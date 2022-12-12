from django.contrib import admin
from .models import items
from .models import menuSections
from .models import design
from django.utils.html import format_html
from django.contrib.sites.models import Site
#from django.contrib.redirects.models import Redirect


@admin.register(items)
class itemsAdmin(admin.ModelAdmin):
    def admin_image(self,obj):
        return format_html('<img src="{0}"  />'.format(obj.image.url))
    list_display = ('name', 'description','price','gramms','calories',)
    ordering = ('section',)
    search_fields = ('name', 'description',)
    list_filter = ('name', 'price', 'section',)
    fields = (('name','section'), 'description', ('gramms', 'calories'), 'price', ('image','admin_image'),)
    readonly_fields = ('admin_image',)

    

admin.site.unregister(Site)
#admin.site.register(Redirect)
admin.site.register(menuSections)
admin.site.register(design)
