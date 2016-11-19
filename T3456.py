T-3

import urllib
url1 = "https://api.twitter.com/1.1/search/tweets.json"
myparam={'q':'seoul','count':20}
mybody=urllib.urlencode(myparam)

resp, tsearch = client.request(url1+"?"+mybody, method="GET")
tsearch_json = json.loads(tsearch)

print type(tsearch_json)
print tsearch_json.keys()
print len(tsearch_json['statuses'])

len(tsearch_json['statuses'][0])

for i,tweet in enumerate(tsearch_json['statuses']):
    #print tweet[u'user'][u'name']
    print "[%d]\t%d\t%s:%s" % (i,tweet['id'],tweet['user']['name'],tweet['text'])

T-4

import urllib
url = "https://api.twitter.com/1.1/search/tweets.json"
myparam={'q':'seoul','count':200,'max_id':'754295227351871489'}
mybody=urllib.urlencode(myparam)
response, content = client.request(url+"?"+mybody, method="GET")
tsearch_json = json.loads(content)

content

print len(tsearch_json)
print len(tsearch_json['statuses'])

f=open('_todel.txt','w')
for i,tweet in enumerate(tsearch_json['statuses']):
    #print str(i),tweet['id'],tweet['user']['name'],tweet['text']
    #f.write(json.dumps([str(i),tweet['id'],tweet['user']['name'],tweet['text']]))
    f.write(json.dumps([str(i),tweet['id'],tweet['user']['name']]))
    f.write("\n")
    #print _t
    #f.write(_t)
f.close()

import urllib
url = "https://api.twitter.com/1.1/search/tweets.json"

prev_id=None
f=open('_todel3.txt','a')
for i in range(0,20):
    myparam={'q':'seoul','count':10,'max_id':prev_id}
    mybody=urllib.urlencode(myparam)
    response, content = client.request(url+"?"+mybody, method="GET")
    tsearch_json = json.loads(content)
    print len(tsearch_json['statuses'])
    for i,tweet in enumerate(tsearch_json['statuses']):
        #print str(i),tweet['id'],tweet['user']['name'],tweet['text']
        f.write(json.dumps([str(i),tweet['id'],tweet['user']['name']]))
        f.write("\n")
    #if data["statuses"] == []:
    #    print "end of data"
    #    break
    #else:
    prev_id=int(tsearch_json['statuses'][-1]['id'])-1
    print prev_id
f.close()

T-5

import urllib
url = "https://api.twitter.com/1.1/followers/list.json"

response, content = client.request(url, method="GET")
tfollower_json = json.loads(content)

print len(tfollower_json)
print type(tfollower_json)

for k,v in tfollower_json.iteritems():
    print k

for k,v in tfollower_json['users'][0].iteritems():
        print k

for i in tfollower_json['users']:
    print i['id'],i['screen_name']

T-6

print _client.follwers()
