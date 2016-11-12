
T-1

auth=twitter.OAuth(
consumer_key=CONSUMER_KEY, 
consumer_secret=CONSUMER_SECRET, 
token=ACCESS_TOKEN_KEY, 
token_secret=ACCESS_TOKEN_SECRET
)

api = twitter.Twitter(auth=auth)

response = api.statuses.show( _id =  ) 
print(response)

response = api.statuses.update( status="Hello World")


T-2

timeline = api.statuses.home_timeline()

print type(timeline)
print len(timeline)

print type(timeline[0])
for key in timeline[0].keys():
    print key,timeline[0][key]

from pymongo import MongoClient
_mclient = MongoClient()
_db=_mclient.ds_twitter
_table=_db.home_timeline

url = "https://api.twitter.com/1.1/statuses/home_timeline.json"
response, content = client.request(url)

home_timeline = json.loads(content)
for tweet in home_timeline:
    _table.insert_one(tweet)

url = "https://api.twitter.com/1.1/statuses/home_timeline.json?count=2"
response, content = client.request(url)

home_timeline = json.loads(content)
for tweet in home_timeline:
    print tweet['id'],tweet['text']

print home_timeline[0]['created_at']
print home_timeline[0]['id']