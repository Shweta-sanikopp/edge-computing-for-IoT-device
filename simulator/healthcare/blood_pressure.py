from simulator.base.device import IoTDevice


PROFILE = {

    "metrics": {

        "systolic": {

            "type": "int",

            "min": 90,

            "max": 150

        },

        "diastolic": {

            "type": "int",

            "min": 60,

            "max": 95

        }

    }

}


class BloodPressureMonitor(IoTDevice):

    def __init__(self, device_id, x, y):

        super().__init__(

            device_id,

            "blood_pressure",

            x,

            y,

            PROFILE

        )