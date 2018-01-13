# -*- coding: utf-8 -*-
import scrapy
from test_scrapy.items import TestScrapyItem

class TestspiderSpider(scrapy.Spider):
    name = 'testSpider'
    # allowed_domains = ['https://www.ybdu.com/']
    start_urls = ['https://www.ybdu.com/xiaoshuo/12/12814/']

    def parse(self, response):
        chapter_urls = response.xpath("/html/body/div[@id='header']/div[@class='warpper']/div[@class='mu_contain']/ul[@class='mulu_list']/li/a/@href").extract()
        for each in chapter_urls:
            # print(self.start_urls[0] + each)
            yield scrapy.Request(self.start_urls[0] + each, callback = self.essay_parse)


    def essay_parse(self, response):
        item = TestScrapyItem()
        essay = response.xpath("//div[@id='htmlContent']").xpath('string(.)').extract()[0]   #/div[@id='htmlContent']   #.xpath('string(.)')
        title = response.xpath("//div[@class='h1title']/h1/text()").extract()[0]

        print(type(essay))
        item['txt_name'] = str(title)
        item['txt_essay'] = str(essay)
        return item


