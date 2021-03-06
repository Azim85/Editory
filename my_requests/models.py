from pages.models import Topic
from django.db import models
from users.models import CustomUser
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.translation import gettext as _


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


# updated
class GetPatent(models.Model):
    last_name = models.CharField(max_length=255, null=True)
    first_name = models.CharField(max_length=255, null=True)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    organization = models.CharField(max_length=255)
    org_contacts = models.CharField(max_length=255)
    org_address = models.CharField(max_length=255)
    application_upload = models.FileField(upload_to='app_requests/', blank=True)
    is_agree = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.last_name} {self.first_name}"

    class Meta:
        verbose_name = 'Patent'
        verbose_name_plural = 'Patents'

# updated
class GetGrant(models.Model):
    last_name = models.CharField(max_length=255, null=True)
    first_name = models.CharField(max_length=255, null=True)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    organization = models.CharField(max_length=255)
    org_contacts = models.CharField(max_length=255)
    org_address = models.CharField(max_length=255)
    application_upload = models.FileField(upload_to='app_requests/', blank=True)
    is_agree = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.last_name} {self.first_name}"

    class Meta:
        verbose_name = 'Grant'
        verbose_name_plural = 'Grants'

#updated
class GetDesign(models.Model):
    last_name = models.CharField(max_length=255, null=True)
    first_name = models.CharField(max_length=255, null=True)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    organization = models.CharField(max_length=255)
    org_contacts = models.CharField(max_length=255)
    org_address = models.CharField(max_length=255)
    is_agree = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.last_name} {self.first_name}"

    class Meta:
        verbose_name = 'Design'
        verbose_name_plural = 'Designs'


# updated
class Baks(models.Model):
    last_name = models.CharField(max_length=255, null=True)
    first_name = models.CharField(max_length=255, null=True)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    organization = models.CharField(max_length=255)
    org_contacts = models.CharField(max_length=255)
    org_address = models.CharField(max_length=255)
    file_upload = models.FileField(upload_to='files/', null=True, blank=True)
    comment = models.TextField(blank=True, null=True)
    is_agree = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.last_name} {self.first_name}"

    class Meta:
        verbose_name = 'BAK'
        verbose_name_plural = 'BAKs'


# updated
class Scopus(models.Model):
    last_name = models.CharField(max_length=255, null=True)
    first_name = models.CharField(max_length=255, null=True)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    organization = models.CharField(max_length=255)
    org_contacts = models.CharField(max_length=255)
    org_address = models.CharField(max_length=255)
    file_upload = models.FileField(upload_to='files/', null=True, blank=True)
    comment = models.TextField(blank=True, null=True)
    is_agree = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.last_name} {self.first_name}"

    class Meta:
        verbose_name = 'Scopus'
        verbose_name_plural = 'Scopus requests'


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
    ('?????????????????? ????????????????????????', '?????????????????? ????????????????????????'),
    ('?????????????? ????????????????????????????', '?????????????? ????????????????????????????'),
    ('?????????????? ????????????????????????????', '?????????????? ????????????????????????????'),
    ('???????????????????? ?? ??????????????', '???????????????????? ?? ??????????????'),
)


class OrganizeResearches(models.Model):
    """
    url: research_strategy name:research_strategy
    page: research_strategy.html
    """
    last_name = models.CharField(max_length=255, null=True)
    first_name = models.CharField(max_length=255, null=True)
    phone = models.CharField(max_length=15)
    email = models.EmailField(blank=True)
    organization = models.CharField(max_length=255)
    org_contacts = models.CharField(max_length=255)
    org_address = models.CharField(max_length=255)
    is_agree = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.last_name

    # class Meta:
    #     verbose_name = '????????????????????????'
    #     verbose_name_plural = '?????????????????? ????????????????????????'


# updated
class OrganizeConferences(models.Model):
    """
    url:creat_conferences  name: 'creat_conferences'
    page: creat_conference.html
    """
    last_name = models.CharField(max_length=255, null=True)
    first_name = models.CharField(max_length=255, null=True)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    organization = models.CharField(max_length=255)
    org_contacts = models.CharField(max_length=255)
    org_address = models.CharField(max_length=255)
    comment = models.TextField(blank=True, null=True)
    is_agree = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = 'Create Conference'
        verbose_name_plural = 'Crete Conferences'


class Grants(models.Model):
    """
    url:grants/  name: 'grants'
    page: grants.html
    """
    last_name = models.CharField(max_length=255, null=True)
    first_name = models.CharField(max_length=255, null=True)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    organization = models.CharField(max_length=255)
    org_contacts = models.CharField(max_length=255)
    org_address = models.CharField(max_length=255)
    is_agree = models.BooleanField(default=False)
    theme = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = 'Grant'
        verbose_name_plural = 'Grants'


class Consultation(models.Model):
    first_name = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=15, null=True)
    is_agree = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name


# todo tugadi
class Language(models.Model):
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=15, null=True)
    email = models.CharField(max_length=100, null=True)
    file = models.FileField(upload_to='files/', null=True, blank=True)
    is_agree = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = "language_editing"
        verbose_name_plural = "language_editing"


RESEARCH_AREA = (
    ('???????????????????? ?? ????????????????????????', _('???????????????????? ?? ????????????????????????')),
    ('????????????????', _('????????????????')),
    ('????????????', _('????????????')),
    ('??????????', _('??????????')),
    ('???????????????? ?? ?????????? ?? ??????????', _('???????????????? ?? ?????????? ?? ??????????')),
    ('??????????????????', _('??????????????????')),
    ('????????????????', _('????????????????')),
    ('????????????', _('????????????')),
    ('???????????????????? ??????????', _('???????????????????? ??????????')),
    ('????????????', _('????????????'),)
)


LANG = (
    ('English', 'English'),
    ('Russian', 'Russian'),
    ('Uzbek', 'Uzbek')
)

# updated
class Translation(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True)
    language = models.CharField(max_length=100, choices=LANG)
    research_area = models.CharField(max_length=100, choices=RESEARCH_AREA)
    comment = models.TextField(blank=True)
    file = models.FileField(upload_to='files/')
    char_amount = models.IntegerField(default=0)
    is_agree = models.BooleanField(default=False)

    def __str__(self):
        return self.language

    class Meta:
        verbose_name = 'Translation'
        verbose_name_plural = 'Translations'


DEGREE = (
    ('???????????????? ????????', '???????????????? ???????? '),
    ('???????????? ????????', '????????????  ????????'),
    ('???????????? ??????????????????', '???????????? ?????????????????? PhD'),
    ('???????????????????????????????? ????????????', '???????????????????????????????? ???????????? (Dr. habil.)'),
)


class ApplicationForFreeConsultation(models.Model):
    """
    url:conferences/   name:conferences
    page: conferences.html  
    """
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
    is_agree = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = 'Participation in Conference'
        verbose_name_plural = 'Participation in Conference'


LANGUAGE = (
    ('English', 'English'),
    ('??????????????', '??????????????'),
    ("O'zbekcha", "O'zbekcha"),
)


# updated
class Proofreading(models.Model):
    author = models.CharField(max_length=100)
    material_name = models.CharField(max_length=255)
    research_area = models.CharField(max_length=255, choices=RESEARCH_AREA)
    choose = models.CharField(max_length=100)
    word_count = models.CharField(max_length=100)
    language_editing = models.CharField(max_length=50, choices=LANGUAGE)
    certificate = models.TextField()
    comment = models.TextField(blank=True)
    upload_file = models.FileField(upload_to='files/')
    is_agree = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author

    # class Meta:
    #     verbose_name = '???????????? ???? ????????????????????'
    #     verbose_name_plural = '???????????? ???? ????????????????????'


class PeerReview(models.Model):
    author = models.CharField(max_length=100)
    material_name = models.CharField(max_length=255)
    research_area = models.CharField(max_length=255)
    choose = models.CharField(max_length=100, choices=TOPICS)
    academic_degree = models.CharField(max_length=255)
    organization = models.CharField(max_length=255)
    scientific_adviser = models.CharField(max_length=50)
    comment = models.TextField(blank=True)
    upload_file = models.FileField(upload_to='files/')
    is_agree = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author

    # class Meta:
    #     verbose_name = '?????????? ???????????????? ???? ??????????????????????'
    #     verbose_name_plural = '?????????? ???????????????? ???? ??????????????????????'


class TranslationCostModel(models.Model):
    cost = models.DecimalField(max_digits=10, decimal_places=2, default=0)



