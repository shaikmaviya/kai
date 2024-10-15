import pywhatkit

def search_on_google(command):
    """Extract the search query and perform a Google search."""
    try:
        # Remove common words like "search for" to focus on the query
        command_words = command.lower().replace('search for', '').replace('search', '').strip()
        
        # Check if there is a search term
        if not command_words:
            return "Please provide a search term."

        # Perform the search
        pywhatkit.search(command_words)
        
        return f"Searching for '{command_words}' on Google..."
    except Exception as e:
        return f"An error occurred while searching: {str(e)}"
