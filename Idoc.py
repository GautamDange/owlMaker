# Dr. Gautam Ravindra Dange,
# Institute of Artificial Intelligence, University of Bremen

from flask import json
class Idoc:
    def __init__(self, productjson, productUnitjson, pDescriptionjson, productGTINjson, planogramjson, shelfInfojson):
        self.product                = json.loads(productjson)
        self.productUnit            = json.loads(productUnitjson)
        self.productDescription     = json.loads(pDescriptionjson)
        self.productGTIN            = json.loads(productGTINjson)
        self.planogram              = json.loads(planogramjson)
        self.shelfInfo              = json.loads(shelfInfojson)
