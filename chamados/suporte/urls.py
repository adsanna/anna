from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("novo-chamado/", views.novo_chamado, name="novo_chamado"),
    path("meus-chamados/", views.meus_chamados, name="meus_chamados"),

    # ADMIN
    path("admin-chamados/", views.admin_chamados, name="admin_chamados"),
    path("admin-chamados/<int:pk>/", views.admin_detalhe_chamado, name="admin_detalhe_chamado"),
]
