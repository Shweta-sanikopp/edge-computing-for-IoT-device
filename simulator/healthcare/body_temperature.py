from simulator.base.device import IoTDevice


PROFILE = {

    "metrics": {

        "body_temperature": {

            "type": "float",

            "min": 35.5,

            "max": 39.5

        }

    }

}


class BodyTemperatureMonitor(IoTDevice):

    def __init__(self, device_id, x, y):

        super().__init__(

            device_id,

            "body_temperature",

            x,

            y,

            PROFILE

        )