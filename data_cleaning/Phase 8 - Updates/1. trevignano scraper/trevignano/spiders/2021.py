# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from scrapy.loader import ItemLoader
from trevignano.items import TrevignanoItem
from bs4 import BeautifulSoup



class TreviSpider(scrapy.Spider):
	name = '2021'
	allowed_domains = ['www.lareginadelrosario.org']
	start_urls = ['https://www.lareginadelrosario.org']

	def parse(self, response):


		url = "https://www.lareginadelrosario.org/2021/05/messaggi-maggio-2021/"
		
		print(url)
		yield Request(url, callback=self.parse_prophecies, meta={"month":"05"})

	def parse_prophecies(self, response):

		main = response.xpath('//*[@class="fusion-content-tb fusion-content-tb-1"]')
		
		paragraphs = main.xpath('.//p')
		for paragraph in paragraphs:
			l = ItemLoader(item=TrevignanoItem(), selector=paragraph)
			title = paragraph.xpath('.//strong/text()').extract_first()
			if title:
				date = 	title.split(" ")[-3:]
				date_str = (" ").join(date)
				text = paragraph.xpath('.//text()').extract()[-1]
				l.add_value('date', date_str)
				l.add_value('author', "Holy Mary")
				l.add_value('text', text)
				yield l.load_item()	
			else:
				pass	
			# return {"x":text}

		# except:
		# 	pass		



# main = response.xpath('//*[@class="fusion-content-tb fusion-content-tb-1"]')
# paragraphs = main.xpath('.//p')
# title = paragraph.xpath('.//strong/text()').extract_first()
# date = title.split(", ")[1]
# text = paragraph.xpath('.//text()').extract()[-1]



















