from src.core.motion_core import MotionCore
from src.core.module import MotionModule


class TestModule(MotionModule):
    def start(self):
        print(f"{self.name} started")

    def stop(self):
        print(f"{self.name} stopped")


def on_started(event):
    print("Event received:", event)


if __name__ == "__main__":
    core = MotionCore()

    core.event_bus.subscribe("motionos_started", on_started)

    test_module = TestModule("Test Module", core.event_bus)
    core.register_module(test_module)

    core.start()
    core.stop()