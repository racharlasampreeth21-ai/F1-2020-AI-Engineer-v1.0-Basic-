from radio import listen
from brain import answer


def radio_loop(game_state):

    print("🎙️ Radio Ready")

    while True:

        question = listen()

        if question != "":

            answer(question, game_state)