# Dr. Gautam Ravindra Dange,
# Institute of Artificial Intelligence, University of Bremen

import json
import Dev.params as params
from OperatingDT import *
import Queries as Queries



class ShelfData:
    pass

class UseShelfData:
    pass

arrayofShelfData=[]


def init():
    #with open(params.shelfLayerinfoFile) as json_file:
    #	data = json.load(json_file)

    datadump = POSTGRAPHQL(Queries.ShelfLayerQuery, params.DevSandbox)
    shelfData = ShelfData()
    shelfData.dto = json.loads(datadump)['data']['stores']
    length = len(shelfData.dto[0]['shelves']) - 1

    for i in range(0, length):
        length2 =len(shelfData.dto[0]['shelves'][i]['shelfLayers'])
        for j in range(0,length2):
            useShelfData =  UseShelfData()
            useShelfData.shelf = shelfData.dto[0]['shelves'][i]['externalReferenceId']
            useShelfData.shelflayer = shelfData.dto[0]['shelves'][i]['shelfLayers'][j]['externalReferenceId']
            useShelfData.id = shelfData.dto[0]['shelves'][i]['shelfLayers'][j]['id']
            arrayofShelfData.append(useShelfData.__dict__)


    jsonArraydumps = json.dumps(arrayofShelfData,sort_keys=True)

    shelfdata =json.loads(jsonArraydumps)
    shelfdata.sort(key=lambda x: x["shelf"])

    with open(params.shelfLayercalculations, "w") as shelflayerfile:
        json.dump(shelfdata, shelflayerfile, indent=4, sort_keys=True)

def findid(shelf,level):
    jsonArraydumps = json.dumps(arrayofShelfData)
    shelfdata =json.loads(jsonArraydumps)
    length3 = len(shelfdata)
    for h in range(length3):
        if int(shelfdata[h]['shelf'])==int(shelf):
            if int(shelfdata[h]['shelflayer'])==int(level):
                return int(shelfdata[h]['id'])

init()

for i in range(0,20):
    for j in range(1,10):
        if(str(findid(i,j)) != "None"):
            print ("Shelf:  "+ str(i) + "   Layer:  " +  str(j) + "   ShelfLayerId:  " +   str(findid(i,j)))
