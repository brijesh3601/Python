import pymongo

mongoCli = pymongo.MongoClient("mongodb://localhost:27017/")
mongoDb = mongoCli["test"]
mongoColln = mongoDb["customers"]

# -1 = desc , 1 = ascend
mongoDoc = mongoColln.find().sort("name", 1)

for x in mongoDoc:
  print(x)