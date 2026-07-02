from src.core.event_bus import EventBus
from src.core.logger import setup_logger


class MotionCore:
    def __init__(self):
        self.logger = setup_logger()
        self.event_bus = EventBus()
        self.modules = []

    def register_module(self, module):
        self.modules.append(module)
        self.logger.info(f"Registered module: {module.name}")

    def start(self):
        self.logger.info("MotionOS Core starting...")

        for module in self.modules:
            module.start()

        self.event_bus.publish("motionos_started")

    def stop(self):
        self.logger.info("MotionOS Core stopping...")

        for module in self.modules:
            module.stop()

        self.event_bus.publish("motionos_stopped")


        class MotionModule:
    def __init__(self, name: str, event_bus):
        self.name = name
        self.event_bus = event_bus

    def start(self):
        pass

    def stop(self):
        pass