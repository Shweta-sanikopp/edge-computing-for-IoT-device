import json
import time

from sensors import (
    TemperatureSensor,
    HumiditySensor,
    PressureSensor,
    MotionSensor,
    AirQualitySensor
)

devices = []

# 10 Temperature Sensors
for i in range(1, 11):
    devices.append(TemperatureSensor(f"TEMP{i:03d}"))

# 10 Humidity Sensors
for i in range(1, 11):
    devices.append(HumiditySensor(f"HUM{i:03d}"))

# 10 Pressure Sensors
for i in range(1, 11):
    devices.append(PressureSensor(f"PRESS{i:03d}"))

# 10 Motion Sensors
for i in range(1, 11):
    devices.append(MotionSensor(f"MOTION{i:03d}"))

# 10 Air Quality Sensors
for i in range(1, 11):
    devices.append(AirQualitySensor(f"AIR{i:03d}"))

print(f"Total Devices Created: {len(devices)}")

print("-" * 50)

while True:

    for device in devices:

        data = device.generate_data()

        print(json.dumps(data, indent=4))

    print("=" * 80)

    time.sleep(2)