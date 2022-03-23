from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
        path('', views.mpmCytoscape,  name='mpmCytoscape'),
        path('mpmCytoscape/', views.mpmCytoscape),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
