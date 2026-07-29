from simulator.base.device import IoTDevice

PROFILE = {

    "metrics": {

        "vehicle_count": {

            "type": "int",

            "min": 0,

            "max": 120

        },

        "average_speed": {

            "type": "float",

            "min": 10,

            "max": 100

        },

        "congestion": {

            "type": "choice",

            "values": [

                "LOW",

                "MEDIUM",

                "HIGH"

            ]

        }

    }

}


class TrafficCamera(IoTDevice):

    def __init__(self, device_id, x, y):

        super().__init__(
            device_id,
            "traffic_camera",
            x,
            y,
            PROFILE
        )