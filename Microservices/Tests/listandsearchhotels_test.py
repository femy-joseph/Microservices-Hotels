import unittest
import requests


class TestlistandsearchhotelService(unittest.TestCase):

    url = "http://192.168.1.11:5001/"
    hotel_obj=[{
        "id": 1,
        "hotel_id": 1001,
        "hotel_name": "Test Hotel 1",
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
    }]

    def test_list_hotels(self):
        r = requests.get("{}/{}".format(TestlistandsearchhotelService.url,"hotellist"))
        self.assertEqual(r.status_code,200)
       # print(len(r.json()))
        #self.assertEqual(len(r.json()),5000)

    def test_get_a_hotel(self):
        hotelid=1001
        r=requests.get("{}/{}/{}".format(TestlistandsearchhotelService.url,"findhotel",hotelid))

        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json(),TestlistandsearchhotelService.hotel_obj)

    def test_not_found(self):

        invalid_hotelid = 110
        r = requests.get("{}/{}/{}".format(TestlistandsearchhotelService.url, "findhotel", invalid_hotelid))
        self.assertNotEqual(r.status_code, 200,
                         "Got {} but expected 200".format(
                             r.status_code))


if __name__ == "__main__":
    unittest.main()
