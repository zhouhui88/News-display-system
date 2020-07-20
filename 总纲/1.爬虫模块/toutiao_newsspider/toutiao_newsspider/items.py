# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy



class NewsItem(scrapy.Item):
    item_id = scrapy.Field()
    title=scrapy.Field()
    behot_time=scrapy.Field()
    article_genre=scrapy.Field()
    chinese_tag=scrapy.Field()
    tag = scrapy.Field()
    group_id=scrapy.Field()
    group_source=scrapy.Field()
    label = scrapy.Field()
    image_url = scrapy.Field()
    source=scrapy.Field()
    source_url=scrapy.Field()
    comments_count=scrapy.Field()
    is_feed_ad=scrapy.Field()
    abstract=scrapy.Field()
    pass
