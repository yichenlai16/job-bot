# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exporters import JsonItemExporter
from scrapy.exceptions import DropItem
from scrapy import logformatter
import logging
import os
from jobspider.util.db import db_connect, create_forum_table, Items
from datetime import date
from sqlalchemy import select, MetaData
from sqlalchemy.orm import sessionmaker
from jobspider.util.notify import alert
from jobspider.util.scrubscope import scrub
from sqlalchemy import and_


class JobspiderPipeline:
    def process_item(self, item, spider):
        return item


class DuplicatesTitlePipeline(object):
    def __init__(self):
        self.article = set()

    def process_item(self, item, spider):
        title = item["jobNo"]
        if title in self.article:
            raise DropItem()
        self.article.add(title)
        return item


class JsonPipeline:
    def __init__(self):
        self.file = open("history.json", "wb")
        self.exporter = JsonItemExporter(self.file, encoding="utf-8")
        self.exporter.start_exporting()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()


class CrawlPipeline:
    def __init__(self):
        """
        Initializes database connection and sessionmaker.
        Creates items table.
        """
        engine = db_connect()
        create_forum_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        """
        Process the item and store to database.
        """
        session = self.Session()

        # Query the database to check if the item already exists
        conditions = [getattr(Items, key) == value for key, value in item.items()]
        condition = and_(*conditions)
        instance = session.query(Items).filter(condition).one_or_none()

        # If the item exists, return the existing instance

        if instance:
            session.close()
            return instance

        JobspiderItem = Items(**item)

        try:
            session.add(JobspiderItem)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

        return item

    def close_spider(self, spider):
        scrub()
        alert()


class PoliteLogFormatter(logformatter.LogFormatter):
    def dropped(self, item, exception, response, spider):
        return {
            "level": logging.DEBUG,  # lowering the level from logging.WARNING
            "msg": "Dropped: %(exception)s" + os.linesep + "%(item)s",
            "args": {
                "exception": exception,
                "item": item,
            },
        }
