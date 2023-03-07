valid_post_schema = {
    "bookingid": "int",
    "booking": {
        "firstname": "string",
        "lastname": "string",
        "totalprice": "int",
        "depositpaid": "boolean",
        "bookingdates": {
            "checkin": "string",
            "checkout": "string"
        },
        "additionalneeds": "string"
    }
}

valid_get_ids_schema = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "array",
    "maxItems": 10000,
    "items": [
        {
            "type": "object",
            "properties": {
                "bookingid": {
                    "type": "integer"
                }
            },
            "required": [
                "bookingid"
            ]
        }
    ]
}
