import flask
from pymongo import MongoClient
import copy

try:
    connect = MongoClient()
    print("Connected successfully!!!")
except:
    print("Could not connect to MongoDB")

# connecting or switching to the static database
db = connect["static"]

# creating or switching to static-hotels Collection

collection = db["static-hotels"]

dict1 = {

        "id": 1,
        "hotel_id": 1001,
        "hotel_name": "Test Hotel 1",
        "address": "Some Address in Dubai",
        "facilities": [{"id": 1, "name": "AC"}, {"id": 2, "name": "NONAC"}, {"id": 3, "name": "FREEPARKING"}],
        "dateOfactive": "02-10-2002",

    }

outF=open("dataset2.json","w")
outF.write(('['+str(dict1)+',').replace("\'","\""))
outF.write("\n")
outF.close()
for i in range(0,5000):

    dictn = copy.deepcopy(dict(dict1))
    dictn.update({"id": 1+i,
                  "hotel_id": 1001+i,
                  "hotel_name": "test Hotel {}".format(1+i)})
    collection.insert_one(dictn)


