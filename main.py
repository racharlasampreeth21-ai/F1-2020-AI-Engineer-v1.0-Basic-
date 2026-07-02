import sys
import threading

from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QTimer

from telemetry import receive_packet
from parser import get_packet_id
from decoder import decode

from overlay import Overlay

from engineer import RaceEngineer
from memory import TelemetryMemory
from game_state import GameState

from radio_thread import radio_loop


def telemetry_loop(game_state, engineer, memory):

    while True:

        packet = receive_packet()

        packet_id = get_packet_id(packet)

        data = decode(packet)

        if data is None:
            continue

        if packet_id == 6:

            game_state.update_telemetry(data)

            memory.add(game_state)

            engineer.analyze(game_state)


def main():

    print("🏎️ Project F1 Started")

    app = QApplication(sys.argv)

    overlay = Overlay()

    overlay.show()

    game_state = GameState()

    engineer = RaceEngineer()

    memory = TelemetryMemory()

    telemetry_thread = threading.Thread(
        target=telemetry_loop,
        args=(game_state, engineer, memory),
        daemon=True
    )

    radio = threading.Thread(
        target=radio_loop,
        args=(game_state,),
        daemon=True
    )

    telemetry_thread.start()
    radio.start()

    timer = QTimer()

    timer.timeout.connect(
        lambda: overlay.update_data(game_state)
    )

    timer.start(30)

    sys.exit(app.exec())


if __name__ == "__main__":
    main()