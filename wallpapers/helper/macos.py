#!/usr/bin/env python

"""
Interaction with Mac os.
Sets random wallpapers on all monitors.
Random might return the same wallpaper :)
Requires appscript (sudo easy_install appscript)
Code thanks to Glen from stackoverflow
Current options: set the wallpaper.
"""

from appscript import *

def set_wallpaper_image(imgs, mode='stretched'):
    """Set the given file as wallpaper."""
    if not len(imgs):
        return

    default_image = imgs[0]

    se = app('System Events')
    desktops = se.desktops.display_name.get()
    for i, d in enumerate(desktops):
        desk = se.desktops[its.display_name == d]
        img = imgs[i] if len(imgs) > i else default_image
        #TODO: figure out how to resize image properly
        #looks like system events doesn't have this property
        desk.picture.set(mactypes.File(img))

def get_no_of_monitors():
    return len(app('System Events').desktops.display_name.get())
