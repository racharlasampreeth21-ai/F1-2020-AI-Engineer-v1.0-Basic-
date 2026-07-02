from collections import deque

class TelemetryMemory:
    def __init__(self, size=300):
        self.history = deque(maxlen=size)

    def add(self, telemetry):
        self.history.append(telemetry)

    def latest(self):
        if self.history:
            return self.history[-1]
        return None

    def previous(self):
        if len(self.history) >= 2:
            return self.history[-2]
        return None