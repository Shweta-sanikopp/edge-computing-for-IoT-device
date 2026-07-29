from simulator.base.device import IoTDevice

PROFILE = {
    "metrics": {
        "water_level": {
            "type": "float",
            "min": 0,
            "max": 100
        },
        "flow_rate": {
            "type": "float",
            "min": 0,
            "max": 50
        }
    }
}


class WaterLevelSensor(IoTDevice):

    def __init__(self, device_id, x, y):
        super().__init__(
            device_id,
            "water_level",
            x,
            y,
            PROFILE
        )