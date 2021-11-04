import pandas as pd
import json
from pymongo import MongoClient
import psycopg2



if __name__ == '__main__':
    
    try:
        connect = MongoClient()
        print("Connected successfully!!!")
    except:
        print("Could not connect to MongoDB")

    # connecting or switching to the database staticm
    db = connect["static"]
    # creating or switching to static-hotels Collection
    collection = db["static-hotels"]
    #export the data from static collection to json
    mongodata = collection.find()
    modata = list(mongodata)
    for item in modata:
        item["_id"] = str(item["_id"])
    with open('mongodata.json', 'w',encoding='utf-8') as outfile:
        json.dump(modata,outfile,indent=4)
    print("mongodb data downloaded succesfully in mongodata.json")
    # to normalise the json file into csv after flattening

    with open(r"mongodata.json", "r") as f:
        data = json.loads(f.read())
        df = pd.json_normalize(data, 'facilities', ['id', 'hotel_id', 'hotel_name', 'address', 'dateOfactive'],
                               record_prefix='facilities_')
        df = df[['id', 'hotel_id', 'hotel_name', 'address', 'facilities_id', 'facilities_name', 'dateOfactive']]
        df.to_csv("statichotels_normalised.csv", index=False)
        print("mongodata.json normalized to statichotels_normalised.csv ")


# to copy the normalized data to postgresql
    conn = psycopg2.connect("host='localhost' port='5432' dbname='static' user='postgres' password='password'")
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS "static-hotels_users" (id INTEGER ,
   hotel_id NUMERIC NOT NULL,
   hotel_name VARCHAR NOT NULL,
   address VARCHAR NOT NULL,
   facilities_id VARCHAR NOT NULL,
   facilities_name VARCHAR NOT NULL,
   dateOfactive VARCHAR  NOT NULL
   )""")
    with  open(r'statichotels_normalised.csv', 'r') as f:
        next(f) #to skip the header
        cur.copy_from(f, 'static-hotels_users', sep=',')
    conn.commit()
    print("successfully migrated to postgresql ")







    #transfer data to postgresql

















