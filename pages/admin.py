from django.contrib import admin
from django import forms
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import (
    ResearchGrant,
    GetPatent,
    PublicationToScopus,
    OrderToGraphicalMaterials,
    Topic,
    OrderReviewForDissertation,
    OrganizeResearches,
    PublicationToMagazines,
)


class TopicAdminForm(forms.ModelForm):
    others = forms.CharField(widget=CKEditorUploadingWidget())
    description = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Topic
        fields = '__all__'


class TopicAdmin(admin.ModelAdmin):
    form = TopicAdminForm


admin.site.register(ResearchGrant)
admin.site.register(GetPatent)
admin.site.register(PublicationToScopus)
admin.site.register(Topic, TopicAdmin)
admin.site.register(OrderReviewForDissertation)
admin.site.register(OrganizeResearches)
admin.site.register(PublicationToMagazines)
admin.site.register(OrderToGraphicalMaterials)
