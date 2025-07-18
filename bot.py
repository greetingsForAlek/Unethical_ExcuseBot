# bot.py

import random

# responses for when the bot has no excuses, e.g. misplaced file
no_excuses_responses = [
    "Oops! something has gone horribly wrong.",
    "Oh, I didn't see that coming.",
    "Well, this is awkward.",
    "I didn't expect that.",
    "Excuse me, where are my excuses?",
    "Lost my excuse manual.",
    "I seem to have misplaced my excuses.",
    "My apologies, I have no excuses for that.",
    "Oh, mighty developer, fix the error, lazy boi!!!",
    "Yikes! Did you read the instructions?"
]

# responses for when the user quits the chat
ghosting_messages = [
    "Finally. I was trying to ghost you politely.",
    "So long! I was hoping you'd ghost me first.",
    "Phew. I'm a bit akward ..",
    "Adios!",
    "Au revoir!",
    "Ciao!",
    "Sayonara!",
    "SO LONG, SUCKER!",
    "Farwell, my (not-so) dear friend.",
    "Goodbye, and good riddance!",
]

# the function that loads excuses from excuses.txt
def load_excuses(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            excuses = [line.strip() for line in f if line.strip()]
        return excuses
    except FileNotFoundError:
        no_excuse = random.choice(no_excuses_responses)
        print(f"🤖 ChatBot: {no_excuse}")
        return ["I'm excuse-less. Please forgive me."]

# the main function that runs the ridiculous chat    
def unethical_chat():
    excuses = load_excuses("excuses.txt")

    # just check for the case when excuses.txt is empty or not found
    if excuses == ["I'm excuse-less. Please forgive me."]:
        print("!🤖 ChatBot: 404: Excuses not found.")
        return
    else:
        print("🤖 ChatBot: Go on, ask me anything. I can answer it.")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit", "bye", "i hate you bye"]:
            ghosting = random.choice(ghosting_messages)
            print(f"🤖 ChatBot: {ghosting}")
            break
        response = random.choice(excuses)
        print(f"🤖 ChatBot: {response}")


if __name__ == "__main__":
    unethical_chat()

# By: greetingsForAlek