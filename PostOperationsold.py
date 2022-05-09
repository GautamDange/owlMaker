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

    #just to Understand the calling sequence
    #productjson       =   PostOperations.PostProduct                  (products)
    #productUnitjson   =   PostOperations.PostProductUnit              (products)
    #pDescriptionjson  =   PostOperations.PostProductDescription       (products)
    #productGTINjson   =   PostOperations.PostProductGTIN              (products)
    #planogramjson     =   PostOperations.PostPlanogram                (products)

PRODUCTID = 0
PRDOUCTUNITID = 0


datadump = OperatingDT.POSTGRAPHQL(Queries.UnitQuery, params.DevSandbox)
datadumploads        = json.loads(datadump)
def getUnitof(unitt):
    for var in range(len(datadumploads['data']['units'])):
        if datadumploads['data']['units'][var]['symbol'] == unitt:
            return datadumploads['data']['units'][var]['id']
        else :
            return 5

def setup(p):
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


def PostProduct(products):
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


        PRODUCTID               = E1WBB01['MATNR_LONG']
        materialGroupId         = params.materialGroupId
        productType             = E1WBB02['MATKL']
        productUnit             = E1WBB03['MEINH']
        product                 = Product(PRODUCTID,materialGroupId,productType,productUnit)
        productjson             = json.dumps(product.__dict__, indent=4, sort_keys=True)
        productjsonloads        = json.loads(productjson)
        retJSON                 = OperatingDT.POST_PRODUCT(productjson)
        print productjson
        return productjson

print "working"
def PostProductUnit(products):
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

        #Product controller
        PRODUCTID               = E1WBB01['MATNR_LONG']
        materialGroupId         = params.materialGroupId
        productType             = E1WBB02['MATKL']
        productUnit             = E1WBB03['MEINH']
        denominatorBaseUnit     = E1WBB03['UMREN']
        du                      = E1WBB03['MEABM']
        dimensionUnit           = getUnitof(du)
        grossWeight             = E1WBB03['BRGEW']
        height                  = E1WBB03['HOEHE']
        productunitid           = 0
        length                  = E1WBB03['LAENG']
        maxStackSize            = int(float(E1WBB12['MABST']))
        netWeight               = E1WBB02['NTGEW']
        numeratorBaseUnit       = E1WBB03['UMREZ']
        unitCode                = 'NONE'
        volume                  = E1WBB03['VOLUM']
        vu                      = E1WBB03['VOLEH']
        volumeUnit              = getUnitof(vu)
        wu                      = E1WBB03['GEWEI']
        weightUnit              = getUnitof(wu)
        width                   = E1WBB03['BREIT']

        productUnit             = ProductUnit(denominatorBaseUnit, dimensionUnit,grossWeight,height,length,maxStackSize,netWeight,numeratorBaseUnit,PRODUCTID,unitCode,volume,volumeUnit,weightUnit,width)
        productUnitjson         = json.dumps(productUnit.__dict__, indent=4, sort_keys=True)
        productUnitjsonloads    = json.loads(productUnitjson)
    # ************* POST ***************************************************
        retJSON = OperatingDT.POST_PRODUCT_UNIT(productUnitjson)
        PRDOUCTUNITID = int(retJSON['id'])
        print productUnitjson
        print "4%%%5"
        print PRDOUCTUNITID
        return PRDOUCTUNITID

def PostProductDescription(products):
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

        PRODUCTID               = E1WBB01['MATNR_LONG']
        materialGroupId         = params.materialGroupId
        productType             = E1WBB02['MATKL']
        productUnit             = E1WBB03['MEINH']
        denominatorBaseUnit     = E1WBB03['UMREN']
        du                      = E1WBB03['MEABM']
        dimensionUnit           = getUnitof(du)
        grossWeight             = E1WBB03['BRGEW']
        height                  = E1WBB03['HOEHE']
        length                  = E1WBB03['LAENG']
        maxStackSize            = int(float(E1WBB12['MABST']))
        netWeight               = E1WBB02['NTGEW']
        numeratorBaseUnit       = E1WBB03['UMREZ']
        unitCode                = 'NONE'
        volume                  = E1WBB03['VOLUM']
        vu                      = E1WBB03['VOLEH']
        volumeUnit              = getUnitof(vu)
        wu                      = E1WBB03['GEWEI']
        weightUnit              = getUnitof(wu)
        width                   = E1WBB03['BREIT']
        description             = E1WBB10['MAKTM']
        isoLanguageCode         = E1WBB01['LANG_ISO']
        pDescription            = ProductDescription(description, isoLanguageCode, PRODUCTID)
        pDescriptionjson        = json.dumps(pDescription.__dict__, indent=4, sort_keys=True)
        pdloads                 = json.loads(pDescriptionjson)
        retJSON                 = OperatingDT.POST_PRODUCTDESC(pDescriptionjson)
        return pDescriptionjson

def PostProductGTIN(products,PRDOUCTUNITID):
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

        PRODUCTID               = E1WBB01['MATNR_LONG']
        materialGroupId         = params.materialGroupId
        productType             = E1WBB02['MATKL']
        productUnit             = E1WBB03['MEINH']
        denominatorBaseUnit     = E1WBB03['UMREN']
        du                      = E1WBB03['MEABM']
        dimensionUnit           = getUnitof(du)
        grossWeight             = E1WBB03['BRGEW']
        height                  = E1WBB03['HOEHE']
        length                  = E1WBB03['LAENG']
        maxStackSize            = int(float(E1WBB12['MABST']))
        netWeight               = E1WBB02['NTGEW']
        numeratorBaseUnit       = E1WBB03['UMREZ']
        unitCode                = 'NONE'
        volume                  = E1WBB03['VOLUM']
        vu                      = E1WBB03['VOLEH']
        volumeUnit              = getUnitof(vu)
        wu                      = E1WBB03['GEWEI']
        weightUnit              = getUnitof(wu)
        width                   = E1WBB03['BREIT']
        description             = E1WBB10['MAKTM']
        isoLanguageCode         = E1WBB01['LANG_ISO']
        description2            = E1WBB02['MTART']
        hierarchyLevel          = 0
        id                      = 400
        name                    = E1WBB02['ATTYP']
        parentId                = 0
        if 'E1WBB04' in E1WBB03:
            gtin                = E1WBB04['EAN11']
            gtinType            = 'NONE'
            mainGtinFlag        = True
            productGTIN         = ProductGTIN(gtin, gtinType, mainGtinFlag,PRDOUCTUNITID)
            productGTINjson     = json.dumps(productGTIN.__dict__, indent=4, sort_keys=True)
            gtloads             = json.loads(productGTINjson)
            # ************* POST ***************************************************
            retJSON = OperatingDT.POST_PRODUCT_GTIN(productGTINjson)
            print productGTINjson
            return productGTINjson


def createShelfData(products):
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

        #Product controller
        PRODUCTID               = E1WBB01['MATNR_LONG']
        materialGroupId         = params.materialGroupId
        productType             = E1WBB02['MATKL']
        productUnit             = E1WBB03['MEINH']
        # product Unit
        denominatorBaseUnit     = E1WBB03['UMREN']
        du                      = E1WBB03['MEABM']
        dimensionUnit           = getUnitof(du)
        grossWeight             = E1WBB03['BRGEW']
        height                  = E1WBB03['HOEHE']
        productunitid           = 0
        length                  = E1WBB03['LAENG']
        maxStackSize            = int(float(E1WBB12['MABST']))
        netWeight               = E1WBB02['NTGEW']
        numeratorBaseUnit       = E1WBB03['UMREZ']
        unitCode                = 'NONE'
        volume                  = E1WBB03['VOLUM']
        vu                      = E1WBB03['VOLEH']
        volumeUnit              = getUnitof(vu)
        wu                      = E1WBB03['GEWEI']
        weightUnit              = getUnitof(wu)
        width                   = E1WBB03['BREIT']
        #Product Description
        description             = E1WBB10['MAKTM']
        isoLanguageCode         = E1WBB01['LANG_ISO']
        #material group controller
        description2            = E1WBB02['MTART']
        hierarchyLevel          = 0
        id                      = 400
        name                    = E1WBB02['ATTYP']
        parentId                = 0
        #product GTIN Controller
        if 'E1WBB04' in E1WBB03:
            gtin                = E1WBB04['EAN11']
            gtinType            = 'NONE'
            mainGtinFlag        = True
            productGTIN         = ProductGTIN(gtin, gtinType, mainGtinFlag,PRDOUCTUNITID)
            productGTINjson     = json.dumps(productGTIN.__dict__, indent=4, sort_keys=True)
            gtloads             = json.loads(productGTINjson)
        # planogram Controller
        shelfInfo = ShelfInfo()
        shelfInfo.shelf         = E1WBB18['SHELF']
        shelfInfo.layerinshelf  = E1WBB18['shelfLayerId']
        shelfInfo.shelflayerid  = ReadJSON.findid(int(shelfInfo.shelf ),int(shelfInfo.layerinshelf))
        with open("shelfInfo.txt","w") as file_object:
            file_object.write('the calculated shelf has shelf: '+ str(int(shelfInfo.shelf)) + '& layer'+ str(int(shelfInfo.layerinshelf)) +' & shelflayerid' +  str(shelfInfo.shelflayerid))
        shelfInfojson           = json.dumps(shelfInfo.__dict__, indent=4, sort_keys=True)
        numberOfFacings         = E1WBB18['numberOfFacings']
        orientationYaw          = E1WBB18['orientationYaw']
        positionX               = E1WBB18['positionX']
        shelfLayerId            = shelfInfo.shelflayerid
        versionTimestamp        = 0
        return




def PostPlanogram(products,PRDOUCTUNITID):
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

        #Product controller
        PRODUCTID               = E1WBB01['MATNR_LONG']
        materialGroupId         = params.materialGroupId
        productType             = E1WBB02['MATKL']
        productUnit             = E1WBB03['MEINH']
        # product Unit
        denominatorBaseUnit     = E1WBB03['UMREN']
        du                      = E1WBB03['MEABM']
        dimensionUnit           = getUnitof(du)
        grossWeight             = E1WBB03['BRGEW']
        height                  = E1WBB03['HOEHE']
        productunitid           = 0
        length                  = E1WBB03['LAENG']
        maxStackSize            = int(float(E1WBB12['MABST']))
        netWeight               = E1WBB02['NTGEW']
        numeratorBaseUnit       = E1WBB03['UMREZ']
        unitCode                = 'NONE'
        volume                  = E1WBB03['VOLUM']
        vu                      = E1WBB03['VOLEH']
        volumeUnit              = getUnitof(vu)
        wu                      = E1WBB03['GEWEI']
        weightUnit              = getUnitof(wu)
        width                   = E1WBB03['BREIT']
        #Product Description
        description             = E1WBB10['MAKTM']
        isoLanguageCode         = E1WBB01['LANG_ISO']
        #material group controller
        description2            = E1WBB02['MTART']
        hierarchyLevel          = 0
        id                      = 400
        name                    = E1WBB02['ATTYP']
        parentId                = 0
        #product GTIN Controller
        if 'E1WBB04' in E1WBB03:
            gtin                = E1WBB04['EAN11']
            gtinType            = 'NONE'
            mainGtinFlag        = True
            productGTIN         = ProductGTIN(gtin, gtinType, mainGtinFlag,PRDOUCTUNITID)
            productGTINjson     = json.dumps(productGTIN.__dict__, indent=4, sort_keys=True)
            gtloads             = json.loads(productGTINjson)
        # planogram Controller
        shelfInfo = ShelfInfo()
        shelfInfo.shelf         = E1WBB18['SHELF']
        shelfInfo.layerinshelf  = E1WBB18['shelfLayerId']
        shelfInfo.shelflayerid  = ReadJSON.findid(int(shelfInfo.shelf ),int(shelfInfo.layerinshelf))
        with open("shelfInfo.txt","w") as file_object:
            file_object.write('the calculated shelf has shelf: '+ str(int(shelfInfo.shelf)) + '& layer'+ str(int(shelfInfo.layerinshelf)) +' & shelflayerid' +  str(shelfInfo.shelflayerid))
        shelfInfojson           = json.dumps(shelfInfo.__dict__, indent=4, sort_keys=True)
        numberOfFacings         = E1WBB18['numberOfFacings']
        orientationYaw          = E1WBB18['orientationYaw']
        positionX               = E1WBB18['positionX']
        shelfLayerId            = shelfInfo.shelflayerid
        versionTimestamp        = 0
        planogram               = Planogram(numberOfFacings,orientationYaw,positionX,PRDOUCTUNITID,shelfLayerId,versionTimestamp)
        planogramjson           = json.dumps(planogram.__dict__, indent=4, sort_keys=True)
        plloads                 = json.loads(planogramjson)
        retJSON                 = OperatingDT.POST_PLANOGRAM(planogramjson)
        return planogramjson
