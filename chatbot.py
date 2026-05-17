print(" DecodeBot Activated!")
print("Type 'bye' to exit.\n")

while True:
    user_input = input("You: ").lower().strip()

    if user_input in ["hi", "hello", "hey"]:
        print("Bot: Hello! Nice to meet you.")

    elif user_input == "how are you":
        print("Bot: I am working perfectly.")

    elif user_input == "what is your name":
        print("Bot: My name is DecodeBot.")

    elif user_input == "what is ai":
        print("Bot: AI stands for Artificial Intelligence.")

    elif user_input == "who created you":
        print("Bot: I was created by Teja during DecodeLabs internship.")

    elif user_input == "bye":
        print("Bot: Goodbye. Have a great day!")
        break
    else:
        print("Bot: Sorry, I don't understand that yet.")