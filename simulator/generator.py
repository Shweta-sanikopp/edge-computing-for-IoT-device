import random

from simulator.base.device_factory import DeviceFactory
from simulator.base.assignment import assign_nearest_edge
from simulator.base.topology import EDGE_NODES


class DeviceGenerator:

    def __init__(self):

        self.devices = []

    def create_device(self, device_type, prefix, count, center_x, center_y):

        for i in range(count):

            x = random.randint(center_x - 10, center_x + 10)

            y = random.randint(center_y - 10, center_y + 10)

            device = DeviceFactory.create(

                device_type,

                f"{prefix}{i+1:03}",

                x,

                y

            )

            assign_nearest_edge(device, EDGE_NODES)

            self.devices.append(device)

    def generate(self):

        # Healthcare

        self.create_device("heart_rate", "HR", 5, 20, 20)
        self.create_device("blood_pressure", "BP", 5, 20, 20)
        self.create_device("spo2", "SP", 5, 20, 20)
        self.create_device("body_temperature", "BT", 5, 20, 20)
        self.create_device("ecg", "ECG", 5, 20, 20)
        self.create_device("fall_detection", "FD", 5, 20, 20)

        # Environment

        self.create_device("weather_station", "WS", 5, 50, 50)
        self.create_device("air_quality", "AQ", 5, 80, 80)

        # Traffic

        self.create_device("traffic_camera", "TC", 5, 80, 20)

        # Utility

        self.create_device("street_light", "SL", 5, 20, 80)

        return self.devices