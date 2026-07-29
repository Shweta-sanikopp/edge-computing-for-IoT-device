# ==============================
# Smart City Simulator Config
# ==============================

CITY_WIDTH = 100
CITY_HEIGHT = 100

# Edge Nodes
NUMBER_OF_EDGE_NODES = 5

# Streaming
STREAM_INTERVAL = 2      # seconds

# Packet Behaviour
INVALID_PACKET_RATE = 0.02
DUPLICATE_PACKET_RATE = 0.03
OFFLINE_DEVICE_RATE = 0.01
DELAY_PACKET_RATE = 0.02

# Initial Battery
BATTERY_MIN = 80
BATTERY_MAX = 100

# Signal Strength
SIGNAL_MIN = 75
SIGNAL_MAX = 100

# Device Counts

DEVICE_COUNTS = {

    # Environment
    "weather_station": 5,
    "air_quality": 5,
    "noise_sensor": 5,

    # Healthcare
    "heart_rate": 5,
    "blood_pressure": 5,
    "spo2": 5,
    "body_temperature": 5,
    "ecg": 5,
    "fall_detection": 5,

    # Traffic
    "traffic_camera": 5,
    "vehicle_counter": 5,
    "parking_sensor": 5,
    "traffic_signal": 5,

    # Utility
    "street_light": 5,
    "energy_meter": 5,
    "water_level": 5,
    "waste_bin": 5

}