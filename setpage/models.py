from django.db import models




class AboutUsModel(models.Model):
    text1 = models.CharField(max_length=255, blank=True, null=True)
    text2 = models.TextField(blank=True)
    text3 = models.CharField(max_length=255, blank=True, null=True)
    text4 = models.CharField(max_length=255, blank=True, null=True)
    text5 = models.TextField(blank=True)
    text6 = models.CharField(max_length=255, blank=True, null=True)
    text7 = models.CharField(max_length=255, blank=True, null=True)
    text8 = models.CharField(max_length=255, blank=True, null=True)
    text9 = models.TextField(blank=True)
    text10 = models.CharField(max_length=255, blank=True, null=True)
    text11 = models.TextField(blank=True)
