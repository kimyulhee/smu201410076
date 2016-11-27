S-5: RDD from url

import os
_datadir='data'
datapath = os.path.join(os.getcwd(),_datadir)
print datapath

_url = 'http://kdd.ics.uci.edu/databases/kddcup99/kddcup.data_10_percent.gz'

_fname=os.path.join(datapath,'kddcup.data_10_percent.gz')
if(not os.path.exists(_fname)):
    print "%s data does not exist! retrieving.." % _fname
    _f=urllib.urlretrieve(_url,_fname)

print _fname

_data = sc.textFile(_fname)

_data.count()

_data.take(5)

_normal_data = _data.filter(lambda x: 'normal.' in x)
print _normal_data.count()

_split_data=_data.map(lambda x: x.split(','))
print _split_data.take(5)from pyspark.sql import Row

_csv_data = _data.map(lambda l: l.split(","))
_row_data = _csv_data.map(lambda p: 
    Row(
        duration=int(p[0]), 
        protocol_type=p[1],
        service=p[2],
        flag=p[3],
        src_bytes=int(p[4]),
        dst_bytes=int(p[5])
    )
)

from pyspark.sql import SQLContext
sqlCtx = SQLContext(sc)

_df=sqlCtx.createDataFrame(_row_data)
_df.registerTempTable("_my")

_df.select("protocol_type", "duration", "dst_bytes").groupBy("protocol_type").count().show()

_df.select("protocol_type", "duration", "dst_bytes").filter(_df.duration>1000).filter(_df.dst_bytes==0).groupBy("protocol_type").count().show()

tcp_interactions = sqlCtx.sql("""
    SELECT duration, dst_bytes FROM _my WHERE protocol_type = 'tcp' AND duration > 1000 AND dst_bytes = 0
""")
tcp_interactions.show()

tcp_interactions_out = tcp_interactions.map(lambda p: "Duration: {}, Dest. bytes: {}".format(p.duration, p.dst_bytes))
for ti_out in tcp_interactions_out.collect():
  print ti_out


S-8: Hello Statistics

from pyspark.mllib.stat import Statistics

parallelData = sc.parallelize([1.0, 2.0, 5.0, 4.0, 3.0, 3.3, 5.5])

# run a KS test for the sample versus a standard normal distribution
testResult = Statistics.kolmogorovSmirnovTest(parallelData, "norm", 0, 1)
print(testResult)

from pyspark.sql import SQLContext
sqlCtx = SQLContext(sc)from pyspark.sql.functions import rand, randn
 # Create a DataFrame with one int column and 10 rows.
df = sqlCtx.range(0, 10)
df.show()

df.select("id", rand(seed=10).alias("uniform"), randn(seed=27).alias("normal")).show()
df.describe().show()

df = sqlCtx.range(0, 10).withColumn('rand1', rand(seed=10)).withColumn('rand2', rand(seed=27))
print df.stat.corr('rand1', 'rand2')
print df.stat.corr('id', 'id')

names = ["Alice", "Bob", "Mike"]
items = ["milk", "bread", "butter", "apples", "oranges"]
df = sqlCtx.createDataFrame([(names[i % 3], items[i % 5]) for i in range(100)], ["name", "item"])
df.show(10)

df = sqlCtx.createDataFrame([(1, 2, 3) if i % 2 == 0 else (i, 2 * i, i % 4) for i in range(100)], ["a", "b", "c"])
print df.show(10)
freq = df.stat.freqItems(["a", "b", "c"], 0.4)
