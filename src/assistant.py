import pyttsx3
import threading
import queue
from websearch.open_web import openweb
from websearch.searchinweb import search_on_google
from application_control.open_software import open_software
from communication.normal_talk import communicate
from filemanagement.open_operation import command_handler
from weather_check.weather import process_command


class Assistant:
    def __init__(self):
        self.engine = pyttsx3.init()  # Initialize the TTS engine
        self.command_queue = queue.Queue()  # Queue to manage speech commands
        self.speech_thread = threading.Thread(target=self._process_speech_queue)
        self.speech_thread.daemon = True  # Ensures thread exits when main program exits
        self.speech_thread.start()
        self.default_speak()
        self.key_phrases = [
    "hello",
    "help",
    "your name",
    "how are you",
    "what can you do",
    "weather",
    "joke",
    "thank you",
    "bye",
    "what is your purpose",
    "tell me a fact",
    "what is your favorite hobby",
    "do you believe in aliens",
    "favorite animal",
    "tell me a riddle",
    "do you have friends",
    "favorite color",
    "do you sleep",
    "what's your favorite movie",
    "do you like music",
    "do you have a family",
    "favorite food",
    "are you a robot",
    "what do you think about humans",
    "do you have emotions",
    "tell me something inspiring",
    "do you get tired",
    "do you have a favorite place",
    "what do you do for fun",
    "can you dream",
    "do you have a goal",
    "do you know any poems",
    "do you have a favorite season",
    "are you real",
    "tell me a story",
    "what is the meaning of life",
    "can you dance",
    "do you like art",
    "do you know any jokes",
    "are you happy",
    "what's your age",
    "can you cook",
    "do you like books",
    "do you like games",
    "tell me a secret",
    "what do you think about time travel",
    "can you see the future",
    "do you have a birthday",
    "do you like nature",
    "do you like space",
    "can you learn",
    "are you always listening",
    "tell me a quote",
    "can you sing",
    "what's your favorite song",
    "do you believe in ghosts",
    "what's your favorite sport",
    "are you afraid of anything",
    "do you have a pet",
    "what makes you laugh",
    "can you keep a secret",
    "do you get bored",
    "can you speak other languages",
    "what is your biggest dream",
    "do you like puzzles",
    "do you know about AI",
    "are you creative",
    "can you solve math problems",
    "do you get lonely",
    "can you read my mind",
    "do you have a favorite memory",
    "what's your favorite drink",
    "can you write poetry",
    "what's your favorite flower",
    "do you like superheroes",
    "do you have any hobbies",
    "what's your favorite holiday",
    "can you do magic tricks",
    "do you know any fun facts",
    "can you make me laugh",
    "what's your favorite weather",
    "do you like robots",
    "can you write stories",
    "do you believe in love",
    "what's your favorite dessert",
    "do you like mysteries",
    "what's your favorite planet",
    "do you like to travel",
    "what do you think of the internet",
    "do you have a catchphrase",
    "can you play chess",
    "what do you think about the future",
    "do you like dancing"
]


    def speak(self, message):
        # Add the message to the speech queue
        self.command_queue.put(message)

    # Function to automatically speak the default message
    def default_speak(self):
        welcome_message = (
            "Hello! Maavi, your personal assistant. How can I help you today?"
        )
        self.speak(welcome_message)  # Automatically speak the welcome message

    def _process_speech_queue(self):
        while True:
            message = self.command_queue.get()  # Get the next message from the queue
            self.engine.say(message)  # Queue the message for speaking
            self.engine.runAndWait()  # Wait for the speaking to finish
            self.command_queue.task_done()

    def process_commands(self, commands):
        responses = []  # List to store responses for each command
        for command in commands:
            # Process each command
            if "bye" in command.lower():
                response = "Goodbye!"
                self.speak(response)
                responses.append(response)
                break
            elif "website" in command.lower():
                search_term = command.replace(
                    "website", ""
                ).strip()  # Extract search term
                response = openweb(search_term)
                self.speak(response)
                responses.append(response)
            elif "search" in command.lower():
                search_term = command.replace(
                    "search", ""
                ).strip()  # Extract search term
                response = search_on_google(search_term)
                self.speak(response)
                responses.append(response)
            elif "folder" in command.lower():
                command_handler(command)
                response = "Command executed."
                self.speak(response)
                responses.append(response)
            elif (
                "open" in command.lower()
            ):  # Extract the software name by removing "open" from the command
                software_name = command.replace("open", "").strip()
                response = open_software(software_name)
                responses.append(response)
            elif "weather" in command.lower():
                response = process_command(command)
            elif any(phrase in command.lower() for phrase in self.key_phrases):
                response = communicate(command)
                self.speak(response)
                responses.append(response)
        return responses
