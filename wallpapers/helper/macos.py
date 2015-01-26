#!/usr/bin/env python

"""
Interaction with Mac os.
Sets random wallpapers on all monitors.
Random might return the same wallpaper :)
Requires appscript (sudo easy_install appscript)
Code thanks to Glen from stackoverflow
Current options: set the wallpaper.
Works wih >10.9 
"""

from appscript import *
import glob
import random
 
from AppKit import NSWorkspace, NSScreen
from Foundation import NSURL

def set_wallpaper_image(imgs, mode='stretched'):
    """Set the given file as wallpaper."""
    if not len(imgs):
        return

    default_image = imgs[0]
    file_url = NSURL.fileURLWithPath_(default_image)
    options = {}
    ws = NSWorkspace.sharedWorkspace()
    for screen in NSScreen.screens():
      (result, error) = ws.setDesktopImageURL_forScreen_options_error_(file_url, screen, options, None)
    
def get_no_of_monitors():
    return len(app('System Events').desktops.display_name.get())
