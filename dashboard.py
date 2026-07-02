import os


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def display(game_state):

    clear()

    print("=" * 45)
    print("🏎️         PROJECT F1")
    print("=" * 45)

    print(f"Speed      : {game_state.speed} km/h")
    print(f"Throttle   : {game_state.throttle:.2f}")
    print(f"Steer      : {game_state.steer:.2f}")
    print(f"Brake      : {game_state.brake:.2f}")
    print(f"Clutch     : {game_state.clutch}")
    print(f"Gear       : {game_state.gear}")
    print(f"RPM        : {game_state.rpm}")
    print(f"DRS        : {game_state.drs}")
    print(f"Rev Lights : {game_state.rev_lights}")

    print("=" * 45)