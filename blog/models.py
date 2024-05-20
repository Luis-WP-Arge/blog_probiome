from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

class Organism(models.Model):
    name = models.CharField(max_length=255, default="uncategorized")

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=255)
    organism = models.ForeignKey(Organism, on_delete=models.PROTECT)
    abstract = RichTextField()
    content = RichTextUploadingField()
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    created_at = models.DateField(auto_now_add=True)
#    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk',
#                                        related_query_name='hit_count_generic_relation')

    def __str__(self):
        return self.title + ' | ' + str(self.author)

#    def save(self, *args, **kwargs):
#        if not self.pk:
#            self.pk = slugify(self.title)
#        return super(Post, self).save(*args, **kwargs)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)
