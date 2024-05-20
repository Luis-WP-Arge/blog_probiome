from django.contrib import admin

# Register your models here.
from oportunidades.models import Oportunidades_category
from oportunidades.models import Oportunidades_campo

#from micro_blog.team.models import Artist
admin.site.register(Oportunidades_campo)
admin.site.register(Oportunidades_category)
