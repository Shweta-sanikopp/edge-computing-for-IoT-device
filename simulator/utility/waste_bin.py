from simulator.base.device import IoTDevice

PROFILE = {
    "metrics": {
        "fill_level": {
            "type": "int",
            "min": 0,
            "max": 100
        },
        "temperature": {
            "type": "float",
            "min": 20,
            "max": 60
        }
    }
}


class WasteBinSensor(IoTDevice):

    def __init__(self, device_id, x, y):
        super().__init__(
            device_id,
            "waste_bin",
            x,
            y,
            PROFILE
        )