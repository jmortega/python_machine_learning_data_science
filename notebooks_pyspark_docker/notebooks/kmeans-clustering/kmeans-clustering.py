## Spark Application for performing Kmeans clustering.

import csv

from numpy import array
from math import sqrt
from StringIO import StringIO

from pyspark import SparkConf, SparkContext
from pyspark.mllib.clustering import KMeans, KMeansModel

# Evalúe el algoritmo calculando la suma de los errores cuadrados
def error(point):
    center = clusters.centers[clusters.predict(point)]
    return sqrt(sum([x**2 for x in (point - center)]))


if __name__ == '__main__':
    conf = SparkConf().setAppName("Kmeans")
    sc   = SparkContext(conf=conf)


    # Cargar los datos
    data = sc.textFile("kmeans_data.txt")
    parsedData = data.map(lambda line: array([float(x) for x in line.split(' ')]))

    
    # Construir el modelo KMeans a partir de los datos y los parámetros necesarios para su ejecución
    clusters = KMeans.train(parsedData, 2, maxIterations=10,
                            runs=10, initializationMode="random")


    WSSSE = parsedData.map(lambda point: error(point)).reduce(lambda x, y: x + y)
    print("Error obtenido = " + str(WSSSE))    
