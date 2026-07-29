from simulator.base.device import IoTDevice

PROFILE = {
    "metrics": {
        "vehicle_count": {
            "type": "int",
            "min": 0,
            "max": 200
        },
        "heavy_vehicle_count": {
            "type": "int",
            "min": 0,
            "max": 40
        }
    }
}


class VehicleCounter(IoTDevice):

    def __init__(self, device_id, x, y):
        super().__init__(
            device_id,
            "vehicle_counter",
            x,
            y,
            PROFILE
        )