from simulator.base.device import IoTDevice


PROFILE = {

    "metrics": {

        "spo2": {

            "type": "int",

            "min": 90,

            "max": 100

        }

    }

}


class SpO2Monitor(IoTDevice):

    def __init__(self, device_id, x, y):

        super().__init__(

            device_id,

            "spo2",

            x,

            y,

            PROFILE

        )