import os
import platform
import shutil

def open_software(software_name):
    """
    Opens a software on your computer based on the provided software name.
    If the software is not present, it suggests installing the app.
    """
    software_name = software_name.strip().lower()

    # Command dictionary for common apps (Windows example)
    common_apps = {
        "cmd": "start cmd", "powershell": "start powershell", "whatsapp": "start whatsapp:",
        "photos": "start ms-photos:", "calculator": "start calculator:", "camera": "start microsoft.windows.camera:",
        "notepad": "start notepad", "settings": "start ms-settings:", "mail": "start outlookmail:",
        "maps": "start bingmaps:", "edge": "start microsoft-edge:", "store": "start ms-windows-store:",
        "skype": "start skype:", "spotify": "start spotify:", "explorer": "start explorer",
        "task manager": "start taskmgr", "vlc": "start vlc", "control panel": "start control",
        "word": "start winword", "excel": "start excel", "powerpoint": "start powerpnt",
        "onenote": "start onenote", "teams": "start teams", "zoom": "start zoom",
        "discord": "start discord", "firefox": "start firefox", "chrome": "start chrome",
        "mspaint": "start mspaint", "wordpad": "start wordpad", "snipping tool": "start SnippingTool",
        "adobe reader": "start AcroRd32", "photoshop": "start photoshop", "illustrator": "start illustrator",
        "premiere pro": "start premiere", "after effects": "start afterfx", "audacity": "start audacity",
        "steam": "start steam", "blender": "start blender", "pycharm": "start pycharm",
        "visual studio": "start devenv", "vscode": "start code", "obs": "start obs",
        "git bash": "start git-bash", "docker": "start docker", "postman": "start postman",
        "filezilla": "start filezilla", "notepad++": "start notepad++", "jupyter notebook": "start jupyter-notebook",
        "xamp": "start xampp-control", "vmware": "start vmware", "virtualbox": "start virtualbox",
        "winrar": "start winrar", "7zip": "start 7zFM", "itunes": "start itunes",
        "dropbox": "start dropbox", "onedrive": "start onedrive", "google drive": "start googledrive",
        "trello": "start trello", "notion": "start notion", "evernote": "start evernote",
        "sketchup": "start sketchup", "lightroom": "start lightroom", "davinci resolve": "start resolve",
        "kodi": "start kodi", "microsoft whiteboard": "start ms-whiteboard", "cyberduck": "start cyberduck",
        "matlab": "start matlab", "anaconda": "start anaconda", "r studio": "start rstudio",
        "putty": "start putty", "bitbucket": "start bitbucket", "teamviewer": "start teamviewer",
        "remote desktop": "start mstsc", "qbittorrent": "start qbittorrent", "cisco anyconnect": "start vpnui",
        "hangouts": "start hangouts", "webex": "start webex", "gotomeeting": "start gotomeeting",
        "bluejeans": "start bluejeans", "twitch": "start twitch", "epic games launcher": "start epicgameslauncher",
        "origin": "start origin", "uplay": "start uplay", "battlenet": "start battlenet",
        "nvidia control panel": "start nvcplui", "amd radeon software": "start amd-radeon-software",
        "logitech g hub": "start lghub", "asus armory crate": "start armorycrate",
        "razer synapse": "start razer-synapse", "wamp": "start wampmanager", "solidworks": "start solidworks",
        "autocad": "start autocad", "revit": "start revit", "fusion 360": "start fusion360",
        "mindmanager": "start mindmanager", "stata": "start stata", "sas": "start sas"
    }

    # Check if the application is installed
    def check_software_installed(software):
        return shutil.which(software) is not None

    # Platform-specific handling
    if platform.system() == "Windows":
        command = common_apps.get(software_name, f"start {software_name}")
        if check_software_installed(software_name) or software_name in common_apps:
            os.system(command)
            return f"Opened {software_name.capitalize()} successfully!"
        else:
            return f"'{software_name}' is not installed. Please install the application."

    elif platform.system() == "Darwin":  # macOS
        if check_software_installed(software_name):
            os.system(f"open -a {software_name}.app")
            return f"Opened {software_name.capitalize()} successfully!"
        else:
            return f"'{software_name}' is not installed. Please install the application."

    elif platform.system() == "Linux":  # Linux
        if check_software_installed(software_name):
            os.system(f"{software_name} &")
            return f"Opened {software_name.capitalize()} successfully!"
        else:
            return f"'{software_name}' is not installed. Please install the application."

    else:
        return "Unsupported operating system."
