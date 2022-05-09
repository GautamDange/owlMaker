# Dr. Gautam Ravindra Dange,
# Institute of Artificial Intelligence, University of Bremen

import contextlib
import OpenSSL.crypto
import os
import requests
import ssl
import tempfile
import json
import Dev.params as params


@contextlib.contextmanager
def pfx_to_pem(pfx_path, pfx_password):
    with tempfile.NamedTemporaryFile(suffix='.pem') as t_pem:
        f_pem = open(t_pem.name, 'wb')
        pfx = open(pfx_path, 'rb').read()
        p12 = OpenSSL.crypto.load_pkcs12(pfx, pfx_password)
        f_pem.write(OpenSSL.crypto.dump_privatekey(OpenSSL.crypto.FILETYPE_PEM, p12.get_privatekey()))
        f_pem.write(OpenSSL.crypto.dump_certificate(OpenSSL.crypto.FILETYPE_PEM, p12.get_certificate()))
        ca = p12.get_ca_certificates()
        if ca is not None:
            for cert in ca:
                f_pem.write(OpenSSL.crypto.dump_certificate(OpenSSL.crypto.FILETYPE_PEM, cert))
        f_pem.close()
        yield t_pem.name

headers = {
  'Content-Type': 'application/json'
}

headers = {
  'Content-Type': 'application/json'
}

#URLS
urlproduct              = params.urlproduct
urlproductUnits         = params.urlproductUnits
urlproductDescription   = params.urlproductDescription
urlproductGTIN          = params.urlproductGTIN
urlplanogram            = params.urlplanogram
keystore                = params.keystore
passphrase              = params.passphrase

#OPERATIONS


def POSTGRAPHQL(query,DevSandbox):
    with pfx_to_pem(keystore, passphrase) as cert:
        url = params.urlGraphql
        response = requests.request("POST", url, cert=cert, headers=headers, json={"query": query})
        return (json.dumps(response.json(), indent = 2))


def POST(jsonn, url):
    with pfx_to_pem(keystore, passphrase) as cert:
        print ("**  POST JSON *** ")
        print jsonn
        response = requests.request("POST", url, cert=cert, headers=headers, data=jsonn)
        print ("*** RESPONSE OF SERVER ***")
        print response.json()
        return response.json()

def GET(id,url):
    if id ==0 :
        with pfx_to_pem(keystore, passphrase) as cert:
            response = requests.request("GET", url, cert=cert, headers=headers)
            jsonRES = json.loads(response.text)
            return jsonRES
    else:
        urlg = str(url) + str('/')+ str(id)
        with pfx_to_pem(keystore, passphrase) as cert:
            response = requests.request("GET", urlg, cert=cert, headers=headers)
            jsonRES = json.loads(response.text)
            return jsonRES



def DELETE(id, url):
    if id == 0:
        jsonlist = GET(0,url)
        print jsonlist
        if bool(jsonlist):
            for i in jsonlist:
                DELETE (i['id'],url)
    else:
        with pfx_to_pem(keystore, passphrase) as cert:
            urld = str(url) + str('/')+ str(id)
            response = requests.request("DELETE", urld, cert=cert, headers=headers)
            return response

def PUT(id, json, url):
    if id == 0:
        return 0
    with pfx_to_pem(keystore, passphrase) as cert:
        urlp = str(url) + str('/')+ str(id)
        response = requests.request("PUT", urlp, cert=cert, headers=headers,data=json )
        jsonRES = json.loads(response.text)
        return jsonRES

#OPERATIONS
def POST_PRODUCT(productObj):
    return POST(productObj,urlproduct)

def GET_PRODUCT(productid):
    return GET(productid,urlproduct)

def GET_PRODUCTS():
    return GET(0,urlproduct)

def DELETE_PRODUCT(productid):
    return DELETE(productid,urlproduct)

def DELETE_PRODUCTS():
    return DELETE(0,urlproduct)

def PUT_PRODUCT(productid, productObj):
    return PUT(productid,productObj,urlproduct)

#OPERATIONS
def POST_PRODUCTDESC(productDescObj):
    return POST(productDescObj,urlproductDescription)

def GET_PRODUCTDESC(productDescid):
    return GET(productDescid,urlproductDescription)

def GET_PRODUCTSDESCS():
    return GET(0,urlproductDescription)

def DELETE_PRODUCTDESC(productDescid):
    return DELETE(productDescid,urlproductDescription)

def DELETE_PRODUCTDESCS():
    return DELETE(0,urlproductDescription)

def PUT_PRODUCTDESC(productDescid,productDescIObj):
    return PUT(productDescid,productDescIObj,urlproductDescription)

#OPERATIONS
def POST_PRODUCT_GTIN(prodctGTINObj):
    return POST(prodctGTINObj,urlproductGTIN)

def GET_PRODUCT_GTIN(productGTINid):
    return GET(productGTINid,urlproductGTIN)

def GET_PRODUCTS_GTINS():
    return GET(0,urlproductGTIN)

def DELETE_PRODUCT_GTIN(productGTINid):
    return DELETE(productGTINid,urlproductGTIN)

def DELETE_PRODUCT_GTINS():
    return DELETE(0,urlproductGTIN)

def PUT_PRODUCT_GTIN(productGTINid,prodctGTINObj):
    return PUT(productGTINid,prodctGTINObj,urlproductGTIN)

#OPERATIONS
def POST_PRODUCT_UNIT(productUnitObj):
    return POST(productUnitObj,urlproductUnits)

def GET_PRODUCT_UNIT(productUnitid):
    return GET(productUnitid,urlproductUnits)

def GET_PRODUCT_UNITS():
    return GET(0,urlproductUnits)

def DELETE_PRODUCT_UNIT(productUnitid):
    return DELETE(productUnitid,urlproductUnits)

def DELETE_PRODUCT_UNITS():
    return DELETE(0,urlproductUnits)

def PUT_PRODUCT_UNIT(productUnitid,productUnitObj):
    return PUT(productUnitid,productUnitObj,urlproductUnits)

#OPERATIONS
def POST_PLANOGRAM(planogramObj):
    return POST(planogramObj,urlplanogram)

def GET_PLANOGRAM(planogramid):
    return GET(planogramid,urlplanogram)

def GET_PLANOGRAMS():
    return GET(0,urlplanogram)

def DELETE_PLANOGRAM(planogramid):
    return DELETE(planogramid,urlplanogram)

def DELETE_PLANOGRAMS():
    return DELETE(0,urlplanogram)

def PUT_PLANOGRAM(planogramid,planogramObj):
    return PUT(planogramid,planogramObj,urlplanogram)
