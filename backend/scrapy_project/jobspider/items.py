# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.exporters import PythonItemExporter


class JobspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    ###jobs model
    jobApplyCount= scrapy.Field()
    jobName= scrapy.Field()
    jobUpDate= scrapy.Field()
    jobDesc= scrapy.Field()
    jobCategory= scrapy.Field()
    salaryLow= scrapy.Field()
    salaryHigh= scrapy.Field()
    salaryType= scrapy.Field()
    jobRole= scrapy.Field()
    workType= scrapy.Field()
    jobArea= scrapy.Field()
    jobAddress= scrapy.Field()
    jobIndustryArea= scrapy.Field()
    jobLon= scrapy.Field()
    jobLat= scrapy.Field()
    manageRespon= scrapy.Field()
    businessTrip= scrapy.Field()
    workPeriod= scrapy.Field()
    vacationPolicy= scrapy.Field()
    startWorkDay= scrapy.Field()
    hireType= scrapy.Field()
    needEmployee= scrapy.Field()
    landmark= scrapy.Field()
    remoteWork= scrapy.Field()
    delegatedRecruit= scrapy.Field()
    roleDesc= scrapy.Field()
    workExp= scrapy.Field()
    edu= scrapy.Field()
    major= scrapy.Field()
    language= scrapy.Field()
    localLanguage= scrapy.Field()
    specialty= scrapy.Field()
    skill= scrapy.Field()
    certificate= scrapy.Field()
    driverLicense= scrapy.Field()
    other= scrapy.Field()
    ###jobs model

    ###company model
    fromComp_companyName = scrapy.Field()
    companyLink = scrapy.Field()
    postalCode = scrapy.Field()
    company_addrNoDesc = scrapy.Field()
    company_address = scrapy.Field()
    capital = scrapy.Field()
    empNo = scrapy.Field()
    hrName = scrapy.Field()
    indcat = scrapy.Field()
    industryDesc = scrapy.Field()
    company_lat = scrapy.Field()
    company_lon = scrapy.Field()
    phone = scrapy.Field()
    fax = scrapy.Field()
    profile = scrapy.Field()
    news = scrapy.Field()
    newsLink = scrapy.Field()
    product = scrapy.Field()
    welfare = scrapy.Field()
    legalTagNames = scrapy.Field()
    tagNames = scrapy.Field()
    ###company model

    ###source model
    jobNo = scrapy.Field()
    fromComp_companyNo = scrapy.Field()
    source_job_website = scrapy.Field()
    source_job_cat = scrapy.Field()
    source_job_sn = scrapy.Field()
    source_company_website = scrapy.Field()
    source_company_cat = scrapy.Field()
    source_company_sn = scrapy.Field()
    ###source model

    pass
