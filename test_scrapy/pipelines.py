# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html



class TestScrapyPipeline(object):

    def __init__(self):
        self.f = open('xiaoshuo.txt', 'w', encoding= 'utf-8')


    def process_item(self, item, spider):

        item = dict(item)
        self.f.write(item['txt_name'] + '\n\n')
        self.f.write(item['txt_essay'] + '\n')
        return item

    def close_spider(self, spider):
        self.f.close()




