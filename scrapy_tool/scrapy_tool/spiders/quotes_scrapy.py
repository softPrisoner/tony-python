import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        #from here you can know the quotes
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            #here return the result immeditely.
            yield scrapy.Request(url=url, callback=self.parse)

#def parse info
    def parse(self, response):
        #from there we can see how to resolve the the page data
        
        '''first of all. find the last before index'''
        # page = response.url.split("/")[-2]
        # #this filename is quotes 
        # filename = 'quotes-%s.html' % page
        
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # self.log('Saved file %s' % filename)

        for quote in response.css("div.quote"):
            yield{
                'text': quote.css('span.text::text').get(),
                "author":quote.css("small.author::text").get(),
                "tags":quote.css("div.tags a.tag::text").getall(),
            }
