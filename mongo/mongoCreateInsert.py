import pymongo

mongoCli = pymongo.MongoClient("mongodb://localhost:27017/")
mongoDb = mongoCli["test"]
mongoColln = mongoDb["customers"]

singRecord = { "name": "John", "address": "Highway 37" }

# insert ONE
x = mongoColln.insert_one(singRecord)


multiRecords = [
  { "name": "Amy", "address": "Apple st 652"},
  { "name": "Hannah", "address": "Mountain 21"},
  { "name": "Michael", "address": "Valley 345"},
  { "name": "Sandy", "address": "Ocean blvd 2"},
  { "name": "Betty", "address": "Green Grass 1"},
  { "name": "Richard", "address": "Sky st 331"},
  { "name": "Susan", "address": "One way 98"},
  { "name": "Ben", "address": "Park Lane 38"},
  { "name": "William", "address": "Central st 954"},
  { "name": "Chuck", "address": "Main Road 989"},
  { "name": "Viola", "address": "sideway 1633"}
]

x = mongoColln.insert_many(multiRecords)

#print list of the _id values of the inserted documents:
print(x.inserted_ids)