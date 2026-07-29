from simulator.base.device import IoTDevice

PROFILE = {
    "metrics": {
        "occupied_slots": {
            "type": "int",
            "min": 0,
            "max": 100
        },
        "available_slots": {
            "type": "int",
            "min": 0,
            "max": 100
        }
    }
}


class ParkingSensor(IoTDevice):

    def __init__(self, device_id, x, y):
        super().__init__(
            device_id,
            "parking_sensor",
            x,
            y,
            PROFILE
        )