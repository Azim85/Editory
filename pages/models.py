from django.db import models
from django.urls import reverse_lazy
from users.models import CustomUser
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


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
