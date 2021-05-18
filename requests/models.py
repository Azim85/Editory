from django.db import models
from users.models import CustomUser
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


class ResearchGrant(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    last_name = models.CharField(max_length=255, null=True)
    first_name = models.CharField(max_length=255, null=True)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    organization = models.CharField(max_length=255)
    org_contacts = models.CharField(max_length=255)
    org_address = models.CharField(max_length=255)
    application_upload = models.FileField(upload_to='app_requests/')
    is_agree = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.fullname

    class Meta:
        verbose_name = 'Research Grant'
        verbose_name_plural = 'Research Grants'


class GetPatent(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    last_name = models.CharField(max_length=255, null=True)
    first_name = models.CharField(max_length=255, null=True)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    organization = models.CharField(max_length=255)
    org_contacts = models.CharField(max_length=255)
    org_address = models.CharField(max_length=255)
    application_upload = models.FileField(upload_to='app_requests/')
    is_agree = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.fullname

    class Meta:
        verbose_name = 'Patent'
        verbose_name_plural = 'Patents'


class PublicationToScopus(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    last_name = models.CharField(max_length=255, null=True)
    first_name = models.CharField(max_length=255, null=True)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    organization = models.CharField(max_length=255)
    org_contacts = models.CharField(max_length=255)
    org_address = models.CharField(max_length=255)
    application_upload = models.FileField(upload_to='app_requests/')
    is_agree = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.fullname

    class Meta:
        verbose_name = 'Publication to Scopus'
        verbose_name_plural = 'Scopus Publications'


class OrderReviewForDissertation(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    astronomy = models.CharField(max_length=255, blank=True)
    biology = models.CharField(max_length=255, blank=True)
    business = models.CharField(max_length=255, blank=True)
    chemistry = models.CharField(max_length=255, blank=True)
    ecology = models.CharField(max_length=255, blank=True)
    engineering = models.CharField(max_length=255, blank=True)
    medicine = models.CharField(max_length=255, blank=True)
    physics = models.CharField(max_length=255, blank=True)
    social_science = models.CharField(max_length=255, blank=True)
    other = models.CharField(max_length=255, blank=True)
    additional_comment = models.TextField()
    author_name = models.CharField(max_length=255)
    science_degree = models.CharField(max_length=255)
    organisation = models.CharField(max_length=255)
    material_name = models.CharField(max_length=255)
    supervisor_name = models.CharField(max_length=255)
    is_agree = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)


class PublicationToMagazines(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    last_name = models.CharField(max_length=255, null=True)
    first_name = models.CharField(max_length=255, null=True)
    phone = models.CharField(max_length=15)
    email = models.EmailField(blank=True)
    organization = models.CharField(max_length=255)
    org_contacts = models.CharField(max_length=255)
    org_address = models.CharField(max_length=255)
    is_agree = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)


TOPICS = (
    ('стратегия исследования', 'стратегия исследования'),
    ('партнёрство и сотрудничество', 'партнёрство и сотрудничество'),
    ('финансирование', 'финансирование'),
    ('управление исследовательским процессом',
     'управление исследовательским процессом'),
    ('общая консультация', 'общая консультация'),
)


class OrganizeResearches(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    last_name = models.CharField(max_length=255, null=True)
    first_name = models.CharField(max_length=255, null=True)
    phone = models.CharField(max_length=15)
    email = models.EmailField(blank=True)
    select_topic = models.CharField(max_length=100, choices=TOPICS)
    organization = models.CharField(max_length=255)
    org_contacts = models.CharField(max_length=255)
    org_address = models.CharField(max_length=255)
    is_agree = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)


class OrderToGraphicalMaterials(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    last_name = models.CharField(max_length=255, null=True)
    first_name = models.CharField(max_length=255, null=True)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    organization = models.CharField(max_length=255)
    org_contacts = models.CharField(max_length=255)
    org_address = models.CharField(max_length=255)
    is_agree = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)



class Consultation(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    material = models.CharField(max_length=100, choices=TOPICS)
    organization = models.CharField(max_length=255)
    organization_contacts = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = 'консультация'
        verbose_name_plural = 'консультации'

    
DEGREE = (
    ('кандидат наук', 'кандидат наук '),
    ('доктор наук', 'доктор  наук'),
    ('доктор философии', 'доктор философии PhD'),
    ('хабилитированный доктор', 'хабилитированный доктор (Dr. habil.)'),
)
class ApplicationForFreeConsultation(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    busyness = models.CharField(max_length=100)
    place_of_work = models.CharField(max_length=100)
    academic_degree = models.CharField(max_length=100, choices=DEGREE)
    application_name = models.CharField(max_length=100)
    conference = models.CharField(max_length=100)
    section = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    upload_file = models.FileField(upload_to='files/')
    created_at = models.DateTimeField(auto_now_add=True)