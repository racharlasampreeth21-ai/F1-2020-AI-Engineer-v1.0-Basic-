from groq import Groq
from config import GROQ_API_KEY
from voice import speak

client = Groq(api_key=GROQ_API_KEY)


def answer(question, game_state):

    telemetry = f"""
Current Telemetry

Speed: {game_state.speed} km/h
Gear: {game_state.gear}
RPM: {game_state.rpm}
Throttle: {int(game_state.throttle*100)}%
Brake: {int(game_state.brake*100)}%
DRS: {"Enabled" if game_state.drs else "Disabled"}
"""

    system_prompt = """
You are Ezio.

You are a professional Formula 1 race engineer.

Rules:
- Keep responses under 20 words.
- Be calm.
- Be concise.
- Never mention that you're an AI.
- Answer only using the telemetry provided.
- If information is unavailable, say so briefly.
"""

    completion = client.chat.completions.create(

        model="llama-3.3-70b-versatile",

        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content":
                telemetry +
                "\n\nDriver Question:\n" +
                question
            }
        ],

        temperature=0.3,
        max_tokens=80
    )

    reply = completion.choices[0].message.content

    print(f"\n🎧 Ezio: {reply}")

    speak(reply)