from __future__ import division
from math import *
import random
import numpy as np
from sklearn import svm
import astroML
from astroML.datasets import fetch_sdss_specgals
import time

data = np.loadtxt("crossmatched1_imagingdata_srane.txt", delimiter = ",", skiprows = 1, usecols = (2, 11, 13, 15, 17, 19, 23, 24, 25))
labels = np.loadtxt("crossmatched1_imagingdata_srane.txt", delimiter = ",", skiprows = 1, usecols = (14,)) #only gets binary label col of elliptical

#data2 = fetch_sdss_specgals()
#print data2.dtype.names

#IS IT NOT CLOSING THE FILE AFTER READING OR SOMETHING? HENCE ALTERNATING OUTPUTS? - 

isElliptical = data[:,7] #corresponds to col 14 of real data file, which is the elliptical bool value
isSpiral = data[:,6]
isUncertain = data[:,8]

ellipticals = data[isElliptical == 1]

spirals = data[isSpiral == 1]
uncertains = data[isUncertain == 1]

trainingSetEllipticals = ellipticals[:5000, 1:6] #check whether these numbers are inclusive
trainingSetSpirals = spirals[:5000, 1:6] #extracting first 5000 spiral and elliptical to train model, excluding last 3 cols (labels)

print trainingSetEllipticals[0]

trainingSet = np.vstack((trainingSetEllipticals, trainingSetSpirals))  #FIX: add label col to training sets, then shuffle sets
print trainingSet.shape
trainingSetLabels = np.empty((len(trainingSetEllipticals) + len(trainingSetSpirals), ))

startTime = time.time()
print "Time before training = ", startTime
counter = 0
for label in trainingSetLabels:
    if counter < len(trainingSetEllipticals):
        trainingSetLabels[counter] = 1
    else:
        trainingSetLabels[counter] = 0

clf = svm.SVC() 
#clf.fit(trainingSet, trainingSetLabels)
print clf.fit(trainingSet, trainingSetLabels)

print "Done training! Time = ", time.time() - startTime, "seconds"
#Training accuracy
numCorrect = 0
#can just do clf.predict(trainingSetEllipticals)
for i in range(len(trainingSetEllipticals)):
    prediction = clf.predict(trainingSetEllipticals[i])
    #print trainingSetEllipticals[i]
    #print prediction
    if prediction[0] > 0:
        numCorrect += 1
        
    if i%100 == 0 and i > 0:
        print "At iteration", i, "Training accuracy = ", numCorrect/i

print "Training accuracy = ", numCorrect/len(trainingSetEllipticals)
print "Time = ", time.time() - startTime, "seconds"
print

#Testing accuracy
testingSetElliptical = ellipticals[5000:10000, 1:6]

numCorrect = 0
for i in range(len(testingSetElliptical)):
    prediction = clf.predict(testingSetElliptical[i])
    #print prediction
    if prediction[0] > 0:
        numCorrect += 1

print "Testing accuracy = ", numCorrect/len(testingSetElliptical)
print "Time = ", time.time() - startTime, "seconds"
