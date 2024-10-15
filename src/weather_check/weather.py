import requests

def weather_api(locationinput):
    # Set the URL for the API endpoint
    url = "https://weatherapi-com.p.rapidapi.com/current.json"
    querystring = {"q": locationinput}  # Location input

    # Headers with your API key (store your API key securely)
    headers = {
        'x-rapidapi-key': "fe610a974cmsh1c955e2a5cd3a77p1700c7jsnab0a32676fab",  # Replace with your actual API key
        'x-rapidapi-host': "weatherapi-com.p.rapidapi.com"
    }

    try:
        # Make a GET request to the API
        response = requests.get(url, headers=headers, params=querystring)
        response.raise_for_status()  # Raise an error for bad responses

        # Automatically parse JSON response
        weather_data = response.json()

        # Example: Print specific information
        location = weather_data.get('location', {})
        current = weather_data.get('current', {})

        if location and current:  # Check if location and current data exist
            output = (
                f"Location: {location.get('name', 'N/A')}, "
                f"{location.get('region', 'N/A')}, "
                f"{location.get('country', 'N/A')}. "
                f"Temperature: {current.get('temp_c', 'N/A')} degrees Celsius. "
                f"Condition: {current.get('condition', {}).get('text', 'N/A')}. "
                f"Wind: {current.get('wind_mph', 'N/A')} miles per hour. "
                f"Humidity: {current.get('humidity', 'N/A')} percent."
            )
            print(output)
        else:
            return "No weather data available for the given location."

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

def extract_location(command):
    unnecessary_words = [
        "weather", "show", "give", "tell", "about", "in", "the", "is", "at", 
        "for", "on", "please", "what", "where", "how", "let", "me", "you", "my", 
        "can", "and", "that", "to", "of", "from"
    ]
    command_lower = command.lower()
    words = command_lower.split()
    location_words = [word for word in words if word not in unnecessary_words]
    location = ' '.join(location_words).strip()
    return location.capitalize()  # Capitalize for better output

def process_command(command):
    print(f"Received command: {command}")  # Debugging line

    if "weather" in command.lower():  # Use lower() to handle case insensitivity
        input_command = command
        extracted_location = extract_location(input_command)
        print(f"Extracted Location: {extracted_location}")
        # Call the weather API with the extracted location
        weather_api(extracted_location)  # Call the weather API function
    else:
        print("This command is not related to weather.")
