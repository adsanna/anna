from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #rota, view responsável, nome de referencia
    #usuarios
    path('', views.home, name='home'), #listadechamados
    path('novo-chamado/', views.novo_chamado, name='novo_chamado'),  # novo chamado
    path('usuarios/', views.documentos, name='lista'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)