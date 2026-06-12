# Simple Rule-Based Chatbot

print("ChatBot: Hello! Type 'exit' to end the chat.")

while True:
    user_input = input("You: ").lower()

    # Exit command
    if user_input == "exit":
        print("ChatBot: Goodbye! Have a nice day!")
        break

    # Greetings
    elif user_input in ["hello", "hi", "hey"]:
        print("ChatBot: Hello! How can I help you?")

    # Asking chatbot's name
    elif user_input == "what is your name":
        print("ChatBot: I am a simple rule-based chatbot.")

    # Asking about well-being
    elif user_input == "how are you":
        print("ChatBot: I am fine. Thank you for asking!")

    # Help command
    elif user_input == "help":
        print("ChatBot: You can greet me, ask my name, ask how I am, or type 'exit' to quit.")

    # Default response
    else:
        print("ChatBot: Sorry, I don't understand that.")