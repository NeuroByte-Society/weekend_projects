import datetime

def greet_user():
    print("Hello! I am ChatSim, your friendly chatbot.")
    print("You can ask me basic questions or type 'bye' or 'exit' to quit.")

def get_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hi there! How can I help you today?"
    elif "your name" in user_input:
        return "I am ChatSim, your command-line chatbot."
    elif "time" in user_input:
        now = datetime.datetime.now().strftime("%H:%M:%S")
        return f"The current time is {now}."
    elif "date" in user_input:
        today = datetime.datetime.now().strftime("%Y-%m-%d")
        return f"Today's date is {today}."
    elif user_input in ["bye", "exit", "quit"]:
        return "exit"
    else:
        return "Sorry, I didn't understand that. Can you ask something else?"

def main():
    greet_user()
    conversation_history = []

    while True:
        user_input = input("You: ")
        conversation_history.append(f"You: {user_input}")

        response = get_response(user_input)
        if response == "exit":
            print("ChatSim: Goodbye! Have a great day!")
            break
        else:
            print(f"ChatSim: {response}")
            conversation_history.append(f"ChatSim: {response}")

    # Optional: Save conversation history to a text file
    with open("chat_history.txt", "w") as f:
        for line in conversation_history:
            f.write(line + "\n")

if __name__ == "__main__":
    main()
