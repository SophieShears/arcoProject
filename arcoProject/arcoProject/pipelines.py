# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import csv
from itemadapter import ItemAdapter


class ArcoprojectPipeline:
    def __init__(self):
       self.csvwriter = csv.writer(open('Links.csv', 'wb')) 
    def process_item(self, item, spider):
       self.csvwriter.writerow((item['title'][0]), item['link'][0])
       return item
