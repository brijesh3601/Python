import pymongo

# make use locally mongodb is running else you will get pymongo.errors.ServerSelectionTimeoutError:: Connection refused
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["test"]

collist = mydb.list_collection_names()

# this will print all schema in 'test' collection
print(collist)


# this will print if 'books' schema exists
if "books" in collist:
  print("The collection exists.")
