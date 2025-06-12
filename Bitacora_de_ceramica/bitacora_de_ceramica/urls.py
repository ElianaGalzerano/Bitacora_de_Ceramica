from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from accounts.views import crear_pieza

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('about/', TemplateView.as_view(template_name='about.html'), name='acerca_de_mi'),
    path('pages/', include('pages.urls')),
    path('accounts/', include('accounts.urls')),
    path('mensajes/', include('mensajes.urls')),
    
    
    


]


from django.conf import settings
from django.conf.urls.static import static



# Servir media en desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

