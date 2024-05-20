from django.shortcuts import render
from .models import Publicacoes

# Create your views here.
def publicacoes(request):
    todasPublicacoes = []
    catPubli = Publicacoes.objects.values('category', 'id')
    cats = {item['category'] for item in catPubli}
    for cat in cats:
        publicacao = Publicacoes.objects.filter(category=cat)
        todasPublicacoes.append(publicacao)

    params = {'todasPublicacoes':todasPublicacoes}
    return render(request, "publicacoes.html", params)

