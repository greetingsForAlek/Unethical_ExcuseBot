import random

def load_excuses(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            excuses = [line.strip() for line in f if line.strip()]
        return excuses
    except FileNotFoundError:
        print("🤖 ExcuseBot: Uh oh. Couldn't find my excuse manual.")
        return ["I'm excuse-less. Please forgive me."]
    
def unethical_chat():
    excuses = load_excuses("excuses.txt")
    print("🤖 ExcuseBot: Go on, ask me anything. I can answer it.")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit", "bye", "i hate you bye"]:
            print("🤖 ExcuseBot: Finally. I was trying to ghost you politely.")
            break
        response = random.choice(excuses)
        print(f"🤖 ExcuseBot: {response}")


if __name__ == "__main__":
    unethical_chat()