from django.contrib import admin
from .models import (
    ResearchGrant,
    PublicationToScopus,
    OrderReviewForDissertation,
    
    OrganizeResearches,
    PublicationToMagazines,
    Consultation,
    ApplicationForFreeConsultation,
    Proofreading,
    PeerReview,
    OrganizeConferences,
    Grants,
    Language,
    Translation,


    GetPatent,
    GetGrant,
    Baks,
    Scopus
)


class GrantsAdmin(admin.ModelAdmin):
    list_display = ['first_name']


class TranslationAdmin(admin.ModelAdmin):
    list_display = ['user', 'language']


admin.site.register(ResearchGrant)
admin.site.register(Language)
admin.site.register(PublicationToScopus)
admin.site.register(OrderReviewForDissertation)
admin.site.register(OrganizeResearches)
admin.site.register(PublicationToMagazines)
admin.site.register(Consultation)
admin.site.register(ApplicationForFreeConsultation)
admin.site.register(Proofreading)
admin.site.register(PeerReview)
admin.site.register(OrganizeConferences)
admin.site.register(Translation, TranslationAdmin)

admin.site.register(GetPatent)
admin.site.register(GetGrant, GrantsAdmin)
admin.site.register(Baks)
admin.site.register(Scopus)
