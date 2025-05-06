from dataclasses import dataclass

@dataclass
class SensorData:
    value: int
    sensor: str
    timestamp: int