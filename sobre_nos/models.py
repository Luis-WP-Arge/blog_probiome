from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Sobre_nos_categoria(models.Model):
    name = models.CharField(max_length=255, default="uncategorized")

    def __str__(self):
        return self.name

class Sobre_nos(models.Model):
    id = models.AutoField
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Sobre_nos_categoria, on_delete=models.PROTECT)
    text = RichTextUploadingField()

    def __str__(self):
        return self.title

class AboutUs_category(models.Model):
    name = models.CharField(max_length=255, default="uncategorized")

    def __str__(self):
        return self.name

class About_us(models.Model):
    id = models.AutoField
    title = models.CharField(max_length=100)
    category = models.ForeignKey(AboutUs_category, on_delete=models.PROTECT)
    text = RichTextUploadingField()

    def __str__(self):
        return self.title

class Image_class(models.Model):
    name = models.CharField(max_length=255, default="uncategorized")

    def __str__(self):
        return self.name

class Image(models.Model):
    name = models.CharField(max_length=120)
    category = models.ForeignKey(Image_class, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to='about_us', default="")

    def __str__(self):
        return self.name