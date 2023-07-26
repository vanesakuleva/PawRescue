
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('PawRescue.common.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('PawRescue.accounts.urls')),
    path('common/', include('PawRescue.common.urls')),
    path('pets/', include('PawRescue.pets.urls')),
    path('adoption/', include('PawRescue.adoption.urls')),
    path('events/', include('PawRescue.events.urls')),



]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
