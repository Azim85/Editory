from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models


class AboutUsModel(models.Model):
    text1 = models.CharField(max_length=255, blank=True, null=True)
    text2 = models.TextField(blank=True)
    text3 = models.CharField(max_length=255, blank=True, null=True)
    text4 = models.CharField(max_length=255, blank=True, null=True)
    text5 = models.TextField(blank=True)
    text6 = models.CharField(max_length=255, blank=True, null=True)
    text7 = RichTextUploadingField(null=True, blank=True)
    text8 = RichTextUploadingField(null=True, blank=True)
    text9 = RichTextUploadingField(blank=True)


class WebinarsModel(models.Model):
    text1 = models.CharField(max_length=255, blank=True, null=True)
    text2 = models.TextField(blank=True)
    image1 = models.ImageField(upload_to='changes/', blank=True)


class TranslationModel(models.Model):
    text1 = models.CharField(max_length=255, blank=True, null=True)
    text2 = RichTextUploadingField()
    text3 = RichTextUploadingField()
    text4 = RichTextUploadingField()
    text5 = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.text1


class BakModel(models.Model):
    text1 = models.CharField(max_length=255, blank=True)
    text2 = models.TextField(max_length=255, blank=True)
    text3 = models.CharField(max_length=255, blank=True)
    text4 = models.ImageField(upload_to='pages/', blank=True)
    text5 = models.TextField(max_length=255, blank=True)
    text6 = models.ImageField(upload_to='pages/', blank=True)
    text7 = models.TextField(max_length=255, blank=True)
    text8 = models.ImageField(upload_to='pages/', blank=True)
    text9 = models.TextField(max_length=255, blank=True)
    text10 = RichTextUploadingField(blank=True)
    text11 = models.TextField(max_length=255, blank=True)

    def __str__(self):
        return self.text1


class ConferencesModel(models.Model):
    text1 = models.CharField(max_length=255, blank=True)
    text2 = models.TextField(blank=True)
    text3 = RichTextUploadingField(default='', blank=True)
    text4 = RichTextUploadingField(default='', blank=True)
    text5 = models.CharField(max_length=255, default='')

    def __str__(self):
        return self.text1


class ContactModel(models.Model):
    text1 = models.CharField(max_length=20, blank=True)
    text2 = models.CharField(max_length=20, blank=True)
    text3 = models.CharField(max_length=20, blank=True)
    text4 = models.CharField(max_length=255, blank=True)
    text5 = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.text1


class CreateConferenceModel(models.Model):
    text1 = models.CharField(max_length=255, blank=True)
    text2 = models.TextField(blank=True)
    text3 = RichTextUploadingField(default='', blank=True)
    text4 = models.CharField(max_length=255, default='')

    def __str__(self):
        return self.text1


class DesignModel(models.Model):
    text1 = models.CharField(max_length=255, blank=True)
    text2 = RichTextUploadingField()
    text3 = models.ImageField(upload_to='design/', blank=True)
    text4 = models.CharField(max_length=255, blank=True)
    text5 = models.TextField(blank=True)
    text6 = models.ImageField(upload_to='design/', blank=True)
    text7 = models.CharField(max_length=255, blank=True)
    text8 = models.TextField(blank=True)
    text9 = models.ImageField(upload_to='design/', blank=True)
    text10 = models.CharField(max_length=255, blank=True)
    text11 = models.TextField(blank=True)

    def __str__(self):
        return self.text1


class GrantsModel(models.Model):
    text1 = models.CharField(max_length=255, blank=True)
    text2 = models.TextField(blank=True)
    text3 = RichTextUploadingField(blank=True)
    text4 = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.text1


class PatentModel(models.Model):
    text1 = models.CharField(max_length=255, blank=True)
    text2 = models.TextField(blank=True)
    text3 = RichTextUploadingField(blank=True)
    text4 = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.text1


class ScopusModel(models.Model):
    text1 = models.CharField(max_length=255, blank=True)
    text2 = models.TextField(blank=True)
    text4 = models.ImageField(upload_to='pages/', blank=True)
    text5 = models.TextField(blank=True)
    text6 = models.ImageField(upload_to='pages/', blank=True)
    text7 = models.TextField(blank=True)
    text8 = models.ImageField(upload_to='pages/', blank=True)
    text9 = models.TextField(blank=True)
    text10 = RichTextUploadingField()
    text11 = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.text1


class ProofModel(models.Model):
    text1 = models.CharField(max_length=255, blank=True)
    text2 = models.TextField(blank=True)
    text3 = models.CharField(max_length=255, blank=True)
    text4 = models.TextField(blank=True)
    text5 = models.CharField(max_length=255, blank=True)
    text6 = models.TextField(blank=True)
    text7 = models.CharField(max_length=255, blank=True)
    text8 = models.TextField(blank=True)
    text9 = RichTextUploadingField()

    def __str__(self):
        return self.text1


class LangEditModel(models.Model):
    text1 = models.CharField(max_length=100, blank=True)
    text2 = RichTextUploadingField()
    text3 = models.CharField(max_length=100, blank=True)
    text4 = models.CharField(max_length=100, blank=True)
    text5 = models.CharField(max_length=100, blank=True)
    text6 = models.CharField(max_length=100, blank=True)
    text7 = models.CharField(max_length=100, blank=True)
    text8 = models.CharField(max_length=100, blank=True)
    text9 = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.text1


class ResearchStrategyModel(models.Model):
    text1 = RichTextUploadingField()
    text2 = RichTextUploadingField()
    text3 = RichTextUploadingField()
    text4 = RichTextUploadingField()
    text5 = RichTextUploadingField()
    text6 = RichTextUploadingField()
    text7 = RichTextUploadingField()
    text8 = RichTextUploadingField()
    text9 = RichTextUploadingField()
