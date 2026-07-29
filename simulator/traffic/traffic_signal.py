from simulator.base.device import IoTDevice

PROFILE = {
    "metrics": {
        "signal": {
            "type": "choice",
            "values": [
                "RED",
                "GREEN",
                "YELLOW"
            ]
        },
        "waiting_time": {
            "type": "int",
            "min": 5,
            "max": 120
        }
    }
}


class TrafficSignal(IoTDevice):

    def __init__(self, device_id, x, y):
        super().__init__(
            device_id,
            "traffic_signal",
            x,
            y,
            PROFILE
        )