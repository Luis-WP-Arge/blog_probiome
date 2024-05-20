from django.shortcuts import render
from .models import Sobre_nos, Image, About_us
# Create your views here.

def sobre_nos(request):
    tudoSobreNos = []
    catabout = Sobre_nos.objects.values('category', 'id')
    cats = {item['category'] for item in catabout}
    for cat in cats:
        Sobre_Nos = Sobre_nos.objects.filter(category=cat)
        tudoSobreNos.append(Sobre_Nos)

    return render(request, "sobre_nos.html", {'tudoSobreNos':tudoSobreNos})

def gallery_view(request, pk):
    allImages = []
    #images = Image.objects.get(id=pk)
    image_cat = Image.object.values('category', 'id')
    icats = {item['category'] for item in image_cat}
    for cat in icats:
        Images = Image.object.filter(category=cat)
        allImages.append(Images)

    LabImages = {'allImages': allImages}
    return render(request, 'sobre_nos.html', LabImages)

def about_us(request):
    allAboutUs = []
    catabout = About_us.objects.values('category', 'id')
    cats = {item['category'] for item in catabout}
    for cat in cats:
        About_Us = About_us.objects.filter(category=cat)
        allAboutUs.append(About_Us)

    return render(request, "about_us.html", {'allAboutUs':allAboutUs})
