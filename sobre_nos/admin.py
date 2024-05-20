from django.contrib import admin

from sobre_nos.models import Sobre_nos, Sobre_nos_categoria, About_us, AboutUs_category, Image_class, Image

# Register your models here.
admin.site.register(Sobre_nos)
admin.site.register(Sobre_nos_categoria)
admin.site.register(About_us)
admin.site.register(AboutUs_category)
admin.site.register(Image)
admin.site.register(Image_class)