S-1: standalone cluster 
S-2: Hello Spark

import os
import findspark

home=os.getenv("HOME")
spark_home=os.path.join(home,"Downloads/spark-1.6.0-bin-hadoop2.6")
findspark.init(spark_home)

import pyspark
conf=pyspark.SparkConf()
conf = pyspark.SparkConf().setAppName("myAppName")
sc = pyspark.SparkContext(conf=conf)

print sc
sc.version

sc._conf.get("spark.jars.packages")

sc._conf.getAll()

S-3: Hello RDD

fivethirtyeight -> data_home=os.path.join(home,"Code/git/else/data")
celsius = [39.2, 36.5, 37.3, 37.8]
def c2f(c):
    f=list()
    for i in c:
        _f=(float(9)/5)*i + 32
        f.append(_f)
    return f

print c2f(celsius)

celsius = [39.2, 36.5, 37.3, 37.8]

def c2f(c):
    return (float(9)/5)*c + 32

f=map(c2f, celsius)
print f

map(lambda c:(float(9)/5)*c + 32, celsius)

sentence = 'Hello World'
words = sentence.split()
print words

sentence = "Hello World"
map(lambda x:x.split(),sentence)

sentence = ["Hello World"]
map(lambda x:x.split(),sentence)

fib = [0,1,1,2,3,5,8,13,21,34,55]
result = filter(lambda x: x % 2, fib)
print result

reduce(lambda x, y: x+y, range(1,101))


%%writefile data/ds_spark_wiki.txt
Wikipedia
Apache Spark is an open source cluster computing framework.
아파치 스파크는 오픈 소스 클러스터 컴퓨팅 프레임워크이다.
Originally developed at the University of California, Berkeley's AMPLab,
the Spark codebase was later donated to the Apache Software Foundation,
which has maintained it since.
Spark provides an interface for programming entire clusters with
implicit data parallelism and fault-tolerance.

textFile = sc.textFile("data/ds_spark_wiki.txt")

textFile.first()

words=textFile.map(lambda x:x.split(' '))

words.collect()

textFile.map(lambda s:len(s)).collect()

_sparkLine=textFile.filter(lambda line: "Spark" in line)

print _sparkLine.count()

_line = textFile.filter(lambda line: u"스파크" in line)

print _line.first()

_aList=[1,2,3]
rdd = sc.parallelize(_aList)

rdd.take(3)

nums = sc.parallelize([1, 2, 3, 4])
squared = nums.map(lambda x: x * x).collect()
print squared

a=["this is","a line"]
_rdd=sc.parallelize(a)

words=_rdd.map(lambda x:x.split())
print words.collect()

_upper=_rdd.map(lambda x:x.replace("a","AA"))
_upper.take(10)

's'.upper()

pluralRDD =words.map(lambda x: x[0].upper())
print pluralRDD.collect()

pluralRDD =words.map(lambda x: [i.upper() for i in x])
print pluralRDD.collect()

pluralRDD =words.map(lambda x: [i.upper() for i in x]).collect()
print pluralRDD

wordsLength = words\
    .map(len)\
    .collect()
print wordsLength%%writefile ./data/ds_spark_2cols.csv
35, 2
40, 27
12, 38
15, 31
21, 1
14, 19
46, 1
10, 34
28, 3
48, 1
16, 2
30, 3
32, 2
48, 1
31, 2
22, 1
12, 3
39, 29
19, 37
25, 2

inp_file = sc.textFile("./data/ds_spark_2cols.csv")
numbers_rdd = inp_file.map(lambda line: line.split(','))

numbers_rdd.take(10)

data_home=os.path.join(home,"Code/git/else/uber-tlc-foil-response")
filePath=os.path.join(data_home,"Uber-Jan-Feb-FOIL.csv")

_fub = sc.textFile(filePath)

type(_fub)

_fub.count()

_fub.first()

_dub = _fub.map(lambda line: line.split(","))

type(_dub)

_row0keys=_dub.map(lambda row: row[0]).distinct().collect()

print _row0keys

_dub.filter(lambda row: "B02512" in row).count()

_dub.filter(lambda row: "B02512" in row).filter(lambda row: int(row[3])>2000).collect()

_noheader = _fub.filter(lambda line: "base" not in line).map(lambda line:line.split(","))
_noheader.count()

_noheader.map(lambda x: (x[0], int(x[3]))).reduceByKey(lambda k,v: k + v).collect()

S-4: RDD word count

!ls data/ds_spark_wiki.txt

def mySplit(x):
    return x.split(" ")

words=textFile.map(mySplit)

type(words)

for i in words.collect():
    print i

words=textFile.map(lambda x:x.split(' '))

lines = sc.textFile("data/ds_spark_wiki.txt")
word_count_bo = lines\
    .flatMap(lambda x: x.split(' '))

word_count_bo.collect()

from operator import add
lines = sc.textFile("data/ds_spark_wiki.txt")
word_count_bo = lines\
    .flatMap(lambda x: x.split(' '))\
    .map(lambda x: (x.lower().rstrip().lstrip().rstrip(',').rstrip('.'), 1))\
    .reduceByKey(add)

word_count_bo.count()

word_count_bo.first()

for x in word_count_bo.take(30):
    print x

