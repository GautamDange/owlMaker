# Dr. Gautam Ravindra Dange,
# Institute of Artificial Intelligence, University of Bremen

bitwiseProduct      = 1
bitwiseProductDesc  = 2
bitwiseProductUnit  = 4
bitwiseProductGtin  = 8
bitwisePlanogram    = 16

This = 3
if This & bitwiseProduct:
    print "bitwiseProduct"
if This & bitwiseProductDesc:
    print "bitwiseProductDesc"
if This & bitwiseProductUnit:
    print "bitwiseProductUnit"
if This & bitwiseProductGtin:
    print "bitwiseProductGtin"
if This & bitwisePlanogram:
    print "bitwisePlanogram"
