import os
import subprocess
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from .forms import SignUpForm
from .models import Article, Report

# Vue pour l'inscription des utilisateurs
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')  # Redirige vers la page d'accueil après l'inscription
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

@login_required
def home(request):
    return render(request, 'home.html')

# Vue de recherche nécessitant une authentification

# views.py
from django.shortcuts import render
from .models import Article

def search_articles(request):
    query = request.GET.get('query', '')  # Récupère la requête de recherche de l'utilisateur
    articles = Article.objects.all()
    
    if query:
        articles = articles.filter(
            title__icontains=query  # Filtre les titres contenant le mot-clé
        )

    return render(request, 'search.html', {'articles': articles, 'query': query})

# views.py
from .utils.nlp_analysis import extract_keywords
from .models import Article

def analyze_articles(request):
    articles = Article.objects.all()

    for article in articles:
        if not article.keywords:
            article.keywords = ', '.join(extract_keywords(article.summary))
            article.save()

    return render(request, 'analyze.html', {'articles': articles})

# Vue pour générer des rapports, nécessite une authentification

def generate_report(request):
    report_content = "Détails du rapport..."
    Report.objects.create(user=request.user, content=report_content)
    return render(request, 'report.html', {'report': report_content})

# Vue pour démarrer le spider, nécessite une authentification

def start_spider(request):
    path_to_script = os.path.join(os.getcwd(), 'myapp', 'spiders', 'run_spider.py')
    subprocess.Popen(['python', path_to_script], shell=True)
    return HttpResponse("Spider started")

# Vue pour afficher les résultats, nécessite une authentification

def display_results(request):
    articles = Article.objects.all()
    reports = Report.objects.all()
    return render(request, 'results.html', {'articles': articles, 'reports': reports})

# Vue pour afficher les articles, nécessite une authentification

def display_articles(request):
    articles = Article.objects.all()
    return render(request, 'articles/display_articles.html', {'articles': articles})




# views.py
from django.http import FileResponse
from .utils.report_generator import generate_pdf
from .models import Article

def generate_report(request):
    articles = Article.objects.all()
    report_path = generate_pdf("techno_vigilance_report", articles)
    return FileResponse(open(report_path, 'rb'), as_attachment=True, filename="report.pdf")
