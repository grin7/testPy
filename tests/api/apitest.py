from api.models.booking import Booking
from api.schemas.user import valid_post_schema, valid_get_ids_schema
from api.bookingservice import BookingService


class TestApi:

    def test_create_booking(self):
        body = Booking.random()
        response = BookingService().create_booking(body=body, schema=valid_post_schema)
        assert response.status == 200
        assert isinstance(response.payload.get('bookingid'), int)

    def test_get_booking_ids(self):
        response = BookingService().get_booking_ids(schema=valid_get_ids_schema)
        assert response.status == 200
