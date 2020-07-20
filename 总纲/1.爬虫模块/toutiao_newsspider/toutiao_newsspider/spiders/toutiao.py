# -*- coding: utf-8 -*-
import scrapy
import json
import time
import datetime
from toutiao_newsspider.items import NewsItem

class ToutiaoSpider(scrapy.Spider):
    name = 'toutiao'

    def start_requests(self):
        for i in range(10000):
            ustring='https://www.toutiao.com/api/pc/feed/?category=news_entertainment&utm_source=toutiao&widen=10&max_behot_time='
            max_behot_time=int(time.time())-i*600
            ustring=ustring+str(max_behot_time)
            ustring=ustring+'&max_behot_time_tmp='
            max_behot_time_tmp=int(time.time())+80000
            ustring=ustring+str(max_behot_time_tmp)
            yield scrapy.Request(url=ustring, callback=self.parse)

    def parse(self, response):
        main_data = json.loads(response.body.decode("utf-8"))["data"]
        newsitem=NewsItem()
        for index in range(len(main_data)):
            item=main_data[index]
            if "title" in item:
                newsitem["title"] = item["title"]
            if "behot_time" in item:
                timeArray = time.localtime(item["behot_time"])
                newsitem["behot_time"] = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
            if "item_id" in item:
                newsitem["item_id"] = item["item_id"]
            if "article_genre" in item:
                newsitem["article_genre"] = item["article_genre"]
            if "chinese_tag" in item:
                newsitem["chinese_tag"] =item["chinese_tag"]
            if "tag" in item:
                newsitem["tag"] = item["tag"]
            if "group_id" in item:
                newsitem["group_id"] = item["group_id"]
            if "group_source" in item:
                newsitem["group_source"] = item["group_source"]
            if "label" in item:
                newsitem["label"] = item["label"]
            if "source" in item:
                newsitem["source"] = item["source"]
            if "image_url" in item:
                newsitem["image_url"] = item["image_url"]
            if "comments_count" in item:
                newsitem["comments_count"] = item["comments_count"]
            if "is_feed_ad" in item:
                newsitem["is_feed_ad"] = item["is_feed_ad"]
            if "abstract" in item:
                newsitem["abstract"] = item["abstract"]
            if "source_url" in item:
                newsitem["source_url"] = "https://www.toutiao.com"+item["source_url"]
            yield  newsitem



        pass
