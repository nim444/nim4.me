from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('', include('app.urls')),
    path('', include('library.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include('api.urls')),

     ]
     
     
     #+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    
handler404 = 'app.views.error_404_view'


