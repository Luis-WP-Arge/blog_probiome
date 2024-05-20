from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Linha_Setaria_category(models.Model):
    name = models.CharField(max_length=255, default="uncategorized")

    def __str__(self):
        return self.name

class Linha_Setaria(models.Model):
    id = models.AutoField
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Linha_Setaria_category, on_delete=models.PROTECT)
    text = RichTextUploadingField()

    def __str__(self):
        return self.title

class Linha_Gossypium_category(models.Model):
    name = models.CharField(max_length=255, default="uncategorized")

    def __str__(self):
        return self.name

class Linha_Gossypium(models.Model):
    id = models.AutoField
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Linha_Gossypium_category, on_delete=models.PROTECT)
    text = RichTextUploadingField()

    def __str__(self):
        return self.title
