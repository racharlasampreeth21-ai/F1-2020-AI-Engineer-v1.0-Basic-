import time
from voice import speak


class RaceEngineer:

    def __init__(self):

        self.last_message = ""
        self.last_time = 0
        self.cooldown = 10  # seconds

    def say(self, message):

        now = time.time()

        if (
            message != self.last_message
            or now - self.last_time > self.cooldown
        ):

            print(f"\n📻 Engineer: {message}")

            speak(message)

            self.last_message = message
            self.last_time = now

    def analyze(self, game_state):

        """
        Automatic radio.

        ONLY IMPORTANT EVENTS BELONG HERE.

        Everything else should be asked by the driver.
        """

        # ---------------------------------------------------
        # FUTURE EVENTS
        # ---------------------------------------------------

        # Fuel Critical
        if game_state.fuel > 0 and game_state.fuel_remaining_laps < 2:
            self.say("Fuel is critical.")

        # Tyres
        elif game_state.tyre_age >= 20:
            self.say("Tyres are getting old.")

        # Future
        # elif game_state.engine_temp > ...
        # elif game_state.damage > ...
        # elif game_state.yellow_flag:
        # elif game_state.safety_car:
        # elif game_state.box_this_lap:

        # Otherwise...
        else:
            return