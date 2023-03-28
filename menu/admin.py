from django.contrib import admin
from .models import item
from .models import menuSection
from .models import design
from .models import font
from django.utils.html import format_html
from django.contrib.sites.models import Site
from django.contrib.auth.models import Group, User
#from .forms import CategoryForm

admin.site.register(menuSection)


@admin.action(description='Mark selected items as available')
def make_available(modeladmin, request, queryset):
    queryset.update(status='a')


@admin.action(description='Mark selected items as unavailable')
def make_unavailable(modeladmin, request, queryset):
    queryset.update(status='u')


@admin.register(item)
class itemsAdmin(admin.ModelAdmin):
    def admin_image(self, obj):
        return format_html(''.format(obj.image.url))

    list_display = ('name', 'description', 'price', 'gramms', 'calories', 'status')
    ordering = ('section',)
    search_fields = ('name', 'description',)
    list_filter = ('name', 'price', 'section',)
    fields = (('name','section'), 'description', ('gramms', 'calories'), 'price', ('image', 'admin_image'),)
    readonly_fields = ('admin_image',)
    actions = [make_available, make_unavailable]

@admin.register(font)
class fontsAdmin(admin.ModelAdmin):
    def example(self, obj):
        return format_html(''.format(obj.font.url))


readonly_fields = ('example',)

@admin.register(design)
class designAdmin(admin.ModelAdmin):
    list_display = ('cafename', 'font', 'fontcolor',)
    fields = (('cafename', 'headertxt'), ('bgheader', 'bgup', 'bgcenter', 'bgdown', 'bgend'), ('font', 'fontcolor'))


admin.site.unregister(Site)
admin.site.unregister(Group)
admin.site.unregister(User)


admin.site.site_header = 'Administration'