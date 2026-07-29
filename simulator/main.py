import json

from simulator.generator import DeviceGenerator


generator = DeviceGenerator()

devices = generator.generate()


for device in devices:

    print(json.dumps(device.create_packet(), indent=4))