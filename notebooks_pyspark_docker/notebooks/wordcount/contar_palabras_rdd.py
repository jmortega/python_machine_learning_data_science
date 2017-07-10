import sys

from pyspark import SparkContext
import str

sc = SparkContext('local[2]', 'pyspark tutorial') 

def noPunctuations(text):
    """Removes punctuation and convert to lower case
    Args:
        text (str): A string.
    Returns:
        str: The cleaned up string.
    """
    return text.translate(str.maketrans("","",string.punctuation)).lower()

lines_rdd = sc.textFile(get(1), 1)
counts = lines_rdd.map(noPunctuations).flatMap(lambda x: x.split(' ')) \
         .map(lambda x: (x, 1)) \
		 .reduceByKey(lambda x, y: x+y)
		 
for (word, count) in counts.collect():
   print(word,count)
