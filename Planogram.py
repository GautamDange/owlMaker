# Dr. Gautam Ravindra Dange,
# Institute of Artificial Intelligence, University of Bremen

class Planogram:
    def __init__(self, numberOfFacings, orientationYaw, positionX, productUnitId,shelfLayerId,versionTimestamp):
        self.numberOfFacings    = numberOfFacings
        self.orientationYaw     = orientationYaw
        self.positionX          = positionX
        self.productUnitId      = productUnitId
        self.shelfLayerId       = shelfLayerId
        self.versionTimestamp   = versionTimestamp
