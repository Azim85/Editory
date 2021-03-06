from django.db import models
from django.db.models.fields import BooleanField
from django.urls import reverse_lazy
from users.models import CustomUser
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from setpage.models import AboutUsModel

from django_resized import ResizedImageField


class Topic(models.Model):
    main_image = models.ImageField(upload_to='news/', blank=True)
    material_name = models.CharField(max_length=100)
    title = models.CharField(max_length=255)
    description = RichTextUploadingField()
    others = RichTextUploadingField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.created_at)

    def get_absolute_url(self):
        return reverse_lazy('pages:article', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'
        ordering = '-id',



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
        return reverse_lazy('pages:paper', kwargs={'pk': self.pk})



class ResumeModel(models.Model):
    """
    url:about/us, name:webinars
    page:about_us.html
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)
    about_me = models.TextField(blank=True, null=True)
    resume = models.FileField(upload_to='resume/')
    is_agree = BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = 'Resume'
        verbose_name_plural = 'Resumes'


class About_us_news(models.Model):
    image = models.ImageField(upload_to = 'about_news/', null=True, blank=True)
    material_name = models.CharField(max_length=100, null=True, blank=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    url = models.CharField(max_length=255, null=True, blank=True)



class Tariffs(models.Model):
    text = models.TextField()
    stendart = models.BooleanField()
    express = models.BooleanField()
    premium = models.BooleanField()


class WebinarsUrl1(models.Model):
    url = models.CharField(max_length=225)

    def __str__(self):
        return self.url

class WebinarsUrl2(models.Model):
    url = models.CharField(max_length=225)

    def __str__(self):
        return self.url

