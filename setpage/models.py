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
    text10 = models.TextField(max_length=255, blank=True)
    text11 = models.TextField(max_length=255, blank=True)
    text12 = models.TextField(max_length=255, blank=True)
    text13 = models.TextField(max_length=255, blank=True)
    text14 = models.TextField(max_length=255, blank=True)
    text15 = models.TextField(max_length=255, blank=True)
    text16 = models.TextField(max_length=255, blank=True)

    def __str__(self):
        return self.text1


class ConferencesModel(models.Model):
    text1 = models.CharField(max_length=255, blank=True)
    text2 = models.TextField(blank=True)
    text3 = models.TextField(blank=True)
    text4 = models.CharField(max_length=255, blank=True)
    text4_link = models.CharField(max_length=255, blank=True)
    text5 = models.TextField(blank=True)
    text6 = models.CharField(max_length=255, blank=True)
    text6_link = models.CharField(max_length=255, blank=True)
    text7 = models.TextField(blank=True)
    text8 = models.CharField(max_length=255, blank=True)
    text8_link = models.CharField(max_length=255, blank=True)
    text9 = models.TextField(blank=True)
    text10 = models.CharField(max_length=255, blank=True)
    text10_link = models.CharField(max_length=255, blank=True)
    text11 = models.TextField(blank=True)
    text12 = models.CharField(max_length=255, blank=True)
    text12_link = models.CharField(max_length=255, blank=True)
    text13 = models.TextField(blank=True)
    text14 = models.CharField(max_length=255, blank=True)
    text14_link = models.CharField(max_length=255, blank=True)
    text15 = models.TextField(blank=True)
    text16 = models.TextField(blank=True)
    text17 = models.TextField(blank=True)

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
  
    def __str__(self):
        return self.text1


class DesignModel(models.Model):
    text1 = models.CharField(max_length=255, blank=True)
    text2 = models.TextField(blank=True)
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
   

    def __str__(self):
        return self.text1


class PatentModel(models.Model):
    text1 = models.CharField(max_length=255, blank=True)
    text2 = models.TextField(blank=True)
    text3 = models.TextField(blank=True)
    text4 = models.TextField(blank=True)
    text5 = models.TextField(blank=True)
    text6 = models.CharField(max_length=255, blank=True)
    text7 = models.CharField(max_length=255, blank=True)
    text8 = models.CharField(max_length=255, blank=True)
    text9 = models.CharField(max_length=255, blank=True)
    text10 = models.TextField(blank=True)
    text11 = models.TextField(blank=True)

    def __str__(self):
        return self.text1


class ScopusModel(models.Model):
    text1 = models.CharField(max_length=255, blank=True)
    text2 = models.TextField( blank=True)
    text3 = models.ImageField(upload_to='scopus', blank=True)
    text4 = models.ImageField(upload_to='pages/', blank=True)
    text5 = models.TextField( blank=True)
    text6 = models.ImageField(upload_to='pages/', blank=True)
    text7 = models.TextField( blank=True)
    text8 = models.ImageField(upload_to='pages/', blank=True)
    text9 = models.TextField( blank=True)
    text10 = models.CharField(max_length=255, blank=True)
    text11 = models.CharField( max_length=255, blank=True)
    text12 = models.CharField(max_length=255, blank=True)
    text13 = models.CharField(max_length=255, blank=True)
    text14 = models.CharField(max_length=255, blank=True)
    text15 = models.CharField(max_length=255, blank=True)
    text16 = models.CharField(max_length=255, blank=True)

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
    text9 = models.CharField(max_length=255, blank=True)
    text10 = models.CharField(max_length=255, blank=True)
    text11 = models.CharField(max_length=255, blank=True)
    text12 = models.CharField(max_length=255, blank=True)
    text13 = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.text1


class LangEditModel(models.Model):
    text1 = models.TextField(blank=True)
    text2 = models.TextField(blank=True)
    text3 = models.CharField(max_length=100, blank=True)
    text4 = models.CharField(max_length=100, blank=True)
    text5 = models.CharField(max_length=100, blank=True)
    text6 = models.CharField(max_length=100, blank=True)
    text7 = models.CharField(max_length=100, blank=True)
    text8 = models.CharField(max_length=100, blank=True)
    text9 = models.CharField(max_length=100, blank=True)
    text10 = models.CharField(max_length=100, blank=True)
    text11 = models.CharField(max_length=100, blank=True)
    text12 = models.CharField(max_length=100, blank=True)
    text13 = models.CharField(max_length=100, blank=True)
    text14 = models.CharField(max_length=100, blank=True)
    text15 = models.CharField(max_length=100, blank=True)
    text16 = models.CharField(max_length=100, blank=True)
    text17 = models.CharField(max_length=100, blank=True)
    text18 = models.CharField(max_length=100, blank=True)
    text19 = models.CharField(max_length=100, blank=True)
    text20 = models.CharField(max_length=100, blank=True)
    text21 = models.CharField(max_length=100, blank=True)
    text22 = models.CharField(max_length=100, blank=True)
    text23 = models.CharField(max_length=100, blank=True)
    text24 = models.CharField(max_length=100, blank=True)
    text25 = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.text1
