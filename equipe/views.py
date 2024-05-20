from django.shortcuts import render
from .models import Equipe, Team, Ex_Membros, Former

# Create your views here.
def equipe(request):
    todosPesquisadores = []
    catEquipe = Equipe.objects.values('category', 'id')
    cats = {item['category'] for item in catEquipe}
    for cat in cats:
        pesquisador = Equipe.objects.filter(category=cat)
        todosPesquisadores.append(pesquisador)

    params = {'todosPesquisadores':todosPesquisadores}
    return render(request, "team.html", params)


def ex_membros(request):
    allEx_membros = []
    catex_membros = Ex_Membros.objects.values('category', 'id')
    catex = {item['category'] for item in catex_membros}
    for cat in catex:
        ex_membros = Ex_Membros.objects.filter(category=cat)
        allEx_membros.append(ex_membros)

    params = {'allEx_membros': allEx_membros}
    return render(request, "ex_membros.html", params)

def team(request):
    allResearchers = []
    catprods = Team.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        researcher = Team.objects.filter(category=cat)
        allResearchers.append(researcher)

    params = {'allResearchers':allResearchers}
    return render(request, "team.html", params)

def former(request):
    allFormers = []
    catformers = Former.objects.values('category', 'id')
    cats = {item['category'] for item in catformers}
    for cat in cats:
        former = Former.objects.filter(category=cat)
        allFormers.append(former)

    params = {'allFormers':allFormers}
    return render(request, "former.html", params)
