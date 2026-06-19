"""
Script pour ajouter les produits initiaux
Exécuter avec: python ajouter_produits.py
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'delices_aicha.settings')
django.setup()

from boutique.models import Produit

# Liste des produits de Les Délices de Aïcha
produits = [
    {
        'nom': 'Jus Bissap',
        'description': 'Notre délicieux jus de fleurs d\'hibiscus (bissap), riche en vitamines C et en antioxydants. Légèrement sucré avec une touche de menthe fraîche. Un incontournable sénégalais !',
        'prix': 500,
        
    },
    {
        'nom': 'Jus Bouyi',
        'description': 'Jus de baobab (bouyi) naturel, superaliment africain riche en calcium et en fibres. Un goût unique et légèrement acidulé qui vous rafraîchit en toute saison.',
        'prix': 600,
        
    },
    {
        'nom': "Jus d'Orange",
        'description': 'Jus d\'oranges fraîchement pressées, sans sucre ajouté. 100% naturel, gorgé de vitamine C pour bien démarrer la journée.',
        'prix': 500,
    },
    {
        'nom': 'Jus Tamarin',
        'description': 'Jus de tamarin (dakhar) rafraîchissant et légèrement acidulé. Riche en minéraux et très apprécié pour ses vertus digestives.',
        'prix': 500,
        
    },
    {
        'nom': 'Jus Cocktail',
        'description': 'Un mélange savoureux de plusieurs fruits tropicaux : mangue, ananas, bissap et citron. Un cocktail fruité et énergisant qui ravira vos papilles !',
        'prix': 700,
        
    },
    {
        'nom': 'Jus de Gingembre',
        'description': 'Jus de gingembre frais avec une pointe de citron et de miel. Tonifiant, réchauffant et idéal pour booster votre système immunitaire.',
        'prix': 500,
        
    },
]

for p in produits:
    produit, cree = Produit.objects.get_or_create(
        nom=p['nom'],
        defaults={
            'description': p['description'],
            'prix': p['prix'],
            'photo': p.get('photo'),
            'disponible': True,
        }
    )
    if cree:
        print(f"✅ Ajouté : {produit.nom} – {produit.prix} FCFA")
    else:
        print(f"⚠️  Déjà existant : {produit.nom}")

print("\n🎉 Tous les produits sont prêts !")
