import sys
sys.path.append('/workspaces/DrugProject/DrugProject/DrugRecommendation')

from scrapy import Spider
import DrugRecommendation


# class DrugSpider(Spider):
#     name = "drug_spider"
#     allowed_urls = ['http://www.webmd.com/']
#     start_urls = ['http://www.webmd.com/drugs/index-drugs.aspx?show=conditions']

#     def parse(self, response):
#         pass
