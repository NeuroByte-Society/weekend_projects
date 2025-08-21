#!/usr/bin/env python3
"""
Chat Simulator - A Simple Command-Line Chatbot
Built using if-else logic, functions, and basic data structures
"""

import datetime
import random


def get_bot_name():
    """Return the chatbot's name"""
    return "ChatBot"


def get_current_time():
    """Return current time in a readable format"""
    return datetime.datetime.now().strftime("%I:%M %p")


def get_current_date():
    """Return current date in a readable format"""
    return datetime.datetime.now().strftime("%B %d, %Y")


def get_greeting_response():
    """Return a random greeting response"""
    greetings = [
        "Hello! Nice to meet you!",
        "Hi there! How are you doing?",
        "Hey! Good to see you!",
        "Greetings! How can I help you today?",
        "Hi! Welcome to our chat!"
    ]
    return random.choice(greetings)


def get_farewell_response():
    """Return a random farewell response"""
    farewells = [
        "Goodbye! Have a great day!",
        "See you later! Take care!",
        "Bye! It was nice chatting with you!",
        "Take care! Come back anytime!",
        "Farewell! Have a wonderful day!"
    ]
    return random.choice(farewells)


def get_default_response():
    """Return a default response when no specific match is found"""
    defaults = [
        "That's interesting! Tell me more.",
        "I see. Can you elaborate on that?",
        "Hmm, I'm not sure about that. Can you ask something else?",
        "That's a good point! What else would you like to know?",
        "I'd love to learn more about that topic!"
    ]
    return random.choice(defaults)


def process_user_input(user_input, conversation_history):
    """
    Process user input and return appropriate response
    """
    # Convert to lowercase for easier matching
    user_input_lower = user_input.lower().strip()
    
    # Check for exit keywords
    exit_keywords = ['bye', 'goodbye', 'exit', 'quit', 'stop', 'end']
    if any(keyword in user_input_lower for keyword in exit_keywords):
        return get_farewell_response(), True
    
    # Check for greeting keywords
    greeting_keywords = ['hello', 'hi', 'hey', 'greetings', 'good morning', 'good afternoon', 'good evening']
    if any(keyword in user_input_lower for keyword in greeting_keywords):
        return get_greeting_response(), False
    
    # Check for name-related questions
    if 'name' in user_input_lower and ('your' in user_input_lower or 'what' in user_input_lower):
        return f"My name is {get_bot_name()}! What's your name?", False
    
    # Check for time-related questions
    if 'time' in user_input_lower and ('what' in user_input_lower or 'current' in user_input_lower):
        return f"The current time is {get_current_time()}", False
    
    # Check for date-related questions
    if 'date' in user_input_lower and ('what' in user_input_lower or 'today' in user_input_lower):
        return f"Today's date is {get_current_date()}", False
    
    # Check for how are you questions
    if 'how are you' in user_input_lower or 'how do you do' in user_input_lower:
        return "I'm doing great, thank you for asking! How are you?", False
    
    # Check for weather questions (simple response since we don't have real weather data)
    if 'weather' in user_input_lower:
        return "I don't have access to real weather data, but I hope it's nice where you are!", False
    
    # Check for help requests
    if 'help' in user_input_lower:
        help_text = """
I can help you with:
- Greetings (hello, hi, hey)
- Telling you the current time
- Telling you today's date
- Sharing my name
- General conversation
- To exit, just say 'bye', 'exit', or 'quit'
        """
        return help_text.strip(), False
    
    # Check for thanks
    if 'thank' in user_input_lower or 'thanks' in user_input_lower:
        return "You're welcome! Happy to help!", False
    
    # Check for age questions
    if 'age' in user_input_lower and ('your' in user_input_lower or 'old' in user_input_lower):
        return "I'm a computer program, so I don't have an age in the traditional sense!", False
    
    # Default response for unmatched input
    return get_default_response(), False


def save_conversation_to_file(conversation_history):
    """Save conversation history to a text file"""
    filename = f"chat_history_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    try:
        with open(filename, 'w') as file:
            file.write("=== Chat Simulator Conversation History ===\n\n")
            for entry in conversation_history:
                file.write(f"{entry}\n")
        print(f"Conversation saved to {filename}")
    except Exception as e:
        print(f"Error saving conversation: {e}")


def display_conversation_history(conversation_history):
    """Display the conversation history"""
    print("\n=== Conversation History ===")
    if not conversation_history:
        print("No conversation history yet.")
    else:
        for entry in conversation_history:
            print(entry)
    print("=" * 30)


def main():
    """Main function to run the chat simulator"""
    print("=" * 50)
    print("🤖 Welcome to Chat Simulator! 🤖")
    print("=" * 50)
    print(f"Hi! I'm {get_bot_name()}, your friendly chatbot!")
    print("Type 'help' for available commands")
    print("Type 'bye', 'exit', or 'quit' to end our chat")
    print("Type 'history' to see our conversation")
    print("Type 'save' to save our conversation to a file")
    print("-" * 50)
    
    conversation_history = []
    
    while True:
        # Get user input
        user_input = input("\nYou: ").strip()
        
        # Skip empty inputs
        if not user_input:
            continue
        
        # Add user input to history
        conversation_history.append(f"You: {user_input}")
        
        # Special commands
        if user_input.lower() == 'history':
            display_conversation_history(conversation_history)
            continue
        
        if user_input.lower() == 'save':
            save_conversation_to_file(conversation_history)
            continue
        
        # Process the input and get response
        response, should_exit = process_user_input(user_input, conversation_history)
        
        # Add bot response to history
        conversation_history.append(f"{get_bot_name()}: {response}")
        
        # Display bot response
        print(f"{get_bot_name()}: {response}")
        
        # Check if we should exit
        if should_exit:
            print("\nThank you for chatting! 👋")
            
            # Ask if user wants to save conversation
            save_choice = input("Would you like to save our conversation? (yes/no): ").lower().strip()
            if save_choice in ['yes', 'y', 'yeah', 'yep']:
                save_conversation_to_file(conversation_history)
            
            break


if __name__ == "__main__":
    main()