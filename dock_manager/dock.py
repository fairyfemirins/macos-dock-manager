import subprocess
import json

def get_current_space():
    """Get the current macOS Space identifier."""
    script = '''
tell application "System Events"
    tell process "Dock"
        set activeSpace to do shell script "echo $SPACE_ID"
    end tell
end tell
'''
    result = subprocess.run(["osascript", "-e", script], capture_output=True, text=True)
    return result.stdout.strip()

def set_dock_apps(apps):
    """Set the dock apps for the current Space."""
    app_list = ", ".join([f"\"{app}\"" for app in apps])
    script = f'''
tell application "Dock"
    set dock preferences to {{autohide:true, magnification:true}}
    set the dock items to {{{app_list}}}
end tell
'''
    subprocess.run(["osascript", "-e", script])