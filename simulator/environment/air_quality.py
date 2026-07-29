from simulator.base.device import IoTDevice


PROFILE = {

    "metrics": {

        "AQI": {

            "type": "int",

            "min": 10,

            "max": 300

        },

        "CO2": {

            "type": "int",

            "min": 350,

            "max": 900

        },

        "PM2_5": {

            "type": "float",

            "min": 5,

            "max": 90

        }

    }

}


class AirQuality(IoTDevice):

    def __init__(self, device_id, x, y):

        super().__init__(

            device_id,

            "air_quality",

            x,

            y,

            PROFILE

        )