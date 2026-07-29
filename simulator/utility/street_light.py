from simulator.base.device import IoTDevice

PROFILE = {

    "metrics": {

        "brightness": {

            "type": "int",

            "min": 0,

            "max": 100

        },

        "power_consumption": {

            "type": "float",

            "min": 20,

            "max": 150

        },

        "status": {

            "type": "choice",

            "values": [

                "ON",

                "OFF",

                "DIM"

            ]

        }

    }

}


class StreetLight(IoTDevice):

    def __init__(self, device_id, x, y):

        super().__init__(
            device_id,
            "street_light",
            x,
            y,
            PROFILE
        )