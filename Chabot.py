import random
import nltk
from nltk.chat.util import Chat, reflections

# Define patterns for the chatbot to recognize and respond to
patterns = [
    (r'hi|hello|hey', ['Hello!', 'Hi there!', 'Hey!']),
    (r'how are you?', ["I'm doing well, thank you!", "I'm good, thanks for asking!"]),
    (r'what is your name?', ["You can call me Idiot.", "My name is Idiot."]),
    (r'(.*)(introduce yourself|tell about yourself|who are you?)', ["Hello my name is Idiot. I am a simple chatbot which can do a lot if trained."]),
    (r'(.*)(Bye|quit)', ['Bye, take care!', 'Goodbye, have a great day!']),
    (r'(.*) stock', ['I am not capable to answer questions about stocks yet']),
    (r'(.*) (weather|temperature)', ['I am not capable to provide weather information yet']),
    (r'(.*) (joke|jokes)', ['Why couldn\'t the bicycle stand up by itself? Because it was two-tired!', 'I told my wife she was drawing her eyebrows too high. She looked surprised.', 'Why don’t skeletons fight each other? They don’t have the guts.']),
    (r'(.*) (movie|film)', ['I am not capable to provide movie recommendations yet']),
    (r'(.*) (time|date)', ['I am not capable to provide current time or date yet']),
    (r'(.*) (age|old)', ['I am a computer program, I do not have an age.']),
    (r'.*', ["I'm sorry, I don't understand."])
]

# Create a Chatbot instance
chatbot = Chat(patterns, reflections)

def main():
    print("Welcome to the Chatbot!")
    print("Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        response = chatbot.respond(user_input)
        print("Chatbot:", response)
        if user_input.lower() == 'quit':
            break

if __name__ == "__main__":
    main()
