import nltk
from nltk.chat.util import Chat, reflections

# Define pairs for input and responses
pairs = [
    ['hi|hello', ['Hello!', 'Hi there!']],
    ['how are you?', ['I am doing well, how about you?']],
    ['what is your name?', ['I am a chatbot created to assist you.']],
    ['bye', ['Goodbye! Take care!']]
]

# Create a chatbot instance
chatbot = Chat(pairs, reflections)

# Start the conversation
def start_chat():
    print("Hi! I'm your chatbot. Type 'bye' to exit.")
    chatbot.converse()

# Run the chatbot
if __name__ == "__main__":  # Corrected this part
    start_chat()
