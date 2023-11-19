from typing import cast
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.json import JSONField


from django.contrib.postgres.fields import ArrayField
from django.utils import timezone
from django.contrib.postgres.fields import ArrayField

# Create your models here.





class Companys(models.Model):
    name = models.TextField()
    link = models.URLField(null=True,blank=True)
    area = models.TextField(null=True,blank=True)
    address = models.TextField(null=True,blank=True)
    capital = models.TextField(null=True,blank=True)
    empNo = models.TextField(null=True,blank=True)
    contactPerson = models.TextField(null=True,blank=True)
    lat = models.FloatField(null=True,blank=True)
    lon = models.FloatField(null=True,blank=True)
    phone = models.TextField(null=True,blank=True)
    fax = models.TextField(null=True,blank=True)
    companyProfile = models.TextField(null=True,blank=True)
    news = models.TextField(null=True,blank=True)
    newsLink = models.TextField(null=True,blank=True)
    product = models.TextField(null=True,blank=True)
    welfare = models.TextField(null=True,blank=True)
    legalTagNames = models.TextField(null=True,blank=True)
    tagNames = models.TextField(null=True,blank=True)
    category = models.TextField(null=True,blank=True)
    categoryDesc = models.TextField(null=True,blank=True)

    class Meta:
        db_table = 'Company'
        verbose_name_plural = '公司'

    def get_jobs(self):
        jobs = Jobs.objects.filter(company=self)
        return jobs

    def __unicode__(self):
        return self.name


class Jobs(models.Model):
    source = models.TextField(null=True)
    source_url = models.URLField(null=True)
    name = models.TextField()
    jobRole = models.IntegerField(null=True)
    workType = ArrayField(
        models.TextField(null=True),null=True
    )
    workPeriod = models.TextField(null=True)
    jobDesc = models.TextField(null=True)
    area = models.TextField(null=True)
    address = models.TextField(null=True)
    IndustryArea = models.TextField(null=True)
    UpDate = models.DateField(null=True)
    ApplyCount = models.IntegerField(null=True)
    company = models.ForeignKey(
        Companys,
        related_name='jobCompany',
        on_delete=models.CASCADE,
    )
    manageRespon = models.TextField(null=True,blank=True)
    businessTrip = models.TextField(null=True,blank=True)
    vacationPolicy = models.TextField(null=True,blank=True)
    startWorkDay = models.TextField(null=True,blank=True)
    lat = models.FloatField(null=True)
    lon = models.FloatField(null=True)
    salaryHigh = models.IntegerField(null=True)
    salaryLow = models.IntegerField(null=True)
    salaryType = models.IntegerField(null=True)
    hireType = models.TextField(null=True,blank=True)
    needEmployee = models.TextField(null=True,blank=True)
    landmark = models.TextField(null=True,blank=True)
    remoteWork = models.TextField(null=True,blank=True)
    delegatedRecruit = models.TextField(null=True,blank=True)
    roleDesc = JSONField(null=True,blank=True)
    workExp = models.TextField(null=True,blank=True)
    edu = models.TextField(null=True,blank=True)
    major = JSONField(null=True,blank=True)
    language = JSONField(null=True,blank=True)
    localLanguage = JSONField(null=True,blank=True)
    specialty = JSONField(null=True,blank=True)
    skill = JSONField(null=True,blank=True)
    certificate = JSONField(null=True,blank=True)
    driverLicense = JSONField(null=True,blank=True)
    other = models.TextField(null=True,blank=True)
    category = ArrayField(
        models.TextField(null=True,default=list()))
    alerted = models.BooleanField(default=False)
    import_date = models.DateField(auto_now_add=True, blank=True,null=True)

    class Meta:
        db_table = 'Job'
        verbose_name_plural = '職缺'



class CompanySource(models.Model):
    company_id = models.ForeignKey(
        Companys, null=True,blank=True, on_delete=CASCADE)
    source = models.TextField(null=True)
    source_url = models.URLField(null=True)

    class Meta:
        db_table = 'CompanySource'
        verbose_name_plural = '公司資料來源'
