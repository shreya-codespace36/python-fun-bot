# Savage Bot Game 😈🔥
# A fun terminal-based Python game with savage + witty replies
# Beginner-friendly & easy to extend

import random
import time

bot_name = "SavageBot"

savage_replies = [
    "Wow. That was… something. I expected better.",
    "I’d explain, but I left my crayons at home.",
    "Bold of you to say that with full confidence.",
    "Error 404: Logic not found.",
    "I’m not judging… okay yes I am.",
    "Interesting choice. Not a good one, but interesting.",
    "I’ve met smarter Wi‑Fi signals.",
    "That sounded better in your head, didn’t it?"
]

friendly_replies = [
    "Hmm okay okay, I see you 👀",
    "Not bad, human. Not bad at all.",
    "You’re improving… slowly 😌",
    "I approve. Rare moment.",
    "That actually made sense. Proud of you 🫶"
]

def typing_effect(text):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.03)
    print()


def intro():
    typing_effect(f"Hey there 😏 I’m {bot_name}.")
    typing_effect("I reply based on my mood — savage or friendly.")
    typing_effect("Type 'bye' anytime to escape me 👋")
    print("-" * 40)


def savage_bot():
    intro()
    while True:
        user_input = input("You: ").strip().lower()

        if user_input == "bye":
            typing_effect("Running away already? Typical. Byeee 😌")
            break

        mood = random.choice(["savage", "friendly"])
        time.sleep(0.5)

        if mood == "savage":
            reply = random.choice(savage_replies)
        else:
            reply = random.choice(friendly_replies)

        typing_effect(f"{bot_name}: {reply}")


if __name__ == "__main__":
    savage_bot()
