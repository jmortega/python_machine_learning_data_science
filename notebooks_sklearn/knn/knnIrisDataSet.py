# -*- coding: utf-8 -*-
from sklearn.neighbors import KNeighborsClassifier as knn
from sklearn import datasets
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

def knnIrisDataSet(X,y, n):

    #definir el clasificador the the classifier and fits it to the data 
    res=0.05
    k1 = knn(n_neighbors=n,p=2,metric='minkowski')
    #entrenar los datos
    k1.fit(X,y)
    
    #definir la malla
    x1_min, x1_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    x2_min, x2_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, res),np.arange(x2_min, x2_max, res))
   
    #realizar la prediccion
    Z = k1.predict(np.array([xx1.ravel(), xx2.ravel()]).T)
    Z = Z.reshape(xx1.shape)
    
    #colores
    cmap_light = ListedColormap(['#FFAAAA', '#AAFFAA', '#AAAAFF'])
    cmap_bold = ListedColormap(['#FF0000', '#00FF00', '#0000FF'])
    
    #dibujar la superficie de decision
    plt.contourf(xx1, xx2, Z, alpha=0.4, cmap=cmap_light)
    plt.xlim(xx1.min(), xx1.max())
    plt.ylim(xx2.min(), xx2.max())
    
    #dibujar los puntos
    for idx, cl in enumerate(np.unique(y)):
        plt.scatter(X[:, 0], X[:, 1], c=y, cmap=cmap_bold)
       
    plt.show()
    

if __name__ == "__main__":

    iris = datasets.load_iris()
    X = iris.data[:, 0:2]
    y = iris.target
    knnIrisDataSet(X,y,15)
