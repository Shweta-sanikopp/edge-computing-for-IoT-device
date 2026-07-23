import random
from device import IoTDevice


class TemperatureSensor(IoTDevice):

    def __init__(self, device_id):
        super().__init__(device_id, "temperature", "°C")

    def generate_value(self):
        return round(random.uniform(18, 40), 2)


class HumiditySensor(IoTDevice):

    def __init__(self, device_id):
        super().__init__(device_id, "humidity", "%")

    def generate_value(self):
        return round(random.uniform(30, 90), 2)


class PressureSensor(IoTDevice):

    def __init__(self, device_id):
        super().__init__(device_id, "pressure", "hPa")

    def generate_value(self):
        return round(random.uniform(980, 1050), 2)


class MotionSensor(IoTDevice):

    def __init__(self, device_id):
        super().__init__(device_id, "motion", "Detected")

    def generate_value(self):
        return random.choice([0, 1])


class AirQualitySensor(IoTDevice):

    def __init__(self, device_id):
        super().__init__(device_id, "air_quality", "AQI")

    def generate_value(self):
        return random.randint(0, 500)