import scrapy
import string
import json
import re
import tldextract
class QuotesSpider(scrapy.Spider):
    name = "quotespider"
    def start_requests(self):
        urls = ["http://www.askiitians.com/forums/Mechanics/please-explain-the-answer-with-each-and-every-step_255519.htm"]
        
        for url in urls:
            
           

           listt = tldextract.extract(url)
			  
           website = listt.domain
           if website == 'brainly':
               yield scrapy.Request(url = url, callback = self.parsebrainly)
           elif website == 'askiitians' :
               yield scrapy.Request(url = url, callback = self.parseaskiitans)
           

    def parsebrainly(self, response):
        with open("ans.txt","a+") as f:
            l = response.xpath('//script[@type ="application/ld+json"]/text()').getall()
            txt =l[0]
            jobj = json.loads(txt)
            
            f.write(str(jobj["mainEntity"]["suggestedAnswer"][0]["text"].encode(encoding='UTF-8',errors='strict')))
            #self.log(str(jobj["mainEntity"]["suggestedAnswer"][0]["text"].encode(encoding='UTF-8',errors='strict')))
            
    def parseaskiitans(self, response):
        with open("ans.txt","a+") as f:
            l = response.xpath('//div[@id ="rptAnswers_ctl01_pnlAnswer"]').getall()
            f.write(str(l))
##            txt =l[0]
##            jobj = json.loads(txt)
##            f.write(str(jobj["mainEntity"]["suggestedAnswer"][0]["text"].encode(encoding='UTF-8',errors='strict')))
##            
            
