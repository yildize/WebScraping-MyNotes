# -*- coding: utf-8 -*-
import scrapy

class GdpDebtSpider(scrapy.Spider):
    name = 'gdp_debth'
    allowed_domains = ['worldpopulationreview.com']
    start_urls = ['http://worldpopulationreview.com/countries/countries-by-national-debt/']
	
    def parse(self, response):
		#satırları selector object list olarak alalım:
        rows = response.xpath("//table/tbody/tr")

		#her satı için name, depth ve population verisini ayrı ayrı çekip yield edelim:	
        for row in rows:
            yield {
                'country_name': row.xpath(".//td[1]/a/text()").get(),
                'gdp_debt': row.xpath(".//td[2]/text()").get()
            }




