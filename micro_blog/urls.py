"""micro_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from blog import views
from blog.views import OrganismView, publicacoes, blog
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from equipe.views import equipe, team, ex_membros
from sobre_nos.views import sobre_nos, about_us
from linha_pesquisa.views import linha_setaria, linha_gossypium
from oportunidades.views import oportunidades
from publicacoes.views import publicacoes

urlpatterns = [
    path('jet/', include('jet.urls', 'jet')),  # Django JET URLS
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', views.home),
    path('sobre_nos/', sobre_nos),
    path('about_us/', about_us),
    path('team/', team),
    path('equipe_atual/', equipe),
    path('ex_membros/', ex_membros),
    path('linha_setaria/', linha_setaria),
    path('linha_gossypium/', linha_gossypium),
    path('publicacoes', publicacoes),
    path('oportunidades', oportunidades),
    path('blog', views.blog, name="blog"),
    path('posts/<int:post_id>', views.post),
    path('oports/<int:oportunidade_id>', oportunidades),
    path('organism/<str:organisms>/', OrganismView, name='organism')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
