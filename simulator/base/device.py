from abc import ABC
from datetime import datetime
import random
import copy


class IoTDevice(ABC):

    def __init__(self, device_id, device_type, x, y, profile):

        self.device_id = device_id
        self.device_type = device_type

        self.x = x
        self.y = y

        self.profile = profile

        self.edge_node = None
        self.distance = 0

        self.status = "ACTIVE"

        self.battery = random.randint(80, 100)

        self.signal_strength = random.randint(75, 100)

        self.packet_number = 0

        self.last_packet = None

        # Behaviour probabilities

        self.invalid_probability = 0.02
        self.duplicate_probability = 0.03
        self.offline_probability = 0.01
        self.delay_probability = 0.02

    ####################################################

    def generate_metrics(self):

        metrics = {}

        for metric, rule in self.profile["metrics"].items():

            if rule["type"] == "int":

                metrics[metric] = random.randint(
                    rule["min"],
                    rule["max"]
                )

            elif rule["type"] == "float":

                metrics[metric] = round(
                    random.uniform(
                        rule["min"],
                        rule["max"]
                    ),
                    2
                )

            elif rule["type"] == "choice":

                metrics[metric] = random.choice(
                    rule["values"]
                )

        return metrics

    ####################################################

    def update_battery(self):

        drain = random.uniform(0.05, 0.30)

        self.battery = max(0, self.battery - drain)

        if self.battery <= 0:

            self.status = "OFFLINE"

        elif self.battery < 15:

            self.status = "LOW_BATTERY"

        else:

            self.status = "ACTIVE"

    ####################################################

    def update_signal(self):

        self.signal_strength += random.randint(-3, 3)

        self.signal_strength = max(
            0,
            min(100, self.signal_strength)
        )

    ####################################################

    def random_offline(self):

        if random.random() < self.offline_probability:

            self.status = "OFFLINE"

    ####################################################

    def inject_faults(self, packet):

        r = random.random()

        # Duplicate packet

        if r < self.duplicate_probability:

            if self.last_packet:

                packet = copy.deepcopy(self.last_packet)
                packet["fault"] = "DUPLICATE_PACKET"
                return packet

        # Invalid packet

        r = random.random()

        if r < self.invalid_probability:

            fault = random.choice([

                "INVALID_VALUE",

                "MISSING_FIELD",

                "WRONG_TYPE"

            ])

            packet["fault"] = fault

            if fault == "INVALID_VALUE":

                key = list(packet["metrics"].keys())[0]

                packet["metrics"][key] = -9999

            elif fault == "MISSING_FIELD":

                packet.pop("timestamp", None)

            elif fault == "WRONG_TYPE":

                key = list(packet["metrics"].keys())[0]

                packet["metrics"][key] = "INVALID"

        return packet

    ####################################################

    def create_packet(self):

        self.packet_number += 1

        self.update_battery()

        self.update_signal()

        self.random_offline()

        packet = {

            "packet_id": self.packet_number,

            "device_id": self.device_id,

            "device_type": self.device_type,

            "location": {

                "x": self.x,

                "y": self.y

            },

            "edge_node": self.edge_node,

            "distance": round(self.distance, 2),

            "battery": round(self.battery, 2),

            "signal_strength": self.signal_strength,

            "status": self.status,

            "metrics": self.generate_metrics(),

            "timestamp": datetime.utcnow().isoformat()

        }

        packet = self.inject_faults(packet)

        self.last_packet = copy.deepcopy(packet)

        return packet