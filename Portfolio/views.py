from django.shortcuts import render
from .models import About, Resume, PortfolioCategory, PortfolioItem  # Ajout des modèles Portfolio

def home(request):
    about = About.objects.first()  # Récupérer l'utilisateur "about"
    resume = Resume.objects.filter(about=about).first()  # Associer un CV à cet utilisateur
    categories = PortfolioCategory.objects.all()  # Récupérer toutes les catégories du portfolio
    items = PortfolioItem.objects.all()  # Récupérer tous les items du portfolio
    
    # On passe les données dans le contexte
    context = {
        'about': about,
        'resume': resume,
        'roles': ['Developer', 'Designer', 'Freelancer'],  # Exemple de rôles (tu pourrais les récupérer dynamiquement si nécessaire)
        'categories': categories,  # Ajout des catégories du portfolio
        'items': items,  # Ajout des items du portfolio
    }
    
    return render(request, 'home.html', context)
