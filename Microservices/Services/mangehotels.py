from flask import Flask,request,json,Response
from microservices.database.MongoDBAPI_manage import *


#initializing flask
app = Flask(__name__)


@app.route('/')
def base():
    response=" Manage Hotels Section :  Hi Welcome to Static hotel Collections "
    return Response(response=json.dumps(response),
                    status=200,
                    mimetype='application/json')

@app.route('/createhotel', methods=['POST'])
def mongo_write():
    data1 = request.json
    if data1 is None or data1 == {} or 'writedata' not in data1:
        return Response(response=json.dumps({"Error": "Please provide connection information"}),
                        status=400,
                        mimetype='application/json')
    obj1 = MongoAPI()
    response = obj1.write(data1)
    return Response(response=json.dumps(response),
                    status=200,
                    mimetype='application/json')

@app.route('/updatehotel', methods=['PUT'])
def mongo_update():
    data1 = request.json
    if data1 is None or data1 == {} or 'updatedata' not in data1:
        return Response(response=json.dumps({"Error": "Please provide connection information"}),
                        status=400,
                        mimetype='application/json')
    obj1 = MongoAPI()
    response = obj1.update(data1)
    return Response(response=json.dumps(response),
                    status=200,
                    mimetype='application/json')

@app.route('/deletehotel', methods=['DELETE'])
def mongo_delete():
    data1 = request.json
    if data1 is None or data1 == {} or 'deletedata' not in data1:
        return Response(response=json.dumps({"Error": "Please provide connection information"}),
                        status=400,
                        mimetype='application/json')
    obj1 = MongoAPI()
    response = obj1.delete(data1)
    return Response(response=json.dumps(response),
                    status=200,
                    mimetype='application/json')

@app.route('/deletehotel/<hotelid>', methods=['DELETE'])
def mongo_deletehotel(hotelid):
    obj1 = MongoAPI()
    data1=int(hotelid)
    filt = {'hotel_id': data1}
    print(filt)
    response = obj1.collection.delete_one(filt)
    output = {'Status': 'Successfully Deleted' if response.deleted_count > 0 else "Document not found."}
    #output = [{item: data[item] for item in data if item != '_id'} for data in hotel]
    return Response(response=json.dumps(output, sort_keys=False, indent=4),
                    status=200,
                    mimetype='application/json')



if __name__ == '__main__':
    app.run(debug=True, port=5002, host='0.0.0.0')