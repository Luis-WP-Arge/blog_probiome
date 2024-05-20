from django.shortcuts import render
from .models import Oportunidades_campo
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def oportunidades(request, oportunidade_id):
    oportunidade = Oportunidades_campo.objects.get(pk=oportunidade_id)

    return render(request, 'post.html', {'oportunidade': oportunidade})

def oport(request):
    oports = Oportunidades_campo.objects.all()
    paginator = Paginator(oports, 1)
    page = request.GET.get('page')
    try:
        oports = paginator.page(page)
    except PageNotAnInteger:
        oports = paginator.page(1)
    except EmptyPage:
        oports = paginator.page(paginator.num_pages)
    return render(request, 'blog.html', {'oports': oports, page:'pages'})