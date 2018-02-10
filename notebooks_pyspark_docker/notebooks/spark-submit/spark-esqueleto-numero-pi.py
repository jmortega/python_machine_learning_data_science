#!/usr/bin/python2

## Spark Application - execute with spark-submit

## Imports
from pyspark import SparkConf, SparkContext
from random import random

## Module Constants
APP_NAME = "Obtener valor del numero pi"

NUM_SAMPLES = 10000000


def sample(p):
    x, y = random(), random()
    return 1 if x*x + y*y < 1 else 0

## Main functionality
def main(sc):

    count = sc.parallelize(xrange(0, NUM_SAMPLES)).map(sample).reduce(lambda a, b: a + b)

    print ("El valor de Pi es aproximadamente %f" % (4.0 * count / NUM_SAMPLES))

if __name__ == "__main__":
    # Configure Spark
    conf = SparkConf().setMaster("local[*]")
    conf = conf.setAppName(APP_NAME)
    sc   = SparkContext(conf=conf)

    # Execute Main functionality
    main(sc)
