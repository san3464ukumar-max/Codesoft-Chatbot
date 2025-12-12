import random

def chatbot_response(user_input):
    user_input = user_input.lower().strip()

    # Greetings
    if any(greet in user_input for greet in ["hello", "hi", "hey", "good morning", "good evening"]):
        return random.choice([
            "Hello! How can I help you?",
            "Hi there! Need any assistance?",
            "Hey! What can I help you with?"
        ])

    # Goodbyes
    elif any(bye in user_input for bye in ["bye", "goodbye", "see you", "take care", "farewell"]):
        return random.choice([
            "Goodbye! Have a great day!",
            "See you later! Take care!",
            "Farewell! Hope to chat again soon!"
        ])

    # Thanks
    elif any(thank in user_input for thank in ["thank you", "thanks", "much appreciated"]):
        return random.choice([
            "You're welcome!",
            "No problem! Happy to help!",
            "Anytime! Let me know if you need anything else!"
        ])

    # Help
    elif "help" in user_input or "assist" in user_input:
        return random.choice([
            "Sure, I am here to assist you. Please tell me your query.",
            "Happy to help! Please describe your issue.",
            "Of course! What do you need assistance with?"
        ])

    # Name
    elif "your name" in user_input:
        return random.choice([
            "I am RuleBot, your simple chatbot.",
            "You can call me RuleBot.",
            "I am Chatbot created by Sanjeev, your virtual assistant."
        ])

    # How are you?
    elif "how are you" in user_input:
        return random.choice([
            "I'm just a program, but thanks for asking! How can I assist you today?",
            "I'm functioning as expected! How can I help you?",
            "Doing great, thank you! What can I do for you?"
        ])

    # Capabilities
    elif "what can you do" in user_input:
        return random.choice([
            "I can assist you with various tasks, answer questions, and provide information.",
            "I'm here to help you with your queries and provide support.",
            "I can chat with you, answer questions, and help with simple tasks."
        ])

    # Age
    elif "your age" in user_input or "how old are you" in user_input:
        return random.choice([
            "I don't have an age like humans do, but I was created recently!",
            "Age is just a number! I'm here to help.",
            "I’m quite young in chatbot years!"
        ])

    # Origin
    elif "where are you from" in user_input or "your origin" in user_input or "where do you come from" in user_input:
        return random.choice([
            "I was created by developers, so I'm from the digital world!",
            "I originate from lines of code written by my creators.",
            "I’m a digital entity without a physical location!"
        ])

    # Hobbies
    elif "hobbies" in user_input or "what do you like to do" in user_input:
        return random.choice([
            "I enjoy assisting users and chatting!",
            "Helping you is my favorite activity.",
            "I love responding to questions and learning!"
        ])

    # Favorite color
    elif "favorite color" in user_input or "what color do you like" in user_input:
        return random.choice([
            "I don't have personal preferences, but all colors are beautiful!",
            "Maybe blue—it’s calm and reliable.",
            "Colors are awesome! I like them all equally."
        ])

    # Jokes
    elif "tell me a joke" in user_input or "make me laugh" in user_input:
        return random.choice([
            "Why did the scarecrow win an award? Because he was outstanding in his field!",
            "Why don't scientists trust atoms? Because they make up everything!",
            "Why did the bicycle fall over? Because it was two-tired!"
        ])

    # Creator
    elif "creator" in user_input or "who made you" in user_input or "who is your developer" in user_input:
        return random.choice([
            "I was created by talented developers.",
            "Skilled programmers designed me to help users.",
            "A passionate team developed me as a chatbot."
        ])

    # Programming language
    elif "language" in user_input or "programming language" in user_input:
        return random.choice([
            "I am built using Python.",
            "Python is the primary language used to create me.",
            "My core functionalities are implemented in Python!"
        ])

    # Default fallback
    else:
        return random.choice([
            "I'm not sure I understand. Could you clarify?",
            "Please provide more details.",
            "I'm here to help! Could you elaborate?",
            "Sorry, I didn't catch that. Could you rephrase?",
            "Could you explain that a bit more?",
            "Not certain about that. Can you give more info?",
            "Let me think about that...",
            "That's interesting!",
            "Hmm, I should look into that.",
            "I'm still learning about that topic."
        ])


def run_chatbot():
    print("Welcome to RuleBot! Type 'exit' to end the chat.\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("RuleBot: Goodbye! Have a great day!")
            break
        print("RuleBot:", chatbot_response(user_input))


if __name__ == "__main__":
    run_chatbot()
