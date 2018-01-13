# -*- coding: utf-8 -*-
import scrapy
from tencent.items import TencentItem


class TencenspiderSpider(scrapy.Spider):
    name = 'tencenspider'
    # allowed_domains = ['http://hr.tencent.com']
    start_urls = ['http://hr.tencent.com/position.php']

    def parse(self, response):
        item = TencentItem()
        node_list = response.xpath("//tr[@class='odd' or @class='even']")
        for each in node_list:
            item['name'] = each.xpath("./td[@class='l square']/a/text()").extract()[0]
            item['number'] = each.xpath("./td[3]/text()").extract()[0]
            item['location'] = each.xpath("./td[4]/text()").extract()[0]
            item['time'] = each.xpath("./td[5]/text()").extract()[0]
            # print('\n'+ str(item) + '\n')
            yield (item)
        url = response.xpath("//a[@id='next']/@href").extract()[0]
        print('http://hr.tencent.com/' + str(url))
        yield scrapy.Request('http://hr.tencent.com/' + str(url), callback = self.parse)







