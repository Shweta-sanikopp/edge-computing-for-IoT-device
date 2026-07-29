import random

def generate_fake_device():

    return {

        "packet_id": random.randint(100000,999999),

        "device_id": "UNKNOWN_" + str(random.randint(1,999)),

        "device_type": "malicious",

        "location":{

            "x":random.randint(0,100),

            "y":random.randint(0,100)

        },

        "metrics":{

            "fake":999

        }

    }