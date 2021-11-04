from flask import Flask,request,json,Response
from pymongo import MongoClient
from bson.objectid import ObjectId

class MongoAPI:
    def __init__(self):
        self.client = MongoClient("mongodb://localhost:27017/")

        database = "static"
        collection = "static-hotels"
        cursor = self.client[database]
        self.collection = cursor[collection]
        #self.data = data

    def read(self):
        documents = self.collection.find()
        output = [{item: data[item] for item in data if item != '_id'} for data in documents]
        return output

    def write(self, data):
        #log.info('Writing Data')
        new_document = data['writedata']
        response = self.collection.insert_one(new_document)
        output = {'Status': 'Successfully Inserted',
                  'Document_ID': str(response.inserted_id)}
        return output

    def retrieve(self,data):
        filt = data['finddata']
        response = list(self.collection.find(filt))
        for item in response:
            item["_id"]=str(item["_id"])

        output = response
        return output

    '''def findhotel(self,data):
        filt={'hotel_id': data}
        print(filt)
        hotel = list(self.collection.find(filt))
        print(hotel)
        output = [{item: data[item] for item in data if item != '_id'} for data in hotel]
        return output'''

    def update(self,data):
        filt = data['updatedata']['Filter']
        updated_data = {"$set": data['updatedata']['DataToBeUpdated']}
        response = self.collection.update_one(filt, updated_data)
        output = {'Status': 'Successfully Updated' if response.modified_count > 0 else "Nothing was updated."}
        return output

    def delete(self, data):
        filt = data['deletedata']
        response = self.collection.delete_one(filt)
        output = {'Status': 'Successfully Deleted' if response.deleted_count > 0 else "Document not found."}
        return output


if __name__ == '__main__':
    #mongo_obj = MongoAPI()
    #print(json.dumps(mongo_obj.findhotel(1001), sort_keys=False, indent=4))
    '''
    data = {
        "database": "Test1",
        "collection": "femy",
        "finddata" : {"hotel_id": 1010,
                      "hotel_name": "test Hotel 10"},
        "writedata" : {"hotel_id" : 1011,
                       "hotel_name" : "my hotel"},
        "updatedata" : { "Filter" : {"Document" : "femy"},
                         "DataToBeUpdated": {"Document": "femimol joseph"}
                         }
        "deletedata" : { "hotel_id" : 1011,
                        "hotel_name" : "Dubai Hotel"   }
    }'''

'''{"updatedata" : {"Filter": {"_id":"617cf065bf10a556fd0f3b98"},
                "DataToBeUpdated" : {"hotel_name":"added with objectid"}

                      }'''


    #print(json.dumps(mongo_obj.read(),sort_keys=False,indent=4))
    #print(json.dumps(mongo_obj.write(data),sort_keys=False, indent=4))
    #print(json.dumps(mongo_obj.update(), sort_keys=False, indent=4))
    #print(json.dumps(mongo_obj.delete(data), sort_keys=False, indent=4))


    #print(mongo_obj.client.list_database_names())

  