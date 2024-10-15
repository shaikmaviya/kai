import random
from fuzzywuzzy import fuzz

# Define possible triggers related to various topics
key_phrases = {
    "favorite color": [
        "I think I’d like blue—it’s calming and reminds me of the sky.",
        "Maybe green, like the color of growth and nature.",
        "Red is vibrant and full of energy—could be a favorite!",
        "Purple has a certain mystery to it, don’t you think?",
        "I might go for yellow—bright and cheerful!"
    ],
    "joke": [
        "Why don't scientists trust atoms? Because they make up everything!",
        "I told my computer I needed a break, and now it won't stop sending me to the beach!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!"
    ],
    "how are you": [
        "I'm just a program, but I'm functioning as expected! How about you?",
        "Doing well, thanks for asking! What can I assist you with today?",
        "I'm here and ready to help! What do you need?"
    ],
    "hello": [
        "Hello! How can I assist you today?",
        "Hi there! What do you need help with?",
        "Greetings! I'm here to help you.",
        "Hello! It's great to see you!",
        "Hey! What can I do for you?"
    ],
    "hi": [
        "Hi! How can I assist you today?",
        "Hello! What do you want to talk about?",
        "Hey there! I'm here to help!",
        "Hi! What can I do for you?",
        "Hello! How's your day going?"
    ],
    "tell me the color you like": [
        "I think I’d like blue—it’s calming and reminds me of the sky.",
        "Maybe green, like the color of growth and nature.",
        "Red is vibrant and full of energy—could be a favorite!",
        "Purple has a certain mystery to it, don’t you think?",
        "I might go for yellow—bright and cheerful!"
    ],
    "your name": [
        "I’m called NOVA, your virtual assistant!",
        "You can call me NOVA!",
        "I go by NOVA. What's your name?",
        "I'm NOVA, at your service!",
        "You can refer to me as NOVA!"
    ],
    # Add more key phrases and responses as needed
}

def communicate(user_input):
    user_input = user_input.lower()

    # Check for direct matches with predefined key phrases
    for phrase, responses in key_phrases.items():
        if fuzz.partial_ratio(user_input, phrase) > 70:  # Match threshold
            return random.choice(responses)

    # Default response if no match is found
    return "I'm not sure what you mean. Could you rephrase your question?"

