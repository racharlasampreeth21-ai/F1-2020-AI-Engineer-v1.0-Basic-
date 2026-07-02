import pyttsx3

VOICE_RATE = 185


def speak(text):

    engine = pyttsx3.init()

    voices = engine.getProperty("voices")

    # Female voice
    engine.setProperty("voice", voices[1].id)

    engine.setProperty("rate", VOICE_RATE)

    engine.say(text)

    engine.runAndWait()

    engine.stop()