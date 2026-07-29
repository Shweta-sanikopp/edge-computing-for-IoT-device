from simulator.base.device import IoTDevice


PROFILE = {

    "metrics": {

        "heart_rate": {

            "type": "int",

            "min": 60,

            "max": 110

        }

    }

}


class HeartRateMonitor(IoTDevice):

    def __init__(self, device_id, x, y):

        super().__init__(

            device_id,

            "heart_rate",

            x,

            y,

            PROFILE

        )