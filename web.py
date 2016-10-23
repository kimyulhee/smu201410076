웹데이터-1: python.org 페이지를 크롤링해서 http url를 출력하기
regex

import re
#p=re.compile('http://.+"')
p=re.compile('href="(http://.*?)"')
nodes=p.findall(_html)
print "http url은 몇 개?",len(nodes)
for node in nodes:
    print node

import re
p=re.compile('<h1>(.*?)</h1>')
h1tags=p.findall(_html)
for tag in h1tags:
    print tag

import re
p=re.compile('<p>(.*?)</p>')
ptags=p.findall(_html)

print len(ptags)

print ptags[0]

#for i in ptags:
    #print i



BeautifulSoup

from bs4 import BeautifulSoup
tree=BeautifulSoup(_html, "lxml")
strongtags=tree('strong')
for tag in strongtags:
    print tag

from urllib import urlopen
from bs4 import BeautifulSoup
_html = urlopen("http://en.wikipedia.org/wiki/Kevin_Bacon")
tree = BeautifulSoup(_html, "lxml")
for link in tree.findAll("a"):
    if 'href' in link.attrs:
        print(link.attrs['href'])


xpath

print len(_html)

from lxml import etree
_htmlTree = etree.HTML(_html)
result = etree.tostring(_htmlTree, pretty_print=True, method="html")

print len(result)

nodes = _htmlTree.xpath('//*[@href]')
print len(nodes)

for node in nodes:
    print node.attrib

css selector

import lxml.html
from lxml.cssselect import CSSSelector
import requests
r = requests.get('http://python.org/')

html = lxml.html.fromstring(r.text)
sel=CSSSelector('a[href]')
# Apply the selector to the DOM tree.
nodes = sel(html)

print len(nodes)
for node in nodes:
    #print lxml.html.tostring(item)
    print node.get('href'), node.text

웹데이터-2: 웹파일 가져와서 자료구조에 넣기
import urllib2
url='http://archive.ics.uci.edu/ml/machine-learning-databases/horse-colic/horse-colic.data'
res=urllib2.urlopen(url)
html = res.read()
res.close()
print len(html)

lines=html.splitlines()
data=[]
for line in lines:
    data.append(line.split())
print len(data), len(data[0])
print data[0]


웹데이터-3: wiki에서 'python'으로 검색해서 http url출력하기

from urllib import urlopen
keyword='python'
resp = urlopen('https://www.google.com/search?q='+keyword)
html=resp.read()
len(html)

import re
p=re.compile('.*(error).*')
print p.search(html).group(1)

import webbrowser
webbrowser.open('http://www.google.com/search?q=python')

REST get query
구글에서 검색하기
import requests

resp = requests.head("http://www.google.com")
print resp.status_code, resp.text, resp.headers

import urllib2
class HeadRequest(urllib2.Request):
     def get_method(self):
         return "HEAD"

response = urllib2.urlopen(HeadRequest("http://google.com/index.html"))
print response.info()
print response.geturl()

# 파이썬에서 사용하는 기본 User Agent
from urllib import URLopener
URLopener.version

# 연습으로 자신의 User Agent 설정
from urllib import FancyURLopener
class MyOpener(FancyURLopener):
    version = 'My new User-Agent'
MyOpener.version

# 리눅스 Firefox User Agent 예
# 맥 Safari User Agent 예
class MyOpener(FancyURLopener):
    #version = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:42.0) Gecko/20100101 Firefox/42.0'
    version = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/601.2.7 (KHTML, like Gecko) Version/9.0.1 Safari/601.2.7'
MyOpener.version

myopener = MyOpener()
page = myopener.open('http://www.google.com/search?q=python')
html=page.read()

import os
f=open('mygoogle.html','w')
f.write(html)
f.close()
import webbrowser
mygoogle='file://'+'localhost'+os.path.join(os.getcwd(), 'mygoogle.html')
print mygoogle
webbrowser.open(mygoogle)

위키에서 검색하기

import urllib2
import urllib
googleurl = 'https://www.google.com/search'
keyValues = {'q' : 'python programming tutorials'}
request = urllib.urlencode(keyValues)
print request
request = request.encode('utf-8') # data should be bytes

req = urllib2.Request(googleurl+'?'+request)
print req

print req.get_full_url()

print req.get_method

resp = urllib2.urlopen(req)
resp = myopener.open(req)
html = resp.read()

import urllib
keyword='Albert_Einstein'
keyword='Python (programming language)'
s = urllib.urlopen('http://en.wikipedia.org/w/index.php?action=raw&title='+keyword).read()
#print s.find('Python is a widely used general-purpose')
print s[:5000]

위키에서 css selector

import lxml.html
from lxml.cssselect import CSSSelector
import requests

r = requests.get('https://en.wikipedia.org/wiki/Python_(programming_language)')
# build the DOM Tree
tree = lxml.html.fromstring(r.text)
# print the parsed DOM Tree
#print lxml.html.tostring(tree)

sel = CSSSelector('#mw-content-text > div:nth-child(1)')
# Apply the selector to the DOM tree.
results = sel(tree)
print results

# print the HTML for the first result.
match = results[0]
print lxml.html.tostring(match)

# print the text of the first result.
print match.text

for result in results:
    print result.text


웹데이터-4: 한국 포털사이트에서 노래 제목을 검색
검색 scraping - ?key=value&...
regex

import urllib
keyword='비오는'
f = urllib.urlopen("http://music.naver.com/search/search.nhn?query="+keyword+"&x=0&y=0")
mydata = f.read();

pos = mydata.find("트랙 리스트")
if (pos>0):
    pos = mydata.find("_title title NPI=", pos);
    pos = mydata.find("title=",pos+20)
    pos2 = mydata.find("\"", pos+8)
    print "---",mydata[pos+7:pos2]
print len(mydata)

import re
p=re.compile('title=".*비.?오는.*"')
#res=p.search(data)
res=p.findall(mydata)
for item in res:
    print item

lxml css selector - 노래제목, 아티스트, 앨범 출력

import lxml.html
from lxml.cssselect import CSSSelector

html = lxml.html.fromstring(mydata)
#tree=lxml.etree.parse('myhtml')
# construct a CSS Selector -> 
sel = CSSSelector('#content > div:nth-child(4) \
    > div._tracklist_mytrack.tracklist_table.tracklist_type1._searchTrack \
    > table > tbody > tr:nth-child(2) > td.name > a.title')
# Apply the selector to the DOM tree.
nodes = sel(html)

len(nodes)

for node in nodes:
    #print lxml.html.tostring(item)
    print node.text_content()

import lxml.html
from lxml.cssselect import CSSSelector

html = lxml.html.fromstring(mydata)
#tree=lxml.etree.parse('myhtml')
# construct a CSS Selector -> 
sel = CSSSelector('#content > div:nth-child(4) \
    > div._tracklist_mytrack.tracklist_table.tracklist_type1._searchTrack \
    > table > tbody > tr > td.name > a.title')
# Apply the selector to the DOM tree.
nodes = sel(html)

for node in nodes:
    #print lxml.html.tostring(item)
    print node.text_content()



