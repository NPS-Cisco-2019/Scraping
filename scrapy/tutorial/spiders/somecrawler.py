import scrapy
import string
import json
import re
import tldextract
import urllib.request
import os
class QuotesSpider(scrapy.Spider):
    name = "quotespider"
    def start_requests(self):
        with open("links.txt", "r") as f:
            links = f.read().split()
            self.log(links)
        urls = ["http://www.askiitians.com/forums/Mechanics/please-explain-the-answer-with-each-and-every-step_255519.htm", "https://brainly.in/question/11481611"]
        
        for url in links[:5]:
            

           listt = tldextract.extract(url)
			  
           website = listt.domain
           if website == 'brainly':
               yield scrapy.Request(url = url, callback = self.parsebrainly)
           elif website == 'askiitians' :
               yield scrapy.Request(url = url, callback = self.parseaskiitans)
           

    def parsebrainly(self, response):
        with open("bans.txt","a+") as f:
            self.log("b")
            l = response.xpath('//div[@class ="sg-text js-answer-content brn-rich-content"]').extract()
            #txt =l[0]
            #jobj = json.loads(txt)
            f.write(str(l))
            #f.write(str(jobj["mainEntity"]["suggestedAnswer"][0]["text"].encode(encoding='UTF-8',errors='strict')))
            #self.log(str(jobj["mainEntity"]["suggestedAnswer"][0]["text"].encode(encoding='UTF-8',errors='strict')))
    """ def downloadImage(self,urll, urllname):
        
        urllib.request.urlretrieve(self.urll, self.urllname) """

           

        
    

    def parseaskiitans(self, response):
        with open("ians.txt","a+") as f:
            self.log("ask")
            l = response.xpath('//div[@id ="rptAnswers_ctl01_pnlAnswer"]//div').extract()[3][5:-6]
            imgsrc = response.xpath('//div[@id ="rptAnswers_ctl01_pnlAnswer"]//div//img[@src]').extract()[0]
            imgsrc = imgsrc[imgsrc.find('src="')+5:imgsrc.find('.jpg"') + 4]
            #downloadImage(imgsrc, "A")
            urllib.request.urlretrieve(imgsrc, "img_Ask")
            self.log(imgsrc)
            f.write(str(l))
            f.write(str(imgsrc))
##            txt =l[0]
##            jobj = json.loads(txt)
##            f.write(str(jobj["mainEntity"]["suggestedAnswer"][0]["text"].encode(encoding='UTF-8',errors='strict')))
##            
            
