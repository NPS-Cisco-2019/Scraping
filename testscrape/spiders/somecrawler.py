import scrapy
import string
import json
import re
import tldextract
class QuotesSpider(scrapy.Spider):
    name = "now"
    def start_requests(self):
        urls = ["https://brainly.com/question/11150414"]
        
        for url in urls:
            
           

           listt = tldextract.extract(url)
			  
           website = listt.domain
           self.log(website)
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
            l = response.xpath('//div[@id ="rptAnswers_ctl01_pnlAnswer"]/text()').getall()
            f.write(str(l))
##            txt =l[0]
##            jobj = json.loads(txt)
##            f.write(str(jobj["mainEntity"]["suggestedAnswer"][0]["text"].encode(encoding='UTF-8',errors='strict')))
##            
            
