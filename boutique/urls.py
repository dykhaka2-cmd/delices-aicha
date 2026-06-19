from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('produits/', views.nos_produits, name='nos_produits'),
    path('produit/<int:pk>/', views.produit_detail, name='produit_detail'),
    path('commander/', views.commander, name='commander'),
    path('commander/<int:pk>/', views.commander, name='commander_produit'),
    path('confirmation/<int:pk>/', views.confirmation, name='confirmation'),
    path('contact/', views.contact, name='contact'),
]
