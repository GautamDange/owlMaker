# Dr. Gautam Ravindra Dange,
# Institute of Artificial Intelligence, University of Bremen

UnitQuery = """
{
  units {
    id,
    name,
    symbol
  }
}
"""


ShelfLayerQuery = """
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



shelfquery = """
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
