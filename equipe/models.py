from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Equipe_categoria(models.Model):
    name = models.CharField(max_length=255, default="uncategorized")

    def __str__(self):
        return self.name

class Equipe(models.Model):
    id = models.AutoField
    name = models.CharField(max_length=100)
    category = models.ForeignKey('Equipe_categoria', on_delete=models.CASCADE, related_name='category', null=False)
    categoria = models.CharField(max_length=100, unique=False, null=True)
    email = models.CharField(max_length=100)
    lattes = models.CharField(max_length=100)
    google_scholar = models.CharField(max_length=100, unique=False, null=True)
    description = RichTextField()
    image = models.ImageField(upload_to='equipe', default="")

    def __str__(self):
        return self.name

class Ex_Membros_categoria(models.Model):
    name = models.CharField(max_length=255, default="uncategorized")

    def __str__(self):
        return self.name

class Ex_Membros(models.Model):
    id = models.AutoField
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Ex_Membros_categoria, on_delete=models.PROTECT)
    description = RichTextField()

    def __str__(self):
        return self.name

class Team_category(models.Model):
    name = models.CharField(max_length=255, default="uncategorized")

    def __str__(self):
        return self.name

class Team(models.Model):
    id = models.AutoField
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Team_category, on_delete=models.PROTECT)
    email = models.CharField(max_length=100)
    lattes = models.CharField(max_length=100)
    description = RichTextField()
    image = models.ImageField(upload_to='team', default="")

    def __str__(self):
        return self.name

class Former_category(models.Model):
    name = models.CharField(max_length=255, default="uncategorized")

    def __str__(self):
        return self.name

class Former(models.Model):
    id = models.AutoField
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Former_category, on_delete=models.PROTECT)
    description = RichTextField()

    def __str__(self):
        return self.name