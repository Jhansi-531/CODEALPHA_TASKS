# CodeAlpha Task 1: Basic Chatbot
# Domain: Python Programming

def chatbot():
    print("🤖 Basic Chatbot")
    print("Type 'bye' to end the conversation.\n")

    while True:
        user_input = input("You: ").lower().strip()

        if user_input == "hello":
            print("Bot: Hi! How can I help you today?")

        elif user_input == "hi":
            print("Bot: Hello! Nice to meet you.")

        elif user_input == "how are you":
            print("Bot: I'm fine, thanks! How are you?")

        elif user_input == "what is your name":
            print("Bot: I am a simple Python chatbot.")

        elif user_input == "who created you":
            print("Bot: I was created by Jhansi using Python!")

        elif user_input == "thank you":
            print("Bot: You're welcome! Happy to help.")

        elif user_input == "bye":
            print("Bot: Goodbye! Have a great day!")
            break

        else:
            print("Bot: Sorry, I don't understand that. Please try another question.")

# Run the chatbot
chatbot()