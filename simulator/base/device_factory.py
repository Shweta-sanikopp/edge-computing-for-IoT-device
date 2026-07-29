from simulator.environment.weather_station import WeatherStation
from simulator.environment.air_quality import AirQuality
from simulator.environment.noise_sensor import NoiseSensor

from simulator.healthcare.heart_rate import HeartRateMonitor
from simulator.healthcare.blood_pressure import BloodPressureMonitor
from simulator.healthcare.spo2 import SpO2Monitor
from simulator.healthcare.body_temperature import BodyTemperatureMonitor
from simulator.healthcare.ecg import ECGMonitor
from simulator.healthcare.fall_detection import FallDetectionSensor

from simulator.traffic.traffic_camera import TrafficCamera
from simulator.traffic.vehicle_counter import VehicleCounter
from simulator.traffic.parking_sensor import ParkingSensor
from simulator.traffic.traffic_signal import TrafficSignal

from simulator.utility.street_light import StreetLight
from simulator.utility.energy_meter import EnergyMeter
from simulator.utility.water_level import WaterLevelSensor
from simulator.utility.waste_bin import WasteBinSensor


class DeviceFactory:

    @staticmethod
    def create(device_type, device_id, x, y):

        devices = {

            # Environment
            "weather_station": WeatherStation,
            "air_quality": AirQuality,
            "noise_sensor": NoiseSensor,

            # Healthcare
            "heart_rate": HeartRateMonitor,
            "blood_pressure": BloodPressureMonitor,
            "spo2": SpO2Monitor,
            "body_temperature": BodyTemperatureMonitor,
            "ecg": ECGMonitor,
            "fall_detection": FallDetectionSensor,

            # Traffic
            "traffic_camera": TrafficCamera,
            "vehicle_counter": VehicleCounter,
            "parking_sensor": ParkingSensor,
            "traffic_signal": TrafficSignal,

            # Utility
            "street_light": StreetLight,
            "energy_meter": EnergyMeter,
            "water_level": WaterLevelSensor,
            "waste_bin": WasteBinSensor

        }

        if device_type not in devices:
            raise ValueError(f"Unknown device type: {device_type}")

        return devices[device_type](device_id, x, y)