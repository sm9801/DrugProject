from scrapy import Spider, Request
from scrapy.selector import Selector
from DrugRecommendation.items import DrugrecommendationItem
import urllib
import re


class DrugSpider(Spider):
    name = "drug_spider"
    allowed_urls = ['http://www.webmd.com/']
    start_urls = ['http://www.webmd.com/drugs/index-drugs.aspx?show=conditions']
