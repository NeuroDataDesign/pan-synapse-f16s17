import sys
sys.path.insert(0, '../functions/')
import mouseVis
import random

data1 = [random.random() for i in range(100)]
mouseVis.generateVoxHist(data1, 'random data 1', yaxis='percentage of data')

data2 = [random.random() for i in range(100)]
mouseVis.generateVoxHist(data2, 'random data 2', yaxis='percentage of data')

data3 = [data1, data2]
mouseVis.generateVoxHist(data3, 'random data multiVoxHist', yaxis='percentage of data')
