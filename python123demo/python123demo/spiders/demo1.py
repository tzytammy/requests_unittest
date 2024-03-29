# -*- coding: utf-8 -*-
import scrapy


class DemoSpider(scrapy.Spider):
    name = 'demo'
    #allowed_domains = ['python123demo.io']
    def start_requests(self):
        urls=[
            'http://python123.io/ws/demo.html'
        ]
        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse)

    def parse(self, response):
        #以/为分割符保留最后一段。
        fname=response.url.split('/')[-1]
        with open (fname,'wb') as f:
            f.write(response.body)
        self.log('save file %s .' % fname)
        pass
