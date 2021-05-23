import scrapy
from ..items import CelticsItem

class CelticsSpider(scrapy.Spider):
    name = "celtics"

    def start_requests(self):
        urls = [
            'https://www.nba.com/celtics/video'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for video in response.css("div.video-thumbnail-info"):
            item = CelticsItem()
            item['title'] = video.css("a.headline::text").get(),
            item['description'] = video.css("div.video-thumbnail-description::text").get()
            item['date'] = video.css("span.video-thumbnail-timestamp::text").get()
            item['duration'] = video.css("span.video-thumbnail-duration::text").get()
            item['link'] = 'https://www.nba.com/celtics/video/' + video.css('a').xpath('@data-videoid').get() 
            yield item
            
