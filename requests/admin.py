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
    Grants
)

class GrantsAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'theme']

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

