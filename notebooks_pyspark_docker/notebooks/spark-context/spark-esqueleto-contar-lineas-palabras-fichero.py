#!/usr/bin/python2

## Spark Application - execute with spark-submit

## Imports
from pyspark import SparkConf, SparkContext

## Module Constants
APP_NAME = "My Spark Application"

## Main functionality
def main(sc):
    lines = sc.textFile("README.md");
    print("numero de lineas:"+str(lines.count()))
    counts = lines.flatMap(lambda x: x.split(' ')).map(lambda x: (x,1)).reduceByKey(lambda x,y: x+y);
    for key,value in counts.collect():
        print(str(key)+"-->"+str(value))

if __name__ == "__main__":
    # Configure Spark
    conf = SparkConf().setMaster("local[*]")
    conf = conf.setAppName(APP_NAME)
    sc   = SparkContext(conf=conf)

    # Execute Main functionality
    main(sc)
