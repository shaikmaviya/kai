# Assistant identity settings
ASSISTANT_NAME = "Kai"
DEFAULT_GREETING = "Hello! How can I assist you today?"
EXIT_COMMANDS = ["exit", "quit", "bye", "shutdown"]
EXIT_MESSAGES = ["Goodbye!", "Have a great day!", "See you later!"]

# Default responses
UNKNOWN_COMMAND_RESPONSE = "I'm sorry, I didn't understand that."

# Logging and debugging
LOGGING_ENABLED = True
LOG_FILE_PATH = "logs/assistant.log"
DEBUG_MODE = False

# Custom command responses
CUSTOM_COMMANDS = {
    "how are you": "I'm just a bunch of code, but thanks for asking!",
    "who made you": "I was created by a team of developers."
}

# Timeouts and limits
TIMEOUT_DURATION = 30  # Seconds
MAX_RETRY_ATTEMPTS = 3

# API keys (use environment variables in production)
OPENAI_API_KEY = "your-openai-api-key"
WEATHER_API_KEY = "your-weather-api-key"

# Feature toggles
ENABLE_JOKES = True
ENABLE_WEATHER = True
MAX_CONVERSATION_LENGTH = 10
