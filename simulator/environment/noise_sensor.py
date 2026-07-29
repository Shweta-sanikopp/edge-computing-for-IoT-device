from simulator.base.device import IoTDevice

PROFILE = {
    "metrics": {
        "noise_level": {
            "type": "float",
            "min": 30,
            "max": 120
        }
    }
}


class NoiseSensor(IoTDevice):

    def __init__(self, device_id, x, y):
        super().__init__(
            device_id,
            "noise_sensor",
            x,
            y,
            PROFILE
        )