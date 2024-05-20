from django.contrib import admin

# Register your models here.
from equipe.models import Equipe_categoria, Team_category, Ex_Membros_categoria, Former_category
from equipe.models import Equipe, Team, Ex_Membros, Former

#from micro_blog.team.models import Artist
admin.site.register(Equipe)
admin.site.register(Equipe_categoria)
admin.site.register(Ex_Membros)
admin.site.register(Ex_Membros_categoria)

admin.site.register(Team)
admin.site.register(Team_category)
admin.site.register(Former)
admin.site.register(Former_category)