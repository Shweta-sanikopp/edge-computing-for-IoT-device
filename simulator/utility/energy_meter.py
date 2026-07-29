from simulator.base.device import IoTDevice

PROFILE = {
    "metrics": {
        "power_usage": {
            "type": "float",
            "min": 0,
            "max": 500
        },
        "voltage": {
            "type": "float",
            "min": 210,
            "max": 240
        }
    }
}


class EnergyMeter(IoTDevice):

    def __init__(self, device_id, x, y):
        super().__init__(
            device_id,
            "energy_meter",
            x,
            y,
            PROFILE
        )