import random


def generate_fake_packet():

    return {

        "packet_id": random.randint(100000,999999),

        "device_id": "UNKNOWN_" + str(random.randint(1,9999)),

        "device_type": "UNKNOWN",

        "location":{

            "x":random.randint(0,100),

            "y":random.randint(0,100)

        },

        "battery":100,

        "signal_strength":100,

        "status":"ACTIVE",

        "metrics":{

            "temperature":999

        }

    }