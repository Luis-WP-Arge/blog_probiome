from django.shortcuts import render
from .models import Linha_Setaria, Linha_Gossypium

# Create your views here.

def linha_setaria(request):
    allLinha_Setaria = []
    catabout = Linha_Setaria.objects.values('category', 'id')
    cats = {item['category'] for item in catabout}
    for cat in cats:
        Linha_Setaria_cat = Linha_Setaria.objects.filter(category=cat)
        allLinha_Setaria.append(Linha_Setaria_cat)

    return render(request, "setaria.html", {'allLinha_Setaria':allLinha_Setaria})

def linha_gossypium(request):
    allLinha_Gossypium = []
    catabout = Linha_Gossypium.objects.values('category', 'id')
    cats = {item['category'] for item in catabout}
    for cat in cats:
        Linha_Gossypium_cat = Linha_Gossypium.objects.filter(category=cat)
        allLinha_Gossypium.append(Linha_Gossypium_cat)

    return render(request, "gossypium.html", {'allLinha_Gossypium':allLinha_Gossypium})
