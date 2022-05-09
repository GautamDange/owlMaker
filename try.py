# Dr. Gautam Ravindra Dange,
# Institute of Artificial Intelligence, University of Bremen

from flask import Flask, jsonify, request, abort, make_response, json
import contextlib
import OpenSSL.crypto
import Dev.params as params
import tempfile
import requests
getUnitIDofProduct = """
  mutation ($input:[PRODUCTID!]!)
  {
    {
        productUnits(productId:$input)
        {
	       id
        }
    }
  }
"""

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

keystore                = params.keystore
passphrase              = params.passphrase
def POSTGRAPHwithVAR(DevSandbox, productid):
    with pfx_to_pem(keystore, passphrase) as cert:
        if (DevSandbox == "Dev"):
            url = "https://dt-api.dev.knowledge4retail.org/k4r/graphql"
        else:
            url = "https://dt-api.sandbox.knowledge4retail.org/k4r/graphql"

        productId = {'input': productid}
        jsonj = {'query': getUnitIDofProduct , 'variables': productId}
        response = requests.request("POST", url, cert=cert, headers=headers, json=jsonj )
        return (json.dumps(response.json(), indent = 2))





print POSTGRAPHwithVAR("Dev","000000000100000968")
