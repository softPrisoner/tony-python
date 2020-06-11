import scrapy

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    #this is spider urls
    start_urls = [
        'http://quotes.toscrape.com/tag/humor/',
    ]

#crawl from the struct 

#异步多线程处理逻辑
#baidu.taobao behaviour r
    def parse(self, response):
        #start from one page with the url from top
        for quote in response.css('div.quote'):
            #quote.info
            #//yield  is the ablity to solve  the prope 
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.xpath('span/small/text()').get(),
            }

#         <div class="quote" itemscope="" itemtype="http://schema.org/CreativeWork">
#         <span class="text" itemprop="text">“The person, be it gentleman or lady, who has not pleasure in a good novel, must be intolerably stupid.”</span>
#         <span>by <small class="author" itemprop="author">Jane Austen</small>
#         <a href="/author/Jane-Austen">(about)</a>
        next_page = response.css('li.next a::attr("href")').get()
        print("next_page[]"+str(next_page))
        if next_page is not None:
            yield response.follow(next_page, self.parse)



# <div class="row">
#     <div class="col-md-8">

#     <div class="quote" itemscope="" itemtype="http://schema.org/CreativeWork">
#         <span class="text" itemprop="text">“The person, be it gentleman or lady, who has not pleasure in a good novel, must be intolerably stupid.”</span>
#         <span>by <small class="author" itemprop="author">Jane Austen</small>
#         <a href="/author/Jane-Austen">(about)</a>
#         </span>
#         <div class="tags">
#             Tags:
#             <meta class="keywords" itemprop="keywords" content="aliteracy,books,classic,humor"> 
            
#             <a class="tag" href="/tag/aliteracy/page/1/">aliteracy</a>
            
#             <a class="tag" href="/tag/books/page/1/">books</a>
            
#             <a class="tag" href="/tag/classic/page/1/">classic</a>
            
#             <a class="tag" href="/tag/humor/page/1/">humor</a>
            
#         </div>
#     </div>

#     <div class="quote" itemscope="" itemtype="http://schema.org/CreativeWork">
#         <span class="text" itemprop="text">“A day without sunshine is like, you know, night.”</span>
#         <span>by <small class="author" itemprop="author">Steve Martin</small>
#         <a href="/author/Steve-Martin">(about)</a>
#         </span>
#         <div class="tags">
#             Tags:
#             <meta class="keywords" itemprop="keywords" content="humor,obvious,simile"> 
            
#             <a class="tag" href="/tag/humor/page/1/">humor</a>
            
#             <a class="tag" href="/tag/obvious/page/1/">obvious</a>
            
#             <a class="tag" href="/tag/simile/page/1/">simile</a>
            
#         </div>
#     </div>

#     <div class="quote" itemscope="" itemtype="http://schema.org/CreativeWork">
#         <span class="text" itemprop="text">“Anyone who thinks sitting in church can make you a Christian must also think that sitting in a garage can make you a car.”</span>
#         <span>by <small class="author" itemprop="author">Garrison Keillor</small>
#         <a href="/author/Garrison-Keillor">(about)</a>
#         </span>
#         <div class="tags">
#             Tags:
#             <meta class="keywords" itemprop="keywords" content="humor,religion"> 
            
#             <a class="tag" href="/tag/humor/page/1/">humor</a>
            
#             <a class="tag" href="/tag/religion/page/1/">religion</a>
            
#         </div>
#     </div>

#     <div class="quote" itemscope="" itemtype="http://schema.org/CreativeWork">
#         <span class="text" itemprop="text">“Beauty is in the eye of the beholder and it may be necessary from time to time to give a stupid or misinformed beholder a black eye.”</span>
#         <span>by <small class="author" itemprop="author">Jim Henson</small>
#         <a href="/author/Jim-Henson">(about)</a>
#         </span>
#         <div class="tags">
#             Tags:
#             <meta class="keywords" itemprop="keywords" content="humor"> 
            
#             <a class="tag" href="/tag/humor/page/1/">humor</a>
            
#         </div>
#     </div>

#     <div class="quote" itemscope="" itemtype="http://schema.org/CreativeWork">
#         <span class="text" itemprop="text">“All you need is love. But a little chocolate now and then doesn't hurt.”</span>
#         <span>by <small class="author" itemprop="author">Charles M. Schulz</small>
#         <a href="/author/Charles-M-Schulz">(about)</a>
#         </span>
#         <div class="tags">
#             Tags:
#             <meta class="keywords" itemprop="keywords" content="chocolate,food,humor"> 
            
#             <a class="tag" href="/tag/chocolate/page/1/">chocolate</a>
            
#             <a class="tag" href="/tag/food/page/1/">food</a>
            
#             <a class="tag" href="/tag/humor/page/1/">humor</a>
            
#         </div>
#     </div>

#     <div class="quote" itemscope="" itemtype="http://schema.org/CreativeWork">
#         <span class="text" itemprop="text">“Remember, we're madly in love, so it's all right to kiss me anytime you feel like it.”</span>
#         <span>by <small class="author" itemprop="author">Suzanne Collins</small>
#         <a href="/author/Suzanne-Collins">(about)</a>
#         </span>
#         <div class="tags">
#             Tags:
#             <meta class="keywords" itemprop="keywords" content="humor"> 
            
#             <a class="tag" href="/tag/humor/page/1/">humor</a>
            
#         </div>
#     </div>

#     <div class="quote" itemscope="" itemtype="http://schema.org/CreativeWork">
#         <span class="text" itemprop="text">“Some people never go crazy. What truly horrible lives they must lead.”</span>
#         <span>by <small class="author" itemprop="author">Charles Bukowski</small>
#         <a href="/author/Charles-Bukowski">(about)</a>
#         </span>
#         <div class="tags">
#             Tags:
#             <meta class="keywords" itemprop="keywords" content="humor"> 
            
#             <a class="tag" href="/tag/humor/page/1/">humor</a>
            
#         </div>
#     </div>

#     <div class="quote" itemscope="" itemtype="http://schema.org/CreativeWork">
#         <span class="text" itemprop="text">“The trouble with having an open mind, of course, is that people will insist on coming along and trying to put things in it.”</span>
#         <span>by <small class="author" itemprop="author">Terry Pratchett</small>
#         <a href="/author/Terry-Pratchett">(about)</a>
#         </span>
#         <div class="tags">
#             Tags:
#             <meta class="keywords" itemprop="keywords" content="humor,open-mind,thinking"> 
            
#             <a class="tag" href="/tag/humor/page/1/">humor</a>
            
#             <a class="tag" href="/tag/open-mind/page/1/">open-mind</a>
            
#             <a class="tag" href="/tag/thinking/page/1/">thinking</a>
            
#         </div>
#     </div>

#     <div class="quote" itemscope="" itemtype="http://schema.org/CreativeWork">
#         <span class="text" itemprop="text">“Think left and think right and think low and think high. Oh, the thinks you can think up if only you try!”</span>
#         <span>by <small class="author" itemprop="author">Dr. Seuss</small>
#         <a href="/author/Dr-Seuss">(about)</a>
#         </span>
#         <div class="tags">
#             Tags:
#             <meta class="keywords" itemprop="keywords" content="humor,philosophy"> 
            
#             <a class="tag" href="/tag/humor/page/1/">humor</a>
            
#             <a class="tag" href="/tag/philosophy/page/1/">philosophy</a>
            
#         </div>
#     </div>

#     <div class="quote" itemscope="" itemtype="http://schema.org/CreativeWork">
#         <span class="text" itemprop="text">“The reason I talk to myself is because I’m the only one whose answers I accept.”</span>
#         <span>by <small class="author" itemprop="author">George Carlin</small>
#         <a href="/author/George-Carlin">(about)</a>
#         </span>
#         <div class="tags">
#             Tags:
#             <meta class="keywords" itemprop="keywords" content="humor,insanity,lies,lying,self-indulgence,truth"> 
            
#             <a class="tag" href="/tag/humor/page/1/">humor</a>
            
#             <a class="tag" href="/tag/insanity/page/1/">insanity</a>
            
#             <a class="tag" href="/tag/lies/page/1/">lies</a>
            
#             <a class="tag" href="/tag/lying/page/1/">lying</a>
            
#             <a class="tag" href="/tag/self-indulgence/page/1/">self-indulgence</a>
            
#             <a class="tag" href="/tag/truth/page/1/">truth</a>
            
#         </div>
#     </div>
#     </div>
            