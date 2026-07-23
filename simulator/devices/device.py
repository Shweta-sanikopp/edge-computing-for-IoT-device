from abc import ABC, abstractmethod
from datetime import datetime


class IoTDevice(ABC):
    """
    Base class for every virtual IoT device.
    """

    def __init__(self, device_id, device_type, unit):
        self.device_id = device_id
        self.device_type = device_type
        self.unit = unit

    @abstractmethod
    def generate_value(self):
        pass

    def generate_data(self):
        return {
            "device_id": self.device_id,
            "device_type": self.device_type,
            "value": self.generate_value(),
            "unit": self.unit,
            "timestamp": datetime.now().isoformat(timespec="seconds")
        }