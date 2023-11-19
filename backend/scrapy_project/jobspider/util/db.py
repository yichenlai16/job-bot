from sqlalchemy.schema import Table
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select, MetaData
from sqlalchemy import (
    create_engine,
    Float,
    Table,
    Column,
    Integer,
    String,
    INT,
    String,
    FLOAT,
    VARCHAR,
)
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.engine.base import Engine
from sqlalchemy.engine.url import URL
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv
import os

load_dotenv()
DATABASE = {
    "drivername": "postgresql",
    "database": os.getenv("POSTGRES_DB"),
    "username": os.getenv("POSTGRES_USER"),
    "password": os.getenv("POSTGRES_PASSWORD"),
    "host": os.getenv("POSTGRES_HOST"),
    "port": os.getenv("POSTGRES_PORT"),
}

DeclarativeBase = declarative_base()
metadata = DeclarativeBase.metadata


def db_connect() -> Engine:
    return create_engine(URL(**DATABASE))


def create_forum_table(engine):
    DeclarativeBase.metadata.create_all(engine)


engine = db_connect()


class Items(DeclarativeBase):
    __tablename__ = "items"

    jobNo = Column("jobNo", INT, nullable=True, primary_key=True)
    jobApplyCount = Column("jobApplyCount", INT, nullable=True)
    source_job_website = Column("source_job_website", String, nullable=True)
    source_job_cat = Column("source_job_cat", String, nullable=True)
    source_job_sn = Column("source_job_sn", String, nullable=True)
    source_company_website = Column("source_company_website", String, nullable=True)
    source_company_cat = Column("source_company_cat", String, nullable=True)
    source_company_sn = Column("source_company_sn", String, nullable=True)
    jobName = Column("jobName", String, nullable=True)
    jobUpDate = Column("jobUpDate", String, nullable=True)
    jobDesc = Column("jobDesc", String, nullable=True)
    jobCategory = Column("jobCategory", ARRAY(String, dimensions=None), nullable=True)
    salaryLow = Column("salaryLow", INT, nullable=True)
    salaryHigh = Column("salaryHigh", INT, nullable=True)
    salaryType = Column("salaryType", INT, nullable=True)
    jobRole = Column("jobRole", INT, nullable=True)
    workType = Column("workType", ARRAY(String, dimensions=None), nullable=True)
    jobArea = Column("jobArea", String, nullable=True)
    jobAddress = Column("jobAddress", String, nullable=True)
    jobIndustryArea = Column("jobIndustryArea", String, nullable=True)
    jobLon = Column("jobLon", FLOAT, nullable=True)
    jobLat = Column("jobLat", FLOAT, nullable=True)
    manageRespon = Column("manageRespon", String, nullable=True)
    businessTrip = Column("businessTrip", String, nullable=True)
    workPeriod = Column("workPeriod", String, nullable=True)
    vacationPolicy = Column("vacationPolicy", String, nullable=True)
    startWorkDay = Column("startWorkDay", String, nullable=True)
    hireType = Column("hireType", INT, nullable=True)
    needEmployee = Column("needEmployee", String, nullable=True)
    landmark = Column("landmark", String, nullable=True)
    remoteWork = Column("remoteWork", String, nullable=True)
    delegatedRecruit = Column("delegatedRecruit", String, nullable=True)
    roleDesc = Column("roleDesc", ARRAY(String, dimensions=None), nullable=True)
    workExp = Column("workExp", String, nullable=True)
    edu = Column("edu", String, nullable=True)
    major = Column("major", ARRAY(String, dimensions=None), nullable=True)
    language = Column("language", ARRAY(String, dimensions=None), nullable=True)
    localLanguage = Column(
        "localLanguage", ARRAY(String, dimensions=None), nullable=True
    )
    specialty = Column("specialty", ARRAY(String, dimensions=None), nullable=True)
    skill = Column("skill", ARRAY(String, dimensions=None), nullable=True)
    certificate = Column("certificate", ARRAY(String, dimensions=None), nullable=True)
    driverLicense = Column(
        "driverLicense", ARRAY(String, dimensions=None), nullable=True
    )
    other = Column("other", String, nullable=True)
    fromComp_companyName = Column("fromComp_companyName", String, nullable=True)
    companyLink = Column("companyLink", String, nullable=True)
    postalCode = Column("postalCode", INT, nullable=True)
    company_addrNoDesc = Column("company_addrNoDesc", String, nullable=True)
    company_address = Column("company_address", String, nullable=True)
    capital = Column("capital", String, nullable=True)
    empNo = Column("empNo", String, nullable=True)
    hrName = Column("hrName", String, nullable=True)
    indcat = Column("indcat", String, nullable=True)
    industryDesc = Column("industryDesc", String, nullable=True)
    company_lat = Column("company_lat", FLOAT, nullable=True)
    company_lon = Column("company_lon", FLOAT, nullable=True)
    phone = Column("phone", String, nullable=True)
    fax = Column("fax", String, nullable=True)
    profile = Column("profile", String, nullable=True)
    news = Column("news", String, nullable=True)
    newsLink = Column("newsLink", String, nullable=True)
    product = Column("product", String, nullable=True)
    welfare = Column("welfare", String, nullable=True)
    legalTagNames = Column(
        "legalTagNames", ARRAY(String, dimensions=None), nullable=True
    )
    tagNames = Column("tagNames", ARRAY(String, dimensions=None), nullable=True)


class Job(DeclarativeBase):
    __table__ = Table("Job", metadata, autoload=True, autoload_with=engine)


class Company(DeclarativeBase):
    __table__ = Table("Company", metadata, autoload=True, autoload_with=engine)


class CompanySource(DeclarativeBase):
    __table__ = Table("CompanySource", metadata, autoload=True, autoload_with=engine)


class Alert(DeclarativeBase):
    __table__ = Table("Alert", metadata, autoload=True, autoload_with=engine)


class Users(DeclarativeBase):
    __table__ = Table("Users", metadata, autoload=True, autoload_with=engine)
