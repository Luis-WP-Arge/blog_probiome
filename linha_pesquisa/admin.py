from django.contrib import admin

# Register your models here.
from linha_pesquisa.models import Linha_Setaria_category, Linha_Setaria
from linha_pesquisa.models import Linha_Gossypium_category, Linha_Gossypium

#from micro_blog.team.models import Artist

admin.site.register(Linha_Setaria)
admin.site.register(Linha_Setaria_category)
admin.site.register(Linha_Gossypium)
admin.site.register(Linha_Gossypium_category)
