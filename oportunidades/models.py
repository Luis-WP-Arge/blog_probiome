from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Oportunidades_category(models.Model):
    name = models.CharField(max_length=255, default="uncategorized")

    def __str__(self):
        return self.name

class Oportunidades_campo(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Oportunidades_category, on_delete=models.PROTECT)
    abstract = RichTextField()
    text = RichTextUploadingField()
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title + ' | ' + str(self.author)