from simulator.base.device import IoTDevice


PROFILE = {

    "metrics": {

        "heart_rate": {

            "type": "int",

            "min": 55,

            "max": 120

        },

        "rhythm": {

            "type": "choice",

            "values": [

                "NORMAL",

                "PVC",

                "AFIB"

            ]

        },

        "voltage": {

            "type": "float",

            "min": 0.7,

            "max": 1.4

        }

    }

}


class ECGMonitor(IoTDevice):

    def __init__(self, device_id, x, y):

        super().__init__(

            device_id,

            "ecg",

            x,

            y,

            PROFILE

        )