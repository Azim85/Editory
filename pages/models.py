from django.db import models
from django.urls import reverse_lazy
from users.models import CustomUser
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django_resized import ResizedImageField


class Topic(models.Model):
    main_image = models.ImageField(upload_to='news/')
    material_name = models.CharField(max_length=100)
    title = models.CharField(max_length=255)
    description = RichTextField()
    others = RichTextUploadingField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.material_name

    def get_absolute_url(self):
        return reverse_lazy('pages:article', kwargs = {'pk':self.pk})

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'



class TopResearches(models.Model):
    image = models.ImageField(upload_to = 'top_researches/')
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=100)
    description = models.TextField()
    more = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy('pages:paper', kwargs = {'pk':self.pk})

