#
# Assignment4 Interface
# Name: Sri Naga Sushma Jyothula
#
from pymongo import MongoClient
import os
import sys
import json
import math
import re

def DistanceFunction(lat2, long2, lat1, long1):
    R = 3959
    l1 = math.radians(lat1)
    l2 = math.radians(lat2)
    latdiff = math.radians(lat2 - lat1)
    longdiff = math.radians(long2 - long1)

    a = (math.sin(latdiff/2) * math.sin(latdiff/2))
    a += (math.cos(l1) * math.cos(l2) * math.sin(longdiff/2) * math.sin(longdiff/2))

    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c

def FindBusinessBasedOnCity(cityToSearch, minReviewCount, saveLocation1, collection):
    dataList = collection.find({'city': re.compile('^' + re.escape(cityToSearch) + '$', re.IGNORECASE), 'type': "business"})
    with open(saveLocation1, "w") as openFile:
        for data in dataList:
            name = data['name']
            addressVar = data['full_address']
            addressVar = addressVar.replace("\n", ", ")
            cityVar = data['city']
            stateVar = data['state']
            starsVar = data['stars']
            reviewCountVar = data['review_count']            

            if(reviewCountVar >= minReviewCount):
                writeValue = ""
                writeValue = name.upper() + "$"
                writeValue = writeValue + addressVar.upper() + "$"
                writeValue = writeValue + cityVar.upper() + "$"
                writeValue = writeValue + stateVar.upper() + "$"
                writeValue = writeValue + str(starsVar).upper()
                writeValue += "\n"
                openFile.write(writeValue)

def FindBusinessBasedOnLocation(categoriesToSearch, myLocation, minDistance, maxDistance, saveLocation2, collection):
    dataList = collection.find({'categories': {'$in': categoriesToSearch}})
    myLocLatitude = float(myLocation[0])
    myLocLongitude = float(myLocation[1])

    with open(saveLocation2, "w") as openFile:
        for dataPoint in dataList:
            nameVar = dataPoint['name']
            currLat = float(dataPoint['latitude'])
            currLong = float(dataPoint['longitude'])
            calculatedDist = DistanceFunction(currLat, currLong, myLocLatitude, myLocLongitude)
            if(calculatedDist >= minDistance and calculatedDist <= maxDistance):
                openFile.write(nameVar.upper() + "\n")