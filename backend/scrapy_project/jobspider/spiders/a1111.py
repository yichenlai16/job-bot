import json
import scrapy
from scrapy.selector import Selector
from scrapy.http import FormRequest, Request
from jobspider.items import JobspiderItem

import re
import requests


class A1111Spider(scrapy.Spider):
    name = '1111'
    allowed_domains = ['www.1111.com.tw']
    start_url = 'https://www.1111.com.tw/search/job?'

    area = ''
    category = ''

    form = {
    'da':'3',
    'page':'1',
    'ps':'100',
    'act':'load_page',
    'd0':area,
    'c0':category
    }
    

    def start_requests(self):
        yield FormRequest(url=self.start_url,method="GET",formdata=self.form,callback=self.parse)

    
    def parse(self, response):
        jobs = response.xpath('/html/body/div')
        for job in jobs:
            jobUrl = job.xpath('./div[1]/div[1]/a/@href').get()
            jobUrl = jobUrl.replace(r'\"', "")
            yield FormRequest(url=jobUrl,method="get",callback=self.jobParse)
            companyUrl = job.xpath('./div[1]/div[2]/a[1]/@href').get()

    def jobParse(self,response):
        title_path = "/html/body/main[@class='wrapper']/section[@class='vacancy-header']/div[@class='container']/div[@class='row']/div[@class='col-lg-12']/div[@class='vacancy-header-row']/div[@class='vacancy-header-col-lg']/div[@class='vacancy-company-infoTop']/h1/span[@class='jobTitle']/text()"
        company_path = "/html/body/main[@class='wrapper']/section[@class='vacancy-header']/div[@class='container']/div[@class='row']/div[@class='col-lg-12']/div[@class='vacancy-header-row']/div[@class='vacancy-header-col-lg']/div[@class='vacancy-company-infoTop']/div[@class='company-name-box']/div[@class='vacancy-company-name']/a/text()"
        #工作時間 日班 晚班
        workPeriod_path = "/html/body/main[@class='wrapper']/section[@id='Job-Detail']/div[@class='container']/div[@class='row']/div[@id='job-detail-info']/div[@class='job-detail-panel mt0']/div[@class='job-detail-panel-content work-system']/dl/dd[1]/span/text()"
        vocationPolicy_path = "/html/body/main[@class='wrapper']/section[@id='Job-Detail']/div[@class='container']/div[@class='row']/div[@id='job-detail-info']/div[@class='job-detail-panel mt0']/div[@class='job-detail-panel-content work-system']/dl/dd[2]/span/text()"
        # salary_path = "/html/body/main[@class='wrapper']/section[@id='Job-Detail']/div[@class='container']/div[@class='row']/div[@id='job-detail-info']/div[@class='job-detail-panel mt0']/div[@class='job-detail-panel-content work-system']/dl/dd[3]/span[@class='text--danger tooltip']/text()"
        
        salary_path = "/html/body/main/section[2]/div/div/div[1]/div[1]/div[2]/dl/dd[3]/span/text()"
       #工作性質 全職 兼職
        jobType_path = "/html/body/main[@class='wrapper']/section[@id='Job-Detail']/div[@class='container']/div[@class='row']/div[@id='job-detail-info']/div[@class='job-detail-panel mt0']/div[@class='job-detail-panel-content work-system']/dl/dd[4]/span/text()"
        
        #職位是list
        category_path = "/html/body/main[@class='wrapper']/section[@id='Job-Detail']/div[@class='container']/div[@class='row']/div[@id='job-detail-info']/div[@class='job-detail-panel mt0']/div[@class='job-detail-panel-content work-system']/dl/dd[5]/span[@class='category']/a/@title"

        address_path = "/html/body/main[@class='wrapper']/section[@id='Job-Detail']/div[@class='container']/div[@class='row']/div[@id='job-detail-info']/div[@class='job-detail-panel mt0']/div[@class='job-detail-panel-content work-location']/div[@class='modal-area']/span/text()"

        # x = response.xpath(x).get()
        
        title = response.xpath(title_path).get().strip()
        company = response.xpath(company_path).get().strip()
        workPeriod = response.xpath(workPeriod_path).get().strip()
        vocationPolicy = response.xpath(vocationPolicy_path).get().strip()
        salary = response.xpath(salary_path).get().strip()
        jobType = response.xpath(jobType_path).get().strip()
        category = response.xpath(category_path).getall()
        address = response.xpath(address_path).get().strip()

        print(salary)
        print(title,company,salary,workPeriod,vocationPolicy,jobType,category,address)
        print()
