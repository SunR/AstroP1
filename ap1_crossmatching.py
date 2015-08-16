from __future__ import division
from math import *
import random
import numpy as np
from sklearn import svm
import astroML
from astroML.datasets import fetch_sdss_specgals
import time

#data = np.loadtxt("GalaxyZoo1_DR_table2.txt", delimiter = ",", skiprows = 1, usecols = (1,2,13, 14, 15))
labels = np.loadtxt("GalaxyZoo1_DR_table2.txt", delimiter = ",", skiprows = 1, usecols = (14,)) #only gets binary label col of elliptical
<<<<<<< HEAD
gzOBJID = np.loadtxt("GalaxyZoo1_DR_table2.txt", delimiter = ",", skiprows = 1, usecols = (0,))
=======
>>>>>>> 43322a5f42e1df8a65e6938c7b83644a7201f1bd

data = open("GalaxyZoo1_DR_table2.txt")
data2 = fetch_sdss_specgals()
print len(data2)
sdss_ras = data2['ra']
sdss_decs = data2['dec']
<<<<<<< HEAD
sdss_objid = data2['objID']

g = set(gzOBJID)
s = set(sdss_objid)

print "crossmatchig objID"
print g.intersection(s)

print gzOBJID[:5]
print sdss_objid[-5:]

for ID in gzOBJID:
    if ID in sdss_objid:
        print "found a objid match"

print "finished looking for objid matches"
print 
=======
>>>>>>> 43322a5f42e1df8a65e6938c7b83644a7201f1bd

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
<<<<<<< HEAD
#print len(RAs)
#print RAs[-5:]
#print DECs[-5:]
=======
print len(RAs)
print RAs[-5:]
print DECs[-5:]
>>>>>>> 43322a5f42e1df8a65e6938c7b83644a7201f1bd
print sdss_ras[:5]

gzIndexes = []
sdss_color_data = []

#round RAs and DECs to 4th decimal place so they can match other catalogue
for row in range(len(RAs)):
<<<<<<< HEAD
    RAs[row] = round(RAs[row], 4) #'%.1f' %
=======
    RAs[row] = round(RAs[row], 4)
>>>>>>> 43322a5f42e1df8a65e6938c7b83644a7201f1bd
    DECs[row] = round(DECs[row], 4)

for row in range(len(data2)):
    sdss_ras[row] = round(sdss_ras[row], 4)
    sdss_decs[row] = round(sdss_decs[row], 4)

startTime = time.time()
<<<<<<< HEAD
print "time at start of cross-matching = ", startTime
=======
print "time at of cross-matching = ", startTime
>>>>>>> 43322a5f42e1df8a65e6938c7b83644a7201f1bd

numMatches = 0
numNoMatch = 0

gzPairs = []
sdssPairs = []

for row in range(len(RAs)):
    gzPairs.append((RAs[row], DECs[row]))

for row in range(len(sdss_ras)):
    sdssPairs.append((sdss_ras[row], sdss_decs[row]))
<<<<<<< HEAD

print sdssPairs[:5]
print gzPairs[:5]

#g = set(DECs)
#s = set(sdss_decs)
#print "searching for intersections"
#print g.intersection(s)
for row in range(len(gzPairs)):
    if RAs[row] in sdss_ras: #cross-matching tuples instead now, ra AND dec
=======
    
for row in range(len(gzPairs)):
    if gzPairs[row] in sdssPairs: #cross-matching tuples instead now, ra AND dec
>>>>>>> 43322a5f42e1df8a65e6938c7b83644a7201f1bd
        #print "found a match!"
        sdss_color_data.append(data2[row])
        gzIndexes.append(row)
        numMatches += 1
    else:
        numNoMatch +=1

<<<<<<< HEAD
    if row%1000 == 0: #every 10000 rows, report in    
=======
    if row%10000 == 0: #every 10000 rows, report in    
>>>>>>> 43322a5f42e1df8a65e6938c7b83644a7201f1bd
        print "completed", row, "tests, found", numMatches, "cross-matches"
        print "time = ", time.time() - startTime

print "Cross-matching finished, time = ", time.time() - startTime
print
print numMatches, "galaxies matched with SDSS data", numNoMatch, "not matched, out of total", numMatches + numNoMatch, "tested from GZ data"
print
print "Indexes of gz data that match", gzIndexes
print
print "Corresponding SDSS data", sdss_color_data

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
