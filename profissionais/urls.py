from django.urls import path
from .views import CadastroProfissionais, EditarExcluirProfissionais

urlpatterns = [
    path('profissionais/', CadastroProfissionais.as_view(), name='profissionais-list-create'),
    path('profissionais/<int:pk>/', EditarExcluirProfissionais.as_view(), name='profissionais-retrieve-update-destroy'),
]