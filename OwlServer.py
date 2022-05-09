# Dr. Gautam Ravindra Dange,
# Institute of Artificial Intelligence, University of Bremen

from flask import Flask, jsonify, request, abort, make_response, json
from lxml import etree
from collections import namedtuple
import os.path

import Dev.params as params
import preprocessXml as preprocessXml
import Script as Script
#import ConvertToOwl as cowl
app = Flask(__name__)

class ProductGroup:
    pass

class ShelfInfo:
    pass

idocArray=[]

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.route('/uploadidoc', methods=['POST'])
def uploadidoc():
    print "request received"
    file_object = open('ShelfLayerDebug.txt', 'a')
    products = preprocessXml.processXML(request.data)
    POSTDATA = True;
    productjson       =   Script.generateOWL(products,15,False)
    return jsonify(products)
    #return "done"

@app.route('/uploadidocfinal', methods=['POST'])
def uploadidocFinal():
    print "request received"
    file_object = open('ShelfLayerDebug.txt', 'a')
    products = preprocessXml.processXML(request.data)
    POSTDATA = True;
    productjson       =   Script.generateOWL(products,15,True)
    return jsonify(products)
    #return "done"

@app.route('/closefile', methods=['POST'])
def closefile():
    productjson       =   Script.closefile()
    return "file closed"

@app.route('/openfile', methods=['POST'])
def openfile():
    productjson       =   Script.closefile()
    return "file closed"

if __name__ == '__main__':
    app.run(debug=True, port=5678)
