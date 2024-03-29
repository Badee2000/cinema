from django.contrib import admin
from django.urls import path, include
from movies.api import app
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', app.urls),

]

# Used with MEDIA_URL and MEDIA_ROOT for uploading images to the media folder.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
