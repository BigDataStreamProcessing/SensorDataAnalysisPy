from dataclasses import dataclass
import json

@dataclass
class SensorDataAgg:
    sensor: str
    max_value: int
    max_timestamp: int
    min_value: int
    min_timestamp: int
    count: int
    sum: int


