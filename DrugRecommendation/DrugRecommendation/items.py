# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DrugrecommendationItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Drug = scrapy.Field()
    Indication = scrapy.Field()
    Type = scrapy.Field()
    Review = scrapy.Field()
    Condition = scrapy.Field()
    Use = scrapy.Field()
    HowtoUse = scrapy.Field()
    Sides = scrapy.Field()
    Precautions = scrapy.Field()
    Interactions = scrapy.Field()
    GenName = scrapy.Field()
    BrandName = scrapy.Field()
    AvoidUse = scrapy.Field()
    Allergies = scrapy.Field()
    Satisfaction = scrapy.Field()
    EaseofUse = scrapy.Field()
    Effectiveness = scrapy.Field()
    EstimatedPrice = scrapy.Field()
    Dosage = scrapy.Field()
    Form = scrapy.Field()
    PkgCount = scrapy.Field()
