# 🌿 Les Délices de Aïcha – Application Web Django

Application web pour présenter les jus, gérer les produits et recevoir des commandes.

---

## 📁 Structure du projet

```
delices_aicha/
├── manage.py                    # Gestionnaire Django
├── requirements.txt             # Dépendances Python
├── ajouter_produits.py          # Script pour ajouter les produits initiaux
│
├── delices_aicha/               # Configuration du projet
│   ├── settings.py              # Paramètres (BD, langues, etc.)
│   ├── urls.py                  # URLs principales
│   └── wsgi.py
│
└── boutique/                    # Application principale
    ├── models.py                # Modèles : Produit, Commande
    ├── views.py                 # Vues (pages)
    ├── urls.py                  # URLs de l'app
    ├── forms.py                 # Formulaire de commande
    ├── admin.py                 # Interface admin
    └── templates/boutique/      # Pages HTML
        ├── base.html            # Template de base (navbar, footer)
        ├── accueil.html         # Page d'accueil
        ├── nos_produits.html    # Liste des jus
        ├── produit_detail.html  # Détail d'un jus
        ├── commander.html       # Formulaire de commande
        ├── confirmation.html    # Confirmation de commande
        └── contact.html         # Page de contact
```

---

## 🚀 Installation et démarrage

### 1. Installer les dépendances
```bash
pip install -r requirements.txt
```

### 2. Créer la base de données
```bash
python manage.py makemigrations
python manage.py migrate
```

### 3. Créer un compte administrateur
```bash
python manage.py createsuperuser
```
Entrez : nom d'utilisateur, email, mot de passe

### 4. Ajouter les produits initiaux
```bash
python ajouter_produits.py
```

### 5. Lancer le serveur
```bash
python manage.py runserver
```

### 6. Ouvrir dans le navigateur
- 🌐 Site principal : http://127.0.0.1:8000/
- 🔧 Administration : http://127.0.0.1:8000/admin/

---

## 📄 Pages disponibles

| URL | Page |
|-----|------|
| `/` | Accueil |
| `/produits/` | Liste des jus |
| `/produit/<id>/` | Détail d'un jus |
| `/commander/` | Formulaire de commande |
| `/commander/<id>/` | Commander un jus précis |
| `/confirmation/<id>/` | Confirmation de commande |
| `/contact/` | Page de contact |
| `/admin/` | Tableau de bord admin |

---

## ⚙️ Interface Admin

L'admin Django permet de :
- ✅ **Ajouter / modifier / supprimer des produits** (nom, prix, description, image, disponibilité)
- ✅ **Gérer les commandes** (voir, changer le statut : en attente → confirmée → en livraison → livrée)
- ✅ **Filtrer les commandes** par statut, zone, date

---

## 🧾 Modèles de données

### Produit
- `nom` – Nom du jus
- `description` – Description
- `prix` – Prix en FCFA
- `image` – Photo (optionnel)
- `disponible` – Affiché ou non

### Commande
- `nom_client`, `telephone` – Infos client
- `adresse`, `zone` – Livraison (Almadies / Kounoune)
- `produit`, `quantite` – Ce qui est commandé
- `message` – Remarques optionnelles
- `statut` – En attente / Confirmée / En livraison / Livrée / Annulée

---

## 🎨 Design

- **Bootstrap 5** – Interface responsive mobile
- **Couleurs** : Vert naturel + Orange chaud
- **Polices** : Poppins + Dancing Script (logo)
- Compatible mobile (téléphones Dakar)

---

## 📞 Personnalisation

Pour mettre votre vrai numéro de téléphone, modifiez dans :
- `base.html` : ligne avec `tel:+221771234567`
- `contact.html` : numéro affiché et lien WhatsApp
