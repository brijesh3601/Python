import pymongo

mongoCli = pymongo.MongoClient("mongodb://localhost:27017/")
mongoDb = mongoCli["test"]
mongoColln = mongoDb["customers"]

# "name": 1, "address": 1  => interpret as show name & address if value is '1' or hide if '0'
for x in mongoColln.find({},{ "_id": 0, "name": 1, "address": 1 }):
  #print(x)

 # "address": 0  will hide addr column
 for x in mongoColln.find({},{ "address": 0 }):
  print(x) 