class GameState:

    def __init__(self):

        # Car Telemetry
        self.speed = 0
        self.throttle = 0.0
        self.steer = 0.0
        self.brake = 0.0
        self.clutch = 0
        self.gear = 0
        self.rpm = 0
        self.drs = 0
        self.rev_lights = 0

        # Car Status (Future)
        self.fuel = 0.0
        self.fuel_capacity = 0.0
        self.fuel_remaining_laps = 0.0
        self.ers = 0.0
        self.tyre_compound = ""
        self.tyre_age = 0

        # Lap Data (Future)
        self.current_lap = 0
        self.position = 0
        self.lap_distance = 0.0

    def update_telemetry(self, telemetry):

        self.speed = telemetry["speed"]
        self.throttle = telemetry["throttle"]
        self.steer = telemetry["steer"]
        self.brake = telemetry["brake"]
        self.clutch = telemetry["clutch"]
        self.gear = telemetry["gear"]
        self.rpm = telemetry["rpm"]
        self.drs = telemetry["drs"]
        self.rev_lights = telemetry["rev_lights"]