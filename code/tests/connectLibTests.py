import sys
import pickle
import numpy as np
sys.path.insert(0, '../functions/')
from epsilonDifference import epsilonDifference as floatEq
from cluster import Cluster
from connectLib import otsuVox, connectedComponents, thresholdByVolumePercentile
from sets import Set

synthGauss = pickle.load(open('synthDat/smallGaussian.synth', 'r'))
synthTwoGauss = pickle.load(open('synthDat/smallTwoGaussian.synth', 'r'))

print '\n\notsuVox in connectLib.py'
synthGaussSolution = [(1, 2, 2), (2, 1, 2), (2, 2, 1), (2, 2, 2), (2, 2, 3), (2, 3, 2), (3, 2, 2)]
synthGaussBian = otsuVox(synthGauss)
test1 = zip(*np.where(synthGaussBian == 1.))
print '\tTest 1: ', test1 == synthGaussSolution,'\n\t\tExpected: ', synthGaussSolution, '\n\t\tResult: ', test1

synthTwoGaussSolution = [(0, 1, 1), (1, 0, 1), (1, 1, 0), (1, 1, 1), (1, 1, 2), (1, 2, 1), (2, 1, 1), (2, 3, 3), (3, 2, 3), (3, 3, 2), (3, 3, 3), (3, 3, 4), (3, 4, 3), (4, 3, 3)]
synthTwoGaussBian = otsuVox(synthTwoGauss)
test2 = zip(*np.where(synthTwoGaussBian == 1.))
print '\tTest 2: ', test2 == synthTwoGaussSolution,'\n\t\tExpected: ', synthTwoGaussSolution, '\n\t\tResult: ', test2

print '\n\nconnectedComponents in connectLib.py'
cluster1Solution = Set([(1,1,1), (0,1,1), (2,1,1), (1,0,1), (1,2,1), (1,1,0), (1,1,2)])
cluster2Solution = Set([(3,3,3), (2,3,3), (4,3,3), (3,2,3), (3,4,3), (3,3,2), (3,3,4)])

clusterList = connectedComponents(synthTwoGaussBian)
memberList = [Set([tuple(subElem) for subElem in elem.members]) for elem in clusterList]
test1, test2, test3 = False, False, False

#Test that the method returns 3 total clusters, one background, and two correct label identifications
if cluster1Solution in memberList:
    test1 = True

if cluster2Solution in memberList:
    test2 = True

if len(memberList) == 3:
    test3 = True

print '\tTest 1: ', test1
print '\tTest 2: ', test2
print '\tTest 3: ', test3

testData0 = [[20, 20, 20], [21, 20, 20], [20, 21, 20], [20, 20, 21], [21, 21, 20], [21, 20, 21], [20, 21, 21], [21, 21, 21], [19, 20, 20], [20, 19, 20], [20, 20, 19], [20, 20, 19], [19, 19, 20], [19, 20, 19], [20, 19, 19]]
testData1 = [[10, 10, 10], [11, 10, 11], [11, 11, 11], [10, 11, 10], [11, 10, 10], [10, 10, 11]]
testData2 = [[3,3,3], [3,3,4], [3,4,4], [3,4,5], [3,5,5], [4,5,5], [4,5,6]]
testData3 = [[0, 0, 0], [0, 0, 1], [1, 0, 0], [0, 1, 0], [1, 1, 0], [0, 1, 1], [1, 0, 1], [1, 1, 1]]
testCluster0 = Cluster(testData0)
testCluster1 = Cluster(testData1)
testCluster2 = Cluster(testData2)
testCluster3 = Cluster(testData3)
testClusterList = [testCluster0, testCluster1, testCluster2, testCluster3]

print '\n\nthresholdByVolumePercentile in connectLib.py'
print '\tTest 1: ', thresholdByVolumePercentile(testClusterList)[1].members == [[3,3,3], [3,3,4], [3,4,4], [3,4,5], [3,5,5], [4,5,5], [4,5,6]], '\n\t\tExpected: ', [[3,3,3], [3,3,4], [3,4,4], [3,4,5], [3,5,5], [4,5,5], [4,5,6]], '\n\t\tResult: ', str(thresholdByVolumePercentile(testClusterList)[1].members)
