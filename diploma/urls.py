""" DIPLOMA URL Configuration """

from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from diploma import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cinema.urls')),
    path('staff/', include('staff.urls')),
    path('api/', include('api.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
