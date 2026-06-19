from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Produit, Commande
from .forms import CommandeForm


def accueil(request):
    """Page d'accueil avec présentation des produits"""
    produits = Produit.objects.filter(disponible=True)
    return render(request, 'boutique/accueil.html', {'produits': produits})


def produit_detail(request, pk):
    """Détail d'un produit"""
    produit = get_object_or_404(Produit, pk=pk, disponible=True)
    return render(request, 'boutique/produit_detail.html', {'produit': produit})


def commander(request, pk=None):
    """Page pour passer une commande"""
    produit_initial = None
    if pk:
        produit_initial = get_object_or_404(Produit, pk=pk, disponible=True)

    if request.method == 'POST':
        form = CommandeForm(request.POST)
        if form.is_valid():
            commande = form.save()
            messages.success(
                request,
                f'✅ Votre commande a bien été reçue ! Nous vous contacterons au {commande.telephone} très bientôt.'
            )
            return redirect('confirmation', pk=commande.pk)
    else:
        initial = {}
        if produit_initial:
            initial['produit'] = produit_initial
        form = CommandeForm(initial=initial)

    return render(request, 'boutique/commander.html', {
        'form': form,
        'produit_initial': produit_initial
    })


def confirmation(request, pk):
    """Page de confirmation de commande"""
    commande = get_object_or_404(Commande, pk=pk)
    return render(request, 'boutique/confirmation.html', {'commande': commande})


def nos_produits(request):
    """Page listant tous les produits"""
    produits = Produit.objects.filter(disponible=True)
    return render(request, 'boutique/nos_produits.html', {'produits': produits})


def contact(request):
    """Page de contact"""
    return render(request, 'boutique/contact.html')
