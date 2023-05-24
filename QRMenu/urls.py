
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
#from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('menu/', include('menu.urls')),
    path('', include('menu.urls')),
    #path('', views.show_menu, name='menu'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
