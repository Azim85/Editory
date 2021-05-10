from django.contrib import admin
from .models import (
    ResearchGrant,
    PublicationToScopus,
    OrderReviewForDissertation,
    GetPatent,
    OrderToGraphicalMaterials,
    OrganizeResearches,
    PublicationToMagazines,
)

admin.site.register(ResearchGrant)
admin.site.register(PublicationToScopus)
admin.site.register(OrderReviewForDissertation)
admin.site.register(GetPatent)
admin.site.register(OrderToGraphicalMaterials)
admin.site.register(OrganizeResearches)
admin.site.register(PublicationToMagazines)
