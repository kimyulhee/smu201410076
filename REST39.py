REST3

KEY=str(key['dataseoul'])
TYPE='xml'
SERVICE='SearchSTNBySubwayLineService'
START_INDEX=str(1)
END_INDEX=str(10)
LINE_NUM=str(2)

params=os.path.join(KEY,TYPE,SERVICE,START_INDEX,END_INDEX,LINE_NUM)
print params[31:]

import urlparse
_url='http://openAPI.seoul.go.kr:8088/'
url=urlparse.urljoin(_url,params)
#print url

import requests
data=requests.get(url).text
print data

type(data)

import re
p=re.compile('<STATION_NM>(.+?)</STATION_NM>')
res=p.findall(data)
for item in res:
    print item

import xml.etree.ElementTree as ET
tree=ET.fromstring(data.encode('utf-8'))

stds=tree.findall('row')
for elements in stds:
    for elm in elements:
        print elm.text

import lxml
import lxml.etree
import StringIO

#tree=lxml.etree.parse(StringIO.StringIO(data.encode('utf-8')))
tree=lxml.etree.fromstring(data.encode('utf-8'))

nodes=tree.xpath('//STATION_NM')
for node in nodes:
    print node.text



REST4

KEY=str(key['dataseoul'])
TYPE='xml'
SERVICE='ListLocaldata470401S'
START_INDEX=str(1)
END_INDEX=str(5)

params=os.path.join(KEY,TYPE,SERVICE,START_INDEX,END_INDEX)

print params[31:]

import urlparse
_url='http://openapi.seoul.go.kr:8088/'
url=urlparse.urljoin(_url,params)
#print url

import requests

data=requests.get(url).text
print data

print type(data.encode('utf-8'))

import lxml
import lxml.etree
import StringIO

#tree=lxml.etree.parse(StringIO.StringIO(data.encode('utf-8')))
tree=lxml.etree.fromstring(data.encode('utf-8'))

nodes=tree.xpath('//STATMAN')
for node in nodes:
    print node.text

REST5

import os
import requests
_url='http://openAPI.seoul.go.kr:8088'
_key=str(key['dataseoul'])
_type='xml'
_service='CardSubwayStatisticsService'
_start_index=1
_end_index=5
_use_mon='201306'
_api=os.path.join(_url,_key,_type,_service,str(_start_index),str(_end_index),_use_mon)

response = requests.get(_api).text
print response

REST6

import os
import requests
_url='http://openAPI.seoul.go.kr:8088'
_key=str(key['dataseoul'])
_type='xml'
_service='CardSubwayStatisticsService'
_start_index=1
_end_index=5
_use_mon='201306'

_maxIter=2
_iter=0
while _iter<_maxIter:
    _api=os.path.join(_url,_key,_type,_service,str(_start_index),str(_end_index),_use_mon)
    #print _api
    response = requests.get(_api).text
    print response
    _start_index+=5
    _end_index+=5
    _iter+=1

_type='json'

_api=os.path.join(_url,_key,_type,_service,str(_start_index),str(_end_index),_use_mon)

data=requests.get(_api).text
print data

import json
jd = json.loads(data)
#print jd['STATION_NM']
#for key,value in jd.items():
#    print "---",key,value

print jd['SearchSTNBySubwayLineService']['row'][0]
#n=len(jd['SearchSTNBySubwayLineService']['row'])
#for i in range(0,n):
#    print jd['SearchSTNBySubwayLineService']['row'][i]
for item in jd['SearchSTNBySubwayLineService']['row']:
    print item.keys()
    for i in item.keys():
        if i=='STATION_NM':
            print ''.join(item.values())
            print item.values()[1]

REST7

!ls -l /var/lib/mongodb/ds_*

%%writefile src/ds_rest_subway_mongo.js
use ds_rest_subwayPassengers_mongo_db
db.db_rest_subway.find({"CardSubwayStatisticsService.row.SUB_STA_NM":"강남구청"})

!mongo < src/ds_rest_subway_mongo.js

REST8

import requests
import re
busstopurl='http://openAPI.seoul.go.kr:8088/sample/xml/CardBusStatisticsService/1/5/201510/7016'
data=requests.get(busstopurl).text
print data
p=re.compile('<BUS_STA_NM>(.+?)</BUS_STA_NM>')
res=p.findall(data)
for item in res:
    print item

buspassengers='http://openAPI.seoul.go.kr:8088/sample/xml/CardBusStatisticsService/1/5/201510/7016/'
data=requests.get(busstopurl).text
print data
p=re.compile('<RIDE_PASGR_NUM>(.+?)</RIDE_PASGR_NUM>')
res=p.findall(data)
for item in res:
    print item

KEY=str(key['dataseoul'])
TYPE='xml'
SERVICE='CardBusStatisticsService'
START_INDEX=str(1)
END_INDEX=str(5)
USE_MON=str(201512)
BUS_ROUTE_NO=str(7016)

params=os.path.join(KEY,TYPE,SERVICE,START_INDEX,END_INDEX,USE_MON,BUS_ROUTE_NO)
print params[31:]

import urlparse
_url='http://openapi.seoul.go.kr:8088/'
url=urlparse.urljoin(_url,params)
#print url

import requests

data=requests.get(url).text
print data

REST9

import requests
import re
weatherurl='http://openAPI.seoul.go.kr:8088/sample/xml/RealtimeWeatherStation/1/5/'
data=requests.get(weatherurl).text
print data
p=re.compile('<SAWS_TA_AVG>(.+?)</SAWS_TA_AVG>')
res=p.findall(data)
for item in res:
    print item

KEY=str(key['dataseoul'])
TYPE='json'
SERVICE='RealtimeWeatherStation'
START_INDEX=str(1)
END_INDEX=str(5)
STN_NM=u'중구'

params=os.path.join(KEY,TYPE,SERVICE,START_INDEX,END_INDEX,STN_NM)
print params[31:]

import urlparse
_url='http://openapi.seoul.go.kr:8088/'
url=urlparse.urljoin(_url,params)
#print url

import requests

data=requests.get(url).text
print data

