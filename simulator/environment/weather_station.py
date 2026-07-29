from simulator.base.device import IoTDevice


PROFILE = {

    "metrics": {

        "temperature": {

            "type": "float",

            "min": 18,

            "max": 40

        },

        "humidity": {

            "type": "float",

            "min": 30,

            "max": 90

        },

        "pressure": {

            "type": "float",

            "min": 980,

            "max": 1045

        },

        "wind_speed": {

            "type": "float",

            "min": 0,

            "max": 20

        }

    }

}


class WeatherStation(IoTDevice):

    def __init__(self, device_id, x, y):

        super().__init__(

            device_id,

            "weather_station",

            x,

            y,

            PROFILE

        )