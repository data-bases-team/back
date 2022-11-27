
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('menu/', include('menu.urls')),
    path('', include('adminmenu.urls')),
    path('', include('adminmenu.urls')),
]
