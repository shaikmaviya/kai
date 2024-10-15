import webbrowser
from websearch.urls import websites

def openweb(webname):
    """Open specified websites based on the input name."""
    website_name = webname.lower().split()
    counts = {}
    
    # Count occurrences of each website name
    for name in website_name:
        counts[name] = counts.get(name, 0) + 1
    
    urls_to_open = []
    
    # Collect URLs based on the counts and the predefined websites
    for name, count in counts.items():
        if name in websites:
            urls_to_open.extend([websites[name]] * count)
    
    # Open the URLs
    if urls_to_open:
        for url in urls_to_open:
            webbrowser.open(url)
        return f"Opening: {', '.join(urls_to_open)}"
    else:
        return "No recognized websites found."
