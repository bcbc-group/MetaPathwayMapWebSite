from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
        path('', views.mpmDatatable,  name='mpmDatable'),
        path('mpmDatatable', views.mpmDatatable),
 ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
