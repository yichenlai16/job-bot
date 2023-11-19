import concurrent.futures
import threading

from scrapy_project.jobspider.util.category import *
from scrapy_project.jobspider.util.db import db_connect, create_forum_table, Job, Company, CompanySource, Items

from sqlalchemy import select, MetaData
from sqlalchemy.orm import sessionmaker

metadata = MetaData()

engine = db_connect()
create_forum_table(engine)
Session = sessionmaker(bind=engine)

lock = threading.Lock() 

def item2job(item):
    with lock:
        item = item
        #if job exists in db?
        
        
        with Session() as session:
            query = session.query(Job.id).\
                filter((Job.source_url) == (item['source_job_website']+'/' +item['source_job_cat']+'/'+item['source_job_sn']))

        if query.first():
            print('pass!')
            query = session.query(Items).\
                filter((Items.jobNo) == item['jobNo'])
            session.delete(query.first())
            session.commit()
        
        else:
            #if company exists in db?
            with Session() as session:
                query = session.query(Company.id).\
                    filter((Company.name) == item['fromComp_companyName'])

                if not query.first():
                    company = Company(
                        name=item['fromComp_companyName'],
                        link=item['companyLink'],
                        area=item['company_addrNoDesc'],
                        address=item['company_address'],
                        capital = item['capital'],
                        empNo=item['empNo'],
                        contactPerson=item['hrName'],
                        lat=item['company_lat'],
                        lon=item['company_lon'],
                        phone=item['phone'],
                        fax=item['fax'],
                        companyProfile=item['profile'],
                        news=item['news'],
                        newsLink=item['newsLink'],
                        product=item['product'],
                        welfare=welfare(item['welfare']),
                        legalTagNames=item['legalTagNames'],
                        tagNames=item['tagNames'],
                        category=company_category(item['indcat']),
                        categoryDesc=item['industryDesc']
                    )
                    session.add(company)
                    session.commit()
                companyID = query.first().id

        # CompanySource

            with Session() as session:
                query = session.query(CompanySource.id).\
                    filter((CompanySource.source_url) == (item['source_company_website']+'/'+item['source_company_cat']+'/'+item['source_company_sn']))
                
                if not query.first():
                    company_source = CompanySource(
                        source=item['source_company_website'],
                        source_url=(item['source_company_website']+'/' +
                                    item['source_company_cat']+'/'+item['source_company_sn']),
                        company_id_id=companyID
                    )
                    # with Session() as session:
                    session.add(company_source)
                    session.commit()


            # Job
            job = Job(
                source=item['source_job_website'],
                source_url=item['source_job_website']+'/' +item['source_job_cat']+'/'+item['source_job_sn'],
                name=item['jobName'],
                jobRole=item['jobRole'],
                workType=item['workType'],
                workPeriod=item['workPeriod'],
                jobDesc=item['jobDesc'],
                area=item['jobArea'],
                address=item['jobAddress'],
                IndustryArea=item['jobIndustryArea'],
                UpDate=item['jobUpDate'],
                ApplyCount=item['jobApplyCount'],
                manageRespon=item['manageRespon'],
                businessTrip=item['businessTrip'],
                vacationPolicy=item['vacationPolicy'],
                startWorkDay=item['startWorkDay'],
                lat=item['jobLat'],
                lon=item['jobLon'],
                salaryHigh=item['salaryHigh'],
                salaryLow=item['salaryLow'],
                salaryType=item['salaryType'],
                hireType=item['hireType'],
                needEmployee=item['needEmployee'],
                landmark=item['landmark'],
                remoteWork=item['remoteWork'],
                delegatedRecruit=item['delegatedRecruit'],
                roleDesc=[identity(x) for x in item['roleDesc']],
                workExp=[experience(x) for x in item['workExp']],
                edu=item['edu'],
                major=[department(x) for x in item['major']],
                language=item['language'],
                localLanguage=item['localLanguage'],
                specialty=item['specialty'],
                skill=item['skill'],
                certificate=item['certificate'],
                driverLicense=item['driverLicense'],
                other=item['other'],
                category=[job_category(x) for x in item['jobCategory']],
                company_id=companyID,
                alerted = False
                
            )

            with Session() as session:
                session.add(job)
                session.commit()
                
                query = session.query(Items).\
                        filter((Items.jobNo) == item['jobNo'])
                session.delete(query.first())
                session.commit()
        

        # if __name__ == '__main__': 
        #     global Processed, num
        #     Processed += 1
        #     print ('Progress: {}/{} members processed'.format(Processed, num))



def scrub():
    with Session() as session:
        items = session.query(Items)
    item = [i.__dict__ for i in items.all()]  
    print(len(item))
    # if __name__ == '__main__': 
    #     num=len(item)
    #     Processed = 0

    # 同時建立及啟用執行緒
    with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
        executor.map(item2job, item)

    
if __name__ == '__main__':
    scrub()