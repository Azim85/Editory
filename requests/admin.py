from django.contrib import admin
from .models import (
    ResearchGrant,
    PublicationToScopus,
    OrderReviewForDissertation,
    GetPatent,
    OrganizeResearches,
    PublicationToMagazines,
    Consultation,
    ApplicationForFreeConsultation,
    Proofreading,
    PeerReview,
    OrganizeConferences,
    Grants,
    Translation
)

class GrantsAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'theme']

class TranslationAdmin(admin.ModelAdmin):
    list_display = ['user', 'language']

admin.site.register(ResearchGrant)
admin.site.register(PublicationToScopus)
admin.site.register(OrderReviewForDissertation)
admin.site.register(GetPatent)
admin.site.register(OrganizeResearches)
admin.site.register(PublicationToMagazines)
admin.site.register(Consultation)
admin.site.register(ApplicationForFreeConsultation)
admin.site.register(Proofreading)
admin.site.register(PeerReview)
admin.site.register(OrganizeConferences)
admin.site.register(Grants, GrantsAdmin)
admin.site.register(Translation, TranslationAdmin)

