import os
import subprocess

# Function to open a folder directly
def open_folder(folder_name, drive):
    folder_path = os.path.join(drive, folder_name)  # Construct the full path
    print(f"Attempting to open folder at: {folder_path}")  # Debugging line
    if os.path.isdir(folder_path):
        subprocess.call(('start', folder_path), shell=True)  # Open the folder in Explorer
        print(f"Opened folder: {folder_path}")
    else:
        # If the exact path doesn't exist, attempt to find it case-insensitively
        found = False
        try:
            items = os.listdir(drive)
            for item in items:
                if item.lower() == folder_name.lower():  # Case-insensitive comparison
                    folder_path = os.path.join(drive, item)
                    subprocess.call(('start', folder_path), shell=True)
                    print(f"Opened folder: {folder_path}")
                    found = True
                    break
        except Exception as e:
            print(f"Error accessing items in {drive}: {e}")
        
        if not found:
            print(f"Folder does not exist: {folder_path}")

# Function to open a file or folder based on name case
def search_and_open(drive='F:'):
    # List all folders and files in the specified drive
    try:
        items = os.listdir(drive)
    except FileNotFoundError:
        print(f"Drive {drive} not found.")
        return
    except Exception as e:
        print(f"Error listing items in {drive}: {e}")
        return
    
    # Check if any item contains a lowercase letter
    found_lowercase = False
    for item in items:
        if any(c.islower() for c in item):  # Check for any lowercase letters
            found_lowercase = True
            item_path = os.path.join(drive, item)
            print(f"Opening: {item_path}")
            subprocess.run(['explorer', item_path])  # Open the item in Explorer
            return  # Exit after opening the first match

    # If no lowercase items were found, search for uppercase names
    if not found_lowercase:
        for item in items:
            if item.isupper():  # Check if the item is all uppercase
                item_path = os.path.join(drive, item)
                print(f"Opening uppercase item: {item_path}")
                subprocess.run(['explorer', item_path])  # Open the item in Explorer
                return  # Exit after opening the first uppercase match

# Function to open all folders in a specified drive
def open_all_folders(drive):
    print(f"Attempting to open all folders in: {drive}")
    try:
        # List all folders in the specified drive
        folders = [d for d in os.listdir(drive) if os.path.isdir(os.path.join(drive, d))]
        if folders:
            for folder in folders:
                folder_path = os.path.join(drive, folder)
                subprocess.call(('start', folder_path), shell=True)  # Open each folder
                print(f"Opened folder: {folder_path}")
        else:
            print(f"No folders found in {drive}.")
    except Exception as e:
        print(f"Error opening folders: {e}")

# Function to analyze and extract folder name and drive from the command
def extract_details(command):
    command = command.lower().strip()

    # Check if the command mentions a specific drive
    if "in" in command and "disk" in command:
        parts = command.split("in")  # Split the command to isolate the drive part
        folder_part = parts[0].replace("open", "").strip()  # Get folder part
        drive_part = parts[1].replace("disk", "").strip()  # Get drive part

        if "all" in folder_part:
            return None, f"{drive_part.upper()}:/"  # No folder specified, open all

        # Extract the folder name (removing "folder" if present)
        folder_name = folder_part.replace("folder", "").strip()  # Don't capitalize yet
        
        # Construct the drive path (add colon and slash)
        drive_name = f"{drive_part.upper()}:/"
        return folder_name, drive_name

    else:
        folder_part = command.replace("open", "").strip()  # Default case if no drive specified
        folder_name = folder_part.replace("folder", "").strip()  # Don't capitalize yet
        default_drive = "F:/"  # Default drive when not specified
        return folder_name, default_drive  # Return the folder name and the default drive

# Function to handle commands
def command_handler(command):
    if command.startswith("open "):
        folder_name, drive_name = extract_details(command)  # Extract folder and drive
        if folder_name is None:  # Check if the user wants to open all folders
            open_all_folders(drive_name)  # Open all folders
        elif folder_name and drive_name:
            open_folder(folder_name, drive_name)  # Open the specific folder
        else:
            print("Could not extract folder or drive details.")
    elif command.startswith("search and open "):
        # Extract drive if specified or use default
        parts = command.split("in")
        drive = parts[1].replace("disk", "").strip() if len(parts) > 1 else 'F:'
        search_and_open(drive)  # Call the search and open function
    else:
        print("Command not recognized.")
