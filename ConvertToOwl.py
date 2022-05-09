# Dr. Gautam Ravindra Dange,
# Institute of Artificial Intelligence, University of Bremen

from flask import Flask, jsonify, request, abort, make_response, json
import Dev.params as params
import OperatingDT as OperatingDT
from Product import *
import Queries as Queries
from Product import *
from ProductUnit import *
from ProductGTIN import *
from ProductDescription import *
from MaterialGroup import *
from Planogram import *
import ReadJSON
import os.path
class ShelfInfo:
    pass

datadump = OperatingDT.POSTGRAPHQL(Queries.UnitQuery, params.DevSandbox)
datadumploads        = json.loads(datadump)
def getUnitof(unitt):
    for var in range(len(datadumploads['data']['units'])):
        if datadumploads['data']['units'][var]['symbol'] == unitt:
            return datadumploads['data']['units'][var]['id']
        else :

def Convert(products,Operation):
    for p in products:
        E1WBB01 = p['E1WBB01']
        if 'E1WBB02' in E1WBB01:
            E1WBB02 = p['E1WBB01']['E1WBB02']
        if 'E1WBB03' in E1WBB01:
            E1WBB03 = p['E1WBB01']['E1WBB03']
        if 'E1WBB04' in E1WBB03:
            E1WBB04 = p['E1WBB01']['E1WBB03']['E1WBB04']
        E1WBB07 = p['E1WBB01']['E1WBB03']['E1WBB07']
        E1WBB08 = p['E1WBB01']['E1WBB03']['E1WBB07']['E1WBB08']
        E1WBB09 = p['E1WBB01']['E1WBB09']
        E1WBB10 = p['E1WBB01']['E1WBB10']
        E1WBB12 = p['E1WBB01']['E1WBB12']
        if 'E1WBB16' in E1WBB01:
            E1WBB16 = p['E1WBB01']['E1WBB16']
        if 'E1WBB18' in E1WBB01:
            E1WBB18 = p['E1WBB01']['E1WBB18']
        if 'E1WBB18_EXT' in E1WBB18:
            E1WBB18_EXT = p['E1WBB01']['E1WBB18']['E1WBB18_EXT']

        ProductId               = 0
        ProductUnitId           = 0
        hierarchyLevel          = 0
        id                      = 400
        parentId                = 0
        versionTimestamp        = 0
        unitCode                = 'NONE'
        bitwiseProduct          = 1
        bitwiseProductDesc      = 2
        bitwiseProductUnit      = 4
        bitwiseProductGtin      = 8
        bitwisePlanogram        = 16

        materialGroupId         = params.materialGroupId
        ProductId               = E1WBB01['MATNR_LONG']
        isoLanguageCode         = E1WBB01['LANG_ISO']
        productType             = E1WBB02['MATKL']
        netWeight               = E1WBB02['NTGEW']
        description2            = E1WBB02['MTART']
        name                    = E1WBB02['ATTYP']
        productUnit             = E1WBB03['MEINH']
        denominatorBaseUnit     = E1WBB03['UMREN']
        du                      = E1WBB03['MEABM']
        wu                      = E1WBB03['GEWEI']
        grossWeight             = E1WBB03['BRGEW']
        height                  = E1WBB03['HOEHE']
        length                  = E1WBB03['LAENG']
        numeratorBaseUnit       = E1WBB03['UMREZ']
        volume                  = E1WBB03['VOLUM']
        vu                      = E1WBB03['VOLEH']
        width                   = E1WBB03['BREIT']
        description             = E1WBB10['MAKTM']
        maxStackSize            = int(float(E1WBB12['MABST']))
        _shelf                  = E1WBB18['SHELF']
        _layerinshelf           = E1WBB18['shelfLayerId']
        numberOfFacings         = E1WBB18['numberOfFacings']
        orientationYaw          = E1WBB18['orientationYaw']
        positionX               = E1WBB18['positionX']
        numberOfFacings         = E1WBB18['numberOfFacings']
        orientationYaw          = E1WBB18['orientationYaw']
        positionX               = E1WBB18['positionX']
        dimensionUnit           = getUnitof(du)
        volumeUnit              = getUnitof(vu)
        weightUnit              = getUnitof(wu)
        shelfInfo               = ShelfInfo()
        _shelflayerid           = ReadJSON.findid(int(_shelf),int(_layerinshelf))
        shelfInfo.shelf         = _shelf
        shelfInfo.layerinshelf  = _layerinshelf
        shelfInfo.shelflayerid  = _shelflayerid
        shelfLayerId            = shelfInfo.shelflayerid

        with open("shelfInfo.txt","w") as file_object:
            file_object.write('the calculated shelf has shelf: '+ str(int(shelfInfo.shelf)) + '& layer'+ str(int(shelfInfo.layerinshelf)) +' & shelflayerid' +  str(shelfInfo.shelflayerid))
        shelfInfojson           = json.dumps(shelfInfo.__dict__, indent=4, sort_keys=True)
