# 💬 Chat Simulator

A simple **command-line chatbot** built in Python using if-else logic, functions, and basic data structures. The bot responds to greetings, answers basic questions, and maintains conversation history.

## 🎯 What This Project Does

This chatbot can:
- **Greet users** with friendly responses
- **Answer basic questions** about its name, current time, and date
- **Respond intelligently** based on keywords in user input
- **Maintain conversation history** during the chat session
- **Save conversations** to a text file for later reference
- **Handle exit commands** gracefully with farewell messages

## 🚀 How to Run

1. **Ensure you have Python 3 installed** on your system
2. **Navigate to the project directory**:
   ```bash
   cd week1_projects/copilot/chat_simulator/
   ```
3. **Run the chat simulator**:
   ```bash
   python chat_simulator.py
   ```
   or
   ```bash
   python3 chat_simulator.py
   ```

## 📋 Features

### Core Functionality
- **Interactive CLI interface** with user-friendly prompts
- **Keyword-based responses** using if-else logic
- **Random response selection** for variety in conversations
- **Conversation history tracking** in real-time
- **File export** functionality for conversation logs

### Supported Commands & Responses
- **Greetings**: hello, hi, hey, good morning, etc.
- **Name queries**: "What's your name?"
- **Time queries**: "What time is it?"
- **Date queries**: "What's today's date?"
- **Help command**: Type "help" for available options
- **Exit commands**: bye, goodbye, exit, quit, stop, end
- **Special commands**:
  - `history` - View conversation history
  - `save` - Save conversation to file

## 💻 Example Input/Output

```
==================================================
🤖 Welcome to Chat Simulator! 🤖
==================================================
Hi! I'm ChatBot, your friendly chatbot!
Type 'help' for available commands
Type 'bye', 'exit', or 'quit' to end our chat
Type 'history' to see our conversation
Type 'save' to save our conversation to a file
--------------------------------------------------

You: hello
ChatBot: Hello! Nice to meet you!

You: what's your name?
ChatBot: My name is ChatBot! What's your name?

You: what time is it?
ChatBot: The current time is 02:30 PM

You: how are you?
ChatBot: I'm doing great, thank you for asking! How are you?

You: help
ChatBot: I can help you with:
- Greetings (hello, hi, hey)
- Telling you the current time
- Telling you today's date
- Sharing my name
- General conversation
- To exit, just say 'bye', 'exit', or 'quit'

You: bye
ChatBot: Goodbye! Have a great day!

Thank you for chatting! 👋
Would you like to save our conversation? (yes/no): yes
Conversation saved to chat_history_20240121_143045.txt
```

## 🛠️ Skills Demonstrated

This project showcases:
- **Python syntax** and best practices
- **Variables and strings** manipulation
- **Conditional statements** (if-elif-else chains)
- **Loops** (while loop for main chat interface)
- **Functions** for organized, reusable code
- **File handling** for conversation export
- **Lists** for conversation history storage
- **CLI user experience** design
- **Error handling** for robust operation

## 📁 File Structure

```
chat_simulator/
├── chat_simulator.py      # Main chatbot script
├── README.md             # This documentation
└── chat_history_*.txt    # Generated conversation logs (optional)
```

## 🔧 Code Structure

The code is organized into clear functions:
- `get_bot_name()` - Returns chatbot name
- `get_current_time()` - Gets formatted current time
- `get_current_date()` - Gets formatted current date
- `get_greeting_response()` - Random greeting selection
- `get_farewell_response()` - Random farewell selection
- `process_user_input()` - Main logic for keyword matching
- `save_conversation_to_file()` - Exports chat history
- `display_conversation_history()` - Shows chat log
- `main()` - Main program loop

## 🎓 What I Learned

- How to build interactive command-line applications
- Implementing keyword-based response systems
- Managing program state with lists and variables
- File I/O operations for data persistence
- User experience design for CLI applications
- Code organization with functions
- Error handling and edge cases

## 🚀 Future Enhancements

Possible improvements:
- Add more sophisticated natural language processing
- Implement conversation context awareness
- Add user profiles and personalization
- Include more topic-specific responses
- Add conversation analytics
- Implement chat themes or personalities

---

**Author**: Copilot (GitHub Copilot Assistant)  
**Project Type**: Beginner Python CLI Application  
**Skills**: Python, CLI Development, File I/O, User Experience