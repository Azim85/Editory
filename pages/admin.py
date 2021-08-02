from django.contrib import admin
from django import forms
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from modeltranslation.admin import TabbedTranslationAdmin
from .models import (
    Topic,
    TopResearches,
    ResumeModel,
    About_us_news
)


# class Topictrans(TabbedTranslationAdmin):


# class TopicAdminForm(forms.ModelForm):
#     others = forms.CharField(widget=CKEditorUploadingWidget())
#     description = forms.CharField(widget=CKEditorWidget())
#
#     class Meta:
#         model = Topic
#         fields = '__all__'


class TopicAdmin(TabbedTranslationAdmin):
    # form = TopicAdminForm
    list_display = ['material_name', 'title', 'created_at']


class TopResearchesAdminForm(TabbedTranslationAdmin):
    # more = forms.CharField(widget=CKEditorUploadingWidget())
    #
    class Meta:
        model = TopResearches
        fields = '__all__'


# class TopResearchesAdmin(admin.ModelAdmin):
#     form = TopResearchesAdminForm


class ResumeModelAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'profession', 'about_me']


admin.site.register(Topic, TopicAdmin)
admin.site.register(TopResearches, TopResearchesAdminForm)
admin.site.register(ResumeModel, ResumeModelAdmin)
admin.site.register(About_us_news)
