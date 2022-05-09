# Dr. Gautam Ravindra Dange,
# Institute of Artificial Intelligence, University of Bremen

import Dev.params as params
import os.path

fext = 0;
owlFile = "owlFile" + str(fext) + ".owl";
while (os.path.exists('./' + owlFile)):
    fext = fext + 1;
    owlFile = "owlFile" + str(fext) + ".owl";
owlFile = "owlFile" + str(fext) + ".owl";


file_object = open(owlFile, "a")

def fWrite(contents):
    ct = contents.encode('ascii', 'ignore')
    file_object.write(ct)

def fClose():
    file_object.close()

def StartingLines():
    Top = open("Top.txt",'r')
    Lines = Top.readlines()
    for line in Lines:
         fWrite(line)
    Top.close()

def ObjectProperties():
        ObjectProperties = open("ObjectProperties.txt",'r')
        Lines = ObjectProperties.readlines()
        fWrite("\n")
        for line in Lines:
             fWrite(line)
        ObjectProperties.close()

def DataProperties():
        DataProperties = open("DataProperties.txt",'r')
        Lines = DataProperties.readlines()
        fWrite("\n")
        for line in Lines:
             fWrite(line)
        DataProperties.close()

def classes():
        Classes = open("Classes.txt",'r')
        Lines = Classes.readlines()
        fWrite("\n")
        for line in Lines:
             fWrite(line)
        Classes.close()

def EndLines():
        EndLines = open("EndLines.txt",'r')
        Lines = EndLines.readlines()
        fWrite("\n")
        for line in Lines:
             fWrite(line)
        EndLines.close()

def ProductClasses():
        ProductClasses = open("ProductClasses.txt",'r')
        Lines = ProductClasses.readlines()
        fWrite("\n")
        for line in Lines:
             fWrite(line)
        ProductClasses.close()

def IndividualsLabel():
        IndividualsLabel = open("IndividualsLabel.txt",'r')
        Lines = IndividualsLabel.readlines()
        fWrite("\n")
        for line in Lines:
             fWrite(line)
        IndividualsLabel.close()


def filler(conditional,ProductId,productType,gtin, length,height,width,netWeight,_shelf,_layerinshelf,numberOfFacings,volume):
    with open("tempowl1.txt", 'a') as out:
        out.write(    "\n   <!-- http://knowrob.org/kb/shop.owl#Product_MaterialNumber_"+ProductId+ "-->")
        out.write(    "\n   <owl:Class rdf:about=\"http://knowrob.org/kb/shop.owl#Product_MaterialNumber_"+ProductId+"\">")
        out.write(    "\n    <rdfs:subClassOf rdf:resource=\"http://knowrob.org/kb/shop.owl#class_"+productType+"\"/>")

        # GTIN
        out.write(    "\n    <rdfs:subClassOf>")
        out.write(    "\n        <owl:Restriction>")
        out.write(    "\n            <owl:onProperty rdf:resource=\"http://knowrob.org/kb/shop.owl#articleNumberOfProduct\"/>")
        out.write(    "\n            <owl:hasValue rdf:resource=\"http://knowrob.org/kb/shop.owl#Product_GTIN_"+gtin+"\"/>")
        out.write(    "\n        </owl:Restriction>")
        out.write(    "\n    </rdfs:subClassOf>")

        #Mass
        out.write(    "\n    <rdfs:subClassOf>")
        out.write(    "\n        <owl:Restriction>")
        out.write(    "\n            <owl:onProperty rdf:resource=\"http://knowrob.org/kb/knowrob.owl#MassAttribute\"/>")
        out.write(    "\n            <owl:hasValue rdf:datatype=\"http://www.w3.org/2001/XMLSchema#float\">"+netWeight+"</owl:hasValue>")
        out.write(    "\n        </owl:Restriction>")
        out.write(    "\n    </rdfs:subClassOf>")

        #Length
        out.write(    "\n    <rdfs:subClassOf>")
        out.write(    "\n        <owl:Restriction>")
        out.write(    "\n            <owl:onProperty rdf:resource=\"http://knowrob.org/kb/shop.owl#depthOfProduct\"/>")
        out.write(    "\n            <owl:hasValue rdf:datatype=\"http://www.w3.org/2001/XMLSchema#float\">"+length+"</owl:hasValue>")
        out.write(    "\n        </owl:Restriction>")
        out.write(    "\n    </rdfs:subClassOf>")

        #shelf
        out.write(    "\n    <rdfs:subClassOf>")
        out.write(    "\n        <owl:Restriction>")
        out.write(    "\n            <owl:onProperty rdf:resource=\"http://knowrob.org/kb/shop.owl#erpShelfId\"/>")
        out.write(    "\n            <owl:hasValue rdf:datatype=\"http://www.w3.org/2001/XMLSchema#float\">"+_shelf+"</owl:hasValue>")
        out.write(    "\n        </owl:Restriction>")
        out.write(    "\n    </rdfs:subClassOf>")

        #_layerinshelf
        out.write(    "\n    <rdfs:subClassOf>")
        out.write(    "\n        <owl:Restriction>")
        out.write(    "\n            <owl:onProperty rdf:resource=\"http://knowrob.org/kb/shop.owl#erpShelfLayerId\"/>")
        out.write(    "\n            <owl:hasValue rdf:datatype=\"http://www.w3.org/2001/XMLSchema#float\">"+_layerinshelf+"</owl:hasValue>")
        out.write(    "\n        </owl:Restriction>")
        out.write(    "\n    </rdfs:subClassOf>")

        #height
        out.write(    "\n    <rdfs:subClassOf>")
        out.write(    "\n        <owl:Restriction>")
        out.write(    "\n            <owl:onProperty rdf:resource=\"http://knowrob.org/kb/knowrob.owl#heightOfProduct\"/>")
        out.write(    "\n            <owl:hasValue rdf:datatype=\"http://www.w3.org/2001/XMLSchema#float\">"+ height+"</owl:hasValue>")
        out.write(    "\n        </owl:Restriction>")
        out.write(    "\n    </rdfs:subClassOf>")

        #numberOfFacings
        out.write(    "\n    <rdfs:subClassOf>")
        out.write(    "\n        <owl:Restriction>")
        out.write(    "\n            <owl:onProperty rdf:resource=\"http://knowrob.org/kb/shop.owl#numberOfFacings\"/>")
        out.write(    "\n            <owl:hasValue rdf:datatype=\"http://www.w3.org/2001/XMLSchema#float\">"+numberOfFacings+"</owl:hasValue>")
        out.write(    "\n        </owl:Restriction>")
        out.write(    "\n    </rdfs:subClassOf>")

        #volume
        out.write(    "\n    <rdfs:subClassOf>")
        out.write(    "\n        <owl:Restriction>")
        out.write(    "\n            <owl:onProperty rdf:resource=\"http://knowrob.org/kb/shop.owl#volumeOfProduct\"/>")
        out.write(    "\n            <owl:hasValue rdf:datatype=\"http://www.w3.org/2001/XMLSchema#float\">"+volume+"</owl:hasValue>")
        out.write(    "\n        </owl:Restriction>")
        out.write(    "\n    </rdfs:subClassOf>")

        #width
        out.write(    "\n    <rdfs:subClassOf>")
        out.write(    "\n        <owl:Restriction>")
        out.write(    "\n            <owl:onProperty rdf:resource=\"http://knowrob.org/kb/shop.owl#widthOfProduct\"/>")
        out.write(    "\n            <owl:hasValue rdf:datatype=\"http://www.w3.org/2001/XMLSchema#float\">"+width+"</owl:hasValue>")
        out.write(    "\n        </owl:Restriction>")
        out.write(    "\n    </rdfs:subClassOf>")

        out.write(    "\n   </owl:Class>")



def Individuals(conditional,ProductId,productType,gtin, length,height,width,netWeight,_shelf,_layerinshelf,numberOfFacings,volume):
    with open("tempowl2.txt", 'a') as out:
        out.write(    "\n<!-- http://knowrob.org/kb/shop.owl#Product_GTIN_"+gtin+"\"/>-->")
        out.write(    "\n<owl:NamedIndividual rdf:about=\"http://knowrob.org/kb/shop.owl#Product_GTIN_"+gtin+"\">")
        out.write(    "\n    <rdf:type rdf:resource=\"http://knowrob.org/kb/shop.owl#ArticleNumber\"/>")
        out.write(    "\n    <shop:gtin rdf:datatype=\"http://www.w3.org/2001/XMLSchema#string\">"+gtin+"</shop:gtin>")
        out.write(    "\n</owl:NamedIndividual>")

def generateOWL(products,Operation,final):
    if(final) :
        StartingLines()
        ObjectProperties()
        DataProperties()
        classes()

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

        #Setup Params
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

        #From XML
        ProductId               = E1WBB01['MATNR_LONG']             #
        isoLanguageCode         = E1WBB01['LANG_ISO']               #
        productType             = E1WBB02['MATKL']                  #
        netWeight               = E1WBB02['NTGEW']                  #
        ExtraDescription        = E1WBB02['MTART']                  #
        name                    = E1WBB02['ATTYP']                  #
        productUnit             = E1WBB03['MEINH']                  #
        denominatorBaseUnit     = E1WBB03['UMREN']                  #
        dimensionUnit           = E1WBB03['MEABM']                  #
        weightUnit              = E1WBB03['GEWEI']                  #
        grossWeight             = E1WBB03['BRGEW']                  #
        heightt                 = (float(E1WBB03['HOEHE']))                   #
        lengthh                 = (float(E1WBB03['LAENG']))                   #
        numeratorBaseUnit       = E1WBB03['UMREZ']                  #
        volume                  = E1WBB03['VOLUM']                  #
        volumeUnit              = E1WBB03['VOLEH']                  #
        widthh                  = (float(E1WBB03['BREIT']))                  #
        description             = E1WBB10['MAKTM']                  #
        maxStackSize            = (float(E1WBB12['MABST']))      #
        _shelf                  = E1WBB18['SHELF']                  #
        _layerinshelf           = E1WBB18['shelfLayerId']           #
        numberOfFacings         = E1WBB18['numberOfFacings']        #
        orientationYaw          = E1WBB18['orientationYaw']         #
        positionX               = E1WBB18['positionX']              #
        numberOfFacings         = E1WBB18['numberOfFacings']        #

        lengthh                 = lengthh/100
        heightt                 = heightt/100
        widthh                  = widthh/100
        length                  = str(lengthh)
        height                  = str(heightt)
        width                   = str(widthh)

        conditional =  False
        if 'E1WBB04' in E1WBB03:
            conditional =  True
            gtin                = E1WBB04['EAN11']
            gtinType            = 'NONE'
            mainGtinFlag        = True
            filler      (conditional,ProductId,productType,gtin, length,height,width,netWeight,_shelf,_layerinshelf,numberOfFacings,volume)
            Individuals (conditional,ProductId,productType,gtin, length,height,width,netWeight,_shelf,_layerinshelf,numberOfFacings,volume)

    if(final) :
        tempowl1 = open("tempowl1.txt",'r')
        Lines = tempowl1.readlines()
        for line in Lines:
             fWrite(line)
        tempowl1.close()
        ProductClasses()
        IndividualsLabel()
        tempowl2 = open("tempowl2.txt",'r')
        Lines = tempowl2.readlines()
        for line in Lines:
             fWrite(line)
        tempowl2.close()
        EndLines()
        tempowl1 = open("tempowl1.txt",'w')
        tempowl2 = open("tempowl2.txt",'w')
        tempowl1.close()
        tempowl2.close()
        fClose();
