from flask import Flask,request,json,Response
from  from microservices.database.MongoDBAPI_user import *
#initializing flask
app = Flask(__name__)


@app.route('/')
def base():
    response="Status UP ! Hi Welcome to Static hotel Collections"
    return Response(response=json.dumps(response),
                    status=200,
                    mimetype='application/json')

@app.route('/hotellist', methods=['GET'])
def mongo_read():

    obj1 = MongoAPI()
    response = obj1.read()
    return Response(response=json.dumps(response,sort_keys=False, indent=4),
                    status=200,
                    mimetype='application/json')


@app.route('/findhotel', methods=['GET'])
def mongo_find():
    data1 = request.json
    if data1 is None or data1 == {} or 'finddata' not in data1:
        return Response(response=json.dumps({"Error": "Please provide connection information"}),
                        status=400,
                        mimetype='application/json')
    obj1 = MongoAPI()
    response = obj1.retrieve(data1)
    if response == [] or response is None:
        response = 'status : Records Not Found'
    out=response
    return Response(response=json.dumps(out,sort_keys=False, indent=4),
                    status=200,
                    mimetype='application/json')

@app.route('/findhotel/<hotelid>', methods=['GET'])
def mongo_findhotel(hotelid):
    obj1 = MongoAPI()
    data1=int(hotelid)
    hotel = list(obj1.collection.find({'hotel_id': data1}))
    if hotel!=[]:
        output = [{item: data[item] for item in data if item != '_id'} for data in hotel]
        return Response(response=json.dumps(output, sort_keys=False, indent=4),
                        status=200,
                        mimetype='application/json')


if __name__ == '__main__':
    app.run(debug=True, port=5001, host='0.0.0.0')