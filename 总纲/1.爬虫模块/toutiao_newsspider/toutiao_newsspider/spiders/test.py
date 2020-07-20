# -*- coding: utf-8 -*-
import scrapy
import json
import time
import  datetime
from toutiao_newsspider.items import  NewsItem

class ToutiaoSpider(scrapy.Spider):
    name = 'test'

    def start_requests(self):
        urlstring="https://www.toutiao.com/api/pc/feed/?category=news_tech&utm_source=toutiao&widen=10&max_behot_time=1521150760&max_behot_time_tmp=1551167560"
        yield scrapy.Request(url=urlstring, callback=self.parse)

    def parse(self, response):
        main_data = json.loads(response.body.decode("utf-8"))["data"]
        newsitem=NewsItem()
        for index in range(len(main_data)):
            item=main_data[index]
            newsitem["title"]=item["title"]
            timeArray = time.localtime(item["behot_time"])
            newsitem["behot_time"]=time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
            newsitem["item_id"] = item["item_id"]
            newsitem["article_genre"] = item["article_genre"]
            if "chinese_tag" in item:
                newsitem["chinese_tag"] =item["chinese_tag"]
            newsitem["tag"] = item["tag"]
            newsitem["group_id"] = item["group_id"]
            newsitem["group_source"] = item["group_source"]
            newsitem["label"] = item["label"]
            newsitem["source"] = item["source"]
            if "image_url" in item:
                newsitem["image_url"] = item["image_url"]
            if "comments_count" in item:
                newsitem["comments_count"] = item["comments_count"]
            newsitem["is_feed_ad"] = item["is_feed_ad"]
            newsitem["abstract"] = item["abstract"]
            newsitem["source_url"] = "https://www.toutiao.com"+item["source_url"]
            yield  newsitem



        pass
