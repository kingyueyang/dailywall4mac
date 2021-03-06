from appscript import app, mactypes
import os
import time
import subprocess
# for single monitor
SCRIPT = """/usr/bin/osascript<<END
tell application "Finder"
set desktop picture to POSIX file "%s"
end tell
END"""

SCRIPT_MULTI = """/usr/bin/osascript<<END
tell application "System Events"
    set desktopCount to count of desktops
    repeat with desktopNumber from 1 to desktopCount
        tell desktop desktopNumber
            set picture to "%s"
        end tell
    end repeat
end tell
END
"""

def set_desktop_background(filename):
    subprocess.call(SCRIPT_MULTI % filename, shell=True)

wallpaper_dir = "%s/Pictures/bing-wallpapers"%os.getenv("HOME")
to_set_picture = ""
for f in os.listdir(wallpaper_dir):
    if f.endswith(".jpg"):
        full_file_path = '/'.join([wallpaper_dir, f])
        file_ctime = os.path.getctime(full_file_path)
        if (time.time() - file_ctime) < 3600 * 24:
            to_set_picture = full_file_path
if to_set_picture:
    set_desktop_background(to_set_picture)
