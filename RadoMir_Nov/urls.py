from django.contrib import admin
from django.urls import path, include
from . import settings
from django.conf.urls.static import static

urlpatterns = [
    path('main_page/', include('main_page.urls')),
    path('admin/', admin.site.urls),
    path('hashtags/', include('hashtags.urls')),
    path('order/', include('order.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
