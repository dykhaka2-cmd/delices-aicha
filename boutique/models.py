from django.db import models


class Produit(models.Model):
    """Modèle pour les jus et produits"""

    NOM_CHOICES = [
        ('bissap', 'Jus Bissap'),
        ('bouyi', 'Jus Bouyi'),
        ('orange', "Jus d'Orange"),
        ('tamarin', 'Jus Tamarin'),
        ('cocktail', 'Jus Cocktail'),
        ('gingembre', 'Jus de Gingembre'),
        ('autre', 'Autre'),
    ]

    nom = models.CharField(max_length=100, verbose_name="Nom du produit")
    description = models.TextField(verbose_name="Description")
    prix = models.DecimalField(max_digits=8, decimal_places=0, verbose_name="Prix (FCFA)")
    image = models.ImageField(upload_to='produits/', blank=True, null=True, verbose_name="Image")
    disponible = models.BooleanField(default=True, verbose_name="Disponible")
    date_ajout = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Produit"
        verbose_name_plural = "Produits"
        ordering = ['nom']

    def __str__(self):
        return self.nom


class Commande(models.Model):
    """Modèle pour les commandes clients"""

    STATUT_CHOICES = [
        ('en_attente', 'En attente'),
        ('confirmee', 'Confirmée'),
        ('en_livraison', 'En livraison'),
        ('livree', 'Livrée'),
        ('annulee', 'Annulée'),
    ]

    ZONE_CHOICES = [
        ('almadies', 'Almadies'),
        ('kounoune', 'Kounoune'),
        ('autre', 'Autre zone Dakar'),
    ]

    # Infos client
    nom_client = models.CharField(max_length=100, verbose_name="Nom complet")
    telephone = models.CharField(max_length=20, verbose_name="Téléphone")
    adresse = models.TextField(verbose_name="Adresse de livraison")
    zone = models.CharField(max_length=20, choices=ZONE_CHOICES, verbose_name="Zone")

    # Commande
    produit = models.ForeignKey(Produit, on_delete=models.SET_NULL, null=True, verbose_name="Produit")
    quantite = models.PositiveIntegerField(default=1, verbose_name="Quantité")
    message = models.TextField(blank=True, verbose_name="Message / Remarques")

    # Statut et date
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES, default='en_attente', verbose_name="Statut")
    date_commande = models.DateTimeField(auto_now_add=True, verbose_name="Date de commande")

    class Meta:
        verbose_name = "Commande"
        verbose_name_plural = "Commandes"
        ordering = ['-date_commande']

    def __str__(self):
        return f"Commande de {self.nom_client} - {self.produit}"

    def total(self):
        if self.produit:
            return self.produit.prix * self.quantite
        return 0
