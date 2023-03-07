from faker import Faker

fake = Faker()


class Booking:
    @staticmethod
    def random():
        # username = fake.email()
        # password = fake.password()
        # return {"username": username, "password": password}
        return {
            "firstname": "Jim",
            "lastname": "Brown",
            "totalprice": 111,
            "depositpaid": "true",
            "bookingdates": {
                "checkin": "2018-01-01",
                "checkout": "2019-01-01"
            },
            "additionalneeds": "Breakfast"
        }


class ResponseModel:
    def __init__(self, status: int, payload: dict = None):
        self.status = status
        self.payload = payload
