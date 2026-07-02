from collections import defaultdict
from typing import Callable, Any


class EventBus:
    def __init__(self):
        self.listeners = defaultdict(list)

    def subscribe(self, event_name: str, callback: Callable[[dict], None]) -> None:
        self.listeners[event_name].append(callback)

    def publish(self, event_name: str, data: dict | None = None) -> None:
        if data is None:
            data = {}

        event = {
            "name": event_name,
            "data": data,
        }

        for callback in self.listeners[event_name]:
            callback(event)