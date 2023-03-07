from jsonschema.validators import validate
import logging

from api.commonservice import Client
from api.models.booking import ResponseModel

logger = logging.getLogger("api")


class BookingService:
    def __init__(self):
        self.client = Client()

    BASE_URL = 'https://restful-booker.herokuapp.com/'
    BOOKING = 'booking'

    def create_booking(self, body: dict, schema: dict):
        response = self.client.custom_request("POST", f"{self.BASE_URL}{self.BOOKING}", json=body)
        validate(instance=response.json(), schema=schema)
        logger.info(response.text)
        return ResponseModel(status=response.status_code, payload=response.json())

    def get_booking_ids(self, schema: dict):
        response = self.client.custom_request("GET", f"{self.BASE_URL}{self.BOOKING}")
        validate(instance=response.json(), schema=schema)
        logger.info(response.text)
        return ResponseModel(status=response.status_code, payload=response.json())
