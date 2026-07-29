from simulator.base.device import IoTDevice


PROFILE = {

    "metrics": {

        "fall_detected": {

            "type": "choice",

            "values": [

                True,

                False

            ]

        }

    }

}


class FallDetectionSensor(IoTDevice):

    def __init__(self, device_id, x, y):

        super().__init__(

            device_id,

            "fall_detection",

            x,

            y,

            PROFILE

        )