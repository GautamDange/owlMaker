# Dr. Gautam Ravindra Dange,
# Institute of Artificial Intelligence, University of Bremen

from OperatingDT import *

query = """
{
  stores(filter: {id: {operator: "eq", value: "36", type: "int"}})
  {
    shelves
    {
      id,
      externalReferenceId

      shelfLayers
      {
        shelfId
        level
        id
        externalReferenceId
      }
    }
  }
}
"""
print POSTGRAPHQL(query)
