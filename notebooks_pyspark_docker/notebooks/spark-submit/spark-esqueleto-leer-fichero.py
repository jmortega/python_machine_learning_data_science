#!/usr/bin/python2

## Spark Application - execute with spark-submit

## Imports
from pyspark import SparkConf, SparkContext

## Module Constants
APP_NAME = "My Spark Application"

## Main functionality
def main(sc):
     file = sc.textFile("README.md")
     print("Numero lineas :"+str(file.count()))
     print("First line"+file.first())
     
     filter = file.filter(lambda line:"MASTER" in line)
     print(filter.collect())



if __name__ == "__main__":
    # Configure Spark
    conf = SparkConf().setMaster("local[*]")
    conf = conf.setAppName(APP_NAME)
    sc   = SparkContext(conf=conf)

    # Execute Main functionality
    main(sc)
