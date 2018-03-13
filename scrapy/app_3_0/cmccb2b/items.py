# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Cmccb2bItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    id = scrapy.Field()
    source_ch = scrapy.Field()
    notice_type = scrapy.Field()
    title = scrapy.Field()
    published_date = scrapy.Field()
    notice_url = scrapy.Field()
    notice_context = scrapy.Field()