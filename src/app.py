from flask import Flask, render_template, jsonify, request
import os
import webbrowser
from threading import Timer
from assistant import Assistant  # Import your Assistant class
app = Flask(__name__)

# Initialize the Assistant
assistant = Assistant()

# Flag to ensure browser opens only once
browser_opened = False

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/api/handle_commands', methods=['POST'])
def handle_commands():
    data = request.get_json()
    commands = data.get('commands', [])  # Expect a list of commands

    # Process the commands
    responses = assistant.process_commands(commands)  # Call the process_commands function

    return jsonify({'responses': responses})  # Return a JSON response


def open_browser():
    global browser_opened
    if not browser_opened:
        webbrowser.open_new_tab("http://127.0.0.1:5000")
        browser_opened = True

def UI():
    Timer(0, open_browser).start()  # Delay opening the browser for 1 second
    app.run(host='0.0.0.0', port=5000, debug=False)

if __name__ == "__main__":
    UI()
