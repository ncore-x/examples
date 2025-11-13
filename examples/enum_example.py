from enum import Enum


class TrafficLight(Enum):
    RED = "STOP"
    YELLOW = "WAIT"
    GREEN = "GO"


def allowed_action(traffic_light: TrafficLight) -> str:
    return traffic_light.value


print(allowed_action(TrafficLight.RED))  # Returns "STOP"
print(allowed_action(TrafficLight.YELLOW))  # Returns "WAIT"
print(allowed_action(TrafficLight.GREEN))  # Returns "GO"
