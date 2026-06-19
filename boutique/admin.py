from django.contrib import admin
from .models import Produit, Commande


@admin.register(Produit)
class ProduitAdmin(admin.ModelAdmin):
    list_display = ['nom', 'prix', 'disponible', 'date_ajout']
    list_filter = ['disponible']
    list_editable = ['prix', 'disponible']
    search_fields = ['nom', 'description']


@admin.register(Commande)
class CommandeAdmin(admin.ModelAdmin):
    list_display = ['nom_client', 'telephone', 'produit', 'quantite', 'total', 'zone', 'statut', 'date_commande']
    list_filter = ['statut', 'zone', 'date_commande']
    list_editable = ['statut']
    search_fields = ['nom_client', 'telephone', 'adresse']
    readonly_fields = ['date_commande', 'total']

    def total(self, obj):
        return f"{obj.total():,} FCFA"
    total.short_description = "Total"
