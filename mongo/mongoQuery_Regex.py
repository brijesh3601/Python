import pymongo

mongoCli = pymongo.MongoClient("mongodb://localhost:27017/")
mongoDb = mongoCli["test"]
mongoColln = mongoDb["customers"]

addrQuery = { "address": "Park Lane 38" }

# starts with 'S'
startWithSQuery = { "address": { "$regex": "^S", "$options" : "i" } }

# start with 'S' or higher like S, T, U etc
startWithS_or_HigherQuery = { "address": { "$gt": "S" } }

mongoDoc = mongoColln.find(addrQuery)

for x in mongoDoc:
  print(x)

  print("## Print S or higher")
  


mongoDoc = mongoColln.find(startWithS_or_HigherQuery)
for x in mongoDoc:
  print(x)  


print("## Print starts with S ")
  

mongoDoc = mongoColln.find(startWithSQuery)
for x in mongoDoc:
  print(x)  