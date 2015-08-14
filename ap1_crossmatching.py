from __future__ import division
from math import *
import random
import numpy as np
from sklearn import svm
import astroML
from astroML.datasets import fetch_sdss_specgals

#data = np.loadtxt("GalaxyZoo1_DR_table2.txt", delimiter = ",", skiprows = 1, usecols = (1,2,13, 14, 15))
labels = np.loadtxt("GalaxyZoo1_DR_table2.txt", delimiter = ",", skiprows = 1, usecols = (14,)) #only gets binary label col of elliptical

data = open("GalaxyZoo1_DR_table2.txt")
data2 = fetch_sdss_specgals()
print len(data2)
sdss_ras = data2['ra']
sdss_decs = data2['dec']

RAs = []
DECs = []

row = 0
data.readline() #crude way of skipping first line, see if you can improve this
for line in data:
    list1 = line.strip().split(",")
    #print line
    ra = (line.strip().split(","))[1].strip().split(":")
    raH = float(ra[0])
    raM = float(ra[1])
    raS = float(ra[2])
    ra = raH + raM/60.0 + raS/3600.0
    RAs.append(ra)
    row += 1
    dec = (line.strip().split(","))[2].strip().split(":")
    decH = float(dec[0])
    decM = float(dec[1])
    decS = float(dec[2])
    dec = decH + decM/60.0 + decS/3600.0
    DECs.append(dec)
    #print ra
print len(RAs)
print RAs[-5:]
print DECs[-5:]
print sdss_ras[:5]

for row in range(len(data2)):
    if sdss_ras[row] in RAs: #go the other way around, you need RAs index to find label
        print "found a match!"
        print sdss_ras[row]

##clf = svm.SVC(random_state = 3) #DON'T DO THIS!
###clf.fit(trainingSet, trainingSetLabels)
##print clf.fit(trainingSet, trainingSetLabels)
##
###Training accuracy
##numCorrect = 0
##for i in range(len(trainingSetEllipticals)):
##    prediction = clf.predict(trainingSetEllipticals[i])
##    #print prediction
##    if prediction[0] > 0.5:
##        numCorrect += 1
##
##print "Training accuracy = ", numCorrect/len(trainingSetEllipticals)
##
##
###Testing accuracy
##testingSetElliptical = ellipticals[500:1000, :9]
##
##numCorrect = 0
##for i in range(len(testingSetElliptical)):
##    prediction = clf.predict(testingSetElliptical[i])
##    #print prediction
##    if prediction[0] > 0.5:
##        numCorrect += 1
##
##print "Testing accuracy = ", numCorrect/len(testingSetElliptical)
