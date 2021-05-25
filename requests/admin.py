from django.contrib import admin
from .models import (
    ResearchGrant,
    PublicationToScopus,
    OrderReviewForDissertation,
    GetPatent,
    OrderToGraphicalMaterials,
    OrganizeResearches,
    PublicationToMagazines,
    Consultation,
    ApplicationForFreeConsultation,
    Proofreading,
    PeerReview
)

admin.site.register(ResearchGrant)
admin.site.register(PublicationToScopus)
admin.site.register(OrderReviewForDissertation)
admin.site.register(GetPatent)
admin.site.register(OrderToGraphicalMaterials)
admin.site.register(OrganizeResearches)
admin.site.register(PublicationToMagazines)
admin.site.register(Consultation)
admin.site.register(ApplicationForFreeConsultation)
admin.site.register(Proofreading)
admin.site.register(PeerReview)

