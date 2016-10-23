web5

import lxml.html
from lxml.cssselect import CSSSelector
import requests
r = requests.get('https://www.ieee.org/conferences_events/index.html')

html = lxml.html.fromstring(r.text)

print lxml.html.tostring(html)

sel=CSSSelector('#inner-container > div.content-gray > div.content-lc \
        > div.content-lc-bottom > div.content-c > div:nth-child(1) > div \
        > div:nth-child(2)')
# Apply the selector to the DOM tree.
nodes = sel(html)
for node in nodes:
    print lxml.html.tostring(node)

#sel = CSSSelector('#inner-container > div.content-gray > div.content-lc > div.content-lc-bottom > div.content-c')
sel=CSSSelector('#inner-container > div.content-gray > div.content-lc \
        > div.content-lc-bottom > div.content-c > div:nth-child(1) > div \
        > div a')
# Apply the selector to the DOM tree.
nodes = sel(html)
print nodes

for node in nodes:
    # print lxml.html.tostring(item)
    print node.text

#sel = CSSSelector('#inner-container > div.content-gray > div.content-lc > div.content-lc-bottom > div.content-c')
sel=CSSSelector('#inner-container > div.content-gray > div.content-lc \
        > div.content-lc-bottom > div.content-c > div:nth-child(1) > div \
        > div p > br')
# Apply the selector to the DOM tree.
nodes = sel(html)
print nodes

for node in nodes:
    print lxml.html.tostring(node)
    #print node.text

sel=CSSSelector('div.box-c-indent p > a')
nodes = sel(html)
print len(nodes)
print nodes

for node in nodes:
    #print lxml.html.tostring(item)
    if node is not None:
        print node.text_content()

web6

import urllib2
import requests
urlperson='http://www.kbreport.com/player/list?key=이대호'
urlbase="http://www.kbreport.com/leader/main?"
url1="rows=20&order=oWAR&orderType=DESC&"
url2="teamId=1&defense_no=2&year_from=2015&year_to=2015&split01=&split02_1=&split02_2=&r_tpa_count=&tpa_count=0"
urlbaseball=urlbase+url1+url2
print urlbaseball
data=requests.get(urlbaseball).text
#data=requests.get(urlperson).text
print data[6000:7000]

print data.find('top-score-top')
print data.find('top-score end')

#import re
#p=re.compile('NC\w+')
#res=re.search('<title>', data)
#res=re.search(u'타자.+', data)
#res=re.search(u'야구.통계.+', data)
#print res.group()

#data.encode('utf-8')
#print data
#from BeautifulSoup import BeautifulSoup
#BeautifulSoup(data)

mydata=data[6340:8353+len('top-score end')]
import re
p=re.compile(u'.승.+')
#p=re.compile(u'.두산.')
#res=p.search(data)
found=p.findall(mydata)
print found
for item in found:
    print item
#print res.group()
#findall?
#print res.groups

import requests
urlkorbase='http://www.koreabaseball.com/Record/Player/HitterBasic/Basic1.aspx'
data=requests.get(urlkorbase).text
#print data

# 국가통게
kosis='http://kosis.kr/statisticsList/statisticsList_01List.jsp?vwcd=MT_ZTITLE&parentId=A#SubCont'
data=requests.get(urlkorbase).text
print len(data)

web7

url = 'http://www.bbc.co.uk/sport/football/premier-league/results'

import requests
r=requests.get(url)
_html=r.text

len(_html)

_html.find('table-stats')

def getIndicesOfAllTableStats(string, query):
    listindex=list()
    offset=0
    i = string.find(query, offset)
    while i >= 0:
        listindex.append(i)
        i = string.find(query, i + 1)
    return listindex

param1=_html
param2='table-stats'
_indices=getIndicesOfAllTableStats(param1, param2)
print _indices

from scrapy.selector import Selector
nodes=Selector(text=_html).xpath("//table[@class='table-stats']/tbody/tr[@class='report']/td[@class='match-details']/p")

print nodes[0].extract()

for node in nodes:
    home_team = node.xpath("span[@class='team-home teams']/a/text()").extract()
    score = node.xpath("span[@class='score']/abbr/text()").extract()
    away_team = node.xpath("span[@class='team-away teams']/a/text()").extract()
    if home_team and score and away_team:
        home_team = home_team[0].strip()
        score = score[0].strip()
        home_goals = int(score.split('-')[0])
        away_goals = int(score.split('-')[1])
        away_team = away_team[0].strip()
    print home_team, score, home_goals, away_goals, away_team

web8

%%writefile src/ds_web_data_paging.py
import scrapy

class QuoteItem(scrapy.Item):
    text = scrapy.Field()
    author = scrapy.Field()

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
    ]
    def parse(self, response):
        for quote in response.xpath('//div[@class="quote"]'):
            item = QuoteItem()
            item['text'] = quote.xpath('span[@class="text"]/text()').extract_first()
            item['author'] = quote.xpath('span/small/text()').extract_first()
            print "crawling ",item['author']
            yield item
        next_page = response.xpath('//li[@class="next"]/a/@href').extract_first()
        if next_page:
            next_page = response.urljoin(next_page)
            print "--> visiting ",next_page
            yield scrapy.Request(next_page, callback=self.parse)

!scrapy runspider src/ds_web_data_paging.py -o src/ds_web_data_paging.json -t json --logfile src/ds_web_data_paging.logfile

web9

%%writefile src/ds_web_data_textpost.py
import scrapy

class TextPostItem(scrapy.item.Item):
    title = scrapy.item.Field()
    url = scrapy.item.Field()
    submitted = scrapy.item.Field()

class RedditCrawler(scrapy.spiders.CrawlSpider):
    name = 'reddit_crawler'
    allowed_domains = ['reddit.com']
    start_urls = ['https://www.reddit.com/r/learnpython/new']
    custom_settings = {
        'BOT_NAME': 'reddit-scraper',
        'DEPTH_LIMIT': 3,
        'DOWNLOAD_DELAY': 3
    }
    def parse(self, response):
        s = scrapy.selector.Selector(response)
        next_link = s.xpath('//span[@class="nextprev"]//a/@href').extract()[0]
        if len(next_link):
            print "--> visiting ",next_link
            yield self.make_requests_from_url(next_link)
        posts = scrapy.selector.Selector(response).xpath('//div[@id="siteTable"]/div[@onclick="click_thing(this)"]')
        for post in posts:
            i = TextPostItem()
            i['title'] = post.xpath('div[2]/p[1]/a/text()').extract()[0]
            i['url'] = post.xpath('div[2]/ul/li[1]/a/@href').extract()[0]
            i['submitted'] = post.xpath('div[2]/p[2]/time/@title').extract()[0]
            print "crawling ",i['title']
            yield i

!scrapy runspider src/ds_web_data_textpost.py -o src/ds_web_data_textpost.json -t json --logfile src/ds_web_data_textpost.logfile

