from django.contrib import admin
from .models import item
from .models import menuSection
from .models import design
from .models import font
from django.utils.html import format_html
from django.contrib.sites.models import Site
from django.contrib.auth.models import Group, User

admin.site.register(menuSection)

@admin.register(item)
class itemsAdmin(admin.ModelAdmin):
    def admin_image(self,obj):
        return format_html('<img src="{0}"  />'.format(obj.image.url))
    list_display = ('name', 'description','price','gramms','calories',)
    ordering = ('section',)
    search_fields = ('name', 'description',)
    list_filter = ('name', 'price', 'section',)
    fields = (('name','section'), 'description', ('gramms', 'calories'), 'price', ('image','admin_image'),)
    readonly_fields = ('admin_image',)

@admin.register(font)
class fontsAdmin(admin.ModelAdmin):
    def example(self,obj):
        return format_html('<img src="{0}"  width="255" />'.format(obj.font.url))
    readonly_fields = ('example',)

@admin.register(design)
class designAdmin(admin.ModelAdmin):
    fields = (('cafename','headertxt'), ('bgheader', 'bgup', 'bgcenter', 'bgdown', 'bgpage', 'bgend'), ('font','fontcolor'), 'style',)

admin.site.unregister(Site)
admin.site.unregister(Group)
admin.site.unregister(User)


admin.site.site_header = 'Administration'

