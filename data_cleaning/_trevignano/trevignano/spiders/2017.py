# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from scrapy.loader import ItemLoader
from trevignano.items import TrevignanoItem
from bs4 import BeautifulSoup


class TreviSpider(scrapy.Spider):
	name = '2017'
	allowed_domains = ['www.lareginadelrosario.com']
	start_urls = ['http://www.lareginadelrosario.com/']

	def parse(self, response):
		for month in ["01","02","03","04","05","06","07","08","09","10","11","12"]:
			url = f"https://www.lareginadelrosario.com/2017/{month}/"
			yield Request(url, callback=self.parse_prophecies, meta={"month":month})

	def parse_prophecies(self, response):
		try:		
			m = response.meta.get('month')	
			main = response.xpath('//div[contains(@class,"main section")]').extract_first()
			l = ItemLoader(item=TrevignanoItem(), selector=main)
			soup = BeautifulSoup(main, features="lxml")
			prophecy = soup.get_text()
			l.add_value('date', f"2017_{m}")	
			l.add_value('author', "Holy Mary")	
			l.add_value('text', prophecy)	
			yield l.load_item()	

		except:
			pass		

