# Dr. Gautam Ravindra Dange,
# Institute of Artificial Intelligence, University of Bremen

from flask import Flask, jsonify, request, abort, make_response, json
from lxml import etree
from collections import namedtuple
import os.path


def processXML(xmldata):
    fext = 0;
    idocdata = "idocdata" + str(fext) + ".xml";
    while (os.path.exists('./' + idocdata)):
        fext = fext + 1;
        idocdata = "idocdata" + str(fext) + ".xml";
    idocdata = "idocdata" + str(fext) + ".xml";

    with open(idocdata, 'w') as f:
            f.write(xmldata)

    tree        = etree.parse(idocdata)
    xslt_root   = etree.parse("xslt-oct.xsl")
    transform   = etree.XSLT(xslt_root)
    result      = transform(tree)
    json_load   = json.loads(str(result))
    json_dump   = json.dumps(json_load, indent=2)

    with open("parseData.json", 'w') as f:
        f.write(json_dump)

    jfext = 0;
    jidocdata = "jidocdata" + str(jfext) + ".json";
    while (os.path.exists('./' + jidocdata)):
        jfext = jfext + 1;
        jidocdata = "jidocdata" +str(jfext) + ".json";
    jidocdata = "jidocdata" + str(jfext) + ".json";



    with open(jidocdata, 'w') as f:
        f.write(json_dump)

    return json_load['products']

print "working"
