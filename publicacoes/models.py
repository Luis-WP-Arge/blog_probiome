from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Publicacoes_categoria(models.Model):
    name = models.CharField(max_length=255, default="uncategorized")

    def __str__(self):
        return self.name

class Publicacoes(models.Model):
    id = models.AutoField
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Publicacoes_categoria, on_delete=models.PROTECT)
    description = RichTextField()

    def __str__(self):
        return self.name
