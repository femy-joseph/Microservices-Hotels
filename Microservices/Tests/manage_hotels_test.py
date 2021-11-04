import unittest
import requests


class TestMangehotelService(unittest.TestCase):

    url = "http://192.168.1.11:5002/"
    new_hotel_obj={"writedata" :{
        "id": 1,
        "hotel_id": 5001,
        "hotel_name": "Test Hotel 5001",
        "address": "Some Address in Dubai",
        "facilities": [
            {
                "id": 1,
                "name": "AC"
            },
            {
                "id": 2,
                "name": "NONAC"
            },
            {
                "id": 3,
                "name": "FREEPARKING"
            }
        ],
        "dateOfactive": "02-10-2002"
    }}

    def test_add_new_hotel(self):
        r = requests.post("{}/{}".format(TestMangehotelService.url,"createhotel"),json=TestMangehotelService.new_hotel_obj)
        self.assertEqual(r.status_code,200)

    def test_update_a_hotel(self):
        update_data={"updatedata" : { "Filter" : { "hotel_id": 5001,},
                         "DataToBeUpdated": {"address": "Some Address in Egypt"}
                         }}
        r=requests.put("{}/{}".format(TestMangehotelService.url,"updatehotel"),json=update_data)

        self.assertEqual(r.status_code, 200)

    def test_delete_a_hotel(self):
        delete_data = {"deletedata": {"hotel_id": 5001 }
                                      }
        r = requests.delete("{}/{}".format(TestMangehotelService.url, "deletehotel"), json=delete_data)

        self.assertEqual(r.status_code, 200)




if __name__ == "__main__":
    unittest.main()