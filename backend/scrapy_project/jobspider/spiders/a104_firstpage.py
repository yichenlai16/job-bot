import json
import scrapy
from scrapy.selector import Selector
from scrapy.http import FormRequest, Request
from jobspider.items import JobspiderItem
from datetime import date
import re
import requests
import inspect


def retrieve_name(var):
    callers_local_vars = inspect.currentframe().f_back.f_locals.items()
    return [var_name for var_name, var_val in callers_local_vars if var_val is var]


class A104Spider(scrapy.Spider):
    name = "104test"
    allowed_domains = ["www.104.com.tw"]

    # start_urls = ['https://www.104.com.tw/jobs/search/list']
    custom_settings = {
        "DEFAULT_REQUEST_HEADERS": {
            "accept": "application/json, text/plain, */*",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "zh=TW",
            "origin": "https://www.104.com.tw/",
            "referer": "https://www.104.com.tw/",
            "Content-Type": "application/json",
        }
    }

    start_url = "https://www.104.com.tw/jobs/search/list"

    def start_requests(self):
        for i in range(10):
            yield FormRequest(
                url=self.start_url + "?page=" + str(i + 1),
                method="GET",
                callback=self.parse,
            )
        # yield FormRequest(url=self.start_url, method="GET", callback=self.parse)

    def parse(self, response):
        body = json.loads(response.body)
        # print(body)
        jobs = body["data"]["list"]

        for job in jobs:
            # 如果沒東西就停止
            source_job_url = job["link"]["job"]
            source_company_url = job["link"]["cust"]

            jobNo = job["jobNo"]
            jobApplyCount = job["applyCnt"]

            source_job_website = str(source_job_url.split("/")[-3])
            source_job_cat = str(source_job_url.split("/")[-2])
            source_job_sn = str(source_job_url.split("/")[-1].split("?")[0])

            source_company_website = str(source_company_url.split("/")[-3])
            source_company_cat = str(source_company_url.split("/")[-2])
            source_company_sn = str(source_company_url.split("/")[-1].split("?")[0])

            metalist = [
                jobNo,
                jobApplyCount,
                source_job_website,
                source_job_cat,
                source_job_sn,
                source_company_website,
                source_company_cat,
                source_company_sn,
            ]
            meta = dict()

            for i in range(len(metalist)):
                meta[retrieve_name(metalist[i])[0]] = metalist[i]

            yield FormRequest(
                ("https://www.104.com.tw/job/ajax/content/" + source_job_sn),
                meta=meta,
                callback=self.getJobDetail,
                dont_filter=False,
            )

    def getJobDetail(self, response):
        body = json.loads(response.body)
        job_data = body["data"]

        jobName = job_data["header"]["jobName"]
        jobUpDate = job_data["header"]["appearDate"]
        jobDesc = job_data["jobDetail"]["jobDescription"]
        jobCategory = list(
            [x["description"] for x in job_data["jobDetail"]["jobCategory"]]
        )
        salaryLow = job_data["jobDetail"]["salaryMin"]
        salaryHigh = job_data["jobDetail"]["salaryMax"]
        salaryType = job_data["jobDetail"]["salaryType"]
        jobRole = job_data["jobDetail"]["jobType"]
        workType = list([x for x in job_data["jobDetail"]["workType"]])
        jobArea = job_data["jobDetail"]["addressRegion"]
        jobAddress = job_data["jobDetail"]["addressDetail"]
        jobIndustryArea = job_data["jobDetail"]["industryArea"]
        jobLon = job_data["jobDetail"]["longitude"]
        jobLat = job_data["jobDetail"]["latitude"]
        manageRespon = job_data["jobDetail"]["manageResp"]
        businessTrip = job_data["jobDetail"]["businessTrip"]
        workPeriod = job_data["jobDetail"]["workPeriod"]
        vacationPolicy = job_data["jobDetail"]["vacationPolicy"]
        startWorkDay = job_data["jobDetail"]["startWorkingDay"]
        hireType = job_data["jobDetail"]["hireType"]
        needEmployee = job_data["jobDetail"]["needEmp"]
        landmark = job_data["jobDetail"]["landmark"]
        if job_data["jobDetail"]["remoteWork"]:
            remoteWork = job_data["jobDetail"]["remoteWork"]["description"]
        else:
            remoteWork = None
        delegatedRecruit = job_data["jobDetail"]["delegatedRecruit"]
        roleDesc = list(
            [x["description"] for x in job_data["condition"]["acceptRole"]["role"]]
        )
        workExp = job_data["condition"]["workExp"]
        edu = job_data["condition"]["edu"]
        major = job_data["condition"]["major"]

        # for i in job_data['condition']['language']:
        #     j = i['language'] + i['ability']

        language = [
            i["language"] + ", " + i["ability"]
            for i in job_data["condition"]["language"]
        ]
        # language = job_data['condition']['language']
        localLanguage = [
            i["language"] + i["ability"] for i in job_data["condition"]["localLanguage"]
        ]
        specialty = list([x["description"] for x in job_data["condition"]["specialty"]])
        skill = list([x["description"] for x in job_data["condition"]["skill"]])
        # certificate = job_data["condition"]["certificate"]
        certificate = ""
        driverLicense = job_data["condition"]["driverLicense"]
        other = job_data["condition"]["other"]

        meta = dict()
        for i in response.meta:
            meta[i] = response.meta[i]

        metalist = [
            jobName,
            jobUpDate,
            jobDesc,
            jobCategory,
            salaryLow,
            salaryHigh,
            salaryType,
            jobRole,
            workType,
            jobArea,
            jobAddress,
            jobIndustryArea,
            jobLon,
            jobLat,
            manageRespon,
            businessTrip,
            workPeriod,
            vacationPolicy,
            startWorkDay,
            hireType,
            needEmployee,
            landmark,
            remoteWork,
            delegatedRecruit,
            roleDesc,
            workExp,
            edu,
            major,
            language,
            localLanguage,
            specialty,
            skill,
            certificate,
            driverLicense,
            other,
        ]

        for i in range(len(metalist)):
            if metalist[i] != "":
                meta[retrieve_name(metalist[i])[0]] = metalist[i]
            else:
                meta[retrieve_name(metalist[i])[0]] = str([])

        yield FormRequest(
            "https://www.104.com.tw/company/ajax/content/" + meta["source_company_sn"],
            meta=meta,
            callback=self.getCompany,
            dont_filter=True,
        )

    def getCompany(self, response):
        body = response.body
        datas = json.loads(body)
        datas = datas["data"]

        item = JobspiderItem()

        results = [
            "jobNo",
            "jobApplyCount",
            "source_job_website",
            "source_job_cat",
            "source_job_sn",
            "source_company_website",
            "source_company_cat",
            "source_company_sn",
            "jobName",
            "jobUpDate",
            "jobDesc",
            "jobCategory",
            "salaryLow",
            "salaryHigh",
            "salaryType",
            "jobRole",
            "workType",
            "jobArea",
            "jobAddress",
            "jobIndustryArea",
            "jobLon",
            "jobLat",
            "manageRespon",
            "businessTrip",
            "workPeriod",
            "vacationPolicy",
            "startWorkDay",
            "hireType",
            "needEmployee",
            "landmark",
            "remoteWork",
            "delegatedRecruit",
            "roleDesc",
            "workExp",
            "edu",
            "major",
            "language",
            "localLanguage",
            "specialty",
            "skill",
            "certificate",
            "driverLicense",
            "other",
        ]

        for i in results:
            try:
                item[i] = response.meta[i]
            except:
                item[i] = None
        # item['jobNo'] = response.meta['jobNo']
        # item['jobApplyCount'] = response.meta['jobApplyCount']
        # item['source_job_website'] = response.meta['source_job_website']
        # item['source_job_cat'] = response.meta['source_job_cat']
        # item['source_job_sn'] = response.meta['source_job_sn']
        # item['source_company_website'] = response.meta['source_company_website']
        # item['source_company_sn'] = response.meta['source_company_sn']
        # item['jobName'] = response.meta['jobName']
        # item['jobUpDate'] = response.meta['jobUpDate']
        # item['jobDesc'] = response.meta['jobDesc']
        # item['jobCategory'] = response.meta['jobCategory']
        # item['salaryLow'] = response.meta['salaryLow']
        # item['salaryHigh'] = response.meta['salaryHigh']
        # item['salaryType'] = response.meta['salaryType']
        # item['jobRole'] = response.meta['jobRole']
        # item['workType'] = response.meta['workType']
        # item['jobArea'] = response.meta['jobArea']
        # item['jobAddress'] = response.meta['jobAddress']
        # item['jobIndustryArea'] = response.meta['jobIndustryArea']
        # item['jobLon'] = response.meta['jobLon']
        # item['jobLat'] = response.meta['jobLat']
        # item['manageRespon'] = response.meta['manageRespon']
        # item['businessTrip'] = response.meta['businessTrip']
        # item['workPeriod'] = response.meta['workPeriod']
        # item['vacationPolicy'] = response.meta['vacationPolicy']
        # item['startWorkDay'] = response.meta['startWorkDay']
        # item['hireType'] = response.meta['hireType']
        # item['needEmployee'] = response.meta['needEmployee']
        # item['landmark'] = response.meta['landmark']
        # item['remoteWork'] = response.meta['remoteWork']
        # item['delegatedRecruit'] = response.meta['delegatedRecruit']
        # item['roleDesc'] = response.meta['roleDesc']
        # item['workExp'] = response.meta['workExp']
        # item['edu'] = response.meta['edu']
        # item['major'] = response.meta['major']
        # item['language'] = response.meta['language']
        # item['localLanguage'] = response.meta['localLanguage']
        # item['specialty'] = response.meta['specialty']
        # item['skill'] = response.meta['skill']
        # item['certificate'] = response.meta['certificate']
        # item['driverLicense'] = response.meta['driverLicense']
        # item['other'] = response.meta['other']

        if datas:
            item["fromComp_companyName"] = datas["custName"]
            item["companyLink"] = datas["custLink"]
            if datas["postalCode"] == "":
                item["postalCode"] = None
            else:
                item["postalCode"] = datas["postalCode"]
            item["company_addrNoDesc"] = datas["addrNoDesc"]
            item["company_address"] = datas["address"]
            item["capital"] = datas["capital"]
            item["empNo"] = datas["empNo"]
            item["hrName"] = datas["hrName"]
            item["indcat"] = datas["indcat"]
            item["industryDesc"] = datas["industryDesc"]
            item["company_lat"] = datas["lat"]
            item["company_lon"] = datas["lon"]
            item["phone"] = datas["phone"]
            item["fax"] = datas["fax"]
            item["profile"] = datas["profile"]
            item["news"] = datas["news"]
            item["newsLink"] = datas["newsLink"]
            item["product"] = datas["product"]
            item["welfare"] = datas["welfare"]
            item["legalTagNames"] = datas["legalTagNames"]
            item["tagNames"] = datas["tagNames"]

        for i in item:
            if item[i] == "":
                item[i] = None

        yield item
