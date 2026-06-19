from django import forms
from .models import Commande


class CommandeForm(forms.ModelForm):
    """Formulaire de commande pour les clients"""

    class Meta:
        model = Commande
        fields = ['nom_client', 'telephone', 'adresse', 'zone', 'produit', 'quantite', 'message']
        widgets = {
            'nom_client': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Votre nom complet'
            }),
            'telephone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex: 77 123 45 67'
            }),
            'adresse': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Votre adresse complète'
            }),
            'zone': forms.Select(attrs={
                'class': 'form-select'
            }),
            'produit': forms.Select(attrs={
                'class': 'form-select'
            }),
            'quantite': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 1,
                'max': 100
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Remarques ou instructions spéciales (optionnel)'
            }),
        }
        labels = {
            'nom_client': 'Nom complet',
            'telephone': 'Numéro de téléphone',
            'adresse': 'Adresse de livraison',
            'zone': 'Zone de livraison',
            'produit': 'Produit souhaité',
            'quantite': 'Quantité',
            'message': 'Message (optionnel)',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Afficher uniquement les produits disponibles
        from .models import Produit
        self.fields['produit'].queryset = Produit.objects.filter(disponible=True)
