from dataclasses import dataclass, asdict
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

    def to_json(self) -> str:
        return json.dumps(asdict(self))
