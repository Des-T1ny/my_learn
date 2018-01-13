# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class TencentPipeline(object):


    def __init__(self):
        self.f = open('info.txt','w',encoding='utf-8')

    def process_item(self, item, spider):
        item = dict(item)
        print(type(item))
        print(str(item) + '5555555555555555555555555555555')
        self.f.write(str(item['name']) + '    ')
        self.f.write(str(item['location']) + '    ')
        self.f.write(str(item['number']) + '    ')
        self.f.write(str(item['time']) + '\n')
        return item


    def close_spider(self, spider):
        self.f.close()
